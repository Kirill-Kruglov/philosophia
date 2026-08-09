#!/usr/bin/env python3
"""Corrected non-citable desk audit for the Wall-B semi-Thue cell.

This audit compares matched bidirectional searches and asks whether a
completion-derived macro library can lower restricted-mean PREW. It never
instantiates ACTIVE or YOKED learners and cannot produce a scientific outcome.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


SEED = 20260809
ALPHABET = "abcd"
PRESENTATIONS = 8
RULES_PER_PRESENTATION = 7
GOALS_PER_STRATUM = 8
WITNESS_STRATA = (6, 10, 14)
START_LENGTH = (6, 9)
MAX_WORD_LENGTH = 18
SEARCH_CAPS = (500, 2_000, 5_000, 20_000)
MAX_SEARCH_CAP = max(SEARCH_CAPS)
MACRO_COUNTS = (0, 8, 32, 64)
MIN_LIBRARY_GAIN_FRACTION = 0.05
COMPLETION_RULE_CAP = RULES_PER_PRESENTATION + max(MACRO_COUNTS)
COMPLETION_PAIR_SCAN_CAP = 2_000_000
COMPLETION_WORD_CAP = 18

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_desk_audit_12b_results.json"
REPORT_PATH = HERE / "WALLB_DESK_AUDIT_12B.md"


@dataclass(frozen=True)
class Equation:
    left: str
    right: str


@dataclass(frozen=True)
class OrientedRule:
    left: str
    right: str
    primitive_path: tuple[str, ...]

    @property
    def witness_cost(self) -> int:
        return len(self.primitive_path) - 1


@dataclass(frozen=True)
class SearchRule:
    left: str
    right: str
    witness_cost: int
    is_macro: bool


@dataclass(frozen=True)
class VerifiedMacro:
    left: str
    right: str
    primitive_path: tuple[str, ...]

    @property
    def witness_cost(self) -> int:
        return len(self.primitive_path) - 1


def stable_hash(*parts: object) -> str:
    payload = "\x1f".join(str(part) for part in parts).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def shortlex(word: str) -> tuple[int, str]:
    return len(word), word


def orient(
    left: str, right: str, primitive_path: tuple[str, ...]
) -> OrientedRule | None:
    if left == right:
        return None
    if primitive_path[0] != left or primitive_path[-1] != right:
        raise AssertionError("rule witness endpoints do not match")
    if shortlex(left) < shortlex(right):
        left, right = right, left
        primitive_path = tuple(reversed(primitive_path))
    return OrientedRule(left, right, primitive_path)


def base_search_rules(equations: list[Equation]) -> list[SearchRule]:
    return [SearchRule(eq.left, eq.right, 1, False) for eq in equations]


def combined_search_rules(
    equations: list[Equation], macros: list[VerifiedMacro]
) -> list[SearchRule]:
    return base_search_rules(equations) + [
        SearchRule(rule.left, rule.right, rule.witness_cost, True)
        for rule in macros
    ]


def rewrite_attempts(word: str, rules: list[SearchRule]) -> Iterator[tuple[str | None, int]]:
    """Yield candidates in canonical order with their PREW charge.

    Every rule-position attempt costs one. A successful macro match additionally
    costs its stored primitive witness length, including matches whose output is
    too long or duplicates an earlier candidate.
    """
    for rule in rules:
        for pattern, replacement in (
            (rule.left, rule.right),
            (rule.right, rule.left),
        ):
            for position in range(max(0, len(word) - len(pattern) + 1)):
                if not word.startswith(pattern, position):
                    yield None, 1
                    continue
                charge = 1 + (rule.witness_cost if rule.is_macro else 0)
                candidate = word[:position] + replacement + word[position + len(pattern) :]
                if len(candidate) > MAX_WORD_LENGTH or candidate == word:
                    yield None, charge
                else:
                    yield candidate, charge


def neighbors_for_generation(word: str, equations: list[Equation]) -> list[str]:
    seen: set[str] = set()
    for candidate, _charge in rewrite_attempts(word, base_search_rules(equations)):
        if candidate is not None:
            seen.add(candidate)
    return sorted(seen)


def is_primitive_step(before: str, after: str, equations: list[Equation]) -> bool:
    for equation in equations:
        for pattern, replacement in (
            (equation.left, equation.right),
            (equation.right, equation.left),
        ):
            for position in range(max(0, len(before) - len(pattern) + 1)):
                if not before.startswith(pattern, position):
                    continue
                candidate = (
                    before[:position]
                    + replacement
                    + before[position + len(pattern) :]
                )
                if candidate == after and len(candidate) <= MAX_WORD_LENGTH:
                    return True
    return False


def random_word(rng: random.Random, low: int, high: int) -> str:
    return "".join(rng.choice(ALPHABET) for _ in range(rng.randint(low, high)))


def sample_presentation(rng: random.Random) -> list[Equation]:
    equations: set[tuple[str, str]] = set()
    while len(equations) < RULES_PER_PRESENTATION:
        left = random_word(rng, 2, 4)
        right = random_word(rng, 2, 4)
        if left == right:
            continue
        equations.add(tuple(sorted((left, right))))
    return [Equation(*pair) for pair in sorted(equations)]


def sample_goal(
    rng: random.Random, equations: list[Equation], witness_length: int
) -> tuple[str, str] | None:
    for _ in range(200):
        start = random_word(rng, *START_LENGTH)
        current = start
        previous: str | None = None
        for _step in range(witness_length):
            choices = [
                word for word in neighbors_for_generation(current, equations)
                if word != previous
            ]
            if not choices:
                break
            previous, current = current, rng.choice(choices)
        else:
            if current != start:
                return start, current
    return None


def verify_macro(rule: OrientedRule, equations: list[Equation]) -> VerifiedMacro:
    """Validate the primitive derivation carried through completion."""
    path = rule.primitive_path
    if path[0] != rule.left or path[-1] != rule.right:
        raise AssertionError("macro witness endpoints do not match")
    for before, after in zip(path, path[1:]):
        if not is_primitive_step(before, after, equations):
            raise AssertionError(
                f"macro witness contains a non-primitive step: {before!r} -> {after!r}"
            )
    return VerifiedMacro(rule.left, rule.right, path)


def surface_distance(word: str, target: str) -> int:
    word_counts = Counter(word)
    target_counts = Counter(target)
    parikh = sum(abs(word_counts[c] - target_counts[c]) for c in ALPHABET)
    return abs(len(word) - len(target)) + parikh


def bidirectional_search(
    start: str,
    target: str,
    rules: list[SearchRule],
    cap: int,
    *,
    surface_order: bool,
) -> tuple[bool, int]:
    """Level-synchronous bidirectional search with optional within-level order."""
    if start == target:
        return True, 0

    front_a, front_b = {start}, {target}
    seen_a, seen_b = {start}, {target}
    root_a, root_b = start, target
    work = 0

    while front_a and front_b and work < cap:
        if len(front_a) > len(front_b):
            front_a, front_b = front_b, front_a
            seen_a, seen_b = seen_b, seen_a
            root_a, root_b = root_b, root_a

        if surface_order:
            ordered_front = sorted(
                front_a,
                key=lambda word: (surface_distance(word, root_b), word),
            )
        else:
            ordered_front = sorted(front_a)

        next_front: set[str] = set()
        for word in ordered_front:
            emitted: set[str] = set()
            for neighbor, charge in rewrite_attempts(word, rules):
                work += charge
                if work > cap:
                    return False, cap
                if neighbor is None or neighbor in emitted:
                    continue
                emitted.add(neighbor)
                if neighbor in seen_b:
                    return True, work
                if neighbor not in seen_a:
                    seen_a.add(neighbor)
                    next_front.add(neighbor)
        front_a = next_front

    return False, min(work, cap)


def normalize(
    word: str, rules: list[OrientedRule], cap: int = 100_000
) -> tuple[str, int, tuple[str, ...], bool]:
    ordered = sorted(rules, key=lambda rule: shortlex(rule.left), reverse=True)
    work = 0
    primitive_path = [word]
    while work < cap:
        changed = False
        for rule in ordered:
            for position in range(max(0, len(word) - len(rule.left) + 1)):
                work += 1
                if work > cap:
                    return word, cap, tuple(primitive_path), False
                if word.startswith(rule.left, position):
                    prefix = word[:position]
                    suffix = word[position + len(rule.left) :]
                    lifted = [prefix + step + suffix for step in rule.primitive_path]
                    primitive_path.extend(lifted[1:])
                    word = lifted[-1]
                    changed = True
                    break
            if changed:
                break
        if not changed:
            return word, work, tuple(primitive_path), True
    return word, cap, tuple(primitive_path), False


def lift_path(path: tuple[str, ...], prefix: str, suffix: str) -> tuple[str, ...]:
    return tuple(prefix + step + suffix for step in path)


def critical_pairs(
    first: OrientedRule, second: OrientedRule
) -> list[tuple[str, str, tuple[str, ...]]]:
    pairs: dict[tuple[str, str], tuple[str, ...]] = {}
    a, b = first.left, second.left
    for overlap in range(1, min(len(a), len(b)) + 1):
        if a[-overlap:] == b[:overlap]:
            prefix = a[:-overlap]
            suffix = b[overlap:]
            first_branch = lift_path(first.primitive_path, "", suffix)
            second_branch = lift_path(second.primitive_path, prefix, "")
            left, right = first_branch[-1], second_branch[-1]
            pairs.setdefault(
                (left, right),
                tuple(reversed(first_branch)) + second_branch[1:],
            )
    for position in range(max(0, len(a) - len(b) + 1)):
        if a.startswith(b, position):
            prefix = a[:position]
            suffix = a[position + len(b) :]
            second_branch = lift_path(second.primitive_path, prefix, suffix)
            left, right = first.right, second_branch[-1]
            pairs.setdefault(
                (left, right),
                tuple(reversed(first.primitive_path)) + second_branch[1:],
            )
    return [(left, right, pairs[(left, right)]) for left, right in sorted(pairs)]


def bounded_completion(
    equations: list[Equation],
) -> tuple[list[OrientedRule], dict[str, object]]:
    rules = [
        rule
        for equation in equations
        if (
            rule := orient(
                equation.left,
                equation.right,
                (equation.left, equation.right),
            )
        )
    ]
    pair_scans = 0
    skipped_long = 0
    scan_cap_hit = False
    changed = True

    while changed and len(rules) < COMPLETION_RULE_CAP:
        changed = False
        for first in list(rules):
            for second in list(rules):
                for left, right, critical_path in critical_pairs(first, second):
                    pair_scans += 1
                    if pair_scans > COMPLETION_PAIR_SCAN_CAP:
                        scan_cap_hit = True
                        break
                    if max(len(left), len(right)) > COMPLETION_WORD_CAP:
                        skipped_long += 1
                        continue
                    if any(len(step) > COMPLETION_WORD_CAP for step in critical_path):
                        skipped_long += 1
                        continue
                    norm_left, _, path_left, ok_left = normalize(left, rules)
                    norm_right, _, path_right, ok_right = normalize(right, rules)
                    if not (ok_left and ok_right) or norm_left == norm_right:
                        continue
                    primitive_path = (
                        tuple(reversed(path_left))
                        + critical_path[1:]
                        + path_right[1:]
                    )
                    if any(len(step) > COMPLETION_WORD_CAP for step in primitive_path):
                        skipped_long += 1
                        continue
                    new_rule = orient(
                        norm_left,
                        norm_right,
                        primitive_path,
                    )
                    existing = {(rule.left, rule.right) for rule in rules}
                    if new_rule and (new_rule.left, new_rule.right) not in existing:
                        rules.append(new_rule)
                        changed = True
                        break
                if changed or scan_cap_hit:
                    break
            if changed or scan_cap_hit:
                break
        if scan_cap_hit:
            break

    bounded_complete = not changed and not scan_cap_hit and skipped_long == 0
    return rules, {
        "bounded_complete": bounded_complete,
        "derived_rule_count": max(0, len(rules) - RULES_PER_PRESENTATION),
        "pair_scans": pair_scans,
        "rule_cap_hit": len(rules) >= COMPLETION_RULE_CAP,
        "scan_cap_hit": scan_cap_hit,
        "skipped_long_pairs": skipped_long,
        "total_rule_count": len(rules),
    }


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or statistics.pstdev(xs) == 0 or statistics.pstdev(ys) == 0:
        return None
    mean_x, mean_y = statistics.mean(xs), statistics.mean(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - mean_x) ** 2 for x in xs)
        * sum((y - mean_y) ** 2 for y in ys)
    )
    return numerator / denominator


def summarize(costs: list[int], cap: int) -> dict[str, float]:
    return {
        "solved_rate": sum(cost <= cap for cost in costs) / len(costs),
        "restricted_mean": statistics.mean(min(cost, cap) for cost in costs),
    }


def stored_cost(solved: bool, cost: int) -> int:
    return cost if solved else MAX_SEARCH_CAP + 1


def audit_presentation(index: int, rng: random.Random) -> dict[str, object]:
    equations = sample_presentation(rng)
    goals: list[dict[str, object]] = []
    for witness_length in WITNESS_STRATA:
        while sum(g["witness_length"] == witness_length for g in goals) < GOALS_PER_STRATUM:
            sampled = sample_goal(rng, equations, witness_length)
            if sampled is None:
                break
            start, target = sampled
            goals.append(
                {"start": start, "target": target, "witness_length": witness_length}
            )

    completion_rules, completion = bounded_completion(equations)
    candidate_macros = completion_rules[RULES_PER_PRESENTATION:]
    macros = [verify_macro(rule, equations) for rule in candidate_macros]
    completion["verified_macro_count"] = len(macros)
    costs: dict[int, list[int]] = {count: [] for count in MACRO_COUNTS}
    surface_costs: list[int] = []

    for goal in goals:
        start, target = str(goal["start"]), str(goal["target"])
        for count in MACRO_COUNTS:
            rules = combined_search_rules(equations, macros[:count])
            solved, cost = bidirectional_search(
                start, target, rules, MAX_SEARCH_CAP, surface_order=False
            )
            costs[count].append(stored_cost(solved, cost))
        solved, cost = bidirectional_search(
            start,
            target,
            base_search_rules(equations),
            MAX_SEARCH_CAP,
            surface_order=True,
        )
        surface_costs.append(stored_cost(solved, cost))

    selected_cap = next(
        (
            cap
            for cap in SEARCH_CAPS
            if 0.20 <= summarize(costs[0], cap)["solved_rate"] <= 0.60
        ),
        None,
    )
    cap = selected_cap or MAX_SEARCH_CAP
    base_summary = summarize(costs[0], cap)
    surface_summary = summarize(surface_costs, cap)
    library_curve = {
        str(count): summarize(costs[count], cap) for count in MACRO_COUNTS
    }
    gains = {
        str(count): base_summary["restricted_mean"]
        - library_curve[str(count)]["restricted_mean"]
        for count in MACRO_COUNTS[1:]
    }
    helpful_counts = [
        count
        for count in MACRO_COUNTS[1:]
        if gains[str(count)] >= MIN_LIBRARY_GAIN_FRACTION * cap
    ]

    by_stratum: dict[str, object] = {}
    for witness_length in WITNESS_STRATA:
        positions = [
            i for i, goal in enumerate(goals)
            if goal["witness_length"] == witness_length
        ]
        by_stratum[str(witness_length)] = {
            "base": summarize([costs[0][i] for i in positions], cap),
            "surface": summarize([surface_costs[i] for i in positions], cap),
            "library": {
                str(count): summarize([costs[count][i] for i in positions], cap)
                for count in MACRO_COUNTS
            },
        }

    witness_lengths = [float(goal["witness_length"]) for goal in goals]
    total_lengths = [
        float(len(str(goal["start"])) + len(str(goal["target"])))
        for goal in goals
    ]
    surface_distances = [
        float(surface_distance(str(goal["start"]), str(goal["target"])))
        for goal in goals
    ]
    correlations = {
        "witness_vs_total_length": pearson(witness_lengths, total_lengths),
        "witness_vs_surface_distance": pearson(witness_lengths, surface_distances),
    }

    reasons: list[str] = []
    if len(goals) != GOALS_PER_STRATUM * len(WITNESS_STRATA):
        reasons.append("INCOMPLETE_GOAL_PANEL")
    if selected_cap is None:
        reasons.append("NO_20_60_BASE_CAP")
    if len(macros) < max(MACRO_COUNTS):
        reasons.append("INSUFFICIENT_VERIFIED_COMPLETION_MACROS")
    if bool(completion["bounded_complete"]):
        reasons.append("BOUNDED_COMPLETION_CONVERGED")
    if (
        surface_summary["solved_rate"] >= 0.80
        or surface_summary["restricted_mean"] <= 0.20 * cap
    ):
        reasons.append("MATCHED_SURFACE_SHORTCUT_SATURATES")
    if any(
        value is not None and abs(value) >= 0.80
        for value in correlations.values()
    ):
        reasons.append("LENGTH_OR_PARIKH_EXPLAINS_LADDER")
    if not helpful_counts:
        reasons.append("NO_HELPFUL_MACRO_REGION")

    return {
        "presentation_id": stable_hash(index, equations)[:12],
        "equations": [[eq.left, eq.right] for eq in equations],
        "goal_count": len(goals),
        "selected_cap": selected_cap,
        "completion": completion,
        "verified_macros": [
            {
                "left": macro.left,
                "right": macro.right,
                "primitive_witness_length": macro.witness_cost,
                "primitive_path_sha256": stable_hash(*macro.primitive_path),
            }
            for macro in macros
        ],
        "at_cap": {
            "base": base_summary,
            "surface": surface_summary,
            "library_curve": library_curve,
            "library_gain_prew": gains,
        },
        "helpful_macro_counts": helpful_counts,
        "by_witness_stratum": by_stratum,
        "correlations": correlations,
        "decision": "FRAME_MEMBER" if not reasons else "REJECT",
        "reasons": reasons,
    }


def metric(summary: dict[str, float]) -> str:
    return f"{summary['solved_rate']:.2f} / {summary['restricted_mean']:.0f}"


def render_report(payload: dict[str, object]) -> str:
    rows: list[str] = []
    for item in payload["presentations"]:
        metrics = item["at_cap"]
        curve = metrics["library_curve"]
        rows.append(
            f"| `{item['presentation_id']}` | {item['selected_cap'] or 'none'} | "
            f"{metric(metrics['base'])} | {metric(metrics['surface'])} | "
            f"{metric(curve['8'])} | {metric(curve['32'])} | "
            f"{metric(curve['64'])} | {item['completion']['derived_rule_count']} | "
            f"{item['decision']} | {', '.join(item['reasons']) or '-'} |"
        )

    frame = [
        item for item in payload["presentations"]
        if item["decision"] == "FRAME_MEMBER"
    ]
    verdict = "SUPERSEDED_CONFIGURATION_FAILURE"
    frame_ids = ", ".join(f"`{item['presentation_id']}`" for item in frame) or "none"

    return "\n".join(
        [
            "# WALLB_DESK_AUDIT_12B",
            "",
            "NON-CITABLE correction to audit 12. No ACTIVE/YOKED learner was instantiated.",
            "",
            f"## VERDICT: {verdict}",
            "",
            "The data establish only",
            "`VOID_UNDER_PER_MATCH_WITNESS_TARIFF_WITH_LINEAR_RULE_SCAN_AND_COMPLETION_ORDER`.",
            "They do not establish that the equational cell is void. Audit 12c must test an",
            "indexed reusable-macro tariff and a disjoint-panel goal-relevant ordering.",
            "",
            "Metrics are `solved-rate / restricted-mean-PREW` at the K=0",
            "bidirectional-search cap. `surface` is the same level-synchronous",
            "bidirectional search with only within-frontier expansion order changed.",
            "For every rule-position attempt PREW charges 1; a successful macro",
            "match additionally charges its completion-derived primitive witness length.",
            "Each presentation supplies exactly 64 macros in deterministic completion order;",
            "every macro carries a full primitive path and each primitive step is rechecked.",
            "Completion construction is supplied for free in this favorable mechanism",
            "screen; its whole-system cost remains mandatory in any later experiment.",
            "",
            "| presentation | B | K=0 | surface | K=8 | K=32 | K=64 | verified | decision | reasons |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
            *rows,
            "",
            f"Finite development frame ({len(frame)} presentations): {frame_ids}.",
            "The frame is every presentation that passed the registered screens; no",
            "single post-hoc anchor is selected. Presentation is the blocking unit in",
            "any later contract. The sampled goals within one presentation are not",
            "treated as independent world replicates.",
            "",
            "Pass requires a non-saturating matched surface arm and at least one",
            "K>0 whose restricted-mean PREW improves on K=0 by >=0.05B, in addition",
            "to the calibration, non-convergence and ladder checks. Normalization by",
            "a non-confluent partial completion is not used as a solver or utility test.",
            "",
            "A passing frame permits only a finite-frame world contract. It is not",
            "evidence for ACTIVE, YOKED, manufactured experience, transfer, or the",
            "essay's scientific claim.",
            "",
            "## Scope of the kill",
            "",
            "This voids only completion-order libraries under linear rule-position scanning",
            "and a tariff that repays the full witness at every match. It does not prove that",
            "the registered equational cell, or any selected/indexed macro library, is void.",
        ]
    ) + "\n"


def main() -> None:
    rng = random.Random(SEED)
    presentations = []
    for index in range(PRESENTATIONS):
        item = audit_presentation(index, rng)
        presentations.append(item)
        print(index + 1, item["presentation_id"], item["decision"], flush=True)

    payload = {
        "schema": "wallb-desk-audit-12b.v1",
        "scientific_outcome": False,
        "supersedes_gate_credit_of": "wallb-desk-audit-12.v1",
        "seed": SEED,
        "constants": {
            "alphabet": ALPHABET,
            "presentations": PRESENTATIONS,
            "rules_per_presentation": RULES_PER_PRESENTATION,
            "goals_per_stratum": GOALS_PER_STRATUM,
            "witness_strata": WITNESS_STRATA,
            "max_word_length": MAX_WORD_LENGTH,
            "search_caps": SEARCH_CAPS,
            "macro_counts": MACRO_COUNTS,
            "min_library_gain_fraction": MIN_LIBRARY_GAIN_FRACTION,
            "completion_rule_cap": COMPLETION_RULE_CAP,
            "completion_pair_scan_cap": COMPLETION_PAIR_SCAN_CAP,
        },
        "presentations": presentations,
    }
    RESULTS_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    REPORT_PATH.write_text(render_report(payload), encoding="ascii")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
