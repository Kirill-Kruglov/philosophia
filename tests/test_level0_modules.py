from __future__ import annotations

import inspect

import pytest
import torch

from philosophia.level0.checkpoint import (
    CheckpointMismatch,
    build_metadata,
    load_checkpoint,
    model_state_hash,
    optimizer_state_hash,
    save_checkpoint,
)
from philosophia.level0.config import (
    ArmConfig,
    RunConfig,
    artifact_fidelity_arm,
    canonical_json,
    config_hash,
    paper_mainline_arm,
)
from philosophia.level0.data import (
    LearnerView,
    build_dataset,
    ordered_modular_addition,
    random_label_control,
)
from philosophia.level0.fourier import project_residue_axis, real_fourier_basis
from philosophia.level0.metrics import (
    Observation,
    _first_persistent_step,
    scored_parameter_l2,
)
from philosophia.level0.interlock import ExecutionInterlock
from philosophia.level0.model import GrokkingTransformer
from philosophia.level0.train import (
    OutcomeRunNotAuthorized,
    make_optimizer,
    optimization_step,
    run_outcome_training,
)


@pytest.fixture(scope="module")
def run_config() -> RunConfig:
    return RunConfig(arm=paper_mainline_arm(), master_seed=0)


def test_arm_serializer_rejects_hybrid_values() -> None:
    arm = paper_mainline_arm()
    config = RunConfig(arm=arm, master_seed=0)
    assert canonical_json(config) == canonical_json(config)
    assert len(config_hash(config)) == 64
    with pytest.raises(ValueError, match="hybrid"):
        ArmConfig(
            identity="A",
            role="paper-mainline-decision",
            weight_decay=0.1,
            fixed_epochs=40_000,
            master_seeds=(0, 1, 2, 3, 4),
        )
    with pytest.raises(ValueError, match="seed 1 alone"):
        artifact_fidelity_arm((1, 2))
    with pytest.raises(ValueError, match="retain master seed 1"):
        artifact_fidelity_arm((0, 2, 3))


def test_modular_dataset_covers_universe_and_split(run_config: RunConfig) -> None:
    inputs, targets = ordered_modular_addition(run_config.model)
    assert inputs.shape == (113**2, 3)
    assert torch.equal(inputs[:, 0] * 113 + inputs[:, 1], torch.arange(113**2))
    assert torch.all(inputs[:, 2] == 113)
    assert torch.equal(targets, (inputs[:, 0] + inputs[:, 1]) % 113)

    bundle = build_dataset(run_config)
    assert bundle.learner.inputs.shape[0] == 3830
    assert bundle.evaluation.inputs.shape[0] == 8939
    joined = torch.cat((bundle.learner.indices, bundle.evaluation.indices))
    assert torch.equal(joined.sort().values, torch.arange(113**2))
    assert len(bundle.split_hash) == 64
    assert bundle.split_hash == build_dataset(run_config).split_hash

    seed_one = RunConfig(arm=paper_mainline_arm(), master_seed=1)
    assert bundle.split_hash != build_dataset(seed_one).split_hash


def test_random_label_control_is_deterministic(run_config: RunConfig) -> None:
    bundle = build_dataset(run_config)
    left = random_label_control(bundle, seed=91)
    right = random_label_control(bundle, seed=91)
    assert torch.equal(left.learner.targets, right.learner.targets)
    assert torch.equal(left.evaluation.targets, right.evaluation.targets)
    assert not torch.equal(left.learner.targets, bundle.learner.targets)
    assert left.split_hash == right.split_hash
    assert left.split_hash != bundle.split_hash


def test_model_shapes_scoring_and_init_observables(run_config: RunConfig) -> None:
    model = GrokkingTransformer(run_config.model, init_seed=run_config.init_seed)
    assert tuple(model.W_E.shape) == (114, 128)
    assert tuple(model.W_pos.shape) == (3, 128)
    assert tuple(model.W_Q.shape) == (4, 32, 128)
    assert tuple(model.W_in.shape) == (512, 128)
    assert tuple(model.W_out.shape) == (128, 512)
    assert tuple(model.W_U.shape) == (128, 114)
    assert not any(isinstance(module, torch.nn.LayerNorm) for module in model.modules())
    assert model.W_E.data_ptr() != model.W_U.data_ptr()

    sample = torch.tensor([[1, 2, 113], [112, 4, 113]])
    logits = model(sample)
    assert logits.shape == (2, 3, 114)
    assert logits[:, -1, :113].shape == (2, 113)

    records = model.init_scale_observables()
    assert len(records) == 21
    assert {record.name for record in records} >= {"W_E", "W_U", "W_Q.0", "W_O.3"}
    assert all(record.xavier_bound > 0 and len(record.sha256) == 64 for record in records)

    replay = GrokkingTransformer(run_config.model, init_seed=run_config.init_seed)
    assert model_state_hash(model) == model_state_hash(replay)


