from __future__ import annotations

from enum import Enum


class FailureCause(str, Enum):
    NONFINITE_BEFORE_SOLVE = "nonfinite-before-solve"
    NONFINITE_AFTER_SOLVE = "nonfinite-after-solve"
    OUTCOME_INDEPENDENT_PROCESS = "outcome-independent-process"
    PROCESS_UNVERIFIED = "process-unverified"
    SEAL_BREACH = "seal-breach"
    DESIGN_INVALIDITY = "design-invalidity"
    INCOMPLETE_EVIDENCE = "incomplete-evidence"


class Route(str, Enum):
    CENSOR_AT_B = "CENSOR_AT_B"
    KEEP_T_WITH_DIAGNOSTIC = "KEEP_T_WITH_DIAGNOSTIC"
    ONE_REEXECUTION = "ONE_REEXECUTION"
    PLATFORM_OR_DESIGN_INVALID = "PLATFORM_OR_DESIGN_INVALID"
    INSUFFICIENT = "INSUFFICIENT"


def route_failure(cause: FailureCause, *, prior_reexecutions: int = 0) -> Route:
    if prior_reexecutions not in (0, 1):
        raise ValueError("prior re-executions must be zero or one")
    if cause == FailureCause.NONFINITE_BEFORE_SOLVE:
        return Route.CENSOR_AT_B
    if cause == FailureCause.NONFINITE_AFTER_SOLVE:
        return Route.KEEP_T_WITH_DIAGNOSTIC
    if cause == FailureCause.OUTCOME_INDEPENDENT_PROCESS:
        return Route.ONE_REEXECUTION if prior_reexecutions == 0 else Route.PLATFORM_OR_DESIGN_INVALID
    if cause in {FailureCause.PROCESS_UNVERIFIED, FailureCause.SEAL_BREACH, FailureCause.DESIGN_INVALIDITY}:
        return Route.PLATFORM_OR_DESIGN_INVALID
    if cause == FailureCause.INCOMPLETE_EVIDENCE:
        return Route.INSUFFICIENT
    raise ValueError(f"unknown cause: {cause}")
