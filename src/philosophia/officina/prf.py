from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
from typing import Sequence, TypeVar


DomainComponent = str | int
Domain = tuple[DomainComponent, ...]
T = TypeVar("T")
_UINT256 = 1 << 256


def _uint16_be(value: int) -> bytes:
    if not 0 <= value < (1 << 16):
        raise ValueError("value does not fit uint16")
    return value.to_bytes(2, "big")


def _uint64_be(value: int) -> bytes:
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
    return _uint16_be(len(payload)) + payload


def encode_domain(domain: Sequence[DomainComponent]) -> bytes:
    if not domain:
        raise ValueError("PRF domain must not be empty")
    return b"".join(encode_component(component) for component in domain)


@dataclass(frozen=True)
class ProvidedKey:
    """Caller-provided key material; this module never obtains entropy."""

    material: bytes
    purpose: str
    test_only: bool

    def __post_init__(self) -> None:
        if len(self.material) != 32:
            raise ValueError("PRF keys are exactly 32 bytes")
        if not self.purpose:
            raise ValueError("key purpose must be named")


def dummy_key(label: str, *, purpose: str = "officina-test") -> ProvidedKey:
    material = hashlib.sha256(
        f"OFFICINA-TEST-ONLY/{purpose}/{label}".encode("ascii")
    ).digest()
    return ProvidedKey(material=material, purpose=purpose, test_only=True)


def prf_digest(key: ProvidedKey, domain: Domain, counter: int) -> bytes:
    return hmac.new(
        key.material,
        encode_domain(domain) + _uint64_be(counter),
        hashlib.sha256,
    ).digest()


@dataclass
class CounterStream:
    key: ProvidedKey
    domain: Domain
    counter: int = 0

    def __post_init__(self) -> None:
        if self.counter < 0:
            raise ValueError("counter must be non-negative")

    def digest(self) -> bytes:
        value = prf_digest(self.key, self.domain, self.counter)
        self.counter += 1
        return value

    def uniform(self, modulus: int) -> int:
        if modulus <= 0:
            raise ValueError("uniform modulus must be positive")
        if modulus == 1:
            return 0
        limit = (_UINT256 // modulus) * modulus
        while True:
            value = int.from_bytes(self.digest(), "big")
            if value < limit:
                return value % modulus


def shuffled(values: Sequence[T], stream: CounterStream) -> list[T]:
    result = list(values)
    for index in range(len(result) - 1, 0, -1):
        swap = stream.uniform(index + 1)
        result[index], result[swap] = result[swap], result[index]
    return result
