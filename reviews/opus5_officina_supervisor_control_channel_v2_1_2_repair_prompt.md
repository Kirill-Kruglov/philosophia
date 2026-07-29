# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.2 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**. You
authored v2.1 and v2.1.1 while Fable 5 was unavailable; you are not an
independent X/Y reviewer of your own bytes. Preserve that provenance literally.

Work in the local `philosophia` repository at or after commit `c4e0930`. Read
the governing chain and both independent v2.1.1 reviews in full, including:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
- `reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`

Pinned hashes:

```text
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  v2.1.1 correction
b5b5614166488bc8dca0856bf6963d84bd701757df153acaf868212687a2d797  Opus 4.8 X review
640305647c9c03d44f40899bf2434c089afb5cbbbf8286e9673852aa795cc6b1  GPT-5.6 Sol Y review
```

Treat your prior closure as authored self-assessment, not evidence. You may
inspect the inactive implementation read-only if needed for implementability.
Do not edit or execute code/tests and do not start an Officina process.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md`

The correction is a narrow replacement layer over v2 + v2.1 + v2.1.1. Include
an exact sentence/clause/table replacement index. Do not rewrite or silently
reinterpret earlier artifacts.

The closure's first line must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_2_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_2_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_2_CONTRACT_CONFLICT`

No new author cell is expected: both independent lines classify every required
repair as mechanical under the signed A3/B1/C1/D1/K1 selections. If you find a
real unavoidable choice, stop with `BLOCKED`; do not default it.

## Frozen meaning

All v2.1.1 repairs accepted by both reviewers carry forward unchanged. In
particular: supervisor-authoritative explicit `NEW`/`RETRY`; journaled STATUS;
descendant-aware reducer; validity-first takeover; two-hash spawn template;
reviewed adapter root; claim/renew/remove watchdog publication; durable
`RUNNING.json` before admission success; no K1 replenishment; total worker
status/EOF; honest non-citable A3 timing/metadata residuals.

The five signed K1 values remain immovable. Signed K1 also literally requires
that the supervisor **writes each output byte once and hashes each output byte
once**, and that capacity is released only after complete custody absence.

## Mandatory repairs

### R1. Acyclic, content-closed custody-disposition authority

Eliminate the circular fixed point in v2.1.1 §Z6.4/§Z6.5. Use one exact
one-directional construction, not a menu. Recommended construction:

1. Derive a canonical tracked author-decision path from already-known values
   (`operation_id` and the fixed repository namespace), never from its own file
   hash.
2. Derive `disposition_id` from a canonical preimage containing only
   already-known values such as `activation_record_sha256`, `operation_id`, and
   the canonical author-decision path/domain tag. It must not depend on
   `author_decision_sha256` or bytes that contain `disposition_id`.
3. The tracked decision file may then contain the already-computable id.
4. Hash the completed file once and bind `author_decision_sha256` in the
   disposition object/verifier; the file hash never feeds back into its id.

Make the tracked decision file content-closed: exact canonical bytes or an
exact schema/parser with no arbitrary prose. It may contain only the fixed
heading/schema and exact token/binding lines needed by the contract. Forbid
additional result, learner, candidate, Q/C, scientific, output-content,
judgment, or free-text fields/bytes. Pin line endings, order, encoding, path,
no-replace rule, Git/tracked/signature verification, and every hash domain.

Show the dependency DAG and a worked construction proving no self-reference.
Attack stale, substituted, replayed, partial, wrong-path, wrong-parent, and
forged objects. No failure releases capacity.

### R2. Complete custody-absence proof

One mutable/pre-rename `custody_root` is insufficient. Define the canonical
**complete custody-location set** for one `operation_id` and prove absence from
every member in one held-lock epoch before release. At minimum include:

- the operation's source `out/` tree;
- every staging/incomplete copy or rename location allowed by the protocol;
- the operation's quarantine location(s);
- `runtime/T_PROMOTED/<operation_id>/`;
- every operation-bound custody record, temporary, or directory that can hold
  or name retained bytes under the signed protocol.

The verifier must derive this set from the immutable operation identity and
fixed roots, not trust one record field. It must use descriptor-safe,
no-symlink enumeration and reject an unknown/additional custody location.
Prove both crash directions: before promotion rename, and after promotion
rename. A pre-rename settled record can never prove post-rename absence alone.
Pin the interaction with quarantine, partial promotion, crash recovery,
delivery acknowledgement, and the eventual supervisor-produced disposed
record. Custody anywhere means `bytes_reserved` remains fully accounted.

### R3. Earliest supervisor-grandchild identity

Close the cut between the second fork and v2.1.1's descriptor-scrub step.
There must be no instruction executed by the grandchild while it holds the
fork-shared `SPAWN.lock` before a parent/CLI-controlled kernel-verifiable
identity makes it killable.

Pin an exact construction in which the middle child or CLI receives and
durably installs the grandchild pid, pgid/session, start identity, boot
identity, and `spawning_id` immediately after the second fork, before the
grandchild performs descriptor enumeration, stdio redirection, endpoint work,
watchdog work, or any wait. Define the sealed report channel, who writes the
record, ordering/fdatasync/parent-fsync, bounded wait, pid/start verification,
kill/death proof, lock ownership, parent/middle-child crash cuts, and cleanup.

Every cut after the grandchild exists must yield either a killable durable
identity or proved process death that releases the lock. Preserve D1 and the
single-supervisor invariant without an unbounded `flock` wait.

### R4. Literal K1 write-once/hash-once

