REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2

# Independent Y-line bounded confirmation — P1 process-claim identity choice v2

**Reviewer:** GPT Sol, independent Y-line scientific-validity and governance reviewer.  
**Scope:** bounded confirmation of the committed v2 packet against the two v1 reviews and the governing signed chain. The author closure was treated as untrusted.

## Findings

### Critical — YV2-C1: the claimed four-consumer durable-use closure omits a signed fifth consumer

**Finding.** Section 2.6.2 says that `C-1..C-4` are the complete persistent-consumer whitelist, §2.6.1 says there is no declassifying operation, `P-R4` prohibits routing either restricted value to a journal, diagnostic, frame, or any record other than the claim and lease, and `ACC-R1..ACC-R4` purport to close every reader. That closure is contradicted by the signed process-claim hash lineage:

- `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:95-102` requires the durable `T_PROCESS_STARTED` event to carry `process_claim_sha256` after the process claim is created and verified;
- `OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238` places `controller_pid` and `process_group_id` in the canonical claim whose bytes are hashed;
- the same activation protocol at `:248-257` requires `process_claim_sha256` in `t-process-record.v1`; and
- v2 §3.2 itself acknowledges that the final record has a content dependency on that digest.

The canonical whole-claim SHA-256 operation is therefore a required fifth persistent consumer, even though its output is not another numeric PID/PGID field. A reload route such as reading the canonical claim bytes and hashing the complete byte string uses neither restricted key literal and binds neither integer; it consequently escapes `ACC-R1` and `ACC-R2`. On the present text it is simultaneously required by the signed chain and forbidden or unclassified by `P-R1`, `P-R4`, and the statement that no declassification exists.

**Exact consequence.** `Y-C1` is not closed as dispositioned. The v2 whitelist cannot be implemented while preserving both its own rules and the signed activation/event lineage. Option A is not selectable on these bytes, and the proposed weakening token is not yet signable. This is not evidence of a process-control, capacity, custody, selection, Q/C, or scientific channel: it is a missing authorization and one-way classification boundary for an already-signed integrity digest.

### Major

None beyond the consequence of YV2-C1.

### Minor

None.

## One-to-one disposition of the original findings

| Original finding | Bounded Y-line determination |
|---|---|
| X `M-1`, incomplete `J4` replay durability | **Closed.** v2 gives `J4` the complete thirteen-key canonical AWAIT_STOP response operand vector, pins encoding and key order, and requires verbatim operand redelivery after `COMPLETED` or `ACKED`, with only the signed replay envelope changes. No post-crash PID/PGID re-observation or reconstruction is permitted. The journal-format edit is now in the blast radius and handoff. |
| X `M-2`, unproved taint closure | **Closed.** The withdrawn taint argument is replaced by a syntactic positional occurrence whitelist. The named laundering forms add a disallowed occurrence rather than relying on interprocedural taint completeness. |
| X `m-1`, fresh PGID authority | **Closed.** `A-P4a..A-P4d` select the fresh stopped-child read as authoritative, require the stored non-null handle value to cross-check, and make disagreement invalid. |
| X `m-2`, PID bound | **Closed.** The platform premise, range `1..4194304`, no truncation, and fail-closed over-range routes are explicit. |
| X `m-3`, freeze-actor conflation | **Closed.** v2 separates supervisor action after PCS EOF from watchdog action after supervisor EOF by actor, trigger, authority, and unresolved status. |
| Y `Y-C1`, incomplete persistent-use/dataflow closure | **Not closed.** Claim hashing into `process_claim_sha256` is the required fifth consumer and a whole-object reload/hash route outside `ACC-1..ACC-3`. |
| Y `Y-C2`, unconstructible replay across `J4` | **Closed.** The byte-identical operand vector is durable before delivery and is replayed without observation, synthesis, or omission. |
| Y `Y-M1`, crash/collision and invalidity dominance | **Closed.** The matrix is keyed to the crossed durability boundary; post-claim PCS death retains the claim; canonical `EEXIST` convergence requires byte, schema, cross-field, and expected-hash agreement; every mismatch is record-first process invalidity and never completion. |
| Y `Y-M2`, overstated Option B process-record schema change | **Closed.** The final record does not inherit the identity keys. Its `process_claim_sha256` dependency is correctly identified as content rather than schema, although that same dependency exposes YV2-C1 above. |
| Y `Y-m1`, overbroad argv rationale | **Closed.** The stale `/proc` route remains unauthorized through staleness, lack of PCS attestation, and bypass of the closed opcode authority; the narrower evidentiary effect of the argv deletion is now stated accurately. |

No other original X/Y finding is reopened. The sole refusal is the concrete signed-chain contradiction identified above.

## Bounded determinations

### 1. Completeness of `C-1..C-4`, the restricted class, and `ACC-1..ACC-3`

**NO.** `C-5` is the canonical whole-claim hashing operation that produces `process_claim_sha256` for the signed start-event and final-record lineage. It is also a concrete reload route that escapes the literal-key accessors: raw canonical bytes can be reopened and hashed without accessing either key by name. The four listed numeric consumers are otherwise the correct direct-value set.

