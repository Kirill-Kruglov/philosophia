REVISE_OFFICINA_SUPERVISOR_V2_1_4

# Independent clean-context Y-line review

Date: 2026-07-31

Reviewer line: Y

## Review base, independence, and hashes

Review base: `f98e7bbb562ddeec169b49014d6b324807bd38cf`, proved to
descend from the required commit
`d6be6b246e853dacb2ce209b2341dfd0d5313da0`.

I read the complete v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4 supervisor
chain, both signed author selections, the inherited generic-harness and
batch-settlement corrections, and both independent v2.1.3 reviews. I treated
the v2.1.4 author closure and its chat response as untrusted author
self-assessment; neither supplies evidence here.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
214ac0d5fb1cecf873e8b91ca95079dc67df8018762a18df46e94cb912d7df75  reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
6cc52972e6229005f98d15db0fac113a77d2c2382133cc745f387fced845b008  reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
```

The v2.1.4 digest exactly matches the expected committed value.

## Answer

No. The correction supplies the intended mechanical repair for each of my
v2.1.3 C1, C2, M1, M2, M3, M4, and m1 findings, and the normal-path traces
carry the earlier closed repairs forward. Two new executable gaps prevent
confirmation:

1. The disposition selector makes `B-P`, `B-QM`, and `B-QN` overlap when both
   terminal records exist, while the same rule also requires that combination
   to refuse. This leaves release versus refusal discretionary in precisely an
   invalid durable layout.
2. The bootstrap covers read/write errnos after c8 but gives no total cleanup
   route for partial pipe construction, `fpathconf` failure, first-fork
   failure, or second-fork failure, and does not pin closure of every CLI-held
   channel on stage failure. These ordinary resource cuts are outside the
   claimed complete automaton.

Both are mechanical repairs. No scientific or resource value must be chosen,
and no new author cell is required. The signature token remains unavailable.

## One-to-one disposition of the v2.1.3 Y findings

| Finding | v2.1.4 repair | Independent disposition |
|---|---|---|
| **C1** blocking bootstrap/report channel and incomplete errno routes | §V214.1 makes all four pipes nonblocking, supplies bounded read/write helpers, and fixes the m7→m8 deadlock | **Named defect closed.** EAGAIN/EINTR/EOF/EPIPE/malformed/overlong/trailing routes are single-valued. New M2 below concerns resource failures before those helpers and cleanup after their failure routes. |
| **C2** orphan-manifest quarantine undisposable | §V214.2 adds the quarantine binding and `B-QM` | **Named ordinary crash state closed.** A genuine orphan manifest can bind to quarantine and dispose without settlement or content reread. New M1 below concerns the separate both-terminal impossible layout. |
| **M1** GC destroys G3 authority | §V214.3 retains `accepted.json` last and adds D6 | **Closed.** Every pre-D7 crash retains the command/effect authority; after D7 only predicate-free directory removal remains. |
| **M2** singleton preflight before/under lock contradiction | §V214.4 orders c1a acquire, c1b preflight | **Closed.** The unlocked stuck-holder route mutates no contract file. |
| **M3** replacement state/ack/condition selection non-total | §V214.5 pins I1→I7, exact-current ack, expanded I3, and the three-way partition | **Closed.** Every locked observation has one branch and one primary condition. |
| **M4** false promoted-byte claim for a during-pass mixed stream | §V214.6 distinguishes A3-R1a/R1b/R2/R3 | **Closed.** The sole hash claims only the exact stream read. |
| **m1** timestamp line miscount | §V214.7 changes 44 to 43 | **Closed.** The eight-line total remains 504 and its hash is unchanged. |

## Trace 1 — A3/K1 write-hash counts and residual windows

For each accepted nonempty frame, grammar, unique relative path, strict
positive content length, stream/path/depth/count ceilings, per-operation
reservation, aggregate ceiling, and filesystem margin are checked before file
creation. The supervisor opens the write descriptor and retained read
descriptor, writes exactly the declared bytes while maintaining integer
counters only, closes transport, validates worker status and group death, and
then performs one descriptor-based pass. The pass re-resolves the path,
matches `(st_dev, st_ino)`, requires `st_nlink == 1`, checks size/read
length/EOF, and feeds each content byte into exactly one hash. Manifest,
settlement, promotion, status, disposition, and GC read metadata only.

| Window or attack | Mechanical result | Meaning of a surviving hash |
|---|---|---|
| Bad path/length/count/ceiling before creation | Refuse or transport/quarantine route; no output byte written | none |
| Inode substitution | inode identity mismatch ⇒ `HASH` quarantine | none |
| Hard-link introduction | `st_nlink != 1` ⇒ `HASH` | none |
| Truncate/extend/short/long/wrong-offset EOF | size, length, or EOF check ⇒ `HASH` | none |
| Equal-size same-inode overwrite completed before pass (R1a) | undetectable | the modified single-state stream read |
| Equal-size same-inode overwrite during pass (R1b) | undetectable if length/EOF stay stable | a mixed successive-`pread` stream; it need not equal any coherent file state |
| In-place change after pass, before settlement/promotion (R2) | undetectable | the earlier read stream, not necessarily promoted bytes |
| Same-name `out/` directory swap before rename (R3) | undetectable | no claim about the substituted promoted tree |
| Crash before/during/after pass but before settlement | `SUPERVISOR_CRASH`; no resume, respawn, settlement, or promotion | no citable result |

The correction makes no stable-file-state, future-immutability, or
promoted-byte claim. R1a/R1b/R2/R3 have no `HASH` route, are same-UID A3
procedural residuals, remain T-development-only and permanently non-citable,
and cannot influence Q, C, C1–C6, selection, or scientific interpretation.
Literal K1 remains one write and one hash per output content byte.

## Trace 2 — spawn/bootstrap cuts and channel ownership

All four channel pairs are `O_NONBLOCK`; `PIPE_BUF >= 4096` is required for
each write end. A release is one byte and a report is one canonical line no
larger than 4096 bytes. `EAGAIN` is paced retry, `EINTR` immediate retry,
incomplete EOF/malformed/overlong/duplicate-or-trailing input fails the stage,
`EPIPE` is peer-gone, every other errno fails the stage, and a partial write is
fail-closed. The group report cannot race the bootstrap report because m5
gates m7/m8 until c9 has consumed the first report and c12 releases rel2.

| Cut | Identity and descriptor facts | Derived continuation |
|---|---|---|
| c1a/c1b/c2 | lock first; preflight and `SPAWNING` under it | conflict/adopt/remove per P0–P3 |
| partial c3 pipe creation or `fpathconf` failure | `SPAWNING` already durable; some pairs may be open | **No pinned close/removal route (new M2).** |
| c4 first `os.fork` failure | no middle exists; CLI owns all channel ends applicable before c5 | **No pinned route (new M2).** |
| c4→c7 CLI death | middle retains its own rel1 writer | m0 cannot rely on EOF; its nonblocking bound `_exit(3)`s |
| c7→c8 | `SPAWNING_MIDDLE` names exact pid/start identity | pre-group failure uses `kill(pid)` only |
| c8/c9 | middle passes m0, closes unused ends, `setsid`, verifies SID=PGID=PID, writes report | c9 bounded read; any failure stage 1 |
| c10/c11 | CLI independently verifies kernel SID/PGID before durable `group_verified:true` | only now may cleanup use `killpg` |
| c12/m5 | rel2 release, middle proceeds | EOF/error/bound in m5 ⇒ `_exit(3)` |
| m7 second `os.fork` failure | verified group and middle record exist; no grandchild exists | **No explicit m7 error route; relying on language exception exit is not contract text (new M2).** |
| middle death m7→m8 | grandchild retains boot writer and waits at g0 | c13 sees EAGAIN until its executable bound, then stage-2 `killpg`; no pipe cycle |
| middle death before m7 | no grandchild boot writer | c13 sees EOF and takes stage 2 |
| valid m8 report | grandchild pid/start/pgid reported | c14 re-verifies; c15 installs child record |
| c16 rel3 release | CLI is sole rel3 writer | grandchild accepts one exact byte; EOF/error/bound ⇒ `_exit(3)` |
| CLI death c12→c16 | sole rel3 writer closes | g0 EOF ⇒ `_exit(3)`; middle report gets EPIPE or exits |
| grandchild death at/before g0 | child identity absent or c17 times out | stage-2 kill/death proof/ordered cleanup |
| g1→g3 / first-ack failure | child record is durable; inherited descriptors scrubbed | watchdog/group cleanup, child→group→middle→spawning removal, `_exit(3)` |
| identity collision | no-replace winner serves | loser writes/unlinks nothing and exits |
| PID reuse | start identity differs | never kill; treat recorded process absent |
| stage helper failure at c8/c9/c12/c13/c16 | stage 1 or 2 kills/proves/removes/releases | record/lock route is pinned, but closure of every still-held CLI pipe fd is not (new M2) |

The original c13 deadlock is gone: boot is nonblocking, and a middle death
after m7 cannot prevent the CLI from reaching the deadline and `killpg`.
Nevertheless the automaton is not complete at construction/fork failures.

The grandchild's `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` self-exit is a total
anti-wedge bound, but §V214.1.1's statement that the factor is “required and
sufficient” for every healthy launch is not proved: c14 kernel verification
and c15's durable no-replace install have no duration bound. This is minor m1
below; expiration still fails the attempt closed and releases the child lock
reference.

## Trace 3 — C1 watchdog replacement state machine

| Observation/cut | Result |
|---|---|
| Watchdog loss; group already overdue at the freeze sample | ordinary deadline freeze, §W3.3 witness or rejected-evidence fallback, then signed invalid route |
| Watchdog loss; group non-overdue | swap-only SIGSTOP/quiescence and `REPLACEMENT_FREEZE`; no witness, fallback, `freeze_ns`, or `overrun_ns` |
| Replacement fork fails | I2 immediately |
| No exact-current valid ack before its bound | `ACK_PENDING`; frozen and evidence-free |
| Only stale/wrong-table/wrong-generation/malformed ack | never satisfies S1 or defeats I2; pending before bound, I2 at bound |
| Exact-current valid ack, identities match, every pre-resume member exactly T | `RESUMABLE`; install `.resumed.json` before SIGCONT |
| Any pre-resume member R/S/D/unknown/absent/Z/mismatched | I3, including the former S1-true/S2-false gap |
| Deadline and exact ack coincide | I1 wins because I1→I7 precedes S |
| Deadline, ack absence, and member defect coincide | primary `I1`; diagnostics `[I1,I2,I3]` |
| Witness/fallback appears | I4 |
| G5/record-first ordering blocks | I5 |
| Lease superseded | I6 |
| Supervisor generation changes | I7; no resume across takeover |
| No I true, no exact ack | exact remaining `ACK_PENDING` state |
| Crash after `.resumed.json`, before SIGCONT | relaxed post-marker T/running check and idempotent SIGCONT |
| Crash after `.invalidated.json` | resume the named signed invalid route; no reclassification |
| Both markers | record-first invalidity naming both paths |

The first true I-condition is deterministic; the sorted diagnostic set is
routing-inert because all I1–I7 share the same invalid route. The supervisor
alone writes transition records and settles. The watchdog cannot install a
terminal, select validity, append runtime state, or settle.

## Trace 4 — B1 and GC for all eight commands

`NEW(i)` is the only allocating form. `RETRY(handle)` names an already
accepted occurrence and never allocates or samples a new effect. Each accepted
effect and its reply are immutable and are replayed under the current
generation envelope.

| Command | Exactly-once/retry-stable effect | G3 selected from `accepted.json` |
|---|---|---|
| `CLAIM` | one process sequence and claim | owning process terminal archival commit |
| `START` | one start event and lease | same terminal archival commit |
| `HEARTBEAT` | one cursor/charge; retry never samples a clock | archive covering the exact charge |
| `CLOSE` | one close automaton and terminal set | signed close archive |
| `PAUSE` | one pause/checkpoint transaction | signed pause archive |
| `RESUME` | one checkpoint-bound resume plan | resume archive, or exact durable no-event predicate |
| `OPERATION_ADMIT` | one operation, reservation, and worker plan | operation terminal plus archive covering settling charge |
| `OPERATION_STATUS` delivery-ack form | one delivery ack | delivery ack plus operation terminal |
| `OPERATION_STATUS` observation form | one cached empty-effect observation per `NEW`; `RETRY` is byte-stable | vacuous predicate selected by `plan_kind=OBSERVATION` |

Shared classification and loss traces:

| Cut/attack | Deterministic result |
|---|---|
| Null ack hash | install no ordinary ack; prefix-first classification continues |
| Non-null hash with no frontier | `INVALID/REPLAY_BYTES`; no allocation or state movement |
| Exact frontier hash with `NEW(m+1)` | acknowledge m as `SUCCESSOR_OCCURRENCE`, advance prefix, then classify/allocate successor |
| Exact frontier hash with `RETRY(m)` | acknowledge m as `CLIENT_ECHO`, advance prefix, then prefix-first `ALREADY_ACKNOWLEDGED` |
| Exact hash with any other mode/index | `INVALID/REPLAY_BYTES` |
| Wrong or stale genuine hash | `INVALID/REPLAY_BYTES`; no state movement |
| Lost request | resend `NEW` only if no handle was allocated; `RETRY` cannot create one |
| Lost reply / client crash after observing reply | `RETRY(handle)` returns cached effect/reply until acknowledged |
| Generation change | current supervisor wraps the same durable effect/reply; effect is not repeated |
| Concurrent same-scope `NEW` | runtime lock serializes; one allocation, loser re-anchors to published next/frontier |
| Repeated STATUS | repeated `RETRY` observes the same cached status; a later `NEW` is a distinct occurrence |
| Non-contiguous ack | only the lowest frontier can ack; prefix stops at the first gap and drains one per frame |
| 64 unacknowledged occurrences | retryable `UNRESOLVED_JOURNAL`; published frontier permits bounded drain |

GC is under the same lock as service. D0 proves ack file, permanent prefix,
and the command-specific G3 selected from `accepted`. It then removes
`committed → reply`, fsyncs, removes `ack`, fsyncs, and at D6 re-proves prefix,
G3, and absence of those three using the still-present `accepted`. Only then
does it remove `accepted`, fsync, rmdir, and fsync the journal parent.

| GC crash prefix | Surviving authority and continuation |
|---|---|
| Before D1 / after committed / after reply | accepted+ack survive; re-run D0, ENOENT-tolerant |
| After ack unlink but before accepted unlink | accepted plus permanent tombstone; D6 re-selects and re-binds G3 |
| Accepted unlink not yet fsynced | accepted may reappear ⇒ D6; or remain absent ⇒ empty-directory rule |
| Empty directory | `i <= prefix` permits predicate-free rmdir |
| Post-rmdir before parent fsync | directory may reappear empty; same completion rule |
| Retry before/during/after any cut | prefix is consulted first; identical `ALREADY_ACKNOWLEDGED`, no reducer |

No reply is deleted until durable acknowledgement is proved. Once final GC
completes, no semantic obligation remains: the permanent prefix is the B1
acknowledgement authority and post-GC replay cannot reapply an effect.

## Trace 5 — result manifest and complete K1 custody

The documented arithmetic reproduced independently:

```text
canonical entries (265 bytes)
result_sha256 = 5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3

