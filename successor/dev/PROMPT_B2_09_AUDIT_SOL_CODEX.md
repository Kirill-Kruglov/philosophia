# PROMPT — B2_INSTRUMENT_REPAIR_09 — adversarial audit (Codex GPT 5.6 Sol, high)

ROLE: adversarial statistical/correctness audit of a completed instrumentation
run. **One round.** You answer exactly one question:

> Is any number in `B2_INSTRUMENT_REPAIR_09.md` wrong, leaked, or
> non-comparable to the number it is being compared against?

You are not asked whether the experiment is well designed. That was settled by
two prior design-review rounds and by pilot 08. A finding that does not change a
number is not a finding here.

## Read before auditing

| file | SHA-256 |
|---|---|
| `successor/dev/B2_INSTRUMENT_REPAIR_09_TICKET.md` | `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85` |
| `successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md` | `160726a6c06fed20b5aa554449c3f14c03f45b9ee52cdcf1ca49ff49ce238dd2` |
| `successor/dev/b2_path_pilot_08.py` | `d5099d56ec78911a8dfb451a94d34350a3b8060fe90a0d05687edcc458f1c03f` |
| `successor/dev/b2_instrument_repair_09.py` | *(builder emits; verify against its stated hash)* |
| `successor/dev/b2_repair_09_results.json` | *(builder emits)* |
| `successor/dev/b2_repair_09_run.log` | *(builder emits)* |
| `successor/dev/B2_INSTRUMENT_REPAIR_09.md` | *(builder emits)* |

Diff `b2_instrument_repair_09.py` against `b2_path_pilot_08.py` and read the
diff, not the summary.

## Attack surface, in priority order

1. **Held-out contamination (R2).** Are the frozen evaluation words provably
   excluded from every training batch, for every arm and both seeds? Is the
   exclusion asserted in code or merely intended? Does the shuffle/`P_shuf` arm
   re-admit them? A contaminated held-out curve invalidates the single criterion
   the ticket says may be read for convergence.

2. **Firewall breach in the new metrics (R3).** `road_gap` must use token counts
   and exact-displacement sameness only. Does any new code path read `modulus`,
   `n_mod`, residue, fold, oracle, panel or truth — directly, or transitively
   through a helper? Is `_assert_path_clean` still armed on every path/alignment
   call site, or was it bypassed for the new metric?

3. **Length ruler in `road_gap` (R3).** Are the `different displacement` pairs
   length-matched against the `equal displacement` pairs? If not, `road_gap`
   measures word length, and the pilot already showed length is ~85% separable
   by construction (left-pad makes length an affine function of `|d|`).

4. **Init baseline mismatch (R4).** Is `init` the same seed and same weight
   construction the arm actually starts from? If the D arm's init was reused for
   P0's delta, or a different RNG draw was used, every `delta_*` is meaningless.

5. **Component arithmetic (R1).** Do `inv_term + var_term + cov_term` reproduce
   the total the optimiser sees, to floating-point tolerance, on the logged
   steps? Is `mean_std` computed on the held-out batch, pre-projector or
   post-projector, and is that the same surface across `pre_fix`/`post_fix`? A
   `mean_std` measured at a different layer before and after the section-3 fix
   makes the collapse threshold non-comparable.

6. **Frozen constants (silent drift).** Does the emitted constants block match
   the source, and the source match pilot 08 for every listed constant? Was the
   optimised `vicreg_pair_loss` return value altered while adding component
   logging?

7. **Conditional-fix discipline.** If the section-3 fix fired, was it the single
   declared change (BN-terminated projector, weights untouched), applied once? Any
   additional tweak, weight change or extra rerun voids the pre-registration and
   the run must be reported as unregistered.

8. **Seed accounting.** Two seeds, both reported, neither dropped or re-rolled.

## What you may not do

Do not comment on the design of the path objective, the choice of VICReg, the
arm set, the panel, the strata, the floor, or M3's thresholds. Do not propose a
new metric, arm or experiment. Do not suggest raising `M_PATH`, sweeping weights
or adding an auxiliary head. Do not evaluate whether the result is scientifically
interesting.

If your finding would not change a logged number or expose a leak, it is not in
scope: return `NO_FINDING` for that item.

## Output

Write to `successor/dev/B2_09_AUDIT_SOL_RESPONSE.md`. Never `/tmp` — it is
volatile on this machine and was wiped on 2026-08-15.

For each of the eight items: `OK`, `NO_FINDING`, or a defect with (a) the exact
file and line, (b) the number it corrupts, (c) the smallest repair. Then one
token:

```text
B2_09_NUMBERS_TRUSTWORTHY=YES      # every logged number may be read as stated
B2_09_NUMBERS_TRUSTWORTHY=NO       # at least one number is wrong or leaked; name it
```

If `NO`, state whether the repair requires a rerun or only a recomputation from
the emitted JSON.

## Negative authorization

No code edit, no rerun, no commit, no push, no design change, no second round.
