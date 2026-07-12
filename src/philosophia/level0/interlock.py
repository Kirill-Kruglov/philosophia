"""Accidental-contamination guard, not a security boundary.

A determined operator can bypass this module by constructing a raw optimizer or
calling an unbound base-class method. The contract prevents accidental outcome
execution through committed Philosophia APIs; it does not resist hostile code.
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Literal, Mapping

from .scientific_spec import ScientificSpecError, load_lock


SCOUT_MAX_STEPS = 100
SCOUT_MAX_SECONDS = 120.0
_INTERNAL_TOKEN = object()


class ExecutionNotAuthorized(RuntimeError):
    pass


class ExecutionInterlock:
    def __init__(
        self,
        *,
        _token: object,
        mode: Literal[
            "single-step-check",
            "bounded-check",
            "timing-storage-scout",
            "locked-outcome",
        ],
        max_steps: int,
        max_seconds: float | None,
        allow_evaluation: bool,
        allow_verdict: bool,
        lock_hash: str | None,
        initial_steps: int = 0,
        initial_elapsed_seconds: float = 0.0,
    ) -> None:
        if _token is not _INTERNAL_TOKEN:
            raise ExecutionNotAuthorized("execution capabilities must use a factory")
        if initial_elapsed_seconds < 0:
            raise ExecutionNotAuthorized("initial elapsed time must be non-negative")
        if not 0 <= initial_steps <= max_steps:
            raise ExecutionNotAuthorized("initial step count exceeds capability budget")
        self.mode = mode
        self.max_steps = max_steps
        self.max_seconds = max_seconds
        self.allow_evaluation = allow_evaluation
        self.allow_verdict = allow_verdict
        self.lock_hash = lock_hash
        self._started = time.monotonic() - initial_elapsed_seconds
        self._steps = initial_steps

    @classmethod
    def single_step_check(cls) -> "ExecutionInterlock":
        return cls(
            _token=_INTERNAL_TOKEN,
            mode="single-step-check",
            max_steps=1,
            max_seconds=None,
            allow_evaluation=False,
            allow_verdict=False,
            lock_hash=None,
        )

    @classmethod
    def bounded_check(cls, max_steps: int) -> "ExecutionInterlock":
        if not 1 <= max_steps <= 16:
            raise ValueError("bounded checks require 1..16 steps")
        return cls(
            _token=_INTERNAL_TOKEN,
            mode="bounded-check",
            max_steps=max_steps,
            max_seconds=None,
            allow_evaluation=False,
            allow_verdict=False,
            lock_hash=None,
        )

    @classmethod
    def timing_storage_scout(cls) -> "ExecutionInterlock":
        return cls(
            _token=_INTERNAL_TOKEN,
            mode="timing-storage-scout",
            max_steps=SCOUT_MAX_STEPS,
            max_seconds=SCOUT_MAX_SECONDS,
            allow_evaluation=False,
            allow_verdict=False,
            lock_hash=None,
        )

    @classmethod
    def from_preregistration(
        cls,
        lock_path: Path,
        *,
        spec_path: Path,
        run_id: str,
        expected_config_hash: str,
        expected_fixed_steps: int,
        consumed_steps: int = 0,
        consumed_seconds: float = 0.0,
    ) -> "ExecutionInterlock":
        try:
            lock = load_lock(
                lock_path,
                spec_path=spec_path,
            )
        except ScientificSpecError as error:
            raise ExecutionNotAuthorized(str(error)) from error
        raw_runs = lock["runs"]
        if not isinstance(raw_runs, Mapping) or run_id not in raw_runs:
            raise ExecutionNotAuthorized(f"run {run_id!r} is not authorized")
        raw_run = raw_runs[run_id]
        if not isinstance(raw_run, Mapping):
            raise ExecutionNotAuthorized("lock run entry is malformed")
        required = {
            "config_hash": expected_config_hash,
            "fixed_updates": expected_fixed_steps,
        }
        for key, expected in required.items():
            if raw_run.get(key) != expected:
                raise ExecutionNotAuthorized(f"run lock field {key!r} mismatch")
        max_seconds = raw_run.get("max_seconds")
        if not isinstance(max_seconds, (int, float)) or max_seconds <= 0:
            raise ExecutionNotAuthorized("run wall-clock cap is missing")
        from .scientific_spec import sha256_file

        return cls(
            _token=_INTERNAL_TOKEN,
            mode="locked-outcome",
            max_steps=expected_fixed_steps,
            max_seconds=float(max_seconds),
            allow_evaluation=True,
            allow_verdict=True,
            lock_hash=sha256_file(lock_path),
            initial_steps=consumed_steps,
            initial_elapsed_seconds=consumed_seconds,
        )

    @property
    def steps_used(self) -> int:
        return self._steps

    @property
    def elapsed_seconds(self) -> float:
        return time.monotonic() - self._started

    def consume_step(self) -> None:
        self.require_within_wall()
        if self._steps >= self.max_steps:
            raise ExecutionNotAuthorized(
                f"{self.mode} is capped at {self.max_steps} optimization steps"
            )
        self._steps += 1

    def require_within_wall(self) -> None:
        if self.max_seconds is not None and self.elapsed_seconds >= self.max_seconds:
            raise ExecutionNotAuthorized(
                f"{self.mode} exceeded its {self.max_seconds:g}s wall-clock cap"
            )

    def require_evaluation(self) -> None:
        if not self.allow_evaluation:
            raise ExecutionNotAuthorized(f"{self.mode} cannot evaluate outcomes")
        self.require_within_wall()

    def require_verdict(self) -> None:
        if not self.allow_verdict:
            raise ExecutionNotAuthorized(f"{self.mode} cannot derive a verdict")
