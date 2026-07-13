from __future__ import annotations

from itertools import chain

import pytest

from philosophia.level1.allocation import (
    assign_roles,
    development_pairs,
    registry_pairs,
    sample_outcome_pairs,
)
from philosophia.level1.config import Level1Config
from philosophia.level1.pool import partition_cells, verify_partition
from philosophia.level1.serialization import (
    CounterStream,
    dummy_key,
    encode_domain,
    prf_digest,
    shuffled,
)
from philosophia.level1.world import (
    acquisition_cells,
    cell_from_global_rank,
    cells_for_difference,
    displacement,
    fold,
    global_cell_rank,
    oracle_eq,
    rank_word,
    unrank_word,
    word_count,
)


def test_signed_geometry_and_cell_counts() -> None:
    Level1Config()
    assert len(tuple(acquisition_cells())) == 24_507
    assert len(cells_for_difference(0)) == 257
    assert len(cells_for_difference(125)) == 132


def test_global_cell_rank_round_trip() -> None:
    cells = tuple(acquisition_cells())
    for rank in (0, 1, 256, 257, 12_000, 24_506):
        assert global_cell_rank(cells[rank]) == rank
        assert cell_from_global_rank(rank) == cells[rank]


def test_z_n_oracle_and_word_rank_round_trip() -> None:
    for net, padding in ((0, 1), (3, 2), (-4, 2), (125, 1), (-128, 0)):
        count = word_count(net, padding)
        for rank in sorted(set((0, count // 2, count - 1))):
            word = unrank_word(net, padding, rank)
            assert displacement(word) == net
            assert rank_word(word) == (net, padding, rank)

    assert oracle_eq(b"R" * 33, b"L" * 33, 66)
    assert fold(b"RRL", 66) == 1
    with pytest.raises(ValueError):
        displacement(b"RX")


def test_domain_encoding_and_uniform_one_consumes_nothing() -> None:
    key = dummy_key("serialization")
    assert encode_domain(("L1", "alloc", "sample", 12, 1)).hex().startswith(
        "00024c310005616c6c6f63"
    )
    stream = CounterStream(key, ("L1", "test"))
    assert stream.uniform(1) == 0
    assert stream.counter == 0
    first = stream.digest()
    assert first == prf_digest(key, ("L1", "test"), 0)
    assert stream.counter == 1



def test_prf_and_allocation_golden_values() -> None:
    key = dummy_key("golden")
    assert prf_digest(key, ("L1", "alloc", "sample", 12, 1), 0).hex() == (
        "b222bb60fbd78dc143d271f2665ba9879435d6d08ee57002dfa92bcecef7cc4b"
    )
    allocation_key = dummy_key("allocation")
    assert [pair.slot for pair in development_pairs(allocation_key)] == [0, 2, 13, 19, 20, 27]

def test_descending_fisher_yates_is_reproducible() -> None:
    key = dummy_key("fy")
    first = shuffled(list(range(20)), CounterStream(key, ("L1", "fy")))
    second = shuffled(list(range(20)), CounterStream(key, ("L1", "fy")))
    assert first == second
    assert sorted(first) == list(range(20))


def test_allocation_domains_and_balanced_sampling() -> None:
    key = dummy_key("allocation")
    assert len(registry_pairs()) == 30
    development = development_pairs(key)
    assert [sum(pair.stratum == h for pair in development) for h in (1, 2, 3)] == [2, 2, 2]
    roles = assign_roles(key)
    assert len(roles) == 24
    assert all(abs(item.target - item.donor) == 1 for item in roles)
    for n3 in (12, 15, 18, 21, 24):
        sample = sample_outcome_pairs(key, n3)
        assert len(sample) == n3
        assert [sum(item.pair.stratum == h for item in sample) for h in (1, 2, 3)] == [n3 // 3] * 3


def test_pool_partition_exact_counts_and_determinism() -> None:
    key = dummy_key("pool")
    first = partition_cells(key)
    second = partition_cells(key)
    verify_partition(first)
    assert first == second
    assert len(set(chain(first.reserved, first.acquisition))) == 24_507
