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
BUILTIN_DYNAMIC_IMPORT_CALLS = {
    name for name in DYNAMIC_IMPORT_CALLS if "." not in name
}
RANDOM_DEVICE_PATHS = {"/dev/" + name for name in ("random", "urandom")}
ALLOWED_ABSOLUTE_IMPORTS = {
    "__future__", "ast", "dataclasses", "datetime", "enum", "fcntl",
    "hashlib", "hmac", "json", "os", "pathlib", "re", "subprocess", "time",
    "typing", "weakref",
}
ALLOWED_RELATIVE_IMPORTS = {
    "accounting", "activation", "canonical", "checkpoint", "interlock", "ledger",
    "quarantine", "runtime", "terminal", "verification", "world",
}

PRODUCTION_TEST_SURFACE_SYMBOLS = frozenset(
    {
        "test_world_capability",
        "issue_test_t_contact_harness",
        "evaluate_test_query",
        "record_test_t_contact",
        "TestWorldCapability",
        "TestTContactHarness",
    }
)
PRODUCTION_MANIFEST_RELATIVE = Path(
    "successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json"
)
PRODUCTION_MANIFEST_SCHEMA = "philosophia.officina.production-call-graph.v1"
PRODUCTION_ROOTS = (
    "scripts/officina_activate_t.py",
    "scripts/verify_officina_active.py",
    "src/philosophia/officina/generic_harness.py",
)


def _resolved_symbol(
    node: ast.AST, aliases: dict[str, str], local_symbols: dict[str, str]
) -> str | None:
    if isinstance(node, ast.Name):
        return local_symbols.get(node.id, aliases.get(node.id, node.id))
    if isinstance(node, ast.Attribute):
        prefix = _resolved_symbol(node.value, aliases, local_symbols)
        return f"{prefix}.{node.attr}" if prefix else None
    return None


def _normalized_capability_name(name: str | None) -> str | None:
    if name is not None and name.startswith("builtins."):
        builtin_name = name.removeprefix("builtins.")
        if builtin_name in BUILTIN_DYNAMIC_IMPORT_CALLS:
            return builtin_name
    return name


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
                    bound = alias.asname or alias.name.split(".")[0]
                    resolved = alias.name if alias.asname else alias.name.split(".")[0]
                    aliases[bound] = resolved
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
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imported = _normalized_capability_name(
                        f"{node.module or ''}.{alias.name}".strip(".")
                    )
                    if imported in ENTROPY_CALLS:
                        failures.append(f"entropy reference {imported} in {path}")
                    if imported in DYNAMIC_IMPORT_CALLS:
                        failures.append(
                            f"reflective or dynamic reference {imported} in {path}"
                        )
            is_loaded_symbol = (
                isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)
            ) or (
                isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load)
            )
            if is_loaded_symbol:
                name = _normalized_capability_name(
                    _resolved_symbol(node, aliases, local_symbols)
                )
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy reference {name} in {path}")
                if name in DYNAMIC_IMPORT_CALLS:
                    failures.append(
                        f"reflective or dynamic reference {name} in {path}"
                    )
            if isinstance(node, ast.Call):
                name = _normalized_capability_name(
                    _resolved_symbol(node.func, aliases, local_symbols)
                )
                if name in ENTROPY_CALLS:
                    failures.append(f"entropy call {name} in {path}")
                if name in DYNAMIC_IMPORT_CALLS:
                    failures.append(f"reflective or dynamic call {name} in {path}")
            static_value = _static_string(node, static_strings)
            if static_value in RANDOM_DEVICE_PATHS:
                failures.append(f"system random device {static_value} in {path}")
    return failures


