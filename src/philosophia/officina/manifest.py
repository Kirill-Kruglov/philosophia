from __future__ import annotations

import re
from typing import Mapping

from .canonical import canonical_json, sha256_bytes


_HEX40 = re.compile(r"[0-9a-f]{40}")
_FIELDS = {
    "schema",
    "code_commit",
    "stack_id",
    "initialization",
    "optimizer",
    "policy",
    "interface",
    "config",
}


def canonical_candidate_manifest(value: Mapping[str, object]) -> bytes:
    if set(value) != _FIELDS:
        missing = sorted(_FIELDS - set(value))
        unknown = sorted(set(value) - _FIELDS)
        raise ValueError(f"candidate manifest fields differ: missing={missing}, unknown={unknown}")
    if value["schema"] != "philosophia.officina.candidate.v1":
        raise ValueError("candidate manifest schema mismatch")
    commit = value["code_commit"]
    if not isinstance(commit, str) or _HEX40.fullmatch(commit) is None:
        raise ValueError("candidate code commit must be lowercase 40-hex")
    stack_id = value["stack_id"]
    if not isinstance(stack_id, str) or not stack_id:
        raise ValueError("candidate stack_id must be named")
    initialization = value["initialization"]
    if initialization != {"checkpoint": None, "kind": "from-scratch"}:
        raise ValueError("successor candidates must initialize from scratch")
    for field in ("optimizer", "policy", "interface", "config"):
        if not isinstance(value[field], dict):
            raise ValueError(f"candidate {field} must be an object")
    return canonical_json(dict(value))


def candidate_id(value: Mapping[str, object]) -> str:
    return sha256_bytes(canonical_candidate_manifest(value))


def behaviorally_equivalent(
    left: Mapping[str, object], right: Mapping[str, object]
) -> bool:
    return canonical_candidate_manifest(left) == canonical_candidate_manifest(right)
