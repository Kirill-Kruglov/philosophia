"""NON-CITABLE D0.1b1 competence diagnostic against the frozen Level 1 floor.

Dev world only. No confirmatory datum. No src/ edits.
Drives successor/dev/gpu_committee_runner.py on RANDOM-STATIC modulus 66,
scores every CHECKPOINT_CADENCE step with frozen scoring.py, writes
successor/dev/COMPETENCE_DIAG_01.md.
"""

from __future__ import annotations

import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import torch

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

from philosophia.level1.config import (  # noqa: E402
    BUDGET,
    CHECKPOINT_CADENCE,
    MODEL_INPUT_LENGTH,
    PANEL_SIZE,
    PANEL_STRATUM_COUNTS,
    PERSISTENCE_CHECKPOINTS,
)
from philosophia.level1.feasibility import (  # noqa: E402
    _committee,
    random_static_schedule,
)
from philosophia.level1.interlock import feasibility_v2_capability  # noqa: E402
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    DTYPE,
    HEADS as MODEL_HEADS,
    LAYERS,
    MLP_WIDTH,
    MODEL_INPUT_LENGTH,
    VOCAB_SIZE,
    build_optimizer,
    committee_equal_probability,
    encode_pair,
)
from philosophia.level1.panel import DummyPanel, DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.scoring import (  # noqa: E402
    ACCURACY_MINIMUM,
    PanelObservation,
    StratumScore,
    checkpoint_qualifies,
    first_persistent_step,
    score_stratum,
)
from philosophia.level1.serialization import dummy_key  # noqa: E402
from philosophia.level1.world import oracle_eq  # noqa: E402

import gpu_committee_runner as runner  # noqa: E402

OUT_MD = _DEV / "COMPETENCE_DIAG_01.md"
MODULUS = 66
WORLD_SLOT = 0  # modulus 66 -> canonical slot 0 in dummy-world enumeration
DEV_PUBLIC_LABEL = "successor-dev-competence-diag-01"
DEV_PANEL_LABEL = "successor-dev-competence-diag-01"
MICROBATCH = 128
DEVICE = torch.device("cuda")


@dataclass(frozen=True)
class CheckpointRecord:
    step: int
    qualifies: bool
    by_stratum: dict[str, StratumScore]
    n_strata_ok: int
    total_correct: int
    total_abstentions: int
    total_confident_lies: int
    mean_brier: float


def _build_dev_panel(public_key) -> tuple[DummyPanel, object]:
    panel_key = dummy_key(DEV_PANEL_LABEL, purpose="panel")
    builder = DummyPanelBuilder(public_key, panel_key)
    panel = builder.build(MODULUS, world_slot=WORLD_SLOT)
    return panel, builder.partition


def _score_panel(models, panel: DummyPanel) -> CheckpointRecord:
    tokens = torch.stack(
        [encode_pair(item.left, item.right).to(DEVICE) for item in panel.items]
    )
    # Recompute oracle truths for the report path; must match panel.truth.
    truths = [bool(oracle_eq(item.left, item.right, MODULUS)) for item in panel.items]
    if any(truth != item.truth for truth, item in zip(truths, panel.items)):
        raise RuntimeError("oracle_eq disagrees with panel.truth")

    probabilities = committee_equal_probability(models, tokens)
    observations = [
        PanelObservation(item.stratum, item.truth, float(probability))
        for item, probability in zip(panel.items, probabilities, strict=True)
    ]
    by_stratum: dict[str, StratumScore] = {}
    for name in PANEL_STRATUM_COUNTS:
        values = [obs for obs in observations if obs.stratum == name]
        by_stratum[name] = score_stratum(name, values)

    qualifies = checkpoint_qualifies(observations)
    return CheckpointRecord(
        step=-1,  # filled by caller
        qualifies=qualifies,
        by_stratum=by_stratum,
        n_strata_ok=sum(1 for score in by_stratum.values() if score.qualifies),
        total_correct=sum(score.correct for score in by_stratum.values()),
        total_abstentions=sum(score.abstentions for score in by_stratum.values()),
        total_confident_lies=sum(score.confident_lies for score in by_stratum.values()),
        mean_brier=sum(score.brier for score in by_stratum.values())
        / len(by_stratum),
    )


