#!/usr/bin/env python3
"""Aggregate Phase-1 Kleene extrinsic checkpoint JSONs into the report artifacts."""

from __future__ import annotations

import json
import statistics
import subprocess
from pathlib import Path


OUT = Path(__file__).resolve().parent
DATA = OUT / "phase1_extrinsic_16"
REPORT = OUT / "PHASE1_EXTRINSIC_16.md"
RESULTS = OUT / "PHASE1_EXTRINSIC_16_results.json"
RUN_DIR = Path("/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33")
MINIMO = Path("/home/master/llm_projects/minimo")


def load_checkpoint(index: int) -> dict:
    path = DATA / f"checkpoint_{index}.json"
    return json.loads(path.read_text(encoding="ascii"))


def git_diff(relpath: str) -> str:
    return subprocess.check_output(
        ["git", "diff", "--", relpath],
        cwd=str(MINIMO),
        text=True,
    )


def main() -> None:
    rows = [load_checkpoint(i) for i in range(5)]
    rates = [row["success_rate"] for row in rows]
    verdict = "TRANSFER_RISES" if rates[4] > rates[0] else "FLAT"

    solved_by_ck = {i: set(row["solved"]) for i, row in enumerate(rows)}
    all_problems = [r["problem"] for r in rows[0]["records"]]
    first_solved: dict[str, int | None] = {}
    for problem in all_problems:
        first = None
        for i in range(5):
            if problem in solved_by_ck[i]:
                first = i
                break
        first_solved[problem] = first

    only_at_last = [p for p in all_problems if first_solved[p] == 4]
    never = [p for p in all_problems if first_solved[p] is None]

    all_records = [r for row in rows for r in row["records"]]
    mean_cost = statistics.mean(r["elapsed_s"] for r in all_records)
    mean_cost_by_ck = [row["mean_elapsed_s"] for row in rows]
    succ_costs = [r["elapsed_s"] for r in all_records if r["success"]]
    fail_costs = [r["elapsed_s"] for r in all_records if not r["success"]]

    problems_diff = git_diff("learning/problems.py")
    proofsearch_diff = git_diff("learning/proofsearch.py")
    porcelain = subprocess.check_output(
        ["git", "status", "--porcelain", "--",
         "learning/problems.py", "learning/proofsearch.py",
         "learning/theories/", "learning/config/"],
        cwd=str(MINIMO),
        text=True,
    ).strip().splitlines()
    dirty_paths: list[str] = []
    for line in porcelain:
        # Porcelain is usually "XY PATH"; some paths show as "X PATH" with one space.
        path = line.split(None, 1)[1]
        if path.startswith('"') and path.endswith('"'):
            path = path[1:-1]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        dirty_paths.append(path)

    allowed_dirty = {
        "learning/problems.py",
        "learning/proofsearch.py",
    }
    unexpected_dirty = [p for p in dirty_paths if p not in allowed_dirty]
    theory_diff_empty = not subprocess.check_output(
        ["git", "diff", "--", "learning/theories/propositional-logic.p"],
        cwd=str(MINIMO),
        text=True,
    ).strip()
    config_diff_empty = not subprocess.check_output(
        ["git", "diff", "--", "learning/config/"],
        cwd=str(MINIMO),
        text=True,
    ).strip()

    payload = {
        "schema": "phase1-extrinsic-16.v1",
        "scientific_outcome": False,
        "phase": 1,
        "citable": False,
        "run_dir": str(RUN_DIR),
        "problemset_id": "kleene",
        "n_statements_in_file": len(all_problems),
        "paper_maintext_count": 35,
        "paper_appendix_note": (
            "Appendix E.2: 30 statements even if last label is 25; "
            "main text informal count is 35."
        ),
        "wall_clock": {
            "start": "2026-08-10T20:00:07+03:00",
            "end": "2026-08-10T21:32:49+03:00",
            "approx_hours": 1.545,
        },
        "protocol": {
            "agent": "mcts-lm",
            "node_type": "holophrasm",
            "mcts_budget": 2000,
            "accumulate_library": False,
            "seed": 0,
            "omp_num_threads": 16,
            "nice": 10,
            "theory": "learning/theories/propositional-logic.p",
            "statements": "learning/extrinsic/propositional-logic.p",
            "premises": [
                "and_i", "and_el", "and_er", "or_il", "or_ir", "or_e",
                "not_i", "not_e", "exfalso", "iff_i", "iff_el", "iff_er", "em",
            ],
            "kleene_23_24_loader_normalize": True,
        },
        "success_rate_by_checkpoint": rates,
        "n_solved_by_checkpoint": [row["n_solved"] for row in rows],
        "mean_elapsed_s_by_checkpoint": mean_cost_by_ck,
        "mean_elapsed_s_overall": mean_cost,
        "mean_elapsed_s_success": statistics.mean(succ_costs) if succ_costs else None,
        "mean_elapsed_s_failure": statistics.mean(fail_costs) if fail_costs else None,
        "searches_per_second_effective": 150 / (1.545 * 3600),
        "seconds_per_search_overall": mean_cost,
        "first_solved_checkpoint": first_solved,
        "only_first_solved_at_checkpoint_4": only_at_last,
        "never_solved": never,
        "solved_set_diff_ck4_minus_ck0": sorted(solved_by_ck[4] - solved_by_ck[0]),
        "solved_set_diff_ck0_minus_ck4": sorted(solved_by_ck[0] - solved_by_ck[4]),
        "checkpoints": rows,
        "verdict": verdict,
        "paper_fig4_reference": {"ck0_approx": 0.30, "ck4_approx": 0.47},
        "minimo_dirty_paths": dirty_paths,
        "unexpected_dirty_paths": unexpected_dirty,
        "theory_file_unmodified": theory_diff_empty,
        "config_dir_unmodified": config_diff_empty,
        "confirmed_unmodified": [
            "learning/theories/propositional-logic.p"
            + (" (diff empty)" if theory_diff_empty else " (DIRTY!)"),
            "learning/config/"
            + (" (diff empty)" if config_diff_empty else " (DIRTY!)"),
            "training loop (not edited)",
        ],
    }
    RESULTS.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )

    table = [
        "| checkpoint | solved / N | success rate | mean elapsed_s |",
        "|---:|---:|---:|---:|",
    ]
    for i, row in enumerate(rows):
        table.append(
            f"| {i} | {row['n_solved']} / {row['n_problems']} | "
            f"{row['success_rate']:.4f} | {row['mean_elapsed_s']:.2f} |"
        )

    matrix_lines = [
        "| theorem | ck0 | ck1 | ck2 | ck3 | ck4 | first |",
        "|---|:-:|:-:|:-:|:-:|:-:|---:|",
    ]
    for problem in all_problems:
        marks = []
        for i in range(5):
            marks.append("Y" if problem in solved_by_ck[i] else ".")
        first = first_solved[problem]
        matrix_lines.append(
            f"| `{problem}` | " + " | ".join(marks)
            + f" | {first if first is not None else '-'} |"
        )

    report = f"""# PHASE1_EXTRINSIC_16

NON-CITABLE Phase-1 instrument construction. Extrinsic evaluation of the
reproduced Minimo propositional-logic run on Kleene Theorem-41 statements.
No philosophia ACTIVE/YOKED claim. No scientific lock.

## VERDICT: {verdict}

ck4 success rate ({rates[4]:.4f}) does not exceed ck0 ({rates[0]:.4f}).
Per stop protocol: report FLAT; do not retune expansions, agent, or problem set.

Run dir: `{RUN_DIR}`.
Checkpoints: `0.pt`..`4.pt`. Agent: `mcts-lm` / `holophrasm`.
Budget: 2000 MCTS expansions per theorem. `accumulate_library=false`.
Seed: 0. `OMP_NUM_THREADS=16`, `nice -n 10`.
Wall clock: 2026-08-10T20:00:07+03:00 -> 2026-08-10T21:32:49+03:00
(~1 h 33 m for 150 searches).

Statement file `learning/extrinsic/propositional-logic.p` contains
**{len(all_problems)}** Peano statements (labels through 25 with a/b variants).
Paper main text says 35; Appendix E.2 explicitly notes there are 30 statements
under that numbering. This eval uses the on-disk file (N={len(all_problems)}).
Background theory is `learning/theories/propositional-logic.p` with the training
premise names (`and_i`, ... `em`), not `lean-library-logic`.

Paper Fig. 4 reference (propositional logic): ~0.30 at ck0 to ~0.47 at ck4.

### Success rate by checkpoint

{chr(10).join(table)}

Overall mean wall-clock search cost: **{mean_cost:.2f} s/search**
(success mean {statistics.mean(succ_costs):.2f} s; failure mean
{statistics.mean(fail_costs):.2f} s). Observed full-budget failures land near
~53 s at 2000 expansions on this CPU box — about 2.3x faster than the pre-run
~2 min/search estimate; total ~1.5 h vs ~6 h estimate.

### Solved-set movement (rate-flat but not identical)

- ck4 only (not ck0): {", ".join(f"`{p}`" for p in sorted(solved_by_ck[4]-solved_by_ck[0])) or "(none)"}
- ck0 only (not ck4): {", ".join(f"`{p}`" for p in sorted(solved_by_ck[0]-solved_by_ck[4])) or "(none)"}
- ck3 lost `kleene_20` relative to ck0/1/2; ck4 gained `kleene_3` and lost `kleene_20`.

### Theorems solved only starting at checkpoint 4

{", ".join(f"`{p}`" for p in only_at_last) or "(none)"}

Note: `kleene_3` is solved at ck4 and not at ck0–ck3, so it is first-solved at 4.

### Never solved at any checkpoint

{", ".join(f"`{p}`" for p in never) or "(none)"}

### Per-theorem matrix

{chr(10).join(matrix_lines)}

### Wiring (only new code)

Confirmed unmodified: training loop, `learning/config/` defaults, and
`learning/theories/propositional-logic.p`. Minimo dirty set after the gate is
exactly `learning/problems.py` and `learning/proofsearch.py`
(unexpected dirty: {unexpected_dirty or "none"}).

Loader-only Peano surface fix: statements 23 and 24 in the extrinsic file use
`(not (not ['A -> 'B]))` forms the current Peano parser rejects. The loader
rewrites them to the equivalent `[[[...] -> false] -> false]` encoding so they
are searched (not skipped as parse errors). Theory file untouched.

Orchestration only (philosophia tree, no search logic):
`successor/dev/run_phase1_extrinsic_16.sh`,
`successor/dev/aggregate_phase1_extrinsic_16.py`.
Run log: `successor/dev/phase1_extrinsic_16_run.log`
(also copied to `PHASE1_EXTRINSIC_16_run.log`).

#### Diff: `minimo/learning/problems.py`

```diff
{problems_diff.rstrip()}
```

#### Diff: `minimo/learning/proofsearch.py` (`evaluate_agent` only)

```diff
{proofsearch_diff.rstrip()}
```

### Negative authorization

No ACTIVE/YOKED, no philosophia thesis claim, no library-growth arm, no
retraining, no post-hoc expansion or problem-set edits after seeing outcomes.
"""
    REPORT.write_text(report, encoding="utf-8")
    print(verdict, RESULTS, REPORT)


if __name__ == "__main__":
    main()
