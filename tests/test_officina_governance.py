from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from philosophia.officina.canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
)
from philosophia.officina.escrow import envelope_metadata, salted_plaintext_commitment
from philosophia.officina.interlock import (
    ExecutionNotAuthorized,
    execute_c,
    generate_real_world,
    launch_q,
    require_test_only,
    run_real_t,
    test_only_capability as make_test_capability,
)
from philosophia.officina.manifest import (
    behaviorally_equivalent,
    candidate_id,
    canonical_behavior_manifest,
    canonical_candidate_manifest,
)
from philosophia.officina.one_shot import (
    AttemptPhase,
    AttemptRegistry,
    OneShotJournal,
)
from philosophia.officina.prf import (
    CounterStream,
    dummy_key,
    encode_component,
    prf_digest,
    shuffled,
)
from philosophia.officina.terminal import (
    CScientificTerminal,
    CTerminal,
    InvalidCause,
    QTerminal,
    QValidity,
    TEnding,
)


def _manifest(**changes: object) -> dict[str, object]:
    value: dict[str, object] = {
        "schema": "philosophia.officina.candidate.v2",
        "provenance_commit": "a" * 40,
        "behavior_source_sha256": "b" * 64,
        "stack_id": "cpu-test-stack",
        "initialization": {"checkpoint": None, "kind": "from-scratch"},
        "optimizer": {"kind": "AdamW", "lr": "0.001"},
        "policy": {"kind": "random-static"},
        "interface": {"encoding": "tokens-v1"},
        "config": {"width": 16},
        "inert_metadata": {},
    }
    value.update(changes)
    return value


def _journal(tmp_path: Path, attempt_id: int = 1) -> OneShotJournal:
    registry = AttemptRegistry(tmp_path / "registry")
    registry.initialize()
    return OneShotJournal(
        tmp_path / f"attempt-{attempt_id}", attempt_id=attempt_id, registry=registry
    )


def test_canonical_files_create_refuse_replace_and_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "artifact.json"
    payload = canonical_json({"z": 1, "a": [2, 3]})
    atomic_create(path, payload)
    assert load_canonical_json(path) == {"a": [2, 3], "z": 1}
    with pytest.raises(FileExistsError):
        atomic_create(path, payload)
    atomic_replace(path, canonical_json({"version": 2}))
    assert load_canonical_json(path) == {"version": 2}
    with pytest.raises(ValueError):
        canonical_json({"not_finite": float("nan")})


def test_prf_is_typed_domain_separated_and_test_only() -> None:
    assert encode_component(1) != encode_component("1")
    assert len({encode_component(value) for value in (0, -1, (1 << 64) - 1)}) == 3
    assert encode_component("") != encode_component(0)
    assert len(encode_component("x" * 65535)) == 65538
    with pytest.raises(ValueError, match="uint16"):
        encode_component("x" * 65536)
    with pytest.raises(TypeError, match="booleans"):
        encode_component(True)
    key = dummy_key("golden")
    with pytest.raises(PermissionError, match="dummy_key"):
        type(key)()
    fake = SimpleNamespace(_material=b"x" * 32, purpose="forged")
    with pytest.raises(PermissionError, match="not issued"):
        prf_digest(fake, ("OFFICINA", "fake"), 0)
    with pytest.raises(PermissionError, match="not issued"):
        CounterStream(fake, ("OFFICINA", "fake"))
    copied = object.__new__(type(key))
    copied._material = key._material  # noqa: SLF001 - copied-key attack
    copied.purpose = key.purpose
    with pytest.raises(PermissionError, match="not issued"):
        prf_digest(copied, ("OFFICINA", "copied"), 0)
    first = CounterStream(key, ("OFFICINA", "A", 1))
    second = CounterStream(key, ("OFFICINA", "A", 1))
    assert first.digest() == second.digest()
    assert first.digest() == second.digest()
    assert CounterStream(key, ("OFFICINA", "A", 1)).digest() != CounterStream(
        key, ("OFFICINA", "A", "1")
    ).digest()
    assert shuffled(list(range(10)), CounterStream(key, ("shuffle",))) == shuffled(
        list(range(10)), CounterStream(key, ("shuffle",))
    )
    for invalid_counter in (True, -1, 1 << 64):
        with pytest.raises(ValueError, match="uint64"):
            prf_digest(key, ("counter",), invalid_counter)


