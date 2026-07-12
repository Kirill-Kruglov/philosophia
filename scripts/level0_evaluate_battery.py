from __future__ import annotations

import argparse
from pathlib import Path

from philosophia.level0.outcome_evaluator import evaluate_locked_battery


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    arguments = parser.parse_args()
    decision = evaluate_locked_battery(
        output_root=arguments.output_root,
        spec_path=arguments.spec,
        lock_path=arguments.lock,
    )
    print(decision)


if __name__ == "__main__":
    main()
