# GPT-5.6 Sol Y-line review: Officina supervisor/control-channel v2

Work in `/home/master/llm_projects/philosophia`.

Perform a bounded adversarial review of idempotency, observation leakage,
validity routing, resource bounds, and scientific non-regression. Do not edit
code, tests, contracts, signatures, existing reviews, or runtime artifacts. Do
not execute any Officina process or smoke. T remains `NOT_ACTIVATED`.

## Read first

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `reviews/fable_officina_supervisor_control_channel_v2_closure.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md`
- `reviews/opus_officina_supervisor_control_channel_v1_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v1_confirmation.md`
- `reviews/codex_officina_generic_harness_implementation_review.md`
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the signed batch-settlement amendment and generic-harness composite
- current uncommitted implementation/tests, read-only, only to test contract
  implementability and non-regression

A3/B1/C1/D1 are signed author selections. Do not reopen them.

## Required attacks

### 1. B1 exactly-once semantics across generations

Trace all eight commands through lost request, lost reply, supervisor crash,
takeover, cached reply, acknowledgement, and retry.

Test the apparent generation contradiction: `request_sha256` binds
`supervisor_generation_sha256`, yet a retry after takeover necessarily names a
new generation. Under the written same-key/different-bytes rule this may become
`REPLAY_BYTES` instead of generation-total replay. Require one exact semantic
identity/rebinding rule if it is a defect.

Also test:

- journal `ACCEPTED -> COMMITTED -> REPLY_CACHED` under atomic/no-replace rules;
- whether a crash after effect but before phase update can ever re-apply;
- `OPERATION_ADMIT` retry without a second worker, cursor, reservation, or
  charge;
- how `OPERATION_STATUS ack_delivery=true` can acknowledge a prior response
  without changing bytes under the same idempotency key;
- release-token redelivery, the relation between request ack and delivery ack,
  and the `ALREADY_DELIVERED` value missing from the earlier closed phase set;
- journal GC without losing future replay proof.

### 2. Reachability of the output-bound protocol

The draft requires supervisor-owned `BOUND.json` to exist before
`OPERATION_ADMIT`, while `OPERATION_ADMIT` itself carries the bound and its
hash. Determine whether any authorized command can create that file without a
worker/controller writing control state. Reject circular or extra-command
interpretations.

Test whether “each op has a positive bound” actually bounds aggregate resource
use. A controller can declare an arbitrarily large positive integer; require an
outcome-independent admission capacity/reservation predicate if needed. Check
logical/allocated bytes, sparse files, no-content-hash-on-excess, quarantine,
and release exactly once.

### 3. Validity and watchdog semantics

Verify that `overrun_ns > 0` has one existing, closed, deterministic invalidity
route and can never be narrated as a valid close, E1 exhaustion, E3 boundary,
or scientific datum. Examine the unresolved `PROCESS or CLOCK` classification,
lost/re-derived freeze observations, and whether re-derivation can honestly
recover `freeze_ns` rather than merely observe a later stopped group.

Check that platform scheduling variability affects validity transparently and
cannot be selected or repaired post hoc.

### 4. A3 observation scope

Confirm A3 makes no mechanical secrecy claim against a deliberate same-UID
controller, while endpoint roles and output grammar remain mechanical against
contract-following/accidental misuse. Confirm no T artifact, leakage result, or
procedural A3 boundary can be cited as Q/C confidentiality or evidence.

### 5. Scientific/resource non-regression

Audit E1/E2/E3, the nine events, T/Q/C boundaries, capability custody, stream
accounting, full-live batch routing, and terminal meanings. New control-plane
artifacts must not create a hidden outcome, a tunable success-conditioned
budget, counter-only terminal, second settlement authority, or new production
root.

Distinguish contract defects from dirty implementation deviations. Answer all
three Fable Sol questions explicitly.

## Deliverable

Write exactly one new file:

`reviews/sol_officina_supervisor_control_channel_v2_review.md`

Its first verdict line must be exactly one of:

- `OFFICINA_SUPERVISOR_V2_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`
- `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`
- `BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`

Lead with Critical/Major findings and minimal exact repairs. State which prior
findings are genuinely closed. If `REVISE`, say whether the repair is bounded
and whether a new author choice is required. If confirmed, state the exact
token made eligible conditional on the X-line.

Confirm no code or runtime action occurred and that T remains
`NOT_ACTIVATED`.
