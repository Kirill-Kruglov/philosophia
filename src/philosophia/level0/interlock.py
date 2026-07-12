"""Accidental-contamination guard, not a security boundary.

A determined operator can bypass this module by constructing a raw optimizer or
calling an unbound base-class method. The contract prevents accidental outcome
execution through committed Philosophia APIs; it does not resist hostile code.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time
from typing import Literal


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
    ) -> None:
        if _token is not _INTERNAL_TOKEN:
            raise ExecutionNotAuthorized("execution capabilities must use a factory")
        self.mode = mode
        self.max_steps = max_steps
        self.max_seconds = max_seconds
        self.allow_evaluation = allow_evaluation
        self.allow_verdict = allow_verdict
        self.lock_hash = lock_hash
        self._started = time.monotonic()
        self._steps = 0

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
        expected_config_hash: str,
        expected_fixed_steps: int,
    ) -> "ExecutionInterlock":
        if lock_path.name != "PREREG.lock" or not lock_path.is_file():
            raise ExecutionNotAuthorized("a real PREREG.lock file is required")
        raw = lock_path.read_bytes()
        try:
            payload = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ExecutionNotAuthorized("PREREG.lock must be canonical JSON") from error
        canonical = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
        ).encode("ascii")
        if raw not in (canonical, canonical + b"\n"):
            raise ExecutionNotAuthorized("PREREG.lock must be canonical JSON")
        required = {
            "schema_version": 1,
            "kind": "philosophia-level0-preregistration",
            "status": "locked",
            "authorized_by": "Kirill",
            "before_lock_complete": True,
            "config_hash": expected_config_hash,
            "fixed_steps": expected_fixed_steps,
        }
        for key, expected in required.items():
            if payload.get(key) != expected:
                raise ExecutionNotAuthorized(f"PREREG.lock field {key!r} is invalid")
        return cls(
            _token=_INTERNAL_TOKEN,
            mode="locked-outcome",
            max_steps=expected_fixed_steps,
            max_seconds=None,
            allow_evaluation=True,
            allow_verdict=True,
            lock_hash=hashlib.sha256(raw).hexdigest(),
        )

    @property
    def steps_used(self) -> int:
        return self._steps

    def consume_step(self) -> None:
        if self._steps >= self.max_steps:
            raise ExecutionNotAuthorized(
                f"{self.mode} is capped at {self.max_steps} optimization steps"
            )
        if (
            self.max_seconds is not None
            and time.monotonic() - self._started >= self.max_seconds
        ):
            raise ExecutionNotAuthorized(
                f"{self.mode} exceeded its {self.max_seconds:g}s wall-clock cap"
            )
        self._steps += 1

    def require_evaluation(self) -> None:
        if not self.allow_evaluation:
            raise ExecutionNotAuthorized(f"{self.mode} cannot evaluate outcomes")

    def require_verdict(self) -> None:
        if not self.allow_verdict:
            raise ExecutionNotAuthorized(f"{self.mode} cannot derive a verdict")
