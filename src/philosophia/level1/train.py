from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor

from .interlock import UnitStepCapability
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
