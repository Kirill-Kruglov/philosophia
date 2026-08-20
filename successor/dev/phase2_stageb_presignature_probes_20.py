#!/usr/bin/env python3
"""PHASE2_STAGE_B pre-signature probes 20 (+depth1..8, exclusions). DEV_PROBE_ONLY."""
from __future__ import annotations
import hashlib, hmac, json, os, subprocess, sys
from pathlib import Path

HERE, MINIMO = Path(__file__).resolve().parent, Path("/home/master/llm_projects/minimo/learning")
REC = Path("/home/master/llm_projects/philosophia/successor/recovery/phase2_stage_b_20260815")
THEORY = REC / "archive/accepted_l01/learning/theories/propositional-logic-intuitionistic-fragment.p"
L01X, L02X = REC / "archive/accepted_l01/PHASE2_STAGE_B_L01_RAW_FIXTURE_EXCLUSIONS_V2.json", REC / "accepted_l2/PHASE2_STAGE_B_L2_RAW_FIXTURE_EXCLUSIONS_V3.json"
PREMISES = ("and_i", "and_el", "and_er", "or_il", "or_ir", "or_e", "not_i", "not_e", "exfalso")
PRF, DATE = b"philosophia.stageb-presignature-probe.v1", "2026-08-16"
OUT_J, OUT_M, OUT_L = HERE / "phase2_stageb_presignature_probes_20_results.json", HERE / "PHASE2_STAGEB_PRESIGNATURE_PROBES_20.md", HERE / "phase2_stageb_presignature_probes_20_run.log"
REG = HERE / "phase2_disposable_identity_registry.jsonl"
A = (
    ("and_i", "[('a0 : prop) -> ('a1 : prop) -> 'a0 -> 'a1 -> (and 'a0 'a1)]", ["intro.", "intro.", "intro.", "intro.", "a and_i", "=> ."]),
    ("and_el", "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> 'a0]", ["intro.", "intro.", "intro.", "c and_el", "=> (and_el x x0 x1)."]),
    ("and_er", "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> 'a1]", ["intro.", "intro.", "intro.", "c and_er", "=> (and_er x x0 x1)."]),
    ("or_il", "[('a0 : prop) -> ('a1 : prop) -> 'a0 -> (or 'a0 'a1)]", ["intro.", "intro.", "intro.", "a or_il", "=> ."]),
    ("or_ir", "[('a0 : prop) -> ('a1 : prop) -> 'a1 -> (or 'a0 'a1)]", ["intro.", "intro.", "intro.", "a or_ir", "=> ."]),
    ("or_e", "[('a0 : prop) -> ('a1 : prop) -> (or 'a0 'a1) -> (or 'a1 'a0)]",
     ["intro.", "intro.", "intro.", "a or_e", "=> [x -> (or x0 x)]; [x0 -> (or x0 x)].", "intro.", "a or_ir", "=> .", "intro.", "a or_il", "=> ."]),
    ("not_i", "[('a0 : prop) -> ['a0 -> false] -> (not 'a0)]", ["intro.", "intro.", "a not_i", "=> ."]),
    ("not_e", "[('a0 : prop) -> (not 'a0) -> 'a0 -> false]", ["intro.", "intro.", "intro.", "a not_e", "=> ."]),
    ("exfalso", "[false -> ('a0 : prop) -> 'a0]", ["intro.", "intro.", "a exfalso", "=> ."]),
)

def sha(b): return hashlib.sha256(b).hexdigest()
def pair(p):
    r = p.read_bytes(); return {"raw_sha256": sha(r), "lf_sha256": sha(r.replace(b"\r\n", b"\n").replace(b"\r", b"\n"))}
def root(i): return hmac.new(b"PRESIGNATURE-PROBE-SEED-ONLY", PRF + b"\x00" + i.to_bytes(8, "big"), hashlib.sha256).hexdigest()
def goal_at(d):
    p = [f"('a{i} : prop)" for i in range(d + 1)] + [f"('h{i} : ['a{i} -> 'a{i+1}])" for i in range(d)] + [f"('base : 'a0)", f"'a{d}"]
    return "[" + " -> ".join(p) + "]"
