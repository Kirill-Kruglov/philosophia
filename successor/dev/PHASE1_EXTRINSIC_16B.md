# PHASE1_EXTRINSIC_16B

NON-CITABLE Phase-1 diagnostic. Not an experiment. No scientific claim.
Does not supersede `PHASE1_EXTRINSIC_16.md`. `FLAT_AT_B2000` remains valid for
that search budget. This run shows only that the result does not carry over to
B8000, and it does not establish transfer.

## STATUS

```text
FLAT_AT_B2000; POSITIVE_ENDPOINT_INTERACTION_AT_B8000; UNDERPOWERED
```

## Question

Are the 19 Kleene statements never solved at 2000 MCTS expansions
budget-limited or policy-limited?

## Setup

Identical wiring to `PHASE1_EXTRINSIC_16` ([run script](run_phase1_extrinsic_16b.sh)).
Exactly two things differ: MCTS budget 2000 -> 8000, and only checkpoints
`0.pt` / `4.pt` were evaluated. All 30 statements were run at the new budget so
the two checkpoints stay directly comparable. `problemset=kleene`,
`accumulate_library=false`, seed 0, same order, same run dir
`outputs/2026-08-10/00-14-33`. No retraining, no agent/theory/config edits.

## Result

| checkpoint | solved @2000 | solved @8000 | mean elapsed @8000 |
| ---: | ---: | ---: | ---: |
| ck0 | 11 / 30 | **11 / 30** | 181.5 s |
| ck4 | 11 / 30 | **13 / 30** | 159.1 s |

At 8000, relative to ck0 the late policy gains `kleene_3`, `kleene_6`,
`kleene_7` and loses `kleene_20`. Relative to its own 2000-expansion run, ck4
gains `kleene_6`, `kleene_7`; ck0 gains nothing.

Paper reference for propositional logic: ~0.30 at ck0 rising to ~0.47 at ck4.
Ours: 0.367 -> 0.433.

## What this supports

`FLAT_AT_B2000` stands as a statement about that budget. What it does not
license is a general statement about the learned policy: at B8000 the endpoint
comparison changes direction, so the earlier result was budget-specific.

The informative structure is a descriptive **checkpoint x budget interaction**,
not the endpoint difference: in these paired runs a uniform main effect of added
search budget is insufficient. This does not exclude chance, seed, or search
stochasticity as the cause.

**Superseded by 16C.** The original wording here read "since only ck4 gained
additional solves". That is false once ck1-ck3 were measured at the same budget:
the budget response is +0 / +8 / +0 / +1 / +2 for ck0..ck4. ck1 gained four
times more than ck4. What survives is narrower: the *cold* policy converts extra
budget into exactly zero additional solves, while trained policies convert it
into between zero and eight. "Later checkpoint is better" does not survive at
all — see `PHASE1_EXTRINSIC_16C`.

Scope of the budget-sensitivity finding: exactly `kleene_6` and `kleene_7` are
shown to be budget-sensitive for ck4 in this run. The other 17 never-solved
statements remain unclassified — they are neither shown budget-limited nor shown
policy-limited.

## What this does NOT support

- **Not statistically established.** Discordant pairs between ck0 and ck4 at
  8000: 3 gains, 1 loss. Exact one-sided McNemar `p = 5/16 = 0.3125`. With only
  four discordant pairs, even a 4/0 split would give one-sided `p = 0.0625`:
  this sample could not cross `alpha = 0.05` under any outcome. That is the
  cleanest illustration of the stop-rule defect below — the rule demanded a
  direction while the sample was incapable of supplying the evidential level the
  verdict implied.
- **Mean search time is not independent evidence.** 159 s vs 181 s is largely
  derivative of solve rate: successes terminate early, failures consume the
  whole budget. It is not quoted here as support.
- **The 8000 budget was chosen after seeing the 2000 result.** This is a
  forking-path exposure and is recorded as such.
- One training seed, one theory, one external set of 30, dependent sequential
  checkpoints. Nothing here identifies *why* the later policy is better; in
  particular it does not separate self-chosen curriculum from any equal-cost
  exposure. That separation needs ACTIVE and matched-cost YOKED arms and is not
  authorized in Phase 1.

## Defect in this diagnostic's own stop rule

The dispatching ticket pre-registered: "BUDGET_MASKED if ck4 solves strictly
more than ck0 at 8000". That rule fired literally. The rule was **too weak**:
it carried no significance or effect-size requirement, so honoring it as written
produces an overclaim. Recorded here rather than silently corrected. Later
binary rules in this line must carry both a direction and a minimum evidential
bar.

## Continuation, and an honest label for its reading rule

`ck1`, `ck2`, `ck3` are being evaluated at budget 8000, everything else
identical ([run script](run_phase1_extrinsic_16c.sh)). Shape rule:

```text
MONOTONE_SHAPE    := solved counts non-decreasing over ck0..ck4 AND ck4 > ck0
NONMONOTONE_SHAPE := anything else
```

This is a **shape** classification and carries no evidential bar, so it cannot
produce a positive verdict — only a description of the trajectory.
Non-monotonicity would not by itself mean noise; it can be a property of
learning.

**This was not a preregistration.** The rule was stated in working discussion
before launch, but `16c` started at 19:05:41 and this file was written at
19:21:56 — during execution, before checkpoint-level completion — and both files
are still untracked. The standard demanded of the Builder elsewhere in this line
is commit-order provenance (prereg commit, then code commit, then data commit,
with the prereg hash inside the results JSON). That standard was not applied
here. Correct label: *reading rule recorded during execution, before
checkpoint-level completion; not a pre-run preregistration.* It must not be
cited as protection against having seen the data.

Five points are **not** five replications: one training seed, one task set,
sequentially dependent checkpoints. Neither outcome changes any essay claim or
authorizes Phase 2. The first evidential step, if the shape holds, is an
independent training seed with the estimand registered before the run under the
same provenance rule used for the frame audits: a prereg commit, then a code
commit, then a data commit, with the prereg hash recorded inside the results.
