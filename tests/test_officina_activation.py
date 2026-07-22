from __future__ import annotations

import ast
import json
from pathlib import Path
import shutil
import subprocess

import pytest

from philosophia.officina.activation import (
    ACTIVATION_TOKEN,
    AUTHORIZATION_RELATIVE,
    AUTHORIZATION_SCHEMA,
    CLAIM_RELATIVE,
    GENERIC_HARNESS_RELATIVE,
    GOVERNING_PATHS,
    IMMUTABLE_CONTROL_PATHS,
    INVALIDITY_RELATIVE,
    PRODUCTION_MANIFEST_RELATIVE,
    PROTOCOL_PATHS,
    RECORD_RELATIVE,
    STATE_RELATIVE,
    ActivationRefused,
    activate_repository,
    canonical_paths,
    verify_active_repository,
)
from philosophia.officina.canonical import canonical_json, sha256_file
from philosophia.officina.ledger import AppendOnlyLedger
from philosophia.officina.verification import (
    PRODUCTION_MANIFEST_SCHEMA,
    PRODUCTION_ROOTS,
    verify_bootstrap,
    verify_production_boundary,
)


REPO = Path(__file__).resolve().parent.parent


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True
    ).stdout.strip()


def _local_edges(repo: Path, python_paths: list[str]) -> dict[str, list[str]]:
    edges: dict[str, list[str]] = {}
    for relative in python_paths:
        tree = ast.parse((repo / relative).read_text(encoding="utf-8"))
        dependencies: set[str] = set()
        for node in ast.walk(tree):
            module = ""
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if node.level > 0 and relative.startswith("src/philosophia/officina/"):
                    module = f"philosophia.officina.{module}".rstrip(".")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.startswith("philosophia.officina."):
                        dependencies.add(
                            "src/philosophia/officina/"
                            + alias.name.rsplit(".", 1)[-1]
                            + ".py"
                        )
            if module.startswith("philosophia.officina."):
                dependencies.add(
                    "src/philosophia/officina/" + module.rsplit(".", 1)[-1] + ".py"
                )
        edges[relative] = sorted(dependencies)
    return edges


def _mirror(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "mirror"
    (repo / "src/philosophia").mkdir(parents=True)
    shutil.copytree(REPO / "src/philosophia/officina", repo / "src/philosophia/officina")
    shutil.copytree(REPO / "successor/officina", repo / "successor/officina")
    for relative_string in (
        *GOVERNING_PATHS,
        *PROTOCOL_PATHS,
        "successor/CHARTER_SIGNATURE.md",
    ):
        relative = Path(relative_string)
        target = repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / relative, target)
    (repo / "scripts").mkdir()
    for name in ("officina_activate_t.py", "verify_officina_active.py"):
        shutil.copy2(REPO / "scripts" / name, repo / "scripts" / name)
    harness = repo / GENERIC_HARNESS_RELATIVE
    harness.write_text(
        '"""Reviewed mirror-only harness fixture."""\n'
        'from .checkpoint import write_pause_checkpoint\n'
        'from .interlock import ExecutionNotAuthorized\n'
        'from .terminal import QTerminal\n'
        'from .world import TDevWorld\n'
        'HARNESS_REVIEWED = True\n',
        encoding="ascii",
    )
    reviewed_python = sorted(
        {
            *IMMUTABLE_CONTROL_PATHS,
            GENERIC_HARNESS_RELATIVE.as_posix(),
            "src/philosophia/officina/quarantine.py",
        }
    )
    manifest_path = repo / PRODUCTION_MANIFEST_RELATIVE
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_bytes(
        canonical_json(
            {
                "schema": PRODUCTION_MANIFEST_SCHEMA,
                "scientific_outcome": False,
                "roots": list(PRODUCTION_ROOTS),
                "reachable_sources": reviewed_python,
                "import_edges": _local_edges(repo, reviewed_python),
                "dynamic_resolution": False,
            }
        )
    )
    _git(repo, "init", "-q")
    _git(repo, "config", "user.name", "Officina Test")
    _git(repo, "config", "user.email", "officina-test@example.invalid")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "reviewed implementation")
    reviewed_head = _git(repo, "rev-parse", "HEAD")

    reviewed_paths = [*reviewed_python, PRODUCTION_MANIFEST_RELATIVE.as_posix()]
    source_hashes = {
        relative: sha256_file(repo / relative) for relative in reviewed_paths
    }
    authorization = {
        "schema": AUTHORIZATION_SCHEMA,
        "scientific_outcome": False,
        "execution_once": True,
        "token": ACTIVATION_TOKEN,
        "reviewed_code_head": reviewed_head,
        "reviewed_source_paths": reviewed_paths,
        "reviewed_source_sha256": source_hashes,
        "governing_sha256": {
            relative: sha256_file(repo / relative) for relative in GOVERNING_PATHS
        },
        "protocol_sha256": {
            relative: sha256_file(repo / relative) for relative in PROTOCOL_PATHS
        },
        "envelope_token": "I_SELECT_T_ENVELOPE_ONE_WEEK",
        "device_policy_token": "I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK",
        "canonical_paths": canonical_paths(repo),
        "command": (
            ".venv/bin/python scripts/officina_activate_t.py "
            "--authorization successor/officina/OFFICINA_T_ACTIVATION_AUTHORIZATION.json"
        ),
    }
    auth_path = repo / AUTHORIZATION_RELATIVE
    auth_path.write_bytes(canonical_json(authorization))
    _git(repo, "add", AUTHORIZATION_RELATIVE.as_posix())
    _git(repo, "commit", "-q", "-m", "authorize mirror activation")
    return repo, auth_path


