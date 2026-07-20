from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Mapping

from .accounting import TEnvelope, TState, parse_utc
from .canonical import (
    atomic_create,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
    sha256_file,
)
from .ledger import AppendOnlyLedger


CHECKPOINT_SCHEMA = "philosophia.officina.pause-checkpoint.v2"


def _artifact_records(paths: Mapping[str, Path]) -> dict[str, object]:
    records: dict[str, object] = {}
    for name, path in sorted(paths.items()):
        if not name or not isinstance(path, Path):
            raise ValueError("pause artifacts require named Path values")
        resolved = path.resolve(strict=True)
        if not resolved.is_file():
            raise ValueError("pause artifact must be a regular file")
        records[name] = {"path": str(resolved), "sha256": sha256_file(resolved)}
    return records


def write_pause_checkpoint(
    *,
    path: Path,
    state: TState,
    artifact_paths: Mapping[str, Path],
    ledger_head_before: str,
) -> str:
    if (
        state.activated_utc is None
        or state.author_stopped
        or state.resume_review_pending
    ):
        raise ValueError("operational pause requires active, available T")
    if len(ledger_head_before) != 64:
        raise ValueError("ledger head must be SHA-256")
    payload = {
        "artifacts": _artifact_records(artifact_paths),
        "ledger_head_before": ledger_head_before,
        "schema": CHECKPOINT_SCHEMA,
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
    artifact_paths: Mapping[str, Path],
    timestamp_utc: str,
    reason: str,
) -> dict[str, object]:
    if not reason:
        raise ValueError("operational pause reason must be named")
    if (
        state.activated_utc is None
        or state.author_stopped
        or state.resume_review_pending
    ):
        raise ValueError("operational pause requires active, available T")
    pause_time = parse_utc(timestamp_utc)
    origin = parse_utc(state.last_review_utc or state.activated_utc)
    if pause_time < origin:
        raise ValueError("operational pause predates active T state")
    entries = ledger.entries()
    ledger_head = str(entries[-1]["entry_sha256"]) if entries else "0" * 64
    checkpoint_hash = write_pause_checkpoint(
        path=checkpoint_path,
        state=state,
        artifact_paths=artifact_paths,
        ledger_head_before=ledger_head,
    )
    return ledger.append(
        event="T_OPERATIONAL_PAUSE",
        timestamp_utc=timestamp_utc,
        data={
            "checkpoint_path": str(checkpoint_path.resolve()),
            "checkpoint_sha256": checkpoint_hash,
            "reason": reason,
            "resets_e3": False,
        },
    )


def record_not_activated_maintenance(
    *, ledger: AppendOnlyLedger, state: TState, timestamp_utc: str, reason: str
) -> dict[str, object]:
    if state != TState():
        raise ValueError("not-activated maintenance requires pristine inactive T")
    return ledger.append(
        event="T_NOT_ACTIVATED_AT_MAINTENANCE",
        timestamp_utc=timestamp_utc,
        data={"reason": reason, "checkpoint_created": False},
    )


@dataclass(frozen=True)
class ResumeGate:
    state: TState
    ledger: AppendOnlyLedger
    envelope: TEnvelope
    resumed_utc: str
    review_required: bool

    def admit_work(self) -> TState:
        if self.review_required or self.state.resume_review_pending:
            raise PermissionError("overdue E3 review blocks resumed work")
        return self.state

    def complete_overdue_review(self, *, timestamp_utc: str) -> TState:
        if not self.review_required:
            raise ValueError("resume review is not due")
        if parse_utc(timestamp_utc) < parse_utc(self.resumed_utc):
            raise ValueError("resume review predates resume admission")
        if not self.state.resume_review_pending:
            raise ValueError("resume gate state is not pending review")
        entries = self.ledger.entries()
        if not entries or entries[-1]["event"] != "T_OPERATIONAL_PAUSE":
            raise ValueError("resume review transaction is no longer current")
        if not self.state.review_due(self.envelope, timestamp_utc):
            raise ValueError("resume review is not due at completion time")
        reviewed = replace(
            self.state,
            last_review_utc=timestamp_utc,
            device_nanoseconds_at_review=self.state.device_nanoseconds,
            resume_review_pending=False,
        )
        self.ledger.append(
            event="T_REVIEW_COMPLETED",
            timestamp_utc=timestamp_utc,
            data={"reason": "overdue-resume-gate", "t_state": reviewed.to_mapping()},
        )
        return reviewed