def verify_production_boundary(repo: Path, reviewed_paths: Iterable[str]) -> list[str]:
    """Verify the closed reviewed Python graph and lint forbidden capabilities."""

    failures: list[str] = []
    reviewed = tuple(sorted(set(reviewed_paths)))
    python_paths = tuple(relative for relative in reviewed if relative.endswith(".py"))
    computed_edges: dict[str, list[str]] = {}

    def module_context(relative: str) -> tuple[tuple[str, ...], bool]:
        path = Path(relative)
        parts = path.with_suffix("").parts
        if parts and parts[0] == "src":
            parts = parts[1:]
        is_package = parts[-1:] == ("__init__",)
        if is_package:
            parts = parts[:-1]
        return tuple(parts), is_package

    def resolve_module(name: str) -> tuple[str | None, bool]:
        parts = tuple(part for part in name.split(".") if part)
        if not parts:
            return None, False
        candidates: set[str] = set()
        for base in (repo, repo / "src"):
            source = base.joinpath(*parts).with_suffix(".py")
            package = base.joinpath(*parts, "__init__.py")
            for candidate in (source, package):
                if candidate.is_file() and not candidate.is_symlink():
                    candidates.add(candidate.relative_to(repo).as_posix())
        if len(candidates) > 1:
            return None, True
        return (next(iter(candidates)), False) if candidates else (None, False)

    def imported_modules(relative: str, tree: ast.Module) -> tuple[set[str], bool]:
        current_parts, is_package = module_context(relative)
        current_package = current_parts if is_package else current_parts[:-1]
        dependencies: set[str] = set()
        ambiguous = False
        for node in ast.walk(tree):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    keep = len(current_package) - (node.level - 1)
                    if keep < 0:
                        ambiguous = True
                        continue
                    base_parts = current_package[:keep]
                    if node.module:
                        base_parts = (*base_parts, *node.module.split("."))
                    base = ".".join(base_parts)
                else:
                    base = node.module or ""
                if base:
                    names.append(base)
                for alias in node.names:
                    if alias.name != "*":
                        candidate = f"{base}.{alias.name}".strip(".")
                        if candidate:
                            names.append(candidate)
            for name in names:
                resolved, is_ambiguous = resolve_module(name)
                ambiguous = ambiguous or is_ambiguous
                if resolved is not None:
                    dependencies.add(resolved)
        return dependencies, ambiguous

    for relative in python_paths:
        path = repo / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"reviewed production source is missing or aliased: {relative}")
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as error:
            failures.append(f"reviewed production source cannot be parsed: {relative}: {error}")
            continue
        aliases: dict[str, str] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    aliases[alias.asname or alias.name.split(".")[0]] = alias.name
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    aliases[alias.asname or alias.name] = f"{module}.{alias.name}".strip(".")
        local_symbols = _local_symbol_table(tree, aliases)
        static_strings = _static_string_table(tree)
        dependencies, ambiguous = imported_modules(relative, tree)
        if ambiguous:
            failures.append(f"production source has ambiguous local imports: {relative}")
        for node in ast.walk(tree):
            imported_names: list[str] = []
            if isinstance(node, ast.Import):
                imported_names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_names.append(node.module or "")
            for imported in imported_names:
                if imported.startswith(FORBIDDEN_IMPORT_PREFIXES):
                    failures.append(
                        f"production source uses quarantined import {imported}: {relative}"
                    )
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imported = _normalized_capability_name(
                        f"{node.module or ''}.{alias.name}".strip(".")
                    )
                    if imported in ENTROPY_CALLS:
                        failures.append(
                            f"production source references entropy {imported}: {relative}"
                        )
                    if imported in DYNAMIC_IMPORT_CALLS:
                        failures.append(
                            "production source references dynamic resolution "
                            f"{imported}: {relative}"
                        )
            names: list[str] = []
            if isinstance(node, ast.ImportFrom):
                names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.Name):
                names.append(node.id)
            elif isinstance(node, ast.Attribute):
                names.append(node.attr)
            for name in names:
                if path.name != "world.py" and name in PRODUCTION_TEST_SURFACE_SYMBOLS:
                    failures.append(
                        f"production source references test-world symbol {name}: {relative}"
                    )
            is_loaded_symbol = (
                isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)
            ) or (
                isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load)
            )
            if is_loaded_symbol:
                resolved = _normalized_capability_name(
                    _resolved_symbol(node, aliases, local_symbols)
                )
                if resolved in ENTROPY_CALLS:
                    failures.append(
                        f"production source references entropy {resolved}: {relative}"
                    )
                if resolved in DYNAMIC_IMPORT_CALLS:
                    failures.append(
                        f"production source references dynamic resolution {resolved}: {relative}"
                    )
            if isinstance(node, ast.Call):
                resolved = _normalized_capability_name(
                    _resolved_symbol(node.func, aliases, local_symbols)
                )
                if resolved in DYNAMIC_IMPORT_CALLS:
                    failures.append(
                        f"production source uses dynamic resolution {resolved}: {relative}"
                    )
                if resolved in ENTROPY_CALLS:
                    failures.append(
                        f"production source uses entropy {resolved}: {relative}"
                    )
            static_value = _static_string(node, static_strings)
            if static_value in RANDOM_DEVICE_PATHS:
                failures.append(
                    f"production source references system random device "
                    f"{static_value}: {relative}"
                )
        missing = dependencies - set(python_paths)
        if missing:
            failures.append(
                f"production source has omitted local dependencies {relative}: {sorted(missing)}"
            )
        computed_edges[relative] = sorted(dependencies)

    roots = set(PRODUCTION_ROOTS)
    missing_roots = roots - set(python_paths)
    if missing_roots:
        failures.append(f"production executable roots are unreviewed: {sorted(missing_roots)}")
    reachable: set[str] = set()
    pending = list(sorted(roots & set(python_paths)))
    while pending:
        relative = pending.pop()
        if relative in reachable:
            continue
        reachable.add(relative)
        pending.extend(
            dependency
            for dependency in computed_edges.get(relative, ())
            if dependency in computed_edges and dependency not in reachable
        )
    unreachable = set(python_paths) - reachable
    if unreachable:
        failures.append(
            f"reviewed production sources are unreachable from roots: {sorted(unreachable)}"
        )

    manifest_path = repo / PRODUCTION_MANIFEST_RELATIVE
    try:
        manifest = load_canonical_json(manifest_path)
    except (OSError, ValueError) as error:
        failures.append(f"production call-graph manifest is unavailable: {error}")
        return sorted(set(failures))
    expected_keys = {
        "schema", "scientific_outcome", "roots", "reachable_sources",
        "import_edges", "dynamic_resolution",
    }
    if not isinstance(manifest, dict) or set(manifest) != expected_keys:
        failures.append("production call-graph manifest fields differ")
        return sorted(set(failures))
    if (
        manifest["schema"] != PRODUCTION_MANIFEST_SCHEMA
        or manifest["scientific_outcome"] is not False
        or manifest["dynamic_resolution"] is not False
    ):
        failures.append("production call-graph manifest contract differs")
    if manifest["roots"] != list(PRODUCTION_ROOTS):
        failures.append("production call-graph roots differ")
    if manifest["reachable_sources"] != sorted(reachable):
        failures.append("production reachable-source closure differs")
    reachable_edges = {
        relative: computed_edges[relative]
        for relative in sorted(reachable)
        if relative in computed_edges
    }
    if canonical_json(manifest["import_edges"]) != canonical_json(reachable_edges):
        failures.append("production import-edge closure differs")
    return sorted(set(failures))


def verify_bootstrap(repo: Path, *, allow_activation_authorization: bool = False) -> list[str]:
    failures: list[str] = []
    root = repo / "successor/officina"
    expected = {
        "README.md",
        "LINEAGE.json",
        "PATH_POLICY.json",
        "T_ENVELOPE.json",
        "T_LEDGER.md",
        "T_LEDGER.md.head.json",
        "T_ACTIVATION_IMPLEMENTATION.md",
        "WP1_WP2_IMPLEMENTATION.md",
    }
    if allow_activation_authorization:
        expected.add("OFFICINA_T_ACTIVATION_AUTHORIZATION.json")
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
    if isinstance(envelope, dict) and envelope.get("activated") is True:
        return ["ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER"]
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

    from .runtime import verify_runtime_lock

    failures.extend(verify_runtime_lock(repo))

    source_paths = sorted((repo / "src/philosophia/officina").glob("*.py"))
    failures.extend(verify_source_quarantine(source_paths))
    return failures
