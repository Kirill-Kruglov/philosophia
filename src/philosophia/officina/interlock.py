"""Fail-closed execution boundary for WP-1/WP-2.

This is an accidental-execution guard, not a security sandbox. The authorized
surface is pure implementation plus dummy/test-only fixtures. No factory for a
real-world, entropy, training, Q, or C capability exists.
"""

from __future__ import annotations

from dataclasses import dataclass


_TOKEN = object()


class ExecutionNotAuthorized(RuntimeError):
    pass


@dataclass(frozen=True)
class TestOnlyCapability:
    purpose: str
    _token: object

    def __post_init__(self) -> None:
        if self._token is not _TOKEN:
            raise ExecutionNotAuthorized("test capability must use the internal factory")
        if not self.purpose.startswith("test-only:"):
            raise ExecutionNotAuthorized("test capability purpose must be explicit")


def test_only_capability(purpose: str) -> TestOnlyCapability:
    return TestOnlyCapability(f"test-only:{purpose}", _TOKEN)


def require_test_only(capability: TestOnlyCapability) -> None:
    if not isinstance(capability, TestOnlyCapability) or capability._token is not _TOKEN:
        raise ExecutionNotAuthorized("WP-1/WP-2 admit only test-only capabilities")


def generate_real_world(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized("real worlds require a signed WP-3 contract")


def run_real_t(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized("real T execution is not authorized")


def launch_q(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized("Q requires a separately signed WP-6 contract")


def execute_c(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise ExecutionNotAuthorized("C requires a separate one-shot authorization")
