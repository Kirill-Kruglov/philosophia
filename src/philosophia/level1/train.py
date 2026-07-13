from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import torch
from torch import Tensor

from .config import COMMITTEE_SIZE
from .interlock import FeasibilityCapability, UnitStepCapability
from .model import ContactTransformer


@dataclass(frozen=True)
class UnitStepResult:
    finite: bool


def unit_training_step(
    model: ContactTransformer,
    optimizer: torch.optim.AdamW,
    tokens: Tensor,
    labels: Tensor,
    capability: UnitStepCapability,
) -> UnitStepResult:
    capability.spend()
    logits = model(tokens)
    loss = torch.nn.functional.cross_entropy(logits, labels, reduction="mean")
    finite = bool(torch.isfinite(loss))
    if finite:
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    return UnitStepResult(finite=finite)


def feasibility_committee_step(
    models: Sequence[ContactTransformer],
    optimizers: Sequence[torch.optim.AdamW],
    tokens: Tensor,
    labels: Tensor,
    capability: FeasibilityCapability,
) -> UnitStepResult:
    if len(models) != COMMITTEE_SIZE or len(optimizers) != COMMITTEE_SIZE:
        raise ValueError("feasibility trains exactly one four-member committee")
    capability.spend_trajectory_step()
    losses = [
        torch.nn.functional.cross_entropy(model(tokens), labels, reduction="mean")
        for model in models
    ]
    finite = all(bool(torch.isfinite(loss)) for loss in losses)
    if finite:
        for loss in losses:
            loss.backward()
        for optimizer in optimizers:
            optimizer.step()
            optimizer.zero_grad()
    return UnitStepResult(finite=finite)
