from __future__ import annotations

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
    IMMUTABLE_CONTROL_PATHS,
    INVALIDITY_RELATIVE,
    RECORD_RELATIVE,
    STATE_RELATIVE,
    ActivationRefused,
    activate_repository,
    canonical_paths,
    verify_active_repository,
)
from philosophia.officina.canonical import canonical_json, sha256_file
from philosophia.officina.verification import verify_bootstrap, verify_production_boundary


REPO = Path(__file__).resolve().parent.parent


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True
    ).stdout.strip()


def _mirror(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "mirror"
    (repo / "src/philosophia").mkdir(parents=True)
    shutil.copytree(REPO / "src/philosophia/officina", repo / "src/philosophia/officina")
    shutil.copytree(REPO / "successor/officina", repo / "successor/officina")
    for relative in (
        Path("successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md"),
        Path("successor/CHARTER_SIGNATURE.md"),
    ):
        target = repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / relative, target)
    (repo / "scripts").mkdir()
    for name in ("officina_activate_t.py", "verify_officina_active.py"):
        shutil.copy2(REPO / "scripts" / name, repo / "scripts" / name)
    harness = repo / GENERIC_HARNESS_RELATIVE
    harness.write_text(
        '"""Reviewed mirror-only harness fixture."""\nHARNESS_REVIEWED = True\n',
        encoding="ascii",
    )
    _git(repo, "init", "-q")
    _git(repo, "config", "user.name", "Officina Test")
    _git(repo, "config", "user.email", "officina-test@example.invalid")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "reviewed implementation")
    reviewed_head = _git(repo, "rev-parse", "HEAD")

    reviewed_paths = [*IMMUTABLE_CONTROL_PATHS, GENERIC_HARNESS_RELATIVE.as_posix()]
    source_hashes = {
        relative: sha256_file(repo / relative) for relative in reviewed_paths
    }
    governing_path = "successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md"
    protocol_path = "successor/CHARTER_SIGNATURE.md"
    authorization = {
        "schema": AUTHORIZATION_SCHEMA,
        "scientific_outcome": False,
        "execution_once": True,
        "token": ACTIVATION_TOKEN,
        "reviewed_code_head": reviewed_head,
        "reviewed_source_paths": reviewed_paths,
        "reviewed_source_sha256": source_hashes,
        "governing_sha256": {governing_path: sha256_file(repo / governing_path)},
        "protocol_sha256": {protocol_path: sha256_file(repo / protocol_path)},
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


def test_authorization_source_drift_is_refused_before_claim(tmp_path: Path) -> None:
    repo, authorization = _mirror(tmp_path)
    (repo / "src/philosophia/officina/accounting.py").write_text(
        "# drift\n", encoding="ascii"
    )
    with pytest.raises(ActivationRefused, match="worktree|pins"):
        activate_repository(repo, authorization)
    assert not (repo / CLAIM_RELATIVE).exists()
