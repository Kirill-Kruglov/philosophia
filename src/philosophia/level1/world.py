from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Iterator

from .config import A_WORD, D_ACQ, MAX_PADDING, MAX_WORD_LENGTH, validate_modulus


R = 0x52
L = 0x4C
SEP = 0x7C
PAD = 0x5F
WORD_TOKENS = frozenset((R, L))


def displacement(word: bytes) -> int:
    if any(token not in WORD_TOKENS for token in word):
        raise ValueError("word contains a non R/L token")
    return word.count(R) - word.count(L)


def fold(word: bytes, modulus: int, *, origin: int = 0) -> int:
    validate_modulus(modulus)
    return (origin + displacement(word)) % modulus


def oracle_eq(left: bytes, right: bytes, modulus: int) -> bool:
    return fold(left, modulus) == fold(right, modulus)


@dataclass(frozen=True, order=True)
class Cell:
    difference: int
    a: int
    b: int

    def __post_init__(self) -> None:
        if self.a < self.b:
            raise ValueError("cell orientation must satisfy a >= b")
        if self.difference != self.a - self.b:
            raise ValueError("cell difference does not match endpoints")

    @property
    def identity(self) -> tuple[int, int]:
        return (self.a, self.b)


def cells_for_difference(difference: int, *, a_word: int = A_WORD) -> tuple[Cell, ...]:
    if not 0 <= difference <= D_ACQ:
        raise ValueError(f"difference must be in [0, {D_ACQ}]")
    return tuple(
        Cell(difference=difference, a=b + difference, b=b)
        for b in range(-a_word, a_word - difference + 1)
    )


def acquisition_cells(*, a_word: int = A_WORD) -> Iterator[Cell]:
    for difference in range(D_ACQ + 1):
        yield from cells_for_difference(difference, a_word=a_word)


def admissible_paddings(
    net_displacement: int,
    *,
    max_padding: int = MAX_PADDING,
    max_length: int = MAX_WORD_LENGTH,
) -> tuple[int, ...]:
    if abs(net_displacement) > A_WORD:
        raise ValueError("word displacement exceeds A_word")
    return tuple(
        padding
        for padding in range(max_padding + 1)
        if abs(net_displacement) + 2 * padding <= max_length
    )


def word_length(net_displacement: int, padding: int) -> int:
    if padding not in admissible_paddings(net_displacement):
        raise ValueError("padding is not admissible")
    return abs(net_displacement) + 2 * padding


def word_count(net_displacement: int, padding: int) -> int:
    length = word_length(net_displacement, padding)
    right_count = (length + net_displacement) // 2
    return comb(length, right_count)


def unrank_word(net_displacement: int, padding: int, rank: int) -> bytes:
    length = word_length(net_displacement, padding)
    right_remaining = (length + net_displacement) // 2
    total = comb(length, right_remaining)
    if not 0 <= rank < total:
        raise ValueError("word rank is out of range")

    output = bytearray()
    for position in range(length):
        remaining = length - position - 1
        right_first = comb(remaining, right_remaining - 1) if right_remaining else 0
        if right_remaining and rank < right_first:
            output.append(R)
            right_remaining -= 1
        else:
            output.append(L)
            rank -= right_first
    return bytes(output)


def rank_word(word: bytes) -> tuple[int, int, int]:
    net_displacement = displacement(word)
    extra = len(word) - abs(net_displacement)
    if extra < 0 or extra % 2:
        raise ValueError("word length and displacement are inconsistent")
    padding = extra // 2
    if padding not in admissible_paddings(net_displacement):
        raise ValueError("word is outside the frozen universe")

    right_remaining = word.count(R)
    rank = 0
    for position, token in enumerate(word):
        remaining = len(word) - position - 1
        if token == L and right_remaining:
            rank += comb(remaining, right_remaining - 1)
        elif token == R:
            right_remaining -= 1
    return net_displacement, padding, rank
