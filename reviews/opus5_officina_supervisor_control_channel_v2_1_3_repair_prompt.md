# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.3 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent reviewer of your own bytes. Preserve that provenance.

Work in the local `philosophia` repository at or after commit `dbd148a`. Read
the full v2→v2.1→v2.1.1→v2.1.2 chain, signed A3/B1/C1/D1/K1 selections,
generic-harness and batch-settlement inheritance, and both independent v2.1.2
reviews:

- `reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md`

Pinned hashes:

```text
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  v2.1.2 correction
aa25b28cedd813fbd2da36e0087cc9773be86b21a96c828bde57778953933dc7  Opus X review
22e2fb392c5758d7bab6840cafd711a9e4fa74b19b60bd5b05aebbde9b66c878  Sol Y review
```

Treat prior author closures as untrusted self-assessments. Static work only:
do not edit/run code or tests and start no Officina process.

## Deliverables

Create exactly two files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md`

The correction is a narrow replacement layer over v2.1.2. Include an exact
replacement index. The closure line 1 must be one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_3_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_3_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_3_CONTRACT_CONFLICT`

Both reviews say no new author cell is required. Do not default any genuinely
new choice if you discover one.

## Frozen closures

Carry all independently accepted v2.1.2 repairs unchanged: acyclic/content-
closed disposition authority; complete protocol-created custody set;
write-once/hash-once counts; rejected-witness fallback object; collision-safe
fd remap; single acknowledgement priority; absent defaults; canonical empty
hash; and the accepted v2.1.1 surfaces. Do not reopen them while repairing the
remaining lifecycle semantics.

## Mandatory repairs

### R1. Honest hash-once A3 boundary (Opus X212-M1; Sol m2)

Delete every claim that the sole content-hash pass mechanically detects
same-inode, equal-size in-place substitution. With no earlier trusted content
reference, it cannot. Preserve literal K1: each output content byte is written
once and hashed once.

State exactly what remains mechanical:

- inode substitution detected by held descriptor identity;
- size/EOF/count anomalies detected;
- link-count and path grammar checked;
- the sole hash accurately describes bytes read during that pass.

Name both windows as signed-A3 procedural, T-only, permanently non-citable
residuals:

1. same-inode/equal-size in-place modification before or during the sole hash
   pass when it is not caught as an unstable read;
2. any in-place modification after the pass and before durable settlement/
   promotion, plus the already-named directory-name swap.

Do not route these unobservable cases to `HASH` or claim future immutability.
Record the fundamental tension: detecting the first case would require a
trusted stored reference or a second content hash and would violate signed
hash-once. This is an honest boundary statement, not a weakening of K1.

### R2. Two-stage middle-child gate and truthful group identity (Sol C1)

Replace v2.1.2's assumption that `middle_child_pid` is already a PGID/session
id immediately after fork. Use one exact two-stage protocol:

1. After the first fork, the **middle child's literal first instruction** is a
   blocking read on a CLI-owned pre-setsid release pipe. CLI death closes the
   only write end, causing EOF and `_exit` so the fork-shared lock is released.
2. The CLI reads and verifies the middle child's pid/start/boot identity and
   durably installs a `SPAWNING_MIDDLE` record before releasing stage 1.
3. The middle child executes `setsid()`, verifies `sid == pgid == pid_mid`,
   reports the verified group/session identity over a sealed channel, and then
   blocks on a second CLI-owned pre-fork release pipe.
4. The CLI verifies `/proc` identity and `sid/pgid`, then durably installs
   `SPAWNING_GROUP.json` with the now-true group identity before releasing
   stage 2.
5. Only after stage 2 may the middle child fork the grandchild. The grandchild
   retains its own existing release gate until `SPAWNING_CHILD` is durable.

Before verified `setsid`, failure/timeout kills only `pid_mid` after exact
start-identity validation. After verified group installation, kill the group.
Pin sealed-fd ownership, EOF behavior, bounded waits, CLI/middle/grandchild
crash cuts, record durability, PID reuse, lock release, and no unbounded wait.
No process may execute an unrecorded action while retaining the shared lock.

### R3. Total swap-only watchdog state machine (Sol C2)

Explicitly replace the carried §W3.5 action for **non-overdue groups** during
watchdog replacement. A swap-only freeze writes only the replacement-freeze
record, never a §W3.3 deadline-freeze witness. Deadline/overdue freezes retain
the existing witness route.

Define three mutually exclusive states with exact precedence:

- `ACK_PENDING`: group remains frozen while the bounded replacement-watchdog
  ack/deadline race is unresolved; this is not yet invalidity;
- `RESUMABLE`: exact current table ack plus every identity/member/state/no-
  invalidity predicate passes; durable resumed marker precedes `SIGCONT`;
- `INVALID`: deadline passed, replacement failed/timed out, definitive
  identity/member/evidence mismatch, or unresolved invalidity; take the signed
  all-live invalid route.

