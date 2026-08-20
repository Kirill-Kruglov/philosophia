#!/usr/bin/env python3
"""PHASE1_17 descriptive inventory over 16B/16C/16D. Read-only. No verdict."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

DEV = Path(__file__).resolve().parent
OUT = DEV / "phase1_17_paired_cost_results.json"
CK = {
    0: DEV / "phase1_extrinsic_16b/checkpoint_0.json",
    1: DEV / "phase1_extrinsic_16c/checkpoint_1.json",
    2: DEV / "phase1_extrinsic_16c/checkpoint_2.json",
    3: DEV / "phase1_extrinsic_16c/checkpoint_3.json",
    4: DEV / "phase1_extrinsic_16b/checkpoint_4.json",
}
LOG16C = DEV / "phase1_extrinsic_16c_run.log"
CK16D = sorted((DEV / "phase1_extrinsic_16d").glob("checkpoint_*.json"))


def sha(p: Path) -> dict:
    raw = p.read_bytes()
    lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return {
        "rel": str(p.relative_to(DEV)),
        "sha256_raw": hashlib.sha256(raw).hexdigest(),
        "sha256_lf": hashlib.sha256(lf).hexdigest(),
        "nbytes": len(raw),
    }


def load(p: Path):
    d = json.loads(p.read_text(encoding="utf-8"))
    rec = {r["problem"]: r for r in d["records"]}
    solved = list(d.get("solved") or [k for k, r in rec.items() if r["success"]])
    return rec, solved


def loss_feats(log: str, losses: list[str]) -> dict:
    m = re.search(
        r"===== checkpoint 1 budget 8000.*?=====(.*?)(?:===== checkpoint |\Z)", log, re.S
    )
    parts = re.split(r"Attempting problem: (kleene_[^\n]+)\n", m.group(1) if m else "")
    out = {}
    for i in range(1, len(parts), 2):
        name, blk = parts[i], parts[i + 1]
        if name not in losses:
            continue
        gm = re.search(r"Goal: (.+)", blk)
        goal = gm.group(1).strip() if gm else None
        marks = [int(x) for x in re.findall(r"(\d+)\s*/\s*8000", blk)]
        pl = None
        if "Found solution!" in blk:
            after = blk.split("Found solution!", 1)[1]
            chunk = re.split(r"\n(?:Success\?|Elapsed_s|Attempting)", after)[0]
            pl = len([ln for ln in chunk.splitlines() if ln.strip()])
        out[name] = {
            "goal": goal,
            "statement_length_chars": len(goal) if goal else None,
            "proof_print_n_nonempty_lines": pl,
            "tqdm_last_n_of_8000": marks[-1] if marks else None,
            "tqdm_note": "timer-refreshed; not a recorded expansion counter",
        }
    return out


def main() -> None:
    script = Path(__file__).resolve()
    inputs = [sha(p) for p in list(CK.values()) + CK16D + [LOG16C]]
    cks = {i: load(p) for i, p in CK.items()}
    fields = sorted({k for rec, _ in cks.values() for r in rec.values() for k in r})
    cost = {
        "host_independent_per_problem_counter_recorded": False,
        "fields_present_in_16b_16c_16d_records": fields,
        "agent_iterations": {
            "where": "checkpoint JSON records via proofsearch.py",
            "unit": "outer agent actions after one MCTS call",
            "observed": "0 on every success, 1 on every exhaustion",
            "is_search_cost": False,
        },
        "elapsed_s": {"where": "checkpoint JSON", "unit": "wall seconds", "host_independent": False},
        "mcts_budget": {"where": "checkpoint JSON", "unit": "MCTS loop ceiling", "is_used_cost": False},
        "mcts_expansions_in_these_artifacts": "mcts_expansions" in fields,
        "smallest_instrumentation_change": (
            "Record integer mcts_expansions (= sum of MonteCarloTreeSearch.evaluate "
            "n_entered) on each ProofSearchResult / JSON record. Do not use elapsed_s or tqdm."
        ),
        "item_2_status": "STOPPED — no host-independent per-problem cost counter",
    }
    solved = {f"ck{i}": cks[i][1] for i in range(5)}
    losses = sorted(set(cks[1][1]) - set(cks[2][1]))
    gains = sorted(set(cks[2][1]) - set(cks[1][1]))
    feats = loss_feats(LOG16C.read_text(encoding="utf-8"), losses)
    for n in losses:
        feats.setdefault(n, {})
        feats[n]["ck1_elapsed_s"] = cks[1][0][n]["elapsed_s"]
        feats[n]["ck2_success"] = cks[2][0][n]["success"]
        feats[n]["ck2_elapsed_s"] = cks[2][0][n]["elapsed_s"]
    near = [n for n in losses if (feats.get(n) or {}).get("tqdm_last_n_of_8000", 0) >= 7500]
    lens = sorted({feats[n].get("statement_length_chars") for n in losses})
    clustering = {
        "ck1_minus_ck2": losses,
        "ck2_minus_ck1": gains,
        "per_theorem_from_16c_run_log": feats,
        "n_with_tqdm_last_ge_7500": len(near),
        "names_tqdm_last_ge_7500": near,
        "logs_support": {
            "related_cluster": f"Goal char-lengths in log: {lens}; names alone do not prove one event.",
            "threshold_effect": (
                f"{len(near)}/{len(losses)} have tqdm_last>=7500 ({near}); not all eight near cap."
            ),
            "divergent_search": "No first-branching / action-trace field in these artifacts.",
            "choice_among_three": "NOT_DECIDED_BY_LOGS",
        },
    }
    table = [{"checkpoint": f"ck{i}", "n_solved": len(cks[i][1]), "solved": cks[i][1]} for i in range(5)]
    payload = {
        "status": "DESCRIPTIVE_ONLY__NO_VERDICT_TOKEN",
        "item_1_cost_counter": cost,
        "item_2_paired_cost": None,
        "item_3_solved_sets": solved,
        "item_3_table": table,
        "item_3_curve_counts": [len(cks[i][1]) for i in range(5)],
        "item_3_ck1_lost_at_ck2": losses,
        "item_4_clustering": clustering,
        "input_hashes": inputs,
        "script_hashes": sha(script),
        "16d_solved_counts": {p.name: json.loads(p.read_text())["n_solved"] for p in CK16D},
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("curve", payload["item_3_curve_counts"])
    print("ck1_lost_at_ck2", losses)
    print(cost["item_2_status"])
    print("wrote", OUT)


if __name__ == "__main__":
    main()
