# Opus 4.8 X-line review — Level 0 scientific lock & outcome driver (commit 72de846)

Reviewer: Opus 4.8 (adversarial X-line). Stage: final pre-lock review of the scientific
specification, lock/outcome/evaluator/verifier machinery, and provenance. No outcome has
run; no `PREREG.lock` or `decision.json` exists. I did not run the outcome driver. I read
the full candidate surface, ran the suite (83 pass) and both verifiers (pass; 71 inherited
files match), and ran bounded read-only checks. I did not create any lock, outcome,
checkpoint, metric, or decision, and I do not predict grokking or infer the programme
thesis from any future result.

## Verdict

**REVISE_LOCK**

The design is sound and near-complete. Provenance (two-commit + 19-path source freeze),
draft/lock gating, evaluator/verifier separation, fixed budgets, resume transaction
recovery, and the decision logic are all correct by inspection and well-tested — with one
exception that, by the programme's own standard, must be closed before the code is frozen:
**the scientific decision-assembly path has no end-to-end test**, so a "green-but-wrong"
mutation in exactly the logic the lock exists to protect would ship undetected, and the
verifier reuses that logic so it cannot catch it. A determinism-contract gap (unpinned CPU
thread count) is the second mandatory item. Both are bounded, concrete edits; neither is a
source-availability problem (BLOCKED_SOURCE) nor a design flaw (REJECT_DESIGN). Hence
REVISE_LOCK, not LOCK_CANDIDATE_ACCEPTED.

---

## Findings

### Critical
None.

### Major

**MJ1 — The scientific decision assembly is not end-to-end tested (Q8).** No test exercises
`_run_predicates`, `evaluate_locked_battery`, `verify_level0_decision`, or
`_dataset_for_run` (verified by grep). The persistence test drives `first_persistent_step`
directly, never through `_run_predicates`, so these are unpinned:
- the section mapping FIT→`train` / GENERALIZE→`held_out` (`outcome_evaluator.py:66-79`) — a
  swap would pass every current test;
- the platform-violation membership `REQUIRED_RUN_IDS[:-1]` plus the two R-0 rules
  (`:219-225`);
- the quorum arithmetic `range(5)` over A and `(1,2,3)` over B, and PLATFORM_INVALID
  precedence over quorum (`:227-240`).
Because `decision_verifier.py` imports the same `_run_predicates`/`_load_complete_run`, a
logic mutation is self-consistent across evaluator and verifier and passes verification
too. I audited this code by eye and it currently matches `SCIENTIFIC_SPEC.json`, so this is
a regression/freeze gap, not a known bug — but the lock will freeze `outcome_evaluator.py`,
so it must be closed first. This is the same "green-but-wrong must be catchable" standard
the team adopted for the model (J1); it must apply to the decision.
*Mandatory before lock:* add (a) direct `_run_predicates` tests on synthetic metric lists
where a train/held_out swap fails and the delay boundary (1900→not DELAYED, 2000→DELAYED)
is pinned; (b) a synthetic-battery test of `evaluate_locked_battery` asserting REPRODUCED at
4/5, NOT_REPRODUCED at 3/5, PLATFORM_INVALID on a real-label FIT failure and on an R-0 that
GENERALIZEs, and that Arm B successes never move the primary decision. Tests are not in
`SOURCE_PATHS`, so adding them does not disturb the freeze; fix any bug they reveal, then
lock.

**MJ2 — CPU thread count is not pinned, so the determinism contract is unenforced (Q7).**
`SCIENTIFIC_SPEC.json:environment` pins backend/dtype/deterministic_algorithms/python/torch
but not `torch.set_num_threads`; only the runbook says "do not change thread counts."
PyTorch CPU reductions can be bitwise thread-count-dependent even under
`use_deterministic_algorithms(True)`, so resume replay and the "deterministic CPU platform"
claim — and the value of the committed v2 prefix certificate — rest on an unpinned
variable. Concurrency itself is safe (each process fixes its own thread count at start, so
within-process determinism holds and A∥B cannot cross-contaminate; the only concurrency
risk is a wall-clock `RESOURCE_STOP` under contention, which is conservative and yields no
verdict). *Mandatory before lock:* set a fixed `torch.set_num_threads()` /
`set_num_interop_threads()` in the outcome and prefix entrypoints and add the value to the
validated `environment` contract, so the trajectory is reproducible across resume and
machines regardless of load.

