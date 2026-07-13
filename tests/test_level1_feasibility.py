from __future__ import annotations

import ast
from pathlib import Path

import pytest

from philosophia.level1.config import BUDGET
from philosophia.level1.feasibility import (
    FeasibilityRun,
    LatencyAggregate,
    ScorerFeasibility,
    TrajectoryFeasibility,
    random_static_schedule,
    report_payload,
)
from philosophia.level1.interlock import (
    ExecutionNotAuthorized,
    bounded_feasibility_check,
)
from philosophia.level1.panel import DummyPanelBuilder
from philosophia.level1.pool import partition_cells, realize_cell, realize_pool_index
from philosophia.level1.serialization import DeterministicKey, dummy_key


REPO = Path(__file__).resolve().parents[1]
DRIVER = REPO / "scripts/level1_run_feasibility.py"


def test_raw_pool_realization_is_exactly_four_distinct_slots() -> None:
    key = dummy_key("feasibility-pool")
    partition = partition_cells(key)
    zero_cell = next(cell for cell in partition.acquisition if cell.difference == 0)
    pairs = realize_cell(key, zero_cell)
    assert len(pairs) == len(set(pairs)) == 4
    assert all(left != right for left, right in pairs)
    flat_index = partition.acquisition.index(zero_cell) * 4 + 3
    realized = realize_pool_index(partition, key, flat_index)
    assert (realized.left, realized.right) == pairs[3]
    assert realized.realization_slot == 3


def test_feasibility_random_static_schedule_is_full_b_without_replacement() -> None:
    key = dummy_key("feasibility-schedule")
    partition = partition_cells(key)
    first = random_static_schedule(key, partition)
    second = random_static_schedule(key, partition)
    assert first == second
    assert len(first) == len(set(first)) == BUDGET
    assert min(first) >= 0 and max(first) < partition.flat_pool_size


def test_feasibility_capability_enforces_one_world_and_bounded_unit_caps() -> None:
    capability = bounded_feasibility_check(trajectory_steps=2, scorer_steps=2)
    capability.claim_development_world(0)
    with pytest.raises(ExecutionNotAuthorized, match="exactly one"):
        capability.claim_development_world(1)
    capability.spend_trajectory_step()
    capability.spend_trajectory_step()
    with pytest.raises(ExecutionNotAuthorized, match="trajectory cap"):
        capability.spend_trajectory_step()
    capability.spend_scorer_step()
    capability.spend_scorer_step()
    with pytest.raises(ExecutionNotAuthorized, match="scorer cap"):
        capability.spend_scorer_step()
    with pytest.raises(ValueError, match="capped at two"):
        bounded_feasibility_check(trajectory_steps=3)


def test_dummy_panel_accepts_real_public_root_but_requires_test_panel_key() -> None:
    public = DeterministicKey(bytes(range(32)), purpose="public-root", test_only=False)
    panel = DummyPanelBuilder(public, dummy_key("feasibility", purpose="panel")).build(
        66, world_slot=0
    )
    assert len(panel.items) == 188
    with pytest.raises(PermissionError, match="test-only panel"):
        DummyPanelBuilder(
            public,
            DeterministicKey(bytes(reversed(range(32))), purpose="panel", test_only=False),
        )


def test_report_surface_contains_only_allowed_aggregates() -> None:
    latency = LatencyAggregate(2, 1.5, 1.5, 1.0, 2.0)
    run = FeasibilityRun(
        trajectory=TrajectoryFeasibility(latency, 2, True, True, True, 1234),
        scorer=ScorerFeasibility(latency, 2, True, True),
        projected_random_static_seconds=3000.0,
        projected_active_scorer_seconds=3000.0,
    )
    payload = report_payload(run)
    serialized = repr(payload).lower()
    assert "query_series" not in serialized
    assert "loss_series" not in serialized
    assert "solve_series" not in serialized
    assert "contrast" not in serialized
    assert payload["trajectory"]["all_losses_finite"] is True
    assert payload["trajectory"]["censored_at_b"] is True


def test_driver_is_authorization_gated_and_has_no_comparative_path() -> None:
    source = DRIVER.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    assert "sample_outcome_pairs" not in imports
    assert "estimate_contrast" not in imports
    assert "choose_n3" not in imports
    assert "I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY" in source
    assert "reviewed feasibility authorization is absent" in source
    assert "--error-unmatch" in source
    assert "feasibility output directory is frozen" in source
    assert "authorization development world changed" in source
    claim = source.index("atomic_create(output_dir / CLAIM_NAME")
    run = source.index("run = run_noncomparative_feasibility(")
    assert claim < run
    assert "started-no-delete-no-retry" in source
    assert source.count("run_noncomparative_feasibility(") == 1
    assert "scientific_outcome\": False" in source
    assert "second_arm\": False" in source
    assert "arm_contrast\": False" in source
    assert "real_panel\": False" in source
