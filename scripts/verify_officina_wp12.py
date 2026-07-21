#!/usr/bin/env python3
"""Verify the authorized Officina WP-1/WP-2 bootstrap without running it."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from philosophia.officina.verification import verify_bootstrap  # noqa: E402


def main() -> int:
    failures = verify_bootstrap(ROOT)
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        if failures == ["ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER"]:
            print("ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER")
        return 1
    print("OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
