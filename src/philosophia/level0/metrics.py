from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import torch
from torch.nn import functional as F

from .interlock import ExecutionInterlock
from .model import GrokkingTransformer


@dataclass(frozen=True)
class Evaluation:
    loss: float
    accuracy: float


@dataclass(frozen=True)
class Observation:
    step: int
    value: float


@torch.no_grad()
def evaluate(
    model: GrokkingTransformer,
    inputs: torch.Tensor,
    targets: torch.Tensor,
    *,
    interlock: ExecutionInterlock,
) -> Evaluation:
    interlock.require_evaluation()
    # This architecture has no dropout or normalization, so eval mode is inert.
    model.eval()
    logits = model(inputs)[:, -1, : model.config.scored_classes]
    loss = F.cross_entropy(logits, targets)
    accuracy = (logits.argmax(dim=-1) == targets).float().mean()
    return Evaluation(loss=float(loss), accuracy=float(accuracy))


@torch.no_grad()
def scored_parameter_l2(model: GrokkingTransformer) -> float:
    total = 0.0
    for name, parameter in model.named_parameters():
        value = parameter
        if name == "W_U":
            value = value[:, : model.config.scored_classes]
        total += float(value.detach().square().sum())
    return math.sqrt(total)


def _first_persistent_step(
    observations: Iterable[Observation],
    *,
    threshold: float,
    minimum_step_span: int,
) -> int | None:
    if minimum_step_span < 0:
        raise ValueError("minimum_step_span must be non-negative")
    ordered = tuple(observations)
    if any(right.step <= left.step for left, right in zip(ordered, ordered[1:])):
        raise ValueError("observations must have strictly increasing steps")

    start: int | None = None
    for observation in ordered:
        if observation.value >= threshold:
            if start is None:
                start = observation.step
            if observation.step - start >= minimum_step_span:
                return start
        else:
            start = None
    return None


def first_persistent_step(
    observations: Iterable[Observation],
    *,
    threshold: float,
    minimum_step_span: int,
    interlock: ExecutionInterlock,
) -> int | None:
    interlock.require_verdict()
    return _first_persistent_step(
        observations,
        threshold=threshold,
        minimum_step_span=minimum_step_span,
    )
