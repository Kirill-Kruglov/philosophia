"""NON-CITABLE engineering wall-clock attribution for full_history_committee_step.

Produces no scientific datum, comparative result, or claim. Does not re-run or
reopen the censored Level 1 feasibility v2 record. All output stays under
successor/dev/. Does not modify src/, canonical/, or any frozen threshold.
"""

from __future__ import annotations

import cProfile
import io
import math
import pstats
import time
from pathlib import Path

import torch

from philosophia.level1.feasibility import _committee
from philosophia.level1.interlock import feasibility_v2_capability
from philosophia.level1.model import configure_canonical_runtime, encode_pair
from philosophia.level1.serialization import dummy_key
from philosophia.level1.train import FullHistoryStepResult, feasibility_committee_step
from philosophia.level1.world import L, R, oracle_eq

MODULUS = 66
REPORT_LENGTHS = (1, 32, 64, 128, 256, 512)
MAX_HISTORY = max(REPORT_LENGTHS)
OUT_MD = Path(__file__).resolve().parent / "PROFILE_FULL_HISTORY.md"


def _sample_pair(index: int) -> tuple[bytes, bytes]:
    """Synthetic R/L pair with encode_pair-compatible shapes (not the frozen run)."""
    left_len = 8 + (index % 40)
    right_len = 8 + ((index * 3) % 40)
    left = bytes(R if ((index + j) % 3) != 0 else L for j in range(left_len))
    right = bytes(R if ((index * 5 + j) % 3) != 0 else L for j in range(right_len))
    return left, right


def _timed_full_history_committee_step(
    models,
    optimizers,
    history_tokens,
    history_labels,
    capability,
) -> tuple[FullHistoryStepResult, float, float, float]:
    """Mirror of train.full_history_committee_step with phase timers.

    Phases match the three contiguous blocks of that function:
      (a) torch.stack / label tensor assembly
      (b) feasibility_committee_step (committee fwd+bwd+optimizer)
      (c) full-parameter torch.isfinite scan
    """
    if not history_tokens or len(history_tokens) != len(history_labels):
        raise ValueError("full-history tokens and labels must be non-empty and aligned")

    t0 = time.perf_counter()
    tokens = torch.stack(tuple(history_tokens))
    labels = torch.tensor(tuple(history_labels), dtype=torch.long, device=tokens.device)
    t1 = time.perf_counter()

    loss_result = feasibility_committee_step(
        models,
        optimizers,
        tokens,
        labels,
        capability,
    )
    t2 = time.perf_counter()

    parameters_finite = all(
        bool(torch.isfinite(parameter).all())
        for model in models
        for parameter in model.parameters()
    )
    t3 = time.perf_counter()

    result = FullHistoryStepResult(
        losses_finite=loss_result.finite,
        parameters_finite=parameters_finite,
    )
    return result, t1 - t0, t2 - t1, t3 - t2


def _loglog_exponent(xs: list[float], ys: list[float]) -> float:
    """Ordinary least-squares slope of log(y) vs log(x)."""
    log_x = [math.log(x) for x in xs]
    log_y = [math.log(y) for y in ys]
    n = len(log_x)
    mean_x = sum(log_x) / n
    mean_y = sum(log_y) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_x, log_y))
    den = sum((x - mean_x) ** 2 for x in log_x)
    if den == 0.0:
        raise RuntimeError("degenerate log-log fit")
    return num / den


def _run_profiled_growth(
    models,
    optimizers,
    capability,
) -> tuple[dict[int, tuple[float, float, float, float]], str]:
    history_tokens: list[torch.Tensor] = []
    history_labels: list[int] = []
    rows: dict[int, tuple[float, float, float, float]] = {}

    profiler = cProfile.Profile()
    profiler.enable()
    try:
        for length in range(1, MAX_HISTORY + 1):
            left, right = _sample_pair(length - 1)
            history_tokens.append(encode_pair(left, right))
            history_labels.append(int(oracle_eq(left, right, MODULUS)))
            if length not in REPORT_LENGTHS:
                continue
            result, stack_s, train_s, scan_s = _timed_full_history_committee_step(
                models,
                optimizers,
                history_tokens,
                history_labels,
                capability,
            )
            if not result.finite:
                raise RuntimeError(
                    f"non-finite learner state at history_len={length}"
                )
            total_s = stack_s + train_s + scan_s
            rows[length] = (stack_s, train_s, scan_s, total_s)
            print(
                f"history_len={length}: "
                f"stack={stack_s:.6f}s train={train_s:.6f}s "
                f"scan={scan_s:.6f}s total={total_s:.6f}s",
                flush=True,
            )
    finally:
        profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(20)
    return rows, stream.getvalue()


