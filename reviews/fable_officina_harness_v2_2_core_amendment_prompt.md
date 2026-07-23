# Fable 5: Officina harness v2.2 and bounded batch-settlement core amendment

Work in `/home/master/llm_projects/philosophia`.

The conditional author signature did **not** activate because the final reviews
diverged:

- `reviews/opus_officina_generic_harness_v2_1_final_confirmation.md` —
  `OFFICINA_GENERIC_HARNESS_V2_1_XLINE_CONFIRMED`;
- `reviews/sol_officina_generic_harness_v2_1_final_confirmation.md` —
  `REVISE_OFFICINA_GENERIC_HARNESS_V2_1_YLINE`.

Sol provides a concrete admitted counterexample: with global remaining 100 ns
and three pre-existing processes each owing a proved case-(b) 60 ns charge, no
sequential ordering can append all three through the unchanged core, because
ordinary charging refuses once the intermediate state is at/above E1. This
cannot be repaired by harness wording or a positive-reservation invariant.

## Authorization boundary

Create exactly three files and change nothing else:

1. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`
2. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`
3. `reviews/fable_officina_harness_v2_2_core_amendment_closure.md`

Do not implement or edit code, create a manifest/authorization, activate T,
issue a capability, create a process/world/learner, draw entropy, spend E1/E2/E3,
or create T/Q/C/runtime data. Preserve v2 and v2.1 unchanged. This is a bounded
engineering/control amendment, not a scientific redesign.

## 1. Independent verification and route

First independently verify Sol's multi-cross counterexample against the current
`accounting.py`, `runtime.py`, event schemas and signed case-(b) semantics. If it
is wrong, return `BLOCKED` with a concrete proof. If correct, adopt the explicit
bounded core-amendment route below; do not invent an impossible pre-batch
invariant and do not clip any proved known-late charge.

The amendment must state loudly that v2.1's unconditional `no-core-amendment`
classification is superseded. It requires a distinct author token:

`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`

The harness contract token remains separate and is not yet eligible:

`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`

## 2. Minimal frozen-batch settlement authority

Specify a new explicit accounting-core operation, separate from ordinary
`charge_device_nanoseconds`, that permits all full positive process-scoped
charges for **one frozen set of pre-existing active leases** to append even when
an earlier charge from that same batch has crossed E1.

Pin, bit-exactly:

- precondition: one held runtime-lock epoch; pre-batch durable state is below E1;
  no admission/resource issue is pending; all affected capabilities are revoked;
  workers/backends are quiesced/synchronized or classified unknowable;
- a durable closed `t-batch-settlement-claim.v1` created before the first charge,
  with exact schema/key set/path, pre-ledger/head/state hashes, sorted exact
  process ids, process sequences, active-lease hashes, per-process full charge
  values, dispositions, dominant cause if invalid, and fixed batch reason;
- charges are positive, finite integer nanoseconds, computed from the already
  signed timely/known-late/unknowable rules; known charges are never clipped;
- authorization is non-reusable and restricted to exactly the claim-enumerated
  pre-existing leases and values. It cannot admit a process, renew a lease,
  authorize behavior, increase a computed value, add an omitted process, or
  charge ordinary work after exhaustion;
- the first charge may cross E1 and later claimed charges may still append, but
  only within this same frozen batch. Outside it, the old refusal at/above E1 is
  unchanged;
- each event remains the existing `T_DEVICE_TIME_CHARGED` with the exact
  process/pre-lease binding; no `stream_index`, batch id or new field enters a
  signed event/runtime schema;
- deterministic ordering and a post-verifier prove each exact claim entry was
  consumed once, no extra/missing/reordered value exists, aggregate E1 equals
  pre-state plus the full claimed sum, and all leases reach their mandated
  terminal/removal route;
- exact crash cuts before claim, after claim, between every tuple, and after the
  last tuple. No crash permits resumption of behavior or silent replay; recovery
  completes only missing claim-enumerated settlement work under the same bounded
  authority or remains invalid/blocked, never recomputes charges from outcomes;
- exact archival set and how the batch claim is auditable despite unchanged
  ledger-event schemas (bind pre-head and final head/process records in the
  closed artifact family without adding a tenth event).

