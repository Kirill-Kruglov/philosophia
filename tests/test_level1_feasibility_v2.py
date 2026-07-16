from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from types import ModuleType, SimpleNamespace

import pytest
import torch

import philosophia.level1.feasibility as feasibility_module

from philosophia.level1.feasibility import (
    FeasibilityV2Run,
    LatencyAggregate,
    TrajectoryFeasibilityV2,
    report_payload_v2,
)
from philosophia.level1.interlock import (
    ExecutionNotAuthorized,
    bounded_feasibility_check,
    feasibility_v2_capability,
)
from philosophia.level1.public_root import atomic_create_no_replace, canonical_json
from philosophia.level1.serialization import dummy_key
from philosophia.level1.train import (
    FullHistoryStepResult,
    full_history_committee_step,
)


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


def test_full_history_step_detects_optimizer_created_nonfinite_parameter() -> None:
    torch.manual_seed(1)
    models = [_RecordingMember() for _ in range(4)]
    optimizers = [torch.optim.AdamW(model.parameters(), lr=0.01) for model in models]
    original_step = optimizers[0].step

    def poisoning_step(*args, **kwargs):
        value = original_step(*args, **kwargs)
        with torch.no_grad():
            next(models[0].parameters()).fill_(float("inf"))
        return value

    optimizers[0].step = poisoning_step
    capability = bounded_feasibility_check(trajectory_steps=1, scorer_steps=0)
    capability.claim_development_world(0)
    result = full_history_committee_step(
        models,
        optimizers,
        [torch.tensor([1.0, 0.0])],
        [0],
        capability,
    )

    assert result.losses_finite is True
    assert result.parameters_finite is False
    assert result.finite is False
    assert capability.trajectory_steps == 1


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
        return FullHistoryStepResult(
            losses_finite=True,
            parameters_finite=True,
        )

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


def _run_nonfinite_wiring(
    monkeypatch: pytest.MonkeyPatch,
    results: list[FullHistoryStepResult],
    *,
    panel_qualifies: bool,
) -> tuple[FeasibilityV2Run, int]:
    partition = SimpleNamespace(flat_pool_size=100)
    models = [object() for _ in range(4)]
    optimizers = [object() for _ in range(4)]
    panel_calls = 0
    remaining = list(results)

    monkeypatch.setattr(feasibility_module, "CHECKPOINT_CADENCE", 1)
    monkeypatch.setattr(feasibility_module, "partition_cells", lambda key: partition)
    monkeypatch.setattr(feasibility_module, "verify_partition", lambda value: None)
    monkeypatch.setattr(
        feasibility_module,
        "random_static_schedule",
        lambda key, value: tuple(range(len(results))),
    )
    monkeypatch.setattr(
        feasibility_module, "_committee", lambda key, block: (models, optimizers)
    )
    monkeypatch.setattr(feasibility_module, "_dummy_panel", lambda *args, **kwargs: object())
    monkeypatch.setattr(
        feasibility_module,
        "realize_pool_index",
        lambda partition, key, index: SimpleNamespace(left=b"R", right=b"L"),
    )
    monkeypatch.setattr(
        feasibility_module,
        "encode_pair",
        lambda left, right: torch.tensor([len(left), len(right)]),
    )
    monkeypatch.setattr(feasibility_module, "oracle_eq", lambda *args: True)
    monkeypatch.setattr(feasibility_module, "_checkpoint_size", lambda *args, **kwargs: 1)

    def evaluate(*args):
        nonlocal panel_calls
        panel_calls += 1
        return panel_qualifies

    def step(*args):
        capability = args[-1]
        capability.spend_trajectory_step()
        return remaining.pop(0)

    monkeypatch.setattr(feasibility_module, "_panel_qualifies", evaluate)
    monkeypatch.setattr(feasibility_module, "full_history_committee_step", step)
    capability = bounded_feasibility_check(
        trajectory_steps=len(results),
        scorer_steps=0,
    )
    run = feasibility_module.run_noncomparative_feasibility_v2(
        dummy_key("v2-nonfinite"),
        pair_slot=0,
        modulus=66,
        capability=capability,
    )
    return run, panel_calls


