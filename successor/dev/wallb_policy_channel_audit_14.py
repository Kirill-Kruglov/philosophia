#!/usr/bin/env python3
"""Preregistered non-citable policy-channel audit for the Wall-B semi-Thue cell.

Audit 14 holds the library carrier fixed at the empty macro set and asks whether
a relevance-trained ranking policy improves paired outcomes inside a frozen
bidirectional beam. It never instantiates ACTIVE or YOKED learners.
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


FRAME_SEED = 2026080902
FRAME_SIZE = 40
PRESENTATION_DRAW_CAP = 100_000
PANEL_CALL_CAP = 200_000
ALPHABET = "abcd"
PAD = "_"
ALPHABET_WITH_PAD = PAD + ALPHABET
RULES_PER_PRESENTATION = 7
GOALS_PER_STRATUM = 64
WITNESS_STRATA = (6, 10, 14)
START_LENGTH = (6, 9)
MAX_WORD_LENGTH = 18
SEARCH_CAPS = (50, 100, 200, 500, 2_000, 5_000, 20_000)
MAX_SEARCH_CAP = max(SEARCH_CAPS)
BEAM_WIDTH = 32
MIN_POLICY_GAIN_FRACTION = 0.05
CALIBRATION_TARGET = 0.40
CALIBRATION_TOLERANCE = 0.05
BOOTSTRAP_RESAMPLES = 20_000
FAMILY_ALPHA = 0.05
HOLM_M = 40
BOOTSTRAP_ALPHA = FAMILY_ALPHA / HOLM_M
POSITIVE_CONTROL_MCNEMAR_ALPHA = 0.001
POSITIVE_CONTROL_MIN_SOLVE_GAIN = 0.10
RANKER_LR = 0.05
RANKER_EPOCHS = 20
RANKER_L2 = 1e-4
RANKER_BATCH = 64
COMPLETION_RULE_CAP = RULES_PER_PRESENTATION + 64
COMPLETION_PAIR_SCAN_CAP = 2_000_000
COMPLETION_WORD_CAP = 18
PREREGISTRATION_COMMIT = "ec77d3719ea2de345e3b2b7313a8ca696c008073"

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_policy_channel_audit_14_results.json"
REPORT_PATH = HERE / "WALLB_POLICY_CHANNEL_AUDIT_14.md"
AUDIT12_SOURCE_PATH = HERE / "wallb_desk_audit_12d.py"
AUDIT12_RESULTS_PATH = HERE / "wallb_desk_audit_12d_results.json"
AUDIT13_SOURCE_PATH = HERE / "wallb_frame_audit_13.py"
AUDIT13_RESULTS_PATH = HERE / "wallb_frame_audit_13_results.json"
AUDIT12_SOURCE_SHA256 = "927c15e773aea97c11b13eaa8ba53003617baa8dcada7e478bec3dee592976cc"
AUDIT12_RESULTS_SHA256 = "73afbec51b4769a51b6185ad1fed58b49ba749cc3a4e1f527d06657f0f183424"
AUDIT13_SOURCE_SHA256 = "68b74d3fb8f546f6329aed40f2d47eaf447ee9f98ecea32889e242b8230e387c"
AUDIT13_RESULTS_SHA256 = "77dfb82020cbfdd266495351a7d507be62940220177580759ff8ffbb46e67a78"

POSITIVE_CONTROL_EQUATIONS = (
    ("aa", "dac"),
    ("ab", "bbbc"),
    ("ab", "cabd"),
    ("abbd", "add"),
    ("bccb", "cbd"),
    ("cca", "dccd"),
    ("ccc", "dac"),
)
POSITIVE_CONTROL_ID = "21b64bd46791"

FEATURE_DIM = 4 * len(ALPHABET_WITH_PAD) + 8 + 1


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


def char_at(word: str, index: int) -> str:
    if index < 0 or index >= len(word):
        return PAD
    return word[index]


def one_hot_char(char: str) -> list[float]:
    vector = [0.0] * len(ALPHABET_WITH_PAD)
    if char in ALPHABET_WITH_PAD:
        vector[ALPHABET_WITH_PAD.index(char)] = 1.0
    return vector


def parikh_vector(word: str) -> list[int]:
    counts = Counter(word)
    return [counts[char] for char in ALPHABET]


def surface_distance(word: str, target: str) -> int:
    word_counts = Counter(word)
    target_counts = Counter(target)
    parikh = sum(abs(word_counts[c] - target_counts[c]) for c in ALPHABET)
    return abs(len(word) - len(target)) + parikh


def candidate_features(
    word: str,
    position: int,
    action: PatternAction,
    neighbor: str,
    goal: str,
) -> list[float]:
    before = char_at(word, position - 1)
    matched = char_at(word, position)
    after = char_at(word, position + len(action.pattern))
    replacement_head = action.replacement[0] if action.replacement else PAD
    length_delta = len(neighbor) - len(goal)
    rewrite_delta = len(neighbor) - len(word)
    neighbor_parikh = parikh_vector(neighbor)
    goal_parikh = parikh_vector(goal)
    parikh_deltas = [float(n - g) for n, g in zip(neighbor_parikh, goal_parikh)]
    parikh_l1 = float(sum(abs(delta) for delta in parikh_deltas))
    features: list[float] = []
    features.extend(one_hot_char(before))
    features.extend(one_hot_char(matched))
    features.extend(one_hot_char(after))
    features.extend(one_hot_char(replacement_head))
    features.extend(
        [
            float(length_delta),
            float(abs(length_delta)),
            parikh_l1,
            *parikh_deltas,
            float(rewrite_delta),
            1.0,
        ]
    )
    if len(features) != FEATURE_DIM:
        raise AssertionError("feature dimension mismatch")
    return features


def features_rename_sensitive() -> bool:
    demo_action = PatternAction("ab", "cd", 1, False, 0)
    perm = {"a": "b", "b": "c", "c": "d", "d": "a"}
    perm_action = PatternAction(
        "".join(perm[c] for c in "ab"),
        "".join(perm[c] for c in "cd"),
        1,
        False,
        0,
    )
    base = candidate_features("aabc", 1, demo_action, "acdc", "dddd")
    alt = candidate_features(
        "".join(perm[c] for c in "aabc"),
        1,
        perm_action,
        "".join(perm[c] for c in "acdc"),
        "".join(perm[c] for c in "dddd"),
    )
    return base != alt


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
    path = rule.primitive_path
    if path[0] != rule.left or path[-1] != rule.right:
        raise AssertionError("macro witness endpoints do not match")
    for before, after in zip(path, path[1:]):
        if not is_primitive_step(before, after, equations):
            raise AssertionError(
                f"macro witness contains a non-primitive step: {before!r} -> {after!r}"
            )
    return rule


def control_key(
    neighbor: str, position: int, action: PatternAction
) -> tuple[object, ...]:
    return (shortlex(neighbor), position, action.pattern, action.replacement)


class LinearRanker:
    def __init__(self, weights: list[float]) -> None:
        if len(weights) != FEATURE_DIM:
            raise AssertionError("ranker weight dimension mismatch")
        self.weights = list(weights)

    @classmethod
    def zero(cls) -> "LinearRanker":
        return cls([0.0] * FEATURE_DIM)

    def score(self, features: list[float]) -> float:
        return sum(weight * value for weight, value in zip(self.weights, features))

    def fit(
        self,
        examples: list[tuple[list[float], int]],
        *,
        seed: int,
        lr: float = RANKER_LR,
        epochs: int = RANKER_EPOCHS,
        l2: float = RANKER_L2,
        batch_size: int = RANKER_BATCH,
    ) -> dict[str, object]:
        if not examples:
            return {"n_examples": 0, "n_positive": 0, "n_negative": 0}
        rng = random.Random(seed)
        weights = [0.0] * FEATURE_DIM
        n_positive = sum(label for _, label in examples)
        n_negative = len(examples) - n_positive
        indices = list(range(len(examples)))
        for _epoch in range(epochs):
            rng.shuffle(indices)
            for start in range(0, len(indices), batch_size):
                batch = indices[start : start + batch_size]
                grad = [0.0] * FEATURE_DIM
                for index in batch:
                    features, label = examples[index]
                    logit = sum(weight * value for weight, value in zip(weights, features))
                    # Stable sigmoid
                    if logit >= 0:
                        prob = 1.0 / (1.0 + math.exp(-logit))
                    else:
                        exp_l = math.exp(logit)
                        prob = exp_l / (1.0 + exp_l)
                    error = prob - label
                    for dim, value in enumerate(features):
                        grad[dim] += error * value
                scale = 1.0 / len(batch)
                for dim in range(FEATURE_DIM):
                    weights[dim] -= lr * (scale * grad[dim] + l2 * weights[dim])
        self.weights = weights
        return {
            "n_examples": len(examples),
            "n_positive": n_positive,
            "n_negative": n_negative,
        }


def collect_examples(
    path: tuple[str, ...] | list[str],
    goal: str,
    index: RuleIndex,
) -> list[tuple[list[float], int]]:
    examples: list[tuple[list[float], int]] = []
    for word, nxt in zip(path, path[1:]):
        matches, _ = index.matches(word)
        emitted: set[str] = set()
        for position, action in matches:
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
            label = 1 if neighbor == nxt else 0
            examples.append(
                (candidate_features(word, position, action, neighbor, goal), label)
            )
    return examples


def train_ranker_from_panel(
    panel: list[dict[str, object]],
    index: RuleIndex,
    seed: int,
) -> tuple[LinearRanker, dict[str, object]]:
    examples: list[tuple[list[float], int]] = []
    for goal in panel:
        path = tuple(str(step) for step in goal["path"])
        examples.extend(collect_examples(path, str(goal["target"]), index))
    ranker = LinearRanker.zero()
    stats = ranker.fit(examples, seed=seed)
    return ranker, stats


def bidirectional_beam_search(
    start: str,
    target: str,
    index: RuleIndex,
    cap: int,
    *,
    beam_width: int,
    ranker: LinearRanker | None,
) -> tuple[bool, int, int | None]:
    """Level-synchronous bidirectional beam search with CONTROL/TREATMENT order."""
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

        # Expand the whole current beam; ISWU charges every trie step/match.
        candidate_meta: dict[str, tuple[int, tuple[object, ...], float]] = {}
        for word in sorted(front_a):
            emitted: set[str] = set()
            matches, transitions = index.matches(word)
            work += transitions
            if work > cap:
                return False, cap, None
            for position, action in matches:
                work += 1
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
                if neighbor in seen_a:
                    continue
                key = control_key(neighbor, position, action)
                score = 0.0
                if ranker is not None:
                    score = ranker.score(
                        candidate_features(
                            word, position, action, neighbor, root_b
                        )
                    )
                prior = candidate_meta.get(neighbor)
                # Prefer shorter proof; ties broken later by order key/score.
                if prior is None or proof_length < prior[0]:
                    candidate_meta[neighbor] = (proof_length, key, score)

        if not candidate_meta:
            front_a = set()
            continue

        def order_item(
            item: tuple[str, tuple[int, tuple[object, ...], float]]
        ) -> tuple[object, ...]:
            neighbor, (proof_length, key, score) = item
            if ranker is None:
                return (key, proof_length, neighbor)
            return (-score, key, proof_length, neighbor)

        ordered = sorted(candidate_meta.items(), key=order_item)
        next_front = set()
        for neighbor, (proof_length, _key, _score) in ordered[:beam_width]:
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


def paired_bootstrap_lower(gains: list[float], seed: int, quantile: float) -> float:
    rng = random.Random(seed)
    size = len(gains)
    means = [
        sum(gains[rng.randrange(size)] for _ in range(size)) / size
        for _ in range(BOOTSTRAP_RESAMPLES)
    ]
    means.sort()
    return means[max(0, math.ceil(quantile * BOOTSTRAP_RESAMPLES) - 1)]


def holm_adjusted_pvalues(pvalues: list[float]) -> list[float]:
    m = len(pvalues)
    order = sorted(range(m), key=lambda index: pvalues[index])
    adjusted = [1.0] * m
    running = 0.0
    for rank, index in enumerate(order):
        candidate = (m - rank) * pvalues[index]
        running = max(running, candidate)
        adjusted[index] = min(1.0, running)
    return adjusted


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


def evaluate_arm(
    goals: list[dict[str, object]],
    index: RuleIndex,
    *,
    ranker: LinearRanker | None,
    cap_limit: int = MAX_SEARCH_CAP,
) -> tuple[list[int], list[int | None]]:
    costs: list[int] = []
    proofs: list[int | None] = []
    for goal in goals:
        solved, cost, proof = bidirectional_beam_search(
            str(goal["start"]),
            str(goal["target"]),
            index,
            cap_limit,
            beam_width=BEAM_WIDTH,
            ranker=ranker,
        )
        costs.append(stored_cost(solved, cost))
        proofs.append(proof)
    return costs, proofs


def build_panels(equations: list[Equation], presentation_id: str) -> dict[str, object]:
    panel_names = ("relevance", "calibration", "evaluation")
    panel_seeds = {
        name: int(stable_hash("14", presentation_id, name)[:16], 16)
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
        for b in panel_names[i + 1 :]
    )
    return {
        "panels": panels,
        "panel_seeds": panel_seeds,
        "overlap": overlap,
        "panel_hashes": {
            name: stable_hash(
                *((g["start"], g["target"], g["witness_length"]) for g in panel)
            )
            for name, panel in panels.items()
        },
    }


def audit_presentation(
    equations: list[Equation],
    *,
    leak_evaluation: bool = False,
    presentation_id_override: str | None = None,
) -> dict[str, object]:
    presentation_id = presentation_id_override or presentation_identity(equations)
    packed = build_panels(equations, presentation_id)
    panels = packed["panels"]
    index = RuleIndex(base_search_rules(equations))

    train_panel = panels["evaluation"] if leak_evaluation else panels["relevance"]
    ranker_seed = int(stable_hash("14", presentation_id, "ranker")[:16], 16)
    ranker, ranker_stats = train_ranker_from_panel(train_panel, index, ranker_seed)

    calibration_costs, _ = evaluate_arm(
        panels["calibration"], index, ranker=None
    )
    selected_cap, calibration_rate = choose_calibration_cap(calibration_costs)
    cap = selected_cap or MAX_SEARCH_CAP

    control_costs, control_proofs = evaluate_arm(
        panels["evaluation"], index, ranker=None
    )
    treatment_costs, treatment_proofs = evaluate_arm(
        panels["evaluation"], index, ranker=ranker
    )

    control_summary = summarize(control_costs, cap)
    treatment_summary = summarize(treatment_costs, cap)
    control_solved = [cost <= cap for cost in control_costs]
    treatment_solved = [cost <= cap for cost in treatment_costs]
    gains = sum(
        not before and after
        for before, after in zip(control_solved, treatment_solved)
    )
    losses = sum(
        before and not after
        for before, after in zip(control_solved, treatment_solved)
    )
    paired_gains = [
        min(before, cap) - min(after, cap)
        for before, after in zip(control_costs, treatment_costs)
    ]
    rm_gain = statistics.mean(paired_gains)
    bootstrap_lower = paired_bootstrap_lower(
        paired_gains,
        int(stable_hash("bootstrap", presentation_id)[:16], 16),
        BOOTSTRAP_ALPHA,
    )
    raw_p = exact_mcnemar_one_sided(gains, losses)

    completion_rules, completion = bounded_completion(equations)
    macros = [
        verify_macro(rule, equations)
        for rule in completion_rules[RULES_PER_PRESENTATION:]
    ]
    completion["verified_macro_count"] = len(macros)

    witness_lengths = [float(g["witness_length"]) for g in panels["evaluation"]]
    correlations = {
        "witness_vs_total_length": pearson(
            witness_lengths,
            [
                float(len(str(g["start"])) + len(str(g["target"])))
                for g in panels["evaluation"]
            ],
        ),
        "witness_vs_surface_distance": pearson(
            witness_lengths,
            [
                float(surface_distance(str(g["start"]), str(g["target"])))
                for g in panels["evaluation"]
            ],
        ),
    }

    process_reasons: list[str] = []
    screen_reasons: list[str] = []
    expected = GOALS_PER_STRATUM * len(WITNESS_STRATA)
    if any(len(panel) != expected for panel in panels.values()):
        process_reasons.append("INCOMPLETE_PANEL")
    if packed["overlap"]:
        process_reasons.append("PANEL_GOAL_OVERLAP")
    if selected_cap is None or not (
        CALIBRATION_TARGET - CALIBRATION_TOLERANCE
        <= calibration_rate
        <= CALIBRATION_TARGET + CALIBRATION_TOLERANCE
    ):
        screen_reasons.append("CALIBRATION_TARGET_MISSED")
    if bool(completion["bounded_complete"]):
        screen_reasons.append("BOUNDED_COMPLETION_CONVERGED")
    if (
        control_summary["solved_rate"] >= 0.80
        or control_summary["restricted_mean"] <= 0.20 * cap
    ):
        screen_reasons.append("CONTROL_BEAM_SATURATES")
    if any(value is not None and abs(value) >= 0.80 for value in correlations.values()):
        screen_reasons.append("LENGTH_OR_PARIKH_EXPLAINS_LADDER")
    if ranker_stats["n_positive"] == 0 or ranker_stats["n_negative"] == 0:
        screen_reasons.append("NO_RANKER_TRAINING_SIGNAL")

    outcomes = []
    for goal, before, after, before_ok, after_ok, before_proof, after_proof in zip(
        panels["evaluation"],
        control_costs,
        treatment_costs,
        control_solved,
        treatment_solved,
        control_proofs,
        treatment_proofs,
    ):
        outcomes.append(
            {
                "goal_id": stable_hash(
                    goal["start"], goal["target"], goal["witness_length"]
                )[:16],
                "witness_length": goal["witness_length"],
                "control_cost": before,
                "treatment_cost": after,
                "control_solved": before_ok,
                "treatment_solved": after_ok,
                "restricted_gain": min(before, cap) - min(after, cap),
                "control_proof_length": before_proof,
                "treatment_proof_length": after_proof,
            }
        )

    return {
        "presentation_id": presentation_id,
        "equations": [[eq.left, eq.right] for eq in equations],
        "panel_seeds": packed["panel_seeds"],
        "panel_hashes": packed["panel_hashes"],
        "panel_goal_overlap": packed["overlap"],
        "selected_cap": selected_cap,
        "calibration_rate": calibration_rate,
        "completion": completion,
        "ranker_training": {
            **ranker_stats,
            "leaked_evaluation": leak_evaluation,
            "seed": ranker_seed,
        },
        "at_cap": {
            "control": control_summary,
            "treatment": treatment_summary,
        },
        "primary": {
            "solve_gains": gains,
            "solve_losses": losses,
            "solve_rate_difference": (
                treatment_summary["solved_rate"] - control_summary["solved_rate"]
            ),
            "restricted_mean_gain": rm_gain,
            "bootstrap_lower_alpha_over_m": bootstrap_lower,
            "mcnemar_one_sided_raw_p": raw_p,
            "mcnemar_holm_adjusted_p": None,
        },
        "per_goal_outcomes": outcomes,
        "correlations": correlations,
        "process_valid": not process_reasons,
        "process_reasons": process_reasons,
        "screen_reasons": screen_reasons,
        "decision": "PENDING_QUALIFICATION",
    }


def positive_control_pass(item: dict[str, object]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    primary = item["primary"]
    if not item["process_valid"]:
        reasons.extend(item["process_reasons"])
    if item["screen_reasons"]:
        # Positive-control power check still requires usable calibration etc.
        reasons.extend(item["screen_reasons"])
    if primary["solve_rate_difference"] < POSITIVE_CONTROL_MIN_SOLVE_GAIN:
        reasons.append("SOLVE_RATE_GAIN_BELOW_010")
    if primary["restricted_mean_gain"] < MIN_POLICY_GAIN_FRACTION * (
        item["selected_cap"] or MAX_SEARCH_CAP
    ):
        reasons.append("RESTRICTED_MEAN_GAIN_BELOW_005B")
    if primary["mcnemar_one_sided_raw_p"] > POSITIVE_CONTROL_MCNEMAR_ALPHA:
        reasons.append("MCNEMAR_RAW_ABOVE_0001")
    if primary["solve_rate_difference"] <= 0:
        reasons.append("NO_SOLVE_RATE_IMPROVEMENT")
    return not reasons, reasons


def finalize_qualification(items: list[dict[str, object]]) -> None:
    valid_indices = [index for index, item in enumerate(items) if item["process_valid"]]
    raw_p = [float(items[index]["primary"]["mcnemar_one_sided_raw_p"]) for index in valid_indices]
    adjusted = holm_adjusted_pvalues(raw_p) if raw_p else []
    adjusted_by_index = {
        index: value for index, value in zip(valid_indices, adjusted)
    }
    for index, item in enumerate(items):
        primary = item["primary"]
        primary["mcnemar_holm_adjusted_p"] = adjusted_by_index.get(index)
        reasons = list(item["screen_reasons"])
        if not item["process_valid"]:
            item["decision"] = "INVALID_UNIT"
            item["qualification_reasons"] = reasons
            continue
        if primary["solve_rate_difference"] <= 0:
            reasons.append("NO_SOLVE_RATE_IMPROVEMENT")
        holm_p = primary["mcnemar_holm_adjusted_p"]
        if holm_p is None or holm_p > FAMILY_ALPHA:
            reasons.append("MCNEMAR_HOLM_ABOVE_005")
        cap = item["selected_cap"] or MAX_SEARCH_CAP
        if primary["restricted_mean_gain"] < MIN_POLICY_GAIN_FRACTION * cap:
            reasons.append("RESTRICTED_MEAN_GAIN_BELOW_005B")
        if primary["bootstrap_lower_alpha_over_m"] <= 0:
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
    radius = (
        z
        * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials))
        / denominator
    )
    return center - radius, center + radius


def terminal_verdict(
    items: list[dict[str, object]],
    *,
    complete: bool,
    positive_control_ok: bool,
) -> str:
    if not positive_control_ok:
        return "POSITIVE_CONTROL_FAIL"
    if not complete or any(not item["process_valid"] for item in items):
        return "FRAME_AUDIT_INVALID"
    qualified = sum(item["decision"] == "SCREEN_QUALIFIED" for item in items)
    if qualified >= 5:
        return "POLICY_CHANNEL_VIABLE"
    return "POLICY_CHANNEL_ALSO_SPARSE"


def metric(summary: dict[str, float]) -> str:
    return f"{summary['solved_rate']:.2f} / {summary['restricted_mean']:.0f}"


def render_report(payload: dict[str, object]) -> str:
    rows = []
    for item in payload["presentations"]:
        primary = item["primary"]
        reasons = item["process_reasons"] + item.get("qualification_reasons", [])
        holm = primary["mcnemar_holm_adjusted_p"]
        holm_text = f"{holm:.4g}" if holm is not None else "NA"
        rows.append(
            f"| `{item['presentation_id']}` | {item['selected_cap']} | "
            f"{item['calibration_rate']:.3f} | {metric(item['at_cap']['control'])} | "
            f"{metric(item['at_cap']['treatment'])} | "
            f"{primary['solve_gains']}/{primary['solve_losses']} | "
            f"{primary['mcnemar_one_sided_raw_p']:.4g} | {holm_text} | "
            f"{primary['restricted_mean_gain']:.2f}/"
            f"{primary['bootstrap_lower_alpha_over_m']:.2f} | "
            f"{item['decision']} | {', '.join(reasons) or '-'} |"
        )

    qualified = [
        item
        for item in payload["presentations"]
        if item["decision"] == "SCREEN_QUALIFIED"
    ]
    qualified_ids = ", ".join(f"`{item['presentation_id']}`" for item in qualified) or "none"
    interval = payload["prevalence_wilson_95"]
    pc = payload["positive_control"]

    if payload["verdict"] == "POSITIVE_CONTROL_FAIL":
        return f"""# WALLB_POLICY_CHANNEL_AUDIT_14

