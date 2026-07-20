from __future__ import annotations

import re
from typing import Mapping

from .canonical import canonical_json, sha256_bytes


_HEX40 = re.compile(r"[0-9a-f]{40}")
_FIELDS = {
    "schema",
    "provenance_commit",
    "behavior_source_sha256",
    "stack_id",
    "initialization",
    "optimizer",
    "policy",
    "interface",
    "config",
    "inert_metadata",
}
_INERT_FIELDS = {
    "comments",
    "display_name",
    "packaging",
    "serialization_order",
    "timestamps",
}


def canonical_candidate_manifest(value: Mapping[str, object]) -> bytes:
    if set(value) != _FIELDS:
        missing = sorted(_FIELDS - set(value))
        unknown = sorted(set(value) - _FIELDS)
        raise ValueError(f"candidate manifest fields differ: missing={missing}, unknown={unknown}")
    if value["schema"] != "philosophia.officina.candidate.v2":
        raise ValueError("candidate manifest schema mismatch")
    commit = value["provenance_commit"]
    if not isinstance(commit, str) or _HEX40.fullmatch(commit) is None:
        raise ValueError("candidate provenance commit must be lowercase 40-hex")
    source_hash = value["behavior_source_sha256"]
    if not isinstance(source_hash, str) or re.fullmatch(r"[0-9a-f]{64}", source_hash) is None:
        raise ValueError("candidate behavior source must be lowercase SHA-256")
    stack_id = value["stack_id"]
    if not isinstance(stack_id, str) or not stack_id:
        raise ValueError("candidate stack_id must be named")
    initialization = value["initialization"]
    if initialization != {"checkpoint": None, "kind": "from-scratch"}:
        raise ValueError("successor candidates must initialize from scratch")
    for field in ("optimizer", "policy", "interface", "config"):
        if not isinstance(value[field], dict):
            raise ValueError(f"candidate {field} must be an object")
    inert = value["inert_metadata"]
    if not isinstance(inert, dict) or not set(inert).issubset(_INERT_FIELDS):
        raise ValueError("candidate inert metadata contains an unrecognized field")
    return canonical_json(dict(value))


def canonical_behavior_manifest(value: Mapping[str, object]) -> bytes:
    normalized = dict(value)
    canonical_candidate_manifest(normalized)
    normalized.pop("provenance_commit")
    normalized.pop("inert_metadata")
    return canonical_json(normalized)


def candidate_id(value: Mapping[str, object]) -> str:
    return sha256_bytes(canonical_behavior_manifest(value))


def behaviorally_equivalent(
    left: Mapping[str, object], right: Mapping[str, object]
) -> bool:
    return canonical_behavior_manifest(left) == canonical_behavior_manifest(right)
