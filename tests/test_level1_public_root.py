from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

import pytest

from philosophia.level1.public_root import (
    CLAIM_SCHEMA,
    TRANSCRIPT_SCHEMA,
    atomic_create,
    build_claim,
    build_transcript,
    canonical_json,
    derive_public_allocations,
    environment_fingerprint,
    load_durable_transcript,
)


REPO = Path(__file__).resolve().parents[1]
DRIVER = REPO / "scripts/level1_draw_public_root.py"
REACHABLE_SOURCES = (
    DRIVER,
    REPO / "src/philosophia/level1/public_root.py",
    REPO / "src/philosophia/level1/allocation.py",
    REPO / "src/philosophia/level1/serialization.py",
    REPO / "src/philosophia/level1/model.py",
)


def _load_driver():
    specification = importlib.util.spec_from_file_location("level1_draw_public_root", DRIVER)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def _environment() -> dict[str, object]:
    return {
        "python_build": "3.12.3",
        "torch_build": "2.9.1+cpu",
        "device": "cpu",
        "dtype": "float32",
    }


def _test_transcript(head: str = "a" * 40) -> dict[str, object]:
    return build_transcript(
        root=bytes(range(32)),
        git_head=head,
        reviewed_code_head=head,
        timestamp_utc="2026-07-13T12:00:01Z",
        environment=_environment(),
        required_spec_hashes={"v3": "1" * 64, "v3.1": "2" * 64},
        governing_lineage_hashes={"signed": "3" * 64},
        allocations=derive_public_allocations(bytes(range(32))),
    )


def test_claim_and_transcript_are_canonical_and_golden() -> None:
    claim = build_claim(
        expected_head="a" * 40,
        reviewed_code_head="a" * 40,
        created_utc="2026-07-13T12:00:00Z",
        transcript_path="PUBLIC_ROOT_TRANSCRIPT.json",
    )
    assert claim["schema"] == CLAIM_SCHEMA
    assert claim["status"] == "armed-before-entropy"
    assert claim["operator_rule"] == "claim presence forbids rerun or deletion"

    transcript = _test_transcript()
    assert transcript["schema"] == TRANSCRIPT_SCHEMA
    assert transcript["root_hex"] == bytes(range(32)).hex()
    assert transcript["environment_fingerprint"] == environment_fingerprint(_environment())
    assert transcript["process_attestation"]["os_csprng_calls"] == 1
    assert transcript["scientific_outcome"] is False
    serialized = canonical_json(transcript)
    assert serialized == canonical_json(json.loads(serialized))
    assert hashlib.sha256(serialized).hexdigest() == (
        "b2bf592a9687a50c8c8cc5bcf32efae3d7c8b2f6436a943db45b477b1420cee9"
    )


def test_public_allocations_materialize_d_and_roles_but_not_r_h() -> None:
    allocations = derive_public_allocations(bytes(range(32)))
    development = allocations["development_pairs"]
    roles = allocations["outcome_role_assignments"]
    assert len(development) == 6
    assert [
        sum(item["stratum"] == h for item in development) for h in (1, 2, 3)
    ] == [2, 2, 2]
    assert len(roles) == 24
    assert [sum(item["stratum"] == h for item in roles) for h in (1, 2, 3)] == [
        8, 8, 8
    ]
    assert all(abs(item["target"] - item["donor"]) == 1 for item in roles)
    assert allocations["outcome_sample"] == "deferred-until-N3"


def test_transcript_rejects_non_32_byte_root() -> None:
    with pytest.raises(ValueError, match="exactly 32"):
        build_transcript(
            root=b"short",
            git_head="a" * 40,
            reviewed_code_head="a" * 40,
            timestamp_utc="2026-07-13T12:00:01Z",
            environment=_environment(),
            required_spec_hashes={},
            governing_lineage_hashes={},
            allocations={},
        )


def test_atomic_create_and_durable_transcript_validation(tmp_path: Path) -> None:
    destination = tmp_path / "nested" / "transcript.json"
    payload = canonical_json(_test_transcript())
    atomic_create(destination, payload)
    assert load_durable_transcript(destination, expected_head="a" * 40)["root_hex"] == bytes(
        range(32)
    ).hex()
    assert not destination.with_name(f".{destination.name}.tmp").exists()
    with pytest.raises(FileExistsError):
        atomic_create(destination, b"second\n")
    with pytest.raises(ValueError, match="HEAD mismatch"):
        load_durable_transcript(destination, expected_head="b" * 40)


def _dotted_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else None
    return None


def test_reachable_modules_contain_exactly_one_entropy_call() -> None:
    entropy_names = {
        "secrets.token_bytes",
        "secrets.randbits",
        "secrets.choice",
        "os.urandom",
        "random.SystemRandom",
        "torch.seed",
        "torch.initial_seed",
    }
    found = []
    for path in REACHABLE_SOURCES:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and _dotted_name(node.func) in entropy_names:
                found.append((path, _dotted_name(node.func), node))
    assert [(path, name) for path, name, _ in found] == [(DRIVER, "secrets.token_bytes")]
    call = found[0][2]
    assert len(call.args) == 1 and isinstance(call.args[0], ast.Constant)
    assert call.args[0].value == 32 and not call.keywords