canonical RESULT_MANIFEST.json (638 bytes)
result_manifest_sha256 = e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed

canonical empty entries (`[]\n`)
result_sha256 = 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

The forward DAG is sole-pass in-memory tuples → canonical entries and
`result_sha256` → manifest bytes and `result_manifest_sha256` → terminal
binding. No verifier opens an output content file.

| Phase | Custody / terminal | Accounted contribution |
|---|---|---|
| admitted, running, pending | L1 source output and possible temporary names | `bytes_reserved` |
| sole pass complete | L1 plus in-memory tuples/manifest | `bytes_reserved` |
| settlement before rename | manifest+settlement; L1 | `bytes_reserved` |
| promotion | atomic L1→L3 rename; metadata retained | `bytes_reserved` |
| quarantine before manifest | L1; `B-QN` null binding | `bytes_reserved` |
| crash after manifest before settlement | record-first invalid terminal, quarantine binds manifest; `B-QM` | `bytes_reserved` |
| delivery ack | L3 unchanged | `bytes_reserved` |
| L4 temp grammar or L5 unknown name | custody present, disposition refuses | `bytes_reserved` |
| all L1–L5 absent in one lock epoch | disposition may verify, but reservation still counts until disposed install | `bytes_reserved` |
| `.disposed.json` installed once | complete absence plus author authority | release exactly `bytes_reserved` |

