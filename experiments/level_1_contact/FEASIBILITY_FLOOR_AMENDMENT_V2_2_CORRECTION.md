# Level 1 feasibility-floor amendment — v2.2 exact-text correction

Status: `BOUNDED_CORRECTION_FOR_SIGNATURE_CONFIRMATION`. This resolves
the sole Sol v2.1 finding
(`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_1`): the v2.1 normative
paragraph added report-`fsync`, Git-archival timing/scope, and pre-run
Git-guard language beyond Sol's exact bounded replacement. Sol's
smaller text governs. `FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md`,
`FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`, and every review are
preserved unedited.

This document creates no code, no authorization, no entropy, no probe,
no trajectory, no comparative datum, no N3, no lock, no panel, no
escrow, and no outcome.

## The correction

Superseded: the entire v2.1 normative paragraph beginning "Before any
learner step…" and ending "…authorizes no automatic rerun."

Replaced by exactly:

> Before any learner step, the driver durably creates the canonical v2
> claim by writing canonical JSON to a new same-directory temporary
> file, `fsync`ing the file, atomically installing it at the absent
> canonical claim path without replacement, and `fsync`ing the parent
> directory; no Git commit of the generated claim is required. The
> valid report is installed atomically only after valid completion.
> Any failure after durable claim installation and before valid report
> installation is
> `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen
> invalidity cause), leaves `censored_at_b` unset, and authorizes no
> automatic rerun.

v2 carries forward in full except for the original §6 sentence as
successively corrected by v2.1 and v2.2. That carry-forward is not a
new requirement.

## Token

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains **unauthorized**
until both bounded confirmations of this v2.2 text are written. This
correction authorizes nothing else: no v2 authorization candidate, no
driver invocation, no implementation, no execution.
