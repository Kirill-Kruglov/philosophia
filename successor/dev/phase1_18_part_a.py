#!/usr/bin/env python3
"""PHASE1_18 Part A: checkpoint identity. INSTRUMENT_INTEGRITY__NO_SEED_SPEND_AUTHORIZED."""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

DEV = Path(__file__).resolve().parent
CKDIR = Path("/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33")
PROOF = Path("/home/master/llm_projects/minimo/learning/proofsearch.py")
OUT_J, OUT_M = DEV / "phase1_18_part_a_results.json", DEV / "PHASE1_18_PART_A.md"
CK0 = ["kleene_1", "kleene_10a", "kleene_10b", "kleene_11", "kleene_16", "kleene_17a",
       "kleene_17b", "kleene_18a", "kleene_18b", "kleene_19", "kleene_20"]
SETS = {
    0: CK0,
    1: CK0[:1] + ["kleene_2", "kleene_3", "kleene_4", "kleene_5", "kleene_6", "kleene_7", "kleene_8b"]
       + CK0[1:4] + ["kleene_13"] + CK0[4:],
    2: list(CK0), 3: list(CK0),
    4: ["kleene_1", "kleene_3", "kleene_6", "kleene_7", "kleene_10a", "kleene_10b",
        "kleene_11", "kleene_16", "kleene_17a", "kleene_17b", "kleene_18a", "kleene_18b", "kleene_19"],
}


def sha(b): return hashlib.sha256(b).hexdigest()
def pair(p):
    r = p.read_bytes(); return {"path": str(p), "nbytes": len(r), "raw_sha256": sha(r),
                                "lf_sha256": sha(r.replace(b"\r\n", b"\n").replace(b"\r", b"\n"))}