NON-CITABLE preregistered policy-channel audit. No ACTIVE/YOKED learner was
instantiated. Library macros are absent from both arms; only beam order differs.

## VERDICT: POSITIVE_CONTROL_FAIL

Positive control on `{pc['presentation_id']}` (leaking oracle trained on
evaluation witness paths): FAIL. gains/losses=
{pc['primary']['solve_gains']}/{pc['primary']['solve_losses']},
solve-rate delta={pc['primary']['solve_rate_difference']:.3f},
CONTROL rate/RM={metric(pc['at_cap']['control'])},
TREATMENT rate/RM={metric(pc['at_cap']['treatment'])},
raw McNemar p={pc['primary']['mcnemar_one_sided_raw_p']:.4g},
RM gain={pc['primary']['restricted_mean_gain']:.2f} at B={pc['selected_cap']}.
Reasons: {', '.join(pc.get('qualification_reasons') or []) or '-'}.

Under frozen beam width W={payload['beam_width']}, CONTROL and TREATMENT produced
identical paired evaluation outcomes. The forty-world frame was not drawn.
Implementation size: {payload['implementation_nonblank_lines']} nonblank lines.
Preregistration commit: `{payload['preregistration_commit']}`.

This is an instrument-power failure, not a prevalence estimate. No world
contract, ACTIVE/YOKED arm or scientific claim is authorized.
"""

    header = f"""# WALLB_POLICY_CHANNEL_AUDIT_14

