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
from philosophia.officina.canonical import canonical_json, sha256_bytes
from philosophia.officina.ledger import build_entry
from philosophia.officina.runtime import (
    HEARTBEAT_LIABILITY_SECONDS,
    MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS,
    InvalidCause,
    ProcessDisposition,
    Reservation,
    ReservationRoute,
    RuntimeContractError,
    RuntimeLock,
    build_active_lease,
    build_process_claim,
    build_process_record,
    issue_real_t_capability,
    reject_scientific_fields,
    reservation_for,
    reservation_route,
    settle_active_lease,
    settle_monotonic_delta,
    validate_invalidity_record,
    validate_ledger_event,
    validate_active_lease,
    validate_active_lease_against_claim,
    validate_process_claim,
    validate_process_claim_against_activation,
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
        state=_state(), envelope=TEnvelope(), live_reservations=()
    )
    assert reservation is not None
    assert reservation.liability_ns_per_unit == (
        HEARTBEAT_LIABILITY_SECONDS * NANOSECONDS_PER_SECOND
    )
    assert reservation.aggregate_liability_ns == 60 * NANOSECONDS_PER_SECOND

    existing = (Reservation(3, 60 * NANOSECONDS_PER_SECOND),)
    last = reservation_for(
        state=_state(), envelope=TEnvelope(), live_reservations=existing
    )
    assert last is not None
    assert sum(item.aggregate_liability_ns for item in existing) + last.aggregate_liability_ns == (
        MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS * NANOSECONDS_PER_SECOND
    )
    with pytest.raises(RuntimeContractError, match="concurrency"):
        reservation_for(
            state=_state(),
            envelope=TEnvelope(),
            live_reservations=(Reservation(4, 60 * NANOSECONDS_PER_SECOND),),
        )
    with pytest.raises(RuntimeContractError, match="concurrency"):
        reservation_for(
            state=_state(),
            envelope=TEnvelope(),
            live_reservations=(Reservation(2, 1),),
            requested_units=3,
        )
    with pytest.raises(ValueError, match="exact Reservation"):
        reservation_for(
            state=_state(),
            envelope=TEnvelope(),
            live_reservations=(1,),  # type: ignore[arg-type]
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
        state=near_e1, envelope=envelope, live_reservations=()
    )
    assert reservation is not None and reservation.liability_ns_per_unit == 7
    exhausted = near_e1.charge_device_nanoseconds(7, envelope)
    assert reservation_for(
        state=exhausted, envelope=envelope, live_reservations=()
    ) is None

    near_e3 = TState(
        activated_utc="2026-07-21T00:00:00Z",
        device_nanoseconds=40 * NANOSECONDS_PER_HOUR - 9,
    )
    reservation = reservation_for(
        state=near_e3, envelope=envelope, live_reservations=()
    )
    assert reservation is not None and reservation.liability_ns_per_unit == 9
    assert reservation_route(
        state=near_e3.charge_device_nanoseconds(9, envelope),
        envelope=envelope,
        live_reservations=(),
    ) is ReservationRoute.E3_DUE
    assert reservation_route(
        state=exhausted,
        envelope=envelope,
        live_reservations=(),
    ) is ReservationRoute.E1_EXHAUSTED
    both_zero = TState(
        activated_utc="2026-07-21T00:00:00Z",
        device_nanoseconds=168 * NANOSECONDS_PER_HOUR,
        last_review_utc="2026-07-21T01:00:00Z",
        device_nanoseconds_at_review=128 * NANOSECONDS_PER_HOUR,
    )
    assert reservation_route(
        state=both_zero,
        envelope=envelope,
        live_reservations=(),
    ) is ReservationRoute.E1_EXHAUSTED


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


