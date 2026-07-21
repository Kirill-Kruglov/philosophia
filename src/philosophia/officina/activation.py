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
from .ledger import AppendOnlyLedger, GENESIS, HEADER
from .runtime import (
    INVALIDITY_SCHEMA,
    POST_ACTIVATION_EVENTS,
    RUNTIME_LOCK_RELATIVE,
    RuntimeLock,
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
ACTIVATION_STAGE_PATHS = (
    CLAIM_RELATIVE.as_posix(),
    STATE_RELATIVE.as_posix(),
    RECORD_RELATIVE.as_posix(),
    ENVELOPE_RELATIVE.as_posix(),
    LEDGER_RELATIVE.as_posix(),
    LEDGER_HEAD_RELATIVE.as_posix(),
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
    missing_control = set(IMMUTABLE_CONTROL_PATHS) - set(paths)
    if missing_control:
        raise ValueError(f"immutable runtime controls are unreviewed: {sorted(missing_control)}")
    if GENERIC_HARNESS_RELATIVE.as_posix() not in paths:
        raise ActivationRefused("generic metered harness has not received review")
    _validate_hash_map(value["governing_sha256"], "governing")
    _validate_hash_map(value["protocol_sha256"], "protocol")
    if value["canonical_paths"] != canonical_paths(repo):
        raise ValueError("authorization canonical paths differ")
    if value["command"] != (
        ".venv/bin/python scripts/officina_activate_t.py "
        "--authorization successor/officina/OFFICINA_T_ACTIVATION_AUTHORIZATION.json"
    ):
        raise ValueError("activation command differs")
    for field in ("envelope_token", "device_policy_token"):
        if not isinstance(value[field], str) or not value[field]:
            raise ValueError(f"{field} must be named")
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
    atomic_create(path, canonical_json(payload))


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
    for trailer in (
        "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>",
        "Co-Authored-By: GPT-5.6 Sol <noreply@openai.com>",
        "Co-Authored-By: Codex GPT-5.5 <noreply@openai.com>",
    ):
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
                path: reviewed_source[path] for path in IMMUTABLE_CONTROL_PATHS
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
        failures = verify_active_repository(repo, require_activation_commit=False)
        if failures:
            raise ActivationRefused("active state does not re-derive: " + "; ".join(failures))
        committed = _commit_activation(repo)
        step = 6
        if failure_after_step == step:
            raise RuntimeError("injected activation failure")
        final_failures = verify_active_repository(repo, require_activation_commit=True)
        if final_failures:
            raise ActivationRefused("committed active state differs: " + "; ".join(final_failures))
        return committed
    except BaseException:
        if step >= 1:
            _record_activation_invalidity(repo, step=step)
        raise


def verify_active_repository(repo: Path, *, require_activation_commit: bool) -> list[str]:
    failures: list[str] = []
    repo = repo.resolve(strict=True)
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
    if not isinstance(envelope, dict) or envelope.get("schema") != ACTIVE_ENVELOPE_SCHEMA or envelope.get("activated") is not True:
        failures.append("active envelope differs")
    try:
        if not isinstance(state_value, dict):
            raise ValueError("state is not an object")
        state = TState.from_mapping(state_value)
        if state.activated_utc is None:
            failures.append("active state lacks activation time")
        entries = AppendOnlyLedger(
            repo / LEDGER_RELATIVE, head_path=repo / LEDGER_HEAD_RELATIVE
        ).entries()
        if not entries or entries[0]["event"] != "T_ACTIVATED":
            failures.append("ledger does not begin with T_ACTIVATED")
        for entry in entries:
            if entry["event"] not in POST_ACTIVATION_EVENTS:
                failures.append(f"ledger contains event outside closed vocabulary: {entry['event']}")
            if entry["event"] in STATE_BEARING_EVENTS:
                data = entry["data"]
                if not isinstance(data, dict) or "t_state" not in data:
                    failures.append(f"state-bearing event lacks t_state: {entry['event']}")
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
    except (OSError, ValueError) as error:
        failures.append(f"active ledger/state verification failed: {error}")
    pairs = (
        ("authorization_sha256", repo / AUTHORIZATION_RELATIVE),
        ("claim_sha256", repo / CLAIM_RELATIVE),
        ("t_state_sha256", repo / STATE_RELATIVE),
        ("active_envelope_sha256", repo / ENVELOPE_RELATIVE),
        ("ledger_head_sha256", repo / LEDGER_HEAD_RELATIVE),
    )
    for field, path in pairs:
        if not isinstance(record, dict) or record.get(field) != sha256_file(path):
            failures.append(f"activation record {field} differs")
    if isinstance(record, dict):
        failures.extend(
            verify_hash_map(repo, record.get("immutable_control_sha256"), name="immutable control")
        )
    if require_activation_commit:
        try:
            tracked = set(_git(repo, "ls-files").stdout.splitlines())
            missing = set(ACTIVATION_STAGE_PATHS) - tracked
            if missing:
                failures.append(f"activation outputs are not tracked: {sorted(missing)}")
            if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
                failures.append("active verifier found a nonempty git index")
        except (OSError, subprocess.SubprocessError) as error:
            failures.append(f"active git verification failed: {error}")
    del authorization
    return failures
