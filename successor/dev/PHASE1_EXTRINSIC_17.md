# PHASE1_EXTRINSIC_17

NON-CITABLE Phase-1 measurement. Not an experiment. No scientific claim.
A measurement with an uncertainty, deliberately **without** a binary verdict:
the two previous binary rules in this line (16B, 16D) were both degenerate.

## Why this run exists

Every earlier Phase-1 reading used a censored binary count (solved / not). On a
near-deterministic evaluator with an effective sample size well below 30, such a
rule has no degrees of freedom. The fix named in `16B` and `16D` was to make the
primary quantity continuous. This run does that.

## Instrumentation (logged)

`minimo/learning/proofsearch.py`, three edits, no behavioural intent:

- `ProofSearchResult` gains `mcts_expansions: int = 0`;
- `proof_search` accumulates the counter returned by
  `MonteCarloTreeSearch.evaluate` across the outer loop;
- `evaluate_agent` records it per problem.

`iterations` was never a cost measure: it is 0 on success and 1 on exhaustion.
No algorithm, config default or theory file changed.

## Estimand, fixed before the data existed

Per theorem, MCTS expansions consumed, censored at the budget (8000) on failure.
Primary quantity: restricted mean expansions per checkpoint over the same fixed
30 statements, compared pairwise against ck0. Budget 8000,
`accumulate_library=false`, seed 0, run dir `outputs/2026-08-10/00-14-33`.

## Result

| checkpoint | solved | restricted mean expansions | saving vs ck0 | 95% CI, per-item | 95% CI, cluster as one unit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| ck0 | 11 / 30 | 5257.5 | 0 | - | - |
| ck1 | 20 / 30 | **4374.3** | **883.2** | [391, 1454] | **[64, 1690]** |
| ck2 | 11 / 30 | 5167.6 | 89.8 | [-39, 249] | [-44, 277] |
| ck3 | 11 / 30 | 5253.9 | 3.6 | [-297, 240] | [-322, 270] |
| ck4 | 13 / 30 | 4915.7 | 341.8 | [-452, 1133] | [-819, 1146] |

Paired bootstrap, 4000 resamples. The **cluster** column resamples blocks rather
than items, treating `kleene_2, 3, 4, 5, 6, 7, 8b, 13` — the implicational-
compositional family identified in `16D` — as a single unit. That is the
dependence correction; it widens ck1's interval roughly fourfold and it still
excludes zero, but only just.

Statement: after one iteration of self-training, search cost on human-written
held-out theorems falls by roughly 880 expansions per theorem relative to the
randomly initialized policy. No later checkpoint is distinguishable from the
cold policy on this measure.

## The evaluator is seed-independent but NOT run-invariant

`16D` concluded "conditional eval variance is zero" from the absence of RNG in
the search path. **That claim is falsified here.** ck1 solves 20/30 in this run
against 19/30 in `16C`/`16D` — same checkpoint, same seed, same budget. The
extra theorem is `kleene_12`, solved at **7711 of 8000 expansions**: a marginal
case at the cap, flipped by a behaviourally neutral code edit. The plausible
source is floating-point and reduction-order nondeterminism under 16 threads,
not randomness.

Magnitude: 1 of 150 theorem-evaluations changed, and its effect on a restricted
mean is bounded by about `(7999 - 7711)/30 ~ 10` expansions — an order of
magnitude below ck1's 883. It does not threaten the result; it does retire the
"zero variance" wording, and it means every binary count in this line carries
roughly +-1 of run-to-run noise.

## What this does not establish

- **One training seed.** The whole five-point trajectory is a single
  realization. Nothing here separates "property of the method" from "property of
  this run".
- **Censoring dominates.** 19 of ck0's 30 items sit at the cap, so the quantity
  measured is cost *under an 8000 cap*, not cost.
- **ck1 was not a prespecified target.** The estimand was fixed before the run;
  the interest in ck1 came from having seen all five points in `16C`. The
  interval is reported for all five checkpoints for that reason, not only for
  ck1.
- **Nothing about philosophia's question.** This measures whether self-generated
  formal training changes a search policy. It says nothing about whether
  self-chosen contact beats matched-cost donated contact; that needs ACTIVE and
  YOKED arms, which are Phase 2 and unauthorized.

## Phase-1 status after this run

The phenomenon is real and now measurable with a continuous, paired,
dependence-corrected quantity: **one iteration of self-training measurably
reduces the cost of proving human-written theorems it was never trained on.**
The trajectory beyond iteration 1 is non-monotone and, on this measure, flat.

The binding constraint on any further Phase-1 claim is the external set: 30
items whose effective size is materially smaller. A larger held-out set must
stay in the propositional-logic theory the checkpoints were trained on.
