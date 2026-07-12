from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"


def test_companion_source_reopens_trajectory_cells_before_lock() -> None:
    audit = (LEVEL0 / "COMPANION_SOURCE_AUDIT.md").read_text(encoding="utf-8")
    assert "LOCK BLOCKER, NOT AN OUTCOME" in audit
    assert "23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1" in audit
    assert "de946fddb1ec509d662829c6bb1e5b456120a1c5bfb31548cdc66b7650cef6ad" in audit
    for cell in (
        "Initialization",
        "Split",
        "Learning rate",
        "Training CE",
    ):
        assert f"| {cell} |" in audit


def test_source_correction_does_not_silently_change_implementation() -> None:
    choices = (LEVEL0 / "RECONSTRUCTION_CHOICES_V1.md").read_text(encoding="utf-8")
    audit = (LEVEL0 / "COMPANION_SOURCE_AUDIT.md").read_text(encoding="utf-8")
    assert "Xavier" in choices
    assert "torch.randperm" in choices
    assert "Alternative: retain the current implementation" in audit
    assert "Proposed resolution for review" in audit


def test_reconciliation_prompt_forbids_lock_and_outcome() -> None:
    prompt = (
        ROOT / "reviews/opus_level0_companion_source_reconciliation_prompt.md"
    ).read_text(encoding="utf-8")
    assert "REVISE_TO_COMPANION" in prompt
    assert "Do not run a" in prompt
    assert "training trajectory" in prompt
    assert "Do not predict grokking" in prompt
    assert (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()
