from __future__ import annotations

import math
import subprocess
import sys

import pytest
import torch

from philosophia.level1.config import BUDGET, PANEL_STRATUM_COUNTS
from philosophia.level1.interlock import ExecutionNotAuthorized, run_level1_trajectory, unit_step_capability
from philosophia.level1.model import ContactTransformer, build_optimizer, encode_pair, state_hash
from philosophia.level1.scoring import MissingCheckpoint, PanelObservation, checkpoint_qualifies, first_persistent_step, score_stratum
from philosophia.level1.serialization import dummy_key
from philosophia.level1.train import unit_training_step


def _model(member: int = 0) -> ContactTransformer:
    return ContactTransformer(dummy_key("model-init"), block=0, replicate=1, member=member)


def test_model_shapes_determinism_and_bidirectional_padding() -> None:
    model_a = _model()
    model_b = _model()
    tokens = encode_pair(b"RLR", b"LLR").unsqueeze(0)
    assert tokens.shape == (1, 277)
    assert tokens[0, -7:].tolist() == [1, 2, 1, 3, 2, 2, 1]
    logits_a = model_a(tokens)
    logits_b = model_b(tokens)
    assert logits_a.shape == (1, 2)
    assert torch.equal(logits_a, logits_b)
    assert torch.isfinite(logits_a).all()



def test_canonical_runtime_in_fresh_process() -> None:
    code = (
        "from philosophia.level1.model import configure_canonical_runtime; "
        "import torch; configure_canonical_runtime(); "
        "assert torch.get_num_threads() == 1; "
        "assert torch.get_num_interop_threads() == 1"
    )
    completed = subprocess.run([sys.executable, "-c", code], check=False, capture_output=True, text=True)
    assert completed.returncode == 0, completed.stderr

def test_init_scales_and_optimizer_groups() -> None:
    model = _model()
    assert model.token_embedding.shape == (4, 128)
    assert model.position_embedding.shape == (277, 128)
    assert model.layers[0].W_in.shape == (128, 512)
    assert model.layers[0].W_out.shape == (512, 128)
    assert model.head_W.shape == (128, 2)
    assert abs(float(model.layers[0].W_Q.detach().std(unbiased=False)) - 1 / math.sqrt(128)) < 0.005
    assert abs(float(model.layers[0].W_out.detach().std(unbiased=False)) - 1 / math.sqrt(512)) < 0.003
    optimizer = build_optimizer(model)
    assert len(optimizer.param_groups) == 2
    assert [group["weight_decay"] for group in optimizer.param_groups] == [0.01, 0.0]
    assert sum(len(group["params"]) for group in optimizer.param_groups) == len(list(model.parameters()))


def test_unit_step_is_single_use_and_trajectory_fails_closed() -> None:
    model = _model()
    optimizer = build_optimizer(model)
    tokens = torch.stack((encode_pair(b"R", b"R"), encode_pair(b"R", b"L")))
    labels = torch.tensor([1, 0], dtype=torch.long)
    capability = unit_step_capability()
    before = state_hash(model, optimizer)
    assert unit_training_step(model, optimizer, tokens, labels, capability).finite
    assert state_hash(model, optimizer) != before
    with pytest.raises(ExecutionNotAuthorized):
        unit_training_step(model, optimizer, tokens, labels, capability)
    with pytest.raises(ExecutionNotAuthorized):
        run_level1_trajectory()


def _perfect_panel() -> list[PanelObservation]:
    observations = []
    for stratum, count in PANEL_STRATUM_COUNTS.items():
        for index in range(count):
            truth = stratum != "S1" and index < count // 2
            observations.append(PanelObservation(stratum, truth, 0.99 if truth else 0.01))
    return observations


def test_scoring_is_per_stratum_and_abstain_is_incorrect() -> None:
    panel = _perfect_panel()
    assert checkpoint_qualifies(panel)
    s4 = [item for item in panel if item.stratum == "S4"]
    s4[0] = PanelObservation("S4", s4[0].truth, 0.5)
    score = score_stratum("S4", s4)
    assert score.correct == 15
    assert score.abstentions == 1
    assert score.brier <= 0.10
    assert score.qualifies
    s4[1] = PanelObservation("S4", True, 0.01)
    assert not score_stratum("S4", s4).qualifies


def test_persistence_window_and_missing_checkpoint_routing() -> None:
    curve = {step: False for step in range(0, BUDGET + 1, 50)}
    for step in (1800, 1850, 1900, 1950, 2000):
        curve[step] = True
    assert first_persistent_step(curve) == 1800
    curve[0] = curve[50] = curve[100] = curve[150] = curve[200] = True
    assert first_persistent_step(curve) == 0
    del curve[150]
    with pytest.raises(MissingCheckpoint):
        first_persistent_step(curve)
