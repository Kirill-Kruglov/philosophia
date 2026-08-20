"""Parse partial PHASE1 Minimo run logs into results JSON. Not part of minimo."""
from __future__ import annotations

import json
import re
import statistics
from pathlib import Path

OUT = Path(r"C:\Users\LEGION\Kirill\ShareTops\philosophia\successor\dev\PHASE1_MINIMO_REPRO_15_run.log")
ERR = Path(r"C:\Users\LEGION\Kirill\ShareTops\philosophia\successor\dev\PHASE1_MINIMO_REPRO_15_run.log.err")
SAMPLES = Path(r"C:\Users\LEGION\Kirill\ShareTops\philosophia\successor\dev\phase1_resource_samples.jsonl")
HYDRA = Path(r"C:\Users\LEGION\Kirill\ShareTops\minimo\learning\outputs\2026-08-09\23-57-05")
RESULT = Path(r"C:\Users\LEGION\Kirill\ShareTops\philosophia\successor\dev\PHASE1_MINIMO_REPRO_15_results.json")


def main() -> None:
    text = OUT.read_text(encoding="utf-8", errors="replace")
    err_text = ERR.read_text(encoding="utf-8", errors="replace")

    outer = re.findall(r"\|\s*(\d+)/200\s*\[([^,\]]+)", err_text)
    last_outer = outer[-1] if outer else None

    prove_starts = list(re.finditer(r"^Proving (.+) on cuda:0\s*$", text, re.M))
    results = []
    for i, m in enumerate(prove_starts):
        start = m.end()
        end = prove_starts[i + 1].start() if i + 1 < len(prove_starts) else len(text)
        chunk = text[start:end]
        if "Did not find solution" in chunk:
            ok: bool | None = False
        elif re.search(r"Found solution|Solution found|Proved!", chunk, re.I):
            ok = True
        else:
            ok = None
        n_actions = len(re.findall(r"Taking action ", chunk))
        results.append(
            {
                "i": i,
                "statement": m.group(1)[:240],
                "success": ok,
                "taking_action_count": n_actions,
            }
        )

    completed = [r for r in results if r["success"] is not None]
    successes = [r for r in completed if r["success"]]
    fails = [r for r in completed if r["success"] is False]
    incomplete = [r for r in results if r["success"] is None]
    lengths = [r["taking_action_count"] for r in successes]

    vram, ram, util = [], [], []
    if SAMPLES.exists():
        for line in SAMPLES.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if "vram_mib" in row:
                vram.append(row["vram_mib"])
            if "ram_mib" in row:
                ram.append(row["ram_mib"])
            if "gpu_util" in row:
                util.append(row["gpu_util"])

    # Parse wall from tqdm elapsed like 5:40:20
    wall_hours = None
    if last_outer:
        parts = last_outer[1].split(":")
        if len(parts) == 3:
            h, m, s = map(int, parts)
            wall_hours = h + m / 60 + s / 3600
        elif len(parts) == 2:
            m, s = map(int, parts)
            wall_hours = m / 60 + s / 3600

    summary = {
        "stop_reason": (
            "iteration_0_exceeds_~6h_stop: proving at ~125/200 after ~5.7h wall; "
            "tqdm ETA remaining ~9h. Killed per stop condition. No outcomes_*.json written "
            "(minimo writes outcomes only after all 200 conjectures finish)."
        ),
        "hydra_dir": str(HYDRA),
        "minimo_commit": "6066f482c6752915ad21119f93dc162f4cb9db72",
        "minimo_commit_msg": "Fix proof checking scope including later definitions",
        "local_modifications": [
            "Host installs only (not minimo source): rustup + VS2022 Build Tools VCTools; "
            "CUDA torch 2.11.0+cu128 into minimo/.venv (pip default was CPU).",
            "Helper bat minimo/build_peano_bin.bat for PYO3_PYTHON-aware cargo build (not algorithm).",
            "No changes to minimo algorithm, config defaults, or theory files.",
        ],
        "config": {
            "theory": "propositional-logic",
            "iterations": 5,
            "n_conjectures": 200,
            "agent": "mcts-lm",
            "expansions": 1000,
            "hindsight": True,
            "wandb_project": None,
            "seed": "single default (no seed override)",
        },
        "iteration_partial": 0,
        "iterations_completed": 0,
        "n_conjectures_target": 200,
        "n_prove_started": len(prove_starts),
        "n_completed": len(completed),
        "n_success": len(successes),
        "n_fail": len(fails),
        "n_incomplete_killed": len(incomplete),
        "proven_fraction_of_completed": (len(successes) / len(completed) if completed else None),
        "paper_reference_proven_fraction": "initial batches ~10-20% (arXiv:2407.00695)",
        "proof_lengths_proxy_taking_action_count": {
            "note": (
                "Stdout does not print final proof action lists for successes reliably; "
                "proxy = count of 'Taking action' lines during the search that eventually succeeded. "
                "This is NOT identical to paper's proof-length metric; use only as rough signal."
            ),
            "mean": statistics.mean(lengths) if lengths else None,
            "max": max(lengths) if lengths else None,
            "min": min(lengths) if lengths else None,
            "n": len(lengths),
            "all": lengths,
        },
        "last_outer_tqdm": (
            {"done": int(last_outer[0]), "of": 200, "elapsed_str": last_outer[1]}
            if last_outer
            else None
        ),
        "cost": {
            "wall_hours_approx_at_stop": wall_hours if wall_hours is not None else 5.7,
            "peak_vram_mib": max(vram) if vram else None,
            "mean_vram_mib": statistics.mean(vram) if vram else None,
            "peak_system_ram_mib": max(ram) if ram else None,
            "mean_gpu_util_pct": statistics.mean(util) if util else None,
            "median_gpu_util_pct": statistics.median(util) if util else None,
            "bound": (
                "GPU-bound during MCTS policy eval (util often 80-100%; VRAM pegged ~7.7-7.9 GiB "
                "of 8.2 GiB). Process RSS ~1.0-1.1 GiB. Not CPU-idle."
            ),
            "scaling_one_line": (
                "Prop-logic alone ~15h+/iteration at this hardware pace for 200×1000-MCTS; "
                "×5 iterations ≈ days; ×3 harder theories ≫ week on one 4060 laptop — "
                "need multi-worker/distributed or smaller n_conjectures for Phase-2 cost."
            ),
        },
        "extrinsic": {
            "status": "SKIPPED",
            "reason": (
                "learning/extrinsic/propositional-logic.p exists, but problems.load_problemset "
                "only knows lean-library-logic and natural-number-game. proofsearch.py "
                "task=eval -> evaluate_agent requires a registered problemset. Wiring Kleene-35 "
                "needs new code; forbidden in this task."
            ),
        },
        "verdict": "PARTIAL",
        "verdict_detail": (
            "Stopped mid-iteration-0 by ~6h/iteration cost stop before any full iteration "
            "completed. Cannot evaluate proof-length growth across iterations or extrinsic "
            "rise. Partial iter-0 proven fraction among completed searches is reported. "
            "Not FLAT (insufficient iterations). Not REPRODUCED (curve incomplete)."
        ),
        "paper_targets_for_eye_check": {
            "arxiv": "https://arxiv.org/abs/2407.00695",
            "fig2_proof_length_prop_logic": "mean 2.75->4.21; longest 5->11 across 5 iters",
            "fig4_extrinsic": "success ~0.30 (ckpt0) -> ~0.47 (ckpt4) on Kleene Thm 41",
            "proven_fraction_initial": "~10-20%",
        },
    }
    RESULT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in summary if k != "proof_lengths_proxy_taking_action_count"}, indent=2))
    print("proof_lengths", summary["proof_lengths_proxy_taking_action_count"])
    print("wrote", RESULT)


if __name__ == "__main__":
    main()
