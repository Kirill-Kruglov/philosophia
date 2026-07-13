from pathlib import Path

from gate_harness.verify_decision import verify_decision


ROOT = Path(__file__).resolve().parents[1]


def test_inherited_primary_decision_is_harness_valid():
    path = ROOT / "inheritance/line12_same_wall/experiment_A/decision.json"
    ok, reasons = verify_decision(path)
    assert ok, reasons


def test_no_stray_root_decision_bypasses_the_admitted_level0_path():
    assert not list((ROOT / "experiments").glob("level_*/decision.json"))
    assert (
        ROOT / "experiments/level_0_grokking/outcomes/decision.json"
    ).is_file()


def test_canonical_results_records_level0_without_programme_inference():
    text = (ROOT / "canonical/RESULTS_CANONICAL.md").read_text(encoding="utf-8")
    assert "VALID — REPRODUCED, PLATFORM ONLY" in text
    assert "## Programme decision" in text
    assert "**OPEN.**" in text