def test_candidate_identity_excludes_only_whitelisted_inert_metadata() -> None:
    manifest = _manifest()
    assert candidate_id(manifest) == sha256_bytes(canonical_behavior_manifest(manifest))
    provenance_only = _manifest(
        provenance_commit="c" * 40,
        inert_metadata={"comments": "same behavior", "display_name": "candidate"},
    )
    assert behaviorally_equivalent(manifest, provenance_only)
    assert candidate_id(manifest) == candidate_id(provenance_only)
    for changed in (
        _manifest(config={"width": 32}),
        _manifest(behavior_source_sha256="d" * 64),
        _manifest(stack_id="different-stack"),
    ):
        assert not behaviorally_equivalent(manifest, changed)
        assert candidate_id(changed) != candidate_id(manifest)
    with pytest.raises(ValueError, match="fields differ"):
        canonical_candidate_manifest({**manifest, "unknown": "inert?"})
    with pytest.raises(ValueError, match="unrecognized"):
        canonical_candidate_manifest(_manifest(inert_metadata={"unknown": "x"}))
    with pytest.raises(ValueError, match="40-hex"):
        canonical_candidate_manifest(_manifest(provenance_commit="not-a-commit"))
    with pytest.raises(ValueError, match="from scratch"):
        canonical_candidate_manifest(
            _manifest(initialization={"kind": "warm-start", "checkpoint": "old.pt"})
        )


def test_terminal_types_cannot_turn_invalidity_into_science() -> None:
    assert QTerminal(QValidity.PASS, True).competence is True
    assert QTerminal(QValidity.FAIL, False).competence is False
    invalid = QTerminal(QValidity.INVALID, None, InvalidCause.PROCESS)
    assert QTerminal.from_mapping(invalid.to_mapping()) == invalid
    with pytest.raises(ValueError, match="unset"):
        QTerminal(QValidity.INVALID, False, InvalidCause.PROCESS)
    with pytest.raises(ValueError, match="typed"):
        QTerminal("Q_INVALID", None, InvalidCause.PROCESS)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="typed"):
        QTerminal(QValidity.INVALID, None, "PROCESS")  # type: ignore[arg-type]
    assert CTerminal(True, CScientificTerminal.INSUFFICIENT).scientific_label \
        is CScientificTerminal.INSUFFICIENT
    assert CTerminal(False, None, InvalidCause.HASH).scientific_label is None
    with pytest.raises(ValueError, match="scientific label"):
        CTerminal(True, "INSUFFICIENT")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="unset"):
        CTerminal(False, CScientificTerminal.BOUNDARY, InvalidCause.HASH)
    with pytest.raises(ValueError, match="typed"):
        CTerminal(False, None, "HASH")  # type: ignore[arg-type]
    forbidden_labels = [
        *(item.value for item in TEnding),
        *(item.value for item in QValidity),
        *(item.value for item in InvalidCause),
        "T_OPERATIONAL_PAUSE",
        "Q_INVALID:PROCESS",
    ]
    for label in forbidden_labels:
        with pytest.raises(ValueError, match="scientific label"):
            CTerminal(True, label)  # type: ignore[arg-type]


def test_interlock_has_only_test_capability_and_real_entry_points_fail() -> None:
    capability = make_test_capability("governance")
    require_test_only(capability)
    for function in (generate_real_world, run_real_t, launch_q, execute_c):
        with pytest.raises(ExecutionNotAuthorized):
            function()


def test_one_shot_has_exhaustive_charged_transition_partition(tmp_path: Path) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    assert journal.recovery_requires_charge() is False
    journal.arm_draw("sealed-postfreeze-root")
    assert journal.recovery_requires_charge() is True
    with pytest.raises(ValueError, match="only as charged Q invalid"):
        journal.record_q_terminal(QTerminal(QValidity.PASS, True))
    terminal = journal.record_q_terminal(
        QTerminal(QValidity.INVALID, None, InvalidCause.PROCESS)
    )
    assert terminal["payload"]["charged"] is True
    assert terminal["payload"]["q_terminal"]["competence"] is None
    assert journal.recovery_requires_charge() is False


