from __future__ import annotations

import copy
import inspect
import math

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
    RunConfig,
    artifact_fidelity_arm,
    config_hash,
    paper_mainline_arm,
)
from philosophia.level0.data import LearnerView, build_dataset
from philosophia.level0.interlock import (
    SCOUT_MAX_SECONDS,
    SCOUT_MAX_STEPS,
    ExecutionInterlock,
    ExecutionNotAuthorized,
)
from philosophia.level0.metrics import Observation, evaluate, first_persistent_step
from philosophia.level0.model import GrokkingTransformer
from philosophia.level0.train import make_optimizer, optimization_step


@torch.no_grad()
def _oracle_forward(
    model: GrokkingTransformer,
    tokens: torch.Tensor,
) -> torch.Tensor:
    residual = model.W_E[tokens] + model.W_pos.unsqueeze(0)
    attention_out = torch.zeros_like(residual)
    for batch in range(tokens.shape[0]):
        for query_position in range(model.config.sequence_length):
            for head in range(model.config.heads):
                query = model.W_Q[head] @ residual[batch, query_position]
                scores = []
                values = []
                for key_position in range(query_position + 1):
                    key = model.W_K[head] @ residual[batch, key_position]
                    scores.append((query @ key) / math.sqrt(model.config.head_width))
                    values.append(model.W_V[head] @ residual[batch, key_position])
                weights = torch.softmax(torch.stack(scores), dim=0)
                attended = sum(
                    weight * value for weight, value in zip(weights, values)
                )
                attention_out[batch, query_position] += (
                    attended @ model.W_O[head]
                )
    residual = residual + attention_out
    hidden = torch.relu(residual @ model.W_in.T + model.b_in)
    residual = residual + hidden @ model.W_out.T + model.b_out
    return residual @ model.W_U


def _small_learner(config: RunConfig) -> LearnerView:
    learner = build_dataset(config).learner
    return LearnerView(
        inputs=learner.inputs[:8],
        targets=learner.targets[:8],
        indices=learner.indices[:8],
    )


def test_attention_is_causal_and_normalized() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    tokens = torch.tensor([[7, 19, 113], [3, 101, 113]])
    weights = model.attention_weights(tokens)

    assert weights.shape == (2, 4, 3, 3)
    assert torch.equal(weights[:, :, 0, 1:], torch.zeros_like(weights[:, :, 0, 1:]))
    assert torch.equal(weights[:, :, 1, 2], torch.zeros_like(weights[:, :, 1, 2]))
    assert torch.allclose(weights.sum(dim=-1), torch.ones(2, 4, 3), atol=1e-7)
    assert torch.all(weights[:, :, 2, :] > 0)


def test_forward_matches_independent_loop_oracle() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=2)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    tokens = torch.tensor([[11, 67, 113]])
    actual = model(tokens)
    expected = _oracle_forward(model, tokens)
    assert torch.allclose(actual, expected, rtol=2e-5, atol=2e-6)


def test_final_readout_depends_on_both_operands() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=3)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    tokens = torch.tensor(
        [
            [5, 17, 113],
            [6, 17, 113],
            [5, 18, 113],
        ]
    )
    logits = model(tokens)[:, -1, :113]
    assert not torch.equal(logits[0], logits[1])
    assert not torch.equal(logits[0], logits[2])


@pytest.mark.parametrize(
    ("config", "expected_factor"),
    [
        (RunConfig(arm=paper_mainline_arm(), master_seed=0), 1.0),
        (
            RunConfig(arm=artifact_fidelity_arm((1,)), master_seed=1),
            1.0,
        ),
    ],
)
def test_adamw_uniform_decay_and_optimizer_coverage(
    config: RunConfig,
    expected_factor: float,
) -> None:
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    with torch.no_grad():
        model.b_in.fill_(0.25)
        model.b_out.fill_(-0.5)
    optimizer = make_optimizer(model, config)

    parameters = list(model.parameters())
    group_parameters = optimizer.param_groups[0]["params"]
    assert len(parameters) == 11
    assert len(optimizer.param_groups) == 1
    assert {id(parameter) for parameter in group_parameters} == {
        id(parameter) for parameter in parameters
    }
    assert optimizer.param_groups[0]["weight_decay"] == config.arm.weight_decay

    before = [parameter.detach().clone() for parameter in parameters]
    for parameter in parameters:
        parameter.grad = torch.zeros_like(parameter)
    optimizer.step(interlock=ExecutionInterlock.single_step_check())

    for previous, parameter in zip(before, parameters):
        assert torch.allclose(
            parameter,
            previous * expected_factor,
            rtol=2e-7,
            atol=1e-8,
        )