def test_all_nine_ledger_payloads_are_closed_and_non_scientific() -> None:
    state = _state().to_mapping()
    stopped_state = TState(
        activated_utc="2026-07-21T00:00:00Z",
        last_review_utc="2026-07-21T00:00:00Z",
        author_stopped=True,
    ).to_mapping()
    exhausted_state = TState(
        activated_utc="2026-07-21T00:00:00Z",
        device_nanoseconds=168 * NANOSECONDS_PER_HOUR,
    ).to_mapping()
    payloads: dict[str, dict[str, object]] = {
        "T_ACTIVATED": {
            "authorization_sha256": "a" * 64,
            "claim_sha256": "b" * 64,
            "device_policy_token": "device",
            "envelope_token": "envelope",
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_PROCESS_STARTED": {
            "process_claim_sha256": "a" * 64,
            "process_id": "b" * 64,
            "scientific_outcome": False,
        },
        "T_DEVICE_TIME_CHARGED": {
            "active_lease_sha256": "a" * 64,
            "charge_ns": 1,
            "process_id": "b" * 64,
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_REVIEW_COMPLETED": {
            "review_record_sha256": "a" * 64,
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_OPERATIONAL_PAUSE": {
            "checkpoint_path": "/tmp/pause",
            "checkpoint_sha256": "a" * 64,
            "reason": "planned",
            "resets_e3": False,
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_PROCESS_STOPPED": {
            "process_id": "a" * 64,
            "process_record_sha256": "b" * 64,
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_RUNTIME_INVALID": {
            "invalid_cause": "PROCESS",
            "invalidity_record_sha256": "a" * 64,
            "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
            "scientific_outcome": False,
            "t_state": state,
        },
        "T_AUTHOR_STOP": {
            "author_decision_sha256": "a" * 64,
            "scientific_outcome": False,
            "t_state": stopped_state,
        },
        "T_ENVELOPE_EXHAUSTED": {
            "resource_axis": "E1",
            "scientific_outcome": False,
            "t_state": exhausted_state,
        },
    }
    for sequence, (event, data) in enumerate(payloads.items()):
        entry = build_entry(
            sequence=sequence,
            previous_sha256="0" * 64,
            event=event,
            timestamp_utc="2026-07-21T00:00:00Z",
            data=data,
        )
        assert validate_ledger_event(entry)["event"] == event

    started = dict(payloads["T_PROCESS_STARTED"])
    started["t_state"] = state
    with pytest.raises(ValueError, match="payload fields"):
        validate_ledger_event(
            build_entry(
                sequence=0,
                previous_sha256="0" * 64,
                event="T_PROCESS_STARTED",
                timestamp_utc="2026-07-21T00:00:00Z",
                data=started,
            )
        )
    contaminated = dict(payloads["T_DEVICE_TIME_CHARGED"])
    contaminated["pass"] = True
    with pytest.raises(ValueError):
        validate_ledger_event(
            build_entry(
                sequence=0,
                previous_sha256="0" * 64,
                event="T_DEVICE_TIME_CHARGED",
                timestamp_utc="2026-07-21T00:00:00Z",
                data=contaminated,
            )
        )
    e2 = dict(payloads["T_ENVELOPE_EXHAUSTED"])
    e2["resource_axis"] = "E2"
    with pytest.raises(ValueError, match="only name E1"):
        validate_ledger_event(
            build_entry(
                sequence=0,
                previous_sha256="0" * 64,
                event="T_ENVELOPE_EXHAUSTED",
                timestamp_utc="2026-07-21T00:00:00Z",
                data=e2,
            )
        )


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


