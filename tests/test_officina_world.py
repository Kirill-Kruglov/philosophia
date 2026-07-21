from __future__ import annotations

import json
import os
from pathlib import Path
from types import SimpleNamespace

import pytest

from philosophia.officina.canonical import canonical_json, sha256_file
from philosophia.officina.interlock import (
    execute_c,
    launch_q,
    test_only_capability as make_test_capability,
)
from philosophia.officina.ledger import AppendOnlyLedger, LedgerIntegrityError
from philosophia.officina.provenance import ArtifactStore, ProvenanceRegistry
from philosophia.officina.quarantine import PathPolicy, QuarantineViolation, Surface
from philosophia.officina.world import (
    CH1_TOKEN,
    CH2_TOKEN,
    LAMBDA,
    SIGNED_CONTRACT_SHA256,
    SIGNED_WP3_SIGNATURE_SHA256,
    TestWorldCapability as WorldCapabilityForTest,
    evaluate_test_query,
    frame_bytes,
    frame_mapping,
    frame_sha256,
    record_test_t_contact,
    issue_test_t_contact_harness,
    test_world_capability as make_test_world_capability,
    verify_frame_bytes,
)


REPO = Path(__file__).resolve().parent.parent


def _capability(surface: Surface = Surface.T):
    return make_test_world_capability(
        surface,
        capability=make_test_capability("world-tests"),
        purpose="world-tests",
    )


def test_signed_contract_and_signature_hashes_are_exact() -> None:
    assert SIGNED_CONTRACT_SHA256 == sha256_file(
        REPO / "successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md"
    )
    assert SIGNED_WP3_SIGNATURE_SHA256 == sha256_file(
        REPO / "successor/OFFICINA_WP3_SIGNATURE.md"
    )


def test_frame_is_canonical_complete_disjoint_and_selected() -> None:
    value = frame_mapping()
    assert value["ch1_token"] == CH1_TOKEN
    assert value["ch2_token"] == CH2_TOKEN
    assert value["band"] == {"n_min": 26, "n_max": 65}
    assert value["lambda"] == LAMBDA == 140
    assert value["c_block_ps"] == [1, 3, 5, 6, 8, 10, 11, 13, 15, 16, 18, 20]
    assert value["q_worlds"] == [
        28, 29, 32, 33, 38, 39, 42, 43,
        48, 49, 52, 53, 58, 59, 62, 63,
    ]
    assert len(value["blocks"]) == 20
    assert verify_frame_bytes(frame_bytes()) == value
    assert frame_sha256() == "cc54cd2e6bf6f0e248008a4d5b64f491340e7fa8673d377c6419a6781d33170b"


