#!/usr/bin/env python3
"""Bounded fresh-process probe of Peano action enumeration order.

Read-only instrument diagnostic. It performs no proof search, training, model
load, source mutation or network access.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
MINIMO_LEARNING = Path("/home/master/llm_projects/minimo/learning")
THEORY_PATH = MINIMO_LEARNING / "theories" / "propositional-logic.p"
OUTPUT_PATH = HERE / "PHASE1_ACTION_ORDER_PROBE_18_results.json"
WORKERS = 8
STATEMENT = "[('P : prop) -> (not 'P) -> 'P -> false]"
PREMISES = [
    "and_i",
    "and_el",
    "and_er",
    "or_il",
    "or_ir",
    "or_e",
    "not_i",
    "not_e",
    "exfalso",
    "iff_i",
    "iff_el",
    "iff_er",
    "em",
]


class FailClosed(RuntimeError):
    pass


def canonical_bytes(value) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True) + "\n").encode(
        "ascii"
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def choose_unique(node, text: str):
    matches = [action for action in node.actions if str(action) == text]
    if len(matches) != 1:
        raise FailClosed("action %r matched %d times" % (text, len(matches)))
    return node.expand(matches[0])


def worker() -> int:
    sys.path.insert(0, str(MINIMO_LEARNING))
    import peano  # pylint: disable=import-outside-toplevel
    from proofsearch import HolophrasmNode  # pylint: disable=import-outside-toplevel

    theory = THEORY_PATH.read_text(encoding="ascii")
    node = HolophrasmNode([peano.PyProofState(theory, PREMISES, STATEMENT)])
    for _ in range(3):
        node = choose_unique(node, "intro.")
    node = choose_unique(node, "a not_e")
    actions = [str(action) for action in node.actions]
    if len(actions) != len(set(actions)):
        raise FailClosed("worker returned duplicate action strings")
    sys.stdout.buffer.write(canonical_bytes({"ordered_actions": actions}))
    return 0


def run_worker(index: int) -> dict:
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--worker"],
        cwd=str(MINIMO_LEARNING),
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise FailClosed(
            "worker %d failed (%d): %s"
            % (index, completed.returncode, completed.stderr.strip())
        )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise FailClosed("worker %d returned malformed JSON" % index) from exc
    actions = payload.get("ordered_actions")
    if not isinstance(actions, list) or not actions or not all(
        isinstance(action, str) for action in actions
    ):
        raise FailClosed("worker %d returned malformed actions" % index)
    if len(actions) != len(set(actions)):
        raise FailClosed("worker %d returned duplicate actions" % index)
    return {
        "index": index,
        "ordered_actions": actions,
        "ordered_sequence_sha256": sha256_bytes(canonical_bytes(actions)),
    }


def parent() -> int:
    theory_bytes = THEORY_PATH.read_bytes()
    rows = [run_worker(index) for index in range(WORKERS)]
    sorted_sets = [sorted(row["ordered_actions"]) for row in rows]
    expected = sorted_sets[0]
    if any(actions != expected for actions in sorted_sets[1:]):
        raise FailClosed("fresh workers returned different action sets")
    set_sha256 = sha256_bytes(canonical_bytes(expected))
    ordered_hashes = sorted(
        {row["ordered_sequence_sha256"] for row in rows}
    )
    distinct_count = len(ordered_hashes)
    status = (
        "ORDER_VARIATION_OBSERVED"
        if distinct_count > 1
        else "NO_VARIATION_OBSERVED_IN_BOUNDED_PROBE"
    )
    result = {
        "action_count": len(expected),
        "distinct_order_count": distinct_count,
        "distinct_order_sha256": ordered_hashes,
        "no_determinism_claim_if_single_order": True,
        "premises": PREMISES,
        "pythonhashseed": "0",
        "schema": "phase1-action-order-probe-18.v1",
        "sorted_action_set": expected,
        "sorted_action_set_sha256": set_sha256,
        "statement": STATEMENT,
        "status": status,
        "theory": {
            "bytes": len(theory_bytes),
            "path": str(THEORY_PATH),
            "sha256": sha256_bytes(theory_bytes),
        },
        "worker_count": WORKERS,
        "workers": rows,
    }
    OUTPUT_PATH.write_bytes(
        (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("ascii")
    )
    print("wrote %s" % OUTPUT_PATH)
    print("status=%s distinct_order_count=%d" % (status, distinct_count))
    return 0


def main() -> int:
    try:
        if sys.argv[1:] == ["--worker"]:
            return worker()
        if sys.argv[1:]:
            raise FailClosed("unexpected arguments: %r" % sys.argv[1:])
        return parent()
    except FailClosed as exc:
        sys.stderr.write("FAIL CLOSED: %s\n" % exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
