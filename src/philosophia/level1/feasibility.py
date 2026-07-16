from __future__ import annotations

from dataclasses import asdict, dataclass
from io import BytesIO
import math
import statistics
import time
from typing import Sequence

import torch

from .acquisition import replay_batch_indices, select_by_disagreement, shortlist
from .config import (
    BUDGET,
    CHECKPOINT_CADENCE,
    COMMITTEE_SIZE,
    SHORTLIST_SIZE,
)
from .interlock import FeasibilityCapability
from .model import (
    ContactTransformer,
    build_optimizer,
    committee_equal_probability,
    encode_pair,
    state_hash,
)
from .panel import DummyPanel, DummyPanelBuilder
from .pool import PoolPartition, partition_cells, realize_pool_index, verify_partition
from .scoring import PanelObservation, checkpoint_qualifies
from .serialization import (
    CounterStream,
    DeterministicKey,
    dummy_key,
    sample_without_replacement,
)
from .train import feasibility_committee_step, full_history_committee_step
from .world import oracle_eq


@dataclass(frozen=True)
class LatencyAggregate:
    count: int
    mean_seconds: float
    median_seconds: float
    min_seconds: float
    max_seconds: float


@dataclass(frozen=True)
class TrajectoryFeasibility:
    latency: LatencyAggregate
    steps_completed: int
    all_losses_finite: bool
    panel_computable: bool
    censored_at_b: bool
    checkpoint_artifact_bytes: int


@dataclass(frozen=True)
class ScorerFeasibility:
    latency: LatencyAggregate
    steps_completed: int
    all_scores_finite: bool
    learner_state_unchanged: bool


@dataclass(frozen=True)
class FeasibilityRun:
    trajectory: TrajectoryFeasibility
    scorer: ScorerFeasibility
    projected_random_static_seconds: float
    projected_active_scorer_seconds: float


@dataclass(frozen=True)
class FeasibilityV2Run:
    trajectory: TrajectoryFeasibility


def latency_aggregate(values: Sequence[float]) -> LatencyAggregate:
    if not values or any(not math.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("latency samples must be finite and non-negative")
    return LatencyAggregate(
        count=len(values),
        mean_seconds=statistics.fmean(values),
        median_seconds=statistics.median(values),
        min_seconds=min(values),
        max_seconds=max(values),
    )


def random_static_schedule(
    key: DeterministicKey,
    partition: PoolPartition,
) -> tuple[int, ...]:
    stream = CounterStream(key, ("L1", "feas"))
    return tuple(
        sample_without_replacement(
            range(partition.flat_pool_size),
            BUDGET,
            stream,
        )
    )


def _committee(
    key: DeterministicKey,
    *,
    block: int,
) -> tuple[list[ContactTransformer], list[torch.optim.AdamW]]:
    models = [
        ContactTransformer(key, block=block, replicate=1, member=member)
        for member in range(COMMITTEE_SIZE)
    ]
    optimizers = [build_optimizer(model) for model in models]
    return models, optimizers


def _dummy_panel(
    public_key: DeterministicKey,
    *,
    modulus: int,
    world_slot: int,
) -> DummyPanel:
    panel_key = dummy_key("level1-feasibility", purpose="panel")
    return DummyPanelBuilder(public_key, panel_key).build(
        modulus,
        world_slot=world_slot,
    )


def _panel_qualifies(
    models: Sequence[ContactTransformer],
    panel: DummyPanel,
) -> bool:
    tokens = torch.stack([encode_pair(item.left, item.right) for item in panel.items])
    probabilities = committee_equal_probability(models, tokens)
    observations = [
        PanelObservation(item.stratum, item.truth, float(probability))
        for item, probability in zip(panel.items, probabilities, strict=True)
    ]
    return checkpoint_qualifies(observations)


def _checkpoint_size(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.AdamW],
    history_tokens: Sequence[torch.Tensor],
    history_labels: Sequence[int],
    answered_indices: Sequence[int],
    step: int,
    *,
    purpose: str = "level1-feasibility-size-only-not-persisted",
) -> int:
    buffer = BytesIO()
    torch.save(
        {
            "models": [model.state_dict() for model in models],
            "optimizers": [optimizer.state_dict() for optimizer in optimizers],
            "history_tokens": list(history_tokens),
            "history_labels": list(history_labels),
            "answered_indices": list(answered_indices),
            "step": step,
            "deterministic_streams": "domain-and-step-derived-from-public-root",
            "purpose": purpose,
        },
        buffer,
    )
    return buffer.tell()