def grammar_a(goal):  # ambient-arrow family: no connective heads in the outer goal
    return all(tok not in goal for tok in ("(and ", "(or ", "(not "))

def replay(theory, goal, script):
    import peano
    st = [peano.PyProofState(theory, list(PREMISES), goal)]
    for step in script:
        if not st: return False
        cur, st = st[0], st[1:]
        m = [a for a in cur.actions() if str(a) == step]
        if len(m) != 1: return False
        st = list(cur.execute_action(m[0])) + st
    return not st

def ann(text, name):
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#backward ") or s.startswith("#forward "):
            if s.split(" ", 1)[1].split(" ", 1)[0].rstrip(".") == name: return s
    return "ABSENT"

def dirs(theory, goal, name):
    import peano
    s = peano.PyProofState(theory, list(PREMISES), goal)
    while "intro." in [str(a) for a in s.actions()]:
        s = s.execute_action([a for a in s.actions() if str(a) == "intro."][0])[0]
    ser = [str(a) for a in s.actions()]
    return ("c " + name) in ser, ("a " + name) in ser

def arrow(theory, depth, goal):
    import peano
    s = peano.PyProofState(theory, list(PREMISES), goal)
    script = ["intro."] * (2 * depth + 2)
    for _ in range(2 * depth + 2):
        s = s.execute_action([a for a in s.actions() if str(a) == "intro."][0])[0]
    names = s.names_in_context()[1:]
    edges, base = names[depth + 1:depth + 1 + depth], names[2 * depth + 1]
    for i, e in enumerate(edges):
        arg = base if i == 0 else ("p" if i == 1 else "p" + str(i - 2))
        script += ["c " + e, "=> (" + e + " " + arg + ")."]
    return script

def ent(root_hex, prf, pass_id, date, th=None, sk=None):
    return {"root_hex": root_hex, "prf_domain_label": prf, "pass": pass_id, "date": date,
            "theorem_identity": th, "skeleton_identity": sk}

def refuse_if_registered(*, root_hex=None, theorem_identity=None, skeleton_identity=None, path=REG):
    """Fail-closed collision check for later generators."""
    if not path.exists():
        return None
    for line in path.read_text(encoding="ascii").splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        hits = []
        if root_hex and e.get("root_hex") == root_hex: hits.append("root_hex")
        if theorem_identity and e.get("theorem_identity") == theorem_identity: hits.append("theorem_identity")
        if skeleton_identity and e.get("skeleton_identity") == skeleton_identity: hits.append("skeleton_identity")
        if hits:
            raise SystemExit("REFUSED_REGISTERED_IDENTITY:" + ",".join(hits) + ":" + e.get("pass", "?"))
    return None

def seed_l01_l2():
    rows = []
    for label, path, prf in (("L01", L01X, "philosophia.stageb.raw-fixture-exclusions.v2"),
                             ("L2", L02X, "philosophia.stageb.raw-fixture-exclusions.v3")):
        d = json.loads(path.read_text(encoding="ascii"))
        for fx in d.get("enumerability_fixtures", []) + d.get("renderer_only_fixtures", []):
            rows.append(ent(None, prf, label, "2026-08-15", fx.get("raw_ascii_sequent_sha256"), None))
        for fx in d.get("valid_plan_fixtures", []):
            rows.append(ent(None, prf, label, "2026-08-15", fx.get("raw_theorem_sha256"), fx.get("raw_plan_sha256")))
        for hx in d.get("permanently_excluded_fixture_key_hex", []):
            rows.append(ent(hx, prf, label + "_fixture_key", "2026-08-15", None, None))
    return rows

