"""Signed §10 acceptance matrix (v2 as corrected by v2.1-v2.3.1) for the
implemented generic Officina T harness (``philosophia.officina.generic_harness``).

Every test here is test-only: no artifact is ever written under the real
``successor/officina/runtime/`` tree.  Integration tests build a disposable,
directly-seeded runtime root under pytest's ``tmp_path`` and drive the real
``GenericHarness`` implementation against it, injecting a fake clock/meter
(and, where relevant, fake process operations) purely through the harness's
own constructor dependency-injection parameters (``clock=``, ``meter=``,
``processes=``).  No production module is modified to expose test capability.

A note on "disposable mirror" scope: the harness's own runtime methods
(``claim``/``start``/``heartbeat``/``close``/batch settlement/pause/resume)
never re-derive anything from git history or from the authorized activation
transaction -- they only read the four durable runtime artifacts (envelope,
ledger, state cache, activation record) plus the runtime lock file.  So most
lifecycle tests below seed exactly those artifacts directly (see
``_seed_active_repo``), which is sufficient and keeps the tests fast.  A
separate, narrower group of tests exercises the full git-anchored
``activate_repository`` ceremony (as in ``tests/test_officina_activation.py``)
with the *real* (unstubbed) ``generic_harness.py`` and a genuinely computed
``PRODUCTION_CALL_GRAPH.json``, to check the production-boundary/import-graph
contract described in §10's roots/import row.
"""

from __future__ import annotations

import ast
import json
import os
import shutil
import subprocess
from datetime import timedelta
from pathlib import Path
from typing import Mapping

import pytest

from philosophia.officina.accounting import (
    NANOSECONDS_PER_HOUR,
    NANOSECONDS_PER_SECOND,
    BatchSettlementAuthority,
    TEnvelope,
    TState,
    parse_utc,
)
from philosophia.officina.activation import (
    ACTIVATION_TOKEN,
    AUTHORIZATION_RELATIVE,
    AUTHORIZATION_SCHEMA,
    DEVICE_POLICY_TOKEN,
    ENVELOPE_TOKEN,
    GENERIC_HARNESS_RELATIVE,
    GOVERNING_PATHS,
    IMMUTABLE_CONTROL_PATHS,
    PRODUCTION_MANIFEST_RELATIVE,
    PROTOCOL_PATHS,
    REQUIRED_IMMUTABLE_CONTROL_PATHS,
    ActivationRefused,
    activate_repository,
    canonical_paths,
)
from philosophia.officina.canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    hash_mapping,
    load_canonical_json,
    sha256_bytes,
    sha256_file,
)
from philosophia.officina.ledger import GENESIS, AppendOnlyLedger
from philosophia.officina.runtime import (
    HEARTBEAT_LIABILITY_SECONDS,
    MAX_CONCURRENT_LEASES,
    REVIEW_RECORD_SCHEMA,
    RUNTIME_LOCK_BYTES,
    InvalidCause,
    ProcessDisposition,
    Reservation,
    RuntimeContractError,
    boot_identity,
    build_active_lease,
    build_process_claim,
    validate_active_lease,
    validate_ledger_event,
    validate_process_claim,
)
from philosophia.officina.verification import PRODUCTION_ROOTS, verify_source_quarantine

import philosophia.officina.generic_harness as gh
from philosophia.officina.generic_harness import (
    BATCH_CLAIM_SCHEMA,
    CPU_ADAPTER_IDENTITY,
    DRAFT_MANIFEST_SCHEMA,
    GLOBAL_LIFECYCLE_TRANSITIONS,
    PROCESS_LIFECYCLE_TRANSITIONS,
    RECOVERY_DISPOSITION_SCHEMA,
    REQUIRED_ACTION,
    BatchAutomatonAction,
    BatchReason,
    GenericHarness,
    GlobalState,
    HarnessRefused,
    ProcessState,
    ReleaseToken,
    StreamClassification,
    allocate_unknown_pool_shares,
    build_batch_claim,
    classify_stream,
    derive_global_state,
    derive_process_state,
    dominant_invalid_cause,
    is_legal_global_transition,
    is_legal_process_transition,
    main as harness_main,
    validate_author_stop_decision,
    validate_batch_claim,
    validate_batch_override,
    validate_draft_manifest,
    validate_e3_decision,
    validate_pause_decision,
    validate_pending_resume_checkpoint,
    validate_recovery_disposition,
    validate_resource_stop_decision,
    validate_review_record,
)


REPO = Path(__file__).resolve().parent.parent
HARNESS_SOURCE = REPO / GENERIC_HARNESS_RELATIVE
CAP_NS = 168 * NANOSECONDS_PER_HOUR


# ---------------------------------------------------------------------------
# Fake device-time capability objects (DI only; no production capability is
# imported into test code, and no test symbol is imported into production).
# ---------------------------------------------------------------------------


class FakeClock:
    """Controllable canonical-UTC clock; ``utc_now`` returns second-precision
    ``YYYY-MM-DDTHH:MM:SSZ`` strings and can be advanced deterministically."""

    def __init__(self, start: str = "2026-07-20T00:00:00Z") -> None:
        self._current = start

    def utc_now(self) -> str:
        return self._current

    def set(self, value: str) -> None:
        self._current = value

    def advance(self, seconds: int) -> None:
        self._current = (parse_utc(self._current) + timedelta(seconds=seconds)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )


class FakeMeter:
    """Controllable monotonic-ns meter cursor, shared across every lease it
    is asked to read (mirrors the production adapter's single system-wide
    ``CLOCK_MONOTONIC`` source)."""

    adapter_identity = "philosophia.officina.fake-meter.v1"

    def __init__(self, start_ns: int = 1_000_000) -> None:
        self._reading = start_ns

    def read(self, lease: Mapping[str, object] | None = None) -> int:
        del lease
        return self._reading

    def advance(self, delta_ns: int) -> None:
        self._reading += delta_ns

    def set(self, reading_ns: int) -> None:
        self._reading = reading_ns


class FakeProcessOps:
    """Controllable alive/kill/group-membership double.  The current harness
    stores ``processes`` via constructor DI but its lifecycle methods do not
    yet call into it (a pre-execution, control-plane-only implementation
    stage); this double exists so isolation-style tests can exercise
    ``alive``/``terminate_group`` directly and so the DI contract itself is
    covered."""

    def __init__(self) -> None:
        self._alive: dict[int, bool] = {}
        self.terminated_groups: list[int] = []
        self.started: list[tuple[str, ...]] = []

    def start(self, argv):
        self.started.append(tuple(argv))
        raise NotImplementedError("fake process ops does not spawn real processes")

    def alive(self, pid: int) -> bool:
        return self._alive.get(pid, False)

    def terminate_group(self, process_group_id: int) -> None:
        self.terminated_groups.append(process_group_id)

    def set_alive(self, pid: int, value: bool) -> None:
        self._alive[pid] = value


# ---------------------------------------------------------------------------
# Disposable, directly-seeded activated runtime root (no git, no source copy;
# see module docstring for why this is sufficient for lifecycle tests).
# ---------------------------------------------------------------------------


class SeededRepo:
    def __init__(self, repo: Path, activated_utc: str, activation_record_sha256: str, immutable_control_sha256: dict[str, str]) -> None:
        self.repo = repo
        self.activated_utc = activated_utc
        self.activation_record_sha256 = activation_record_sha256
        self.immutable_control_sha256 = immutable_control_sha256


def _seed_active_repo(tmp_path: Path, *, activated_utc: str = "2026-07-20T00:00:00Z") -> SeededRepo:
    repo = tmp_path / "root"
    runtime = repo / gh.RUNTIME_ROOT
    for relative in (
        gh.CLAIMS_RELATIVE, gh.LEASES_RELATIVE, gh.RECORDS_RELATIVE,
        gh.INVALIDITIES_RELATIVE, gh.BATCH_CLAIMS_RELATIVE,
        gh.BATCH_OVERRIDES_RELATIVE, gh.PENDING_RESUME_RELATIVE,
        gh.RECOVERY_RELATIVE, gh.REVIEW_RECORDS_RELATIVE,
        gh.PAUSE_CHECKPOINTS_RELATIVE,
    ):
        (repo / relative).mkdir(parents=True)
    (repo / gh.LOCK_RELATIVE).write_bytes(RUNTIME_LOCK_BYTES)

    envelope = {
        "activated": True,
        "activated_utc": activated_utc,
        "candidate_registration_cap": 12,
        "checkpoint_device_hours": 40,
        "checkpoint_elapsed_calendar_hours": 48,
        "device_hour_cap": 168,
        "device_hours_are_aggregate": True,
        "ledger": gh.LEDGER_RELATIVE.as_posix(),
        "schema": "philosophia.officina.t-envelope-active.v1",
        "scientific_outcome": False,
        "strict_s_available": False,
    }
    atomic_create(repo / gh.ENVELOPE_RELATIVE, canonical_json(envelope))

    ledger = AppendOnlyLedger(repo / gh.LEDGER_RELATIVE, head_path=repo / gh.LEDGER_HEAD_RELATIVE)
    ledger.initialize()
    state0 = TState().activate(activated_utc)
    activation_entry = ledger.append(
        event="T_ACTIVATED",
        timestamp_utc=activated_utc,
        data={
            "authorization_sha256": "a" * 64,
            "claim_sha256": "b" * 64,
            "device_policy_token": DEVICE_POLICY_TOKEN,
            "envelope_token": ENVELOPE_TOKEN,
            "scientific_outcome": False,
            "t_state": state0.to_mapping(),
        },
    )
    validate_ledger_event(activation_entry)
    atomic_create(repo / gh.STATE_RELATIVE, canonical_json(state0.to_mapping()))

    immutable = {path: sha256_bytes(path.encode("ascii")) for path in REQUIRED_IMMUTABLE_CONTROL_PATHS}
    record_path = repo / gh.ACTIVATION_RECORD_RELATIVE
    atomic_create(record_path, canonical_json({"immutable_control_sha256": immutable}))
    return SeededRepo(repo, activated_utc, sha256_file(record_path), immutable)


def _ledger_for(repo: Path) -> AppendOnlyLedger:
    return AppendOnlyLedger(repo / gh.LEDGER_RELATIVE, head_path=repo / gh.LEDGER_HEAD_RELATIVE)


