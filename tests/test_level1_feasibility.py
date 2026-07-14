from __future__ import annotations

import ast
from pathlib import Path
from types import SimpleNamespace

import pytest
import torch

import philosophia.level1.feasibility as feasibility_module

from philosophia.level1.acquisition import AcquisitionChoice
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
from philosophia.level1.train import UnitStepResult, feasibility_committee_step
from philosophia.level1.world import Cell
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
    with pytest.raises(ValueError, match="capped at five"):
        bounded_feasibility_check(trajectory_steps=6)


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
    assert "scheduled checkpoint evaluation" in payload["projection_scope"]["random_static"]
    assert "shortlist realization" in payload["projection_scope"]["active_scorer_only"]


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
    assert "src/philosophia/level1/public_root.py" in source
    claim = source.index("atomic_create(output_dir / CLAIM_NAME")
    run = source.index("run = run_noncomparative_feasibility(")
    assert claim < run
    assert "started-no-delete-no-retry" in source
    assert source.count("run_noncomparative_feasibility(") == 1
    assert "scientific_outcome\": False" in source
    assert "second_arm\": False" in source
    assert "arm_contrast\": False" in source
    assert "real_panel\": False" in source


class _RecordingMember(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.seen: list[torch.Tensor] = []

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        self.seen.append(tokens.detach().clone())
        return self.linear(tokens)


def test_feasibility_committee_step_spends_once_and_updates_shared_batch() -> None:
    torch.manual_seed(0)
    models = [_RecordingMember() for _ in range(4)]
    optimizers = [torch.optim.AdamW(model.parameters(), lr=0.01) for model in models]
    tokens = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    labels = torch.tensor([0, 1], dtype=torch.long)
    before = [model.linear.weight.detach().clone() for model in models]
    capability = bounded_feasibility_check(trajectory_steps=1, scorer_steps=0)
    capability.claim_development_world(0)

    result = feasibility_committee_step(models, optimizers, tokens, labels, capability)

    assert result.finite
    assert capability.trajectory_steps == 1
    assert all(len(model.seen) == 1 for model in models)
    assert all(torch.equal(model.seen[0], tokens) for model in models)
    assert all(not torch.equal(model.linear.weight, old) for model, old in zip(models, before, strict=True))
    assert all(parameter.grad is None for model in models for parameter in model.parameters())

    nonfinite_models = [_RecordingMember() for _ in range(4)]
    nonfinite_optimizers = [
        torch.optim.AdamW(model.parameters(), lr=0.01) for model in nonfinite_models
    ]
    nonfinite_before = [
        model.linear.weight.detach().clone() for model in nonfinite_models
    ]
    nonfinite_capability = bounded_feasibility_check(
        trajectory_steps=1, scorer_steps=0
    )
    nonfinite_capability.claim_development_world(0)
    nonfinite = feasibility_committee_step(
        nonfinite_models,
        nonfinite_optimizers,
        torch.tensor([[float("nan"), 0.0]]),
        torch.tensor([0], dtype=torch.long),
        nonfinite_capability,
    )
    assert not nonfinite.finite
    assert nonfinite_capability.trajectory_steps == 1
    assert all(
        torch.equal(model.linear.weight, old)
        for model, old in zip(nonfinite_models, nonfinite_before, strict=True)
    )


def _install_bounded_wiring(
    monkeypatch: pytest.MonkeyPatch,
    *,
    finite_sequence: list[bool],
    panel_sequence: list[bool],
    state_hashes: list[str] | None = None,
) -> list[str]:
    events: list[str] = []
    partition = SimpleNamespace(flat_pool_size=1_000)
    models = [object() for _ in range(4)]
    optimizers = [object() for _ in range(4)]
    finite_values = iter(finite_sequence)
    panel_values = iter(panel_sequence)

    monkeypatch.setattr(feasibility_module, "CHECKPOINT_CADENCE", 1)
    monkeypatch.setattr(feasibility_module, "partition_cells", lambda key: partition)
    monkeypatch.setattr(feasibility_module, "verify_partition", lambda value: None)
    monkeypatch.setattr(
        feasibility_module,
        "random_static_schedule",
        lambda key, value: tuple(range(len(finite_sequence))),
    )
    monkeypatch.setattr(
        feasibility_module, "_committee", lambda key, block: (models, optimizers)
    )
    monkeypatch.setattr(feasibility_module, "_dummy_panel", lambda *args, **kwargs: object())

    def panel_qualifies(current_models, panel) -> bool:
        del current_models, panel
        events.append("panel")
        return next(panel_values)

    monkeypatch.setattr(feasibility_module, "_panel_qualifies", panel_qualifies)
    monkeypatch.setattr(
        feasibility_module,
        "realize_pool_index",
        lambda *args: SimpleNamespace(left=b"R", right=b"R"),
    )
    monkeypatch.setattr(
        feasibility_module, "encode_pair", lambda *args: torch.tensor([1.0, 0.0])
    )
    monkeypatch.setattr(feasibility_module, "oracle_eq", lambda *args: True)
    monkeypatch.setattr(
        feasibility_module,
        "replay_batch_indices",
        lambda key, **kwargs: (kwargs["history_size"] - 1,),
    )

    def committee_step(current_models, current_optimizers, tokens, labels, capability):
        del current_models, current_optimizers
        assert tokens.shape == (1, 2)
        assert labels.shape == (1,)
        capability.spend_trajectory_step()
        events.append("step")
        return UnitStepResult(next(finite_values))

    monkeypatch.setattr(
        feasibility_module, "feasibility_committee_step", committee_step
    )
    monkeypatch.setattr(feasibility_module, "_checkpoint_size", lambda *args: 321)
    monkeypatch.setattr(
        feasibility_module,
        "shortlist",
        lambda *args, **kwargs: tuple(range(100, 612)),
    )
    monkeypatch.setattr(
        feasibility_module,
        "select_by_disagreement",
        lambda *args, **kwargs: AcquisitionChoice(100, 0.1),
    )
    hashes = iter(state_hashes) if state_hashes is not None else None
    monkeypatch.setattr(
        feasibility_module,
        "state_hash",
        (lambda *args: next(hashes)) if hashes is not None else (lambda *args: "same"),
    )
    return events


def test_bounded_wiring_pins_cadence_persistence_and_nonfinite_break(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    events = _install_bounded_wiring(
        monkeypatch,
        finite_sequence=[True, True, True, True],
        panel_sequence=[True, True, True, True, True],
    )
    capability = bounded_feasibility_check(trajectory_steps=4, scorer_steps=1)
    run = feasibility_module.run_noncomparative_feasibility(
        dummy_key("bounded-wiring"), pair_slot=0, modulus=66, capability=capability
    )
    assert capability.trajectory_steps == 4
    assert capability.scorer_steps == 1
    assert events == ["panel", "step", "panel", "step", "panel", "step", "panel", "step", "panel"]
    assert run.trajectory.all_losses_finite
    assert run.trajectory.censored_at_b is False
    assert run.trajectory.checkpoint_artifact_bytes == 321
    assert run.scorer.learner_state_unchanged

    events = _install_bounded_wiring(
        monkeypatch,
        finite_sequence=[True, False, True, True],
        panel_sequence=[False, False],
    )
    nonfinite_capability = bounded_feasibility_check(
        trajectory_steps=4, scorer_steps=1
    )
    nonfinite = feasibility_module.run_noncomparative_feasibility(
        dummy_key("bounded-nonfinite"),
        pair_slot=0,
        modulus=66,
        capability=nonfinite_capability,
    )
    assert nonfinite_capability.trajectory_steps == 2
    assert events == ["panel", "step", "panel", "step"]
    assert not nonfinite.trajectory.all_losses_finite
    assert nonfinite.trajectory.censored_at_b


def test_bounded_wiring_scorer_mutation_guard_fires(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_bounded_wiring(
        monkeypatch,
        finite_sequence=[True],
        panel_sequence=[False, False],
        state_hashes=["before"] * 4 + ["after"] * 4,
    )
    capability = bounded_feasibility_check(trajectory_steps=1, scorer_steps=1)
    with pytest.raises(RuntimeError, match="scorer microbenchmark mutated"):
        feasibility_module.run_noncomparative_feasibility(
            dummy_key("bounded-mutation"),
            pair_slot=0,
            modulus=66,
            capability=capability,
        )


def test_raw_pool_realization_exhaustion_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "philosophia.level1.pool.CounterStream.uniform", lambda self, modulus: 0
    )
    with pytest.raises(RuntimeError, match="exhaustion is design invalidity"):
        realize_cell(dummy_key("forced-exhaustion"), Cell(0, 0, 0))
