from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any, Callable, NoReturn

import torch
from torch.nn import functional as F

from .config import RunConfig
from .data import LearnerView
from .interlock import ExecutionInterlock, ExecutionNotAuthorized
from .model import GrokkingTransformer


class OutcomeRunNotAuthorized(ExecutionNotAuthorized):
    pass


class InterlockedAdamW(torch.optim.AdamW):
    def __init__(self, *args: object, warmup_updates: int, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        if warmup_updates != 10:
            raise ValueError("companion warmup is frozen at ten updates")
        self.warmup_updates = warmup_updates
        self._scheduler = torch.optim.lr_scheduler.LambdaLR(
            self,
            lr_lambda=lambda step: min(step / self.warmup_updates, 1.0),
        )

    def step(
        self,
        closure: Callable[[], float] | None = None,
        *,
        interlock: ExecutionInterlock | None = None,
    ) -> Any:
        if interlock is None:
            raise ExecutionNotAuthorized("AdamW.step requires an execution interlock")
        if interlock.mode == "single-step-check" and getattr(
            self, "_single_step_consumed", False
        ):
            raise ExecutionNotAuthorized(
                "this optimizer already consumed its one non-scout step"
            )
        interlock.consume_step()
        if interlock.mode == "single-step-check":
            self._single_step_consumed = True
        result = super().step(closure)
        self._scheduler.step()
        return result

    def state_dict(self) -> dict[str, object]:
        return {
            "optimizer": super().state_dict(),
            "scheduler": self._scheduler.state_dict(),
            "warmup_updates": self.warmup_updates,
        }

    def load_state_dict(self, state_dict: dict[str, object]) -> None:
        if state_dict.get("warmup_updates") != self.warmup_updates:
            raise ValueError("optimizer checkpoint warmup mismatch")
        super().load_state_dict(state_dict["optimizer"])
        self._scheduler.load_state_dict(state_dict["scheduler"])


@dataclass(frozen=True)
class StepResult:
    loss: float
    gradient_l2: float
    learning_rate_used: float
    learning_rate_after: float


def make_optimizer(
    model: GrokkingTransformer,
    config: RunConfig,
) -> InterlockedAdamW:
    return InterlockedAdamW(
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
        warmup_updates=config.warmup_updates,
    )


def optimization_step(
    model: GrokkingTransformer,
    optimizer: InterlockedAdamW,
    learner: LearnerView,
    *,
    interlock: ExecutionInterlock,
) -> StepResult:
    if not isinstance(learner, LearnerView):
        raise TypeError("optimization_step accepts LearnerView only")
    model.train()
    optimizer.zero_grad(set_to_none=True)
    logits = model(learner.inputs)[:, -1, : model.config.training_classes]
    loss = F.cross_entropy(logits, learner.targets)
    if not torch.isfinite(loss):
        raise FloatingPointError("non-finite training loss")
    loss.backward()
    gradient_squared = sum(
        float(parameter.grad.detach().square().sum())
        for parameter in model.parameters()
        if parameter.grad is not None
    )
    learning_rate_used = float(optimizer.param_groups[0]["lr"])
    optimizer.step(interlock=interlock)
    optimizer.zero_grad(set_to_none=True)
    return StepResult(
        loss=float(loss.detach()),
        gradient_l2=math.sqrt(gradient_squared),
        learning_rate_used=learning_rate_used,
        learning_rate_after=float(optimizer.param_groups[0]["lr"]),
    )


def run_outcome_training(*_args: object, **_kwargs: object) -> NoReturn:
    raise OutcomeRunNotAuthorized(
        "no full-run driver exists; a complete PREREG.lock is required first"
    )