For normal states, B-P binds the manifest to settlement, B-QM binds an orphan
manifest to quarantine and validates its standalone schema/entries, and B-QN
requires both a null field and physical manifest absence. Forged, replayed,
wrong-operation, partial, absent, mismatched, wrong-parent, scientific-field,
or custody-still-present submissions refuse. `actual_bytes` and manifest byte
totals are diagnostic and never reduce accounting. Settlement, failure,
quarantine, promotion, rename, unused reservation, or delivery ack never
replenishes capacity.

The selector is not total as written for the both-terminal attack. Because
`B-P` requires only settlement presence and B-QM/B-QN require only quarantine
presence, both-terminal history satisfies a branch condition even though the
same paragraph orders `REFUSE`; see new M1.

## Trace 6 — singleton-record lifecycle

The four records are inspected under the acquired `SPAWN.lock` in
child→group→middle→spawning order.

| State | Continuation |
|---|---|
| Absent | install/continue |
| Malformed, nonregular, symlinked, wrong nlink | nonretryable `BOOTSTRAP`; no unlink or kill |
| Same live spawning id and byte-identical | adopt at the corresponding step |
| Same id but differing bytes | retryable conflict; no unlink/kill |
| Different live attempt | retryable conflict; aged handling only through s2–s4 |
| PID absent | prove absence; ordered cleanup; continue |
| Matching zombie | prove/reap only if own child; ordered cleanup |
| PID reused | never kill; treat recorded identity stale and clean under lock |
| EEXIST at c2/c7/c11/c15 | re-read under lock; P1/P2/P3; P3 retries install once |
| Crash during cleanup | resume child→group→middle→spawning, ENOENT-tolerant, fsync after each unlink |

