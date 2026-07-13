import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_level0_draft_cannot_be_mistaken_for_a_lock():
    draft = (
        ROOT / "experiments/level_0_grokking/DESIGN_DRAFT.md"
    ).read_text(encoding="utf-8")
    assert "DRAFT, NOT LOCKED, NO OUTCOME RUN AUTHORIZED" in draft
    assert (ROOT / "experiments/level_0_grokking/PREREG.lock").exists()
    assert not (ROOT / "experiments/level_0_grokking/decision.json").exists()


def test_level0_draft_names_nulls_and_unit():
    draft = (
        ROOT / "experiments/level_0_grokking/DESIGN_DRAFT.md"
    ).read_text(encoding="utf-8")
    assert "Random labels" in draft
    assert "Shuffled checkpoint order" in draft
    assert "full seeded runs" in draft


def test_literature_map_marks_open_cells():
    literature = (ROOT / "references/LITERATURE_MAP.md").read_text(encoding="utf-8")
    assert "realized answer entropy as a mediator, not a matching target" in literature
    assert "cross-world and algebra-to-geometry transfer remain open" in literature


def test_hardware_smoke_is_non_scientific():
    script = (ROOT / "scripts/hardware_smoke.py").read_text(encoding="utf-8")
    baseline = (
        ROOT / "experiments/level_0_grokking/HARDWARE_BASELINE.md"
    ).read_text(encoding="utf-8")
    assert "hardware_capability_smoke_not_scientific_outcome" in script
    assert "not a scientific outcome" in baseline


def test_committed_cpu_smoke_passed_without_gpu_claim():
    report = json.loads(
        (ROOT / "experiments/level_0_grokking/hardware_smoke_cpu.json").read_text(
            encoding="utf-8"
        )
    )
    assert report["kind"] == "hardware_capability_smoke_not_scientific_outcome"
    assert report["passed"] is True
    assert report["device"] == "cpu"
    assert report["platform"]["torch_hip"] is None