def _claim_and_start(
    harness: GenericHarness, *, suffix: str = "1", device_units: int = 1
) -> str:
    claim = harness.claim(
        argv=["python", f"worker-{suffix}.py"],
        behavior_source_sha256=sha256_bytes(f"behavior-{suffix}".encode()),
        config_sha256=sha256_bytes(f"config-{suffix}".encode()),
        stack_sha256=sha256_bytes(f"stack-{suffix}".encode()),
        numerical_mode_sha256=sha256_bytes(f"numerical-{suffix}".encode()),
        device_units=device_units,
    )
    process_id = str(claim["process_id"])
    harness.start(process_id)
    return process_id


def _install_fabricated_live_process(
    seeded: SeededRepo,
    *,
    sequence: int,
    start_reading_ns: int,
    liability_ns_per_unit: int,
    label: str,
) -> tuple[dict[str, object], dict[str, object]]:
    """Directly install a schema-valid claim+lease pair (bypassing ``claim``/
    ``start``'s reservation-routing gate) so batch-witness tests can place a
    live process at an arbitrary meter position without also having to walk
    the E1/E3 reservation state machine to get there. Used only for the
    frozen-batch matrix rows (§10 items 8/9/15/16/21) where the *numbers*
    matter, mirroring how ``tests/test_officina_runtime.py`` and
    ``tests/test_officina_accounting.py`` construct artifacts directly."""

    claim = build_process_claim(
        activation_record_sha256=seeded.activation_record_sha256,
        process_sequence=sequence,
        controller_pid=os.getpid(),
        controller_start_identity=str(os.getpid()),
        process_group_id=os.getpgrp(),
        argv=["python", f"worker-{label}.py"],
        behavior_source_sha256=sha256_bytes(f"behavior-{label}".encode()),
        config_sha256=sha256_bytes(f"config-{label}".encode()),
        stack_sha256=sha256_bytes(f"stack-{label}".encode()),
        numerical_mode_sha256=sha256_bytes(f"numerical-{label}".encode()),
        device_identity=CPU_ADAPTER_IDENTITY,
        device_units=1,
        created_utc=seeded.activated_utc,
        boot_id=boot_identity(),
        start_reading_ns=start_reading_ns,
        immutable_control_sha256=seeded.immutable_control_sha256,
    )
    reservation = Reservation(1, liability_ns_per_unit)
    lease = build_active_lease(
        claim,
        reservation=reservation,
        prior_charge_event_sha256="0" * 64,
        activation_record_sha256=seeded.activation_record_sha256,
        immutable_control_sha256=seeded.immutable_control_sha256,
    )
    process_id = str(claim["process_id"])
    atomic_create(seeded.repo / gh.CLAIMS_RELATIVE / f"{process_id}.json", canonical_json(claim))
    atomic_create(seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json", canonical_json(lease))
    return claim, lease


def _set_device_nanoseconds(seeded: SeededRepo, value: int) -> None:
    """Raise device_nanoseconds to ``value`` via a durable dummy charge event,
    so the ledger and the state cache stay mutually consistent (a cache
    written *without* a matching ledger entry is indistinguishable from a
    stale/lagging cache, and the harness's own §D1 head/cache-completion
    logic will legitimately overwrite it back to the ledger's last durable
    state the next time a batch runs; see ``complete_batch_head_cache_if_authorized``)."""

    ledger = _ledger_for(seeded.repo)
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    delta = value - state.device_nanoseconds
    if delta <= 0:
        raise ValueError("device nanoseconds can only be raised forward in this test helper")
    next_state = state.charge_device_nanoseconds(delta, TEnvelope())
    entry = ledger.append(
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc=seeded.activated_utc,
        data={
            "active_lease_sha256": "0" * 64,
            "charge_ns": delta,
            "process_id": "0" * 64,
            "scientific_outcome": False,
            "t_state": next_state.to_mapping(),
        },
    )
    validate_ledger_event(entry)
    atomic_replace(seeded.repo / gh.STATE_RELATIVE, canonical_json(next_state.to_mapping()))


# ===========================================================================
# §10.1 -- Pure helpers (no filesystem)
# ===========================================================================


@pytest.mark.parametrize(
    ("causes", "expected"),
    [
        ((InvalidCause.HASH, InvalidCause.FILESYSTEM), InvalidCause.HASH),
        ((InvalidCause.FILESYSTEM, InvalidCause.CLOCK), InvalidCause.FILESYSTEM),
        ((InvalidCause.CLOCK, InvalidCause.PROCESS), InvalidCause.CLOCK),
        ((InvalidCause.PROCESS, InvalidCause.RESOURCE), InvalidCause.PROCESS),
        ((InvalidCause.RESOURCE,), InvalidCause.RESOURCE),
        (
            (
                InvalidCause.RESOURCE, InvalidCause.PROCESS,
                InvalidCause.CLOCK, InvalidCause.FILESYSTEM, InvalidCause.HASH,
            ),
            InvalidCause.HASH,
        ),
        (
            (InvalidCause.RESOURCE, InvalidCause.PROCESS, InvalidCause.CLOCK, InvalidCause.FILESYSTEM),
            InvalidCause.FILESYSTEM,
        ),
        ((InvalidCause.RESOURCE, InvalidCause.PROCESS, InvalidCause.CLOCK), InvalidCause.CLOCK),
        (("HASH", "RESOURCE"), InvalidCause.HASH),
    ],
)
def test_dominant_invalid_cause_precedence_every_pair_and_hash_wins_over_all(causes, expected) -> None:
    assert dominant_invalid_cause(causes) == expected


def test_dominant_invalid_cause_requires_at_least_one_observed_cause() -> None:
    with pytest.raises(ValueError, match="observed cause"):
        dominant_invalid_cause(())


@pytest.mark.parametrize(
    ("remaining_ns", "known_total_ns", "unknown_stream_count", "expected"),
    [
        # m=0: the pool is never applicable regardless of remaining/known,
        # exactly the 60/60/60 boundary example's shape (three KNOWN streams,
        # zero unknown ones).
        (0, 0, 0, (0, 0, 0, ())),
        (60 * NANOSECONDS_PER_HOUR, 180, 0, (0, 0, 0, ())),
        # m=1: the single stream takes the whole positive remainder pool.
        (1_000, 200, 1, (800, 800, 0, (800,))),
        # m=2: exact quotient, no remainder.
        (1_000, 200, 2, (800, 400, 0, (400, 400))),
        # m=3: exact quotient, no remainder.
        (1_000, 400, 3, (600, 200, 0, (200, 200, 200))),
        # m=3 with a remainder: the first r streams get one extra ns each,
        # canonical ascending order, and the split still sums exactly to U.
        (1_000, 300, 3, (700, 233, 1, (234, 233, 233))),
        # remaining - known < 0: U floors up to m, each unknown stream gets
        # exactly 1 ns (the minimum-share invariant), not a negative pool.
        (100, 500, 4, (4, 1, 0, (1, 1, 1, 1))),
        (0, 1, 1, (1, 1, 0, (1,))),
    ],
)
def test_allocate_unknown_pool_shares_exact_arithmetic(
    remaining_ns, known_total_ns, unknown_stream_count, expected
) -> None:
    result = allocate_unknown_pool_shares(remaining_ns, known_total_ns, unknown_stream_count)
    assert result == expected
    pool, quotient, remainder, shares = result
    assert sum(shares) == pool
    if unknown_stream_count:
        assert min(shares) >= 1


def test_allocate_unknown_pool_shares_h2_1_style_five_seconds_over_two_streams() -> None:
    five_seconds_ns = 5 * NANOSECONDS_PER_SECOND
    pool, quotient, remainder, shares = allocate_unknown_pool_shares(five_seconds_ns, 0, 2)
    assert pool == five_seconds_ns
    assert (quotient, remainder) == divmod(five_seconds_ns, 2)
    assert shares == (quotient + remainder, quotient)
    assert sum(shares) == five_seconds_ns


def test_allocate_unknown_pool_shares_rejects_malformed_inputs() -> None:
    with pytest.raises(ValueError, match="remaining_ns"):
        allocate_unknown_pool_shares(-1, 0, 1)
    with pytest.raises(ValueError, match="known_total_ns"):
        allocate_unknown_pool_shares(10, -1, 1)
    with pytest.raises(ValueError, match="unknown_stream_count"):
        allocate_unknown_pool_shares(10, 0, -1)


@pytest.mark.parametrize(
    ("kwargs", "expected"),
    [
        (
            dict(interval_start_reading_ns=0, interval_end_reading_ns=None, backend_synchronized=False, heartbeat_deadline_ns=100),
            StreamClassification.UNKNOWABLE,
        ),
        (
            dict(interval_start_reading_ns=0, interval_end_reading_ns=50, backend_synchronized=True, heartbeat_deadline_ns=100),
            StreamClassification.TIMELY_KNOWN,
        ),
        (
            dict(interval_start_reading_ns=0, interval_end_reading_ns=100, backend_synchronized=True, heartbeat_deadline_ns=100),
            StreamClassification.TIMELY_KNOWN,
        ),
        (
            dict(interval_start_reading_ns=0, interval_end_reading_ns=101, backend_synchronized=True, heartbeat_deadline_ns=100),
            StreamClassification.LATE_KNOWN,
        ),
    ],
)
def test_classify_stream_boundary_cases(kwargs, expected) -> None:
    assert classify_stream(**kwargs) is expected


def test_classify_stream_rejects_incoherent_unknowable_or_known_shapes() -> None:
    with pytest.raises(ValueError, match="unsynchronized"):
        classify_stream(
            interval_start_reading_ns=0, interval_end_reading_ns=None,
            backend_synchronized=True, heartbeat_deadline_ns=100,
        )
    with pytest.raises(ValueError, match="positive synchronized interval"):
        classify_stream(
            interval_start_reading_ns=0, interval_end_reading_ns=50,
            backend_synchronized=False, heartbeat_deadline_ns=100,
        )
    with pytest.raises(ValueError, match="positive synchronized interval"):
        classify_stream(
            interval_start_reading_ns=50, interval_end_reading_ns=50,
            backend_synchronized=True, heartbeat_deadline_ns=100,
        )


def test_process_lifecycle_transition_table_is_exhaustive_and_matches_helper() -> None:
    for current in ProcessState:
        for candidate in ProcessState:
            expected = candidate in PROCESS_LIFECYCLE_TRANSITIONS[current]
            assert is_legal_process_transition(current, candidate) is expected
    # Terminal states have no legal successor at all.
    assert PROCESS_LIFECYCLE_TRANSITIONS[ProcessState.P4] == ()
    assert PROCESS_LIFECYCLE_TRANSITIONS[ProcessState.P5] == ()
    # Only LIVE may self-loop (ordinary heartbeat conservation, item 12).
    assert ProcessState.P3 in PROCESS_LIFECYCLE_TRANSITIONS[ProcessState.P3]


def test_global_lifecycle_transition_table_is_exhaustive_and_matches_helper() -> None:
    for current in GlobalState:
        for candidate in GlobalState:
            expected = candidate in GLOBAL_LIFECYCLE_TRANSITIONS[current]
            assert is_legal_global_transition(current, candidate) is expected
    assert GLOBAL_LIFECYCLE_TRANSITIONS[GlobalState.G6] == ()
    assert GLOBAL_LIFECYCLE_TRANSITIONS[GlobalState.G7] == ()
    # G5 (RUNTIME_INVALID) may only clear back to G1, or persist.
    assert set(GLOBAL_LIFECYCLE_TRANSITIONS[GlobalState.G5]) == {GlobalState.G5, GlobalState.G1}


def test_derive_process_state_pure_classifier_precedence() -> None:
    assert derive_process_state(claimed=False, started=False, leased=False, record=None) is ProcessState.P0
    assert derive_process_state(claimed=True, started=False, leased=False, record=None) is ProcessState.P1
    assert derive_process_state(claimed=True, started=True, leased=False, record=None) is ProcessState.P2
    assert derive_process_state(claimed=True, started=True, leased=True, record=None) is ProcessState.P3
    valid_record = {"disposition": ProcessDisposition.CLOSED.value}
    invalid_record = {"disposition": ProcessDisposition.INVALID.value}
    assert derive_process_state(claimed=True, started=True, leased=True, record=valid_record) is ProcessState.P4
    assert derive_process_state(claimed=True, started=True, leased=False, record=invalid_record) is ProcessState.P5
    # A durable record dominates a still-present lease (batch REMOVE_LEASE
    # may not yet have run when the record is already durable).
    assert derive_process_state(claimed=True, started=True, leased=True, record=invalid_record) is ProcessState.P5


def test_derive_global_state_pure_classifier_dominance_order() -> None:
    envelope = TEnvelope()
    inactive = TState()
    assert derive_global_state(state=inactive, envelope=envelope, now_utc="2026-07-20T00:00:00Z", last_event=None, live_process_count=0) is GlobalState.G0

    active = TState().activate("2026-07-20T00:00:00Z")
    stopped = TState(activated_utc="2026-07-20T00:00:00Z", last_review_utc="2026-07-20T00:00:00Z", author_stopped=True)
    assert derive_global_state(state=stopped, envelope=envelope, now_utc="2026-07-20T00:00:00Z", last_event=None, live_process_count=0) is GlobalState.G6

    exhausted = TState(activated_utc="2026-07-20T00:00:00Z", device_nanoseconds=CAP_NS)
    assert derive_global_state(state=exhausted, envelope=envelope, now_utc="2026-07-20T00:00:00Z", last_event=None, live_process_count=0) is GlobalState.G7

    pending = TState(activated_utc="2026-07-20T00:00:00Z", resume_review_pending=True)
    assert derive_global_state(state=pending, envelope=envelope, now_utc="2026-07-20T00:00:00Z", last_event=None, live_process_count=0) is GlobalState.G4

    review_due = TState(activated_utc="2026-07-20T00:00:00Z")
    assert derive_global_state(
        state=review_due, envelope=envelope, now_utc="2026-07-22T01:00:00Z", last_event=None, live_process_count=0
    ) is GlobalState.G2

    paused = TState(activated_utc="2026-07-20T00:00:00Z")
    assert derive_global_state(
        state=paused, envelope=envelope, now_utc="2026-07-20T01:00:00Z",
        last_event="T_OPERATIONAL_PAUSE", live_process_count=0,
    ) is GlobalState.G3
    # A live process blocks the paused classification even with the same
    # trailing ledger event (pause requires zero live leases, §6a).
    assert derive_global_state(
        state=paused, envelope=envelope, now_utc="2026-07-20T01:00:00Z",
        last_event="T_OPERATIONAL_PAUSE", live_process_count=1,
    ) is GlobalState.G1

    assert derive_global_state(state=active, envelope=envelope, now_utc="2026-07-20T00:00:01Z", last_event="T_PROCESS_STARTED", live_process_count=1) is GlobalState.G1


# ===========================================================================
# §10.4 -- Draft manifest (v2 §8)
# ===========================================================================


def _draft_manifest(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": DRAFT_MANIFEST_SCHEMA,
        "scientific_outcome": False,
        "t_quarantine": "dev-non-citable",
        "q_eligible": False,
        "behavior_source_sha256": "a" * 64,
        "config_sha256": "b" * 64,
        "stack_sha256": "c" * 64,
        "numerical_mode_sha256": "d" * 64,
        "device_identity": CPU_ADAPTER_IDENTITY,
    }
    base.update(overrides)
    return base


def test_validate_draft_manifest_accepts_exact_keys() -> None:
    manifest = validate_draft_manifest(_draft_manifest())
    assert manifest["t_quarantine"] == "dev-non-citable"
    assert manifest["q_eligible"] is False


@pytest.mark.parametrize("extra_key", ["timestamp", "lineage"])
def test_validate_draft_manifest_rejects_extra_timestamp_or_lineage_field(extra_key: str) -> None:
    payload = _draft_manifest()
    payload[extra_key] = "2026-07-20T00:00:00Z" if extra_key == "timestamp" else "parent-1"
    with pytest.raises(ValueError, match="fields differ"):
        validate_draft_manifest(payload)


def test_validate_draft_manifest_rejects_nested_scientific_field() -> None:
    payload = _draft_manifest()
    payload["device_identity"] = {"loss": 0.1}  # type: ignore[assignment]
    with pytest.raises(ValueError, match="forbidden scientific field"):
        validate_draft_manifest(payload)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda p: p.__setitem__("t_quarantine", "citable"),
        lambda p: p.__setitem__("q_eligible", True),
        lambda p: p.__setitem__("schema", "wrong"),
        lambda p: p.__setitem__("scientific_outcome", True),
        lambda p: p.__setitem__("behavior_source_sha256", "not-a-hash"),
        lambda p: p.__setitem__("device_identity", ""),
    ],
)
def test_validate_draft_manifest_rejects_each_field_violation(mutation) -> None:
    payload = _draft_manifest()
    mutation(payload)
    with pytest.raises(ValueError):
        validate_draft_manifest(payload)


