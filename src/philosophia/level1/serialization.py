from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
from typing import Iterable, Sequence, TypeVar


DomainComponent = str | int
Domain = tuple[DomainComponent, ...]
T = TypeVar("T")
_UINT256 = 1 << 256


def uint16_be(value: int) -> bytes:
    if not 0 <= value < (1 << 16):
        raise ValueError("value does not fit uint16")
    return value.to_bytes(2, "big")


def uint32_be(value: int) -> bytes:
    if not 0 <= value < (1 << 32):
        raise ValueError("value does not fit uint32")
    return value.to_bytes(4, "big")


def uint64_be(value: int) -> bytes:
    if not 0 <= value < (1 << 64):
        raise ValueError("value does not fit uint64")
    return value.to_bytes(8, "big")


def encode_component(component: DomainComponent) -> bytes:
    if isinstance(component, bool):
        raise TypeError("booleans are not domain integers")
    if isinstance(component, int):
        payload = str(component).encode("ascii")
    elif isinstance(component, str):
        payload = component.encode("utf-8")
    else:
        raise TypeError(f"unsupported domain component: {type(component)!r}")
    return uint16_be(len(payload)) + payload


def encode_domain(domain: Sequence[DomainComponent]) -> bytes:
    if not domain:
        raise ValueError("PRF domain must not be empty")
    return b"".join(encode_component(component) for component in domain)


@dataclass(frozen=True)
class DeterministicKey:
    """A provided key, never entropy obtained by this package."""

    material: bytes
    purpose: str
    test_only: bool

    def __post_init__(self) -> None:
        if len(self.material) != 32:
            raise ValueError("Level 1 PRF keys are exactly 32 bytes")
        if not self.purpose:
            raise ValueError("key purpose must be named")


def dummy_key(label: str, *, purpose: str = "public-root") -> DeterministicKey:
    material = hashlib.sha256(f"L1-TEST-ONLY/{purpose}/{label}".encode("ascii")).digest()
    return DeterministicKey(material=material, purpose=purpose, test_only=True)


def prf_digest(key: DeterministicKey, domain: Domain, counter: int) -> bytes:
    return hmac.new(
        key.material,
        encode_domain(domain) + uint64_be(counter),
        hashlib.sha256,
    ).digest()


@dataclass
class CounterStream:
    key: DeterministicKey
    domain: Domain
    counter: int = 0

    def __post_init__(self) -> None:
        if self.counter < 0:
            raise ValueError("counter must be non-negative")

    def digest(self) -> bytes:
        digest = prf_digest(self.key, self.domain, self.counter)
        self.counter += 1
        return digest

    def uniform(self, modulus: int) -> int:
        if modulus <= 0:
            raise ValueError("uniform modulus must be positive")
        if modulus == 1:
            return 0
        limit = (_UINT256 // modulus) * modulus
        while True:
            value = int.from_bytes(self.digest(), "big", signed=False)
            if value < limit:
                return value % modulus


def shuffled(values: Sequence[T], stream: CounterStream) -> list[T]:
    result = list(values)
    for index in range(len(result) - 1, 0, -1):
        swap = stream.uniform(index + 1)
        result[index], result[swap] = result[swap], result[index]
    return result


def sample_without_replacement(
    values: Sequence[T], count: int, stream: CounterStream
) -> list[T]:
    if not 0 <= count <= len(values):
        raise ValueError("sample size exceeds population")
    return shuffled(values, stream)[:count]


def serialize_byte_list(values: Iterable[bytes]) -> bytes:
    material = list(values)
    return uint32_be(len(material)) + b"".join(
        uint32_be(len(value)) + value for value in material
    )
