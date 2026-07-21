from __future__ import annotations

import os
from pathlib import Path

import pytest

from philosophia.officina.accounting import (
    NANOSECONDS_PER_HOUR,
    NANOSECONDS_PER_SECOND,
    TEnvelope,
    TState,
)
from philosophia.officina.runtime import (
    HEARTBEAT_LIABILITY_SECONDS,
    MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS,
    InvalidCause,
    ProcessDisposition,
    RuntimeContractError,
    RuntimeLock,
    build_active_lease,
    build_process_claim,
    build_process_record,
    issue_real_t_capability,
    reject_scientific_fields,
    reservation_for,
    settle_active_lease,
    settle_monotonic_delta,
    validate_invalidity_record,
    validate_active_lease,
    validate_process_claim,
    validate_process_record,
    verify_runtime_lock,
)


REPO = Path(__file__).resolve().parent.parent


def _state() -> TState:
    return TState().activate("2026-07-21T00:00:00Z")


def test_tracked_runtime_lock_is_exact_held_descriptor_infrastructure() -> None:
    assert verify_runtime_lock(REPO) == []
    with RuntimeLock(REPO) as held:
        assert held.anchor_matches(REPO / "successor/officina/runtime/T_RUNTIME.lock")
    assert held.descriptor == -1


def test_runtime_lock_refuses_symlink_and_byte_substitution(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    path = root / "successor/officina/runtime/T_RUNTIME.lock"
    path.parent.mkdir(parents=True)
    path.write_bytes(b"wrong\n")
    assert verify_runtime_lock(root)
    path.unlink()
    path.symlink_to(REPO / "successor/officina/runtime/T_RUNTIME.lock")
    assert verify_runtime_lock(root)
    with pytest.raises(OSError):
        with RuntimeLock(root):
            pass


def test_reservation_caps_concurrency_and_aggregate_liability() -> None:
    reservation = reservation_for(
        state=_state(), envelope=TEnvelope(), live_liabilities_ns=()
    )
    assert reservation is not None
    assert reservation.liability_ns_per_unit == (
        HEARTBEAT_LIABILITY_SECONDS * NANOSECONDS_PER_SECOND
    )
    assert reservation.aggregate_liability_ns == 60 * NANOSECONDS_PER_SECOND

    existing = (60 * NANOSECONDS_PER_SECOND,) * 3
    last = reservation_for(
        state=_state(), envelope=TEnvelope(), live_liabilities_ns=existing
    )
    assert last is not None
    assert sum(existing) + last.aggregate_liability_ns == (
        MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS * NANOSECONDS_PER_SECOND
    )
    with pytest.raises(RuntimeContractError, match="concurrency"):
        reservation_for(
            state=_state(),
            envelope=TEnvelope(),
            live_liabilities_ns=(60 * NANOSECONDS_PER_SECOND,) * 4,
        )


def test_reservation_shortens_at_e1_and_e3_boundaries_without_stranding() -> None:
    envelope = TEnvelope()
    near_e1 = TState(
        activated_utc="2026-07-21T00:00:00Z",
        device_nanoseconds=168 * NANOSECONDS_PER_HOUR - 7,
        last_review_utc="2026-07-21T01:00:00Z",
        device_nanoseconds_at_review=167 * NANOSECONDS_PER_HOUR,
    )
    reservation = reservation_for(
        state=near_e1, envelope=envelope, live_liabilities_ns=()
    )
    assert reservation is not None and reservation.liability_ns_per_unit == 7
    exhausted = near_e1.charge_device_nanoseconds(7, envelope)
    assert reservation_for(
        state=exhausted, envelope=envelope, live_liabilities_ns=()
    ) is None

    near_e3 = TState(
        activated_utc="2026-07-21T00:00:00Z",
        device_nanoseconds=40 * NANOSECONDS_PER_HOUR - 9,
    )
    reservation = reservation_for(
        state=near_e3, envelope=envelope, live_liabilities_ns=()
    )
    assert reservation is not None and reservation.liability_ns_per_unit == 9


def test_monotonic_settlement_is_additive_and_retains_crossing_charge() -> None:
    state = settle_monotonic_delta(
        state=_state(),
        envelope=TEnvelope(),
        prior_ns=100,
        current_ns=160,
        units=3,
    )
    assert state.device_nanoseconds == 180
    with pytest.raises(RuntimeContractError, match="did not increase"):
        settle_monotonic_delta(
            state=state,
            envelope=TEnvelope(),
            prior_ns=160,
            current_ns=160,
            units=1,
        )
    with pytest.raises(ValueError, match="integer"):
        settle_monotonic_delta(
            state=state,
            envelope=TEnvelope(),
            prior_ns=160,
            current_ns=200,
            units=True,
        )


def test_invalidity_schema_is_closed_and_has_no_learner_cause() -> None:
    value = {
        "schema": "philosophia.officina.t-runtime-invalidity.v1",
        "scientific_outcome": False,
        "validity": "INVALID_PROCESS_RECORD",
        "invalid_cause": InvalidCause.CLOCK.value,
        "transaction_kind": "HEARTBEAT",
        "durable_step_index": 2,
        "affected_path_sha256": {},
        "clock_kind": "CLOCK_MONOTONIC",
        "boot_identity": "test-boot",
        "observed_utc": "2026-07-21T00:00:00Z",
        "outstanding_liability_ns": 60 * NANOSECONDS_PER_SECOND,
        "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
    }
    assert validate_invalidity_record(value)["invalid_cause"] == "CLOCK"
    assert {item.value for item in InvalidCause} == {
        "PROCESS", "RESOURCE", "HASH", "CLOCK", "FILESYSTEM"
    }
    assert {item.value for item in ProcessDisposition} == {
        "T_PROCESS_CLOSED", "T_PROCESS_VOLUNTARY_STOP",
        "T_PROCESS_RESOURCE_STOP", "T_PROCESS_INVALID",
        "T_PROCESS_E1_EXHAUSTED", "T_PROCESS_E3_DUE",
    }
    value["invalid_cause"] = "NONFINITE_DEVELOPMENT"
    with pytest.raises(ValueError):
        validate_invalidity_record(value)


def test_public_runtime_records_reject_scientific_and_behavior_fields() -> None:
    reject_scientific_fields({"scientific_outcome": False, "device_units": 1})
    for forbidden in ("loss", "competence", "C1", "outcome_summary"):
        with pytest.raises(ValueError, match="forbidden scientific field"):
            reject_scientific_fields({"nested": {forbidden: 0}})


def test_real_capability_factory_remains_absent() -> None:
    with pytest.raises(RuntimeContractError, match="harness is absent"):
        issue_real_t_capability()


def _claim() -> dict[str, object]:
    return build_process_claim(
        activation_record_sha256="a" * 64,
        process_sequence=0,
        controller_pid=os.getpid(),
        controller_start_identity="proc-start-1",
        process_group_id=os.getpgrp(),
        argv=("python", "learner.py"),
        behavior_source_sha256="b" * 64,
        config_sha256="c" * 64,
        stack_sha256="d" * 64,
        numerical_mode_sha256="e" * 64,
        device_identity="cpu:test",
        device_units=1,
        created_utc="2026-07-21T00:00:00Z",
        boot_id="test-boot-id",
        start_reading_ns=100,
        immutable_control_sha256={"control.py": "f" * 64},
    )


def test_process_claim_identity_is_canonical_and_mutation_detected() -> None:
    claim = _claim()
    assert validate_process_claim(claim)["process_id"] == claim["process_id"]
    mutated = dict(claim)
    mutated["config_sha256"] = "1" * 64
    with pytest.raises(ValueError, match="process id"):
        validate_process_claim(mutated)
    extra = {**claim, "loss": 0.0}
    with pytest.raises(ValueError, match="fields differ"):
        validate_process_claim(extra)


def test_lease_heartbeat_and_process_close_round_trip() -> None:
    claim = _claim()
    reservation = reservation_for(
        state=_state(), envelope=TEnvelope(), live_liabilities_ns=()
    )
    assert reservation is not None
    lease = build_active_lease(
        claim, reservation=reservation, prior_charge_event_sha256="0" * 64
    )
    assert validate_active_lease(lease)["heartbeat_deadline_ns"] == (
        100 + 60 * NANOSECONDS_PER_SECOND
    )
    state, renewed = settle_active_lease(
        lease=lease,
        state=_state(),
        envelope=TEnvelope(),
        current_reading_ns=160,
        next_reservation=reservation,
        charge_event_sha256="1" * 64,
    )
    assert state.device_nanoseconds == 60
    assert renewed["cumulative_charge_ns"] == 60
    record = build_process_record(
        claim=claim,
        claim_sha256="2" * 64,
        lease=renewed,
        disposition=ProcessDisposition.CLOSED,
        invalid_cause=None,
        closed_utc="2026-07-21T00:00:01Z",
        final_charge_event_sha256="3" * 64,
        final_t_state_sha256="4" * 64,
    )
    assert validate_process_record(record)["validity"] == "VALID_PROCESS_RECORD"
    with pytest.raises(ValueError, match="typed public cause"):
        build_process_record(
            claim=claim,
            claim_sha256="2" * 64,
            lease=renewed,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=None,
            closed_utc="2026-07-21T00:00:01Z",
            final_charge_event_sha256="3" * 64,
            final_t_state_sha256="4" * 64,
        )
