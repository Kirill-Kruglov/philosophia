# Level 1 feasibility-floor amendment — v2.1 bounded correction

Status: `BOUNDED_CORRECTION_FOR_SIGNATURE_CONFIRMATION`. This is a
single-paragraph procedural correction, not a design revision.
`FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md` and every historical artifact
are preserved unedited; **v2 carries forward in full except for the one
sentence quoted below.** No scientific cell, schema, path, cap, hash,
source-pin principle, terminal route, signature token, or gate changes.
Inputs: the Opus and Sol final confirmations (both
`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL`), which confirmed
every substantive v2 closure and flagged exactly one ambiguity — §6's
"written and committed before any learner step" — agreeing that a Git
commit before step 1 is unnecessary and that the reviewed v1-style
durable atomic claim discipline must govern.

This document creates no code, no authorization, no entropy, no probe,
no trajectory, no comparative datum, no N3, no lock, no panel, no
escrow, and no outcome.

## The correction

Superseded — exactly this v2 §6 sentence and only it:

> The durable v2 claim is written and committed **before any learner
> step**; the report is written **atomically after valid completion**.

Replaced by exactly this normative paragraph (combining Sol's stricter
process wording and Opus's archival clarification):

> Before any learner step, the driver durably creates the canonical v2
> claim by writing canonical JSON to a new same-directory temporary
> file, `fsync`ing the file, atomically installing it at the absent
> canonical claim path without replacement, and `fsync`ing the parent
> directory; no Git commit of the generated claim is required. The
> valid report is installed by the same durable atomic-create protocol
> only after valid completion. Git archival of the terminal artifacts
> (claim and report) occurs only after the valid report is installed
> and is never a precondition of any learner step; the pre-run Git
> guards remain exactly the reviewed set: clean tracked tree, empty
> index, `EXPECTED_HEAD == HEAD`, and the authorization and public-root
> transcript Git-tracked. Any failure after durable claim installation
> and before valid report installation is
> `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen
> invalidity cause), leaves `censored_at_b` unset, and authorizes no
> automatic rerun.

Clarification of scope (no new rule): the driver itself performs no Git
archival; archival is an out-of-band act after the report is installed,
exactly as in the reviewed v1 discipline. Everything else in v2 §6 —
the frozen names table, `scorer_steps: 0`, the preflight guard list,
the full recomputed v1 hash pins, the refusals on existing v2 paths and
later-gate artifacts, and the not-created-here boundary for the
authorization candidate — carries forward verbatim, as does every other
section of v2.

## Token

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains **unauthorized**
until both bounded signature confirmations of this v2.1 text are
written. This correction authorizes nothing else: no v2 authorization
candidate, no driver invocation, no implementation, no execution.
