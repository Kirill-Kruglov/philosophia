# B2_INSTRUMENT_REPAIR_09 — pre-fix results and escalation to the author

Date: 2026-08-16
Status: `INCONCLUSIVE__ESCALATE_TO_AUTHOR`

Source: `b2_repair_09_results.json` (Legion), SHA-256
`78a792718f327466da63e525ee2e722b87d387f3dd5ddb5c0e37075496e6ed28`.
Executed script `a827ab87…` (repo `f5b23a90…` plus five device-placement edits;
none touches any region Sol audited — verified line-by-line). Device `cuda`,
pre-fix wall 4386 s, post-fix 4382 s.

`post_fix` numbers are **discarded** under static-audit defect 7 (different
held-out words via `run_tag`, and `mean_std` measured on a 256-dim BN-projector
surface against a threshold calibrated for the 128-dim trunk). They appear below
only as a labelled pointer.

## 1. Decision table — all five criteria fail

| criterion | required | seed 0 | seed 1 | result |
|---|---|---|---|---|
| 1. held-out loss monotone | monotone decrease | rises at steps 200 and 500 | monotone | **FAIL** |
| 2. `mean_std >= 1.0` @600 | ≥ 1.0 | 0.454 | 0.505 | **FAIL** |
| 3. `road_gap(P0) > init` and `> P_shuf` | both | 0.240 vs init 0.373 | 0.281 vs init 0.318 | **FAIL**, and VOID under defect 3 |
| 4. `delta exact_d > 0` | > 0 | **−0.531** | **−0.459** | **FAIL** |
| 5. M3: S1 & S3 qualify | — | S1 2/118 | S1 17/118 | **FAIL** |

Criteria 1-4 do not all pass, so neither `DONE` nor `KILL` is reachable.
Verdict: **`INCONCLUSIVE`**. No verdict prompt is dispatched; Opus 5 stays on
hold.

## 2. Why — the loss decomposition, which is the point of the whole ticket

Held-out components at step 600, arm P0:

| seed | total | `inv_term` | `var_term` | `cov_term` | `mean_std` |
|---|---|---|---|---|---|
| 0 | 16.13 | **0.086 (0.53 %)** | 13.65 (85 %) | 2.40 (15 %) | 0.454 |
| 1 | 15.42 | **0.272 (1.77 %)** | 12.37 (80 %) | 2.77 (18 %) | 0.505 |

**The invariance term is under two per cent of the objective.** It is the only
term that encodes "different roads to the same displacement should align" —
the entire content of path-credit. The optimiser spends 80-85 % of its budget on
the anti-collapse hinge and never gets traction on alignment. On seed 1
`inv_term` *rose* over training (0.144 → 0.272) while the total fell: alignment
got worse as the loss improved.

Pilot 08's flat 15-18 curve is now explained exactly: it was the variance hinge,
pinned near its maximum, and nothing else. `M3_PASS = False` in pilot 08 carried
no information about the design. That question is settled.

## 3. The finding that matters more than the verdict

Re-referencing the probes to matched init (repair R4) inverted the reading.

| | init | after path | delta |
|---|---|---|---|
| `exact_d` seed 0 | **0.770** | 0.238 | −0.531 |
| `exact_d` seed 1 | **0.753** | 0.294 | −0.459 |
| `length_only` seed 0 | 0.785 | 0.140 | −0.645 |
| `sign_d` both | 1.000 | 1.000 | 0.000 |

**At random initialisation the trunk decodes displacement at 0.77 — thirty-one
times chance.** Displacement is `#R − #L`, a linear function of token counts, and
left-padding makes length affine in `|d|`; a random projection preserves that.
Path training then destroys it, along with length decodability.

Against chance (0.025) the trained figure 0.238 reads as "9.5× chance", which is
what pilot 08 reported and what led nowhere. Against the architecture's own
starting point it is a 53-point loss.

`exact_d_within_length` is `INSUFFICIENT` in both seeds, and the reason is
itself diagnostic: the matched-length stratum holds 1036 / 904 samples at init
and 21 / 20 after training. The trained representation flattens length structure
so far that the control cannot be populated.

