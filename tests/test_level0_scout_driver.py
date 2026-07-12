from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from philosophia.level0.interlock import (
    SCOUT_MAX_SECONDS,
    SCOUT_MAX_STEPS,
    ExecutionInterlock,
    ExecutionNotAuthorized,
)
from philosophia.level0.scout import (
    CHECKPOINT_NAME,
    PRIMARY_STEPS,
    REPLAY_STEPS,
    REPORT_NAME,
    SCOUT_KIND,
    _aggregate_latencies,
    run_timing_storage_scout,
)


ROOT = Path(__file__).resolve().parents[1]


def test_scout_scope_is_fixed_below_reviewed_caps() -> None:
    assert PRIMARY_STEPS == 25
    assert REPLAY_STEPS == 25
    assert PRIMARY_STEPS + REPLAY_STEPS == 50 <= SCOUT_MAX_STEPS == 100
    assert SCOUT_MAX_SECONDS == 120.0
    assert SCOUT_KIND == "timing-storage-scout / non-outcome"
    source = inspect.getsource(
        __import__("philosophia.level0.scout", fromlist=["scout"])
    )
    assert "configure_canonical_torch_runtime()" in source
    assert "non-outcome" in REPORT_NAME
    assert "non-outcome" in CHECKPOINT_NAME


def test_scout_driver_has_no_outcome_dependency_or_held_out_access() -> None:
    source = inspect.getsource(__import__(
        "philosophia.level0.scout",
        fromlist=["scout"],
    ))
    tree = ast.parse(source)
    imported_modules = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    attributes = {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    scout_capability_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "timing_storage_scout"
    ]

    assert not any(module.endswith("metrics") for module in imported_modules)
    assert "evaluation" not in attributes
    assert "evaluate" not in attributes
    assert "first_persistent_step" not in attributes
    assert len(scout_capability_calls) == 1
    assert "StepResult" not in source


def test_scout_latency_helper_persists_aggregates_only() -> None:
    aggregate = _aggregate_latencies([0.001, 0.003, 0.002])
    assert aggregate == {
        "count": 3,
        "mean_ms": 2.0,
        "median_ms": 2.0,
        "min_ms": 1.0,
        "max_ms": 3.0,
    }
    assert "series" not in aggregate


def test_bounded_check_is_distinct_from_scout_mode() -> None:
    permit = ExecutionInterlock.bounded_check(2)
    assert permit.mode == "bounded-check"
    permit.consume_step()
    permit.consume_step()
    with pytest.raises(ExecutionNotAuthorized, match="capped at 2"):
        permit.consume_step()
    with pytest.raises(ExecutionNotAuthorized, match="cannot evaluate"):
        permit.require_evaluation()


def test_driver_executed_once_before_locked_outcome_execution() -> None:
    assert callable(run_timing_storage_scout)
    assert (ROOT / "experiments/level_0_grokking/PREREG.lock").exists()
    assert not (ROOT / "experiments/level_0_grokking/decision.json").exists()
    reports = list(ROOT.glob("**/timing-storage-scout_non-outcome.json"))
    assert len(reports) == 1
