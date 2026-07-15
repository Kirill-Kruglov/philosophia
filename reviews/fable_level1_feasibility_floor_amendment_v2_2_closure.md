# Fable 5 — Level 1 feasibility-floor amendment v2.2 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md`.
Inputs: the Opus v2.1 signature confirmation
(`LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_1_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`)
and the Sol v2.1 signature confirmation
(`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_1`), whose sole finding
was that the v2.1 paragraph exceeded Sol's exact bounded replacement.
v2, v2.1, and every review remain unedited; v2.2 supersedes only the
v2.1 normative paragraph with Sol's exact text.

## Verdict

**READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_2_SIGNATURE_CONFIRMATION**

## Delta table (the entire change)

| Location | Superseded | Replacement |
|---|---|---|
| v2.1 normative paragraph ("Before any learner step… authorizes no automatic rerun.") | The v2.1 paragraph, which added report-`fsync` protocol wording ("by the same durable atomic-create protocol"), Git-archival timing and driver-scope sentences, and repeated pre-run Git-guard language beyond the bounded replacement | Sol's exact paragraph, byte-for-byte apart from Markdown line wrapping: durable atomic claim creation before any learner step (same-directory temp file, file `fsync`, atomic install at the absent canonical path without replacement, parent-directory `fsync`; no Git commit of the generated claim required); the valid report installed atomically only after valid completion; any failure between durable claim installation and valid report installation → `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen cause), `censored_at_b` unset, no automatic rerun |

**No other cell moved.** The removed v2.1 sentences added no rule that
v2 does not already carry: the pre-run Git guards (clean tracked tree,
empty index, `EXPECTED_HEAD == HEAD`, tracked authorization and
public-root transcript) and every other artifact rule remain in v2 §6
by carry-forward, which the v2.2 document states is not a new
requirement. Every scientific cell, schema, path, cap, hash,
source-pin principle, terminal route, signature token, and gate is
unchanged; the substantive closures both reviewers confirmed (AM-1–AM-7,
the §2 literal replacement text, the learner-class conditional
estimand, the §6 contract with byte-accurate v1 hash pins, the §7
validity-first strict-Sol recovery table) stand and are not reopened.

## Bounded confirmation questions

**Sol:** did your exact paragraph land in
`FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md`, byte-for-byte apart
from Markdown line wrapping, with nothing else changed?

**Opus:** does removing the extra v2.1 sentences (report-protocol
wording, Git-archival timing/scope, repeated Git-guard language) leave
your sole §6 ambiguity resolved — given that the paragraph explicitly
says no Git commit of the generated claim is required and pins durable
claim creation before step 1, and that the pre-run Git guards and all
other artifact rules remain in v2 §6 by carry-forward?

## Token disposition

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains **unauthorized**
until both bounded confirmations of v2.2 are written. After both
accept: Kirill may sign (or issue a named refusal, routing Level 1 to
`BLOCKED_LEVEL1_FEASIBILITY` by decision). Only after signature may the
v2 authorization candidate be drafted, and only Kirill's explicit
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` can execute the
one-shot check.

## Confirmation

This task created exactly the two mandated documents. No code,
authorization, entropy, probe, trajectory, comparative datum, N3
selection, lock, panel, escrow, or outcome was created; no series was
inspected; no arms were compared; nothing was committed; v2, v2.1, and
all reviews are unedited. Every signed negative destination is
preserved verbatim; Level 1 remains a detector, never a programme
falsifier; censored and `UNKNOWN` are never success.