def test_launched_attempts_are_always_charged_and_typed(tmp_path: Path) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    journal.arm_draw("sealed-postfreeze-root")
    journal.record_launch_commitment("b" * 64)
    terminal = journal.record_q_terminal(QTerminal(QValidity.FAIL, False))
    assert terminal["payload"] == {
        "charged": True,
        "q_terminal": {
            "competence": False,
            "invalid_cause": None,
            "validity": "Q_VALID_FAIL",
        },
    }


def test_claimed_attempt_can_close_only_by_signed_pre_entropy_disposition(
    tmp_path: Path,
) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    terminal = journal.record_pre_entropy_disposition(
        signature_id="author-decision-1", reason="candidate withdrawn before launch"
    )
    assert terminal["payload"]["charged"] is False
    assert terminal["payload"]["competence"] is None


@pytest.mark.parametrize("launched", [False, True])
def test_pre_entropy_disposition_is_rejected_after_draw_boundary(
    tmp_path: Path, launched: bool
) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    journal.arm_draw("sealed-postfreeze-root")
    if launched:
        journal.record_launch_commitment("b" * 64)
    with pytest.raises(ValueError, match="only from CLAIMED"):
        journal.record_pre_entropy_disposition(
            signature_id="late-stop", reason="must remain charged"
        )


def test_q_journal_rejects_duck_types_subclasses_and_malicious_payloads(
    tmp_path: Path,
) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    journal.arm_draw("sealed-postfreeze-root")

    class DuckTerminal:
        validity = QValidity.INVALID

        @staticmethod
        def to_mapping() -> dict[str, object]:
            return {
                "competence": True,
                "extra": "injection",
                "invalid_cause": "PROCESS",
                "validity": "Q_INVALID",
            }

    with pytest.raises(TypeError, match="exact QTerminal"):
        journal.record_q_terminal(DuckTerminal())  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="charged Q terminal payload differs"):
        journal._append(  # noqa: SLF001 - direct invariant attack
            AttemptPhase.TERMINAL,
            {"charged": False, "competence": None},
        )


def test_one_shot_registry_blocks_id_reuse_and_suffix_reset(tmp_path: Path) -> None:
    registry = AttemptRegistry(tmp_path / "registry")
    registry.initialize()
    first = OneShotJournal(tmp_path / "first", attempt_id=7, registry=registry)
    first.create_claim("a" * 64)
    first.arm_draw("sealed-postfreeze-root")
    second = OneShotJournal(tmp_path / "second", attempt_id=7, registry=registry)
    with pytest.raises(ValueError, match="already been used"):
        second.create_claim("b" * 64)
    last_event = sorted((tmp_path / "first").glob("*-attempt-*.json"))[-1]
    last_event.unlink()
    with pytest.raises(ValueError, match="head mismatch"):
        first.recovery_requires_charge()


def test_terminal_persistence_crash_is_ambiguous_not_reopenable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    journal.arm_draw("sealed-postfreeze-root")

    def fail_registry_append(**_: object) -> None:
        raise OSError("injected registry persistence failure")

    monkeypatch.setattr(journal.registry, "append", fail_registry_append)
    with pytest.raises(OSError, match="injected"):
        journal.record_q_terminal(
            QTerminal(QValidity.INVALID, None, InvalidCause.PROCESS)
        )
    with pytest.raises(ValueError, match="registry and journal head differ"):
        journal.recovery_requires_charge()


def test_one_shot_journal_detects_content_tampering(tmp_path: Path) -> None:
    journal = _journal(tmp_path)
    journal.create_claim("a" * 64)
    path = next((tmp_path / "attempt-1").glob("*-attempt-*.json"))
    value = json.loads(path.read_bytes())
    value["payload"]["manifest_sha256"] = "b" * 64
    path.write_bytes(canonical_json(value))
    with pytest.raises(ValueError, match="hash mismatch"):
        journal.arm_draw("test")


def test_escrow_building_blocks_use_only_caller_supplied_material() -> None:
    commitment = salted_plaintext_commitment(salt=b"s" * 32, plaintext=b"secret")
    metadata = envelope_metadata(
        ciphertext_sha256="a" * 64,
        salted_plaintext_sha256=commitment,
        contract_hashes={"lock": "b" * 64},
    )
    assert json.loads(metadata)["scientific_outcome"] is False
    with pytest.raises(ValueError, match="32"):
        salted_plaintext_commitment(salt=b"short", plaintext=b"secret")
