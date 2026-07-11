#!/usr/bin/env python3
"""Capability-only PyTorch smoke test; never a grokking outcome run."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import time
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="cpu")
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260711)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def state_digest(model: Any) -> str:
    digest = hashlib.sha256()
    for name, tensor in sorted(model.state_dict().items()):
        digest.update(name.encode("utf-8"))
        digest.update(tensor.detach().cpu().contiguous().numpy().tobytes())
    return digest.hexdigest()


def select_device(torch: Any, requested: str) -> str:
    if requested == "auto":
        return "cuda" if torch.cuda.is_available() else "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("requested cuda/ROCm but torch reports no device")
    return requested


def run_once(torch: Any, device: str, seed: int, steps: int) -> dict[str, Any]:
    if steps < 2:
        raise ValueError("steps must be at least 2")
    torch.manual_seed(seed)
    if device == "cuda":
        torch.cuda.manual_seed_all(seed)
    torch.use_deterministic_algorithms(True)
    nn = torch.nn

    class TinyTransformer(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.embed = nn.Embedding(17, 32)
            layer = nn.TransformerEncoderLayer(
                d_model=32,
                nhead=4,
                dim_feedforward=64,
                dropout=0.0,
                activation="relu",
                batch_first=True,
            )
            self.encoder = nn.TransformerEncoder(layer, num_layers=1)
            self.readout = nn.Linear(32, 17)

        def forward(self, tokens: Any) -> Any:
            encoded = self.encoder(self.embed(tokens))
            return self.readout(encoded[:, 0, :])

    model = TinyTransformer().to(device)
    initial_digest = state_digest(model)
    generator = torch.Generator(device="cpu").manual_seed(seed + 1)
    cpu_tokens = torch.randint(0, 17, (64, 4), generator=generator)
    cpu_targets = (cpu_tokens[:, 0] + cpu_tokens[:, 1]) % 17
    tokens = cpu_tokens.to(device)
    targets = cpu_targets.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-2, weight_decay=1e-2)

    losses: list[float] = []
    started = time.perf_counter()
    for _ in range(steps):
        optimizer.zero_grad(set_to_none=True)
        loss = nn.functional.cross_entropy(model(tokens), targets)
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach().cpu()))
    elapsed = time.perf_counter() - started

    final_digest = state_digest(model)
    return {
        "losses": losses,
        "initial_state_sha256": initial_digest,
        "final_state_sha256": final_digest,
        "elapsed_seconds": elapsed,
        "finite": all(math.isfinite(value) for value in losses),
        "parameters_changed": initial_digest != final_digest,
        "loss_decreased": losses[-1] < losses[0],
    }


def main() -> int:
    args = parse_args()
    try:
        import torch
    except ImportError as exc:
        raise SystemExit("PyTorch required; install the train extra") from exc

    torch.set_num_threads(min(8, os.cpu_count() or 1))
    device = select_device(torch, args.device)
    first = run_once(torch, device, args.seed, args.steps)
    second = run_once(torch, device, args.seed, args.steps)
    replay_diff = max(abs(a - b) for a, b in zip(first["losses"], second["losses"]))
    passed = (
        first["finite"]
        and first["parameters_changed"]
        and first["loss_decreased"]
        and first["initial_state_sha256"] == second["initial_state_sha256"]
        and first["final_state_sha256"] == second["final_state_sha256"]
        and replay_diff == 0.0
    )
    report = {
        "kind": "hardware_capability_smoke_not_scientific_outcome",
        "passed": passed,
        "device": device,
        "seed": args.seed,
        "steps": args.steps,
        "platform": {
            "python": platform.python_version(),
            "system": platform.platform(),
            "cpu_count": os.cpu_count(),
            "torch": torch.__version__,
            "torch_hip": getattr(torch.version, "hip", None),
            "torch_cuda_available": torch.cuda.is_available(),
            "device_name": torch.cuda.get_device_name(0) if device == "cuda" else None,
        },
        "first_run": first,
        "deterministic_replay_max_abs_loss_diff": replay_diff,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
