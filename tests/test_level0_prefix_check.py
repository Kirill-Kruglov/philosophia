from __future__ import annotations

import json
import ast
import inspect
from pathlib import Path

from philosophia.level0.prefix_check import (
    PREFIX_KIND,
    PREFIX_STEPS,
    REPORT_NAME,
    run_companion_v2_prefix_check,
)


ROOT = Path(__file__).resolve().parents[1]


def test_v2_prefix_scope_and_artifact_are_non_outcome() -> None:
    assert PREFIX_STEPS == 10
    assert "non-outcome" in PREFIX_KIND
    assert "non-outcome" in REPORT_NAME
    assert callable(run_companion_v2_prefix_check)
    source = inspect.getsource(
        __import__("philosophia.level0.prefix_check", fromlist=["prefix_check"])
    )
    assert "configure_canonical_torch_runtime()" in source
    reports = list(ROOT.glob("**/companion-v2-determinism-prefix_non-outcome.json"))
    assert len(reports) <= 1
    if reports:
        payload = json.loads(reports[0].read_text(encoding="utf-8"))
        assert payload["scientific_outcome"] is False
        assert payload["deterministic_prefix"]["match"] is True


def test_v2_prefix_driver_has_no_evaluation_verdict_or_raw_loss_persistence() -> None:
    source = inspect.getsource(
        __import__("philosophia.level0.prefix_check", fromlist=["prefix_check"])
    )
    tree = ast.parse(source)
    imported_modules = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    attributes = {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    bounded_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "bounded_check"
    ]
    assert not any(module.endswith("metrics") for module in imported_modules)
    assert "evaluation" not in attributes
    assert "evaluate" not in attributes
    assert "first_persistent_step" not in attributes
    assert len(bounded_calls) == 1
    assert '"losses"' not in source
    assert '"loss"' not in source
