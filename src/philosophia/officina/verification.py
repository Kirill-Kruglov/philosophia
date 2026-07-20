from __future__ import annotations

import ast
from pathlib import Path
from typing import Iterable

from .canonical import canonical_json, load_canonical_json, sha256_file
from .ledger import GENESIS, HEADER, HEAD_SCHEMA


FORBIDDEN_IMPORT_PREFIXES = (
    "philosophia.level0",
    "philosophia.level1",
    "gate_harness",
)
ENTROPY_CALLS = {
    "os.getrandom",
    "os.urandom",
    "random.SystemRandom",
    "secrets.choice",
    "secrets.randbits",
    "secrets.randbelow",
    "secrets.token_bytes",
    "torch.initial_seed",
    "torch.seed",
}
DYNAMIC_IMPORT_CALLS = {
    "__import__", "compile", "eval", "exec", "getattr",
    "importlib.import_module",
}
RANDOM_DEVICE_PATHS = {"/dev/" + name for name in ("random", "urandom")}
ALLOWED_ABSOLUTE_IMPORTS = {
    "__future__", "ast", "dataclasses", "datetime", "enum", "fcntl",
    "hashlib", "hmac", "json", "os", "pathlib", "re", "typing", "weakref",
}
ALLOWED_RELATIVE_IMPORTS = {
    "accounting", "canonical", "interlock", "ledger", "quarantine", "terminal"
}


def _dotted_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else None
    return None


def verify_source_quarantine(paths: Iterable[Path]) -> list[str]:
    failures: list[str] = []
    for path in paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        aliases: dict[str, str] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    aliases[alias.asname or alias.name.split(".")[0]] = alias.name
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    aliases[alias.asname or alias.name] = f"{module}.{alias.name}".strip(".")
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            else:
                names = []
            for name in names:
                if name.startswith(FORBIDDEN_IMPORT_PREFIXES):
                    failures.append(f"forbidden import {name} in {path}")
                top = name.split(".")[0]
                relative = isinstance(node, ast.ImportFrom) and node.level > 0
                allowed = (
                    name in ALLOWED_RELATIVE_IMPORTS
                    if relative
                    else top in ALLOWED_ABSOLUTE_IMPORTS
                )
                if not allowed:
                    failures.append(f"unreviewed import {name} in {path}")
            if isinstance(node, ast.Call):
                name = _dotted_name(node.func)
                if name:
                    first, separator, rest = name.partition(".")
                    if first in aliases:
                        name = aliases[first] + (separator + rest if separator else "")
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy call {name} in {path}")
                if name in DYNAMIC_IMPORT_CALLS:
                    failures.append(f"reflective or dynamic call {name} in {path}")
            if isinstance(node, ast.Constant) and node.value in RANDOM_DEVICE_PATHS:
                failures.append(f"system random device {node.value} in {path}")
    return failures


def verify_bootstrap(repo: Path) -> list[str]:
    failures: list[str] = []
    root = repo / "successor/officina"
    expected = {
        "README.md",
        "LINEAGE.json",
        "PATH_POLICY.json",
        "T_ENVELOPE.json",
        "T_LEDGER.md",
        "T_LEDGER.md.head.json",
        "WP1_WP2_IMPLEMENTATION.md",
    }
    actual = {path.name for path in root.iterdir() if path.is_file()}
    if actual != expected:
        failures.append(f"Officina bootstrap files differ: {sorted(actual)}")

    lineage = load_canonical_json(root / "LINEAGE.json")
    if not isinstance(lineage, dict):
        failures.append("lineage manifest is not an object")
    else:
        authorization = repo / "successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md"
        charter = repo / "successor/CHARTER_SIGNATURE.md"
        expected_lineage = {
            "authorization_commit": "d3be92f116ec10580fe28423adaac0c56119b492",
            "authorization_sha256": sha256_file(authorization),
            "charter_signature_sha256": sha256_file(charter),
            "line_identifier": "officina",
            "predecessor": "philosophia:stopped-open-non-continuation",
            "predecessor_commit": "6159b7bae12d7eb080d886d3d72f7919025b4ffa",
            "runtime_inheritance": "forbidden",
            "schema": "philosophia.officina.lineage.v1",
            "scientific_outcome": False,
        }
        if canonical_json(lineage) != canonical_json(expected_lineage):
            failures.append("lineage manifest differs from the signed bootstrap")

    policy = load_canonical_json(root / "PATH_POLICY.json")
    expected_policy = {
        "allowed_runtime_root": "successor/officina",
        "declared_engineering_fixtures": [],
        "default": "deny",
        "fixture_rule": "read-only-t-context-non-promotable",
        "forbidden_runtime_roots": [
            "experiments/level_0_grokking",
            "experiments/level_1_contact",
            "inheritance/line12_same_wall",
        ],
        "realpath_before_decision": True,
        "schema": "philosophia.officina.path-policy.v1",
        "scientific_outcome": False,
    }
    if canonical_json(policy) != canonical_json(expected_policy):
        failures.append("path policy differs from the signed bootstrap")
    envelope = load_canonical_json(root / "T_ENVELOPE.json")
    expected_envelope = {
        "activated": False,
        "candidate_registration_cap": 12,
        "checkpoint_device_hours": 40,
        "checkpoint_elapsed_calendar_hours": 48,
        "device_hour_cap": 168,
        "device_hours_are_aggregate": True,
        "ledger": "successor/officina/T_LEDGER.md",
        "schema": "philosophia.officina.t-envelope.v1",
        "scientific_outcome": False,
        "strict_s_available": False,
    }
    if canonical_json(envelope) != canonical_json(expected_envelope):
        failures.append("T envelope differs from the signed inactive bootstrap")
    ledger = (root / "T_LEDGER.md").read_bytes()
    if ledger != HEADER.encode("ascii"):
        failures.append("committed T ledger differs from exact inactive genesis")
    head = load_canonical_json(root / "T_LEDGER.md.head.json")
    expected_head = {
        "entry_count": 0,
        "head_sha256": GENESIS,
        "schema": HEAD_SCHEMA,
        "scientific_outcome": False,
    }
    if canonical_json(head) != canonical_json(expected_head):
        failures.append("committed T ledger head is not genesis")

    source_paths = sorted((repo / "src/philosophia/officina").glob("*.py"))
    failures.extend(verify_source_quarantine(source_paths))
    return failures