### Minor

**MN1 — Duplicated cadence constants outside the validator (silent-drift surface).** The
evaluator hard-codes `range(0, fixed+1, 100)` (`outcome_evaluator.py:126`) and the save
path hard-codes `step % 1000 == 0` (`outcome.py:340`), while the resume path reads
`spec["observations"][...]`. All equal today (validate_spec freezes 100/100/1000), but read
the validated spec everywhere to remove the duplicated constant.

**MN2 — The verifier shares predicate/loader code with the evaluator.**
`decision_verifier.py` re-derives via the evaluator's `_run_predicates`/`_load_complete_run`,
so it certifies reproducibility and artifact integrity, not logic independence. Acceptable;
the MJ1 tests are the pragmatic substitute for a second implementation.

**MN3 — Observation, confirm intent:** all real-label runs including B-1..B-3 must FIT or the
verdict is PLATFORM_INVALID (`:219`). This couples Arm B memorization health to the Arm A
decision. It is coherent (memorization is a universal platform floor, distinct from
grokking, consistent with "B non-grokking is no inference"), but confirm it is intended.

## Mandatory edits (before `create_lock` runs)

1. MJ1 — add the `_run_predicates` and synthetic-battery decision tests; fix any revealed
   bug in `outcome_evaluator.py`, then re-freeze.
2. MJ2 — pin CPU thread count in code and in the validated `environment` contract.
3. MN1 — read cadences from the validated spec in the evaluator and save path.

---

## Traceability of every scientific cell (prose → JSON → validation → lock → runtime → tests)

Confirmed end-to-end for: predicates FIT 0.99/1000, GENERALIZE 0.95/1000, DELAYED
Δ_min 2000; cadences 100/100/1000; quorum 4/5; environment; resource walls
(21600/64800/21600s, 25 GiB); run battery A-0..A-4, B-1..B-3 (seeds 1,2,3), R-0
(random, seed 0, label_seed 20000). Each cell is in `SCIENTIFIC_SPEC.json`, enforced by
`validate_spec`, re-pinned per run in the schema-2 lock (`validate_lock`), carried into the
runtime `locked-outcome` interlock, and (except the decision-assembly cells, MJ1) covered by
tests. `Δ_min=2000` is derived in `ANCHOR_CLAIMS.md` from published anchors (5,000-epoch
grokking lower bound − 1,400-epoch memorization = 3,600 gap, locked at 2,000 with margin),
cited to PDF pages, explicitly not a prediction, and frozen in the locked source set.

**Silently-driftable values:** MN1 (evaluator/save cadence constants). All run-identity
values — config/split/label hashes — are recomputed at runtime (`_dataset_for_run:216-219`
compares recomputed split and label hashes to the spec), so a stale hash cannot run.

## Accepted contracts

- **Two-commit provenance (Q2):** `create_lock` requires the accepted spec committed clean,
  records `source_commit=HEAD` + a 19-path `source_hashes` map (incl. spec, all level0
  modules, all scripts) + spec sha; runtime `_verify_repository_binding` enforces canonical
  `PREREG.lock`, `source_commit` ancestor of HEAD, lock tracked and unchanged, and
  `_verify_locked_sources` enforces byte-identical locked paths. Post-lock tampering of any
  locked module (incl. the evaluator/verifier) is caught.
- **No outcome under draft / without canonical lock (Q3):** `load_spec(require_accepted=True)`
  and `load_lock` (canonical JSON, Kirill's `I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC`, spec-hash
  match) gate every entrypoint; `from_preregistration` mints the only step/eval/verdict-
  capable capability and only from a valid lock. `test_draft_spec_cannot_authorize_outcome`
  confirms a draft spec creates no output/lock/decision.
- **Evaluator cannot optimize; trainer cannot judge (Q3):** AST test confirms the evaluator
  imports no `optimization_step`/`make_optimizer`/`GrokkingTransformer` and the trainer no
  `first_persistent_step`/`.decision`. No decision before all nine complete: `_load_complete_run`
  requires each `run_complete.json` with metrics/manifest/checkpoint integrity and exact
  cadence; `evaluate_locked_battery` refuses if a decision exists.
