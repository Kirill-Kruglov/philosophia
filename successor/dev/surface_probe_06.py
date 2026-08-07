"""NON-CITABLE SURFACE_PROBE_06: seen-word vs novel-word held-out equals.

No training. Loads capacity_diag_04_final.pt. Splits panel+reserved held-out
equals by whether either word appeared in ANY training pair.
Writes successor/dev/SURFACE_PROBE_06.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

import torch

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

from philosophia.level1.config import BUDGET, PANEL_SIZE  # noqa: E402
from philosophia.level1.feasibility import _committee  # noqa: E402
from philosophia.level1.model import committee_equal_probability, encode_pair  # noqa: E402
from philosophia.level1.panel import DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_cell,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.scoring import PanelObservation  # noqa: E402
from philosophia.level1.serialization import dummy_key  # noqa: E402
from philosophia.level1.world import oracle_eq  # noqa: E402

import gpu_committee_runner as runner  # noqa: E402
from capacity_diag_04 import (  # noqa: E402
    DEV_PANEL_LABEL,
    DEV_PUBLIC_LABEL,
    MODULUS,
    OUT_CKPT,
    WORLD_SLOT,
    curated_rich_equal_schedule,
    _pair_key,
)

OUT_MD = _DEV / "SURFACE_PROBE_06.md"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _load_committee(ckpt_path: Path):
    blob = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    models, _ = _committee(public_key, block=WORLD_SLOT)
    state_dicts = blob["models"]
    if len(state_dicts) != len(models):
        raise RuntimeError("checkpoint committee size mismatch")
    for model, state in zip(models, state_dicts):
        model.load_state_dict(state)
        model.to(DEVICE)
        model.eval()
    return models, blob


def _collect_train_words_and_pairs(public_key, partition, schedule):
    """All words and pairs appearing in the curated training schedule."""
    train_pairs: set[tuple[bytes, bytes]] = set()
    train_words: set[bytes] = set()
    for pool_index in schedule:
        raw = realize_pool_index(partition, public_key, pool_index)
        train_pairs.add(_pair_key(raw.left, raw.right))
        train_words.add(raw.left)
        train_words.add(raw.right)
    return train_words, train_pairs


def _held_out_equals(public_key, partition, panel, train_pairs):
    panel_pairs = {_pair_key(item.left, item.right) for item in panel.items}
    if train_pairs & panel_pairs:
        raise RuntimeError("panel∩train nonempty")

    specs: list[tuple[bytes, bytes, str]] = []  # left, right, source

    for item in panel.items:
        if not item.truth:
            continue
        if not oracle_eq(item.left, item.right, MODULUS):
            raise RuntimeError("panel truth disagrees with oracle_eq")
        specs.append((item.left, item.right, "panel"))

    for cell in partition.reserved:
        if cell.difference % MODULUS != 0:
            continue
        for left, right in realize_cell(public_key, cell):
            if not oracle_eq(left, right, MODULUS):
                raise RuntimeError("reserved equal-cell failed oracle")
            key = _pair_key(left, right)
            if key in train_pairs or key in panel_pairs:
                continue
            specs.append((left, right, "extra"))

    extra_keys = {_pair_key(a, b) for a, b, src in specs if src == "extra"}
    if extra_keys & panel_pairs:
        raise RuntimeError("extra∩panel nonempty")
    if extra_keys & train_pairs:
        raise RuntimeError("extra∩train nonempty")
    return specs


def _word_bucket(left: bytes, right: bytes, train_words: set[bytes]) -> str:
    left_seen = left in train_words
    right_seen = right in train_words
    if left_seen or right_seen:
        return "SEEN-WORD"
    return "NOVEL-WORD"


def _score(models, specs, train_words):
    if not specs:
        return []
    tokens = torch.stack(
        [encode_pair(left, right).to(DEVICE) for left, right, _ in specs]
    )
    # Micro-chunk if needed for VRAM; 568 is fine.
    with torch.no_grad():
        probs = committee_equal_probability(models, tokens).detach().cpu()
    rows = []
    for (left, right, source), p in zip(specs, probs.tolist()):
        obs = PanelObservation("S2", True, float(p))
        bucket = _word_bucket(left, right, train_words)
        n_seen_sides = int(left in train_words) + int(right in train_words)
        rows.append(
            {
                "source": source,
                "bucket": bucket,
                "n_seen_sides": n_seen_sides,
                "p_equal": float(p),
                "correct": bool(obs.correct),
                "abstains": bool(obs.abstains),
            }
        )
    return rows


def _summarize(rows, bucket: str) -> dict:
    items = [r for r in rows if r["bucket"] == bucket]
    n = len(items)
    if n == 0:
        return {
            "bucket": bucket,
            "n": 0,
            "n_correct": 0,
            "acc": None,
            "mean_p": None,
            "n_panel": 0,
            "n_extra": 0,
            "both_sides_seen": 0,
            "one_side_seen": 0,
        }
    n_correct = sum(1 for r in items if r["correct"])
    return {
        "bucket": bucket,
        "n": n,
        "n_correct": n_correct,
        "acc": n_correct / n,
        "mean_p": sum(r["p_equal"] for r in items) / n,
        "n_panel": sum(1 for r in items if r["source"] == "panel"),
        "n_extra": sum(1 for r in items if r["source"] == "extra"),
        "both_sides_seen": sum(1 for r in items if r["n_seen_sides"] == 2),
        "one_side_seen": sum(1 for r in items if r["n_seen_sides"] == 1),
    }


def _fmt_acc(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{100.0 * value:.1f}%"


def _fmt_p(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.4f}"


def _verdict(seen: dict, novel: dict) -> tuple[str, str]:
    if seen["n"] == 0 or novel["n"] == 0:
        raise RuntimeError("empty SEEN-WORD or NOVEL-WORD bucket")
    # SURFACE-LATCHING if seen substantially beats novel on acc or mean_p.
    acc_gap = seen["acc"] - novel["acc"]
    p_gap = seen["mean_p"] - novel["mean_p"]
    surface = acc_gap >= 0.15 or (p_gap >= 0.15 and acc_gap >= 0.05)
    # Comparable: small gaps.
    comparable = abs(acc_gap) < 0.10 and abs(p_gap) < 0.10

    if surface and not comparable:
        tag = "SURFACE-LATCHING"
        body = (
            f"SURFACE-LATCHING: SEEN-WORD held-out equals "
            f"(n={seen['n']}, acc={_fmt_acc(seen['acc'])}, "
            f"mean p={_fmt_p(seen['mean_p'])}) substantially outperform "
            f"NOVEL-WORD "
            f"(n={novel['n']}, acc={_fmt_acc(novel['acc'])}, "
            f"mean p={_fmt_p(novel['mean_p'])}; "
            f"Δacc={acc_gap:+.3f}, Δp={p_gap:+.3f}). "
            f"The residual ~63% signal is largely token reuse. A gap-closer must "
            f"induce a per-word element (fold) representation from scratch for "
            f"novel words — surface co-occurrence with train tokens will not "
            f"transfer equality to unseen roads."
        )
    else:
        tag = "NOT-PURELY-SURFACE"
        body = (
            f"NOT-PURELY-SURFACE: SEEN-WORD "
            f"(n={seen['n']}, acc={_fmt_acc(seen['acc'])}, "
            f"mean p={_fmt_p(seen['mean_p'])}) and NOVEL-WORD "
            f"(n={novel['n']}, acc={_fmt_acc(novel['acc'])}, "
            f"mean p={_fmt_p(novel['mean_p'])}) are comparable "
            f"(Δacc={acc_gap:+.3f}, Δp={p_gap:+.3f}). "
            f"The weak held-out-equal signal is not explained by token reuse "
            f"alone — some fragile structure already exists for novel words. "
            f"A gap-closer should strengthen that weak per-word element "
            f"representation (make fold equality explicit/robust), not rebuild "
            f"token-latching; more contact of the same kind is unlikely to "
            f"suffice at B=2000."
        )
    return tag, body


def main() -> None:
    if not OUT_CKPT.is_file():
        raise FileNotFoundError(f"missing checkpoint {OUT_CKPT}")

    runner.patch_contact_transformer_device_guard()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(
        public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")
    ).build(MODULUS, world_slot=WORLD_SLOT)
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted")

    print("reconstructing train schedule / word set...", flush=True)
    schedule = curated_rich_equal_schedule(public_key, partition)
    if len(schedule) != BUDGET:
        raise RuntimeError("schedule length != BUDGET")
    train_words, train_pairs = _collect_train_words_and_pairs(
        public_key, partition, schedule
    )
    specs = _held_out_equals(public_key, partition, panel, train_pairs)
    n_panel = sum(1 for _, _, s in specs if s == "panel")
    n_extra = sum(1 for _, _, s in specs if s == "extra")
    print(
        f"held-out equals={len(specs)} (panel={n_panel}, extra={n_extra}); "
        f"train pairs={len(train_pairs)}; train words={len(train_words)}",
        flush=True,
    )

    print(f"loading {OUT_CKPT.name} on {DEVICE}...", flush=True)
    models, blob = _load_committee(OUT_CKPT)

    rows = _score(models, specs, train_words)
    seen = _summarize(rows, "SEEN-WORD")
    novel = _summarize(rows, "NOVEL-WORD")
    verdict_tag, verdict_body = _verdict(seen, novel)

    # Source × bucket crosstab for transparency.
    cross_lines = []
    for source in ("panel", "extra"):
        for bucket in ("SEEN-WORD", "NOVEL-WORD"):
            items = [r for r in rows if r["source"] == source and r["bucket"] == bucket]
            n = len(items)
            if n == 0:
                cross_lines.append(
                    f"| {source} | {bucket} | 0 | 0 | n/a | n/a |"
                )
                continue
            n_ok = sum(1 for r in items if r["correct"])
            cross_lines.append(
                f"| {source} | {bucket} | {n} | {n_ok} | "
                f"{_fmt_acc(n_ok / n)} | "
                f"{_fmt_p(sum(r['p_equal'] for r in items) / n)} |"
            )

    lines = [
        "# SURFACE_PROBE_06",
        "",
        "NON-CITABLE surface-token probe. No training. No src/ edits.",
        "No confirmatory datum. Loads CAPACITY_DIAG_04 final committee only.",
        "",
        f"checkpoint: `{OUT_CKPT.name}` (step={blob.get('step')}, "
        f"schedule={blob.get('schedule_kind')}).",
        f"device: {DEVICE}.",
        "",
        "## Setup",
        "",
        "- Held-out equals = panel equals (32) + reserved extras "
        f"({n_extra}), same construction as GENFAIL_SHAPE_05.",
        "- SEEN-WORD: ≥1 of the two words appears in ANY training pair "
        "(equal or unequal).",
        "- NOVEL-WORD: BOTH words never appear in any training pair.",
        f"- panel∩train pairs = 0; extra∩train = 0; extra∩panel = 0.",
        f"- Train vocabulary: {len(train_words)} distinct words across "
        f"{len(train_pairs)} distinct training pairs.",
        "",
        "## Table (held-out equals)",
        "",
        "| bucket | n | n_correct | accuracy | mean p_equal | "
        "n_panel | n_extra | both_sides_seen | one_side_seen |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| SEEN-WORD (i) | {seen['n']} | {seen['n_correct']} | "
            f"{_fmt_acc(seen['acc'])} | {_fmt_p(seen['mean_p'])} | "
            f"{seen['n_panel']} | {seen['n_extra']} | "
            f"{seen['both_sides_seen']} | {seen['one_side_seen']} |"
        ),
        (
            f"| NOVEL-WORD (ii) | {novel['n']} | {novel['n_correct']} | "
            f"{_fmt_acc(novel['acc'])} | {_fmt_p(novel['mean_p'])} | "
            f"{novel['n_panel']} | {novel['n_extra']} | "
            f"{novel['both_sides_seen']} | {novel['one_side_seen']} |"
        ),
        "",
        "### Source × bucket",
        "",
        "| source | bucket | n | n_correct | accuracy | mean p_equal |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
        *cross_lines,
        "",
        "## Verdict",
        "",
        f"**{verdict_tag}**",
        "",
        verdict_body,
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
