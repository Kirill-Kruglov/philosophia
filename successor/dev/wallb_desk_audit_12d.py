#!/usr/bin/env python3
"""Powered non-citable mechanism screen for the Wall-B semi-Thue cell.

Audit 12d freezes eight presentations, uses independent relevance/calibration/
evaluation panels, and applies paired inference with familywise correction. It
never instantiates ACTIVE or YOKED learners or produces a scientific outcome.
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


SEED = 20260809
ALPHABET = "abcd"
RULES_PER_PRESENTATION = 7
GOALS_PER_STRATUM = 64
WITNESS_STRATA = (6, 10, 14)
START_LENGTH = (6, 9)
MAX_WORD_LENGTH = 18
SEARCH_CAPS = (50, 100, 200, 500, 2_000, 5_000, 20_000)
MAX_SEARCH_CAP = max(SEARCH_CAPS)
MACRO_COUNTS = (0, 8, 32, 64)
MIN_LIBRARY_GAIN_FRACTION = 0.05
CALIBRATION_TARGET = 0.40
CALIBRATION_TOLERANCE = 0.05
PRIMARY_MACRO_COUNT = 8
BOOTSTRAP_RESAMPLES = 20_000
FAMILY_ALPHA = 0.05
COMPLETION_RULE_CAP = RULES_PER_PRESENTATION + max(MACRO_COUNTS)
COMPLETION_PAIR_SCAN_CAP = 2_000_000
COMPLETION_WORD_CAP = 18

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_desk_audit_12d_results.json"
REPORT_PATH = HERE / "WALLB_DESK_AUDIT_12D.md"

FIXED_PRESENTATIONS = (
    (("ab", "cadb"), ("abcc", "da"), ("ba", "bbb"), ("baaa", "ccb"),
     ("bab", "cb"), ("bca", "cc"), ("da", "dd")),
    (("abad", "caa"), ("acdc", "bb"), ("ad", "ccdc"), ("ad", "ddcb"),
     ("bd", "ca"), ("bdb", "dca"), ("cdb", "dc")),
    (("aaa", "bad"), ("abc", "dd"), ("bb", "cc"), ("bcc", "dbcd"),
     ("bcd", "dbcd"), ("cda", "dcdd"), ("dc", "dcab")),
    (("aa", "cbba"), ("aaaa", "ca"), ("ba", "dcb"), ("ca", "cab"),
     ("cadc", "dcc"), ("ccdc", "cdaa"), ("dabb", "dddb")),
    (("aaad", "bb"), ("ac", "cc"), ("ad", "bbdc"), ("bb", "dbcb"),
     ("cc", "cdd"), ("ccd", "dd"), ("da", "dbd")),
    (("aa", "cb"), ("aac", "ba"), ("acac", "dd"), ("ad", "bbdb"),
     ("ca", "ccc"), ("cba", "cc"), ("cbc", "ddd")),
    (("aa", "dac"), ("ab", "bbbc"), ("ab", "cabd"), ("abbd", "add"),
     ("bccb", "cbd"), ("cca", "dccd"), ("ccc", "dac")),
    (("aaab", "dbbb"), ("aab", "bcab"), ("aacd", "abab"), ("acda", "baa"),
     ("adbb", "da"), ("bbbb", "bdbd"), ("cd", "dd")),
)


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
class PatternAction:
    pattern: str
    replacement: str
    witness_cost: int
    is_macro: bool
    order: int


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
    equations: list[Equation], macros: list[OrientedRule]
) -> list[SearchRule]:
    return base_search_rules(equations) + [
        SearchRule(rule.left, rule.right, rule.witness_cost, True)
        for rule in macros
    ]


class RuleIndex:
    """Deterministic trie index over both directions of every rule."""

    def __init__(self, rules: list[SearchRule]) -> None:
        self.goto: list[dict[str, int]] = [{}]
        self.outputs: list[list[PatternAction]] = [[]]
        order = 0
        for rule in rules:
            for pattern, replacement in (
                (rule.left, rule.right),
                (rule.right, rule.left),
            ):
                state = 0
                for char in pattern:
                    if char not in self.goto[state]:
                        self.goto[state][char] = len(self.goto)
                        self.goto.append({})
                        self.outputs.append([])
                    state = self.goto[state][char]
                self.outputs[state].append(
                    PatternAction(
                        pattern,
                        replacement,
                        rule.witness_cost,
                        rule.is_macro,
                        order,
                    )
                )
                order += 1
        for output in self.outputs:
            output.sort(key=lambda action: action.order)

    def matches(self, word: str) -> tuple[list[tuple[int, PatternAction]], int]:
        matches: list[tuple[int, PatternAction]] = []
        transitions = 0
        for start in range(len(word)):
            state = 0
            for char in word[start:]:
                transitions += 1
                if char not in self.goto[state]:
                    break
                state = self.goto[state][char]
                matches.extend((start, action) for action in self.outputs[state])
        return matches, transitions


def neighbors_for_generation(word: str, equations: list[Equation]) -> list[str]:
    seen: set[str] = set()
    for equation in equations:
        for pattern, replacement in (
            (equation.left, equation.right),
            (equation.right, equation.left),
        ):
            for position in range(max(0, len(word) - len(pattern) + 1)):
                if word.startswith(pattern, position):
                    candidate = word[:position] + replacement + word[position + len(pattern) :]
                    if len(candidate) <= MAX_WORD_LENGTH and candidate != word:
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
) -> tuple[str, str, tuple[str, ...]] | None:
    for _ in range(200):
        start = random_word(rng, *START_LENGTH)
        current = start
        path = [start]
        previous: str | None = None
        for _step in range(witness_length):
            choices = [
                word for word in neighbors_for_generation(current, equations)
                if word != previous
            ]
            if not choices:
                break
            previous, current = current, rng.choice(choices)
            path.append(current)
        else:
            if current != start:
                return start, current, tuple(path)
    return None


def verify_macro(rule: OrientedRule, equations: list[Equation]) -> OrientedRule:
    """Validate the primitive derivation carried through completion."""
    path = rule.primitive_path
    if path[0] != rule.left or path[-1] != rule.right:
        raise AssertionError("macro witness endpoints do not match")
    for before, after in zip(path, path[1:]):
        if not is_primitive_step(before, after, equations):
            raise AssertionError(
                f"macro witness contains a non-primitive step: {before!r} -> {after!r}"
            )
    return rule


def surface_distance(word: str, target: str) -> int:
    word_counts = Counter(word)
    target_counts = Counter(target)
    parikh = sum(abs(word_counts[c] - target_counts[c]) for c in ALPHABET)
    return abs(len(word) - len(target)) + parikh


def bidirectional_search(
    start: str,
    target: str,
    index: RuleIndex,
    cap: int,
    *,
    surface_order: bool,
    expanded_match: bool,
) -> tuple[bool, int, int | None]:
    """Level-synchronous bidirectional search with optional within-level order."""
    if start == target:
        return True, 0, 0

    front_a, front_b = {start}, {target}
    seen_a, seen_b = {start}, {target}
    proof_a, proof_b = {start: 0}, {target: 0}
    root_a, root_b = start, target
    work = 0

    while front_a and front_b and work < cap:
        if len(front_a) > len(front_b):
            front_a, front_b = front_b, front_a
            seen_a, seen_b = seen_b, seen_a
            proof_a, proof_b = proof_b, proof_a
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
            matches, transitions = index.matches(word)
            work += transitions
            if work > cap:
                return False, cap, None
            for position, action in matches:
                work += 1 + (
                    action.witness_cost
                    if expanded_match and action.is_macro
                    else 0
                )
                if work > cap:
                    return False, cap, None
                neighbor = (
                    word[:position]
                    + action.replacement
                    + word[position + len(action.pattern) :]
                )
                if (
                    len(neighbor) > MAX_WORD_LENGTH
                    or neighbor == word
                    or neighbor in emitted
                ):
                    continue
                emitted.add(neighbor)
                proof_length = proof_a[word] + action.witness_cost
                if neighbor in seen_b:
                    return True, work, proof_length + proof_b[neighbor]
                if neighbor not in seen_a:
                    seen_a.add(neighbor)
                    proof_a[neighbor] = proof_length
                    next_front.add(neighbor)
        front_a = next_front

    return False, min(work, cap), None


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


def choose_calibration_cap(costs: list[int]) -> tuple[int | None, float]:
    candidates = sorted({cost for cost in costs if cost <= MAX_SEARCH_CAP})
    if not candidates:
        return None, 0.0
    rates = {cap: sum(cost <= cap for cost in costs) / len(costs) for cap in candidates}
    cap = min(candidates, key=lambda value: (abs(rates[value] - CALIBRATION_TARGET), value))
    return cap, rates[cap]


def exact_mcnemar_one_sided(gains: int, losses: int) -> float:
    discordant = gains + losses
    if discordant == 0:
        return 1.0
    numerator = sum(math.comb(discordant, k) for k in range(gains, discordant + 1))
    return numerator / (2 ** discordant)


def paired_bootstrap_lower(gains: list[float], seed: int) -> float:
    rng = random.Random(seed)
    size = len(gains)
    means = [
        sum(gains[rng.randrange(size)] for _ in range(size)) / size
        for _ in range(BOOTSTRAP_RESAMPLES)
    ]
    means.sort()
    quantile = FAMILY_ALPHA / len(FIXED_PRESENTATIONS)
    return means[max(0, math.ceil(quantile * BOOTSTRAP_RESAMPLES) - 1)]


def holm_adjust(p_values: list[float]) -> list[float]:
    adjusted = [1.0] * len(p_values)
    running = 0.0
    for rank, index in enumerate(sorted(range(len(p_values)), key=p_values.__getitem__)):
        running = max(running, min(1.0, (len(p_values) - rank) * p_values[index]))
        adjusted[index] = running
    return adjusted


def sample_panel(
    rng: random.Random, equations: list[Equation]
) -> list[dict[str, object]]:
    panel: list[dict[str, object]] = []
    for witness_length in WITNESS_STRATA:
        while sum(g["witness_length"] == witness_length for g in panel) < GOALS_PER_STRATUM:
            sampled = sample_goal(rng, equations, witness_length)
            if sampled is None:
                break
            start, target, path = sampled
            panel.append(
                {
                    "start": start,
                    "target": target,
                    "path": path,
                    "witness_length": witness_length,
                }
            )
    return panel


def occurrence_count(pattern: str, text: str) -> int:
    return sum(
        text.startswith(pattern, position)
        for position in range(max(0, len(text) - len(pattern) + 1))
    )


def goal_relevant_order(
    macros: list[OrientedRule], relevance_panel: list[dict[str, object]]
) -> tuple[list[OrientedRule], list[int]]:
    corpus = [
        str(word)
        for goal in relevance_panel
        for word in goal["path"]
    ]
    scored = [
        (
            sum(
                occurrence_count(macro.left, word)
                + occurrence_count(macro.right, word)
                for word in corpus
            ),
            macro,
        )
        for macro in macros
    ]
    scored.sort(
        key=lambda item: (
            -item[0],
            item[1].witness_cost,
            shortlex(item[1].left),
            item[1].right,
        )
    )
    return [item[1] for item in scored], [item[0] for item in scored]


def summarize_run(
    costs: list[int], proof_lengths: list[int | None], cap: int
) -> dict[str, float | None]:
    summary: dict[str, float | None] = summarize(costs, cap)
    solved_lengths = [length for length in proof_lengths if length is not None]
    summary["median_expanded_proof_length_solved"] = (
        statistics.median(solved_lengths) if solved_lengths else None
    )
    return summary


def evaluate_curve(
    goals: list[dict[str, object]],
    indexes: dict[int, RuleIndex],
    *,
    expanded_match: bool,
) -> dict[int, dict[str, list[int | None]]]:
    curve = {
        count: {"costs": [], "proof_lengths": []}
        for count in MACRO_COUNTS
    }
    for goal in goals:
        for count in MACRO_COUNTS:
            solved, cost, proof = bidirectional_search(
                str(goal["start"]), str(goal["target"]), indexes[count],
                MAX_SEARCH_CAP, surface_order=False,
                expanded_match=expanded_match,
            )
            curve[count]["costs"].append(stored_cost(solved, cost))
            curve[count]["proof_lengths"].append(proof)
    return curve


def summarize_curve(
    curve: dict[int, dict[str, list[int | None]]], cap: int
) -> dict[str, dict[str, float | None]]:
    return {
        str(count): summarize_run(
            [int(value) for value in values["costs"]],
            values["proof_lengths"], cap,
        )
        for count, values in curve.items()
    }


def audit_presentation(index: int, equations: list[Equation]) -> dict[str, object]:
    presentation_id = stable_hash(index, equations)[:12]
    panel_names = ("relevance", "calibration", "evaluation")
    panel_seeds = {
        name: int(stable_hash("12d", presentation_id, name)[:16], 16)
        for name in panel_names
    }
    panels = {
        name: sample_panel(random.Random(panel_seeds[name]), equations)
        for name in panel_names
    }
    pair_sets = {
        name: {(g["start"], g["target"]) for g in panel}
        for name, panel in panels.items()
    }
    overlap = sum(
        len(pair_sets[a] & pair_sets[b])
        for i, a in enumerate(panel_names)
        for b in panel_names[i + 1:]
    )

    completion_rules, completion = bounded_completion(equations)
    macros = [
        verify_macro(rule, equations)
        for rule in completion_rules[RULES_PER_PRESENTATION:]
    ]
    completion["verified_macro_count"] = len(macros)
    relevant_macros, relevance_scores = goal_relevant_order(macros, panels["relevance"])
    orderings = {"completion": macros, "goal_relevant": relevant_macros}
    indexes = {
        name: {
            count: RuleIndex(combined_search_rules(equations, ordered[:count]))
            for count in MACRO_COUNTS
        }
        for name, ordered in orderings.items()
    }
    calibration_curve = evaluate_curve(
        panels["calibration"], indexes["completion"], expanded_match=False
    )
    calibration_costs = [int(value) for value in calibration_curve[0]["costs"]]
    selected_cap, calibration_rate = choose_calibration_cap(calibration_costs)
    cap = selected_cap or MAX_SEARCH_CAP

    completion_reuse = evaluate_curve(
        panels["evaluation"], indexes["completion"], expanded_match=False
    )
    relevant_reuse = evaluate_curve(
        panels["evaluation"], indexes["goal_relevant"], expanded_match=False
    )
    relevant_expanded = evaluate_curve(
        panels["evaluation"], indexes["goal_relevant"], expanded_match=True
    )
    surface_costs, surface_proofs = [], []
    for goal in panels["evaluation"]:
        solved, cost, proof = bidirectional_search(
            str(goal["start"]), str(goal["target"]), indexes["completion"][0],
            MAX_SEARCH_CAP, surface_order=True, expanded_match=False,
        )
        surface_costs.append(stored_cost(solved, cost))
        surface_proofs.append(proof)

    summaries = {
        "reuse": {
            "completion": summarize_curve(completion_reuse, cap),
            "goal_relevant": summarize_curve(relevant_reuse, cap),
        },
        "expanded_match": {"goal_relevant": summarize_curve(relevant_expanded, cap)},
    }
    base_costs = [int(value) for value in completion_reuse[0]["costs"]]
    primary_costs = [
        int(value) for value in relevant_reuse[PRIMARY_MACRO_COUNT]["costs"]
    ]
    base_solved = [cost <= cap for cost in base_costs]
    primary_solved = [cost <= cap for cost in primary_costs]
    gains = sum(not before and after for before, after in zip(base_solved, primary_solved))
    losses = sum(before and not after for before, after in zip(base_solved, primary_solved))
    paired_gains = [min(before, cap) - min(after, cap) for before, after in zip(base_costs, primary_costs)]
    rm_gain = statistics.mean(paired_gains)
    bootstrap_lower = paired_bootstrap_lower(
        paired_gains, int(stable_hash("bootstrap", presentation_id)[:16], 16)
    )
    raw_p = exact_mcnemar_one_sided(gains, losses)
    base_summary = summaries["reuse"]["completion"]["0"]
    surface_summary = summarize_run(surface_costs, surface_proofs, cap)

    witness_lengths = [float(g["witness_length"]) for g in panels["evaluation"]]
    correlations = {
        "witness_vs_total_length": pearson(
            witness_lengths,
            [float(len(str(g["start"])) + len(str(g["target"]))) for g in panels["evaluation"]],
        ),
        "witness_vs_surface_distance": pearson(
            witness_lengths,
            [float(surface_distance(str(g["start"]), str(g["target"]))) for g in panels["evaluation"]],
        ),
    }
    reasons = []
    expected = GOALS_PER_STRATUM * len(WITNESS_STRATA)
    if any(len(panel) != expected for panel in panels.values()):
        reasons.append("INCOMPLETE_PANEL")
    if overlap:
        reasons.append("PANEL_GOAL_OVERLAP")
    if selected_cap is None or not (
        CALIBRATION_TARGET - CALIBRATION_TOLERANCE
        <= calibration_rate
        <= CALIBRATION_TARGET + CALIBRATION_TOLERANCE
    ):
        reasons.append("CALIBRATION_TARGET_MISSED")
    if len(macros) < max(MACRO_COUNTS):
        reasons.append("INSUFFICIENT_VERIFIED_COMPLETION_MACROS")
    if bool(completion["bounded_complete"]):
        reasons.append("BOUNDED_COMPLETION_CONVERGED")
    if surface_summary["solved_rate"] >= 0.80 or surface_summary["restricted_mean"] <= 0.20 * cap:
        reasons.append("MATCHED_SURFACE_SHORTCUT_SATURATES")
    if any(value is not None and abs(value) >= 0.80 for value in correlations.values()):
        reasons.append("LENGTH_OR_PARIKH_EXPLAINS_LADDER")
    if not any(relevance_scores):
        reasons.append("NO_GOAL_RELEVANCE_SIGNAL")

    outcomes = []
    for goal, before, after, before_ok, after_ok, before_proof, after_proof in zip(
        panels["evaluation"], base_costs, primary_costs, base_solved, primary_solved,
        completion_reuse[0]["proof_lengths"],
        relevant_reuse[PRIMARY_MACRO_COUNT]["proof_lengths"],
    ):
        outcomes.append({
            "goal_id": stable_hash(goal["start"], goal["target"], goal["witness_length"])[:16],
            "witness_length": goal["witness_length"],
            "base_cost": before, "k8_cost": after,
            "base_solved": before_ok, "k8_solved": after_ok,
            "restricted_gain": min(before, cap) - min(after, cap),
            "base_proof_length": before_proof, "k8_proof_length": after_proof,
        })

    return {
        "presentation_id": presentation_id,
        "equations": [[eq.left, eq.right] for eq in equations],
        "panel_seeds": panel_seeds,
        "panel_hashes": {
            name: stable_hash(*((g["start"], g["target"], g["witness_length"]) for g in panel))
            for name, panel in panels.items()
        },
        "panel_goal_overlap": overlap,
        "selected_cap": selected_cap,
        "calibration_rate": calibration_rate,
        "completion": completion,
        "goal_relevance_scores": relevance_scores,
        "at_cap": {"base": base_summary, "surface": surface_summary, "curves": summaries},
        "primary": {
            "macro_count": PRIMARY_MACRO_COUNT,
            "solve_gains": gains, "solve_losses": losses,
            "solve_rate_difference": statistics.mean(primary_solved) - statistics.mean(base_solved),
            "restricted_mean_gain": rm_gain,
            "bootstrap_lower_bonferroni": bootstrap_lower,
            "mcnemar_one_sided_raw_p": raw_p,
            "mcnemar_holm_p": None,
            "mcnemar_holm_all_units_p": None,
        },
        "per_goal_outcomes": outcomes,
        "correlations": correlations,
        "screen_valid": not reasons,
        "decision": "PENDING_HOLM",
        "reasons": reasons,
    }


def metric(summary: dict[str, float]) -> str:
    return f"{summary['solved_rate']:.2f} / {summary['restricted_mean']:.0f}"


def finalize_holm(items: list[dict[str, object]]) -> None:
    all_adjusted = holm_adjust(
        [item["primary"]["mcnemar_one_sided_raw_p"] for item in items]
    )
    valid_items = [item for item in items if item["screen_valid"]]
    valid_adjusted = holm_adjust(
        [item["primary"]["mcnemar_one_sided_raw_p"] for item in valid_items]
    )
    valid_p_by_id = {
        item["presentation_id"]: adjusted_p
        for item, adjusted_p in zip(valid_items, valid_adjusted)
    }
    for item, all_adjusted_p in zip(items, all_adjusted):
        primary = item["primary"]
        primary["mcnemar_holm_all_units_p"] = all_adjusted_p
        adjusted_p = valid_p_by_id.get(item["presentation_id"])
        primary["mcnemar_holm_p"] = adjusted_p
        reasons = item["reasons"]
        if not item["screen_valid"]:
            item["decision"] = "INVALID_UNIT"
            continue
        if primary["solve_rate_difference"] <= 0:
            reasons.append("NO_SOLVE_RATE_IMPROVEMENT")
        if adjusted_p > FAMILY_ALPHA:
            reasons.append("MCNEMAR_HOLM_NOT_SIGNIFICANT")
        if primary["restricted_mean_gain"] < MIN_LIBRARY_GAIN_FRACTION * item["selected_cap"]:
            reasons.append("RESTRICTED_MEAN_GAIN_BELOW_005B")
        if primary["bootstrap_lower_bonferroni"] <= 0:
            reasons.append("PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE")
        item["decision"] = "POWERED_SIGNAL" if not reasons else "REJECT"


def p_value(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.4g}"


def render_report(payload: dict[str, object]) -> str:
    rows, sensitivity_rows = [], []
    for item in payload["presentations"]:
        metrics = item["at_cap"]
        curves = metrics["curves"]
        primary = curves["reuse"]["goal_relevant"]
        expanded = curves["expanded_match"]["goal_relevant"]
        test = item["primary"]
        rows.append(
            f"| `{item['presentation_id']}` | {item['selected_cap']} | "
            f"{item['calibration_rate']:.3f} | {metric(metrics['base'])} | "
            f"{metric(primary['8'])} | {test['solve_gains']}/{test['solve_losses']} | "
            f"{test['mcnemar_one_sided_raw_p']:.4g}/"
            f"{p_value(test['mcnemar_holm_p'])}/"
            f"{test['mcnemar_holm_all_units_p']:.4g} | "
            f"{test['restricted_mean_gain']:.2f}/{test['bootstrap_lower_bonferroni']:.2f} | "
            f"{item['decision']} | {', '.join(item['reasons']) or '-'} |"
        )
        sensitivity_rows.append(
            f"| `{item['presentation_id']}` | "
            f"{metric(primary['32'])} | {metric(primary['64'])} | "
            f"{metric(expanded['8'])} | {metric(metrics['surface'])} |"
        )

    signals = [item for item in payload["presentations"] if item["decision"] == "POWERED_SIGNAL"]
    invalid_units = [item for item in payload["presentations"] if not item["screen_valid"]]
    if signals:
        verdict = "POWERED_SIGNAL_IN_1_OF_8_PENDING_PREREGISTERED_FRAME_AUDIT"
    else:
        verdict = "NO_POWERED_MECHANISM_SIGNAL_CELL_VOID"
    signal_ids = ", ".join(f"`{item['presentation_id']}`" for item in signals) or "none"

    header = f"""# WALLB_DESK_AUDIT_12D

