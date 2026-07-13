# Sol review — Level 1 v3.1 bounded signature check

Verdict: `REVISE_LEVEL1_V3_1_INFERENCE`

This is a bounded Y-line signature check of the v3.1 repairs A1–A10 only.
It does not reopen the 24-pair outcome frame, adjacent-only C1 scope, the
three-zone support design, or the signed total selector. No entropy was
drawn, no feasibility or comparative run was executed, and no scout,
escrow, lock, or outcome was created.

## Findings

### Critical

No remaining critical design rejection is found. A2 replaces the v3
public-string pseudo-random allocation with a genuine one-shot entropy
mechanism, and the estimator/predicate repairs adopt the requested
finite-frame structure. The design is no longer blocked on
randomization-as-such.

### Major

1. **Allocation stream order is still under-specified.** A2 gives exact
   HMAC, `U(r)`, and Fisher-Yates mechanics, but allocation domains for
   `dev`, `role`, and `sample` do not include stratum/pair components.
   That is acceptable only if the spec states a single canonical
   stateful counter and draw order across strata/pairs. Otherwise
   implementers could reset counters per stratum/pair and silently make
   correlated or duplicated selections.

   Mandatory bounded edit: in A2, add either explicit domain components
   such as `("L1","alloc","dev",h)`, `("L1","alloc","role",pair_slot)`,
   and `("L1","alloc","sample",N3,h)`, or state that each listed domain
   has exactly one persistent counter, never reset, consumed in canonical
   order `h=1,2,3`, then ascending pair slot within each stratum. The
   same rule must cover rejection draws and `r=1` no-consumption cases.

2. **The N3 prose still contains an unreachable statistical branch.**
   A9 keeps "if no candidate through 24 passes: no lock." But at
   `N3=24`, `n_h=8` and `1-n_h/8=0`, so every projected half-width is
   exactly zero regardless of development variance or fallback. Therefore
   the statistical precision rule cannot fail at 24.

   Mandatory bounded edit: replace the "fails at 24" statistical prose
   with: candidates below 24 may fail the projected precision rule; if
   none below 24 passes, the frozen rule selects the 24-block census. A
   lock can still be blocked by resource infeasibility, process
   invalidity, feasibility-gate failure, or a signed decision not to run
   all 24 blocks, but not by projected sampling half-width at the census.

3. **The `B²` fallback conflates two variance concepts.** A9 says
   `s²=B²` is the bounded-difference maximum because differences lie in
   `[-B,B]`. That is Popoviciu's population-variance upper bound for a
   variable in that interval, not the maximum possible unbiased two-point
   sample variance; the latter can reach `2B²` when the two development
   values are `-B` and `+B`.

   Mandatory bounded edit: state explicitly that the zero/undefined
   fallback is a conservative finite-population variance cap, not the
   maximum two-point sample variance. Also state that any observed
   nonzero development `s²_dev` is used as observed, even if it exceeds
   `B²`, unless a separate pre-scout cap is explicitly justified and
   frozen.

4. **All-zero variance at `N3<24` needs an operational df bypass.** A9
   says the interval is a point and reports estimated zero sample
   variance, which is scientifically coherent, but the Satterthwaite df
   and critical quantile are undefined when every `v_h=0`.

   Mandatory bounded edit: add that if all `v_h=0` at `N3<24`, the
   interval is defined directly as `[Δhat, Δhat]`, no `t` quantile is
   evaluated, and the decision artifact must label it "estimated zero
   sample variance, not census certainty."

### Minor

1. **Witness scope should be explicit.** A2's procedural witness should
   attest only process facts: transcript path absent before draw, exactly
   one OS-CSPRNG call, durable write/commit, environment fingerprint, and
   no redraw. It need not and should not claim cryptographic independence
   from operators.

2. **Transcript visibility should be named.** Because A2's root drives
   panel and learner stochasticity, the spec should state whether root
   bytes are public immediately, sealed until an audit point, or visible
   only to the reviewed driver. This is not a demand for cryptographic
   independence, but it is needed to keep the A4 pre-outcome surface
   statement unambiguous.

