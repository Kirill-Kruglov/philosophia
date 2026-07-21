#!/usr/bin/env python3
"""Verify an activated Officina T tree without issuing any capability."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from philosophia.officina.activation import verify_active_repository  # noqa: E402


def main() -> int:
    failures = verify_active_repository(ROOT, require_activation_commit=True)
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print("OK: Officina T active state is canonical and fail-closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
