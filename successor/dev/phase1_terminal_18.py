#!/usr/bin/env python3
"""Phase-1 terminal aggregator (exploratory close-out). ASCII, deterministic, fail closed.

Does not authorize Phase 2 and does not make a scientific Philosophia claim.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
MINIMO = Path("/home/master/llm_projects/minimo")
MINIMO_LEARNING = MINIMO / "learning"
RUN_DIR = MINIMO_LEARNING / "outputs" / "2026-08-10" / "00-14-33"
PHASE17_DIR = HERE / "phase1_extrinsic_17"
FULL_LOG = Path("/home/master/minimo_prop_full.log")
PINNED_COMMIT = "6066f482c6752915ad21119f93dc162f4cb9db72"
MINIMO_VENV_PYTHON = MINIMO / ".venv" / "bin" / "python"

N_CHECKPOINTS = 5
N_PROBLEMS = 30
MCTS_BUDGET = 8000
REQUIRED_CONFIG = {
    "accumulate_library": False,
    "begin": 0,
    "end": 30,
    "mcts_budget": 8000,
    "n_problems": 30,
    "problemset": "kleene",
    "seed": 0,
}

RESULTS_PATH = HERE / "PHASE1_TERMINAL_18_results.json"
REPORT_PATH = HERE / "PHASE1_TERMINAL_18.md"
PROVENANCE_PATH = HERE / "PHASE1_PROVENANCE_18.json"
ACTION_ORDER_PATH = HERE / "PHASE1_ACTION_ORDER_PROBE_18_results.json"

VERDICT = "EXPLORATORY_FEASIBILITY_OBSERVED__NO_PHILOSOPHIA_CLAIM"

REQUIRED_TABLE = {
    0: {
        "n_solved": 11,
        "restricted_mean": 5257.833333,
        "saving_vs_ck0": 0.0,
        "positive": 0,
        "negative": 0,
        "tie": 30,
    },
    1: {
        "n_solved": 20,
        "restricted_mean": 4374.966667,
        "saving_vs_ck0": 882.866667,
        "positive": 19,
        "negative": 1,
        "tie": 10,
    },
    2: {
        "n_solved": 11,
        "restricted_mean": 5168.0,
        "saving_vs_ck0": 89.833333,
        "positive": 8,
        "negative": 3,
        "tie": 19,
    },
    3: {
        "n_solved": 11,
        "restricted_mean": 5254.233333,
        "saving_vs_ck0": 3.6,
        "positive": 8,
        "negative": 3,
        "tie": 19,
    },
    4: {
        "n_solved": 13,
        "restricted_mean": 4916.133333,
        "saving_vs_ck0": 341.7,
        "positive": 9,
        "negative": 5,
        "tie": 16,
    },
}


class FailClosed(RuntimeError):
    pass


def round6(value: float) -> float:
    return float("%.6f" % value)


def sha256_file(path: Path) -> dict:
    if not path.is_file():
        raise FailClosed("missing required file: %s" % path)
    data = path.read_bytes()
    return {
        "bytes": len(data),
        "path": str(path),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def load_phase17(index: int) -> tuple[dict, Path]:
    path = PHASE17_DIR / ("checkpoint_%d.json" % index)
    raw = path.read_text(encoding="ascii")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise FailClosed("malformed JSON %s: %s" % (path, exc)) from exc
    if not isinstance(payload, dict):
        raise FailClosed("%s is not a JSON object" % path)
    return payload, path


def require_bool(payload: dict, key: str, expected: bool, path: Path) -> None:
    if key not in payload:
        raise FailClosed("%s missing %s" % (path, key))
    value = payload[key]
    if not isinstance(value, bool) or value is not expected:
        raise FailClosed("%s %s=%r, expected %r" % (path, key, value, expected))


def require_int(payload: dict, key: str, expected: int, path: Path) -> None:
    if key not in payload:
        raise FailClosed("%s missing %s" % (path, key))
    value = payload[key]
    if not isinstance(value, int) or isinstance(value, bool) or value != expected:
        raise FailClosed("%s %s=%r, expected %r" % (path, key, value, expected))


def require_str(payload: dict, key: str, expected: str, path: Path) -> None:
    if key not in payload:
        raise FailClosed("%s missing %s" % (path, key))
    value = payload[key]
    if value != expected:
        raise FailClosed("%s %s=%r, expected %r" % (path, key, value, expected))


def validate_header(payload: dict, path: Path) -> None:
    require_bool(payload, "accumulate_library", False, path)
    require_int(payload, "begin", 0, path)
    require_int(payload, "end", 30, path)
    require_int(payload, "mcts_budget", MCTS_BUDGET, path)
    require_int(payload, "n_problems", N_PROBLEMS, path)
    require_str(payload, "problemset", "kleene", path)
    require_int(payload, "seed", 0, path)
    if "records" not in payload or not isinstance(payload["records"], list):
        raise FailClosed("%s missing records list" % path)
    if len(payload["records"]) != N_PROBLEMS:
        raise FailClosed(
            "%s records length %d, expected %d"
            % (path, len(payload["records"]), N_PROBLEMS)
        )


def reconstruct_entered_mcts_iterations(raw, problem: str, path: Path) -> int:
    if isinstance(raw, bool) or not isinstance(raw, int):
        raise FailClosed(
            "%s problem %s mcts_expansions malformed: %r" % (path, problem, raw)
        )
    if raw < 0 or raw >= MCTS_BUDGET:
        raise FailClosed(
            "%s problem %s mcts_expansions out of range: %r" % (path, problem, raw)
        )
    return raw + 1


def parse_records(
    payload: dict, path: Path
) -> tuple[list[str], list[int], list[int], list[str]]:
    theorem_ids = []
    expansions = []
    legacy_raw = []
    solved = []
    seen = set()
    for rec in payload["records"]:
        if not isinstance(rec, dict):
            raise FailClosed("%s has a non-object record" % path)
        if (
            "problem" not in rec
            or "success" not in rec
            or "mcts_expansions" not in rec
            or "agent_iterations" not in rec
        ):
            raise FailClosed("%s record missing required keys: %r" % (path, rec))
        problem = rec["problem"]
        if not isinstance(problem, str) or not problem:
            raise FailClosed("%s malformed problem id: %r" % (path, problem))
        if problem in seen:
            raise FailClosed("%s duplicate theorem id %s" % (path, problem))
        seen.add(problem)
        success = rec["success"]
        if not isinstance(success, bool):
            raise FailClosed("%s problem %s success malformed: %r" % (path, problem, success))
        agent_iterations = rec["agent_iterations"]
        expected_iterations = 0 if success else 1
        if (
            isinstance(agent_iterations, bool)
            or not isinstance(agent_iterations, int)
            or agent_iterations != expected_iterations
        ):
            raise FailClosed(
                "%s problem %s agent_iterations=%r, expected %d"
                % (path, problem, agent_iterations, expected_iterations)
            )
        raw = rec["mcts_expansions"]
        exact = reconstruct_entered_mcts_iterations(raw, problem, path)
        if not success and exact != MCTS_BUDGET:
            raise FailClosed(
                "%s censored problem %s exact work %d != budget %d"
                % (path, problem, exact, MCTS_BUDGET)
            )
        theorem_ids.append(problem)
        legacy_raw.append(raw)
        expansions.append(exact)
        if success:
            solved.append(problem)
    if len(theorem_ids) != N_PROBLEMS:
        raise FailClosed("%s unique theorem count %d" % (path, len(theorem_ids)))
    return theorem_ids, legacy_raw, expansions, solved


def load_action_order_probe() -> dict:
    try:
        payload = json.loads(ACTION_ORDER_PATH.read_text(encoding="ascii"))
    except (OSError, json.JSONDecodeError) as exc:
        raise FailClosed("invalid action-order probe artifact: %s" % exc) from exc
    if payload.get("schema") != "phase1-action-order-probe-18.v1":
        raise FailClosed("unexpected action-order probe schema")
    if payload.get("worker_count", 0) < 8:
        raise FailClosed("action-order probe used fewer than eight workers")
    distinct = payload.get("distinct_order_count")
    if isinstance(distinct, bool) or not isinstance(distinct, int) or distinct < 1:
        raise FailClosed("invalid distinct_order_count")
    expected_status = (
        "ORDER_VARIATION_OBSERVED"
        if distinct > 1
        else "NO_VARIATION_OBSERVED_IN_BOUNDED_PROBE"
    )
    if payload.get("status") != expected_status:
        raise FailClosed("action-order status/count mismatch")
    workers = payload.get("workers")
    expected_set = payload.get("sorted_action_set")
    if not isinstance(workers, list) or len(workers) != payload["worker_count"]:
        raise FailClosed("malformed action-order workers")
    if not isinstance(expected_set, list) or len(expected_set) != len(set(expected_set)):
        raise FailClosed("malformed action-order set")
    for row in workers:
        actions = row.get("ordered_actions") if isinstance(row, dict) else None
        if not isinstance(actions, list) or sorted(actions) != expected_set:
            raise FailClosed("action-order worker set mismatch")
    return payload


def cross_check_solved(payload: dict, solved: list[str], path: Path) -> None:
    if "n_solved" not in payload or not isinstance(payload["n_solved"], int):
        raise FailClosed("%s missing integer n_solved" % path)
    if payload["n_solved"] != len(solved):
        raise FailClosed(
            "%s n_solved=%r but recomputed %d"
            % (path, payload["n_solved"], len(solved))
        )
    if "solved" not in payload or not isinstance(payload["solved"], list):
        raise FailClosed("%s missing solved list" % path)
    declared = payload["solved"]
    if declared != solved:
        raise FailClosed(
            "%s solved list mismatch: declared %r recomputed %r"
            % (path, declared, solved)
        )


def paired_counts(base: list[int], other: list[int]) -> tuple[int, int, int]:
    positive = negative = tie = 0
    for left, right in zip(base, other):
        if right < left:
            positive += 1
        elif right > left:
            negative += 1
        else:
            tie += 1
    return positive, negative, tie


def compare_required(index: int, row: dict) -> None:
    expected = REQUIRED_TABLE[index]
    checks = [
        ("n_solved", row["n_solved"], expected["n_solved"]),
        (
            "restricted_mean",
            round6(row["restricted_mean_exact_entered_mcts_iterations"]),
            round6(expected["restricted_mean"]),
        ),
        (
            "saving_vs_ck0",
            round6(row["mean_saving_vs_ck0"]),
            round6(expected["saving_vs_ck0"]),
        ),
        ("positive", row["paired_positive_vs_ck0"], expected["positive"]),
        ("negative", row["paired_negative_vs_ck0"], expected["negative"]),
        ("tie", row["paired_tie_vs_ck0"], expected["tie"]),
    ]
    for name, got, want in checks:
        if got != want:
            raise FailClosed(
                "ck%d %s computed %r != required %r" % (index, name, got, want)
            )


def dump_canonical(payload: dict) -> bytes:
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True)
    return (text + "\n").encode("ascii")


def git_output(repo: Path, args: list[str]) -> str:
    return subprocess.check_output(["git"] + args, cwd=str(repo), text=True)


def inspect_minimo_checkpoints() -> list[dict]:
    script = r"""
