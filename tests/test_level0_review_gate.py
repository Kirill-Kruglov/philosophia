from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"


def test_trace_records_anchor_discrepancies():
    trace = (LEVEL0 / "CONFIG_TRACE.md").read_text(encoding="utf-8")
    assert "optimizer param group stores weight_decay=0.1" in trace
    assert "paper states 40,000 epochs" in trace
    assert "No preregistration lock is allowed" in trace


def test_v2_prefix_matches_and_outcome_remains_blocked():
    spec = (LEVEL0 / "IMPLEMENTATION_SPEC_DRAFT.md").read_text(encoding="utf-8")
    assert "companion-fidelity v2 is implemented" in spec
    assert "matching bounded" in spec
    assert "determinism-prefix report" in spec
    assert "Full training and every outcome" in spec
    assert "run remain disabled" in spec
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()


def test_opus_prompt_forbids_outcome_prediction():
    prompt = (
        ROOT / "reviews/opus_level0_design_prompt.md"
    ).read_text(encoding="utf-8")
    assert "Do not predict whether grokking will occur" in prompt
    assert "BLOCKED_SOURCE" in prompt
    assert "proposed positive-arm table" in prompt