def test_post_step_nonfinite_skips_checkpoint_panel_and_censors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    finite = FullHistoryStepResult(True, True)
    nonfinite = FullHistoryStepResult(True, False)
    run, panel_calls = _run_nonfinite_wiring(
        monkeypatch,
        [finite, nonfinite],
        panel_qualifies=False,
    )

    assert run.trajectory.steps_completed == 2
    assert run.trajectory.all_losses_finite is True
    assert run.trajectory.all_parameters_finite is False
    assert run.trajectory.censored_at_b is True
    assert panel_calls == 2  # step 0 and step 1; never the bad step-2 checkpoint


def test_post_step_nonfinite_at_b_preserves_completed_window(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    finite = FullHistoryStepResult(True, True)
    nonfinite = FullHistoryStepResult(True, False)
    run, panel_calls = _run_nonfinite_wiring(
        monkeypatch,
        [finite, finite, finite, finite, nonfinite],
        panel_qualifies=True,
    )

    assert run.trajectory.steps_completed == 5
    assert run.trajectory.all_losses_finite is True
    assert run.trajectory.all_parameters_finite is False
    assert run.trajectory.censored_at_b is False
    assert panel_calls == 5  # step 0 plus steps 1..4; no evaluation after bad step 5


def test_v2_report_surface_is_trajectory_only() -> None:
    latency = LatencyAggregate(2, 1.5, 1.5, 1.0, 2.0)
    run = FeasibilityV2Run(
        TrajectoryFeasibilityV2(latency, 2, True, False, True, True, 1234)
    )
    payload = report_payload_v2(run)
    assert set(payload) == {"trajectory", "projection_scope"}
    assert payload["trajectory"]["censored_at_b"] is True
    assert payload["trajectory"]["all_losses_finite"] is True
    assert payload["trajectory"]["all_parameters_finite"] is False
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


@pytest.mark.parametrize(
    "failure",
    [
        RuntimeError("simulated process failure"),
        ExecutionNotAuthorized("simulated resource wall"),
    ],
)
def test_driver_failure_after_claim_leaves_binary_unset_and_no_report(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: BaseException,
) -> None:
    driver = _load_driver()
    output = tmp_path / "feasibility_v2"
    authorization = {
        "schema": driver.AUTHORIZATION_SCHEMA,
        "token": driver.AUTHORIZATION_TOKEN,
        "reviewed_code_head": "a" * 40,
        "development_world": {"pair_slot": 0, "modulus": 66},
    }
    transcript = {"root_hex": "00" * 32}
    monkeypatch.setattr(
        driver,
        "_preflight",
        lambda repo, expected_head, output_dir: (authorization, transcript),
    )
    monkeypatch.setattr(driver, "configure_canonical_runtime", lambda: None)
    monkeypatch.setattr(driver, "_verify_current_environment", lambda value: None)
    monkeypatch.setattr(driver, "_development_world", lambda value: (0, 66))
    monkeypatch.setattr(driver, "sha256_file", lambda path: "b" * 64)
    monkeypatch.setattr(driver, "feasibility_v2_capability", lambda: object())

    def fail(*args, **kwargs):
        raise failure

    monkeypatch.setattr(driver, "run_noncomparative_feasibility_v2", fail)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "level1_run_feasibility_v2.py",
            "--expected-head",
            "a" * 40,
            "--output-dir",
            str(output),
        ],
    )

    with pytest.raises(type(failure), match=str(failure)):
        driver.main()

    claim = json.loads((output / driver.CLAIM_NAME).read_text())
    assert "censored_at_b" not in claim
    assert claim["censored_at_b_status"] == "unset-until-valid-terminal-report"
    assert not (output / driver.REPORT_NAME).exists()


def test_driver_preflight_failure_creates_no_claim_or_report(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    driver = _load_driver()
    output = tmp_path / "feasibility_v2"

    def fail_preflight(*args, **kwargs):
        raise PermissionError("simulated hash or seal failure")

    monkeypatch.setattr(driver, "_preflight", fail_preflight)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "level1_run_feasibility_v2.py",
            "--expected-head",
            "a" * 40,
            "--output-dir",
            str(output),
        ],
    )

    with pytest.raises(PermissionError, match="hash or seal"):
        driver.main()

    assert not (output / driver.CLAIM_NAME).exists()
    assert not (output / driver.REPORT_NAME).exists()


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
