#!/usr/bin/env python3
"""Fail if any file copied verbatim from Ascesis has changed."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKSUMS = ROOT / "SOURCE_SHA256SUMS"


def main() -> int:
    failures: list[str] = []
    checked = 0
    for raw in CHECKSUMS.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split("  ", 1)
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing: {relative}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        checked += 1
        if actual != expected:
            failures.append(f"changed: {relative} ({actual} != {expected})")

    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"OK: {checked} inherited files match the extraction manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
