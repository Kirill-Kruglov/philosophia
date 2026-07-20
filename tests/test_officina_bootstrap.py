from __future__ import annotations

import ast
import json
from pathlib import Path
import shutil

import pytest

from philosophia.officina.canonical import canonical_json, sha256_bytes, sha256_file
from philosophia.officina.quarantine import (
    ArtifactLabel,
    FixtureGrant,
    PathPolicy,
    QuarantineViolation,
    Surface,
)
from philosophia.officina.interlock import test_only_capability as make_test_capability
from philosophia.officina.ledger import AppendOnlyLedger, parse_ledger
from philosophia.officina.provenance import ArtifactStore
from philosophia.officina.verification import verify_bootstrap, verify_source_quarantine


REPO = Path(__file__).resolve().parents[1]
OFFICINA_SOURCE = REPO / "src/philosophia/officina"


def test_committed_bootstrap_is_canonical_quarantined_and_inactive() -> None:
    assert verify_bootstrap(REPO) == []
    for name in ("LINEAGE.json", "PATH_POLICY.json", "T_ENVELOPE.json"):
        raw = (REPO / "successor/officina" / name).read_bytes()
        assert canonical_json(json.loads(raw)) == raw
    assert parse_ledger((REPO / "successor/officina/T_LEDGER.md").read_bytes()) == []
    assert AppendOnlyLedger(REPO / "successor/officina/T_LEDGER.md").entries() == []


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
    assert label.certified is False
    with pytest.raises(QuarantineViolation, match="ArtifactStore"):
        policy.read_bytes(native / "untracked.json", surface=Surface.T)
    with pytest.raises(QuarantineViolation, match="denied by default"):
        policy.read_bytes(stopped, surface=Surface.T)


def test_fixture_is_hash_pinned_read_only_t_only_and_nonpromotable(tmp_path: Path) -> None:
    policy, _, _, fixture = _policy(tmp_path)
    payload, label = policy.read_bytes(fixture, surface=Surface.T)
    assert payload == b"fixture\n"
    assert label == ArtifactLabel.engineering_fixture()
    derived = ArtifactLabel.derived(ArtifactLabel.native(), label)
    assert derived.promotable is False
    assert derived.sources == ("engineering-fixture", "officina-storage")
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


def test_artifact_store_propagates_taint_and_blocks_copy_relabel_mutation(
    tmp_path: Path,
) -> None:
    policy, native, _, fixture = _policy(tmp_path)
    store = ArtifactStore(policy)
    parent = store.read(fixture, surface=Surface.T)
    derived_path = native / "derived.bin"
    derived = store.write_derived(
        path=derived_path,
        payload=b"derived\n",
        purpose="fixture-derived-test",
        parents=(parent,),
    )
    assert derived.label.sources == ("engineering-fixture",)
    assert derived.label.promotable is False
    with pytest.raises(QuarantineViolation, match="cannot enter Q"):
        store.admit(derived_path, surface=Surface.Q)

    copied = native / "copied-fixture.bin"
    copied.write_bytes(fixture.read_bytes())
    with pytest.raises(QuarantineViolation, match="provenance is missing"):
        store.read(copied, surface=Surface.T)

    relabeled = native / "relabeled.bin"
    relabeled.write_bytes(derived_path.read_bytes())
    shutil.copyfile(store.metadata_path(derived_path), store.metadata_path(relabeled))
    with pytest.raises(QuarantineViolation, match="path mismatch"):
        store.read(relabeled, surface=Surface.T)

    forged = json.loads(store.metadata_path(derived_path).read_bytes())
    core = {key: value for key, value in forged.items() if key != "provenance_sha256"}
    core["promotable"] = True
    forged = {**core, "provenance_sha256": sha256_bytes(canonical_json(core))}
    store.metadata_path(derived_path).write_bytes(canonical_json(forged))
    with pytest.raises(QuarantineViolation, match="no promotable"):
        store.read(derived_path, surface=Surface.T)

    # Restore the genuine record before testing content mutation.
    core["promotable"] = False
    genuine = {**core, "provenance_sha256": sha256_bytes(canonical_json(core))}
    store.metadata_path(derived_path).write_bytes(canonical_json(genuine))

    derived_path.write_bytes(b"mutated\n")
    with pytest.raises(QuarantineViolation, match="content hash mismatch"):
        store.read(derived_path, surface=Surface.T)