Remove the inline content hash from the output write path. The supervisor still
writes each frame's bytes exactly once and enforces byte/count/path ceilings
while writing, but computes the sole content hash only in the bounded
pre-settlement descriptor-held verification pass. That pass must read and hash
each output byte exactly once, retain the equal-size/inode substitution
defence, and feed the canonical result hash used by settlement/promotion.

Pin how crashes before/during that sole hash pass route, how counts are checked
without hashing, and why no later path hashes content again. Metadata/hash-tree
construction may hash canonical metadata, but no output content byte twice.
Preserve the named directory-swap A3 residual rather than claiming more.

### R5. Writable rejected-witness fallback

The supervisor cannot replace a malformed current-generation no-replace
watchdog witness at the same `witness_id`. Define a separate deterministic
supervisor-fallback/rejection witness namespace and id, bound to at least the
rejected object's path/id and SHA-256 (or an explicit missing sentinel), the
current generation/process/table, and a domain tag. The original object remains
immutable and non-evidence; it is never overwritten or deleted to make room.

Separate `unknown_reason` (historical freeze instant/evidence unverifiable)
from the **current** unresolved-member count. Allow an `UNKNOWN` historical
fact with zero currently unresolved members after the supervisor itself proves
quiescence. Pin schema, name, no-replace continuation, duplicate/conflict
handling, consumption order, and all-live invalid route. The fallback remains
a supervisor runtime-authority fact; the watchdog remains only a witness.

Also close Opus's inherited non-overdue-group ambiguity: after a watchdog death,
groups frozen only for replacement and still non-overdue may be `SIGCONT`ed
only after the replacement watchdog's exact current table is durably acked and
their identity/state is revalidated. Any mismatch/overdue/unknown condition
takes the signed invalid route. Pin this transition and its crash cuts.

### R6. Collision-safe fixed-fd remap

Specify an exact remap algorithm total for every distinct valid `(low, high)`,
including `(4,3)`, `(3,4)`, one source already in `{3,4}`, and sources outside
the set. Safest route: duplicate both original sources to fresh private
descriptors outside `{3,4}` before either target is overwritten; set the exact
inheritability/CLOEXEC state; `dup2` temporaries to 3 and 4; close originals and
temporaries without closing a target; then verify pipe type, direction, role,
and forbidden-fd closure. Pin failure cleanup and self-stop ordering. Do not
add imports or rely on implementation discretion.

### R7. Total acknowledgement priority

Remove the overlap between `SUCCESSOR_OCCURRENCE` and `CLIENT_ECHO`. Pin one
pre-allocation/pre-effect priority rule for `acked_effect_reply_sha256_or_null`:

- `null`: no ordinary acknowledgement;
- the exact permitted prior cached reply hash: install the named ack according
  to the closed source rule;
- any non-null mismatch: `INVALID/REPLAY_BYTES` before allocation or any other
  state movement.

Define which exact prior occurrence/hash is permitted for a successor and for
an explicit retry. A stale-but-genuine hash must have one deterministic result;
adopt a no-op/specific older acknowledgement only if it preserves the
contiguous-prefix proof and remains completely specified. Otherwise reject it
as the mismatch case. Update the eight-command trace and enums consistently.

### R8. Later safe GC

Keep `ack.json` installation and contiguous-prefix advance atomic in the same
lock epoch. Delete the requirement that physical GC occur only in that same
epoch. Permit GC in any later held-lock epoch once the immutable ack,
contiguous prefix, and the command-specific archival predicate are all
verified. Define the archival predicate for every command, including
observation-form STATUS with empty effect tuples (state explicitly whether it
is satisfied by durable committed+reply). Pin concurrent GC/retry behavior,
crash cuts, retention bounds, and post-GC classification.

### R9. Absent-scope defaults and exact reconciliation

Pin:

```text
tombstone_next(absent) := 1
acknowledged_prefix(absent) := 0
```

Reconcile every affected schema/path/constant/table, worked example, immutable
object owner, verifier duty, and implementation-test obligation. Add no free
text, hidden author judgment, scientific field, new public command, signed
event, resource value, or Q/C surface.

## Required proof obligations in the correction/closure

Include at least:

1. Exact replacement index v2.1.1 → v2.1.2.
2. One-to-one dispositions for Opus X211-C1/m1/m2 and all Sol
   C1..C4/M1..M5/m1, distinguishing required from optional observations.
3. Acyclic hash dependency graph and a byte-level canonical author-decision
   example whose hashes can be computed in forward order.
4. Complete custody-location table and before/after-rename crash proof.
5. Earliest-grandchild fork/record/lock automaton with every crash cut.
6. Write-once/hash-once byte accounting proof.
7. Watchdog rejected-witness and non-overdue replacement traces.
8. Exhaustive fd-remap table.
9. B1 acknowledgement-priority and later-GC traces for all eight commands.
10. No-regression table for A3/B1/C1/D1/K1, signed generic harness,
    batch-settlement amendment, nine events, E1/E2/E3, roots, and Q/C boundary.
11. Exact implementation/test obligations, but no implementation authorization.
12. One bounded literal final-confirmation question each for an independent
    clean-context Claude Opus 4.8 X-line and GPT-5.6 Sol Y-line, requiring them
    to read and hash the actual v2.1.2 bytes rather than trust your closure.

## Authorization and custody

Do not edit old specifications, signatures, reviews, code, tests, runtime
trees, or unrelated dirty files. Do not run tests/probes or start any process.
Do not authorize implementation, signing, activation, entropy, T/Q/C work, or
scientific execution. The author token remains unavailable until both
independent v2.1.2 confirmations accept the corrected bytes.

Confirm that exactly the two deliverables were created; T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`; and no runtime,
scientific, capacity, disposition, entropy, or outcome artifact exists.