def test_frame_verifier_refuses_noncanonical_and_mutated_payloads() -> None:
    value = frame_mapping()
    with pytest.raises(ValueError, match="not canonical"):
        verify_frame_bytes(json.dumps(value).encode("ascii"))
    value["q_worlds"] = [28]
    with pytest.raises(ValueError, match="differs"):
        verify_frame_bytes(canonical_json(value))


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (canonical_json({"u": "RL", "v": "R"}), canonical_json(0)),
        (canonical_json({"u": "", "v": ""}), canonical_json(1)),
        (b"not-json\n", canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (b'{"u":"R", "v":"L"}\n', canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (b'{"u":"R","u":"L","v":"R"}\n', canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (canonical_json({"u": "R", "v": 1}), canonical_json({"refusal": "MALFORMED_QUERY_STRUCTURE"})),
        (canonical_json({"u": "R_", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
        (canonical_json({"u": "R|", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
        (canonical_json({"u": "R" * (LAMBDA + 1), "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_LENGTH"})),
        (canonical_json({"u": "R" * (LAMBDA + 1) + "_", "v": "R"}), canonical_json({"refusal": "MALFORMED_QUERY_BYTE"})),
    ],
)
def test_oracle_wire_classifier_is_total_ordered_and_exact(
    raw: bytes, expected: bytes
) -> None:
    assert evaluate_test_query(
        capability=_capability(), modulus=10, raw_query=raw
    ) == expected


def test_oracle_matches_cyclic_equality_and_surface_gates() -> None:
    query = canonical_json({"u": "R" * 10, "v": ""})
    assert evaluate_test_query(
        capability=_capability(), modulus=10, raw_query=query
    ) == canonical_json(1)
    assert evaluate_test_query(
        capability=_capability(), modulus=11, raw_query=query
    ) == canonical_json(0)
    with pytest.raises(PermissionError, match="outside the T"):
        evaluate_test_query(
            capability=_capability(), modulus=26, raw_query=query
        )
    for surface in (Surface.Q, Surface.C):
        with pytest.raises(PermissionError, match="T-only"):
            _capability(surface)
    with pytest.raises(Exception, match="separately signed WP-6"):
        launch_q()
    with pytest.raises(Exception, match="one-shot authorization"):
        execute_c()


@pytest.mark.parametrize(
    ("surface", "modulus"),
    [(Surface.Q, 28), (Surface.C, 26), (Surface.TEST, 26)],
)
def test_issued_t_capability_cannot_be_relabelled_at_use(
    surface: Surface, modulus: int
) -> None:
    capability = _capability()
    object.__setattr__(capability, "surface", surface)
    with pytest.raises(PermissionError, match="T-only at use"):
        evaluate_test_query(
            capability=capability,
            modulus=modulus,
            raw_query=b"not-json\n",
        )


def test_world_capability_is_test_only_exact_and_unforgeable() -> None:
    with pytest.raises(PermissionError, match="factory"):
        WorldCapabilityForTest(Surface.T, "test-only:forged", object())
    forged = SimpleNamespace(surface=Surface.T, purpose="test-only:forged")
    with pytest.raises(PermissionError, match="issued"):
        evaluate_test_query(
            capability=forged,  # type: ignore[arg-type]
            modulus=10,
            raw_query=canonical_json({"u": "", "v": ""}),
        )
    with pytest.raises(PermissionError, match="T-only"):
        _capability(Surface.TEST)


def test_test_contact_hook_charges_and_logs_without_real_activation(
    tmp_path: Path,
) -> None:
    harness = issue_test_t_contact_harness(
        temp_root=tmp_path,
        capability=make_test_capability("contact-harness"),
        purpose="world-tests",
    )
    query = canonical_json({"u": "R" * 10, "v": ""})
    next_state, response, entry = record_test_t_contact(
        capability=_capability(),
        modulus=10,
        raw_query=query,
        device_nanoseconds=123,
        timestamp_utc="2026-07-21T00:00:01Z",
        harness=harness,
    )
    assert response == canonical_json(1)
    assert next_state.device_nanoseconds == 123
    assert next_state.test_only is True
    assert next_state.purpose == "test-only:world-tests"
    assert entry["event"] == "T_TEST_ONLY_WORLD_CONTACT"
    assert entry["data"]["test_only"] is True
    assert entry["data"]["scientific_outcome"] is False
    assert len(harness.entries()) == 1
    with pytest.raises(ValueError, match="positive integer"):
        record_test_t_contact(
            capability=_capability(),
            modulus=10,
            raw_query=query,
            device_nanoseconds=True,
            timestamp_utc="2026-07-21T00:00:02Z",
            harness=harness,
        )
    final_state, _, _ = record_test_t_contact(
        capability=_capability(),
        modulus=10,
        raw_query=query,
        device_nanoseconds=1,
        timestamp_utc="2026-07-21T00:00:02Z",
        harness=harness,
    )
    assert final_state.device_nanoseconds == 124
    assert len(harness.entries()) == 2
    harness.close()
    with pytest.raises(PermissionError, match="closed"):
        harness.entries()


def test_test_contact_harness_refuses_production_compatible_objects_and_aliases(
    tmp_path: Path,
) -> None:
    protected = (
        REPO / "successor/officina/T_ENVELOPE.json",
        REPO / "successor/officina/T_LEDGER.md",
        REPO / "successor/officina/T_LEDGER.md.head.json",
    )
    before = {path: sha256_file(path) for path in protected}
    query = canonical_json({"u": "", "v": ""})
    ordinary = AppendOnlyLedger(tmp_path / "ordinary.md")
    ordinary.initialize()
    with pytest.raises(PermissionError, match="issued test harness"):
        record_test_t_contact(
            capability=_capability(),
            modulus=10,
            raw_query=query,
            device_nanoseconds=1,
            timestamp_utc="2026-07-21T00:00:02Z",
            harness=ordinary,  # type: ignore[arg-type]
        )

    with pytest.raises(PermissionError, match="outside the repository"):
        issue_test_t_contact_harness(
            temp_root=REPO / "successor/officina",
            capability=make_test_capability("direct-alias"),
            purpose="direct-alias",
        )
    with pytest.raises(PermissionError, match="absolute Path"):
        issue_test_t_contact_harness(
            temp_root=Path("successor/officina"),
            capability=make_test_capability("relative-alias"),
            purpose="relative-alias",
        )

    symlink_root = tmp_path / "symlink-root"
    symlink_root.symlink_to(REPO / "successor/officina", target_is_directory=True)
    with pytest.raises(PermissionError, match="path aliases"):
        issue_test_t_contact_harness(
            temp_root=symlink_root,
            capability=make_test_capability("symlink-alias"),
            purpose="symlink-alias",
        )

    for name, protected_path in (
        ("ledger-hardlink", protected[1]),
        ("head-hardlink", protected[2]),
    ):
        root = tmp_path / name
        root.mkdir()
        alias_name = "T_LEDGER.md" if "ledger" in name else "T_LEDGER.md.head.json"
        os.link(protected_path, root / alias_name)
        with pytest.raises(PermissionError, match="aliases a committed|newly created"):
            issue_test_t_contact_harness(
                temp_root=root,
                capability=make_test_capability(name),
                purpose=name,
            )

    assert {path: sha256_file(path) for path in protected} == before


def test_test_contact_harness_rejects_valid_post_issuance_substitution(
    tmp_path: Path,
) -> None:
    issued_root = tmp_path / "issued"
    issued_root.mkdir()
    harness = issue_test_t_contact_harness(
        temp_root=issued_root,
        capability=make_test_capability("substitution-target"),
        purpose="substitution-target",
    )

    replacement_root = tmp_path / "replacement"
    replacement_root.mkdir()
    replacement = AppendOnlyLedger(replacement_root / "T_LEDGER.md")
    replacement.initialize()
    replacement.append(
        event="FORGED_TEST_ENTRY",
        timestamp_utc="2026-07-21T00:00:00Z",
        data={"scientific_outcome": False, "test_only": True},
    )
    os.replace(replacement.path, issued_root / "T_LEDGER.md")
    os.replace(replacement.head_path, issued_root / "T_LEDGER.md.head.json")

    assert not os.path.samestat(
        os.fstat(harness._ledger_fd),  # noqa: SLF001 - adversarial anchor test
        (issued_root / "T_LEDGER.md").stat(),
    )
    with pytest.raises(PermissionError, match="changed identity"):
        harness.entries()
    with pytest.raises(PermissionError, match="changed identity"):
        record_test_t_contact(
            capability=_capability(),
            modulus=10,
            raw_query=canonical_json({"u": "", "v": ""}),
            device_nanoseconds=1,
            timestamp_utc="2026-07-21T00:00:01Z",
            harness=harness,
        )
    substituted = AppendOnlyLedger(issued_root / "T_LEDGER.md")
    replacement_bytes = substituted.path.read_bytes()
    with pytest.raises(LedgerIntegrityError, match="differs from its anchor"):
        substituted.append(
            event="SECOND_FORGED_ENTRY",
            timestamp_utc="2026-07-21T00:00:01Z",
            data={"scientific_outcome": False, "test_only": True},
            expected_file_descriptor=harness._ledger_fd,  # noqa: SLF001
        )
    assert substituted.path.read_bytes() == replacement_bytes
    harness.close()


def test_test_oracle_artifact_cannot_be_admitted_to_q_or_c(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    successor = repository / "successor"
    successor.mkdir(parents=True)
    registry = ProvenanceRegistry(repository / "registry")
    registry.initialize()
    store = ArtifactStore(
        PathPolicy(repository_root=repository, successor_root=successor), registry
    )
    artifact = successor / "test-response.json"
    response = evaluate_test_query(
        capability=_capability(),
        modulus=10,
        raw_query=canonical_json({"u": "", "v": ""}),
    )
    store.write_test_only(
        path=artifact,
        payload=response,
        purpose="test-only-oracle-response",
        capability=make_test_capability("test-response"),
    )
    for surface in (Surface.Q, Surface.C):
        with pytest.raises(QuarantineViolation, match="cannot enter"):
            store.admit(artifact, surface=surface)
