from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import torch
from torch import Tensor

from .config import COMMITTEE_SIZE, SHORTLIST_SIZE
from .model import ContactTransformer, state_hash
from .serialization import CounterStream, DeterministicKey, sample_without_replacement


@dataclass(frozen=True)
class AcquisitionChoice:
    pool_index: int
    disagreement: float


def shortlist(
    key: DeterministicKey,
    *,
    block: int,
    arm_slot: str,
    step: int,
    pool_size: int,
    answered: frozenset[int],
) -> tuple[int, ...]:
    if arm_slot not in {"active", "donor"}:
        raise ValueError("only ACTIVE-class arms draw shortlists")
    available = [index for index in range(pool_size) if index not in answered]
    if len(available) < SHORTLIST_SIZE:
        raise ValueError("shortlist exhaustion is unreachable under the signed budget")
    stream = CounterStream(key, ("L1", "shortlist", block, arm_slot, step))
    return tuple(sample_without_replacement(available, SHORTLIST_SIZE, stream))


def replay_batch_indices(
    key: DeterministicKey,
    *,
    block: int,
    arm: str,
    replicate: int,
    step: int,
    history_size: int,
) -> tuple[int, ...]:
    if history_size <= 0:
        raise ValueError("history must include the newest pair")
    newest = history_size - 1
    previous = list(range(newest))
    count = min(31, len(previous))
    stream = CounterStream(key, ("L1", "replay", block, arm, replicate, step))
    sampled = sample_without_replacement(previous, count, stream)
    return tuple([newest, *sampled])


@torch.no_grad()
def select_by_disagreement(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.Optimizer],
    candidates: Mapping[int, Tensor],
) -> AcquisitionChoice:
    if len(models) != COMMITTEE_SIZE:
        raise ValueError("the acquisition committee has exactly four members")
    if len(optimizers) != COMMITTEE_SIZE:
        raise ValueError("the acquisition committee has exactly four optimizers")
    if not candidates:
        raise ValueError("candidate set must not be empty")
    before = tuple(
        state_hash(model, optimizer)
        for model, optimizer in zip(models, optimizers, strict=True)
    )
    training_modes = tuple(model.training for model in models)
    for model in models:
        model.eval()
    try:
        best_index = -1
        best_variance = -1.0
        for pool_index in sorted(candidates):
            tokens = candidates[pool_index]
            if tokens.ndim == 1:
                tokens = tokens.unsqueeze(0)
            probabilities = torch.stack(
                [model.equal_probability(tokens).squeeze(0) for model in models]
            )
            variance = float(torch.var(probabilities, unbiased=False))
            if variance > best_variance:
                best_index = pool_index
                best_variance = variance
    finally:
        for model, training in zip(models, training_modes, strict=True):
            model.train(training)
    after = tuple(
        state_hash(model, optimizer)
        for model, optimizer in zip(models, optimizers, strict=True)
    )
    if before != after:
        raise RuntimeError("acquisition scoring mutated learner parameters")
    return AcquisitionChoice(pool_index=best_index, disagreement=best_variance)
