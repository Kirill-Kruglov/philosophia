from __future__ import annotations

import argparse
from pathlib import Path

from philosophia.level0.scout import run_timing_storage_scout


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the bounded Level 0 timing/storage non-outcome scout."
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()
    report = run_timing_storage_scout(output_dir=arguments.output_dir)
    print(report)


if __name__ == "__main__":
    main()