_ACTIVATION_HASH = "a" * 64
_CONTROL_HASHES = {"control.py": "f" * 64}


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
        state=_state(), envelope=TEnvelope(), live_reservations=()
    )
    assert reservation is not None
    lease = build_active_lease(
        claim,
        reservation=reservation,
        prior_charge_event_sha256="0" * 64,
        activation_record_sha256=_ACTIVATION_HASH,
        immutable_control_sha256=_CONTROL_HASHES,
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
    final_event = build_entry(
        sequence=1,
        previous_sha256="0" * 64,
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc="2026-07-21T00:00:01Z",
        data={
            "active_lease_sha256": sha256_bytes(canonical_json(renewed)),
            "charge_ns": 60,
            "process_id": claim["process_id"],
            "scientific_outcome": False,
            "t_state": state.to_mapping(),
        },
    )
    record = build_process_record(
        claim=claim,
        lease=renewed,
        disposition=ProcessDisposition.CLOSED,
        invalid_cause=None,
        closed_utc="2026-07-21T00:00:01Z",
        final_charge_event=final_event,
        final_state=state,
        activation_record_sha256=_ACTIVATION_HASH,
        immutable_control_sha256=_CONTROL_HASHES,
    )
    assert validate_process_record(record)["validity"] == "VALID_PROCESS_RECORD"
    with pytest.raises(ValueError, match="typed public cause"):
        build_process_record(
            claim=claim,
            lease=renewed,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=None,
            closed_utc="2026-07-21T00:00:01Z",
            final_charge_event=final_event,
            final_state=state,
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
        )


def test_claim_lease_and_activation_links_are_byte_exact() -> None:
    claim = _claim()
    reservation = Reservation(1, 60 * NANOSECONDS_PER_SECOND)
    lease = build_active_lease(
        claim,
        reservation=reservation,
        prior_charge_event_sha256="0" * 64,
        activation_record_sha256=_ACTIVATION_HASH,
        immutable_control_sha256=_CONTROL_HASHES,
    )
    validate_process_claim_against_activation(
        claim,
        activation_record_sha256="a" * 64,
        immutable_control_sha256={"control.py": "f" * 64},
    )
    changed_controller = dict(lease)
    changed_controller["controller_pid"] = int(lease["controller_pid"]) + 1
    validate_active_lease(changed_controller)
    with pytest.raises(ValueError, match="byte-exact durable claim"):
        validate_active_lease_against_claim(changed_controller, claim)
    final_event = build_entry(
        sequence=1,
        previous_sha256="0" * 64,
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc="2026-07-21T00:00:01Z",
        data={
            "active_lease_sha256": sha256_bytes(canonical_json(lease)),
            "charge_ns": 1,
            "process_id": claim["process_id"],
            "scientific_outcome": False,
            "t_state": _state().to_mapping(),
        },
    )
    with pytest.raises(ValueError, match="byte-exact durable claim"):
        build_process_record(
            claim=claim,
            lease=changed_controller,
            disposition=ProcessDisposition.CLOSED,
            invalid_cause=None,
            closed_utc="2026-07-21T00:00:01Z",
            final_charge_event=final_event,
            final_state=_state(),
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
        )
    changed_liability = dict(lease)
    changed_liability["outstanding_liability_ns"] = 1
    with pytest.raises(ValueError, match="liability and deadline"):
        validate_active_lease(changed_liability)
    wrong_data = dict(final_event["data"])
    wrong_data["process_id"] = "9" * 64
    wrong_process_event = build_entry(
        sequence=1,
        previous_sha256="0" * 64,
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc="2026-07-21T00:00:01Z",
        data=wrong_data,
    )
    with pytest.raises(ValueError, match="process id differs"):
        build_process_record(
            claim=claim,
            lease=lease,
            disposition=ProcessDisposition.CLOSED,
            invalid_cause=None,
            closed_utc="2026-07-21T00:00:01Z",
            final_charge_event=wrong_process_event,
            final_state=_state(),
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
        )
    with pytest.raises(ValueError, match="immutable controls"):
        validate_process_claim_against_activation(
            claim,
            activation_record_sha256="a" * 64,
            immutable_control_sha256={"other.py": "f" * 64},
        )
    with pytest.raises(ValueError, match="immutable controls"):
        build_active_lease(
            claim,
            reservation=reservation,
            prior_charge_event_sha256="0" * 64,
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256={"other.py": "f" * 64},
        )


def test_process_record_requires_typed_settlement_and_invalidity_chain() -> None:
    claim = _claim()
    reservation = Reservation(1, 60 * NANOSECONDS_PER_SECOND)
    lease = build_active_lease(
        claim,
        reservation=reservation,
        prior_charge_event_sha256="0" * 64,
        activation_record_sha256=_ACTIVATION_HASH,
        immutable_control_sha256=_CONTROL_HASHES,
    )
    state, renewed = settle_active_lease(
        lease=lease,
        state=_state(),
        envelope=TEnvelope(),
        current_reading_ns=160,
        next_reservation=reservation,
        charge_event_sha256="1" * 64,
    )
    charge = build_entry(
        sequence=1,
        previous_sha256="0" * 64,
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc="2026-07-21T00:00:01Z",
        data={
            "active_lease_sha256": sha256_bytes(canonical_json(renewed)),
            "charge_ns": 60,
            "process_id": claim["process_id"],
            "scientific_outcome": False,
            "t_state": state.to_mapping(),
        },
    )
    invalidity = {
        "schema": "philosophia.officina.t-runtime-invalidity.v1",
        "scientific_outcome": False,
        "validity": "INVALID_PROCESS_RECORD",
        "invalid_cause": "CLOCK",
        "transaction_kind": "T_PROCESS",
        "durable_step_index": 3,
        "affected_path_sha256": {},
        "clock_kind": "CLOCK_MONOTONIC",
        "boot_identity": "test-boot-id",
        "observed_utc": "2026-07-21T00:00:02Z",
        "outstanding_liability_ns": renewed["outstanding_liability_ns"],
        "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
    }
    invalid_event = build_entry(
        sequence=2,
        previous_sha256=str(charge["entry_sha256"]),
        event="T_RUNTIME_INVALID",
        timestamp_utc="2026-07-21T00:00:02Z",
        data={
            "invalid_cause": "CLOCK",
            "invalidity_record_sha256": sha256_bytes(canonical_json(invalidity)),
            "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
            "scientific_outcome": False,
            "t_state": state.to_mapping(),
        },
    )
    record = build_process_record(
        claim=claim,
        lease=renewed,
        disposition=ProcessDisposition.INVALID,
        invalid_cause=InvalidCause.CLOCK,
        closed_utc="2026-07-21T00:00:02Z",
        final_charge_event=charge,
        final_state=state,
        activation_record_sha256=_ACTIVATION_HASH,
        immutable_control_sha256=_CONTROL_HASHES,
        terminal_event=invalid_event,
        invalidity_record=invalidity,
    )
    assert validate_process_record(record)["validity"] == "INVALID_PROCESS_RECORD"

    with pytest.raises(ValueError, match="device-time charge"):
        build_process_record(
            claim=claim,
            lease=renewed,
            disposition=ProcessDisposition.CLOSED,
            invalid_cause=None,
            closed_utc="2026-07-21T00:00:02Z",
            final_charge_event=invalid_event,
            final_state=state,
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
        )
    with pytest.raises(ValueError, match="runtime-invalid event"):
        build_process_record(
            claim=claim,
            lease=renewed,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=InvalidCause.CLOCK,
            closed_utc="2026-07-21T00:00:01Z",
            final_charge_event=charge,
            final_state=state,
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
        )
    wrong_cause = dict(invalidity)
    wrong_cause["invalid_cause"] = "PROCESS"
    with pytest.raises(ValueError, match="cause differs|record hash differs"):
        build_process_record(
            claim=claim,
            lease=renewed,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=InvalidCause.CLOCK,
            closed_utc="2026-07-21T00:00:02Z",
            final_charge_event=charge,
            final_state=state,
            activation_record_sha256=_ACTIVATION_HASH,
            immutable_control_sha256=_CONTROL_HASHES,
            terminal_event=invalid_event,
            invalidity_record=wrong_cause,
        )


def test_ledger_event_refuses_pre_wp6_candidate_state() -> None:
    state = _state().to_mapping()
    state["candidate_ids"] = ["a" * 64]
    event = build_entry(
        sequence=1,
        previous_sha256="0" * 64,
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc="2026-07-21T00:00:01Z",
        data={
            "active_lease_sha256": "b" * 64,
            "charge_ns": 1,
            "process_id": "c" * 64,
            "scientific_outcome": False,
            "t_state": state,
        },
    )
    with pytest.raises(ValueError, match="absent signed WP-6"):
        validate_ledger_event(event)