def _amend_authorization(repo: Path, mutate) -> Path:
    path = repo / AUTHORIZATION_RELATIVE
    value = json.loads(path.read_bytes())
    mutate(value)
    path.write_bytes(canonical_json(value))
    _git(repo, "add", AUTHORIZATION_RELATIVE.as_posix())
    _git(repo, "commit", "-q", "--amend", "--no-edit")
    return path


def test_real_repository_remains_inactive_and_has_no_authorization() -> None:
    assert not (REPO / AUTHORIZATION_RELATIVE).exists()
    assert not (REPO / STATE_RELATIVE).exists()
    assert not (REPO / CLAIM_RELATIVE).exists()
    assert not (REPO / RECORD_RELATIVE).exists()
    assert verify_bootstrap(REPO) == []


def test_production_boundary_detects_test_world_imports(tmp_path: Path) -> None:
    source = tmp_path / "bad.py"
    source.write_text(
        "from philosophia.officina.world import evaluate_test_query\n",
        encoding="ascii",
    )
    failures = verify_production_boundary(tmp_path, ("bad.py",))
    assert any("evaluate_test_query" in item for item in failures)


def test_production_boundary_rejects_reflection_and_omitted_local_source(
    tmp_path: Path,
) -> None:
    source = tmp_path / "src/philosophia/officina/generic_harness.py"
    source.parent.mkdir(parents=True)
    (source.parent / "world.py").write_text("\n", encoding="ascii")
    source.write_text(
        'import philosophia.officina.world as w\n'
        'name = "evaluate_" + "test_query"\n'
        'call = getattr(w, name)\n',
        encoding="ascii",
    )
    failures = verify_production_boundary(
        tmp_path, ("src/philosophia/officina/generic_harness.py",)
    )
    assert any("dynamic resolution" in item for item in failures)
    assert any("omitted local dependencies" in item for item in failures)


