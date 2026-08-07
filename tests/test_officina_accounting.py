from __future__ import annotations

import json
from pathlib import Path

import pytest

from philosophia.officina.accounting import (
    NANOSECONDS_PER_HOUR,
    BatchSettlementAuthority,
    TEnvelope,
    TState,
)
from philosophia.officina.canonical import canonical_json, hash_mapping

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
    with pytest.raises(PermissionError, match="absent signed WP-6"):
        state.register_candidate("a" * 64, envelope)
    assert state.candidate_ids == ()


def test_pre_wp6_state_cannot_represent_or_interpret_e2_consumption() -> None:
    envelope = TEnvelope()
    active = _active_state()
    candidate = "a" * 64
    with pytest.raises(ValueError, match="absent signed WP-6"):
        TState(activated_utc=active.activated_utc, candidate_ids=(candidate,))
    mapping = active.to_mapping()
    mapping["candidate_ids"] = [candidate]
    with pytest.raises(ValueError, match="absent signed WP-6"):
        TState.from_mapping(mapping)
    assert not active.exhausted(envelope)
    charged = TState(
        activated_utc=active.activated_utc,
        device_nanoseconds=envelope.device_hour_cap * NANOSECONDS_PER_HOUR,
    )
    assert charged.exhausted(envelope)


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
    )
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
    with pytest.raises(PermissionError, match="absent signed WP-6"):
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


def _authority(
    *,
    state: TState,
    entries: tuple[tuple[str, str, int], ...],
    head: str = "a" * 64,
    claim: str = "b" * 64,
    consumed: int = 0,
) -> BatchSettlementAuthority:
    return BatchSettlementAuthority.from_validated_claim(
        claim_sha256=claim,
        entries=entries,
        expected_ledger_head_sha256=head,
        expected_state_sha256=hash_mapping(state.to_mapping()),
        consumed_count=consumed,
    )


def test_batch_settlement_represents_signed_60_60_60_counterexample() -> None:
    envelope = TEnvelope()
    cap = envelope.device_hour_cap * NANOSECONDS_PER_HOUR
    processes = ("1" * 64, "2" * 64, "3" * 64)
    leases = ("c" * 64, "d" * 64, "e" * 64)
    entries = tuple(
        (process_id, lease, 60)
        for process_id, lease in zip(processes, leases, strict=True)
    )
    # Ordinary sequential charging cannot represent the batch: after the
    # second 60 ns charge the envelope is exhausted and the third refuses.
    ordinary = TState(
        activated_utc="2026-07-20T00:00:00Z",
        device_nanoseconds=cap - 100,
    )
    ordinary = ordinary.charge_device_nanoseconds(60, envelope)
    assert ordinary.device_nanoseconds == cap - 40
    ordinary = ordinary.charge_device_nanoseconds(60, envelope)
    assert ordinary.device_nanoseconds == cap + 20
    assert ordinary.exhausted(envelope)
    with pytest.raises(ValueError, match="already exhausted"):
        ordinary.charge_device_nanoseconds(60, envelope)

    # Frozen-batch authority appends all three charges, including post-cap.
    state = TState(
        activated_utc="2026-07-20T00:00:00Z",
        device_nanoseconds=cap - 100,
    )
    head = "f" * 64
    authority = _authority(state=state, entries=entries, head=head)
    expected_totals = (cap - 40, cap + 20, cap + 80)
    for (process_id, lease, value), expected in zip(
        entries, expected_totals, strict=True
    ):
        if state.exhausted(envelope):
            with pytest.raises(ValueError, match="already exhausted"):
                state.charge_device_nanoseconds(value, envelope)
        state, authority = state.charge_batch_settlement(
            process_id=process_id,
            active_lease_sha256=lease,
            value=value,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )
        assert state.device_nanoseconds == expected
        assert hash_mapping(state.to_mapping()) == authority.expected_state_sha256
    assert authority.consumed_count == 3
    assert state.device_nanoseconds == cap + 80


def test_ordinary_post_cap_charge_still_refused_after_batch_crossing() -> None:
    envelope = TEnvelope()
    cap = envelope.device_hour_cap * NANOSECONDS_PER_HOUR
    state = TState(
        activated_utc="2026-07-20T00:00:00Z",
        device_nanoseconds=cap - 10,
    )
    lease = "a" * 64
    process = "b" * 64
    head = "c" * 64
    authority = _authority(
        state=state,
        entries=((process, lease, 20),),
        head=head,
    )
    state, authority = state.charge_batch_settlement(
        process_id=process,
        active_lease_sha256=lease,
        value=20,
        envelope=envelope,
        authority=authority,
        current_ledger_head_sha256=head,
    )
    assert state.device_nanoseconds == cap + 10
    with pytest.raises(ValueError, match="already exhausted"):
        state.charge_device_nanoseconds(1, envelope)