Before c1a no record read may lead to adoption, removal, kill, or mutation.
After acquisition c1b owns all record mutation. The unlocked stuck-holder
route may read, validate, identity-prove, kill the one aged tier permitted by
the existing discipline, prove death, and retry acquisition once; it may not
unlink, adopt, install, or rewrite. On success c1b removes the now-stale
records. A malformed record remains an explicit operator-inspection
fail-close, not a silently unlinked wedge. No live record is unlinked and no
PID-reused process is killed.

The singleton lifecycle itself is repaired. New M2 is earlier/lateral to it:
resource failures at c3/c4/m7 and channel closures on stage failure are not
assigned a complete cleanup invocation.

## Trace 7 — author authority and exactness

The authority remains forward and acyclic:

```text
operation_id → canonical decision path
{domain tag, activation hash, path, operation id} → disposition_id
disposition_id → exact eight decision lines → file hash
file hash → disposition object → verified disposed record
```

The literal examples reproduced:

```text
disposition preimage: 396 bytes
disposition_id = e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

decision file: 504 bytes, eight LF-terminated lines
author_decision_sha256 = 0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f

operation-directory enumeration
3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc
```

Line 8 is 43 bytes including LF: 10-byte key + colon + space + 30-byte
timestamp + LF. The signed timestamp and disposition `authorized_utc` are the
same 30 bytes. Extra content, wrong path/id, stale activation/generation,
substituted operation or parent, replay, partial object, malformed time,
prohibited identifier, and custody-present cases all refuse. The exact
eight-line grammar prevents result-responsive prose or a narrowing of actual
custody absence.

