from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from philosophia.officina.accounting import TEnvelope, TState
from philosophia.officina.canonical import canonical_json, sha256_file
from philosophia.officina.interlock import test_only_capability as make_test_capability
from philosophia.officina.ledger import AppendOnlyLedger
from philosophia.officina.quarantine import Surface
from philosophia.officina.world import (
    CH1_TOKEN,
    CH2_TOKEN,
    LAMBDA,
    SIGNED_CONTRACT_SHA256,
    SIGNED_WP3_SIGNATURE_SHA256,
    TestWorldCapability as WorldCapabilityForTest,
    evaluate_test_query,
    frame_bytes,
    frame_mapping,
    frame_sha256,
    record_test_t_contact,
    test_world_capability as make_test_world_capability,
    verify_frame_bytes,
)


REPO = Path(__file__).resolve().parent.parent


def _capability(surface: Surface):
    return make_test_world_capability(
        surface,
        capability=make_test_capability("world-tests"),
        purpose="world-tests",
    )


def test_signed_contract_and_signature_hashes_are_exact() -> None:
    assert SIGNED_CONTRACT_SHA256 == sha256_file(
        REPO / "successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md"
    )
    assert SIGNED_WP3_SIGNATURE_SHA256 == sha256_file(
        REPO / "successor/OFFICINA_WP3_SIGNATURE.md"
    )


def test_frame_is_canonical_complete_disjoint_and_selected() -> None:
    value = frame_mapping()
    assert value["ch1_token"] == CH1_TOKEN
    assert value["ch2_token"] == CH2_TOKEN
    assert value["band"] == {"n_min": 26, "n_max": 65}
    assert value["lambda"] == LAMBDA == 140
    assert value["c_block_ps"] == [1, 3, 5, 6, 8, 10, 11, 13, 15, 16, 18, 20]
    assert value["q_worlds"] == [
        28, 29, 32, 33, 38, 39, 42, 43,
        48, 49, 52, 53, 58, 59, 62, 63,
    ]
    assert len(value["blocks"]) == 20
    assert verify_frame_bytes(frame_bytes()) == value
    assert frame_sha256() == "cc54cd2e6bf6f0e248008a4d5b64f491340e7fa8673d377c6419a6781d33170b"


def test_frame_verifier_refuses_noncanonical_and_mutated_payloads() -> None:
    value = frame_mapping()
    with pytest.raises(ValueError, match="not canonical"):
        verify_frame_bytes(json.dumps(value).encode("ascii"))
    value["q_worlds"] = [28]
    with pytest.raises(ValueError, match="differs"):
        verify_frame_bytes(canonical_json(value))


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (canonical_json({"u": "RL", "v": "R"}), canonical_json(0)),
        (canonical_json({"u": "", "v": ""}), canonical_json(1)),
        (b"not-json\n", canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (b'{"u":"R", "v":"L"}\n', canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (b'{"u":"R","u":"L","v":"R"}\n', canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (canonical_json({"u": "R", "v": 1}), canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (canonical_json({"u": "R_", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
        (canonical_json({"u": "R|", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
        (canonical_json({"u": "R" * (LAMBDA + 1), "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_LENGTH"})),
        (canonical_json({"u": "R" * (LAMBDA + 1) + "_", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
    ],
)
def test_oracle_wire_classifier_is_total_ordered_and_exact(
    raw: bytes, expected: bytes
) -> None:
    assert evaluate_test_query(
        capability=_capability(Surface.T), modulus=10, raw_query=raw
    ) == expected


def test_oracle_matches_cyclic_equality_and_surface_gates() -> None:
    query = canonical_json({"u": "R" * 10, "v": ""})
    assert evaluate_test_query(
        capability=_capability(Surface.T), modulus=10, raw_query=query
    ) == canonical_json(1)
    assert evaluate_test_query(
        capability=_capability(Surface.T), modulus=11, raw_query=query
    ) == canonical_json(0)
    with pytest.raises(PermissionError, match="outside the T"):
        evaluate_test_query(
            capability=_capability(Surface.T), modulus=26, raw_query=query
        )
    assert evaluate_test_query(
        capability=_capability(Surface.Q), modulus=28, raw_query=query
    ) in {canonical_json(0), canonical_json(1)}
    with pytest.raises(PermissionError, match="outside the Q"):
        evaluate_test_query(
            capability=_capability(Surface.Q), modulus=26, raw_query=query
        )
    assert evaluate_test_query(
        capability=_capability(Surface.C), modulus=26, raw_query=query
    ) in {canonical_json(0), canonical_json(1)}


def test_world_capability_is_test_only_exact_and_unforgeable() -> None:
    with pytest.raises(PermissionError, match="factory"):
        WorldCapabilityForTest(Surface.T, "test-only:forged", object())
    forged = SimpleNamespace(surface=Surface.T, purpose="test-only:forged")
    with pytest.raises(PermissionError, match="issued"):
        evaluate_test_query(
            capability=forged,  # type: ignore[arg-type]
            modulus=10,
            raw_query=canonical_json({"u": "", "v": ""}),
        )
    with pytest.raises(ValueError, match="T, Q, or C"):
        _capability(Surface.TEST)


def test_test_contact_hook_charges_and_logs_without_real_activation(
    tmp_path: Path,
) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    state = TState().activate("2026-07-21T00:00:00Z")
    query = canonical_json({"u": "R" * 10, "v": ""})
    next_state, response, entry = record_test_t_contact(
        capability=_capability(Surface.T),
        modulus=10,
        raw_query=query,
        device_nanoseconds=123,
        timestamp_utc="2026-07-21T00:00:01Z",
        state=state,
        envelope=TEnvelope(),
        ledger=ledger,
    )
    assert response == canonical_json(1)
    assert next_state.device_nanoseconds == 123
    assert entry["event"] == "T_TEST_ONLY_WORLD_CONTACT"
    assert entry["data"]["test_only"] is True
    assert entry["data"]["scientific_outcome"] is False
    assert len(ledger.entries()) == 1
    with pytest.raises(ValueError, match="positive integer"):
        record_test_t_contact(
            capability=_capability(Surface.T),
            modulus=10,
            raw_query=query,
            device_nanoseconds=True,
            timestamp_utc="2026-07-21T00:00:02Z",
            state=next_state,
            envelope=TEnvelope(),
            ledger=ledger,
        )
    with pytest.raises(PermissionError, match="T test capability"):
        record_test_t_contact(
            capability=_capability(Surface.Q),
            modulus=28,
            raw_query=query,
            device_nanoseconds=1,
            timestamp_utc="2026-07-21T00:00:02Z",
            state=next_state,
            envelope=TEnvelope(),
            ledger=ledger,
        )
