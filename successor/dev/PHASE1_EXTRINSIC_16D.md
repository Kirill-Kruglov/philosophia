# PHASE1_EXTRINSIC_16D

NON-CITABLE Phase-1 **evaluator audit**. Not an experiment. No scientific claim.
This is not evidence about the stability of the method; it is evidence about the
instrument.

## CLASSIFICATION

```text
EVAL_RESEED_PROBE_VOID_BY_DETERMINISTIC_SEARCH
REALIZED_CK1_GT_CK2_ON_FIXED_TASKSET
TRAINING_AND_TASK_FRAME_UNCERTAINTY_UNMEASURED
```

## What was run

ck1 and ck2 re-evaluated at seeds 1, 2, 3 (seed 0 from 16C), budget 8000, same
30 Kleene statements, `accumulate_library=false`
([run script](run_phase1_extrinsic_16d.sh)). Nothing retrained.

| checkpoint | seed 0 | seed 1 | seed 2 | seed 3 |
| ---: | ---: | ---: | ---: | ---: |
| ck1 | 19 | 19 | 19 | 19 |
| ck2 | 11 | 11 | 11 | 11 |

Solved sets are identical across seeds, not merely equal in count.

## Why: verified in code, not inferred from the numbers

`proofsearch.py` uses `random` only at the training-example sampling site and in
problem-selection strategies that this evaluation path does not exercise (it
iterates `problem_names()` in order). The MCTS loop contains no sampling; UCT
ties resolve by element order. The seed is set in `evaluate_agent` but nothing
downstream consumes it.

**The evaluation is deterministic by construction.** The probe was structurally
incapable of returning its own negative branch.

## What this establishes, and what it does not

Establishes, narrowly: the ck1-vs-ck2 gap is not produced by evaluation-seed
randomness, because this evaluator has none.

**Correction from `PHASE1_EXTRINSIC_17`.** This section originally read
"conditional eval variance is zero". That is false. Seed-independence is not
run-invariance: re-running ck1 at the same seed and budget after a behaviourally
neutral code edit produced 20/30 instead of 19/30, the extra theorem being
`kleene_12` at 7711 of 8000 expansions — a marginal case at the cap, plausibly
flipped by floating-point and reduction-order nondeterminism under 16 threads.
Correct wording: the evaluator is **seed-independent but not run-invariant**,
and every binary count in this line carries roughly +-1 of run-to-run noise.

Does **not** establish: that the gap is large relative to unmeasured
variability. Zero here means *not measured*, not *small*. Training-seed
variation, task sampling, dependence within the Kleene set, and behaviour in
another formal domain are all untouched.

Correct wording going forward: *one realized training run produced a sharply
non-monotone external trajectory under a fixed deterministic evaluator*. Not
"the training trajectory is unstable" — that needs training seeds.

## The eight lost theorems are not eight events

`kleene_2, 3, 4, 5, 6, 7` are implication transitivity, premise permutation and
export/import with conjunction; `8b` is monotonicity of conjunction under
implication; `13` is contraposition. This is one tight implicational-
compositional cluster plus one contraposition — on the order of two capabilities,
not eight independent observations. **The effective sample size of the 30-item
set is materially below 30**, and every binary count in 16, 16B and 16C inherits
that.

The competing "all eight were merely near the 8000 cap" explanation is not
supported: last visible tqdm marks for ck1's wins are 2274, 4157, 4197, 4733,
4945, 6324, 7007, 7854 of 8000, so at least five are not marginal. (These marks
are approximate: tqdm refreshes on a timer, not per node.)

## A paired cost series is NOT available from these files

A per-theorem expansion-cost comparison across checkpoints would be far more
powerful than the censored binary count, and under a deterministic evaluator it
would carry no noise at all. It cannot be extracted from what we have:
`MonteCarloTreeSearch.evaluate` returns an expansion counter, but
`ProofSearchResult.iterations` records outer agent actions instead — verified as
`0` for every success and `1` for every exhaustion in our own results. Obtaining
the cost series requires instrumenting the search and re-running; it is not free.

## Two process defects, and the pattern behind them

1. **The reading rule could not fail.** `CHECKPOINT_DIFFERENCE_STABLE := ck1 >
   ck2 at every seed` can only return STABLE under a deterministic evaluator.
   Its two branches are also neither mutually exclusive nor exhaustive.
2. **The run was not stopped early.** The degenerate outcome was predicted before
   launch and was visible after the first of six runs; ~6.5 h were spent where
   ~1 h sufficed.

The pattern joining this with the 16B defect: **both rules set a threshold but
no magnitude.** A binary rule on a deterministic instrument has no degrees of
freedom. The Wall-B memo already fixed this by making the primary quantity
continuous; Phase 1 keeps reproducing the defect because its default metric is
binary. Rules in this line must henceforth (a) be checked for reachability of
both branches before launch, and (b) carry a magnitude, not only a direction.

## Provenance

The reading rule was written into the run script before launch, but the script
was not committed first. Dev chronology, not preregistration.

## Consequence for the next purchase

The binding constraint is the **task set**, not the training seed. Thirty binary
items with an effective n well below 30 will not settle a trend at any number of
seeds. A larger held-out set must stay in the *propositional-logic* theory the
checkpoints were trained on — the Natural Number Game is not a valid extension
here, since it uses the arithmetic theory with a different action set.