v2.1.4 adds exactly two schema keys:
`result_manifest_sha256_or_null` to `t-operation-quarantine.v1` and
`diagnostic_conditions` to `t-replacement-invalidation.v1`. It adds no schema,
object, path, enum token, command, event, signed constant, resource value,
root, T band, import, or author token. The new fields are respectively a
mechanically observed metadata hash-or-null and a sorted array over the
already-closed I1–I7 token set.

The correction's §V214.8.3 reconciliation table is itself mislabeled: it maps
Sol C2 to replacement states rather than orphan-manifest custody, shifts M2/M3,
calls M4 “m2”, omits m1, and calls seven Sol repairs six rows. This does not
change executable rules but is an exactness defect (new m2).

## Trace 8 — no regression

| Surface | Independent result |
|---|---|
| Acyclic disposition | Preserved; all forward hashes reproduce |
| Complete custody | L1 source, L2 closed control set, L3 promoted, L4 temp grammar, L5 unknown-name scan and P1–P7 paired absence all preserved |
| Rejected-evidence fallback | Supervisor fallback remains disjoint from watchdog namespace, validates supervisor identity, handles historical-unknown/current-zero, and is consumed in pinned order |
| Replacement witness | Swap-only record remains non-evidence; deadline witness/fallback and replacement records cannot settle |
| Result manifest | Sole-pass tuples, immutable manifest, settlement/quarantine binding, empty/quarantined terminals, and no-content-reread rule preserved; selector ambiguity is new M1 |
| FD remap | Both crossing cases `(3,4)`/`(4,3)`, overlaps/outside targets, temporary duplication ≥5, inheritability/CLOEXEC normalization, direction/pipe checks, forbidden-fd closure, self-stop, post-resume recheck, exec, and all-step cleanup preserved |
| B1 acknowledgement | Null/exact/wrong/stale priority, published frontier, CLIENT_ECHO, successor ack, prefix-first classification, bounds, and all eight commands preserved |
| C1 evidence authority | Watchdog freezes/witnesses only; supervisor validates and is sole settlement/valid-terminal authority; UNKNOWN fallback remains fail-closed |
| D1 | Supervisor has no idle exit; bootstrap helper deadlock fixed, but resource-cut automaton is incomplete (M2) |
| K1 | Five constants fixed; one write/one hash; `bytes_reserved` until complete absence and disposition; no replenishment at any intermediate state |
| Nine signed events / E1-E2-E3 | Unchanged |
| Generic harness v2.3.1 | F1–F4/R1–R4 and §D1 head/cache and §D2 inline meter evidence carried unchanged |
| Batch settlement v1.1.1 | All-live settlement, `ARCHIVE` before `RESOLVED`, fixed arithmetic, and token order unchanged |
| Scientific/Q/C boundary | Every new object and residual is control-plane, `scientific_outcome:false`, archival-excluded, T-only, and permanently non-citable |

