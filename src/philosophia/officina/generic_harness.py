"""Fail-closed implementation of the signed Officina generic T harness.

This module is a mechanical implementation of the composite, signed contract:

- ``successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`` through
  ``…_V2_3_1_CORRECTION.md`` (the generic metered harness contract, v1..v2.3.1);
- ``successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`` through
  ``…_V1_1_1_CORRECTION.md`` (the frozen-batch settlement core amendment).

It deliberately contains control-plane code only.  It neither selects
scientific work nor imports a learner, plugin, backend, or predecessor
surface.  Every name below is imported directly; no namespace-facade class
re-exports another module's symbols.
"""

from __future__ import annotations

import dataclasses
import enum
import os
import subprocess
import time
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence

from .accounting import (
    BatchSettlementAuthority,
    NANOSECONDS_PER_HOUR,
    NANOSECONDS_PER_SECOND,
    TEnvelope,
    TState,
    parse_utc,
)
from .activation import utc_now as _activation_utc_now
from .canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    fsync_directory,
    hash_mapping,
    load_canonical_json,
    sha256_bytes,
    sha256_file,
)
from .checkpoint import record_operational_pause, verify_resume
from .ledger import AppendOnlyLedger, GENESIS
from .runtime import (
    CLOCK_KIND,
    HEARTBEAT_LIABILITY_SECONDS,
    INVALIDITY_SCHEMA,
    InvalidCause,
    ProcessDisposition,
    Reservation,
    ReservationRoute,
    REVIEW_RECORD_SCHEMA,
    RuntimeContractError,
    RuntimeLock,
    boot_identity,
    build_active_lease,
    build_process_claim,
    build_process_record,
    reject_scientific_fields,
    require_sha256_map,
    reservation_for,
    reservation_route,
    settle_active_lease,
    validate_active_lease,
    validate_active_lease_against_claim,
    validate_invalidity_record,
    validate_ledger_event,
    validate_process_claim,
    validate_process_claim_against_activation,
    validate_process_record,
)

import re


# --------------------------------------------------------------------------
# Canonical repository paths (relative to the repository root)
# --------------------------------------------------------------------------

RUNTIME_ROOT = Path("successor/officina/runtime")
LEDGER_RELATIVE = Path("successor/officina/T_LEDGER.md")
LEDGER_HEAD_RELATIVE = Path("successor/officina/T_LEDGER.md.head.json")
ENVELOPE_RELATIVE = Path("successor/officina/T_ENVELOPE.json")
STATE_RELATIVE = RUNTIME_ROOT / "T_STATE.json"
ACTIVATION_RECORD_RELATIVE = RUNTIME_ROOT / "T_ACTIVATION_RECORD.json"
LOCK_RELATIVE = RUNTIME_ROOT / "T_RUNTIME.lock"
CLAIMS_RELATIVE = RUNTIME_ROOT / "T_PROCESS_CLAIMS"
LEASES_RELATIVE = RUNTIME_ROOT / "T_ACTIVE_LEASES"
RECORDS_RELATIVE = RUNTIME_ROOT / "T_PROCESS_RECORDS"
INVALIDITIES_RELATIVE = RUNTIME_ROOT / "T_RUNTIME_INVALIDITIES"
BATCH_CLAIMS_RELATIVE = RUNTIME_ROOT / "T_BATCH_SETTLEMENT_CLAIMS"
BATCH_OVERRIDES_RELATIVE = RUNTIME_ROOT / "T_BATCH_SETTLEMENT_OVERRIDES"
PENDING_RESUME_RELATIVE = RUNTIME_ROOT / "T_PENDING_RESUME_CHECKPOINTS"
RECOVERY_RELATIVE = RUNTIME_ROOT / "T_RECOVERY_DISPOSITIONS"
REVIEW_RECORDS_RELATIVE = RUNTIME_ROOT / "T_REVIEW_RECORDS"
PAUSE_CHECKPOINTS_RELATIVE = RUNTIME_ROOT / "T_PAUSE_CHECKPOINTS"

CPU_ADAPTER_IDENTITY = "philosophia.officina.cpu-monotonic-meter.v1"

_HEX64 = re.compile(r"[0-9a-f]{64}\Z")
_ISSUANCE_TOKEN = object()

DRAFT_MANIFEST_SCHEMA = "philosophia.officina.t-draft-manifest.v1"
BATCH_CLAIM_SCHEMA = "philosophia.officina.t-batch-settlement-claim.v1"
BATCH_OVERRIDE_SCHEMA = "philosophia.officina.t-batch-settlement-invalidity-override.v1"
PENDING_RESUME_SCHEMA = "philosophia.officina.t-pending-resume-checkpoint.v1"
RECOVERY_DISPOSITION_SCHEMA = "philosophia.officina.t-recovery-disposition.v1"
REQUIRED_ACTION = "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY"


class HarnessRefused(RuntimeError):
    """A safety or contract precondition was not established."""


# --------------------------------------------------------------------------
# Closed enumerations (v2 §2a/§2b; amendment §1a/§1b/§1c)
# --------------------------------------------------------------------------


class GlobalState(str, enum.Enum):
    """The eight exclusive, total global T states (v2 §2a)."""

    G0 = "GENESIS_INACTIVE"
    G1 = "ACTIVE"
    G2 = "E3_DUE"
    G3 = "PAUSED"
    G4 = "RESUME_REVIEW_PENDING"
    G5 = "RUNTIME_INVALID"
    G6 = "AUTHOR_STOPPED"
    G7 = "ENVELOPE_EXHAUSTED"


class ProcessState(str, enum.Enum):
    """The six exclusive, total per-process states (v2 §2b)."""

    P0 = "ABSENT"
    P1 = "CLAIMED"
    P2 = "STARTED"
    P3 = "LIVE"
    P4 = "CLOSED_VALID"
    P5 = "CLOSED_INVALID"


class BatchReason(str, enum.Enum):
    E1_BOUNDARY = "E1_BOUNDARY"
    E3_BOUNDARY = "E3_BOUNDARY"
    RUNTIME_INVALIDITY = "RUNTIME_INVALIDITY"
    RECOVERY_SETTLEMENT = "RECOVERY_SETTLEMENT"


class StreamClassification(str, enum.Enum):
    TIMELY_KNOWN = "TIMELY_KNOWN"
    LATE_KNOWN = "LATE_KNOWN"
    UNKNOWABLE = "UNKNOWABLE"


class BatchAutomatonAction(str, enum.Enum):
    """The finite next-actions of the amendment §4a/§4b prefix automaton."""

    APPEND_CHARGE = "APPEND_CHARGE"
    WRITE_INVALID_DETAIL = "WRITE_INVALID_DETAIL"
    APPEND_INVALID_EVENT = "APPEND_INVALID_EVENT"
    WRITE_INVALID_RECORD = "WRITE_INVALID_RECORD"
    WRITE_VALID_RECORD = "WRITE_VALID_RECORD"
    APPEND_STOPPED = "APPEND_STOPPED"
    REMOVE_LEASE = "REMOVE_LEASE"
    APPEND_EXHAUSTION = "APPEND_EXHAUSTION"
    ARCHIVE = "ARCHIVE"
    RESOLVED = "RESOLVED"


# Lifecycle tables as data (v2 §2b/§2a), used only for legality checks; they
# select no scientific cell and carry no execution authority by themselves.
PROCESS_LIFECYCLE_TRANSITIONS: dict[ProcessState, tuple[ProcessState, ...]] = {
    ProcessState.P0: (ProcessState.P1,),
    ProcessState.P1: (ProcessState.P2,),
    ProcessState.P2: (ProcessState.P3,),
    ProcessState.P3: (ProcessState.P3, ProcessState.P4, ProcessState.P5),
    ProcessState.P4: (),
    ProcessState.P5: (),
}
GLOBAL_LIFECYCLE_TRANSITIONS: dict[GlobalState, tuple[GlobalState, ...]] = {
    GlobalState.G0: (GlobalState.G1,),
    GlobalState.G1: (
        GlobalState.G1,
        GlobalState.G2,
        GlobalState.G3,
        GlobalState.G5,
        GlobalState.G6,
        GlobalState.G7,
    ),
    GlobalState.G2: (GlobalState.G1, GlobalState.G5),
    GlobalState.G3: (GlobalState.G1, GlobalState.G4, GlobalState.G5),
    GlobalState.G4: (GlobalState.G1, GlobalState.G5),
    GlobalState.G5: (GlobalState.G5, GlobalState.G1),
    GlobalState.G6: (),
    GlobalState.G7: (),
}


def is_legal_process_transition(current: ProcessState, next_state: ProcessState) -> bool:
    return next_state in PROCESS_LIFECYCLE_TRANSITIONS[current]


def is_legal_global_transition(current: GlobalState, next_state: GlobalState) -> bool:
    return next_state in GLOBAL_LIFECYCLE_TRANSITIONS[current]


# --------------------------------------------------------------------------
# Generic validation primitives
# --------------------------------------------------------------------------


def _sha(value: object, name: str = "hash") -> str:
    if not isinstance(value, str) or _HEX64.fullmatch(value) is None:
        raise ValueError(f"{name} must be lowercase SHA-256")
    return value


def _utc(value: object, name: str = "timestamp") -> str:
    if not isinstance(value, str):
        raise ValueError(f"{name} must be canonical UTC")
    parse_utc(value)
    return value


