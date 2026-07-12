from __future__ import annotations

import argparse
from pathlib import Path

from philosophia.level0.outcome import run_locked_outcome


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--resume", action="store_true")
    arguments = parser.parse_args()
    report = run_locked_outcome(
        run_id=arguments.run_id,
        output_root=arguments.output_root,
        spec_path=arguments.spec,
        lock_path=arguments.lock,
        resume=arguments.resume,
    )
    print(report)


if __name__ == "__main__":
    main()
