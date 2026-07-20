"""Signed WP-3 world substrate with no real execution capability.

The public surface is deterministic frame construction plus explicitly
test-only oracle contacts. A later, separately reviewed T-activation driver must
provide any real capability and durable production transaction.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from typing import Mapping

from .accounting import TEnvelope, TState, parse_utc
from .canonical import canonical_json, sha256_bytes
from .interlock import TestOnlyCapability, require_test_only
from .ledger import AppendOnlyLedger
from .quarantine import Surface


CONSTRUCT_ID = "officina.construct.cyclic-equality.v1"
FRAME_SCHEMA = "officina.frame.v1"
CONTACT_SCHEMA = "philosophia.officina.test-t-contact.v1"
SIGNED_CONTRACT_SHA256 = (
    "6085d9b695e2a74c0b46c56bc61971d29dd6b646a5ae70068e33c93090735c7d"
)
SIGNED_WP3_SIGNATURE_SHA256 = (
    "24fd12b61d2fb75c38adee4bebda498f6ca67aade5e08b412c39530289086781"
)
CH1_TOKEN = "I_SELECT_OFFICINA_FRAME_BAND_LOW"
CH2_TOKEN = "I_SELECT_OFFICINA_SPLIT_C_RICH"
N_MIN = 26
N_MAX = 65
LAMBDA = 140
STRATUM_COUNT = 4
BLOCKS_PER_STRATUM = 5
C_POSITIONS = frozenset({1, 3, 5})
Q_POSITIONS = frozenset({2, 4})
T_DEV_BANDS = ((10, 25), (166, 205))
PREDECESSOR_BAND = (66, 125)


class RefusalCode(str, Enum):
    STRUCTURE = "MALFORMED_QUERY_STRUCTURE"
    BYTE = "MALFORMED_QUERY_BYTE"
    LENGTH = "MALFORMED_QUERY_LENGTH"


_WORLD_TOKEN = object()


@dataclass(frozen=True)
class TestWorldCapability:
    """Test-only surface authority; it cannot be promoted to real execution."""

    surface: Surface
    purpose: str
    _token: object

    def __post_init__(self) -> None:
        if self._token is not _WORLD_TOKEN:
            raise PermissionError("world capability must use the test-only factory")
        if self.surface not in {Surface.T, Surface.Q, Surface.C}:
            raise ValueError("test world capability requires T, Q, or C surface")
        if not self.purpose.startswith("test-only:"):
            raise PermissionError("world capability purpose must be test-only")


def test_world_capability(
    surface: Surface, *, capability: TestOnlyCapability, purpose: str
) -> TestWorldCapability:
    if not purpose:
        raise ValueError("test world capability purpose must be named")
    require_test_only(capability)
    if type(surface) is not Surface:
        raise TypeError("world surface must be an exact Surface")
    return TestWorldCapability(surface, f"test-only:{purpose}", _WORLD_TOKEN)


def _require_world_capability(capability: TestWorldCapability) -> None:
    if (
        type(capability) is not TestWorldCapability
        or capability._token is not _WORLD_TOKEN
        or not capability.purpose.startswith("test-only:")
    ):
        raise PermissionError("world operation requires an issued test-only capability")


def _block(h: int, j: int) -> tuple[int, int]:
    p = BLOCKS_PER_STRATUM * (h - 1) + j
    lower = N_MIN + 2 * (p - 1)
    return lower, lower + 1


def _frame_blocks() -> list[dict[str, object]]:
    blocks: list[dict[str, object]] = []
    for h in range(1, STRATUM_COUNT + 1):
        for j in range(1, BLOCKS_PER_STRATUM + 1):
            p = BLOCKS_PER_STRATUM * (h - 1) + j
            assignment = "C" if j in C_POSITIONS else "Q"
            blocks.append(
                {
                    "assignment": assignment,
                    "h": h,
                    "j": j,
                    "members": list(_block(h, j)),
                    "p": p,
                }
            )
    return blocks


def _validate_frame(blocks: list[dict[str, object]]) -> None:
    if len(blocks) != STRATUM_COUNT * BLOCKS_PER_STRATUM:
        raise ValueError("frame block cardinality differs")
    c_worlds: set[int] = set()
    q_worlds: set[int] = set()
    c_counts = {h: 0 for h in range(1, STRATUM_COUNT + 1)}
    q_counts = {h: 0 for h in range(1, STRATUM_COUNT + 1)}
    for expected_p, block in enumerate(blocks, start=1):
        expected_h = (expected_p - 1) // BLOCKS_PER_STRATUM + 1
        expected_j = (expected_p - 1) % BLOCKS_PER_STRATUM + 1
        expected_assignment = "C" if expected_j in C_POSITIONS else "Q"
        expected_block = {
            "assignment": expected_assignment,
            "h": expected_h,
            "j": expected_j,
            "members": list(_block(expected_h, expected_j)),
            "p": expected_p,
        }
        if block != expected_block:
            raise ValueError("frame block differs from the governing formula")
        members = block["members"]
        h = block["h"]
        if not isinstance(members, list) or len(members) != 2 or type(h) is not int:
            raise ValueError("frame block values are malformed")
        target = c_worlds if block["assignment"] == "C" else q_worlds
        target.update(members)
        counts = c_counts if block["assignment"] == "C" else q_counts
        counts[h] += 1
    expected = set(range(N_MIN, N_MAX + 1))
    t_worlds = {
        modulus
        for lower, upper in T_DEV_BANDS
        for modulus in range(lower, upper + 1)
    }
    predecessor = set(range(PREDECESSOR_BAND[0], PREDECESSOR_BAND[1] + 1))
    if c_worlds & q_worlds or c_worlds | q_worlds != expected:
        raise ValueError("frame Q/C partition differs")
    if expected & t_worlds or expected & predecessor or t_worlds & predecessor:
        raise ValueError("frame, T, and predecessor supports overlap")
    if set(c_counts.values()) != {3} or set(q_counts.values()) != {2}:
        raise ValueError("frame stratum balance differs")
    if len(c_worlds) != 24 or len(q_worlds) != 16:
        raise ValueError("frame world cardinalities differ")


def frame_mapping() -> dict[str, object]:
    blocks = _frame_blocks()
    _validate_frame(blocks)
    return {
        "band": {"n_max": N_MAX, "n_min": N_MIN},
        "blocks": blocks,
        "c_block_ps": [
            block["p"] for block in blocks if block["assignment"] == "C"
        ],
        "ch1_token": CH1_TOKEN,
        "ch2_token": CH2_TOKEN,
        "construct": CONSTRUCT_ID,
        "contract_sha256": SIGNED_CONTRACT_SHA256,
        "lambda": LAMBDA,
        "q_worlds": sorted(_surface_moduli(Surface.Q)),
        "schema": FRAME_SCHEMA,
        "scientific_outcome": False,
        "strata": {
            "blocks_per_stratum": BLOCKS_PER_STRATUM,
            "count": STRATUM_COUNT,
        },
        "t_dev_bands": [list(band) for band in T_DEV_BANDS],
    }


def frame_bytes() -> bytes:
    return canonical_json(frame_mapping())


def frame_sha256() -> str:
    return sha256_bytes(frame_bytes())


def verify_frame_bytes(payload: bytes) -> Mapping[str, object]:
    if type(payload) is not bytes:
        raise TypeError("frame payload must be bytes")
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("frame payload is not JSON") from error
    if not isinstance(value, dict) or canonical_json(value) != payload:
        raise ValueError("frame payload is not canonical JSON")
    if canonical_json(value) != frame_bytes():
        raise ValueError("frame payload differs from the signed frame")
    return value


def _surface_moduli(surface: Surface) -> frozenset[int]:
    if surface is Surface.T:
        return frozenset(
            modulus
            for lower, upper in T_DEV_BANDS
            for modulus in range(lower, upper + 1)
        )
    blocks = _frame_blocks()
    assignment = "Q" if surface is Surface.Q else "C"
    return frozenset(
        member
        for block in blocks
        if block["assignment"] == assignment
        for member in block["members"]  # type: ignore[union-attr]
    )


class _DuplicateKey(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKey(key)
        value[key] = item
    return value


def _refusal(code: RefusalCode) -> bytes:
    return canonical_json({"refusal": code.value})


def _decode_query(raw: bytes) -> tuple[str, str] | bytes:
    try:
        value = json.loads(raw, object_pairs_hook=_unique_object)
        if (
            not isinstance(value, dict)
            or set(value) != {"u", "v"}
            or type(value["u"]) is not str
            or type(value["v"]) is not str
            or canonical_json(value) != raw
        ):
            return _refusal(RefusalCode.STRUCTURE)
    except (
        UnicodeDecodeError,
        json.JSONDecodeError,
        _DuplicateKey,
        ValueError,
        TypeError,
    ):
        return _refusal(RefusalCode.STRUCTURE)
    u, v = value["u"], value["v"]
    if any(character not in {"R", "L"} for character in u + v):
        return _refusal(RefusalCode.BYTE)
    if len(u) > LAMBDA or len(v) > LAMBDA:
        return _refusal(RefusalCode.LENGTH)
    return u, v


def _oracle_answer(modulus: int, u: str, v: str) -> int:
    displacement_u = u.count("R") - u.count("L")
    displacement_v = v.count("R") - v.count("L")
    return int((displacement_u - displacement_v) % modulus == 0)


def evaluate_test_query(
    *, capability: TestWorldCapability, modulus: int, raw_query: bytes
) -> bytes:
    _require_world_capability(capability)
    if type(modulus) is not int or modulus not in _surface_moduli(capability.surface):
        raise PermissionError(
            f"modulus is outside the {capability.surface.value} test surface"
        )
    if type(raw_query) is not bytes:
        raise TypeError("raw query must be bytes")
    decoded = _decode_query(raw_query)
    if isinstance(decoded, bytes):
        return decoded
    return canonical_json(_oracle_answer(modulus, *decoded))


def record_test_t_contact(
    *,
    capability: TestWorldCapability,
    modulus: int,
    raw_query: bytes,
    device_nanoseconds: int,
    timestamp_utc: str,
    state: TState,
    envelope: TEnvelope,
    ledger: AppendOnlyLedger,
) -> tuple[TState, bytes, dict[str, object]]:
    """Exercise accounting/logging on temporary test ledgers only."""

    _require_world_capability(capability)
    if capability.surface is not Surface.T:
        raise PermissionError("T contact logging requires a T test capability")
    if type(device_nanoseconds) is not int or device_nanoseconds <= 0:
        raise ValueError("test contact device charge must be a positive integer")
    parse_utc(timestamp_utc)
    response = evaluate_test_query(
        capability=capability, modulus=modulus, raw_query=raw_query
    )
    next_state = state.charge_device_nanoseconds(device_nanoseconds, envelope)
    entry = ledger.append(
        event="T_TEST_ONLY_WORLD_CONTACT",
        timestamp_utc=timestamp_utc,
        data={
            "construct": CONSTRUCT_ID,
            "device_nanoseconds": device_nanoseconds,
            "modulus": modulus,
            "query_sha256": sha256_bytes(raw_query),
            "response_sha256": sha256_bytes(response),
            "schema": CONTACT_SCHEMA,
            "scientific_outcome": False,
            "t_state": next_state.to_mapping(),
            "test_only": True,
        },
    )
    return next_state, response, entry
