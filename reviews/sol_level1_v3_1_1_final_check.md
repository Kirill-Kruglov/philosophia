# Sol review — Level 1 v3.1.1 final bounded check

Verdict: `LEVEL1_V3_1_1_YLINE_APPROVED_FOR_AUTHOR_SIGNATURE`

This is a bounded Y-line check of C2–C7 in
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`.
It does not reopen the accepted world, the 24-pair finite frame,
adjacent-only C1 scope, or the total selector. No code was written, no
entropy was drawn, no feasibility or comparative datum was run, and no
scout, lock, escrow, or outcome was created.

## Findings

### Critical

No critical statistical or randomization blocker remains in C2–C7. The
v3.1.1 correction supplies the bounded text needed after the v3.1 Y-line
review: independent allocation domains, a public-root/secret-panel split,
the all-zero variance bypass, corrected census prose, corrected fallback
wording, and canonicalized noninterference surfaces.

### Major

No major inference correction remains. The remaining work is
implementation/test enforcement after author signature, not further
scientific text design.

### Minor

1. The implementation tests should assert that real panel emission is
   impossible under the dummy/test seed and requires the locked escrow
   environment attestation.
2. The allocation transcript test should assert that the public root is
   committed exactly once, that the path pre-exists check is fail-closed,
   and that witness attestation covers only process facts.
3. The noninterference test should fail if canonicalization changes
   anything except the opaque schedule-slot field.

These are enforcement details already implied by C2, C3, C5, and C7; they
do not require another design cycle.

## Check 1 — randomization

C2 repairs the allocation stream-order defect. The allocation domains are
now independently scoped:

- `("L1","alloc","dev", h)` for development-pair selection per stratum;
- `("L1","alloc","role", pair_slot)` for exactly one role bit per
  canonical outcome pair;
- `("L1","alloc","sample", N3, h)` for outcome sampling per stratum
  after `N3`.

Each domain owns its own counter starting at zero. Rejection redraws
increment only that domain's counter; `U(1)` consumes no digest and leaves
the counter unchanged. Canonical processing order is `h=1,2,3`, with pair
slots ascending inside strata. This removes the prior ambiguity between
counter-reset and continuous-counter implementations.

The one-shot public root remains a genuine design-based randomization
source: it is drawn once from the OS CSPRNG after signatures and before
development use, committed durably, refused if the transcript path already
exists, and never redrawn. Its public visibility after durable commitment
does not alter inclusion probabilities or the finite-population reading:
randomness is realized before downstream information can condition a
redraw, and no post-information regeneration is allowed. Conditional on
the realized `D`, roles, and later sampled `R_h`, inclusion probabilities
remain known as `π_h = n_h/8`.

C3 correctly separates this public root from the secret evaluator seed.
The public root derives allocation, pool reserve and zone-1 realizations,
model initializations, shortlists, replay, controls, and feasibility
streams. It does not derive real panel content, real panel realizations,
panel ordering, encryption salt, or escrow plaintext. Those are keyed by a
separate 256-bit escrow-secret seed generated later inside the locked
escrow environment. This preserves both reproducibility for allocation
and sealed evaluation for the panel.

## Check 2 — inference

C6 lands the required inference corrections:

- If all `v_h=0` at `N3<24`, the interval is defined directly as
  `[Δhat, Δhat]`; no degrees of freedom and no `t` quantile are evaluated.
- If only some `v_h=0`, their denominator terms are omitted exactly as
  in A9.
- The decision artifact must label an all-zero non-census interval as
  "estimated zero sample variance, not census certainty."
- `B²` is correctly named as Popoviciu's finite-population variance bound
  for a variable in `[-B,B]`, not as the maximum two-point unbiased sample
  variance.
- Any observed finite nonzero `s²_dev` is used as observed, even if it
  exceeds `B²`.
- The projection remains maximum-over-three contrasts `{A-Y, Y-R, A-R}`.

The directional guard and margin semantics carry forward correctly:
all-censored compared arms resolve no predicate; one-sided predicates may
resolve when exactly one arm has events; equivalence requires both arms to
have events; `SUP`, `NI`, and `NONSUP` use strict one-sided inequalities;
`EQ` uses inclusive `[-60,+60]` bounds subject to the guard. A one-sided
predicate cannot become equivalence by narration.

## Check 3 — census

C6 fixes the unreachable "projection fails at 24" branch. Candidates
below 24 use projected half-widths under the frozen rule. If none below
24 passes, the statistical rule selects the 24-block census; at `N3=24`,
`n_h=8`, the FPC is zero, and the projected half-width is identically
zero.

The correction also preserves the needed distinction between statistical
precision and operational feasibility. Resource infeasibility, process or
design invalidity, feasibility-gate failure, or Kirill's signed refusal
to run the census may block a lock, but none of those is statistical
imprecision. Census refusal, resource failure, UNKNOWN, and all-censored
outcomes remain separate routes.

## Check 4 — surfaces

C3 and C5 close the surface ambiguity. The public root is appropriate for
allocation and training reproducibility, while the secret escrow seed
protects real panel content and ordering. Dummy panels use a declared
test-only seed and cannot emit real artifacts.

C5 defines noninterference comparison by canonicalizing only the opaque
schedule-slot field, or omitting it if learner code never reads it, before
byte comparison across development worlds. The slot-to-world mapping
stays outside learner/acquisition reach. The required test is strong
enough: canonicalization must be the only permitted difference, and no
`n`, pair id, world hash, target-specific length, or panel-root material
may appear in the pre-contact bundle.

This preserves pre-contact noninterference and sealed evaluation without
pretending that public allocation reproducibility is cryptographic
independence.

## Check 5 — signature packet

The operational-modulus token is a scope choice, not a statistical
inference change. It names the certificate's honest meaning after the S4
repair: operational recovery of a contact-anchored modulus sufficient to
classify novel opposite-corner differences. It does not alter the C1
estimand, finite-population frame, comparison family, selector, censoring
rules, margins, or estimator.

All verdict-moving statistical procedures are frozen: allocation timing
and domains; public-root and secret-panel separation; estimator and df
rules; zero-variance handling; strict/inclusive predicate boundaries;
determinacy guard; three-contrast N3 projection; census behavior; and
resource/invalidity routing.

## Signature and gate boundary

Author signature may proceed on the three-token packet in C7:

1. `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`
2. `I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`
3. `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` incorporating v3.1 and v3.1.1

This approval authorizes author signature only. It authorizes no
implementation, entropy draw, feasibility run, comparative scout, N3
selection, lock, escrow, or outcome. After signatures, the next boundary
is implementation/tests; the public-root draw remains a later reviewed
single execution; real panel escrow remains later and secret-keyed.

UNKNOWN, all-censored, resource failure, feasibility refusal, census
refusal, and process/design invalidity remain distinct. None may be
narrated as equivalence, boundary support, or success.
