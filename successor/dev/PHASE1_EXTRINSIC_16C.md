# PHASE1_EXTRINSIC_16C

NON-CITABLE Phase-1 diagnostic. Not an experiment. No scientific claim.
Completes the five-checkpoint curve at budget 8000 begun in
`PHASE1_EXTRINSIC_16B.md`.

## SHAPE VERDICT

```text
NONMONOTONE_SHAPE
```

Classified by the rule recorded in `PHASE1_EXTRINSIC_16B.md` before ck1-ck3 were
measured. The rule is a shape classification and carries no evidential bar.

## Result

Same 30 Kleene statements, `problemset=kleene`, budget 8000,
`accumulate_library=false`, seed 0, run dir `outputs/2026-08-10/00-14-33`.
ck0 and ck4 from 16B; ck1-ck3 from [this run](run_phase1_extrinsic_16c.sh).

| checkpoint | solved @2000 | solved @8000 | budget response | mean elapsed @8000 |
| ---: | ---: | ---: | ---: | ---: |
| ck0 | 11 / 30 | 11 / 30 | +0 | 181.5 s |
| ck1 | 11 / 30 | **19 / 30** | **+8** | 124.3 s |
| ck2 | 11 / 30 | 11 / 30 | +0 | 134.2 s |
| ck3 | 10 / 30 | 11 / 30 | +1 | 152.7 s |
| ck4 | 11 / 30 | 13 / 30 | +2 | 159.1 s |

Sequence at 8000: `[11, 19, 11, 11, 13]`.

ck2 and ck3 solve exactly the ck0 set — no gains, no losses. ck1 adds
`kleene_2, 3, 4, 5, 6, 7, 8b, 13`. ck4 adds `kleene_3, 6, 7` and loses
`kleene_20`.

## Not a loading artifact

Checked before interpreting, because three checkpoints returning an identical
solved set is the signature of a silent load failure:

- `0.pt`..`4.pt` have five distinct md5 sums;
- each result JSON records its own `agent_path`, all five distinct;
- budget 8000 and seed 0 recorded identically in all five.

## What this changes

**The endpoint comparison in 16B was not a trend.** Checkpoint-to-checkpoint
variation (11 to 19 and back to 11) is four times the ck0->ck4 difference (+2)
that 16B reported. Two points were sampled from a sequence whose variation
exceeds the effect they appeared to show.

**"Later checkpoint is better" does not survive.** The best checkpoint on this
external set is ck1, not ck4.

**What does survive, narrowly:** the cold policy converts a 4x search budget
into exactly zero additional solves, while trained policies convert it into
between zero and eight. A learned policy can make search budget usable; nothing
here shows that later training makes it more usable.

**Non-monotonicity is not automatically noise.** It may be a property of this
training run: the training-side proven fraction also collapsed at iteration 2
(0.34 / 0.16 / 0.11 / 0.165 / 0.18). With one training seed and one evaluation
seed these two explanations cannot be separated.

## Dominant uncertainty, and the cheapest probe for it

The dominant uncertainty is no longer direction but **variance**. Thirty binary
items with swings of eight cannot support any trend claim.

**Correction, from `PHASE1_EXTRINSIC_16D`.** This section originally proposed
re-seeding the evaluation on the premise that "MCTS is stochastic". That premise
is false. The evaluation path contains no randomness: `random` is used in
`proofsearch.py` only for training-example sampling and for problem-selection
strategies that this eval path does not use, and UCT ties are broken by element
order. Re-seeding therefore cannot measure anything here, and 16D confirmed it
empirically — four seeds, byte-identical solved sets.

The uncertainty that remains unmeasured is training-seed variation, task
sampling, and dependence within the Kleene set. None of it is reachable by
re-running the evaluator.

Only after that does a second training seed become a sensible purchase, and it
must then carry commit-order provenance: prereg commit, code commit, data
commit, prereg hash inside the results.
