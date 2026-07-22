"""Fail-closed Officina T activation transaction.

The real repository cannot pass this module's preflight until a separately
reviewed generic metered harness and exact authorization are committed.  Tests
may exercise the transaction only in disposable git mirrors.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
from typing import Mapping

from .accounting import TState
from .canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
    sha256_file,
)
from .ledger import AppendOnlyLedger, GENESIS, HEADER, HEAD_SCHEMA
from .runtime import (
    INVALIDITY_SCHEMA,
    RUNTIME_LOCK_RELATIVE,
    RuntimeLock,
    validate_active_lease,
    validate_ledger_event,
    validate_process_claim_against_activation,
    verify_hash_map,
    verify_runtime_lock,
)
from .verification import verify_bootstrap, verify_production_boundary


AUTHORIZATION_SCHEMA = "philosophia.officina.t-activation-authorization.v1"
CLAIM_SCHEMA = "philosophia.officina.t-activation-claim.v1"
ACTIVE_ENVELOPE_SCHEMA = "philosophia.officina.t-envelope-active.v1"
RECORD_SCHEMA = "philosophia.officina.t-activation-record.v1"
ACTIVATION_TOKEN = "I_AUTHORIZE_OFFICINA_T_ACTIVATION"

AUTHORIZATION_RELATIVE = Path(
    "successor/officina/OFFICINA_T_ACTIVATION_AUTHORIZATION.json"
)
ENVELOPE_RELATIVE = Path("successor/officina/T_ENVELOPE.json")
LEDGER_RELATIVE = Path("successor/officina/T_LEDGER.md")
LEDGER_HEAD_RELATIVE = Path("successor/officina/T_LEDGER.md.head.json")
RUNTIME_ROOT_RELATIVE = Path("successor/officina/runtime")
STATE_RELATIVE = RUNTIME_ROOT_RELATIVE / "T_STATE.json"
CLAIM_RELATIVE = RUNTIME_ROOT_RELATIVE / "T_ACTIVATION_CLAIM.json"
RECORD_RELATIVE = RUNTIME_ROOT_RELATIVE / "T_ACTIVATION_RECORD.json"
INVALIDITY_RELATIVE = RUNTIME_ROOT_RELATIVE / "T_TRANSACTION_INVALIDITY_REQUIRED.json"
GENERIC_HARNESS_RELATIVE = Path("src/philosophia/officina/generic_harness.py")
PRODUCTION_MANIFEST_RELATIVE = Path(
    "successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json"
)

GOVERNING_PATHS = (
    "successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md",
    "successor/OFFICINA_WP3_SIGNATURE.md",
    "successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md",
    "successor/OFFICINA_WP4_IMPLEMENTATION.md",
    "reviews/sol_officina_wp4_anchor_confirmation.md",
    "reviews/opus_officina_wp4_anchor_confirmation.md",
)
PROTOCOL_PATHS = (
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V1_DRAFT.md",
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md",
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_1_CORRECTION.md",
    "reviews/opus_officina_t_activation_protocol_v2_1_final_confirmation.md",
    "reviews/sol_officina_t_activation_protocol_v2_1_final_confirmation.md",
)
GOVERNING_SHA256 = {
    "successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md": (
        "aacea407e7cb436ac2092ddb8424a2ceab94e5fb67e3d164fea2511b23ede203"
    ),
    "successor/OFFICINA_WP3_SIGNATURE.md": (
        "24fd12b61d2fb75c38adee4bebda498f6ca67aade5e08b412c39530289086781"
    ),
    "successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md": (
        "6085d9b695e2a74c0b46c56bc61971d29dd6b646a5ae70068e33c93090735c7d"
    ),
    "successor/OFFICINA_WP4_IMPLEMENTATION.md": (
        "8d27c338fc562b45bfc3179909c6d8609ff5ada1e378a04936f1e48afe530d14"
    ),
    "reviews/sol_officina_wp4_anchor_confirmation.md": (
        "42b46cdb5cbd6f9a8ade99dcce165716fb87ac9488b0cb094f6e306597175804"
    ),
    "reviews/opus_officina_wp4_anchor_confirmation.md": (
        "fd25a6fc3af306def242df4c1077c5eb2d75d9218b78f0c02e66d8dba23d79a2"
    ),
}
PROTOCOL_SHA256 = {
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V1_DRAFT.md": (
        "aa0cb7574d549b359bec8e71bcf75b696e74f6e4de819e16f33a010a8adf2e8f"
    ),
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md": (
        "cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c"
    ),
    "successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_1_CORRECTION.md": (
        "2f9b1d474859abeb88efa528c9ad4129d9e787abaa574cce96cd056089fd4dc0"
    ),
    "reviews/opus_officina_t_activation_protocol_v2_1_final_confirmation.md": (
        "2dd8cdaaf807642bfc56272b9cfb41beb6791c25e2a7197d1e34276a16ffcc2d"
    ),
    "reviews/sol_officina_t_activation_protocol_v2_1_final_confirmation.md": (
        "125fea03d70d8706745514821d5c889e58d1091de4127e08cf71b26bf265df5c"
    ),
}
ENVELOPE_TOKEN = "I_SELECT_T_ENVELOPE_ONE_WEEK"
DEVICE_POLICY_TOKEN = "I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK"

IMMUTABLE_CONTROL_PATHS = (
    "scripts/officina_activate_t.py",
    "scripts/verify_officina_active.py",
    "src/philosophia/officina/activation.py",
    "src/philosophia/officina/runtime.py",
    "src/philosophia/officina/interlock.py",
    "src/philosophia/officina/world.py",
    "src/philosophia/officina/accounting.py",
    "src/philosophia/officina/ledger.py",
    "src/philosophia/officina/checkpoint.py",
    "src/philosophia/officina/terminal.py",
    "src/philosophia/officina/canonical.py",
    "src/philosophia/officina/verification.py",
)
REQUIRED_IMMUTABLE_CONTROL_PATHS = (
    *IMMUTABLE_CONTROL_PATHS,
    GENERIC_HARNESS_RELATIVE.as_posix(),
    PRODUCTION_MANIFEST_RELATIVE.as_posix(),
)
ACTIVATION_STAGE_PATHS = (
    CLAIM_RELATIVE.as_posix(),
    STATE_RELATIVE.as_posix(),
    RECORD_RELATIVE.as_posix(),
    ENVELOPE_RELATIVE.as_posix(),
    LEDGER_RELATIVE.as_posix(),
    LEDGER_HEAD_RELATIVE.as_posix(),
)
ACTIVATION_COMMIT_TRAILERS = (
    "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>",
    "Co-Authored-By: GPT-5.6 Sol <noreply@openai.com>",
    "Co-Authored-By: Codex GPT-5.5 <noreply@openai.com>",
)
STATE_BEARING_EVENTS = frozenset(
    {
        "T_ACTIVATED",
        "T_DEVICE_TIME_CHARGED",
        "T_REVIEW_COMPLETED",
        "T_OPERATIONAL_PAUSE",
        "T_PROCESS_STOPPED",
        "T_RUNTIME_INVALID",
        "T_AUTHOR_STOP",
        "T_ENVELOPE_EXHAUSTED",
    }
)

_AUTHORIZATION_KEYS = {
    "schema", "scientific_outcome", "execution_once", "token",
    "reviewed_code_head", "reviewed_source_paths", "reviewed_source_sha256",
    "governing_sha256", "protocol_sha256", "envelope_token",
    "device_policy_token", "canonical_paths", "command",
}
_CLAIM_KEYS = {
    "schema", "scientific_outcome", "authorization_sha256",
    "reviewed_code_head", "reviewed_source_sha256", "governing_sha256",
    "protocol_sha256", "created_utc", "canonical_paths", "pre_state_sha256",
    "planned_event", "planned_t_state_sha256",
}
_RECORD_KEYS = {
    "schema", "scientific_outcome", "validity", "authorization_sha256",
    "claim_sha256", "reviewed_code_head", "reviewed_source_sha256",
    "governing_sha256", "protocol_sha256", "created_utc", "t_state_sha256",
    "active_envelope_sha256", "ledger_entry_sha256", "ledger_head_sha256",
    "immutable_control_sha256",
}
_HEX40 = re.compile(r"[0-9a-f]{40}")
_HEX64 = re.compile(r"[0-9a-f]{64}")


class ActivationRefused(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def canonical_paths(repo: Path) -> dict[str, str]:
    root = repo.resolve(strict=True)
    return {
        "claim": str((root / CLAIM_RELATIVE).resolve()),
        "envelope": str((root / ENVELOPE_RELATIVE).resolve()),
        "ledger": str((root / LEDGER_RELATIVE).resolve()),
        "ledger_head": str((root / LEDGER_HEAD_RELATIVE).resolve()),
        "record": str((root / RECORD_RELATIVE).resolve()),
        "runtime_lock": str((root / RUNTIME_LOCK_RELATIVE).resolve()),
        "runtime_root": str((root / RUNTIME_ROOT_RELATIVE).resolve()),
        "state": str((root / STATE_RELATIVE).resolve()),
    }


def _git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=repo, check=check, capture_output=True, text=True
    )


def _validate_hash_map(value: object, name: str) -> dict[str, str]:
    if not isinstance(value, dict) or not value:
        raise ValueError(f"{name} must be a nonempty hash map")
    result: dict[str, str] = {}
    for key, digest in value.items():
        if not isinstance(key, str) or not key or not isinstance(digest, str):
            raise ValueError(f"{name} entries are malformed")
        if _HEX64.fullmatch(digest) is None:
            raise ValueError(f"{name} contains a non-SHA-256 value")
        result[key] = digest
    return result


def validate_authorization(value: object, *, repo: Path) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != _AUTHORIZATION_KEYS:
        raise ValueError("T activation authorization fields differ")
    if value["schema"] != AUTHORIZATION_SCHEMA:
        raise ValueError("T activation authorization schema differs")
    if value["scientific_outcome"] is not False or value["execution_once"] is not True:
        raise ValueError("T activation authorization flags differ")
    if value["token"] != ACTIVATION_TOKEN:
        raise ValueError("T activation token is absent")
    if not isinstance(value["reviewed_code_head"], str) or _HEX40.fullmatch(
        value["reviewed_code_head"]
    ) is None:
        raise ValueError("reviewed code HEAD is malformed")
    paths = value["reviewed_source_paths"]
    if not isinstance(paths, list) or not paths or not all(
        isinstance(item, str) and item for item in paths
    ) or len(paths) != len(set(paths)):
        raise ValueError("reviewed source paths are malformed")
    source_hashes = _validate_hash_map(value["reviewed_source_sha256"], "reviewed source")
    if set(paths) != set(source_hashes):
        raise ValueError("reviewed source paths and hashes differ")
    missing_control = set(REQUIRED_IMMUTABLE_CONTROL_PATHS) - set(paths)
    if missing_control:
        raise ValueError(f"immutable runtime controls are unreviewed: {sorted(missing_control)}")
    if GENERIC_HARNESS_RELATIVE.as_posix() not in paths:
        raise ActivationRefused("generic metered harness has not received review")
    governing = _validate_hash_map(value["governing_sha256"], "governing")
    protocol = _validate_hash_map(value["protocol_sha256"], "protocol")
    if set(governing) != set(GOVERNING_PATHS):
        raise ValueError("governing path set differs from the signed six pins")
    if set(protocol) != set(PROTOCOL_PATHS):
        raise ValueError("protocol path set differs from the accepted chain")
    if canonical_json(governing) != canonical_json(GOVERNING_SHA256):
        raise ValueError("governing hashes differ from the signed six pins")
    if canonical_json(protocol) != canonical_json(PROTOCOL_SHA256):
        raise ValueError("protocol hashes differ from the accepted chain")
    if value["canonical_paths"] != canonical_paths(repo):
        raise ValueError("authorization canonical paths differ")
    if value["command"] != (
        ".venv/bin/python scripts/officina_activate_t.py "
        "--authorization successor/officina/OFFICINA_T_ACTIVATION_AUTHORIZATION.json"
    ):
        raise ValueError("activation command differs")
    if value["envelope_token"] != ENVELOPE_TOKEN:
        raise ValueError("signed T envelope token differs")
    if value["device_policy_token"] != DEVICE_POLICY_TOKEN:
        raise ValueError("signed device policy token differs")
    return dict(value)


def _active_envelope(inactive: Mapping[str, object], timestamp: str) -> dict[str, object]:
    expected = {
        "activated", "candidate_registration_cap", "checkpoint_device_hours",
        "checkpoint_elapsed_calendar_hours", "device_hour_cap",
        "device_hours_are_aggregate", "ledger", "schema",
        "scientific_outcome", "strict_s_available",
    }
    if set(inactive) != expected or inactive["activated"] is not False:
        raise ValueError("inactive T envelope differs")
    return {
        **dict(inactive),
        "activated": True,
        "activated_utc": timestamp,
        "schema": ACTIVE_ENVELOPE_SCHEMA,
    }


def _preflight_git(repo: Path, authorization: Mapping[str, object]) -> str:
    root = Path(_git(repo, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if root != repo.resolve(strict=True):
        raise ActivationRefused("activation driver repository root differs")
    head = _git(repo, "rev-parse", "HEAD").stdout.strip()
    authorization_commit = _git(
        repo, "log", "-1", "--format=%H", "--", AUTHORIZATION_RELATIVE.as_posix()
    ).stdout.strip()
    if authorization_commit != head:
        raise ActivationRefused("activation authorization commit must be current HEAD")
    reviewed = str(authorization["reviewed_code_head"])
    if _git(repo, "cat-file", "-e", f"{reviewed}^{{commit}}", check=False).returncode:
        raise ActivationRefused("reviewed code HEAD is not a local commit")
    paths = tuple(str(item) for item in authorization["reviewed_source_paths"])
    if _git(repo, "diff", "--quiet", reviewed, head, "--", *paths, check=False).returncode:
        raise ActivationRefused("reviewed source bytes differ from reviewed code HEAD")
    if _git(repo, "diff", "--quiet", check=False).returncode != 0:
        raise ActivationRefused("tracked worktree must be clean before activation")
    if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise ActivationRefused("git index must be empty before activation")
    auth_relative = AUTHORIZATION_RELATIVE.as_posix()
    tracked = _git(repo, "ls-files", "--error-unmatch", auth_relative, check=False)
    if tracked.returncode != 0:
        raise ActivationRefused("activation authorization must be tracked")
    for relative in (
        *tuple(str(item) for item in authorization["reviewed_source_paths"]),
        *GOVERNING_PATHS,
        *PROTOCOL_PATHS,
    ):
        path = repo / relative
        if (
            _git(repo, "ls-files", "--error-unmatch", relative, check=False).returncode
            or not path.is_file()
            or path.is_symlink()
            or path.stat(follow_symlinks=False).st_nlink != 1
            or not path.resolve(strict=True).is_relative_to(repo)
        ):
            raise ActivationRefused(f"activation pinned path is untracked or aliased: {relative}")
    reviewed_commit_paths = tuple(
        dict.fromkeys(
            (
                *tuple(
                    str(item) for item in authorization["reviewed_source_paths"]
                ),
                *GOVERNING_PATHS,
                *PROTOCOL_PATHS,
            )
        )
    )
    for relative in reviewed_commit_paths:
        if _git(
            repo,
            "cat-file",
            "-e",
            f"{reviewed}:{relative}",
            check=False,
        ).returncode:
            raise ActivationRefused(f"pinned path is absent at reviewed HEAD: {relative}")
    return head


def activation_preflight(repo: Path, authorization_path: Path) -> dict[str, object]:
    repo = repo.resolve(strict=True)
    if authorization_path.resolve(strict=True) != (repo / AUTHORIZATION_RELATIVE).resolve():
        raise ActivationRefused("activation authorization path differs")
    authorization = validate_authorization(
        load_canonical_json(authorization_path), repo=repo
    )
    _preflight_git(repo, authorization)
    failures = verify_bootstrap(repo, allow_activation_authorization=True)
    failures.extend(verify_runtime_lock(repo))
    if failures:
        raise ActivationRefused("inactive bootstrap differs: " + "; ".join(failures))
    for relative in (CLAIM_RELATIVE, STATE_RELATIVE, RECORD_RELATIVE, INVALIDITY_RELATIVE):
        path = repo / relative
        if path.exists() or path.with_name(f".{path.name}.tmp").exists():
            raise ActivationRefused(f"activation output already exists: {relative}")
    reviewed_paths = tuple(str(item) for item in authorization["reviewed_source_paths"])
    source_failures = verify_hash_map(
        repo, authorization["reviewed_source_sha256"], name="reviewed source"
    )
    source_failures.extend(verify_production_boundary(repo, reviewed_paths))
    source_failures.extend(
        verify_hash_map(repo, authorization["governing_sha256"], name="governing")
    )
    source_failures.extend(
        verify_hash_map(repo, authorization["protocol_sha256"], name="protocol")
    )
    if source_failures:
        raise ActivationRefused("activation pins differ: " + "; ".join(source_failures))
    return authorization


def _record_activation_invalidity(repo: Path, *, step: int) -> None:
    path = repo / INVALIDITY_RELATIVE
    if path.exists():
        return
    affected: dict[str, str] = {}
    for relative in (CLAIM_RELATIVE, STATE_RELATIVE, RECORD_RELATIVE):
        candidate = repo / relative
        if candidate.is_file():
            affected[relative.as_posix()] = sha256_file(candidate)
    payload = {
        "schema": INVALIDITY_SCHEMA,
        "scientific_outcome": False,
        "validity": "INVALID_PROCESS_RECORD",
        "invalid_cause": "PROCESS",
        "transaction_kind": "T_ACTIVATION",
        "durable_step_index": step,
        "affected_path_sha256": affected,
        "clock_kind": None,
        "boot_identity": None,
        "observed_utc": utc_now(),
        "outstanding_liability_ns": 0,
        "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
    }
    with RuntimeLock(repo):
        atomic_create(path, canonical_json(payload))
        ledger = AppendOnlyLedger(
            repo / LEDGER_RELATIVE, head_path=repo / LEDGER_HEAD_RELATIVE
        )
        entries = ledger.entries()
        if entries and entries[0]["event"] == "T_ACTIVATED":
            state_value = load_canonical_json(repo / STATE_RELATIVE)
            if not isinstance(state_value, dict):
                raise ValueError("post-anchor invalidity lacks a canonical T state")
            TState.from_mapping(state_value)
            event = ledger.append(
                event="T_RUNTIME_INVALID",
                timestamp_utc=str(payload["observed_utc"]),
                data={
                    "invalid_cause": "PROCESS",
                    "invalidity_record_sha256": sha256_file(path),
                    "required_action": "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY",
                    "scientific_outcome": False,
                    "t_state": state_value,
                },
            )
            validate_ledger_event(event)


def _commit_activation(repo: Path) -> str:
    if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise ActivationRefused("git index changed during activation")
    _git(repo, "add", "--", *ACTIVATION_STAGE_PATHS)
    staged = tuple(
        line for line in _git(repo, "diff", "--cached", "--name-only").stdout.splitlines()
        if line
    )
    if len(staged) != len(ACTIVATION_STAGE_PATHS) or set(staged) != set(
        ACTIVATION_STAGE_PATHS
    ):
        raise ActivationRefused(f"activation staged paths differ: {staged!r}")
    args = ["commit", "--no-gpg-sign", "-m", "Activate the Officina T surface"]
    for trailer in ACTIVATION_COMMIT_TRAILERS:
        args.extend(("-m", trailer))
    _git(repo, *args)
    return _git(repo, "rev-parse", "HEAD").stdout.strip()


def activate_repository(
    repo: Path, authorization_path: Path, *, failure_after_step: int | None = None
) -> str:
    """Execute once in an authorized repository; tests use disposable mirrors."""

    repo = repo.resolve(strict=True)
    authorization = activation_preflight(repo, authorization_path)
    timestamp = utc_now()
    authorization_hash = sha256_file(authorization_path)
    state = TState().activate(timestamp)
    state_raw = canonical_json(state.to_mapping())
    paths = canonical_paths(repo)
    reviewed_source = dict(authorization["reviewed_source_sha256"])  # type: ignore[arg-type]
    claim = {
        "schema": CLAIM_SCHEMA,
        "scientific_outcome": False,
        "authorization_sha256": authorization_hash,
        "reviewed_code_head": authorization["reviewed_code_head"],
        "reviewed_source_sha256": reviewed_source,
        "governing_sha256": authorization["governing_sha256"],
        "protocol_sha256": authorization["protocol_sha256"],
        "created_utc": timestamp,
        "canonical_paths": paths,
        "pre_state_sha256": sha256_bytes(canonical_json(TState().to_mapping())),
        "planned_event": "T_ACTIVATED",
        "planned_t_state_sha256": sha256_bytes(state_raw),
    }
    step = 0
    try:
        with RuntimeLock(repo):
            atomic_create(repo / CLAIM_RELATIVE, canonical_json(claim))
            step = 1
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            atomic_create(repo / STATE_RELATIVE, state_raw)
            step = 2
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            ledger = AppendOnlyLedger(repo / LEDGER_RELATIVE, head_path=repo / LEDGER_HEAD_RELATIVE)
            entry = ledger.append(
                event="T_ACTIVATED",
                timestamp_utc=timestamp,
                data={
                    "authorization_sha256": authorization_hash,
                    "claim_sha256": sha256_file(repo / CLAIM_RELATIVE),
                    "device_policy_token": authorization["device_policy_token"],
                    "envelope_token": authorization["envelope_token"],
                    "scientific_outcome": False,
                    "t_state": state.to_mapping(),
                },
            )
            step = 3
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            inactive_envelope = load_canonical_json(repo / ENVELOPE_RELATIVE)
            if not isinstance(inactive_envelope, dict):
                raise ValueError("inactive envelope is not an object")
            atomic_replace(
                repo / ENVELOPE_RELATIVE,
                canonical_json(_active_envelope(inactive_envelope, timestamp)),
                mode=0o644,
            )
            step = 4
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            immutable = {
                path: reviewed_source[path]
                for path in REQUIRED_IMMUTABLE_CONTROL_PATHS
            }
            record = {
                "schema": RECORD_SCHEMA,
                "scientific_outcome": False,
                "validity": "VALID_PROCESS_RECORD",
                "authorization_sha256": authorization_hash,
                "claim_sha256": sha256_file(repo / CLAIM_RELATIVE),
                "reviewed_code_head": authorization["reviewed_code_head"],
                "reviewed_source_sha256": reviewed_source,
                "governing_sha256": authorization["governing_sha256"],
                "protocol_sha256": authorization["protocol_sha256"],
                "created_utc": timestamp,
                "t_state_sha256": sha256_file(repo / STATE_RELATIVE),
                "active_envelope_sha256": sha256_file(repo / ENVELOPE_RELATIVE),
                "ledger_entry_sha256": entry["entry_sha256"],
                "ledger_head_sha256": sha256_file(repo / LEDGER_HEAD_RELATIVE),
                "immutable_control_sha256": immutable,
            }
            atomic_create(repo / RECORD_RELATIVE, canonical_json(record))
            step = 5
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            failures = verify_active_repository(
                repo, require_activation_commit=False, runtime_lock_held=True
            )
            if failures:
                raise ActivationRefused(
                    "active state does not re-derive: " + "; ".join(failures)
                )
            committed = _commit_activation(repo)
            step = 6
            if failure_after_step == step:
                raise RuntimeError("injected activation failure")
            final_failures = verify_active_repository(
                repo, require_activation_commit=True, runtime_lock_held=True
            )
            if final_failures:
                raise ActivationRefused(
                    "committed active state differs: " + "; ".join(final_failures)
                )
            return committed
    except BaseException:
        if step >= 1:
            _record_activation_invalidity(repo, step=step)
        raise


def _active_cleanliness_failures(
    repo: Path, *, activation_record: Mapping[str, object]
) -> list[str]:
    status = _git(
        repo, "status", "--porcelain=v1", "--untracked-files=all"
    ).stdout.splitlines()
    if not status:
        return []
    leases_root = repo / RUNTIME_ROOT_RELATIVE / "T_ACTIVE_LEASES"
    lease_paths = sorted(leases_root.glob("*.json")) if leases_root.is_dir() else []
    if not lease_paths:
        return ["active worktree is dirty without a verified open lease"]
    allowed = {
        LEDGER_RELATIVE.as_posix(),
        LEDGER_HEAD_RELATIVE.as_posix(),
        STATE_RELATIVE.as_posix(),
    }
    activation_record_hash = sha256_file(repo / RECORD_RELATIVE)
    immutable = activation_record.get("immutable_control_sha256")
    if not isinstance(immutable, dict):
        return ["active record immutable controls are malformed"]
    for lease_path in lease_paths:
        process_id = lease_path.stem
        claim_path = (
            repo / RUNTIME_ROOT_RELATIVE / "T_PROCESS_CLAIMS" / f"{process_id}.json"
        )
        try:
            lease = validate_active_lease(load_canonical_json(lease_path))
            claim = validate_process_claim_against_activation(
                load_canonical_json(claim_path),
                activation_record_sha256=activation_record_hash,
                immutable_control_sha256=immutable,  # type: ignore[arg-type]
            )
            lease_claim = {
                key: item
                for key, item in lease.items()
                if key not in {
                    "last_charged_reading_ns", "cumulative_charge_ns",
                    "heartbeat_deadline_ns", "outstanding_liability_ns",
                    "prior_charge_event_sha256",
                }
            }
            lease_claim["schema"] = "philosophia.officina.t-process-claim.v1"
            if canonical_json(lease_claim) != canonical_json(claim):
                raise ValueError("active lease differs from its durable claim")
            if lease["process_id"] != process_id:
                raise ValueError("active lease filename differs from process id")
        except (OSError, ValueError) as error:
            return [f"active lease ownership is invalid: {error}"]
        allowed.add(lease_path.relative_to(repo).as_posix())
        allowed.add(claim_path.relative_to(repo).as_posix())
    observed = {line[3:] for line in status if len(line) >= 4}
    unexpected = observed - allowed
    return (
        [f"active worktree contains paths outside verified lease ownership: {sorted(unexpected)}"]
        if unexpected
        else []
    )


def verify_active_repository(
    repo: Path,
    *,
    require_activation_commit: bool,
    runtime_lock_held: bool = False,
) -> list[str]:
    failures: list[str] = []
    repo = repo.resolve(strict=True)
    if not runtime_lock_held:
        failures.extend(verify_runtime_lock(repo))
    try:
        authorization = validate_authorization(
            load_canonical_json(repo / AUTHORIZATION_RELATIVE), repo=repo
        )
        claim = load_canonical_json(repo / CLAIM_RELATIVE)
        state_value = load_canonical_json(repo / STATE_RELATIVE)
        record = load_canonical_json(repo / RECORD_RELATIVE)
        envelope = load_canonical_json(repo / ENVELOPE_RELATIVE)
    except (OSError, ValueError, ActivationRefused) as error:
        return [f"active artifact load failed: {error}"]
    if not isinstance(claim, dict) or set(claim) != _CLAIM_KEYS or claim["schema"] != CLAIM_SCHEMA:
        failures.append("activation claim fields differ")
    elif claim.get("scientific_outcome") is not False:
        failures.append("activation claim scientific flag differs")
    if not isinstance(record, dict) or set(record) != _RECORD_KEYS or record["schema"] != RECORD_SCHEMA:
        failures.append("activation record fields differ")
    elif record.get("scientific_outcome") is not False or record.get("validity") != "VALID_PROCESS_RECORD":
        failures.append("activation record validity differs")
    expected_envelope = {
        "activated": True,
        "activated_utc": claim.get("created_utc") if isinstance(claim, dict) else None,
        "candidate_registration_cap": 12,
        "checkpoint_device_hours": 40,
        "checkpoint_elapsed_calendar_hours": 48,
        "device_hour_cap": 168,
        "device_hours_are_aggregate": True,
        "ledger": LEDGER_RELATIVE.as_posix(),
        "schema": ACTIVE_ENVELOPE_SCHEMA,
        "scientific_outcome": False,
        "strict_s_available": False,
    }
    if canonical_json(envelope) != canonical_json(expected_envelope):
        failures.append("active envelope differs from the signed resource contract")
    entries: list[dict[str, object]] = []
    try:
        if not isinstance(state_value, dict):
            raise ValueError("state is not an object")
        state = TState.from_mapping(state_value)
        if state.activated_utc is None:
            failures.append("active state lacks activation time")
        if state.candidate_ids:
            failures.append("pre-WP-6 active state contains candidate registrations")
        entries = AppendOnlyLedger(
            repo / LEDGER_RELATIVE, head_path=repo / LEDGER_HEAD_RELATIVE
        ).entries()
        if not entries or entries[0]["event"] != "T_ACTIVATED":
            failures.append("ledger does not begin with T_ACTIVATED")
        for entry in entries:
            try:
                validate_ledger_event(entry)
            except ValueError as error:
                failures.append(f"ledger event validation failed: {error}")
        last_state_entry = next(
            (entry for entry in reversed(entries) if entry["event"] in STATE_BEARING_EVENTS),
            None,
        )
        if last_state_entry is None or not isinstance(last_state_entry["data"], dict):
            failures.append("ledger has no state-bearing event")
        elif canonical_json(last_state_entry["data"].get("t_state")) != canonical_json(state_value):
            failures.append("state cache differs from last state-bearing event")
        if record.get("ledger_entry_sha256") != entries[0]["entry_sha256"]:
            failures.append("activation record ledger entry differs")
        historical_head = canonical_json(
            {
                "entry_count": 1,
                "head_sha256": entries[0]["entry_sha256"],
                "schema": HEAD_SCHEMA,
                "scientific_outcome": False,
            }
        )
        if record.get("ledger_head_sha256") != sha256_bytes(historical_head):
            failures.append("activation record historical ledger-head anchor differs")
    except (OSError, ValueError) as error:
        failures.append(f"active ledger/state verification failed: {error}")
    pairs = (
        ("authorization_sha256", repo / AUTHORIZATION_RELATIVE),
        ("claim_sha256", repo / CLAIM_RELATIVE),
        ("active_envelope_sha256", repo / ENVELOPE_RELATIVE),
    )
    for field, path in pairs:
        if not isinstance(record, dict) or record.get(field) != sha256_file(path):
            failures.append(f"activation record {field} differs")
    if isinstance(record, dict):
        failures.extend(
            verify_hash_map(
                repo,
                authorization.get("reviewed_source_sha256"),
                name="reviewed source",
            )
        )
        failures.extend(
            verify_hash_map(repo, authorization.get("governing_sha256"), name="governing")
        )
        failures.extend(
            verify_hash_map(repo, authorization.get("protocol_sha256"), name="protocol")
        )
        failures.extend(
            verify_production_boundary(
                repo, tuple(str(item) for item in authorization["reviewed_source_paths"])
            )
        )
        if isinstance(claim, dict):
            first_state = entries[0]["data"].get("t_state") if entries else None
            expected_claim_links = {
                "authorization_sha256": sha256_file(repo / AUTHORIZATION_RELATIVE),
                "reviewed_code_head": authorization["reviewed_code_head"],
                "reviewed_source_sha256": authorization["reviewed_source_sha256"],
                "governing_sha256": authorization["governing_sha256"],
                "protocol_sha256": authorization["protocol_sha256"],
                "canonical_paths": authorization["canonical_paths"],
                "planned_event": "T_ACTIVATED",
                "pre_state_sha256": sha256_bytes(canonical_json(TState().to_mapping())),
                "planned_t_state_sha256": sha256_bytes(canonical_json(first_state)),
            }
            for field, expected in expected_claim_links.items():
                if canonical_json(claim.get(field)) != canonical_json(expected):
                    failures.append(f"activation claim {field} cross-link differs")
            if claim.get("created_utc") != expected_envelope["activated_utc"]:
                failures.append("activation claim timestamp differs")
            for field in (
                "authorization_sha256", "reviewed_code_head",
                "reviewed_source_sha256", "governing_sha256", "protocol_sha256",
                "created_utc",
            ):
                if canonical_json(record.get(field)) != canonical_json(claim.get(field)):
                    failures.append(f"activation record {field} differs from claim")
            if record.get("t_state_sha256") != sha256_bytes(canonical_json(first_state)):
                failures.append("activation record initial T-state anchor differs")
        expected_immutable = {
            path: authorization["reviewed_source_sha256"][path]
            for path in REQUIRED_IMMUTABLE_CONTROL_PATHS
        }
        if canonical_json(record.get("immutable_control_sha256")) != canonical_json(
            expected_immutable
        ):
            failures.append("activation record immutable-control set differs")
        failures.extend(
            verify_hash_map(repo, record.get("immutable_control_sha256"), name="immutable control")
        )
    if require_activation_commit:
        try:
            tracked = set(_git(repo, "ls-files").stdout.splitlines())
            missing = set(ACTIVATION_STAGE_PATHS) - tracked
            if missing:
                failures.append(f"activation outputs are not tracked: {sorted(missing)}")
            activation_commit = _git(
                repo, "log", "-1", "--format=%H", "--", RECORD_RELATIVE.as_posix()
            ).stdout.strip()
            committed_paths = set(
                filter(
                    None,
                    _git(
                        repo,
                        "diff-tree",
                        "--no-commit-id",
                        "--name-only",
                        "-r",
                        activation_commit,
                    ).stdout.splitlines(),
                )
            )
            if committed_paths != set(ACTIVATION_STAGE_PATHS):
                failures.append("activation commit path set differs")
            message = _git(
                repo, "show", "-s", "--format=%B", activation_commit
            ).stdout
            if any(message.count(trailer) != 1 for trailer in ACTIVATION_COMMIT_TRAILERS):
                failures.append("activation commit authorship trailers differ")
            immutable_tracked = (
                AUTHORIZATION_RELATIVE.as_posix(),
                CLAIM_RELATIVE.as_posix(),
                RECORD_RELATIVE.as_posix(),
                ENVELOPE_RELATIVE.as_posix(),
                *REQUIRED_IMMUTABLE_CONTROL_PATHS,
            )
            if _git(
                repo, "diff", "--quiet", "HEAD", "--", *immutable_tracked,
                check=False,
            ).returncode:
                failures.append("active immutable tracked bytes differ from current HEAD")
            if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
                failures.append("active verifier found a nonempty git index")
            failures.extend(_active_cleanliness_failures(repo, activation_record=record))
        except (OSError, subprocess.SubprocessError) as error:
            failures.append(f"active git verification failed: {error}")
    del authorization
    return failures
