from __future__ import annotations

from dataclasses import dataclass

from .config import D_ACQ, POOL_MULTIPLICITY
from .serialization import CounterStream, DeterministicKey, shuffled
from .world import Cell, cells_for_difference


@dataclass(frozen=True)
class PoolPartition:
    reserved: tuple[Cell, ...]
    acquisition: tuple[Cell, ...]

    @property
    def flat_pool_size(self) -> int:
        return len(self.acquisition) * POOL_MULTIPLICITY


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