def test_test_only_native_artifacts_are_durably_nonpromotable(tmp_path: Path) -> None:
    policy, native, _, _ = _policy(tmp_path)
    store = ArtifactStore(policy)
    artifact = store.write_test_only(
        path=native / "dummy.bin",
        payload=b"dummy",
        purpose="unit-fixture",
        capability=make_test_capability("provenance"),
    )
    assert artifact.label.sources == ("test-only-native",)
    with pytest.raises(QuarantineViolation, match="cannot enter C"):
        store.admit(artifact.path, surface=Surface.C)


def test_realpath_resolution_blocks_symlink_escape(tmp_path: Path) -> None:
    policy, native, stopped, _ = _policy(tmp_path)
    escape = native / "escape"
    escape.symlink_to(stopped)
    with pytest.raises(QuarantineViolation, match="denied by default"):
        policy.read_bytes(escape, surface=Surface.T)


@pytest.mark.parametrize(
    ("filename", "field", "value"),
    [
        ("LINEAGE.json", "runtime_inheritance", "allowed"),
        ("PATH_POLICY.json", "default", "allow"),
        ("T_ENVELOPE.json", "device_hour_cap", 169),
    ],
)
def test_bootstrap_verifier_rejects_every_governing_manifest_mutation(
    tmp_path: Path, filename: str, field: str, value: object
) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(REPO / "successor", repo / "successor")
    root = repo / "successor/officina"
    path = root / filename
    payload = json.loads(path.read_bytes())
    payload[field] = value
    path.write_bytes(canonical_json(payload))
    assert verify_bootstrap(repo)


def test_bootstrap_verifier_rejects_each_governing_field_and_type(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(REPO / "successor", repo / "successor")
    root = repo / "successor/officina"
    for filename in ("LINEAGE.json", "PATH_POLICY.json", "T_ENVELOPE.json"):
        path = root / filename
        original = json.loads(path.read_bytes())
        for field, old_value in original.items():
            mutant = dict(original)
            if type(old_value) is bool:
                mutant[field] = 1 if old_value else 0
            elif type(old_value) is int:
                mutant[field] = str(old_value)
            elif isinstance(old_value, str):
                mutant[field] = old_value + "-mutant"
            elif isinstance(old_value, list):
                mutant[field] = [*old_value, "mutant"]
            else:
                raise AssertionError(f"unhandled field type: {filename}:{field}")
            path.write_bytes(canonical_json(mutant))
            assert verify_bootstrap(repo), f"accepted mutation {filename}:{field}"
            path.write_bytes(canonical_json(original))


def test_entropy_scan_resolves_import_aliases_and_dynamic_imports(tmp_path: Path) -> None:
    aliased = tmp_path / "aliased.py"
    aliased.write_text(
        "import secrets as hidden\nvalue = hidden.token_bytes(32)\n",
        encoding="utf-8",
    )
    direct = tmp_path / "direct.py"
    direct.write_text("from os import urandom as draw\nvalue = draw(32)\n", encoding="utf-8")
    dynamic = tmp_path / "dynamic.py"
    dynamic.write_text("module = __import__('secrets')\n", encoding="utf-8")
    failures = verify_source_quarantine((aliased, direct, dynamic))
    assert any("secrets.token_bytes" in failure for failure in failures)
    assert any("os.urandom" in failure for failure in failures)
    assert any("dynamic import" in failure for failure in failures)


def test_pyproject_packages_officina() -> None:
    text = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert '"philosophia.officina"' in text
