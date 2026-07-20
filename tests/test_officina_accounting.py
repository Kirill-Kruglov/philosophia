from __future__ import annotations

import json
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
    write_pause_checkpoint,
)
from philosophia.officina.ledger import (
    AppendOnlyLedger,
    LedgerIntegrityError,
    parse_ledger,
)


def _active_state() -> TState:
    return TState().activate("2026-07-20T00:00:00Z")


def _pause(
    tmp_path: Path,
    *,
    state: TState | None = None,
    artifacts: dict[str, Path] | None = None,
) -> tuple[AppendOnlyLedger, Path, TState]:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    active = state or _active_state()
    checkpoint = tmp_path / "pause.json"
    record_operational_pause(
        ledger=ledger,
        checkpoint_path=checkpoint,
        state=active,
        artifact_paths=artifacts or {},
        timestamp_utc="2026-07-20T08:00:00Z",
        reason="scheduled-power-off",
    )
    return ledger, checkpoint, active


def test_ledger_is_hash_chained_and_external_head_blocks_suffix_truncation(
    tmp_path: Path,
) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    first = ledger.append(
        event="TEST_ONLY", timestamp_utc="2026-07-20T00:00:00Z", data={"value": 1}
    )
    second = ledger.append(
        event="TEST_ONLY", timestamp_utc="2026-07-20T00:00:01Z", data={"value": 2}
    )
    assert second["previous_sha256"] == first["entry_sha256"]
    assert [entry["sequence"] for entry in ledger.entries()] == [0, 1]
    lines = ledger.path.read_bytes().splitlines(keepends=True)
    ledger.path.write_bytes(b"".join(lines[:-1]))
    with pytest.raises(LedgerIntegrityError, match="external head mismatch"):
        ledger.entries()