def run_noncomparative_feasibility(
    key: DeterministicKey,
    *,
    pair_slot: int,
    modulus: int,
    capability: FeasibilityCapability,
) -> FeasibilityRun:
    """Run the single permitted arm and scorer microbenchmark in memory."""
    capability.claim_development_world(pair_slot)
    partition = partition_cells(key)
    verify_partition(partition)
    schedule = random_static_schedule(key, partition)
    models, optimizers = _committee(key, block=pair_slot)
    panel = _dummy_panel(key, modulus=modulus, world_slot=pair_slot)

    history_tokens: list[torch.Tensor] = []
    history_labels: list[int] = []
    step_latencies: list[float] = []
    all_finite = True
    panel_computable = True
    first_complete_window = False
    recent_qualifying: list[bool] = [_panel_qualifies(models, panel)]

    for step, pool_index in enumerate(schedule, start=1):
        started = time.monotonic()
        capability.check_wall()
        raw_pair = realize_pool_index(partition, key, pool_index)
        history_tokens.append(encode_pair(raw_pair.left, raw_pair.right))
        history_labels.append(int(oracle_eq(raw_pair.left, raw_pair.right, modulus)))
        batch_indices = replay_batch_indices(
            key,
            block=pair_slot,
            arm="random",
            replicate=1,
            step=step,
            history_size=len(history_tokens),
        )
        tokens = torch.stack([history_tokens[index] for index in batch_indices])
        labels = torch.tensor(
            [history_labels[index] for index in batch_indices],
            dtype=torch.long,
        )
        result = feasibility_committee_step(
            models,
            optimizers,
            tokens,
            labels,
            capability,
        )
        capability.check_wall()
        if not result.finite:
            all_finite = False
            step_latencies.append(time.monotonic() - started)
            break
        if step % CHECKPOINT_CADENCE == 0:
            recent_qualifying.append(_panel_qualifies(models, panel))
            if len(recent_qualifying) >= 5 and all(recent_qualifying[-5:]):
                first_complete_window = True
        step_latencies.append(time.monotonic() - started)
        capability.check_wall()

    trajectory_latency = latency_aggregate(step_latencies)
    trajectory = TrajectoryFeasibility(
        latency=trajectory_latency,
        steps_completed=capability.trajectory_steps,
        all_losses_finite=all_finite,
        panel_computable=panel_computable,
        censored_at_b=not first_complete_window,
        checkpoint_artifact_bytes=_checkpoint_size(
            models,
            optimizers,
            history_tokens,
            history_labels,
            schedule[: capability.trajectory_steps],
            capability.trajectory_steps,
        ),
    )

    scorer_latencies: list[float] = []
    scores_finite = True
    state_before = tuple(
        state_hash(model, optimizer)
        for model, optimizer in zip(models, optimizers, strict=True)
    )
    answered = frozenset(schedule[: capability.trajectory_steps])
    for step in range(capability.scorer_cap):
        started = time.monotonic()
        capability.check_wall()
        indices = shortlist(
            key,
            block=pair_slot,
            arm_slot="active",
            step=step,
            pool_size=partition.flat_pool_size,
            answered=answered,
        )
        if len(indices) != SHORTLIST_SIZE:
            raise RuntimeError("signed scorer shortlist size changed")
        candidates = {}
        for index in indices:
            raw_pair = realize_pool_index(partition, key, index)
            candidates[index] = encode_pair(raw_pair.left, raw_pair.right)
        capability.spend_scorer_step()
        choice = select_by_disagreement(models, optimizers, candidates)
        scorer_latencies.append(time.monotonic() - started)
        capability.check_wall()
        scores_finite = scores_finite and math.isfinite(choice.disagreement)
    state_after = tuple(
        state_hash(model, optimizer)
        for model, optimizer in zip(models, optimizers, strict=True)
    )
    scorer_latency = latency_aggregate(scorer_latencies)
    scorer = ScorerFeasibility(
        latency=scorer_latency,
        steps_completed=capability.scorer_steps,
        all_scores_finite=scores_finite,
        learner_state_unchanged=state_before == state_after,
    )
    if not scorer.learner_state_unchanged:
        raise RuntimeError("scorer microbenchmark mutated the learner")

    return FeasibilityRun(
        trajectory=trajectory,
        scorer=scorer,
        projected_random_static_seconds=trajectory_latency.mean_seconds * BUDGET,
        projected_active_scorer_seconds=scorer_latency.mean_seconds * BUDGET,
    )


