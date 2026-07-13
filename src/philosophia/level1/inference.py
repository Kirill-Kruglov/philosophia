from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Literal, Mapping, Sequence

import numpy as np
from scipy.stats import t as student_t

from .config import BUDGET


ArmName = Literal["active", "yoked", "random"]
PredicateName = Literal["SUP", "EQ", "NI", "NONSUP"]
MARGIN = 60.0
FAMILY_ALPHA = 0.05
CONTRAST_COUNT = 3


@dataclass(frozen=True)
class ArmOutcome:
    cost: float
    solve_events: int

    def __post_init__(self) -> None:
        if not 0.0 <= self.cost <= BUDGET:
            raise ValueError("cost must be min(T,B) aggregated over replicates")
        if self.solve_events not in (0, 1, 2):
            raise ValueError("solve_events counts the two frozen replicates")


@dataclass(frozen=True)
class BlockOutcome:
    stratum: int
    active: ArmOutcome
    yoked: ArmOutcome
    random: ArmOutcome

    def __post_init__(self) -> None:
        if self.stratum not in (1, 2, 3):
            raise ValueError("unknown stratum")

    def arm(self, name: ArmName) -> ArmOutcome:
        return getattr(self, name)


@dataclass(frozen=True)
class ContrastInterval:
    x: ArmName
    y: ArmName
    estimate: float
    lower: float
    upper: float
    variance: float
    degrees_of_freedom: float | None
    variance_label: str
    x_solves: int
    y_solves: int


def estimate_contrast(
    blocks: Sequence[BlockOutcome], x: ArmName, y: ArmName
) -> ContrastInterval:
    if x == y:
        raise ValueError("contrast arms must differ")
    by_stratum = {1: [], 2: [], 3: []}
    for block in blocks:
        by_stratum[block.stratum].append(block.arm(y).cost - block.arm(x).cost)
    sizes = {len(values) for values in by_stratum.values()}
    if len(sizes) != 1 or not sizes or next(iter(sizes)) not in range(4, 9):
        raise ValueError("outcome contrast requires equal 4..8 block counts per stratum")
    n_h = next(iter(sizes))
    estimate = sum(float(np.mean(values)) / 3.0 for values in by_stratum.values())
    components = []
    for values in by_stratum.values():
        sample_variance = float(np.var(values, ddof=1))
        components.append((1.0 / 9.0) * (1.0 - n_h / 8.0) * sample_variance / n_h)
    variance = sum(components)
    census = n_h == 8
    if census:
        lower = upper = estimate
        degrees = None
        label = "census certainty over the conditioned 24-block frame"
    elif variance == 0.0:
        lower = upper = estimate
        degrees = None
        label = "estimated zero sample variance, not census certainty"
    else:
        denominator = sum(component**2 / (n_h - 1) for component in components if component > 0)
        degrees = variance**2 / denominator
        critical = float(student_t.ppf(1.0 - FAMILY_ALPHA / (2 * CONTRAST_COUNT), degrees))
        half_width = critical * math.sqrt(variance)
        lower, upper = estimate - half_width, estimate + half_width
        label = "estimated finite-population sampling variance"
    return ContrastInterval(
        x=x,
        y=y,
        estimate=estimate,
        lower=lower,
        upper=upper,
        variance=variance,
        degrees_of_freedom=degrees,
        variance_label=label,
        x_solves=sum(block.arm(x).solve_events for block in blocks),
        y_solves=sum(block.arm(y).solve_events for block in blocks),
    )


def predicate(interval: ContrastInterval, name: PredicateName) -> bool:
    neither = interval.x_solves == 0 and interval.y_solves == 0
    if neither:
        return False
    if name == "EQ" and (interval.x_solves == 0 or interval.y_solves == 0):
        return False
    if name == "SUP":
        return interval.lower > MARGIN
    if name == "EQ":
        return interval.lower >= -MARGIN and interval.upper <= MARGIN
    if name == "NI":
        return interval.lower > -MARGIN
    if name == "NONSUP":
        return interval.upper < MARGIN
    raise ValueError(f"unknown predicate: {name}")


def choose_n3(development_variances: Mapping[str, Mapping[int, float]]) -> int:
    if set(development_variances) != {"A-Y", "Y-R", "A-R"}:
        raise ValueError("projection requires exactly the three frozen contrasts")
    for contrast in development_variances.values():
        if set(contrast) != {1, 2, 3}:
            raise ValueError("each contrast requires all three strata")

    for n3 in (12, 15, 18, 21):
        n_h = n3 // 3
        half_widths = []
        for contrast in development_variances.values():
            components = []
            for stratum in (1, 2, 3):
                observed = contrast[stratum]
                variance = observed if math.isfinite(observed) and observed > 0 else BUDGET**2
                components.append((1.0 / 9.0) * (1.0 - n_h / 8.0) * variance / n_h)
            total = sum(components)
            denominator = sum(component**2 / (n_h - 1) for component in components if component > 0)
            degrees = total**2 / denominator
            critical = float(student_t.ppf(1.0 - FAMILY_ALPHA / (2 * CONTRAST_COUNT), degrees))
            half_widths.append(critical * math.sqrt(total))
        if max(half_widths) <= 30.0:
            return n3
    return 24
