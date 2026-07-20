from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import weakref
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


_ISSUED_TEST_KEYS: weakref.WeakSet[_TestOnlyKey]


class _TestOnlyKey:
    __slots__ = ("_material", "purpose", "__weakref__")

    def __init__(self, *_: object, **__: object) -> None:
        raise PermissionError("test-only PRF keys must come from dummy_key")


_ISSUED_TEST_KEYS = weakref.WeakSet()


def require_test_only_key(key: object) -> _TestOnlyKey:
    if type(key) is not _TestOnlyKey or key not in _ISSUED_TEST_KEYS:
        raise PermissionError("PRF key was not issued by dummy_key")
    if len(key._material) != 32 or not key.purpose:
        raise PermissionError("issued PRF key is malformed")
    return key


def dummy_key(label: str, *, purpose: str = "officina-test") -> _TestOnlyKey:
    if not label or not purpose:
        raise ValueError("dummy key label and purpose must be named")
    material = hashlib.sha256(
        f"OFFICINA-TEST-ONLY/{purpose}/{label}".encode("ascii")
    ).digest()
    key = object.__new__(_TestOnlyKey)
    key._material = material
    key.purpose = purpose
    _ISSUED_TEST_KEYS.add(key)
    return key


def prf_digest(key: object, domain: Domain, counter: int) -> bytes:
    issued = require_test_only_key(key)
    if type(counter) is not int or not 0 <= counter < (1 << 64):
        raise ValueError("PRF counter must be a uint64 integer")
    return hmac.new(
        issued._material,
        encode_domain(domain) + _uint64_be(counter),
        hashlib.sha256,
    ).digest()


@dataclass
class CounterStream:
    key: object
    domain: Domain
    counter: int = 0

    def __post_init__(self) -> None:
        require_test_only_key(self.key)
        if type(self.counter) is not int or not 0 <= self.counter < (1 << 64):
            raise ValueError("counter must be a uint64 integer")

    def digest(self) -> bytes:
        value = prf_digest(self.key, self.domain, self.counter)
        self.counter += 1
        return value

    def uniform(self, modulus: int) -> int:
        if type(modulus) is not int or modulus <= 0:
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