- **Resume & recovery (Q4):** metric-append → snapshot → atomic resume-checkpoint (+cadence
  archive) ordering; on resume the manifest must match, checkpoint config/split hashes and
  source/metrics-prefix hashes must match, and the transaction recovery discards **at most
  one** hash-verified uncommitted tail, logs it hash-only (no elapsed/outcome data), removes
  the stale snapshot, and fails closed on any multi-line ambiguity
  (`_recover_uncommitted_metric_tail`, tested).
- **Integrity, budgets, stopping, no warm start (Q5):** schema-4 model+optimizer+scheduler
  hashing and torch/CPython/CPU/float32 enforcement; exact fixed budgets with a post-loop
  `steps_used == fixed_updates` assertion; per-run + battery byte ceilings; non-finite →
  abort with no verdict; wall/byte stops write `RESOURCE_STOP.json` with `scientific_verdict:
  null` and are terminal; every run starts from a fresh seed-initialized model (no warm
  start); early success/failure stop is impossible in code.
- **Decision logic (Q6):** A 4/5 quorum only; B annotation only (`ALTERNATE_ANCHOR_GROKS`/
  `NO_INFERENCE`, never counted); all real-label runs must FIT; R-0 must FIT and must not
  GENERALIZE; PLATFORM_INVALID takes precedence. Persistence/delay boundary verified
  (fit_start=1000, generalize_start=3000, delay=2000=Δ_min → DELAYED). Correct by inspection;
  MJ1 requires it be locked in by test.
- **Concurrency (Q7):** A and B on distinct run-ids may run concurrently without altering
  semantics (separate output dirs, per-process fixed thread count, independent RNG); the only
  effect is contention against the locked wall clocks, which can only produce a conservative
  `RESOURCE_STOP`, never a wrong verdict — subject to MJ2 pinning the thread count.
- **verify_all wiring:** verifies the inherited decision, verifies the Level 0 decision when
  present, and fails on any stray `decision.json` under `experiments/`.

---

## Ordered authorization answers

- **May the candidate implementation/spec be committed before signature?** **Yes.** The spec
  is `draft-before-review-and-signature`, nothing runs under draft, and no lock/decision
  exists; the candidate is already committed. Land MJ1/MJ2/MN1 first. Tests are outside
  `SOURCE_PATHS`, so adding them does not disturb a later freeze.
- **After Sol/Opus findings close, may Kirill set status to
  `accepted-by-kirill-before-outcome`?** **Yes**, once MJ1 (with any evaluator fix) and MJ2
  are committed. The status edit must then be committed before `create_lock` (which requires
  the accepted spec clean at HEAD).
- **May the canonical lock script then run exactly once and its result be committed?**
  **Yes.** After the accepted spec is committed, run `create_lock` with `--authorized-by
  Kirill --confirm I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC`; it records `source_commit=HEAD` + hashes,
  writes `PREREG.lock` (refusing if one exists), and then commit the lock.
- **Only after that lock commit, may Codex give Kirill the runbook commands?** **Yes** — and
  only then. The runbook is explicitly invalid until the lock is created, committed, and the
  verifiers pass at that commit. Relay the commands after that, not before.
- **Are two distinct run-id processes authorized concurrently?** **Yes**, for distinct
  run-ids (A∥B), with MJ2 applied to keep determinism thread-count-independent; never two
  processes for the same run-id. Concurrency affects only wall-clock contention, not results
  or the verdict.

*Distinguishing defect from choice: nothing here is a runtime defect; MJ1 is a test-freeze
obligation on the decision logic (likely no evaluator change), MJ2 a determinism-contract
pin, MN1 a duplicated-constant cleanup. The scientific choices (thresholds, Δ_min, quorum,
walls, null set, B-seed count) are locked in the spec and I did not reopen or retune them.
Negative space preserved: I confirmed the machinery cannot produce a verdict before nine
complete runs and cannot run under draft, and I did not infer any Level 0 outcome.*