def _verify_artifacts(value: object) -> None:
    if not isinstance(value, dict):
        raise ValueError("pause artifact records must be an object")
    for name, record in value.items():
        if not isinstance(name, str) or not name:
            raise ValueError("pause artifact name is malformed")
        if not isinstance(record, dict) or set(record) != {"path", "sha256"}:
            raise ValueError("pause artifact record fields differ")
        path_value = record["path"]
        digest = record["sha256"]
        if not isinstance(path_value, str) or not isinstance(digest, str):
            raise ValueError("pause artifact identity is malformed")
        path = Path(path_value)
        try:
            resolved = path.resolve(strict=True)
        except FileNotFoundError as error:
            raise ValueError("pause artifact is missing") from error
        if str(resolved) != path_value or not resolved.is_file():
            raise ValueError("pause artifact path identity changed")
        if sha256_file(resolved) != digest:
            raise ValueError("pause artifact hash mismatch")


def verify_resume(
    *,
    ledger: AppendOnlyLedger,
    checkpoint_path: Path,
    envelope: TEnvelope,
    timestamp_utc: str,
) -> ResumeGate:
    checkpoint = load_canonical_json(checkpoint_path)
    expected_checkpoint_keys = {
        "artifacts", "ledger_head_before", "schema", "scientific_outcome", "t_state"
    }
    if not isinstance(checkpoint, dict) or set(checkpoint) != expected_checkpoint_keys:
        raise ValueError("pause checkpoint fields differ")
    if checkpoint["schema"] != CHECKPOINT_SCHEMA or checkpoint["scientific_outcome"] is not False:
        raise ValueError("pause checkpoint schema mismatch")
    entries = ledger.entries()
    if not entries or entries[-1].get("event") != "T_OPERATIONAL_PAUSE":
        raise ValueError("ledger does not end in an operational pause")
    data = entries[-1].get("data")
    if not isinstance(data, dict) or set(data) != {
        "checkpoint_path", "checkpoint_sha256", "reason", "resets_e3"
    }:
        raise ValueError("pause ledger data fields differ")
    if data["resets_e3"] is not False:
        raise ValueError("operational pause cannot reset E3")
    if data["checkpoint_sha256"] != sha256_file(checkpoint_path):
        raise ValueError("pause checkpoint hash mismatch")
    if data["checkpoint_path"] != str(checkpoint_path.resolve()):
        raise ValueError("pause checkpoint path mismatch")
    expected_previous = str(entries[-2]["entry_sha256"]) if len(entries) > 1 else "0" * 64
    if checkpoint["ledger_head_before"] != expected_previous:
        raise ValueError("pause checkpoint prior ledger head mismatch")
    _verify_artifacts(checkpoint["artifacts"])
    state_value = checkpoint["t_state"]
    if not isinstance(state_value, dict):
        raise ValueError("pause checkpoint T state is malformed")
    state = TState.from_mapping(state_value)
    if (
        state.activated_utc is None
        or state.author_stopped
        or state.resume_review_pending
    ):
        raise ValueError("pause checkpoint does not contain available active T")
    pause_timestamp = entries[-1]["timestamp_utc"]
    if not isinstance(pause_timestamp, str):
        raise ValueError("pause ledger timestamp is malformed")
    resume_time = parse_utc(timestamp_utc)
    pause_time = parse_utc(pause_timestamp)
    if resume_time < pause_time:
        raise ValueError("resume timestamp predates operational pause")
    due = state.review_due(envelope, timestamp_utc)
    resumed_state = replace(state, resume_review_pending=due)
    return ResumeGate(
        state=resumed_state,
        ledger=ledger,
        envelope=envelope,
        resumed_utc=timestamp_utc,
        review_required=due,
    )
