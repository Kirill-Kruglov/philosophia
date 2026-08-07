"""NON-CITABLE CAPACITY_DIAG_04: rich curated equal contact vs DIAG_02 floor.

Dev world only. No confirmatory datum. No src/ edits.
ONE change vs competence_diag_02: STATIC curated acquisition schedule with rich
distinct equal pairs (multi-road where pool allows), interleaved with unequals.
Keeps class-balanced weighted CE, B=2000, cadence 50, same arch/optimizer/keys.
Adds cheap train-stream p_equal probes + one final weight dump.
Writes successor/dev/CAPACITY_DIAG_04.md.
"""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
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
    POOL_MULTIPLICITY,
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
    VOCAB_SIZE,
    build_optimizer,
    committee_equal_probability,
    encode_pair,
)
from philosophia.level1.panel import DummyPanel, DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    PoolPartition,
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
from philosophia.level1.serialization import (  # noqa: E402
    CounterStream,
    DeterministicKey,
    dummy_key,
    sample_without_replacement,
    shuffled,
)
from philosophia.level1.world import fold, oracle_eq  # noqa: E402

import gpu_committee_runner as runner  # noqa: E402

OUT_MD = _DEV / "CAPACITY_DIAG_04.md"
OUT_CKPT = _DEV / "capacity_diag_04_final.pt"
OUT_PROGRESS = _DEV / "capacity_diag_04_progress.json"
MODULUS = 66
WORLD_SLOT = 0
# Same world/seeds as DIAG_01/02 — only the schedule construction differs.
DEV_PUBLIC_LABEL = "successor-dev-competence-diag-01"
DEV_PANEL_LABEL = "successor-dev-competence-diag-01"
MICROBATCH = 128
DEVICE = torch.device("cuda")

# CONTACT_DIAG_03 passive reference (RANDOM-STATIC).
_PASSIVE_DISTINCT_EQUALS = 43
_PASSIVE_RESIDUES = 31
_PASSIVE_MULTI_ROAD = 9


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
    p_equal_by_stratum_truth: dict[str, dict[str, float | None]]
    train_p_eq: float | None
    train_p_neq: float | None
    train_n_eq: int
    train_n_neq: int


def _build_dev_panel(public_key) -> tuple[DummyPanel, object]:
    panel_key = dummy_key(DEV_PANEL_LABEL, purpose="panel")
    builder = DummyPanelBuilder(public_key, panel_key)
    panel = builder.build(MODULUS, world_slot=WORLD_SLOT)
    return panel, builder.partition


