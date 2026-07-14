# Level 1 feasibility-floor amendment — bounded Y-line review

`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

## Critical findings

### C1. The draft improperly merges a valid second censoring with an invalid v2 execution

The proposed route "censored again, or invalid execution" →
`BLOCKED_LEVEL1_FEASIBILITY`, followed by the statement that the amended learner
did not reach a certified solve, is not admissible. A valid feasibility censoring
is a learner-floor observation under the amended policy. An environment mismatch,
resource stop, process fault, hash failure, or seal failure produces no binary
learner observation at all.

Only a valid v2 record may set `censored_at_b`. A wall-cap stop before a valid
completion is resource invalidity, not censoring, even if no qualifying window
has yet been observed. The one signed exception remains the already frozen
scientific non-finiteness rule: a validly recorded non-finite learner trajectory
is treated as scientific censoring according to v3 §7 and v3.1 A6, not as a
hardware or process fault.

The pass/censor branch is conservative only after validity has been established:

- valid `censored_at_b:false` → comparative-scout review only;
- valid `censored_at_b:true` → `BLOCKED_LEVEL1_FEASIBILITY`, C1 untested, and no
  third feasibility intervention;
- invalid v2 → no feasibility binary, no learner-floor narration, and a signed
  invalidity disposition with no automatic retry or replacement intervention.

### C2. The resource-cap semantics do not yet preserve validity

The exact work ratio is
`2,001,000 / 63,504 = 31.5098…`, appropriately reported as 31.51. Multiplying
the measured minibatch-32 component by this ratio is not a demonstrated upper
bound. It assumes at-most-linear scaling of an unchunked full-history
forward/backward despite changing batch size, memory traffic, allocator behavior,
and possible paging. It is only a planning projection.

The 36 h cap is outcome-independent in origin: it is frozen from a resource
projection rather than from a desired pass/fail observation. That is acceptable.
It is not evidence that 36 h is sufficient. The amended protocol must state that
the cap is enforced without consulting evaluator performance; reaching it before
a valid terminal report yields a resource-stop invalidity with
`censored_at_b` unset. A partial run cannot be called pass or censored.

## Major findings

### M1. Branch 1 is licensed only in its narrow procedural sense

A8, C6, and C7 support the following narrow reading: the valid v1 binary records
that the original locked learner did not produce a complete qualifying window on
the one predeclared RANDOM-STATIC `n=66` fixture; the current learner policy is
therefore blocked at the feasibility gate; and A8 permits a signed, reviewed
feasibility-floor amendment followed by a new one-shot binary gate.

They do not establish that an amendment is empirically necessary in other worlds
or arms, identify full-history training as the repair, or predict comparative or
outcome behavior. The phrases that the development contrasts would
"predictably" be all-censored and that the outcome battery would be designed to
return `INSUFFICIENT` exceed the one-fixture observation and must be withdrawn.
The gate may decline to spend the scout under the original learner without
pretending to know what that scout would have returned.

A8 licenses consideration of a floor amendment; it does not license a search for
a preferred result. A v2 pass remains a gate fact only. It is never evidence for
ACTIVE, YOKED, RANDOM-STATIC, C1, an outcome-world solve probability, or the
programme.

### M2. Full-history training changes the learner-class conditional estimand

The population, contrast formula, endpoint, cadence, margins, estimator, and N3
rule retain their mathematical forms. The potential outcomes entering that
formula do not. Full-history training changes the learner policy that generates
the target ACTIVE state and queries and the donor ACTIVE state and hence the
geometry inherited by YOKED. The high-level ACTIVE-vs-YOKED question remains,
but it becomes the contrast conditional on the amended full-history learner
class. It is not the same locked-policy estimand numerically or operationally.

Applying the change to every arm prevents a direct arm-label implementation
asymmetry. It does not make the change inferentially inert. Retiring replay removes
a stochastic nuisance source, while simultaneously changing what retained
contact means. Under full-history mean CE, every retained pair is included in
every later update, with per-update gradient weight `1/t`; earlier pairs therefore
receive more cumulative optimizer exposure. Under the original policy, the
newest pair was guaranteed once and older pairs were included through stochastic
replay. This is a substantive reweighting of contact history. Any differential
effect across arms is an effect under the new learner policy, not evidence that
the amendment itself is neutral.

The amendment must loudly update the learner-class scope in the question,
estimand, and treatment sections. It may say that the estimator is unchanged; it
must not say that the scientific estimand or inference contract is wholly
unchanged.

### M3. Compute is matched per learner trajectory, not across complete arm packages

For every valid target-arm trajectory at step `t`, ACTIVE, YOKED, and
RANDOM-STATIC each have `t` target oracle answers and each of four committee
members takes one AdamW update over the same `t` padded examples. Thus update
count, nominal training examples evaluated, tensor shape, and target query budget
are matched at every `t`. Each donor ACTIVE trajectory must obey the same rule for
its own four members and its own `t` donor answers. Replicates must use the same
schedule.

This does not make total system resources equal across arm packages. YOKED also
requires a separate donor trajectory; ACTIVE and donor ACTIVE incur shortlist
scoring that YOKED and RANDOM-STATIC do not. Those are fixed parts of the
treatments and do not give the YOKED target extra training examples or target
answers, but they must be counted in the operational resource ledger. The draft
must distinguish matched target scientific exposure and matched per-trajectory
training from unmatched acquisition-generation compute. Donor answers and state
must remain inaccessible to the YOKED learner except through the already defined
query geometry.

### M4. Level 0 supplies no choice among learner repairs

Level 0 supports only the weak engineering precedent that full-batch AdamW ran on
the locked CPU platform for its own task and configuration. It does not select
full-history as the unique Level 1 repair and does not predict Level 1
feasibility. Level 1 still takes only 2,000 optimizer updates, whereas the Level
0 Arm A generalization starts occurred at about 5,200–7,700 updates. Architecture,
sequence length, task, training set, decay specification, and execution threading
differ. The Level 0 outcome itself expressly forbids generalization beyond its
locked task, and v3 §5 permits it only as engineering precedent, not capacity
evidence.

With mean CE, `2,001,000` is an example-evaluation count, not an optimizer-step
count or a quantity that can be compared as if it were conserved gradient mass.
The "about 400× below" explanation and the claim that failure was mechanically
unsurprising must be removed. At most, Level 0 can motivate full batch as a known
executable optimizer form; it gives no choice among full history, a different
replay policy, more updates, a different learning rate schedule, a different
architecture, or a changed B.

The proposed rule is free of a newly chosen numeric hyperparameter in the narrow
syntactic sense. It is nevertheless an outcome-triggered 31.51× increase in
example evaluations plus a history-reweighting intervention. It must be named as
a capacity/optimization-policy increase authorized for review by A8, not called
inferentially parameter-free. Its defensible provenance is simplicity,
determinism, and removal of replay sampling—not evidence that it is uniquely
likely to pass.

### M5. The same-fixture v2 check is acceptable only as a non-inferential amended-regime gate

The same fixture and byte-identical criterion do not create an impermissible
second look because A8 pre-authorized a signed amendment and repeat review. The
new learner policy, new reviewed HEAD, new authorization, immutable v1 link,
one-shot path, and frozen route make v2 a new feasibility gate rather than a rerun
of v1.

Because the v1 binary triggered the amendment, v2 is not independent confirmation
and cannot estimate improvement. No v1/v2 contrast may be formed. A pass merely
removes the feasibility blocker and opens comparative-scout review. A valid
second censoring deterministically closes this amendment route with no third
intervention. An invalid v2 closes no scientific question and cannot silently
authorize another run; any further action requires a new explicit signed
programme decision and full review.

## Minor finding

### m1. “Upper bound,” “parameter-free,” “unchanged science,” and “new experiment” need qualified usage

Use “planning projection,” “no new numeric hyperparameter,” “unchanged estimator
and endpoint, amended learner-class estimand,” and “new non-inferential
amended-regime gate.” These terms retain the intended distinctions without
claiming more than the governing documents support.

## Exact mandatory edits

1. Replace the branch-1 rationale with: “The valid v1 record establishes only a
   floor failure on the frozen original-policy fixture. Under the signed gate
   policy, that blocks the comparative scout under the original learner and
   permits—but does not empirically select—a signed floor amendment.” Delete both
   the “predictably all-censored” and “designed to route to `INSUFFICIENT`”
   statements.

2. Replace every claim that Level 0 uniquely anchors or selects full-history
   training with: “Level 0 is an engineering precedent that full-batch AdamW ran
   on this platform for a different locked task; it supplies no comparative
   evidence and no choice among Level 1 repairs.” Rename all
   “example-gradients” as “example evaluations,” delete the “about 400×” causal
   comparison, and state that both v1 and v2 retain 2,000 AdamW updates.

3. Add a learner-scope amendment to the C1/estimand language: “All Level 1
   potential outcomes and contrasts are conditional on the full-history,
   mean-CE, one-update-per-answer learner policy. This replaces the stochastic
   replay learner class; it preserves the high-level ACTIVE-vs-YOKED question and
   estimator form but defines a new learner-class conditional estimand.”

4. Add an exact resource-matching table covering target ACTIVE, donor ACTIVE,
   YOKED, and RANDOM-STATIC. At each `t`, state target/donor oracle answers,
   committee size four, one update per member, batch size `t`, target history
   accessibility, scorer work, and donor-only generation work. Do not describe
   total package compute as arm-matched.

5. Replace the combined censor/invalid route with a validity-first decision
   table. Use `censored_at_b` only after validation. Record invalid v2 as
   `LEVEL1_FEASIBILITY_V2_INVALID:<ENVIRONMENT|RESOURCE_CAP|PROCESS|HASH|SEAL>`
   with `censored_at_b` unset; preserve the governing
   `PLATFORM_OR_DESIGN_INVALID` destination wherever v3 §7 requires it. State
   explicitly that no invalidity subtype authorizes a rerun or another learner
   intervention.

6. Replace “30 h upper bound” with “30 h linear-scaling planning projection.”
   Keep 31.51 as the exact work-ratio summary. Specify that the 36 h wall is
   checked independently of panel performance and that a cap hit before valid
   completion is `LEVEL1_FEASIBILITY_V2_INVALID:RESOURCE_CAP`, not learner
   censoring.

7. Add these canonical status lines after v2, without changing any signed claim
   destination:

   - valid second censoring, ledger: “Level 1 feasibility floor —
     `BLOCKED_LEVEL1_FEASIBILITY`; C1 untested; no comparative scout; no programme
     evidence.”
   - valid second censoring, ROADMAP: “Level 1 — BLOCKED BY VALID V2 FEASIBILITY
     CENSORING; detector not run; no third feasibility intervention.”
   - invalid v2, ledger: “Level 1 feasibility v2 —
     `LEVEL1_FEASIBILITY_V2_INVALID:<cause>`; feasibility binary unset; no
     learner-floor evidence; C1 untested,” followed by the governing
     `PLATFORM_OR_DESIGN_INVALID` route where applicable.
   - invalid v2, ROADMAP: “Level 1 — V2 INVALID (<cause>); no pass/censor result;
     no automatic rerun or intervention.”

8. State beside the pass route: “A v2 pass is a gate condition only and has no
   arm, C1, outcome-world, or programme interpretation.” State beside the valid
   censor route: “The amended fixture did not clear the floor; the C1 detector
   remains unrun and untested.”

## Allowed and forbidden interpretations

| State | Allowed interpretation | Forbidden interpretation |
|---|---|---|
| v1 `censored_at_b:true` | The one frozen RANDOM-STATIC `n=66` fixture under the original replay learner did not complete a qualifying window within B; under A8 it may trigger a signed floor-amendment review and blocks the original policy at the gate. | Generalization to another world, arm, seed, scout, or battery; learner lacks `n`; RANDOM-STATIC is inferior; Level 1 or C1 is false; full history is uniquely selected; scout is predictably all-censored; outcome is designed to be `INSUFFICIENT`. |
| valid v2 `censored_at_b:false` | The same fixture under the amended learner cleared the same binary floor; comparative-scout review may begin. | Evidence that the amendment improved performance; a v1/v2 effect; evidence for any arm, C1, outcome feasibility, boundary, or programme claim; direct authorization to execute the scout. |
| valid v2 `censored_at_b:true` | The amended fixture did not clear the floor; record `BLOCKED_LEVEL1_FEASIBILITY`, leave C1 untested, and permit no third feasibility intervention. | Level 1 false; learner lacks the modulus; arm comparison; `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; outcome `INSUFFICIENT` derived from an executed battery; permission for another knob change. |
| v2 process or other invalidity | No valid v2 binary exists; record the exact invalidity subtype, keep `censored_at_b` unset, and follow the signed invalidity disposition. | Learner-floor failure or success; pass/censor narration; evidence about the amended learner; automatic retry; replacement feasibility intervention; C1 or programme inference. |

## Signed destinations and detector status

All signed negative destinations remain unchanged. In particular, only a valid
comparative C1 result can reach `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`;
unresolved executed comparisons route to `INSUFFICIENT`; applicable
process/design failures retain `PLATFORM_OR_DESIGN_INVALID`; certificate failure
or censoring never proves that the learner lacked `n`; and neither feasibility
gate can support `PROOF_CORE` or any programme claim. Level 1 remains a detector,
not programme evidence, in every branch. Censoring and `UNKNOWN` are never
success, equivalence, or a narrated boundary.

## Author-token disposition

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` is not signable on the present
draft. The repairs are bounded, but they alter load-bearing scope, provenance,
resource, and invalidity language. After the exact edits above, a new final
bounded Y-line check of the amended text is required; no new feasibility data or
broader scientific review is required for that check.

## Bounded-review confirmation

This review created only this Markdown review. It created no code, entropy,
comparative datum, N3 selection, lock, panel, escrow, trajectory, or outcome. It
did not execute a learner, inspect or reconstruct a series, compare arms, or
generate any development or outcome evidence.
