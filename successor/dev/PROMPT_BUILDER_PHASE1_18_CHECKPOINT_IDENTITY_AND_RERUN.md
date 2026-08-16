# PHASE1_18 — checkpoint identity, then the instrumented re-run

Status: `INSTRUMENT_INTEGRITY__NO_SEED_SPEND_AUTHORIZED`
Compute: minutes for part A, hours for part B. No training. No new seed.

## Why this runs before any seed

PHASE1_17 established two things that together block the multi-seed run:

1. **No host-independent per-problem search-cost counter exists** in the
   16B/16C/16D artifacts. `mcts_expansions` was never written. Every earlier
   statement about cheaper search — including "159 s vs 181 s" in 16B — was
   wall seconds presented as search cost, and no other quantity was ever
   recorded.
2. **`ck2` and `ck3` solve exactly the set `ck0` solves.** Not the same count —
   the same theorem identities. `ck4` is `ck0` minus `{20}` plus `{3, 6, 7}`,
   and `ck1` strictly dominates `ck4`.

Two checkpoints in a row reproducing the cold set to the last identity is not
something that happens on its own. Until it is explained, `BUDGET_MASKED` and
the whole `[11, 19, 11, 11, 13]` curve are provisional, and spending 18.5
hours per seed on top of them is spending on an unverified instrument.

## Part A — checkpoint identity (minutes, run first)

For `ck0 .. ck4`:

- SHA-256 of each checkpoint file;
- a parameter-level digest computed after loading — a stable hash over the
  loaded tensors, not over the file — so that a silent load failure is visible
  even when the files differ;
- pairwise equality of those digests;
- confirmation that the evaluation path actually loaded the checkpoint it was
  asked for, traced in code, not inferred from filenames.

Three outcomes, and the ticket does not choose between them:

- **weights differ, sets identical** — a fact about transfer: training moved
  the parameters and did not move external behaviour on this set. The curve
  stands and Part B proceeds.
- **weights identical** — the checkpoints are not distinct states; the curve
  is void and Part B is pointless until the training loop's checkpoint cadence
  is fixed.
- **load path defective** — `ck2`/`ck3` ran cold. The curve is void, and this
  is an instrument defect of the same class as B2/09's corpus mismatch.

**Stop after Part A and report.** Part B is authorized only on the first
outcome.

## Part B — instrument, then re-run evaluation

Add one field: `mcts_expansions`, the sum of `n_entered` over
`MonteCarloTreeSearch.evaluate`, written into every per-problem JSON record.
Nothing else changes — no training, no policy change, no budget change, no
checkpoint change.

Re-run external evaluation for `ck0 .. ck4` on the 30 Kleene theorems at
budget 8000, identical in every other respect to 16C.

**This re-run is its own positive control.** 16D established, by reading
`proofsearch.py`, that the search contains no randomness. The re-run must
therefore reproduce `[11, 19, 11, 11, 13]` and the exact solved sets from
PHASE1_17 §3. If it does not, the determinism finding is wrong, and that
matters more than any cost number this ticket would produce. Assert set
equality against the PHASE1_17 sets fail-closed and report the comparison
whatever it shows.

Then emit the paired table PHASE1_17 could not build: for every ordered
checkpoint pair, restricted to theorems solved by both — `n`, per-theorem
expansions for each checkpoint listed individually, counts cheaper /
costlier / identical, and the median and interquartile range of the ratio.

## Schema guard

Add a fail-closed schema check, used by this and every later analysis: **any
analysis claiming a "search cost" quantity is refused unless
`mcts_expansions` is present on every record it reads.** `elapsed_s` is never
a substitute and no count may be reconstructed from timings. This guard exists
because the defect it prevents has already been published once.

## Analysis discipline

The 30 Kleene theorems are a fixed external set, not a sample. Every quantity
is a deterministic description of that set: **no hypothesis test, no
confidence interval, no bootstrap**, including no signed-rank test on the
paired expansions however tempting the paired structure makes it.

No verdict token. This ticket restores an instrument; it decides nothing.

## Provenance

Raw-byte and LF-normalized SHA-256 for the script and every input and output,
quoted identically in the report and the JSON.

## Cap

`<= 150` lines for Part A plus the instrumentation diff; the diff must touch
only the record-writing path. Hard ceiling 6 wall hours for Part B across all
five checkpoints. Stop early on any Part A outcome other than the first, or on
a set-equality failure in Part B.

## Negative authorization

No training, no new seed, no policy or budget change, no curriculum, no
scientific claim, no commit to a citable path. The multi-seed run remains
unauthorized until Part A returns the first outcome and Part B reproduces the
PHASE1_17 sets.