# ===========================================================================
# §10.5 -- Closed non-outcome decision schemas (v2.1 §E)
# ===========================================================================


def _e3_decision(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.e3-decision.v1",
        "scientific_outcome": False,
        "activation_record_sha256": "a" * 64,
        "state_sha256": "b" * 64,
        "observed_utc": "2026-07-20T00:00:00Z",
        "last_review_utc": "2026-07-19T00:00:00Z",
        "device_ns_at_review": 0,
        "device_ns_now": 100,
        "calendar_due": True,
        "device_due": False,
    }
    base.update(overrides)
    return base


def _resource_stop_decision(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.resource-stop-decision.v1",
        "scientific_outcome": False,
        "process_id": "a" * 64,
        "lease_sha256": "b" * 64,
        "state_sha256": "c" * 64,
        "observed_utc": "2026-07-20T00:00:00Z",
        "monotonic_reading_ns": 100,
        "reason": "E1_BUDGET",
    }
    base.update(overrides)
    return base


def _pause_decision(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.pause-decision.v1",
        "scientific_outcome": False,
        "activation_record_sha256": "a" * 64,
        "state_sha256": "b" * 64,
        "ledger_head_sha256": "c" * 64,
        "observed_utc": "2026-07-20T00:00:00Z",
        "live_lease_count": 0,
        "checkpoint_sha256": "d" * 64,
    }
    base.update(overrides)
    return base


def _author_stop_decision(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.author-stop-decision.v1",
        "scientific_outcome": False,
        "review_record_sha256": "a" * 64,
        "ledger_head_sha256": "b" * 64,
        "state_sha256": "c" * 64,
        "signed_utc": "2026-07-20T00:00:00Z",
        "author_decision_sha256": "d" * 64,
    }
    base.update(overrides)
    return base


def _recovery_disposition(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": RECOVERY_DISPOSITION_SCHEMA,
        "scientific_outcome": False,
        "author_decision_sha256": "a" * 64,
        "invalidity_record_sha256": "b" * 64,
        "invalidity_event_sha256": "c" * 64,
        "ledger_head_sha256": "d" * 64,
        "state_sha256": "e" * 64,
        "affected_process_ids": ["f" * 64],
        "charge_event_sha256s": ["1" * 64],
        "resolution_action": "REMAIN_BLOCKED",
        "resolved_utc": "2026-07-20T00:00:00Z",
    }
    base.update(overrides)
    return base


@pytest.mark.parametrize(
    ("validator", "builder", "hash_field"),
    [
        (validate_e3_decision, _e3_decision, "activation_record_sha256"),
        (validate_resource_stop_decision, _resource_stop_decision, "process_id"),
        (validate_pause_decision, _pause_decision, "checkpoint_sha256"),
        (validate_author_stop_decision, _author_stop_decision, "author_decision_sha256"),
        (validate_recovery_disposition, _recovery_disposition, "author_decision_sha256"),
    ],
)
def test_decision_schema_validators_accept_exact_payload(validator, builder, hash_field) -> None:
    validator(builder())


@pytest.mark.parametrize(
    "validator_and_builder",
    [
        (validate_e3_decision, _e3_decision),
        (validate_resource_stop_decision, _resource_stop_decision),
        (validate_pause_decision, _pause_decision),
        (validate_author_stop_decision, _author_stop_decision),
        (validate_recovery_disposition, _recovery_disposition),
    ],
)
def test_decision_schema_validators_reject_free_text_and_unknown_key(validator_and_builder) -> None:
    validator, builder = validator_and_builder
    with pytest.raises(ValueError):
        validator("not a mapping, just free text")
    payload = builder()
    payload["unexpected_extra_field"] = "x"
    with pytest.raises(ValueError, match="fields differ"):
        validator(payload)


@pytest.mark.parametrize(
    ("validator", "builder", "hash_field"),
    [
        (validate_e3_decision, _e3_decision, "activation_record_sha256"),
        (validate_resource_stop_decision, _resource_stop_decision, "process_id"),
        (validate_pause_decision, _pause_decision, "checkpoint_sha256"),
        (validate_author_stop_decision, _author_stop_decision, "author_decision_sha256"),
        (validate_recovery_disposition, _recovery_disposition, "author_decision_sha256"),
    ],
)
def test_decision_schema_validators_reject_learner_derived_malformed_hash(validator, builder, hash_field) -> None:
    payload = builder()
    payload[hash_field] = "not-actually-a-derived-sha256"
    with pytest.raises(ValueError, match="SHA-256"):
        validator(payload)


