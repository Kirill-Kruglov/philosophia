# Fable 5 — Level 1 feasibility-floor amendment v2.1 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`.
Inputs: the Opus and Sol final confirmations (both
`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL`), which confirmed
every substantive v2 closure — AM-1–AM-7, the §2 literal replacement
text, the single-valued full-history rule, the §6 contract (v1 hash
pins independently recomputed and matched by Opus), the §7
validity-first strict-Sol recovery table, and all Y-line repairs
including the learner-class conditional estimand that the author token
accepts — and returned for exactly one ambiguity: §6's "written and
committed before any learner step."

## Verdict

**READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_SIGNATURE_CONFIRMATION**

## Replacement table (the entire delta)

| Location | Superseded (exact) | Replacement |
|---|---|---|
| v2 §6, claim/report sentence | "The durable v2 claim is written and committed **before any learner step**; the report is written **atomically after valid completion**." | The v2.1 normative paragraph: durable atomic claim creation before any learner step (same-directory temp file, file `fsync`, atomic install at the absent canonical path without replacement, parent-directory `fsync`; no Git commit of the generated claim required); the report installed by the same protocol only after valid completion; Git archival of the terminal artifacts only after the valid report is installed, never a precondition of any learner step and never performed by the driver (out-of-band, as in v1); pre-run Git guards unchanged (clean tracked tree, empty index, `EXPECTED_HEAD == HEAD`, authorization and public-root transcript Git-tracked); any failure between durable claim installation and valid report installation → `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen cause), `censored_at_b` unset, no automatic rerun |

**Nothing else moved.** Every other sentence of v2 — §1 narrow scope,
§2 literal signed replacement cells, §3 learner-class conditional
estimand and temporal weighting, §4 corrected provenance/arithmetic,
§5 resource table and planning projection, the rest of §6 (names,
caps, hash pins, refusals), §7 validity-first routes and future
ledger/ROADMAP lines, §8 superseded-sentence register, §9 token — and
every historical artifact carry forward verbatim. No scientific cell,
schema, path, cap, hash, source-pin principle, terminal route,
signature token, or gate changed. The reconciled paragraph combines
Sol's stricter atomic-create process wording with Opus's archival and
pre-run-guard clarification; both reviewers' requirements are contained
in it, and Opus's source-pin ruling (pin set frozen at reviewed v2
driver implementation, principle already fixed in §6) required no edit.

## Bounded signature-confirmation questions

**Opus (yes/no):** did the exact replacement paragraph land in
`FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`, and does it remove
the sole blocker without changing another cell?

**Sol (yes/no):** did the exact replacement paragraph land in
`FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md`, and does it remove
the sole blocker without changing another cell?

## Token disposition

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` remains **unauthorized**
until both bounded signature confirmations are written. After both
accept: Kirill may sign (or issue a named refusal, routing Level 1 to
`BLOCKED_LEVEL1_FEASIBILITY` by decision). Only after signature may the
v2 authorization candidate be drafted, and only Kirill's explicit
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` can execute the
one-shot check.

## Confirmation

This task created exactly the two mandated documents. No code,
authorization, entropy, probe, trajectory, comparative datum, N3
selection, lock, panel, escrow, or outcome was created; no series was
inspected; no arms were compared; nothing was committed; the v2 draft
and all historical artifacts are unedited. Every signed negative
destination is preserved verbatim; Level 1 remains a detector, never a
programme falsifier; censored and `UNKNOWN` are never success.
