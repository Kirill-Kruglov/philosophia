# Sol review - Level 0 scientific lock and outcome system

Reviewer: Sol, independent scientific/statistical review. Scope: pre-outcome
scientific lock, outcome driver, evaluator, verifier, and cited Level 0
evidence. I did not run any outcome step, create `PREREG.lock`, inspect
anticipated curves, select thresholds from outcomes, or derive a scientific
decision.

## Verdict

REVISE_LOCK

The design is close and scientifically usable after revision. The narrow
estimand is defensible as a five-seed replication demonstration of the
canonical CPU reconstruction, not a powered statistical claim and not evidence
for Philosophia. However, the lock should not be created until the observed
persistence definition, decision-path regression coverage, CPU determinism
contract, and Arm B annotation language are tightened before any outcome run.

## Critical Findings

None.

## Major Findings

**M1 - Persistence is implemented as observed-sample persistence, but the prose
can be read as continuous persistence.** `PREREGISTRATION_DRAFT.md:23` fixes
metric sampling every 100 steps, while `PREREGISTRATION_DRAFT.md:25` and
`PREREGISTRATION_DRAFT.md:27` say the metric "remains" above threshold for a
1,000-step span. The executable predicate in `metrics.py:62` to `metrics.py:83`
requires consecutive recorded observations at or above threshold until
`observation.step - start >= 1000`; it cannot see sub-cadence dips. This is not
outcome leakage and does not reward a one-point excursion, but it can reward a
trajectory that dips below threshold between two 100-step observations. That is
acceptable only if the estimand is explicitly "observed reporting persistence"
rather than continuous accuracy persistence. Mandatory edit: revise the prose
and JSON predicate descriptions to say: "FIT/GENERALIZE start at the first
recorded observation such that every recorded observation from that step through
at least start+1000, inclusive, is at or above the threshold; no claim is made
about unobserved sub-cadence values." Add tests showing that an observed below-
threshold value inside the window resets persistence, exact threshold equality
passes, exact 1,000-step span passes, and 900-step span fails.

**M2 - The scientific decision assembly is correct by inspection but not locked
by independent tests.** The current evaluator maps FIT to `train` and
GENERALIZE to `held_out` in `outcome_evaluator.py:66` to
`outcome_evaluator.py:79`, applies platform invalidity in
`outcome_evaluator.py:218` to `outcome_evaluator.py:225`, and computes Arm A
and Arm B counts in `outcome_evaluator.py:227` to `outcome_evaluator.py:240`.
Those clauses match the prose and `SCIENTIFIC_SPEC.json` by inspection.
However, `tests/test_level0_scientific_lock.py:160` tests the lower
`first_persistent_step` helper directly rather than the full `_run_predicates`,
all-nine-run battery, decision artifact, and verifier recomputation. The
verifier imports `_run_predicates` from the evaluator in
`decision_verifier.py:10`, so a shared wrong predicate could verify itself.
Mandatory edit: add synthetic tests that exercise `_run_predicates` through the
train/held-out mapping, exact delay 2000 vs 1900, observed-window reset, 4/5
Arm A -> reproduced decision, 3/5 Arm A -> not reproduced decision,
PLATFORM_INVALID precedence for a completed real-label FIT failure, R-0 FIT
failure, R-0 GENERALIZE, and an Arm B success that changes only annotation and
never the primary decision. The tests should cover all nine required run ids or
a minimal synthetic harness that proves the same membership and precedence.

**M3 - CPU thread count is a determinism/platform variable but is only in the
runbook as an instruction.** `OUTCOME_RUNBOOK_DRAFT.md:9` says not to change
thread counts, but `SCIENTIFIC_SPEC.json` and `scientific_spec.py:132` to
`scientific_spec.py:139` validate only backend, dtype, deterministic
algorithms, Python, and torch. `outcome.py:419` to `outcome.py:421` enforces
float32 and deterministic algorithms but does not set or validate torch intraop
or interop threads. CPU reductions can be thread-count dependent, and
concurrent distinct run ids make this operationally salient. Mandatory edit:
choose fixed `torch_num_threads` and `torch_num_interop_threads` values, add
them to `SCIENTIFIC_SPEC.json`, validate them in `scientific_spec.py`, set them
in all outcome/prefix/scout entrypoints before model construction, and record
them in manifests/reports.

**M4 - Arm B is coherent as a diagnostic arm, but the decision artifact wording
can still invite a forbidden independent-success reading.**
`PREREGISTRATION_DRAFT.md:46` to `PREREGISTRATION_DRAFT.md:49` correctly says
Arm B never enters the primary quorum and B failure is uninformative. The code
honors that: `outcome_evaluator.py:235` to `outcome_evaluator.py:240` selects
the primary decision from platform validity and Arm A only. But
`outcome_evaluator.py:250` to `outcome_evaluator.py:252` emits
`ALTERNATE_ANCHOR_GROKS` whenever any B seed succeeds, even when Arm A already
reproduces. That label invites exactly the inference forbidden by
`SCIENTIFIC_SPEC.json`: Arm B as an independent success target. Mandatory edit:
rename and condition the annotation so it reads as a diagnostic only, e.g.
`ANCHOR_FIDELITY_SENSITIVE_DIAGNOSTIC` only when the primary decision is not
reproduced and `arm_b_successes >= 1`, otherwise `NO_PRIMARY_INFERENCE`; update
the verifier and tests accordingly.

