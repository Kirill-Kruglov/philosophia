from __future__ import annotations

import json
from pathlib import Path
import subprocess
from typing import Any, Mapping
import torch

from .checkpoint import SCHEMA_VERSION, state_tree_hash

from .interlock import ExecutionInterlock
from .metrics import Observation, first_persistent_step
from .outcome import COMPLETE_NAME, MANIFEST_NAME, METRICS_NAME, RESUME_NAME, _read_metrics, _verify_locked_sources, _verify_repository_binding
from .scientific_spec import (
    REQUIRED_RUN_IDS,
    ScientificSpecError,
    load_lock,
    load_spec,
    run_definitions,
    sha256_file,
)


DECISION_NAME = "decision.json"


def _repository_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _persistent_start(
    metrics: list[dict[str, Any]],
    *,
    section: str,
    threshold: float,
    window: int,
    interlock: ExecutionInterlock,
) -> int | None:
    observations = [
        Observation(step=int(item["step"]), value=float(item[section]["accuracy"]))
        for item in metrics
    ]
    return first_persistent_step(
        observations,
        threshold=threshold,
        minimum_step_span=window,
        interlock=interlock,
    )


def _run_predicates(
    metrics: list[dict[str, Any]],
    *,
    spec: Mapping[str, Any],
    interlock: ExecutionInterlock,
) -> dict[str, object]:
    fit_spec = spec["predicates"]["fit"]
    generalize_spec = spec["predicates"]["generalize"]
    fit_start = _persistent_start(
        metrics,
        section="train",
        threshold=float(fit_spec["minimum"]),
        window=int(fit_spec["persistence_window"]),
        interlock=interlock,
    )
    generalize_start = _persistent_start(
        metrics,
        section="held_out",
        threshold=float(generalize_spec["minimum"]),
        window=int(generalize_spec["persistence_window"]),
        interlock=interlock,
    )
    delay = (
        generalize_start - fit_start
        if fit_start is not None and generalize_start is not None
        else None
    )
    delayed = delay is not None and delay >= int(
        spec["predicates"]["delayed"]["delta_min"]
    )
    return {
        "fit_start": fit_start,
        "generalize_start": generalize_start,
        "delay": delay,
        "FIT": fit_start is not None,
        "GENERALIZE": generalize_start is not None,
        "DELAYED": delayed,
        "replicates_delayed_generalization": (
            fit_start is not None and generalize_start is not None and delayed
        ),
    }


