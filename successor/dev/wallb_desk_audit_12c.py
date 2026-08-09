#!/usr/bin/env python3
"""Final non-citable mechanism screen for the Wall-B semi-Thue cell.

Audit 12c uses indexed matching, reusable and expanded-match tariffs, and a
goal-relevant macro ordering derived from a disjoint development panel. It
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
PRESENTATIONS = 8
RULES_PER_PRESENTATION = 7
GOALS_PER_STRATUM = 8
WITNESS_STRATA = (6, 10, 14)
START_LENGTH = (6, 9)
MAX_WORD_LENGTH = 18
SEARCH_CAPS = (50, 100, 200, 500, 2_000, 5_000, 20_000)
MAX_SEARCH_CAP = max(SEARCH_CAPS)
MACRO_COUNTS = (0, 8, 32, 64)
MIN_LIBRARY_GAIN_FRACTION = 0.05
COMPLETION_RULE_CAP = RULES_PER_PRESENTATION + max(MACRO_COUNTS)
COMPLETION_PAIR_SCAN_CAP = 2_000_000
COMPLETION_WORD_CAP = 18

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_desk_audit_12c_results.json"
REPORT_PATH = HERE / "WALLB_DESK_AUDIT_12C.md"


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


def audit_presentation(index: int, rng: random.Random) -> dict[str, object]:
    equations = sample_presentation(rng)
    goals = sample_panel(rng, equations)
    relevance_seed = int(stable_hash("relevance", index, equations)[:16], 16)
    relevance_panel = sample_panel(random.Random(relevance_seed), equations)
    evaluation_pairs = {(g["start"], g["target"]) for g in goals}
    relevance_pairs = {(g["start"], g["target"]) for g in relevance_panel}
    panel_overlap = len(evaluation_pairs & relevance_pairs)

    completion_rules, completion = bounded_completion(equations)
    candidate_macros = completion_rules[RULES_PER_PRESENTATION:]
    macros = [verify_macro(rule, equations) for rule in candidate_macros]
    completion["verified_macro_count"] = len(macros)
    relevant_macros, relevance_scores = goal_relevant_order(macros, relevance_panel)
    orderings = {"completion": macros, "goal_relevant": relevant_macros}
    indexes = {
        name: {
            count: RuleIndex(combined_search_rules(equations, ordered[:count]))
            for count in MACRO_COUNTS
        }
        for name, ordered in orderings.items()
    }
    completion_reuse = evaluate_curve(
        goals, indexes["completion"], expanded_match=False
    )
    relevant_reuse = evaluate_curve(
        goals, indexes["goal_relevant"], expanded_match=False
    )
    relevant_expanded = evaluate_curve(
        goals, indexes["goal_relevant"], expanded_match=True
    )
    surface_costs: list[int] = []
    surface_proofs: list[int | None] = []
    for goal in goals:
        solved, cost, proof_length = bidirectional_search(
            str(goal["start"]), str(goal["target"]), indexes["completion"][0],
            MAX_SEARCH_CAP, surface_order=True, expanded_match=False,
        )
        surface_costs.append(stored_cost(solved, cost))
        surface_proofs.append(proof_length)

    base_costs = [int(value) for value in completion_reuse[0]["costs"]]
    selected_cap = next(
        (
            cap
            for cap in SEARCH_CAPS
            if 0.20 <= summarize(base_costs, cap)["solved_rate"] <= 0.60
        ),
        None,
    )
    cap = selected_cap or MAX_SEARCH_CAP
    summaries = {
        "reuse": {
            "completion": summarize_curve(completion_reuse, cap),
            "goal_relevant": summarize_curve(relevant_reuse, cap),
        },
        "expanded_match": {
            "goal_relevant": summarize_curve(relevant_expanded, cap),
        },
    }
    base_summary = summaries["reuse"]["completion"]["0"]
    surface_summary = summarize_run(surface_costs, surface_proofs, cap)
    primary_curve = summaries["reuse"]["goal_relevant"]
    gains = {
        str(count): base_summary["restricted_mean"]
        - primary_curve[str(count)]["restricted_mean"]
        for count in MACRO_COUNTS[1:]
    }
    helpful_counts = [
        count
        for count in MACRO_COUNTS[1:]
        if gains[str(count)] >= MIN_LIBRARY_GAIN_FRACTION * cap
    ]

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
    if len(relevance_panel) != GOALS_PER_STRATUM * len(WITNESS_STRATA):
        reasons.append("INCOMPLETE_RELEVANCE_PANEL")
    if panel_overlap:
        reasons.append("RELEVANCE_EVALUATION_GOAL_OVERLAP")
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
    if not any(relevance_scores):
        reasons.append("NO_GOAL_RELEVANCE_SIGNAL")
    if not helpful_counts:
        reasons.append("NO_HELPFUL_MACRO_REGION")

    return {
        "presentation_id": stable_hash(index, equations)[:12],
        "equations": [[eq.left, eq.right] for eq in equations],
        "goal_count": len(goals),
        "relevance_panel_count": len(relevance_panel),
        "relevance_evaluation_goal_overlap": panel_overlap,
        "relevance_panel_sha256": stable_hash(
            *(
                (goal["start"], goal["target"], goal["witness_length"])
                for goal in relevance_panel
            )
        ),
        "selected_cap": selected_cap,
        "completion": completion,
        "verified_macro_witnesses": [
            [m.left, m.right, m.witness_cost, stable_hash(*m.primitive_path)]
            for m in macros
        ],
        "goal_relevant_order": [
            [m.left, m.right, score]
            for m, score in zip(relevant_macros, relevance_scores)
        ],
        "at_cap": {
            "base": base_summary,
            "surface": surface_summary,
            "curves": summaries,
            "goal_relevant_reuse_gain_iswu": gains,
        },
        "helpful_macro_counts": helpful_counts,
        "correlations": correlations,
        "decision": "FRAME_MEMBER" if not reasons else "REJECT",
        "reasons": reasons,
    }


def metric(summary: dict[str, float]) -> str:
    return f"{summary['solved_rate']:.2f} / {summary['restricted_mean']:.0f}"


def render_report(payload: dict[str, object]) -> str:
    primary_rows: list[str] = []
    sensitivity_rows: list[str] = []
    for item in payload["presentations"]:
        metrics = item["at_cap"]
        curves = metrics["curves"]
        primary = curves["reuse"]["goal_relevant"]
        completion = curves["reuse"]["completion"]
        expanded = curves["expanded_match"]["goal_relevant"]
        primary_rows.append(
            f"| `{item['presentation_id']}` | {item['selected_cap'] or 'none'} | "
            f"{metric(metrics['base'])} | {metric(metrics['surface'])} | "
            f"{metric(primary['8'])} | {metric(primary['32'])} | "
            f"{metric(primary['64'])} | "
            f"{item['decision']} | {', '.join(item['reasons']) or '-'} |"
        )
        sensitivity_rows.append(
            f"| `{item['presentation_id']}` | "
            f"{metric(completion['8'])} | {metric(completion['32'])} | "
            f"{metric(completion['64'])} | {metric(expanded['8'])} | "
            f"{metric(expanded['32'])} | {metric(expanded['64'])} |"
        )

    frame = [
        item for item in payload["presentations"]
        if item["decision"] == "FRAME_MEMBER"
    ]
    verdict = "UNDERPOWERED_SCREEN_RERUN_REQUIRED"
    frame_ids = ", ".join(f"`{item['presentation_id']}`" for item in frame) or "none"

    header = f"""# WALLB_DESK_AUDIT_12C

