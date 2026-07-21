from __future__ import annotations

import fcntl
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Mapping

from .canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    fsync_directory,
    load_canonical_json,
    sha256_bytes,
)


HEADER = (
    "# Officina T Ledger\n\n"
    "Status: `NOT_ACTIVATED`\n\n"
    "This is an append-only public ledger skeleton. Machine entries, once authorized,\n"
    "are canonical JSON objects prefixed by `- ` and linked by SHA-256. WP-1/WP-2\n"
    "tests use temporary ledgers only. No real T entry exists in this file.\n"
)
GENESIS = "0" * 64
HEAD_SCHEMA = "philosophia.officina.ledger-head.v1"


class LedgerIntegrityError(ValueError):
    pass


def _parse_timestamp(value: object) -> datetime:
    if not isinstance(value, str) or re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
        value,
    ) is None:
        raise LedgerIntegrityError("ledger timestamp must use canonical UTC Z form")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as error:
        raise LedgerIntegrityError("ledger timestamp is invalid") from error
    if parsed.tzinfo != timezone.utc:
        raise LedgerIntegrityError("ledger timestamp must be UTC")
    return parsed


def _entry_payload(
    *,
    sequence: int,
    previous_sha256: str,
    event: str,
    timestamp_utc: str,
    data: Mapping[str, object],
) -> dict[str, object]:
    if sequence < 0:
        raise ValueError("ledger sequence must be non-negative")
    if len(previous_sha256) != 64:
        raise ValueError("previous ledger hash must be SHA-256")
    if not event or not timestamp_utc:
        raise ValueError("ledger event and timestamp must be named")
    return {
        "data": dict(data),
        "event": event,
        "previous_sha256": previous_sha256,
        "sequence": sequence,
        "timestamp_utc": timestamp_utc,
    }


def build_entry(
    *,
    sequence: int,
    previous_sha256: str,
    event: str,
    timestamp_utc: str,
    data: Mapping[str, object],
) -> dict[str, object]:
    payload = _entry_payload(
        sequence=sequence,
        previous_sha256=previous_sha256,
        event=event,
        timestamp_utc=timestamp_utc,
        data=data,
    )
    return {**payload, "entry_sha256": sha256_bytes(canonical_json(payload))}


def parse_ledger(raw: bytes) -> list[dict[str, object]]:
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise LedgerIntegrityError("ledger must be ASCII") from error
    if not text.startswith(HEADER):
        raise LedgerIntegrityError("ledger header mismatch")
    entries: list[dict[str, object]] = []
    previous = GENESIS
    previous_timestamp: datetime | None = None
    for line in text[len(HEADER) :].splitlines():
        if not line:
            continue
        if not line.startswith("- "):
            raise LedgerIntegrityError("ledger contains a non-entry line")
        try:
            value = json.loads(line[2:])
        except json.JSONDecodeError as error:
            raise LedgerIntegrityError("ledger entry is not JSON") from error
        if not isinstance(value, dict):
            raise LedgerIntegrityError("ledger entry must be an object")
        expected_keys = {
            "data",
            "entry_sha256",
            "event",
            "previous_sha256",
            "sequence",
            "timestamp_utc",
        }
        if set(value) != expected_keys:
            raise LedgerIntegrityError("ledger entry fields differ")
        entry_hash = value["entry_sha256"]
        payload = {key: item for key, item in value.items() if key != "entry_sha256"}
        if canonical_json(value).decode("ascii").rstrip("\n") != line[2:]:
            raise LedgerIntegrityError("ledger entry is not canonical JSON")
        if type(value["sequence"]) is not int or value["sequence"] != len(entries):
            raise LedgerIntegrityError("ledger sequence is not contiguous")
        if value["previous_sha256"] != previous:
            raise LedgerIntegrityError("ledger hash chain is broken")
        if entry_hash != sha256_bytes(canonical_json(payload)):
            raise LedgerIntegrityError("ledger entry hash mismatch")
        timestamp = _parse_timestamp(value["timestamp_utc"])
        if previous_timestamp is not None and timestamp < previous_timestamp:
            raise LedgerIntegrityError("ledger timestamps move backwards")
        previous_timestamp = timestamp
        previous = str(entry_hash)
        entries.append(value)
    return entries


def _head_payload(entries: list[dict[str, object]]) -> bytes:
    return canonical_json(
        {
            "entry_count": len(entries),
            "head_sha256": str(entries[-1]["entry_sha256"]) if entries else GENESIS,
            "schema": HEAD_SCHEMA,
            "scientific_outcome": False,
        }
    )


class AppendOnlyLedger:
    def __init__(self, path: Path, *, head_path: Path | None = None) -> None:
        self.path = path
        self.head_path = head_path or path.with_name(f"{path.name}.head.json")

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        atomic_create(self.path, HEADER.encode("ascii"), mode=0o644)
        try:
            atomic_create(self.head_path, _head_payload([]), mode=0o644)
        except BaseException:
            # A ledger without its external head is invalid and intentionally
            # not removed or retried silently.
            raise

    def _verify_head(self, entries: list[dict[str, object]]) -> None:
        value = load_canonical_json(self.head_path)
        expected = json.loads(_head_payload(entries))
        if canonical_json(value) != canonical_json(expected):
            raise LedgerIntegrityError("ledger external head mismatch")

    def entries(self) -> list[dict[str, object]]:
        entries = parse_ledger(self.path.read_bytes())
        self._verify_head(entries)
        return entries

    def append(
        self,
        *,
        event: str,
        timestamp_utc: str,
        data: Mapping[str, object],
        expected_file_descriptor: int | None = None,
    ) -> dict[str, object]:
        descriptor = os.open(
            self.path, os.O_RDWR | os.O_APPEND | os.O_CLOEXEC | os.O_NOFOLLOW
        )
        try:
            if expected_file_descriptor is not None:
                if type(expected_file_descriptor) is not int:
                    raise LedgerIntegrityError("ledger anchor descriptor is malformed")
                try:
                    matches_anchor = os.path.samestat(
                        os.fstat(descriptor), os.fstat(expected_file_descriptor)
                    )
                except OSError as error:
                    raise LedgerIntegrityError(
                        "ledger anchor descriptor is unavailable"
                    ) from error
                if not matches_anchor:
                    raise LedgerIntegrityError("opened ledger differs from its anchor")
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            with os.fdopen(descriptor, "r+b", closefd=False) as target:
                target.seek(0)
                entries = parse_ledger(target.read())
                self._verify_head(entries)
                timestamp = _parse_timestamp(timestamp_utc)
                if entries and timestamp < _parse_timestamp(entries[-1]["timestamp_utc"]):
                    raise LedgerIntegrityError("ledger timestamps move backwards")
                previous = str(entries[-1]["entry_sha256"]) if entries else GENESIS
                entry = build_entry(
                    sequence=len(entries),
                    previous_sha256=previous,
                    event=event,
                    timestamp_utc=timestamp_utc,
                    data=data,
                )
                target.seek(0, os.SEEK_END)
                target.write(b"- " + canonical_json(entry))
                target.flush()
                os.fsync(target.fileno())
                entries.append(entry)
            atomic_replace(self.head_path, _head_payload(entries), mode=0o644)
            fsync_directory(self.path.parent)
            return entry
        finally:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            os.close(descriptor)
