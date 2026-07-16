from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
from types import ModuleType, SimpleNamespace

import pytest
import torch

import philosophia.level1.feasibility as feasibility_module

from philosophia.level1.feasibility import (
    FeasibilityV2Run,
    LatencyAggregate,
    TrajectoryFeasibility,
    report_payload_v2,
)
from philosophia.level1.interlock import (
    ExecutionNotAuthorized,
    bounded_feasibility_check,
    feasibility_v2_capability,
)
from philosophia.level1.public_root import atomic_create_no_replace, canonical_json
from philosophia.level1.serialization import dummy_key
from philosophia.level1.train import UnitStepResult, full_history_committee_step


REPO = Path(__file__).resolve().parents[1]
DRIVER_PATH = REPO / "scripts/level1_run_feasibility_v2.py"


def _load_driver() -> ModuleType:
    specification = importlib.util.spec_from_file_location(
        "level1_run_feasibility_v2_test", DRIVER_PATH
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class _RecordingMember(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.seen: list[torch.Tensor] = []

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        self.seen.append(tokens.detach().clone())
        return self.linear(tokens)


def test_full_history_step_uses_canonical_growing_shared_batch() -> None:
    torch.manual_seed(0)
    models = [_RecordingMember() for _ in range(4)]
    optimizers = [torch.optim.AdamW(model.parameters(), lr=0.01) for model in models]
    first = torch.tensor([1.0, 0.0])
    second = torch.tensor([0.0, 1.0])
    capability = bounded_feasibility_check(trajectory_steps=2, scorer_steps=0)
    capability.claim_development_world(0)

    one = full_history_committee_step(models, optimizers, [first], [0], capability)
    two = full_history_committee_step(
        models, optimizers, [first, second], [0, 1], capability
    )

    assert one.finite and two.finite
    assert capability.trajectory_steps == 2
    expected_one = torch.stack([first])
    expected_two = torch.stack([first, second])
    assert all(torch.equal(model.seen[0], expected_one) for model in models)
    assert all(torch.equal(model.seen[1], expected_two) for model in models)
    assert all(
        parameter.grad is None
        for model in models
        for parameter in model.parameters()
    )

    with pytest.raises(ValueError, match="non-empty and aligned"):
        full_history_committee_step(models, optimizers, [], [], capability)


def test_v2_capability_is_b2000_scorer_zero_and_36_hours() -> None:
    capability = feasibility_v2_capability()
    assert capability.trajectory_cap == 2000
    assert capability.scorer_cap == 0
    assert capability.wall_seconds == 129600
    assert capability.purpose == "level1-noncomparative-feasibility-v2-full-history"
    with pytest.raises(ExecutionNotAuthorized, match="scorer cap"):
        capability.spend_scorer_step()


def test_atomic_create_no_replace_preserves_racing_destination(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    destination = tmp_path / "claim.json"
    atomic_create_no_replace(destination, b"first\n")
    assert destination.read_bytes() == b"first\n"
    with pytest.raises(FileExistsError, match="refusing to replace"):
        atomic_create_no_replace(destination, b"second\n")
    assert destination.read_bytes() == b"first\n"

    raced = tmp_path / "raced.json"

    def collide(
        source: str | bytes | os.PathLike[str],
        target: str | bytes | os.PathLike[str],
    ) -> None:
        del source
        Path(target).write_bytes(b"racer\n")
        raise FileExistsError("simulated no-replace collision")

    monkeypatch.setattr(os, "link", collide)
    with pytest.raises(FileExistsError, match="simulated"):
        atomic_create_no_replace(raced, b"ours\n")
    assert raced.read_bytes() == b"racer\n"
    assert not raced.with_name(f".{raced.name}.tmp").exists()


def _install_v2_bounded_wiring(monkeypatch: pytest.MonkeyPatch) -> list[int]:
    partition = SimpleNamespace(flat_pool_size=100)
    models = [object() for _ in range(4)]
    optimizers = [object() for _ in range(4)]
    seen_history_lengths: list[int] = []

    monkeypatch.setattr(feasibility_module, "CHECKPOINT_CADENCE", 1)
    monkeypatch.setattr(feasibility_module, "partition_cells", lambda key: partition)
    monkeypatch.setattr(feasibility_module, "verify_partition", lambda value: None)
    monkeypatch.setattr(
        feasibility_module,
        "random_static_schedule",
        lambda key, value: (0, 1, 2, 3),
    )
    monkeypatch.setattr(
        feasibility_module, "_committee", lambda key, block: (models, optimizers)
    )
    monkeypatch.setattr(feasibility_module, "_dummy_panel", lambda *args, **kwargs: object())
    monkeypatch.setattr(feasibility_module, "_panel_qualifies", lambda *args: True)
    monkeypatch.setattr(
        feasibility_module,
        "realize_pool_index",
        lambda partition, key, index: SimpleNamespace(
            left=bytes([82]) * (index + 1),
            right=bytes([76]),
        ),
    )
    monkeypatch.setattr(
        feasibility_module,
        "encode_pair",
        lambda left, right: torch.tensor([len(left), len(right)]),
    )
    monkeypatch.setattr(feasibility_module, "oracle_eq", lambda *args: True)
    monkeypatch.setattr(
        feasibility_module,
        "replay_batch_indices",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("v2 called replay")),
    )

    def full_history_step(
        current_models,
        current_optimizers,
        history_tokens,
        history_labels,
        capability,
    ):
        del current_models, current_optimizers
        expected = list(range(1, len(history_tokens) + 1))
        assert [int(token[0]) for token in history_tokens] == expected
        assert history_labels == [1] * len(history_tokens)
        seen_history_lengths.append(len(history_tokens))
        capability.spend_trajectory_step()
        return UnitStepResult(True)

    monkeypatch.setattr(
        feasibility_module, "full_history_committee_step", full_history_step
    )
    monkeypatch.setattr(feasibility_module, "_checkpoint_size", lambda *args, **kwargs: 456)
    return seen_history_lengths


def test_v2_bounded_wiring_uses_full_history_and_no_scorer(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen = _install_v2_bounded_wiring(monkeypatch)
    capability = bounded_feasibility_check(trajectory_steps=4, scorer_steps=0)
    run = feasibility_module.run_noncomparative_feasibility_v2(
        dummy_key("v2-wiring"),
        pair_slot=0,
        modulus=66,
        capability=capability,
    )

    assert seen == [1, 2, 3, 4]
    assert run.trajectory.steps_completed == 4
    assert run.trajectory.censored_at_b is False
    assert run.trajectory.checkpoint_artifact_bytes == 456
    payload = report_payload_v2(run)
    serialized = repr(payload).lower()
    assert "scorer" not in serialized
    assert "loss_series" not in serialized
    assert "query_series" not in serialized
    assert "contrast" in serialized and "no arm or v1/v2 contrast" in serialized

    wrong_capability = bounded_feasibility_check(trajectory_steps=1, scorer_steps=1)
    with pytest.raises(ValueError, match="forbids scorer"):
        feasibility_module.run_noncomparative_feasibility_v2(
            dummy_key("v2-scorer-refusal"),
            pair_slot=0,
            modulus=66,
            capability=wrong_capability,
        )


def test_v2_report_surface_is_trajectory_only() -> None:
    latency = LatencyAggregate(2, 1.5, 1.5, 1.0, 2.0)
    run = FeasibilityV2Run(
        TrajectoryFeasibility(latency, 2, True, True, True, 1234)
    )
    payload = report_payload_v2(run)
    assert set(payload) == {"trajectory", "projection_scope"}
    assert payload["trajectory"]["censored_at_b"] is True
    assert "scorer" not in repr(payload).lower()


def test_v2_driver_environment_must_match_public_root(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    driver = _load_driver()
    transcript = driver._load_canonical(REPO / driver.TRANSCRIPT_RELATIVE)
    current = dict(transcript["environment"])
    monkeypatch.setattr(driver, "_environment", lambda: current)
    driver._verify_current_environment(transcript)

    drifted = dict(current)
    drifted["machine"] = "not-the-drawn-machine"
    monkeypatch.setattr(driver, "_environment", lambda: drifted)
    with pytest.raises(RuntimeError, match="differs from the public-root fingerprint"):
        driver._verify_current_environment(transcript)


def test_v2_driver_surface_is_authorization_gated_and_claim_first() -> None:
    source = DRIVER_PATH.read_text(encoding="utf-8")
    assert "I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2" in source
    assert "philosophia.level1.noncomparative-feasibility.v2" in source
    assert "FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json" in source
    assert '"scorer_steps": 0' in source
    assert "sample_outcome_pairs" not in source
    assert "estimate_contrast" not in source
    assert "choose_n3" not in source
    claim = source.index("atomic_create_no_replace(output_dir / CLAIM_NAME")
    run = source.index("run = run_noncomparative_feasibility_v2(")
    report = source.index("atomic_create_no_replace(output_dir / REPORT_NAME")
    assert claim < run < report
    assert source.count("run_noncomparative_feasibility_v2(") == 1
    assert "run_noncomparative_feasibility(" not in source
    assert "censored_at_b_status" in source
    assert '"v1_v2_contrast": False' in source
    assert "current environment differs from the public-root fingerprint" in source


def _prepare_temp_preflight_repo(tmp_path: Path) -> tuple[ModuleType, Path, str, str]:
    driver = _load_driver()
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.name", "Level1 Test")
    _git(repo, "config", "user.email", "level1-test@example.invalid")

    lineage = (
        driver.TRANSCRIPT_RELATIVE,
        driver.SIGNATURE_RELATIVE,
        *(Path("experiments/level_1_contact") / name for name in driver.AMENDMENT_SHA256),
        *(
            Path("experiments/level_1_contact/feasibility") / name
            for name in driver.V1_EVIDENCE_SHA256
        ),
    )
    for relative in (*lineage, *(Path(path) for path in driver.REVIEWED_SOURCE_PATHS)):
        source = REPO / relative
        destination = repo / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "reviewed v2 sources")
    reviewed = _git(repo, "rev-parse", "HEAD")

    authorization = {
        "schema": driver.AUTHORIZATION_SCHEMA,
        "token": driver.AUTHORIZATION_TOKEN,
        "scientific_outcome": False,
        "execution_once": True,
        "arm": "RANDOM-STATIC",
        "caps": {
            "development_worlds": 1,
            "trajectory_steps": 2000,
            "scorer_steps": 0,
            "wall_seconds": 129600,
        },
        "development_world": {"pair_slot": 0, "modulus": 66},
        "output_directory": driver.CANONICAL_OUTPUT_RELATIVE.as_posix(),
        "reviewed_code_head": reviewed,
        "governing_signature_sha256": driver.SIGNATURE_SHA256,
        "governing_amendment_sha256": driver.AMENDMENT_SHA256,
        "v1_evidence_sha256": driver.V1_EVIDENCE_SHA256,
    }
    authorization_path = repo / driver.AUTHORIZATION_RELATIVE
    authorization_path.parent.mkdir(parents=True, exist_ok=True)
    authorization_path.write_bytes(canonical_json(authorization))
    _git(repo, "add", authorization_path.relative_to(repo).as_posix())
    _git(repo, "commit", "-q", "-m", "authorize v2 fixture")
    head = _git(repo, "rev-parse", "HEAD")
    return driver, repo, reviewed, head


def test_v2_preflight_accepts_exact_lineage_and_rejects_source_drift(
    tmp_path: Path,
) -> None:
    driver, repo, reviewed, head = _prepare_temp_preflight_repo(tmp_path)
    output = repo / driver.CANONICAL_OUTPUT_RELATIVE
    authorization, transcript = driver._preflight(repo, head, output)
    assert authorization["reviewed_code_head"] == reviewed
    assert transcript["scientific_outcome"] is False

    source = repo / driver.REVIEWED_SOURCE_PATHS[0]
    source.write_text(source.read_text() + "\n# drift\n")
    _git(repo, "add", source.relative_to(repo).as_posix())
    _git(repo, "commit", "-q", "-m", "source drift")
    changed = _git(repo, "rev-parse", "HEAD")
    with pytest.raises(RuntimeError, match="source bytes changed"):
        driver._preflight(repo, changed, output)


def test_v2_preflight_rejects_mutated_v1_evidence_and_existing_claim(
    tmp_path: Path,
) -> None:
    driver, repo, _, head = _prepare_temp_preflight_repo(tmp_path)
    output = repo / driver.CANONICAL_OUTPUT_RELATIVE
    output.mkdir(parents=True)
    (output / driver.CLAIM_NAME).write_text("occupied\n")
    with pytest.raises(FileExistsError, match="refusing to repeat"):
        driver._preflight(repo, head, output)

    (output / driver.CLAIM_NAME).unlink()
    evidence = (
        repo
        / "experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json"
    )
    evidence.write_text(evidence.read_text() + " ")
    _git(repo, "add", evidence.relative_to(repo).as_posix())
    _git(repo, "commit", "-q", "-m", "mutate v1 evidence")
    changed = _git(repo, "rev-parse", "HEAD")
    with pytest.raises(PermissionError, match="immutable v1 evidence hash changed"):
        driver._preflight(repo, changed, output)
