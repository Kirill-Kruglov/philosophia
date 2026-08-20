#!/usr/bin/env python3
"""PHASE1_18 Part B analysis (amendment 5). Structural gate only; pin equality reported."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path

DEV = Path(__file__).resolve().parent
OUT = DEV / "phase1_18_part_b"
RES = DEV / "phase1_18_part_b_results.json"
MD = DEV / "PHASE1_18_PART_B.md"
GATE_OK = OUT / "OMP1_GATE_OK"
CKPT_DIR = Path("/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33")
PRE_PATCH_SHA = "66ffb139374696cc51b55fe1e5b88c6bf2243b0911b32b83cc084b178de2bf4e"
KLEENE_SET = {
    "kleene_1", "kleene_2", "kleene_3", "kleene_4", "kleene_5", "kleene_6", "kleene_7",
    "kleene_8a", "kleene_8b", "kleene_9a", "kleene_9b", "kleene_10a", "kleene_10b",
    "kleene_11", "kleene_12", "kleene_13", "kleene_14", "kleene_15", "kleene_16",
    "kleene_17a", "kleene_17b", "kleene_18a", "kleene_18b", "kleene_19", "kleene_20",
    "kleene_21", "kleene_22", "kleene_23", "kleene_24", "kleene_25",
}
HIST = {
    "16c": {1: DEV / "phase1_extrinsic_16c/checkpoint_1.json",
            2: DEV / "phase1_extrinsic_16c/checkpoint_2.json",
            3: DEV / "phase1_extrinsic_16c/checkpoint_3.json"},
    "17": {i: DEV / ("phase1_extrinsic_17/checkpoint_%d.json" % i) for i in range(5)},
}
# PHASE1_17 pins: OMP=16 reference. Reported as configuration sensitivity, never gated.
PIN = {
    0: ["kleene_1", "kleene_10a", "kleene_10b", "kleene_11", "kleene_16", "kleene_17a",
        "kleene_17b", "kleene_18a", "kleene_18b", "kleene_19", "kleene_20"],
    1: ["kleene_1", "kleene_2", "kleene_3", "kleene_4", "kleene_5", "kleene_6", "kleene_7",
        "kleene_8b", "kleene_10a", "kleene_10b", "kleene_11", "kleene_13", "kleene_16",
        "kleene_17a", "kleene_17b", "kleene_18a", "kleene_18b", "kleene_19", "kleene_20"],
    4: ["kleene_1", "kleene_3", "kleene_6", "kleene_7", "kleene_10a", "kleene_10b",
        "kleene_11", "kleene_16", "kleene_17a", "kleene_17b", "kleene_18a", "kleene_18b",
        "kleene_19"],
}
PIN[2] = list(PIN[0]); PIN[3] = list(PIN[0])

INSTRUMENTATION_CHECK = {
    "class": "VERIFIED_BY_CODE_READ",
    "claim": "mcts_expansions accumulates n_entered and is written to JSON only; "
             "it is not read by tree policy or action selection",
    "file": "/home/master/llm_projects/minimo/learning/proofsearch.py",
    "lines": {
        "n_entered_accumulate": 825,
        "evaluate_return_n_entered": 863,
        "proof_search_add": 1006,
        "record_write": 1375,
    },
}


class Refuse(RuntimeError):
    pass


def sha(b): return hashlib.sha256(b).hexdigest()
def pair(p: Path):
    r = p.read_bytes()
    return {"path": str(p), "nbytes": len(r), "raw_sha256": sha(r),
            "lf_sha256": sha(r.replace(b"\r\n", b"\n").replace(b"\r", b"\n")),
            "field_provenance": {"class": "MEASURED_IN_PROCESS"}}


def require_search_cost(records, path):
    if not records:
        raise Refuse("%s: empty records" % path)
    for i, rec in enumerate(records):
        if "mcts_expansions" not in rec:
            raise Refuse("%s record %d missing mcts_expansions; elapsed_s refused" % (path, i))
        v = rec["mcts_expansions"]
        if isinstance(v, bool) or not isinstance(v, int) or v < 0:
            raise Refuse("%s record %d mcts_expansions malformed: %r" % (path, i, v))


def field_class(payload: dict, name: str, default: str = "UNKNOWN") -> str:
    fp = payload.get("field_provenance") or {}
    meta = fp.get(name) or {}
    return meta.get("class", default)


def load_stamped(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="ascii"))
    require_search_cost(payload.get("records") or [], path)
    if "omp_num_threads" not in payload:
        raise Refuse("%s: omp_num_threads unrecorded; not comparable" % path)
    solved = [r["problem"] for r in payload["records"] if r["success"]]
    exp = {r["problem"]: r["mcts_expansions"] for r in payload["records"]}
    return {
        "payload": payload, "solved": set(solved), "exp": exp, "path": path,
        "omp_num_threads": payload["omp_num_threads"],
        "omp_class": field_class(payload, "omp_num_threads", "MEASURED_IN_PROCESS"),
        "torch_are_deterministic_algorithms_enabled":
            payload.get("torch_are_deterministic_algorithms_enabled"),
        "torch_class": field_class(payload, "torch_are_deterministic_algorithms_enabled"),
        "proofsearch_py_sha256": payload.get("proofsearch_py_sha256"),
        "binary_class": field_class(payload, "proofsearch_py_sha256"),
        "host_load": payload.get("host_load"),
        "canonical": payload.get("canonical_for_homogeneous_omp1_arm"),
        "omp1_arm_role": payload.get("omp1_arm_role"),
        "agent_path": payload.get("agent_path"),
    }


def load_historical(path: Path, label: str) -> dict:
    payload = json.loads(path.read_text(encoding="ascii"))
    records = payload.get("records") or []
    has_exp = all("mcts_expansions" in r for r in records)
    if has_exp:
        require_search_cost(records, path)
    solved = [r["problem"] for r in records if r["success"]]
    exp = {r["problem"]: r.get("mcts_expansions") for r in records} if has_exp else None
    return {
        "payload": payload, "solved": set(solved), "exp": exp, "path": path,
        "omp_num_threads": 16,
        "omp_class": "INFERRED",
        "omp_inference_basis": "INFERRED_FROM_RUN_SCRIPT",
        "historical_label": label, "has_mcts_expansions": has_exp,
    }


def compare_sets(a: dict, b: dict, a_name: str, b_name: str) -> dict:
    """Symmetric difference with provenance classes travelling into the comparison."""
    return {
        "a": a_name, "b": b_name,
        "a_omp_class": a.get("omp_class"), "b_omp_class": b.get("omp_class"),
        "a_binary_sha": a.get("proofsearch_py_sha256"),
        "b_binary_sha": b.get("proofsearch_py_sha256"),
        "a_binary_class": a.get("binary_class"), "b_binary_class": b.get("binary_class"),
        "symmetric_difference": sorted(a["solved"] ^ b["solved"]),
        "identical_sets": a["solved"] == b["solved"],
        "field_provenance": {
            "class": "DERIVED",
            "inputs": ["%s.solved" % a_name, "%s.solved" % b_name],
            "classes_in_comparison": [a.get("omp_class"), b.get("omp_class")],
            "note": (
                "INFERRED side present; class travels into any statement from this comparison"
                if "INFERRED" in (a.get("omp_class"), b.get("omp_class")) else None
            ),
        },
    }


def structural_defects_omp1(ck: int, obj: dict) -> list:
    """Amendment 5: only these stop the run. No threshold on set difference."""
    defects = []
    path, payload = obj["path"], obj["payload"]
    records = payload.get("records") or []
    if len(records) != 30:
        defects.append({"checkpoint": "ck%d" % ck, "defect": "record_count",
                        "got": len(records), "expected": 30, "path": str(path)})
    names = [r.get("problem") for r in records]
    if any(n is None for n in names) or set(names) != KLEENE_SET:
        defects.append({"checkpoint": "ck%d" % ck, "defect": "problem_name_set_not_kleene",
                        "got": sorted(n for n in names if n), "path": str(path)})
    for i, rec in enumerate(records):
        if "mcts_expansions" not in rec:
            defects.append({"checkpoint": "ck%d" % ck, "defect": "mcts_expansions_absent",
                            "record": i, "path": str(path)})
            break
    omp = payload.get("omp_num_threads")
    if omp is None or omp != 1:
        defects.append({"checkpoint": "ck%d" % ck, "defect": "omp_num_threads",
                        "got": omp, "expected": 1, "path": str(path)})
    if len(obj["solved"]) == 0:
        defects.append({"checkpoint": "ck%d" % ck, "defect": "zero_theorems_solved",
                        "path": str(path)})
    expected_agent = str(CKPT_DIR / ("%d.pt" % ck))
    got_agent = str(payload.get("agent_path") or "")
    if Path(got_agent).resolve() != Path(expected_agent).resolve():
        defects.append({"checkpoint": "ck%d" % ck, "defect": "agent_path_mismatch",
                        "got": got_agent, "expected": expected_agent, "path": str(path)})
    return defects


def pin_report(omp1: dict) -> dict:
    """PHASE1_17 pin equality: configuration sensitivity, reported not gated."""
    rows = []
    for ck in range(5):
        got, pin = omp1[ck]["solved"], set(PIN[ck])
        rows.append({
            "checkpoint": "ck%d" % ck,
            "identical_to_phase1_17_pin": got == pin,
            "n_solved": len(got),
            "n_pin": len(pin),
            "symmetric_difference": sorted(got ^ pin),
            "only_got": sorted(got - pin),
            "only_pin": sorted(pin - got),
            "pin_omp_class": "INFERRED",
            "pin_basis": "PHASE1_17 pins produced at OMP=16; not a same-config reference",
            "omp1_omp_class": omp1[ck]["omp_class"],
            "field_provenance": {
                "class": "DERIVED",
                "inputs": ["omp1.solved", "PHASE1_17.pin"],
                "classes_in_comparison": [omp1[ck]["omp_class"], "INFERRED"],
            },
        })
    return {
        "role": "configuration_sensitivity_vs_phase1_17_pins",
        "gated": False,
        "note": "Set equality against OMP=16 pins is reported, never a stop condition "
                "(amendment 5). Thread interleaving can produce differences.",
        "per_checkpoint": rows,
    }


def median(xs):
    ys = sorted(xs); n = len(ys)
    if not n: return None
    return ys[n // 2] if n % 2 else 0.5 * (ys[n // 2 - 1] + ys[n // 2])


def iqr(xs):
    ys = sorted(xs); n = len(ys)
    if n < 2: return [None, None]
    def q(p):
        i = (n - 1) * p; lo = int(math.floor(i)); hi = int(math.ceil(i))
        return ys[lo] if lo == hi else ys[lo] * (hi - i) + ys[hi] * (i - lo)
    return [q(0.25), q(0.75)]


def paired(a_exp, b_exp, both):
    rows = [{"theorem": t, "a": a_exp[t], "b": b_exp[t],
             "ratio": (b_exp[t] / a_exp[t]) if a_exp[t] else None} for t in both]
    ratios = [r["ratio"] for r in rows if r["ratio"] is not None]
    return {"n": len(both), "per_theorem": rows,
            "cheaper": sum(1 for r in rows if r["b"] < r["a"]),
            "costlier": sum(1 for r in rows if r["b"] > r["a"]),
            "identical": sum(1 for r in rows if r["b"] == r["a"]),
            "median_ratio": median(ratios), "iqr_ratio": iqr(ratios),
            "field_provenance": {"class": "DERIVED", "inputs": ["mcts_expansions"]}}


def find_prepatch_ck0() -> Path:
    for name in ("checkpoint_0_omp1_PRE_PATCH.json",
                 "checkpoint_0_omp1_bin_%s.json" % PRE_PATCH_SHA[:16]):
        p = OUT / name
        if p.exists():
            return p
    raise Refuse("missing pre-patch ck0 object (expected PRE_PATCH or bin_%s)" % PRE_PATCH_SHA[:16])


def analyze(gate_omp1_only: bool) -> int:
    omp1 = {}
    for ck in range(5):
        path = OUT / ("checkpoint_%d_omp1.json" % ck)
        if not path.exists():
            payload = {"schema": "phase1-18-part-b-am5.v1",
                       "status": "INSTRUMENT_DEFECT__STRUCTURAL",
                       "structural_defects": [{"checkpoint": "ck%d" % ck,
                                               "defect": "missing_results_object",
                                               "path": str(path)}],
                       "part_b_stopped": True}
            RES.write_bytes((json.dumps(payload, sort_keys=True) + "\n").encode("ascii"))
            print("STOP: STRUCTURAL_DEFECT", json.dumps(payload["structural_defects"]))
            return 2
        try:
            omp1[ck] = load_stamped(path)
        except (Refuse, OSError, json.JSONDecodeError) as exc:
            payload = {"schema": "phase1-18-part-b-am5.v1",
                       "status": "INSTRUMENT_DEFECT__STRUCTURAL",
                       "structural_defects": [{"checkpoint": "ck%d" % ck,
                                               "defect": "unreadable_or_schema",
                                               "error": str(exc), "path": str(path)}],
                       "part_b_stopped": True}
            RES.write_bytes((json.dumps(payload, sort_keys=True) + "\n").encode("ascii"))
            print("STOP: STRUCTURAL_DEFECT", json.dumps(payload["structural_defects"]))
            return 2

    defects = []
    for ck in range(5):
        defects.extend(structural_defects_omp1(ck, omp1[ck]))
    pins = pin_report(omp1)

    if defects:
        payload = {"schema": "phase1-18-part-b-am5.v1",
                   "status": "INSTRUMENT_DEFECT__STRUCTURAL",
                   "structural_defects": defects,
                   "omp1_vs_phase1_17_pins": pins,
                   "part_b_stopped": True}
        RES.write_bytes((json.dumps(payload, sort_keys=True) + "\n").encode("ascii"))
        print("STOP: STRUCTURAL_DEFECT", json.dumps(defects))
        return 2

    if gate_omp1_only:
        # D3: write marker before print. Pin equality is reported, not required.
        gate_note = OUT / "OMP1_GATE_PIN_REPORT.json"
        gate_note.write_text(json.dumps(pins, indent=2, sort_keys=True) + "\n", encoding="ascii")
        GATE_OK.write_text("ok\n", encoding="ascii")
        n_diff = sum(1 for r in pins["per_checkpoint"] if not r["identical_to_phase1_17_pin"])
        print("STRUCTURAL_GATE_OK; omp1_vs_phase1_17_pins reported (%d/5 differ); "
              "proceeding to amendment-5 arms (ck0 re-run + ck1 det + OMP16 floor)."
              % n_diff)
        return 0

    if omp1[0].get("canonical") is False or omp1[0].get("omp1_arm_role") == "PRE_PATCH_REPORTED_ALONGSIDE":
        raise Refuse("checkpoint_0_omp1.json is still pre-patch; canonical re-run missing")
    pre_ck0 = load_stamped(find_prepatch_ck0())
    ck0_binary_pair = compare_sets(pre_ck0, omp1[0], "ck0_pre_patch", "ck0_canonical_post_patch")
    ck0_disagree = not ck0_binary_pair["identical_sets"]
    ck0_binary_pair.update({
        "role": "determinism_across_binary_change",
        "pre_patch_sha": pre_ck0["proofsearch_py_sha256"],
        "post_patch_sha": omp1[0]["proofsearch_py_sha256"],
        "pre_patch_path": str(pre_ck0["path"]),
        "canonical_path": str(omp1[0]["path"]),
        "patch_inert_if_sets_agree": ck0_binary_pair["identical_sets"],
        "on_disagree": "RECORD_AND_CONTINUE",
        "ambiguity_if_disagree": [
            "D1 patch not inert (changed search behaviour)",
            "OMP=1 not deterministic",
        ],
        "resolution": "ck1 OMP=1 same-binary repeat separates the two causes",
    })
    if ck0_disagree:
        ck0_binary_pair["hard_consequence"] = (
            "Central finding that ck2 and ck3 solve exactly ck0's identities was "
            "stated against pre-patch ck0 while ck2/ck3 are post-patch. If ck0 is "
            "binary-sensitive, that identity claim is not established and must be "
            "restated against a homogeneous arm before it appears in any document."
        )
        print("Q1: ck0 pre-patch != post-patch; recorded; continuing "
              "(ck1 same-binary repeat resolves patch vs determinism).")

    rep1 = load_stamped(OUT / "checkpoint_1_omp1_rep1.json")
    det_cmp = compare_sets(omp1[1], rep1, "omp1_ck1", "omp1_ck1_rep1")
    identical = det_cmp["identical_sets"]
    det = {
        "checkpoint": "ck1",
        "role": "positive_control_on_omp1_determinism_assumption",
        "expected": "identical",
        "comparison": det_cmp,
        "on_mismatch": "RECORD_AND_CONTINUE_TO_NOISE_FLOOR",
        "determinism_assumption_falsified": (not identical),
        "torch_are_deterministic_algorithms_enabled_omp1_ck1":
            omp1[1]["torch_are_deterministic_algorithms_enabled"],
        "torch_class_omp1_ck1": omp1[1]["torch_class"],
        "torch_are_deterministic_algorithms_enabled_omp1_ck1_rep1":
            rep1["torch_are_deterministic_algorithms_enabled"],
        "torch_class_omp1_ck1_rep1": rep1["torch_class"],
    }
    if ck0_disagree:
        if identical:
            det["resolves_ck0_binary_disagreement"] = (
                "ck1 same-binary repeat identical => OMP=1 deterministic under "
                "patched binary; ck0 disagreement is the patch"
            )
        else:
            det["resolves_ck0_binary_disagreement"] = (
                "ck1 same-binary repeat also differs => determinism assumption false; "
                "patch question moot"
            )
    if not identical:
        det["consequences"] = {
            "1": "OMP=1 stops being the canonical instrument; it is one configuration "
                 "among others. Later documents must not call it canonical.",
            "2": "Multi-seed sizing needs a noise floor at OMP=1 by the same repeat "
                 "construction before it can be sized.",
        }
        print("Q1: OMP=1 ck1 repeat != OMP=1 ck1; recorded; continuing to noise floor.")

    floor_runs = [load_stamped(OUT / ("checkpoint_1_omp16_rep%d.json" % i)) for i in (1, 2, 3)]
    pairwise = []
    fresh_union = set()
    for i in range(3):
        for j in range(i + 1, 3):
            cmp = compare_sets(floor_runs[i], floor_runs[j],
                               "omp16_rep%d" % (i + 1), "omp16_rep%d" % (j + 1))
            fresh_union |= set(cmp["symmetric_difference"])
            pairwise.append(cmp)
    h16c = load_historical(HIST["16c"][1], "16c")
    h17 = load_historical(HIST["17"][1], "17")
    hist_cmp = compare_sets(h16c, h17, "16c_ck1", "17_ck1")
    hist_union = set(hist_cmp["symmetric_difference"])
    total_union = fresh_union | hist_union
    host_loads = []
    any_not_idle = False
    for i, fr in enumerate(floor_runs, 1):
        hl = fr.get("host_load")
        host_loads.append({"run": "omp16_rep%d" % i, "host_load": hl})
        if hl is not None and hl.get("host_otherwise_idle") is False:
            any_not_idle = True

    noise_floor = {
        "checkpoint": "ck1",
        "role": "noise_floor_at_omp16",
        "sizing_rule": "NEVER_SIZE_MULTI_SEED_AGAINST_FRESH_FLOOR_ALONE",
        "fresh_floor": {
            "bound_on": "lower_bound_most_favourable_back_to_back_same_host_state_same_seed_same_binary",
            "repeats": 3,
            "pairwise_symmetric_differences": pairwise,
            "union_theorems_that_ever_flip": sorted(fresh_union),
            "host_load_per_repeat": host_loads,
            "host_otherwise_idle_all_repeats": (not any_not_idle),
            "host_otherwise_idle_provenance": {
                "class": "DERIVED",
                "inputs": ["host_load.series.other_phase_jobs"],
                "rule": "false if any periodic/endpoint sample saw other_phase_jobs",
            },
            "host_not_idle_note": (
                None if not any_not_idle else
                "At least one fresh repeat saw other Phase-1/2 jobs in the series; "
                "do not average that away. Fresh floor remains a lower bound."
            ),
        },
        "historical_pair": {
            "bound_on": "realistic_days_apart_host_state_and_binary_differ_inferred_thread_config",
            "comparison": hist_cmp,
            "kleene_12_in_scope": True,
            "kleene_12_in_difference": ("kleene_12" in hist_union),
            "instrumentation_enters_search_decision": INSTRUMENTATION_CHECK,
            "confounds": [
                "thread_config class=INFERRED (basis INFERRED_FROM_RUN_SCRIPT)",
                "instrumentation difference (mcts_expansions) present in 17; "
                "VERIFIED_BY_CODE_READ not to enter search decisions",
            ],
        },
        "total_union": {
            "bound_on": "union_of_fresh_lower_bound_and_historical_realistic_pair",
            "union_theorems_that_ever_flip": sorted(total_union),
            "use_for_multi_seed_sizing": True,
            "field_provenance": {
                "class": "DERIVED",
                "inputs": ["fresh_floor.union", "historical_pair.comparison.symmetric_difference"],
                "classes_in_comparison": ["MEASURED_IN_PROCESS", "INFERRED"],
            },
        },
        "solved_sets": {"omp16_rep%d" % (i + 1): sorted(floor_runs[i]["solved"]) for i in range(3)},
    }

    config_sens = []
    for ck in range(5):
        row = {"checkpoint": "ck%d" % ck, "omp1_recorded": sorted(omp1[ck]["solved"]),
               "omp1_omp_class": omp1[ck]["omp_class"],
               "omp1_binary_sha": omp1[ck]["proofsearch_py_sha256"],
               "comparisons": []}
        if ck in HIST["16c"]:
            h = load_historical(HIST["16c"][ck], "16c")
            row["comparisons"].append(compare_sets(omp1[ck], h, "omp1_ck%d" % ck, "16c"))
        h = load_historical(HIST["17"][ck], "17")
        row["comparisons"].append(compare_sets(omp1[ck], h, "omp1_ck%d" % ck, "17"))
        if ck == 1:
            for i, fr in enumerate(floor_runs, 1):
                row["comparisons"].append(
                    compare_sets(omp1[ck], fr, "omp1_ck1", "omp16_rep%d" % i))
        config_sens.append(row)

    identity = {
        "role": "ck2_ck3_vs_ck0_solved_set_identity",
        "arm": "canonical_post_patch_omp1",
        "ck0_sha": omp1[0]["proofsearch_py_sha256"],
        "ck2_equals_ck0": omp1[2]["solved"] == omp1[0]["solved"],
        "ck3_equals_ck0": omp1[3]["solved"] == omp1[0]["solved"],
        "ck2_symdiff_ck0": sorted(omp1[2]["solved"] ^ omp1[0]["solved"]),
        "ck3_symdiff_ck0": sorted(omp1[3]["solved"] ^ omp1[0]["solved"]),
        "pre_patch_identity_not_established_if_ck0_binary_sensitive": ck0_disagree,
        "field_provenance": {"class": "DERIVED", "inputs": ["omp1.solved"]},
    }

    pairs = []
    for i in range(5):
        for j in range(5):
            if i == j: continue
            both = sorted(omp1[i]["solved"] & omp1[j]["solved"])
            pairs.append({"a": "ck%d" % i, "b": "ck%d" % j,
                          "a_binary_sha": omp1[i]["proofsearch_py_sha256"],
                          "b_binary_sha": omp1[j]["proofsearch_py_sha256"],
                          "omp1": paired(omp1[i]["exp"], omp1[j]["exp"], both)})

    omp1_role = (
        "one_configuration_among_others__determinism_falsified"
        if not identical else
        "intended_instrument_pending_no_contradiction"
    )

    inputs = [pair(Path(__file__)), pair(DEV / "run_phase1_18_part_b_am2.sh"),
              pair(DEV / "phase1_18_stamp_threads.py"),
              pair(DEV / "phase1_18_host_monitor.py"),
              pair(DEV / "STANDING_RULES.md")]
    for ck in range(5):
        inputs.append(pair(OUT / ("checkpoint_%d_omp1.json" % ck)))
    inputs.append(pair(pre_ck0["path"]))
    inputs.append(pair(OUT / "checkpoint_1_omp1_rep1.json"))
    for i in (1, 2, 3):
        inputs.append(pair(OUT / ("checkpoint_1_omp16_rep%d.json" % i)))

    payload = {
        "schema": "phase1-18-part-b-am5.v1",
        "status": "PART_B_AUTHORIZED_AS_AMENDED__NO_SEED_SPEND",
        "standing_rules": str(DEV / "STANDING_RULES.md"),
        "standing_rule_provenance_classes": [
            "MEASURED_IN_PROCESS", "VERIFIED_BY_CODE_READ", "DERIVED", "INFERRED",
        ],
        "omp1_role": omp1_role,
        "full_omp16_five_checkpoint_arm": "CUT",
        "schema_guard": "search_cost requires mcts_expansions on every record; elapsed_s refused",
        "structural_gate": "passed",
        "omp1_vs_phase1_17_pins": pins,
        "ck0_across_binary_change": ck0_binary_pair,
        "homogeneous_identity_ck2_ck3_vs_ck0": identity,
        "determinism_positive_control": det,
        "noise_floor": noise_floor,
        "configuration_sensitivity": config_sens,
        "paired_cost_omp1": pairs,
        "inputs": inputs,
        "calibration_forbidden": True,
        "no_hypothesis_test": True,
        "multi_seed_unauthorized_until_noise_floor": True,
        "omp1_noise_floor_also_required_if_determinism_falsified": (not identical),
    }
    RES.write_bytes((json.dumps(payload, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii"))
    write_md(payload)
    print("wrote %s %s" % (RES, MD))
    return 0


def write_md(p: dict) -> None:
    d, n = p["determinism_positive_control"], p["noise_floor"]
    fresh, hist, total = n["fresh_floor"], n["historical_pair"], n["total_union"]
    ck0 = p["ck0_across_binary_change"]
    pins = p["omp1_vs_phase1_17_pins"]
    ident = p["homogeneous_identity_ck2_ck3_vs_ck0"]
    lines = [
        "# PHASE1_18 Part B (amendment 5)", "",
        "Status: `PART_B_AUTHORIZED_AS_AMENDED__NO_SEED_SPEND`", "",
        "Full five-checkpoint OMP=16 arm: **CUT**.", "",
        "OMP=1 role: `%s`" % p["omp1_role"], "",
        "Standing rules: `%s`" % p["standing_rules"], "",
        "Structural gate: passed. Pin equality vs PHASE1_17 is reported, not gated.", "",
        "## 0. OMP=1 vs PHASE1_17 pins (configuration sensitivity; not a gate)", "",
    ]
    for row in pins["per_checkpoint"]:
        lines.append("- %s identical=%s symdiff=%s" % (
            row["checkpoint"], row["identical_to_phase1_17_pin"],
            ", ".join(row["symmetric_difference"]) or "(empty)"))
    lines += [
        "", "## 1. ck0 across binary change (pre-patch vs canonical post-patch)", "",
        "- pre_patch_sha: `%s` [%s]" % (ck0["pre_patch_sha"], ck0["a_binary_class"]),
        "- post_patch_sha: `%s` [%s]" % (ck0["post_patch_sha"], ck0["b_binary_class"]),
        "- identical_sets: `%s`" % ck0["identical_sets"],
        "- symmetric_difference: %s" % (", ".join(ck0["symmetric_difference"]) or "(empty)"),
        "- on_disagree: record and continue; ck1 same-binary repeat resolves causes",
        "",
    ]
    if ck0.get("hard_consequence"):
        lines += ["Hard consequence:", ck0["hard_consequence"], ""]
    lines += [
        "## 2. Homogeneous identity (ck2/ck3 vs canonical ck0)", "",
        "- ck2_equals_ck0: `%s`" % ident["ck2_equals_ck0"],
        "- ck3_equals_ck0: `%s`" % ident["ck3_equals_ck0"],
        "- pre_patch_identity_not_established_if_ck0_binary_sensitive: `%s`" % (
            ident["pre_patch_identity_not_established_if_ck0_binary_sensitive"]),
        "",
        "## 3. Determinism control (OMP=1 ck1 repeat)", "",
        "- expected: identical",
        "- identical_sets: `%s`" % d["comparison"]["identical_sets"],
        "- symmetric_difference: %s" % (
            ", ".join(d["comparison"]["symmetric_difference"]) or "(empty)"),
        "- on_mismatch: record and continue to noise floor",
    ]
    if d.get("resolves_ck0_binary_disagreement"):
        lines.append("- resolves ck0 binary disagreement: %s" % d["resolves_ck0_binary_disagreement"])
    if d.get("determinism_assumption_falsified"):
        lines += [
            "", "Determinism assumption falsified. Consequences:",
            "1. OMP=1 is no longer the canonical instrument.",
            "2. Multi-seed needs an OMP=1 noise floor by the same repeat construction.",
            "",
        ]
    lines += [
        "", "## 4. Noise floor (size against the union)", "",
        "Never size the multi-seed run against the fresh floor alone.", "",
        "### Fresh floor (lower bound)", "",
        "- bound on: %s" % fresh["bound_on"],
        "- union flip: %s" % (", ".join(fresh["union_theorems_that_ever_flip"]) or "(empty)"),
        "- host_otherwise_idle_all_repeats: `%s` [%s]" % (
            fresh["host_otherwise_idle_all_repeats"],
            fresh["host_otherwise_idle_provenance"]["class"]),
    ]
    if fresh.get("host_not_idle_note"):
        lines.append("- note: %s" % fresh["host_not_idle_note"])
    for row in fresh["pairwise_symmetric_differences"]:
        lines.append("- %s vs %s: %s" % (
            row["a"], row["b"], ", ".join(row["symmetric_difference"]) or "(empty)"))
    for hl in fresh["host_load_per_repeat"]:
        h = hl["host_load"] or {}
        lines.append(
            "- %s wall_s=%s idle=%s n_periodic=%s max_load1=%s" % (
                hl["run"], h.get("wall_s"), h.get("host_otherwise_idle"),
                h.get("n_periodic_samples"), h.get("max_loadavg_1")))
    hc = hist["comparison"]
    lines += [
        "", "### Historical pair 16C vs 17 (realistic)", "",
        "- bound on: %s" % hist["bound_on"],
        "- omp classes: `%s` / `%s`" % (hc["a_omp_class"], hc["b_omp_class"]),
        "- symmetric_difference: %s" % (", ".join(hc["symmetric_difference"]) or "(empty)"),
        "- kleene_12 in scope / in difference: `%s` / `%s`" % (
            hist["kleene_12_in_scope"], hist["kleene_12_in_difference"]),
        "", "### Total union (use for multi-seed sizing)", "",
        "- bound on: %s" % total["bound_on"],
        "- union: %s" % (", ".join(total["union_theorems_that_ever_flip"]) or "(empty)"),
        "", "## 5. Configuration sensitivity", "",
    ]
    for row in p["configuration_sensitivity"]:
        lines.append("### %s [omp_class=%s sha=%s]" % (
            row["checkpoint"], row["omp1_omp_class"], (row["omp1_binary_sha"] or "")[:16]))
        for c in row["comparisons"]:
            lines.append("- vs %s [omp %s/%s]: %s" % (
                c["b"], c["a_omp_class"], c["b_omp_class"],
                ", ".join(c["symmetric_difference"]) or "(empty)"))
    lines += ["", "## 6. Paired cost (OMP=1 five-ck, canonical homogeneous arm)", "",
              "| a | b | n | cheaper/costlier/identical | median ratio | IQR |",
              "|---|---|---:|---|---:|---|"]
    for row in p["paired_cost_omp1"]:
        a = row["omp1"]
        lines.append("| %s | %s | %d | %d/%d/%d | %s | %s |" % (
            row["a"], row["b"], a["n"], a["cheaper"], a["costlier"], a["identical"],
            a["median_ratio"], a["iqr_ratio"]))
    lines += ["", "## Hashes", ""]
    for h in p["inputs"]:
        lines.append("- `%s` raw `%s` lf `%s`" % (h["path"], h["raw_sha256"], h["lf_sha256"]))
    lines += ["", "No verdict token. Multi-seed unauthorized until noise floor exists.",
              "Last amendment before this report.", ""]
    MD.write_text("\n".join(lines), encoding="ascii")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate-omp1-only", action="store_true")
    args = ap.parse_args()
    try:
        return analyze(args.gate_omp1_only)
    except Refuse as exc:
        sys.stderr.write("REFUSED: %s\n" % exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
