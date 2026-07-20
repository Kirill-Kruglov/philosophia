from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from philosophia.officina.canonical import canonical_json, sha256_file
from philosophia.officina.quarantine import (
    ArtifactLabel,
    FixtureGrant,
    PathPolicy,
    QuarantineViolation,
    Surface,
)
from philosophia.officina.ledger import parse_ledger
from philosophia.officina.verification import verify_bootstrap, verify_source_quarantine


REPO = Path(__file__).resolve().parents[1]
OFFICINA_SOURCE = REPO / "src/philosophia/officina"


def test_committed_bootstrap_is_canonical_quarantined_and_inactive() -> None:
    assert verify_bootstrap(REPO) == []
    for name in ("LINEAGE.json", "PATH_POLICY.json", "T_ENVELOPE.json"):
        raw = (REPO / "successor/officina" / name).read_bytes()
        assert canonical_json(json.loads(raw)) == raw
    assert parse_ledger((REPO / "successor/officina/T_LEDGER.md").read_bytes()) == []


def test_officina_source_imports_no_predecessor_runtime_and_draws_no_entropy() -> None:
    sources = sorted(OFFICINA_SOURCE.glob("*.py"))
    assert sources
    assert verify_source_quarantine(sources) == []

    call_names: set[str] = set()
    for source in sources:
        tree = ast.parse(source.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    call_names.add(f"{node.func.value.id}.{node.func.attr}")
    assert "secrets.token_bytes" not in call_names
    assert "os.urandom" not in call_names


def _policy(tmp_path: Path) -> tuple[PathPolicy, Path, Path, Path]:
    repo = tmp_path / "repo"
    native = repo / "successor/officina"
    native.mkdir(parents=True)
    stopped = repo / "experiments/level_1_contact/result.json"
    stopped.parent.mkdir(parents=True)
    stopped.write_text("stopped\n", encoding="utf-8")
    fixture = repo / "fixtures/context.txt"
    fixture.parent.mkdir()
    fixture.write_text("fixture\n", encoding="utf-8")
    policy = PathPolicy(
        repository_root=repo,
        successor_root=native,
        fixture_grants=(FixtureGrant(fixture, sha256_file(fixture)),),
    )
    return policy, native, stopped, fixture


def test_path_policy_allows_native_and_denies_predecessor_by_default(tmp_path: Path) -> None:
    policy, native, stopped, _ = _policy(tmp_path)
    destination, label = policy.authorize(native / "data.json", surface=Surface.T, write=True)
    assert destination == (native / "data.json").resolve()
    assert label == ArtifactLabel.native()
    with pytest.raises(QuarantineViolation, match="denied by default"):
        policy.read_bytes(stopped, surface=Surface.T)


def test_fixture_is_hash_pinned_read_only_t_only_and_nonpromotable(tmp_path: Path) -> None:
    policy, _, _, fixture = _policy(tmp_path)
    payload, label = policy.read_bytes(fixture, surface=Surface.T)
    assert payload == b"fixture\n"
    assert label == ArtifactLabel.engineering_fixture()
    derived = ArtifactLabel.derived(ArtifactLabel.native(), label)
    assert derived.promotable is False
    assert derived.sources == ("engineering-fixture", "officina-native")
    with pytest.raises(QuarantineViolation, match="read-only"):
        policy.authorize(fixture, surface=Surface.T, write=True)
    with pytest.raises(QuarantineViolation, match="T-only"):
        policy.read_bytes(fixture, surface=Surface.Q)
    with pytest.raises(QuarantineViolation, match="cannot enter Q"):
        label.require_promotable(Surface.Q)
    with pytest.raises(QuarantineViolation, match="engineering-fixture"):
        derived.require_promotable(Surface.C)
    fixture.write_text("mutated\n", encoding="utf-8")
    with pytest.raises(QuarantineViolation, match="hash mismatch"):
        policy.read_bytes(fixture, surface=Surface.T)


def test_realpath_resolution_blocks_symlink_escape(tmp_path: Path) -> None:
    policy, native, stopped, _ = _policy(tmp_path)
    escape = native / "escape"
    escape.symlink_to(stopped)
    with pytest.raises(QuarantineViolation, match="denied by default"):
        policy.read_bytes(escape, surface=Surface.T)


def test_pyproject_packages_officina() -> None:
    text = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert '"philosophia.officina"' in text
