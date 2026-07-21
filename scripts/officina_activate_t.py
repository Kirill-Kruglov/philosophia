#!/usr/bin/env python3
"""One-shot Officina T activation driver; inert without exact authorization."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from philosophia.officina.activation import activate_repository  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", required=True)
    arguments = parser.parse_args()
    authorization = (ROOT / arguments.authorization).resolve()
    committed = activate_repository(ROOT, authorization)
    print(
        json.dumps(
            {
                "commit": committed,
                "kind": "officina-t-activation",
                "scientific_outcome": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
