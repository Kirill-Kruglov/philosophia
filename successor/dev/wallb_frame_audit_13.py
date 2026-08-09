#!/usr/bin/env python3
"""Preregistered non-citable frame audit for the Wall-B semi-Thue cell.

Audit 13 samples forty fresh presentations and applies the fixed audit-12d
qualification predicate. It never instantiates ACTIVE or YOKED learners and
never produces a scientific outcome.
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


FRAME_SEED = 2026080901
FRAME_SIZE = 40
PRESENTATION_DRAW_CAP = 100_000
PANEL_CALL_CAP = 200_000
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
QUALIFICATION_ALPHA = FAMILY_ALPHA / 8
COMPLETION_RULE_CAP = RULES_PER_PRESENTATION + max(MACRO_COUNTS)
COMPLETION_PAIR_SCAN_CAP = 2_000_000
COMPLETION_WORD_CAP = 18

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_frame_audit_13_results.json"
REPORT_PATH = HERE / "WALLB_FRAME_AUDIT_13.md"
AUDIT12_SOURCE_PATH = HERE / "wallb_desk_audit_12d.py"
AUDIT12_RESULTS_PATH = HERE / "wallb_desk_audit_12d_results.json"
AUDIT12_SOURCE_SHA256 = "927c15e773aea97c11b13eaa8ba53003617baa8dcada7e478bec3dee592976cc"
AUDIT12_RESULTS_SHA256 = "73afbec51b4769a51b6185ad1fed58b49ba749cc3a4e1f527d06657f0f183424"

AUDIT12_PRESENTATIONS = (
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


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def presentation_identity(equations: list[Equation]) -> str:
    return stable_hash(*((eq.left, eq.right) for eq in equations))[:12]


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
    quantile = QUALIFICATION_ALPHA
    return means[max(0, math.ceil(quantile * BOOTSTRAP_RESAMPLES) - 1)]


def sample_panel(
    rng: random.Random,
    equations: list[Equation],
    forbidden_pairs: set[tuple[str, str]],
) -> list[dict[str, object]]:
    panel: list[dict[str, object]] = []
    occupied = set(forbidden_pairs)
    calls = 0
    for witness_length in WITNESS_STRATA:
        while sum(g["witness_length"] == witness_length for g in panel) < GOALS_PER_STRATUM:
            calls += 1
            if calls > PANEL_CALL_CAP:
                return panel
            sampled = sample_goal(rng, equations, witness_length)
            if sampled is None:
                continue
            start, target, path = sampled
            pair = (start, target)
            if pair in occupied:
                continue
            occupied.add(pair)
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


def audit_presentation(equations: list[Equation]) -> dict[str, object]:
    presentation_id = presentation_identity(equations)
    panel_names = ("relevance", "calibration", "evaluation")
    panel_seeds = {
        name: int(stable_hash("13", presentation_id, name)[:16], 16)
        for name in panel_names
    }
    panels: dict[str, list[dict[str, object]]] = {}
    occupied_pairs: set[tuple[str, str]] = set()
    for name in panel_names:
        panels[name] = sample_panel(
            random.Random(panel_seeds[name]), equations, occupied_pairs
        )
        occupied_pairs.update(
            (str(goal["start"]), str(goal["target"])) for goal in panels[name]
        )
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
    process_reasons = []
    screen_reasons = []
    expected = GOALS_PER_STRATUM * len(WITNESS_STRATA)
    if any(len(panel) != expected for panel in panels.values()):
        process_reasons.append("INCOMPLETE_PANEL")
    if overlap:
        process_reasons.append("PANEL_GOAL_OVERLAP")
    if selected_cap is None or not (
        CALIBRATION_TARGET - CALIBRATION_TOLERANCE
        <= calibration_rate
        <= CALIBRATION_TARGET + CALIBRATION_TOLERANCE
    ):
        screen_reasons.append("CALIBRATION_TARGET_MISSED")
    if len(macros) < max(MACRO_COUNTS):
        screen_reasons.append("INSUFFICIENT_VERIFIED_COMPLETION_MACROS")
    if bool(completion["bounded_complete"]):
        screen_reasons.append("BOUNDED_COMPLETION_CONVERGED")
    if surface_summary["solved_rate"] >= 0.80 or surface_summary["restricted_mean"] <= 0.20 * cap:
        screen_reasons.append("MATCHED_SURFACE_SHORTCUT_SATURATES")
    if any(value is not None and abs(value) >= 0.80 for value in correlations.values()):
        screen_reasons.append("LENGTH_OR_PARIKH_EXPLAINS_LADDER")
    if not any(relevance_scores):
        screen_reasons.append("NO_GOAL_RELEVANCE_SIGNAL")

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
        },
        "per_goal_outcomes": outcomes,
        "correlations": correlations,
        "process_valid": not process_reasons,
        "process_reasons": process_reasons,
        "screen_reasons": screen_reasons,
        "decision": "PENDING_QUALIFICATION",
    }


def metric(summary: dict[str, float]) -> str:
    return f"{summary['solved_rate']:.2f} / {summary['restricted_mean']:.0f}"


def finalize_qualification(items: list[dict[str, object]]) -> None:
    for item in items:
        primary = item["primary"]
        reasons = list(item["screen_reasons"])
        if not item["process_valid"]:
            item["decision"] = "INVALID_UNIT"
            item["qualification_reasons"] = reasons
            continue
        if primary["solve_rate_difference"] <= 0:
            reasons.append("NO_SOLVE_RATE_IMPROVEMENT")
        if primary["mcnemar_one_sided_raw_p"] > QUALIFICATION_ALPHA:
            reasons.append("MCNEMAR_RAW_ABOVE_000625")
        cap = item["selected_cap"] or MAX_SEARCH_CAP
        if primary["restricted_mean_gain"] < MIN_LIBRARY_GAIN_FRACTION * cap:
            reasons.append("RESTRICTED_MEAN_GAIN_BELOW_005B")
        if primary["bootstrap_lower_bonferroni"] <= 0:
            reasons.append("PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE")
        item["qualification_reasons"] = reasons
        item["decision"] = "SCREEN_QUALIFIED" if not reasons else "NOT_QUALIFIED"


def wilson_interval(successes: int, trials: int) -> tuple[float, float]:
    if trials == 0:
        return 0.0, 1.0
    z = 1.959963984540054
    p = successes / trials
    denominator = 1 + z * z / trials
    center = (p + z * z / (2 * trials)) / denominator
    radius = z * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials)) / denominator
    return center - radius, center + radius


def terminal_verdict(items: list[dict[str, object]], complete: bool) -> str:
    if not complete or any(not item["process_valid"] for item in items):
        return "FRAME_AUDIT_INVALID"
    qualified = sum(item["decision"] == "SCREEN_QUALIFIED" for item in items)
    if qualified >= 5:
        return "MULTI_WORLD_DEVELOPMENT_FRAME_AVAILABLE"
    if qualified:
        return "SPARSE_SELECTION_CONDITIONAL_FRAME_ONLY"
    return "NO_USABLE_FRAME_EQUATIONAL_CELL_VOID"


def render_report(payload: dict[str, object]) -> str:
    rows, sensitivity_rows = [], []
    for item in payload["presentations"]:
        metrics = item["at_cap"]
        curves = metrics["curves"]
        primary = curves["reuse"]["goal_relevant"]
        completion = curves["reuse"]["completion"]
        expanded = curves["expanded_match"]["goal_relevant"]
        test = item["primary"]
        reasons = item["process_reasons"] + item["qualification_reasons"]
        rows.append(
            f"| `{item['presentation_id']}` | {item['selected_cap']} | "
            f"{item['calibration_rate']:.3f} | {metric(metrics['base'])} | "
            f"{metric(primary['8'])} | {test['solve_gains']}/{test['solve_losses']} | "
            f"{test['mcnemar_one_sided_raw_p']:.4g} | "
            f"{test['restricted_mean_gain']:.2f}/{test['bootstrap_lower_bonferroni']:.2f} | "
            f"{item['decision']} | {', '.join(reasons) or '-'} |"
        )
        sensitivity_rows.append(
            f"| `{item['presentation_id']}` | "
            f"{metric(completion['8'])} | "
            f"{metric(primary['32'])} | {metric(primary['64'])} | "
            f"{metric(expanded['8'])} | {metric(metrics['surface'])} |"
        )

    qualified = [
        item for item in payload["presentations"]
        if item["decision"] == "SCREEN_QUALIFIED"
    ]
    qualified_ids = ", ".join(
        f"`{item['presentation_id']}`" for item in qualified
    ) or "none"
    interval = payload["prevalence_wilson_95"]

    header = f"""# WALLB_FRAME_AUDIT_13

