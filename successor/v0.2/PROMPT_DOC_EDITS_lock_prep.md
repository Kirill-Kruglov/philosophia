# Lock-prep doc edit — reconcile the single-thread deviation (pre-data, pre-lock)

You are making a small, purely documentary edit to the `successor/v0.2/` preregistration bundle **before it is locked and before any outcome-bearing run exists**. Do not touch any code, do not run any calibration/pilot/confirmatory step, and do not change any scientific value (estimand, arms, SESOI, gates, N rule, module pools, interpretation). Work on `main` (or a branch you then merge) with repo access.

## Why
External review found an internal inconsistency to fix before lock:
- the inherited Level-0 `src/philosophia/level0/config.py` pins `PINNED_TORCH_NUM_THREADS=16` / `interop=32`;
- the implementation contract §17 requires **single-thread** execution for the strict k=1 bit-identity gate and the D0/D1 determinism replays;
- but PREREG §6.3 "Allowed deviations only" (which states "only these deviations" are authorized) does **not** list the thread override.

So the single-thread execution is currently an undocumented deviation. Reconcile it by adding it explicitly.

## Edit 1 — PREREG §6.3
File: `successor/v0.2/PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md`, section **6.3 Allowed deviations only**. After existing item 6 ("data generation, fixed history budget, and probe stopping semantics follow v0.2.") and **before** the paragraph beginning "No architecture search…", insert:

```
7. execution is pinned to a single intra-op and single inter-op thread, overriding the inherited Level 0 runtime thread pinning (16 intra-op / 32 inter-op); the inherited `configure_canonical_torch_runtime()` is not invoked. This is a runtime/determinism setting, not an architecture or optimizer change; single-thread execution is required for the bit-reproducibility that the k=1 identity gate and the D0/D1 replays depend on (implementation contract §17).
```

Do not alter items 1–6 or the "No architecture search…" paragraph.

## Edit 2 — amendment record
Append a dated entry to `AMENDMENTS.md` at the repo root, in the file's existing style (create a clearly-labelled entry if the file is freeform). It must state: date; that this is a **pre-data, pre-lock** amendment (no outcome-bearing run exists, so nothing is invalidated); the reason (§6.3 did not enumerate the single-thread execution that impl-contract §17 mandates and that overrides the inherited 16/32-thread pin in `config.py`); the exact files touched (this list); and that no scientific value changed.

## Edit 3 — confirmatory config template
File: `successor/v0.2/CONFIRMATORY_CONFIG_TEMPLATE_V0.2.json`. Add two fields for completeness so the locked runtime records the thread contract:
```
"torch_num_threads": 1,
"torch_num_interop_threads": 1
```
Place them next to the other determinism/runtime fields; keep the JSON valid and the schema/version fields unchanged.

## Edit 4 — recompute bundle hashes
Because Edits 1 and 3 change file bytes, recompute `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt` over the v0.2 bundle files (the same set it already lists), e.g. `sha256sum` each listed file and rewrite the manifest so every hash matches the edited files. The manifest must be internally consistent after your edits.

## Verify before committing
- `grep -rn -iE "16|thread" successor/v0.2/` and confirm nothing in the v0.2 bundle still asserts 16/32 threads as the authoritative v0.2 execution setting (the inherited `src/philosophia/level0/config.py` may keep pinning 16 — that is fine; it is Level-0 source, and deviation 7 + brief §2's "do not call `configure_canonical_torch_runtime()`" govern the override).
- Confirm impl-contract §17 already states single-thread (it should) — do not edit it; it is now consistent with §6.3.
- Re-verify `CANDIDATE_BUNDLE_SHA256.txt` matches the on-disk files.

## Deliver
Show the diff of all touched files, the new `CANDIDATE_BUNDLE_SHA256.txt`, and commit with a message like `lock-prep: add PREREG §6.3 deviation 7 (single-thread) + amendment + rehash (pre-data, pre-lock)`. Do not proceed to any calibration or run.
