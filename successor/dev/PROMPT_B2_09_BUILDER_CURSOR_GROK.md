# PROMPT — B2_INSTRUMENT_REPAIR_09 — Builder (Cursor Composer 2.5 / Grok 4.5)

ROLE: Builder. Implement instrumentation repairs R1-R5, run the pilot, emit
artifacts. You do **not** interpret the results and you do **not** decide
DONE/KILL/INCONCLUSIVE — an independent road does that.

## Authority — read these before writing anything

| file | SHA-256 |
|---|---|
| `successor/dev/B2_INSTRUMENT_REPAIR_09_TICKET.md` | `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85` |
| `successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md` | `160726a6c06fed20b5aa554449c3f14c03f45b9ee52cdcf1ca49ff49ce238dd2` |
| `successor/dev/B2_PILOT_08.md` | `107d8a6ed5dcf3e6dac9d4f43196f6c3bdf3d372ff5068e0df050bcceeb76d7f` |
| `successor/dev/b2_path_pilot_08.py` | `d5099d56ec78911a8dfb451a94d34350a3b8060fe90a0d05687edcc458f1c03f` |
| `successor/dev/b2_pilot_08_results.json` | `593b478811eea533428805f60f618d58df04de4fed2bd06aaae6fe767aa63052` |

Verify each hash before starting. The ticket is the governing document; this
prompt does not replace it.

## Why this exists — read once, it determines every choice below

Pilot 08 returned `M3_PASS = False`. That verdict is **not** evidence about the
design, because the instrument could not distinguish "the path invariance was
installed" from "the representation collapsed":

1. the logged path loss is computed on a **different length stratum every step**
   (`ell` is the word length, resampled per step at line ~484), so its flatness
   says nothing about convergence;
2. only the scalar total is logged — the three VICReg components and the
   embedding std are not, so collapse is neither confirmed nor refuted;
3. every mechanism probe is referenced to **chance** (0.025), while the randomly
   initialised trunk already decodes displacement at 0.40-0.46, because
   displacement is `#R - #L`, a linear function of token counts.

You are fixing the instrument. You are **not** fixing the experiment.

## Hard constraint — do not change the experiment

Copy `b2_path_pilot_08.py` to `successor/dev/b2_instrument_repair_09.py` and work
there. **Leave `b2_path_pilot_08.py` byte-identical** — it is the record of what
produced pilot 08.

These must not change, in value or in sampling logic:

```text
N_max=2000  K=250  H_DEST=500  M_PATH=600  PATH_BATCH=32  M_ROADS=4
VICREG_INV=25.0  VICREG_VAR=25.0  VICREG_COV=1.0  CONTRAST_TEMP=0.1
PILOT_SEEDS=(0,1)  _D_PATH_LO=-80  _D_PATH_HI=80
world, panel, floor, strata, scoring, arms (D/P0/P0-neg/P+/P_shuf)
```

The path firewall `_assert_path_clean` and `_FORBIDDEN_PATH_NAMES` must remain
active and must not be weakened. Every metric you add is subject to it: path and
road-alignment code may read token counts and exact-displacement sameness only.
`modulus`, `n_mod`, residue, fold, oracle, panel and truth remain forbidden
there.

## R1 — log VICReg components separately

At every existing log cadence, in addition to the total, record:

```text
inv_term  = VICREG_INV * F.mse_loss(z1, z2)
var_term  = VICREG_VAR * var          # var as already computed in vicreg_pair_loss
cov_term  = VICREG_COV * cov
mean_std  = 0.5 * (std_z1.mean() + std_z2.mean())
```

`vicreg_pair_loss` must return the same scalar it returns today. Add a parallel
function or an out-parameter for the components; do not change the optimised
value.

## R2 — fixed held-out evaluation batch

Draw once, before any training, per seed:

- the same `ell` mix as training (sample lengths from `_LENGTHS` with the same
  law), at least 512 pairs total;
- these exact words are **excluded from every training batch for every arm**;
  assert this, do not assume it.

At every log cadence, evaluate the frozen-batch loss and its R1 components in
`torch.no_grad()`. **This is the only curve that may be read for convergence.**
Keep logging the training-loss curve too, marked `not_interpretable`.

