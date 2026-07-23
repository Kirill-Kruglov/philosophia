# Fable 5: bounded Officina generic harness contract v2.1 repair

Work in `/home/master/llm_projects/philosophia`.

The complete v2 contract received two bounded confirmation verdicts:

- `reviews/opus_officina_generic_harness_contract_v2_confirmation.md`
  (`REVISE_OFFICINA_GENERIC_HARNESS_V2_XLINE`, M-1..M-6);
- `reviews/sol_officina_generic_harness_contract_v2_confirmation.md`
  (`REVISE_OFFICINA_GENERIC_HARNESS_V2_YLINE`, corrections A..E).

Both reviewers confirm that all original v1 findings C-1..C-4/R5..R12 and the
majority of Sol repairs 1..14 are closed. Do not reopen them. The inactive C4
verifier gate is independently closed by both final confirmations at `fbac493`.

## Authorization boundary

Create exactly two new files and change nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md`
2. `reviews/fable_officina_generic_harness_contract_v2_1_closure.md`

The correction must state exactly which v2 clauses/examples it replaces and
that all other v2 text carries forward. Do not implement code, amend
`runtime.py`, create `generic_harness.py`, create a production manifest or
authorization, activate T, issue a capability, create a process/world/learner,
draw entropy, spend E1/E2/E3, or create T/Q/C data.

## Governing resolution

Adopt the code-compatible no-core-amendment route. Do **not** add a zero-charge
invalid-close constructor. Apply every Opus M-1..M-6 and every Sol correction
A..E one-to-one, using the following strict reconciliation.

### 1. Representable per-process settlement (Opus M-1/M-3; Sol A)

- Compute per-stream known charges and unknown shares inside one frozen batch,
  then aggregate by process id. Append at most one positive
  `T_DEVICE_TIME_CHARGED` per affected process, bound to that process's exact
  pre-settlement lease. Add no `stream_index` or other field to signed schemas.
- State whether a lease's streams share a cursor interval. For non-coextensive
  streams, the adapter proves and the harness sums individual intervals before
  the one event; ambiguity selects the unknowable case.
- Remove v2's zero-share branch and Example C. Every unknowable live stream
  receives at least 1 ns. Use Sol correction A's one-pool construction and prove
  exact allocation/conservation in integer nanoseconds. Order all unknown and
  non-crossing tuples before the final known case-(b) charge that crosses E1.
  Admission's positive reserved liabilities are the precondition; if the
  required floor cannot be represented, fail closed before charging rather than
  hand-building a record.
- For every invalid process, append the indivisible tuple:
  positive final charge -> invalidity detail -> `T_RUNTIME_INVALID` -> INVALID
  process record -> verified lease removal. Tuples are deterministically ordered
  by process sequence; the invalid event must be the immediate successor of its
  own charge. No "all charges first" wording may survive.

Include worked batches for: all-known; known-late overrun with unknowable
siblings; multiple unknowables belonging to one process; multiple processes;
and an invalid batch whose final known charge crosses E1.

### 2. Total compound terminal routes (Opus M-2/M-4/M-5; Sol B/D)

Pin the exact artifact routes from Sol correction B:

- fault-free E1: settle all, valid `T_PROCESS_E1_EXHAUSTED` record then
  `T_PROCESS_STOPPED` for each process in ascending sequence, verified lease
  removal, then exactly one `T_ENVELOPE_EXHAUSTED`, G7;
- fault-free E3: settle all, valid `T_PROCESS_E3_DUE` record then stopped event
  per process, remove all leases, G2, then only the durable review transaction;
- concurrent invalidity: freeze the whole batch, then deterministic per-process
  invalid tuples; later invalid events are explicitly legal G5->G5; no
  `T_PROCESS_STOPPED`;
- invalidity plus exhausted/due counters: retain numeric facts in every invalid
  post-state but append no valid exhaustion/stop/pause event while invalidity is
  unresolved; G5 remains the sole terminal route.

Every collaterally invalid-closed sibling inherits the one dominant triggering
cause selected by the existing precedence. The exact signed invalidity record
contains only that single `invalid_cause`; delete the unrepresentable statement
that it lists all observed causes. Co-observed causes create no public/runtime
field and cannot enter recovery.

Give an exhaustive compound-boundary table and one fixed route for every pair.

### 3. Durable clean/overdue resume and recovery (Opus M-6; Sol C)

- Clean resume verification and the first new claim occur under one lock epoch.
  G3->G1 becomes durable only through the existing `T_PROCESS_STARTED` appended
  directly on the verified pause/review head; no capability or behavior exists
  before it. Pin crash behavior before/after claim and event.
- Reconcile the checkpoint requirements strictly: the original pause checkpoint
  remains immutable. For an overdue resume, the harness writes a **new** pending
  checkpoint artifact referencing byte-identical model/optimizer/config/stack
  payload hashes and binding `ledger_head_before` to the first pause entry. It
  then appends the second `T_OPERATIONAL_PAUSE` through the generic §3
  transaction, not the old helper, with `RESUME_E3_REVIEW_PENDING` and
  `resets_e3:false`. Pin the old/new relation, schema keys, canonical path,
  archive set, verifier rule and every crash cut. Only the new event/cache carries
  the pending post-state; the original checkpoint is never mutated.
- Define the recovery-disposition schema id, exact key set/types/enums, canonical
  path, signature and invalidity/head bindings, finite action tokens, atomic
  no-replace/fsync/verification ordering, exact archive set, resolution
  predicate and every crash cut. It must use only signed v2 §F fact classes,
  leave events/charges immutable, add no tenth event, complete no failed
  operation, and require a fresh process id.
- Clarify the ledger-ahead-of-head cut: the detail record may be written, but the
  invalidity event is deferred until the signed recovery route can reconcile the
  head. No silent repair is permitted outside the already signed sole cache/
  lease-successor case.

### 4. Closed decision inputs (Sol E)

Enumerate closed schema ids and exact canonical key sets, types and fixed enums
for:

- E3 decision;
- resource-stop decision;
- pause decision;
- recovery disposition;
- author-stop decision.

Permit only the clock, charge, identity, integrity and authorization facts
allowed by signed v2 §F. Forbid free text and hashes selected from learner/output
bytes as decision values. Existing signed runtime schemas/events remain
unchanged and may reference these objects only through already permitted hashes.
Human author stop may remain T-informed and permanently non-citable; close the
machine input, not the author's cognition.

### 5. Compatibility and determinacy

Provide a literal compatibility table showing that no signed event, runtime
schema, constant, root, phase rule or metering-core constructor changes. The new
checkpoint/decision/recovery objects are closed generic-harness artifacts, not
new runtime events. If any required clause cannot be expressed without a signed
schema/core change, return `BLOCKED` and name it; do not silently amend.

Prove that two independent implementers now derive identical:

- per-process charge-event counts and values;
- tuple/event ordering and hashes;
- terminal state for every compound boundary;
- invalid cause and artifact key sets;
- pause/resume/recovery admission decision.

Do not choose a learner, candidate, architecture, optimizer, device winner,
breathing threshold, Q predicate, alpha, endpoint, margin, or scientific result.
WP-6/WP-9 ownership and all negative destinations remain unchanged.

## Closure deliverable

The closure's first line must be exactly one token:

- `READY_FOR_OFFICINA_GENERIC_HARNESS_V2_1_FINAL_CONFIRMATION`
- `REVISE_OFFICINA_GENERIC_HARNESS_V2_1`
- `BLOCKED_OFFICINA_GENERIC_HARNESS_V2_1`

Then include:

1. a one-to-one disposition table for Opus M-1..M-6 and Sol A..E;
2. the exact replacement index into v2;
3. accounting proofs and worked batches;
4. the complete boundary/event-order table;
5. all new closed artifact schemas/paths and compatibility classification;
6. a two-implementer determinacy checklist;
7. two bounded yes/no questions for Opus and two for Sol, restricted to these
   repairs;
8. the exact negative authorization surface and confirmation that nothing ran.

The intended next step is one literal bounded final confirmation by each line,
then Kirill's contract signature. No new design round is authorized.