Name the smallest future code/control surface this amendment would authorize
after signature and review. Prefer a new narrow pure constructor/capability over
weakening the ordinary method. State every invariant that the implementation and
verifier must enforce. Do not write that code now.

## 3. Harness v2.2 corrections A1/A3/B

Supersede only the necessary v2.1 clauses:

### A1 mixed streams

- Classification remains per stream. Every proved interval remains in `K`.
  Only genuinely unknowable streams enter `m` and receive unknown-pool shares.
- If any stream is unknowable the **process** takes the invalid route, but its
  known sibling charges are preserved. Its one process event aggregates all
  known charges plus all unknown shares for that process.
- Non-coextensive proved streams use adapter-proved intervals; ambiguity affects
  only the ambiguous streams, not proved siblings.
- Add a complete integer mixed example matching Sol's 50/100 ns counterexample,
  exact charge, post-state, terminal and event tuple.

### A2/B multiple crossings

- Replace the single-crossing-last assumption with the frozen-batch authority.
  Give one deterministic per-process tuple order for zero, one and multiple
  known-late crossings, with unknown/non-crossing work first and multiple
  crossing processes sorted by the existing stable order.
- Preserve immediate charge→invalid adjacency, full known charges, one positive
  event per process, invalidity dominance and no valid exhaustion event in an
  invalid batch. A fault-free all-valid E1 batch still emits exactly one final
  `T_ENVELOPE_EXHAUSTED` after every valid process closes.
- Work the exact three-process 60/60/60 ns with 100 ns remaining example and a
  mixed-known/unknown multi-process example. Show event order, intermediate
  above-cap states, final aggregate and terminal route.

### A3 examples

Make all five inherited worked batches independently recomputable. For former
batches 3 and 4 provide `D0`, `remaining`, `K`, `m`, `U`, every share/process
aggregate, exact post-state and terminal. Correct "no crossing" to distinguish
no known crossing from reaching the cap through the unknown pool.

## 4. Repeatable overdue resume path (Sol C)

Replace the singleton pending-checkpoint path with an immutable generation keyed
by the immediately preceding ordinary-pause event hash, for example:

`runtime/T_PENDING_RESUME_CHECKPOINTS/<pause_event_sha256>.json`

Pin exact schema binding, no-replace behavior, archive retention and lookup.
Prior generations are never deleted or replaced. Add a complete two-pause/
two-overdue-resume acceptance route with distinct hashes and all crash cuts.
Preserve the original checkpoint/payload/head relation and no-tenth-event rule.

## 5. Compatibility and authorization

Produce separate compatibility tables:

- what remains unchanged in signed events/runtime schemas/scientific contracts;
- the exact bounded accounting/control amendment;
- harness-only deterministic corrections;
- future implementation files/tests/verifier pins that become eligible only
  after both X/Y approval and Kirill's explicit amendment token.

No learner, candidate, architecture, optimizer, device winner, Q predicate,
alpha, endpoint, margin or scientific result may be selected. WP-6/WP-9 and all
negative destinations remain unchanged; T stays `NOT_ACTIVATED`.

## Closure deliverable

First line exactly one verdict:

- `READY_FOR_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_XY_REVIEW`
- `REVISE_OFFICINA_BATCH_SETTLEMENT_AMENDMENT`
- `BLOCKED_OFFICINA_BATCH_SETTLEMENT_AMENDMENT`

Then include:

1. independent counterexample verification;
2. one-to-one disposition of Sol A1/A2/A3/C and interaction with Opus M-1..M-6;
3. exact amendment invariants/schema/path/crash/archival table;
4. complete multi-cross and mixed-stream worked ledgers;
5. exact v2.1→v2.2 replacement index;
6. two-implementer determinacy proof;
7. the two-token signature order and what each token authorizes;
8. three bounded questions for Opus and three for Sol;
9. negative authorization confirmation that nothing executed or activated.

The next step is one bounded X/Y review of the explicit amendment and correction,
then any required literal confirmation, then Kirill's two informed signatures.
Do not claim the prior conditional harness signature was accepted.
