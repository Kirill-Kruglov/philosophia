#!/usr/bin/env python3
"""Verify every decision currently admitted by the Philosophia repository."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from gate_harness.verify_decision import verify_decision  # noqa: E402
from philosophia.level0.decision_verifier import verify_level0_decision  # noqa: E402


def main() -> int:
    inherited = ROOT / "inheritance/line12_same_wall/experiment_A/decision.json"
    ok, reasons = verify_decision(inherited)
    print(f"{'VALID' if ok else 'INVALID'}  {inherited.relative_to(ROOT)}")
    for reason in reasons:
        print(f"  - {reason}")
    if not ok:
        return 1

    level0 = ROOT / "experiments/level_0_grokking"
    active = level0 / "outcomes/decision.json"
    if active.exists():
        ok, reasons = verify_level0_decision(
            decision_path=active,
            spec_path=level0 / "SCIENTIFIC_SPEC.json",
            lock_path=level0 / "PREREG.lock",
        )
        print(f"{'VALID' if ok else 'INVALID'}  {active.relative_to(ROOT)}")
        for reason in reasons:
            print(f"  - {reason}")
        if not ok:
            return 1
        print("OK: inherited primary and Philosophia Level 0 decisions are valid.")
        return 0

    unexpected = sorted((ROOT / "experiments").glob("**/decision.json"))
    if unexpected:
        print("FAIL: unadmitted Philosophia decisions exist")
        for path in unexpected:
            print(f"  - {path.relative_to(ROOT)}")
        return 1

    print("OK: inherited primary is VALID; no Philosophia decisions claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
