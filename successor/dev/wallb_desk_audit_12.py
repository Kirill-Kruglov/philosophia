#!/usr/bin/env python3
"""Non-citable desk audit for the Wall-B semi-Thue cell.
This script may reject a presentation family or calibrate a search cap. It does
not instantiate ACTIVE/YOKED learners and cannot produce a scientific outcome.
"""
from __future__ import annotations
import hashlib
import heapq
import json
import math
import random
import statistics
import time
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
SEARCH_CAPS = (500, 2_000, 5_000, 20_000)
MAX_SEARCH_CAP = max(SEARCH_CAPS)
COMPLETION_RULE_CAP = 64
COMPLETION_SECONDS = 2.0
COMPLETION_WORD_CAP = 18
HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "wallb_desk_audit_12_results.json"
REPORT_PATH = HERE / "WALLB_DESK_AUDIT_12.md"
@dataclass(frozen=True)
class Equation:
    left: str
    right: str
@dataclass(frozen=True)
class OrientedRule:
    left: str
    right: str
    witness_cost: int
def stable_hash(*parts: object) -> str:
    payload = "\x1f".join(str(part) for part in parts).encode("ascii")
    return hashlib.sha256(payload).hexdigest()
def shortlex(word: str) -> tuple[int, str]:
    return (len(word), word)
def orient(left: str, right: str, witness_cost: int) -> OrientedRule | None:
    if left == right:
        return None
    if shortlex(left) < shortlex(right):
        left, right = right, left
    return OrientedRule(left, right, witness_cost)
def applicable_rewrites(word: str, equations: list[Equation]) -> tuple[list[str], int]:
    out: set[str] = set()
    attempts = 0
    for equation in equations:
        for pattern, replacement in (
            (equation.left, equation.right),
            (equation.right, equation.left),
        ):
            for position in range(max(0, len(word) - len(pattern) + 1)):
                attempts += 1
                if word.startswith(pattern, position):
                    candidate = word[:position] + replacement + word[position + len(pattern) :]
                    if len(candidate) <= MAX_WORD_LENGTH and candidate != word:
                        out.add(candidate)
    return sorted(out), attempts
def random_word(rng: random.Random, low: int, high: int) -> str:
    return "".join(rng.choice(ALPHABET) for _ in range(rng.randint(low, high)))
def sample_presentation(rng: random.Random) -> list[Equation]:
    equations: set[tuple[str, str]] = set()
    while len(equations) < RULES_PER_PRESENTATION:
        left = random_word(rng, 2, 4)
        right = random_word(rng, 2, 4)
        if left == right:
            continue
        key = tuple(sorted((left, right)))
        if key in equations:
            continue
        equations.add(key)
    return [Equation(*pair) for pair in sorted(equations)]
def sample_goal(
    rng: random.Random, equations: list[Equation], witness_length: int
) -> tuple[str, str] | None:
    for _ in range(200):
        start = random_word(rng, *START_LENGTH)
        current = start
        previous: str | None = None
        for _step in range(witness_length):
            neighbors, _ = applicable_rewrites(current, equations)
            choices = [word for word in neighbors if word != previous]
            if not choices:
                break
            previous, current = current, rng.choice(choices)
        else:
            if current != start:
                return start, current
    return None
def bidirectional_bfs(
    start: str, target: str, equations: list[Equation], cap: int
) -> tuple[bool, int]:
    if start == target:
        return True, 0
    front_a, front_b = {start}, {target}
    seen_a, seen_b = {start}, {target}
    work = 0
    while front_a and front_b and work < cap:
        if len(front_a) > len(front_b):
            front_a, front_b = front_b, front_a
            seen_a, seen_b = seen_b, seen_a
        next_front: set[str] = set()
        for word in sorted(front_a):
            neighbors, attempts = applicable_rewrites(word, equations)
            work += attempts
            if work > cap:
                return False, cap
            for neighbor in neighbors:
                if neighbor in seen_b:
                    return True, work
                if neighbor not in seen_a:
                    seen_a.add(neighbor)
                    next_front.add(neighbor)
        front_a = next_front
    return False, min(work, cap)
def surface_distance(word: str, target: str) -> int:
    counts_word = Counter(word)
    counts_target = Counter(target)
    parikh = sum(abs(counts_word[c] - counts_target[c]) for c in ALPHABET)
    return abs(len(word) - len(target)) + parikh
