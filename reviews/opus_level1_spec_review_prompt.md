# Opus 4.8 review prompt: Level 1 world and learner specification

Review the consolidated pre-S-gate Level 1 specification as an adversarial
scientific and systems reviewer. This is narrower than the completed claim-graph
review. Do not write implementation code, create a scout/lock/escrow/outcome, or
predict which arm will win.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2.md`
3. `reviews/fable_levels1_3_claim_graph_v2_1.md`
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md`
5. `experiments/level_1_contact/README.md`
6. `canonical/CLAIM_LEDGER.md`
7. `canonical/KILL_MATRIX.md`
8. `ROADMAP.md`
9. `essay/climbing-the-wall-of-experience.md`, especially §§VI–VII

Level 0 is valid platform evidence only. The claim graph is signed. No Level 1
comparative datum, scout, escrow, lock, or outcome exists.

## Review objective

Decide whether the cyclic-world, learner, independent-donor, and fail-closed
contracts are precise enough to begin implementing pure substrate modules, and
identify exactly which scientific choices must close before implementation,
before the S-gate, before a comparative scout, and before lock.

## Required attacks

### O1. Is `Z/n` an adequate experimental world?

- Confirm or refute the draft's statement that `n` is the complete world
  identity under fixed R/L and origin-EQ semantics.
- Test the consequence: duplicate `n` values are repeated learner measurements,
  not independent world blocks.
- Check that `n_donor != n_target` within a declared size stratum breaks
  instance adaptivity without manufacturing an easy mismatch.
- Determine whether finite distinct `n` values provide enough genuinely
  heterogeneous blocks for the intended claim, or whether a second hidden
  parameter is scientifically necessary.
- Verify the N1/N2 wrap-around constraint. State the exact mathematical coverage
  condition without choosing an unsupported range.

If the minimal world cannot identify C1, say so now. Give the smallest repair;
do not enlarge the curriculum for aesthetic reasons.

### O2. Query grammar and geometry

Every R/L word reduces to an integer displacement, so many syntactically
different EQ pairs are oracle-equivalent. Audit:

- whether candidate cells should be raw word pairs, displacement-difference
  classes, or a locked two-level design preserving both structure and syntax;
- `(u,v)` symmetry, trivial `(u,u)` positives, inverse/cancellation shortcuts,
  duplicate semantic classes, and label imbalance;
- whether ACTIVE can win through syntactic multiplicity rather than target
  adaptation;
- whether a tractable shortlist changes the estimand;
- whether RANDOM-STATIC truly samples the same candidate geometry.

Require a canonical candidate-pool contract and an enumeration verifier.

### O3. Learner and acquisition behavior

Audit what must be frozen about model architecture, input encoding, calibration,
online updates, replay/history view, initialization pairing, and optimizer. Check
whether `abs(p_equal - 0.5)` from a single head is a meaningful uncertainty
policy before calibration exists. Evaluate deterministic ties, repeated queries,
selection compute, and the risk that ACTIVE scores all candidates while controls
receive different computational work.

State what may be implemented as a neutral interface now and what would encode a
scientific choice too early.

### O4. Certified solve and negative controls

Attack the balanced EQ panel as a truth criterion. Can high held-out EQ accuracy
be achieved without recovering the hidden order? Are word-length/relation cells,
calibration, ABSTAIN, and confident-lie gates sufficient? Specify the minimum
family-independent certificate for the cyclic world.

Review the shuffled-answer control, parameter-stratum shift, and encoding-only
probe. Distinguish legitimate post-contact query-sequence mediation from
pre-contact leakage. State whether any control belongs in the scientific outcome
or only in design invalidity.

### O5. Donor and escrow sequencing

Check the target+donor block, one-to-one/no-reuse rules, hash timing, target-arm
pairing, execution order, and the procedural LOCAL_LLAMA wrapper. Identify any
way donor results, hidden strata, evaluator panels, or plaintext can leak into
the learner or researcher path.

### O6. Gate decision

Produce a gate table for:

- neutral substrate implementation;
- trajectory-bearing learner implementation;
- S-gate signature;
- comparative scout driver;
- Level 1 lock and escrow.

Do not allow "we will preregister later" for a choice that changes the world,
estimand, unit, endpoint, or arm behavior.

## Required output

Write `reviews/opus_level1_spec_review.md`. Use exactly one verdict:

- `SUBSTRATE_IMPLEMENTATION_ELIGIBLE`
- `REVISE_LEVEL1_SPEC`
- `BLOCKED_CYCLIC_WORLD`
- `REJECT_LEVEL1_IDENTIFIABILITY`

Provide findings ordered Critical/Major/Minor, answers O1–O6, exact mandatory
revisions, a candidate-pool recommendation, and the precise next authorization
for Codex/Cursor. Preserve every signed negative destination.
