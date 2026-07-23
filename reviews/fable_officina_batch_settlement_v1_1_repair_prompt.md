# Fable 5: Officina batch-settlement amendment v1.1 bounded repair

Work in `/home/master/llm_projects/philosophia`.

The bounded v1 reviews both returned `REVISE` while confirming the amendment is
necessary and correctly scoped:

- `reviews/opus_officina_batch_settlement_amendment_v1_review.md` — F1..F4;
- `reviews/sol_officina_batch_settlement_amendment_v1_review.md` — R1..R4.

No scientific or learner cell is reopened. Neither author token is eligible.

## Authorization boundary

Create exactly three files and change nothing else:

1. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md`
3. `reviews/fable_officina_batch_settlement_v1_1_closure.md`

Carry v1 amendment and harness v2/v2.1/v2.2 forward except for an exact
replacement index. Do not edit code, implement the authority, create a runtime
claim/manifest/authorization, activate T, issue capabilities, draw entropy,
spend resources, or create T/Q/C data.

## 1. Closed accounting witness and claim completeness (Sol R1; Opus F1)

Extend the durable claim, or bind one exact immutable pre-charge witness, so an
independent verifier can recompute every claimed process charge from closed
non-outcome meter facts rather than trusting `charge_ns`.

Pin exact schema/key/type/enum/order rules for:

- global integer inputs: `remaining_ns`, `known_total_ns`,
  `unknown_stream_count`, `unknown_pool_ns`, quotient and remainder;
- every stream: globally unique batch `stream_index`, owning process id,
  classification enum `TIMELY_KNOWN|LATE_KNOWN|UNKNOWABLE`, known charge or null,
  unknown share or null, and exact non-outcome meter-evidence hash;
- per-process decomposition and aggregate, exact lease hash, process sequence,
  planned disposition and cause;
- relation of disposition/cause to `batch_reason` and all-valid/invalid routes.

Validator duties before authority exists: recompute U and its integer allocation;
preserve every proved known charge; verify each process aggregate and full sum;
reject missing/extra/duplicate stream/process/evidence; validate enums/nullability.

For `E1_BOUNDARY`, `E3_BOUNDARY`, and `RUNTIME_INVALIDITY`, the claim process set
must equal the **entire durable active-lease set** at the pre-head. For
`RECOVERY_SETTLEMENT`, define the exact admissible subset and prove every omitted
lease is already terminal/removed or belongs to one specifically named unresolved
ancestor claim; no live lease may be silently stranded.

## 2. One canonical order (Sol R2)

Now that the amendment permits every claimed post-cap append, remove all class
ordering. Claim array and execution order are exactly global ascending
`process_sequence` for every batch. Crossing/non-crossing is descriptive only,
never an ordering predicate and never inferred from evolving state. Update all
worked ledgers and replacement text accordingly.

## 3. Unresolved-claim registry and exact core authority (Sol R3; Opus F3)

At every runtime-lock entry, scan retained claims. If a claim's pre-entry is an
ancestor of the current ledger and its terminal/archive predicate is incomplete,
that claim blocks every new claim, admission, renewal and behavior.

Reconstruct progress from the durable suffix after `pre_ledger_entry_sha256` and
accept only a complete prefix of the canonical tuple automaton. Pin how ledger
entries and dependent files prove each prefix.

Define the smallest exact core API, including entry identity and consumption,
substantively equivalent to:

```text
charge_batch_settlement(
  *, process_id, active_lease_sha256, value, envelope, authority
) -> (TState, BatchSettlementAuthority)
```

The authority binds claim hash, next process/index, current ledger head, current
state hash, exact lease/value and validated consumed prefix. It refuses stale
head/state, already-consumed index, reorder, duplicate, omitted process, value
increase/decrease or claim substitution, then returns a successor authority.
The initial pre-state match applies only before tuple 1; restart reconstructs the
next-step authority from the exact durable prefix, never by requiring current
state to equal the old pre-state.

Pin orchestration so `runtime.py` remains unchanged: the new accounting method
produces the post-cap TState; the harness uses existing event/record/lease
constructors directly. Existing `settle_active_lease` and
`settle_monotonic_delta` remain unchanged and are not used for batch charges.
Name every verifier/control pin and future code file honestly.

## 4. Complete prefix automaton and byte-identical recovery (Sol R4; Opus F4)

Enumerate every durable substep for valid and invalid tuples:

- claim installed;
- charge ledger append before head/cache completion;
- completed charge before invalidity detail or valid process record;
- invalidity detail before `T_RUNTIME_INVALID`;
- invalid event before INVALID process record;
- valid process record before `T_PROCESS_STOPPED`;
- final record/event before verified lease removal;
- last valid removal before the single `T_ENVELOPE_EXHAUSTED`;
- final tuple before archive/post-verifier.

For every prefix, specify exactly one next action: finish head/cache, finish the
already-charged tuple without another charge, append next claimed charge, append
the already-authorized global terminal, archive, or remain blocked. Reconcile
each cut with the inherited §3 record-first rules. No crash may re-charge,
abandon, nest, reorder or recompute from outcomes.

All re-derived dependent artifacts must be byte-identical. Pin each timestamp
and otherwise variable field as a deterministic function of durable parent facts
(claim and/or durable charge/event), never a fresh recovery clock. Provide exact
derivation rules for invalidity detail, invalid event and final process records.

## 5. In-flight infrastructure fault override

Resolve the all-valid-claim fault case without mutating the claim or relabelling
already durable history:

- distinguish a recoverable crash (resume canonical prefix) from a verified
  infrastructure invalidity;
- define one closed immutable `t-batch-settlement-invalidity-override.v1` created
  before further tuple work, binding original claim hash, exact validated prefix,
  current head/state, dominant cause, remaining process ids and deterministic
  replacement dispositions;
- already valid-closed processes remain immutable; the incomplete/current and
  remaining live processes follow the invalid route with the one dominant cause;
  no global valid exhaustion event is appended; final global route is G5;
- give exact schema/path/no-replace/order/archive/crash rules and prevent nested
  or competing overrides;
- if an invalidity prevents durable creation/verification of the override, the
  runtime remains blocked; it does not improvise a route.

If this override would require a signed event/schema change, return `BLOCKED`
and say so. It must remain a closed control artifact, not a tenth event.

## 6. Harness v2.3 consistency

Update v2.2 only where required:

- per-stream witness and process aggregation references;
- one global ascending sequence order in the mixed and 60/60/60 examples;
- exact F1 full-live-set rule;
- prefix/override terminal behavior;
- A3 worked ledgers remain fully recomputable;
- generational overdue-resume path remains unchanged and closed.

Include complete integer examples for a low-sequence crossing process beside a
higher-sequence unknown/non-crossing process, the 60/60/60 batch, a mixed process,
and an all-valid E1 batch that crashes after final removal but before exhaustion.

## 7. Governance

Keep the two-token order unchanged and **not yet eligible**:

1. `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`
2. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`

Classify exact amendment surfaces versus harness clarifications. No learner,
candidate, optimizer, device winner, scientific endpoint, Q/C numeric or claim
movement is allowed; T remains `NOT_ACTIVATED`.

## Closure

First line exactly one verdict:

- `READY_FOR_OFFICINA_BATCH_SETTLEMENT_V1_1_FINAL_CONFIRMATION`
- `REVISE_OFFICINA_BATCH_SETTLEMENT_V1_1`
- `BLOCKED_OFFICINA_BATCH_SETTLEMENT_V1_1`

Then include:

1. one-to-one F1..F4 and R1..R4 disposition;
2. exact replacement index;
3. closed witness/claim/override schemas;
4. complete prefix automaton and deterministic timestamp table;
5. core API and restart-authority reconstruction;
6. full-live-set and recovery-subset proofs;
7. worked ledgers and two-implementer determinacy;
8. two bounded final-confirmation questions per reviewer;
9. negative authorization confirmation.

The next step is one literal bounded X/Y confirmation of these repairs, then the
two author signatures in order. No new design round is authorized absent another
concrete output-changing contradiction.