def _mean_or_none(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def _pair_key(left: bytes, right: bytes) -> tuple[bytes, bytes]:
    return (left, right)


def _element(left: bytes, right: bytes) -> int:
    el = fold(left, MODULUS)
    er = fold(right, MODULUS)
    if el != er:
        raise ValueError("not an equal pair")
    return el


def _inventory_pool_indices(
    public_key: DeterministicKey,
    partition: PoolPartition,
) -> tuple[list[int], list[int], dict[int, list[int]]]:
    """Split flat acquisition indices into equal / unequal; group equals by residue."""
    equal_indices: list[int] = []
    unequal_indices: list[int] = []
    by_residue: dict[int, list[int]] = defaultdict(list)
    for pool_index in range(partition.flat_pool_size):
        cell = partition.acquisition[pool_index // POOL_MULTIPLICITY]
        if cell.difference % MODULUS == 0:
            equal_indices.append(pool_index)
            raw = realize_pool_index(partition, public_key, pool_index)
            if not oracle_eq(raw.left, raw.right, MODULUS):
                raise RuntimeError("equal-cell realization failed oracle_eq")
            by_residue[_element(raw.left, raw.right)].append(pool_index)
        else:
            unequal_indices.append(pool_index)
    return equal_indices, unequal_indices, dict(by_residue)


def curated_rich_equal_schedule(
    public_key: DeterministicKey,
    partition: PoolPartition,
) -> tuple[int, ...]:
    """STATIC curated schedule: ALL acquisition equals + filled unequals, shuffled.

    Maximizes distinct equal contact and multi-road residue coverage from the
    frozen acquisition pool. Not active selection — fixed before training.
    """
    equal_indices, unequal_indices, by_residue = _inventory_pool_indices(
        public_key, partition
    )
    if len(equal_indices) >= BUDGET:
        raise RuntimeError("equal inventory alone exceeds BUDGET; revise curation")
    n_neq = BUDGET - len(equal_indices)
    stream = CounterStream(public_key, ("L1", "capacity-diag-04", "curated"))
    selected_neq = sample_without_replacement(unequal_indices, n_neq, stream)
    combined = list(equal_indices) + list(selected_neq)
    if len(combined) != BUDGET:
        raise RuntimeError("curated schedule length != BUDGET")
    # Prefer multi-road residues first in reporting; shuffle for interleave.
    _ = by_residue  # used by contact scan after realize
    return tuple(shuffled(combined, stream))


def _scan_schedule_contact(
    public_key: DeterministicKey,
    partition: PoolPartition,
    schedule: Sequence[int],
) -> dict:
    seen_distinct: set[tuple[bytes, bytes]] = set()
    total_equal_draws = 0
    distinct_at_step: dict[int, int] = {0: 0}
    total_equal_at_step: dict[int, int] = {0: 0}
    element_pair_count: dict[int, int] = {}
    training_pairs: set[tuple[bytes, bytes]] = set()

    for step, pool_index in enumerate(schedule, start=1):
        raw = realize_pool_index(partition, public_key, pool_index)
        training_pairs.add(_pair_key(raw.left, raw.right))
        if oracle_eq(raw.left, raw.right, MODULUS):
            total_equal_draws += 1
            key = _pair_key(raw.left, raw.right)
            if key not in seen_distinct:
                seen_distinct.add(key)
                el = _element(raw.left, raw.right)
                element_pair_count[el] = element_pair_count.get(el, 0) + 1
        distinct_at_step[step] = len(seen_distinct)
        total_equal_at_step[step] = total_equal_draws

    multi_road = sum(1 for c in element_pair_count.values() if c >= 2)
    return {
        "seen_distinct": seen_distinct,
        "total_equal_draws": total_equal_draws,
        "distinct_at_step": distinct_at_step,
        "total_equal_at_step": total_equal_at_step,
        "element_pair_count": element_pair_count,
        "n_residues": len(element_pair_count),
        "n_multi_road": multi_road,
        "training_pairs": training_pairs,
    }


def _score_panel(models, panel: DummyPanel) -> tuple[
    bool,
    dict[str, StratumScore],
    int,
    int,
    int,
    int,
    float,
    dict[str, dict[str, float | None]],
]:
    tokens = torch.stack(
        [encode_pair(item.left, item.right).to(DEVICE) for item in panel.items]
    )
    truths = [bool(oracle_eq(item.left, item.right, MODULUS)) for item in panel.items]
    if any(truth != item.truth for truth, item in zip(truths, panel.items)):
        raise RuntimeError("oracle_eq disagrees with panel.truth")

    probabilities = committee_equal_probability(models, tokens)
    observations = [
        PanelObservation(item.stratum, item.truth, float(probability))
        for item, probability in zip(panel.items, probabilities, strict=True)
    ]
    by_stratum: dict[str, StratumScore] = {}
    p_map: dict[str, dict[str, float | None]] = {}
    for name in PANEL_STRATUM_COUNTS:
        values = [obs for obs in observations if obs.stratum == name]
        by_stratum[name] = score_stratum(name, values)
        eq_ps = [obs.p_equal for obs in values if obs.truth]
        neq_ps = [obs.p_equal for obs in values if not obs.truth]
        p_map[name] = {"eq": _mean_or_none(eq_ps), "neq": _mean_or_none(neq_ps)}

    qualifies = checkpoint_qualifies(observations)
    return (
        qualifies,
        by_stratum,
        sum(1 for score in by_stratum.values() if score.qualifies),
        sum(score.correct for score in by_stratum.values()),
        sum(score.abstentions for score in by_stratum.values()),
        sum(score.confident_lies for score in by_stratum.values()),
        sum(score.brier for score in by_stratum.values()) / len(by_stratum),
        p_map,
    )


def _train_stream_probe(
    models,
    history_tokens: torch.Tensor,
    history_labels: torch.Tensor,
    n: int,
) -> tuple[float | None, float | None, int, int]:
    """Mean committee p_equal on train equals vs unequals seen so far."""
    if n <= 0:
        return None, None, 0, 0
    tokens = history_tokens[:n].to(DEVICE)
    labels = history_labels[:n]
    with torch.no_grad():
        probs = committee_equal_probability(models, tokens).detach().cpu()
    eq_mask = labels == 1
    neq_mask = labels == 0
    n_eq = int(eq_mask.sum().item())
    n_neq = int(neq_mask.sum().item())
    p_eq = float(probs[eq_mask].mean().item()) if n_eq else None
    p_neq = float(probs[neq_mask].mean().item()) if n_neq else None
    return p_eq, p_neq, n_eq, n_neq


def _longest_qualifying_run(
    qualifying: dict[int, bool],
) -> tuple[int, int | None, int | None]:
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
            -r.step,
        ),
    )


