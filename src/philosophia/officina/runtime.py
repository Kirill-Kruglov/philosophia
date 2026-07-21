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

    @property
    def aggregate_liability_ns(self) -> int:
        return self.units * self.liability_ns_per_unit

    @property
    def deadline_delta_ns(self) -> int:
        return self.liability_ns_per_unit


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
    live_liabilities_ns: Iterable[int],
    requested_units: int = DEVICE_UNITS_PER_LEASE,
) -> Reservation | None:
    if type(requested_units) is not int or not 1 <= requested_units <= MAX_CONCURRENT_LEASES:
        raise ValueError("requested behavior-capable stream count is invalid")
    liabilities = tuple(live_liabilities_ns)
    if any(type(value) is not int or value <= 0 for value in liabilities):
        raise ValueError("live liability values must be positive integers")
    if len(liabilities) + requested_units > MAX_CONCURRENT_LEASES:
        raise RuntimeContractError("behavior-capable concurrency cap reached")
    if state.activated_utc is None or state.author_stopped or state.resume_review_pending:
        raise RuntimeContractError("T runtime state is unavailable")

    live_total = sum(liabilities)
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
    reject_scientific_fields(value)
    return dict(value)


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
    _require_sha256(value["prior_charge_event_sha256"], "prior charge event")
    return dict(value)


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
    claim_sha256: str,
    lease: Mapping[str, object],
    disposition: ProcessDisposition,
    invalid_cause: InvalidCause | None,
    closed_utc: str,
    final_charge_event_sha256: str,
    final_t_state_sha256: str,
) -> dict[str, object]:
    from .accounting import parse_utc

    claim_value = validate_process_claim(dict(claim))
    lease_value = validate_active_lease(dict(lease))
    if claim_value["process_id"] != lease_value["process_id"]:
        raise ValueError("claim and lease process identities differ")
    if not isinstance(disposition, ProcessDisposition):
        raise ValueError("process disposition must be typed")
    if disposition is ProcessDisposition.INVALID:
        if not isinstance(invalid_cause, InvalidCause):
            raise ValueError("invalid process requires a typed public cause")
    elif invalid_cause is not None:
        raise ValueError("valid process disposition cannot carry invalid cause")
    for name, digest in (
        ("process claim", claim_sha256),
        ("final charge event", final_charge_event_sha256),
        ("final T state", final_t_state_sha256),
    ):
        _require_sha256(digest, name)
    parse_utc(closed_utc)
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
        "final_t_state_sha256": final_t_state_sha256,
        "immutable_control_sha256": claim_value["immutable_control_sha256"],
    }
    validate_process_record(record)
    return record


def validate_process_record(value: object) -> dict[str, object]:
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
            if key in _PUBLIC_FORBIDDEN_KEYS or re.fullmatch(r"c[1-6]", lowered):
                raise ValueError(f"{path} contains forbidden scientific field {key}")
            reject_scientific_fields(item, path=f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_scientific_fields(item, path=f"{path}[{index}]")


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
