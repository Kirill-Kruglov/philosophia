# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.4 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**, not an
independent reviewer. Work in `philosophia` at or after commit `3b7d9e6`.

Read the complete supervisor correction chain, signed A3/B1/C1/D1/K1
selections, inherited generic-harness/batch-settlement surfaces, and both
v2.1.3 reviews in full:

- `reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md`

Pinned hashes:

```text
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  v2.1.3 correction
6cc52972e6229005f98d15db0fac113a77d2c2382133cc745f387fced845b008  Opus X confirmation
214ac0d5fb1cecf873e8b91ca95079dc67df8018762a18df46e94cb912d7df75  Sol Y review
```

Treat prior author closures as untrusted. Static authoring only: no code/test
edits or execution and no Officina process.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md`

The correction must be a narrow replacement layer over v2.1.3 with an exact
replacement index. Closure line 1 must be one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_4_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_4_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_4_CONTRACT_CONFLICT`

No new author cell is expected. Preserve every independently confirmed v2.1.3
closure; repair only the findings below and any exact references they affect.

## Mandatory repairs

### R1. Actually bounded pipe protocol and every errno branch (Sol C1; Opus X213-m2)

Make the report channel genuinely nonblocking: create `boot_pipe` with
`O_NONBLOCK` or set the CLI read end nonblocking before any bounded read. Pin
one exact helper-level state machine for every stage read/write:

- `EAGAIN`/`EWOULDBLOCK`: paced retry using an existing polling constant until
  the existing stage deadline;
- EOF before a complete canonical frame: the stage-specific failure cleanup;
- malformed/overlong/duplicate/trailing report bytes: fail-closed cleanup;
- every other read error: fail-closed cleanup;
- nonblocking report/release write: retry partial/EAGAIN until the same bounded
  stage deadline; `EPIPE` or other error takes the stage-specific cleanup.

Pin exact frame lengths (all report/release writes are ≤ `PIPE_BUF` if you rely
on atomicity), ownership and close order. The grandchild must not retain the
middle-child report write end in a way that prevents EOF; explicitly close it
as an authorized first bootstrap fd action before its rel3 gate, or show why
the nonblocking deadline alone makes every cut total. Do not claim `m0` “sees
EOF” while the middle child still owns a write end: state whether it exits by
EOF, EAGAIN-until-bound, or an explicit release byte.

Re-run c4→c18, m0→m9 and g0→identity for CLI/middle/grandchild death at every
instruction. No blocking syscall may prevent deadline evaluation, no pipe
cycle may retain `SPAWN.lock`, and every cleanup uses the already-signed
identity/kill discipline.

### R2. Orphan-manifest quarantine is a valid K1 disposition branch (Sol C2; Opus X213-m1)

Extend the exact immutable `QUARANTINE.json` schema with
`result_manifest_sha256_or_null` and pin when it is non-null. If
`RESULT_MANIFEST.json` becomes durable but `SETTLEMENT.json` does not, the
record-first crash reducer must install/verify a quarantined terminal that
binds the orphan manifest hash; if no manifest exists, the field is null.

Split disposition-manifest verification into three exact, exclusive branches:

1. `PROMOTED`/settled: resolve the manifest hash through `SETTLEMENT.json`;
2. `QUARANTINED + manifest`: resolve it through `QUARANTINE.json`, validate the
   immutable manifest, operation id, canonical entries/result hash and content-
   prohibition identifiers, with no settlement required and no output reread;
3. `QUARANTINED + no manifest`: require null plus physical manifest absence;
   manifest-dependent checks are vacuous only here.

Unexpected combinations, orphan file without binding, hash mismatch, duplicate
or partial objects release nothing. Pin crash cuts, no-replace/EEXIST,
retention, custody-set interaction, and exact schemas/test obligations. This
must restore the legitimate complete-custody release route for all admitted
quarantine states without weakening `bytes_reserved` accounting.

### R3. Preserve G3 authority throughout GC (Sol M1)

Replace v2.1.3's deletion order with this exact authority-preserving order:

```text
committed.json → reply.json → ack.json → accepted.json (last)
```

Before the first deletion verify immutable `ack.json`, prefix and the command-
specific G3 predicate using `accepted.json`'s command/effect plan. While any of
`committed`, `reply`, or `ack` remains, both `accepted` and (until its turn)
`ack` preserve eligibility. After `ack` is removed, only `accepted` may remain;
a dedicated finalization rule re-verifies prefix + the exact G3 authority in
`accepted` and deletes `accepted` last. Once it is gone, only empty-directory
completion is legal.