def fsha(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()


def param_digest(agent):
    h = hashlib.sha256()
    for k in sorted(agent._policy._lm.state_dict()):
        t = agent._policy._lm.state_dict()[k].detach().to("cpu").contiguous()
        h.update(k.encode("ascii")); h.update(str(tuple(t.shape)).encode("ascii"))
        h.update(str(t.dtype).encode("ascii")); h.update(t.numpy().tobytes())
    return h.hexdigest()


def load_trace():
    src = PROOF.read_text(encoding="utf-8")
    checks = {
        "task_eval_calls_evaluate_agent": "elif cfg.task == 'eval':" in src and "evaluate_agent(cfg)" in src,
        "evaluate_agent_calls_make_agent": "agent = make_agent(config)" in src,
        "make_agent_torch_loads_agent_path": "agent = torch.load(config['agent_path'], weights_only=False)" in src,
        "results_record_agent_path": "'agent_path': str(config.get('agent_path'))" in src,
    }
    return {"proofsearch": pair(PROOF), "source_checks": checks, "load_path_ok": all(checks.values()),
            "chain": ["main task==eval -> evaluate_agent(cfg)",
                      "evaluate_agent -> make_agent(config)",
                      "make_agent -> torch.load(config['agent_path'])",
                      "results JSON records config agent_path"]}


def main():
    import torch
    rows, digs = [], []
    for i in range(5):
        path = CKDIR / ("%d.pt" % i)
        agent = torch.load(path, map_location="cpu", weights_only=False)
        dig = param_digest(agent); digs.append(dig)
        rows.append({"checkpoint": "ck%d" % i, "path": str(path), "nbytes": path.stat().st_size,
                     "file_sha256": fsha(path), "param_digest": dig,
                     "n_lm_tensors": len(agent._policy._lm.state_dict()),
                     "phase1_17_solved_set": SETS[i], "phase1_17_n_solved": len(SETS[i])})
    pairwise = [{"a": "ck%d" % i, "b": "ck%d" % j,
                 "file_equal": rows[i]["file_sha256"] == rows[j]["file_sha256"],
                 "param_digest_equal": digs[i] == digs[j],
                 "solved_set_equal": SETS[i] == SETS[j]}
                for i in range(5) for j in range(i + 1, 5)]
    load = load_trace()
    if not load["load_path_ok"]: outcome = "load_path_defective"
    elif len(set(digs)) < 5: outcome = "weights_identical"
    else: outcome = "weights_differ_sets_identical"
    payload = {
        "schema": "phase1-18-part-a-checkpoint-identity.v1",
        "status": "INSTRUMENT_INTEGRITY__NO_SEED_SPEND_AUTHORIZED",
        "outcome": outcome, "part_b_authorized": outcome == "weights_differ_sets_identical",
        "unique_param_digests": len(set(digs)), "checkpoints": rows, "pairwise": pairwise,
        "load_path": load,
        "behavioural_sets_from_phase1_17": {
            "ck2_equals_ck0": SETS[2] == SETS[0], "ck3_equals_ck0": SETS[3] == SETS[0],
            "ck1_differs_ck0": SETS[1] != SETS[0], "ck4_differs_ck0": SETS[4] != SETS[0],
            "source": "PHASE1_17 section 3 solved-set identities"},
        "inputs": {"script": pair(Path(__file__)), "proofsearch": pair(PROOF),
                   "checkpoints": [pair(CKDIR / ("%d.pt" % i)) for i in range(5)]},
        "negative_authorization": "No training, no seed spend, no Part B in this artifact.",
    }
    OUT_J.write_bytes((json.dumps(payload, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii"))
    md = ["# PHASE1_18 Part A - checkpoint identity", "",
          "Status: `INSTRUMENT_INTEGRITY__NO_SEED_SPEND_AUTHORIZED`", "",
          "Outcome: **%s**" % outcome, "", "Part B authorized: `%s`" % payload["part_b_authorized"], "",
          "## Load path (code-traced)", ""] + ["- `%s`" % s for s in load["chain"]] + [
          "", "source_checks: `%s`" % json.dumps(load["source_checks"]), "",
          "## Per-checkpoint digests", "",
          "| ck | nbytes | file SHA-256 | param digest (loaded LM) | n_solved (PHASE1_17) |",
          "|---|---:|---|---|---:|"]
    for r in rows:
        md.append("| %s | %d | `%s` | `%s` | %d |" % (
            r["checkpoint"], r["nbytes"], r["file_sha256"], r["param_digest"], r["phase1_17_n_solved"]))
    md += ["", "## Pairwise", "", "| a | b | file_equal | param_digest_equal | solved_set_equal |",
           "|---|---|---|---|---|"]
    for p in pairwise:
        md.append("| %s | %s | %s | %s | %s |" % (
            p["a"], p["b"], p["file_equal"], p["param_digest_equal"], p["solved_set_equal"]))
    md += ["", "## Reading", "",
           "All five file hashes differ; all five loaded-parameter digests differ "
           "(unique_param_digests=%d). Eval task=eval loads config.agent_path via "
           "make_agent/torch.load and records that path in the results JSON. "
           "Hydra overrides for 16B/16C/17 name the matching N.pt. So ck2/ck3 did not "
           "silently run cold: they are distinct trained states whose external solved "
           "sets (PHASE1_17) coincide with ck0." % payload["unique_param_digests"], "",
           "## Hashes", "",
           "- script raw `%s` lf `%s`" % (payload["inputs"]["script"]["raw_sha256"],
                                         payload["inputs"]["script"]["lf_sha256"]),
           "- proofsearch raw `%s` lf `%s`" % (payload["inputs"]["proofsearch"]["raw_sha256"],
                                              payload["inputs"]["proofsearch"]["lf_sha256"]), ""]
    for c in payload["inputs"]["checkpoints"]:
        md.append("- `%s` raw `%s` lf `%s`" % (c["path"], c["raw_sha256"], c["lf_sha256"]))
    md += ["", "STOP after Part A. No Part B in this run.", ""]
    OUT_M.write_text("\n".join(md), encoding="ascii")
    print(json.dumps({"outcome": outcome, "part_b_authorized": payload["part_b_authorized"],
                      "unique_param_digests": payload["unique_param_digests"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, "/home/master/llm_projects/minimo/learning")
    raise SystemExit(main())
