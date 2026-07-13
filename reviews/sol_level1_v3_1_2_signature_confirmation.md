# Sol review — Level 1 v3.1.2 bounded signature confirmation

Verdict: `LEVEL1_V3_1_2_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`

This is a bounded Y-line confirmation of
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`.
It checks only the v3.1.2 repairs against the previously approved Y-line
position. It does not reopen the accepted world, population, adjacent-only
scope, endpoint, estimand, inference family, selector, or gate order. No
code was written, no entropy was drawn, no data were run, and no
feasibility run, scout, lock, escrow, or outcome was created.

## Findings

### Critical

No critical Y-line issue remains. The v3.1.2 changes are bounded text and
arithmetic repairs; they do not alter the finite-population estimand,
allocation law, censoring endpoint, comparison family, margins,
predicates, or selector.

### Major

No major inference or randomization issue remains. The count
reconciliation, secret-keyed panel realization surface, and verifier
scope are compatible with the v3.1.1 approval.

### Minor

The three gate-3 enforcement notes from the v3.1.1 Y-line check remain
test obligations only: dummy/test seeds must be unable to emit real panel
artifacts; the public-root transcript must be asserted one-shot and
fail-closed; and noninterference canonicalization must change only the
opaque schedule-slot field. They do not introduce scientific degrees of
freedom.

## Check 1 — count reconciliation

F-2 changes only the arithmetic carried forward after `A_word = 128`.
The normative acquisition support is still `|d| ≤ d_acq = 125`, and the
per-class reservation rule remains `floor(3·N_d/10)`. With endpoints in
`[-128,128]`, the corrected counts are:

- `24,507` acquisition-support cells;
- `7,295` reserved cells;
- `17,212` non-reserved cells;
- `68,848` flat-pool realizations, or `34.424 × B`.

These figures replace stale headroom/count statements only. They do not
change allocation probabilities, the 24-pair outcome frame, the FPC, the
`N3` rule, endpoint definition, persistence/censoring, margin `60`, or
any predicate boundary.

## Check 2 — secret panel surface

F-3 preserves the approved public-root randomization reading. Public
reservation geometry remains reproducible from the public root; real panel
raw words, panel realizations, and panel order are keyed only by the
escrow-secret seed. The common secret-keyed domain skeleton now covers
S1, S2, S3, S4, and S5, with owned counters, `U(1)` no-consumption
behavior, canonical per-item draw order, and collision rejection scoped
to the relevant panel stratum/item process.

This fixes the remaining panel-surface gap without changing the
design-based draw. Public-root visibility still does not affect inclusion
probabilities, because allocation randomness is realized once before any
downstream information can condition a redraw. Secret panel realization
preserves sealed evaluation because public-root pool words cannot be
reused as real panel words, and dummy/test panels cannot emit or attest a
real artifact.

## Check 3 — distinct failure routes

The v3.1.2 text leaves the approved routing intact:

- `UNKNOWN` remains unresolved evidence, not success.
- All-censored compared arms resolve no predicate.
- Resource or feasibility failure is not statistical imprecision.
- Census refusal is a signed/operational refusal, not a projected
  half-width failure.
- Process/design invalidity remains separate from scientific censoring.

None of these states may be narrated as equivalence, boundary support, or
success.

## Check 4 — gate-3 enforcement notes

The v3.1.1 Y-line enforcement notes are carried without becoming new
scientific choices:

- The dummy/test seed rule is now binding for all five panel strata:
  dummy panels use a test-only seed and cannot emit real artifacts.
- The one-shot public-root transcript remains a later reviewed execution
  with process-fact witness scope only.
- The noninterference canonicalization rule remains exact: only the
  opaque schedule-slot field may be canonicalized or omitted.

These are implementation tests after author signature. They cannot tune a
threshold, alter a trajectory, change the endpoint, or move a verdict.

## Check 5 — bit-exact ambiguity

No remaining C2-C7 bit-exact ambiguity is found that would produce
divergent scientific artifacts under the accepted scope. F-3 supplies the
missing five-stratum secret panel realization domains; F-2 supplies the
normative counts under the existing per-class rule; F-1 scopes the
feature-null verifier to satisfiable non-structural nuisance checks while
explicitly treating `d`-reconstructing combinations as the legitimate
operational signal.

## Signature and gate boundary

This confirmation permits only Kirill's three author signatures:

1. `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`
2. `I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`
3. `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` incorporating v3.1, v3.1.1, and
   v3.1.2

It authorizes no implementation, entropy draw, data run, feasibility
execution, comparative scout, `N3` selection, lock, escrow, or outcome.
After author signature, the next boundary is implementation/tests only;
the public-root draw and secret real-panel escrow remain later gated
single executions.
