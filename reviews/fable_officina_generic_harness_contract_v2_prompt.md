# Fable 5: close the Officina generic metered harness contract v2

Work in `/home/master/llm_projects/philosophia`.

The v1 contract received two independent `REVISE` verdicts:

- `reviews/opus_officina_generic_harness_contract_v1_review.md`
- `reviews/sol_officina_generic_harness_contract_v1_review.md`

The reviewed inputs are immutable. Preserve:

- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`
- `reviews/fable_officina_generic_harness_contract_v1_closure.md`
- both formal reviews and chat captures;
- the signed activation protocol v1 as corrected by v2 and v2.1;
- the signed WP-3 contract and WP-4 inactive boundary.

The current C4 namespace repair at `38ea2f3` is undergoing its own bounded
confirmation in parallel. Treat it as engineering context only; do not pin a
production manifest or activate T.

## Authorization boundary

Create exactly two new files and change nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`
2. `reviews/fable_officina_generic_harness_contract_v2_closure.md`

The v2 contract must be a complete self-contained replacement, not an addendum.
Do not implement code, create `generic_harness.py`, create a production graph or
authorization, activate T, issue a capability, create a world/learner/process,
draw entropy, spend E1/E2/E3, or create any T/Q/C datum.

## Finite mandatory repair set

Adopt and disposition every Opus finding `C-1..C-4` and `R5..R12`, including
the exact replacement text in its section D. Adopt and disposition every Sol
mandatory repair 1..14. Nothing may be silently dropped. Where the reviews
overlap, use the stricter rule that preserves signed semantics and resource
conservation. If two literal requirements conflict, name the conflict and give
one deterministic resolution justified against the signed protocol; do not
invent an author choice merely to avoid reconciliation.

The resulting contract must close at least these load-bearing surfaces:

1. **Total lifecycle and durable ordering.** Valid close is charge -> durable
   final record -> `T_PROCESS_STOPPED`; live-process invalidity and global
   no-process invalidity are distinct; entering global invalidity settles and
   invalid-closes every live sibling. Give exact artifact/event/head/cache/
   archival order and every crash cut.
2. **Conserving concurrent settlement.** Preserve the signed three-case
   recovery charge. Add the single global unknown-pool allocation, exact
   multi-stream reservation arithmetic, batch settlement, conservation
   equations, pre-lease/event hash relation, and total terminal/invalid-cause
   precedence. Known overruns remain fully charged; unknown work cannot multiply
   or erase the remaining E1 pool.
3. **No silent recovery.** Pin the one permitted idempotent completion of a
   fully derivable interrupted successor. Every other ledger/head/cache mismatch
   is record-first invalidity. Define the closed signed recovery-disposition and
   durable overdue-resume protocol without adding a tenth event or authorizing
   automatic retry.
4. **Physical pause.** Specify the exact zero-live-lease, quiesced, charged,
   immutable-checkpoint, event/head/cache/fsync/archive conditions. Every power
   cut before completion routes fail-closed; boot/clock ambiguity cannot be
   converted into an ordinary pause.
5. **Isolation before promotion.** A response wrapper is insufficient. Specify
   supervised worker/backend isolation of mutable memory, IPC, file descriptors,
   temporary files and output buffers; revoke, quiesce, synchronize, hash,
   durably charge, then atomically promote through a one-use release token.
   Invalid or escaped work exposes no result.
6. **Meter contracts.** Separate CPU elapsed-time and off-CPU submitted-command
   semantics. Static reviewed adapters only; unmeasurable cessation/concurrency
   routes to the unknown case. State the exact supervisor ownership, process-
   group containment, durable paths, sole writer/issuer, private production
   capability, and exclusion of fake/test types.
7. **Closed non-outcome inputs.** Resource, E3, recovery and validity decisions
   reject learner behavior and scientific fields recursively. State honestly
   that an author stop in open adaptive T may be T-informed and is quarantined,
   never Q/C evidence or a scientific destination.
8. **No pre-WP-6 information channel.** Remove or neutralize timestamps and
   ordered lineage from the unregistered draft surface. Q/C rejects the entire
   T artifact. A future WP-6 may recompute only a narrowly defined opaque
   identity digest and remains free to replace the draft-adjacent surface.
   Release tokens never enter candidate/Q/H_preC/C schemas.
9. **Immutable implementation boundary.** Use exactly the pinned roots:
   `scripts/officina_activate_t.py`, `scripts/verify_officina_active.py`, and
   `src/philosophia/officina/generic_harness.py`, with the latter invoked via
   `python -m philosophia.officina.generic_harness`. Do not add
   `scripts/officina_t_process.py`. Respect current import allowlists; any future
   backend adapter/control expansion requires its own reviewed amendment.
10. **Executable acceptance matrix.** Enumerate deterministic tests for all
    single and compound boundaries, every durable cut, concurrency/unknown-pool
    conservation, isolation escapes, CPU/off-CPU ambiguity, pause/resume,
    recovery, exact archive sets, and proof that invalidity can never be
    relabelled as a valid terminal.

## Compatibility and authority

Classify each v2 clause as one of: inherited signed rule, deterministic
clarification necessary to implement it, or proposed protocol amendment. A
contradiction in v1 that is repaired back to signed v2.1 is not an amendment.
Do not claim `no amendment` unless the completed table supports it. If a real
protocol amendment remains unavoidable, stop before implementation and provide
its exact minimal author token and reason; do not hide it inside the contract.

The contract must choose no learner, architecture, optimizer, candidate,
device winner, breathing threshold, Q predicate, alpha, margin, endpoint, or
scientific result. It must leave T `NOT_ACTIVATED` and preserve E2/WP-6 and all
Q/C gates.

## Closure deliverable

The closure must contain:

1. first-line verdict exactly one of:
   - `READY_FOR_OFFICINA_GENERIC_HARNESS_V2_CONFIRMATION`
   - `REVISE_OFFICINA_GENERIC_HARNESS_V2`
   - `BLOCKED_OFFICINA_GENERIC_HARNESS_V2`
2. a one-to-one disposition table for Opus `C-1..C-4`, `R5..R12` and Sol
   repairs 1..14;
3. a strictness/conflict table for every overlap;
4. a state-transition and durable-order summary proving totality;
5. accounting invariants and worked concurrent known/unknown examples;
6. exact production roots/modules/paths/schema ownership and Cursor handoff;
7. the compatibility classification and any genuinely required token;
8. three bounded yes/no confirmation questions for Opus and three for Sol;
9. the exact negative authorization surface and confirmation that nothing ran.

The intended next step is one bounded Opus/Sol confirmation, not a new design
round. A `READY` verdict must therefore mean two independent implementers can
produce identical classifications, charges, durable ordering and admission
decisions from the contract.
