from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"


def test_companion_trace_pins_every_reopened_cell() -> None:
    trace = (LEVEL0 / "COMPANION_CONFIG_TRACE.md").read_text(encoding="utf-8")
    assert "binding source trace" in trace
    assert "W_K;" in trace
    assert "normal / sqrt(128)" in trace
    assert "random.Random(master_seed)" in trace
    assert "CPython 3.12.3" in trace
    assert "| 0 | 0 | 0.0001 |" in trace
    assert "| 10+ | 0.001 | 0.001 |" in trace
    assert "training loss: logits indices 0..113, 114 classes" in trace
    assert "FIT/GENERALIZE accuracy: residue logits indices 0..112" in trace


def test_v2_addendum_supersedes_only_source_reopened_cells() -> None:
    choices = (LEVEL0 / "RECONSTRUCTION_CHOICES_V2.md").read_text(encoding="utf-8")
    assert "implementation accepted" in choices
    for label in ("R1-v2", "R2-v2", "R4-v2", "R5-v2"):
        assert label in choices
    assert "R3 attention scaling and R6 arm hierarchy are unchanged" in choices


def test_trace_commit_still_cannot_authorize_outcome() -> None:
    review = (
        ROOT / "reviews/opus_level0_companion_source_reconciliation_review.md"
    ).read_text(encoding="utf-8")
    assert "**REVISE_TO_COMPANION**" in review
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()
