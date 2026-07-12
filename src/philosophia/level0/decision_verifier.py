from __future__ import annotations

import json
from pathlib import Path
import subprocess
from typing import Any

from .interlock import ExecutionInterlock
from .outcome import _verify_locked_sources, _verify_repository_binding
from .outcome_evaluator import _load_complete_run, _repository_head, _run_predicates
from .scientific_spec import (
    REQUIRED_RUN_IDS,
    ScientificSpecError,
    load_lock,
    load_spec,
    run_definitions,
    sha256_file,
)


def _independent_decision_summary(
    runs: dict[str, dict[str, object]],
    *,
    arm_a_quorum: int,
) -> dict[str, object]:
    violations: list[str] = []
    for run_id in ("A-0", "A-1", "A-2", "A-3", "A-4", "B-1", "B-2", "B-3"):
        if runs[run_id]["FIT"] is not True:
            violations.append(f"{run_id} failed memorization reachability")
    if runs["R-0"]["FIT"] is not True:
        violations.append("R-0 failed to memorize random labels")
    if runs["R-0"]["GENERALIZE"] is True:
        violations.append("R-0 generalized random held-out labels")
    a_count = sum(
        runs[run_id]["replicates_delayed_generalization"] is True
        for run_id in ("A-0", "A-1", "A-2", "A-3", "A-4")
    )
    b_count = sum(
        runs[run_id]["replicates_delayed_generalization"] is True
        for run_id in ("B-1", "B-2", "B-3")
    )
    verdict = (
        "PLATFORM_INVALID"
        if violations
        else ("REPRODUCED" if a_count >= arm_a_quorum else "NOT_REPRODUCED")
    )
    return {
        "decision": verdict,
        "arm_a_successes": a_count,
        "arm_a_quorum": arm_a_quorum,
        "arm_b_successes": b_count,
        "arm_b_annotation": (
            "ANCHOR_FIDELITY_SENSITIVE_DIAGNOSTIC"
            if verdict == "NOT_REPRODUCED" and b_count >= 1
            else "NO_PRIMARY_INFERENCE"
        ),
        "platform_violations": violations,
    }


def verify_level0_decision(
    *,
    decision_path: Path,
    spec_path: Path,
    lock_path: Path,
) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    try:
        root = Path(__file__).resolve().parents[3]
        repository_head = _repository_head(root)
        spec = load_spec(spec_path, require_accepted=True)
        output_root = (root / str(spec["output_root"])).resolve()
        if decision_path.resolve() != output_root / "decision.json":
            raise ScientificSpecError("decision path differs from scientific spec")
        lock = load_lock(lock_path, spec_path=spec_path)
        _verify_locked_sources(lock, root=root)
        _verify_repository_binding(root=root, lock_path=lock_path, lock=lock)
        definitions = run_definitions(spec)
        decision: dict[str, Any] = json.loads(
            decision_path.read_text(encoding="utf-8")
        )
        if decision.get("kind") != "philosophia-level0-decision":
            raise ScientificSpecError("decision identity mismatch")
        if decision.get("scientific_spec_sha256") != sha256_file(spec_path):
            raise ScientificSpecError("decision scientific spec hash mismatch")
        if decision.get("prereg_lock_sha256") != sha256_file(lock_path):
            raise ScientificSpecError("decision lock hash mismatch")
        decision_head = decision.get("repository_head")
        if not isinstance(decision_head, str) or len(decision_head) != 40:
            raise ScientificSpecError("decision repository head is invalid")
        if subprocess.run(
            ["git", "merge-base", "--is-ancestor", decision_head, repository_head],
            cwd=root,
            check=False,
        ).returncode != 0:
            raise ScientificSpecError("decision repository head is not an ancestor")

        recomputed: dict[str, dict[str, object]] = {}
        report_hashes: dict[str, str] = {}
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
            permit = ExecutionInterlock.from_preregistration(
                lock_path,
                spec_path=spec_path,
                run_id=run_id,
                expected_config_hash=definition.config_hash,
                expected_fixed_steps=definition.fixed_updates,
                consumed_steps=definition.fixed_updates,
            )
            recomputed[run_id] = _run_predicates(
                metrics,
                spec=spec,
                interlock=permit,
            )
            report_hashes[run_id] = sha256_file(
                output_root / run_id / "run_complete.json"
            )
        if decision.get("runs") != recomputed:
            raise ScientificSpecError("decision predicates do not match metrics")
        if decision.get("complete_report_hashes") != report_hashes:
            raise ScientificSpecError("decision report hashes mismatch")

        checks = _independent_decision_summary(
            recomputed,
            arm_a_quorum=int(spec["decision"]["arm_a_quorum"]),
        )
        checks["claims_forbidden"] = spec["claims_forbidden"]
        for key, expected in checks.items():
            if decision.get(key) != expected:
                raise ScientificSpecError(f"decision field {key!r} mismatch")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ScientificSpecError) as error:
        reasons.append(str(error))
    return not reasons, reasons
