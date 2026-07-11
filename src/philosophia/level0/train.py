from __future__ import annotations

from dataclasses import dataclass
import math
from typing import NoReturn

import torch
from torch.nn import functional as F

from .config import RunConfig
from .data import LearnerView
from .model import GrokkingTransformer


class OutcomeRunNotAuthorized(RuntimeError):
    pass


@dataclass(frozen=True)
class StepResult:
    loss: float
    gradient_l2: float


def make_optimizer(
    model: GrokkingTransformer,
    config: RunConfig,
) -> torch.optim.AdamW:
    return torch.optim.AdamW(
        model.parameters(),
        lr=config.learning_rate,
        betas=config.betas,
        eps=config.epsilon,
        weight_decay=config.arm.weight_decay,
        amsgrad=False,
        foreach=False,
        fused=False,
        capturable=False,
        differentiable=False,
    )


def optimization_step(
    model: GrokkingTransformer,
    optimizer: torch.optim.AdamW,
    learner: LearnerView,
) -> StepResult:
    if not isinstance(learner, LearnerView):
        raise TypeError("optimization_step accepts LearnerView only")
    model.train()
    optimizer.zero_grad(set_to_none=True)
    logits = model(learner.inputs)[:, -1, : model.config.scored_classes]
    loss = F.cross_entropy(logits, learner.targets)
    if not torch.isfinite(loss):
        raise FloatingPointError("non-finite training loss")
    loss.backward()
    gradient_squared = sum(
        float(parameter.grad.detach().square().sum())
        for parameter in model.parameters()
        if parameter.grad is not None
    )
    optimizer.step()
    return StepResult(loss=float(loss.detach()), gradient_l2=math.sqrt(gradient_squared))


def run_outcome_training(*_args: object, **_kwargs: object) -> NoReturn:
    raise OutcomeRunNotAuthorized(
        "full training is disabled until a complete PREREG.lock is signed"
    )
