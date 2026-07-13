# GPT-5.6 Sol review prompt: Level 1 endpoint and inference specification

Review the consolidated Level 1 draft as the independent causal/statistical
Y-line. This is pre-S-gate and pre-comparative-data. Do not write code, invent
effect sizes, tune margins, create a scout/lock/escrow/outcome, or predict a
winner.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2_1.md`
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md`
4. `canonical/CLAIM_LEDGER.md`
5. `canonical/KILL_MATRIX.md`
6. `essay/climbing-the-wall-of-experience.md`, §§VI–VII
7. `references/LITERATURE_MAP.md`

The claim graph and endpoint family are signed; exact margins, estimator,
world/block schedule, and scout sizing are not. No Level 1 comparative datum
exists.

## Required review

### S1. Experimental and variance unit

Under fixed R/L cyclic semantics, the oracle truth table is determined by `n`.
Assess the draft's treatment of distinct `n` values as world units and learner
seeds as repeated measures. Decide whether target+unique-donor is the correct
inferential block and how finite sampling without replacement from an N1 set
changes the variance model. Repeated `n`, seeds, queries, and checkpoints must
not create pseudoreplication.

Determine whether donor/target pairing within size strata but with unequal `n`
identifies target-specific coupling or mixes it with donor-target difficulty.
State the narrow estimand it can support.

### S2. Censoring and RMST

Formalize the paired ACTIVE/YOKED right-censored endpoint at common B. Check:

- whether censoring is administrative and common-horizon;
- how persistent solve times are formed from checkpoint cadence;
- how seeds nest inside finite world blocks;
- whether RMST_YOKED − RMST_ACTIVE is the right orientation;
- what estimator and uncertainty family is valid for paired finite blocks;
- what happens when few/no arms solve;
- how `UNKNOWN` differs from equivalence and boundary.

Do not choose a numeric B, cadence, or threshold. State the evidence required to
choose them before comparative data.

### S3. Solve certificate and balanced panel

Determine whether a balanced held-out EQ panel measures recovery of hidden
cyclic structure rather than memorized syntactic classes. Require panel strata
and a construction that cannot leak `n` to learners. Audit calibration,
ABSTAIN, confident-lie, repeated-query, and class-balance rules. State which
thresholds can come from mathematical baselines, which require external anchors,
and which cannot be learned from the comparative scout.

### S4. Three-arm comparisons and total selector

Write the minimum simultaneous comparison family needed for:

- C1 ACTIVE versus YOKED;
- YOKED geometry versus RANDOM-STATIC;
- the total Level 2 mode selector.

Define the direction of superiority, equivalence, non-inferiority, and
non-superiority on the common benefit scale. Check familywise/multiplicity
handling, non-transitive intervals, least-adaptive tie priority, and the
RANDOM-superior anomaly. N6 margins must represent scientific relevance and
freeze before the scout.

### S5. Development contrast scout

Specify exactly what the non-citable scout may estimate and a defensible N3
precision rule without an invented effect size. Check whether the same
development worlds/policies can estimate censoring and paired variance without
tuning the endpoint. State minimum block/stratum coverage conceptually and what
resource stop is outcome-independent.

### S6. Leakage and invalidity statistics

Assess shuffled answers, parameter shift, encoding probes, donor balance, block
invalidity, and missing/failed runs. State which failures invalidate a block,
which invalidate the design, and why no invalid block may simply be excluded.

Use primary sources only if a source materially constrains the analysis. Do not
expand into a general literature survey or use secondary chat links as evidence.

## Required output

Write `reviews/sol_level1_spec_review.md`. Use exactly one verdict:

- `INFERENCE_SPEC_ELIGIBLE_FOR_CLOSURE`
- `REVISE_LEVEL1_INFERENCE`
- `BLOCKED_FINITE_WORLD_UNIT`
- `REJECT_LEVEL1_ESTIMAND`

Provide Critical/Major/Minor findings, answers S1–S6, a corrected estimand and
comparison table, the pre-scout freeze list, and an explicit boundary between
what may be implemented now and what must wait for S-gate signature.
