REVISE_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_YLINE

# Sol Y-line — Officina batch-settlement amendment v1 review

The packet chooses the honest amendment route and fixes the v2.1 mathematical examples, mixed-stream rule, and repeat-resume path. Its claimed frozen-batch authority is appropriately narrow in intent. It is not yet a closed durable authority: claim order conflicts with execution order, the claim cannot re-derive its own per-stream accounting, unresolved claims can be shadowed at a later prefix head, and the crash table omits intra-tuple and pre-terminal prefixes. Those defects change ordering, admissibility, and whether a charge can be repeated or abandoned.

## Critical findings

### 1. The closed claim does not contain enough information to verify its claimed charges

The claim's process entries contain only `{process_id, process_sequence, active_lease_sha256, charge_ns, disposition, invalid_cause}` (`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md:69-83`). They do not retain:

- each claim-enumerated stream and its case-(a), case-(b), or case-(c) classification;
- each proved known interval/charge and its meter-evidence binding;
- the global `remaining`, `K`, `m`, and `U` values;
- each unknown share and its deterministic remainder position; or
- the per-process decomposition whose sum must equal `charge_ns`.

Consequently a syntactically valid claim containing 50 ns for the mixed 50/100 case and the correct 101 ns claim are indistinguishable to the post-verifier. The pre-state and lease hashes do not name the captured per-stream quiescence readings or unknown classifications. After a crash, recovery can enforce only “charge exactly what the claim says,” not that proved charges remained in `K`, the pool was allocated once, or the aggregate was not clipped, multiplied, or erased.

**Mandatory R1:** extend the closed claim, or bind one equally closed pre-charge accounting artifact, with exact global integer inputs (`remaining_ns`, `known_total_ns`, `unknown_stream_count`, `unknown_pool_ns`) and exact per-stream entries (`stream_index`, closed case enum, known charge or null, unknown share or null, and the relevant non-outcome meter-evidence hash). Require the validator to recompute `U`, quotient/remainder allocation, every process aggregate, and the full claimed sum before authority exists. Pin the exact disposition enum and its relation to `batch_reason`; a positive integer plus prose saying “computed from the signed rules” is insufficient durable authority.

### 2. The claim order and the execution order contradict each other

Amendment §2b requires `processes` to be globally sorted by `process_sequence`. Section 2d and v2.2 A2 instead require class order—unknown/non-crossing processes first, crossing processes second—with sequence order only within a class. These orders differ whenever a low-sequence crossing process coexists with a higher-sequence non-crossing or unknown process; v2.1 batch 5 is the immediate form of that case. The 60/60/60 ledger further calls all three entries “crossing-class” even though, from the frozen pre-state, the first 60 ns charge leaves the state 40 ns below cap. “Crossing process” therefore has no non-circular closed predicate.

**Mandatory R2:** now that the amendment permits every claimed post-cap append, use one global ascending-`process_sequence` order for all process tuples. Make the claim array order and execution order identical and update affected ledgers. If class ordering is retained instead, define the class predicate from frozen values, add an exact execution index to the claim schema, and remove the global-sort requirement. No implementation may infer a class from the evolving state.

### 3. Prefix recovery does not prevent re-charge, abandonment, or nested authority

The immutable path prevents two claims at the **same** external-head hash, but a partial tuple advances the ledger/head. Section 2c then says a second batch needs a new claim at the new head. Without a global unresolved-claim invariant, a caller can create a new claim at that advanced prefix head, omit or recompute remaining entries, and leave the earlier retained claim unfinished. This defeats the stated no-abandonment/no-recomputation rule.

The proposed future `BatchSettlementAuthority` is described as constructed from a claim plus a **pre-state match**. After the first charge, neither current state nor current head equals the pre-state/pre-head, so that construction cannot safely resume. The amendment does not define reconstruction of the exact consumed prefix or a single-use authority for the next entry.

**Mandatory R3:** require a scan of the retained claim registry at every lock entry. Any claim whose pre-entry is an ancestor of the current ledger and whose terminal/archival predicate is incomplete blocks every new batch claim, admission, renewal, and behavior. Reconstruct its progress by validating the exact ledger/artifact suffix from `pre_ledger_entry_sha256`; accept only a complete prefix of the one canonical tuple order. Derive a single-use next-step authority bound to claim hash, next process/index, current ledger head, current state hash, exact lease, and exact value. A stale authority, different head, already-consumed index, reordered process, omitted process, or increased/decreased value must refuse. The initial pre-state match applies only before tuple 1; resumed authority requires the exact validated prefix, not the current state to equal the old pre-state.

### 4. “Indivisible tuple” does not close durable crash cuts

The §2e table covers only between-tuples cuts. Each tuple contains multiple separately durable operations. It does not state the next action after:

- charge ledger append before head/cache settlement;
- completed charge before invalidity detail or valid process record;
- invalidity detail before `T_RUNTIME_INVALID`;
- `T_RUNTIME_INVALID` before INVALID process record;
- a valid process record before `T_PROCESS_STOPPED`;
- either final record/event before verified lease removal; or
- the last process tuple before the required all-valid `T_ENVELOPE_EXHAUSTED` event.

The carried §3 rules normally treat an orphan dependent artifact as record-first invalidity, while this amendment appears to expect completion of the claimed tuple. Those are different routes. A fault arising during an originally all-valid batch also makes invalidity dominant, but the immutable claim has valid dispositions and null cause; the packet does not say whether exact continuation, deterministic invalid override, or permanent blocking applies. “Routes to recovery” does not choose one artifact sequence.

**Mandatory R4:** add a complete prefix automaton. For every durable substep, state whether the sole next action is: finish the already-charged tuple without another charge; perform the §3 head/cache completion; append the next claimed charge; append the one global terminal event; archive; or remain blocked. Reconcile each dependent-artifact cut explicitly with §3. Define the exact in-flight-fault rule, including whether and how an all-valid claim becomes an invalid batch without mutating or contradicting its claim. Add an explicit cut after the final valid process removal and before the single `T_ENVELOPE_EXHAUSTED`; its sole next operation must be that already-authorized terminal event, never archival or a new claim.

## Accounting recomputation

All v2.2 arithmetic is correct in integer nanoseconds:

| Ledger | Claimed charges | Durable states relative to cap | Check |
|---|---:|---:|---|
| Original counterexample, pre = cap − 100 ns | 60, 60, 60 ns | −40, +20, +80 ns | Sum 180 ns; final = pre + 180 = cap + 80. The ordinary constructor has zero valid permutations; the amendment is genuinely needed. |
| A1 mixed 50/100 | 101 ns | +51 ns | `K=100`, `m=1`, `U=1`; known 100 is preserved and the pool is debited once. |
| Mixed multi-process, pre = cap − 200 ns | 50, 135, 15 ns | −150, −15, 0 ns | `K=170`, `m=2`, `U=30`, shares 15/15; P2 aggregate 120+15=135; total 200. |
| Batch 3, pre = cap − 4 ns | 4 ns | 0 ns | `K=0`, `m=2`, `U=4`, shares 2/2; one process event. |
| Batch 4, pre = cap − 30 s − 3 ns | 30 s, 2 ns, 1 ns | −3, −1, 0 ns | `K=30 s`, `m=3`, `U=3`, shares 1/1/1; exact cap through the pool. |

Thus A1 and A3 are mathematically closed, and the generational C path is closed: `T_PENDING_RESUME_CHECKPOINTS/<pause_event_sha256>.json` gives two complete overdue-resume cycles distinct immutable artifacts, preserves the original checkpoint/head relation, and needs no deletion or policy fork.

## Conditional terminal and conservation audit

- The intended batch exception is the narrowest honest authority class: one below-cap frozen pre-state, one held lock, only pre-existing claim-enumerated leases and frozen positive values. Ordinary post-cap charge, admission, renewal, omitted processes, value changes, and behavior remain forbidden. That scope is acceptable once R1-R4 make it enforceable.
- Arithmetic conservation is exact: post E1 equals pre E1 plus the full claimed sum, with one positive process event and no cross-process aggregation.
- Invalid batches correctly remain G5, retain numeric E1/E3 facts, and append no valid exhaustion/stop/pause terminal.
- An all-valid E1 batch correctly requires every valid record → `T_PROCESS_STOPPED` → removal, followed by exactly one `T_ENVELOPE_EXHAUSTED` and G7. R4 is required to make the final-event crash prefix representable.
- The claim path is collision-resistant and no-replace at one pre-head, but R3 is required to prevent reuse/nesting at a different partial head and to reject stale authority after restart.

## Governance and scientific boundary

The ordered-token model is correct in principle:

1. `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` must come only after final X/Y approval of the repaired amendment.
2. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT` may come only after token 1 and final confirmation of the complete v2/v2.1/v2.2 harness contract.

Neither token is eligible under this verdict. The amendment changes only engineering accounting/control semantics. It does not change E1/E2/E3 constants, the scientific estimand, T/Q non-citability, WP-3/WP-4 boundaries, WP-6/WP-9 ownership, or any negative destination.

This verdict authorizes only bounded repairs R1-R4 and another bounded Y-line confirmation. It authorizes no code, accounting implementation, harness, manifest, activation authorization, activation, capability, process, learner, entropy, E1/E2/E3 spend, T/Q/C datum, outcome, or scientific interpretation. The real tree remains `NOT_ACTIVATED`; `successor/officina/runtime/` contains only `T_RUNTIME.lock`.
