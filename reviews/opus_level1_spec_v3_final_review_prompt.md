# Opus 4.8 prompt: final Level 1 v3 scientific and implementation-contract review

Perform the final X-line review of the Level 1 v3 specification. This is the
last pre-signature audit, not a code task. Do not implement modules, run
feasibility/comparative data, generate escrow, create a lock/outcome, tune a
constant, or predict an arm.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2_1.md`
3. `reviews/opus_level1_spec_v2_sgate_review.md`
4. `reviews/sol_level1_spec_v2_sgate_review.md`
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
6. `reviews/fable_level1_spec_v3_closure.md`
7. `canonical/CLAIM_LEDGER.md`
8. `canonical/KILL_MATRIX.md`

No Level 1 code or datum exists. Review the actual v3 file independently. The
standard is stronger than conceptual adequacy: a separate implementer must be
able to produce the same pool, panel, trajectory, event, and decision without
making an unreviewed choice.

## Required attacks

### X1. Three-zone enumeration and exact generators

Recompute all cell counts and edge support. Confirm `A_word=126`, `d_acq=125`,
and `2n +/- 1` realizability. Then audit whether the generators are actually
specified:

- exact integer rule implementing “30% reserved” independently within classes;
- exact ordering/orientation of cells;
- exact four raw realizations per cell, including word token ordering, padding
  draw, collision rejection, and parity;
- exact seed/counter encoding and unbiased integer sampling;
- exact treatment when fewer requested reserved realizations exist;
- exact pool and panel serialization.

Approximate cardinality is fine for a headroom argument, but no approximate or
“locked draw” placeholder may determine learner input. Identify every remaining
implementation choice that can change a trajectory.

### X2. Panel constructibility and metadata sealing

Independently construct every row at `n=66` and `n=125`. Check:

- availability of 124 S1 reserved items under repeated residues;
- the S2 `n=125` zone crossing and whether its “difference novelty” column is
  accurate;
- S3 distinct `d=0` words;
- S4 exact raw words and length matching for odd/even near misses;
- S5 `n+2`, length >=100, and imbalance >=60 at both edges;
- exact label/count totals and compatibility of accuracy, ABSTAIN,
  confident-lie, and Brier conditions.

The table uses phrases such as “lowest unused reserved index,” “locked draw,”
“length-matched,” “matched,” and “locked d.” Decide whether these are executable
rules or unresolved endpoint choices.

Audit the claimed byte-identical exposed surface. Panel-local ids and schema can
be identical, but salted integrity digests/ciphertexts and cell mappings should
differ across worlds. Determine whether “hashes byte-identical” is impossible or
whether the spec means a narrower learner-visible surface. Require a precise
separation among learner-visible metadata, researcher-visible commitments, and
sealed evaluator mappings.

### X3. Model and optimizer bit-level contract

Trace the proposed 273-token transformer. Require answers for:

- causal versus bidirectional attention;
- Q/K/V/output projections, biases, storage orientation, and attention scale;
- PAD query/key behavior and whether every all-masked row is defined;
- LayerNorm placement, final LayerNorm, and epsilon;
- token and positional embedding initialization, head/init draw order, and
  domain-separated seed derivation;
- MLP biases and residual ordering;
- dtype/device/determinism contract;
- gradient clipping or explicit none;
- AdamW update semantics and exact decay membership;
- loss reduction, replay sampling, optimizer/zero ordering, and checkpoint
  cadence/state.

“Two-layer pre-LN transformer” is not enough if two faithful implementers can
produce different trajectories. Verify the 2-replicate master seed schedule is
actually enumerated, not only counted.

### X4. Controls and feasibility contract

Audit the shuffled-answer and encoding-probe invalidity gates. “Top-1 <= 1/6
over 12 worlds” is not a protocol: specify/check probe model, train/eval split,
features, repetitions, null statistic, and finite-sample decision. Likewise,
state how many shuffled runs and which seeds make “zero certified solves” a
defined gate without arbitrary false invalidation.

RANDOM-STATIC feasibility does not exercise the dominant `B*S*E` ACTIVE scorer.
Decide whether the non-comparative check must include a scorer-only timing path
or a single ACTIVE run while still forbidding arm contrasts. Check whether a
single-arm censoring indicator may trigger architecture/B amendment without
silently tuning the scientific endpoint.

### X5. Failure and endpoint semantics

Check the one-re-execution rule for deterministic, audit-safe behavior. Decide
whether a trajectory that reaches a persistent solve before later becoming
non-finite is always forced to censored-at-B, and require that choice to be
explicit. Verify missing checkpoints, partial artifacts, seal failures, and
prefix divergence cannot be classified after seeing performance.

Audit whether global Brier on non-abstained items is coherent with the heavily
NO S1 stratum and whether excluding abstentions from Brier permits selective
calibration reporting despite per-stratum abstain caps. This is a certificate
question, not a request to optimize a threshold.

### X6. Gate verdict

List accepted v3 closures that must not be reopened. Distinguish:

- genuine blockers requiring a v3.1 addendum before signature;
- implementation details safely delegated under an exact verifier;
- non-comparative feasibility facts that may be observed only after a reviewed
  driver;
- authorial scope choices already isolated in S-1.

## Required output

Write `reviews/opus_level1_spec_v3_final_review.md`. Use exactly one verdict:

- `LEVEL1_V3_XLINE_ACCEPTED_FOR_SIGNATURE`
- `REVISE_LEVEL1_V3_CONTRACT`
- `BLOCKED_LEVEL1_IMPLEMENTABILITY`
- `REJECT_LEVEL1_V3_CERTIFICATE`

Lead with Critical/Major/Minor findings. Answer X1-X6, give exact mandatory
edits if any, and provide a precise implementation/gate authorization. Preserve
the adjacent-only negative scope and every signed negative destination. No
Level 1 execution is authorized merely by writing this review.