def test_interlock_blocks_composable_outcome_paths(tmp_path) -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    learner = _small_learner(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    permit = ExecutionInterlock.single_step_check()

    optimization_step(model, optimizer, learner, interlock=permit)
    with pytest.raises(ExecutionNotAuthorized, match="already consumed"):
        optimization_step(
            model,
            optimizer,
            learner,
            interlock=ExecutionInterlock.single_step_check(),
        )
    with pytest.raises(ExecutionNotAuthorized, match="requires an execution"):
        optimizer.step()

    assert SCOUT_MAX_STEPS == 100
    assert SCOUT_MAX_SECONDS == 120.0

    with pytest.raises(ExecutionNotAuthorized, match="cannot evaluate"):
        evaluate(
            model,
            learner.inputs,
            learner.targets,
            interlock=ExecutionInterlock.single_step_check(),
        )
    with pytest.raises(ExecutionNotAuthorized, match="cannot derive"):
        first_persistent_step(
            [Observation(0, 1.0), Observation(10, 1.0)],
            threshold=0.9,
            minimum_step_span=10,
            interlock=ExecutionInterlock.single_step_check(),
        )
    with pytest.raises(ExecutionNotAuthorized, match="real PREREG.lock"):
        ExecutionInterlock.from_preregistration(
            tmp_path / "PREREG.lock",
            spec_path=tmp_path / "SCIENTIFIC_SPEC.json",
            run_id="A-0",
            expected_config_hash=config_hash(config),
            expected_fixed_steps=config.arm.fixed_epochs,
        )


def test_checkpoint_detects_state_and_environment_tampering(tmp_path) -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    bundle = build_dataset(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    metadata = build_metadata(
        purpose="unit-test / non-outcome",
        config=config,
        split_hash=bundle.split_hash,
        repository_head="test-head",
        source_hashes={"paper": "test-source-hash"},
        model=model,
        optimizer=optimizer,
    )
    assert metadata.model_state_hash == model_state_hash(model)
    assert metadata.optimizer_state_hash == optimizer_state_hash(optimizer)

    original = tmp_path / "original.pt"
    save_checkpoint(
        original,
        step=0,
        config=config,
        model=model,
        optimizer=optimizer,
        metadata=metadata,
    )
    payload = torch.load(original, weights_only=True)

    model_corrupt = copy.deepcopy(payload)
    model_corrupt["model_state"]["W_E"][0, 0].add_(1)
    model_path = tmp_path / "model-corrupt.pt"
    torch.save(model_corrupt, model_path)
    with pytest.raises(CheckpointMismatch, match="model state integrity"):
        load_checkpoint(
            model_path,
            model=GrokkingTransformer(config.model, init_seed=config.init_seed),
            optimizer=make_optimizer(
                GrokkingTransformer(config.model, init_seed=config.init_seed),
                config,
            ),
            expected_config_hash=config_hash(config),
            expected_split_hash=bundle.split_hash,
        )

    optimizer_corrupt = copy.deepcopy(payload)
    optimizer_corrupt["optimizer_state"]["optimizer"]["param_groups"][0]["lr"] = 0.25
    optimizer_path = tmp_path / "optimizer-corrupt.pt"
    torch.save(optimizer_corrupt, optimizer_path)
    target = GrokkingTransformer(config.model, init_seed=config.init_seed)
    with pytest.raises(CheckpointMismatch, match="optimizer state integrity"):
        load_checkpoint(
            optimizer_path,
            model=target,
            optimizer=make_optimizer(target, config),
            expected_config_hash=config_hash(config),
            expected_split_hash=bundle.split_hash,
        )

    for field, value, message in (
        ("torch_version", "9.9.9", "pinned PyTorch"),
        ("python_version", "9.9.9", "pinned CPython"),
        ("torch_num_threads", 15, "pinned PyTorch thread counts"),
        ("torch_num_interop_threads", 31, "pinned PyTorch thread counts"),
        ("device", "cuda:0", "requires CPU"),
        ("dtype", "torch.float64", "requires float32"),
    ):
        environment_corrupt = copy.deepcopy(payload)
        environment_corrupt["metadata"][field] = value
        environment_path = tmp_path / f"{field}-corrupt.pt"
        torch.save(environment_corrupt, environment_path)
        target = GrokkingTransformer(config.model, init_seed=config.init_seed)
        with pytest.raises(CheckpointMismatch, match=message):
            load_checkpoint(
                environment_path,
                model=target,
                optimizer=make_optimizer(target, config),
                expected_config_hash=config_hash(config),
                expected_split_hash=bundle.split_hash,
            )
