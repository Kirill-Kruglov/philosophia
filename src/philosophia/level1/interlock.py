"""Accidental-execution guard for the pre-entropy implementation stage.

This is a procedural boundary, not a security seal. Committed Level 1 APIs expose
only one-step unit-test capabilities until later reviewed drivers are added.
"""

from __future__ import annotations


_TOKEN = object()


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


def unit_step_capability() -> UnitStepCapability:
    return UnitStepCapability(_TOKEN)


def run_level1_trajectory(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized(
        "Level 1 trajectory execution awaits later reviewed gate drivers"
    )
