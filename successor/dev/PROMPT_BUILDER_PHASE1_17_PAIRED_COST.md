# PHASE1_17 — paired search cost on already-collected artifacts

Status: `DESCRIPTIVE_ONLY__NO_VERDICT_TOKEN`
Compute: none. No training, no re-run, no checkpoint loaded for search.

## Why this exists

Every Phase 1 external reading so far has been **binary** — solved or not, out
of 30. That metric produced `FLAT` (an artifact of a 2000-node ceiling), then
`BUDGET_MASKED` (11 → 13 at 8000, four discordant pairs, exact McNemar
one-sided `p = 0.31`), then a non-monotone curve `[11, 19, 11, 11, 13]` across
`ck0..ck4`. Thirty binary outcomes cannot resolve any of it.

16D established, by reading `proofsearch.py` rather than by reseeding, that the
search itself contains no randomness. That fact has been treated as a
limitation. It is an asset: **the difference in search cost between two
checkpoints on the same theorem is a pure checkpoint effect with exactly zero
noise.**

This ticket extracts the continuous quantity that has been collected four
times and never read.

## Scope

Read-only over existing artifacts from 16B, 16C and 16D. Produce one results
JSON and one short table. **No verdict token, no threshold, no kill.** This is
description; nothing here can be wrong in the way a degenerate reading rule is
wrong, because there is no rule to be degenerate.

## Items

**1. Locate the cost counter.** Determine what per-problem search-cost quantity
the existing logs actually contain — node expansions, MCTS iterations,
verifier calls, wall seconds — and which of those are host-independent.
Report the counter's name, where it is emitted, and its unit.

If no host-independent per-problem counter was recorded, **say so and stop
item 2**. Name the smallest instrumentation change that would record it on the
next run. Do not substitute wall seconds for expansions and do not
reconstruct a count from timings.

**2. Paired cost table.** For every ordered checkpoint pair `(ck_i, ck_j)` at
budget 8000, restricted to the theorems solved by **both**:

- `n` = size of the intersection;
- per-theorem cost for each checkpoint, listed, not only summarized;
- count of theorems where `ck_j` is cheaper, costlier, identical;
- median and interquartile range of the per-theorem ratio `cost_j / cost_i`.

Report every numerator and denominator.

**3. Set membership, explicitly.** For each checkpoint at 8000, the exact set
of solved theorem names. The curve `[11, 19, 11, 11, 13]` has been read as a
count; print the sets so that gains and losses are visible as identities. In
particular, name the eight theorems solved at `ck1` and lost at `ck2`.

**4. Clustering of the ck1 → ck2 losses.** For those eight, report shared
structure available from the logs alone — statement length, proof length where
known, whether their searches at `ck1` terminated near the 8000 cap. Three
readings are being distinguished and they differ in what the run means:

- a related cluster (one event, not eight — effective `n` far below 30);
- a threshold effect (all eight sat just under the cap at `ck1` and just over
  at `ck2` — an artifact, not a loss of knowledge);
- divergent search (different first branchings).

Report what the logs support. **Do not choose between the three if the logs
do not decide it.**

## Analysis discipline

The 30 Kleene theorems are a fixed external set, not a sample from a
population of theorems. Every quantity here is therefore a deterministic
description of that set. **No hypothesis test, no confidence interval, no
bootstrap** — including no signed-rank test on the paired costs, however
tempting the paired structure makes it.

## Provenance

Record raw-byte and LF-normalized SHA-256 for every input artifact read and
for the analysis script. Quote the same digests in the report. In B2/09 the
results JSON recorded a `script_hash` matching no document because the
executed file was CRLF and the archived copy LF.

## Cap

One analysis script, `<= 150` lines, plus a results JSON. Read-only over
existing artifacts; the script must not import training, search, or
checkpoint-loading code. If a needed number is absent from the artifacts,
report its absence — do not regenerate it.

## Negative authorization

No training, no search, no checkpoint loaded, no seed run, no new
instrumentation executed, no scientific claim, no commit to a citable path.
The output is a description of data already collected.
