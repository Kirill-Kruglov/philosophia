from __future__ import annotations

import fcntl
import json
import os
from pathlib import Path
from typing import Mapping

from .canonical import canonical_json, fsync_directory, sha256_bytes


HEADER = (
    "# Officina T Ledger\n\n"
    "Status: `NOT_ACTIVATED`\n\n"
    "This is an append-only public ledger skeleton. Machine entries, once authorized,\n"
    "are canonical JSON objects prefixed by `- ` and linked by SHA-256. WP-1/WP-2\n"
    "tests use temporary ledgers only. No real T entry exists in this file.\n"
)
GENESIS = "0" * 64


class LedgerIntegrityError(ValueError):
    pass


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
        entry_hash = value.get("entry_sha256")
        payload = {key: item for key, item in value.items() if key != "entry_sha256"}
        if canonical_json(value).decode("ascii").rstrip("\n") != line[2:]:
            raise LedgerIntegrityError("ledger entry is not canonical JSON")
        if value.get("sequence") != len(entries):
            raise LedgerIntegrityError("ledger sequence is not contiguous")
        if value.get("previous_sha256") != previous:
            raise LedgerIntegrityError("ledger hash chain is broken")
        if entry_hash != sha256_bytes(canonical_json(payload)):
            raise LedgerIntegrityError("ledger entry hash mismatch")
        previous = str(entry_hash)
        entries.append(value)
    return entries


class AppendOnlyLedger:
    def __init__(self, path: Path) -> None:
        self.path = path

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor = os.open(
            self.path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o644,
        )
        with os.fdopen(descriptor, "wb") as target:
            target.write(HEADER.encode("ascii"))
            target.flush()
            os.fsync(target.fileno())
        fsync_directory(self.path.parent)

    def entries(self) -> list[dict[str, object]]:
        return parse_ledger(self.path.read_bytes())

    def append(
        self,
        *,
        event: str,
        timestamp_utc: str,
        data: Mapping[str, object],
    ) -> dict[str, object]:
        descriptor = os.open(self.path, os.O_RDWR | os.O_APPEND)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            with os.fdopen(descriptor, "r+b", closefd=False) as target:
                target.seek(0)
                entries = parse_ledger(target.read())
                previous = str(entries[-1]["entry_sha256"]) if entries else GENESIS
                entry = build_entry(
                    sequence=len(entries),
                    previous_sha256=previous,
                    event=event,
                    timestamp_utc=timestamp_utc,
                    data=data,
                )
                line = b"- " + canonical_json(entry)
                target.seek(0, os.SEEK_END)
                target.write(line)
                target.flush()
                os.fsync(target.fileno())
            fsync_directory(self.path.parent)
            return entry
        finally:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            os.close(descriptor)