def surface_best_first(
    start: str, target: str, equations: list[Equation], cap: int
) -> tuple[bool, int]:
    queue: list[tuple[int, int, str]] = [(surface_distance(start, target), 0, start)]
    seen = {start}
    serial = 1
    work = 0
    while queue and work < cap:
        _, _, word = heapq.heappop(queue)
        if word == target:
            return True, work
        neighbors, attempts = applicable_rewrites(word, equations)
        work += attempts
        if work > cap:
            return False, cap
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                heapq.heappush(
                    queue, (surface_distance(neighbor, target), serial, neighbor)
                )
                serial += 1
    return False, min(work, cap)
def normalize(
    word: str, rules: list[OrientedRule], cap: int = 100_000
) -> tuple[str, int, int, bool]:
    ordered = sorted(rules, key=lambda rule: shortlex(rule.left), reverse=True)
    work = 0
    primitive_witness = 0
    while work < cap:
        changed = False
        for rule in ordered:
            for position in range(max(0, len(word) - len(rule.left) + 1)):
                work += 1
                if work > cap:
                    return word, cap, primitive_witness, False
                if word.startswith(rule.left, position):
                    word = word[:position] + rule.right + word[position + len(rule.left) :]
                    work += rule.witness_cost
                    primitive_witness += rule.witness_cost
                    changed = True
                    break
            if changed:
                break
        if not changed:
            return word, work, primitive_witness, True
    return word, cap, primitive_witness, False
def critical_pairs(first: OrientedRule, second: OrientedRule) -> list[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    a, b = first.left, second.left
    for overlap in range(1, min(len(a), len(b)) + 1):
        if a[-overlap:] == b[:overlap]:
            pairs.add((first.right + b[overlap:], a[:-overlap] + second.right))
    for position in range(max(0, len(a) - len(b) + 1)):
        if a.startswith(b, position):
            pairs.add((first.right, a[:position] + second.right + a[position + len(b) :]))
    return sorted(pairs)
def bounded_completion(equations: list[Equation]) -> tuple[list[OrientedRule], dict[str, object]]:
    rules = [rule for equation in equations if (rule := orient(equation.left, equation.right, 1))]
    started = time.monotonic()
    skipped_long = 0
    timed_out = False
    changed = True
    while changed and len(rules) < COMPLETION_RULE_CAP:
        if time.monotonic() - started > COMPLETION_SECONDS:
            timed_out = True
            break
        changed = False
        for first in list(rules):
            for second in list(rules):
                for left, right in critical_pairs(first, second):
                    if max(len(left), len(right)) > COMPLETION_WORD_CAP:
                        skipped_long += 1
                        continue
                    norm_left, _, witness_left, ok_left = normalize(left, rules)
                    norm_right, _, witness_right, ok_right = normalize(right, rules)
                    if not (ok_left and ok_right) or norm_left == norm_right:
                        continue
                    new_rule = orient(
                        norm_left,
                        norm_right,
                        first.witness_cost + second.witness_cost + witness_left + witness_right,
                    )
                    if new_rule and (new_rule.left, new_rule.right) not in {
                        (rule.left, rule.right) for rule in rules
                    }:
                        rules.append(new_rule)
                        changed = True
                        break
                if changed:
                    break
            if changed:
                break
    bounded_complete = not changed and not timed_out and skipped_long == 0
    return rules, {
        "bounded_complete": bounded_complete,
        "rule_count": len(rules),
        "rule_cap_hit": len(rules) >= COMPLETION_RULE_CAP,
        "skipped_long_pairs": skipped_long,
        "timed_out": timed_out,
        "seconds": time.monotonic() - started,
    }
def completion_solve(
    start: str, target: str, rules: list[OrientedRule], cap: int
) -> tuple[bool, int]:
    left, left_work, _, left_ok = normalize(start, rules, cap)
    remaining = max(0, cap - left_work)
    right, right_work, _, right_ok = normalize(target, rules, remaining)
    work = min(cap, left_work + right_work)
    return left_ok and right_ok and left == right, work
def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or statistics.pstdev(xs) == 0 or statistics.pstdev(ys) == 0:
        return None
    mean_x, mean_y = statistics.mean(xs), statistics.mean(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - mean_x) ** 2 for x in xs) * sum((y - mean_y) ** 2 for y in ys)
    )
    return numerator / denominator
