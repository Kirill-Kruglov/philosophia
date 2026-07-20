from __future__ import annotations

from dataclasses import dataclass, field
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
        tag = b"i"
        payload = str(component).encode("ascii")
    elif isinstance(component, str):
        tag = b"s"
        payload = component.encode("utf-8")
    else:
        raise TypeError(f"unsupported domain component: {type(component)!r}")
    return tag + _uint16_be(len(payload)) + payload


def encode_domain(domain: Sequence[DomainComponent]) -> bytes:
    if not domain:
        raise ValueError("PRF domain must not be empty")
    return b"".join(encode_component(component) for component in domain)


_TEST_KEY_TOKEN = object()


@dataclass(frozen=True)
class TestOnlyKey:
    """A deterministic dummy key. WP-1/WP-2 expose no production key type."""

    material: bytes
    purpose: str
    _token: object = field(repr=False, compare=False)

    def __post_init__(self) -> None:
        if len(self.material) != 32:
            raise ValueError("PRF keys are exactly 32 bytes")
        if not self.purpose:
            raise ValueError("key purpose must be named")
        if self._token is not _TEST_KEY_TOKEN:
            raise PermissionError("test-only PRF keys must come from dummy_key")


def dummy_key(label: str, *, purpose: str = "officina-test") -> TestOnlyKey:
    material = hashlib.sha256(
        f"OFFICINA-TEST-ONLY/{purpose}/{label}".encode("ascii")
    ).digest()
    return TestOnlyKey(material=material, purpose=purpose, _token=_TEST_KEY_TOKEN)


def prf_digest(key: TestOnlyKey, domain: Domain, counter: int) -> bytes:
    return hmac.new(
        key.material,
        encode_domain(domain) + _uint64_be(counter),
        hashlib.sha256,
    ).digest()


@dataclass
class CounterStream:
    key: TestOnlyKey
    domain: Domain
    counter: int = 0

    def __post_init__(self) -> None:
        if self.key._token is not _TEST_KEY_TOKEN:
            raise PermissionError("only test-only PRF keys exist before WP-6")
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
