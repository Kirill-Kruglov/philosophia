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


def _resolved_symbol(
    node: ast.AST, aliases: dict[str, str], local_symbols: dict[str, str]
) -> str | None:
    if isinstance(node, ast.Name):
        return local_symbols.get(node.id, aliases.get(node.id, node.id))
    if isinstance(node, ast.Attribute):
        prefix = _resolved_symbol(node.value, aliases, local_symbols)
        return f"{prefix}.{node.attr}" if prefix else None
    return None


def _assignment_pairs(tree: ast.AST) -> list[tuple[str, ast.AST]]:
    pairs: list[tuple[str, ast.AST]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    pairs.append((target.id, node.value))
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.value is not None:
                pairs.append((node.target.id, node.value))
    return pairs


def _local_symbol_table(
    tree: ast.AST, aliases: dict[str, str]
) -> dict[str, str]:
    result: dict[str, str] = {}
    assignments = _assignment_pairs(tree)
    for _ in range(len(assignments) + 1):
        changed = False
        for target, value in assignments:
            resolved = _resolved_symbol(value, aliases, result)
            if resolved is not None and result.get(target) != resolved:
                result[target] = resolved
                changed = True
        if not changed:
            break
    return result


def _static_string(node: ast.AST, values: dict[str, str]) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return values.get(node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _static_string(node.left, values)
        right = _static_string(node.right, values)
        return left + right if left is not None and right is not None else None
    if isinstance(node, ast.FormattedValue):
        return _static_string(node.value, values)
    if isinstance(node, ast.JoinedStr):
        parts = [_static_string(value, values) for value in node.values]
        return "".join(parts) if all(part is not None for part in parts) else None
    return None


def _static_string_table(tree: ast.AST) -> dict[str, str]:
    result: dict[str, str] = {}
    assignments = _assignment_pairs(tree)
    for _ in range(len(assignments) + 1):
        changed = False
        for target, value in assignments:
            resolved = _static_string(value, result)
            if resolved is not None and result.get(target) != resolved:
                result[target] = resolved
                changed = True
        if not changed:
            break
    return result


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
                    if alias.name != "*":
                        aliases[alias.asname or alias.name] = (
                            f"{module}.{alias.name}".strip(".")
                        )
        local_symbols = _local_symbol_table(tree, aliases)
        static_strings = _static_string_table(tree)
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
            if isinstance(node, ast.ImportFrom) and any(
                alias.name == "*" for alias in node.names
            ):
                failures.append(f"star import is forbidden in {path}")
            is_loaded_symbol = (
                isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)
            ) or (
                isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load)
            )
            if is_loaded_symbol:
                name = _resolved_symbol(node, aliases, local_symbols)
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy reference {name} in {path}")
                if name in DYNAMIC_IMPORT_CALLS:
                    failures.append(
                        f"reflective or dynamic reference {name} in {path}"
                    )
            if isinstance(node, ast.Call):
                name = _resolved_symbol(node.func, aliases, local_symbols)
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy call {name} in {path}")
                if name in DYNAMIC_IMPORT_CALLS:
                    failures.append(f"reflective or dynamic call {name} in {path}")
            static_value = _static_string(node, static_strings)
            if static_value in RANDOM_DEVICE_PATHS:
                failures.append(f"system random device {static_value} in {path}")
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