def test_parameter_norm_excludes_equals_column(run_config: RunConfig) -> None:
    model = GrokkingTransformer(run_config.model, init_seed=run_config.init_seed)
    before = scored_parameter_l2(model)
    with torch.no_grad():
        model.W_U[:, 113].add_(1000)
    assert scored_parameter_l2(model) == before


def test_fourier_basis_is_orthonormal_and_projects() -> None:
    basis = real_fourier_basis()
    identity = basis.T @ basis
    assert torch.allclose(identity, torch.eye(113, dtype=basis.dtype), atol=1e-12)
    projected = project_residue_axis(basis[:, 7])
    expected = torch.zeros(113, dtype=basis.dtype)
    expected[7] = 1
    assert torch.allclose(projected, expected, atol=1e-12)


def test_persistence_predicate_has_no_default_window() -> None:
    curve = [
        Observation(0, 0.2),
        Observation(10, 0.95),
        Observation(20, 0.96),
        Observation(30, 0.97),
    ]
    assert _first_persistent_step(curve, threshold=0.95, minimum_step_span=20) == 10
    assert _first_persistent_step(curve, threshold=0.98, minimum_step_span=20) is None


def test_single_step_and_checkpoint_resume_are_identical(
    run_config: RunConfig,
    tmp_path,
) -> None:
    bundle = build_dataset(run_config)
    learner = LearnerView(
        inputs=bundle.learner.inputs[:8],
        targets=bundle.learner.targets[:8],
        indices=bundle.learner.indices[:8],
    )

    model = GrokkingTransformer(run_config.model, init_seed=run_config.init_seed)
    optimizer = make_optimizer(model, run_config)
    original_interlock = ExecutionInterlock.timing_storage_scout()
    first = optimization_step(
        model, optimizer, learner, interlock=original_interlock
    )
    assert first.loss > 0
    assert first.gradient_l2 > 0

    metadata = build_metadata(
        config=run_config,
        split_hash=bundle.split_hash,
        repository_head="test-head",
        source_hashes={"paper": "test-source-hash"},
        model=model,
        optimizer=optimizer,
    )
    path = tmp_path / "roundtrip.pt"
    save_checkpoint(
        path,
        step=1,
        config=run_config,
        model=model,
        optimizer=optimizer,
        metadata=metadata,
    )

    resumed = GrokkingTransformer(run_config.model, init_seed=999)
    resumed_optimizer = make_optimizer(resumed, run_config)
    step, loaded_metadata = load_checkpoint(
        path,
        model=resumed,
        optimizer=resumed_optimizer,
        expected_config_hash=config_hash(run_config),
        expected_split_hash=bundle.split_hash,
    )
    assert step == 1
    assert loaded_metadata.init_scales == metadata.init_scales
    assert model_state_hash(resumed) == metadata.model_state_hash
    assert optimizer_state_hash(resumed_optimizer) == metadata.optimizer_state_hash

    expected_next = optimization_step(
        model, optimizer, learner, interlock=original_interlock
    )
    resumed_next = optimization_step(
        resumed,
        resumed_optimizer,
        learner,
        interlock=ExecutionInterlock.timing_storage_scout(),
    )
    assert expected_next == resumed_next
    assert model_state_hash(model) == model_state_hash(resumed)

    with pytest.raises(CheckpointMismatch, match="split hash"):
        load_checkpoint(
            path,
            model=resumed,
            optimizer=resumed_optimizer,
            expected_config_hash=config_hash(run_config),
            expected_split_hash="wrong",
        )


def test_training_boundary_is_fail_closed() -> None:
    import philosophia.level0.train as train_module

    source = inspect.getsource(train_module)
    assert "level0.metrics" not in source
    assert "EvaluationView" not in source
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    bundle = build_dataset(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    with pytest.raises(TypeError, match="LearnerView only"):
        optimization_step(
            model,
            optimizer,
            bundle.evaluation,
            interlock=ExecutionInterlock.single_step_check(),
        )
    with pytest.raises(OutcomeRunNotAuthorized):
        run_outcome_training()