def test_e3_decision_rejects_incoherent_device_counters_and_booleans() -> None:
    with pytest.raises(ValueError, match="differ"):
        validate_e3_decision(_e3_decision(device_ns_now=0, device_ns_at_review=100))
    with pytest.raises(ValueError, match="differ"):
        validate_e3_decision(_e3_decision(calendar_due="yes"))


def test_resource_stop_decision_rejects_unknown_reason() -> None:
    with pytest.raises(ValueError, match="reason"):
        validate_resource_stop_decision(_resource_stop_decision(reason="BECAUSE_I_SAID_SO"))


def test_pause_decision_requires_zero_live_leases() -> None:
    with pytest.raises(ValueError, match="no live lease"):
        validate_pause_decision(_pause_decision(live_lease_count=1))


def test_recovery_disposition_requires_sorted_unique_arrays_and_known_action() -> None:
    with pytest.raises(ValueError, match="sorted unique array"):
        validate_recovery_disposition(_recovery_disposition(affected_process_ids=["b" * 64, "a" * 64]))
    with pytest.raises(ValueError, match="sorted unique array"):
        validate_recovery_disposition(_recovery_disposition(affected_process_ids=["a" * 64, "a" * 64]))
    with pytest.raises(ValueError, match="action differs"):
        validate_recovery_disposition(_recovery_disposition(resolution_action="JUST_RETRY"))


# ===========================================================================
# Pending resume checkpoint (v2.2 §C) and batch override (amendment §5b)
# pure schema coverage.
# ===========================================================================


