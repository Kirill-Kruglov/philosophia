from __future__ import annotations

import argparse
from pathlib import Path

from philosophia.level0.prefix_check import run_companion_v2_prefix_check


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()
    report = run_companion_v2_prefix_check(output_dir=arguments.output_dir)
    print(report)


if __name__ == "__main__":
    main()
