#!/usr/bin/env python3
"""Stamp / label Part B results JSON (amendment 4 provenance + binary identity)."""
from __future__ import annotations
import hashlib, json, os, shutil, sys
from pathlib import Path

KEYS = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
        "NUMEXPR_NUM_THREADS", "TORCH_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")

PRE_PATCH_SHA = "66ffb139374696cc51b55fe1e5b88c6bf2243b0911b32b83cc084b178de2bf4e"
PRE_PATCH_BASIS = (
    "eval process imported proofsearch before D1/am4 patch; "
    "sha256 recovered from git HEAD:learning/proofsearch.py "
    "(saved as phase1_18_part_b/proofsearch_pre_d1_patch.py)"
)


def prov_put(payload: dict, field: str, meta: dict) -> None:
    fp = payload.setdefault("field_provenance", {})
    fp[field] = meta


def main() -> int:
    path = Path(sys.argv[1])
    threads = int(sys.argv[2])
    sidecar_arg = sys.argv[3] if len(sys.argv) > 3 else "-"
    sidecar = Path(sidecar_arg) if sidecar_arg not in ("", "-") else None
    role = sys.argv[4] if len(sys.argv) > 4 else "default"
    payload = json.loads(path.read_text(encoding="ascii"))
    had_eval_torch = "torch_are_deterministic_algorithms_enabled" in payload
    had_eval_sha = "proofsearch_py_sha256" in payload
    # Auto-detect the in-flight pre-patch ck0 object (no eval-process stamps).
    if role == "default" and (not had_eval_torch) and (not had_eval_sha):
        role = "pre_patch_ck0"
    fp = payload.setdefault("field_provenance", {})

    # Threads: prefer eval-process measurement; else stamp from this environ (INFERRED).
    if "omp_num_threads" in payload and payload["omp_num_threads"] is not None:
        # already MEASURED_IN_PROCESS from proofsearch
        pass
    else:
        payload["omp_num_threads"] = threads
        prov_put(payload, "omp_num_threads", {
            "class": "INFERRED",
            "basis": "stamp process environ; eval did not record omp_num_threads",
        })
    if "thread_controls" not in payload:
        payload["thread_controls"] = {k: int(os.environ.get(k, threads)) for k in KEYS}
        prov_put(payload, "thread_controls", {
            "class": "INFERRED",
            "basis": "stamp process environ; eval did not record thread_controls",
        })

    # Torch determinism.
    if "torch_are_deterministic_algorithms_enabled" not in payload:
        payload["torch_are_deterministic_algorithms_enabled"] = None
        prov_put(payload, "torch_are_deterministic_algorithms_enabled", {
            "class": "INFERRED",
            "basis": "ABSENT_PRE_PATCH_EVAL; field not written by eval process",
        })
    elif "torch_are_deterministic_algorithms_enabled" not in fp:
        prov_put(payload, "torch_are_deterministic_algorithms_enabled", {
            "class": "MEASURED_IN_PROCESS",
        })

    # Binary identity.
    if "proofsearch_py_sha256" not in payload:
        if role == "pre_patch_ck0":
            payload["proofsearch_py_sha256"] = PRE_PATCH_SHA
            prov_put(payload, "proofsearch_py_sha256", {
                "class": "INFERRED",
                "basis": PRE_PATCH_BASIS,
            })
        else:
            # Hash current on-disk file — not what a pre-patch process loaded.
            cur = Path("/home/master/llm_projects/minimo/learning/proofsearch.py")
            payload["proofsearch_py_sha256"] = hashlib.sha256(cur.read_bytes()).hexdigest()
            prov_put(payload, "proofsearch_py_sha256", {
                "class": "INFERRED",
                "basis": "sha256 of on-disk proofsearch.py at stamp time; "
                         "eval did not record import-time hash",
            })
    elif "proofsearch_py_sha256" not in fp:
        prov_put(payload, "proofsearch_py_sha256", {
            "class": "MEASURED_IN_PROCESS",
            "basis": "sha256 of proofsearch.py bytes at module import",
        })

    if sidecar is not None and sidecar.exists():
        payload["host_load"] = json.loads(sidecar.read_text(encoding="ascii"))
        prov_put(payload, "host_load", {
            "class": "DERIVED",
            "inputs": ["host_load.start", "host_load.periodic_jsonl", "host_load.end"],
            "basis": "sidecar from phase1_18_host_monitor finalize",
        })

    bhash = payload["proofsearch_py_sha256"]
    short = bhash[:16]
    payload["binary_label"] = "bin_%s" % short
    prov_put(payload, "binary_label", {
        "class": "DERIVED", "inputs": ["proofsearch_py_sha256"],
    })
    if role == "pre_patch_ck0":
        payload["omp1_arm_role"] = "PRE_PATCH_REPORTED_ALONGSIDE"
        payload["canonical_for_homogeneous_omp1_arm"] = False
    elif role == "canonical":
        payload["omp1_arm_role"] = "CANONICAL_POST_PATCH"
        payload["canonical_for_homogeneous_omp1_arm"] = True
    prov_put(payload, "omp1_arm_role", {
        "class": "DERIVED", "inputs": ["role_arg", "proofsearch_py_sha256"],
    })
    prov_put(payload, "canonical_for_homogeneous_omp1_arm", {
        "class": "DERIVED", "inputs": ["omp1_arm_role"],
    })

    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")

    # Always keep a binary-labeled sibling; never destroy the source path's content
    # without a labeled copy.
    labeled = path.with_name("%s_bin_%s.json" % (path.stem, short))
    if labeled.resolve() != path.resolve():
        shutil.copy2(path, labeled)
        print("labeled_copy %s" % labeled)

    print("stamped %s omp=%s torch_det=%r sha=%s role=%s" % (
        path, payload.get("omp_num_threads"),
        payload.get("torch_are_deterministic_algorithms_enabled"),
        short, role))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
