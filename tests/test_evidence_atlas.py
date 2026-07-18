import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "docs" / "index.html"


def atlas_data() -> dict:
    html = ATLAS.read_text(encoding="utf-8")
    match = re.search(
        r'<script id="evidence-data" type="application/json">\s*(\{.*?\})\s*</script>',
        html,
        flags=re.DOTALL,
    )
    assert match, "embedded evidence JSON is missing"
    return json.loads(match.group(1))


def test_atlas_level0_events_match_canonical_decision() -> None:
    data = atlas_data()
    decision = json.loads(
        (ROOT / "experiments/level_0_grokking/outcomes/decision.json").read_text()
    )
    expected = [
        {
            "run": run_id,
            "fit": decision["runs"][run_id]["fit_start"],
            "generalize": decision["runs"][run_id]["generalize_start"],
            "delay": decision["runs"][run_id]["delay"],
        }
        for run_id in ("A-0", "A-1", "A-2", "A-3", "A-4")
    ]
    assert data["level0"] == expected
    assert decision["runs"]["R-0"]["fit_start"] == 200
    assert decision["runs"]["R-0"]["generalize_start"] is None


def test_atlas_holdout_matrix_matches_escrowed_result() -> None:
    data = atlas_data()
    result = json.loads(
        (
            ROOT
            / "inheritance/line12_same_wall/experiment_A/holdout_result.json"
        ).read_text()
    )
    detail_keys = {
        "H1": "H1_fwd_derived",
        "H2": "H2_rev_derived",
        "H3": "H3_same_prior_diff_mech",
        "H4": "H4_cross_prior_cleanroom",
        "H5": "H5_derived_replication",
    }
    for row in data["holdout"]:
        detail = result["detail"][detail_keys[row["id"]]]
        assert row["token"] == detail["P_tok"]
        assert row["journal"] == detail["P_j"]
        assert row["combined"] == detail["P_union"]
    h4 = next(row for row in data["holdout"] if row["id"] == "H4")
    assert h4["adverse"] is True
    assert h4["token"] == "CLEAN"
    assert h4["journal"] == "DEPENDENT"


def test_atlas_line12_gradient_and_visibility_are_registered() -> None:
    data = atlas_data()
    assert [row["value"] for row in data["gradient"]] == [24, 12, 0]
    assert all(row["total"] == 24 for row in data["gradient"])

    first_contact = (
        ROOT
        / "inheritance/line12_same_wall/experiment_A/integration_first_contact.md"
    ).read_text()
    assert "| A ~ opus-A | 24/24 |" in first_contact
    assert "| A ~ grok | 12/24 |" in first_contact
    assert "| A ~ gemini | 0/24 |" in first_contact

    prereg = (
        ROOT
        / "inheritance/line12_same_wall/experiment_A/PREREG_v4_DRAFT.md"
    ).read_text()
    assert "derived-A 200/200" in prereg
    assert "derived-gem 198/200" in prereg
    assert "derived-gptA 0/200 (0/1200" in prereg


def test_atlas_level1_language_matches_terminal_evidence() -> None:
    report = json.loads(
        (
            ROOT
            / "experiments/level_1_contact/feasibility_v2/"
            "LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json"
        ).read_text()
    )
    trajectory = report["measurements"]["trajectory"]
    assert report["validity"] == "valid-scientific-terminal"
    assert report["scientific_outcome"] is False
    assert trajectory["steps_completed"] == 2000
    assert trajectory["all_losses_finite"] is True
    assert trajectory["all_parameters_finite"] is True
    assert trajectory["panel_computable"] is True
    assert trajectory["censored_at_b"] is True
    assert not any(report["contamination_guards"].values())

    html = ATLAS.read_text(encoding="utf-8")
    required = (
        "BLOCKED_LEVEL1_FEASIBILITY",
        "C1 was never tested",
        "not a negative C1 result",
        "programme remains open",
        "no scientifically admissible\n            learning curve",
    )
    for phrase in required:
        assert phrase in html


def test_atlas_source_manifest_points_to_existing_files() -> None:
    data = atlas_data()
    assert data["sourceCommit"] == "c25bd652611d85133bfc924fa7c930c2f49226fa"
    for source in data["sources"].values():
        assert (ROOT / source["path"]).is_file(), source["path"]