## R3 — direct road-alignment metric

The quantity the objective actually optimises, never measured in pilot 08. On
the held-out batch, in `no_grad`:

```text
align_same = mean cos(z(w1), z(w2))  over pairs, distinct roads, EQUAL displacement
align_diff = mean cos(z(w1), z(w2))  over pairs, distinct roads, DIFFERENT displacement
road_gap   = align_same - align_diff
```

Report `road_gap` for: the freshly initialised trunk (`init`), after path
training (`P0`), and for `P_shuf`. Same held-out batch in all three. Sample the
`different displacement` pairs length-matched, so the contrast is not a length
ruler.

## R4 — re-reference every mechanism probe to matched init

For **every** arm and seed, run the full probe suite on the freshly initialised
trunk before any training, tagged `init`, and report

```text
delta_<probe> = acc(trained) - acc(init, same seed, same architecture)
```

`init` must be the same weights the arm starts from — same seed, same
construction — not the D arm's init reused. Chance may remain in the table as a
footnote column; it may not be the comparison.

## R5 — `d_within_len`

Pilot 08 returned `nan` (stratum too thin after filtering). Enlarge the probe
sample until the stratum is populated. If it still cannot be populated, emit the
literal string `INSUFFICIENT` with the achieved stratum size. It may not silently
disappear — it is the control against the length ruler.

## Pre-registered conditional repair — declared before the run, not after

Run seeds 0 and 1. Then check, on the held-out batch at step 600:

- **if `mean_std >= 0.5`** — stop. Emit artifacts. Done.
- **if `mean_std < 0.5`** — collapse is confirmed. Apply **exactly one** fix and
  rerun **once**:

  > insert a projector head terminated by `BatchNorm1d` before the VICReg loss,
  > as in the original VICReg, leaving `(INV, VAR, COV) = (25, 25, 1)`
  > untouched.

  Emit both runs, tagged `pre_fix` and `post_fix`.

No weight sweep. No second variant. No third attempt. No other change. If
`mean_std < 0.5` persists after that single fix, stop and say so — you are not
authorised to try anything further.

## Outputs — under `successor/`, never `/tmp`

`/tmp` is volatile on this machine and was wiped on 2026-08-15, taking eight
pinned documents with it. Write only to:

```text
successor/dev/b2_instrument_repair_09.py
successor/dev/b2_repair_09_results.json
successor/dev/b2_repair_09_run.log
successor/dev/B2_INSTRUMENT_REPAIR_09.md
```

`B2_INSTRUMENT_REPAIR_09.md` must contain, and nothing more:

1. the five verified input hashes and the SHA-256 of your modified script;
2. the frozen-constants block, copied from your source, proving it is unchanged;
3. held-out loss and component table (`inv/var/cov/mean_std`) per seed per
   cadence step;
4. the training-loss curve, marked `not_interpretable`;
5. `road_gap` table: `init` / `P0` / `P_shuf`, per seed;
6. the full probe table with `delta` against matched init, chance as a footnote;
7. `d_within_len` value or `INSUFFICIENT` with the achieved stratum size;
8. the per-arm per-stratum floor table and M3 outcome, in the same format as
   `B2_PILOT_08.md`;
9. whether the section-3 conditional fix fired, and `mean_std` at step 600;
10. wall time per arm.

## Explicitly not your job

Do not state whether the ticket's DONE, KILL or INCONCLUSIVE branch is met. Do
not recommend a next step. Do not propose a design change. Do not add an arm, a
metric beyond R1-R5, a weight sweep, or a fold/residue auxiliary head — that last
one has been declined four times and injects the relation the experiment asks
whether the mind can derive.

Report the numbers. The verdict is another road's job.

## Budget

<= 4 focused engineering hours, plus ~45 min per run (pilot 08 total was 2432 s),
at most two runs. If you exceed this, stop and report where it went.

## Negative authorization

No commit, no push, no change to `b2_path_pilot_08.py`, no change to any frozen
constant, no Stage-B / Stage-R / MINIMO work, no Stage-2 six-block call.
