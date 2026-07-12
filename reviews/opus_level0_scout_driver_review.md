# Opus 4.8 X-line review — Level 0 scout driver (commit 5ea236b vs 7f4ca5f)

Reviewer: Opus 4.8 (adversarial X-line). Stage: bounded orchestration review of the
timing/storage scout driver, required by `HARDENING_ACCEPTED` before the single scout
execution. I did not run the scout. I read the sources, ran the full suite (58 pass) and
both verifiers (pass), and confirmed the gitignore/artifact posture. No scout report or
checkpoint, `PREREG.lock`, or `decision.json` exists. This review does not predict
grokking, inspect a learning curve, or select any scientific threshold.

## Verdict

**SCOUT_DRIVER_ACCEPTED**

The driver is a faithful implementation of the reviewed scope: single seed (master 0),
Arm A, canonical CPU float32, 25 measured primary steps + 25 unmeasured determinism
replay = 50 interlock-counted steps under the 100 hard cap, one shared scout capability,
a 120 s hard wall enforced around every step, no held-out access, no persisted loss,
no verdict path, a purpose-tagged checkpoint whose bytes/hash are recorded, and a
fail-closed refusal on pre-existing artifacts. My prior hardening notes are both
resolved (a distinct `bounded_check` capability now backs the round-trip test, and
`interlock.py` states the threat model). The findings below are Minor and non-blocking;
execution is authorized under §3.

---

## 1. Findings

### Critical / Major
None. Every contamination guard I required is present and test-enforced (§3 rationale).

### Minor

**m1 — the 120 s wall is enforced around steps but not around the inter-phase
checkpoint I/O and `git rev-parse` (`scout.py:149-177`).** `_step_prefix` checks the
deadline before and after each step, and the shared interlock's `_started` bounds the
*whole* run — but the checkpoint save, `load_checkpoint`, source-file hashing, and the
`_repository_head` subprocess between the primary and replay phases have no interior
deadline check. For this ~200k-parameter CPU model these operations are sub-second, and
any overrun is caught at the first replay step's pre-check, so this is not a practical
risk. Recommend one line extending the documented "uninterruptible step" limitation to
cover checkpoint/subprocess I/O. Non-blocking.

