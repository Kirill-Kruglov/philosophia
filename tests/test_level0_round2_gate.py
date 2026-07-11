from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"


def test_round1_review_is_preserved_at_key_cracks():
    review = (
        ROOT / "reviews/opus_level0_design_review.md"
    ).read_text(encoding="utf-8")
    assert "**READY_FOR_REVISION**" in review
    assert "**C1 —" in review
    assert "One arm decides grokking" in review
    assert "Cursor may not implement yet" in review


def test_six_reconstruction_choices_are_explicit():
    choices = (LEVEL0 / "RECONSTRUCTION_CHOICES_V1.md").read_text(encoding="utf-8")
    for label in ("R1:", "R2:", "R3:", "R4:", "R5:", "R6:"):
        assert label in choices
    assert "No implementation may expose defaults" in choices


def test_round2_gate_still_forbids_implementation_and_outcome():
    prompt = (
        ROOT / "reviews/opus_level0_choices_round2_prompt.md"
    ).read_text(encoding="utf-8")
    assert "REVISE_CHOICES" in prompt
    assert "No training loop, scout, or" in prompt
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()