**Consequence for the design, not just the instrument.** Arm P0's registered
mechanism check is "does self-resampling induce displacement?" — with the
modulus panel expected to fail, isolating the world-wall. If displacement sits
at 0.77 before any training, there is nothing for P0 to induce, and the
mechanism check is **non-identified on this architecture**. This is IDEA_GATE
item 1 — identifiability — and it was answerable from a single init probe before
any harness existed.

It also puts a number on the design's own three-level ladder: word →
language-wall, displacement → **false wall**, fold/modulus → world-wall. The
false wall is not learned from correlated roads here. It is present at
initialisation, at 77 %.

## 4. Post-fix, labelled and discarded

| seed | total | `inv_term` | `var_term` | `cov_term` | `mean_std` |
|---|---|---|---|---|---|
| 0 | 21.33 | 0.952 | 5.32 | 15.06 | 0.793 |
| 1 | 18.22 | 0.830 | 7.25 | 10.14 | 0.712 |

Not admissible as evidence (defect 7). As a pointer only: the BN projector does
hand the invariance term real weight (11× and 3×) and does relieve the variance
hinge — but covariance then dominates (2.40 → 15.06), the total rises, and
`mean_std` still reaches only 0.79 / 0.71 against the required 1.0.

**No single canonical fix brings this configuration to spec.** The ticket's
pre-registered one-change repair was the right thing to try and it is not
sufficient.

## 5. Why this escalates instead of spending dispatch 2

Operating rule 4: two dispatches per ticket, then the author decides; stuck →
escalate, not a third round.

The scoped repair S1/S3/S7/S2b fixes measurement — held-out disjointness, the
length-matched `road_gap`, one collapse surface, an armed firewall. All four
remain correct and necessary. But section 4 shows they would not reach criterion
2: BN alone lands at 0.79 / 0.71. Spending the last dispatch on a repair whose
outcome is already visible would burn the budget and land on `INCONCLUSIVE`
again.

Reaching criterion 2 requires rebalancing `(VICREG_INV, VICREG_VAR, VICREG_COV)
= (25, 25, 1)`. Those are **frozen constants** of the experiment, not
instrumentation. Changing them is an author decision.

## 6. Options for the author

**(a) Bounded recalibration, one dispatch.** Authorise a single principled
re-weighting — for example, scale the terms so `inv_term` and `var_term` are
comparable at step 0 — pre-registered before the run, no sweep, criteria
unchanged, bundled with S1/S3/S7/S2b. Defensible: the canonical VICReg weights
assume a ~8192-dim projector with BatchNorm, and this trunk is 128-dim, so the
imbalance is a misconfiguration rather than a design flaw. **It does not address
section 3.**

**(b) Report the diagnosis as the finding and close Slot 4c.** Positive-only
VICReg alignment cannot be brought to spec on this architecture within the
frozen configuration, and the arm's mechanism check is non-identified because its
target is present at initialisation. Both statements are now supported by
numbers, cheaply obtained. This is a result about the design, of the kind the
essay's own gate exists to produce.

**(c) Re-aim the arm.** If displacement is architecturally given, then
self-resampling cannot demonstrate its induction, and Slot 4c needs a different
invariant — one the architecture does not already encode. That is a design
question for a fresh IDEA_GATE pass, not a calibration.

**Recommendation: (b), with (c) recorded as the open question.** (a) is
defensible but would leave section 3 untouched: a perfectly balanced loss still
aims P0 at a target the trunk already contains at 77 %. The identifiability
problem is the larger finding, and it is worth more to the essay than a working
P0 arm would have been.

## 7. What this run established regardless of the choice

- Pilot 08's `M3_PASS = False` is void as evidence about the design; the flat
  loss was the variance hinge.
- The path objective as configured cannot install road-invariance: the alignment
  term carries under 2 % of the gradient.
- The `P_shuf` fake-ledger control works — `road_gap` 0.023 / 0.016 against P0's
  0.240 / 0.281.
- `sign_d` is architectural (1.000 at init, delta 0.000), confirming pilot 08's
  bug note 3 with a matched baseline.
- Referencing probes to chance rather than to matched init inverts conclusions.
  This is a reusable lesson for every probe in the programme.