def report_payload(run: FeasibilityRun) -> dict[str, object]:
    return {
        "trajectory": asdict(run.trajectory),
        "scorer": asdict(run.scorer),
        "projected_wall_seconds": {
            "random_static": run.projected_random_static_seconds,
            "active_scorer_only": run.projected_active_scorer_seconds,
            "combined": (
                run.projected_random_static_seconds
                + run.projected_active_scorer_seconds
            ),
        },
        "projection_scope": {
            "random_static": (
                "mean full oracle-step including scheduled checkpoint evaluation "
                "times B; excludes one-time initialization and step-0 evaluation"
            ),
            "active_scorer_only": (
                "mean shortlist realization, encoding, and E-by-S scoring times B; "
                "excludes ACTIVE training and all other Level 1 arms"
            ),
        },
    }


def run_noncomparative_feasibility_v2(
    key: DeterministicKey,
    *,
    pair_slot: int,
    modulus: int,
    capability: FeasibilityCapability,
) -> FeasibilityV2Run:
    """Run the amended full-history fixture without scorer or arm contrast."""
    if capability.scorer_cap != 0:
        raise ValueError("v2 feasibility forbids scorer execution")
    capability.claim_development_world(pair_slot)
    partition = partition_cells(key)
    verify_partition(partition)
    schedule = random_static_schedule(key, partition)
    models, optimizers = _committee(key, block=pair_slot)
    panel = _dummy_panel(key, modulus=modulus, world_slot=pair_slot)

    history_tokens: list[torch.Tensor] = []
    history_labels: list[int] = []
    step_latencies: list[float] = []
    all_finite = True
    first_complete_window = False
    recent_qualifying: list[bool] = [_panel_qualifies(models, panel)]

    for step, pool_index in enumerate(schedule, start=1):
        started = time.monotonic()
        capability.check_wall()
        raw_pair = realize_pool_index(partition, key, pool_index)
        history_tokens.append(encode_pair(raw_pair.left, raw_pair.right))
        history_labels.append(int(oracle_eq(raw_pair.left, raw_pair.right, modulus)))
        result = full_history_committee_step(
            models,
            optimizers,
            history_tokens,
            history_labels,
            capability,
        )
        capability.check_wall()
        if not result.finite:
            all_finite = False
            step_latencies.append(time.monotonic() - started)
            break
        if step % CHECKPOINT_CADENCE == 0:
            recent_qualifying.append(_panel_qualifies(models, panel))
            if len(recent_qualifying) >= 5 and all(recent_qualifying[-5:]):
                first_complete_window = True
        step_latencies.append(time.monotonic() - started)
        capability.check_wall()

    completed = capability.trajectory_steps
    trajectory = TrajectoryFeasibility(
        latency=latency_aggregate(step_latencies),
        steps_completed=completed,
        all_losses_finite=all_finite,
        panel_computable=True,
        censored_at_b=not first_complete_window,
        checkpoint_artifact_bytes=_checkpoint_size(
            models,
            optimizers,
            history_tokens,
            history_labels,
            schedule[:completed],
            completed,
            purpose="level1-feasibility-v2-size-only-not-persisted",
        ),
    )
    return FeasibilityV2Run(trajectory=trajectory)


def report_payload_v2(run: FeasibilityV2Run) -> dict[str, object]:
    return {
        "trajectory": asdict(run.trajectory),
        "projection_scope": {
            "trajectory": (
                "measured full-history oracle-step latency including scheduled "
                "dummy-panel evaluation; no arm or v1/v2 contrast"
            )
        },
    }