**m2 — `metadata.purpose` is recorded but not integrity-verified on load
(`checkpoint.py`).** Like the other provenance fields (`repository_head`,
`source_hashes`), the schema-3 `purpose` tag is not covered by the model/optimizer state
hashes, so it could be edited in a saved payload without a `CheckpointMismatch`. The
contamination label is triangulated three ways (filename, `metadata.purpose`, and the
report's `scientific_outcome: false` / `kind`), so this is acceptable and consistent
with the existing contract; noted for the eventual full-metadata-hash item. Non-blocking.

**m3 — `peak_rss_delta_kib` may under-report the scout's own allocation
(`scout.py:218`).** `ru_maxrss` is a monotonic high-water mark, so if the interpreter's
peak was already reached during import, the delta can read ~0. The absolute
`peak_rss_kib` is the field to use for the storage/memory projection; the delta is
informational only. State that in the derived documentation. Non-blocking.

## 2. Mandatory code/test edits

None. m1–m3 are recommended documentation touches, not blockers. The gitignore already
covers the checkpoint (`*.pt`), so no repository change is required before execution.

## 3. Exact execution authorization

**Authorized: exactly one invocation.**

- **Command:**
  `.venv/bin/python scripts/level0_timing_storage_scout.py --output-dir experiments/level_0_grokking/scout`
- **Approved output directory: `experiments/level_0_grokking/scout/`.** The report
  `timing-storage-scout_non-outcome.json` there is committable; the sibling
  `timing-storage-scout_non-outcome.pt` is already ignored by the repo-wide `*.pt` rule
  and must stay local. (Verified: `.json` is not ignored, `*.pt` is ignored at any
  depth, and no scout artifacts currently exist.)
- **One-run guards:**
  1. Invoke exactly once. If the driver fail-closes or errors, do **not** delete
     artifacts and rerun to "get a clean number" — report the failure and stop; a rerun
     needs fresh authorization.
  2. Never `git add -f` the `.pt`; never reuse it as a warm-start or treat it as an
     outcome — it is a step-25 partial-weight blob retained only to measure checkpoint
     bytes and round-trip integrity.
  3. After the run, verify before committing: `scientific_outcome` is `false`;
     `steps.total ≤ 100`; `wall_seconds ≤ 120`; `deterministic_prefix.match` is `true`;
     `contamination_guards` are all `false`; both artifact names carry `non-outcome`; and
     no `PREREG.lock` / `decision.json` was created.

## 4. Allowed report fields and forbidden interpretations

**Allowed (all present in the driver's JSON):** `kind`, `scientific_outcome: false`,
`arm`, `master_seed`, `device`, `dtype`, `torch_version`, `config_hash`, `split_hash`,
`steps{primary,replay,total,hard_cap}`, `wall_seconds`, `wall_hard_cap_seconds`,
`primary_step_latency{count,mean,median,min,max}` (aggregates only — no per-step series),
`peak_rss_kib`, `peak_rss_delta_kib`, `checkpoint{name,bytes,sha256,purpose}`,
`deterministic_prefix{primary_hash,replay_hash,match}`, `contamination_guards{...}`.

**Forbidden interpretations:** no loss or accuracy value appears and none may be inferred
or added; the run says **nothing** about grokking, generalization, memorization, or
convergence; the 25 primary steps are **not** a learning curve and must not be read as
training dynamics; latency × budget is a wall-time **projection** for planning only, not
evidence about the model; the prefix hashes are determinism fingerprints, not results;
the checkpoint is neither an outcome nor a warm-start.

## 5. May the JSON report be committed after inspection?

**Yes — the `.json` report only**, after the §3 verification passes. It is a non-outcome
resource artifact and belongs in `experiments/level_0_grokking/scout/`. Documentation
derived from its numbers (latency, RSS, checkpoint bytes) may also be committed. The
`.pt` checkpoint must **not** be committed (already enforced by `*.pt`).

## 6. Lock-stage cells the scout may inform vs. cannot resolve

**May inform (resource-only):**
- **Storage projection** — `checkpoint.bytes` × the eventual cadence count × seeds ×
  arms feeds the uniform-cadence/storage-projection cell.
- **Resource wall** — `primary_step_latency.mean` × fixed budget × seeds, plus
  `peak_rss_kib`, feeds the outcome-independent time/memory wall.
- **Determinism evidence** — the matching primary/replay prefix hashes support (but do
  not lock) the canonical-path determinism contract.

**Cannot resolve (scientific cells, untouched):** persistence window W; Δ_min (with its
Xavier init-timing margin); quorum k-of-5 and demonstration-only claim strength; control
pass/fail semantics (memorization, random-label leakage, Arm B's asymmetric
interpretation); the Arm B seed-count decision; the final null set; and any accuracy/loss
threshold. The scout is a resource probe; it moves none of these, and the `PREREG.lock`
envelope still authorizes execution only, pending Kirill's acceptance of every open cell.

---

### Question index

1. 25+25 is a valid single ≤100-step scout: 50 interlock-counted steps on one capability,
   with the 25-step replay doubling as the required independent determinism check
   (`scout.py:129,181`). Yes.
2. Wall enforcement is sufficient in practice — checked before/after every step and
   bounded by the shared interlock's 120 s window; the uninterruptible-step and (m1)
   checkpoint-I/O gaps are sub-second here. Yes, with the m1 note.
3. Latency aggregates (count/mean/median/min/max, no series) and `peak_rss_kib` are
   adequate for projection and are not a learning curve (m3 caveat on the delta). Yes.
4. Purpose tag + both filenames + `scientific_outcome:false` satisfy the contamination
   label. Yes.
5. No path touches held-out targets (learner-only; AST-verified no `.evaluation`),
   persists loss (`StepResult` discarded; AST-verified absent), derives a verdict, exceeds
   caps (static + interlock + wall), overwrites a prior scout (`FileExistsError`), or
   creates lock/decision files. Confirmed.
6. Schema-3 `purpose` is correct and compatible — it sits outside the state-hash integrity
   surface (unaffected) and is required non-empty at build; m2 notes it is label-grade,
   not integrity-grade. Yes.
7. Output directory: `experiments/level_0_grokking/scout/` — report committable, `.pt`
   ignored (§3).
8. Codex may execute exactly once and commit only the non-outcome JSON plus
   number-derived documentation; never the checkpoint (§3, §5).

*Distinguishing defect from open cell: no defect blocks the run; m1–m3 are documentation
hygiene. The scout informs only the resource cells in §6 and resolves no scientific cell.
Negative space preserved: this run measures the platform's cost and determinism, not its
behavior — it is authorized to execute once and to be read as nothing more.*