def summarize_costs(costs: list[int], cap: int) -> dict[str, float]:
    truncated = [min(cost, cap) for cost in costs]
    return {
        "solved_rate": sum(cost <= cap for cost in costs) / len(costs),
        "restricted_mean": statistics.mean(truncated),
    }
def audit_presentation(index: int, rng: random.Random) -> dict[str, object]:
    equations = sample_presentation(rng)
    goals: list[dict[str, object]] = []
    for witness_length in WITNESS_STRATA:
        while sum(goal["witness_length"] == witness_length for goal in goals) < GOALS_PER_STRATUM:
            sampled = sample_goal(rng, equations, witness_length)
            if sampled is None:
                break
            start, target = sampled
            goals.append({"start": start, "target": target, "witness_length": witness_length})
    completion_rules, completion = bounded_completion(equations)
    bfs_costs: list[int] = []
    surface_costs: list[int] = []
    completion_costs: list[int] = []
    for goal in goals:
        start, target = str(goal["start"]), str(goal["target"])
        solved, cost = bidirectional_bfs(start, target, equations, MAX_SEARCH_CAP)
        bfs_costs.append(cost if solved else MAX_SEARCH_CAP + 1)
        solved, cost = surface_best_first(start, target, equations, MAX_SEARCH_CAP)
        surface_costs.append(cost if solved else MAX_SEARCH_CAP + 1)
        solved, cost = completion_solve(start, target, completion_rules, MAX_SEARCH_CAP)
        completion_costs.append(cost if solved else MAX_SEARCH_CAP + 1)
    selected_cap = None
    for cap in SEARCH_CAPS:
        rate = summarize_costs(bfs_costs, cap)["solved_rate"]
        if 0.20 <= rate <= 0.60:
            selected_cap = cap
            break
    cap = selected_cap or MAX_SEARCH_CAP
    bfs_summary = summarize_costs(bfs_costs, cap)
    surface_summary = summarize_costs(surface_costs, cap)
    completion_summary = summarize_costs(completion_costs, cap)
    by_stratum = {}
    for witness_length in WITNESS_STRATA:
        positions = [i for i, goal in enumerate(goals) if goal["witness_length"] == witness_length]
        by_stratum[str(witness_length)] = {
            "bfs": summarize_costs([bfs_costs[i] for i in positions], cap),
            "surface": summarize_costs([surface_costs[i] for i in positions], cap),
            "completion": summarize_costs([completion_costs[i] for i in positions], cap),
        }
    witness_lengths = [float(goal["witness_length"]) for goal in goals]
    total_lengths = [float(len(str(goal["start"])) + len(str(goal["target"]))) for goal in goals]
    parikh_distances = [
        float(surface_distance(str(goal["start"]), str(goal["target"]))) for goal in goals
    ]
    correlations = {
        "witness_vs_total_length": pearson(witness_lengths, total_lengths),
        "witness_vs_surface_distance": pearson(witness_lengths, parikh_distances),
    }
    reasons: list[str] = []
    if selected_cap is None:
        reasons.append("NO_20_60_BFS_CAP")
    if bool(completion["bounded_complete"]):
        reasons.append("BOUNDED_COMPLETION_CONVERGED")
    if completion_summary["solved_rate"] >= 0.80 or completion_summary["restricted_mean"] <= 0.20 * cap:
        reasons.append("FREE_COMPLETION_LIBRARY_SATURATES")
    if surface_summary["solved_rate"] >= 0.80 or surface_summary["restricted_mean"] <= 0.20 * cap:
        reasons.append("SURFACE_SHORTCUT_SATURATES")
    if any(value is not None and abs(value) >= 0.80 for value in correlations.values()):
        reasons.append("LENGTH_OR_PARIKH_EXPLAINS_LADDER")
    return {
        "presentation_id": stable_hash(index, equations)[:12],
        "equations": [[equation.left, equation.right] for equation in equations],
        "goal_count": len(goals),
        "selected_cap": selected_cap,
        "completion": completion,
        "at_cap": {
            "bfs": bfs_summary,
            "surface": surface_summary,
            "completion": completion_summary,
        },
        "by_witness_stratum": by_stratum,
        "correlations": correlations,
        "decision": "DESK_CANDIDATE" if not reasons else "REJECT",
        "reasons": reasons,
    }
