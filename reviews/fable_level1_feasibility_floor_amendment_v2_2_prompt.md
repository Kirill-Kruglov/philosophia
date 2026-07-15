# Fable 5 prompt: exact-text Level 1 floor-amendment v2.2 correction

Write one exact-text correction resolving the sole Sol v2.1 finding. Preserve
v2, v2.1, and every review unedited. This is not a design review or an invitation
to strengthen the procedure. Do not add explanatory requirements to the
normative replacement paragraph.

Do not implement code, create authorization, run anything, inspect a series,
compare arms, select N3, create a lock, or generate panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`
2. `reviews/opus_level1_feasibility_floor_amendment_v2_1_signature_confirmation.md`
3. `reviews/sol_level1_feasibility_floor_amendment_v2_1_signature_confirmation.md`

Opus confirmed v2.1. Sol returned
`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_1` because v2.1 added report-fsync,
Git-archival timing/scope, and repeated Git-guard language beyond Sol's exact
bounded replacement. Sol's smaller text now governs. The pre-run Git guards and
all other artifact rules already remain in v2 §6 by carry-forward; do not repeat
them inside the replacement.

## Only permitted replacement

Supersede the entire normative paragraph in v2.1 beginning "Before any learner
step..." and ending "...authorizes no automatic rerun." Replace it with exactly
the following text, byte-for-byte apart from Markdown line wrapping:

> Before any learner step, the driver durably creates the canonical v2 claim by
> writing canonical JSON to a new same-directory temporary file, `fsync`ing the
> file, atomically installing it at the absent canonical claim path without
> replacement, and `fsync`ing the parent directory; no Git commit of the
> generated claim is required. The valid report is installed atomically only
> after valid completion. Any failure after durable claim installation and
> before valid report installation is
> `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen
> invalidity cause), leaves `censored_at_b` unset, and authorizes no automatic
> rerun.

Do not add the v2.1 scope-clarification sentence about archival to the normative
replacement. State outside the block only that v2 carries forward in full except
for the original §6 sentence as successively corrected by v2.1 and v2.2. That
carry-forward is not a new requirement.

## Deliverables

Write exactly:

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md`
2. `reviews/fable_level1_feasibility_floor_amendment_v2_2_closure.md`

Closure verdict:

`READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_2_SIGNATURE_CONFIRMATION`

Include a one-row delta table and confirm no other cell moved. Ask Sol whether
his exact paragraph landed. Ask Opus whether removing the extra v2.1 sentences
leaves his sole ambiguity resolved because the paragraph explicitly says no Git
commit is required and pins durable claim creation before step 1.

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains unauthorized until both
confirm v2.2. Confirm no code, authorization, entropy, probe, trajectory,
comparative datum, N3, lock, panel, escrow, or outcome was created.
