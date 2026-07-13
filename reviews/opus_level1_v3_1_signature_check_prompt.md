# Opus 4.8 prompt: bounded Level 1 v3.1 signature check

Perform a final **bounded signature check** of the v3.1 addendum. Do not reopen
accepted v3 world/estimand choices, invent a new curriculum, write code, draw
entropy, run data, create escrow/lock/outcome, or predict an arm.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
3. `reviews/opus_level1_spec_v3_final_review.md`
4. `reviews/sol_level1_spec_v3_final_review.md`
5. `reviews/fable_level1_spec_v3_1_closure.md`
6. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`

No Level 1 code or datum exists. Check only whether A1-A10 land the mandated
repairs without a new contradiction.

## Required checks

### O1. S4 joint-feature leakage

Do not test features one at a time. Reconstruct the complete 16-item S4 feature
table for general `n` and separately `n=125`. Test **joint** feature vectors and
low-order combinations, especially:

- `(side parity, symmetric/offset)`;
- `(magnitude equality, padding pattern)`;
- ordered side lengths, endpoint magnitudes, max/min magnitude, and split type;
- interactions among parity, symmetry, and length.

The addendum claims zero MI for each marginal feature. Verify the suspected XOR:
general YES appears to use `(sym, parity n)` and `(off, parity n+1)`, while NO
uses `(sym, parity n+1)` and `(off, parity n)`; the `n=125` special table appears
to retain the same joint separation. If a fixed non-modular rule classifies S4,
the signature check fails even though every marginal is balanced.

Decide the smallest bounded repair. It may require a different split table or a
small increase of `A_word`; do not accept a verifier that checks only individual
mutual information. A valid feature-null condition must cover the **joint
declared nuisance-feature vector**, with identical label-conditional multisets
or an equally strong exact proof. Recheck realizability and acquisition
uncontactability at both registry edges.

### O2. Generator and serialization exactness

Trace A2-A4 as an implementer:

- HMAC component encoding and byte-to-uint seed conversion;
- counter ownership/reset across strata and domains;
- whether dev/sample domains need an explicit stratum component to avoid
  accidental repeated permutations;
- Fisher-Yates and reserve rounding;
- cell orientation/order, word rank/unrank, four-realization collision handling;
- reserved-cell availability/consumption for every panel row;
- distinction between model token ids and serialized ASCII token bytes;
- schema/content/ciphertext surfaces.

Identify only gaps that let two conforming implementations differ. Cosmetic
preferences are not blockers.

### O3. Model trajectory uniqueness

Verify A5 fixes all C-3 items: bidirectional mask behavior, scale/softmax,
residual/LN order, final LN, biases, epsilon, init distribution and draw order,
fresh per-tensor generator, parameter groups, replay sharing, dtype/environment,
checkpoint state, exact replicate/member/arm identifiers. Check the expression
converting the first 8 PRF bytes into a PyTorch seed and require explicit
big-endian bytes-to-integer semantics if ambiguous.

### O4. Endpoint, routing, and controls

Verify:

- per-stratum Brier uses all items and is jointly satisfiable with count/ABSTAIN/
  confident-lie constraints;
- solve-before-divergence versus divergence-before-window is exclusive;
- pre-fault replay and seal-breach routes are deterministic;
- byte-identity noninterference bundle does not contain different world-slot
  bytes while claiming literal identity (state the required alpha-renaming or
  canonical placeholder if needed);
- shuffled controls are fully reproducible;
- scorer feasibility records no scientific series.

### O5. Signature and implementation boundary

State whether any remaining issue is:

1. signature-blocking scientific/trajectory ambiguity;
2. a one-paragraph v3.1 correction;
3. safely enforceable by implementation tests without changing the contract.

## Output

Write `reviews/opus_level1_v3_1_signature_check.md`. Use exactly one verdict:

- `LEVEL1_V3_1_XLINE_SIGNATURE_APPROVED`
- `REVISE_LEVEL1_V3_1_ADDENDUM`
- `BLOCKED_LEVEL1_V3_1_CERTIFICATE`

Findings first, then O1-O5, exact bounded edits if needed, and gate authorization.
Preserve adjacent-only scope and all negative destinations. The review itself
authorizes no entropy draw, feasibility run, scout, lock, escrow, or outcome.
