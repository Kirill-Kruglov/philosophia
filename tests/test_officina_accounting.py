from __future__ import annotations

from pathlib import Path

import pytest

from philosophia.officina.accounting import (
    NANOSECONDS_PER_HOUR,
    TEnvelope,
    TState,
)
from philosophia.officina.canonical import canonical_json
from philosophia.officina.checkpoint import (
    record_not_activated_maintenance,
    record_operational_pause,
    verify_resume,
)
from philosophia.officina.ledger import (
    AppendOnlyLedger,
    LedgerIntegrityError,
    parse_ledger,
)


def test_ledger_is_append_only_hash_chained_and_tamper_evident(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    first = ledger.append(
        event="TEST_ONLY",
        timestamp_utc="2026-07-20T00:00:00Z",
        data={"value": 1},
    )
    second = ledger.append(
        event="TEST_ONLY",
        timestamp_utc="2026-07-20T00:00:01Z",
        data={"value": 2},
    )
    assert second["previous_sha256"] == first["entry_sha256"]
    assert [entry["sequence"] for entry in ledger.entries()] == [0, 1]
    raw = ledger.path.read_bytes().replace(b'"value":1', b'"value":9')
    with pytest.raises(LedgerIntegrityError, match="hash mismatch"):
        parse_ledger(raw)


def test_t_envelope_is_cumulative_additive_and_candidate_bounded() -> None:
    envelope = TEnvelope()
    state = TState().activate("2026-07-20T00:00:00Z")
    state = state.charge_device_nanoseconds(20 * NANOSECONDS_PER_HOUR, envelope)
    state = state.charge_device_nanoseconds(20 * NANOSECONDS_PER_HOUR, envelope)
    assert state.review_due(envelope, "2026-07-20T01:00:00Z")
    state = state.complete_review(envelope, "2026-07-20T01:00:00Z")
    with pytest.raises(ValueError, match="early review"):
        state.complete_review(envelope, "2026-07-21T00:00:00Z")
    for index in range(12):
        state = state.register_candidate(f"{index:064x}", envelope)
    assert state.exhausted(envelope)
    assert state.register_candidate(f"{11:064x}", envelope) == state
    with pytest.raises(ValueError, match="already exhausted"):
        state.register_candidate(f"{12:064x}", envelope)


def test_e3_wall_clock_includes_powered_off_time_and_pause_does_not_reset() -> None:
    envelope = TEnvelope()
    state = TState().activate("2026-07-20T00:00:00Z")
    state = state.charge_device_nanoseconds(3 * NANOSECONDS_PER_HOUR, envelope)
    assert not state.review_due(envelope, "2026-07-21T23:59:59Z")
    assert state.review_due(envelope, "2026-07-22T00:00:00Z")


def test_operational_pause_round_trip_preserves_counters(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    state = TState().activate("2026-07-20T00:00:00Z")
    envelope = TEnvelope()
    state = state.charge_device_nanoseconds(7 * NANOSECONDS_PER_HOUR, envelope)
    state = state.register_candidate("a" * 64, envelope)
    checkpoint = tmp_path / "pause.json"
    record_operational_pause(
        ledger=ledger,
        checkpoint_path=checkpoint,
        state=state,
        artifact_hashes={"model": "a" * 64, "optimizer": "b" * 64},
        timestamp_utc="2026-07-20T08:00:00Z",
        reason="scheduled-power-off",
    )
    restored = verify_resume(ledger=ledger, checkpoint_path=checkpoint)
    assert restored == state
    assert ledger.entries()[-1]["data"]["resets_e3"] is False


def test_resume_refuses_checkpoint_mutation(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    state = TState().activate("2026-07-20T00:00:00Z")
    checkpoint = tmp_path / "pause.json"
    record_operational_pause(
        ledger=ledger,
        checkpoint_path=checkpoint,
        state=state,
        artifact_hashes={},
        timestamp_utc="2026-07-20T01:00:00Z",
        reason="scheduled-power-off",
    )
    value = checkpoint.read_bytes()
    checkpoint.write_bytes(value.replace(b'"author_stopped":false', b'"author_stopped":true'))
    with pytest.raises(ValueError, match="hash mismatch"):
        verify_resume(ledger=ledger, checkpoint_path=checkpoint)


def test_not_activated_maintenance_creates_no_checkpoint(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    record_not_activated_maintenance(
        ledger=ledger,
        timestamp_utc="2026-07-20T01:00:00Z",
        reason="scheduled-power-off",
    )
    assert ledger.entries()[-1]["event"] == "T_NOT_ACTIVATED_AT_MAINTENANCE"
    assert list(tmp_path.glob("*checkpoint*")) == []


def test_t_state_canonical_round_trip() -> None:
    state = TState().activate("2026-07-20T00:00:00Z")
    state = state.charge_device_nanoseconds(NANOSECONDS_PER_HOUR, TEnvelope())
    restored = TState.from_mapping(state.to_mapping())
    assert restored == state
    assert canonical_json(restored.to_mapping()).endswith(b"\n")