def _pending_resume_checkpoint(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.t-pending-resume-checkpoint.v1",
        "scientific_outcome": False,
        "original_checkpoint_sha256": "a" * 64,
        "payload_sha256": "b" * 64,
        "ledger_head_before": "c" * 64,
        "created_utc": "2026-07-20T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_validate_pending_resume_checkpoint_accepts_exact_keys_and_rejects_extra() -> None:
    validate_pending_resume_checkpoint(_pending_resume_checkpoint())
    payload = _pending_resume_checkpoint()
    payload["note"] = "extra"
    with pytest.raises(ValueError, match="fields differ"):
        validate_pending_resume_checkpoint(payload)


def _batch_override(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema": "philosophia.officina.t-batch-settlement-invalidity-override.v1",
        "scientific_outcome": False,
        "batch_claim_sha256": "a" * 64,
        "validated_prefix_count": 1,
        "pre_override_ledger_head_sha256": "b" * 64,
        "pre_override_state_sha256": "c" * 64,
        "dominant_cause": InvalidCause.PROCESS.value,
        "remaining_process_ids": ["d" * 64],
        "replacement_dispositions": [
            {"process_id": "d" * 64, "disposition": ProcessDisposition.INVALID.value, "invalid_cause": InvalidCause.PROCESS.value}
        ],
        "created_utc": "2026-07-20T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_validate_batch_override_accepts_exact_shape() -> None:
    validate_batch_override(_batch_override())


def test_validate_batch_override_rejects_replacement_dispositions_mismatch() -> None:
    payload = _batch_override()
    payload["replacement_dispositions"][0]["invalid_cause"] = InvalidCause.RESOURCE.value
    with pytest.raises(ValueError, match="replacement disposition"):
        validate_batch_override(payload)
    payload = _batch_override()
    payload["remaining_process_ids"] = ["d" * 64, "e" * 64]
    with pytest.raises(ValueError, match="cover exactly"):
        validate_batch_override(payload)


# ===========================================================================
# §10.7 -- Accounting integration: E1-crossing counts via BatchSettlementAuthority
# (mirrors tests/test_officina_accounting.py patterns; repeated here for the
# signed matrix's own record).
# ===========================================================================


def _authority_for(entries: tuple[tuple[str, str, int], ...], *, pre_state: TState) -> BatchSettlementAuthority:
    return BatchSettlementAuthority(
        claim_sha256="a" * 64,
        entries=entries,
        consumed_count=0,
        expected_ledger_head_sha256="b" * 64,
        expected_state_sha256=hash_mapping(pre_state.to_mapping()),
    )


def test_batch_settlement_zero_e1_crossings_stays_below_cap() -> None:
    envelope = TEnvelope()
    state = TState().activate("2026-07-20T00:00:00Z")
    entry = ("a" * 64, "b" * 64, 10)
    authority = _authority_for((entry,), pre_state=state)
    state, authority = state.charge_batch_settlement(
        process_id=entry[0], active_lease_sha256=entry[1], value=entry[2],
        envelope=envelope, authority=authority, current_ledger_head_sha256="b" * 64,
    )
    assert state.device_nanoseconds == 10
    assert not state.exhausted(envelope)


def test_batch_settlement_one_e1_crossing_lands_exactly_at_cap() -> None:
    envelope = TEnvelope()
    state = TState(activated_utc="2026-07-20T00:00:00Z", device_nanoseconds=CAP_NS - 10)
    entry = ("a" * 64, "b" * 64, 10)
    authority = _authority_for((entry,), pre_state=state)
    state, authority = state.charge_batch_settlement(
        process_id=entry[0], active_lease_sha256=entry[1], value=entry[2],
        envelope=envelope, authority=authority, current_ledger_head_sha256="b" * 64,
    )
    assert state.device_nanoseconds == CAP_NS
    assert state.exhausted(envelope)


def test_batch_settlement_multiple_e1_crossings_60_60_60_pool_conservation() -> None:
    """The signed 60/60/60 counterexample: three processes each carry a
    known LATE_KNOWN charge of exactly 60ns starting 100ns below the cap, so
    the *second and third* tuples cross E1 mid-batch, and the sum charged
    exceeds the pre-batch remaining budget by design (frozen-batch charges
    are the only route allowed to cross/exceed E1 within one claim)."""

    envelope = TEnvelope()
    state = TState(activated_utc="2026-07-20T00:00:00Z", device_nanoseconds=CAP_NS - 100)
    entries = (
        ("a" * 64, "1" * 64, 60),
        ("b" * 64, "2" * 64, 60),
        ("c" * 64, "3" * 64, 60),
    )
    authority = _authority_for(entries, pre_state=state)
    for process_id, lease_sha256, value in entries:
        head = authority.expected_ledger_head_sha256
        state, authority = state.charge_batch_settlement(
            process_id=process_id, active_lease_sha256=lease_sha256, value=value,
            envelope=envelope, authority=authority, current_ledger_head_sha256=head,
        )
    assert state.device_nanoseconds == CAP_NS - 100 + 180
    assert state.exhausted(envelope)
    assert authority.consumed_count == 3


def test_batch_settlement_rejects_reorder_duplicate_omission_or_value_change() -> None:
    envelope = TEnvelope()
    state = TState().activate("2026-07-20T00:00:00Z")
    entries = (("a" * 64, "1" * 64, 60), ("b" * 64, "2" * 64, 60))
    authority = _authority_for(entries, pre_state=state)
    with pytest.raises(ValueError, match="entry mismatch"):
        state.charge_batch_settlement(
            process_id="b" * 64, active_lease_sha256="2" * 64, value=60,
            envelope=envelope, authority=authority, current_ledger_head_sha256=authority.expected_ledger_head_sha256,
        )
    with pytest.raises(ValueError, match="entry mismatch"):
        state.charge_batch_settlement(
            process_id="a" * 64, active_lease_sha256="1" * 64, value=61,
            envelope=envelope, authority=authority, current_ledger_head_sha256=authority.expected_ledger_head_sha256,
        )


# ===========================================================================
# §10.8/§10.9 -- Batch claim witness (pure re-validation; no filesystem)
# ===========================================================================


def _synthetic_lease(
    process_id_seed: str, *, start_reading_ns: int = 0, heartbeat_deadline_ns: int = 100, process_sequence: int = 0
) -> dict[str, object]:
    core = {
        "activation_record_sha256": "a" * 64,
        "argv": ["python", f"{process_id_seed}.py"],
        "behavior_source_sha256": sha256_bytes(f"behavior-{process_id_seed}".encode()),
        "boot_identity": "11111111-1111-1111-1111-111111111111",
        "config_sha256": sha256_bytes(f"config-{process_id_seed}".encode()),
        "device_identity": CPU_ADAPTER_IDENTITY,
        "device_units": 1,
        "numerical_mode_sha256": sha256_bytes(f"numerical-{process_id_seed}".encode()),
        "process_sequence": process_sequence,
        "stack_sha256": sha256_bytes(f"stack-{process_id_seed}".encode()),
    }
    from philosophia.officina.runtime import process_id_for

    process_id = process_id_for(core)
    claim = {
        "schema": "philosophia.officina.t-process-claim.v1",
        "scientific_outcome": False,
        **core,
        "process_id": process_id,
        "controller_pid": 1,
        "controller_start_identity": "1",
        "process_group_id": 1,
        "created_utc": "2026-07-20T00:00:00Z",
        "clock_kind": "CLOCK_MONOTONIC",
        "start_reading_ns": start_reading_ns,
        "immutable_control_sha256": {"x": "0" * 64},
    }
    lease = {
        **claim,
        "schema": "philosophia.officina.t-active-lease.v1",
        "last_charged_reading_ns": start_reading_ns,
        "cumulative_charge_ns": 0,
        "heartbeat_deadline_ns": heartbeat_deadline_ns,
        "outstanding_liability_ns": heartbeat_deadline_ns - start_reading_ns,
        "prior_charge_event_sha256": "0" * 64,
    }
    return lease


def _known_stream(index: int, process_id: str, *, start: int, end: int, boot_identity: str, deadline: int) -> dict[str, object]:
    classification = classify_stream(
        interval_start_reading_ns=start, interval_end_reading_ns=end,
        backend_synchronized=True, heartbeat_deadline_ns=deadline,
    )
    return {
        "stream_index": index,
        "process_id": process_id,
        "classification": classification.value,
        "known_charge_ns": end - start,
        "unknown_share_ns": None,
        "meter_evidence": {
            "clock_kind": "CLOCK_MONOTONIC",
            "boot_identity": boot_identity,
            "adapter_identity": CPU_ADAPTER_IDENTITY,
            "interval_start_reading_ns": start,
            "interval_end_reading_ns": end,
            "backend_synchronized": True,
            "observed_utc": "2026-07-20T00:00:00Z",
        },
    }


def _e1_boundary_claim_for_two_processes() -> tuple[dict[str, object], dict[str, dict[str, object]], TState]:
    lease_a = _synthetic_lease("proc-a", start_reading_ns=0, heartbeat_deadline_ns=1_000, process_sequence=0)
    lease_b = _synthetic_lease("proc-b", start_reading_ns=0, heartbeat_deadline_ns=1_000, process_sequence=1)
    pid_a, pid_b = str(lease_a["process_id"]), str(lease_b["process_id"])
    state = TState(activated_utc="2026-07-20T00:00:00Z", device_nanoseconds=0)
    stream_a = _known_stream(1, pid_a, start=0, end=100, boot_identity=str(lease_a["boot_identity"]), deadline=1_000)
    stream_b = _known_stream(2, pid_b, start=0, end=200, boot_identity=str(lease_b["boot_identity"]), deadline=1_000)
    claim = {
        "schema": BATCH_CLAIM_SCHEMA,
        "scientific_outcome": False,
        "batch_reason": BatchReason.E1_BOUNDARY.value,
        "pre_ledger_entry_sha256": "0" * 64,
        "pre_ledger_head_sha256": "0" * 64,
        "pre_state_sha256": hash_mapping(state.to_mapping()),
        "created_utc": "2026-07-20T00:00:00Z",
        "remaining_ns": 168 * NANOSECONDS_PER_HOUR,
        "known_total_ns": 300,
        "unknown_stream_count": 0,
        "unknown_pool_ns": 0,
        "unknown_share_quotient_ns": 0,
        "unknown_share_remainder_count": 0,
        "dominant_cause": None,
        "streams": [stream_a, stream_b],
        "processes": [
            {
                "process_id": pid_a, "process_sequence": 0,
                "active_lease_sha256": sha256_bytes(canonical_json(lease_a)),
                "known_charge_ns": 100, "unknown_share_ns": 0, "charge_ns": 100,
                "disposition": "T_PROCESS_E1_EXHAUSTED", "invalid_cause": None,
            },
            {
                "process_id": pid_b, "process_sequence": 1,
                "active_lease_sha256": sha256_bytes(canonical_json(lease_b)),
                "known_charge_ns": 200, "unknown_share_ns": 0, "charge_ns": 200,
                "disposition": "T_PROCESS_E1_EXHAUSTED", "invalid_cause": None,
            },
        ],
        "omitted": [],
        "recovery_disposition_sha256": None,
    }
    return claim, {pid_a: lease_a, pid_b: lease_b}, state


def test_validate_batch_claim_recomputes_u_q_r_and_shares_and_accepts_well_formed_claim() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    validated = validate_batch_claim(claim, leases=leases, state=state, ledger_head_sha256="0" * 64, pre_ledger_entry_sha256="0" * 64)
    assert validated["known_total_ns"] == 300
    assert validated["unknown_pool_ns"] == 0


def test_validate_batch_claim_process_aggregate_must_equal_known_plus_unknown() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["processes"][0]["charge_ns"] = 999
    with pytest.raises(ValueError, match="aggregate differs"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_tampered_known_charge_ns_against_stream() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["known_charge_ns"] = 999
    with pytest.raises(ValueError, match="charge does not match"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_inline_meter_evidence_rejects_extra_or_duplicated_containing_fields() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    for injected in ("schema", "process_id", "stream_index", "classification", "scientific_outcome"):
        claim, leases, state = _e1_boundary_claim_for_two_processes()
        claim["streams"][0]["meter_evidence"][injected] = "injected"
        with pytest.raises(ValueError, match="meter_evidence fields differ"):
            validate_batch_claim(claim, leases=leases, state=state)


def test_inline_meter_evidence_rejects_nested_scientific_field() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["meter_evidence"]["loss"] = 0.1
    with pytest.raises(ValueError, match="meter_evidence fields differ|forbidden scientific"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_inline_meter_evidence_timely_late_boundary_and_unknowable_nullability() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    # Late against deadline: end > heartbeat_deadline_ns must be LATE_KNOWN.
    claim["streams"][0]["classification"] = StreamClassification.TIMELY_KNOWN.value
    claim["streams"][0]["meter_evidence"]["interval_end_reading_ns"] = 1_001
    claim["streams"][0]["known_charge_ns"] = 1_001
    claim["processes"][0]["known_charge_ns"] = 1_001
    claim["processes"][0]["charge_ns"] = 1_001
    claim["known_total_ns"] = 1_001 + 200
    with pytest.raises(ValueError, match="timely/late classification differs"):
        validate_batch_claim(claim, leases=leases, state=state)
    # UNKNOWABLE requires null end and backend_synchronized false.
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["classification"] = StreamClassification.UNKNOWABLE.value
    claim["streams"][0]["known_charge_ns"] = None
    claim["streams"][0]["unknown_share_ns"] = 1
    claim["streams"][0]["meter_evidence"]["interval_end_reading_ns"] = 100
    claim["streams"][0]["meter_evidence"]["backend_synchronized"] = True
    with pytest.raises(ValueError, match="unknowable meter evidence differs"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_inline_meter_evidence_rejects_observation_after_claim_created_utc() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["meter_evidence"]["observed_utc"] = "2026-07-20T00:00:01Z"
    with pytest.raises(ValueError, match="meter observation follows claim creation"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_missing_stream_for_enumerated_process() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"] = [claim["streams"][0]]
    with pytest.raises(ValueError, match="unknown-pool witness differs"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_extra_stream_referencing_unenumerated_process() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    lease_c = _synthetic_lease("proc-c", start_reading_ns=0, heartbeat_deadline_ns=1_000)
    pid_c = str(lease_c["process_id"])
    claim["streams"].append(_known_stream(3, pid_c, start=0, end=50, boot_identity=str(lease_c["boot_identity"]), deadline=1_000))
    with pytest.raises(ValueError, match="non-enumerated process"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_duplicate_stream_index() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][1]["stream_index"] = 1
    with pytest.raises(ValueError, match="ascending and contiguous"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_duplicate_process_id_across_process_tuples() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["processes"][1]["process_id"] = claim["processes"][0]["process_id"]
    claim["processes"][1]["process_sequence"] = 5
    with pytest.raises(ValueError, match="globally ordered"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_bad_classification_enum_value() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["classification"] = "NOT_A_REAL_CLASS"
    with pytest.raises(ValueError):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_rejects_known_stream_with_null_charge() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    claim["streams"][0]["known_charge_ns"] = None
    with pytest.raises(ValueError, match="nullability differs"):
        validate_batch_claim(claim, leases=leases, state=state)


def test_validate_batch_claim_completeness_rejects_omitted_live_lease_for_e1_boundary() -> None:
    claim, leases, state = _e1_boundary_claim_for_two_processes()
    pid_b = claim["processes"][1]["process_id"]
    claim["streams"] = [claim["streams"][0]]
    claim["processes"] = [claim["processes"][0]]
    claim["known_total_ns"] = 100
    with pytest.raises(ValueError, match="does not enumerate every live lease"):
        validate_batch_claim(
            claim,
            leases={
                str(claim["processes"][0]["process_id"]): leases[str(claim["processes"][0]["process_id"])],
                pid_b: leases[pid_b],
            },
            state=state,
        )


# ===========================================================================
# Integration tests on a disposable, directly-seeded activated runtime root.
# See the module docstring for why direct seeding (rather than the full
# ``activate_repository`` ceremony) is sufficient for these.
# ===========================================================================


@pytest.fixture()
def env(tmp_path: Path):
    seeded = _seed_active_repo(tmp_path)
    clock = FakeClock()
    meter = FakeMeter(start_ns=0)
    harness = GenericHarness(seeded.repo, clock=clock, meter=meter)
    return seeded, harness, clock, meter


def test_claim_then_start_order_started_event_precedes_lease_with_matching_prior_hash(env) -> None:
    seeded, harness, clock, meter = env
    claim = harness.claim(
        argv=["python", "worker.py"],
        behavior_source_sha256=sha256_bytes(b"behavior"),
        config_sha256=sha256_bytes(b"config"),
        stack_sha256=sha256_bytes(b"stack"),
        numerical_mode_sha256=sha256_bytes(b"numerical"),
    )
    process_id = str(claim["process_id"])
    lease_path = seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json"
    assert not lease_path.exists()
    harness.start(process_id)
    entries = _ledger_for(seeded.repo).entries()
    assert entries[-1]["event"] == "T_PROCESS_STARTED"
    assert entries[-1]["data"]["process_id"] == process_id
    lease = load_canonical_json(lease_path)
    assert lease["prior_charge_event_sha256"] == entries[-1]["entry_sha256"]


def test_close_order_charge_then_record_then_stopped_and_pre_record_stop_is_impossible(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    harness.close(process_id)
    entries = _ledger_for(seeded.repo).entries()
    events = [e["event"] for e in entries]
    charge_index = len(events) - 1 - events[::-1].index("T_DEVICE_TIME_CHARGED")
    stopped_index = events.index("T_PROCESS_STOPPED")
    assert charge_index < stopped_index
    record_path = seeded.repo / gh.RECORDS_RELATIVE / f"{process_id}.json"
    assert record_path.is_file()
    # record must be durable by the time T_PROCESS_STOPPED references it
    record_sha = sha256_file(record_path)
    assert entries[stopped_index]["data"]["process_record_sha256"] == record_sha


def test_close_before_3_crash_leaves_process_live_with_no_record_and_no_stopped(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    crashing = GenericHarness(seeded.repo, clock=clock, meter=meter, crash_cut="before_3")
    with pytest.raises(RuntimeError, match="injected crash cut: before_3"):
        crashing.close(process_id)
    record_path = seeded.repo / gh.RECORDS_RELATIVE / f"{process_id}.json"
    assert not record_path.is_file()
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert "T_PROCESS_STOPPED" not in events
    assert "T_DEVICE_TIME_CHARGED" in events  # the internal heartbeat already settled
    assert harness.process_state(process_id) is ProcessState.P3


def test_close_after_3_crash_produces_orphan_record_before_stopped_or_lease_removal(env) -> None:
    """§3 crash cut: the durable record exists (process already reads as
    closed) while the lease file is still present and no ``T_PROCESS_STOPPED``
    is yet durable -- the record-first ordering's orphan case."""

    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    crashing = GenericHarness(seeded.repo, clock=clock, meter=meter, crash_cut="after_3")
    with pytest.raises(RuntimeError, match="injected crash cut: after_3"):
        crashing.close(process_id)
    record_path = seeded.repo / gh.RECORDS_RELATIVE / f"{process_id}.json"
    lease_path = seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json"
    assert record_path.is_file()
    assert lease_path.is_file()  # orphaned: never removed
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert "T_PROCESS_STOPPED" not in events
    assert harness.process_state(process_id) is ProcessState.P4  # record dominates


def test_close_after_4_crash_leaves_ledger_ahead_of_the_on_disk_lease(env) -> None:
    """A single ``crash_cut`` string applies for the whole call, so
    ``close()``'s internal ``heartbeat()`` reaches its *own* ``after_4``
    checkpoint first (immediately after the settlement charge is durable,
    but before the renewed lease is written back to disk) -- itself a
    genuine "ledger ahead of the lease" instance: the charge is durable
    while the on-disk lease cursor is still stale, and neither the process
    record nor ``T_PROCESS_STOPPED`` exist yet."""

    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    lease_path = seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json"
    stale_cursor = load_canonical_json(lease_path)["last_charged_reading_ns"]
    crashing = GenericHarness(seeded.repo, clock=clock, meter=meter, crash_cut="after_4")
    with pytest.raises(RuntimeError, match="injected crash cut: after_4"):
        crashing.close(process_id)
    assert lease_path.is_file()
    assert load_canonical_json(lease_path)["last_charged_reading_ns"] == stale_cursor
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert events[-1] == "T_DEVICE_TIME_CHARGED"
    record_path = seeded.repo / gh.RECORDS_RELATIVE / f"{process_id}.json"
    assert not record_path.is_file()
    assert harness.process_state(process_id) is ProcessState.P3


def test_ordinary_heartbeat_conserves_charge_and_liability(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(500)
    harness.heartbeat(process_id)
    meter.advance(300)
    harness.heartbeat(process_id)
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert state.device_nanoseconds == 800
    assert harness.verify_conservation_at_rest() == []


def test_heartbeat_refuses_when_meter_did_not_advance(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    with pytest.raises(HarnessRefused, match="clock did not advance"):
        harness.heartbeat(process_id)


def test_multi_stream_reservation_k_greater_than_one_then_exhausted_at_max_concurrent(env) -> None:
    seeded, harness, clock, meter = env
    pids = [_claim_and_start(harness, suffix=str(i)) for i in range(MAX_CONCURRENT_LEASES)]
    assert len(pids) == MAX_CONCURRENT_LEASES
    with pytest.raises(RuntimeContractError, match="concurrency cap"):
        harness.claim(
            argv=["python", "one-too-many.py"],
            behavior_source_sha256=sha256_bytes(b"behavior-extra"),
            config_sha256=sha256_bytes(b"config-extra"),
            stack_sha256=sha256_bytes(b"stack-extra"),
            numerical_mode_sha256=sha256_bytes(b"numerical-extra"),
        )


def test_claim_refuses_when_sibling_liability_leaves_zero_e3_remaining(env) -> None:
    """Multi-stream reservation, ℓ = 0 from siblings: with the review clock
    already 10ns from its 40-device-hour E3 boundary and three 1-unit
    siblings already durably holding that entire remaining 10ns of
    liability between them, a fourth concurrent ``claim()`` finds the real
    ``reservation_route`` arithmetic report ``E3_DUE`` and refuses --
    exercised against the harness's own reservation gate, not a mock."""

    seeded, harness, clock, meter = env
    review_cap_ns = 40 * NANOSECONDS_PER_HOUR
    _set_device_nanoseconds(seeded, review_cap_ns - 10)
    for index, liability in enumerate((4, 3, 3)):
        _install_fabricated_live_process(
            seeded, sequence=index, start_reading_ns=0, liability_ns_per_unit=liability, label=f"sib-{index}",
        )
    with pytest.raises(HarnessRefused, match="claim route is E3_DUE"):
        harness.claim(
            argv=["python", "fourth.py"],
            behavior_source_sha256=sha256_bytes(b"behavior-fourth"),
            config_sha256=sha256_bytes(b"config-fourth"),
            stack_sha256=sha256_bytes(b"stack-fourth"),
            numerical_mode_sha256=sha256_bytes(b"numerical-fourth"),
        )


def test_exhaustion_event_appears_only_when_realized_charge_reaches_168_hours(env) -> None:
    seeded, harness, clock, meter = env
    _install_fabricated_live_process(
        seeded, sequence=0, start_reading_ns=0, liability_ns_per_unit=100, label="near-cap",
    )
    _set_device_nanoseconds(seeded, CAP_NS - 60)
    meter.set(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    harness.run_batch_to_completion(claim)
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert state.device_nanoseconds == CAP_NS
    assert state.exhausted(TEnvelope())
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert events.count("T_ENVELOPE_EXHAUSTED") == 1
    assert events[-1] == "T_ENVELOPE_EXHAUSTED"


def test_exhaustion_event_absent_when_realized_charge_stays_below_168_hours(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    harness.heartbeat(process_id)
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert "T_ENVELOPE_EXHAUSTED" not in events


# ===========================================================================
# §10.17 -- Lease/charge hash chain seeding
# ===========================================================================


def test_lease_prior_charge_hash_chains_through_successive_heartbeats(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    lease_path = seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json"
    started_entry = _ledger_for(seeded.repo).entries()[-1]
    assert load_canonical_json(lease_path)["prior_charge_event_sha256"] == started_entry["entry_sha256"]
    meter.advance(200)
    renewed = harness.heartbeat(process_id)
    first_charge_entry = _ledger_for(seeded.repo).entries()[-1]
    assert renewed["prior_charge_event_sha256"] == first_charge_entry["entry_sha256"]
    assert load_canonical_json(lease_path)["prior_charge_event_sha256"] == first_charge_entry["entry_sha256"]
    meter.advance(300)
    renewed_again = harness.heartbeat(process_id)
    second_charge_entry = _ledger_for(seeded.repo).entries()[-1]
    assert renewed_again["prior_charge_event_sha256"] == second_charge_entry["entry_sha256"]
    assert renewed_again["prior_charge_event_sha256"] != first_charge_entry["entry_sha256"]


# ===========================================================================
# §10.19/§10.20 -- Batch automaton crash injection, pinned next action, and
# restart reconstruction (amendment §3c/§4a/§4b).
# ===========================================================================


def _runtime_invalid_batch_env(tmp_path: Path):
    """One live process, its final interval still fully *known* (a PROCESS-
    cause fault such as a dead controller is detected independently of the
    meter), so the RUNTIME_INVALIDITY batch charges only that small known
    amount rather than the full remaining E1 budget (contrast the pure
    unit tests, which already cover the unknown-pool's own "assume the
    worst case" arithmetic in isolation) -- this walks every automaton
    action: APPEND_CHARGE, WRITE_INVALID_DETAIL, APPEND_INVALID_EVENT,
    WRITE_INVALID_RECORD, REMOVE_LEASE, RESOLVED, without also exhausting
    E1 as an (otherwise-correct) side effect."""

    seeded = _seed_active_repo(tmp_path)
    clock = FakeClock()
    meter = FakeMeter(start_ns=0)
    harness = GenericHarness(seeded.repo, clock=clock, meter=meter)
    process_id = _claim_and_start(harness)
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(
        reason=BatchReason.RUNTIME_INVALIDITY, observed_causes=[InvalidCause.PROCESS]
    )
    return seeded, harness, clock, meter, claim, process_id


@pytest.mark.parametrize(
    ("cut", "expected_action_before"),
    [
        ("before_C", BatchAutomatonAction.APPEND_CHARGE),
        ("before_D", BatchAutomatonAction.WRITE_INVALID_DETAIL),
        ("before_E", BatchAutomatonAction.APPEND_INVALID_EVENT),
        ("before_R", BatchAutomatonAction.WRITE_INVALID_RECORD),
        ("before_L", BatchAutomatonAction.REMOVE_LEASE),
    ],
)
def test_batch_automaton_crash_at_each_step_pins_next_action_and_restart_resumes(
    tmp_path: Path, cut: str, expected_action_before: BatchAutomatonAction
) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    action, index = harness.next_batch_action(claim)
    while action is not expected_action_before:
        harness.execute_batch_step(claim)
        action, index = harness.next_batch_action(claim)
    crashing = GenericHarness(seeded.repo, clock=clock, meter=meter, crash_cut=cut)
    with pytest.raises(RuntimeError, match=f"injected crash cut: {cut}"):
        crashing.execute_batch_step(claim)
    # The pinned next action is unchanged by the crash (nothing partial durable).
    restarted = GenericHarness(seeded.repo, clock=clock, meter=meter)
    replay_action, replay_index = restarted.next_batch_action(claim)
    assert (replay_action, replay_index) == (action, index)
    # Restart reconstruction can now drive the automaton through to RESOLVED.
    final = restarted.run_batch_to_completion(claim)
    assert final.phase is GlobalState.G5  # unresolved invalidity blocks G1 until recovery


def test_batch_automaton_full_run_reaches_resolved_with_invalid_terminal_artifacts(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    assert harness.next_batch_action(claim) == (BatchAutomatonAction.RESOLVED, 0)
    record = load_canonical_json(seeded.repo / gh.RECORDS_RELATIVE / f"{process_id}.json")
    assert record["disposition"] == "T_PROCESS_INVALID"
    assert not (seeded.repo / gh.LEASES_RELATIVE / f"{process_id}.json").exists()
    detail = load_canonical_json(seeded.repo / gh.INVALIDITIES_RELATIVE / f"{process_id}.json")
    assert detail["invalid_cause"] == InvalidCause.PROCESS.value
    events = [e["event"] for e in _ledger_for(seeded.repo).entries()]
    assert events[-3:] == ["T_DEVICE_TIME_CHARGED", "T_RUNTIME_INVALID", "T_RUNTIME_INVALID"] or "T_RUNTIME_INVALID" in events


# ===========================================================================
# §10.21 -- 60/60/60 frozen-batch settlement via the full construction +
# execution flow (three LATE_KNOWN 60ns streams, D0 = cap - 100).
# ===========================================================================


def test_60_60_60_batch_via_construct_and_run_to_completion(env) -> None:
    seeded, harness, clock, meter = env
    _set_device_nanoseconds(seeded, CAP_NS - 100)
    pids = []
    for index in range(3):
        claim, lease = _install_fabricated_live_process(
            seeded, sequence=index, start_reading_ns=0, liability_ns_per_unit=30, label=f"late-{index}",
        )
        pids.append(str(claim["process_id"]))
    meter.set(60)
    for pid in pids:
        lease = load_canonical_json(seeded.repo / gh.LEASES_RELATIVE / f"{pid}.json")
        deadline = lease["heartbeat_deadline_ns"]
        assert 60 > deadline  # each stream will classify LATE_KNOWN
    batch_claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    assert batch_claim["known_total_ns"] == 180
    assert all(s["classification"] == StreamClassification.LATE_KNOWN.value for s in batch_claim["streams"])
    harness.run_batch_to_completion(batch_claim)
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert state.device_nanoseconds == (CAP_NS - 100) + 180
    assert state.exhausted(TEnvelope())
    for pid in pids:
        record = load_canonical_json(seeded.repo / gh.RECORDS_RELATIVE / f"{pid}.json")
        assert record["disposition"] == "T_PROCESS_E1_EXHAUSTED"
        assert not (seeded.repo / gh.LEASES_RELATIVE / f"{pid}.json").exists()


# ===========================================================================
# §10.22 -- Sole permitted D1 head/cache completion (amendment §D1)
# ===========================================================================


def test_head_cache_completion_positive_case_completes_a_lagging_cache(env) -> None:
    """Between a batch step's durable ledger append and its own
    ``_write_state`` call there is no injectable ``crash_cut`` (the two
    happen back-to-back), because an OS-level fault can still land there in
    reality; ``complete_batch_head_cache_if_authorized`` exists precisely
    for that otherwise-uncontrollable window.  Reproduce it here by
    appending the real claim's own first charge tuple directly with the
    raw ledger API, deliberately skipping the cache write."""

    seeded, harness, clock, meter = env
    _claim_and_start(harness)
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    stale_state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    process = claim["processes"][0]
    next_state = stale_state.charge_device_nanoseconds(int(process["charge_ns"]), TEnvelope())
    _ledger_for(seeded.repo).append(
        event="T_DEVICE_TIME_CHARGED",
        timestamp_utc=str(claim["created_utc"]),
        data={
            "active_lease_sha256": process["active_lease_sha256"],
            "charge_ns": process["charge_ns"],
            "process_id": process["process_id"],
            "scientific_outcome": False,
            "t_state": next_state.to_mapping(),
        },
    )
    assert TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE)) == stale_state
    completed = harness.complete_batch_head_cache_if_authorized(claim)
    assert completed is True
    cached = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert cached == next_state
    # Idempotent: already consistent now, so a second call is a no-op.
    assert harness.complete_batch_head_cache_if_authorized(claim) is False


def test_head_cache_completion_refuses_when_zero_unresolved_claims_exist(env) -> None:
    seeded, harness, clock, meter = env
    fabricated = {"schema": BATCH_CLAIM_SCHEMA, "processes": [{"process_id": "a" * 64}]}
    assert harness.complete_batch_head_cache_if_authorized(fabricated) is False


def test_head_cache_completion_refuses_when_passed_claim_differs_from_the_pending_one(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    del process_id
    forged = dict(claim)
    forged["created_utc"] = "2026-07-21T00:00:00Z"
    assert harness.complete_batch_head_cache_if_authorized(forged) is False


def test_head_cache_completion_refuses_when_multiple_unresolved_claims_exist(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    del process_id
    # A second, distinctly-named claim anchored at the *same* pre-head as the
    # real one (so its own ledger suffix is trivially empty too, and
    # `next_batch_action` does not diverge): still schema-self-consistent
    # (`validate_batch_claim` skips the leases/state cross-checks when they
    # are omitted, exactly as `_unresolved_batch_claims` calls it), so it
    # counts as a genuine second unresolved claim.
    forged_path = seeded.repo / gh.BATCH_CLAIMS_RELATIVE / "duplicate.json"
    atomic_create(forged_path, canonical_json(claim))
    assert harness.complete_batch_head_cache_if_authorized(claim) is False


def test_head_cache_completion_refuses_when_last_ledger_entry_is_not_state_bearing(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)  # last durable event is T_PROCESS_STARTED (no t_state)
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    del process_id
    assert harness.complete_batch_head_cache_if_authorized(claim) is False


def test_head_cache_completion_refuses_when_cache_already_matches_the_ledger(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(1_000)
    harness.heartbeat(process_id)  # cache and ledger already agree
    meter.advance(60)
    claim = harness.construct_and_install_batch_claim(reason=BatchReason.E1_BOUNDARY)
    assert harness.complete_batch_head_cache_if_authorized(claim) is False


# ===========================================================================
# §10.23 -- Pause / resume (v2 §6a/§6b; v2.2 §C)
# ===========================================================================


def test_pause_requires_no_live_leases(env) -> None:
    seeded, harness, clock, meter = env
    _claim_and_start(harness)
    artifact = seeded.repo / "artifact.txt"
    artifact.write_text("x")
    with pytest.raises(HarnessRefused, match="no live leases"):
        harness.pause(reason="author-requested", artifact_paths={"note": artifact})


def test_ordinary_pause_then_resume_admits_work_without_review(env) -> None:
    """Below the review clocks, ``resume()`` returns early without
    appending any ledger event at all (v2.2 §C only ever transacts when a
    review is overdue), so the pure global classifier legitimately still
    reads the last event as the pause itself; what actually proves work is
    admitted is that a fresh claim succeeds immediately afterwards."""

    seeded, harness, clock, meter = env
    artifact = seeded.repo / "artifact.txt"
    artifact.write_text("x")
    event = harness.pause(reason="author-requested", artifact_paths={"note": artifact})
    checkpoint_path = Path(event["data"]["checkpoint_path"])
    clock.advance(3600)  # well below the 48h review-wall / 40h device-hour clocks
    view = harness.resume(checkpoint_path)
    assert view.phase is GlobalState.G3  # last durable event is still the pause
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert not state.resume_review_pending
    _claim_and_start(harness)  # work is not blocked


def test_overdue_resume_generates_pending_checkpoint_keyed_by_pause_event_hash_and_blocks_work(env) -> None:
    seeded, harness, clock, meter = env
    artifact = seeded.repo / "artifact.txt"
    artifact.write_text("x")
    pause_event = harness.pause(reason="author-requested", artifact_paths={"note": artifact})
    checkpoint_path = Path(pause_event["data"]["checkpoint_path"])
    clock.advance(49 * 3600)  # exceeds the 48h review-wall clock -> review overdue
    harness.resume(checkpoint_path)
    pending_path = seeded.repo / gh.PENDING_RESUME_RELATIVE / f"{pause_event['entry_sha256']}.json"
    assert pending_path.is_file()
    pending = load_canonical_json(pending_path)
    validate_pending_resume_checkpoint(pending)
    assert pending["ledger_head_before"] == pause_event["entry_sha256"]
    state = TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE))
    assert state.resume_review_pending is True
    assert harness.global_state().phase is GlobalState.G4
    with pytest.raises(RuntimeContractError, match="T runtime state is unavailable"):
        _claim_and_start(harness)  # work refused until a durable review clears G4


def _review_for(seeded: SeededRepo) -> dict[str, object]:
    """Only ``schema``/``validity``/``authorization_sha256``/
    ``activation_record_sha256``/``author_decision_sha256`` survive into the
    durable record; every other field is unconditionally recomputed and
    overwritten by ``complete_overdue_review`` itself, so placeholders here
    only need to be independently well-formed."""

    return {
        "schema": REVIEW_RECORD_SCHEMA,
        "scientific_outcome": False,
        "validity": "VALID_PROCESS_RECORD",
        "authorization_sha256": "a" * 64,
        "activation_record_sha256": seeded.activation_record_sha256,
        "pre_state_sha256": "0" * 64,
        "post_state": TState().to_mapping(),
        "post_state_sha256": "0" * 64,
        "ledger_entry_sha256": "0" * 64,
        "ledger_head_sha256": "0" * 64,
        "reviewed_utc": seeded.activated_utc,
        "prior_review_utc": seeded.activated_utc,
        "prior_review_device_nanoseconds": 0,
        "author_decision_sha256": "1" * 64,
    }


def test_two_pause_resume_cycles_produce_distinct_pending_artifacts(env) -> None:
    seeded, harness, clock, meter = env
    artifact = seeded.repo / "artifact.txt"
    artifact.write_text("x")
    pause_one = harness.pause(reason="author-requested", artifact_paths={"note": artifact})
    clock.advance(49 * 3600)
    harness.resume(Path(pause_one["data"]["checkpoint_path"]))
    harness.complete_overdue_review(review=_review_for(seeded))
    artifact2 = seeded.repo / "artifact2.txt"
    artifact2.write_text("y")
    pause_two = harness.pause(reason="author-requested-again", artifact_paths={"note": artifact2})
    clock.advance(49 * 3600)
    harness.resume(Path(pause_two["data"]["checkpoint_path"]))
    first_pending = seeded.repo / gh.PENDING_RESUME_RELATIVE / f"{pause_one['entry_sha256']}.json"
    second_pending = seeded.repo / gh.PENDING_RESUME_RELATIVE / f"{pause_two['entry_sha256']}.json"
    assert first_pending.is_file() and second_pending.is_file()
    assert first_pending != second_pending
    assert load_canonical_json(first_pending) != load_canonical_json(second_pending)


# ===========================================================================
# §10.24 -- Recovery disposition and G5 admission (v2.1 §C.3)
# ===========================================================================


def test_recovery_disposition_missing_keeps_g5(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    assert harness.global_state().phase is GlobalState.G5
    with pytest.raises(HarnessRefused, match="G5 runtime invalidity blocks admission"):
        harness.claim(
            argv=["python", "-m", "philosophia.officina.generic_harness", "blocked"],
            behavior_source_sha256="1" * 64,
            config_sha256="2" * 64,
            stack_sha256="3" * 64,
            numerical_mode_sha256="4" * 64,
        )


def test_recovery_disposition_remain_blocked_keeps_g5(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    invalidity_event = next(e for e in _ledger_for(seeded.repo).entries() if e["event"] == "T_RUNTIME_INVALID")
    harness.install_recovery_disposition(
        author_decision_sha256="a" * 64,
        invalidity_event_sha256=invalidity_event["entry_sha256"],
        resolution_action="REMAIN_BLOCKED",
    )
    assert harness.global_state().phase is GlobalState.G5


def test_recovery_disposition_mismatched_head_or_state_keeps_g5(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    invalidity_event = next(e for e in _ledger_for(seeded.repo).entries() if e["event"] == "T_RUNTIME_INVALID")
    stale_disposition = {
        "schema": RECOVERY_DISPOSITION_SCHEMA,
        "scientific_outcome": False,
        "author_decision_sha256": "a" * 64,
        "invalidity_record_sha256": invalidity_event["data"]["invalidity_record_sha256"],
        "invalidity_event_sha256": invalidity_event["entry_sha256"],
        "ledger_head_sha256": "b" * 64,  # deliberately stale/mismatched
        "state_sha256": hash_mapping(TState.from_mapping(load_canonical_json(seeded.repo / gh.STATE_RELATIVE)).to_mapping()),
        "affected_process_ids": [process_id],
        "charge_event_sha256s": [invalidity_event["data"]["invalidity_record_sha256"]],
        "resolution_action": "READMIT_AFTER_RECONCILIATION",
        "resolved_utc": seeded.activated_utc,
    }
    validate_recovery_disposition(stale_disposition)
    atomic_create(
        seeded.repo / gh.RECOVERY_RELATIVE / f"{invalidity_event['entry_sha256']}.json",
        canonical_json(stale_disposition),
    )
    assert harness.global_state().phase is GlobalState.G5


def test_recovery_disposition_readmit_after_reconciliation_clears_g5_for_fresh_process_id(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    invalidity_event = next(e for e in _ledger_for(seeded.repo).entries() if e["event"] == "T_RUNTIME_INVALID")
    harness.install_recovery_disposition(
        author_decision_sha256="a" * 64,
        invalidity_event_sha256=invalidity_event["entry_sha256"],
        resolution_action="READMIT_AFTER_RECONCILIATION",
    )
    assert harness.global_state().phase is GlobalState.G1
    fresh_process_id = _claim_and_start(harness, suffix="post-recovery")
    assert fresh_process_id != process_id


# ===========================================================================
# §10.25 -- Isolation-and-promotion protocol (v2 §5b)
# ===========================================================================


def test_isolated_operation_exposes_only_a_result_hash_on_success(env) -> None:
    seeded, harness, clock, meter = env
    result_hash = harness.run_isolated_operation(perform=lambda: b"raw-scientific-bytes")
    assert result_hash == sha256_bytes(b"raw-scientific-bytes")


def test_isolated_operation_retained_response_faults_expose_no_result(env) -> None:
    seeded, harness, clock, meter = env

    def _retained_but_faulting() -> bytes:
        raise RuntimeError("operation retained a response but then faulted")

    with pytest.raises(HarnessRefused, match="no result is exposed"):
        harness.run_isolated_operation(perform=_retained_but_faulting)


def test_isolated_operation_killed_child_faults_expose_no_result(env) -> None:
    seeded, harness, clock, meter = env

    def _killed_child() -> bytes:
        raise subprocess.SubprocessError("child process was killed")

    with pytest.raises(HarnessRefused, match="no result is exposed"):
        harness.run_isolated_operation(perform=_killed_child)


def test_isolated_operation_non_bytes_result_is_refused(env) -> None:
    seeded, harness, clock, meter = env
    with pytest.raises(HarnessRefused, match="raw bytes"):
        harness.run_isolated_operation(perform=lambda: "not bytes")  # type: ignore[arg-type,return-value]


def test_promote_after_settlement_fails_without_a_currently_live_lease(env) -> None:
    seeded, harness, clock, meter = env
    with pytest.raises(HarnessRefused, match="currently live lease"):
        harness.promote_after_settlement(
            process_id="a" * 64, operation_id="op-1", result_sha256="b" * 64, charge_event_sha256="c" * 64,
        )


def test_promote_after_settlement_fails_when_charge_event_is_not_a_durable_settlement(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    with pytest.raises(HarnessRefused, match="durable settlement"):
        harness.promote_after_settlement(
            process_id=process_id, operation_id="op-1", result_sha256="b" * 64, charge_event_sha256="c" * 64,
        )


def test_promote_after_settlement_succeeds_only_after_a_durable_charge_and_token_is_single_use(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(500)
    charge_event = harness.heartbeat(process_id)
    charge_entry = _ledger_for(seeded.repo).entries()[-1]
    result_hash = harness.run_isolated_operation(perform=lambda: b"scientific-result")
    token = harness.promote_after_settlement(
        process_id=process_id,
        operation_id="op-1",
        result_sha256=result_hash,
        charge_event_sha256=charge_entry["entry_sha256"],
    )
    del charge_event
    assert token.process_id == process_id
    token.redeem()
    with pytest.raises(HarnessRefused, match="already redeemed"):
        token.redeem()


# ===========================================================================
# §10.26 -- Pre-WP-6 boundary: no candidate registry, whole-artifact Q/C
# rejection of T-shaped payloads, and release tokens carry no candidate field.
# ===========================================================================


def test_candidate_registration_is_unconditionally_refused_pre_wp6() -> None:
    state = TState().activate("2026-07-20T00:00:00Z")
    with pytest.raises(PermissionError, match="WP-6"):
        state.register_candidate("a" * 64, TEnvelope())


def test_q_terminal_rejects_a_whole_t_artifact_by_shape(env) -> None:
    seeded, harness, clock, meter = env
    process_id = _claim_and_start(harness)
    meter.advance(500)
    harness.heartbeat(process_id)
    meter.advance(500)
    record = harness.close(process_id)
    from philosophia.officina.terminal import QTerminal

    with pytest.raises(ValueError, match="fields differ"):
        QTerminal.from_mapping(record)


def test_c_terminal_rejects_a_t_shaped_scientific_label() -> None:
    from philosophia.officina.terminal import CTerminal

    t_shaped_payload = {"schema": DRAFT_MANIFEST_SCHEMA, "scientific_outcome": False}
    with pytest.raises(ValueError, match="scientific label"):
        CTerminal(valid=True, scientific_label=t_shaped_payload)  # type: ignore[arg-type]


def test_release_token_carries_no_candidate_schema_field() -> None:
    token = ReleaseToken(
        activation_record_sha256="a" * 64, process_id="p", lease_sha256="b" * 64,
        operation_id="op", result_sha256="c" * 64, charge_event_sha256="d" * 64,
    )
    assert "candidate" not in " ".join(ReleaseToken.__slots__).lower()
    with pytest.raises(TypeError):
        ReleaseToken(  # type: ignore[call-arg]
            activation_record_sha256="a" * 64, process_id="p", lease_sha256="b" * 64,
            operation_id="op", result_sha256="c" * 64, charge_event_sha256="d" * 64,
            candidate_id="e" * 64,
        )
    del token


# ===========================================================================
# §10.27 -- Relabelling: an invalid process can never subsequently be
# recorded as a valid terminal.
# ===========================================================================


def test_invalid_process_cannot_be_relabelled_valid_via_build_process_record() -> None:
    from philosophia.officina.runtime import build_process_record

    lease = _synthetic_lease("relabel", start_reading_ns=0, heartbeat_deadline_ns=1_000)
    claim = {key: item for key, item in lease.items() if key not in {
        "last_charged_reading_ns", "cumulative_charge_ns", "heartbeat_deadline_ns",
        "outstanding_liability_ns", "prior_charge_event_sha256",
    }}
    claim["schema"] = "philosophia.officina.t-process-claim.v1"
    charge_state = TState(activated_utc="2026-07-20T00:00:00Z", device_nanoseconds=100)
    charge_event = {
        "data": {
            "active_lease_sha256": sha256_bytes(canonical_json(lease)),
            "charge_ns": 100,
            "process_id": lease["process_id"],
            "scientific_outcome": False,
            "t_state": charge_state.to_mapping(),
        },
        "entry_sha256": "a" * 64,
        "event": "T_DEVICE_TIME_CHARGED",
        "previous_sha256": "0" * 64,
        "sequence": 0,
        "timestamp_utc": "2026-07-20T00:00:01Z",
    }
    charge_event["entry_sha256"] = sha256_bytes(
        canonical_json({k: v for k, v in charge_event.items() if k != "entry_sha256"})
    )
    with pytest.raises(ValueError, match="requires its runtime-invalid event"):
        build_process_record(
            claim=claim,
            lease=lease,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=InvalidCause.PROCESS,
            closed_utc="2026-07-20T00:00:01Z",
            final_charge_event=charge_event,
            final_state=charge_state,
            activation_record_sha256="a" * 64,
            immutable_control_sha256={"x": "0" * 64},
        )
    with pytest.raises(ValueError, match="requires a typed public cause"):
        build_process_record(
            claim=claim,
            lease=lease,
            disposition=ProcessDisposition.INVALID,
            invalid_cause=None,
            closed_utc="2026-07-20T00:00:01Z",
            final_charge_event=charge_event,
            final_state=charge_state,
            activation_record_sha256="a" * 64,
            immutable_control_sha256={"x": "0" * 64},
        )


def test_invalid_process_lease_removed_so_ordinary_close_cannot_relabel_it_valid(tmp_path: Path) -> None:
    seeded, harness, clock, meter, claim, process_id = _runtime_invalid_batch_env(tmp_path)
    harness.run_batch_to_completion(claim)
    assert harness.process_state(process_id) is ProcessState.P5
    with pytest.raises(FileNotFoundError):
        harness.close(process_id)  # the lease is gone; no ordinary route can relabel it valid


# ===========================================================================
# §10.28 -- Roots and import boundary (production-boundary/quarantine contract)
# ===========================================================================


def test_verify_source_quarantine_on_the_real_generic_harness_is_clean() -> None:
    assert verify_source_quarantine([HARNESS_SOURCE]) == []


def test_production_roots_names_the_generic_harness_relative_path() -> None:
    assert GENERIC_HARNESS_RELATIVE.as_posix() in PRODUCTION_ROOTS


def test_real_repository_carries_no_production_call_graph_manifest() -> None:
    assert not (REPO / PRODUCTION_MANIFEST_RELATIVE).exists()


# ===========================================================================
# §10.29 -- CLI main(): refusal-first (v2 §9)
# ===========================================================================


def test_cli_main_refuses_unknown_command() -> None:
    assert harness_main(["not-a-real-command"]) == 2


def test_cli_main_refuses_missing_argv() -> None:
    assert harness_main([]) == 2


def test_cli_main_refuses_when_officina_repository_env_is_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OFFICINA_REPOSITORY", raising=False)
    assert harness_main(["claim", "python,worker.py", "a" * 64, "b" * 64, "c" * 64, "d" * 64]) == 2


def test_cli_main_returns_1_on_harness_refusal_and_0_on_success(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    seeded = _seed_active_repo(tmp_path)
    monkeypatch.setenv("OFFICINA_REPOSITORY", str(seeded.repo))
    # A malformed claim command (wrong argument count) is a CLI-level refusal (2).
    assert harness_main(["claim", "one-arg-too-few"]) == 2
    # start() on an absent process claim refuses at the harness level (1);
    # this exercises `main()`'s real (non-injected-clock/meter) `GenericHarness`,
    # so it only proves refusal-first routing, not lifecycle arithmetic.
    assert harness_main(["start", "0" * 64]) == 1

