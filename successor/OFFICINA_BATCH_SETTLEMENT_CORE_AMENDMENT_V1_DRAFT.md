# Officina batch-settlement core amendment — v1 draft

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`. This is an explicit,
bounded **metering-core amendment** to the accounting surface of the
signed activation protocol's implementation. **It loudly supersedes
v2.1's unconditional no-core-amendment classification**: the Y-line
final confirmation exhibited an admitted settlement batch that the
unchanged core cannot represent, and this draft's author independently
verified it (§1). The amendment requires its own distinct author token:

```text
I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT
```

The harness contract token
(`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`) remains separate and is
**not yet eligible**; the prior conditional signature was not accepted
and is not claimed. This draft implements nothing, edits no code,
creates no manifest/authorization/capability/process/world/learner/
entropy/spend/datum, and leaves T `NOT_ACTIVATED`. It selects no
learner, candidate, architecture, optimizer, device winner, Q
predicate, alpha, endpoint, margin, or scientific result.

## 1. Independent verification of the counterexample

Reproduced read-only against the current
`accounting.py:TState.charge_device_nanoseconds` (refuses when
`exhausted()` — i.e. `device_nanoseconds ≥ cap` — before any charge):
with `D0 = E1_cap − 100 ns` and three pre-existing processes each
owing a proved case-(b) charge of 60 ns, **all six permutations fail**:
the first charge reaches `cap − 40`, the second reaches `cap + 20`
(exhausted), and the third is refused
(`ValueError: T envelope is already exhausted`). The signed case-(b)
rule ("the full actual interval … recorded in full even where it
exceeds the reservation and crosses E1") plus the process-scoped
event/lease binding (one positive event per process; no cross-process
aggregation) therefore **cannot be honored by any sequential order
through the unchanged core** when more than one known-late process
must charge past the cap. No pre-batch invariant can exclude the case:
each 60 ns *reservation* fit the 100 ns remainder at admission; the
*actual* intervals legally exceeded it. v2.1's "single crossing last"
was necessary but not sufficient. The counterexample is correct; the
route below follows.

## 2. Frozen-batch settlement authority (the amendment)

A new, explicit accounting-core operation — separate from ordinary
`charge_device_nanoseconds`, which is **unchanged for all ordinary
work** — permits all full positive process-scoped charges for **one
frozen set of pre-existing active leases** to append even after an
earlier charge of the same batch has crossed E1.

### 2a. Preconditions (all mandatory)

One held runtime-lock epoch; the pre-batch durable state is **below**
E1; no admission or reservation is pending; every affected capability
is revoked; every affected worker/backend is quiesced and synchronized
or classified unknowable per the signed rules; the batch's per-process
charges, dispositions, and (if invalid) the dominant cause are already
computed from the signed timely/known-late/unknowable rules and frozen.

### 2b. Durable batch claim (before the first charge)

Schema `philosophia.officina.t-batch-settlement-claim.v1`, canonical
path
`successor/officina/runtime/T_BATCH_SETTLEMENT_CLAIMS/<pre_ledger_head_sha256>.json`
(atomic no-replace — at most one batch per ledger position; prior
claims retained forever), canonical ASCII JSON, keys exactly:

```text
schema, scientific_outcome (false), batch_reason,
pre_ledger_entry_sha256, pre_ledger_head_sha256, pre_state_sha256,
processes, dominant_cause, created_utc
```

`batch_reason` ∈ {`E1_BOUNDARY`, `E3_BOUNDARY`, `RUNTIME_INVALIDITY`,
`RECOVERY_SETTLEMENT`} (fixed enum). `processes` is a
sorted-by-`process_sequence` array of objects with keys exactly
`{process_id, process_sequence, active_lease_sha256, charge_ns,
disposition, invalid_cause}` — `charge_ns` a positive finite integer
computed from the signed rules and **never clipped**;
`invalid_cause` null for valid dispositions, else the one
precedence-selected cause; `dominant_cause` null for fault-free
batches. File `fsync` + directory `fsync` + post-verify before any
charge.

### 2c. Authority semantics

- Non-reusable: the authority exists only for the claim at the current
  pre-head and is consumed by the batch; a second batch needs a new
  claim at the new head.
- Restricted exactly to the claim-enumerated **pre-existing** leases
  and values: it cannot admit a process, renew a lease, authorize any
  behavior-capable work, increase a computed value, add an omitted
  process, or charge ordinary work after exhaustion.
- The first claimed charge may cross E1; **later claimed charges may
  still append — only within this same frozen batch**. Outside it, the
  ordinary refusal at/above E1 is byte-for-byte unchanged.
- Each appended event remains the existing `T_DEVICE_TIME_CHARGED`
  with the exact process/pre-settlement-lease binding; **no
  `stream_index`, batch id, or any new field enters a signed
  event/runtime schema**. Auditability comes from the closed claim
  artifact (which binds the pre-head) plus the final process records
  and post-head — the closed artifact family, no tenth event.

### 2d. Ordering and post-verifier

Deterministic order: the claim's `processes` array order (ascending
`process_sequence`, with unknown/non-crossing processes enumerated
before crossing processes at claim construction per the harness
contract). Each process's tuple is emitted indivisibly (charge →
[detail record → `T_RUNTIME_INVALID` → INVALID record] for invalid
dispositions, or [valid record → `T_PROCESS_STOPPED`] for valid ones)
→ verified lease removal. The post-verifier must prove: every claim
entry consumed exactly once; no extra, missing, or reordered value;
aggregate E1 equals the pre-state plus the full claimed sum; every
enumerated lease reached its mandated terminal and removal; the
terminal global state matches the batch reason (G7 only for an
all-valid `E1_BOUNDARY` batch, after its single final
`T_ENVELOPE_EXHAUSTED`; G2 for `E3_BOUNDARY`; G5 otherwise, with no
valid exhaustion/stop/pause event).

### 2e. Crash cuts

| Cut | Durable | Legal action |
|---|---|---|
| before claim | nothing | batch not started; state below cap; ordinary rules govern |
| after claim, before first tuple | claim | at next lock entry the batch **must** be completed under the same authority (claim-enumerated work only) or the runtime remains blocked; never abandoned silently |
| between tuples | claim + prefix of tuples | complete only the missing claim-enumerated tuples, in order, under the same authority; already-appended charges are immutable; no recomputation from outcomes; no behavior resumes |
| after last tuple, before archival | all runtime facts | capability blocked; archival completed only under the signed process disposition; nothing recharged |

No crash permits resumption of behavior-capable work or a silent
replay; a batch that cannot be completed routes to record-first
invalidity and the signed recovery disposition, never to recomputed
charges.

### 2f. Archival set

The batch claim, every tuple artifact (charges are ledger entries;
detail/process records are files), state, ledger, head — staged
exactly, committed with the fixed trailers at the existing v2 §B
boundaries.

## 3. Smallest future code/control surface (authorized only after X/Y review AND the amendment token; not written now)

- `src/philosophia/officina/accounting.py`: one new frozen dataclass
  `BatchSettlementAuthority` (constructed only from a validated batch
  claim + pre-state match) and one new pure method
  `TState.charge_batch_settlement(value, envelope, authority)` that
  permits the post-cap append **iff** the authority enumerates the
  exact process/value; `charge_device_nanoseconds` is not weakened —
  the new narrow constructor is preferred over relaxing the ordinary
  method. No other core file changes; `runtime.py`, `checkpoint.py`,
  `ledger.py`, schemas, events, and constants are untouched.
- Tests for: the verified counterexample now representable; ordinary
  post-exhaustion charging still refused; authority
  non-reusability/mismatch/extra-process/value-increase refusals; every
  §2e cut.
- Because `accounting.py` is on the immutable-control allowlist, this
  is a **reviewed control change**: implementation is eligible only
  after both X/Y approvals of this amendment and Kirill's explicit
  `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`.

**Invariants the implementation and verifier must enforce:** ordinary
charging unchanged below cap and refused at/above cap; batch charges
only under a validated, non-reused authority at the claimed pre-head;
claimed values immutable and never clipped or increased; one positive
event per claimed process; conservation (post E1 = pre + Σ claimed);
tuple order and adjacency preserved; terminal routes per §2d; no
admission during a batch; no new field in any signed schema.

---

This amendment moves no scientific claim, spends nothing, and
activates nothing. WP-6/WP-9 ownership and every negative destination
are unchanged; T and Q remain permanently non-citable for C1–C6; the
programme claim remains `OPEN`.
