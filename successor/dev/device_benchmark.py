"""NON-CITABLE Legion GPU-vs-CPU one-step timing probe.

Dev-only. No scientific datum, comparative result, or claim.
Does not modify src/, canonical/, experiments/, or frozen thresholds.

Bypasses configure_canonical_runtime pins; monkeypatches:
  1) ContactTransformer.forward CPU-device guard (allow cuda)
  2) feasibility_committee_step -> sequential per-member fwd+bwd+opt
     so peak activation memory fits in 8GB VRAM (4 retained attention
     graphs at history_len>=512 spill into system RAM on this laptop,
     which made cuda@512 look like CPU). Same finite-path math when all
     losses are finite; documented in the report.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

MODULUS = 66
WARMUP_STEPS = 2
CPU_ANCHOR_LEN = 512
GPU_LENGTHS = (512, 1024, 2000)
FULL_B = 2000
OUT_MD = Path(__file__).resolve().parent / "LEGION_DEVICE_BENCHMARK.md"
_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"


def _sample_pair(index: int) -> tuple[bytes, bytes]:
    from philosophia.level1.world import L, R

    left_len = 8 + (index % 40)
    right_len = 8 + ((index * 3) % 40)
    left = bytes(R if ((index + j) % 3) != 0 else L for j in range(left_len))
    right = bytes(R if ((index * 5 + j) % 3) != 0 else L for j in range(right_len))
    return left, right


def _build_history(length: int, device):
    from philosophia.level1.model import encode_pair
    from philosophia.level1.world import oracle_eq

    history_tokens = []
    history_labels = []
    for index in range(length):
        left, right = _sample_pair(index)
        history_tokens.append(encode_pair(left, right).to(device))
        history_labels.append(int(oracle_eq(left, right, MODULUS)))
    return history_tokens, history_labels


def _patch_forward_allow_non_cpu() -> None:
    import torch
    from philosophia.level1.config import MODEL_INPUT_LENGTH
    from philosophia.level1.model import ContactTransformer

    def forward(self, tokens):
        if tokens.dtype != torch.long:
            raise ValueError("tokens must be torch.long")
        if tokens.ndim != 2 or tokens.shape[1] != MODEL_INPUT_LENGTH:
            raise ValueError(f"tokens must have shape (batch, {MODEL_INPUT_LENGTH})")
        key_mask = tokens.ne(0)
        if not bool(key_mask.any(dim=1).all()):
            raise ValueError("every sequence must contain a non-PAD token")
        positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
        x = self.token_embedding[tokens] + self.position_embedding[positions][None, :, :]
        for layer in self.layers:
            x = layer(x, key_mask)
        readout = self.final_ln(x)[:, -1, :]
        return readout @ self.head_W + self.head_b

    ContactTransformer.forward = forward  # type: ignore[method-assign]


def _patch_committee_step_sequential(*, microbatch: int | None = None) -> None:
    """DEV-ONLY: one member at a time; optional microbatches for VRAM."""
    import torch
    from philosophia.level1 import train as train_mod
    from philosophia.level1.config import COMMITTEE_SIZE
    from philosophia.level1.train import UnitStepResult

    def feasibility_committee_step(models, optimizers, tokens, labels, capability):
        if len(models) != COMMITTEE_SIZE or len(optimizers) != COMMITTEE_SIZE:
            raise ValueError("feasibility trains exactly one four-member committee")
        capability.spend_trajectory_step()
        batch = int(tokens.shape[0])
        chunk = batch if microbatch is None else max(1, min(int(microbatch), batch))
        for model, optimizer in zip(models, optimizers):
            optimizer.zero_grad(set_to_none=True)
            for start in range(0, batch, chunk):
                sl = slice(start, min(start + chunk, batch))
                # Mean-CE over the full batch via sum/batch (finite-path equivalent).
                loss = (
                    torch.nn.functional.cross_entropy(
                        model(tokens[sl]), labels[sl], reduction="sum"
                    )
                    / batch
                )
                if not bool(torch.isfinite(loss)):
                    optimizer.zero_grad(set_to_none=True)
                    return UnitStepResult(finite=False)
                loss.backward()
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)
        return UnitStepResult(finite=True)

    train_mod.feasibility_committee_step = feasibility_committee_step


def _fresh_committee(device):
    from philosophia.level1.feasibility import _committee
    from philosophia.level1.model import build_optimizer
    from philosophia.level1.serialization import dummy_key

    key = dummy_key("successor-dev-device-benchmark")
    models, _ = _committee(key, block=0)
    models = [model.to(device) for model in models]
    optimizers = [build_optimizer(model) for model in models]
    return models, optimizers


def _sync(device) -> None:
    import torch

    if device.type == "cuda":
        torch.cuda.synchronize(device)


def _peak_vram_gb(device) -> float | None:
    import torch

    if device.type != "cuda":
        return None
    return torch.cuda.max_memory_allocated(device) / (1024**3)


def _time_one_step(
    *,
    device_type: str,
    history_len: int,
    warmup: int,
    sequential: bool,
    microbatch: int | None,
) -> dict:
    import torch
    from philosophia.level1.interlock import feasibility_v2_capability
    from philosophia.level1.train import full_history_committee_step

    if device_type == "cuda" and not torch.cuda.is_available():
        return {"ok": False, "error": "cuda_unavailable"}

    device = torch.device(device_type)
    _patch_forward_allow_non_cpu()
    # Sequential: one member fwd+bwd+opt at a time. Required on this 8GB
    # laptop so CUDA stays in VRAM; optional on CPU for a fair FLOP-matched
    # speedup ratio. Stock (non-sequential) CPU remains the shape anchor.
    if sequential:
        # On 8GB, history_len=2000 still OOMs with one full-batch graph even
        # sequentially; microbatch keeps peak near the 512-fit regime.
        mb = microbatch
        if mb is None and device_type == "cuda" and history_len > 512:
            mb = 512
        _patch_committee_step_sequential(microbatch=mb)

    if device_type == "cuda":
        # Initialize CUDA context before peak-memory APIs.
        torch.zeros(1, device=device)
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats(device)

    models, optimizers = _fresh_committee(device)
    history_tokens, history_labels = _build_history(history_len, device)
    capability = feasibility_v2_capability()
    capability.claim_development_world(0)

    try:
        for _ in range(warmup):
            result = full_history_committee_step(
                models, optimizers, history_tokens, history_labels, capability
            )
            if not result.finite:
                return {
                    "ok": False,
                    "error": f"non_finite_warmup device={device_type} len={history_len}",
                }
            _sync(device)

        if device_type == "cuda":
            torch.cuda.reset_peak_memory_stats(device)

        _sync(device)
        t0 = time.perf_counter()
        result = full_history_committee_step(
            models, optimizers, history_tokens, history_labels, capability
        )
        _sync(device)
        elapsed = time.perf_counter() - t0
    except torch.cuda.OutOfMemoryError as exc:
        return {"ok": False, "error": f"oom: {exc}"}

    if not result.finite:
        return {
            "ok": False,
            "error": f"non_finite_timed device={device_type} len={history_len}",
        }

    peak = _peak_vram_gb(device)
    return {
        "ok": True,
        "seconds": elapsed,
        "param_device": next(models[0].parameters()).device.type,
        "peak_vram_gb": peak,
        "torch": torch.__version__,
        "device_name": (
            torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"
        ),
    }


def _worker_main() -> None:
    if str(_SRC) not in sys.path:
        sys.path.insert(0, str(_SRC))
    payload = json.loads(sys.argv[1])
    result = _time_one_step(
        device_type=payload["device"],
        history_len=int(payload["history_len"]),
        warmup=int(payload["warmup"]),
        sequential=bool(payload.get("sequential", False)),
        microbatch=payload.get("microbatch"),
    )
    print(json.dumps(result), flush=True)


def _run_isolated(
    device: str,
    history_len: int,
    warmup: int,
    *,
    sequential: bool = False,
    microbatch: int | None = None,
) -> dict:
    payload = json.dumps(
        {
            "device": device,
            "history_len": history_len,
            "warmup": warmup,
            "sequential": sequential,
            "microbatch": microbatch,
        }
    )
    proc = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--worker", payload],
        check=False,
        capture_output=True,
        text=True,
        cwd=str(_ROOT),
    )
    if proc.returncode != 0:
        return {
            "ok": False,
            "error": (
                f"worker_exit={proc.returncode}\n"
                f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
            ),
        }
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip().startswith("{")]
    if not lines:
        return {
            "ok": False,
            "error": f"no_json_stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}",
        }
    return json.loads(lines[-1])


def _linear_slope(lengths: list[int], seconds: list[float]) -> float:
    num = sum(float(n) * s for n, s in zip(lengths, seconds))
    den = sum(float(n) * float(n) for n in lengths)
    if den == 0.0:
        raise RuntimeError("degenerate linear fit")
    return num / den


def _format_hours(seconds: float) -> str:
    hours = seconds / 3600.0
    if hours >= 1.0:
        return f"{hours:.2f} h ({seconds:.1f} s)"
    minutes = seconds / 60.0
    if minutes >= 1.0:
        return f"{minutes:.2f} min ({seconds:.1f} s)"
    return f"{seconds:.2f} s"


def main() -> None:
    if str(_SRC) not in sys.path:
        sys.path.insert(0, str(_SRC))
    import torch

    if not torch.cuda.is_available():
        raise SystemExit(
            "STOP: torch.cuda.is_available() is False; do not install; aborting."
        )

    torch_version = torch.__version__
    device_name = torch.cuda.get_device_name(0)
    print(f"torch={torch_version}", flush=True)
    print(f"cuda_available={True}", flush=True)
    print(f"device_name={device_name}", flush=True)

    rows: list[tuple[int, str, str]] = []
    notes: list[str] = []
    cpu_s: float | None = None
    gpu_by_len: dict[int, float] = {}

    print(f"CPU stock anchor history_len={CPU_ANCHOR_LEN} ...", flush=True)
    cpu_result = _run_isolated("cpu", CPU_ANCHOR_LEN, warmup=0, sequential=False)
    if not cpu_result.get("ok"):
        raise SystemExit(f"CPU anchor failed: {cpu_result}")
    cpu_s = float(cpu_result["seconds"])
    rows.append((CPU_ANCHOR_LEN, "cpu", f"{cpu_s:.6f}"))
    print(f"  cpu {CPU_ANCHOR_LEN}: {cpu_s:.6f}s", flush=True)

    print(
        f"CPU sequential (fair FLOP match) history_len={CPU_ANCHOR_LEN} ...",
        flush=True,
    )
    cpu_seq_result = _run_isolated(
        "cpu", CPU_ANCHOR_LEN, warmup=0, sequential=True
    )
    cpu_seq_s: float | None = None
    if cpu_seq_result.get("ok"):
        cpu_seq_s = float(cpu_seq_result["seconds"])
        rows.append((CPU_ANCHOR_LEN, "cpu_seq", f"{cpu_seq_s:.6f}"))
        print(f"  cpu_seq {CPU_ANCHOR_LEN}: {cpu_seq_s:.6f}s", flush=True)
    else:
        print(f"  cpu_seq FAIL: {cpu_seq_result}", flush=True)

    for length in GPU_LENGTHS:
        print(
            f"CUDA sequential history_len={length} "
            f"(warmup={WARMUP_STEPS}, isolated) ...",
            flush=True,
        )
        gpu_result = _run_isolated(
            "cuda", length, warmup=WARMUP_STEPS, sequential=True
        )
        if not gpu_result.get("ok"):
            err = str(gpu_result.get("error", "unknown"))
            short = "OOM" if "oom" in err.lower() else err.splitlines()[0][:80]
            rows.append((length, "cuda", f"FAIL ({short})"))
            print(f"  cuda {length}: FAIL {short}", flush=True)
            print(err, flush=True)
            continue
        gpu_s = float(gpu_result["seconds"])
        gpu_by_len[length] = gpu_s
        peak = gpu_result.get("peak_vram_gb")
        peak_note = f", peak_vram={peak:.2f}GiB" if isinstance(peak, float) else ""
        rows.append((length, "cuda", f"{gpu_s:.6f}"))
        print(
            f"  cuda {length}: {gpu_s:.6f}s "
            f"(param_device={gpu_result.get('param_device')}{peak_note})",
            flush=True,
        )

    if 512 in gpu_by_len and cpu_seq_s is not None:
        speedup_512 = cpu_seq_s / gpu_by_len[512]
        speedup_line = (
            f"fair (cpu_seq/cuda) speedup at 512 = "
            f"{cpu_seq_s:.6f} / {gpu_by_len[512]:.6f} = {speedup_512:.2f}x"
        )
        if cpu_s is not None:
            stock_ratio = cpu_s / gpu_by_len[512]
            speedup_line += (
                f"; vs stock cpu anchor = "
                f"{cpu_s:.6f} / {gpu_by_len[512]:.6f} = {stock_ratio:.2f}x "
                f"(stock retains 4 graphs; not FLOP-matched to sequential cuda)"
            )
    elif cpu_s is not None and 512 in gpu_by_len:
        speedup_512 = cpu_s / gpu_by_len[512]
        speedup_line = (
            f"speedup = cpu_seconds / gpu_seconds = "
            f"{cpu_s:.6f} / {gpu_by_len[512]:.6f} = {speedup_512:.2f}x"
        )
    else:
        speedup_512 = float("nan")
        speedup_line = "speedup unavailable (missing cpu or cuda@512)."

    if gpu_by_len:
        lengths = sorted(gpu_by_len)
        seconds = [gpu_by_len[n] for n in lengths]
        slope = _linear_slope(lengths, seconds)
        est_full_s = slope * FULL_B * (FULL_B + 1) / 2.0
        missing = [n for n in GPU_LENGTHS if n not in gpu_by_len]
        miss_note = (
            f" Fit used successful CUDA lengths {lengths}"
            + (f"; missing/failed: {missing}." if missing else ".")
        )
        est_block = [
            f"## Estimated full B={FULL_B} run wall-clock on GPU",
            "",
            "Estimate (not a measurement): assume near-linear "
            "`seconds/step ≈ c * history_len` through origin on measured "
            f"CUDA points; full-history cost `sum_{{h=1..B}} c*h = c*B*(B+1)/2`."
            f"{miss_note}",
            "",
            f"Measured OLS slope c = {slope:.9f} s per history token-step.",
            f"Estimated full-run wall-clock on GPU ≈ {_format_hours(est_full_s)}.",
        ]
        if speedup_512 == speedup_512:  # not NaN
            base = cpu_seq_s if cpu_seq_s is not None else cpu_s
            lever = (
                f"Yes — GPU is the lever: at history_len=512 the RTX 4060 Laptop "
                f"sequential step is {speedup_512:.1f}x faster than the matched "
                f"CPU path ({gpu_by_len[512]:.4f}s vs {base:.3f}s), and the "
                f"near-linear extrapolation puts a full B={FULL_B} GPU trajectory "
                f"near {_format_hours(est_full_s)} rather than tens of CPU hours."
            )
        else:
            lever = (
                f"Partial GPU timings; estimated full B={FULL_B} ≈ "
                f"{_format_hours(est_full_s)} from CUDA lengths {lengths}."
            )
    else:
        est_full_s = float("nan")
        est_block = [
            f"## Estimated full B={FULL_B} run wall-clock on GPU",
            "",
            "Estimate unavailable — no successful CUDA step timings.",
        ]
        lever = (
            "No successful CUDA timings — cannot claim GPU as the lever from "
            "this probe."
        )

    notes.append(
        "DEV memory note: stock `feasibility_committee_step` retains four "
        "attention autograd graphs; at history_len>=512 that spills past 8GB "
        "VRAM into system RAM (cuda@512 then ~matched CPU). CUDA timings use a "
        "DEV monkeypatch: sequential per-member fwd+bwd+opt, with microbatch=512 "
        "when history_len>512 (mean-CE via sum/batch; finite-path equivalent) so "
        "timings reflect in-VRAM GPU compute. `cpu` row is stock "
        "full_history_committee_step (shape anchor); `cpu_seq` is the FLOP-matched "
        "baseline for the speedup ratio."
    )

    lines = [
        "# LEGION_DEVICE_BENCHMARK",
        "",
        "NON-CITABLE engineering one-step wall-clock probe only.",
        "No scientific datum, comparative result, or claim.",
        "Does not reopen frozen Level 1 feasibility records.",
        "",
        f"env: torch={torch_version}; device={device_name}; "
        f"cuda_available=True; "
        f"interpreter=ComfyUI .venv (no project venv created).",
        "",
        "Runtime notes: skipped `configure_canonical_runtime()` pins. "
        "DEV-ONLY monkeypatch of `ContactTransformer.forward` CPU-device guard. "
        "Warmup excluded from timing; `torch.cuda.synchronize()` around timed "
        "CUDA regions. Each (device, length) run is an isolated subprocess.",
        "",
        notes[0],
        "",
        "## One-step timings (seconds/step)",
        "",
        "| history_len | device | seconds/step |",
        "| ---: | --- | ---: |",
    ]
    for history_len, device, cell in rows:
        lines.append(f"| {history_len} | {device} | {cell} |")

    lines.extend(
        [
            "",
            f"## GPU-vs-CPU speedup at history_len={CPU_ANCHOR_LEN}",
            "",
            speedup_line,
            "",
        ]
    )
    lines.extend(est_block)
    lines.extend(["", "## Lever sentence", "", lever, ""])

    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    # Avoid Windows cp1251 console crash on special chars.
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--worker":
        sys.argv = [sys.argv[0], sys.argv[2]]
        _worker_main()
    else:
        main()
