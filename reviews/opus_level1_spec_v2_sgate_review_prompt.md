# Opus 4.8 prompt: adversarial Level 1 v2 S-gate review

Review the complete Level 1 v2 draft as the X-line scientific and systems
reviewer. This is a pre-S-gate review, not an implementation task. Do not write
code, run a resource or comparative scout, generate escrow, create a lock or
outcome, choose thresholds from imagined results, or predict an arm.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2.md`
3. `reviews/fable_levels1_3_claim_graph_v2_1.md`
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md`
5. `reviews/opus_level1_spec_review.md`
6. `reviews/sol_level1_spec_review.md`
7. `reviews/fable_level1_spec_v2_closure.md`
8. `experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md`
9. `canonical/CLAIM_LEDGER.md`
10. `canonical/KILL_MATRIX.md`

No Level 1 comparative datum, scout, escrow, lock, or outcome exists. Review the
file, not Fable's summary. Recompute all cardinalities and support inequalities
independently.

## Decision standard

Decide whether v2 is complete enough for Kirill to sign the S-gate without a
later choice changing the world, estimand, unit, endpoint, arm trajectory, or
decision rule. A value is not harmless merely because it fits inside a named
field. In particular, model/optimizer/init details, panel composition,
thresholds, margins, seed aggregation, interval method, and invalidity handling
may be load-bearing.

## Required attacks

### X1. Registry, pairing, and scope

Verify the adjacent-pair construction, development/outcome allocation, role
randomization, `N3_min/max`, per-stratum capacity, and assignment-conditioned
claim. Decide whether distance 1 genuinely removes the donor-distance confound,
whether it is merely the narrowest possible version of that mediator, and what
a negative C1 can support under this deliberately conservative donor.

Check which finite population the estimator actually describes after six pairs
are assigned to development and one member of each outcome pair is assigned as
target. Reject any silent switch among all 60 `n`, 30 pairs, 24 outcome pairs,
or 24 realized target worlds.

### X2. Candidate and evaluator support arithmetic

Reconstruct the exact universe of:

- endpoint displacements `a,b`;
- acquisition semantic cells;
- evaluator-reserved cells;
- raw word lengths and parity-realizable padding;
- acquisition differences and evaluator-only differences.

Test the following suspected contradictions rather than assuming them:

1. Section 3 defines the cell/reserved universe with `|d| <= 125`, while
   section 7 says a panel built only from those reserved cells contains
   `d = 2n` and `2n +/- 1`, which exceed 125 for every registered world.
2. At `n = 125`, `2n + 1 = 251`, while the claimed grammar support is only
   `[-250,250]`; determine the correct strengthened inequality, including the
   near-miss probes rather than only `k*n`.
3. The prompt required held-out semantic displacement classes, but v2 reserves
   cells *within every difference class*. Decide whether this closes
   difference-lookup memorization or whether only the double-wrap stratum does,
   and repair the claim language accordingly.

Require an exact, implementable separation between a world-independent
acquisition universe and a target-specific sealed evaluator universe. Confirm
that opaque indices and serialized artifacts cannot expose semantic grouping or
`n` to learner/acquisition code.

### X3. Panel logic and anti-lookup certificate

Audit every panel stratum algebraically. In particular, for fixed `n`, EQ is
true exactly when `d mod n = 0`; test whether the phrase "for each residue class
... YES/NO balanced" is mathematically possible. Require a corrected panel
table giving, for every stratum, label rule, support, count rule, raw/semantic
novelty, and interaction with acquisition support.

Attack whether `d=2n` extrapolation certifies a learned period or instead tests
uncontrolled sequence-length, padding, position, or compositional
generalization. Determine the exact conditions under which a compositional
learner passing it is a feature. Verify that a lookup over contacted support,
syntax memorization, "unequal unless identical," abstention concentrated on
periodicity probes, or panel serialization leakage cannot pass.

### X4. Learner and arm trajectory completeness

Trace one full target/donor step and list every state that changes. Check whether
the following are actually frozen rather than named as candidates:

- embedding/positional scheme and maximum supported length;
- initialization and shared/member seed semantics;
- exact loss, ensemble aggregation used by evaluator, calibration, and ABSTAIN;
- AdamW learning rate, weight decay, betas, epsilon, decay groups, scheduler;
- minibatch sampling before history reaches 32, replay RNG, update ordering;
- committee disagreement definition and tie handling;
- whether ACTIVE and donor ACTIVE share or independently draw shortlist
  randomness, and whether that exogenous randomness belongs in the estimand;
- checkpoint and deterministic-resume state.

"Level 0 platform hyperparameters" is not an executable reference unless the
exact imported contract is named and scientifically justified for this task.
Decide whether committee disagreement at random initialization provides the
claimed early signal or only scopes C1 to a particular randomized heuristic.

### X5. Endpoint closure and invalidity

Determine whether open panel counts, accuracy/calibration/ABSTAIN/confident-lie
thresholds, solve-count floor, seed schedule, N6 margin, interval method,
leakage tolerances, and resource wall can change the endpoint or decision. If
yes, the draft cannot call them harmless signature confirmations; specify which
must be resolved in a revised spec before signature.

Audit block exclusion. Missing arms, non-finite states, and replay failures may
be outcome-related. Decide whether excluding up to four such blocks and applying
FPC to the survivors yields an identifiable finite-population estimand, or must
route the level directly to invalid/insufficient under a stricter rule.

### X6. Resource and gate decision

Estimate symbolically the dominant work: `B * S * E` scoring forwards plus
training and checkpoint evaluation. Decide what non-comparative evidence may
set B/resource wall before S-gate without becoming a forbidden comparative
scout. Give a gate table for neutral substrate, full implementation, resource
check, S-gate signature, comparative scout, lock, escrow, and outcome.

## Required output

Write `reviews/opus_level1_spec_v2_sgate_review.md`. Use exactly one verdict:

- `LEVEL1_S_GATE_SPEC_ACCEPTED`
- `REVISE_LEVEL1_V2_SPEC`
- `BLOCKED_LEVEL1_WORLD`
- `REJECT_LEVEL1_CERTIFICATE`

Findings first, ordered Critical/Major/Minor. Then answer X1-X6, give exact
mandatory revisions, state which v2 constructions are accepted, and provide a
precise Codex/Cursor authorization. Preserve every signed negative destination
and explicitly state whether any Level 1 execution remains forbidden.