import json, os, sys
os.chdir(%r)
sys.path.insert(0, ".")
import torch
import proofsearch
run = %r
out = []
for i in range(5):
    path = os.path.join(run, "%%d.pt" %% i)
    agent = torch.load(path, map_location="cpu", weights_only=False)
    inner = agent._policy._lm
    gpt = inner._lm
    cfg = gpt.config
    inner_opt = inner._optimizer
    outer_opt = getattr(agent._policy, "_optimizer", None)
    out.append({
        "checkpoint": i,
        "device": str(next(gpt.parameters()).device),
        "embedding": int(cfg.n_embd),
        "heads": int(cfg.n_head),
        "inner_optimizer_state_entries": len(inner_opt.state),
        "layers": int(cfg.n_layer),
        "max_searches": int(agent._max_searches),
        "model_parameters": int(sum(p.numel() for p in gpt.parameters())),
        "outer_optimizer_state_entries": (len(outer_opt.state) if outer_opt is not None else None),
        "positions": int(cfg.n_positions),
        "training_iteration_field": int(agent._training_its),
    })
print(json.dumps(out, sort_keys=True))
""" % (str(MINIMO_LEARNING), str(RUN_DIR))
    raw = subprocess.check_output(
        [str(MINIMO_VENV_PYTHON), "-c", script],
        text=True,
    )
    rows = json.loads(raw)
    if len(rows) != N_CHECKPOINTS:
        raise FailClosed("checkpoint inspect returned %d rows" % len(rows))
    for row in rows:
        if (
            row["layers"] != 2
            or row["heads"] != 2
            or row["embedding"] != 128
            or row["positions"] != 512
            or row["max_searches"] != 1
            or row["model_parameters"] != 478720
        ):
            raise FailClosed("architecture mismatch at ck%d: %r" % (row["checkpoint"], row))
        if row["checkpoint"] == 0:
            if row["inner_optimizer_state_entries"] != 0:
                raise FailClosed("ck0 optimizer-state entries != 0")
        else:
            if row["inner_optimizer_state_entries"] != 28:
                raise FailClosed(
                    "ck%d optimizer-state entries != 28" % row["checkpoint"]
                )
    return rows


def aggregate() -> dict:
    payloads = []
    input_hashes = []
    theorem_ids = None
    rows = []
    expansions_by_ck = []
    legacy_raw_by_ck = []
    solved_by_ck = []

    for index in range(N_CHECKPOINTS):
        payload, path = load_phase17(index)
        validate_header(payload, path)
        ids, legacy_raw, expansions, solved = parse_records(payload, path)
        cross_check_solved(payload, solved, path)
        if theorem_ids is None:
            theorem_ids = ids
        elif ids != theorem_ids:
            raise FailClosed(
                "%s theorem id order differs from checkpoint_0.json" % path
            )
        payloads.append(payload)
        input_hashes.append(sha256_file(path))
        expansions_by_ck.append(expansions)
        legacy_raw_by_ck.append(legacy_raw)
        solved_by_ck.append(solved)

    if len(set(theorem_ids)) != N_PROBLEMS:
        raise FailClosed("theorem ids are not 30 unique values")

    base = expansions_by_ck[0]
    base_mean = sum(base) / float(N_PROBLEMS)

    for index in range(N_CHECKPOINTS):
        expansions = expansions_by_ck[index]
        solved = solved_by_ck[index]
        mean = sum(expansions) / float(N_PROBLEMS)
        saving = base_mean - mean
        positive, negative, tie = paired_counts(base, expansions)
        row = {
            "checkpoint": index,
            "mean_saving_vs_ck0": round6(saving),
            "n_solved": len(solved),
            "n_total": N_PROBLEMS,
            "exact_entered_mcts_iterations": expansions,
            "legacy_raw_zero_based_index": legacy_raw_by_ck[index],
            "paired_negative_vs_ck0": negative,
            "paired_positive_vs_ck0": positive,
            "paired_tie_vs_ck0": tie,
            "restricted_mean_exact_entered_mcts_iterations": round6(mean),
            "solved": solved,
        }
        compare_required(index, row)
        rows.append(row)

    result = {
        "bootstrap_interval": None,
        "citable": False,
        "input_hashes": input_hashes,
        "n_checkpoints": N_CHECKPOINTS,
        "n_problems": N_PROBLEMS,
        "p_value": None,
        "phase": 1,
        "phase17_dir": str(PHASE17_DIR),
        "population_inference": False,
        "problem_ids": theorem_ids,
        "problemset": "kleene",
        "realization": "repository-default CPU-debug MINIMO realization",
        "rows": rows,
        "run_dir": str(RUN_DIR),
        "legacy_counter_reconstruction": (
            "Every record made one MCTS invocation under max_searches=1; the old "
            "field stored zero-based loop index i, so exact entered MCTS iterations=raw+1. "
            "This is not asserted to equal the number of newly expanded leaves."
        ),
        "schema": "phase1-terminal-18.v2",
        "scientific_claim": False,
        "scientific_outcome": False,
        "supersedes_phase17_claim": (
            "Supersedes the Phase-17 sentence 'the phenomenon is real' and its "
            "bootstrap-CI interpretation. Historical file PHASE1_EXTRINSIC_17.md "
            "is retained unchanged."
        ),
        "theorem_population_inference": False,
        "verdict": VERDICT,
    }
    return result


def write_markdown(result: dict) -> str:
    lines = [
        "# PHASE1_TERMINAL_18",
        "",
        "NON-CITABLE Phase-1 close-out. Not an experiment. No scientific claim.",
        "",
        "## VERDICT: `%s`" % VERDICT,
        "",
        "This package closes exploratory MINIMO Phase 1 with an exact counter",
        "repair, deterministic aggregation, and honest provenance. It does not",
        "authorize Phase 2 and does not make a scientific Philosophia claim.",
        "",
        "Authoritative evaluation inputs are the five Phase-17 JSON files under",
        "`successor/dev/phase1_extrinsic_17/`. The training run is",
        "`minimo/learning/outputs/2026-08-10/00-14-33`, a repository-default",
        "CPU-debug MINIMO realization. Lenovo Legion runs `2026-08-09/23-57-05`",
        "and `2026-08-10/07-27-05` are excluded as",
        "`STOPPED_PERFORMANCE_FEASIBILITY` and are not Phase-16/17 evidence.",
        "",
        "Every Phase-17 record made one MCTS invocation under `max_searches=1`.",
        "The legacy field stored zero-based loop index `i`; exact entered MCTS work is",
        "therefore reconstructed as `raw+1` for every item, including `7999 -> 8000`.",
        "This counts entered search-loop iterations, not necessarily newly expanded leaves.",
        "This changes absolute means and two mean savings slightly, but not the",
        "direction, solved counts or paired sign counts. No bootstrap interval,",
        "p-value, or theorem-population inference is emitted.",
        "",
        "This report supersedes the broad Phase-17 sentence \"the phenomenon is",
        "real\" and its bootstrap-CI interpretation. Historical file",
        "`PHASE1_EXTRINSIC_17.md` is not rewritten or deleted.",
        "",
        "## Computed table",
        "",
        "| ck | solved | restricted mean | saving vs ck0 | positive/negative/tie |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in result["rows"]:
        ck = row["checkpoint"]
        lines.append(
            "| %d | %d/%d | %.6f | %.6f | %d/%d/%d |"
            % (
                ck,
                row["n_solved"],
                row["n_total"],
                row["restricted_mean_exact_entered_mcts_iterations"],
                row["mean_saving_vs_ck0"],
                row["paired_positive_vs_ck0"],
                row["paired_negative_vs_ck0"],
                row["paired_tie_vs_ck0"],
            )
        )
    lines.extend(
        [
            "",
            "## Terminal reading",
            "",
            "> In one unseeded repository-default CPU-debug MINIMO realization, the post-hoc",
            "> checkpoint after one self-training iteration reduced capped proof-search work",
            "> on the fixed 30-item Kleene panel relative to checkpoint zero. This is a",
            "> property of saved artifacts, not an estimate of a theorem population,",
            "> training-seed stability, monotone self-improvement, ACTIVE versus YOKED, or a",
            "> general Philosophia effect.",
            "",
            "## Input hashes",
            "",
        ]
    )
    for item in result["input_hashes"]:
        lines.append(
            "- `%s`: sha256 `%s` (%d bytes)"
            % (item["path"], item["sha256"], item["bytes"])
        )
    lines.append("")
    probe = result["action_order_probe"]
    lines.extend(
        [
            "## Bounded action-order probe",
            "",
            "Status: `%s`; distinct ordered-sequence hashes: `%d` across `%d` fresh workers."
            % (
                probe["status"],
                probe["distinct_order_count"],
                probe["worker_count"],
            ),
            "",
        ]
    )
    if probe["status"] == "ORDER_VARIATION_OBSERVED":
        lines.extend(
            [
                "Phase-17 evaluation is not demonstrated fresh-process invariant.",
                "Peano enumeration order is a demonstrated candidate mechanism, not",
                "an established sole cause. Phase 2 must canonicalize unique action",
                "identities before constructing children.",
                "",
            ]
        )
    return "\n".join(lines)


def collect_hashes() -> dict:
    files = {
        "config_yaml": RUN_DIR / ".hydra" / "config.yaml",
        "log_jsonl": RUN_DIR / "log.jsonl",
        "overrides_yaml": RUN_DIR / ".hydra" / "overrides.yaml",
    }
    out = {}
    for key, path in files.items():
        out[key] = sha256_file(path)
    if FULL_LOG.is_file():
        out["full_run_log"] = sha256_file(FULL_LOG)
    else:
        out["full_run_log"] = None
    checkpoints = []
    outcomes = []
    phase17 = []
    for index in range(N_CHECKPOINTS):
        checkpoints.append(sha256_file(RUN_DIR / ("%d.pt" % index)))
        outcomes.append(sha256_file(RUN_DIR / ("outcomes_%d.json" % index)))
        phase17.append(sha256_file(PHASE17_DIR / ("checkpoint_%d.json" % index)))
    out["checkpoints_pt"] = checkpoints
    out["outcomes_json"] = outcomes
    out["phase17_json"] = phase17
    return out


def build_provenance(result: dict, action_order: dict) -> dict:
    commit = git_output(MINIMO, ["rev-parse", "HEAD"]).strip()
    if commit != PINNED_COMMIT:
        raise FailClosed("MINIMO HEAD %s != pinned %s" % (commit, PINNED_COMMIT))
    status_short = git_output(MINIMO, ["status", "--short"])
    architecture = inspect_minimo_checkpoints()
    hashes = collect_hashes()
    start_evidence = [
        "hydra output_dir %s" % RUN_DIR,
        "config.yaml mtime 2026-08-10T00:14:33.452666286+03:00",
        "0.pt mtime 2026-08-10T00:14:34.302903289+03:00",
        "minimo_prop_full.log first timestamp [2026-08-10T00:14:34.303900] Iteration #0",
    ]
    end_evidence = [
        "outcomes_4.json mtime 2026-08-10T18:49:59.327684942+03:00",
        "log.jsonl mtime 2026-08-10T18:49:59.627687111+03:00 last record iteration 4 training",
        "minimo_prop_full.log mtime 2026-08-10T18:49:59.695687602+03:00",
    ]
    return {
        "architecture": {
            "checkpoints": architecture,
            "source_rule": {
                "cpu_branch": (
                    "comment-labelled debug code fixed at 2 layers / 2 heads / embedding 128, "
                    "n_positions=512"
                ),
                "cuda_branch": (
                    "defaults to 8 layers / 8 heads / embedding 512, n_positions=1024"
                ),
                "file": "minimo/learning/policy.py",
                "transformer_lm_policy_init": "TransformerLMPolicy.__init__",
            },
            "verified_anchor": {
                "checkpoints": "0..4",
                "embedding": 128,
                "heads": 2,
                "layers": 2,
                "model_parameters": 478720,
                "optimizer_state_entries": {
                    "ck0": 0,
                    "ck1_to_ck4": 28,
                },
                "positions": 512,
            },
        },
        "conjecture_grammar_limitation": {
            "causal_explanation_of_ck1": False,
            "kind": "instrument-scope limitation",
            "statement": (
                "current learning/conjecture.py::Decl.parse delegates a declaration type to "
                "Value.parse_with_target_type_options, while Value does not parse Arrow. "
                "The self-conjecture grammar therefore cannot place an implication/function "
                "type in a hypothesis declaration. Phase 1 must not be described as having "
                "tested a rich compositional implication curriculum."
            ),
            "source_anchor": {
                "decl_parse": "minimo/learning/conjecture.py::Decl.parse",
                "value_parse": "minimo/learning/conjecture.py::Value.parse",
                "value_parse_with_target_type_options": (
                    "minimo/learning/conjecture.py::Value.parse_with_target_type_options"
                ),
                "value_type_union": "Value.value: Union[Atom, App] (no Arrow)",
            },
        },
        "excluded_runs": [
            {
                "classification": "STOPPED_PERFORMANCE_FEASIBILITY",
                "gpu_model": "NVIDIA GeForce RTX 4060 Laptop GPU",
                "gpu_model_source": (
                    "philosophia/successor/dev/PHASE1_MINIMO_REPRO_15.md"
                ),
                "inference_forbidden": [
                    "do not infer that the GPU was intrinsically slower",
                    "do not infer that 8 GB VRAM was the sole cause",
                ],
                "machine_name": "Lenovo Legion",
                "not_equal_architecture_hardware_benchmark": True,
                "not_phase16_17_checkpoint_source": True,
                "reason": (
                    "ended because the observed end-to-end performance did not provide "
                    "the expected operational gain"
                ),
                "run_id": "2026-08-09/23-57-05",
                "vram": "8 GB VRAM",
            },
            {
                "classification": "STOPPED_PERFORMANCE_FEASIBILITY",
                "gpu_model": "NVIDIA GeForce RTX 4060 Laptop GPU",
                "gpu_model_source": (
                    "philosophia/successor/dev/PHASE1_MINIMO_REPRO_15.md "
                    "(same named Lenovo Legion host as the cost-adapted continuation "
                    "recorded in PHASE1B_MINIMO_COST_ADAPTED.md)"
                ),
                "inference_forbidden": [
                    "do not infer that the GPU was intrinsically slower",
                    "do not infer that 8 GB VRAM was the sole cause",
                ],
                "machine_name": "Lenovo Legion",
                "not_equal_architecture_hardware_benchmark": True,
                "not_phase16_17_checkpoint_source": True,
                "reason": (
                    "ended because the observed end-to-end performance did not provide "
                    "the expected operational gain"
                ),
                "run_id": "2026-08-10/07-27-05",
                "vram": "8 GB VRAM",
            },
        ],
        "forward_boundary": (
            "Phase 2 must pin architecture explicitly, may not let CUDA availability "
            "choose the scientific learner, and must canonicalize unique action "
            "identities before constructing children. This package does not implement "
            "Phase 2."
        ),
        "hashes": hashes,
        "bounded_action_order_probe": {
            "artifact": sha256_file(ACTION_ORDER_PATH),
            "distinct_order_count": action_order["distinct_order_count"],
            "sole_cause_claim": False,
            "status": action_order["status"],
            "worker_count": action_order["worker_count"],
        },
        "minimo_git": {
            "commit": commit,
            "status_short": status_short,
        },
        "no_public_archive": True,
        "no_public_archive_statement": (
            "No public archive currently exists for this Phase-1 realization."
        ),
        "not_paper_scale": True,
        "not_equal_architecture_reproduction": True,
        "realization": "repository-default CPU-debug MINIMO realization",
        "run": {
            "end_evidence": end_evidence,
            "execution_route": "single-process CPU",
            "execution_route_evidence": [
                "minimo_prop_full.log: Running in single-process mode.",
                "bootstrap.py submit_task uses worker.try_prove.run when DISTRIBUTED is unset",
                "hydra launcher: hydra._internal.core_plugins.basic_launcher.BasicLauncher",
                "TransformerLMPolicy CPU debug branch; checkpoints load on cpu",
            ],
            "path": str(RUN_DIR),
            "start_evidence": start_evidence,
        },
        "schema": "phase1-provenance-18.v1",
        "scientific_claim": False,
        "training_rng": {
            "status": "UNSEEDED",
            "reason": (
                "bootstrap.py did not initialize and persist Python/NumPy/Torch launch RNG state"
            ),
        },
        "verdict": VERDICT,
    }


def write_bytes(path: Path, data: bytes) -> None:
    path.write_bytes(data)
    if path.read_bytes() != data:
        raise FailClosed("write/read mismatch for %s" % path)


def main() -> int:
    try:
        action_order = load_action_order_probe()
        result = aggregate()
        result["action_order_probe"] = {
            "distinct_order_count": action_order["distinct_order_count"],
            "sorted_action_set_sha256": action_order["sorted_action_set_sha256"],
            "status": action_order["status"],
            "worker_count": action_order["worker_count"],
        }
        markdown = write_markdown(result)
        markdown_bytes = markdown.encode("ascii")
        result_bytes = dump_canonical(result)
        provenance = build_provenance(result, action_order)
        provenance_bytes = dump_canonical(provenance)
        write_bytes(RESULTS_PATH, result_bytes)
        write_bytes(REPORT_PATH, markdown_bytes)
        write_bytes(PROVENANCE_PATH, provenance_bytes)
    except FailClosed as exc:
        sys.stderr.write("FAIL CLOSED: %s\n" % exc)
        return 1
    sys.stdout.write("wrote %s\n" % RESULTS_PATH)
    sys.stdout.write("wrote %s\n" % REPORT_PATH)
    sys.stdout.write("wrote %s\n" % PROVENANCE_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
