from __future__ import annotations

from dataclasses import dataclass

from .config import (
    DEVELOPMENT_PAIRS_PER_STRATUM,
    OUTCOME_PAIRS_PER_STRATUM,
    STRATUM_COUNT,
)
from .serialization import CounterStream, DeterministicKey, sample_without_replacement


@dataclass(frozen=True, order=True)
class AdjacentPair:
    slot: int
    lower: int
    upper: int
    stratum: int

    def __post_init__(self) -> None:
        if self.upper != self.lower + 1:
            raise ValueError("Level 1 pairs must be adjacent")
        if self.stratum not in (1, 2, 3):
            raise ValueError("unknown stratum")


@dataclass(frozen=True)
class RoleAssignment:
    pair: AdjacentPair
    role_bit: int

    @property
    def target(self) -> int:
        return self.pair.lower if self.role_bit == 0 else self.pair.upper

    @property
    def donor(self) -> int:
        return self.pair.upper if self.role_bit == 0 else self.pair.lower


def registry_pairs() -> tuple[AdjacentPair, ...]:
    pairs = []
    for slot, lower in enumerate(range(66, 126, 2)):
        stratum = slot // 10 + 1
        pairs.append(AdjacentPair(slot=slot, lower=lower, upper=lower + 1, stratum=stratum))
    return tuple(pairs)


def development_pairs(key: DeterministicKey) -> tuple[AdjacentPair, ...]:
    selected = []
    pairs = registry_pairs()
    for stratum in range(1, STRATUM_COUNT + 1):
        candidates = [pair for pair in pairs if pair.stratum == stratum]
        stream = CounterStream(key, ("L1", "alloc", "dev", stratum))
        selected.extend(
            sample_without_replacement(
                candidates, DEVELOPMENT_PAIRS_PER_STRATUM, stream
            )
        )
    return tuple(sorted(selected))


def outcome_pairs(key: DeterministicKey) -> tuple[AdjacentPair, ...]:
    development = set(development_pairs(key))
    result = tuple(pair for pair in registry_pairs() if pair not in development)
    for stratum in range(1, STRATUM_COUNT + 1):
        if sum(pair.stratum == stratum for pair in result) != OUTCOME_PAIRS_PER_STRATUM:
            raise RuntimeError("outcome stratum size changed")
    return result


def assign_roles(key: DeterministicKey) -> tuple[RoleAssignment, ...]:
    assignments = []
    for pair in outcome_pairs(key):
        stream = CounterStream(key, ("L1", "alloc", "role", pair.slot))
        assignments.append(RoleAssignment(pair=pair, role_bit=stream.uniform(2)))
    return tuple(assignments)


def sample_outcome_pairs(
    key: DeterministicKey, n3: int
) -> tuple[RoleAssignment, ...]:
    if n3 not in (12, 15, 18, 21, 24):
        raise ValueError("N3 must be a frozen balanced candidate")
    per_stratum = n3 // STRATUM_COUNT
    assignments = assign_roles(key)
    sampled = []
    for stratum in range(1, STRATUM_COUNT + 1):
        candidates = [item for item in assignments if item.pair.stratum == stratum]
        stream = CounterStream(key, ("L1", "alloc", "sample", n3, stratum))
        sampled.extend(sample_without_replacement(candidates, per_stratum, stream))
    return tuple(sorted(sampled, key=lambda item: item.pair.slot))
