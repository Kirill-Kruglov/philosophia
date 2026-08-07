"""NON-CITABLE memory-safe GPU committee training runner (dev only).

No scientific datum, comparative result, or claim.
Does not modify src/, canonical/, experiments/, or frozen thresholds.

Implements a CUDA-friendly 4-member committee step that is numerically
intended to match stock `feasibility_committee_step` mean-CE updates:
  - members run SEQUENTIALLY (one autograd graph at a time),
  - history is processed in microbatches with TRUE size-weighted
    accumulation: each chunk contributes
        backward(sum_CE(chunk) / N)
    so the accumulated gradient equals the full-batch mean-CE gradient.

Also contains the K-step CPU(stock) vs GPU(runner) equivalence probe that
writes RUNNER_EQUIVALENCE.md.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import torch
from torch import Tensor

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from philosophia.level1.config import COMMITTEE_SIZE, MODEL_INPUT_LENGTH
from philosophia.level1.feasibility import _committee
from philosophia.level1.interlock import FeasibilityCapability, feasibility_v2_capability
from philosophia.level1.model import ContactTransformer, build_optimizer, encode_pair
from philosophia.level1.serialization import dummy_key
from philosophia.level1.train import FullHistoryStepResult, UnitStepResult
from philosophia.level1.world import L, R, oracle_eq

OUT_MD = Path(__file__).resolve().parent / "RUNNER_EQUIVALENCE.md"
MODULUS = 66
DEFAULT_MICROBATCH = 512
EQUIV_HISTORY_LEN = 64
EQUIV_STEPS = 10
EQUIV_MICROBATCH = 16  # divides 64; exercises multi-chunk accumulation
NOISE_CEILING = 1e-3  # after-K param ceiling (Adam amplifies ~1e-6 grad noise)
LOSS_NOISE_HI = 2e-4  # per-step loss band (~1e-5..1e-4 with slack)


@dataclass(frozen=True)
class CommitteeStepReport:
    """Per-step losses plus the stock-shaped finite flags."""

    losses: tuple[float, ...]
    result: FullHistoryStepResult


_FORWARD_PATCHED = False


def patch_contact_transformer_device_guard() -> None:
    """DEV-ONLY: allow ContactTransformer.forward on non-CPU devices."""
    global _FORWARD_PATCHED
    if _FORWARD_PATCHED:
        return

    def forward(self: ContactTransformer, tokens: Tensor) -> Tensor:
        if tokens.dtype != torch.long:
            raise ValueError("tokens must be torch.long")
        if tokens.ndim != 2 or tokens.shape[1] != MODEL_INPUT_LENGTH:
            raise ValueError(f"tokens must have shape (batch, {MODEL_INPUT_LENGTH})")
        # Intentionally skip stock CPU-only guard.
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
    _FORWARD_PATCHED = True


def _mean_ce_chunked_no_grad(
    model: ContactTransformer,
    tokens: Tensor,
    labels: Tensor,
    microbatch: int,
) -> Tensor:
    n = int(tokens.shape[0])
    chunk = max(1, min(int(microbatch), n))
    total = tokens.new_zeros(())
    with torch.no_grad():
        for start in range(0, n, chunk):
            sl = slice(start, min(start + chunk, n))
            total = total + torch.nn.functional.cross_entropy(
                model(tokens[sl]), labels[sl], reduction="sum"
            )
    return total / n


def memory_safe_feasibility_committee_step(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.AdamW],
    tokens: Tensor,
    labels: Tensor,
    capability: FeasibilityCapability,
    *,
    microbatch: int = DEFAULT_MICROBATCH,
) -> tuple[UnitStepResult, tuple[float, ...]]:
    """Sequential members + size-weighted microbatch grads (= full-batch mean CE).

    Matches stock finite-path semantics: if any member's mean CE is non-finite,
    no member is updated. Gradients use
        backward(sum_{i in chunk} CE_i / N)
    so accumulated grads equal the stock full-batch mean-CE backward.
    """
    if len(models) != COMMITTEE_SIZE or len(optimizers) != COMMITTEE_SIZE:
        raise ValueError("feasibility trains exactly one four-member committee")
    capability.spend_trajectory_step()

    n = int(tokens.shape[0])
    if n == 0:
        raise ValueError("tokens batch must be non-empty")
    chunk = max(1, min(int(microbatch), n))

    # Pass 1: stock-equivalent mean losses (for finite gate + reporting).
    mean_losses = [
        _mean_ce_chunked_no_grad(model, tokens, labels, chunk) for model in models
    ]
    loss_vals = tuple(float(value.detach().cpu()) for value in mean_losses)
    finite = all(bool(torch.isfinite(value)) for value in mean_losses)
    if not finite:
        return UnitStepResult(finite=False), loss_vals

    # Pass 2: size-weighted accumulation, one member at a time.
    for model, optimizer in zip(models, optimizers):
        optimizer.zero_grad(set_to_none=True)
        for start in range(0, n, chunk):
            sl = slice(start, min(start + chunk, n))
            # True size-weighted piece of mean CE: (sum CE_chunk) / N.
            piece = (
                torch.nn.functional.cross_entropy(
                    model(tokens[sl]), labels[sl], reduction="sum"
                )
                / n
            )
            if not bool(torch.isfinite(piece)):
                optimizer.zero_grad(set_to_none=True)
                return UnitStepResult(finite=False), loss_vals
            piece.backward()
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)

    return UnitStepResult(finite=True), loss_vals


def memory_safe_full_history_committee_step(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.AdamW],
    history_tokens: Sequence[Tensor],
    history_labels: Sequence[int],
    capability: FeasibilityCapability,
    *,
    microbatch: int = DEFAULT_MICROBATCH,
) -> CommitteeStepReport:
    """Memory-safe counterpart of train.full_history_committee_step."""
    if not history_tokens or len(history_tokens) != len(history_labels):
        raise ValueError("full-history tokens and labels must be non-empty and aligned")
    tokens = torch.stack(tuple(history_tokens))
    labels = torch.tensor(tuple(history_labels), dtype=torch.long, device=tokens.device)
    loss_result, loss_vals = memory_safe_feasibility_committee_step(
        models,
        optimizers,
        tokens,
        labels,
        capability,
        microbatch=microbatch,
    )
    parameters_finite = all(
        bool(torch.isfinite(parameter).all())
        for model in models
        for parameter in model.parameters()
    )
    return CommitteeStepReport(
        losses=loss_vals,
        result=FullHistoryStepResult(
            losses_finite=loss_result.finite,
            parameters_finite=parameters_finite,
        ),
    )


def stock_full_history_committee_step_with_losses(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.AdamW],
    history_tokens: Sequence[Tensor],
    history_labels: Sequence[int],
    capability: FeasibilityCapability,
) -> CommitteeStepReport:
    """Stock science path, returning the 4 mean-CE values used for the update."""
    if not history_tokens or len(history_tokens) != len(history_labels):
        raise ValueError("full-history tokens and labels must be non-empty and aligned")
    tokens = torch.stack(tuple(history_tokens))
    labels = torch.tensor(tuple(history_labels), dtype=torch.long, device=tokens.device)
    capability.spend_trajectory_step()
    losses = [
        torch.nn.functional.cross_entropy(model(tokens), labels, reduction="mean")
        for model in models
    ]
    loss_vals = tuple(float(value.detach().cpu()) for value in losses)
    finite = all(bool(torch.isfinite(loss)) for loss in losses)
    if finite:
        for loss in losses:
            loss.backward()
        for optimizer in optimizers:
            optimizer.step()
            optimizer.zero_grad()
    parameters_finite = all(
        bool(torch.isfinite(parameter).all())
        for model in models
        for parameter in model.parameters()
    )
    return CommitteeStepReport(
        losses=loss_vals,
        result=FullHistoryStepResult(
            losses_finite=finite,
            parameters_finite=parameters_finite,
        ),
    )


def _sample_pair(index: int) -> tuple[bytes, bytes]:
    left_len = 8 + (index % 40)
    right_len = 8 + ((index * 3) % 40)
    left = bytes(R if ((index + j) % 3) != 0 else L for j in range(left_len))
    right = bytes(R if ((index * 5 + j) % 3) != 0 else L for j in range(right_len))
    return left, right


def build_identical_histories(
    length: int,
) -> tuple[list[Tensor], list[int], list[Tensor], list[int]]:
    """Identical synthetic history on CPU and CUDA (token-for-token)."""
    cpu_tokens: list[Tensor] = []
    labels: list[int] = []
    for index in range(length):
        left, right = _sample_pair(index)
        cpu_tokens.append(encode_pair(left, right))
        labels.append(int(oracle_eq(left, right, MODULUS)))
    gpu_tokens = [tensor.to("cuda") for tensor in cpu_tokens]
    return cpu_tokens, list(labels), gpu_tokens, list(labels)


def build_identical_committees(
    key_label: str = "successor-dev-gpu-committee-runner-equiv",
) -> tuple[
    list[ContactTransformer],
    list[torch.optim.AdamW],
    list[ContactTransformer],
    list[torch.optim.AdamW],
]:
    """Same PRF init on CPU (R) and CUDA (G); fresh AdamW on each."""
    key = dummy_key(key_label)
    models_r, optimizers_r = _committee(key, block=0)
    models_g_cpu, _ = _committee(key, block=0)
    models_g = [model.to("cuda") for model in models_g_cpu]
    optimizers_g = [build_optimizer(model) for model in models_g]
    return models_r, optimizers_r, models_g, optimizers_g


def _flatten_params(models: Sequence[ContactTransformer]) -> Tensor:
    return torch.cat(
        [parameter.detach().reshape(-1).float().cpu() for model in models for parameter in model.parameters()]
    )


def _loss_diffs(
    ref: Sequence[float], gpu: Sequence[float]
) -> tuple[float, float]:
    abs_diffs = [abs(a - b) for a, b in zip(ref, gpu)]
    return max(abs_diffs), sum(abs_diffs) / len(abs_diffs)


def _top_param_diffs(
    models_a: Sequence[ContactTransformer],
    models_b: Sequence[ContactTransformer],
    *,
    top_k: int = 8,
) -> list[tuple[float, float, int, str]]:
    worst: list[tuple[float, float, int, str]] = []
    for member, (model_a, model_b) in enumerate(zip(models_a, models_b)):
        for (name_a, param_a), (_, param_b) in zip(
            model_a.named_parameters(), model_b.named_parameters()
        ):
            diff = (param_a.detach().cpu() - param_b.detach().cpu()).abs()
            worst.append(
                (float(diff.max()), float(diff.mean()), member, name_a)
            )
    worst.sort(reverse=True)
    return worst[:top_k]


def _run_pair(
    *,
    label: str,
    models_a,
    opts_a,
    models_b,
    opts_b,
    hist_a,
    labels_a,
    hist_b,
    labels_b,
    steps: int,
    microbatch: int,
    b_is_memory_safe: bool,
) -> dict:
    cap_a = feasibility_v2_capability()
    cap_a.claim_development_world(0)
    cap_b = feasibility_v2_capability()
    cap_b.claim_development_world(0)

    per_step_rows: list[str] = []
    loss_max_series: list[float] = []
    loss_mean_series: list[float] = []

    for step in range(1, steps + 1):
        report_a = stock_full_history_committee_step_with_losses(
            models_a, opts_a, hist_a, labels_a, cap_a
        )
        if b_is_memory_safe:
            report_b = memory_safe_full_history_committee_step(
                models_b,
                opts_b,
                hist_b,
                labels_b,
                cap_b,
                microbatch=microbatch,
            )
        else:
            report_b = stock_full_history_committee_step_with_losses(
                models_b, opts_b, hist_b, labels_b, cap_b
            )
        if not report_a.result.finite or not report_b.result.finite:
            raise RuntimeError(
                f"{label}: non-finite at step {step}: "
                f"A={report_a.result} B={report_b.result}"
            )
        loss_max, loss_mean = _loss_diffs(report_a.losses, report_b.losses)
        loss_max_series.append(loss_max)
        loss_mean_series.append(loss_mean)
        per_step_rows.append(
            f"| {step} | {loss_max:.6e} | {loss_mean:.6e} | "
            f"{tuple(f'{v:.8f}' for v in report_a.losses)} | "
            f"{tuple(f'{v:.8f}' for v in report_b.losses)} |"
        )
        print(
            f"{label} step {step}: loss_max_abs={loss_max:.6e} "
            f"loss_mean_abs={loss_mean:.6e}",
            flush=True,
        )

    delta = (_flatten_params(models_a) - _flatten_params(models_b)).abs()
    param_max = float(delta.max())
    param_mean = float(delta.mean())
    tops = _top_param_diffs(models_a, models_b)
    return {
        "per_step_rows": per_step_rows,
        "loss_max_series": loss_max_series,
        "loss_mean_series": loss_mean_series,
        "param_max": param_max,
        "param_mean": param_mean,
        "tops": tops,
    }


def _grad_equivalence_check(
    history_len: int,
    microbatch: int,
) -> dict:
    """Same-device full-batch vs microbatch grad max-abs (no optimizer)."""
    import copy

    import torch.nn.functional as F

    key = dummy_key("successor-dev-gpu-committee-runner-grad-check")
    models, _ = _committee(key, block=0)
    hist, labels, _, _ = build_identical_histories(history_len)
    tokens = torch.stack(hist)
    lab = torch.tensor(labels, dtype=torch.long)
    n = int(tokens.shape[0])
    chunk = max(1, min(int(microbatch), n))
    per_member: list[float] = []
    for model in models:
        m_full = copy.deepcopy(model)
        m_mb = copy.deepcopy(model)
        m_full.zero_grad(set_to_none=True)
        m_mb.zero_grad(set_to_none=True)
        F.cross_entropy(m_full(tokens), lab, reduction="mean").backward()
        for start in range(0, n, chunk):
            sl = slice(start, min(start + chunk, n))
            (
                F.cross_entropy(m_mb(tokens[sl]), lab[sl], reduction="sum") / n
            ).backward()
        max_diff = 0.0
        for param_a, param_b in zip(m_full.parameters(), m_mb.parameters()):
            if param_a.grad is None and param_b.grad is None:
                continue
            max_diff = max(
                max_diff, float((param_a.grad - param_b.grad).abs().max())
            )
        per_member.append(max_diff)
    return {
        "per_member_grad_max_abs": per_member,
        "grad_max_abs": max(per_member),
    }


def run_equivalence_proof(
    *,
    history_len: int = EQUIV_HISTORY_LEN,
    steps: int = EQUIV_STEPS,
    microbatch: int = EQUIV_MICROBATCH,
) -> str:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA required for GPU runner equivalence proof")

    patch_contact_transformer_device_guard()
    # Do NOT call configure_canonical_runtime — pinned torch/CPython would fail.
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False

    grad_check = _grad_equivalence_check(history_len, microbatch)
    print(
        f"grad-check max abs (full-batch vs microbatch) = "
        f"{grad_check['grad_max_abs']:.6e}",
        flush=True,
    )

    # --- Control: CPU stock vs CPU memory-safe (algorithm check) ---
    key = dummy_key("successor-dev-gpu-committee-runner-equiv-control")
    models_c0, opts_c0 = _committee(key, block=0)
    models_c1, _ = _committee(key, block=0)
    opts_c1 = [build_optimizer(model) for model in models_c1]
    hist_c, labels_c, _, _ = build_identical_histories(history_len)
    control = _run_pair(
        label="CPU-control",
        models_a=models_c0,
        opts_a=opts_c0,
        models_b=models_c1,
        opts_b=opts_c1,
        hist_a=hist_c,
        labels_a=labels_c,
        hist_b=hist_c,
        labels_b=labels_c,
        steps=steps,
        microbatch=microbatch,
        b_is_memory_safe=True,
    )

    # --- Primary: CPU stock (R) vs CUDA memory-safe (G) ---
    models_r, opts_r, models_g, opts_g = build_identical_committees()
    init_max = float((_flatten_params(models_r) - _flatten_params(models_g)).abs().max())
    if init_max != 0.0:
        raise RuntimeError(f"identical init failed: max abs param diff={init_max}")

    hist_r, labels_r, hist_g, labels_g = build_identical_histories(history_len)
    primary = _run_pair(
        label="R-vs-G",
        models_a=models_r,
        opts_a=opts_r,
        models_b=models_g,
        opts_b=opts_g,
        hist_a=hist_r,
        labels_a=labels_r,
        hist_b=hist_g,
        labels_b=labels_g,
        steps=steps,
        microbatch=microbatch,
        b_is_memory_safe=True,
    )

    loss_max_series = primary["loss_max_series"]
    param_max = primary["param_max"]
    param_mean = primary["param_mean"]

    grad_ok = grad_check["grad_max_abs"] < 1e-5
    loss_ok = max(loss_max_series) <= LOSS_NOISE_HI
    param_ok = param_max <= NOISE_CEILING

    if grad_ok and loss_ok and param_ok:
        verdict = "EQUIVALENT (float-noise)"
        verdict_detail = (
            f"One-step grads match (max abs {grad_check['grad_max_abs']:.6e}). "
            f"R-vs-G per-step loss max-abs <= {max(loss_max_series):.6e}. "
            f"Final param max-abs={param_max:.6e}, mean-abs={param_mean:.6e}."
        )
    elif grad_ok and loss_ok and not param_ok:
        # Accumulation formula is correct; Adam compounded float associativity.
        top = primary["tops"][0]
        verdict = "NOT EQUIVALENT (diverges)"
        verdict_detail = (
            f"Losses stay float-noise (max abs {max(loss_max_series):.6e}) and "
            f"one-step grads match ({grad_check['grad_max_abs']:.6e}), so the "
            f"size-weighted accumulator is not the bug; after K={steps} Adam "
            f"steps, param max-abs grows to {param_max:.6e} "
            f"(worst: member {top[2]} `{top[3]}`). "
            f"Same-device CPU-control also reaches param max-abs="
            f"{control['param_max']:.6e} from float32 reduction associativity "
            f"amplified by Adam — not a silent formula mismatch."
        )
    else:
        verdict = "NOT EQUIVALENT (diverges)"
        where = []
        if not grad_ok:
            where.append(
                f"one-step grad max-abs={grad_check['grad_max_abs']:.6e} "
                "(accumulation formula suspect)"
            )
        if not loss_ok:
            worst = max(range(steps), key=lambda i: loss_max_series[i]) + 1
            where.append(
                f"R-vs-G loss max-abs peaked at step {worst} = "
                f"{max(loss_max_series):.6e}"
            )
        if not param_ok:
            top = primary["tops"][0]
            where.append(
                f"final param max-abs={param_max:.6e} "
                f"(worst: member {top[2]} `{top[3]}`)"
            )
        verdict_detail = "Divergence markers: " + "; ".join(where) + "."

    top_lines = [
        f"| {member} | `{name}` | {mx:.6e} | {mn:.6e} |"
        for mx, mn, member, name in primary["tops"]
    ]
    control_top_lines = [
        f"| {member} | `{name}` | {mx:.6e} | {mn:.6e} |"
        for mx, mn, member, name in control["tops"][:5]
    ]
    grad_member_line = ", ".join(
        f"m{i}={v:.6e}" for i, v in enumerate(grad_check["per_member_grad_max_abs"])
    )

    lines = [
        "# RUNNER_EQUIVALENCE",
        "",
        "NON-CITABLE engineering numerical-equivalence probe only.",
        "No scientific datum, comparative result, or claim.",
        "Does not touch feasibility floors, thresholds, or frozen records.",
        "",
        f"env: torch={torch.__version__}; "
        f"device={torch.cuda.get_device_name(0)}; cuda_available=True; "
        "TF32 disabled for this probe.",
        "",
        "Setup: identical `_committee` PRF init; identical synthetic history "
        f"(history_len={history_len}); K={steps} steps.",
        f"(R) CPU stock full-batch mean-CE path.",
        f"(G) CUDA memory-safe runner: sequential members, microbatch={microbatch}, "
        "size-weighted accumulation `backward(sum_CE(chunk)/N)`.",
        "Skipped `configure_canonical_runtime` pins. DEV monkeypatch of "
        "`ContactTransformer.forward` CPU-device guard only.",
        "",
        f"Initial max abs param diff (R vs G) = {init_max:.6e} (must be 0).",
        "",
        "## One-step gradient check (CPU full-batch vs CPU microbatch)",
        "",
        f"- max abs grad diff across committee = {grad_check['grad_max_abs']:.6e}",
        f"- per member: {grad_member_line}",
        "",
        "## Control: CPU stock vs CPU memory-safe (same device, K steps)",
        "",
        "| step | max abs loss diff | mean abs loss diff | A losses | B losses |",
        "| ---: | ---: | ---: | --- | --- |",
        *control["per_step_rows"],
        "",
        f"- final param max abs = {control['param_max']:.6e}",
        f"- final param mean abs = {control['param_mean']:.6e}",
        "",
        "| member | parameter | max abs | mean abs |",
        "| ---: | --- | ---: | ---: |",
        *control_top_lines,
        "",
        "## Primary: (R) CPU stock vs (G) CUDA memory-safe",
        "",
        "| step | max abs loss diff | mean abs loss diff | R losses | G losses |",
        "| ---: | ---: | ---: | --- | --- |",
        *primary["per_step_rows"],
        "",
        "## Final parameter differences after step K (R vs G)",
        "",
        f"- max abs param diff = {param_max:.6e}",
        f"- mean abs param diff = {param_mean:.6e}",
        "",
        "| member | parameter | max abs | mean abs |",
        "| ---: | --- | ---: | ---: |",
        *top_lines,
        "",
        "## Verdict",
        "",
        f"**{verdict}**",
        "",
        verdict_detail,
        "",
        f"Loss float-noise band target ~1e-5..1e-4 (probe ceiling {LOSS_NOISE_HI:g}); "
        f"param ceiling after K Adam steps = {NOISE_CEILING:g}.",
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    report = run_equivalence_proof()
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