## New findings

### Critical

None.

### Major

#### M1. The three disposition branches overlap the mandatory both-terminal refusal

Locus: v2.1.4 §V214.2.3, the B-P/B-QM/B-QN selector and its immediately
following `REFUSE` list.

`B-P` is stated as `SETTLEMENT.json durable ⇒ settled branch`; B-QM and B-QN
are stated from quarantine presence and the nullable hash alone. None requires
the opposite terminal to be absent. Thus a layout containing both settlement
and quarantine satisfies B-P and one Q branch. The same block expressly says
that exact layout is an impossible state that must record invalidity and
release nothing. “Selection in this order” would select B-P; the REFUSE clause
would refuse. The contract therefore has two continuations and can release or
retain capacity according to implementer choice.

Smallest bounded repair: test `both terminal records durable` first and route
only to record-first invalidity/refusal. Then define B-P as settlement present
**and quarantine absent**, B-QM/B-QN as quarantine present **and settlement
absent**, and retain the neither/absence/hash-mismatch refusals. Re-run the
three-branch truth table. No author choice is needed.

#### M2. Bootstrap construction and failure cleanup do not cover ordinary resource cuts

Loci: v2.1.4 §V214.1.1's four creations and `fpathconf` check; inherited
§U2.2 c2–c4; inherited §U2.3 m7; §V214.1.2's normal-only close table; and
§V214.1.5's stage routes.

c2 installs `SPAWNING.json` before c3 creates and verifies four pipe pairs.
Failure on the second/later `pipe2`, or on any `fpathconf`, can therefore leave
a prefix of open channel descriptors and the singleton record, but the text
only says “no spawn attempt” and returns a refusal. It does not say which
descriptors close or invoke §U6.3. `os.fork` failure at c4 has no branch at
all. The second `os.fork` at m7 likewise has no specified `_exit(3)` route.
Finally, stage-1/2 helper failures name kill/record/lock cleanup but the
descriptor table closes CLI ends only on their normal c8/c12/c13/c16 points;
it never pins closure of all still-owned bootstrap fds on the failure path.

These are resource events, not deliberate A3 interference. Relying on an
uncaught language exception or eventual process exit leaves lifecycle and fd
retention to the implementer and can accumulate leaked descriptors or a live
`SPAWNING` conflict in a long-lived caller.

