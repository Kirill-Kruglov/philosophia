# B2_INSTRUMENT_REPAIR_09 — ticket

Status: `READY_FOR_DISPATCH`
Date: 2026-08-15
Slot: 4c (path-credit vs destination-credit)
WIP: 1 — Stage-B L3 and all Stage-R lines are frozen for the duration.

Predecessor: `successor/dev/B2_PILOT_08.md` (Stage-1 pilot, `M3_PASS = False`).
Design of record: `successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md` — **unchanged**.
This ticket repairs the instrument only. It does not reopen the design and
requires no new review round: the pilot was the design check.

## 1. What the pilot data actually shows

Read from `b2_pilot_08_run.log` and `b2_pilot_08_results.json`, not from the
summary.

**(a) The path loss curve is uninterpretable by construction.**

```text
P0 seed0 : 17.47  16.69  18.39  16.28  15.10  17.54   (steps 100..600)
P0 seed1 : 18.50  18.15  18.32  17.54  18.41  16.47
P_shuf   : 22.09  23.75  21.68  22.08  22.25  22.15
```

Flat and noisy, no trend. But `ell` — logged alongside — is the **word length of
the batch**, resampled uniformly per step (`sample_length_matched_positive_batch`,
line 484): 69, 76, 81, 34, 54, 13. Every step trains on a different length
stratum, so the loss is computed on a different data distribution each time.
Convergence cannot be read off this curve at all. The `P_shuf` gap of ~5 is the
only thing the curve supports.

**(b) The likely root cause is partial collapse, and it is arithmetically
checkable.**

`vicreg_pair_loss` (line 366) with `INV=25, VAR=25, COV=1`:

```text
var = mean(relu(1 - std))   -> bounded above by 1.0
so   VICREG_VAR * var       -> bounded above by 25.0
```

Observed total is 15–18. If the variance hinge were satisfied (`std >= 1`), the
var term would be 0 and the whole 15–18 would have to come from `25*MSE + cov`.
The consistent reading is the opposite: **per-dimension std sits well below 1,
the variance hinge is pinned near its maximum (~0.6–0.7 -> ~15–18), and the
invariance term contributes almost nothing to the gradient.**

This is the canonical VICReg failure mode: the paper's weights `(25, 25, 1)`
assume its projector + BatchNorm at ~8192 dims. The pilot inherited the weights
without the architecture. **Nothing is logged that would confirm or refute this**
— only the scalar total.

**(c) The mechanism probes are not diagnostic — they use the wrong reference.**

| arm | seed | exact_d | length_only |
|---|---:|---:|---:|
| **D at init** | 0 | **0.398** | 0.526 |
| P0 (after path) | 0 | 0.238 | 0.145 |
| **D at init** | 1 | **0.455** | 0.667 |
| P0 (after path) | 1 | 0.269 | 0.100 |

Every probe in the pilot is reported against **chance** (0.025). But the
randomly initialised trunk already decodes displacement at 0.40–0.46 — sixteen
times chance — because displacement is `#R − #L`, a linear function of token
counts that a random projection preserves. Against the correct reference, path
training **reduced** linear displacement decodability rather than increasing it.

The pilot already noticed this for `sign(d)` (design-bug note 3: "sign(d)=1.0
even at init ... not evidence of learned path structure") but did not apply the
same logic to `exact_d`, and the M3 verdict rests on the path readout.

**Consequence.** The pilot cannot distinguish "the invariance was installed" from
"the representation collapsed". `M3_PASS = False` is therefore **not** evidence
about the design.

## 2. Required repairs — instrumentation only

No change to the objective, the world, the panel, the floor, K, H_DEST, M_PATH,
seeds or scoring in step R1–R3.

**R1. Log the three VICReg components separately**, plus `mean(std_z1)` and
`mean(std_z2)`, at every logged step.

**R2. Add a fixed held-out evaluation batch.** Same words, same `ell` mix, drawn
once before training, never trained on. Log its loss and components at the same
cadence. This is the curve that may be read for convergence; the training-loss
curve may not.

**R3. Add the direct road-alignment metric** — the quantity the objective
actually optimises, which the pilot never measured. On the held-out batch:

```text
align_same = mean cosine(z(w1), z(w2))  over pairs with equal displacement,
                                         distinct roads
align_diff = mean cosine(z(w1), z(w2))  over pairs with different displacement
road_gap   = align_same - align_diff
```

Report `road_gap` at init, after path training, and for `P_shuf`. This answers
"was the invariance installed" without any probe.

**R4. Re-reference every mechanism probe to the matched random-init trunk.**
Report `Δ = acc(trained) − acc(init, same seed, same architecture)`. Chance may
stay in the table as a footnote; it may not be the comparison.

**R5. `d_within_len` returned `nan`** (stratum too thin after filtering).
Enlarge the probe sample until the stratum is populated, or report it as
`INSUFFICIENT` explicitly. It may not silently vanish — it is the control Opus
C3a prescribed against the length ruler.

## 3. Pre-registered conditional repair — declared before the run

If R1/R2 confirm collapse — operationally **`mean(std) < 0.5` on the held-out
batch at step 600** — then apply exactly one canonical fix and rerun once:

> add a BatchNorm-terminated projector head before the VICReg loss, as in the
> original VICReg, leaving `(INV, VAR, COV) = (25, 25, 1)` untouched.

No weight sweep. No second variant. No third attempt. If collapse persists after
that single fix, the run stops and returns to the author — this ticket does not
authorise a third round.

## 4. Kill / done — fixed before dispatch

**DONE — instrument validated, Slot 4c proceeds to the Stage-2 six-block call:**

1. held-out loss decreases monotonically over `M_PATH`;
2. `mean(std) >= 1.0` at step 600 (variance hinge satisfied, no collapse);
3. `road_gap(P0) > road_gap(init)` **and** `road_gap(P0) > road_gap(P_shuf)`;
4. `Δ exact_d > 0` against the matched-init baseline;
5. M3 panel prediction holds on at least one seed: S1 & S3 qualify, S2/S4/S5
   fail.

**KILL — Slot 4c answered negatively, published as-is:**

criteria 1–4 all pass (the invariance genuinely was installed) **and** M3 fails
on both seeds. Then manufactured road-invariance does not produce the predicted
panel pattern, and path-credit is redundant to destination-credit in this world.
This is the design's own registered kill — "indistinguishable → the path is
redundant to the destination; also an answer, published" — and it is a result,
not a failure.

**INCONCLUSIVE — stop, return to author, no third round:**

collapse persists (`mean(std) < 0.5`) after the section 3 fix.

## 5. Budget

- instrumentation R1–R5: ≤ 4 focused engineering hours;
- pilot rerun at frozen constants (2 seeds, all arms): ~45 min wall, as measured
  (pilot total was 2432 s);
- at most one conditional rerun under section 3: ~45 min.

Ceiling: **≤ 6 engineering hours + 2 runs.** Inside the project's 8-hour
prospective limit. Two dispatches maximum, both declared here.

## 6. Out of scope

No new arm, no new metric beyond R1–R5, no weight sweep, no change to world,
panel, floor, K, H_DEST, M_PATH, seeds, scoring or the VICReg weights. No
fold/residue auxiliary head — declined four times and declined again here: it
injects the relation we are asking whether the mind can derive. No Stage-2 call
until DONE is met. No Stage-B, Stage-R or MINIMO work while this is in flight.
