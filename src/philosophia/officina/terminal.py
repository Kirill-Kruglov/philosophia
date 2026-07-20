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


class CScientificTerminal(str, Enum):
    PASS = "C_PASS"
    NULL = "C_NULL"
    BOUNDARY = "C_BOUNDARY"
    INSUFFICIENT = "C_INSUFFICIENT"
    CENSORED = "C_CENSORED"


@dataclass(frozen=True)
class QTerminal:
    validity: QValidity
    competence: bool | None
    invalid_cause: InvalidCause | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.validity, QValidity):
            raise ValueError("Q validity must be typed")
        if self.invalid_cause is not None and not isinstance(
            self.invalid_cause, InvalidCause
        ):
            raise ValueError("Q invalid cause must be typed")
        if self.competence is not None and type(self.competence) is not bool:
            raise ValueError("Q competence must be bool or unset")
        if self.validity is QValidity.INVALID:
            if self.competence is not None or self.invalid_cause is None:
                raise ValueError("invalid Q terminal leaves competence unset")
        elif self.invalid_cause is not None or self.competence is None:
            raise ValueError("valid Q terminal requires competence and no invalid cause")
        elif (self.validity is QValidity.PASS) is not self.competence:
            raise ValueError("Q validity and competence disagree")

    def to_mapping(self) -> dict[str, object]:
        return {
            "competence": self.competence,
            "invalid_cause": self.invalid_cause.value if self.invalid_cause else None,
            "validity": self.validity.value,
        }

    @classmethod
    def from_mapping(cls, value: object) -> "QTerminal":
        if not isinstance(value, dict) or set(value) != {
            "competence", "invalid_cause", "validity"
        }:
            raise ValueError("Q terminal fields differ")
        competence = value["competence"]
        if competence is not None and type(competence) is not bool:
            raise ValueError("Q competence must be bool or null")
        cause = value["invalid_cause"]
        if cause is not None and not isinstance(cause, str):
            raise ValueError("Q invalid cause must be string or null")
        validity = value["validity"]
        if not isinstance(validity, str):
            raise ValueError("Q validity must be a string")
        return cls(
            QValidity(validity),
            competence,
            InvalidCause(cause) if cause is not None else None,
        )


@dataclass(frozen=True)
class CTerminal:
    valid: bool
    scientific_label: CScientificTerminal | None
    invalid_cause: InvalidCause | None = None

    def __post_init__(self) -> None:
        if type(self.valid) is not bool:
            raise ValueError("C validity must be bool")
        if self.invalid_cause is not None and not isinstance(
            self.invalid_cause, InvalidCause
        ):
            raise ValueError("C invalid cause must be typed")
        if self.valid:
            if (
                not isinstance(self.scientific_label, CScientificTerminal)
                or self.invalid_cause is not None
            ):
                raise ValueError("valid C terminal requires only a scientific label")
        elif self.scientific_label is not None or self.invalid_cause is None:
            raise ValueError("invalid C terminal leaves every scientific field unset")
