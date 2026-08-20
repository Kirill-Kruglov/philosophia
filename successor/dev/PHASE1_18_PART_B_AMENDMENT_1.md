# PHASE1_18 Part B — amendment 1

Status: `PART_B_AUTHORIZED_AS_AMENDED__NO_SEED_SPEND`

Part A returned `weights_differ_sets_identical`. Five distinct file digests,
five distinct loaded parameter digests, load path traced in code. `ck2`/`ck3`
did not run cold; they are different parameter states that solve exactly
`ck0`'s identities. That is a transfer fact and the
`[11, 19, 11, 11, 13]` curve is not voided.

Part B is authorized, with one change of design forced by a fact reported in
passing rather than as a finding.

## The reason for this amendment

The Part A report notes floating-point reduction-order noise under
multithreading, which **flipped `kleene_12` in run 17**.

16D concluded that the search contains no randomness and that evaluation
dispersion is "exactly zero, and a property of construction". That conclusion
was reached by varying the **search seed** while holding the thread
configuration fixed, and by reading `proofsearch.py` for PRNG use. Neither
method can see reduction-order variance: non-associative floating-point
summation under a varying thread schedule is a different channel from a
pseudo-random number generator.

So 16D is correct about what it measured and wrong about what it concluded.
Dispersion is zero **at fixed thread configuration**. It is not zero.

This matters because the whole external reading rests on differences of two or
three theorems out of thirty. A noise channel that has already flipped one
theorem is the same size as the effect being claimed.

## Amended item — the noise channel is the first measurement

Run the 16C-identical evaluation for `ck0 .. ck4` at budget 8000 **twice**:

- `OMP_NUM_THREADS=1`, plus any other thread controls the runtime honours,
  as the deterministic reference;
- `OMP_NUM_THREADS=16`, matching 16C exactly.

Report, per checkpoint: the solved set under each configuration, the symmetric
difference, and the per-theorem `mcts_expansions` under each. **The
configuration difference is a result, not a nuisance to be tuned away.**

Then the paired cost table from the original ticket, computed on the
single-thread run, with the multi-thread run reported alongside.

## Set-equality assertion, downgraded from gate to comparison

The original ticket made equality with the PHASE1_17 sets a fail-closed gate.
With a live noise channel that gate would fire for the right reason and be
read as the wrong one, or worse, be relaxed until it passed.

Amended: compare and report. A mismatch at 16 threads is expected and is
evidence about the channel. A mismatch at **one** thread is an instrument
defect and stops the run, because the single-thread path has no remaining
declared source of variance.

## What this changes downstream

- **Single-threaded evaluation becomes the canonical instrument** for every
  later external reading, and the thread configuration is recorded in every
  results JSON from now on. A run whose thread configuration is unrecorded is
  not comparable to one whose is.
- Any earlier claim of "byte-identical across two fresh executions" — in Phase
  1 or in the Stage B probes — is to be read as byte-identical *at that thread
  configuration*, which is a weaker claim than it appeared.
- The multi-seed run stays unauthorized. Its primary quantity was going to be
  chosen from Part B; it must now also be sized against a noise floor that did
  not previously exist on paper.

No further minimo diff is needed: `mcts_expansions` is already in
`proofsearch.py` from PHASE1_17. Part B is the schema guard, the two runs and
the table.

## Unchanged

Analysis discipline, provenance, caps and negative authorization from the
original ticket stand. The 30 Kleene theorems remain a fixed external set:
no hypothesis test, no confidence interval, no bootstrap. No verdict token.
No training, no new seed, no policy or budget change.

Wall ceiling raised from 6 to 10 hours to cover the second configuration, and
for no other purpose.
