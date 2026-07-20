from __future__ import annotations

import json
from pathlib import Path

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
    canonical_candidate_manifest,
)
from philosophia.officina.one_shot import OneShotJournal
from philosophia.officina.prf import CounterStream, dummy_key, shuffled
from philosophia.officina.terminal import (
    CTerminal,
    InvalidCause,
    QTerminal,
    QValidity,
)


def _manifest(**changes: object) -> dict[str, object]:
    value: dict[str, object] = {
        "schema": "philosophia.officina.candidate.v1",
        "code_commit": "a" * 40,
        "stack_id": "cpu-test-stack",
        "initialization": {"checkpoint": None, "kind": "from-scratch"},
        "optimizer": {"kind": "AdamW", "lr": "0.001"},
        "policy": {"kind": "random-static"},
        "interface": {"encoding": "tokens-v1"},
        "config": {"width": 16},
    }
    value.update(changes)
    return value


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


def test_prf_is_domain_separated_deterministic_and_caller_supplied() -> None:
    key = dummy_key("golden")
    first = CounterStream(key, ("OFFICINA", "A", 1))
    second = CounterStream(key, ("OFFICINA", "A", 1))
    other = CounterStream(key, ("OFFICINA", "B", 1))
    assert first.digest() == second.digest()
    assert first.digest() == second.digest()
    assert other.digest() != CounterStream(key, ("OFFICINA", "A", 1)).digest()
    assert shuffled(list(range(10)), CounterStream(key, ("shuffle",))) == shuffled(
        list(range(10)), CounterStream(key, ("shuffle",))
    )


def test_candidate_manifest_is_conservative_and_content_addressed() -> None:
    manifest = _manifest()
    raw = canonical_candidate_manifest(manifest)
    assert candidate_id(manifest) == sha256_bytes(raw)
    assert behaviorally_equivalent(manifest, dict(manifest))
    changed = _manifest(config={"width": 32})
    assert candidate_id(changed) != candidate_id(manifest)
    with pytest.raises(ValueError, match="fields differ"):
        canonical_candidate_manifest({**manifest, "comment": "inert?"})
    with pytest.raises(ValueError, match="40-hex"):
        canonical_candidate_manifest(_manifest(code_commit="not-a-commit"))
    with pytest.raises(ValueError, match="from scratch"):
        canonical_candidate_manifest(
            _manifest(initialization={"kind": "warm-start", "checkpoint": "old.pt"})
        )


def test_terminal_types_cannot_turn_invalidity_into_science() -> None:
    assert QTerminal(QValidity.PASS, True).competence is True
    assert QTerminal(QValidity.FAIL, False).competence is False
    assert QTerminal(QValidity.INVALID, None, InvalidCause.PROCESS).competence is None
    with pytest.raises(ValueError, match="unset"):
        QTerminal(QValidity.INVALID, False, InvalidCause.PROCESS)
    assert CTerminal(True, "INSUFFICIENT").scientific_label == "INSUFFICIENT"
    assert CTerminal(False, None, InvalidCause.HASH).scientific_label is None
    with pytest.raises(ValueError, match="unset"):
        CTerminal(False, "BOUNDARY", InvalidCause.HASH)


def test_interlock_has_only_test_capability_and_real_entry_points_fail() -> None:
    capability = make_test_capability("governance")
    require_test_only(capability)
    for function in (generate_real_world, run_real_t, launch_q, execute_c):
        with pytest.raises(ExecutionNotAuthorized):
            function()


def test_one_shot_journal_is_monotonic_and_ambiguous_draw_armed_is_charged(
    tmp_path: Path,
) -> None:
    journal = OneShotJournal(tmp_path / "attempt")
    journal.create_claim({"attempt_id": 1, "manifest": "a" * 64})
    assert journal.recovery_requires_charge() is False
    journal.arm_draw({"source": "caller-owned-future-root"})
    assert journal.recovery_requires_charge() is True
    journal.record_launch_commitment("b" * 64)
    assert journal.recovery_requires_charge() is True
    journal.record_terminal({"validity": "Q_INVALID:PROCESS", "competence": None})
    assert journal.recovery_requires_charge() is False
    with pytest.raises(ValueError, match="invalid one-shot transition"):
        journal.record_terminal({"again": True})


def test_one_shot_journal_detects_tampering(tmp_path: Path) -> None:
    journal = OneShotJournal(tmp_path / "attempt")
    journal.create_claim({"attempt_id": 1})
    path = next((tmp_path / "attempt").glob("*.json"))
    value = json.loads(path.read_bytes())
    value["payload"]["attempt_id"] = 2
    path.write_bytes(canonical_json(value))
    with pytest.raises(ValueError, match="hash mismatch"):
        journal.arm_draw({"source": "test"})


def test_ambiguous_draw_armed_recovery_closes_as_charged_invalid(tmp_path: Path) -> None:
    journal = OneShotJournal(tmp_path / "attempt")
    journal.create_claim({"attempt_id": 1})
    journal.arm_draw({"source": "future-root"})
    with pytest.raises(ValueError, match="charged with competence unset"):
        journal.record_terminal({"charged": False, "competence": None})
    journal.record_terminal(
        {
            "charged": True,
            "competence": None,
            "validity": "Q_INVALID:PROCESS",
        }
    )
    assert journal.recovery_requires_charge() is False


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