## Minor Findings

**m1 - The thresholds are defensible but should be called operational, not paper
thresholds.** The archive supports near-perfect train/test behavior and a
published timing gap: `ANCHOR_CLAIMS.md` derives 3,600 epochs from the 5,000
lower grokking anchor minus the 1,400 memorization anchor, then locks
`delta_min = 2,000` and `persistence_window = 1,000`. The 0.99 FIT and 0.95
GENERALIZE thresholds are fixed before outcome and weaker than "100%" / "near
100%" paper prose, so I do not see circularity or leakage. Still, the final
lock language should call them pre-outcome operational thresholds, not recovered
paper thresholds.

**m2 - Cadence constants are duplicated in executable code.** The spec freezes
metric cadence at 100 and checkpoint cadence at 1,000, and the runtime mostly
reads the spec. But `outcome_evaluator.py:126` hard-codes cadence 100, and
`outcome.py:340` hard-codes archival checkpoint cadence 1,000. These match the
draft today. Prefer reading the already validated spec values everywhere before
lock.

**m3 - All real-label runs, including Arm B, must FIT.** This is coherent:
memorization reachability is treated as a platform floor rather than a grokking
result, and `outcome_evaluator.py:219` applies it to A and B while R-0 receives
separate rules. This should remain explicit because it means a completed B FIT
failure can invalidate the platform even though B GENERALIZE failure cannot
alter the Arm A verdict.

## Audit Conclusions

**Thresholds and delayedness.** FIT >= 0.99, GENERALIZE >= 0.95, W = 1000, and
DELAYED >= 2000 are fixed pre-outcome and anchored to archived paper timing
only as conservative operational predicates. The exact-threshold and exact-
delay semantics are inclusive in code. No outcome-dependent threshold selection
is visible. The only scientific ambiguity is cadence aliasing, handled by M1.

**Quorum and claim strength.** The 4/5 Arm A quorum is defensible only as a
replication demonstration: one complete seeded run is the unit of replication,
not a checkpoint, metric observation, or Fourier vector. The draft correctly
forbids p-values, effect sizes, or generalization beyond the locked task. The
claim should remain: "at least 4/5 paper-mainline seeds in this canonical CPU
reconstruction reproduced delayed generalization under the locked predicates."

**Platform controls.** The control structure is coherent. Every completed
real-label run must FIT; completed R-0 must FIT and must not GENERALIZE; control
violations yield PLATFORM_INVALID. Arm B's three-seed asymmetric role is
coherent after M4: B can annotate anchor-fidelity sensitivity but cannot rescue
or worsen the primary Arm A verdict.

**Pseudoreplication and diagnostics.** The draft keeps checkpoints, cadence
observations, and Fourier energy vectors as diagnostics rather than replication
units or post-hoc predictors. I found no executable path that counts them toward
the quorum.

**Resource stops and incomplete runs.** The distinction is coherent. Integrity,
canonical-environment, non-finite, hash, or resource failures abort without a
scientific outcome. Completed control failures can yield PLATFORM_INVALID.
`outcome.py:581` to `outcome.py:604` writes terminal RESOURCE_STOP artifacts
with `scientific_verdict: None`; `outcome_evaluator.py:101` to
`outcome_evaluator.py:162` requires all nine complete reports before any
decision.

**Evaluator and verifier.** The evaluator matches the prose/machine spec by
inspection: all nine run ids are required, exact budgets and cadence are checked,
platform invalidity takes precedence, Arm A quorum controls the primary verdict,
and Arm B is counted only for annotation. The verifier recomputes the same
fields, but because it shares evaluator helpers, it is not an independent logic
oracle; M2 is required before lock.

**Forbidden claims still invited.** Even after a clean Level 0 result, the
decision artifact must not invite: evidence for the Philosophia programme;
progress/Fourier diagnostics predicting, explaining, or causing grokking;
weight decay causality or necessity; a new Fourier basis appearing at grokking;
cross-world or cross-representation transfer; architecture/modulus/task
generality; p-values, effect sizes, or a powered population claim; ROCm/GPU
validity; Arm B as an independent success; R-0 as the only scientific null for
future levels; or timing/threshold equivalence to the original paper beyond the
locked operational predicates.

**Concurrent distinct run ids.** Two distinct run ids may be executed
concurrently without changing the scientific estimand: each run has a locked
run id, seed, split/config hash, fixed budget, and separate output directory,
and the decision is a function of completed reports only. Concurrency is a
timing-efficiency choice, not a scientific-design change. It does increase
resource-wall risk through CPU contention; that risk is conservative because a
wall crossing yields RESOURCE_STOP and no scientific verdict. M3 must be fixed
so concurrency does not leave the deterministic CPU platform under-specified.

## Authorization Answers

**Can the implementation be committed as a reviewed candidate?** Yes, as a
reviewed pre-lock candidate with the above mandatory edits outstanding. The
current draft status correctly prevents outcome execution.

**May Kirill change spec status and create the lock after those edits?** Yes,
after M1 through M4 are committed, tests/verifiers pass, and Kirill explicitly
accepts the revised pre-outcome spec. The lock should be created only after that
accepted spec is committed.

**May the long-run commands be issued now?** No. They may be issued only after
the revised spec is accepted, `PREREG.lock` is created by the canonical script,
the lock is committed unchanged, and the repository verifiers pass at that
commit.