Smallest bounded repair: define one idempotent bootstrap-fd cleanup over every
successfully created end and invoke it on every CLI refusal/failure path;
after c2, remove all singleton records in §U6.3 order under the held lock.
Pin c3 partial-creation and `fpathconf` failures to that route, c4 fork failure
to stage 0 with no kill, and m7 fork failure to middle `_exit(3)` so c13 sees
EOF and takes stage 2. State close-error handling and re-run every creation,
fork, helper, and cleanup crash prefix. No new constant or author cell is
needed.

### Minor

#### m1. The derived grandchild bound is total but not proved sufficient for every healthy launch

Loci: v2.1.4 §V214.1.1 “Grandchild gate bound”; inherited §U2.4 c14/c15.

The proof budgets at most c13's 10-second read and then asserts c14 kernel
verification plus c15's durable no-replace install fit inside the remaining
10 seconds. Neither c14 nor c15, including file and parent-directory fsync,
has a duration bound. The 20-second gate is a sound anti-wedge policy, but the
claim that it is mathematically sufficient for every healthy launch does not
follow. A slow otherwise-valid install can make g0 exit before c16; the
attempt then fails closed rather than wedging.

Smallest repair: delete the universal sufficiency assertion and state that
expiry is a permitted bootstrap refusal, or give c14/c15 an executable bound
inside the same derived deadline without introducing a tunable.

#### m2. The v2.1.3 finding reconciliation table misidentifies the repaired findings

Locus: v2.1.4 §V214.8.3, “The six v2.1.3 rows”.

The actual mapping is C1→§V214.1, C2→§V214.2, M1→§V214.3,
M2→§V214.4, M3→§V214.5, M4→§V214.6, and m1→§V214.7. The table instead maps
C2 to replacement states, shifts M2/M3, labels M4 as m2, omits m1, and calls
the seven repairs six rows. The replacement index and operative sections are
clear, so this is non-executable provenance error only.

Smallest repair: replace that table with the seven-row mapping above.

## No-regression summary by signed cell

| Signed cell | Result |
|---|---|
| **A3** | Not reopened. The correction removes an overclaim and keeps all same-UID residuals procedural and non-citable. |
| **B1** | Not reopened. GC occurs only after durable acknowledgement and keeps permanent prefix authority; all eight command effects remain exactly once and retry stable. |
| **C1** | Not reopened. Dedicated watchdog remains freezer/witness only; supervisor remains sole writer and settler. |
| **D1** | Policy unchanged. No idle exit is introduced; new M2 is a bootstrap construction-totality defect, not an alternative lifetime choice. |
| **K1** | Policy unchanged. Constants, fixed ceiling, literal counts, full-reservation accounting, complete-custody release, and no-replenishment rule remain. New M1 makes one invalid-layout continuation ambiguous and must be repaired. |
| **Inherited signed surfaces** | Generic harness and batch settlement remain byte-identical and no event/resource/scientific/Q/C surface moves. |

## Author-cell determination

No genuinely new author cell is required. The branch predicates, bootstrap
cleanup, bound wording, and finding labels can all be repaired mechanically
without choosing a scientific fact, resource quantity, invalidity meaning,
custody destination, lifecycle policy, or new token. A3/B1/C1/D1/K1 remain
the complete signed policy basis.

## Authorization boundary

Because the verdict is `REVISE`, Kirill's informed signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is **unavailable**. The repaired bytes require another bounded independent X/Y
check. This review authorizes no implementation, code/test edit, commit, T
activation, entropy, runtime construction, supervisor, controller, worker,
watchdog, adapter, endpoint, pipe, FIFO, journal, spawn record, result
manifest, capacity or custody artifact, author decision file, E1/E2/E3 spend,
Q/C work, or scientific work.

## Static custody and programme state

This was a static review. No repository code, test, probe, smoke, supervisor,
controller, worker, watchdog, adapter, endpoint, or other Officina process ran.
Only read-only file display, Git ancestry/status, SHA-256, and permitted
literal-example hashing/arithmetic were used. No existing file or runtime
state was changed; exactly this review file was created. No runtime, T/Q/C,
capacity, custody, result-manifest, entropy, or scientific artifact was
created. The pre-existing modified and untracked workspace paths were
preserved.

`successor/officina/runtime/` still contains only `T_RUNTIME.lock`,
`successor/officina/runtime_control/` remains absent, and
`successor/officina/T_ENVELOPE.json` remains unactivated. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