def _fmt_p(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.4f}"


def _verdict_paragraph(
    best: CheckpointRecord,
    records: Sequence[CheckpointRecord],
    persistent: int | None,
    contact: dict,
) -> tuple[str, str]:
    """Return (tag, paragraph) for CAPACITY / GENERALIZATION / FAIL."""
    # Train separation: any late checkpoint with train_p_eq >> train_p_neq.
    late = [r for r in records if r.step >= 500]
    train_sep = any(
        r.train_p_eq is not None
        and r.train_p_neq is not None
        and r.train_p_eq > r.train_p_neq + 0.15
        for r in late
    )
    # Stronger: last checkpoint
    last = records[-1]
    last_train_sep = (
        last.train_p_eq is not None
        and last.train_p_neq is not None
        and last.train_p_eq > last.train_p_neq + 0.15
    )
    train_sep = train_sep or last_train_sep

    # Panel separation: S2–S5 mean p_eq > p_neq with some margin, or strata qualify.
    s2_s5 = ["S2", "S3", "S4", "S5"]
    panel_sep = False
    for name in s2_s5:
        pm = best.p_equal_by_stratum_truth[name]
        if (
            pm["eq"] is not None
            and pm["neq"] is not None
            and pm["eq"] > pm["neq"] + 0.15
        ):
            panel_sep = True
            break
    panel_floor = best.n_strata_ok >= 3 or (
        persistent is not None
    ) or all(best.by_stratum[n].correct > 8 for n in s2_s5)

    if train_sep and (panel_sep or panel_floor or best.n_strata_ok == 5):
        tag = "CAPACITY-SUFFICIENT"
        body = (
            f"CAPACITY-SUFFICIENT: with rich curated contact "
            f"({contact['total_equal_draws']} equal draws, "
            f"{len(contact['seen_distinct'])} distinct equals, "
            f"{contact['n_residues']} residues, "
            f"{contact['n_multi_road']} multi-road), the model separates "
            f"train equals (last train p_eq={_fmt_p(last.train_p_eq)} vs "
            f"p_neq={_fmt_p(last.train_p_neq)}) and generalizes to the held-out "
            f"panel (best step {best.step}: strata_ok={best.n_strata_ok}/5, "
            f"first_persistent_step={persistent!r}). "
            f"CONTACT_DIAG_03 starvation was the blocker, not capacity."
        )
    elif train_sep and not panel_sep and best.n_strata_ok <= 1:
        tag = "GENERALIZATION-FAIL"
        body = (
            f"GENERALIZATION-FAIL: under rich contact the model separates on the "
            f"train stream (last p_eq={_fmt_p(last.train_p_eq)} vs "
            f"p_neq={_fmt_p(last.train_p_neq)}) but fails panel / unseen residues "
            f"(best strata_ok={best.n_strata_ok}/5, S2–S5 still weak; "
            f"first_persistent_step={persistent!r}). Suggests memorization of "
            f"seen equal pairs rather than learning the reduction."
        )
    else:
        tag = "CAPACITY-FAIL"
        body = (
            f"CAPACITY-FAIL: even with rich curated equal contact "
            f"({len(contact['seen_distinct'])} distinct equals / "
            f"{contact['n_residues']} residues / {contact['n_multi_road']} "
            f"multi-road vs passive "
            f"{_PASSIVE_DISTINCT_EQUALS}/{_PASSIVE_RESIDUES}/"
            f"{_PASSIVE_MULTI_ROAD}), the model never cleanly separates "
            f"train equals from unequals "
            f"(last train p_eq={_fmt_p(last.train_p_eq)} vs "
            f"p_neq={_fmt_p(last.train_p_neq)}); "
            f"panel strata_ok={best.n_strata_ok}/5; "
            f"first_persistent_step={persistent!r}. "
            f"Architecture/objective too weak for the equality relation "
            f"under this floor — not merely contact starvation."
        )
    return tag, body


