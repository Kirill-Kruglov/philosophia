from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TEnding(str, Enum):
    ENVELOPE_EXHAUSTED = "T_ENVELOPE_EXHAUSTED"
    AUTHOR_STOP = "T_AUTHOR_STOP"
    CANDIDATE_SUBMITTED = "T_CANDIDATE_SUBMITTED"


class InvalidCause(str, Enum):
    ENVIRONMENT = "ENVIRONMENT"
    RESOURCE = "RESOURCE"
    PROCESS = "PROCESS"
    HASH = "HASH"
    SEAL = "SEAL"


class QValidity(str, Enum):
    PASS = "Q_VALID_PASS"
    FAIL = "Q_VALID_FAIL"
    INVALID = "Q_INVALID"


@dataclass(frozen=True)
class QTerminal:
    validity: QValidity
    competence: bool | None
    invalid_cause: InvalidCause | None = None

    def __post_init__(self) -> None:
        if self.validity is QValidity.INVALID:
            if self.competence is not None or self.invalid_cause is None:
                raise ValueError("invalid Q terminal leaves competence unset")
        elif self.invalid_cause is not None or self.competence is None:
            raise ValueError("valid Q terminal requires competence and no invalid cause")
        elif (self.validity is QValidity.PASS) is not self.competence:
            raise ValueError("Q validity and competence disagree")


@dataclass(frozen=True)
class CTerminal:
    valid: bool
    scientific_label: str | None
    invalid_cause: InvalidCause | None = None

    def __post_init__(self) -> None:
        if self.valid:
            if not self.scientific_label or self.invalid_cause is not None:
                raise ValueError("valid C terminal requires only a scientific label")
        elif self.scientific_label is not None or self.invalid_cause is None:
            raise ValueError("invalid C terminal leaves every scientific field unset")