NON-CITABLE powered mechanism screen. No ACTIVE/YOKED learner was instantiated.

## VERDICT: {verdict}

Each presentation independently generates relevance, calibration and evaluation
panels of 192 goals; any observed overlap invalidates only that world-unit and
is reported. K=8
is the sole primary library size. B is selected only on the
calibration panel at target solve rate 0.40 +/- 0.05. Primary inference combines
one-sided exact McNemar with Holm FWER over the valid world-units,
restricted-mean gain >=0.05B and a conservative one-sided paired-bootstrap
lower bound at alpha=0.05/8. Holm over all eight units is retained as a
sensitivity analysis.
Implementation size: {payload['implementation_nonblank_lines']} nonblank lines.

### Primary powered screen

| presentation | B | cal rate | K=0 rate/RM | K=8 rate/RM | gains/losses | raw/Holm-valid/Holm-all p | RM gain/bootstrap lower | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
"""
    sensitivity = """\n\n### Sensitivity

| presentation | reuse K=32 | reuse K=64 | expanded K=8 | surface K=0 |
|---|---:|---:|---:|---:|
"""
    footer = f"""

Powered signals ({len(signals)}): {signal_ids}. This is one signal among eight
sampled presentations, not evidence of a family-wide mechanism. {len(invalid_units)}
non-signal presentations were invalidated locally; Holm over the six valid
units and conservative Holm over all eight give the same signal decision. The
next permitted step is only a preregistered, independently sampled frame audit
with its size, inclusion rule and acceptance rule frozen in advance. No result
here authorizes a world contract, ACTIVE/YOKED arm or family-wide claim.
"""
    return header + "\n".join(rows) + sensitivity + "\n".join(sensitivity_rows) + footer


def main() -> None:
    presentations = []
    for index, raw_equations in enumerate(FIXED_PRESENTATIONS):
        equations = [Equation(*pair) for pair in raw_equations]
        item = audit_presentation(index, equations)
        presentations.append(item)
        print(index + 1, item["presentation_id"], "PENDING_HOLM", flush=True)
    finalize_holm(presentations)

    payload = {
        "schema": "wallb-desk-audit-12d.v2",
        "scientific_outcome": False,
        "supersedes_gate_credit_of": "wallb-desk-audit-12c.v1",
        "seed": SEED,
        "implementation_nonblank_lines": sum(
            bool(line.strip())
            for line in Path(__file__).read_text(encoding="ascii").splitlines()
        ),
        "constants": {
            "alphabet": ALPHABET,
            "presentations": len(FIXED_PRESENTATIONS),
            "rules_per_presentation": RULES_PER_PRESENTATION,
            "goals_per_stratum": GOALS_PER_STRATUM,
            "witness_strata": WITNESS_STRATA,
            "max_word_length": MAX_WORD_LENGTH,
            "search_caps": SEARCH_CAPS,
            "macro_counts": MACRO_COUNTS,
            "min_library_gain_fraction": MIN_LIBRARY_GAIN_FRACTION,
            "primary_macro_count": PRIMARY_MACRO_COUNT,
            "calibration_target": CALIBRATION_TARGET,
            "calibration_tolerance": CALIBRATION_TOLERANCE,
            "bootstrap_resamples": BOOTSTRAP_RESAMPLES,
            "family_alpha": FAMILY_ALPHA,
            "completion_rule_cap": COMPLETION_RULE_CAP,
            "completion_pair_scan_cap": COMPLETION_PAIR_SCAN_CAP,
            "tariffs": ["reuse", "expanded_match"],
            "library_orderings": ["completion", "goal_relevant"],
        },
        "presentations": presentations,
        "valid_holm_family_size": sum(item["screen_valid"] for item in presentations),
        "all_units_holm_family_size": len(presentations),
    }
    RESULTS_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    REPORT_PATH.write_text(render_report(payload), encoding="ascii")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
