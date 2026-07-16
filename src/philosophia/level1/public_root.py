from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Mapping

from .allocation import assign_roles, development_pairs
from .serialization import DeterministicKey


TRANSCRIPT_SCHEMA = "philosophia.level1.public-root.v1"
CLAIM_SCHEMA = "philosophia.level1.public-root-claim.v1"


def canonical_json(value: Mapping[str, object]) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        + "\n"
    ).encode("ascii")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def environment_fingerprint(environment: Mapping[str, object]) -> str:
    return hashlib.sha256(canonical_json(environment)).hexdigest()


def build_claim(
    *,
    expected_head: str,
    reviewed_code_head: str,
    created_utc: str,
    transcript_path: str,
) -> dict[str, object]:
    return {
        "schema": CLAIM_SCHEMA,
        "status": "armed-before-entropy",
        "expected_head": expected_head,
        "reviewed_code_head": reviewed_code_head,
        "created_utc": created_utc,
        "transcript_path": transcript_path,
        "no_redraw": True,
        "operator_rule": "claim presence forbids rerun or deletion",
    }


def build_transcript(
    *,
    root: bytes,
    git_head: str,
    reviewed_code_head: str,
    timestamp_utc: str,
    environment: Mapping[str, object],
    required_spec_hashes: Mapping[str, str],
    governing_lineage_hashes: Mapping[str, str],
    allocations: Mapping[str, object],
) -> dict[str, object]:
    if len(root) != 32:
        raise ValueError("public root must contain exactly 32 bytes")
    return {
        "schema": TRANSCRIPT_SCHEMA,
        "kind": "level1-public-allocation-root",
        "scientific_outcome": False,
        "root_hex": root.hex(),
        "git_head_before_draw": git_head,
        "reviewed_code_head": reviewed_code_head,
        "timestamp_utc": timestamp_utc,
        "environment": dict(environment),
        "environment_fingerprint": environment_fingerprint(environment),
        "required_spec_hashes": dict(required_spec_hashes),
        "governing_lineage_hashes": dict(governing_lineage_hashes),
        "allocations": dict(allocations),
        "process_attestation": {
            "transcript_absent_before_draw": True,
            "durable_claim_before_draw": True,
            "os_csprng_api": "secrets.token_bytes",
            "os_csprng_calls": 1,
            "root_bytes": 32,
            "atomic_transcript_write": True,
            "no_redraw": True,
            "threat_model": "procedural-not-cryptographic-independence",
        },
        "witness_attestation": (
            "Kirill Kruglov attests the recorded process facts, durable transcript "
            "write and enclosing git commit; no cryptographic independence is claimed."
        ),
        "forbidden_derivations": [
            "real evaluator panel",
            "panel raw realizations",
            "panel ordering",
            "encryption salt",
            "escrow plaintext",
        ],
    }


def derive_public_allocations(root: bytes) -> dict[str, object]:
    key = DeterministicKey(root, purpose="public-root", test_only=False)
    development = [
        {
            "slot": pair.slot,
            "lower": pair.lower,
            "upper": pair.upper,
            "stratum": pair.stratum,
        }
        for pair in development_pairs(key)
    ]
    if len(development) != 6 or [
        sum(item["stratum"] == stratum for item in development)
        for stratum in (1, 2, 3)
    ] != [2, 2, 2]:
        raise RuntimeError("signed development allocation cardinality changed")
    roles = [
        {
            "slot": item.pair.slot,
            "lower": item.pair.lower,
            "upper": item.pair.upper,
            "stratum": item.pair.stratum,
            "role_bit": item.role_bit,
            "target": item.target,
            "donor": item.donor,
        }
        for item in assign_roles(key)
    ]
    if len(roles) != 24 or [
        sum(item["stratum"] == stratum for item in roles)
        for stratum in (1, 2, 3)
    ] != [8, 8, 8]:
        raise RuntimeError("signed outcome role cardinality changed")
    return {
        "development_pairs": development,
        "outcome_role_assignments": roles,
        "outcome_sample": "deferred-until-N3",
    }


def load_durable_transcript(path: Path, *, expected_head: str) -> dict[str, object]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict) or canonical_json(value) != raw:
        raise ValueError("public-root transcript is not canonical JSON")
    if value.get("schema") != TRANSCRIPT_SCHEMA:
        raise ValueError("public-root transcript schema mismatch")
    if value.get("git_head_before_draw") != expected_head:
        raise ValueError("public-root transcript HEAD mismatch")
    root_hex = value.get("root_hex")
    if not isinstance(root_hex, str) or len(root_hex) != 64:
        raise ValueError("public-root transcript root is not 32 bytes")
    try:
        bytes.fromhex(root_hex)
    except ValueError as error:
        raise ValueError("public-root transcript root is not hexadecimal") from error
    return value


def atomic_create(path: Path, payload: bytes, *, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    if path.exists() or temporary.exists():
        raise FileExistsError(f"refusing to replace one-shot artifact: {path}")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as target:
            target.write(payload)
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        raise


def atomic_create_no_replace(path: Path, payload: bytes, *, mode: int = 0o600) -> None:
    """Durably install a one-shot artifact without a replace race."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    if path.exists() or temporary.exists():
        raise FileExistsError(f"refusing to replace one-shot artifact: {path}")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as target:
            target.write(payload)
            target.flush()
            os.fsync(target.fileno())
        os.link(temporary, path)
        os.unlink(temporary)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise
