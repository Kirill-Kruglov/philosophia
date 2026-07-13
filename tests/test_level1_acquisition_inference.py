from __future__ import annotations

import pytest
import torch

from philosophia.level1.acquisition import replay_batch_indices, select_by_disagreement, shortlist
from philosophia.level1.inference import ArmOutcome, BlockOutcome, choose_n3, estimate_contrast, predicate
from philosophia.level1.model import ContactTransformer, build_optimizer, encode_pair, state_hash
from philosophia.level1.routing import FailureCause, Route, route_failure
from philosophia.level1.serialization import dummy_key


def test_shortlist_and_replay_are_domain_reproducible() -> None:
    key = dummy_key("policy")
    first = shortlist(key, block=2, arm_slot="active", step=7, pool_size=1000, answered=frozenset(range(10)))
    second = shortlist(key, block=2, arm_slot="active", step=7, pool_size=1000, answered=frozenset(range(10)))
    assert first == second
    assert len(first) == 512
    assert not set(first) & set(range(10))
    batch = replay_batch_indices(key, block=2, arm="active", replicate=1, step=40, history_size=40)
    assert batch[0] == 39
    assert len(batch) == 32
    assert len(set(batch)) == 32


def test_disagreement_scorer_is_side_effect_free_and_tie_breaks_low() -> None:
    key = dummy_key("committee")
    models = [ContactTransformer(key, block=1, replicate=1, member=member) for member in range(4)]
    optimizers = [build_optimizer(model) for model in models]
    candidates = {
        9: encode_pair(b"R", b"L"),
        3: encode_pair(b"R", b"L"),
    }
    before = [state_hash(model) for model in models]
    choice = select_by_disagreement(models, optimizers, candidates)
    assert choice.pool_index == 3
    assert [state_hash(model) for model in models] == before


def _blocks(n_h: int, active_cost: float, yoked_cost: float, *, solves: tuple[int, int] = (2, 2)) -> list[BlockOutcome]:
    blocks = []
    for stratum in (1, 2, 3):
        for _ in range(n_h):
            blocks.append(
                BlockOutcome(
                    stratum,
                    ArmOutcome(active_cost, solves[0]),
                    ArmOutcome(yoked_cost, solves[1]),
                    ArmOutcome(1500.0, 2),
                )
            )
    return blocks


def test_census_interval_predicates_and_strict_margin() -> None:
    interval = estimate_contrast(_blocks(8, 1000.0, 1100.0), "active", "yoked")
    assert interval.estimate == interval.lower == interval.upper == 100.0
    assert predicate(interval, "SUP")
    assert not predicate(interval, "NONSUP")
    boundary = estimate_contrast(_blocks(8, 1000.0, 1060.0), "active", "yoked")
    assert not predicate(boundary, "SUP")
    assert not predicate(boundary, "NONSUP")
    assert predicate(boundary, "EQ")


def test_determinacy_guard_and_zero_variance_label() -> None:
    neither = estimate_contrast(_blocks(4, 2000.0, 2000.0, solves=(0, 0)), "active", "yoked")
    assert "estimated zero" in neither.variance_label
    assert not any(predicate(neither, name) for name in ("SUP", "EQ", "NI", "NONSUP"))
    one = estimate_contrast(_blocks(4, 2000.0, 1000.0, solves=(0, 2)), "active", "yoked")
    assert not predicate(one, "EQ")
    assert predicate(one, "NONSUP")


@pytest.mark.parametrize("n_h", (2, 3))
def test_outcome_estimator_rejects_unregistered_sample_sizes(n_h: int) -> None:
    with pytest.raises(ValueError, match="equal 4..8"):
        estimate_contrast(_blocks(n_h, 1000.0, 1100.0), "active", "yoked")


def test_non_census_interval_pins_fpc_satterthwaite_and_bonferroni() -> None:
    differences = {
        1: (10.0, 20.0, 30.0, 40.0),
        2: (0.0, 20.0, 40.0, 60.0),
        3: (-10.0, 0.0, 10.0, 20.0),
    }
    blocks = [
        BlockOutcome(
            stratum,
            ArmOutcome(1000.0, 2),
            ArmOutcome(1000.0 + difference, 2),
            ArmOutcome(1500.0, 2),
        )
        for stratum, values in differences.items()
        for difference in values
    ]
    interval = estimate_contrast(blocks, "active", "yoked")

    assert interval.estimate == pytest.approx(20.0)
    assert interval.variance == pytest.approx(13.88888888888889)
    assert interval.degrees_of_freedom == pytest.approx(6.0)
    assert interval.lower == pytest.approx(20.0 - 12.2516220070524)
    assert interval.upper == pytest.approx(20.0 + 12.2516220070524)
    assert interval.variance_label == "estimated finite-population sampling variance"


def test_n3_projection_uses_census_fallback() -> None:
    conservative = {name: {1: 0.0, 2: float("nan"), 3: 0.0} for name in ("A-Y", "Y-R", "A-R")}
    assert choose_n3(conservative) == 24
    tiny = {name: {1: 1.0, 2: 1.0, 3: 1.0} for name in ("A-Y", "Y-R", "A-R")}
    assert choose_n3(tiny) == 12


def test_failure_routes_are_cause_based() -> None:
    assert route_failure(FailureCause.NONFINITE_BEFORE_SOLVE) == Route.CENSOR_AT_B
    assert route_failure(FailureCause.NONFINITE_AFTER_SOLVE) == Route.KEEP_T_WITH_DIAGNOSTIC
    assert route_failure(FailureCause.OUTCOME_INDEPENDENT_PROCESS) == Route.ONE_REEXECUTION
    assert route_failure(FailureCause.OUTCOME_INDEPENDENT_PROCESS, prior_reexecutions=1) == Route.PLATFORM_OR_DESIGN_INVALID
    assert route_failure(FailureCause.SEAL_BREACH) == Route.PLATFORM_OR_DESIGN_INVALID