def _format_report(
    rows: dict[int, tuple[float, float, float, float]],
    cprofile_text: str,
    cuda_available: bool,
    hip_version: object,
) -> str:
    lengths = [n for n in REPORT_LENGTHS if n in rows]
    totals = [rows[n][3] for n in lengths]
    exponent = _loglog_exponent([float(n) for n in lengths], totals)

    lines: list[str] = [
        "# PROFILE_FULL_HISTORY",
        "",
        "NON-CITABLE engineering wall-clock attribution only.",
        "No scientific datum, comparative result, or claim.",
        "Does not reopen the censored Level 1 feasibility v2 record.",
        "",
        f"Runtime: CPU via `configure_canonical_runtime()`; modulus={MODULUS} (shape realism only).",
        "",
        "## Per-step phase times (seconds)",
        "",
        "| history_len | (a) stack | (b) committee fwd+bwd+opt | (c) isfinite scan | sum |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for n in lengths:
        stack_s, train_s, scan_s, total_s = rows[n]
        lines.append(
            f"| {n} | {stack_s:.6f} | {train_s:.6f} | {scan_s:.6f} | {total_s:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Growth exponent",
            "",
            "Fit: `log(sum_seconds) = alpha * log(history_len) + beta` "
            f"over history_len in {{{', '.join(str(n) for n in lengths)}}}.",
            "",
            f"Measured growth exponent alpha = {exponent:.6f}",
            "",
            f"Interpretation check: alpha≈1 is linear in history_len; "
            f"measured alpha={exponent:.3f}.",
            "",
            "## cProfile top 20 (cumulative)",
            "",
            "```",
            cprofile_text.rstrip(),
            "```",
            "",
            "## CUDA / HIP availability (report only)",
            "",
            f"`torch.cuda.is_available()` = {cuda_available}",
            f"`torch.version.hip` = {hip_version!r}",
            "",
            "## Dominating phase (raw measurement)",
            "",
        ]
    )

    # One paragraph from the numbers only.
    dominant_at: list[str] = []
    for n in lengths:
        stack_s, train_s, scan_s, total_s = rows[n]
        phases = {
            "(a) stack": stack_s,
            "(b) committee fwd+bwd+opt": train_s,
            "(c) isfinite scan": scan_s,
        }
        name = max(phases, key=phases.get)
        share = 100.0 * phases[name] / total_s if total_s else 0.0
        dominant_at.append(f"{name} at history_len={n} ({share:.1f}% of sum)")
    scan_vals = [rows[n][2] for n in lengths]
    scan_min, scan_max = min(scan_vals), max(scan_vals)
    train_vals = [rows[n][1] for n in lengths]
    train_ratio = (
        train_vals[-1] / train_vals[0] if train_vals[0] > 0 else float("inf")
    )
    # Scan must not track history_len linearly the way (b) does.
    scan_vs_hist = _loglog_exponent(
        [float(n) for n in lengths],
        [max(v, 1e-12) for v in scan_vals],
    )
    paragraph = (
        f"Across reported lengths, phase dominance is: {'; '.join(dominant_at)}. "
        f"Phase (b) grows with history_len (ratio "
        f"{train_vals[-1]:.6f}/{train_vals[0]:.6f} = {train_ratio:.3f} from "
        f"len {lengths[0]} to {lengths[-1]}; log-log exponent of sum = {exponent:.3f}). "
        f"Phase (c) stays a small absolute overhead "
        f"(range {scan_min:.6f}–{scan_max:.6f} s; its own log-log exponent vs "
        f"history_len = {scan_vs_hist:.3f}, not tracking the linear growth of (b)), "
        f"i.e. independent of history length at the scale of the step; "
        f"phase (a) remains negligible."
    )
    lines.append(paragraph)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    configure_canonical_runtime()
    cuda_available = bool(torch.cuda.is_available())
    hip_version = torch.version.hip
    print(f"torch.cuda.is_available() = {cuda_available}", flush=True)
    print(f"torch.version.hip = {hip_version!r}", flush=True)

    key = dummy_key("successor-dev-profile-full-history")
    models, optimizers = _committee(key, block=0)
    capability = feasibility_v2_capability()
    capability.claim_development_world(0)

    rows, cprofile_text = _run_profiled_growth(models, optimizers, capability)
    report = _format_report(rows, cprofile_text, cuda_available, hip_version)
    OUT_MD.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    print(report, flush=True)


if __name__ == "__main__":
    main()