def test_batch_authority_non_reuse_and_membership_refusals() -> None:
    envelope = TEnvelope()
    state = _active_state().charge_device_nanoseconds(100, envelope)
    p1, p2 = "1" * 64, "2" * 64
    l1, l2 = "3" * 64, "4" * 64
    head = "5" * 64
    entries = ((p1, l1, 10), (p2, l2, 20))
    authority = _authority(state=state, entries=entries, head=head)
    original = authority
    state, authority = state.charge_batch_settlement(
        process_id=p1,
        active_lease_sha256=l1,
        value=10,
        envelope=envelope,
        authority=authority,
        current_ledger_head_sha256=head,
    )
    # Reusing the pre-charge authority fails on advanced state.
    with pytest.raises(ValueError, match="expected state"):
        state.charge_batch_settlement(
            process_id=p1,
            active_lease_sha256=l1,
            value=10,
            envelope=envelope,
            authority=original,
            current_ledger_head_sha256=head,
        )
    # Wrong process / value / order.
    with pytest.raises(ValueError, match="entry mismatch"):
        state.charge_batch_settlement(
            process_id=p1,
            active_lease_sha256=l1,
            value=10,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )
    with pytest.raises(ValueError, match="entry mismatch"):
        state.charge_batch_settlement(
            process_id=p2,
            active_lease_sha256=l2,
            value=21,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )
    with pytest.raises(ValueError, match="entry mismatch"):
        state.charge_batch_settlement(
            process_id=p2,
            active_lease_sha256=l1,
            value=20,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )
    state, authority = state.charge_batch_settlement(
        process_id=p2,
        active_lease_sha256=l2,
        value=20,
        envelope=envelope,
        authority=authority,
        current_ledger_head_sha256=head,
    )
    with pytest.raises(ValueError, match="fully consumed"):
        state.charge_batch_settlement(
            process_id=p2,
            active_lease_sha256=l2,
            value=20,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )


def test_batch_settlement_refuses_stale_head_and_state() -> None:
    envelope = TEnvelope()
    state = _active_state()
    other = state.charge_device_nanoseconds(5, envelope)
    p1, l1 = "1" * 64, "2" * 64
    head = "3" * 64
    authority = _authority(
        state=state,
        entries=((p1, l1, 7),),
        head=head,
    )
    with pytest.raises(ValueError, match="expected ledger head"):
        state.charge_batch_settlement(
            process_id=p1,
            active_lease_sha256=l1,
            value=7,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256="4" * 64,
        )
    with pytest.raises(ValueError, match="expected state"):
        other.charge_batch_settlement(
            process_id=p1,
            active_lease_sha256=l1,
            value=7,
            envelope=envelope,
            authority=authority,
            current_ledger_head_sha256=head,
        )


def test_batch_settlement_prefix_reconstruction_and_multiple_e1_crossings() -> None:
    envelope = TEnvelope()
    cap = envelope.device_hour_cap * NANOSECONDS_PER_HOUR
    pre = TState(
        activated_utc="2026-07-20T00:00:00Z",
        device_nanoseconds=cap - 50,
    )
    entries = (
        ("1" * 64, "a" * 64, 30),
        ("2" * 64, "b" * 64, 40),
        ("3" * 64, "c" * 64, 25),
    )
    head = "d" * 64
    authority = _authority(state=pre, entries=entries, head=head)
    state = pre
    # Consume a prefix, then reconstruct the successor authority from the
    # durable consumed count and post-prefix state (restart reconstruction).
    state, authority = state.charge_batch_settlement(
        process_id=entries[0][0],
        active_lease_sha256=entries[0][1],
        value=entries[0][2],
        envelope=envelope,
        authority=authority,
        current_ledger_head_sha256=head,
    )
    assert state.device_nanoseconds == cap - 20
    reconstructed = BatchSettlementAuthority.from_validated_claim(
        claim_sha256=authority.claim_sha256,
        entries=entries,
        expected_ledger_head_sha256=head,
        expected_state_sha256=hash_mapping(state.to_mapping()),
        consumed_count=1,
    )
    assert reconstructed == authority
    state, authority = state.charge_batch_settlement(
        process_id=entries[1][0],
        active_lease_sha256=entries[1][1],
        value=entries[1][2],
        envelope=envelope,
        authority=reconstructed,
        current_ledger_head_sha256=head,
    )
    assert state.device_nanoseconds == cap + 20
    state, authority = state.charge_batch_settlement(
        process_id=entries[2][0],
        active_lease_sha256=entries[2][1],
        value=entries[2][2],
        envelope=envelope,
        authority=authority,
        current_ledger_head_sha256=head,
    )
    assert state.device_nanoseconds == cap + 45
    assert authority.consumed_count == 3
    # Conservation: post = pre + Σ claimed.
    assert state.device_nanoseconds == pre.device_nanoseconds + sum(
        entry[2] for entry in entries
    )
