# Opus 4.8 prompt: final X-line confirmation of the Level 1 floor amendment v2

Perform a **bounded final confirmation**, not a fresh design review. Do not
reopen branch 1, introduce another learner repair, edit files, implement code,
run a resource probe or trajectory, inspect a series, compare arms, select N3,
create an authorization/lock, or generate panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md`
2. `reviews/fable_level1_feasibility_floor_amendment_v2_closure.md`
3. `reviews/opus_level1_feasibility_floor_amendment_review.md`
4. `reviews/sol_level1_feasibility_floor_amendment_review.md`
5. `experiments/level_1_contact/FEASIBILITY_GATE_DECISION_DRAFT.md` (historical only)

## Confirm only these closures

1. AM-1 through AM-7 landed exactly, especially:
   - valid censoring is separate from resource/process/hash/seal invalidity;
   - 2,000 optimizer updates remain unchanged and 31.51 is compute only;
   - Level 0 is engineering precedent only;
   - the unobserved-arm/all-censored predictions are withdrawn;
   - the 30 h value is a planning projection, never an upper bound.
2. Section 2 is literal signed replacement text for every changed governing
   cell: v3 section 5, v3.1 A2/A5, and the C3 conforming deletion, with C2/C4
   correctly left unchanged; retirement of replay cannot perturb another PRF
   domain.
3. The full-history rule is executable and single-valued: own history only,
   canonical schedule order, one shared unchunked tensor, four independent
   member updates, CE mean, U=1, no replay draw, no chunking/accumulation.
4. Section 6 freezes a complete v2 contract: distinct authorization/claim/report
   paths and schemas, scorer cap zero, exact v1 hashes verified, amended source
   pins, environment/HEAD/tree guards, and later-gate refusal.
5. Section 7 implements the strict Sol recovery rule without losing your AM-1
   distinction: invalidity sets no censoring bit and authorizes no automatic
   rerun; future resource recovery would require a new signed decision/review.

## One concrete ambiguity to adjudicate

Section 6 says: "The durable v2 claim is written and committed before any
learner step." Decide whether `committed` is sufficiently executable. The v1
driver atomically created a claim before step 1 but Git-committed evidence only
after completion. For v2, either:

- the amendment must specify an exact two-phase or automatic Git-commit protocol
  (commit contents, clean-index checks, HEAD transition, resume command, and
  failure behavior); or
- `committed` must be corrected to an exact durable `atomic_create`/fsync-style
  claim-before-step contract, with Git archival after the terminal artifact.

Do not choose based on convenience. Require the smallest correction if the
current sentence leaves two implementations possible. Also check whether
"source-byte pins over every amended and reachable module" needs an enumerated
path set in the amendment itself or may be frozen during reviewed implementation.

## Deliverable

Write `reviews/opus_level1_feasibility_floor_amendment_v2_final_confirmation.md`
with exactly one verdict:

- `LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_XLINE_CONFIRMED_FOR_SIGNATURE`
- `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL`

If REVISE, give only exact bounded replacement sentences and state whether one
last confirmation is needed. If CONFIRMED, explicitly authorize only Kirill's
author token `I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`, not implementation or
execution. Confirm no code, authorization, entropy, probe, trajectory,
comparative datum, N3, lock, panel, escrow, or outcome was created.
