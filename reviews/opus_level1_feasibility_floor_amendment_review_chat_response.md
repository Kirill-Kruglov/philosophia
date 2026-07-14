Written to `reviews/opus_level1_feasibility_floor_amendment_review.md`.

## Verdict: `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

The gate route is right and the repair is a legitimate parameter-free, symmetric training-policy change â but it ships with an overclaiming justification and a dangerous failure-routing merge. Five mandatory edits, one near-Critical.

**Critical**
- **AM-1 â resource stop â  learner floor.** The draft's single "censored again, or invalid execution â BLOCKED" route folds a *completed* zero-solve run together with a 36 h **wall-hit**, OOM, or crash. A wall-hit is a RESOURCE_STOP (the run never completes B, so `censored_at_b` isn't even defined), and routing it to `BLOCKED_LEVEL1_FEASIBILITY` would narrate a resource/platform limit as a permanent verdict against the learner â contrary to C6's own distinct taxonomy (resource infeasibility vs feasibility-gate failure). Must be split; "no third attempt" must be scoped to *no third floor amendment*, leaving a clean resource-cap re-execution (A6 category) available.

**Major**
- **AM-2 â wrong axis.** The `63,504 / 2,001,000 / Ã31.51` arithmetic is correct but it's *cumulative examples processed* (compute cost), not learning capacity. Under `reduction='mean'` with `U=1`, the optimizer-update count is **2000 in both regimes** â I verified it against `train.py`. On the axis Level 0 actually anchors (updates), Level 0 generalized at **5,200â7,700 updates**, so Level 1 sits *below* the anchor, not "â400Ã below." Level 0 can anchor only optimizer family/betas + full-batch viability. Strike every "example-gradient budget / â400Ã / â10Ã below" claim.
- **AM-3 â v2 protocol under-specified:** no report schema, no distinct authorization path, no source pin over the *amended* code, caps must set `scorer_steps:0`/36 h, and the v1 link must be *verify-and-refuse-on-mutation*. Plus the update-rule change edits **signed spec text** (A5 Â§5 / v3 Â§5, retiring `("L1","replay",â¦)`) and must be written as explicit signed replacement text, not decision-draft prose.
- **AM-4 â Â§6's "â¤30 h upper bound" is a planning projection, not a bound** (per-step example ratio at t=2000 is 62.5Ã, not 31.5Ã; full-batch memory/latency is unmeasured).
- **AM-5 â branch-2 rejection predicts unobserved arms/worlds** ("scout would predictably yield all-censoredâ¦ designed to route to INSUFFICIENT") â a forbidden inference from one RANDOM-STATIC fixture. Rest the block on gate-order prudence + the mechanical budget argument instead.

**Minor:** AM-6 (replay retirement is clean â state it as a proof; mean-reduction makes history order immaterial), AM-7 (name the temporal-weighting property honestly).

**The five questions:** (1) Branch 1 is correct, conditional on the edits. (2) Honest single repair; Level 0 anchors only optimizer-family/betas + full-batch viability, not update count/exposure/solve probability. (3) Bounded implementation/resource pre-check is eligible *after* signature, *before* v2 execution, structured so it can't become a config search. (4) Five distinct routes (table in the review), with resource/process/seal invalidity never recorded as `censored_at_b`. (5) **A bounded re-confirmation is required before signing** â the edits touch signed spec text and the failure taxonomy â plus Sol's outstanding statistical cross-check.

**Boundary:** preparation only, after signature â Codex may draft the corrected amendment + the v2 authorization *candidate*, but must not assert tokens, commit, invoke any driver, run a trajectory/scorer, draw entropy, inspect any series, compare arms, select N3, lock, panel, escrow, or produce an outcome.

**Confirmed:** I ran no feasibility trajectory and created no entropy, comparative datum, N3, lock, panel, escrow, or outcome; edited/committed nothing; inspected no series. My only actions were reading the governing files and re-deriving the arithmetic.
