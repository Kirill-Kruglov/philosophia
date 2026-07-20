from __future__ import annotations

import ast
from pathlib import Path
from typing import Iterable

from .canonical import load_canonical_json, sha256_file


FORBIDDEN_IMPORT_PREFIXES = (
    "philosophia.level0",
    "philosophia.level1",
    "gate_harness",
)
ENTROPY_CALLS = {
    "os.urandom",
    "random.SystemRandom",
    "secrets.choice",
    "secrets.randbits",
    "secrets.token_bytes",
    "torch.initial_seed",
    "torch.seed",
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
            if isinstance(node, ast.Call):
                name = _dotted_name(node.func)
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy call {name} in {path}")
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
        if lineage.get("authorization_sha256") != sha256_file(authorization):
            failures.append("authorization signature hash mismatch")
        if lineage.get("charter_signature_sha256") != sha256_file(charter):
            failures.append("charter signature hash mismatch")
        if lineage.get("runtime_inheritance") != "forbidden":
            failures.append("runtime inheritance is not forbidden")
        predecessor = lineage.get("predecessor_commit")
        if not isinstance(predecessor, str) or len(predecessor) != 40:
            failures.append("predecessor commit is not pinned")

    policy = load_canonical_json(root / "PATH_POLICY.json")
    if not isinstance(policy, dict) or policy.get("default") != "deny":
        failures.append("path policy is not deny-by-default")
    envelope = load_canonical_json(root / "T_ENVELOPE.json")
    if not isinstance(envelope, dict) or envelope.get("activated") is not False:
        failures.append("T envelope must remain inactive")
    ledger = (root / "T_LEDGER.md").read_text(encoding="utf-8")
    if "Status: `NOT_ACTIVATED`" not in ledger or '\n- {' in ledger:
        failures.append("committed T ledger is not an empty inactive skeleton")

    source_paths = sorted((repo / "src/philosophia/officina").glob("*.py"))
    failures.extend(verify_source_quarantine(source_paths))
    return failures
