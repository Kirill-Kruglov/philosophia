from __future__ import annotations

from dataclasses import dataclass

from .config import D_ACQ, POOL_MULTIPLICITY
from .serialization import CounterStream, DeterministicKey, shuffled
from .world import (
    Cell,
    admissible_paddings,
    cells_for_difference,
    unrank_word,
    word_count,
)


_REALIZATION_ATTEMPT_CAP = 10_000


@dataclass(frozen=True)
class PoolPartition:
    reserved: tuple[Cell, ...]
    acquisition: tuple[Cell, ...]

    @property
    def flat_pool_size(self) -> int:
        return len(self.acquisition) * POOL_MULTIPLICITY


@dataclass(frozen=True)
class RawPoolPair:
    pool_index: int
    cell: Cell
    realization_slot: int
    left: bytes
    right: bytes


def partition_cells(key: DeterministicKey) -> PoolPartition:
    reserved = []
    acquisition = []
    for difference in range(D_ACQ + 1):
        cells = cells_for_difference(difference)
        reserve_count = (3 * len(cells)) // 10
        stream = CounterStream(key, ("L1", "pool", "reserve", difference))
        chosen = set(shuffled(cells, stream)[:reserve_count])
        reserved.extend(cell for cell in cells if cell in chosen)
        acquisition.extend(cell for cell in cells if cell not in chosen)
    return PoolPartition(reserved=tuple(reserved), acquisition=tuple(acquisition))


def verify_partition(partition: PoolPartition) -> None:
    if len(partition.reserved) != 7_295:
        raise ValueError("reserved-cell count diverges from the signed spec")
    if len(partition.acquisition) != 17_212:
        raise ValueError("acquisition-cell count diverges from the signed spec")
    if partition.flat_pool_size != 68_848:
        raise ValueError("flat pool size diverges from the signed spec")
    if set(partition.reserved) & set(partition.acquisition):
        raise ValueError("reserved and acquisition cells overlap")


def realize_cell(key: DeterministicKey, cell: Cell) -> tuple[tuple[bytes, bytes], ...]:
    """Materialize the four signed raw-pair slots for one acquisition cell."""
    stream = CounterStream(key, ("L1", "pool", "realize", cell.a, cell.b))
    accepted: list[tuple[bytes, bytes]] = []
    attempts = 0
    while len(accepted) < POOL_MULTIPLICITY:
        attempts += 1
        if attempts > _REALIZATION_ATTEMPT_CAP:
            raise RuntimeError("raw-pool realization exhaustion is design invalidity")
        left_paddings = admissible_paddings(cell.a)
        padding_left = left_paddings[stream.uniform(len(left_paddings))]
        left = unrank_word(
            cell.a,
            padding_left,
            stream.uniform(word_count(cell.a, padding_left)),
        )
        right_paddings = admissible_paddings(cell.b)
        padding_right = right_paddings[stream.uniform(len(right_paddings))]
        right = unrank_word(
            cell.b,
            padding_right,
            stream.uniform(word_count(cell.b, padding_right)),
        )
        candidate = (left, right)
        if candidate in accepted or (cell.difference == 0 and left == right):
            continue
        accepted.append(candidate)
    return tuple(accepted)


def realize_pool_index(
    partition: PoolPartition,
    key: DeterministicKey,
    pool_index: int,
) -> RawPoolPair:
    if not 0 <= pool_index < partition.flat_pool_size:
        raise ValueError("flat pool index is out of range")
    cell_offset, realization_slot = divmod(pool_index, POOL_MULTIPLICITY)
    cell = partition.acquisition[cell_offset]
    left, right = realize_cell(key, cell)[realization_slot]
    return RawPoolPair(pool_index, cell, realization_slot, left, right)
