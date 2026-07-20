from __future__ import annotations

from pathlib import Path
from typing import Mapping

from .accounting import TState
from .canonical import (
    atomic_create,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
)
from .ledger import AppendOnlyLedger


def write_pause_checkpoint(
    *,
    path: Path,
    state: TState,
    artifact_hashes: Mapping[str, str],
    ledger_head_before: str,
) -> str:
    if len(ledger_head_before) != 64:
        raise ValueError("ledger head must be SHA-256")
    if any(len(value) != 64 for value in artifact_hashes.values()):
        raise ValueError("artifact hashes must be SHA-256")
    payload = {
        "artifact_hashes": dict(artifact_hashes),
        "ledger_head_before": ledger_head_before,
        "schema": "philosophia.officina.pause-checkpoint.v1",
        "scientific_outcome": False,
        "t_state": state.to_mapping(),
    }
    raw = canonical_json(payload)
    atomic_create(path, raw)
    return sha256_bytes(raw)


def record_operational_pause(
    *,
    ledger: AppendOnlyLedger,
    checkpoint_path: Path,
    state: TState,
    artifact_hashes: Mapping[str, str],
    timestamp_utc: str,
    reason: str,
) -> dict[str, object]:
    entries = ledger.entries()
    ledger_head = str(entries[-1]["entry_sha256"]) if entries else "0" * 64
    checkpoint_hash = write_pause_checkpoint(
        path=checkpoint_path,
        state=state,
        artifact_hashes=artifact_hashes,
        ledger_head_before=ledger_head,
    )
    return ledger.append(
        event="T_OPERATIONAL_PAUSE",
        timestamp_utc=timestamp_utc,
        data={
            "checkpoint_path": checkpoint_path.name,
            "checkpoint_sha256": checkpoint_hash,
            "reason": reason,
            "resets_e3": False,
        },
    )


def record_not_activated_maintenance(
    *, ledger: AppendOnlyLedger, timestamp_utc: str, reason: str
) -> dict[str, object]:
    return ledger.append(
        event="T_NOT_ACTIVATED_AT_MAINTENANCE",
        timestamp_utc=timestamp_utc,
        data={"reason": reason, "checkpoint_created": False},
    )


def verify_resume(
    *, ledger: AppendOnlyLedger, checkpoint_path: Path
) -> TState:
    checkpoint = load_canonical_json(checkpoint_path)
    if not isinstance(checkpoint, dict):
        raise ValueError("pause checkpoint must be an object")
    if checkpoint.get("schema") != "philosophia.officina.pause-checkpoint.v1":
        raise ValueError("pause checkpoint schema mismatch")
    entries = ledger.entries()
    if not entries or entries[-1].get("event") != "T_OPERATIONAL_PAUSE":
        raise ValueError("ledger does not end in an operational pause")
    data = entries[-1].get("data")
    if not isinstance(data, dict):
        raise ValueError("pause ledger data is malformed")
    if data.get("checkpoint_sha256") != sha256_bytes(checkpoint_path.read_bytes()):
        raise ValueError("pause checkpoint hash mismatch")
    if data.get("checkpoint_path") != checkpoint_path.name:
        raise ValueError("pause checkpoint path mismatch")
    expected_previous = (
        str(entries[-2]["entry_sha256"]) if len(entries) > 1 else "0" * 64
    )
    if checkpoint.get("ledger_head_before") != expected_previous:
        raise ValueError("pause checkpoint prior ledger head mismatch")
    state = checkpoint.get("t_state")
    if not isinstance(state, dict):
        raise ValueError("pause checkpoint T state is malformed")
    return TState.from_mapping(state)
