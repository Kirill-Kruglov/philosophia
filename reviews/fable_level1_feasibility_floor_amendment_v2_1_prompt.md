# Fable 5 prompt: one-paragraph Level 1 floor-amendment v2.1 correction

Write a **single-paragraph bounded correction** to the Level 1 feasibility-floor
amendment v2. This is not a design revision. Preserve the v2 draft and every
historical artifact unedited. Do not change any scientific cell, schema, path,
cap, hash, source-pin principle, terminal route, signature token, or gate.

Do not implement code, create an authorization, run a probe/trajectory, inspect a
series, compare arms, select N3, create a lock, or generate panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md`
2. `reviews/fable_level1_feasibility_floor_amendment_v2_closure.md`
3. `reviews/opus_level1_feasibility_floor_amendment_v2_final_confirmation.md`
4. `reviews/sol_level1_feasibility_floor_amendment_v2_final_confirmation.md`

Both final reviews confirmed every substantive closure and returned
`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL` for exactly one ambiguity:
§6's phrase "written and committed before any learner step." They agree that a
Git commit before step 1 is unnecessary and that the reviewed v1-style durable
atomic claim discipline must govern.

## The only permitted correction

Supersede exactly this v2 §6 sentence:

> The durable v2 claim is written and committed **before any learner step**; the
> report is written **atomically after valid completion**.

with exactly this normative paragraph, combining Sol's stricter process wording
and Opus's archival clarification:

> Before any learner step, the driver durably creates the canonical v2 claim by
> writing canonical JSON to a new same-directory temporary file, `fsync`ing the
> file, atomically installing it at the absent canonical claim path without
> replacement, and `fsync`ing the parent directory; no Git commit of the
> generated claim is required. The valid report is installed by the same durable
> atomic-create protocol only after valid completion. Git archival of the
> terminal artifacts (claim and report) occurs only after the valid report is
> installed and is never a precondition of any learner step; the pre-run Git
> guards remain exactly the reviewed set: clean tracked tree, empty index,
> `EXPECTED_HEAD == HEAD`, and the authorization and public-root transcript
> Git-tracked. Any failure after durable claim installation and before valid
> report installation is `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more
> specific frozen invalidity cause), leaves `censored_at_b` unset, and authorizes
> no automatic rerun.

Do not paraphrase this paragraph. State that it replaces only the quoted §6
sentence. It must not imply that the driver itself performs Git archival; archival
is an out-of-band post-report act, as in v1.

## Deliverables

Write exactly:

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`
2. `reviews/fable_level1_feasibility_floor_amendment_v2_1_closure.md`

The correction must say v2 carries forward in full except for the one quoted
sentence. The closure verdict must be exactly:

`READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_SIGNATURE_CONFIRMATION`

The closure must include a one-row replacement table, confirm that nothing else
moved, and ask each reviewer only this yes/no question: did the exact paragraph
land and does it remove the sole blocker without changing another cell?

State that `I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains unauthorized
until both bounded signature confirmations are written. Confirm no code,
authorization, entropy, probe, trajectory, comparative datum, N3, lock, panel,
escrow, or outcome was created.