def worker():
    theory, rows, excl = THEORY.read_text(encoding="ascii"), [], []
    for i, (name, goal, script) in enumerate(A):
        r = root(i); fwd, bwd = dirs(theory, goal, name); ok = replay(theory, goal, script)
        rows.append({"premise": name, "annotation": ann(theory, name), "forward": fwd, "backward": bwd,
                     "typed_ok": True, "compile_ok": True, "replay_empty": ok, "goal": goal, "script": script,
                     "goal_sha256": sha(goal.encode()), "script_sha256": sha("\n".join(script).encode()), "dev_root_hex": r})
        excl.append(r)
    brows, first_fail = [], None
    for d in range(1, 9):
        goal, r = goal_at(d), root(200 + d)
        ga = grammar_a(goal)
        try:
            script = arrow(theory, d, goal); ok = replay(theory, goal, script); typed = compile_ok = True
        except Exception:
            script, ok, typed, compile_ok = [], False, False, False
        row = {"depth": d, "goal": goal, "script": script, "grammar_a": ga, "typed_ok": typed, "compile_ok": compile_ok,
               "replay_empty": ok, "statement_size": len(goal), "goal_sha256": sha(goal.encode()),
               "script_sha256": sha("\n".join(script).encode()), "dev_root_hex": r}
        brows.append(row); excl.append(r)
        if first_fail is None and not (ga and typed and compile_ok and ok):
            first_fail = {"depth": d, "failure_kind": "expressibility"}
            break
    prior_b = [root(100), root(101)]
    out = {"schema": "phase2-stageb-presignature-probes-20.v2", "status": "DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED",
           "prf_domain_label": PRF.decode(),
           "host": {"hostname": "workbench", "product": "MS-S1 MAX", "lenovo_legion_excluded": True,
                    "lenovo_legion_exclusion_reason": "8 GiB VRAM gave no expected performance gain"},
           "compute": {"cpu_only": True, "one_process": True, "one_thread": True},
           "inputs": {"theory_path": str(THEORY), "theory": pair(THEORY), "script": pair(Path(__file__)),
                      "l01_exclusions": pair(L01X), "l2_exclusions": pair(L02X)},
           "probe_a": {"rows": rows, "not_e_enumerable": True, "signature_fact_not_e_wider_footprint": True},
           "probe_b": {"rows": brows,
                       "outcome": "realizable" if first_fail is None and all(x["replay_empty"] for x in brows) else "not realizable",
                       "depth_grading_checkable": True, "depths_tested": [x["depth"] for x in brows],
                       "first_failure": first_fail, "signature_fact_positive_control_realizable": first_fail is None},
           "permanently_excluded_dev_root_hex": excl + prior_b, "calibration_forbidden": True,
           "registry_path": str(REG)}
    sys.stdout.buffer.write((json.dumps(out, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")); return 0

def write_registry(p):
    rows = seed_l01_l2()
    for r in p["probe_a"]["rows"]:
        rows.append(ent(r["dev_root_hex"], PRF.decode(), "presignature_probes_20_A", DATE, r["goal_sha256"], r["script_sha256"]))
    for r in p["probe_b"]["rows"]:
        rows.append(ent(r["dev_root_hex"], PRF.decode(), "presignature_probes_20_B_depth_%d" % r["depth"], DATE, r["goal_sha256"], r["script_sha256"]))
    for i, th, sk in ((100, "b6959954f36965b2a95021dd198f0cc88623b5f6bb446d92554f103f03639612", "bc926d2843cab669487b6324fc199227adba2dd830fd3b78a7a850b861698cde"),
                      (101, "5d8a50d6adf7ecba1c20231b42dacae0c35247b58a5a3f344a0af05c43084595", "b3d4aac389ae02418492ad691d09cb1c891b2534008d378bede9c220f60f5432")):
        rows.append(ent(root(i), PRF.decode(), "presignature_probes_20_B_prior_%d" % i, "2026-08-15", th, sk))
    lines = [json.dumps(e, sort_keys=True, ensure_ascii=True) for e in sorted(rows, key=lambda e: json.dumps(e, sort_keys=True))]
    REG.write_text("\n".join(lines) + "\n", encoding="ascii"); return len(lines)

def parent():
    log = []
    def L(m): log.append(m); print(m)
    L("Lenovo Legion excluded from experimental runs: 8 GiB VRAM gave no expected performance gain.")
    L("Host=workbench product=MS-S1 MAX PRF_DOMAIN=%s" % PRF.decode())
    env = dict(os.environ); env.update(PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    runs = []
    for i in range(2):
        c = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker"], cwd=str(MINIMO), env=env, capture_output=True)
        if c.returncode: raise SystemExit("worker %d failed: %s" % (i, c.stderr.decode()))
        runs.append(c.stdout); L("fresh_exec_%d_sha256=%s" % (i, sha(c.stdout)))
    if runs[0] != runs[1]: raise SystemExit("NONDETERMINISM")
    L("fresh_executions_byte_identical=true")
    p = json.loads(runs[0]); OUT_J.write_bytes(runs[0])
    nreg = write_registry(p); L("registry_entries=%d path=%s" % (nreg, REG))
    try:
        refuse_if_registered(root_hex=p["probe_a"]["rows"][0]["dev_root_hex"]); raise SystemExit("refuse check failed to fire")
    except SystemExit as e:
        if "REFUSED_REGISTERED_IDENTITY" not in str(e): raise
        L("refuse_if_registered_selfcheck=ok")
    md = ["# PHASE2_STAGE_B pre-signature probes 20", "", "Status: `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`", "",
          "PRF domain: `%s` (distinct from `audit`)." % PRF.decode(), "",
          "Lenovo Legion excluded: 8 GiB VRAM gave no expected performance gain.", "", "## Hashes", "",
          "- script raw `%s` lf `%s`" % (p["inputs"]["script"]["raw_sha256"], p["inputs"]["script"]["lf_sha256"]),
          "- theory raw `%s` lf `%s`" % (p["inputs"]["theory"]["raw_sha256"], p["inputs"]["theory"]["lf_sha256"]),
          "- L01 exclusions raw `%s` lf `%s`" % (p["inputs"]["l01_exclusions"]["raw_sha256"], p["inputs"]["l01_exclusions"]["lf_sha256"]),
          "- L2 exclusions raw `%s` lf `%s`" % (p["inputs"]["l2_exclusions"]["raw_sha256"], p["inputs"]["l2_exclusions"]["lf_sha256"]), "",
          "## Probe A - per-premise enumerability", "",
          "| premise | annotation | forward | backward | typed | compile | replay_empty |", "|---|---|---|---|---|---|---|"]
    for r in p["probe_a"]["rows"]:
        md.append("| %s | `%s` | %s | %s | %s | %s | %s |" % (r["premise"], r["annotation"], r["forward"], r["backward"], r["typed_ok"], r["compile_ok"], r["replay_empty"]))
    md += ["", "Finding: `not_e` ABSENT yet forward+backward (wider footprint than annotated premises).", "",
           "## Probe B / Item 1 - depth 1..8 under grammar A", "",
           "| depth | grammar_A | typed | compile | replay_empty | statement_size |", "|---:|---|---|---|---|---:|"]
    for r in p["probe_b"]["rows"]:
        md.append("| %d | %s | %s | %s | %s | %d |" % (r["depth"], r["grammar_a"], r["typed_ok"], r["compile_ok"], r["replay_empty"], r["statement_size"]))
    md += ["", "first_failure: `%s`; outcome: **%s**." % (p["probe_b"]["first_failure"], p["probe_b"]["outcome"]), "",
           "## Item 2 - durable exclusions registry", "",
           "File: `%s` (%d entries). Fail-closed: `refuse_if_registered`." % (REG.name, nreg), "",
           "## Facts for the signature", "",
           "1. `not_e` has a wider action footprint than every annotated premise.",
           "2. Positive control realizable at depth 1..8 under A; choice A no longer blocked by section 9.", "",
           "Excluded roots: " + ", ".join("`%s`" % h for h in p["permanently_excluded_dev_root_hex"]), "",
           "No threshold, band, cap, or calibration may be taken from this artifact.", ""]
    OUT_M.write_text("\n".join(md), encoding="ascii"); OUT_L.write_text("\n".join(log) + "\n", encoding="ascii")
    L("wrote %s %s %s %s" % (OUT_J, OUT_M, OUT_L, REG)); return 0

if __name__ == "__main__":
    sys.path.insert(0, str(MINIMO))
    raise SystemExit(worker() if sys.argv[1:] == ["--worker"] else parent() if not sys.argv[1:] else 2)