def test_ledger_rejects_content_mutation_and_partial_suffix(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    ledger.append(
        event="TEST_ONLY", timestamp_utc="2026-07-20T00:00:00Z", data={"value": 1}
    )
    raw = ledger.path.read_bytes().replace(b'"value":1', b'"value":9')
    with pytest.raises(LedgerIntegrityError, match="hash mismatch"):
        parse_ledger(raw)
    with pytest.raises(LedgerIntegrityError):
        parse_ledger(ledger.path.read_bytes() + b"- {")


def test_t_envelope_is_cumulative_additive_and_candidate_bounded() -> None:
    envelope = TEnvelope()
    state = _active_state()
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
    state = _active_state().charge_device_nanoseconds(
        3 * NANOSECONDS_PER_HOUR, envelope
    )
    assert not state.review_due(envelope, "2026-07-21T23:59:59Z")
    assert state.review_due(envelope, "2026-07-22T00:00:00Z")


def test_operational_pause_recomputes_artifacts_and_preserves_counters(
    tmp_path: Path,
) -> None:
    model = tmp_path / "model.bin"
    optimizer = tmp_path / "optimizer.bin"
    model.write_bytes(b"model-state")
    optimizer.write_bytes(b"optimizer-state")
    envelope = TEnvelope()
    state = _active_state().charge_device_nanoseconds(
        7 * NANOSECONDS_PER_HOUR, envelope
    ).register_candidate("a" * 64, envelope)
    ledger, checkpoint, _ = _pause(
        tmp_path, state=state, artifacts={"model": model, "optimizer": optimizer}
    )
    gate = verify_resume(
        ledger=ledger,
        checkpoint_path=checkpoint,
        envelope=envelope,
        timestamp_utc="2026-07-20T09:00:00Z",
    )
    assert gate.admit_work() == state
    assert ledger.entries()[-1]["data"]["resets_e3"] is False
    records = json.loads(checkpoint.read_bytes())["artifacts"]
    assert records["model"]["path"] == str(model.resolve())


@pytest.mark.parametrize("failure", ["mutation", "deletion", "substitution"])
def test_resume_refuses_artifact_identity_failures(tmp_path: Path, failure: str) -> None:
    artifact = tmp_path / "state.bin"
    artifact.write_bytes(b"original")
    ledger, checkpoint, _ = _pause(tmp_path, artifacts={"state": artifact})
    if failure == "mutation":
        artifact.write_bytes(b"changed")
    elif failure == "deletion":
        artifact.unlink()
    else:
        original = artifact.resolve()
        artifact.rename(tmp_path / "moved.bin")
        artifact.symlink_to(tmp_path / "moved.bin")
        assert artifact.resolve() != original
    with pytest.raises(ValueError, match="artifact"):
        verify_resume(
            ledger=ledger,
            checkpoint_path=checkpoint,
            envelope=TEnvelope(),
            timestamp_utc="2026-07-20T09:00:00Z",
        )


def test_resume_refuses_checkpoint_mutation(tmp_path: Path) -> None:
    ledger, checkpoint, _ = _pause(tmp_path)
    value = checkpoint.read_bytes()
    checkpoint.write_bytes(value.replace(b'"author_stopped":false', b'"author_stopped":true'))
    with pytest.raises(ValueError, match="hash mismatch"):
        verify_resume(
            ledger=ledger,
            checkpoint_path=checkpoint,
            envelope=TEnvelope(),
            timestamp_utc="2026-07-20T09:00:00Z",
        )


def test_checkpoint_before_ledger_and_stale_checkpoint_fail_closed(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    checkpoint = tmp_path / "orphan.json"
    write_pause_checkpoint(
        path=checkpoint,
        state=_active_state(),
        artifact_paths={},
        ledger_head_before="0" * 64,
    )
    with pytest.raises(ValueError, match="does not end"):
        verify_resume(
            ledger=ledger,
            checkpoint_path=checkpoint,
            envelope=TEnvelope(),
            timestamp_utc="2026-07-20T09:00:00Z",
        )

    other = tmp_path / "complete"
    other.mkdir()
    complete_ledger, complete_checkpoint, _ = _pause(other)
    complete_ledger.append(
        event="TEST_LATER_EVENT",
        timestamp_utc="2026-07-20T08:01:00Z",
        data={"scientific_outcome": False},
    )
    with pytest.raises(ValueError, match="does not end"):
        verify_resume(
            ledger=complete_ledger,
            checkpoint_path=complete_checkpoint,
            envelope=TEnvelope(),
            timestamp_utc="2026-07-20T09:00:00Z",
        )


def test_overdue_resume_blocks_work_until_durable_review(tmp_path: Path) -> None:
    ledger, checkpoint, state = _pause(tmp_path)
    gate = verify_resume(
        ledger=ledger,
        checkpoint_path=checkpoint,
        envelope=TEnvelope(),
        timestamp_utc="2026-07-22T00:00:00Z",
    )
    assert gate.review_required is True
    with pytest.raises(PermissionError, match="blocks"):
        gate.admit_work()
    with pytest.raises(ValueError, match="not available"):
        gate.state.charge_device_nanoseconds(NANOSECONDS_PER_HOUR, TEnvelope())
    with pytest.raises(ValueError, match="not available"):
        gate.state.register_candidate("b" * 64, TEnvelope())
    with pytest.raises(ValueError, match="durable ResumeGate"):
        gate.state.complete_review(TEnvelope(), "2026-07-22T00:00:00Z")
    with pytest.raises(ValueError, match="predates resume"):
        gate.complete_overdue_review(timestamp_utc="2026-07-21T23:59:59Z")
    reviewed = gate.complete_overdue_review(timestamp_utc="2026-07-22T00:00:00Z")
    assert reviewed.last_review_utc == "2026-07-22T00:00:00Z"
    assert reviewed.device_nanoseconds == state.device_nanoseconds
    assert ledger.entries()[-1]["event"] == "T_REVIEW_COMPLETED"
    with pytest.raises(ValueError, match="no longer current"):
        gate.complete_overdue_review(timestamp_utc="2026-07-22T00:00:01Z")


def test_pause_resume_and_ledger_timestamps_cannot_move_backwards(tmp_path: Path) -> None:
    ledger, checkpoint, _ = _pause(tmp_path)
    with pytest.raises(ValueError, match="predates operational pause"):
        verify_resume(
            ledger=ledger,
            checkpoint_path=checkpoint,
            envelope=TEnvelope(),
            timestamp_utc="2026-07-20T07:59:59Z",
        )
    with pytest.raises(LedgerIntegrityError, match="move backwards"):
        ledger.append(
            event="BACKDATED",
            timestamp_utc="2026-07-20T07:59:59Z",
            data={"scientific_outcome": False},
        )

    fresh = AppendOnlyLedger(tmp_path / "fresh-ledger.md")
    fresh.initialize()
    state = _active_state()
    with pytest.raises(ValueError, match="predates active"):
        record_operational_pause(
            ledger=fresh,
            checkpoint_path=tmp_path / "backdated-pause.json",
            state=state,
            artifact_paths={},
            timestamp_utc="2026-07-19T23:59:59Z",
            reason="backdated",
        )


def test_pause_and_inactive_maintenance_are_mutually_exclusive(tmp_path: Path) -> None:
    ledger = AppendOnlyLedger(tmp_path / "T_LEDGER.md")
    ledger.initialize()
    with pytest.raises(ValueError, match="active"):
        record_operational_pause(
            ledger=ledger,
            checkpoint_path=tmp_path / "fake.json",
            state=TState(),
            artifact_paths={},
            timestamp_utc="2026-07-20T01:00:00Z",
            reason="fake-pause",
        )
    record_not_activated_maintenance(
        ledger=ledger,
        state=TState(),
        timestamp_utc="2026-07-20T01:00:00Z",
        reason="scheduled-power-off",
    )
    assert ledger.entries()[-1]["event"] == "T_NOT_ACTIVATED_AT_MAINTENANCE"
    with pytest.raises(ValueError, match="pristine"):
        record_not_activated_maintenance(
            ledger=ledger,
            state=_active_state(),
            timestamp_utc="2026-07-20T02:00:00Z",
            reason="false-inactive",
        )


def test_t_state_mapping_is_exact_and_noncoercive() -> None:
    state = _active_state().charge_device_nanoseconds(
        NANOSECONDS_PER_HOUR, TEnvelope()
    )
    restored = TState.from_mapping(state.to_mapping())
    assert restored == state
    assert canonical_json(restored.to_mapping()).endswith(b"\n")
    for field, bad_value in (
        ("device_nanoseconds", "3600"),
        ("author_stopped", 0),
        ("activated_utc", 123),
    ):
        malformed = state.to_mapping()
        malformed[field] = bad_value
        with pytest.raises(ValueError):
            TState.from_mapping(malformed)
    extra = state.to_mapping()
    extra["unknown"] = False
    with pytest.raises(ValueError, match="fields differ"):
        TState.from_mapping(extra)
    for noncanonical in (
        "2026-07-20 00:00:00Z",
        "2026-07-20T00:00:00.000Z",
        "2026-7-20T00:00:00Z",
    ):
        with pytest.raises(ValueError, match="canonical UTC"):
            TState().activate(noncanonical)
