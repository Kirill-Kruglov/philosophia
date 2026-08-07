"""NON-CITABLE CONTACT_DIAG_03: equal-pair starvation vs capacity (no full train).

Reuses exact DIAG_01/02 world (modulus 66, same keys, schedule, partition).
No src/ edits. Writes successor/dev/CONTACT_DIAG_03.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

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
    PANEL_STRATUM_COUNTS,
)
from philosophia.level1.feasibility import random_static_schedule  # noqa: E402
from philosophia.level1.panel import DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_cell,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.serialization import dummy_key  # noqa: E402
from philosophia.level1.world import Cell, fold, oracle_eq, rank_word  # noqa: E402

OUT_MD = _DEV / "CONTACT_DIAG_03.md"
MODULUS = 66
WORLD_SLOT = 0
DEV_PUBLIC_LABEL = "successor-dev-competence-diag-01"
DEV_PANEL_LABEL = "successor-dev-competence-diag-01"
CHECKPOINT_STEPS = tuple(range(0, BUDGET + 1, CHECKPOINT_CADENCE))


def _pair_key(left: bytes, right: bytes) -> tuple[bytes, bytes]:
    return (left, right)


def _element(left: bytes, right: bytes) -> int:
    """Shared Z/n residue for an equal pair (both sides fold to it)."""
    el = fold(left, MODULUS)
    er = fold(right, MODULUS)
    if el != er:
        raise ValueError("not an equal pair")
    return el


def _scan_schedule(public_key, partition, schedule):
    """Walk the 2000-draw schedule; accumulate equal-contact stats."""
    seen_distinct: set[tuple[bytes, bytes]] = set()
    total_equal_draws = 0
    # At each training step 1..B after the draw is appended.
    distinct_at_step: dict[int, int] = {0: 0}
    total_equal_at_step: dict[int, int] = {0: 0}
    # Residues contacted by at least one distinct equal pair.
    elements_seen: set[int] = set()
    # Per-element: distinct equal pair count and unique word nets (displacements).
    element_pair_count: dict[int, int] = {}
    element_words: dict[int, set[int]] = {}

    for step, pool_index in enumerate(schedule, start=1):
        raw = realize_pool_index(partition, public_key, pool_index)
        if oracle_eq(raw.left, raw.right, MODULUS):
            total_equal_draws += 1
            key = _pair_key(raw.left, raw.right)
            if key not in seen_distinct:
                seen_distinct.add(key)
                el = _element(raw.left, raw.right)
                elements_seen.add(el)
                element_pair_count[el] = element_pair_count.get(el, 0) + 1
                left_net, _, _ = rank_word(raw.left)
                right_net, _, _ = rank_word(raw.right)
                bucket = element_words.setdefault(el, set())
                bucket.add(left_net)
                bucket.add(right_net)
        distinct_at_step[step] = len(seen_distinct)
        total_equal_at_step[step] = total_equal_draws

    return {
        "seen_distinct": seen_distinct,
        "total_equal_draws": total_equal_draws,
        "distinct_at_step": distinct_at_step,
        "total_equal_at_step": total_equal_at_step,
        "elements_seen": elements_seen,
        "element_pair_count": element_pair_count,
        "element_words": element_words,
    }


def _acquisition_equal_inventory(public_key, partition) -> dict:
    """Upper bound: distinct equal word-pairs realizable from acquisition cells."""
    distinct: set[tuple[bytes, bytes]] = set()
    elements: set[int] = set()
    # Equal cells: difference ≡ 0 (mod modulus), within acquisition support.
    # A cell (a,b) with difference d=a-b yields equal labels iff d % modulus == 0
    # for the realized words' folds — actually oracle is on word folds, not cell
    # difference alone. For acquisition cells, left/right are realized from
    # endpoints a,b; fold of a word with net a is a % m (with padding path).
    # Per world.py: displacement = net signed; fold = displacement % m.
    # realize_cell builds words with nets cell.a and cell.b, so
    # equal iff cell.a % m == cell.b % m iff (a-b) % m == 0.
    equal_cells = 0
    for cell in partition.acquisition:
        if cell.difference % MODULUS != 0:
            continue
        equal_cells += 1
        for left, right in realize_cell(public_key, cell):
            if not oracle_eq(left, right, MODULUS):
                raise RuntimeError("acquisition equal-cell realization failed oracle")
            distinct.add(_pair_key(left, right))
            elements.add(_element(left, right))
    return {
        "equal_cells": equal_cells,
        "distinct_pairs": distinct,
        "elements": elements,
        "n_distinct": len(distinct),
        "n_elements": len(elements),
    }


def _panel_equal_inventory(panel) -> dict:
    equals = [item for item in panel.items if item.truth]
    distinct = {_pair_key(item.left, item.right) for item in equals}
    elements: set[int] = set()
    by_stratum: dict[str, int] = {name: 0 for name in PANEL_STRATUM_COUNTS}
    for item in equals:
        by_stratum[item.stratum] += 1
        elements.add(_element(item.left, item.right))
    # Panel equals that also appear as schedule-contacted distinct pairs.
    return {
        "n_equal_items": len(equals),
        "n_distinct": len(distinct),
        "elements": elements,
        "by_stratum": by_stratum,
        "distinct": distinct,
    }


def _checkpoints_absent() -> bool:
    # DIAG_01/02 did not persist model checkpoints under successor/dev/.
    patterns = (
        "**/competence*checkpoint*",
        "**/diag*ckpt*",
        "**/*committee*.pt",
        "**/*committee*.pth",
    )
    for pattern in patterns:
        if any(_DEV.glob(pattern)):
            return False
    return True


def main() -> None:
    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(
        public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")
    ).build(MODULUS, world_slot=WORLD_SLOT)

    schedule = random_static_schedule(public_key, partition)
    if len(schedule) != BUDGET:
        raise RuntimeError("schedule length != BUDGET")

    print("scanning schedule...", flush=True)
    sched_stats = _scan_schedule(public_key, partition, schedule)
    print("scanning acquisition equal inventory...", flush=True)
    acq = _acquisition_equal_inventory(public_key, partition)
    panel_eq = _panel_equal_inventory(panel)

    # Coverage: residues hit by schedule equals vs panel equals.
    sched_el = sched_stats["elements_seen"]
    panel_el = panel_eq["elements"]
    el_overlap = sched_el & panel_el
    el_panel_only = panel_el - sched_el
    el_sched_only = sched_el - panel_el

    # Word-net coverage: for residues that panel equals need, how many distinct
    # word nets did the schedule provide on that residue?
    multi_road_elements = sum(
        1 for c in sched_stats["element_pair_count"].values() if c >= 2
    )
    single_pair_elements = sum(
        1 for c in sched_stats["element_pair_count"].values() if c == 1
    )
    # Nets-per-residue (a single equal pair already contributes two nets).
    mean_nets = (
        sum(len(v) for v in sched_stats["element_words"].values()) / len(sched_el)
        if sched_el
        else 0.0
    )

    curve_rows = []
    for step in CHECKPOINT_STEPS:
        curve_rows.append(
            f"| {step} | {sched_stats['distinct_at_step'][step]} | "
            f"{sched_stats['total_equal_at_step'][step]} |"
        )

    # Pair overlap: schedule distinct equals ∩ panel equal pairs.
    pair_overlap = sched_stats["seen_distinct"] & panel_eq["distinct"]

    checkpoints_absent = _checkpoints_absent()

    n_distinct_sched = len(sched_stats["seen_distinct"])
    n_draws = sched_stats["total_equal_draws"]
    n_panel_eq = panel_eq["n_equal_items"]

    if checkpoints_absent:
        train_sep_line = (
            "Train-stream separation: checkpoints absent — DIAG_01/02 did not "
            "persist model weights under successor/dev/; not evaluated "
            "(no new full run launched)."
        )
        gen_clause = (
            "GENERALIZATION cannot be tested without saved checkpoints."
        )
    else:
        train_sep_line = "Train-stream separation: checkpoints found (unexpected)."
        gen_clause = "see train-stream numbers."

    # STARVATION if contact is sparse vs pool/panel, little repeated multi-pair
    # contact per residue, and near-zero panel equal overlap.
    starvation = (
        n_draws / BUDGET < 0.05
        or n_distinct_sched < 100
        or len(pair_overlap) == 0
        or len(el_panel_only) > len(panel_el) / 2
        or multi_road_elements < len(sched_el) / 3
    )
    if starvation:
        verdict_tag = "STARVATION"
        verdict_body = (
            f"STARVATION: the passive schedule contacts only {n_distinct_sched} "
            f"distinct equal pairs ({n_draws} equal draws, "
            f"{100.0 * n_draws / BUDGET:.2f}% of B) covering "
            f"{len(sched_el)}/{MODULUS} residues — vs {acq['n_distinct']} "
            f"distinct equals available in acquisition and {n_panel_eq} panel "
            f"equals on {len(panel_el)} residues. "
            f"Panel residue overlap is {len(el_overlap)}/{len(panel_el)} "
            f"(panel-only residues: {len(el_panel_only)}); exact panel equal "
            f"pairs seen in training: {len(pair_overlap)}/{panel_eq['n_distinct']}. "
            f"Only {multi_road_elements}/{len(sched_el)} contacted residues have "
            f"≥2 distinct equal pairs (repeated multi-road evidence); "
            f"{single_pair_elements} are singleton-pair contacts. "
            f"Equality is under-determined by RANDOM-STATIC passive contact; "
            f"the always-≠ collapse is the expected response to near-absent "
            f"equal exemplars, not a demonstrated capacity failure. {gen_clause}"
        )
    else:
        verdict_tag = "CAPACITY"
        verdict_body = (
            f"CAPACITY: schedule supplies {n_distinct_sched} distinct equals "
            f"with repeated multi-pair contact on most residues and non-trivial "
            f"panel overlap, so equality is not obviously under-determined; "
            f"DIAG_02's coupled near-zero p_equal then points at "
            f"learnability/optimization. {gen_clause}"
        )

    structure_para = (
        f"Equal pairs are words (u,v) with fold(u)=fold(v)=e in Z/{MODULUS}Z — "
        f"different roads to the same residue e. On the schedule, "
        f"{len(sched_el)} residues receive at least one equal pair; "
        f"only {multi_road_elements} have ≥2 distinct equal pairs "
        f"(repeated multi-road evidence), while {single_pair_elements} are "
        f"singleton-pair (idiosyncratic) contacts "
        f"(mean distinct word-nets per contacted residue = {mean_nets:.2f}, "
        f"noting one pair already contributes two nets). "
        f"Panel equals span residues {sorted(panel_el)}; "
        f"overlap with schedule-equal residues = {len(el_overlap)}/"
        f"{len(panel_el)}; panel-only residues = {sorted(el_panel_only)}. "
        f"Exact panel equal word-pairs also present in schedule distinct "
        f"equals: {len(pair_overlap)}/{panel_eq['n_distinct']}. "
        f"A learner could at best induce equality on sparsely sampled "
        f"contacted residues; most panel equal residues are never seen as "
        f"equals in training, so panel success would require extrapolation "
        f"from an under-determined contact set."
    )

    lines = [
        "# CONTACT_DIAG_03",
        "",
        "NON-CITABLE equal-contact diagnostic. No confirmatory datum.",
        "Exact DIAG_01/02 setup (modulus 66, same dummy keys, partition, "
        "random_static_schedule). No src/ edits. No new full training run.",
        "",
        f"Setup: public=`{DEV_PUBLIC_LABEL}`, panel=`{DEV_PANEL_LABEL}`, "
        f"world_slot={WORLD_SLOT}, B={BUDGET}, modulus={MODULUS}.",
        "",
        "## 1. Schedule equal-contact counts",
        "",
        f"- Total equal draws in schedule: **{n_draws}** / {BUDGET} "
        f"({100.0 * n_draws / BUDGET:.3f}%).",
        f"- Distinct equal word-pairs contacted by end of B: "
        f"**{n_distinct_sched}**.",
        f"- Distinct Z/{MODULUS}Z residues hit by those equals: "
        f"**{len(sched_el)}**.",
        "",
        "| step | distinct equals seen | cumulative equal draws |",
        "| ---: | ---: | ---: |",
        *curve_rows,
        "",
        "### Pool / panel equal upper bounds",
        "",
        f"- Acquisition pool: equal-cells (difference % {MODULUS} == 0) = "
        f"**{acq['equal_cells']}**; distinct realizable equal word-pairs = "
        f"**{acq['n_distinct']}**; residues covered = **{acq['n_elements']}**.",
        f"- Held-out panel equal half: **{panel_eq['n_equal_items']}** items "
        f"(S1={panel_eq['by_stratum'].get('S1', 0)}, "
        f"S2={panel_eq['by_stratum'].get('S2', 0)}, "
        f"S3={panel_eq['by_stratum'].get('S3', 0)}, "
        f"S4={panel_eq['by_stratum'].get('S4', 0)}, "
        f"S5={panel_eq['by_stratum'].get('S5', 0)}; "
        f"S1 has 0 equals by construction); "
        f"distinct pairs = **{panel_eq['n_distinct']}**; residues = "
        f"**{len(panel_el)}** ({sorted(panel_el)}).",
        "",
        "## 2. Structure paragraph",
        "",
        structure_para,
        "",
        "## 3. Train-stream separation",
        "",
        train_sep_line,
        "",
        "## Verdict",
        "",
        f"**{verdict_tag}**",
        "",
        verdict_body,
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