def _load_complete_run(
    *,
    output_root: Path,
    run_id: str,
    fixed_updates: int,
    metric_cadence: int,
    torch_num_threads: int,
    torch_num_interop_threads: int,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    run_dir = output_root / run_id
    complete_path = run_dir / COMPLETE_NAME
    if not complete_path.is_file():
        raise ScientificSpecError(f"required run is incomplete: {run_id}")
    report = json.loads(complete_path.read_text(encoding="utf-8"))
    if report.get("kind") != "philosophia-level0-complete-run":
        raise ScientificSpecError(f"run report identity mismatch: {run_id}")
    if report.get("run_id") != run_id:
        raise ScientificSpecError(f"run report id mismatch: {run_id}")
    if report.get("steps_used") != fixed_updates:
        raise ScientificSpecError(f"run budget mismatch: {run_id}")
    if (
        report.get("torch_num_threads") != torch_num_threads
        or report.get("torch_num_interop_threads") != torch_num_interop_threads
    ):
        raise ScientificSpecError(f"run thread contract mismatch: {run_id}")
    metrics_path = run_dir / METRICS_NAME
    if report.get("metrics_sha256") != sha256_file(metrics_path):
        raise ScientificSpecError(f"metrics integrity failure: {run_id}")
    metrics = _read_metrics(metrics_path)
    if not metrics or int(metrics[0]["step"]) != 0:
        raise ScientificSpecError(f"run has no step-zero metric: {run_id}")
    if int(metrics[-1]["step"]) != fixed_updates:
        raise ScientificSpecError(f"run has no final metric: {run_id}")
    expected_steps = list(range(0, fixed_updates + 1, metric_cadence))
    if [int(item["step"]) for item in metrics] != expected_steps:
        raise ScientificSpecError(f"metric cadence drift: {run_id}")
    manifest_path = run_dir / MANIFEST_NAME
    if report.get("manifest_sha256") != sha256_file(manifest_path):
        raise ScientificSpecError(f"manifest integrity failure: {run_id}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("run_id") != run_id or manifest.get("fixed_updates") != fixed_updates:
        raise ScientificSpecError(f"manifest identity failure: {run_id}")
    if (
        manifest.get("torch_num_threads") != torch_num_threads
        or manifest.get("torch_num_interop_threads") != torch_num_interop_threads
    ):
        raise ScientificSpecError(f"manifest thread contract mismatch: {run_id}")
    if report.get("prereg_lock_sha256") != manifest.get("prereg_lock_sha256"):
        raise ScientificSpecError(f"manifest/report lock mismatch: {run_id}")
    checkpoint = torch.load(run_dir / RESUME_NAME, map_location="cpu", weights_only=True)
    if checkpoint.get("schema_version") != SCHEMA_VERSION:
        raise ScientificSpecError(f"final checkpoint schema failure: {run_id}")
    if int(checkpoint.get("step", -1)) != fixed_updates:
        raise ScientificSpecError(f"final checkpoint budget failure: {run_id}")
    metadata = checkpoint.get("metadata")
    if not isinstance(metadata, Mapping):
        raise ScientificSpecError(f"final checkpoint metadata failure: {run_id}")
    if (
        metadata.get("torch_num_threads") != torch_num_threads
        or metadata.get("torch_num_interop_threads") != torch_num_interop_threads
    ):
        raise ScientificSpecError(f"checkpoint thread contract mismatch: {run_id}")
    model_hash = state_tree_hash(checkpoint.get("model_state"))
    optimizer_hash = state_tree_hash(checkpoint.get("optimizer_state"))
    if metadata.get("model_state_hash") != model_hash:
        raise ScientificSpecError(f"final model checkpoint integrity failure: {run_id}")
    if metadata.get("optimizer_state_hash") != optimizer_hash:
        raise ScientificSpecError(f"final optimizer checkpoint integrity failure: {run_id}")
    if report.get("final_model_state_hash") != model_hash:
        raise ScientificSpecError(f"final model report hash failure: {run_id}")
    if report.get("final_optimizer_state_hash") != optimizer_hash:
        raise ScientificSpecError(f"final optimizer report hash failure: {run_id}")
    source_hashes = metadata.get("source_hashes")
    if not isinstance(source_hashes, Mapping):
        raise ScientificSpecError(f"checkpoint source hashes missing: {run_id}")
    if source_hashes.get("metrics_prefix") != sha256_file(metrics_path):
        raise ScientificSpecError(f"checkpoint metrics-prefix failure: {run_id}")
    if source_hashes.get("run_manifest") != sha256_file(manifest_path):
        raise ScientificSpecError(f"checkpoint manifest-prefix failure: {run_id}")
    return report, metrics


def _assemble_decision(
    results: Mapping[str, Mapping[str, object]],
    *,
    arm_a_quorum: int,
) -> dict[str, object]:
    if tuple(results) != REQUIRED_RUN_IDS:
        raise ScientificSpecError("decision run membership or order mismatch")
    platform_violations: list[str] = []
    for run_id in REQUIRED_RUN_IDS[:-1]:
        if not bool(results[run_id]["FIT"]):
            platform_violations.append(f"{run_id} failed memorization reachability")
    if not bool(results["R-0"]["FIT"]):
        platform_violations.append("R-0 failed to memorize random labels")
    if bool(results["R-0"]["GENERALIZE"]):
        platform_violations.append("R-0 generalized random held-out labels")

    arm_a_successes = sum(
        bool(results[f"A-{seed}"]["replicates_delayed_generalization"])
        for seed in range(5)
    )
    arm_b_successes = sum(
        bool(results[f"B-{seed}"]["replicates_delayed_generalization"])
        for seed in (1, 2, 3)
    )
    if platform_violations:
        decision = "PLATFORM_INVALID"
    elif arm_a_successes >= arm_a_quorum:
        decision = "REPRODUCED"
    else:
        decision = "NOT_REPRODUCED"
    annotation = (
        "ANCHOR_FIDELITY_SENSITIVE_DIAGNOSTIC"
        if decision == "NOT_REPRODUCED" and arm_b_successes >= 1
        else "NO_PRIMARY_INFERENCE"
    )
    return {
        "decision": decision,
        "arm_a_successes": arm_a_successes,
        "arm_a_quorum": arm_a_quorum,
        "arm_b_successes": arm_b_successes,
        "arm_b_annotation": annotation,
        "platform_violations": platform_violations,
    }


def evaluate_locked_battery(
    *,
    output_root: Path,
    spec_path: Path,
    lock_path: Path,
) -> Path:
    root = Path(__file__).resolve().parents[3]
    repository_head = _repository_head(root)
    spec = load_spec(spec_path, require_accepted=True)
    expected_output_root = (root / str(spec["output_root"])).resolve()
    if output_root.resolve() != expected_output_root:
        raise ScientificSpecError("outcome root differs from scientific spec")
    definitions = run_definitions(spec)
    lock = load_lock(
        lock_path,
        spec_path=spec_path,
    )
    _verify_locked_sources(lock, root=root)
    _verify_repository_binding(root=root, lock_path=lock_path, lock=lock)
    decision_path = output_root / DECISION_NAME
    if decision_path.exists():
        raise FileExistsError("Level 0 decision already exists")

    results: dict[str, dict[str, object]] = {}
    complete_hashes: dict[str, str] = {}
    for run_id in REQUIRED_RUN_IDS:
        definition = definitions[run_id]
        report, metrics = _load_complete_run(
            output_root=output_root,
            run_id=run_id,
            fixed_updates=definition.fixed_updates,
            metric_cadence=int(spec["observations"]["metric_cadence"]),
            torch_num_threads=int(spec["environment"]["torch_num_threads"]),
            torch_num_interop_threads=int(
                spec["environment"]["torch_num_interop_threads"]
            ),
        )
        if report.get("config_hash") != definition.config_hash:
            raise ScientificSpecError(f"run config drift: {run_id}")
        if report.get("split_hash") != definition.split_hash:
            raise ScientificSpecError(f"run split drift: {run_id}")
        interlock = ExecutionInterlock.from_preregistration(
            lock_path,
            spec_path=spec_path,
            run_id=run_id,
            expected_config_hash=definition.config_hash,
            expected_fixed_steps=definition.fixed_updates,
            consumed_steps=definition.fixed_updates,
        )
        results[run_id] = _run_predicates(
            metrics,
            spec=spec,
            interlock=interlock,
        )
        complete_hashes[run_id] = sha256_file(
            output_root / run_id / COMPLETE_NAME
        )

    assembly = _assemble_decision(
        results,
        arm_a_quorum=int(spec["decision"]["arm_a_quorum"]),
    )
    payload = {
        "schema_version": 1,
        "kind": "philosophia-level0-decision",
        "scientific_scope": "five-seed Level 0 replication demonstration only",
        **assembly,
        "runs": results,
        "complete_report_hashes": complete_hashes,
        "scientific_spec_sha256": sha256_file(spec_path),
        "prereg_lock_sha256": sha256_file(lock_path),
        "repository_head": repository_head,
        "claims_forbidden": spec["claims_forbidden"],
    }
    output_root.mkdir(parents=True, exist_ok=True)
    temporary = decision_path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(decision_path)
    return decision_path
