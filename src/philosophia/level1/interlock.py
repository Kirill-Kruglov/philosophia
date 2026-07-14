"""Accidental-execution guards for reviewed Level 1 gates.

This is a procedural boundary, not a security seal. Unit tests receive one-step
or explicitly bounded capabilities. The production feasibility capability is
limited to one development world, one B-step RANDOM-STATIC trajectory, 200
scorer-only steps, and one shared 12-hour wall. No outcome capability exists.
"""

from __future__ import annotations

import time

from .config import BUDGET


_TOKEN = object()
_FEASIBILITY_SCORER_CAP = 200
_FEASIBILITY_WALL_SECONDS = 12 * 60 * 60


class ExecutionNotAuthorized(RuntimeError):
    pass


class UnitStepCapability:
    def __init__(self, token: object) -> None:
        if token is not _TOKEN:
            raise ExecutionNotAuthorized("capabilities must use the test factory")
        self._spent = False

    def spend(self) -> None:
        if self._spent:
            raise ExecutionNotAuthorized("unit-step capability is already spent")
        self._spent = True


class FeasibilityCapability:
    def __init__(
        self,
        token: object,
        *,
        trajectory_cap: int,
        scorer_cap: int,
        wall_seconds: float,
        purpose: str,
    ) -> None:
        if token is not _TOKEN:
            raise ExecutionNotAuthorized("capabilities must use a reviewed factory")
        if not 0 <= trajectory_cap <= BUDGET:
            raise ValueError("feasibility trajectory cap exceeds B")
        if not 0 <= scorer_cap <= _FEASIBILITY_SCORER_CAP:
            raise ValueError("feasibility scorer cap exceeds 200")
        if not 0 < wall_seconds <= _FEASIBILITY_WALL_SECONDS:
            raise ValueError("feasibility wall exceeds 12 hours")
        self.trajectory_cap = trajectory_cap
        self.scorer_cap = scorer_cap
        self.wall_seconds = wall_seconds
        self.purpose = purpose
        self._trajectory_steps = 0
        self._scorer_steps = 0
        self._world_slot: int | None = None
        self._started = time.monotonic()

    def claim_development_world(self, world_slot: int) -> None:
        self.check_wall()
        if self._world_slot is not None:
            raise ExecutionNotAuthorized("feasibility admits exactly one development world")
        if world_slot < 0:
            raise ValueError("world slot must be non-negative")
        self._world_slot = world_slot

    def spend_trajectory_step(self) -> None:
        self.check_wall()
        if self._world_slot is None:
            raise ExecutionNotAuthorized("development world must be claimed first")
        if self._trajectory_steps >= self.trajectory_cap:
            raise ExecutionNotAuthorized("feasibility trajectory cap exhausted")
        self._trajectory_steps += 1

    def spend_scorer_step(self) -> None:
        self.check_wall()
        if self._scorer_steps >= self.scorer_cap:
            raise ExecutionNotAuthorized("feasibility scorer cap exhausted")
        self._scorer_steps += 1

    def check_wall(self) -> None:
        if time.monotonic() - self._started > self.wall_seconds:
            raise ExecutionNotAuthorized("feasibility wall-clock cap exhausted")

    @property
    def trajectory_steps(self) -> int:
        return self._trajectory_steps

    @property
    def scorer_steps(self) -> int:
        return self._scorer_steps


def unit_step_capability() -> UnitStepCapability:
    return UnitStepCapability(_TOKEN)


def feasibility_capability() -> FeasibilityCapability:
    return FeasibilityCapability(
        _TOKEN,
        trajectory_cap=BUDGET,
        scorer_cap=_FEASIBILITY_SCORER_CAP,
        wall_seconds=_FEASIBILITY_WALL_SECONDS,
        purpose="level1-noncomparative-feasibility",
    )


def bounded_feasibility_check(
    *, trajectory_steps: int = 1, scorer_steps: int = 1
) -> FeasibilityCapability:
    if trajectory_steps > 5 or scorer_steps > 5:
        raise ValueError("unit feasibility checks are capped at five steps")
    return FeasibilityCapability(
        _TOKEN,
        trajectory_cap=trajectory_steps,
        scorer_cap=scorer_steps,
        wall_seconds=120.0,
        purpose="unit-check-not-feasibility-execution",
    )


def run_level1_trajectory(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized(
        "Level 1 outcome trajectory execution awaits later reviewed gate drivers"
    )