def test_production_boundary_closes_arbitrary_repository_local_imports(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    reviewed = json.loads(authorization.read_bytes())["reviewed_source_paths"]
    harness = repo / GENERIC_HARNESS_RELATIVE
    harness.write_text("import external_behavior\n", encoding="ascii")
    external = repo / "external_behavior.py"
    external.write_text("import local_helper\n", encoding="ascii")
    helper = repo / "local_helper.py"
    helper.write_text(
        "from philosophia.officina.world import evaluate_test_query\n",
        encoding="ascii",
    )
    reviewed_without_helper = [
        *[item for item in reviewed if item != PRODUCTION_MANIFEST_RELATIVE.as_posix()],
        "external_behavior.py",
    ]
    failures = verify_production_boundary(repo, reviewed_without_helper)
    assert any("omitted local dependencies" in item for item in failures)
    failures = verify_production_boundary(
        repo, (*reviewed_without_helper, "local_helper.py")
    )
    assert any("evaluate_test_query" in item for item in failures)


def test_production_boundary_rejects_unreachable_roots_and_ambiguous_modules(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    reviewed = json.loads(authorization.read_bytes())["reviewed_source_paths"]
    reviewed_python = [item for item in reviewed if item.endswith(".py")]
    orphan = repo / "orphan.py"
    orphan.write_text("VALUE = 1\n", encoding="ascii")
    failures = verify_production_boundary(repo, (*reviewed_python, "orphan.py"))
    assert any("unreachable from roots" in item for item in failures)

    without_root = [
        item for item in reviewed_python if item != PRODUCTION_ROOTS[0]
    ]
    failures = verify_production_boundary(repo, without_root)
    assert any("executable roots are unreviewed" in item for item in failures)

    harness = repo / GENERIC_HARNESS_RELATIVE
    harness.write_text("import ambiguous\n", encoding="ascii")
    (repo / "ambiguous.py").write_text("VALUE = 1\n", encoding="ascii")
    (repo / "src/ambiguous.py").write_text("VALUE = 2\n", encoding="ascii")
    failures = verify_production_boundary(
        repo, (*reviewed_python, "ambiguous.py", "src/ambiguous.py")
    )
    assert any("ambiguous local imports" in item for item in failures)


def test_activation_completes_only_in_disposable_reviewed_mirror(tmp_path: Path) -> None:
    repo, authorization = _mirror(tmp_path)
    committed = activate_repository(repo, authorization)
    assert len(committed) == 40
    assert verify_active_repository(repo, require_activation_commit=True) == []
    assert verify_bootstrap(repo) == ["ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER"]
    assert json.loads((repo / STATE_RELATIVE).read_bytes())["activated_utc"]
    assert not (repo / INVALIDITY_RELATIVE).exists()
    changed = _git(repo, "show", "--pretty=format:", "--name-only", "HEAD").splitlines()
    assert set(filter(None, changed)) == {
        CLAIM_RELATIVE.as_posix(), STATE_RELATIVE.as_posix(),
        RECORD_RELATIVE.as_posix(),
        "successor/officina/T_ENVELOPE.json",
        "successor/officina/T_LEDGER.md",
        "successor/officina/T_LEDGER.md.head.json",
    }


def test_partial_activation_is_durable_invalidity_and_cannot_rerun(tmp_path: Path) -> None:
    repo, authorization = _mirror(tmp_path)
    with pytest.raises(RuntimeError, match="injected"):
        activate_repository(repo, authorization, failure_after_step=2)
    assert (repo / CLAIM_RELATIVE).exists()
    assert (repo / STATE_RELATIVE).exists()
    invalidity = json.loads((repo / INVALIDITY_RELATIVE).read_bytes())
    assert invalidity["validity"] == "INVALID_PROCESS_RECORD"
    assert invalidity["required_action"] == "SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY"
    with pytest.raises(ActivationRefused):
        activate_repository(repo, authorization)


def test_post_anchor_activation_failure_records_invalidity_before_event(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    with pytest.raises(RuntimeError, match="injected"):
        activate_repository(repo, authorization, failure_after_step=3)
    invalidity_hash = sha256_file(repo / INVALIDITY_RELATIVE)
    entries = AppendOnlyLedger(
        repo / "successor/officina/T_LEDGER.md",
        head_path=repo / "successor/officina/T_LEDGER.md.head.json",
    ).entries()
    assert [entry["event"] for entry in entries] == [
        "T_ACTIVATED", "T_RUNTIME_INVALID"
    ]
    assert entries[-1]["data"]["invalidity_record_sha256"] == invalidity_hash


def test_authorization_source_drift_is_refused_before_claim(tmp_path: Path) -> None:
    repo, authorization = _mirror(tmp_path)
    (repo / "src/philosophia/officina/accounting.py").write_text(
        "# drift\n", encoding="ascii"
    )
    with pytest.raises(ActivationRefused, match="worktree|pins"):
        activate_repository(repo, authorization)
    assert not (repo / CLAIM_RELATIVE).exists()


def test_authorization_must_be_head_and_every_reviewed_path_tracked(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    unrelated = repo / "unrelated.txt"
    unrelated.write_text("later\n", encoding="ascii")
    _git(repo, "add", "unrelated.txt")
    _git(repo, "commit", "-q", "-m", "later unrelated commit")
    with pytest.raises(ActivationRefused, match="current HEAD"):
        activate_repository(repo, authorization)

    other = tmp_path / "untracked-case"
    repo, _ = _mirror(other)
    untracked = repo / "external_behavior.py"
    untracked.write_text("VALUE = 1\n", encoding="ascii")

    def add_untracked(value: dict[str, object]) -> None:
        paths = list(value["reviewed_source_paths"])
        paths.append("external_behavior.py")
        value["reviewed_source_paths"] = paths
        hashes = dict(value["reviewed_source_sha256"])
        hashes["external_behavior.py"] = sha256_file(untracked)
        value["reviewed_source_sha256"] = hashes

    authorization = _amend_authorization(repo, add_untracked)
    with pytest.raises(ActivationRefused, match="untracked or aliased"):
        activate_repository(repo, authorization)


def test_authorization_requires_exact_governing_chain_and_tokens(tmp_path: Path) -> None:
    repo, _ = _mirror(tmp_path)

    def remove_pin(value: dict[str, object]) -> None:
        governing = dict(value["governing_sha256"])
        governing.pop(GOVERNING_PATHS[-1])
        value["governing_sha256"] = governing

    authorization = _amend_authorization(repo, remove_pin)
    with pytest.raises(ValueError, match="signed six pins"):
        activate_repository(repo, authorization)

    other = tmp_path / "self-rehashed"
    repo, _ = _mirror(other)
    governing_path = repo / GOVERNING_PATHS[0]
    governing_path.write_bytes(governing_path.read_bytes() + b"\nmutation\n")

    def rehash_pin(value: dict[str, object]) -> None:
        governing = dict(value["governing_sha256"])
        governing[GOVERNING_PATHS[0]] = sha256_file(governing_path)
        value["governing_sha256"] = governing

    authorization = repo / AUTHORIZATION_RELATIVE
    value = json.loads(authorization.read_bytes())
    rehash_pin(value)
    authorization.write_bytes(canonical_json(value))
    _git(repo, "add", AUTHORIZATION_RELATIVE.as_posix(), GOVERNING_PATHS[0])
    _git(repo, "commit", "-q", "--amend", "--no-edit")
    with pytest.raises(ValueError, match="governing hashes"):
        activate_repository(repo, authorization)


@pytest.mark.parametrize("kind", ["governing", "protocol"])
def test_every_pinned_path_must_exist_at_reviewed_head(
    tmp_path: Path, kind: str
) -> None:
    repo, authorization = _mirror(tmp_path)
    path_set = GOVERNING_PATHS if kind == "governing" else PROTOCOL_PATHS
    relative = path_set[0]
    path = repo / relative
    original = path.read_bytes()
    path.unlink()
    _git(repo, "add", relative)
    _git(repo, "commit", "-q", "-m", f"reviewed head missing {kind}")
    deficient_head = _git(repo, "rev-parse", "HEAD")
    path.write_bytes(original)
    value = json.loads(authorization.read_bytes())
    value["reviewed_code_head"] = deficient_head
    authorization.write_bytes(canonical_json(value))
    _git(repo, "add", relative, AUTHORIZATION_RELATIVE.as_posix())
    _git(repo, "commit", "-q", "-m", f"restore {kind} and authorize")
    with pytest.raises(ActivationRefused, match="absent at reviewed HEAD"):
        activate_repository(repo, authorization)


def test_reviewed_hardlink_alias_is_refused_before_claim(tmp_path: Path) -> None:
    repo, authorization = _mirror(tmp_path)
    source = repo / "src/philosophia/officina/accounting.py"
    saved = tmp_path / "accounting-hardlink-source.py"
    source.rename(saved)
    source.hardlink_to(saved)
    assert source.stat().st_nlink == 2
    assert not _git(repo, "status", "--porcelain")
    with pytest.raises(ActivationRefused, match="untracked or aliased"):
        activate_repository(repo, authorization)


def test_active_verifier_rejects_resource_mutation_even_with_rehashed_record(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    activate_repository(repo, authorization)
    envelope_path = repo / "successor/officina/T_ENVELOPE.json"
    envelope = json.loads(envelope_path.read_bytes())
    envelope["device_hour_cap"] = 999
    envelope_path.write_bytes(canonical_json(envelope))
    record_path = repo / RECORD_RELATIVE
    record = json.loads(record_path.read_bytes())
    record["active_envelope_sha256"] = sha256_file(envelope_path)
    record_path.write_bytes(canonical_json(record))
    failures = verify_active_repository(repo, require_activation_commit=True)
    assert any("signed resource contract" in item for item in failures)
    assert any("immutable tracked bytes" in item for item in failures)


def test_activation_head_is_historical_anchor_not_current_runtime_head(
    tmp_path: Path,
) -> None:
    repo, authorization = _mirror(tmp_path)
    activate_repository(repo, authorization)
    state = json.loads((repo / STATE_RELATIVE).read_bytes())
    ledger = AppendOnlyLedger(
        repo / "successor/officina/T_LEDGER.md",
        head_path=repo / "successor/officina/T_LEDGER.md.head.json",
    )
    ledger.append(
        event="T_PROCESS_STARTED",
        timestamp_utc=state["activated_utc"],
        data={
            "process_claim_sha256": "a" * 64,
            "process_id": "b" * 64,
            "scientific_outcome": False,
        },
    )
    failures = verify_active_repository(repo, require_activation_commit=False)
    assert not any("historical ledger-head" in item for item in failures)
    assert failures == []
    PRODUCTION_MANIFEST_RELATIVE,
    PROTOCOL_PATHS,
