from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"
SOURCE = ROOT / "src/philosophia/level0"


def test_opus_implementation_review_is_preserved() -> None:
    review = (
        ROOT / "reviews/opus_level0_implementation_review.md"
    ).read_text(encoding="utf-8")
    assert "**REVISE_IMPLEMENTATION**" in review
    assert "**J1 —" in review
    assert "**J2 —" in review
    assert "**J3 —" in review
    assert "Eligible only after J1 and J2 land" in review


def test_scout_prerequisites_are_interlocked() -> None:
    interlock = (SOURCE / "interlock.py").read_text(encoding="utf-8")
    checkpoint = (SOURCE / "checkpoint.py").read_text(encoding="utf-8")
    assert "SCOUT_MAX_STEPS = 100" in interlock
    assert "SCOUT_MAX_SECONDS = 120.0" in interlock
    assert "allow_evaluation=False" in interlock
    assert "allow_verdict=False" in interlock
    assert "model_state_hash" in checkpoint
    assert "optimizer_state_hash" in checkpoint
    assert "weights_only=True" in checkpoint


def test_hardening_does_not_create_scientific_authorization() -> None:
    contract = (LEVEL0 / "EXECUTION_INTERLOCK.md").read_text(encoding="utf-8")
    assert "no preregistration lock or outcome" in contract
    assert "contamination boundary" in contract
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()


def test_hardening_acceptance_allows_driver_not_execution() -> None:
    review = (
        ROOT / "reviews/opus_level0_hardening_review.md"
    ).read_text(encoding="utf-8")
    assert review.startswith("# Opus 4.8")
    assert "**HARDENING_ACCEPTED**" in review
    assert "**Eligible.**" in review
    assert "**Not yet — implement the driver" in review
    assert not list(ROOT.glob("**/timing-storage-scout_non-outcome.json"))
