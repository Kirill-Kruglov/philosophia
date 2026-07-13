# GPT-5.6 Sol prompt: bounded Level 1 v3.1 signature check

Perform the final bounded Y-line signature check of v3.1. Do not reopen the
24-pair frame or adjacent-only scope, write code, draw entropy, run data, create
escrow/lock/outcome, or tune a rule.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
3. `reviews/sol_level1_spec_v3_final_review.md`
4. `reviews/opus_level1_spec_v3_final_review.md`
5. `reviews/fable_level1_spec_v3_1_closure.md`
6. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`

No Level 1 datum exists. Check only the bounded repairs A1-A10.

## Required checks

### S1. One-shot randomization

Verify that A2 restores a genuine design-based draw and known inclusion
probabilities. Audit:

- root timing, durable transcript, no-redraw failure path, witness scope;
- HMAC/domain/counter encoding;
- exact unbiased `U(r)` and Fisher-Yates;
- counter/reset behavior across the three strata;
- whether domains require explicit stratum/pair components;
- `D` before development, roles once, `R_h` only after N3;
- conditioning and impossibility of post-information regeneration.

Distinguish a reproducibility defect from the explicitly procedural threat
model; do not demand cryptographic independence the programme does not claim.

### S2. Estimator and zero-variance cases

Check A9's `s_h^2`, `v_h`, `Vhat`, Satterthwaite df, critical quantile, strict
boundary behavior, and census rule. Require a defined rule when all `v_h=0` at
`N3<24` and when only some components are zero.

Notice that at `N3=24`, FPC is identically zero, so every projected half-width is
zero regardless of the development fallback. Therefore the statistical branch
“projection fails at 24” appears unreachable. Decide whether this is a harmless
consequence of the finite-frame census or contradictory prose that must be
corrected. Separate statistical precision from resource/invalidity inability to
run all 24 blocks.

### S3. Directional determinacy

Verify every row of the adopted Sol table against `SUP`, `NI`, `NONSUP`, and
`EQ`, including:

- both all-censored;
- X events/Y none;
- X none/Y events;
- both events;
- exact equality at +/-60.

Confirm that C1 can earn a positive or distance-1 negative only through the
correct ordered A-Y interval and that no one-sided predicate becomes equivalence
by narration.

### S4. N3 development projection

Check projection over all three contrasts, use of two development blocks per
stratum, fallback `B^2`, Satterthwaite df, maximum half-width, and smallest-N3
selection. Determine whether `B^2` is the intended Popoviciu upper bound for a
population variable in `[-B,B]`, notwithstanding that an unbiased two-point
sample variance can numerically reach `2B^2`; require the text to distinguish
those concepts if necessary.

### S5. Calibration and invalidity statistics

Verify per-stratum Brier over all items, shuffled-answer run count, byte-identity
noninterference, divergence routing, and single re-execution. Check whether
world-independent slot identifiers must be canonicalized before literal byte
comparison. Ensure controls remain finite-scope invalidity gates, not evidence.

### S6. Signature readiness

List any remaining verdict-moving procedure. Classify it as blocking, bounded
text correction, or implementation-test detail. Do not reopen accepted design
choices unless the formulas are inconsistent.

## Output

Write `reviews/sol_level1_v3_1_signature_check.md`. Use exactly one verdict:

- `LEVEL1_V3_1_YLINE_SIGNATURE_APPROVED`
- `REVISE_LEVEL1_V3_1_INFERENCE`
- `BLOCKED_LEVEL1_V3_1_RANDOMIZATION`

Lead with findings, answer S1-S6, and give exact bounded edits and gate boundary.
UNKNOWN/all-censored never becomes equivalence, boundary, or success. This review
authorizes no entropy draw, feasibility run, scout, lock, escrow, or outcome.