def _longest_qualifying_run(
    qualifying: dict[int, bool],
) -> tuple[int, int | None, int | None]:
    """Return (length, start_step, end_step) over cadence grid."""
    steps = tuple(range(0, BUDGET + 1, CHECKPOINT_CADENCE))
    best_len = 0
    best_start: int | None = None
    best_end: int | None = None
    run = 0
    run_start: int | None = None
    for step in steps:
        if qualifying[step]:
            if run == 0:
                run_start = step
            run += 1
            if run > best_len:
                best_len = run
                best_start = run_start
                best_end = step
        else:
            run = 0
            run_start = None
    return best_len, best_start, best_end


def _pick_best(records: Sequence[CheckpointRecord]) -> CheckpointRecord:
    return max(
        records,
        key=lambda r: (
            r.n_strata_ok,
            r.total_correct,
            -r.total_confident_lies,
            -r.total_abstentions,
            -r.mean_brier,
            -r.step,  # prefer earlier on ties
        ),
    )


def _gap_paragraph(best: CheckpointRecord) -> str:
    failing = [name for name, score in best.by_stratum.items() if not score.qualifies]
    passing = [name for name, score in best.by_stratum.items() if score.qualifies]
    if not failing:
        return (
            "At the best checkpoint every stratum qualifies; the gap to a "
            "persistent window is temporal persistence, not a stratum shortfall."
        )
    details = []
    for name in failing:
        score = best.by_stratum[name]
        need = ACCURACY_MINIMUM[name]
        reasons = []
        if score.correct < need:
            reasons.append(f"correct {score.correct}/{need} (of {score.count})")
        if score.abstentions > 2:
            reasons.append(f"abstentions {score.abstentions}>2")
        lie_cap = 0 if name == "S4" else 1
        if score.confident_lies > lie_cap:
            reasons.append(f"confident_lies {score.confident_lies}>{lie_cap}")
        if score.brier > 0.10:
            reasons.append(f"brier {score.brier:.4f}>0.10")
        details.append(f"{name}[{', '.join(reasons)}]")
    if len(failing) == 1 and len(passing) >= 3:
        return (
            f"Near-miss regime: at best step {best.step}, "
            f"{len(passing)}/5 strata qualify and the binding constraint is "
            f"{details[0]}; the other strata clear the frozen floor."
        )
    return (
        f"Broad shortfall: at best step {best.step}, only {len(passing)}/5 "
        f"strata qualify ({', '.join(passing) if passing else 'none'}). "
        f"Failing: {'; '.join(details)}. This matches a v2-like "
        f"no-persistent-window competence regime rather than a single-stratum miss."
    )