Remove the rule “any failed conjunct ⇒ invalidity” where the only missing
predicate is a still-pending bounded ack. Pin transitions, timestamps, records,
crash cuts, supervisor-loss behavior, and ensure no healthy non-overdue group
is mechanically forced into invalidity. No swap-only record may synthesize a
freeze instant or become a second watchdog/runtime authority.

### R4. Crash-completable GC with `ack.json` last (Sol M1)

Adopt an exact deletion order under the held lock:

```text
accepted.json → committed.json → reply.json → ack.json (last)
```

Eligibility is checked before the first deletion from immutable ack + prefix +
command archival predicate. Because `ack.json` is last, every partial prefix
still has the durable eligibility witness needed by the next epoch. After the
last deletion, prefix-first classification is sufficient and no continuation
is needed.

Pin every crash cut, missing-prefix state, retry concurrency, EEXIST/ENOENT,
idempotent restart, directory fsync, and per-command archival predicates.
Delete the claim that arbitrary deletion order is safe.

### R5. Immutable result manifest and settlement binding (Sol M2)

The sole content-hash pass must create one exact immutable result manifest from
in-memory tuples produced during that same pass, without rereading content.
Define:

- canonical path and schema;
- exact keys and sorted tuple entries
  `{relative_path, byte_length, content_sha256}`;
- canonical ordering/encoding/hash;
- no-replace durability and crash cuts;
- `result_manifest_sha256` binding in the exact `SETTLEMENT.json` schema;
- `result_sha256` derivation from the canonical manifest/metadata;
- disposition verifier resolution of the manifest and recursive scientific-
  field prohibition;
- retention and custody relation.

No content byte may be reread or rehashed to build/verify this object. Verifiers
verify manifest/object hashes and canonical metadata only. Reconcile all
schemas, object tables and tests that currently claim per-file hashes already
exist in `SETTLEMENT.json`.

### R6. Total singleton spawn-record lifecycle (Sol M3)

Extend preflight under `SPAWN.lock` to all singleton attempt records, including
the new middle/group/child records. Before a new attempt:

- byte-identical live same-attempt record is idempotent;
- dead/stale record may be removed only after exact pid/start/death proof;
- conflicting live identity is `BOOTSTRAP`, with no unlink;
- malformed/ambiguous record is fail-closed and releases no live process.

Pin `EEXIST` at every no-replace install. Every death-proved failure route
removes records in exact child → group → middle → spawning order with parent
directory fsyncs. No route may omit `SPAWNING_CHILD` or leave a stale singleton
that wedges the next conforming attempt. Reconcile takeover discovery/removal
actors and all new R2 records.

### R7. Bind author timestamp (Sol M4)

Require disposition-object `authorized_utc` to equal the byte-exact decision
file's `signed_utc` exactly. Prefer one field name in both objects if that does
not create a wider schema change. Pin format, parser, verifier and mismatch
route (release nothing). No independent timestamp may remain outside the
content-closed authority.

### R8. Deterministic custody-proof summary (Sol m1)

Do not serialize L4/L5 grammars as if they were concrete path strings. Replace
`custody_locations_proved` with a fixed closed proof-class representation, for
example:

```text
SOURCE
OPERATION_DIRECTORY
PROMOTED
TEMP_GRAMMAR
UNKNOWN_NAME_SCAN
```

Bind the relevant fixed-root hashes and canonical directory-enumeration hashes
for the proof epoch. Pin exact ordering, encoding, empty-set representation,
and verifier. This field is diagnostic evidence of the complete proof; it may
not narrow the actual absence predicate.

## Required proof obligations

The correction and closure must include:

1. Exact v2.1.2→v2.1.3 replacement index.
2. One-to-one disposition of Opus X212-M1/m1 and Sol C1/C2/M1–M4/m1/m2,
   while explicitly carrying all independently closed v2.1.2 findings.
3. Truth table for what the sole hash pass detects and cannot detect.
4. Complete two-stage middle-child/group/grandchild automaton and every cut.
5. Exclusive watchdog replacement state machine and deadline/ack races.
6. GC deletion-prefix proof with `ack.json` last.
7. Exact result-manifest and `SETTLEMENT.json` schemas plus forward hash DAG.
8. Singleton spawn-record EEXIST/death/cleanup table.
9. Timestamp and custody-proof-summary canonical byte examples.
10. No-regression table for A3/B1/C1/D1/K1, inherited signed surfaces, nine
    events, E1/E2/E3, roots/imports and Q/C boundary.
11. Exact implementation/test obligations, but no implementation authorization.
12. One bounded final-confirmation question each for independent clean-context
    Claude Opus 4.8 X and GPT-5.6 Sol Y, requiring the actual v2.1.3 hash.

## Prohibitions and authorization

Do not edit old specs, signatures, reviews, code, tests, runtime trees or
unrelated dirty files. Do not run tests/probes or start any process. Do not
authorize implementation, signature, activation, entropy, T/Q/C work or
scientific execution. The author token remains unavailable until both
independent confirmations accept the v2.1.3 bytes.

Confirm exactly two deliverables, T `NOT_ACTIVATED`, programme claim `OPEN`,
and no runtime/scientific/capacity/disposition/entropy/outcome artifact.
