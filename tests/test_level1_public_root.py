from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

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
)


REPO = Path(__file__).resolve().parents[1]
DRIVER = REPO / "scripts/level1_draw_public_root.py"


def _environment() -> dict[str, object]:
    return {
        "python_build": "3.12.3",
        "torch_build": "2.9.1+cpu",
        "device": "cpu",
        "dtype": "float32",
    }


def test_claim_and_transcript_are_canonical_and_golden() -> None:
    claim = build_claim(
        expected_head="a" * 40,
        created_utc="2026-07-13T12:00:00Z",
        transcript_path="PUBLIC_ROOT_TRANSCRIPT.json",
    )
    assert claim["schema"] == CLAIM_SCHEMA
    assert claim["status"] == "armed-before-entropy"

    transcript = build_transcript(
        root=bytes(range(32)),
        git_head="a" * 40,
        timestamp_utc="2026-07-13T12:00:01Z",
        environment=_environment(),
        required_spec_hashes={"v3": "1" * 64, "v3.1": "2" * 64},
        governing_lineage_hashes={"signed": "3" * 64},
        allocations=derive_public_allocations(bytes(range(32))),
    )
    assert transcript["schema"] == TRANSCRIPT_SCHEMA
    assert transcript["root_hex"] == bytes(range(32)).hex()
    assert transcript["environment_fingerprint"] == environment_fingerprint(_environment())
    assert transcript["process_attestation"]["os_csprng_calls"] == 1
    assert transcript["scientific_outcome"] is False
    serialized = canonical_json(transcript)
    assert serialized == canonical_json(json.loads(serialized))
    assert hashlib.sha256(serialized).hexdigest() == (
        "cecd64d27b9a053e54ba690ed16354c11efeb3caae9b6ada90b8c2cd5c3dfbb6"
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
            timestamp_utc="2026-07-13T12:00:01Z",
            environment=_environment(),
            required_spec_hashes={},
            governing_lineage_hashes={},
            allocations={},
        )


def test_atomic_create_is_exclusive_and_leaves_no_temporary_file(tmp_path: Path) -> None:
    destination = tmp_path / "nested" / "transcript.json"
    atomic_create(destination, b"first\n")
    assert destination.read_bytes() == b"first\n"
    assert not destination.with_name(f".{destination.name}.tmp").exists()
    with pytest.raises(FileExistsError):
        atomic_create(destination, b"second\n")
    assert destination.read_bytes() == b"first\n"


def test_driver_contains_exactly_one_literal_csprng_call_outside_loops() -> None:
    tree = ast.parse(DRIVER.read_text(encoding="utf-8"))
    parents: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent
    calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "secrets"
        and node.func.attr == "token_bytes"
    ]
    assert len(calls) == 1
    call = calls[0]
    assert len(call.args) == 1 and isinstance(call.args[0], ast.Constant)
    assert call.args[0].value == 32 and not call.keywords
    ancestor = parents.get(call)
    while ancestor is not None:
        assert not isinstance(ancestor, (ast.For, ast.AsyncFor, ast.While))
        ancestor = parents.get(ancestor)


def test_driver_orders_claim_draw_transcript_commit_and_invalidity_route() -> None:
    source = DRIVER.read_text(encoding="utf-8")
    claim = source.index("atomic_create(repo / CLAIM_RELATIVE")
    draw = source.index("secrets.token_bytes(32)")
    transcript = source.index("atomic_create(repo / TRANSCRIPT_RELATIVE")
    commit = source.index("_commit_transcript(repo)")
    assert claim < draw < transcript < commit
    assert source.count("_commit_transcript(repo)") == 1
    assert "sample_outcome_pairs" not in source
    marker = "_record_invalidity(repo, actual_head, error)"
    assert source.count(marker) == 2
    assert source.rindex(marker) > commit


def test_real_one_shot_artifacts_do_not_exist_during_unit_tests() -> None:
    allocation = REPO / "experiments/level_1_contact/allocation"
    assert not (allocation / "PUBLIC_ROOT_DRAW_CLAIM.json").exists()
    assert not (allocation / "PUBLIC_ROOT_TRANSCRIPT.json").exists()
    assert not (allocation / "PUBLIC_ROOT_INVALIDITY_REQUIRED.json").exists()
