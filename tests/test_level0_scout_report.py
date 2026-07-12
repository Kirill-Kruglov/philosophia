import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"
REPORT_PATH = LEVEL0 / "scout/timing-storage-scout_non-outcome.json"


def test_admitted_scout_report_passes_every_execution_guard() -> None:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert report["kind"] == "timing-storage-scout / non-outcome"
    assert report["scientific_outcome"] is False
    assert report["arm"] == "A"
    assert report["master_seed"] == 0
    assert report["device"] == "cpu"
    assert report["dtype"] == "torch.float32"
    assert report["steps"] == {
        "hard_cap": 100,
        "primary": 25,
        "replay": 25,
        "total": 50,
    }
    assert report["wall_seconds"] <= report["wall_hard_cap_seconds"] == 120.0
    assert report["deterministic_prefix"]["match"] is True
    assert (
        report["deterministic_prefix"]["primary_hash"]
        == report["deterministic_prefix"]["replay_hash"]
    )
    assert all(value is False for value in report["contamination_guards"].values())
    assert "non-outcome" in report["checkpoint"]["name"]
    assert report["checkpoint"]["purpose"] == report["kind"]


def test_scout_report_schema_contains_aggregates_not_a_curve() -> None:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert set(report["primary_step_latency"]) == {
        "count",
        "max_ms",
        "mean_ms",
        "median_ms",
        "min_ms",
    }
    assert report["primary_step_latency"]["count"] == 25
    assert not any(key in report for key in ("loss", "accuracy", "observations"))
    assert report["checkpoint"]["bytes"] == 2_740_993
    assert len(report["checkpoint"]["sha256"]) == 64


def test_scout_did_not_authorize_scientific_execution() -> None:
    resource_doc = (LEVEL0 / "RESOURCE_SCOUT.md").read_text(encoding="utf-8")
    assert "planning projections, not runtime guarantees" in resource_doc
    assert "does not inform grokking" in resource_doc
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()