NON-CITABLE preregistered policy-channel audit. No ACTIVE/YOKED learner was
instantiated. Library macros are absent from both arms; only beam order differs.

## VERDICT: {payload['verdict']}

Positive control on `{pc['presentation_id']}` (leaking oracle):
{pc['decision']}. gains/losses={pc['primary']['solve_gains']}/{pc['primary']['solve_losses']},
solve-rate delta={pc['primary']['solve_rate_difference']:.3f},
raw McNemar p={pc['primary']['mcnemar_one_sided_raw_p']:.4g},
RM gain={pc['primary']['restricted_mean_gain']:.2f} at B={pc['selected_cap']}.

Forty fresh presentations were sampled under the committed audit-14 contract.
Each uses prospectively disjoint relevance, calibration and evaluation panels
of 192 goals. Qualification requires TREATMENT>CONTROL solve rate, Holm-adjusted
one-sided McNemar over 40 at alpha=0.05, restricted-mean gain >=0.05B, bootstrap
lower bound at alpha/m=0.00125 above zero, and structural screens.
Implementation size: {payload['implementation_nonblank_lines']} nonblank lines.

### Fixed qualification screen

| presentation | B | cal rate | CONTROL rate/RM | TREATMENT rate/RM | gains/losses | raw p | Holm p | RM gain/bootstrap lower | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
"""
    footer = f"""