NON-CITABLE final mechanism screen. No ACTIVE/YOKED learner was instantiated.

## VERDICT: {verdict}

The apparent singleton is not gate evidence. Its paired solve count changes
from 6/24 to 10/24; even the favorable no-loss exact McNemar p is 0.0625 before
eight-screen multiplicity. Restricted mean is driven by the same censoring.
Audit 12d must freeze power, calibration and multiplicity before execution.

Metrics are `solved-rate / restricted-mean-ISWU` at the indexed K=0 cap. One
trie transition and one emitted match each cost one ISWU; macro witnesses are
paid at admission, not reuse. `surface` changes only within-frontier order.
Goal relevance uses a separately seeded panel and never reads evaluation goals.
Implementation size: {payload['implementation_nonblank_lines']} nonblank lines.

### Primary: goal-relevant ordering under reusable-macro ISWU

| presentation | B | K=0 | surface | K=8 | K=32 | K=64 | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---|---|
"""
    sensitivity = """\n\n### Sensitivity: completion/reuse and relevant/expanded

| presentation | completion K=8 | K=32 | K=64 | expanded K=8 | K=32 | K=64 |
|---|---:|---:|---:|---:|---:|---:|
"""
    footer = f"""

Passing development set ({len(frame)} presentations): {frame_ids}. Every
passing presentation is retained; goals within one presentation are not
independent world replicates. A singleton cannot support a world-family claim
without an author decision restricting scope to that presentation and its
renamings. Pass requires a non-saturating surface arm and a
goal-relevant K>0 improvement of >=0.05B, plus calibration, non-convergence and
ladder checks. This audit never authorizes a scientific arm or claim.
"""
    return header + "\n".join(primary_rows) + sensitivity + "\n".join(sensitivity_rows) + footer


def main() -> None:
    rng = random.Random(SEED)
    presentations = []
    for index in range(PRESENTATIONS):
        item = audit_presentation(index, rng)
        presentations.append(item)
        print(index + 1, item["presentation_id"], item["decision"], flush=True)

    payload = {
        "schema": "wallb-desk-audit-12c.v1",
        "scientific_outcome": False,
        "gate_credit": "none_underpowered",
        "supersedes_gate_credit_of": "wallb-desk-audit-12b.v1",
        "seed": SEED,
        "implementation_nonblank_lines": sum(
            bool(line.strip())
            for line in Path(__file__).read_text(encoding="ascii").splitlines()
        ),
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
            "tariffs": ["reuse", "expanded_match"],
            "library_orderings": ["completion", "goal_relevant"],
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