### 2. Legitimate copies, comparisons, and forbidden laundering

The claim-to-lease whole-mapping copy is legitimate because the signed lease is the claim keys plus its additional keys. The claim/lease immutability comparison and freeze-predicate read are legitimate boolean consumers. Reload does not turn either integer into authority, addressing, process control, capacity, custody, spend, selection, qualification/comparison, Q/C, evidence, outcome, or Proof. The occurrence/accessor rules correctly make all such routes invalidity-first.

The exception is not a laundering permission: the signed chain requires one exact full-claim integrity hash. Its result must remain a lineage digest with no authority or scientific meaning. That exception must be written explicitly rather than inferred against `P-R1`/`P-R4`.

### 3. Replay, collision, retained claims, and invalidity dominance

The repaired `J4` representation supports byte-identical replay of the complete stored operand vector. Replay does not re-observe the process or reconstruct fields. Malformed, partial, tuple-inconsistent, out-of-range, or cross-field-inconsistent branches route deterministically to record-first process invalidity.

Crash before durable claim installation leaves no claim. Crash after installation cannot delete or replace it: PCS death retains the claim and follows the signed invalid-process route. `EEXIST` is convergence only after canonical-byte, schema, cross-field, and expected-hash checks all pass; otherwise the occupant is retained and invalidity dominates. These repairs preserve B1 replay semantics and remove post-outcome discretion.

### 4. Authority under A3/P1

PCS-attested PID/PGID observation remains provenance only. Same-UID kernel capacity pre-exists the observation; the signed procedural authority remains the handle-indexed, closed request grammar with PCS as sole process-control caller. Neither receipt, persistence, reload, equality comparison, nor hashing authorizes addressing, signalling, waiting, custody, selection, or any other process-control initiative.

### 5. Corrected A/B comparison and recommendation

The correction is honest that A grew through the journal-format repair and B shrank because `t-process-record.v1` is not superseded. B nevertheless remains non-selectable: its PCS peer-visible write and `R-L4` authority sub-cells are unresolved and cannot be closed by the existing signed chain without another author choice.

A would remain the validity/governance recommendation after the exact repair below because it reopens no signed validity predicate and inverts no architectural authority rule, while B is not selectable. That recommendation is independent of any predicted learner, arm, qualification, comparison, Q/C, datum, or scientific outcome. On the current bytes, however, A is **not yet selectable** because the persistent-consumer closure is false.

### 6. Disclosure and conditional author token

Section 2.12 adequately displays the old and proposed authority sentence, identifies the change as a real lexical-to-syntactic bounded weakening, and requires the dedicated conditional token `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`. This is sufficiently loud for informed author signature **once** YV2-C1 is repaired and independently confirmed. It does not itself confer process-control power.

### 7. Watchdog-freeze orthogonality

The separate watchdog-freeze choice remains unresolved and orthogonal. The identity packet correctly distinguishes supervisor handling of PCS loss from watchdog handling of supervisor loss. Nothing in this review solves, selects, merges, or authorizes that cell; P1 remains non-operative while it is unresolved.

## Smallest exact repair

Revise only the persistent-use closure and its dependent counts/checks:

1. Add `C-5`: after canonical claim validation, exactly one whole-object SHA-256 operation over the canonical claim bytes may produce `process_claim_sha256`, solely for the already-signed `T_PROCESS_STARTED` and final process-record lineage destinations. No partial-field hash, alternate encoding, secondary digest, or numeric identity binding is permitted.
2. State the one-way classification boundary explicitly: the exact full-claim digest is an integrity/lineage identifier, not process identity; it cannot be reversed or used for addressing, process control, capacity, custody, spend, selection, qualification/comparison, Q/C, datum, outcome, evidence, or Proof. Either define this as the sole declassification from `RESTRICTED_PROCESS_IDENTITY`, or retain the digest inside a restricted derived class and whitelist only those two signed lineage destinations.
3. Add one centralized canonical-byte hash accessor/verifier rule. It may read the validated raw claim bytes but may not bind either identity field individually. Update `P-R1`, `P-R4`, `ACC-R1..ACC-R4`, the schema-reader audit, `S-25d/e/g`, `A-T9`, the A-side consumer/count text, the closure disposition, and the v1.3 handoff to include this exact site and no other.

No new A/B design cell is required. After this bounded repair, A remains the Y-line validity/governance recommendation; B remains non-selectable.

## Custody and authorization boundary

Recomputed target hashes:

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
```

For comparison, the reviewed v1 finding reports recompute as:

```text
bfa7f6dd6a09313033b2a00c75f0e1e0632c63f65733b80424ee889433364f3b  reviews/opus_officina_p1_process_claim_identity_choice_review.md
705b36b6ce1a9387261f66f2a473295be4384903b0e0240ae8e7496af6899e80  reviews/sol_officina_p1_process_claim_identity_choice_review.md
```

This verdict authorizes no selection or weakening token on the present bytes and no implementation, activation, process-control action, spend, data, outcome, Proof, or claim movement.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
```
