# PHASE1_18 Part B — amendment 5

Status: `PART_B_AUTHORIZED_AS_AMENDED__NO_SEED_SPEND`
Binding before the gate fires. Arm priority from amendment 2 unchanged.

## Q1 exposes a defect in the gate itself, not only in the `ck0` case

The gate as written declares `INSTRUMENT_DEFECT__OMP1_SET_MISMATCH` when the
`OMP=1` five-checkpoint run differs from the PHASE1_17 pins.

**The PHASE1_17 pins were produced at `OMP=16`.**

So the gate compares a single-threaded run against a multi-threaded reference
and treats any difference as a defect — while the entire reason this ticket
exists is that thread configuration flips theorems, with a floor of at least
one (`kleene_12`, between `16C` and `17`, at the *same* configuration). The
gate can therefore fire for exactly the phenomenon it was built to measure,
and stop the run that would have measured it.

This is the same shape as the rules retired in 16B and 16D, in the opposite
direction: not a rule that can only pass, but a rule that fires on the
expected outcome and reports it as a fault.

### Amended gate

Set equality against the PHASE1_17 pins is **reported, not gated**. It is
configuration sensitivity and it is one of the three quantities amendment 2
named.

The gate stops the run only on **structural** defects, which are unambiguous
and cannot be produced by thread interleaving:

- a results object missing, unreadable, or with a record count other than 30;
- a problem-name set that is not the Kleene set;
- `mcts_expansions` absent on any record (the existing schema guard);
- `omp_num_threads` absent or not equal to 1 on an `OMP=1` object;
- a checkpoint solving zero theorems;
- an `agent_path` in the results not matching the checkpoint requested.

No threshold on set difference is introduced. Any number chosen now would be a
guess: the configuration-sensitivity floor is known to be at least one theorem
and has no measured upper bound, so a cutoff would encode a belief the data do
not yet support.

### Consequence for `ck0`

The specific case asked about — pre-patch `ck0` matches the pins, post-patch
re-run does not — is therefore **a recorded finding that continues**, for the
same reason as the `ck1` determinism mismatch in amendment 3, plus one of its
own: **continuing is what resolves it.**

That disagreement has two possible causes and the comparison alone cannot
separate them:

- the D1 patch is not inert and changed search behaviour;
- `OMP=1` is not deterministic.

The queued `ck1` `OMP=1` repeat, same binary on both sides, separates them. If
it is identical, `OMP=1` is deterministic under the patched binary and the
`ck0` disagreement is the patch. If it also differs, the determinism
assumption is false and the patch question is moot. Stopping at `ck0` would
discard the only measurement that distinguishes the two.

**Hard consequence if it fires**, written now rather than discovered later:
the central finding — that `ck2` and `ck3` solve exactly `ck0`'s identities —
is currently stated against a pre-patch `ck0` while `ck2` and `ck3` are
post-patch. If `ck0` proves binary-sensitive, that identity claim is not
established and must be restated against a homogeneous arm before it appears
in any document.

## Q2 — yes, and as one file, not four

`PROVENANCE_CLASSES.md` should exist, but not alone. Five standing rules have
now been extracted from incidents across B2/09, TWOPRES and PHASE1_18, and
five one-page rule files would be their own apparatus problem — the failure
mode this programme keeps writing caps to prevent.

One file, `successor/dev/STANDING_RULES.md`, provenance classes as its first
section. Each rule records the incident that produced it, because a rule
without its incident gets read as bureaucracy and quietly dropped. A starting
set is supplied alongside this amendment; it is a draft to be extended, not a
frozen contract, and it carries no verdict token.

## Unchanged

Analysis discipline, schema guard, provenance hashing, caps and negative
authorization stand. No training, no new seed, no policy or budget change, no
verdict token. The 30 Kleene theorems remain a fixed external set: no
hypothesis test, no confidence interval, no bootstrap. The multi-seed run
remains unauthorized until the noise floor exists.

This amendment is the last before the Part B report, as declared in amendment
4. It exists because the gate would otherwise have fired on the expected
outcome, and it had to be corrected before that happened rather than after.