def run_diagnostic() -> str:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA required for D0.1b1 competence diagnostic")

    runner.patch_contact_transformer_device_guard()
    started_wall = time.perf_counter()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel, panel_partition = _build_dev_panel(public_key)
    if panel_partition.reserved is not partition.reserved:
        # Same public key => identical partition object contents.
        pass
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted from frozen PANEL_SIZE")

    # Disjointness: panel cells must not intersect acquisition (frozen verify).
    acquisition_cells = set(partition.acquisition)
    panel_cells = {item.cell for item in panel.items if item.zone == 2}
    if panel_cells & acquisition_cells:
        raise RuntimeError("panel reserved cells intersect acquisition")
    for item in panel.items:
        if item.cell in acquisition_cells:
            raise RuntimeError("panel used an acquisition cell")

    schedule = random_static_schedule(public_key, partition)
    if len(schedule) != BUDGET:
        raise RuntimeError("RANDOM-STATIC schedule length != BUDGET")

    models, _ = _committee(public_key, block=WORLD_SLOT)
    models = [model.to(DEVICE) for model in models]
    optimizers = [build_optimizer(model) for model in models]
    capability = feasibility_v2_capability()
    capability.claim_development_world(WORLD_SLOT)

    history_tokens = torch.empty((BUDGET, MODEL_INPUT_LENGTH), dtype=torch.long)
    history_labels_t = torch.empty((BUDGET,), dtype=torch.long)
    training_pairs: set[tuple[bytes, bytes]] = set()
    records: list[CheckpointRecord] = []
    qualifying: dict[int, bool] = {}

    def record_checkpoint(step: int) -> None:
        rec = _score_panel(models, panel)
        rec = CheckpointRecord(
            step=step,
            qualifies=rec.qualifies,
            by_stratum=rec.by_stratum,
            n_strata_ok=rec.n_strata_ok,
            total_correct=rec.total_correct,
            total_abstentions=rec.total_abstentions,
            total_confident_lies=rec.total_confident_lies,
            mean_brier=rec.mean_brier,
        )
        records.append(rec)
        qualifying[step] = rec.qualifies
        print(
            f"checkpoint step={step}: qualifies={rec.qualifies} "
            f"strata_ok={rec.n_strata_ok}/5 correct={rec.total_correct} "
            f"abst={rec.total_abstentions} lies={rec.total_confident_lies}",
            flush=True,
        )

    # Step 0: pre-training panel score (required by first_persistent_step grid).
    record_checkpoint(0)

    for step, pool_index in enumerate(schedule, start=1):
        raw = realize_pool_index(partition, public_key, pool_index)
        training_pairs.add((raw.left, raw.right))
        history_tokens[step - 1] = encode_pair(raw.left, raw.right)
        history_labels_t[step - 1] = int(oracle_eq(raw.left, raw.right, MODULUS))

        loss_result, _loss_vals = runner.memory_safe_feasibility_committee_step(
            models,
            optimizers,
            history_tokens[:step],
            history_labels_t[:step],
            capability,
            microbatch=MICROBATCH,
        )
        parameters_finite = all(
            bool(torch.isfinite(parameter).all())
            for model in models
            for parameter in model.parameters()
        )
        if not (loss_result.finite and parameters_finite):
            raise RuntimeError(f"non-finite learner state at step={step}")

        if step % CHECKPOINT_CADENCE == 0:
            torch.cuda.empty_cache()
            record_checkpoint(step)
            elapsed = time.perf_counter() - started_wall
            print(
                f"progress step={step}/{BUDGET} wall={elapsed/60.0:.1f} min "
                f"peak_vram_gb={torch.cuda.max_memory_allocated()/1024**3:.2f}",
                flush=True,
            )
            torch.cuda.reset_peak_memory_stats()
        elif step % 25 == 0:
            torch.cuda.empty_cache()

    wall_seconds = time.perf_counter() - started_wall

    panel_pairs = {(item.left, item.right) for item in panel.items}
    pair_overlap = training_pairs & panel_pairs
    cell_overlap_ok = not any(item.cell in acquisition_cells for item in panel.items)

    persistent = first_persistent_step(qualifying)
    longest_len, longest_start, longest_end = _longest_qualifying_run(qualifying)
    best = _pick_best(records)

    # Learner config (frozen ContactTransformer + build_optimizer).
    learner_lines = [
        f"- architecture: ContactTransformer d_model={D_MODEL}, "
        f"heads={MODEL_HEADS}, layers={LAYERS}, mlp={MLP_WIDTH}, "
        f"vocab={VOCAB_SIZE}, dtype={DTYPE}, input_len={MODEL_INPUT_LENGTH}",
        "- committee: 4 members (replicate=1, members 0..3), block=world_slot",
        "- objective: full-history mean cross-entropy (memory-safe sequential "
        f"+ microbatch={MICROBATCH} size-weighted accumulation on CUDA)",
        "- optimizer: AdamW lr=1e-3 betas=(0.9, 0.98) eps=1e-8; "
        "weight_decay=0.01 on attention/MLP/head_W, 0.0 on embeddings/LN/biases",
        f"- budget B={BUDGET}, checkpoint every {CHECKPOINT_CADENCE}, "
        f"persistence window={PERSISTENCE_CHECKPOINTS} checkpoints",
        f"- device: {torch.cuda.get_device_name(0)}; torch={torch.__version__}",
    ]

    best_rows = []
    for name in PANEL_STRATUM_COUNTS:
        score = best.by_stratum[name]
        need = ACCURACY_MINIMUM[name]
        best_rows.append(
            f"| {name} | {score.correct}/{need} (of {score.count}) | "
            f"{score.abstentions} | {score.confident_lies} | "
            f"{score.brier:.6f} | {score.qualifies} |"
        )

    qualifying_steps = [step for step, ok in sorted(qualifying.items()) if ok]
    gap = _gap_paragraph(best)

    lines = [
        "# COMPETENCE_DIAG_01",
        "",
        "NON-CITABLE engineering competence diagnostic only.",
        "No confirmatory datum. Dev world only. Floor/scoring/panel/config "
        "reused verbatim from src/philosophia/level1; no src/ edits.",
        "",
        f"env: torch={torch.__version__}; device={torch.cuda.get_device_name(0)}; "
        f"cuda_available=True.",
        "",
        "## Dev world",
        "",
        f"- family: RANDOM-STATIC",
        f"- modulus: {MODULUS}",
        f"- world_slot / pair_slot: {WORLD_SLOT}",
        f"- public-root key label: `{DEV_PUBLIC_LABEL}` "
        f"(dummy_key SHA256 material; test_only)",
        f"- panel key label: `{DEV_PANEL_LABEL}` purpose=`panel`",
        f"- schedule: `random_static_schedule` length {len(schedule)} "
        f"(sample_without_replacement over flat pool)",
        "",
        "## Learner config",
        "",
        *learner_lines,
        "",
        "## Panel ⊥ training disjointness",
        "",
        "`partition_cells(public_key)` splits every difference-class cell set "
        "into reserved (~30%) and acquisition (remainder). Training pairs are "
        "realized only from `partition.acquisition` via `realize_pool_index`. "
        "The held-out panel (`DummyPanelBuilder`) draws zone-2 cells exclusively "
        "from `partition.reserved` (and constructs zone-3 S4/edge cells outside "
        "the acquisition set). Frozen `verify_dummy_panel` rejects any panel "
        "item whose cell lies in acquisition. "
        f"This run: acquisition∩panel_cells empty = {cell_overlap_ok}; "
        f"realized training word-pair ∩ panel word-pair size = {len(pair_overlap)} "
        f"(must be 0); panel size = {len(panel.items)} (frozen {PANEL_SIZE}).",
        "",
        f"Wall-clock: {wall_seconds:.1f} s ({wall_seconds/3600.0:.2f} h).",
        "",
        "## Persistence against frozen floor",
        "",
        f"- `first_persistent_step(...)` = `{persistent!r}`",
        f"- longest consecutive qualifying checkpoints = {longest_len}"
        + (
            f" (steps {longest_start}..{longest_end})"
            if longest_len > 0
            else " (none)"
        ),
        f"- qualifying checkpoints: {qualifying_steps if qualifying_steps else 'none'}",
        f"- persistence requires {PERSISTENCE_CHECKPOINTS} consecutive "
        f"cadence hits; cadence grid = 0..{BUDGET} step {CHECKPOINT_CADENCE}.",
        "",
        f"## Best checkpoint (step {best.step})",
        "",
        f"qualifies_overall={best.qualifies}; strata_ok={best.n_strata_ok}/5; "
        f"total_correct={best.total_correct}; abstentions={best.total_abstentions}; "
        f"confident_lies={best.total_confident_lies}; mean_brier={best.mean_brier:.6f}.",
        "",
        "| stratum | correct/expected | abstentions | confident_lies | brier | qualifies |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
        *best_rows,
        "",
        "ACCURACY_MINIMUM (frozen): "
        + ", ".join(f"{k}≥{v}" for k, v in ACCURACY_MINIMUM.items())
        + ".",
        "",
        "## Gap paragraph",
        "",
        gap,
        "",
        "## Checkpoint strip (qualifies)",
        "",
        "| step | qualifies | strata_ok | correct | abst | lies | mean_brier |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rec in records:
        lines.append(
            f"| {rec.step} | {rec.qualifies} | {rec.n_strata_ok} | "
            f"{rec.total_correct} | {rec.total_abstentions} | "
            f"{rec.total_confident_lies} | {rec.mean_brier:.4f} |"
        )
    lines.append("")
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    report = run_diagnostic()
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
