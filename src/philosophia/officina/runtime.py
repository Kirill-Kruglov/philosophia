"""Inactive implementation of the signed Officina T runtime contract.

The module defines canonical runtime records, locking, reservation arithmetic,
and fail-closed validation.  It deliberately exposes no usable real-T world or
learner capability: that boundary remains blocked until the separately reviewed
generic metered harness exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import fcntl
import os
from pathlib import Path
import re
from typing import Iterable, Mapping

from .accounting import NANOSECONDS_PER_HOUR, NANOSECONDS_PER_SECOND, TEnvelope, TState
from .canonical import canonical_json, load_canonical_json, sha256_bytes, sha256_file


RUNTIME_LOCK_RELATIVE = Path("successor/officina/runtime/T_RUNTIME.lock")
RUNTIME_LOCK_BYTES = b"OFFICINA_T_RUNTIME_LOCK_V1\n"
HEARTBEAT_LIABILITY_SECONDS = 60
MAX_CONCURRENT_LEASES = 4
DEVICE_UNITS_PER_LEASE = 1
MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS = 240
CLOCK_KIND = "CLOCK_MONOTONIC"
BOOT_ID_PATH = Path("/proc/sys/kernel/random/boot_id")

POST_ACTIVATION_EVENTS = frozenset(
    {
        "T_ACTIVATED",
        "T_PROCESS_STARTED",
        "T_DEVICE_TIME_CHARGED",
        "T_REVIEW_COMPLETED",
        "T_OPERATIONAL_PAUSE",
        "T_PROCESS_STOPPED",
        "T_RUNTIME_INVALID",
        "T_AUTHOR_STOP",
        "T_ENVELOPE_EXHAUSTED",
    }
)
STATE_BEARING_EVENTS = POST_ACTIVATION_EVENTS - {"T_PROCESS_STARTED"}

PROCESS_CLAIM_SCHEMA = "philosophia.officina.t-process-claim.v1"
ACTIVE_LEASE_SCHEMA = "philosophia.officina.t-active-lease.v1"
PROCESS_RECORD_SCHEMA = "philosophia.officina.t-process-record.v1"
REVIEW_RECORD_SCHEMA = "philosophia.officina.t-review-record.v1"
INVALIDITY_SCHEMA = "philosophia.officina.t-runtime-invalidity.v1"

_HEX64 = re.compile(r"[0-9a-f]{64}")
_PUBLIC_FORBIDDEN_KEYS = frozenset(
    {
        "arm",
        "contrast",
        "score",
        "scores",
        "loss",
        "losses",
        "accuracy",
        "competence",
        "censoring",
        "effect",
        "margin",
        "scientific_label",
        "outcome",
        "outcome_summary",
        "pass",
        "fail",
        "insufficient",
        "equivalence",
        "boundary",
    }
)


class RuntimeContractError(RuntimeError):
    pass


class InvalidCause(str, Enum):
    PROCESS = "PROCESS"
    RESOURCE = "RESOURCE"
    HASH = "HASH"
    CLOCK = "CLOCK"
    FILESYSTEM = "FILESYSTEM"


class ProcessDisposition(str, Enum):
    CLOSED = "T_PROCESS_CLOSED"
    VOLUNTARY_STOP = "T_PROCESS_VOLUNTARY_STOP"
    RESOURCE_STOP = "T_PROCESS_RESOURCE_STOP"
    INVALID = "T_PROCESS_INVALID"
    E1_EXHAUSTED = "T_PROCESS_E1_EXHAUSTED"
    E3_DUE = "T_PROCESS_E3_DUE"


@dataclass(frozen=True)
class Reservation:
    units: int
    liability_ns_per_unit: int

    def __post_init__(self) -> None:
        if type(self.units) is not int or not 1 <= self.units <= MAX_CONCURRENT_LEASES:
            raise ValueError("reservation units are outside the signed boundary")
        if type(self.liability_ns_per_unit) is not int or not (
            0 < self.liability_ns_per_unit
            <= HEARTBEAT_LIABILITY_SECONDS * NANOSECONDS_PER_SECOND
        ):
            raise ValueError("reservation liability is outside the signed boundary")

    @property
    def aggregate_liability_ns(self) -> int:
        return self.units * self.liability_ns_per_unit

    @property
    def deadline_delta_ns(self) -> int:
        return self.liability_ns_per_unit


class ReservationRoute(str, Enum):
    RESERVE = "RESERVE"
    E1_EXHAUSTED = "E1_EXHAUSTED"
    E3_DUE = "E3_DUE"


class RuntimeLock:
    """Held-descriptor lock for every active-state read and mutation."""

    def __init__(self, repo: Path) -> None:
        self.repo = repo.resolve(strict=True)
        self.path = self.repo / RUNTIME_LOCK_RELATIVE
        self.descriptor = -1

    def __enter__(self) -> "RuntimeLock":
        flags = os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW
        descriptor = os.open(self.path, flags)
        try:
            stat = os.fstat(descriptor)
            if not os.path.samestat(stat, self.path.stat(follow_symlinks=False)):
                raise RuntimeContractError("runtime lock descriptor identity changed")
            os.lseek(descriptor, 0, os.SEEK_SET)
            lock_bytes = os.read(descriptor, len(RUNTIME_LOCK_BYTES) + 1)
            if not self.path.is_file() or lock_bytes != RUNTIME_LOCK_BYTES:
                raise RuntimeContractError("runtime lock bytes differ")
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            if not os.path.samestat(
                os.fstat(descriptor), self.path.stat(follow_symlinks=False)
            ):
                raise RuntimeContractError("runtime lock changed while acquiring lock")
        except BaseException:
            os.close(descriptor)
            raise
        self.descriptor = descriptor
        return self

    def anchor_matches(self, path: Path) -> bool:
        if self.descriptor < 0:
            return False
        try:
            return os.path.samestat(
                os.fstat(self.descriptor), path.stat(follow_symlinks=False)
            )
        except OSError:
            return False

    def __exit__(self, *args: object) -> None:
        del args
        if self.descriptor >= 0:
            fcntl.flock(self.descriptor, fcntl.LOCK_UN)
            os.close(self.descriptor)
            self.descriptor = -1


def verify_runtime_lock(repo: Path) -> list[str]:
    path = repo / RUNTIME_LOCK_RELATIVE
    failures: list[str] = []
    try:
        if path.is_symlink() or not path.is_file():
            failures.append("T runtime lock is missing or not a regular file")
        elif path.read_bytes() != RUNTIME_LOCK_BYTES:
            failures.append("T runtime lock bytes differ")
        else:
            with RuntimeLock(repo) as held:
                if not held.anchor_matches(path):
                    failures.append("T runtime lock descriptor identity differs")
    except OSError as error:
        failures.append(f"T runtime lock cannot be opened: {error}")
    return failures


def boot_identity() -> str:
    value = BOOT_ID_PATH.read_text(encoding="ascii").strip()
    if re.fullmatch(r"[0-9a-f-]{36}", value) is None:
        raise RuntimeContractError("boot identity is unavailable or malformed")
    return value


def reservation_for(
    *,
    state: TState,
    envelope: TEnvelope,
    live_reservations: Iterable[Reservation],
    requested_units: int = DEVICE_UNITS_PER_LEASE,
) -> Reservation | None:
    if type(requested_units) is not int or not 1 <= requested_units <= MAX_CONCURRENT_LEASES:
        raise ValueError("requested behavior-capable stream count is invalid")
    reservations = tuple(live_reservations)
    if any(type(value) is not Reservation for value in reservations):
        raise ValueError("live reservations must use the exact Reservation type")
    live_units = sum(value.units for value in reservations)
    if live_units + requested_units > MAX_CONCURRENT_LEASES:
        raise RuntimeContractError("behavior-capable concurrency cap reached")
    if state.activated_utc is None or state.author_stopped or state.resume_review_pending:
        raise RuntimeContractError("T runtime state is unavailable")

    live_total = sum(value.aggregate_liability_ns for value in reservations)
    e1_remaining = envelope.device_hour_cap * NANOSECONDS_PER_HOUR - (
        state.device_nanoseconds + live_total
    )
    e3_remaining = envelope.review_device_hours * NANOSECONDS_PER_HOUR - (
        state.device_nanoseconds - state.device_nanoseconds_at_review + live_total
    )
    per_unit = min(
        HEARTBEAT_LIABILITY_SECONDS * NANOSECONDS_PER_SECOND,
        e1_remaining // requested_units,
        e3_remaining // requested_units,
    )
    if per_unit <= 0:
        return None
    result = Reservation(requested_units, per_unit)
    if live_total + result.aggregate_liability_ns > (
        MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS * NANOSECONDS_PER_SECOND
    ):
        raise RuntimeContractError("aggregate liability bound exceeded")
    return result


def reservation_route(
    *,
    state: TState,
    envelope: TEnvelope,
    live_reservations: Iterable[Reservation],
    requested_units: int = DEVICE_UNITS_PER_LEASE,
) -> ReservationRoute:
    reservations = tuple(live_reservations)
    if any(type(value) is not Reservation for value in reservations):
        raise ValueError("live reservations must use the exact Reservation type")
    live_total = sum(value.aggregate_liability_ns for value in reservations)
    e1_remaining = envelope.device_hour_cap * NANOSECONDS_PER_HOUR - (
        state.device_nanoseconds + live_total
    )
    e3_remaining = envelope.review_device_hours * NANOSECONDS_PER_HOUR - (
        state.device_nanoseconds - state.device_nanoseconds_at_review + live_total
    )
    if e1_remaining <= 0:
        return ReservationRoute.E1_EXHAUSTED
    if e3_remaining <= 0:
        return ReservationRoute.E3_DUE
    result = reservation_for(
        state=state,
        envelope=envelope,
        live_reservations=reservations,
        requested_units=requested_units,
    )
    if result is None:
        raise RuntimeContractError("positive reservation boundary became empty")
    return ReservationRoute.RESERVE


def settle_monotonic_delta(
    *, state: TState, envelope: TEnvelope, prior_ns: int, current_ns: int, units: int
) -> TState:
    for name, value in (("prior", prior_ns), ("current", current_ns), ("units", units)):
        if type(value) is not int:
            raise ValueError(f"{name} must be an integer")
    if current_ns <= prior_ns:
        raise RuntimeContractError("monotonic cursor did not increase")
    if not 1 <= units <= MAX_CONCURRENT_LEASES:
        raise RuntimeContractError("device-unit count is outside the signed boundary")
    return state.charge_device_nanoseconds((current_ns - prior_ns) * units, envelope)


def process_id_for(claim_core: Mapping[str, object]) -> str:
    return sha256_bytes(canonical_json(dict(claim_core)))


_PROCESS_CLAIM_KEYS = {
    "schema", "scientific_outcome", "activation_record_sha256", "process_id",
    "process_sequence", "controller_pid", "controller_start_identity",
    "process_group_id", "argv", "behavior_source_sha256", "config_sha256",
    "stack_sha256", "numerical_mode_sha256", "device_identity", "device_units",
    "created_utc", "clock_kind", "boot_identity", "start_reading_ns",
    "immutable_control_sha256",
}
_LEASE_EXTRA_KEYS = {
    "last_charged_reading_ns", "cumulative_charge_ns", "heartbeat_deadline_ns",
    "outstanding_liability_ns", "prior_charge_event_sha256",
}
_PROCESS_RECORD_KEYS = {
    "schema", "scientific_outcome", "validity", "disposition", "invalid_cause",
    "activation_record_sha256", "process_claim_sha256", "process_id",
    "process_sequence", "behavior_source_sha256", "config_sha256", "stack_sha256",
    "numerical_mode_sha256", "device_identity", "device_units", "started_utc",
    "closed_utc", "cumulative_charge_ns", "final_charge_event_sha256",
    "final_t_state_sha256", "immutable_control_sha256",
}


def _require_sha256(value: object, name: str) -> str:
    if not isinstance(value, str) or _HEX64.fullmatch(value) is None:
        raise ValueError(f"{name} must be lowercase SHA-256")
    return value


def _process_identity_core(value: Mapping[str, object]) -> dict[str, object]:
    return {
        "activation_record_sha256": value["activation_record_sha256"],
        "argv": value["argv"],
        "behavior_source_sha256": value["behavior_source_sha256"],
        "boot_identity": value["boot_identity"],
        "config_sha256": value["config_sha256"],
        "device_identity": value["device_identity"],
        "device_units": value["device_units"],
        "numerical_mode_sha256": value["numerical_mode_sha256"],
        "process_sequence": value["process_sequence"],
        "stack_sha256": value["stack_sha256"],
    }


def build_process_claim(
    *,
    activation_record_sha256: str,
    process_sequence: int,
    controller_pid: int,
    controller_start_identity: str,
    process_group_id: int,
    argv: Iterable[str],
    behavior_source_sha256: str,
    config_sha256: str,
    stack_sha256: str,
    numerical_mode_sha256: str,
    device_identity: str,
    device_units: int,
    created_utc: str,
    boot_id: str,
    start_reading_ns: int,
    immutable_control_sha256: Mapping[str, str],
) -> dict[str, object]:
    from .accounting import parse_utc

    hashes = {
        "activation_record_sha256": activation_record_sha256,
        "behavior_source_sha256": behavior_source_sha256,
        "config_sha256": config_sha256,
        "stack_sha256": stack_sha256,
        "numerical_mode_sha256": numerical_mode_sha256,
    }
    for name, digest in hashes.items():
        _require_sha256(digest, name)
    if type(process_sequence) is not int or process_sequence < 0:
        raise ValueError("process sequence must be a non-negative integer")
    if type(controller_pid) is not int or controller_pid <= 0:
        raise ValueError("controller PID must be positive")
    if type(process_group_id) is not int or process_group_id <= 0:
        raise ValueError("process group id must be positive")
    if type(device_units) is not int or not 1 <= device_units <= MAX_CONCURRENT_LEASES:
        raise ValueError("device units must equal admitted behavior-capable streams")
    if type(start_reading_ns) is not int or start_reading_ns < 0:
        raise ValueError("start reading must be a non-negative integer")
    argv_tuple = tuple(argv)
    if not argv_tuple or not all(type(item) is str and item for item in argv_tuple):
        raise ValueError("canonical argv must contain named strings")
    if not controller_start_identity or not device_identity or not boot_id:
        raise ValueError("process, device, and boot identities must be named")
    parse_utc(created_utc)
    immutable = require_sha256_map(
        dict(immutable_control_sha256), name="immutable control"
    )
    core: dict[str, object] = {
        **hashes,
        "argv": list(argv_tuple),
        "boot_identity": boot_id,
        "device_identity": device_identity,
        "device_units": device_units,
        "process_sequence": process_sequence,
    }
    claim = {
        "schema": PROCESS_CLAIM_SCHEMA,
        "scientific_outcome": False,
        **core,
        "process_id": process_id_for(core),
        "controller_pid": controller_pid,
        "controller_start_identity": controller_start_identity,
        "process_group_id": process_group_id,
        "created_utc": created_utc,
        "clock_kind": CLOCK_KIND,
        "start_reading_ns": start_reading_ns,
        "immutable_control_sha256": immutable,
    }
    validate_process_claim(claim)
    return claim


def validate_process_claim(value: object) -> dict[str, object]:
    from .accounting import parse_utc

    if not isinstance(value, dict) or set(value) != _PROCESS_CLAIM_KEYS:
        raise ValueError("process claim fields differ")
    if value["schema"] != PROCESS_CLAIM_SCHEMA or value["scientific_outcome"] is not False:
        raise ValueError("process claim schema differs")
    for field in (
        "activation_record_sha256", "behavior_source_sha256", "config_sha256",
        "stack_sha256", "numerical_mode_sha256", "process_id",
    ):
        _require_sha256(value[field], field)
    if value["clock_kind"] != CLOCK_KIND:
        raise ValueError("process claim clock kind differs")
    if value["process_id"] != process_id_for(_process_identity_core(value)):
        raise ValueError("process id does not match its immutable identity")
    if type(value["process_sequence"]) is not int or value["process_sequence"] < 0:
        raise ValueError("process sequence is malformed")
    for field in ("controller_pid", "process_group_id", "device_units"):
        if type(value[field]) is not int or value[field] <= 0:
            raise ValueError(f"{field} is malformed")
    if value["device_units"] > MAX_CONCURRENT_LEASES:
        raise ValueError("device units exceed the concurrency cap")
    if type(value["start_reading_ns"]) is not int or value["start_reading_ns"] < 0:
        raise ValueError("process start cursor is malformed")
    if not isinstance(value["argv"], list) or not value["argv"] or not all(
        type(item) is str and item for item in value["argv"]
    ):
        raise ValueError("process argv is malformed")
    require_sha256_map(value["immutable_control_sha256"], name="immutable control")
    for field in (
        "controller_start_identity", "device_identity", "boot_identity"
    ):
        if not isinstance(value[field], str) or not value[field]:
            raise ValueError(f"process claim {field} is malformed")
    parse_utc(str(value["created_utc"]))
    reject_scientific_fields(value)
    return dict(value)


def validate_process_claim_against_activation(
    value: object,
    *,
    activation_record_sha256: str,
    immutable_control_sha256: Mapping[str, str],
) -> dict[str, object]:
    claim = validate_process_claim(value)
    _require_sha256(activation_record_sha256, "activation record")
    expected_hashes = require_sha256_map(
        dict(immutable_control_sha256), name="activation immutable control"
    )
    if canonical_json(claim["immutable_control_sha256"]) != canonical_json(
        expected_hashes
    ):
        raise ValueError("process claim immutable controls differ from activation")
    if claim["activation_record_sha256"] != activation_record_sha256:
        raise ValueError("process claim activation record hash differs")
    return claim


def build_active_lease(
    claim: Mapping[str, object], *, reservation: Reservation, prior_charge_event_sha256: str
) -> dict[str, object]:
    validated = validate_process_claim(dict(claim))
    if reservation.units != validated["device_units"]:
        raise ValueError("lease reservation units differ from the process claim")
    _require_sha256(prior_charge_event_sha256, "prior charge event")
    start = int(validated["start_reading_ns"])
    lease = {
        **validated,
        "schema": ACTIVE_LEASE_SCHEMA,
        "last_charged_reading_ns": start,
        "cumulative_charge_ns": 0,
        "heartbeat_deadline_ns": start + reservation.deadline_delta_ns,
        "outstanding_liability_ns": reservation.aggregate_liability_ns,
        "prior_charge_event_sha256": prior_charge_event_sha256,
    }
    validate_active_lease(lease)
    return lease


def validate_active_lease(value: object) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != _PROCESS_CLAIM_KEYS | _LEASE_EXTRA_KEYS:
        raise ValueError("active lease fields differ")
    claim = {key: item for key, item in value.items() if key not in _LEASE_EXTRA_KEYS}
    claim["schema"] = PROCESS_CLAIM_SCHEMA
    validate_process_claim(claim)
    if value["schema"] != ACTIVE_LEASE_SCHEMA:
        raise ValueError("active lease schema differs")
    for field in (
        "last_charged_reading_ns", "cumulative_charge_ns",
        "heartbeat_deadline_ns", "outstanding_liability_ns",
    ):
        if type(value[field]) is not int or value[field] < 0:
            raise ValueError(f"active lease {field} is malformed")
    if value["last_charged_reading_ns"] < value["start_reading_ns"]:
        raise ValueError("active lease cursor predates process start")
    if value["heartbeat_deadline_ns"] <= value["last_charged_reading_ns"]:
        raise ValueError("active lease deadline is not future")
    if value["outstanding_liability_ns"] <= 0:
        raise ValueError("active lease liability must be positive")
    expected_liability = int(value["device_units"]) * (
        int(value["heartbeat_deadline_ns"])
        - int(value["last_charged_reading_ns"])
    )
    if value["outstanding_liability_ns"] != expected_liability:
        raise ValueError("active lease liability and deadline differ")
    _require_sha256(value["prior_charge_event_sha256"], "prior charge event")
    return dict(value)


def validate_active_lease_against_claim(
    lease: object, claim: object
) -> tuple[dict[str, object], dict[str, object]]:
    lease_value = validate_active_lease(lease)
    claim_value = validate_process_claim(claim)
    lease_claim = {
        key: item for key, item in lease_value.items() if key not in _LEASE_EXTRA_KEYS
    }
    lease_claim["schema"] = PROCESS_CLAIM_SCHEMA
    if canonical_json(lease_claim) != canonical_json(claim_value):
        raise ValueError("lease does not contain the byte-exact durable claim")
    return lease_value, claim_value


def settle_active_lease(
    *,
    lease: Mapping[str, object],
    state: TState,
    envelope: TEnvelope,
    current_reading_ns: int,
    next_reservation: Reservation,
    charge_event_sha256: str,
) -> tuple[TState, dict[str, object]]:
    current = validate_active_lease(dict(lease))
    if next_reservation.units != current["device_units"]:
        raise ValueError("renewed reservation units differ")
    _require_sha256(charge_event_sha256, "charge event")
    next_state = settle_monotonic_delta(
        state=state,
        envelope=envelope,
        prior_ns=int(current["last_charged_reading_ns"]),
        current_ns=current_reading_ns,
        units=int(current["device_units"]),
    )
    delta = (current_reading_ns - int(current["last_charged_reading_ns"])) * int(
        current["device_units"]
    )
    renewed = {
        **current,
        "last_charged_reading_ns": current_reading_ns,
        "cumulative_charge_ns": int(current["cumulative_charge_ns"]) + delta,
        "heartbeat_deadline_ns": current_reading_ns + next_reservation.deadline_delta_ns,
        "outstanding_liability_ns": next_reservation.aggregate_liability_ns,
        "prior_charge_event_sha256": charge_event_sha256,
    }
    validate_active_lease(renewed)
    return next_state, renewed


def build_process_record(
    *,
    claim: Mapping[str, object],
    lease: Mapping[str, object],
    disposition: ProcessDisposition,
    invalid_cause: InvalidCause | None,
    closed_utc: str,
    final_charge_event: Mapping[str, object],
    final_state: TState,
) -> dict[str, object]:
    from .accounting import parse_utc

    lease_value, claim_value = validate_active_lease_against_claim(
        dict(lease), dict(claim)
    )
    if not isinstance(disposition, ProcessDisposition):
        raise ValueError("process disposition must be typed")
    if disposition is ProcessDisposition.INVALID:
        if not isinstance(invalid_cause, InvalidCause):
            raise ValueError("invalid process requires a typed public cause")
    elif invalid_cause is not None:
        raise ValueError("valid process disposition cannot carry invalid cause")
    event = validate_ledger_event(dict(final_charge_event))
    if event["event"] not in {"T_DEVICE_TIME_CHARGED", "T_RUNTIME_INVALID"}:
        raise ValueError("final process event is not a settlement event")
    event_data = event["data"]
    if not isinstance(event_data, dict):
        raise ValueError("final settlement payload is malformed")
    if event["event"] == "T_DEVICE_TIME_CHARGED" and (
        event_data["process_id"] != claim_value["process_id"]
    ):
        raise ValueError("final settlement process id differs")
    if event["event"] == "T_DEVICE_TIME_CHARGED" and (
        event_data["active_lease_sha256"]
        != sha256_bytes(canonical_json(lease_value))
    ):
        raise ValueError("final settlement lease hash differs")
    if canonical_json(event_data["t_state"]) != canonical_json(final_state.to_mapping()):
        raise ValueError("final settlement state differs")
    claim_sha256 = sha256_bytes(canonical_json(claim_value))
    final_charge_event_sha256 = str(event["entry_sha256"])
    closed = parse_utc(closed_utc)
    if closed < parse_utc(str(claim_value["created_utc"])):
        raise ValueError("process close predates process start")
    final_state_sha256 = sha256_bytes(canonical_json(final_state.to_mapping()))
    record = {
        "schema": PROCESS_RECORD_SCHEMA,
        "scientific_outcome": False,
        "validity": (
            "INVALID_PROCESS_RECORD"
            if disposition is ProcessDisposition.INVALID
            else "VALID_PROCESS_RECORD"
        ),
        "disposition": disposition.value,
        "invalid_cause": invalid_cause.value if invalid_cause else None,
        "activation_record_sha256": claim_value["activation_record_sha256"],
        "process_claim_sha256": claim_sha256,
        "process_id": claim_value["process_id"],
        "process_sequence": claim_value["process_sequence"],
        "behavior_source_sha256": claim_value["behavior_source_sha256"],
        "config_sha256": claim_value["config_sha256"],
        "stack_sha256": claim_value["stack_sha256"],
        "numerical_mode_sha256": claim_value["numerical_mode_sha256"],
        "device_identity": claim_value["device_identity"],
        "device_units": claim_value["device_units"],
        "started_utc": claim_value["created_utc"],
        "closed_utc": closed_utc,
        "cumulative_charge_ns": lease_value["cumulative_charge_ns"],
        "final_charge_event_sha256": final_charge_event_sha256,
        "final_t_state_sha256": final_state_sha256,
        "immutable_control_sha256": claim_value["immutable_control_sha256"],
    }
    validate_process_record(record)
    return record


def validate_process_record(value: object) -> dict[str, object]:
    from .accounting import parse_utc

    if not isinstance(value, dict) or set(value) != _PROCESS_RECORD_KEYS:
        raise ValueError("process record fields differ")
    if value["schema"] != PROCESS_RECORD_SCHEMA or value["scientific_outcome"] is not False:
        raise ValueError("process record schema differs")
    disposition = ProcessDisposition(str(value["disposition"]))
    cause = value["invalid_cause"]
    if disposition is ProcessDisposition.INVALID:
        if not isinstance(cause, str):
            raise ValueError("invalid process record lacks a cause")
        InvalidCause(cause)
        if value["validity"] != "INVALID_PROCESS_RECORD":
            raise ValueError("invalid process record validity differs")
    elif cause is not None or value["validity"] != "VALID_PROCESS_RECORD":
        raise ValueError("valid process record carries invalidity")
    for field in (
        "activation_record_sha256", "process_claim_sha256", "process_id",
        "behavior_source_sha256", "config_sha256", "stack_sha256",
        "numerical_mode_sha256", "final_charge_event_sha256",
        "final_t_state_sha256",
    ):
        _require_sha256(value[field], field)
    if type(value["cumulative_charge_ns"]) is not int or value["cumulative_charge_ns"] < 0:
        raise ValueError("process record charge is malformed")
    if type(value["process_sequence"]) is not int or value["process_sequence"] < 0:
        raise ValueError("process record sequence is malformed")
    if type(value["device_units"]) is not int or not (
        1 <= value["device_units"] <= MAX_CONCURRENT_LEASES
    ):
        raise ValueError("process record device units are malformed")
    if not isinstance(value["device_identity"], str) or not value["device_identity"]:
        raise ValueError("process record device identity is malformed")
    started = parse_utc(str(value["started_utc"]))
    closed = parse_utc(str(value["closed_utc"]))
    if closed < started:
        raise ValueError("process record closes before it starts")
    require_sha256_map(value["immutable_control_sha256"], name="immutable control")
    reject_scientific_fields(value)
    return dict(value)


def require_sha256_map(value: object, *, name: str) -> dict[str, str]:
    if not isinstance(value, dict) or not value:
        raise ValueError(f"{name} must be a nonempty object")
    result: dict[str, str] = {}
    for path, digest in value.items():
        if not isinstance(path, str) or not path or not isinstance(digest, str):
            raise ValueError(f"{name} entries are malformed")
        if _HEX64.fullmatch(digest) is None:
            raise ValueError(f"{name} contains a non-SHA-256 value")
        result[path] = digest
    return result


def verify_hash_map(repo: Path, value: object, *, name: str) -> list[str]:
    failures: list[str] = []
    try:
        mapping = require_sha256_map(value, name=name)
    except ValueError as error:
        return [str(error)]
    for relative, expected in sorted(mapping.items()):
        path = repo / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"{name} path is missing or aliased: {relative}")
        elif sha256_file(path) != expected:
            failures.append(f"{name} hash differs: {relative}")
    return failures


def reject_scientific_fields(value: object, *, path: str = "record") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{path} contains a non-string key")
            lowered = key.lower()
            if lowered in _PUBLIC_FORBIDDEN_KEYS or re.fullmatch(r"c[1-6]", lowered):
                raise ValueError(f"{path} contains forbidden scientific field {key}")
            reject_scientific_fields(item, path=f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_scientific_fields(item, path=f"{path}[{index}]")


_EVENT_DATA_KEYS = {
    "T_ACTIVATED": {
        "authorization_sha256", "claim_sha256", "device_policy_token",
        "envelope_token", "scientific_outcome", "t_state",
    },
    "T_PROCESS_STARTED": {
        "process_claim_sha256", "process_id", "scientific_outcome",
    },
    "T_DEVICE_TIME_CHARGED": {
        "active_lease_sha256", "charge_ns", "process_id",
        "scientific_outcome", "t_state",
    },
    "T_REVIEW_COMPLETED": {
        "review_record_sha256", "scientific_outcome", "t_state",
    },
    "T_OPERATIONAL_PAUSE": {
        "checkpoint_path", "checkpoint_sha256", "reason", "resets_e3",
        "scientific_outcome", "t_state",
    },
    "T_PROCESS_STOPPED": {
        "process_id", "process_record_sha256", "scientific_outcome", "t_state",
    },
    "T_RUNTIME_INVALID": {
        "invalid_cause", "invalidity_record_sha256", "required_action",
        "scientific_outcome", "t_state",
    },
    "T_AUTHOR_STOP": {
        "author_decision_sha256", "scientific_outcome", "t_state",
    },
    "T_ENVELOPE_EXHAUSTED": {
        "resource_axis", "scientific_outcome", "t_state",
    },
}


def validate_ledger_event(value: object) -> dict[str, object]:
    from .accounting import parse_utc

    if not isinstance(value, dict) or set(value) != {
        "data", "entry_sha256", "event", "previous_sha256", "sequence",
        "timestamp_utc",
    }:
        raise ValueError("ledger event fields differ")
    event = value["event"]
    if not isinstance(event, str) or event not in POST_ACTIVATION_EVENTS:
        raise ValueError("ledger event is outside the closed vocabulary")
    data = value["data"]
    if not isinstance(data, dict) or set(data) != _EVENT_DATA_KEYS[event]:
        raise ValueError(f"{event} payload fields differ")
    if data["scientific_outcome"] is not False:
        raise ValueError(f"{event} must be non-scientific")
    if type(value["sequence"]) is not int or value["sequence"] < 0:
        raise ValueError("ledger event sequence is malformed")
    _require_sha256(value["previous_sha256"], "previous ledger event")
    _require_sha256(value["entry_sha256"], "ledger event")
    payload = {key: item for key, item in value.items() if key != "entry_sha256"}
    if value["entry_sha256"] != sha256_bytes(canonical_json(payload)):
        raise ValueError("ledger event hash differs")
    parse_utc(str(value["timestamp_utc"]))
    reject_scientific_fields(data, path=f"ledger.{event}")
    if event in STATE_BEARING_EVENTS:
        state = data.get("t_state")
        if not isinstance(state, dict):
            raise ValueError(f"{event} lacks a complete post-state")
        parsed_state = TState.from_mapping(state)
    elif "t_state" in data:
        raise ValueError("T_PROCESS_STARTED must not carry t_state")
    if event == "T_RUNTIME_INVALID":
        InvalidCause(str(data["invalid_cause"]))
        _require_sha256(data["invalidity_record_sha256"], "invalidity record")
        if data["required_action"] != "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY":
            raise ValueError("runtime invalidity event recovery route differs")
    if event == "T_ENVELOPE_EXHAUSTED" and data["resource_axis"] != "E1":
        raise ValueError("pre-WP-6 exhaustion may only name E1")
    hash_fields = {
        "T_ACTIVATED": ("authorization_sha256", "claim_sha256"),
        "T_PROCESS_STARTED": ("process_claim_sha256", "process_id"),
        "T_DEVICE_TIME_CHARGED": ("active_lease_sha256", "process_id"),
        "T_REVIEW_COMPLETED": ("review_record_sha256",),
        "T_OPERATIONAL_PAUSE": ("checkpoint_sha256",),
        "T_PROCESS_STOPPED": ("process_id", "process_record_sha256"),
        "T_RUNTIME_INVALID": ("invalidity_record_sha256",),
        "T_AUTHOR_STOP": ("author_decision_sha256",),
        "T_ENVELOPE_EXHAUSTED": (),
    }
    for field in hash_fields[event]:
        _require_sha256(data[field], f"{event} {field}")
    if event == "T_ACTIVATED":
        if any(
            not isinstance(data[field], str) or not data[field]
            for field in ("device_policy_token", "envelope_token")
        ):
            raise ValueError("activation event tokens are malformed")
        if parsed_state.activated_utc != value["timestamp_utc"]:
            raise ValueError("activation event timestamp and state differ")
        if parsed_state.device_nanoseconds != 0 or parsed_state.candidate_ids:
            raise ValueError("activation event state is not pristine-active")
    elif event == "T_DEVICE_TIME_CHARGED":
        if type(data["charge_ns"]) is not int or data["charge_ns"] <= 0:
            raise ValueError("device-time event charge is malformed")
    elif event == "T_OPERATIONAL_PAUSE":
        if (
            not isinstance(data["checkpoint_path"], str)
            or not data["checkpoint_path"]
            or not isinstance(data["reason"], str)
            or not data["reason"]
            or data["resets_e3"] is not False
        ):
            raise ValueError("operational-pause payload values differ")
    elif event == "T_AUTHOR_STOP" and not parsed_state.author_stopped:
        raise ValueError("author-stop event lacks an author-stopped post-state")
    elif event == "T_ENVELOPE_EXHAUSTED" and (
        parsed_state.device_nanoseconds < 168 * NANOSECONDS_PER_HOUR
    ):
        raise ValueError("E1 exhaustion event precedes the signed E1 cap")
    return dict(value)


def validate_invalidity_record(value: object) -> dict[str, object]:
    expected = {
        "schema", "scientific_outcome", "validity", "invalid_cause",
        "transaction_kind", "durable_step_index", "affected_path_sha256",
        "clock_kind", "boot_identity", "observed_utc",
        "outstanding_liability_ns", "required_action",
    }
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError("runtime invalidity fields differ")
    if value["schema"] != INVALIDITY_SCHEMA or value["scientific_outcome"] is not False:
        raise ValueError("runtime invalidity schema differs")
    if value["validity"] != "INVALID_PROCESS_RECORD":
        raise ValueError("runtime invalidity validity differs")
    InvalidCause(str(value["invalid_cause"]))
    if value["required_action"] != "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY":
        raise ValueError("runtime invalidity recovery route differs")
    if type(value["durable_step_index"]) is not int or value["durable_step_index"] < 0:
        raise ValueError("runtime invalidity step is malformed")
    if type(value["outstanding_liability_ns"]) is not int or value["outstanding_liability_ns"] < 0:
        raise ValueError("runtime invalidity liability is malformed")
    reject_scientific_fields(value)
    return dict(value)


def load_runtime_invalidity(path: Path) -> dict[str, object]:
    return validate_invalidity_record(load_canonical_json(path))


class RealTCapability:
    """Nominal exact type. No factory exists in the inactive implementation."""

    __slots__ = ("_token",)

    def __init__(self, token: object) -> None:
        del token
        raise RuntimeContractError(
            "real-T capability requires the separately reviewed generic metered harness"
        )


def issue_real_t_capability(*args: object, **kwargs: object) -> None:
    del args, kwargs
    raise RuntimeContractError(
        "generic metered learner harness is absent; T activation remains blocked"
    )
