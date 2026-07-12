from __future__ import annotations

import math
import random

import pytest
import torch
from torch.nn import functional as F

from philosophia.level0.config import (
    RECONSTRUCTION_ID,
    RunConfig,
    artifact_fidelity_arm,
    paper_mainline_arm,
)
from philosophia.level0.data import LearnerView, build_dataset
from philosophia.level0.interlock import ExecutionInterlock
from philosophia.level0.model import GrokkingTransformer
from philosophia.level0.train import make_optimizer, optimization_step


def _small_learner(config: RunConfig) -> LearnerView:
    learner = build_dataset(config).learner
    return LearnerView(
        inputs=learner.inputs[:8],
        targets=learner.targets[:8],
        indices=learner.indices[:8],
    )


def test_companion_v2_config_and_python_shuffle_fixture() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    bundle = build_dataset(config)
    assert RECONSTRUCTION_ID == "level0-companion-v2"
    assert config.warmup_updates == 10
    assert config.model.training_classes == 114
    assert config.model.reporting_classes == 113
    assert bundle.python_version == "3.12.3"
    assert bundle.learner.indices[:12].tolist() == [
        2068,
        1213,
        6243,
        2876,
        7184,
        1686,
        3107,
        4032,
        4705,
        2032,
        10442,
        11534,
    ]
    assert bundle.split_hash == (
        "b864b16accf8202e5dbe9de566f3e53a0750c07009293fd1eb8763657386177f"
    )
    permutation = list(range(113**2))
    random.Random(0).shuffle(permutation)
    assert bundle.learner.indices.tolist() == permutation[:3830]


def test_companion_normal_init_draw_order_and_scale() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    d_model_divisor = math.sqrt(128)
    output_divisor = math.sqrt(114)
    expected: dict[str, torch.Tensor] = {}
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(config.init_seed)
        for name, divisor in (
            ("W_E", d_model_divisor),
            ("W_pos", d_model_divisor),
            ("W_K", d_model_divisor),
            ("W_Q", d_model_divisor),
            ("W_V", d_model_divisor),
            ("W_O", d_model_divisor),
            ("W_in", d_model_divisor),
            ("W_out", d_model_divisor),
            ("W_U", output_divisor),
        ):
            expected[name] = torch.randn_like(getattr(model, name)) / divisor
    for name, value in expected.items():
        assert torch.equal(getattr(model, name), value)
    assert torch.count_nonzero(model.b_in) == 0
    assert torch.count_nonzero(model.b_out) == 0

    records = {record.name: record for record in model.init_scale_observables()}
    assert records["W_E"].configured_divisor == d_model_divisor
    assert records["W_U"].configured_divisor == output_divisor
    for record in records.values():
        assert record.realized_std == pytest.approx(record.expected_std, rel=0.15)


def test_companion_warmup_lr_sequence_updates_zero_through_eleven() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    learner = _small_learner(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    permit = ExecutionInterlock.bounded_check(12)
    results = [
        optimization_step(model, optimizer, learner, interlock=permit)
        for _ in range(12)
    ]
    expected_used = [0.0] + [step * 0.0001 for step in range(1, 10)] + [0.001] * 2
    expected_after = [step * 0.0001 for step in range(1, 10)] + [0.001] * 3
    assert [result.learning_rate_used for result in results] == pytest.approx(expected_used)
    assert [result.learning_rate_after for result in results] == pytest.approx(expected_after)


@pytest.mark.parametrize(
    "config",
    [
        RunConfig(arm=paper_mainline_arm(), master_seed=0),
        RunConfig(arm=artifact_fidelity_arm((1,)), master_seed=1),
    ],
)
def test_post_warmup_adamw_decay_reaches_every_parameter(config: RunConfig) -> None:
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    with torch.no_grad():
        model.b_in.fill_(0.25)
        model.b_out.fill_(-0.5)
    optimizer = make_optimizer(model, config)
    permit = ExecutionInterlock.bounded_check(11)
    parameters = tuple(model.parameters())
    for _ in range(10):
        for parameter in parameters:
            parameter.grad = torch.zeros_like(parameter)
        optimizer.step(interlock=permit)
    before = tuple(parameter.detach().clone() for parameter in parameters)
    assert optimizer.param_groups[0]["lr"] == pytest.approx(0.001)
    for parameter in parameters:
        parameter.grad = torch.zeros_like(parameter)
    optimizer.step(interlock=permit)
    expected_factor = 1.0 - config.learning_rate * config.arm.weight_decay
    for previous, parameter in zip(before, parameters):
        assert torch.allclose(parameter, previous * expected_factor, rtol=2e-7, atol=1e-8)


def test_training_ce_uses_114_logits_while_reporting_contract_is_113() -> None:
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    learner = _small_learner(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    logits = model(learner.inputs)[:, -1]
    expected_114 = F.cross_entropy(logits, learner.targets)
    residue_only_113 = F.cross_entropy(logits[:, :113], learner.targets)
    expected_114.backward()
    assert model.W_U.grad is not None
    assert torch.count_nonzero(model.W_U.grad[:, 113]) > 0
    model.zero_grad(set_to_none=True)
    optimizer = make_optimizer(model, config)
    result = optimization_step(
        model,
        optimizer,
        learner,
        interlock=ExecutionInterlock.single_step_check(),
    )
    assert result.loss == pytest.approx(float(expected_114.detach()))
    assert result.loss != pytest.approx(float(residue_only_113.detach()), abs=1e-7)
