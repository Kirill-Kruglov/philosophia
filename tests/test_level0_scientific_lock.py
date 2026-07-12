from __future__ import annotations

import ast
import inspect
import json
from pathlib import Path

import pytest

from philosophia.level0.config import PINNED_PYTHON_VERSION
from philosophia.level0.interlock import ExecutionInterlock, ExecutionNotAuthorized
from philosophia.level0.metrics import Observation, first_persistent_step
from philosophia.level0.outcome import (
    RECOVERY_LOG_NAME,
    _recover_uncommitted_metric_tail,
    run_locked_outcome,
)
from philosophia.level0.scientific_spec import (
    REQUIRED_RUN_IDS,
    ScientificSpecError,
    canonical_json_bytes,
    load_lock,
    load_spec,
    run_definitions,
    sha256_file,
)


ROOT = Path(__file__).resolve().parents[1]
LEVEL0 = ROOT / "experiments/level_0_grokking"
SPEC_PATH = LEVEL0 / "SCIENTIFIC_SPEC.json"


def _accepted_spec(tmp_path: Path) -> tuple[Path, dict[str, object]]:
    raw = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    raw["status"] = "accepted-by-kirill-before-outcome"
    path = tmp_path / "SCIENTIFIC_SPEC.json"
    path.write_text(json.dumps(raw, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path, raw


def _fake_lock(
    tmp_path: Path,
    *,
    spec_path: Path,
    spec: dict[str, object],
    source_commit: str = "0123456789012345678901234567890123456789",
) -> Path:
    definitions = run_definitions(spec)
    runs = {
        run_id: {
            "config_hash": definitions[run_id].config_hash,
            "split_hash": definitions[run_id].split_hash,
            "control": definitions[run_id].control,
            "fixed_updates": definitions[run_id].fixed_updates,
            "max_seconds": 64800 if run_id.startswith("B-") else 21600,
            "max_artifact_bytes": 4294967296 if run_id.startswith("B-") else 2147483648,
        }
        for run_id in REQUIRED_RUN_IDS
    }
    payload = {
        "schema_version": 2,
        "kind": "philosophia-level0-preregistration",
        "status": "locked",
        "authorized_by": "Kirill",
        "authorization_statement": "I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC",
        "scientific_spec_sha256": sha256_file(spec_path),
        "source_commit": source_commit,
        "max_total_artifact_bytes": int(spec["resource_wall"]["max_total_artifact_bytes"]),
        "source_hashes": {"placeholder": "0" * 64},
        "runs": runs,
    }
    path = tmp_path / "PREREG.lock"
    path.write_bytes(canonical_json_bytes(payload))
    return path


def test_scientific_spec_closes_every_named_lock_cell() -> None:
    spec = load_spec(SPEC_PATH)
    definitions = run_definitions(spec)
    assert tuple(definitions) == REQUIRED_RUN_IDS
    assert spec["status"] == "draft-before-review-and-signature"
    assert spec["predicates"]["fit"] == {
        "metric": "reporting train accuracy",
        "minimum": 0.99,
        "persistence_window": 1000,
    }
    assert spec["predicates"]["generalize"]["minimum"] == 0.95
    assert spec["predicates"]["delayed"]["delta_min"] == 2000
    assert spec["decision"]["arm_a_quorum"] == 4
    assert spec["observations"]["metric_cadence"] == 100
    assert spec["observations"]["model_snapshot_cadence"] == 100
    assert spec["observations"]["full_checkpoint_cadence"] == 1000
    assert [definitions[f"B-{seed}"].master_seed for seed in (1, 2, 3)] == [1, 2, 3]
    assert definitions["R-0"].label_hash is not None
    assert PINNED_PYTHON_VERSION == (3, 12, 3)


def test_draft_spec_cannot_authorize_outcome(tmp_path: Path) -> None:
    with pytest.raises(ScientificSpecError, match="not accepted"):
        load_spec(SPEC_PATH, require_accepted=True)
    output_root = tmp_path / "outcomes"
    with pytest.raises(ScientificSpecError, match="not accepted"):
        run_locked_outcome(
            run_id="A-0",
            output_root=output_root,
            spec_path=SPEC_PATH,
            lock_path=LEVEL0 / "PREREG.lock",
            resume=False,
        )
    assert not output_root.exists()
    assert not (LEVEL0 / "PREREG.lock").exists()
    assert not (LEVEL0 / "decision.json").exists()


def test_schema2_lock_binds_run_config_budget_and_resume_count(tmp_path: Path) -> None:
    spec_path, spec = _accepted_spec(tmp_path)
    lock_path = _fake_lock(tmp_path, spec_path=spec_path, spec=spec)
    definition = run_definitions(spec)["A-0"]
    permit = ExecutionInterlock.from_preregistration(
        lock_path,
        spec_path=spec_path,
        run_id="A-0",
        expected_config_hash=definition.config_hash,
        expected_fixed_steps=definition.fixed_updates,
        consumed_steps=12,
        consumed_seconds=2.5,
    )
    assert permit.mode == "locked-outcome"
    assert permit.steps_used == 12
    assert permit.allow_evaluation is True
    assert permit.allow_verdict is True
    with pytest.raises(ExecutionNotAuthorized, match="config_hash"):
        ExecutionInterlock.from_preregistration(
            lock_path,
            spec_path=spec_path,
            run_id="A-0",
            expected_config_hash="wrong",
            expected_fixed_steps=definition.fixed_updates,
        )
    with pytest.raises(ExecutionNotAuthorized, match="not authorized"):
        ExecutionInterlock.from_preregistration(
            lock_path,
            spec_path=spec_path,
            run_id="A-9",
            expected_config_hash=definition.config_hash,
            expected_fixed_steps=definition.fixed_updates,
        )


def test_persistence_and_delay_predicate_is_curve_only(tmp_path: Path) -> None:
    spec_path, spec = _accepted_spec(tmp_path)
    lock_path = _fake_lock(tmp_path, spec_path=spec_path, spec=spec)
    definition = run_definitions(spec)["A-0"]
    permit = ExecutionInterlock.from_preregistration(
        lock_path,
        spec_path=spec_path,
        run_id="A-0",
        expected_config_hash=definition.config_hash,
        expected_fixed_steps=definition.fixed_updates,
    )
    fit_curve = [Observation(step, 0.99 if step >= 1000 else 0.5) for step in range(0, 3001, 100)]
    generalize_curve = [
        Observation(step, 0.96 if step >= 3000 else 0.1)
        for step in range(0, 5001, 100)
    ]
    fit = first_persistent_step(
        fit_curve,
        threshold=0.99,
        minimum_step_span=1000,
        interlock=permit,
    )
    generalize = first_persistent_step(
        generalize_curve,
        threshold=0.95,
        minimum_step_span=1000,
        interlock=permit,
    )
    assert fit == 1000
    assert generalize == 3000
    assert generalize - fit == 2000


def test_training_and_evaluator_have_separate_capabilities() -> None:
    import philosophia.level0.outcome as outcome_module
    import philosophia.level0.outcome_evaluator as evaluator_module

    training_source = inspect.getsource(outcome_module)
    evaluator_source = inspect.getsource(evaluator_module)
    training_tree = ast.parse(training_source)
    evaluator_tree = ast.parse(evaluator_source)
    training_names = {
        node.id for node in ast.walk(training_tree) if isinstance(node, ast.Name)
    }
    evaluator_names = {
        node.id for node in ast.walk(evaluator_tree) if isinstance(node, ast.Name)
    }
    assert "first_persistent_step" not in training_names
    assert "decision" not in {
        node.attr for node in ast.walk(training_tree) if isinstance(node, ast.Attribute)
    }
    assert "optimization_step" not in evaluator_names
    assert "make_optimizer" not in evaluator_names
    assert "GrokkingTransformer" not in evaluator_names


def test_anchor_claim_and_prefix_hash_are_frozen() -> None:
    spec = load_spec(SPEC_PATH)
    assert spec["source_hashes"]["paper_pdf"] == (
        "93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f"
    )
    prefix = LEVEL0 / "prefix/companion-v2-determinism-prefix_non-outcome.json"
    assert spec["source_hashes"]["v2_prefix_report"] == sha256_file(prefix)
    claims = (LEVEL0 / "ANCHOR_CLAIMS.md").read_text(encoding="utf-8")
    assert "5,000 to" in claims
    assert "10,000 epochs" in claims
    assert "3,600-epoch gap" in claims
    assert "delta_min = 2,000 epochs" in claims


def test_lock_rejects_resource_contract_drift(tmp_path: Path) -> None:
    spec_path, spec = _accepted_spec(tmp_path)
    lock_path = _fake_lock(tmp_path, spec_path=spec_path, spec=spec)
    raw = json.loads(lock_path.read_text(encoding="ascii"))
    raw["runs"]["A-0"]["max_seconds"] += 1
    lock_path.write_bytes(canonical_json_bytes(raw))
    with pytest.raises(ScientificSpecError, match="run contract mismatch"):
        load_lock(lock_path, spec_path=spec_path)


def test_resume_recovers_one_uncommitted_metric_tail(tmp_path: Path) -> None:
    metrics_path = tmp_path / "metrics.jsonl"
    first = json.dumps({"step": 0, "elapsed_seconds": 0.0}, separators=(",", ":")) + "\n"
    tail = json.dumps({"step": 100, "elapsed_seconds": 1.0}, separators=(",", ":")) + "\n"
    metrics_path.write_text(first + tail, encoding="utf-8")
    snapshots = tmp_path / "snapshots"
    snapshots.mkdir()
    stale = snapshots / "model_00000100.pt"
    stale.write_bytes(b"partial-cadence-transaction")

    recovered = _recover_uncommitted_metric_tail(
        metrics_path=metrics_path,
        checkpoint_step=0,
        checkpoint_metrics_hash=__import__("hashlib").sha256(first.encode()).hexdigest(),
        snapshot_dir=snapshots,
    )

    assert [item["step"] for item in recovered] == [0]
    assert metrics_path.read_text(encoding="utf-8") == first
    assert not stale.exists()
    audit = (tmp_path / RECOVERY_LOG_NAME).read_text(encoding="utf-8")
    assert "discarded_tail_step" in audit
    assert "elapsed_seconds" not in audit
