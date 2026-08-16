# PHASE2_STAGE_B — two pre-signature probes

Status: `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`
Compute: CPU, hours. No audit root, no carrier candidate, no learner.

## Why these run before the signature

Disposition 20 asks the author to sign choices A–E. Two facts that A and E
depend on are currently assumed rather than measured, and both are answerable
in about an hour. Signing first would be signing over an assumption — and
choice A, if wrong, is not cheap to reverse: it is the object language, and
changing it later requires a new version and fresh roots.

This is the B2/09 lesson applied forward: that arm was answerable from a
single init probe before any harness existed, and the probe was run last.

Both probes use **disposable development roots only**, domain-separated from
the audit keyspace by a distinct PRF label. Every identity produced here is
permanently barred from the audit, the cost block, the selector, the pilot and
the scientific frame.

## Probe A — per-premise enumerability

The theory file declares nine premises. `not_e` carries no
`#forward`/`#backward` annotation while the other eight do. The standalone
feasibility note nonetheless reports that direct traces for `not_i`, `not_e`
and `exfalso` terminated. **Those two facts are in tension and one of them is
wrong.**

It matters because the annotations determine the action space. If `not_e` is
not enumerable as an action, every plan using it compiles to nothing — while
choice C requires at least three distinct rule families per retained plan and
requires every declared hypothesis to be used. The frame would be silently
biased and the bias would be invisible in the audit.

Produce a table, one row per premise: annotation present, enumerable as a
forward action, enumerable as a backward action, and a minimal hand fixture
that exercises it end to end — typed check, compile, fresh-process replay to
an empty goal.

Report the table whatever it says. If `not_e` is not enumerable, that is a
finding about choice C and about the seven-family partition, not a defect to
be worked around.

## Probe B — is the §9 positive control realizable under grammar A?

Choice A fixes `F ::= atom | false | (not F) | (and F F) | (or F F)`.
Implication is not a formula constructor, and the theory declares no
implication-elimination premise.

The §9 positive control is a depth-graded implication-DAG family, and a failed
positive control returns `CARRIER_CLOSED_NO_USABLE_FRAME` — a carrier kill.
**So an unrealizable control would kill a carrier that is otherwise fine, and
the grammar that makes it unrealizable is being signed now.**

Construct by hand, on dev roots, one instance of the intended family at
depth 1 and one at depth 3, expressed under grammar A with ambient arrows
occurring only in the outer sequent and in the declared premise types of
`or_e` and `not_i`. For each: does it type-check, compile to primitive Peano
actions, and replay to an empty goal in a fresh process?

Then state one of three outcomes, plainly:

- **realizable** — the family expresses under A; §9 stands as written;
- **realizable with a changed family** — A stands, but the positive control
  must be redesigned before it can gate anything; describe what changes;
- **not realizable** — A and §9 are incompatible, and the author must choose
  which one moves. Do not choose for the author.

Whichever it is, the depth grading must be checkable: Spearman over depth is
what §9 scores, so a family whose depth cannot be varied under A fails even if
a single instance types.

## Shared requirements

- CPU only, one process, one thread, deterministic; two fresh executions must
  agree byte for byte;
- dev roots only, distinct PRF domain label from `audit`; every identity
  recorded and permanently excluded;
- `<= 150` lines total across both probes, plus a results JSON;
- hard ceiling **3 wall hours** across both;
- Lenovo Legion excluded from experimental runs — its 8 GiB VRAM gave no
  expected performance gain; record the exclusion and its reason in the log
  so it travels with the artifact;
- raw-byte and LF-normalized SHA-256 for the script and every input, quoted
  identically in the report and the JSON.

## What the results may and may not do

They may inform choices A, C and E, and they may block the signature.

They may **not** set any threshold, band, cap, or scientific constant, and no
number produced here may appear in the later audit contract as a calibration.
These are existence facts about the object language, not measurements of the
carrier.

## Negative authorization

No audit root, no carrier candidate, no cost block, no calibration, no
learner, no training, no selector, no SELF/YOKED, no scientific outcome, no
signature, no commit to a citable path. Accepted Stage-A behaviour is not
reopened.