def run_diagnostic() -> str:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA required for CAPACITY_DIAG_04")

    runner.patch_contact_transformer_device_guard()
    started_wall = time.perf_counter()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel, _panel_partition = _build_dev_panel(public_key)
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted from frozen PANEL_SIZE")

    acquisition_cells = set(partition.acquisition)
    panel_cells = {item.cell for item in panel.items if item.zone == 2}
    if panel_cells & acquisition_cells:
        raise RuntimeError("panel reserved cells intersect acquisition")
    for item in panel.items:
        if item.cell in acquisition_cells:
            raise RuntimeError("panel used an acquisition cell")

    # Passive schedule only for contrast counts (not trained).
    passive_schedule = random_static_schedule(public_key, partition)
    schedule = curated_rich_equal_schedule(public_key, partition)
    if len(schedule) != BUDGET:
        raise RuntimeError("curated schedule length != BUDGET")

    print("scanning curated schedule contact...", flush=True)
    contact = _scan_schedule_contact(public_key, partition, schedule)
    print(
        f"curated: equal_draws={contact['total_equal_draws']} "
        f"distinct={len(contact['seen_distinct'])} "
        f"residues={contact['n_residues']} "
        f"multi_road={contact['n_multi_road']}",
        flush=True,
    )

    panel_pairs = {(item.left, item.right) for item in panel.items}
    pair_overlap = contact["training_pairs"] & panel_pairs
    if pair_overlap:
        raise RuntimeError(
            f"panel⊥training violated: {len(pair_overlap)} overlapping pairs"
        )

    models, _ = _committee(public_key, block=WORLD_SLOT)
    models = [model.to(DEVICE) for model in models]
    optimizers = [build_optimizer(model) for model in models]
    capability = feasibility_v2_capability()
    capability.claim_development_world(WORLD_SLOT)

    history_tokens = torch.empty((BUDGET, MODEL_INPUT_LENGTH), dtype=torch.long)
    history_labels_t = torch.empty((BUDGET,), dtype=torch.long)
    records: list[CheckpointRecord] = []
    qualifying: dict[int, bool] = {}

    def record_checkpoint(step: int) -> None:
        (
            qualifies,
            by_stratum,
            n_ok,
            total_correct,
            total_abst,
            total_lies,
            mean_brier,
            p_map,
        ) = _score_panel(models, panel)
        train_p_eq, train_p_neq, train_n_eq, train_n_neq = _train_stream_probe(
            models, history_tokens, history_labels_t, step
        )
        rec = CheckpointRecord(
            step=step,
            qualifies=qualifies,
            by_stratum=by_stratum,
            n_strata_ok=n_ok,
            total_correct=total_correct,
            total_abstentions=total_abst,
            total_confident_lies=total_lies,
            mean_brier=mean_brier,
            p_equal_by_stratum_truth=p_map,
            train_p_eq=train_p_eq,
            train_p_neq=train_p_neq,
            train_n_eq=train_n_eq,
            train_n_neq=train_n_neq,
        )
        records.append(rec)
        qualifying[step] = rec.qualifies
        p2 = rec.p_equal_by_stratum_truth["S2"]
        print(
            f"checkpoint step={step}: qualifies={rec.qualifies} "
            f"strata_ok={rec.n_strata_ok}/5 correct={rec.total_correct} "
            f"train_p(eq/neq)={_fmt_p(rec.train_p_eq)}/{_fmt_p(rec.train_p_neq)} "
            f"S2_p(eq/neq)={_fmt_p(p2['eq'])}/{_fmt_p(p2['neq'])}",
            flush=True,
        )
        # Lightweight progress dump for crash recovery of metrics.
        progress = {
            "step": step,
            "qualifies": rec.qualifies,
            "strata_ok": rec.n_strata_ok,
            "train_p_eq": rec.train_p_eq,
            "train_p_neq": rec.train_p_neq,
            "wall_s": time.perf_counter() - started_wall,
        }
        OUT_PROGRESS.write_text(json.dumps(progress), encoding="utf-8")

    record_checkpoint(0)

    for step, pool_index in enumerate(schedule, start=1):
        raw = realize_pool_index(partition, public_key, pool_index)
        history_tokens[step - 1] = encode_pair(raw.left, raw.right)
        history_labels_t[step - 1] = int(oracle_eq(raw.left, raw.right, MODULUS))

        loss_result, _loss_vals = (
            runner.memory_safe_class_balanced_feasibility_committee_step(
                models,
                optimizers,
                history_tokens[:step],
                history_labels_t[:step],
                capability,
                microbatch=MICROBATCH,
            )
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

    # Final weight dump (one file).
    torch.save(
        {
            "step": BUDGET,
            "modulus": MODULUS,
            "world_slot": WORLD_SLOT,
            "public_label": DEV_PUBLIC_LABEL,
            "schedule_kind": "curated_rich_equal",
            "models": [m.state_dict() for m in models],
            "train_n_eq": int((history_labels_t == 1).sum().item()),
            "train_n_neq": int((history_labels_t == 0).sum().item()),
        },
        OUT_CKPT,
    )
    print(f"wrote checkpoint {OUT_CKPT}", flush=True)

    cell_overlap_ok = not any(item.cell in acquisition_cells for item in panel.items)
    persistent = first_persistent_step(qualifying)
    longest_len, longest_start, longest_end = _longest_qualifying_run(qualifying)
    best = _pick_best(records)
    verdict_tag, verdict_body = _verdict_paragraph(
        best, records, persistent, contact
    )

    # Contact curve at cadence.
    curve_rows = []
    for step in range(0, BUDGET + 1, CHECKPOINT_CADENCE):
        curve_rows.append(
            f"| {step} | {contact['distinct_at_step'][step]} | "
            f"{contact['total_equal_at_step'][step]} |"
        )

    learner_lines = [
        f"- architecture: ContactTransformer d_model={D_MODEL}, "
        f"heads={MODEL_HEADS}, layers={LAYERS}, mlp={MLP_WIDTH}, "
        f"vocab={VOCAB_SIZE}, dtype={DTYPE}, input_len={MODEL_INPUT_LENGTH}",
        "- committee: 4 members (replicate=1, members 0..3), block=world_slot",
        "- objective: CLASS-BALANCED weighted full-history mean CE "
        "(w_i=0.5/freq(class_i); loss=Σ w_i·CE_i / Σ w_i); "
        f"memory-safe sequential + microbatch={MICROBATCH} on CUDA",
        "- optimizer: AdamW lr=1e-3 betas=(0.9, 0.98) eps=1e-8; "
        "weight_decay=0.01 on attention/MLP/head_W, 0.0 on embeddings/LN/biases",
        f"- budget B={BUDGET}, checkpoint every {CHECKPOINT_CADENCE}, "
        f"persistence window={PERSISTENCE_CHECKPOINTS} checkpoints",
        f"- device: {torch.cuda.get_device_name(0)}; torch={torch.__version__}",
        "- config diff vs DIAG_02: ONLY the training schedule "
        "(random_static_schedule → curated STATIC rich-equal schedule from "
        "acquisition equals + interleaved unequals). Loss/arch/keys/panel "
        "unchanged. Plus train-stream p_equal probes and one final ckpt dump.",
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

    p_header = (
        "| step | "
        + " | ".join(f"{s}_eq | {s}_neq" for s in PANEL_STRATUM_COUNTS)
        + " |"
    )
    p_sep = (
        "| ---: | "
        + " | ".join("---: | ---:" for _ in PANEL_STRATUM_COUNTS)
        + " |"
    )

    residue_list = sorted(contact["element_pair_count"])
    multi_list = sorted(
        e for e, c in contact["element_pair_count"].items() if c >= 2
    )

    lines = [
        "# CAPACITY_DIAG_04",
        "",
        "NON-CITABLE capacity diagnostic only. No confirmatory datum.",
        "Dev world only. Floor/scoring/panel/config reused verbatim; no src/ edits.",
        "Purpose: with RICH curated equal contact (static, not active), can THIS "
        "model learn equality and generalize to the held-out panel?",
        "",
        f"env: torch={torch.__version__}; device={torch.cuda.get_device_name(0)}; "
        f"cuda_available=True.",
        "",
        "## Dev world",
        "",
        f"- family: CURATED-STATIC rich-equal (vs DIAG_02 RANDOM-STATIC)",
        f"- modulus: {MODULUS}",
        f"- world_slot / pair_slot: {WORLD_SLOT}",
        f"- public-root key label: `{DEV_PUBLIC_LABEL}` "
        f"(same as DIAG_01/02; dummy_key SHA256 material; test_only)",
        f"- panel key label: `{DEV_PANEL_LABEL}` purpose=`panel`",
        f"- schedule: curated length {len(schedule)} — ALL acquisition equal "
        f"pool indices ({contact['total_equal_draws']}) + "
        f"{BUDGET - contact['total_equal_draws']} unequals, deterministic "
        f"shuffle via CounterStream(`capacity-diag-04`/`curated`)",
        f"- passive RANDOM-STATIC (contrast only, not trained): "
        f"len={len(passive_schedule)}",
        "",
        "## Learner config",
        "",
        *learner_lines,
        "",
        "## 1. Distinct-equals-seen curve (curated vs passive)",
        "",
        f"- Curated: equal draws **{contact['total_equal_draws']}** / {BUDGET} "
        f"({100.0 * contact['total_equal_draws'] / BUDGET:.2f}%); "
        f"distinct equals **{len(contact['seen_distinct'])}**; "
        f"residues **{contact['n_residues']}**; "
        f"multi-road (≥2 distinct pairs/residue) **{contact['n_multi_road']}**.",
        f"- Passive (CONTACT_DIAG_03): {_PASSIVE_DISTINCT_EQUALS} distinct / "
        f"{_PASSIVE_RESIDUES} residues / {_PASSIVE_MULTI_ROAD} multi-road.",
        f"- Residues contacted: {residue_list}",
        f"- Multi-road residues: {multi_list}",
        "",
        "| step | distinct equals seen | cumulative equal draws |",
        "| ---: | ---: | ---: |",
        *curve_rows,
        "",
        "## Panel ⊥ training disjointness",
        "",
        "Training draws only from `partition.acquisition` via "
        "`realize_pool_index` (panel zone-2 from reserved). "
        f"acquisition∩panel_cells empty = {cell_overlap_ok}; "
        f"training word-pair ∩ panel word-pair size = {len(pair_overlap)} "
        f"(must be 0); panel size = {len(panel.items)} (frozen {PANEL_SIZE}). "
        f"Final checkpoint: `{OUT_CKPT.name}`.",
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
        "## TRAIN-stream separation (mean p_equal)",
        "",
        "Committee mean p_equal on training history equals vs unequals at each "
        "cadence (cheap forward probe; no weight dumps).",
        "",
        "| step | train_n_eq | train_n_neq | train_p_eq | train_p_neq | gap |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rec in records:
        gap = (
            "n/a"
            if rec.train_p_eq is None or rec.train_p_neq is None
            else f"{rec.train_p_eq - rec.train_p_neq:.4f}"
        )
        lines.append(
            f"| {rec.step} | {rec.train_n_eq} | {rec.train_n_neq} | "
            f"{_fmt_p(rec.train_p_eq)} | {_fmt_p(rec.train_p_neq)} | {gap} |"
        )

    lines.extend(
        [
            "",
            "## PANEL mean p_equal by stratum × truth",
            "",
            "Always-≠ collapse ≈ both columns near 0; recovery needs high eq / low neq.",
            "",
            p_header,
            p_sep,
        ]
    )
    for rec in records:
        cells = [str(rec.step)]
        for name in PANEL_STRATUM_COUNTS:
            pm = rec.p_equal_by_stratum_truth[name]
            cells.append(_fmt_p(pm["eq"]))
            cells.append(_fmt_p(pm["neq"]))
        lines.append("| " + " | ".join(cells) + " |")

    lines.extend(
        [
            "",
            "## Checkpoint strip (qualifies)",
            "",
            "| step | qualifies | strata_ok | correct | abst | lies | mean_brier |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for rec in records:
        lines.append(
            f"| {rec.step} | {rec.qualifies} | {rec.n_strata_ok} | "
            f"{rec.total_correct} | {rec.total_abstentions} | "
            f"{rec.total_confident_lies} | {rec.mean_brier:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Verdict",
            "",
            f"**{verdict_tag}**",
            "",
            verdict_body,
            "",
        ]
    )
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
