from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .config import (
    BUDGET,
    CHECKPOINT_CADENCE,
    PANEL_STRATUM_COUNTS,
    PERSISTENCE_CHECKPOINTS,
)


ACCURACY_MINIMUM = {"S1": 118, "S2": 15, "S3": 15, "S4": 15, "S5": 14}


class MissingCheckpoint(RuntimeError):
    pass


@dataclass(frozen=True)
class PanelObservation:
    stratum: str
    truth: bool
    p_equal: float

    def __post_init__(self) -> None:
        if self.stratum not in PANEL_STRATUM_COUNTS:
            raise ValueError("unknown panel stratum")
        if not 0.0 <= self.p_equal <= 1.0:
            raise ValueError("probability must be finite and in [0,1]")

    @property
    def abstains(self) -> bool:
        return abs(self.p_equal - 0.5) < 0.10

    @property
    def prediction(self) -> bool:
        return self.p_equal >= 0.5

    @property
    def correct(self) -> bool:
        return not self.abstains and self.prediction == self.truth

    @property
    def confident_lie(self) -> bool:
        return (
            not self.abstains
            and self.prediction != self.truth
            and (self.p_equal >= 0.9 or self.p_equal <= 0.1)
        )


@dataclass(frozen=True)
class StratumScore:
    count: int
    correct: int
    abstentions: int
    confident_lies: int
    brier: float
    qualifies: bool


def score_stratum(stratum: str, observations: Sequence[PanelObservation]) -> StratumScore:
    expected = PANEL_STRATUM_COUNTS[stratum]
    if len(observations) != expected or any(item.stratum != stratum for item in observations):
        raise ValueError("stratum observations do not match the frozen panel surface")
    correct = sum(item.correct for item in observations)
    abstentions = sum(item.abstains for item in observations)
    confident_lies = sum(item.confident_lie for item in observations)
    brier = sum((item.p_equal - float(item.truth)) ** 2 for item in observations) / expected
    lie_cap = 0 if stratum == "S4" else 1
    qualifies = (
        correct >= ACCURACY_MINIMUM[stratum]
        and abstentions <= 2
        and confident_lies <= lie_cap
        and brier <= 0.10
    )
    return StratumScore(
        count=expected,
        correct=correct,
        abstentions=abstentions,
        confident_lies=confident_lies,
        brier=brier,
        qualifies=qualifies,
    )


def checkpoint_qualifies(observations: Sequence[PanelObservation]) -> bool:
    by_stratum = {name: [] for name in PANEL_STRATUM_COUNTS}
    for observation in observations:
        by_stratum[observation.stratum].append(observation)
    return all(score_stratum(name, values).qualifies for name, values in by_stratum.items())


def first_persistent_step(qualifying: Mapping[int, bool]) -> int | None:
    expected_steps = tuple(range(0, BUDGET + 1, CHECKPOINT_CADENCE))
    missing = [step for step in expected_steps if step not in qualifying]
    if missing:
        raise MissingCheckpoint(f"missing checkpoint {missing[0]}")
    for start_index in range(len(expected_steps) - PERSISTENCE_CHECKPOINTS + 1):
        window = expected_steps[start_index : start_index + PERSISTENCE_CHECKPOINTS]
        if all(qualifying[step] for step in window):
            return window[0]
    return None
