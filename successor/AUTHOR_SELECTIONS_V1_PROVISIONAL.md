# Successor author selections — v1 provisional record

Recorded from Kirill Kruglov's explicit provisional selection on 2026-07-20.
Review base: `AUTHOR_CHOICE_PACKET_V1_DRAFT.md` at commit `080b699`.

Status: `PROVISIONAL_FOR_BOUNDED_XY_REVIEW`. This is not an author signature,
does not make the WP gate effective, and authorizes no implementation or
execution.

## Provisional tokens

```text
PROVISIONAL_SELECTIONS_FOR_XY_REVIEW
I_NAME_SUCCESSOR_LINE_OFFICINA
I_SELECT_SUCCESSOR_LAYOUT_SAME_REPO
I_SELECT_C_INTERPRETATION_FINITE_FRAME_SAMPLE
I_SELECT_Q_ENTROPY_SEALED_POSTFREEZE_ROOT
I_SELECT_T_ENVELOPE_ONE_WEEK
E1=168_DEVICE_HOURS
E2=12_CANONICAL_CANDIDATES
E3=48_WALL_HOURS_OR_40_DEVICE_HOURS
I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK
```

## Exact provisional meanings

### Identity and layout

The successor line identifier is `officina`. This does not select the essay or
publication title. The line remains in this repository under `successor/`, with
the predecessor as a literal hash-pinned ancestor. Scientific quarantine comes
from the signed semantics and a fail-closed path allowlist, not from the
directory boundary.

### C interpretation

The WP-3 contract must instantiate a probability sample from a fixed finite
frame with locked inclusion probabilities, analysis weights, and
finite-population correction. A valid C claim may generalize by design only to
that registered frame. Frame membership, size, support, strata, weights, and C
sample size remain WP-3/WP-9 cells and are not selected here.

### Q unpredictability policy

WP-6 must instantiate a one-shot sealed OS-CSPRNG root drawn only after the
candidate manifest and attempt claim are durable. The first entropy byte marks
launch: from that instant the attempt consumes its id, cap slot, and error
allocation even if it later becomes invalid. Before entropy, no launch exists;
recovery requires a signed pre-attempt disposition. There is no redraw,
standing fallback, or custody substitution. Concrete custody, attestation,
driver, caps, alpha spending, and Q numerics remain WP-6 cells.

### One-week T envelope

- `E1 = 168_DEVICE_HOURS`: the total aggregate active time of all processes
  training registrable learners on real T worlds. Concurrent real-T processes
  consume hours additively. Unit tests, dummy fixtures under test-only seeds,
  and smoke runs that cannot touch a real T world consume zero E1.
- `E2 = 12_CANONICAL_CANDIDATES`: at most twelve behavior-distinct canonical
  candidate registrations. A behavior-relevant change creates and consumes a
  new slot; behavior-inert changes do not.
- `E3 = 48_WALL_HOURS_OR_40_DEVICE_HOURS`: the first review checkpoint occurs
  at the earlier of 48 elapsed wall-hours after T-envelope activation or 40
  consumed E1 hours. Each later checkpoint resets both checkpoint counters and
  uses the same rule.
- Reaching E1 or E2 mechanically records `T_ENVELOPE_EXHAUSTED`. Kirill may
  record `T_AUTHOR_STOP` only as a distinct signed decision at a checkpoint.
  Any extension requires a loud signed amendment and bounded review.
- The public append-only T ledger path is `successor/officina/T_LEDGER.md`.
  Every real T run, candidate registration, checkpoint, exhaustion, and author
  stop is recorded there under the implementation contract.

These values are Kirill's provisional resource commitment. They are not
derived from predecessor efficacy or outcome records and imply no expectation
that a candidate will qualify.

### Device policy

Off-CPU T development is permitted. Before a candidate on an off-CPU stack
family may be registered for Q, that family must pass a bounded, deterministic,
non-citable breathing check under a later reviewed WP-2/WP-6 contract. Level 0's
CPU result does not transfer. The concrete stack, tolerance, and reproducibility
criterion are not selected here.

### Fixed planning surface

Strict S remains unavailable. The signed base has only T, Q, and C; this record
offers no S route or token.

## Authorization boundary

The earlier out-of-sequence text `I_AUTHORIZE_SUCCESSOR_WP1_WP2_IMPLEMENTATION`
did not satisfy the packet's review preconditions and is not an effective or
recorded authorization. After bounded X/Y confirmation, Kirill must sign the
complete selection packet together with that WP gate in one final author
record.

Until then this provisional record authorizes no WP-1/WP-2 implementation, no
world, entropy, model, candidate, run, registration, Q attempt, promotion,
scientific specification, lock, escrow, C execution, outcome, or claim change.
