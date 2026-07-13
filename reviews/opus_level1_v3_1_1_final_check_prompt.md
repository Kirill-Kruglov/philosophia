# Opus 4.8 prompt: final bounded check of Level 1 v3.1.1

Perform the final bounded X-line check of the v3.1.1 correction. Do not reopen
the world, 24-pair frame, adjacent-only scope, or inference family; do not write
code, draw entropy, run data, create escrow/lock/outcome, or predict an arm.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`
4. `reviews/opus_level1_v3_1_signature_check.md`
5. `reviews/sol_level1_v3_1_signature_check.md`
6. `reviews/fable_level1_spec_v3_1_1_closure.md`

No Level 1 artifact has executed. Check only the bounded corrections C1-C7.

## O1. S4 and the operational-certificate boundary

Verify support, remainders, endpoint bounds, parity, offset-only construction,
and raw-length arithmetic at `n=66`, representative odd/even worlds, and
`n=125`.

Then test the **full joint** nuisance claim. The correction appears to prove only
marginals:

- YES = `(padding A, length class L_A)` plus `(padding A+1, length class L_B)`;
- NO = `(padding A+1, length class L_A)` plus `(padding A, length class L_B)`.

Thus `(padding class, ordered side-length class)` may be another XOR even though
each marginal multiset is identical. Recompute it explicitly.

Also confront the logical boundary: raw tokens determine lengths and token
counts; with the learned net skill they determine `(a,b)` and hence `d`. A joint
vector containing padding and lengths can reconstruct structural `d`, so it
cannot be label-conditionally identical when labels intentionally differ by
`d mod n`. Decide whether C1's verifier is internally contradictory.

The permitted bounded resolution is **not another endless masking table**. If
the construction removes the original `n`-free parity/symmetry shortcut, accept
the honest authorial scope:

`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`

meaning recovered/contact-anchored `n` plus correct arithmetic on novel `d`, not
an abstract representation claim. Require the verifier to cover only a precisely
declared non-structural nuisance family and explicitly allow combinations that
reconstruct `d`; it must not assert full raw-feature joint identity. If even an
`n`-free rule not reconstructing `d` still separates labels, reject and give the
smallest concrete repair.

Check whether increasing `A_word` from 126 to 128 changes the acquisition cell
count/reserve/headroom. If so, require corrected exact counts rather than the
stale 24,003/67k figures carried from v3.

## O2. Generator/model closure

Verify C2-C5 close the prior gaps: stratum/pair domains, counter ownership, S4
secret-seed word ranks, S5 eligibility, token decoder, public-root/panel-secret
separation, input length 277, fan-in and seed decode, slot canonicalization.
Report only trajectory-divergent ambiguities.

In particular, ensure the public root cannot reconstruct any real panel content,
and dummy panel seeds cannot pass the real-artifact attestation gate.

## O3. Scope/signature readiness

State exactly what the operational certificate proves and forbids. Decide whether
the three author tokens make the irreducible cyclic-world limitation loud enough
for signature, or whether a scientific blocker remains.

## Output

Write `reviews/opus_level1_v3_1_1_final_check.md`. Use exactly one verdict:

- `LEVEL1_V3_1_1_XLINE_APPROVED_FOR_AUTHOR_SIGNATURE`
- `REVISE_LEVEL1_V3_1_1_SCOPE_TEXT`
- `BLOCKED_LEVEL1_OPERATIONAL_CERTIFICATE`

Lead with findings, answer O1-O3, and give only bounded edits. This check
authorizes no implementation, entropy, feasibility, scout, lock, escrow, or
outcome.