3. **World-slot canonicalization belongs in tests.** A7 correctly maps
   handles through world-independent slots before byte comparison; the
   implementation tests should assert canonical slot serialization before
   literal byte-identity checks.

## S1 — one-shot randomization

A2 repairs the v3 randomization blocker in substance. A single 32-byte
OS-CSPRNG root, generated after signature and before any development use,
with a durable no-redraw transcript, restores a real random mechanism.
Conditional on the realized `D`, roles, and later `R_h`, the design can
use known inclusion probabilities `π_h=n_h/8` for sampled outcome blocks,
and the FPC is justified for `N3<24`.

The HMAC construction is adequate for reproducible pseudo-random streams
after the one real entropy draw: length-prefixed domain components,
decimal integer rendering, and a `uint64_be` counter avoid ordinary
domain concatenation ambiguity. The exact `U(r)` rule is unbiased:
rejecting `x≥floor(2^256/r)·r` before `x mod r` removes modulo bias, and
descending Fisher-Yates with that `U` is uniform. With `r=1`, consuming no
digest is fine if counter state is explicitly unaffected.

The remaining bounded defect is stream scope. A2's complete domain list
does not include stratum in `dev`/`sample` or pair in `role`; therefore it
must either add those components or freeze a single non-resetting counter
and canonical call order. This is a reproducibility and allocation-law
exactness defect, not a renewed objection to the procedural threat model.

Timing is otherwise correct: `D` is drawn before development; roles over
`O` are assigned once and conditioned on; `R_h` is drawn only after `N3`
using a domain that includes `N3`; and no regeneration after feasibility,
censoring, loss, or contrast information is permitted. A failure before
durable transcript commitment routes to signed invalidity, not a quiet
second draw.

## S2 — estimator and zero-variance cases

A9 adopts the requested finite-population paired estimator:

- `d_XY(p)=Y_Y(p)-Y_X(p)`, positive favors `X`;
- `s²_h` uses denominator `n_h-1`;
- `v_h=W_h²(1-n_h/8)s²_h/n_h`;
- `Vhat=Σ_h v_h`;
- Satterthwaite df uses `Vhat² / Σ_h[v_h²/(n_h-1)]`;
- zero components contribute zero;
- the Bonferroni quantile is `t_{1-0.05/(2·3),ν}`;
- one-sided predicate boundaries are strict and equivalence is inclusive.

When only some `v_h` are zero, the df formula is defined using the
nonzero components. When all `v_h=0` at `N3<24`, A9's intended point
interval is coherent but must bypass the undefined df/quantile calculation
explicitly.

At `N3=24`, the census rule is coherent: `n_h=8`, the FPC is identically
zero, intervals collapse to points, and the result is descriptive of the
24 role-assigned blocks under the conditioned two-seed schedule. This is
statistical precision, not seed-superpopulation inference. Because the
projected half-width is also zero at `N3=24`, "projection fails at 24" is
not a live statistical branch. Resource inability to run 24 blocks,
process invalidity, or feasibility failure can still block a lock, but
they are not precision-projection failures.

## S3 — directional determinacy

A9's determinacy table is the correct repair.

| Solve pattern | Predicate consequence |
|---|---|
| both compared arms all-censored | no predicate is eligible; route `INSUFFICIENT`; never equivalence, boundary, or success |
| `X` events, `Y` none | `SUP`, `NI`, and `NONSUP` are decided only by the ordered interval; `EQ` forbidden |
| `X` none, `Y` events | `SUP`, `NI`, and `NONSUP` are decided only by the ordered interval; `EQ` forbidden |
| both arms have events | all four predicates may be decided by the interval |

Exact equality at `+60` does not satisfy `SUP` or `NONSUP` because those
are strict (`L>+60`, `U<+60`). Exact equality at `-60` does not satisfy
`NI` because it is strict (`L>-60`). `EQ` includes the boundaries
(`L≥-60` and `U≤+60`) but only when the determinacy guard allows
equivalence, which requires events in both compared arms.

