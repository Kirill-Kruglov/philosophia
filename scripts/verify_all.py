#!/usr/bin/env python3
"""Verify every decision currently admitted by the bootstrap repository."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from gate_harness.verify_decision import verify_decision  # noqa: E402


def main() -> int:
    inherited = ROOT / "inheritance/line12_same_wall/experiment_A/decision.json"
    ok, reasons = verify_decision(inherited)
    print(f"{'VALID' if ok else 'INVALID'}  {inherited.relative_to(ROOT)}")
    for reason in reasons:
        print(f"  - {reason}")
    if not ok:
        return 1

    active_decisions = sorted((ROOT / "experiments").glob("level_*/decision.json"))
    if active_decisions:
        print("FAIL: active decisions exist but have not yet been admitted here")
        for path in active_decisions:
            print(f"  - {path.relative_to(ROOT)}")
        return 1

    print("OK: inherited primary is VALID; no Philosophia decisions claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
