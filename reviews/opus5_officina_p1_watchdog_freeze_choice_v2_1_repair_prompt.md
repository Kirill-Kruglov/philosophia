# Task: bounded v2.1 correction of the P1 watchdog-freeze choice packet

You are Claude Code Opus 5 acting as specification author, not an independent reviewer. This is a bounded correction of five concrete specification defects, not a new mechanism round. Do not implement code, execute process control, activate T, or alter scientific/programme state.

## Inputs

Read the committed bytes of:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
- `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md`
- `reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md`
- `reviews/sol_officina_p1_watchdog_freeze_choice_v2_confirmation.md`
- the governing composite and peer corrections cited by those confirmations

Treat both `REVISE` verdicts as binding. Preserve all existing files untouched.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md`
2. `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_1_closure.md`

The correction carries v2 forward except for the exact replacements below. Do not select W-A/W-B and do not accept any amendment token.

## Mandatory repairs

### 1. Bind `CLOCK_MONOTONIC`

Close X R-A:

- Add `CLOCK_MONOTONIC` as the second explicit pinned-integer-constant addition to the §P1-3.4 PCS binding block, alongside `_MSG_EOR`.
- Pin its source/value/validation and exact use by `_clock(CLOCK_MONOTONIC)` for `freeze_ns`.
- Count the addition in both options' blast radius, binding-block handoff, verifier rules and tests.
- Refuse structurally if the runtime binding does not equal the pinned constant; do not silently use an implicit default clock.

### 2. Complete the freezer/witness and execution-site audit

Close X R-B and reconcile it with Sol YV2-M2:

- Add every omitted normative composite site, including at minimum:
  - §P1-13.2 row-4 rationale paragraph around lines 2278-2287 (“dedicated freezer watchdog as the normal witness”, “two possible executing processes”);
  - the freeze-evidence reader sentence around line 2389;
  - invariant 89 around line 2758.
- Re-audit the whole governing composite and give the final exact site count. Do not preserve “twelve-site” wording if the count grows.
- Replace, rather than append to, every contradictory sentence.
- In invariant 89, admit the PCS autonomous §3 classifier `_killpg` path as a signed freeze-execution site. Distinguish it from the request-driven `SIGNAL_GROUP` opcode while retaining the sole-PCS-caller rule and rejecting every other writer/executor.
- Keep PCS journal state scientifically invisible and distinct from peer freeze evidence.

### 3. Complete the count-key rename surface

Close Sol YV2-M1:

- In §6.3 and the v1.3 handoff, enumerate and replace all four normative references in `OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md` that still use `current_unresolved_member_count`:
  - §N5.4 field-definition block around line 900;
  - §N5.4 legal `FREEZE_INSTANT_UNKNOWN` example around line 906;
  - §N10.2 fact-location table around line 1370;
  - §N11 crash-cut example around line 1416.
- Each must use `current_unresolved_member_count_or_null`.
- Generic definitions must say `null` iff `rejection_conjunct == 0`; non-ABSENT examples retain integer `0`.
- Update schema/readers/examples/tests and the claimed reopened-sentence count exactly.

### 4. Separate the two observation schemas in R2

Close Sol YV2-M2:

- Replace v2 §7.3 `R2` so that row-4 `t-freeze-observation.v1` is written only by the supervisor on the signed dead-watchdog route.
- State separately that §N5 `ABSENT` writes `t-freeze-fallback-observation.v1` under `WATCHDOG/FREEZE_FALLBACK/`.
- Never assign the fallback object to the row-4 freeze-observation writer/class/namespace.

### 5. Remove the fallback route from R9

- Remove §N5 `ABSENT` from `R9`'s row-4 executing-process clause.
- Keep `R10` semantically unchanged: the row-4 freeze-witness function is called from the supervisor's dead-watchdog route only.
- Update the closure dispositions for X F1/F3 and Y-C3 accordingly.

## Preserve

- Every mechanism finding both confirmations accepted as closed.
- The total PCS classifier, W-A one-shot gate, W-B endpoint-loss semantics, pre-action journaling, nullable ABSENT values, full charging, publication boundary and recommendation remain unchanged.
- `process_id` remains a constructible opaque claim identifier, not a PID.
- No new author cell is opened.
- W-B may remain recommended, but neither option is selected.
- Identity cell remains unselected.
- `T = NOT_ACTIVATED`; programme claim `OPEN`.

## Closure requirements

Include:

- verdict `READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_1_FINAL_XY_CONFIRMATION` only if all five repairs are exact;
- hashes and a five-row replacement index;
- one-to-one disposition of X R-A/R-B and Sol YV2-M1/YV2-M2;
- final corrected normative-site count and exact blast-radius delta;
- no-regression table for all already-closed findings;
- one bounded yes/no confirmation question per reviewer;
- residual author choices and explicit negative authorization.

Do not modify existing files. Report created paths, verdict, and recommendation after repair.
