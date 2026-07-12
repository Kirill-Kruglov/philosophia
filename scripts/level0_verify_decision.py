from __future__ import annotations

import argparse
from pathlib import Path

from philosophia.level0.decision_verifier import verify_level0_decision


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--decision", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    arguments = parser.parse_args()
    ok, reasons = verify_level0_decision(
        decision_path=arguments.decision,
        spec_path=arguments.spec,
        lock_path=arguments.lock,
    )
    print("VALID" if ok else "INVALID")
    for reason in reasons:
        print(f"- {reason}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