def test_driver_orders_claim_draw_transcript_commit_and_failure_route() -> None:
    source = DRIVER.read_text(encoding="utf-8")
    claim = source.index("atomic_create(repo / CLAIM_RELATIVE")
    draw = source.index("secrets.token_bytes(32)")
    transcript = source.index("atomic_create(repo / TRANSCRIPT_RELATIVE")
    commit = source.index("_commit_transcript(repo)")
    route = source.index("route = _route_post_draw_failure")
    assert claim < draw < transcript < commit < route
    assert source.count("secrets.token_bytes(32)") == 1
    assert source.count("_commit_transcript(repo)") == 1
    assert "sample_outcome_pairs" not in source


def _git(repo: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments], cwd=repo, check=True, capture_output=True, text=True
    )


def _fresh_repo(path: Path, driver) -> tuple[Path, str]:
    path.mkdir()
    _git(path, "init", "-q")
    _git(path, "config", "user.name", "Test")
    _git(path, "config", "user.email", "test@example.com")
    required = {
        *(item.as_posix() for item in driver.GOVERNING_LINEAGE),
        *driver.REVIEWED_SOURCE_PATHS,
    }
    for relative in required:
        destination = path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(f"fixture:{relative}\n", encoding="utf-8")
    _git(path, "add", "--", ".")
    _git(path, "commit", "-q", "-m", "fixture")
    return path, _git(path, "rev-parse", "HEAD").stdout.strip()


def test_preflight_refuses_head_source_tree_index_and_artifact_states(tmp_path: Path) -> None:
    driver = _load_driver()

    repo, head = _fresh_repo(tmp_path / "head", driver)
    with pytest.raises(RuntimeError, match="HEAD mismatch"):
        driver._preflight(repo, "0" * 40, head)

    repo, head = _fresh_repo(tmp_path / "source", driver)
    reviewed = head
    source = repo / driver.REVIEWED_SOURCE_PATHS[0]
    source.write_text("changed\n", encoding="utf-8")
    _git(repo, "add", "--", source.relative_to(repo).as_posix())
    _git(repo, "commit", "-q", "-m", "source drift")
    changed = _git(repo, "rev-parse", "HEAD").stdout.strip()
    with pytest.raises(RuntimeError, match="source bytes differ"):
        driver._preflight(repo, changed, reviewed)

    repo, head = _fresh_repo(tmp_path / "dirty", driver)
    (repo / driver.REVIEWED_SOURCE_PATHS[0]).write_text("dirty\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="working tree"):
        driver._preflight(repo, head, head)

    repo, head = _fresh_repo(tmp_path / "staged", driver)
    (repo / "staged.txt").write_text("staged\n", encoding="utf-8")
    _git(repo, "add", "--", "staged.txt")
    with pytest.raises(RuntimeError, match="index"):
        driver._preflight(repo, head, head)

    repo, head = _fresh_repo(tmp_path / "artifact", driver)
    artifact = repo / driver.TRANSCRIPT_RELATIVE
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text("present\n", encoding="utf-8")
    with pytest.raises(FileExistsError, match="already exists"):
        driver._preflight(repo, head, head)


def test_commit_stages_only_claim_and_transcript(monkeypatch: pytest.MonkeyPatch) -> None:
    driver = _load_driver()
    calls: list[tuple[str, ...]] = []

    def fake_git(repo: Path, *arguments: str, check: bool = True):
        del repo, check
        calls.append(arguments)
        if arguments == ("diff", "--cached", "--name-only"):
            output = "\n".join(
                (driver.CLAIM_RELATIVE.as_posix(), driver.TRANSCRIPT_RELATIVE.as_posix())
            ) + "\n"
        else:
            output = ""
        return subprocess.CompletedProcess(["git", *arguments], 0, output, "")

    monkeypatch.setattr(driver, "_run_git", fake_git)
    driver._commit_transcript(Path("/unused"))
    assert calls[0] == ("diff", "--cached", "--quiet")
    assert calls[1] == (
        "add", "--", driver.CLAIM_RELATIVE.as_posix(), driver.TRANSCRIPT_RELATIVE.as_posix()
    )
    assert calls[2] == ("diff", "--cached", "--name-only")
    assert calls[3][0:2] == ("commit", "--no-gpg-sign")


def test_post_draw_failure_routes_durable_root_to_commit_pending(tmp_path: Path) -> None:
    driver = _load_driver()
    expected_head = "a" * 40
    durable_repo = tmp_path / "durable"
    transcript = durable_repo / driver.TRANSCRIPT_RELATIVE
    atomic_create(transcript, canonical_json(_test_transcript(expected_head)))
    route = driver._route_post_draw_failure(durable_repo, expected_head, RuntimeError("git"))
    assert "commit pending" in route
    assert (durable_repo / driver.COMMIT_PENDING_RELATIVE).exists()
    assert not (durable_repo / driver.INVALIDITY_RELATIVE).exists()

    lost_repo = tmp_path / "lost"
    route = driver._route_post_draw_failure(lost_repo, expected_head, RuntimeError("write"))
    assert "invalidity required" in route
    assert (lost_repo / driver.INVALIDITY_RELATIVE).exists()
    assert not (lost_repo / driver.COMMIT_PENDING_RELATIVE).exists()


def test_real_one_shot_artifacts_do_not_exist_during_unit_tests() -> None:
    allocation = REPO / "experiments/level_1_contact/allocation"
    for name in (
        "PUBLIC_ROOT_DRAW_CLAIM.json",
        "PUBLIC_ROOT_TRANSCRIPT.json",
        "PUBLIC_ROOT_COMMIT_PENDING.json",
        "PUBLIC_ROOT_INVALIDITY_REQUIRED.json",
    ):
        assert not (allocation / name).exists()
