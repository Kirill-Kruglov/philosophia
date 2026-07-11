from pathlib import Path

from gate_harness.verify_decision import verify_decision


ROOT = Path(__file__).resolve().parents[1]


def test_inherited_primary_decision_is_harness_valid():
    path = ROOT / "inheritance/line12_same_wall/experiment_A/decision.json"
    ok, reasons = verify_decision(path)
    assert ok, reasons


def test_no_active_philosophia_decision_exists_at_bootstrap():
    assert not list((ROOT / "experiments").glob("level_*/decision.json"))


def test_canonical_results_state_no_result():
    text = (ROOT / "canonical/RESULTS_CANONICAL.md").read_text(encoding="utf-8")
    assert "NO PHILOSOPHIA RESULT YET" in text