C1 can be earned only by the ordered `A-Y` interval satisfying
`SUP(A,Y)`. The distance-1 negative can be reached only by the ordered
`A-Y` interval satisfying `NONSUP(A,Y)`. A one-sided predicate cannot be
renamed as equivalence, and an all-censored administrative tie cannot
become a C1 result.

## S4 — N3 development projection

A9 correctly moves the projection to all three contrasts `{A-Y,Y-R,A-R}`,
uses the same bounded-cost endpoint and seed aggregation, computes
two-block development variances within each stratum, and selects the
smallest candidate whose maximum Bonferroni projected half-width is
`≤30`.

The fallback needs the bounded edit above. `B²` is defensible as a
Popoviciu finite-population variance cap for a variable bounded in
`[-B,B]`, and it is intentionally conservative for zero or undefined
two-block scout variances. It is not the maximum possible unbiased sample
variance from two development observations. The text must say which
concept it uses and must not overwrite observed nonzero sample variance
with the lower population cap unless that cap is explicitly part of the
frozen rule.

The same six development blocks may estimate censoring, covariance, and
precision only as a non-citable engineering precision model. They cannot
alter margins, endpoints, policies, arms, cadence, controls, or
determinacy guards.

## S5 — calibration and invalidity statistics

A6 fixes the Brier problem: calibration is per-stratum, computed over all
items, and abstentions contribute their actual `p̄` rather than being
excluded. This prevents S1's many easy negatives from hiding poor S4
calibration and prevents abstention from improving calibration.

A7's shuffled-answer gate is now finite in scope and exact: all 12
development worlds, RANDOM-STATIC schedule, two replicates per world, a
domain-separated Fisher-Yates permutation of the `B` answer bits, full
budget, sealed evaluator, and zero certified solves tolerated. This is a
finite design-invalidity gate, not evidence of global leakage absence.

The pre-contact noninterference gate is a stronger replacement for the
underdefined ML probe. Byte-identity after mapping opaque handles through
world-independent slots is the right target; implementation tests must
canonicalize those slot identifiers before comparison. Any target-`n`
dependent byte, length, hash, or pre-contact query ordering remains
design invalidity.

A6's divergence and re-execution ordering is coherent. A complete
five-checkpoint qualifying window before first non-finite state fixes `T`;
otherwise non-finite trajectories are censored at `B`. Missing checkpoints
caused by non-finite state route as outcome-related censoring, not process
re-execution. Process re-execution is limited to one attempt under the v3
rule and must reproduce hashes through the last committed pre-fault
checkpoint; seal breach remains whole-level invalidity.

## S6 — signature readiness

Remaining verdict-moving procedures:

| Procedure or value | Classification | Required action |
|---|---|---|
| Allocation domain/counter reset across strata and pairs | bounded text correction | add explicit stratum/pair domains or a single persistent counter and canonical draw order |
| `N3=24` "projection fails" prose | bounded text correction | state that statistical precision always passes at the census; separate resource/invalidity inability to run all 24 |
| `B²` fallback wording | bounded text correction | distinguish Popoviciu population variance cap from two-point sample variance; preserve observed nonzero `s²_dev` |
| all-`v_h=0` at `N3<24` | bounded text correction | define direct point interval and skip df/quantile evaluation |
| witness attestation scope | implementation-test detail with text clarification recommended | attest process facts only; no cryptographic-independence claim |
| root transcript visibility | implementation-test detail with text clarification recommended | name pre-outcome visibility so A4 surfaces remain unambiguous |
| slot canonicalization for byte identity | implementation-test detail | assert canonical slot serialization in tests |

No formula inconsistency requires reopening the 24-pair frame, the
adjacent-only detector scope, or the total selector. No remaining issue
requires a new outcome estimand. The repairs are bounded but must be
incorporated before Kirill signs the Level 1 v3.1 specification.

## Gate boundary

This review authorizes no entropy draw, feasibility run, comparative
scout, N3 selection, lock, escrow, or outcome. Before signature, only the
bounded text repairs above should be made and rechecked. After signature,
implementation may proceed only according to the repaired gate sequence;
the one-shot root draw remains a later reviewed single execution.

UNKNOWN, all-censored, and administratively tied outcomes remain
forbidden from becoming equivalence, boundary support, or success.