Pin directory fsyncs, ENOENT/EEXIST, crash after every unlink/fsync, concurrent
retry/GC, prefix-first classification, observation STATUS, and every command's
G3 binding. No surviving semantic phase may lack the information needed to
resume GC, and no owed reply may be deleted before durable acknowledgement.

### R4. Acquire `SPAWN.lock` before singleton preflight (Sol M2)

Make the order single-valued:

1. bounded acquire `SPAWN.lock` or take the signed stuck-holder route;
2. while holding it, run the full §U6 singleton preflight/adoption/removal;
3. only then install the new `SPAWNING` attempt record and continue.

No preflight read that can lead to adoption, removal, kill, or mutation may
occur before lock acquisition. Reconcile c1/c2, takeover, P0–P3, EEXIST and
every cleanup/crash table.

### R5. Total watchdog replacement priority (Sol M3)

Pin invalid conditions in exact priority order `I1 → I2 → … → I7`; the marker
records the **first true** condition and may optionally record a closed
diagnostic set only if that cannot affect routing.

I2 must mean: **no valid acknowledgement of the exact current `table_seq` by
the bounded absence deadline**. Stale, wrong, malformed or prior-table acks do
not satisfy it.

Make the state partition exhaustive:

- evaluate I1–I7 in priority; first true ⇒ `INVALID`;
- otherwise exact-current-table ack plus every member identity matching and
  every pre-resume member state exactly `T` ⇒ `RESUMABLE`;
- otherwise, only while the exact-current ack is pending and before the bound ⇒
  `ACK_PENDING`;
- if the exact ack exists but any member is not exactly `T`, I3 must be true;
  no S1-true/S2-false gap remains.

Pin timestamps, locked observations, deadline/ack simultaneous edge,
replacement failure, crash cuts and supervisor loss. Reproduce the complete
race truth table. No healthy non-overdue group may be invalidated merely by a
pending ack; no state may have two or zero continuations.

### R6. Correct the during-pass A3 statement (Sol M4)

Split completed-before-pass from concurrent-during-pass modification. Claim
only that the sole hash describes the exact byte **stream read**. During a
concurrent overwrite, the stream may mix states and need not equal any final
inode state or the later promoted bytes. Post-pass changes likewise can make
`result_sha256` differ from promoted content.

Name all such cases procedural, T-only, permanently non-citable, unobservable
under literal K1 hash-once, and with no `HASH` route. Remove every phrase that
says or implies the recorded hash truthfully describes promoted bytes.

### R7. Correct the timestamp example (Sol m1)

Change only the incorrect illustrative count: the literal
`signed_utc: ...Z\n` line is **43 bytes including LF**, while the compared
timestamp value remains 30 ASCII bytes. Reconcile any derived example lengths
without changing the already-verified decision-file hash or timestamp rule.

## Required proof obligations

Include:

1. Exact v2.1.3→v2.1.4 replacement index.
2. One-to-one disposition of Sol C1/C2/M1–M4/m1 and Opus X213-m1/m2,
   carrying the X confirmation and every prior closed finding accurately.
3. Pipe descriptor/errno ownership table and every bootstrap cut.
4. Three-branch result-manifest/quarantine verifier and K1 release trace.
5. GC prefix proof using only files present after each cut.
6. Lock/preflight/EEXIST order table.
7. Exhaustive watchdog I-priority and ack/deadline race truth table.
8. Correct A3 hash-stream truth table.
9. No-regression table for A3/B1/C1/D1/K1 and inherited signed surfaces.
10. Exact implementation/test obligations, but no authorization.
11. One bounded question each for independent Opus 4.8 X and GPT-5.6 Sol Y,
    requiring actual v2.1.4 hash verification.

## Prohibitions

Do not edit prior artifacts, code, tests, runtime trees or unrelated dirty
files. Do not execute tests/probes/processes. Do not authorize signature,
implementation, activation, entropy, T/Q/C or science. Token remains
unavailable until both confirmations accept v2.1.4.

Confirm exactly two deliverables, T `NOT_ACTIVATED`, claim `OPEN`, and no
runtime/scientific/capacity/disposition/manifest/entropy/outcome artifact.