NON-CITABLE preregistered frame audit. No ACTIVE/YOKED learner was instantiated.

## VERDICT: {payload['verdict']}

Forty fresh presentations were sampled under the committed audit-13 contract.
Each uses prospectively disjoint relevance, calibration and evaluation panels
of 192 goals. Qualification is the fixed per-unit audit-12d predicate: K=8
improves solve rate, raw one-sided McNemar p<=0.00625, restricted-mean gain
>=0.05B, bootstrap lower bound at 0.00625 above zero, and all structural screens.
Implementation size: {payload['implementation_nonblank_lines']} nonblank lines.

### Fixed qualification screen

| presentation | B | cal rate | K=0 rate/RM | K=8 rate/RM | gains/losses | raw p | RM gain/bootstrap lower | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
"""
    sensitivity = """\n\n### Sensitivity

| presentation | completion K=8 | reuse K=32 | reuse K=64 | expanded K=8 | surface K=0 |
|---|---:|---:|---:|---:|---:|
"""
    footer = f"""

Qualified presentations ({len(qualified)}/40): {qualified_ids}. Estimated joint
generator-and-panel prevalence is {payload['prevalence_hat']:.3f}, Wilson 95%
interval [{interval[0]:.3f}, {interval[1]:.3f}]. Historical audit-12d worlds are
reported only in the JSON calibration block and are not pooled. This gate does
not authorize a world contract, ACTIVE/YOKED arm or scientific claim.
"""
    return header + "\n".join(rows) + sensitivity + "\n".join(sensitivity_rows) + footer


def main() -> None:
    if file_sha256(AUDIT12_SOURCE_PATH) != AUDIT12_SOURCE_SHA256:
        raise RuntimeError("audit-12d source pin mismatch")
    if file_sha256(AUDIT12_RESULTS_PATH) != AUDIT12_RESULTS_SHA256:
        raise RuntimeError("audit-12d result pin mismatch")
    historical = json.loads(AUDIT12_RESULTS_PATH.read_text(encoding="ascii"))
    excluded = {
        presentation_identity([Equation(*pair) for pair in raw_equations])
        for raw_equations in AUDIT12_PRESENTATIONS
    }
    seen = set(excluded)
    rng = random.Random(FRAME_SEED)
    sampled_presentations: list[list[Equation]] = []
    draws = 0
    while len(sampled_presentations) < FRAME_SIZE and draws < PRESENTATION_DRAW_CAP:
        draws += 1
        equations = sample_presentation(rng)
        identity = presentation_identity(equations)
        if identity in seen:
            continue
        seen.add(identity)
        sampled_presentations.append(equations)

    presentations = []
    for index, equations in enumerate(sampled_presentations):
        item = audit_presentation(equations)
        presentations.append(item)
        print(index + 1, item["presentation_id"], "PENDING_QUALIFICATION", flush=True)
    finalize_qualification(presentations)
    complete = len(presentations) == FRAME_SIZE
    verdict = terminal_verdict(presentations, complete)
    qualified_count = sum(
        item["decision"] == "SCREEN_QUALIFIED" for item in presentations
    )
    interval = wilson_interval(qualified_count, len(presentations))

    payload = {
        "schema": "wallb-frame-audit-13.v1",
        "scientific_outcome": False,
        "preregistration_commit": "aa0754929767d988dd4ddc9fb373cb92bb00d781",
        "frame_seed": FRAME_SEED,
        "presentation_draws": draws,
        "verdict": verdict,
        "qualified_count": qualified_count,
        "prevalence_hat": qualified_count / len(presentations) if presentations else 0.0,
        "prevalence_wilson_95": interval,
        "implementation_nonblank_lines": sum(
            bool(line.strip())
            for line in Path(__file__).read_text(encoding="ascii").splitlines()
        ),
        "constants": {
            "alphabet": ALPHABET,
            "presentations": FRAME_SIZE,
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
            "qualification_alpha": QUALIFICATION_ALPHA,
            "completion_rule_cap": COMPLETION_RULE_CAP,
            "completion_pair_scan_cap": COMPLETION_PAIR_SCAN_CAP,
            "tariffs": ["reuse", "expanded_match"],
            "library_orderings": ["completion", "goal_relevant"],
        },
        "presentations": presentations,
        "historical_audit12_calibration": {
            "result_sha256": AUDIT12_RESULTS_SHA256,
            "presentation_ids": [
                item["presentation_id"] for item in historical["presentations"]
            ],
            "decisions": [item["decision"] for item in historical["presentations"]],
        },
    }
    RESULTS_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    REPORT_PATH.write_text(render_report(payload), encoding="ascii")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