def render_report(payload: dict[str, object]) -> str:
    rows = []
    for item in payload["presentations"]:
        cap = item["selected_cap"] or "none"
        metrics = item["at_cap"]
        completion = item["completion"]
        rows.append(
            f"| `{item['presentation_id']}` | {cap} | "
            f"{metrics['bfs']['solved_rate']:.2f} / {metrics['bfs']['restricted_mean']:.0f} | "
            f"{metrics['surface']['solved_rate']:.2f} / {metrics['surface']['restricted_mean']:.0f} | "
            f"{metrics['completion']['solved_rate']:.2f} / {metrics['completion']['restricted_mean']:.0f} | "
            f"{completion['rule_count']} / {completion['bounded_complete']} | "
            f"{item['decision']} | {', '.join(item['reasons']) or '-'} |"
        )
    candidates = [item for item in payload["presentations"] if item["decision"] == "DESK_CANDIDATE"]
    verdict = "WITHDRAWN_UNFAIR_COMPARATORS"
    recommended = max(candidates, key=lambda x: (x["at_cap"]["bfs"]["solved_rate"] - max(x["at_cap"]["surface"]["solved_rate"], x["at_cap"]["completion"]["solved_rate"]), -abs(x["at_cap"]["bfs"]["solved_rate"] - 0.40))) if candidates else None
    recommended_rules = "; ".join(f"{a}<->{b}" for a, b in recommended["equations"]) if recommended else "none"
    return "\n".join(
        [
            "# WALLB_DESK_AUDIT_12",
            "",
            "NON-CITABLE desk audit. No ACTIVE/YOKED learner was instantiated.",
            "",
            f"## VERDICT: {verdict}",
            "",
            "This audit is retained as a failed design artifact and carries no gate credit.",
            "Its surface arm was one-directional against bidirectional BFS; its completion",
            "arm normalized without search under a non-confluent partial system. See 12b.",
            "",
            "Metrics are `solved-rate / restricted-mean-PREW` at the calibrated BFS cap.",
            "Completion is screened with its partial library supplied for free. Failure to saturate",
            "under this favorable upper bound implies that cost-matched completion cannot saturate.",
            "",
            "| presentation | B | BFS | length+Parikh | bounded completion | rules / bounded-complete | decision | reasons |",
            "|---|---:|---:|---:|---:|---:|---|---|",
            *rows,
            "",
            f"Desk candidates: {len(candidates)} / {len(payload['presentations'])}.",
            f"Recommended desk candidate: `{recommended['presentation_id'] if recommended else 'none'}`; rules: `{recommended_rules}`.",
            f"Recommended BFS solve rates at witness lengths 6/10/14: `{recommended['by_witness_stratum']['6']['bfs']['solved_rate']:.3f} / {recommended['by_witness_stratum']['10']['bfs']['solved_rate']:.3f} / {recommended['by_witness_stratum']['14']['bfs']['solved_rate']:.3f}`." if recommended else "No stratum profile: no candidate.",
            "Post-dev selection rule: maximize BFS advantage over the stronger surface/completion shortcut, then proximity to 0.40 BFS solve rate.",
            "Residual limits: bounded completion is not a proof that no finite completion exists; 24 goals per presentation are a calibration sample.",
            "",
            "A desk candidate only permits a concrete world contract. It is not evidence for ACTIVE,",
            "YOKED, manufactured experience, transfer, or the essay's scientific claim.",
        ]
    ) + "\n"
def main() -> None:
    rng = random.Random(SEED)
    presentations = [audit_presentation(index, rng) for index in range(PRESENTATIONS)]
    payload = {
        "schema": "wallb-desk-audit-12.v1",
        "scientific_outcome": False,
        "seed": SEED,
        "constants": {
            "alphabet": ALPHABET,
            "presentations": PRESENTATIONS,
            "rules_per_presentation": RULES_PER_PRESENTATION,
            "goals_per_stratum": GOALS_PER_STRATUM,
            "witness_strata": WITNESS_STRATA,
            "max_word_length": MAX_WORD_LENGTH,
            "search_caps": SEARCH_CAPS,
            "completion_rule_cap": COMPLETION_RULE_CAP,
            "completion_seconds": COMPLETION_SECONDS,
        },
        "presentations": presentations,
    }
    RESULTS_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")
    REPORT_PATH.write_text(render_report(payload), encoding="ascii")
    print(REPORT_PATH)
if __name__ == "__main__":
    main()