def _integer(value: object, name: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer at least {minimum}")
    return value


def _exact(value: object, keys: set[str], name: str) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != keys:
        raise ValueError(f"{name} fields differ")
    reject_scientific_fields(value, path=name)
    return dict(value)


# --------------------------------------------------------------------------
# Pure helpers (testable without a filesystem)
# --------------------------------------------------------------------------


def dominant_invalid_cause(causes: Iterable[InvalidCause | str]) -> InvalidCause:
    """Return the one public cause allowed by the signed precedence table.

    Fixed precedence (v2 §2a): ``HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE``.
    """

    values = {InvalidCause(item) for item in causes}
    if not values:
        raise ValueError("invalidity dominance requires an observed cause")
    for cause in (
        InvalidCause.HASH,
        InvalidCause.FILESYSTEM,
        InvalidCause.CLOCK,
        InvalidCause.PROCESS,
        InvalidCause.RESOURCE,
    ):
        if cause in values:
            return cause
    raise AssertionError("closed InvalidCause enum changed")


def allocate_unknown_pool_shares(
    remaining_ns: int, known_total_ns: int, unknown_stream_count: int
) -> tuple[int, int, int, tuple[int, ...]]:
    """Pure exact unknown-pool allocation (amendment §1f duty 6; v2.1 §A).

    Returns ``(U, q, r, shares)`` where ``U = max(m, remaining - known)``,
    ``q = floor(U / m)``, ``r = U mod m``, and ``shares`` assigns ``q + 1`` ns
    to the first ``r`` streams (in canonical ascending order) and ``q`` to the
    rest.  ``sum(shares) == U`` exactly; every share is at least 1 ns whenever
    ``m > 0``.
    """

    remaining = _integer(remaining_ns, "remaining_ns")
    known = _integer(known_total_ns, "known_total_ns")
    count = _integer(unknown_stream_count, "unknown_stream_count")
    if count == 0:
        return (0, 0, 0, ())
    pool = max(count, remaining - known)
    quotient, remainder = divmod(pool, count)
    shares = tuple(quotient + (1 if index < remainder else 0) for index in range(count))
    if sum(shares) != pool or min(shares) < 1:
        raise AssertionError("unknown-pool arithmetic lost conservation")
    return pool, quotient, remainder, shares


def classify_stream(
    *,
    interval_start_reading_ns: int,
    interval_end_reading_ns: int | None,
    backend_synchronized: bool,
    heartbeat_deadline_ns: int,
) -> StreamClassification:
    """Pure per-stream classification (amendment §D2b; signed §4c cases a/b/c)."""

    if interval_end_reading_ns is None:
        if backend_synchronized is not False:
            raise ValueError("an unknowable stream must be unsynchronized")
        return StreamClassification.UNKNOWABLE
    if backend_synchronized is not True or interval_end_reading_ns <= interval_start_reading_ns:
        raise ValueError("a known stream interval must be a positive synchronized interval")
    return (
        StreamClassification.TIMELY_KNOWN
        if interval_end_reading_ns <= heartbeat_deadline_ns
        else StreamClassification.LATE_KNOWN
    )


def derive_process_state(
    *, claimed: bool, started: bool, leased: bool, record: Mapping[str, object] | None
) -> ProcessState:
    """Pure per-process phase classifier from durable artifact presence."""

    if record is not None:
        disposition = ProcessDisposition(str(record["disposition"]))
        return ProcessState.P5 if disposition is ProcessDisposition.INVALID else ProcessState.P4
    if leased:
        return ProcessState.P3
    if started:
        return ProcessState.P2
    if claimed:
        return ProcessState.P1
    return ProcessState.P0


def derive_global_state(
    *,
    state: TState,
    envelope: TEnvelope,
    now_utc: str,
    last_event: str | None,
    live_process_count: int,
) -> GlobalState:
    """Pure global-phase classifier (v2 §2a dominance, simple/common case).

    ``GenericHarness.global_state`` refines this with the durable G5-admission
    predicate, because an unresolved invalidity is not always the last ledger
    event (a batch may append a later charge for a different process).
    """

    if state.activated_utc is None:
        return GlobalState.G0
    if state.author_stopped:
        return GlobalState.G6
    if state.exhausted(envelope):
        return GlobalState.G7
    if state.resume_review_pending:
        return GlobalState.G4
    if state.review_due(envelope, now_utc):
        return GlobalState.G2
    if live_process_count == 0 and last_event == "T_OPERATIONAL_PAUSE":
        return GlobalState.G3
    return GlobalState.G1


def _ledger_suffix_after(entries: list[dict[str, object]], pre_hash: str) -> list[dict[str, object]]:
    if pre_hash == GENESIS:
        return list(entries)
    for index, entry in enumerate(entries):
        if entry["entry_sha256"] == pre_hash:
            return entries[index + 1 :]
    raise HarnessRefused("batch pre-ledger entry is not an ancestor of the current chain")


# --------------------------------------------------------------------------
# Device-time capability object model
# --------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class RuntimeView:
    """A read-only snapshot of the durable runtime, used by callers/tests."""

    t_state: TState
    ledger_head_sha256: str
    live_process_ids: tuple[str, ...]
    phase: GlobalState


@dataclasses.dataclass(frozen=True)
class SystemClock:
    def monotonic_ns(self) -> int:
        return time.clock_gettime_ns(time.CLOCK_MONOTONIC)

    def utc_now(self) -> str:
        return _activation_utc_now()


@dataclasses.dataclass(frozen=True)
class CpuMonotonicMeter:
    """The CPU adapter's cursor is a monotonic kernel-clock observation."""

    adapter_identity: str = CPU_ADAPTER_IDENTITY

    def read(self, process: Mapping[str, object] | None = None) -> int:
        del process
        return time.clock_gettime_ns(time.CLOCK_MONOTONIC)


class SubprocessProcessOps:
    def start(self, argv: Sequence[str]) -> "subprocess.Popen[bytes]":
        if not argv or any(type(item) is not str or not item for item in argv):
            raise HarnessRefused("process argv is malformed")
        return subprocess.Popen(list(argv), start_new_session=True)

    def alive(self, pid: int) -> bool:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True

    def terminate_group(self, process_group_id: int) -> None:
        try:
            os.killpg(process_group_id, 15)  # SIGTERM by integer; no `signal` import.
        except ProcessLookupError:
            pass


class RealTCapability:
    """A nominal capability which only this harness can issue after admission."""

    __slots__ = ("_token", "__weakref__")

    def __init__(self, token: object) -> None:
        if token is not _ISSUANCE_TOKEN:
            raise RuntimeContractError("real-T capability is harness-issued only")
        self._token = token


def _issue_capability(token: object) -> RealTCapability:
    if token is not _ISSUANCE_TOKEN:
        raise HarnessRefused("capability issuance token differs")
    return RealTCapability(token)


class ReleaseToken:
    """A one-use, non-exportable release token (v2 §5b isolation protocol)."""

    __slots__ = (
        "activation_record_sha256",
        "process_id",
        "lease_sha256",
        "operation_id",
        "result_sha256",
        "charge_event_sha256",
        "_redeemed",
    )

    def __init__(
        self,
        *,
        activation_record_sha256: str,
        process_id: str,
        lease_sha256: str,
        operation_id: str,
        result_sha256: str,
        charge_event_sha256: str,
    ) -> None:
        _sha(activation_record_sha256, "activation record")
        _sha(lease_sha256, "lease")
        _sha(result_sha256, "result")
        _sha(charge_event_sha256, "charge event")
        if not isinstance(process_id, str) or not process_id:
            raise ValueError("release token process id is malformed")
        if not isinstance(operation_id, str) or not operation_id:
            raise ValueError("release token operation id is malformed")
        self.activation_record_sha256 = activation_record_sha256
        self.process_id = process_id
        self.lease_sha256 = lease_sha256
        self.operation_id = operation_id
        self.result_sha256 = result_sha256
        self.charge_event_sha256 = charge_event_sha256
        self._redeemed = False

    def redeem(self) -> None:
        if self._redeemed:
            raise HarnessRefused("release token already redeemed")
        self._redeemed = True


# --------------------------------------------------------------------------
# Meter evidence and batch-claim structures (amendment v1.1 + v1.1.1 D2)
# --------------------------------------------------------------------------

_STREAM_KEYS = {
    "stream_index",
    "process_id",
    "classification",
    "known_charge_ns",
    "unknown_share_ns",
    "meter_evidence",
}
_PROCESS_KEYS = {
    "process_id",
    "process_sequence",
    "active_lease_sha256",
    "known_charge_ns",
    "unknown_share_ns",
    "charge_ns",
    "disposition",
    "invalid_cause",
}
_OMITTED_KEYS = {"process_id", "omission_reason", "ancestor_claim_sha256"}
_BATCH_KEYS = {
    "schema",
    "scientific_outcome",
    "batch_reason",
    "pre_ledger_entry_sha256",
    "pre_ledger_head_sha256",
    "pre_state_sha256",
    "created_utc",
    "remaining_ns",
    "known_total_ns",
    "unknown_stream_count",
    "unknown_pool_ns",
    "unknown_share_quotient_ns",
    "unknown_share_remainder_count",
    "dominant_cause",
    "streams",
    "processes",
    "omitted",
    "recovery_disposition_sha256",
}
_METER_EVIDENCE_KEYS = {
    "clock_kind",
    "boot_identity",
    "adapter_identity",
    "interval_start_reading_ns",
    "interval_end_reading_ns",
    "backend_synchronized",
    "observed_utc",
}


def _validate_meter_evidence(
    value: object,
    *,
    stream: Mapping[str, object],
    lease: Mapping[str, object] | None,
    created_utc: str,
) -> dict[str, object]:
    evidence = _exact(value, _METER_EVIDENCE_KEYS, "meter_evidence")
    if evidence["clock_kind"] != CLOCK_KIND:
        raise ValueError("meter evidence clock kind differs")
    if not isinstance(evidence["adapter_identity"], str) or not evidence["adapter_identity"]:
        raise ValueError("meter adapter identity is malformed")
    if not isinstance(evidence["boot_identity"], str) or not evidence["boot_identity"]:
        raise ValueError("meter evidence boot identity is malformed")
    if lease is not None and evidence["boot_identity"] != lease["boot_identity"]:
        raise ValueError("meter evidence boot identity differs from the owning lease")
    start = _integer(evidence["interval_start_reading_ns"], "interval start")
    if lease is not None and start < int(lease["last_charged_reading_ns"]):
        raise ValueError("meter interval predates the durable cursor")
    observed = _utc(evidence["observed_utc"], "meter observation")
    if parse_utc(observed) > parse_utc(created_utc):
        raise ValueError("meter observation follows claim creation")
    classification = StreamClassification(str(stream["classification"]))
    end = evidence["interval_end_reading_ns"]
    if classification is StreamClassification.UNKNOWABLE:
        if end is not None or evidence["backend_synchronized"] is not False:
            raise ValueError("unknowable meter evidence differs")
    else:
        if type(end) is not int or end <= start or evidence["backend_synchronized"] is not True:
            raise ValueError("known meter interval differs")
        if int(stream["known_charge_ns"]) != end - start:
            raise ValueError("known charge does not match the inline meter interval")
        if lease is not None:
            expected = (
                StreamClassification.TIMELY_KNOWN
                if end <= int(lease["heartbeat_deadline_ns"])
                else StreamClassification.LATE_KNOWN
            )
            if classification is not expected:
                raise ValueError("stream timely/late classification differs")
    return evidence


def _validate_streams(
    streams_value: object,
    processes: Mapping[str, Mapping[str, object]],
    leases: Mapping[str, Mapping[str, object]] | None,
    created_utc: str,
) -> list[dict[str, object]]:
    if not isinstance(streams_value, list) or not streams_value:
        raise ValueError("batch streams must be a nonempty list")
    streams: list[dict[str, object]] = []
    for position, raw in enumerate(streams_value, 1):
        stream = _exact(raw, _STREAM_KEYS, "batch stream")
        if stream["stream_index"] != position:
            raise ValueError("stream indexes must be ascending and contiguous")
        process_id = _sha(stream["process_id"], "stream process id")
        if process_id not in processes:
            raise ValueError("stream references a non-enumerated process")
        classification = StreamClassification(str(stream["classification"]))
        known, share = stream["known_charge_ns"], stream["unknown_share_ns"]
        if classification is StreamClassification.UNKNOWABLE:
            if known is not None or type(share) is not int or share <= 0:
                raise ValueError("unknowable stream charge nullability differs")
        elif type(known) is not int or known <= 0 or share is not None:
            raise ValueError("known stream charge nullability differs")
        lease = leases.get(process_id) if leases is not None else None
        _validate_meter_evidence(stream["meter_evidence"], stream=stream, lease=lease, created_utc=created_utc)
        streams.append(stream)
    return streams


def validate_batch_claim(
    value: object,
    *,
    leases: Mapping[str, Mapping[str, object]] | None = None,
    state: TState | None = None,
    ledger_head_sha256: str | None = None,
    pre_ledger_entry_sha256: str | None = None,
) -> dict[str, object]:
    """Validate the frozen accounting witness (amendment §1a/§1b/§1c/§1f).

    ``leases`` is the durable active-lease map at the pre-head; when it is
    supplied every stream's inline meter evidence is cross-checked against
    the owning lease.  When it is omitted (durable re-validation of an
    already-installed claim whose leases may have since been removed by the
    automaton) only the claim's own internal consistency is checked.
    """

    claim = _exact(value, _BATCH_KEYS, "batch claim")
    if claim["schema"] != BATCH_CLAIM_SCHEMA or claim["scientific_outcome"] is not False:
        raise ValueError("batch claim schema differs")
    reason = BatchReason(str(claim["batch_reason"]))
    created = _utc(claim["created_utc"], "batch claim creation")
    for field in ("pre_ledger_entry_sha256", "pre_ledger_head_sha256", "pre_state_sha256"):
        _sha(claim[field], field)
    if ledger_head_sha256 is not None and claim["pre_ledger_head_sha256"] != ledger_head_sha256:
        raise ValueError("batch claim pre-head differs")
    if pre_ledger_entry_sha256 is not None and claim["pre_ledger_entry_sha256"] != pre_ledger_entry_sha256:
        raise ValueError("batch claim pre-entry differs")
    if state is not None:
        if claim["pre_state_sha256"] != hash_mapping(state.to_mapping()):
            raise ValueError("batch claim pre-state differs")
        if state.device_nanoseconds >= 168 * NANOSECONDS_PER_HOUR:
            raise ValueError("batch claim begins at or above E1")
    for field in (
        "remaining_ns",
        "known_total_ns",
        "unknown_stream_count",
        "unknown_pool_ns",
        "unknown_share_quotient_ns",
        "unknown_share_remainder_count",
    ):
        _integer(claim[field], field)
    if state is not None and claim["remaining_ns"] != 168 * NANOSECONDS_PER_HOUR - state.device_nanoseconds:
        raise ValueError("batch claim remaining E1 budget differs")
    cause = claim["dominant_cause"]
    if cause is not None:
        InvalidCause(str(cause))
    recovery = claim["recovery_disposition_sha256"]
    if reason is BatchReason.RECOVERY_SETTLEMENT:
        _sha(recovery, "recovery disposition")
    elif recovery is not None:
        raise ValueError("non-recovery claim carries a recovery disposition")
    raw_processes = claim["processes"]
    if not isinstance(raw_processes, list) or not raw_processes:
        raise ValueError("batch processes must be a nonempty list")
    process_by_id: dict[str, dict[str, object]] = {}
    prior_sequence = -1
    for raw in raw_processes:
        process = _exact(raw, _PROCESS_KEYS, "batch process")
        pid = _sha(process["process_id"], "batch process id")
        sequence = _integer(process["process_sequence"], "process sequence")
        if sequence <= prior_sequence or pid in process_by_id:
            raise ValueError("batch processes are not globally ordered")
        prior_sequence = sequence
        _sha(process["active_lease_sha256"], "active lease")
        known = _integer(process["known_charge_ns"], "process known charge")
        unknown = _integer(process["unknown_share_ns"], "process unknown share")
        if process["charge_ns"] != known + unknown or known + unknown <= 0:
            raise ValueError("batch process aggregate differs")
        disposition = ProcessDisposition(str(process["disposition"]))
        invalid = process["invalid_cause"]
        if disposition is ProcessDisposition.INVALID:
            if invalid != cause or cause is None:
                raise ValueError("invalid batch cause differs")
        elif invalid is not None:
            raise ValueError("valid batch process carries invalidity")
        process_by_id[pid] = process
    lease_map: dict[str, Mapping[str, object]] | None = None
    if leases is not None:
        lease_map = {pid: validate_active_lease(dict(lease)) for pid, lease in leases.items()}
        if set(lease_map) != set(process_by_id) and reason is not BatchReason.RECOVERY_SETTLEMENT:
            raise ValueError("batch does not enumerate every live lease")
        for pid, process in process_by_id.items():
            if pid in lease_map:
                if sha256_bytes(canonical_json(lease_map[pid])) != process["active_lease_sha256"]:
                    raise ValueError("batch lease hash differs")
                if int(lease_map[pid]["process_sequence"]) != process["process_sequence"]:
                    raise ValueError("batch process sequence differs")
    streams = _validate_streams(claim["streams"], process_by_id, lease_map, created)
    known_total = sum(int(stream["known_charge_ns"] or 0) for stream in streams)
    unknown = [stream for stream in streams if stream["classification"] == StreamClassification.UNKNOWABLE.value]
    pool, quotient, remainder, shares = allocate_unknown_pool_shares(
        int(claim["remaining_ns"]), known_total, len(unknown)
    )
    if (
        claim["known_total_ns"],
        claim["unknown_stream_count"],
        claim["unknown_pool_ns"],
        claim["unknown_share_quotient_ns"],
        claim["unknown_share_remainder_count"],
    ) != (known_total, len(unknown), pool, quotient, remainder):
        raise ValueError("batch unknown-pool witness differs")
    if tuple(int(item["unknown_share_ns"]) for item in unknown) != shares:
        raise ValueError("batch unknown shares differ")
    for pid, process in process_by_id.items():
        own = [stream for stream in streams if stream["process_id"] == pid]
        if not own or (int(process["known_charge_ns"]), int(process["unknown_share_ns"])) != (
            sum(int(stream["known_charge_ns"] or 0) for stream in own),
            sum(int(stream["unknown_share_ns"] or 0) for stream in own),
        ):
            raise ValueError("batch per-process stream aggregation differs")
    if sum(int(item["charge_ns"]) for item in process_by_id.values()) != known_total + pool:
        raise ValueError("batch charge conservation differs")
    if any(stream["classification"] == StreamClassification.UNKNOWABLE.value for stream in streams):
        if reason not in (BatchReason.RUNTIME_INVALIDITY, BatchReason.RECOVERY_SETTLEMENT):
            raise ValueError("an unknown stream requires an invalid batch route")
    expected_disposition = {
        BatchReason.E1_BOUNDARY: ProcessDisposition.E1_EXHAUSTED,
        BatchReason.E3_BOUNDARY: ProcessDisposition.E3_DUE,
        BatchReason.RUNTIME_INVALIDITY: ProcessDisposition.INVALID,
        BatchReason.RECOVERY_SETTLEMENT: ProcessDisposition.INVALID,
    }[reason]
    if any(
        ProcessDisposition(str(item["disposition"])) is not expected_disposition
        for item in process_by_id.values()
    ):
        raise ValueError("batch reason and process disposition differ")
    if (reason in (BatchReason.RUNTIME_INVALIDITY, BatchReason.RECOVERY_SETTLEMENT)) != (cause is not None):
        raise ValueError("batch reason and dominant cause differ")
    omitted = claim["omitted"]
    if not isinstance(omitted, list) or (omitted and reason is not BatchReason.RECOVERY_SETTLEMENT):
        raise ValueError("batch omissions differ")
    for item in omitted:
        omission = _exact(item, _OMITTED_KEYS, "batch omission")
        _sha(omission["process_id"], "omitted process")
        if omission["omission_reason"] not in {"TERMINAL_RECORD_DURABLE", "ANCESTOR_CLAIM_ENUMERATED"}:
            raise ValueError("omission reason differs")
        ancestor = omission["ancestor_claim_sha256"]
        if (omission["omission_reason"] == "TERMINAL_RECORD_DURABLE") != (ancestor is None):
            raise ValueError("omission ancestor nullability differs")
        if ancestor is not None:
            _sha(ancestor, "omission ancestor")
    return claim


def build_batch_claim(**values: object) -> dict[str, object]:
    """Construct only a fully specified frozen witness; no value is inferred."""

    claim = dict(values)
    validate_batch_claim(claim)
    return claim


# --------------------------------------------------------------------------
# Closed non-outcome decision schemas (v2.1 §E)
# --------------------------------------------------------------------------


def _validate_decision(value: object, schema: str, keys: set[str]) -> dict[str, object]:
    result = _exact(value, keys, "decision")
    if result["schema"] != schema or result["scientific_outcome"] is not False:
        raise ValueError("decision schema differs")
    return result


def validate_e3_decision(value: object) -> dict[str, object]:
    result = _validate_decision(
        value,
        "philosophia.officina.e3-decision.v1",
        {
            "schema",
            "scientific_outcome",
            "activation_record_sha256",
            "state_sha256",
            "observed_utc",
            "last_review_utc",
            "device_ns_at_review",
            "device_ns_now",
            "calendar_due",
            "device_due",
        },
    )
    for name in ("activation_record_sha256", "state_sha256"):
        _sha(result[name], name)
    for name in ("observed_utc", "last_review_utc"):
        _utc(result[name], name)
    for name in ("device_ns_at_review", "device_ns_now"):
        _integer(result[name], name)
    if (
        result["device_ns_now"] < result["device_ns_at_review"]
        or type(result["calendar_due"]) is not bool
        or type(result["device_due"]) is not bool
    ):
        raise ValueError("E3 decision values differ")
    return result


def validate_resource_stop_decision(value: object) -> dict[str, object]:
    result = _validate_decision(
        value,
        "philosophia.officina.resource-stop-decision.v1",
        {
            "schema",
            "scientific_outcome",
            "process_id",
            "lease_sha256",
            "state_sha256",
            "observed_utc",
            "monotonic_reading_ns",
            "reason",
        },
    )
    for name in ("process_id", "lease_sha256", "state_sha256"):
        _sha(result[name], name)
    _utc(result["observed_utc"])
    _integer(result["monotonic_reading_ns"], "monotonic reading")
    if result["reason"] not in {"E1_BUDGET", "E3_BUDGET", "HOST_RESOURCE"}:
        raise ValueError("resource-stop reason differs")
    return result


def validate_pause_decision(value: object) -> dict[str, object]:
    result = _validate_decision(
        value,
        "philosophia.officina.pause-decision.v1",
        {
            "schema",
            "scientific_outcome",
            "activation_record_sha256",
            "state_sha256",
            "ledger_head_sha256",
            "observed_utc",
            "live_lease_count",
            "checkpoint_sha256",
        },
    )
    for name in ("activation_record_sha256", "state_sha256", "ledger_head_sha256", "checkpoint_sha256"):
        _sha(result[name], name)
    _utc(result["observed_utc"])
    if result["live_lease_count"] != 0:
        raise ValueError("pause decision requires no live lease")
    return result


def validate_recovery_disposition(value: object) -> dict[str, object]:
    result = _validate_decision(
        value,
        RECOVERY_DISPOSITION_SCHEMA,
        {
            "schema",
            "scientific_outcome",
            "author_decision_sha256",
            "invalidity_record_sha256",
            "invalidity_event_sha256",
            "ledger_head_sha256",
            "state_sha256",
            "affected_process_ids",
            "charge_event_sha256s",
            "resolution_action",
            "resolved_utc",
        },
    )
    for name in (
        "author_decision_sha256",
        "invalidity_record_sha256",
        "invalidity_event_sha256",
        "ledger_head_sha256",
        "state_sha256",
    ):
        _sha(result[name], name)
    for name in ("affected_process_ids", "charge_event_sha256s"):
        items = result[name]
        if not isinstance(items, list) or items != sorted(items) or len(items) != len(set(items)):
            raise ValueError(f"{name} must be a sorted unique array")
        for item in items:
            _sha(item, name)
    if result["resolution_action"] not in {"READMIT_AFTER_RECONCILIATION", "REMAIN_BLOCKED"}:
        raise ValueError("recovery action differs")
    _utc(result["resolved_utc"])
    return result


def validate_author_stop_decision(value: object) -> dict[str, object]:
    result = _validate_decision(
        value,
        "philosophia.officina.author-stop-decision.v1",
        {
            "schema",
            "scientific_outcome",
            "review_record_sha256",
            "ledger_head_sha256",
            "state_sha256",
            "signed_utc",
            "author_decision_sha256",
        },
    )
    for name in ("review_record_sha256", "ledger_head_sha256", "state_sha256", "author_decision_sha256"):
        _sha(result[name], name)
    _utc(result["signed_utc"])
    return result


# --------------------------------------------------------------------------
# Draft manifest (v2 §8)
# --------------------------------------------------------------------------

_DRAFT_MANIFEST_KEYS = {
    "schema",
    "scientific_outcome",
    "t_quarantine",
    "q_eligible",
    "behavior_source_sha256",
    "config_sha256",
    "stack_sha256",
    "numerical_mode_sha256",
    "device_identity",
}


def validate_draft_manifest(value: object) -> dict[str, object]:
    """A draft manifest may name only its own non-scientific, unregistered provenance."""

    manifest = _exact(value, _DRAFT_MANIFEST_KEYS, "draft manifest")
    if manifest["schema"] != DRAFT_MANIFEST_SCHEMA or manifest["scientific_outcome"] is not False:
        raise ValueError("draft manifest schema differs")
    if manifest["t_quarantine"] != "dev-non-citable":
        raise ValueError("draft manifest quarantine label differs")
    if manifest["q_eligible"] is not False:
        raise ValueError("draft manifest eligibility differs")
    for field in ("behavior_source_sha256", "config_sha256", "stack_sha256", "numerical_mode_sha256"):
        _sha(manifest[field], field)
    if not isinstance(manifest["device_identity"], str) or not manifest["device_identity"]:
        raise ValueError("draft manifest device identity is malformed")
    return manifest


# --------------------------------------------------------------------------
# Pending resume checkpoint (v2.2 §C generational path)
# --------------------------------------------------------------------------

_PENDING_RESUME_KEYS = {
    "schema",
    "scientific_outcome",
    "original_checkpoint_sha256",
    "payload_sha256",
    "ledger_head_before",
    "created_utc",
}


def validate_pending_resume_checkpoint(value: object) -> dict[str, object]:
    record = _exact(value, _PENDING_RESUME_KEYS, "pending resume checkpoint")
    if record["schema"] != PENDING_RESUME_SCHEMA or record["scientific_outcome"] is not False:
        raise ValueError("pending resume checkpoint schema differs")
    for field in ("original_checkpoint_sha256", "payload_sha256", "ledger_head_before"):
        _sha(record[field], field)
    _utc(record["created_utc"], "pending resume checkpoint creation")
    return record


# --------------------------------------------------------------------------
# Batch settlement override artifact (amendment §5b)
# --------------------------------------------------------------------------

_OVERRIDE_KEYS = {
    "schema",
    "scientific_outcome",
    "batch_claim_sha256",
    "validated_prefix_count",
    "pre_override_ledger_head_sha256",
    "pre_override_state_sha256",
    "dominant_cause",
    "remaining_process_ids",
    "replacement_dispositions",
    "created_utc",
}
_REPLACEMENT_KEYS = {"process_id", "disposition", "invalid_cause"}


def validate_batch_override(value: object) -> dict[str, object]:
    override = _exact(value, _OVERRIDE_KEYS, "batch settlement override")
    if override["schema"] != BATCH_OVERRIDE_SCHEMA or override["scientific_outcome"] is not False:
        raise ValueError("batch override schema differs")
    _sha(override["batch_claim_sha256"], "batch claim")
    _integer(override["validated_prefix_count"], "validated prefix count")
    _sha(override["pre_override_ledger_head_sha256"], "pre-override ledger head")
    _sha(override["pre_override_state_sha256"], "pre-override state")
    cause = InvalidCause(str(override["dominant_cause"]))
    ids = override["remaining_process_ids"]
    if not isinstance(ids, list) or not ids or ids != sorted(ids) or len(ids) != len(set(ids)):
        raise ValueError("remaining process ids must be a sorted, unique, nonempty array")
    for item in ids:
        _sha(item, "remaining process id")
    replacements = override["replacement_dispositions"]
    if not isinstance(replacements, list) or [item.get("process_id") for item in replacements] != ids:
        raise ValueError("replacement dispositions must cover exactly the remaining process ids, in order")
    for item in replacements:
        entry = _exact(item, _REPLACEMENT_KEYS, "replacement disposition")
        _sha(entry["process_id"], "replacement process id")
        if entry["disposition"] != ProcessDisposition.INVALID.value or entry["invalid_cause"] != cause.value:
            raise ValueError("replacement disposition must be invalid with the dominant cause")
    _utc(override["created_utc"], "override creation")
    return override


# --------------------------------------------------------------------------
# Review record (activation protocol; used by complete_overdue_review)
# --------------------------------------------------------------------------

_REVIEW_RECORD_KEYS = {
    "schema",
    "scientific_outcome",
    "validity",
    "authorization_sha256",
    "activation_record_sha256",
    "pre_state_sha256",
    "post_state",
    "post_state_sha256",
    "ledger_entry_sha256",
    "ledger_head_sha256",
    "reviewed_utc",
    "prior_review_utc",
    "prior_review_device_nanoseconds",
    "author_decision_sha256",
}


def validate_review_record(value: object) -> dict[str, object]:
    record = _exact(value, _REVIEW_RECORD_KEYS, "review record")
    if record["schema"] != REVIEW_RECORD_SCHEMA or record["scientific_outcome"] is not False:
        raise ValueError("review record schema differs")
    for field in (
        "authorization_sha256",
        "activation_record_sha256",
        "pre_state_sha256",
        "post_state_sha256",
        "ledger_entry_sha256",
        "ledger_head_sha256",
        "author_decision_sha256",
    ):
        _sha(record[field], field)
    for field in ("reviewed_utc", "prior_review_utc"):
        _utc(record[field], field)
    _integer(record["prior_review_device_nanoseconds"], "prior review device nanoseconds")
    if record["validity"] not in {"VALID_PROCESS_RECORD", "INVALID_PROCESS_RECORD"}:
        raise ValueError("review record validity differs")
    if not isinstance(record["post_state"], dict):
        raise ValueError("review record post-state is malformed")
    TState.from_mapping(record["post_state"])
    return record


# --------------------------------------------------------------------------
# The harness
# --------------------------------------------------------------------------


class GenericHarness:
    """The sole issuer/revoker of exact real-T capabilities (v2 §1)."""

    def __init__(
        self,
        repo: Path,
        *,
        clock: object | None = None,
        meter: object | None = None,
        processes: object | None = None,
        crash_cut: str | None = None,
    ) -> None:
        self.repo = Path(repo).resolve(strict=True)
        self.clock = clock if clock is not None else SystemClock()
        self.meter = meter if meter is not None else CpuMonotonicMeter()
        self.processes = processes if processes is not None else SubprocessProcessOps()
        self.crash_cut = crash_cut

    # -- small primitives ---------------------------------------------

    def _cut(self, point: str) -> None:
        if self.crash_cut == point:
            raise RuntimeError(f"injected crash cut: {point}")

    def _path(self, relative: Path) -> Path:
        return self.repo / relative

    def _now(self) -> str:
        return _utc(self.clock.utc_now())  # type: ignore[union-attr]

    def _reading(self, lease: Mapping[str, object] | None = None) -> int:
        return _integer(self.meter.read(lease), "meter reading")  # type: ignore[union-attr]

    def _ledger(self) -> AppendOnlyLedger:
        return AppendOnlyLedger(self._path(LEDGER_RELATIVE), head_path=self._path(LEDGER_HEAD_RELATIVE))

    def _state(self) -> TState:
        value = load_canonical_json(self._path(STATE_RELATIVE))
        if not isinstance(value, dict):
            raise HarnessRefused("T state is not an object")
        return TState.from_mapping(value)

    def _write_state(self, state: TState) -> None:
        atomic_replace(self._path(STATE_RELATIVE), canonical_json(state.to_mapping()), mode=0o644)

    def _head(self, entries: list[dict[str, object]] | None = None) -> str:
        entries = self._ledger().entries() if entries is None else entries
        return str(entries[-1]["entry_sha256"]) if entries else GENESIS

    def _envelope(self) -> TEnvelope:
        value = load_canonical_json(self._path(ENVELOPE_RELATIVE))
        if not isinstance(value, dict) or value.get("activated") is not True:
            raise HarnessRefused("active signed envelope is unavailable")
        return TEnvelope()

    def _activation(self) -> tuple[str, dict[str, str]]:
        path = self._path(ACTIVATION_RECORD_RELATIVE)
        record = load_canonical_json(path)
        if not isinstance(record, dict):
            raise HarnessRefused("activation record is malformed")
        immutable = require_sha256_map(record.get("immutable_control_sha256"), name="immutable control")
        return sha256_file(path), immutable

    def _leases(self) -> dict[str, dict[str, object]]:
        directory = self._path(LEASES_RELATIVE)
        result: dict[str, dict[str, object]] = {}
        if not directory.exists():
            return result
        for path in sorted(directory.glob("*.json")):
            value = validate_active_lease(load_canonical_json(path))
            if path.stem != value["process_id"] or value["process_id"] in result:
                raise HarnessRefused("active lease filename identity differs")
            result[str(value["process_id"])] = value
        return result

    def _reservations(self, leases: Mapping[str, Mapping[str, object]]) -> tuple[Reservation, ...]:
        return tuple(
            Reservation(
                int(item["device_units"]),
                int(item["outstanding_liability_ns"]) // int(item["device_units"]),
            )
            for item in leases.values()
        )

    # -- global/process view --------------------------------------------

    def global_state(self) -> RuntimeView:
        state = self._state()
        envelope = self._envelope()
        leases = self._leases()
        entries = self._ledger().entries()
        last_event = str(entries[-1]["event"]) if entries else None
        if not self._g5_admission_clear():
            phase = GlobalState.G5
        else:
            phase = derive_global_state(
                state=state,
                envelope=envelope,
                now_utc=self._now(),
                last_event=last_event,
                live_process_count=len(leases),
            )
        return RuntimeView(state, self._head(entries), tuple(sorted(leases)), phase)

    def process_state(self, process_id: str) -> ProcessState:
        claimed = self._path(CLAIMS_RELATIVE / f"{process_id}.json").is_file()
        leased = self._path(LEASES_RELATIVE / f"{process_id}.json").is_file()
        record_path = self._path(RECORDS_RELATIVE / f"{process_id}.json")
        record = load_canonical_json(record_path) if record_path.is_file() else None
        started = leased or record is not None
        if not started and claimed:
            entries = self._ledger().entries()
            started = any(
                entry["event"] == "T_PROCESS_STARTED" and entry["data"].get("process_id") == process_id
                for entry in entries
            )
        return derive_process_state(
            claimed=claimed,
            started=started,
            leased=leased,
            record=record if isinstance(record, dict) else None,
        )

    # -- batch-claim registry --------------------------------------------

    def _unresolved_batch_claims(self) -> list[tuple[Path, dict[str, object]]]:
        root = self._path(BATCH_CLAIMS_RELATIVE)
        if not root.is_dir():
            return []
        entries = self._ledger().entries()
        chain = {GENESIS} | {str(entry["entry_sha256"]) for entry in entries}
        result: list[tuple[Path, dict[str, object]]] = []
        for path in sorted(root.glob("*.json")):
            claim = validate_batch_claim(load_canonical_json(path))
            if str(claim["pre_ledger_entry_sha256"]) not in chain:
                continue
            action, _ = self.next_batch_action(claim)
            if action is not BatchAutomatonAction.RESOLVED:
                result.append((path, claim))
        return result

    def _refuse_if_unresolved_batch(self) -> None:
        if self._unresolved_batch_claims():
            raise HarnessRefused("an unresolved batch settlement claim blocks this operation")

    def _refuse_if_g5_unresolved(self) -> None:
        """v2 §2a / v2.1 §C.3: G5 refuses every admission until disposition clears."""
        if not self._g5_admission_clear():
            raise HarnessRefused(
                "G5 runtime invalidity blocks admission until a verified recovery disposition"
            )

    # -- ordinary lifecycle (v2 §2c.1/.2/.3/.5/.6) -----------------------

    def claim(self, **kwargs: object) -> dict[str, object]:
        """Create a durable process claim, without starting a process."""

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            self._refuse_if_g5_unresolved()
            state, envelope, leases = self._state(), self._envelope(), self._leases()
            route = reservation_route(state=state, envelope=envelope, live_reservations=self._reservations(leases))
            if route is not ReservationRoute.RESERVE:
                raise HarnessRefused(f"claim route is {route.value}")
            activation_hash, immutable = self._activation()
            sequence = max((int(item["process_sequence"]) for item in leases.values()), default=-1) + 1
            start_reading = self._reading()
            self._cut("before_3")
            record = build_process_claim(
                activation_record_sha256=activation_hash,
                process_sequence=sequence,
                controller_pid=os.getpid(),
                controller_start_identity=str(os.getpid()),
                process_group_id=os.getpgrp(),
                argv=typing_cast_sequence(kwargs["argv"]),
                behavior_source_sha256=str(kwargs["behavior_source_sha256"]),
                config_sha256=str(kwargs["config_sha256"]),
                stack_sha256=str(kwargs["stack_sha256"]),
                numerical_mode_sha256=str(kwargs["numerical_mode_sha256"]),
                device_identity=str(kwargs.get("device_identity", CPU_ADAPTER_IDENTITY)),
                device_units=int(kwargs.get("device_units", 1)),
                created_utc=self._now(),
                boot_id=boot_identity(),
                start_reading_ns=start_reading,
                immutable_control_sha256=immutable,
            )
            path = self._path(CLAIMS_RELATIVE / f"{record['process_id']}.json")
            atomic_create(path, canonical_json(record))
            self._cut("after_3")
            return record

    def start(self, process_id: str) -> RealTCapability:
        """§2c.3, corrected order: ``T_PROCESS_STARTED`` first, then the lease
        seeded with ``prior_charge_event_sha256`` equal to that entry's hash."""

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            self._refuse_if_g5_unresolved()
            state, envelope = self._state(), self._envelope()
            claim_path = self._path(CLAIMS_RELATIVE / f"{process_id}.json")
            claim = validate_process_claim(load_canonical_json(claim_path))
            activation_hash, immutable = self._activation()
            validate_process_claim_against_activation(
                claim, activation_record_sha256=activation_hash, immutable_control_sha256=immutable
            )
            lease_path = self._path(LEASES_RELATIVE / f"{process_id}.json")
            if lease_path.exists():
                raise HarnessRefused("process already has an installed lease")
            leases = self._leases()
            reservation = reservation_for(
                state=state,
                envelope=envelope,
                live_reservations=self._reservations(leases),
                requested_units=int(claim["device_units"]),
            )
            if reservation is None:
                raise HarnessRefused("no signed reservation remains")
            self._cut("before_4")
            start_event = self._ledger().append(
                event="T_PROCESS_STARTED",
                timestamp_utc=self._now(),
                data={
                    "process_claim_sha256": sha256_file(claim_path),
                    "process_id": process_id,
                    "scientific_outcome": False,
                },
            )
            validate_ledger_event(start_event)
            self._cut("after_4")
            lease = build_active_lease(
                claim,
                reservation=reservation,
                prior_charge_event_sha256=str(start_event["entry_sha256"]),
                activation_record_sha256=activation_hash,
                immutable_control_sha256=immutable,
            )
            atomic_create(lease_path, canonical_json(lease))
            self._cut("after_6")
            return _issue_capability(_ISSUANCE_TOKEN)

    def heartbeat(self, process_id: str) -> dict[str, object]:
        """§2c.5: settle the monotonic cursor delta only; never used for a batch."""

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            self._refuse_if_g5_unresolved()
            lease_path = self._path(LEASES_RELATIVE / f"{process_id}.json")
            claim_path = self._path(CLAIMS_RELATIVE / f"{process_id}.json")
            lease, _claim = validate_active_lease_against_claim(
                load_canonical_json(lease_path), load_canonical_json(claim_path)
            )
            current = self._reading(lease)
            state, envelope = self._state(), self._envelope()
            leases = self._leases()
            siblings = self._reservations({pid: item for pid, item in leases.items() if pid != process_id})
            provisional_charge = (current - int(lease["last_charged_reading_ns"])) * int(lease["device_units"])
            if provisional_charge <= 0:
                raise HarnessRefused("heartbeat clock did not advance")
            self._cut("before_4")
            next_state = state.charge_device_nanoseconds(provisional_charge, envelope)
            charge_event = self._ledger().append(
                event="T_DEVICE_TIME_CHARGED",
                timestamp_utc=self._now(),
                data={
                    "active_lease_sha256": sha256_bytes(canonical_json(lease)),
                    "charge_ns": provisional_charge,
                    "process_id": process_id,
                    "scientific_outcome": False,
                    "t_state": next_state.to_mapping(),
                },
            )
            validate_ledger_event(charge_event)
            self._cut("after_4")
            reservation = reservation_for(
                state=next_state, envelope=envelope, live_reservations=siblings, requested_units=int(lease["device_units"])
            )
            if reservation is None:
                reservation = Reservation(int(lease["device_units"]), HEARTBEAT_LIABILITY_SECONDS * NANOSECONDS_PER_SECOND)
            settled_state, renewed = settle_active_lease(
                lease=lease,
                state=state,
                envelope=envelope,
                current_reading_ns=current,
                next_reservation=reservation,
                charge_event_sha256=str(charge_event["entry_sha256"]),
            )
            if settled_state != next_state:
                raise HarnessRefused("ordinary settlement re-derivation differs")
            self._write_state(next_state)
            atomic_replace(lease_path, canonical_json(renewed), mode=0o644)
            self._cut("after_6")
            return renewed

    def close(self, process_id: str) -> dict[str, object]:
        """§2c.6, valid ordinary close: final settle -> record -> stopped -> lease removal.

        The final settlement's ``T_DEVICE_TIME_CHARGED`` event witnesses the
        lease exactly as it stood *before* that last heartbeat's settlement
        (the same "authorizing lease" convention the frozen-batch witness
        uses, since a batch charge never rewrites its lease file mid-flight
        either).  ``build_process_record`` therefore requires the *pre*-final
        -heartbeat lease, not the renewed one the heartbeat call durably
        replaces it with; the pre-heartbeat lease and claim are captured
        below before that call so the final-settlement cross-check matches.
        """

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            lease_path = self._path(LEASES_RELATIVE / f"{process_id}.json")
            claim_path = self._path(CLAIMS_RELATIVE / f"{process_id}.json")
            lease, claim = validate_active_lease_against_claim(
                load_canonical_json(lease_path), load_canonical_json(claim_path)
            )
        renewed = self.heartbeat(process_id)
        del renewed
        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            entries, state = self._ledger().entries(), self._state()
            activation_hash, immutable = self._activation()
            self._cut("before_3")
            record = build_process_record(
                claim=claim,
                lease=lease,
                disposition=ProcessDisposition.CLOSED,
                invalid_cause=None,
                closed_utc=str(entries[-1]["timestamp_utc"]),
                final_charge_event=entries[-1],
                final_state=state,
                activation_record_sha256=activation_hash,
                immutable_control_sha256=immutable,
            )
            record_path = self._path(RECORDS_RELATIVE / f"{process_id}.json")
            atomic_create(record_path, canonical_json(record))
            self._cut("after_3")
            stop = self._ledger().append(
                event="T_PROCESS_STOPPED",
                timestamp_utc=str(record["closed_utc"]),
                data={
                    "process_id": process_id,
                    "process_record_sha256": sha256_file(record_path),
                    "scientific_outcome": False,
                    "t_state": state.to_mapping(),
                },
            )
            validate_ledger_event(stop)
            self._cut("after_4")
            os.unlink(lease_path)
            fsync_directory(lease_path.parent)
            self._cut("after_6")
            return record

    # -- pause / resume / overdue review (v2 §6a/§6b; v2.2 §C) ----------

    def pause(self, *, reason: str, artifact_paths: Mapping[str, Path]) -> dict[str, object]:
        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            self._refuse_if_g5_unresolved()
            if self._leases():
                raise HarnessRefused("pause requires no live leases")
            state, entries = self._state(), self._ledger().entries()
            checkpoint_path = self._path(PAUSE_CHECKPOINTS_RELATIVE / f"{self._head(entries)}.json")
            self._cut("before_3")
            event = record_operational_pause(
                ledger=self._ledger(),
                checkpoint_path=checkpoint_path,
                state=state,
                artifact_paths=artifact_paths,
                timestamp_utc=self._now(),
                reason=reason,
            )
            validate_ledger_event(event)
            self._cut("after_4")
            return event

    def resume(self, checkpoint_path: Path) -> RuntimeView:
        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            envelope = self._envelope()
            gate = verify_resume(
                ledger=self._ledger(), checkpoint_path=checkpoint_path, envelope=envelope, timestamp_utc=self._now()
            )
            if not gate.review_required:
                return self.global_state()
            entries = self._ledger().entries()
            pause_event_sha256 = str(entries[-1]["entry_sha256"])
            payload = load_canonical_json(checkpoint_path)
            if not isinstance(payload, dict):
                raise HarnessRefused("pause checkpoint is malformed")
            pending_path = self._path(PENDING_RESUME_RELATIVE / f"{pause_event_sha256}.json")
            pending_record = {
                "schema": PENDING_RESUME_SCHEMA,
                "scientific_outcome": False,
                "original_checkpoint_sha256": sha256_file(checkpoint_path),
                "payload_sha256": sha256_bytes(canonical_json(payload["artifacts"])),
                "ledger_head_before": pause_event_sha256,
                "created_utc": self._now(),
            }
            validate_pending_resume_checkpoint(pending_record)
            self._cut("before_3")
            if not pending_path.is_file():
                atomic_create(pending_path, canonical_json(pending_record))
            self._cut("after_3")
            pending_state = dataclasses.replace(gate.state, resume_review_pending=True)
            event = self._ledger().append(
                event="T_OPERATIONAL_PAUSE",
                timestamp_utc=self._now(),
                data={
                    "checkpoint_path": str(pending_path.resolve()),
                    "checkpoint_sha256": sha256_file(pending_path),
                    "reason": "RESUME_E3_REVIEW_PENDING",
                    "resets_e3": False,
                    "scientific_outcome": False,
                    "t_state": pending_state.to_mapping(),
                },
            )
            validate_ledger_event(event)
            self._cut("after_4")
            self._write_state(pending_state)
            self._cut("after_6")
            return self.global_state()

    def complete_overdue_review(self, *, review: Mapping[str, object]) -> TState:
        """Complete a durable overdue-resume review; uses the signed review schema
        directly (imported from ``.runtime``), never a facade attribute."""

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            state, entries = self._state(), self._ledger().entries()
            envelope = self._envelope()
            if not state.resume_review_pending or not state.review_due(envelope, self._now()):
                raise HarnessRefused("no overdue resume review is pending")
            record = dict(validate_review_record(dict(review)))
            reviewed = dataclasses.replace(
                state,
                last_review_utc=self._now(),
                device_nanoseconds_at_review=state.device_nanoseconds,
                resume_review_pending=False,
            )
            head = self._head(entries)
            record["pre_state_sha256"] = hash_mapping(state.to_mapping())
            record["post_state"] = reviewed.to_mapping()
            record["post_state_sha256"] = hash_mapping(reviewed.to_mapping())
            record["ledger_entry_sha256"] = head
            record["ledger_head_sha256"] = head
            record["reviewed_utc"] = self._now()
            record["prior_review_utc"] = state.last_review_utc or str(state.activated_utc)
            record["prior_review_device_nanoseconds"] = state.device_nanoseconds_at_review
            validate_review_record(record)
            path = self._path(REVIEW_RECORDS_RELATIVE / f"{head}.json")
            self._cut("before_3")
            atomic_create(path, canonical_json(record))
            self._cut("after_3")
            event = self._ledger().append(
                event="T_REVIEW_COMPLETED",
                timestamp_utc=str(record["reviewed_utc"]),
                data={
                    "review_record_sha256": sha256_file(path),
                    "scientific_outcome": False,
                    "t_state": reviewed.to_mapping(),
                },
            )
            validate_ledger_event(event)
            self._cut("after_4")
            self._write_state(reviewed)
            self._cut("after_6")
            return reviewed

    # -- recovery disposition and G5 admission (v2.1 §C.3) ---------------

    def _g5_admission_clear(self) -> bool:
        entries = self._ledger().entries()
        invalid_events = [entry for entry in entries if entry["event"] == "T_RUNTIME_INVALID"]
        if not invalid_events:
            return True
        head = self._head(entries)
        state_hash = hash_mapping(self._state().to_mapping())
        for event in invalid_events:
            path = self._path(RECOVERY_RELATIVE / f"{event['entry_sha256']}.json")
            if not path.is_file():
                return False
            disposition = validate_recovery_disposition(load_canonical_json(path))
            if (
                disposition["resolution_action"] != "READMIT_AFTER_RECONCILIATION"
                or disposition["ledger_head_sha256"] != head
                or disposition["state_sha256"] != state_hash
            ):
                return False
        return True

    def install_recovery_disposition(
        self,
        *,
        author_decision_sha256: str,
        invalidity_event_sha256: str,
        resolution_action: str,
        affected_process_ids: Sequence[str] | None = None,
        charge_event_sha256s: Sequence[str] | None = None,
    ) -> dict[str, object]:
        with RuntimeLock(self.repo):
            entries = self._ledger().entries()
            target = next((entry for entry in entries if entry["entry_sha256"] == invalidity_event_sha256), None)
            if target is None or target["event"] != "T_RUNTIME_INVALID":
                raise HarnessRefused("named invalidity event is not durable")
            invalidity_record_sha256 = str(target["data"]["invalidity_record_sha256"])
            state = self._state()
            head = self._head(entries)
            if affected_process_ids is None or charge_event_sha256s is None:
                position = entries.index(target)
                preceding = entries[position - 1] if position > 0 else None
                if preceding is None or preceding["event"] != "T_DEVICE_TIME_CHARGED":
                    raise HarnessRefused("recovery disposition requires explicit affected process ids")
                affected_process_ids = [str(preceding["data"]["process_id"])]
                charge_event_sha256s = [str(preceding["entry_sha256"])]
            disposition = {
                "schema": RECOVERY_DISPOSITION_SCHEMA,
                "scientific_outcome": False,
                "author_decision_sha256": author_decision_sha256,
                "invalidity_record_sha256": invalidity_record_sha256,
                "invalidity_event_sha256": invalidity_event_sha256,
                "ledger_head_sha256": head,
                "state_sha256": hash_mapping(state.to_mapping()),
                "affected_process_ids": sorted(affected_process_ids),
                "charge_event_sha256s": sorted(charge_event_sha256s),
                "resolution_action": resolution_action,
                "resolved_utc": self._now(),
            }
            validate_recovery_disposition(disposition)
            path = self._path(RECOVERY_RELATIVE / f"{invalidity_event_sha256}.json")
            self._cut("before_recovery")
            atomic_create(path, canonical_json(disposition))
            self._cut("after_recovery")
            return disposition

    # -- batch settlement construction (amendment §1) --------------------

    def construct_and_install_batch_claim(
        self,
        *,
        reason: BatchReason,
        unknowable_process_ids: Iterable[str] = (),
        observed_causes: Iterable[InvalidCause] = (),
        recovery_disposition_sha256: str | None = None,
        recovery_process_ids: Iterable[str] | None = None,
        omitted: Sequence[Mapping[str, object]] = (),
    ) -> dict[str, object]:
        """Freeze the live-lease set into one durable batch claim (§1a/§1b/§1c)."""

        with RuntimeLock(self.repo):
            self._refuse_if_unresolved_batch()
            state = self._state()
            entries = self._ledger().entries()
            pre_head = self._head(entries)
            pre_entry = str(entries[-1]["entry_sha256"]) if entries else GENESIS
            leases = self._leases()
            unknowable = set(unknowable_process_ids)
            if reason in (BatchReason.E1_BOUNDARY, BatchReason.E3_BOUNDARY):
                if unknowable:
                    raise HarnessRefused("a fault-free boundary batch cannot contain unknowable streams")
                selected = dict(leases)
            elif reason is BatchReason.RUNTIME_INVALIDITY:
                selected = dict(leases)
            else:  # RECOVERY_SETTLEMENT
                if recovery_process_ids is None:
                    raise HarnessRefused("recovery settlement requires its enumerated process ids")
                recovery_ids = set(recovery_process_ids)
                selected = {pid: leases[pid] for pid in recovery_ids if pid in leases}
                omitted_ids = {str(item["process_id"]) for item in omitted}
                if (set(selected) | omitted_ids) != set(leases) or (set(selected) & omitted_ids):
                    raise HarnessRefused("recovery settlement does not exactly partition the live lease set")
            if not selected:
                raise HarnessRefused("batch settlement requires at least one live process")
            ordered = sorted(selected.items(), key=lambda item: int(item[1]["process_sequence"]))
            created_utc = self._now()
            streams: list[dict[str, object]] = []
            known_totals: dict[str, int] = {}
            try:
                adapter_identity = self.meter.adapter_identity  # type: ignore[union-attr]
            except AttributeError:
                adapter_identity = CPU_ADAPTER_IDENTITY
            for stream_index, (process_id, lease) in enumerate(ordered, start=1):
                if process_id in unknowable:
                    evidence = {
                        "clock_kind": CLOCK_KIND,
                        "boot_identity": lease["boot_identity"],
                        "adapter_identity": adapter_identity,
                        "interval_start_reading_ns": int(lease["last_charged_reading_ns"]),
                        "interval_end_reading_ns": None,
                        "backend_synchronized": False,
                        "observed_utc": created_utc,
                    }
                    streams.append(
                        {
                            "stream_index": stream_index,
                            "process_id": process_id,
                            "classification": StreamClassification.UNKNOWABLE.value,
                            "known_charge_ns": None,
                            "unknown_share_ns": None,
                            "meter_evidence": evidence,
                        }
                    )
                else:
                    start = int(lease["last_charged_reading_ns"])
                    current = self._reading(lease)
                    if current <= start:
                        raise HarnessRefused("batch meter cursor did not advance for a known stream")
                    known_charge_ns = current - start
                    classification = classify_stream(
                        interval_start_reading_ns=start,
                        interval_end_reading_ns=current,
                        backend_synchronized=True,
                        heartbeat_deadline_ns=int(lease["heartbeat_deadline_ns"]),
                    )
                    known_totals[process_id] = known_charge_ns
                    evidence = {
                        "clock_kind": CLOCK_KIND,
                        "boot_identity": lease["boot_identity"],
                        "adapter_identity": adapter_identity,
                        "interval_start_reading_ns": start,
                        "interval_end_reading_ns": current,
                        "backend_synchronized": True,
                        "observed_utc": created_utc,
                    }
                    streams.append(
                        {
                            "stream_index": stream_index,
                            "process_id": process_id,
                            "classification": classification.value,
                            "known_charge_ns": known_charge_ns,
                            "unknown_share_ns": None,
                            "meter_evidence": evidence,
                        }
                    )
            known_total_ns = sum(known_totals.values())
            unknown_process_ids = [pid for pid in unknowable if pid in selected]
            remaining_ns = 168 * NANOSECONDS_PER_HOUR - state.device_nanoseconds
            pool, quotient, remainder, shares = allocate_unknown_pool_shares(
                remaining_ns, known_total_ns, len(unknown_process_ids)
            )
            unknown_stream_indexes = [s["stream_index"] for s in streams if s["classification"] == StreamClassification.UNKNOWABLE.value]
            share_by_index = dict(zip(unknown_stream_indexes, shares, strict=True))
            for stream in streams:
                if stream["classification"] == StreamClassification.UNKNOWABLE.value:
                    stream["unknown_share_ns"] = share_by_index[stream["stream_index"]]
            dominant_cause: InvalidCause | None = None
            if reason in (BatchReason.RUNTIME_INVALIDITY, BatchReason.RECOVERY_SETTLEMENT):
                causes = list(observed_causes)
                if not causes and unknown_process_ids:
                    causes = [InvalidCause.PROCESS]
                if not causes:
                    raise HarnessRefused("an invalid batch requires at least one observed cause")
                dominant_cause = dominant_invalid_cause(causes)
            expected_disposition = {
                BatchReason.E1_BOUNDARY: ProcessDisposition.E1_EXHAUSTED,
                BatchReason.E3_BOUNDARY: ProcessDisposition.E3_DUE,
                BatchReason.RUNTIME_INVALIDITY: ProcessDisposition.INVALID,
                BatchReason.RECOVERY_SETTLEMENT: ProcessDisposition.INVALID,
            }[reason]
            processes: list[dict[str, object]] = []
            for process_id, lease in ordered:
                own = [s for s in streams if s["process_id"] == process_id]
                known = sum(int(s["known_charge_ns"] or 0) for s in own)
                unknown = sum(int(s["unknown_share_ns"] or 0) for s in own)
                processes.append(
                    {
                        "process_id": process_id,
                        "process_sequence": int(lease["process_sequence"]),
                        "active_lease_sha256": sha256_bytes(canonical_json(dict(lease))),
                        "known_charge_ns": known,
                        "unknown_share_ns": unknown,
                        "charge_ns": known + unknown,
                        "disposition": expected_disposition.value,
                        "invalid_cause": dominant_cause.value if expected_disposition is ProcessDisposition.INVALID else None,
                    }
                )
            claim = {
                "schema": BATCH_CLAIM_SCHEMA,
                "scientific_outcome": False,
                "batch_reason": reason.value,
                "pre_ledger_entry_sha256": pre_entry,
                "pre_ledger_head_sha256": pre_head,
                "pre_state_sha256": hash_mapping(state.to_mapping()),
                "created_utc": created_utc,
                "remaining_ns": remaining_ns,
                "known_total_ns": known_total_ns,
                "unknown_stream_count": len(unknown_process_ids),
                "unknown_pool_ns": pool,
                "unknown_share_quotient_ns": quotient,
                "unknown_share_remainder_count": remainder,
                "dominant_cause": dominant_cause.value if dominant_cause else None,
                "streams": streams,
                "processes": processes,
                "omitted": list(omitted) if reason is BatchReason.RECOVERY_SETTLEMENT else [],
                "recovery_disposition_sha256": recovery_disposition_sha256,
            }
            validate_batch_claim(
                claim, leases=selected, state=state, ledger_head_sha256=pre_head, pre_ledger_entry_sha256=pre_entry
            )
            path = self._path(BATCH_CLAIMS_RELATIVE / f"{pre_head}.json")
            self._cut("before_claim")
            atomic_create(path, canonical_json(claim))
            self._cut("after_claim")
            return claim

    # -- batch settlement authority reconstruction (amendment §3b/§3c) ---

    def reconstruct_batch_authority(self, claim: Mapping[str, object]) -> BatchSettlementAuthority:
        """Rebuild the authority from the durable ledger prefix, never from an
        assumed in-memory pre-state (§3c restart reconstruction).

        A fully-consumed process contributes *two* ledger entries once its
        own follow-up event is durable (its charge, then its
        ``T_RUNTIME_INVALID`` or ``T_PROCESS_STOPPED``), so the suffix
        position of the next process's charge is not simply
        ``consumed_count`` -- a separate cursor walks past each already-
        settled process's own follow-up event exactly as ``next_batch_action``
        does, so that a two-or-more-process claim reconstructs correctly
        after every step, not only immediately after a crash."""

        entries = self._ledger().entries()
        suffix = _ledger_suffix_after(entries, str(claim["pre_ledger_entry_sha256"]))
        processes = self._effective_batch_processes(claim)
        entry_tuples = tuple(
            (str(p["process_id"]), str(p["active_lease_sha256"]), int(p["charge_ns"])) for p in processes
        )
        consumed = 0
        cursor = 0
        state_hash = str(claim["pre_state_sha256"])
        for process in processes:
            if cursor >= len(suffix):
                break
            candidate = suffix[cursor]
            if candidate.get("event") != "T_DEVICE_TIME_CHARGED":
                break
            data = candidate.get("data")
            if not isinstance(data, dict):
                break
            if (
                data.get("process_id") != process["process_id"]
                or data.get("active_lease_sha256") != process["active_lease_sha256"]
                or data.get("charge_ns") != process["charge_ns"]
            ):
                break
            if isinstance(data.get("t_state"), dict):
                state_hash = hash_mapping(data["t_state"])
            consumed += 1
            cursor += 1
            disposition = ProcessDisposition(str(process["disposition"]))
            expected_follow = (
                "T_RUNTIME_INVALID" if disposition is ProcessDisposition.INVALID else "T_PROCESS_STOPPED"
            )
            if cursor < len(suffix) and suffix[cursor].get("event") == expected_follow:
                cursor += 1
        claim_sha256 = sha256_bytes(canonical_json(dict(claim)))
        return BatchSettlementAuthority(
            claim_sha256=claim_sha256,
            entries=entry_tuples,
            consumed_count=consumed,
            expected_ledger_head_sha256=self._head(entries),
            expected_state_sha256=state_hash,
        )

    # -- override support (amendment §5) ---------------------------------

    def _batch_override_path(self, claim: Mapping[str, object]) -> Path:
        claim_sha256 = sha256_bytes(canonical_json(dict(claim)))
        return self._path(BATCH_OVERRIDES_RELATIVE / f"{claim_sha256}.json")

    def _effective_batch_processes(self, claim: Mapping[str, object]) -> list[dict[str, object]]:
        processes = [dict(p) for p in claim["processes"]]
        override_path = self._batch_override_path(claim)
        if override_path.is_file():
            override = validate_batch_override(load_canonical_json(override_path))
            replacement_by_id = {item["process_id"]: item for item in override["replacement_dispositions"]}
            for process in processes:
                replacement = replacement_by_id.get(process["process_id"])
                if replacement is not None:
                    process["disposition"] = replacement["disposition"]
                    process["invalid_cause"] = replacement["invalid_cause"]
        return processes

    def _batch_timestamp(self, claim: Mapping[str, object], process_id: str) -> str:
        override_path = self._batch_override_path(claim)
        if override_path.is_file():
            override = validate_batch_override(load_canonical_json(override_path))
            if process_id in set(override["remaining_process_ids"]):
                return str(override["created_utc"])
        return str(claim["created_utc"])

    def install_batch_override(self, claim: Mapping[str, object], *, dominant_cause: InvalidCause) -> dict[str, object]:
        """§5b: install the in-flight infrastructure-fault override, exactly once.

        ``validated_prefix_count`` is the number of *fully complete* tuples
        (§5b), which is one less than the automaton's current tuple index —
        not the number of durable charges (a charge may be durable for a
        tuple that is not yet fully complete; §5c requires that partially
        complete tuple's process to be included in ``remaining_process_ids``,
        finishing on the invalid route without another charge)."""

        with RuntimeLock(self.repo):
            reason = BatchReason(str(claim["batch_reason"]))
            if reason in (BatchReason.RUNTIME_INVALIDITY, BatchReason.RECOVERY_SETTLEMENT):
                raise HarnessRefused(
                    "a claim already carrying invalid dispositions follows its own invalid route "
                    "or the signed recovery-disposition route, never an override (§5a)"
                )
            override_path = self._batch_override_path(claim)
            if override_path.is_file():
                raise HarnessRefused("a batch override already exists for this claim")
            action, index = self.next_batch_action(claim)
            if action in (
                BatchAutomatonAction.RESOLVED,
                BatchAutomatonAction.ARCHIVE,
                BatchAutomatonAction.APPEND_EXHAUSTION,
            ):
                raise HarnessRefused("no remaining process is available to override")
            processes = self._effective_batch_processes(claim)
            validated_prefix_count = index - 1
            remaining = processes[validated_prefix_count:]
            if not remaining:
                raise HarnessRefused("a batch override requires at least one remaining process")
            remaining_ids = sorted(str(p["process_id"]) for p in remaining)
            replacement = [
                {
                    "process_id": process_id,
                    "disposition": ProcessDisposition.INVALID.value,
                    "invalid_cause": dominant_cause.value,
                }
                for process_id in remaining_ids
            ]
            override = {
                "schema": BATCH_OVERRIDE_SCHEMA,
                "scientific_outcome": False,
                "batch_claim_sha256": sha256_bytes(canonical_json(dict(claim))),
                "validated_prefix_count": validated_prefix_count,
                "pre_override_ledger_head_sha256": self._head(),
                "pre_override_state_sha256": hash_mapping(self._state().to_mapping()),
                "dominant_cause": dominant_cause.value,
                "remaining_process_ids": remaining_ids,
                "replacement_dispositions": replacement,
                "created_utc": self._now(),
            }
            validate_batch_override(override)
            self._cut("before_override")
            atomic_create(override_path, canonical_json(override))
            self._cut("after_override")
            return override

    # -- amendment §D1: claim-authorized head/cache completion -----------

    def complete_batch_head_cache_if_authorized(self, claim: Mapping[str, object]) -> bool:
        """Amendment §D1: complete a lagging state cache under six mandatory
        preconditions.  Note: this repository's ``ledger.py`` binds a ledger
        entry and its external head atomically within one ``append()`` call,
        so the external head can never independently lag through this
        harness's own write path; only the separate state-cache file can, and
        only that is completed here."""

        with RuntimeLock(self.repo):
            unresolved = self._unresolved_batch_claims()
            if len(unresolved) != 1:
                return False  # precondition 1: exactly one unresolved claim
            _, current = unresolved[0]
            if canonical_json(dict(current)) != canonical_json(dict(claim)):
                return False  # precondition 1: it must be re-validated as this claim
            entries = self._ledger().entries()
            if not entries:
                return False
            last = entries[-1]
            data = last.get("data")
            if not isinstance(data, dict) or "t_state" not in data:
                return False  # precondition 2/3: lag must be exactly one state-bearing entry
            durable_post_state = TState.from_mapping(data["t_state"])
            cached_state = self._state()
            if cached_state == durable_post_state:
                return False  # already consistent; nothing to complete
            self._cut("before_head_cache_completion")
            self._write_state(durable_post_state)
            self._cut("after_head_cache_completion")
            return True

    # -- amendment §4a/§4b: complete prefix automaton --------------------

    def next_batch_action(self, claim: Mapping[str, object]) -> tuple[BatchAutomatonAction, int]:
        """Return the sole next action and its 1-based tuple index (0 for the
        pre-tuple-work and terminal/resolved actions)."""

        entries = self._ledger().entries()
        suffix = _ledger_suffix_after(entries, str(claim["pre_ledger_entry_sha256"]))
        processes = self._effective_batch_processes(claim)
        reason = BatchReason(str(claim["batch_reason"]))
        cursor = 0
        for position, process in enumerate(processes, start=1):
            disposition = ProcessDisposition(str(process["disposition"]))
            expected = (process["process_id"], process["active_lease_sha256"], process["charge_ns"])
            if cursor >= len(suffix):
                return BatchAutomatonAction.APPEND_CHARGE, position
            entry = suffix[cursor]
            if entry.get("event") != "T_DEVICE_TIME_CHARGED":
                raise HarnessRefused("batch ledger suffix diverges from the claim automaton")
            data = entry.get("data")
            if not isinstance(data, dict) or (
                data.get("process_id"),
                data.get("active_lease_sha256"),
                data.get("charge_ns"),
            ) != expected:
                raise HarnessRefused("batch charge entry differs from its claim tuple")
            cursor += 1
            lease_path = self._path(LEASES_RELATIVE / f"{process['process_id']}.json")
            record_path = self._path(RECORDS_RELATIVE / f"{process['process_id']}.json")
            if disposition is ProcessDisposition.INVALID:
                detail_path = self._path(INVALIDITIES_RELATIVE / f"{process['process_id']}.json")
                if not detail_path.is_file():
                    return BatchAutomatonAction.WRITE_INVALID_DETAIL, position
                if cursor >= len(suffix) or suffix[cursor].get("event") != "T_RUNTIME_INVALID":
                    return BatchAutomatonAction.APPEND_INVALID_EVENT, position
                cursor += 1
                if not record_path.is_file():
                    return BatchAutomatonAction.WRITE_INVALID_RECORD, position
                if lease_path.is_file():
                    return BatchAutomatonAction.REMOVE_LEASE, position
            else:
                if not record_path.is_file():
                    return BatchAutomatonAction.WRITE_VALID_RECORD, position
                if cursor >= len(suffix) or suffix[cursor].get("event") != "T_PROCESS_STOPPED":
                    return BatchAutomatonAction.APPEND_STOPPED, position
                cursor += 1
                if lease_path.is_file():
                    return BatchAutomatonAction.REMOVE_LEASE, position
        overridden = self._batch_override_path(claim).is_file()
        if reason is BatchReason.E1_BOUNDARY and not overridden:
            # §5c: an override never appends the global exhaustion event, even
            # for an E1_BOUNDARY claim; the final route is G5, not G7.
            if cursor >= len(suffix) or suffix[cursor].get("event") != "T_ENVELOPE_EXHAUSTED":
                return BatchAutomatonAction.APPEND_EXHAUSTION, 0
            cursor += 1
        return BatchAutomatonAction.RESOLVED, 0

    def _matching_charge_entry(self, claim: Mapping[str, object], index: int) -> dict[str, object]:
        process = self._effective_batch_processes(claim)[index - 1]
        entries = self._ledger().entries()
        suffix = _ledger_suffix_after(entries, str(claim["pre_ledger_entry_sha256"]))
        expected = (process["process_id"], process["active_lease_sha256"], process["charge_ns"])
        for entry in suffix:
            if entry.get("event") != "T_DEVICE_TIME_CHARGED":
                continue
            data = entry.get("data")
            if isinstance(data, dict) and (
                data.get("process_id"),
                data.get("active_lease_sha256"),
                data.get("charge_ns"),
            ) == expected:
                return entry
        raise HarnessRefused("batch charge event for process is not yet durable")

    def _matching_event_after(self, after_entry: Mapping[str, object], event_name: str) -> dict[str, object]:
        entries = self._ledger().entries()
        for position, entry in enumerate(entries):
            if entry["entry_sha256"] == after_entry["entry_sha256"]:
                if position + 1 < len(entries) and entries[position + 1]["event"] == event_name:
                    return entries[position + 1]
                raise HarnessRefused(f"expected {event_name} immediately after the charge is absent")
        raise HarnessRefused("charge entry is not durable")

    def _perform_batch_action(
        self,
        claim: Mapping[str, object],
        authority: BatchSettlementAuthority,
        action: BatchAutomatonAction,
        index: int,
    ) -> None:
        processes = self._effective_batch_processes(claim)
        reason = BatchReason(str(claim["batch_reason"]))
        if action is BatchAutomatonAction.APPEND_CHARGE:
            process = processes[index - 1]
            state = self._state()
            current_head = self._head()
            envelope = self._envelope()
            timestamp = self._batch_timestamp(claim, str(process["process_id"]))
            state, authority = state.charge_batch_settlement(
                process_id=str(process["process_id"]),
                active_lease_sha256=str(process["active_lease_sha256"]),
                value=int(process["charge_ns"]),
                envelope=envelope,
                authority=authority,
                current_ledger_head_sha256=current_head,
            )
            self._cut("before_C")
            entry = self._ledger().append(
                event="T_DEVICE_TIME_CHARGED",
                timestamp_utc=timestamp,
                data={
                    "active_lease_sha256": process["active_lease_sha256"],
                    "charge_ns": process["charge_ns"],
                    "process_id": process["process_id"],
                    "scientific_outcome": False,
                    "t_state": state.to_mapping(),
                },
            )
            validate_ledger_event(entry)
            self._write_state(state)
            self._cut("after_C")
            return
        if action is BatchAutomatonAction.WRITE_INVALID_DETAIL:
            process = processes[index - 1]
            lease_path = self._path(LEASES_RELATIVE / f"{process['process_id']}.json")
            lease = validate_active_lease(load_canonical_json(lease_path))
            cause = InvalidCause(str(process["invalid_cause"]))
            charge_entry = self._matching_charge_entry(claim, index)
            claim_path = self._path(BATCH_CLAIMS_RELATIVE / f"{claim['pre_ledger_head_sha256']}.json")
            affected_paths = {
                (BATCH_CLAIMS_RELATIVE / f"{claim['pre_ledger_head_sha256']}.json").as_posix(): sha256_file(claim_path),
                (LEASES_RELATIVE / f"{process['process_id']}.json").as_posix(): str(process["active_lease_sha256"]),
            }
            override_path = self._batch_override_path(claim)
            if override_path.is_file():
                override = validate_batch_override(load_canonical_json(override_path))
                if process["process_id"] in set(override["remaining_process_ids"]):
                    affected_paths[
                        BATCH_OVERRIDES_RELATIVE.joinpath(f"{override['batch_claim_sha256']}.json").as_posix()
                    ] = sha256_file(override_path)
            detail = {
                "schema": INVALIDITY_SCHEMA,
                "scientific_outcome": False,
                "validity": "INVALID_PROCESS_RECORD",
                "invalid_cause": cause.value,
                "transaction_kind": "T_BATCH_SETTLEMENT",
                "durable_step_index": index,
                "affected_path_sha256": affected_paths,
                "clock_kind": CLOCK_KIND,
                "boot_identity": lease["boot_identity"],
                "observed_utc": str(charge_entry["timestamp_utc"]),
                "outstanding_liability_ns": int(lease["outstanding_liability_ns"]),
                "required_action": REQUIRED_ACTION,
            }
            validate_invalidity_record(detail)
            self._cut("before_D")
            atomic_create(self._path(INVALIDITIES_RELATIVE / f"{process['process_id']}.json"), canonical_json(detail))
            self._cut("after_D")
            return
        if action is BatchAutomatonAction.APPEND_INVALID_EVENT:
            process = processes[index - 1]
            detail_path = self._path(INVALIDITIES_RELATIVE / f"{process['process_id']}.json")
            detail = validate_invalidity_record(load_canonical_json(detail_path))
            charge_entry = self._matching_charge_entry(claim, index)
            charge_state = TState.from_mapping(charge_entry["data"]["t_state"])
            self._cut("before_E")
            entry = self._ledger().append(
                event="T_RUNTIME_INVALID",
                timestamp_utc=str(detail["observed_utc"]),
                data={
                    "invalid_cause": detail["invalid_cause"],
                    "invalidity_record_sha256": sha256_file(detail_path),
                    "required_action": REQUIRED_ACTION,
                    "scientific_outcome": False,
                    "t_state": charge_state.to_mapping(),
                },
            )
            validate_ledger_event(entry)
            self._cut("after_E")
            return
        if action is BatchAutomatonAction.WRITE_INVALID_RECORD:
            process = processes[index - 1]
            process_claim = validate_process_claim(
                load_canonical_json(self._path(CLAIMS_RELATIVE / f"{process['process_id']}.json"))
            )
            lease = validate_active_lease(
                load_canonical_json(self._path(LEASES_RELATIVE / f"{process['process_id']}.json"))
            )
            charge_entry = self._matching_charge_entry(claim, index)
            invalid_entry = self._matching_event_after(charge_entry, "T_RUNTIME_INVALID")
            detail = validate_invalidity_record(
                load_canonical_json(self._path(INVALIDITIES_RELATIVE / f"{process['process_id']}.json"))
            )
            final_state = TState.from_mapping(invalid_entry["data"]["t_state"])
            activation_hash, immutable = self._activation()
            record = build_process_record(
                claim=process_claim,
                lease=lease,
                disposition=ProcessDisposition.INVALID,
                invalid_cause=InvalidCause(str(process["invalid_cause"])),
                closed_utc=str(invalid_entry["timestamp_utc"]),
                final_charge_event=charge_entry,
                final_state=final_state,
                activation_record_sha256=activation_hash,
                immutable_control_sha256=immutable,
                terminal_event=invalid_entry,
                invalidity_record=detail,
            )
            self._cut("before_R")
            atomic_create(self._path(RECORDS_RELATIVE / f"{process['process_id']}.json"), canonical_json(record))
            self._cut("after_R")
            return
        if action is BatchAutomatonAction.WRITE_VALID_RECORD:
            # A valid tuple is never override-routed (§5c converts every
            # remaining process to the invalid route), so its terminal event
            # is always S_i, whose timestamp is unconditionally the claim's
            # created_utc (amendment §4e) — computed here before S_i exists.
            process = processes[index - 1]
            process_claim = validate_process_claim(
                load_canonical_json(self._path(CLAIMS_RELATIVE / f"{process['process_id']}.json"))
            )
            lease = validate_active_lease(
                load_canonical_json(self._path(LEASES_RELATIVE / f"{process['process_id']}.json"))
            )
            charge_entry = self._matching_charge_entry(claim, index)
            final_state = TState.from_mapping(charge_entry["data"]["t_state"])
            activation_hash, immutable = self._activation()
            disposition = {
                BatchReason.E1_BOUNDARY: ProcessDisposition.E1_EXHAUSTED,
                BatchReason.E3_BOUNDARY: ProcessDisposition.E3_DUE,
            }[reason]
            record = build_process_record(
                claim=process_claim,
                lease=lease,
                disposition=disposition,
                invalid_cause=None,
                closed_utc=str(claim["created_utc"]),
                final_charge_event=charge_entry,
                final_state=final_state,
                activation_record_sha256=activation_hash,
                immutable_control_sha256=immutable,
            )
            self._cut("before_V")
            atomic_create(self._path(RECORDS_RELATIVE / f"{process['process_id']}.json"), canonical_json(record))
            self._cut("after_V")
            return
        if action is BatchAutomatonAction.APPEND_STOPPED:
            process = processes[index - 1]
            record_path = self._path(RECORDS_RELATIVE / f"{process['process_id']}.json")
            record = validate_process_record(load_canonical_json(record_path))
            charge_entry = self._matching_charge_entry(claim, index)
            final_state = TState.from_mapping(charge_entry["data"]["t_state"])
            self._cut("before_S")
            entry = self._ledger().append(
                event="T_PROCESS_STOPPED",
                timestamp_utc=str(record["closed_utc"]),
                data={
                    "process_id": process["process_id"],
                    "process_record_sha256": sha256_file(record_path),
                    "scientific_outcome": False,
                    "t_state": final_state.to_mapping(),
                },
            )
            validate_ledger_event(entry)
            self._cut("after_S")
            return
        if action is BatchAutomatonAction.REMOVE_LEASE:
            process = processes[index - 1]
            lease_path = self._path(LEASES_RELATIVE / f"{process['process_id']}.json")
            record_path = self._path(RECORDS_RELATIVE / f"{process['process_id']}.json")
            validate_process_record(load_canonical_json(record_path))
            self._cut("before_L")
            os.unlink(lease_path)
            fsync_directory(lease_path.parent)
            self._cut("after_L")
            return
        if action is BatchAutomatonAction.APPEND_EXHAUSTION:
            state = self._state()
            self._cut("before_X")
            entry = self._ledger().append(
                event="T_ENVELOPE_EXHAUSTED",
                timestamp_utc=str(claim["created_utc"]),
                data={"resource_axis": "E1", "scientific_outcome": False, "t_state": state.to_mapping()},
            )
            validate_ledger_event(entry)
            self._cut("after_X")
            return
        raise HarnessRefused(f"no batch action is pending: {action}")

    def execute_batch_step(self, claim: Mapping[str, object]) -> BatchAutomatonAction:
        """Perform exactly the one action named by the prefix automaton."""

        with RuntimeLock(self.repo):
            action, index = self.next_batch_action(claim)
            if action is BatchAutomatonAction.RESOLVED:
                return action
            authority = self.reconstruct_batch_authority(claim)
            self._perform_batch_action(claim, authority, action, index)
            return action

    def run_batch_to_completion(self, claim: Mapping[str, object]) -> RuntimeView:
        """Drive the automaton to resolution; safe to re-invoke after any crash."""

        self.complete_batch_head_cache_if_authorized(claim)
        while True:
            action = self.execute_batch_step(claim)
            if action is BatchAutomatonAction.RESOLVED:
                break
        return self.global_state()

    # -- conservation (v2 §4e) -------------------------------------------

    def verify_conservation_at_rest(self) -> list[str]:
        failures: list[str] = []
        state = self._state()
        entries = self._ledger().entries()
        total = sum(
            int(entry["data"]["charge_ns"]) for entry in entries if entry["event"] == "T_DEVICE_TIME_CHARGED"
        )
        if total != state.device_nanoseconds:
            failures.append("global E1 differs from the sum of durable per-charge events")
        for process_id, lease in self._leases().items():
            expected = int(lease["device_units"]) * (
                int(lease["heartbeat_deadline_ns"]) - int(lease["last_charged_reading_ns"])
            )
            if int(lease["outstanding_liability_ns"]) != expected:
                failures.append(f"lease liability differs for process {process_id}")
        return failures

    # -- isolation-and-promotion protocol (v2 §5b) -----------------------

    def run_isolated_operation(self, *, perform: Callable[[], bytes]) -> str:
        """Execute ``perform`` in isolation; only its result hash ever leaves
        this call.  A fault of any kind exposes no result (§5b)."""

        try:
            raw = perform()
        except BaseException:
            raise HarnessRefused("isolated operation faulted; no result is exposed") from None
        if not isinstance(raw, (bytes, bytearray)):
            raise HarnessRefused("an isolated operation must yield raw bytes")
        return sha256_bytes(bytes(raw))

    def promote_after_settlement(
        self, *, process_id: str, operation_id: str, result_sha256: str, charge_event_sha256: str
    ) -> ReleaseToken:
        """Issue a one-use release token only after the charge is durable."""

        activation_hash, _immutable = self._activation()
        lease = self._leases().get(process_id)
        if lease is None:
            raise HarnessRefused("promotion requires a currently live lease")
        entries = self._ledger().entries()
        if not any(
            entry["entry_sha256"] == charge_event_sha256 and entry["event"] == "T_DEVICE_TIME_CHARGED"
            for entry in entries
        ):
            raise HarnessRefused("promotion charge event is not a durable settlement")
        return ReleaseToken(
            activation_record_sha256=activation_hash,
            process_id=process_id,
            lease_sha256=sha256_bytes(canonical_json(lease)),
            operation_id=operation_id,
            result_sha256=result_sha256,
            charge_event_sha256=charge_event_sha256,
        )


def typing_cast_sequence(value: object) -> Sequence[str]:
    """Narrow an untyped keyword value to ``Sequence[str]`` without importing
    ``typing.cast`` as a separate name (kept trivial and inline-reviewable)."""

    if not isinstance(value, (list, tuple)) or not all(isinstance(item, str) for item in value):
        raise ValueError("argv must be a sequence of strings")
    return list(value)


# --------------------------------------------------------------------------
# CLI (v2 §9: claim/start/heartbeat/close/pause/resume, refusal-first)
# --------------------------------------------------------------------------


def _argv() -> list[str]:
    raw = Path("/proc/self/cmdline").read_bytes().split(b"\0")
    return [item.decode("utf-8") for item in raw if item]


def main(argv: Sequence[str] | None = None) -> int:
    """Refusal-first command entry point; tests may provide argv explicitly."""

    arguments = list(_argv()[1:] if argv is None else argv)
    commands = {"claim", "start", "heartbeat", "close", "pause", "resume"}
    if not arguments or arguments[0] not in commands:
        return 2
    root = os.environ.get("OFFICINA_REPOSITORY")
    if not root:
        return 2
    try:
        harness = GenericHarness(Path(root))
        command, rest = arguments[0], arguments[1:]
        if command == "claim" and len(rest) == 5:
            harness.claim(
                argv=rest[0].split(","),
                behavior_source_sha256=rest[1],
                config_sha256=rest[2],
                stack_sha256=rest[3],
                numerical_mode_sha256=rest[4],
            )
        elif command == "start" and len(rest) == 1:
            harness.start(rest[0])
        elif command == "heartbeat" and len(rest) == 1:
            harness.heartbeat(rest[0])
        elif command == "close" and len(rest) == 1:
            harness.close(rest[0])
        elif command == "pause" and len(rest) == 1:
            harness.pause(reason=rest[0], artifact_paths={})
        elif command == "resume" and len(rest) == 1:
            harness.resume(Path(rest[0]))
        else:
            return 2
    except (HarnessRefused, ValueError, RuntimeContractError, OSError):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