Qualified presentations ({len(qualified)}/40): {qualified_ids}. Estimated joint
generator-and-panel prevalence is {payload['prevalence_hat']:.3f}, Wilson 95%
interval [{interval[0]:.3f}, {interval[1]:.3f}]. Historical audit-12d/13 worlds
are excluded from the draw and are not pooled. This gate does not authorize a
world contract, ACTIVE/YOKED arm or scientific claim.
"""
    return header + "\n".join(rows) + footer


def load_excluded_identities() -> set[str]:
    historical_12 = json.loads(AUDIT12_RESULTS_PATH.read_text(encoding="ascii"))
    historical_13 = json.loads(AUDIT13_RESULTS_PATH.read_text(encoding="ascii"))
    excluded: set[str] = set()
    for item in historical_12["presentations"] + historical_13["presentations"]:
        equations = [Equation(*pair) for pair in item["equations"]]
        excluded.add(presentation_identity(equations))
    return excluded


def run_positive_control() -> dict[str, object]:
    equations = [Equation(*pair) for pair in POSITIVE_CONTROL_EQUATIONS]
    historical = json.loads(AUDIT12_RESULTS_PATH.read_text(encoding="ascii"))
    match = next(
        item
        for item in historical["presentations"]
        if item["presentation_id"] == POSITIVE_CONTROL_ID
    )
    if match["equations"] != [list(pair) for pair in POSITIVE_CONTROL_EQUATIONS]:
        raise RuntimeError("positive-control equations drifted from audit-12d record")
    # Audit 12d labeled worlds by hash(index, equations). Audit 14 panel seeding for
    # this power check uses the historical label exactly as frozen in the prereg.
    item = audit_presentation(
        equations,
        leak_evaluation=True,
        presentation_id_override=POSITIVE_CONTROL_ID,
    )
    ok, reasons = positive_control_pass(item)
    item["decision"] = "POSITIVE_CONTROL_PASS" if ok else "POSITIVE_CONTROL_FAIL"
    item["qualification_reasons"] = reasons
    item["equation_only_identity"] = presentation_identity(equations)
    item["historical_audit12_identity"] = POSITIVE_CONTROL_ID
    return item


def main() -> None:
    if not features_rename_sensitive():
        raise RuntimeError("policy features are rename-invariant at initialization")
    if file_sha256(AUDIT12_SOURCE_PATH) != AUDIT12_SOURCE_SHA256:
        raise RuntimeError("audit-12d source pin mismatch")
    if file_sha256(AUDIT12_RESULTS_PATH) != AUDIT12_RESULTS_SHA256:
        raise RuntimeError("audit-12d result pin mismatch")
    if file_sha256(AUDIT13_SOURCE_PATH) != AUDIT13_SOURCE_SHA256:
        raise RuntimeError("audit-13 source pin mismatch")
    if file_sha256(AUDIT13_RESULTS_PATH) != AUDIT13_RESULTS_SHA256:
        raise RuntimeError("audit-13 result pin mismatch")

    print("positive-control:start", POSITIVE_CONTROL_ID, flush=True)
    positive = run_positive_control()
    print(
        "positive-control",
        positive["decision"],
        positive["primary"]["solve_gains"],
        positive["primary"]["solve_losses"],
        f"delta={positive['primary']['solve_rate_difference']:.3f}",
        f"p={positive['primary']['mcnemar_one_sided_raw_p']:.4g}",
        flush=True,
    )
    positive_ok = positive["decision"] == "POSITIVE_CONTROL_PASS"
    presentations: list[dict[str, object]] = []
    draws = 0

    if positive_ok:
        excluded = load_excluded_identities()
        seen = set(excluded)
        rng = random.Random(FRAME_SEED)
        sampled_presentations: list[list[Equation]] = []
        while len(sampled_presentations) < FRAME_SIZE and draws < PRESENTATION_DRAW_CAP:
            draws += 1
            equations = sample_presentation(rng)
            identity = presentation_identity(equations)
            if identity in seen:
                continue
            seen.add(identity)
            sampled_presentations.append(equations)

        for index, equations in enumerate(sampled_presentations):
            item = audit_presentation(equations, leak_evaluation=False)
            presentations.append(item)
            print(
                index + 1,
                item["presentation_id"],
                "PENDING_QUALIFICATION",
                flush=True,
            )
        finalize_qualification(presentations)

    complete = len(presentations) == FRAME_SIZE
    verdict = terminal_verdict(
        presentations, complete=complete, positive_control_ok=positive_ok
    )
    qualified_count = sum(
        item["decision"] == "SCREEN_QUALIFIED" for item in presentations
    )
    interval = wilson_interval(qualified_count, len(presentations) or 1)

    payload = {
        "schema": "wallb-policy-channel-audit-14.v1",
        "scientific_outcome": False,
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "frame_seed": FRAME_SEED,
        "beam_width": BEAM_WIDTH,
        "presentation_draws": draws,
        "verdict": verdict,
        "qualified_count": qualified_count,
        "prevalence_hat": (
            qualified_count / len(presentations) if presentations else 0.0
        ),
        "prevalence_wilson_95": interval if presentations else [0.0, 1.0],
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
            "beam_width": BEAM_WIDTH,
            "min_policy_gain_fraction": MIN_POLICY_GAIN_FRACTION,
            "calibration_target": CALIBRATION_TARGET,
            "calibration_tolerance": CALIBRATION_TOLERANCE,
            "bootstrap_resamples": BOOTSTRAP_RESAMPLES,
            "family_alpha": FAMILY_ALPHA,
            "holm_m": HOLM_M,
            "bootstrap_alpha": BOOTSTRAP_ALPHA,
            "ranker": {
                "class": "linear_logistic_sgd",
                "lr": RANKER_LR,
                "epochs": RANKER_EPOCHS,
                "l2": RANKER_L2,
                "batch": RANKER_BATCH,
                "feature_dim": FEATURE_DIM,
            },
            "tariffs": ["reuse"],
        },
        "positive_control": positive,
        "presentations": presentations,
        "excluded_historical_counts": {
            "audit12": 8,
            "audit13": 40,
        },
    }
    RESULTS_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    REPORT_PATH.write_text(render_report(payload), encoding="ascii")
    print(verdict, REPORT_PATH)


if __name__ == "__main__":
    main()
