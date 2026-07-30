REVISE_OFFICINA_SUPERVISOR_V2_1_3

# Independent clean-context Y-line review

Date: 2026-07-30

Reviewer line: Y

## Review base, method, and recomputed hashes

Review base:
`20fd2129406d4144be76e79a955f27a62ed418ba`, verified to descend from
required commit `45f30f6`.

I read the complete v2/v2.1/v2.1.1/v2.1.2/v2.1.3 supervisor chain,
both signed author selections, the inherited generic-harness and
batch-settlement corrections, and both independent v2.1.2 reviews in
full. I treated
`reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md`
as an untrusted author self-assessment; none of its claims is evidence
for this review.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
22e2fb392c5758d7bab6840cafd711a9e4fa74b19b60bd5b05aebbde9b66c878  reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
aa25b28cedd813fbd2da36e0087cc9773be86b21a96c828bde57778953933dc7  reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
1ba2f792c4db272669282de589cc8176a37e3ddff3ed263c10575bd234ff91e8  reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md
```

The v2.1.3 correction digest exactly matches the expected
`72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888`.

This was a static review. I ran no repository code, test, probe,
supervisor, controller, worker, watchdog, adapter, endpoint, smoke, or
other Officina process. I used only read-only file-display, Git, and
SHA-256 utilities, including the expressly permitted hashing of
documented literal examples. I changed no existing file and created
only this review.

## Answer

No. v2.1.3 carries forward the independently closed acyclic authority,
complete protocol custody set, fallback namespace, fd remap,
acknowledgement priority, absent defaults, canonical empty hash, and
literal K1 write/hash counts. It also supplies the intended repairs for
the pre-`setsid()` group claim, swap-only witness collision, GC order,
durable result metadata, timestamp binding, singleton records, proof
summary, and A3 residual list.

The resulting text is nevertheless not total:

1. `boot_pipe` is created blocking, while c9 and c13 claim a bounded
   nonblocking poll. If the middle child dies after forking the
   grandchild but before the second report, the grandchild retains the
   boot write end while waiting for rel3 and the CLI blocks forever in
   c13. The stated timeout cannot execute.
2. A crash after `RESULT_MANIFEST.json` but before `SETTLEMENT.json`
   deliberately creates a quarantined orphan manifest, but verifier V2
   requires that manifest's hash to equal a nonexistent settlement
   field. V6 exempts only quarantines with **no** manifest. The one
   legitimate author custody-absence authority is impossible for this
   ordinary crash state, permanently retaining `bytes_reserved`.
3. GC deletes `accepted.json` first, then requires a later epoch to
   re-prove the command-specific G3 predicate. The remaining phase
   files do not contain the command/effect plan and cannot identify the
   owning archival predicate.
4. Spawn singleton preflight is specified both “under `SPAWN.lock`”
   and before acquiring that lock.
5. The swap state machine has no deterministic priority among
   simultaneously true I1–I7 conditions, treats “an ack of any
   table_seq” as defeating I2 even when the exact current table was
   never acked, and leaves the S1-true/S2-false non-I3 state outside its
   claimed partition.
6. A3-R1 says a during-pass modification still leaves a hash that
   describes the promoted bytes. A concurrent equal-size overwrite can
   instead produce a mixed read stream that never equals the final
   promoted inode. The hash describes the bytes read, not necessarily
   the promoted bytes.

These defects can wedge spawn, GC, watchdog progress, or K1 release
under histories the correction itself admits. The signature token must
remain unavailable. No new scientific/resource choice or author cell
is required; all repairs are mechanical.

## One-to-one disposition of the v2.1.2 Y-line findings

| Finding | v2.1.3 disposition | Independent result |
|---|---|---|
| **C1** pre-`setsid()` group identity / unrecorded middle holder | **Not fully closed** | §U2 correctly separates `SPAWNING_MIDDLE` from the verified group and gates both forks, but the blocking boot read makes c13's admitted middle-death cut unbounded (new C1). |
| **C2** unreachable/dual-valued watchdog replacement | **Not fully closed** | §U3 correctly suppresses deadline witnesses for swap-only freezes and adds `ACK_PENDING`, but its state and invalid-condition selection are not total (M3). |
| **M1** crash-mid-GC after early ack deletion | **Not closed** | `ack.json` is now last, but deleting `accepted.json` first destroys the information needed to re-prove G3 after a crash (M1). |
| **M2** missing durable per-file result metadata | **Not fully closed** | The manifest closes the promoted path and reproduces all hashes, but the explicitly admitted orphan-manifest quarantine cannot pass V2/V6 and can never dispose (C2). |
| **M3** singleton conflicts/removal incomplete | **Not fully closed** | All four records and ordered cleanup are stated, but preflight is ordered both before and under the lock (M2). |
| **M4** `signed_utc` unbound from `authorized_utc` | **Closed** | §U7.1 adds exact byte equality; the parser and real-date checks are fixed. |
| **m1** non-canonical `custody_locations_proved` | **Closed** | §U8 uses a fixed five-token class array, fixed roots, and canonical enumeration hashes without narrowing P1–P7. |
| **m2** incomplete post-pass A3 residual | **Not fully closed** | Before/during/after-pass and directory-swap windows are named, but A3-R1 still falsely says a during-pass hash describes the promoted bytes (M4). |

## New findings

### Critical

#### C1. The supposedly bounded boot reports use a blocking descriptor

Loci: v2.1.3 §U2.1 `boot_pipe = os.pipe2(0)`, §U2.4 c9 and c13
(`nonblocking poll`), §U2.6 row “after m7, before m8,” and test rows
101/105.

`boot_pipe` has no `O_NONBLOCK`, and no later step sets its read end
nonblocking. `os.read` therefore blocks; a loop cadence and deadline
cannot be checked while it is blocked. The ordinary admitted cut is:

```text
m7 forks grandchild
grandchild blocks at g0 and retains boot-write
middle child dies before m8's bootstrap report
CLI calls blocking read at c13
```

The pipe cannot reach EOF because the grandchild still owns a write end.
The grandchild cannot proceed because the CLI has not written rel3.
The CLI cannot reach its timeout or stage-2 `killpg`. The fork-shared
lock is retained indefinitely.

The same exactness gap exists in m0/m5: their `O_NONBLOCK` `os.read`
loops do not state the normal `EAGAIN`/`BlockingIOError` continuation,
and c8/c12/c16 do not state `EPIPE`/write-error routes after a child
dies between validation and release.

Smallest bounded repair: create `boot_pipe` with `os.O_NONBLOCK` on
the CLI read end (or set that end nonblocking before c9); explicitly
pin `EAGAIN` to paced retry, EOF to the applicable failure route, and
every other read error to fail-closed cleanup for c9/c13 and m0/m5.
Pin `EPIPE`/other write errors at c8/c12/c16 to the corresponding
stage route. Re-run every cut with the descriptor ownership table.

#### C2. An orphan-manifest quarantine can never satisfy the disposition verifier

Loci: v2.1.3 §U5.2's crash-after-manifest row, §U5.4 V2–V6, §U5.5,
and test row 117.

The correction intentionally makes this ordinary crash state:

```text
RESULT_MANIFEST.json durable
SETTLEMENT.json absent
terminal = QUARANTINED / SUPERVISOR_CRASH
manifest retained forever
```

V2 nevertheless requires the manifest bytes to hash to
`SETTLEMENT.json.result_manifest_sha256`. No settlement exists.
V6 makes V1–V4 vacuous only for a quarantined terminal **with no
manifest**. Thus a quarantine with the admitted orphan manifest has no
valid branch: V2 cannot pass and V6 cannot apply. Even after every
custody location is absent and the author signs the exact decision, no
`.disposed.json` can be installed and `bytes_reserved` remains
accounted forever.

This is not harmless retention: it makes the signed K1
custody-absence release authority impossible for a normal crash cut and
can eventually wedge the aggregate envelope.

Smallest bounded repair: bind
`result_manifest_sha256_or_null` in `QUARANTINE.json` (hash when an
orphan manifest exists, null otherwise), then define V1–V6 separately
for `PROMOTED`, `QUARANTINED+manifest`, and
`QUARANTINED+no-manifest`. The middle branch must validate and bind the
orphan manifest without a settlement, use its identifiers for the
content-prohibition check, and never reread output bytes.

### Major

#### M1. GC loses the authority required to re-prove G3

Loci: v2.1.3 §U4.1 D0–D3 and §U4.2's first three crash rows;
carried §N8.2; the immutable journal schemas in v2.1 §W1.3 /
v2.1.1 §Z10.3.

`accepted.json` is the phase that records `command`, `effect_plan`,
process/lease bindings, and argument identity. The command-specific G3
rules need those facts—for example the heartbeat charge, close/pause
archive set, admit terminal/charge, or STATUS form.

After D1, only `committed`, `reply`, and `ack` remain. None stores the
command or effect plan. A crash before D2 therefore leaves `ack.json`
so G1 holds, but a later epoch cannot determine which §N8.2 G3
predicate to re-check. The assertion “G1 still holds ⇒ re-verify
G1–G3” is not executable.

Smallest bounded repair: either install a durable immutable
`GC_ELIGIBLE.json` binding the command, exact G3 proof identities, ack,
prefix, and archival commit before D1, and delete it last; or retain
`accepted.json` until all other semantic phases are gone and add an
exact prefix-only completion rule for the final
`accepted+ack`/`ack-only` states. Re-prove every deletion prefix using
only the files actually present.

#### M2. Singleton preflight is simultaneously before and under the lock

Loci: v2.1.3 §U2.2 c1 and §U6.1 opening sentence.

§U6.1 requires the mutating P3 removal scan “under `SPAWN.lock`,
before c2.” c1 instead orders “§U6.1 singleton preflight, **then
acquire** `SPAWN.lock`.” An implementation following c1 can inspect or
remove records concurrently with the current lock holder; one following
§U6.1 must reverse c1. The singleton lifecycle therefore has two
incompatible lock orders.

Smallest bounded repair: c1 must acquire the lock first (or take the
bounded stuck-holder route), then run §U6.1 under that acquired lock,
then c2. No P3 removal or P2 adoption may occur before acquisition.

#### M3. The watchdog replacement partition and invalid marker are not total

Loci: v2.1.3 §U3.2 I1–I7/S1–S2/`ACK_PENDING`, §U3.3's singular
`invalid_condition`, and §U3.4.

Three independent gaps remain:

1. Multiple I conditions can be true in one locked observation
   (deadline passed, ack absent, and a member dead). The marker stores
   one `invalid_condition`, but no lowest-number/other priority is
   specified.
2. I2 fires on “no ack of **any** table_seq.” A stale/wrong table ack
   makes that phrase false while S1 still fails because the exact
   current table was not acked. The claimed absence-timeout bound then
   need not fire.
3. `ACK_PENDING` is defined as not-invalid with S1 unsatisfied. If S1
   is satisfied but S2 is false because a member is running before a
   resume marker, I3 does not expressly apply: “running” is
   classifiable, but it is neither absent, Z, mismatched, nor T. The
   state is neither `INVALID`, `RESUMABLE`, nor the defined
   `ACK_PENDING`.

Smallest bounded repair: test I1→I7 in an explicitly pinned priority
and record the first true condition; make I2 “no valid ack of the exact
current table_seq by the absence bound” (wrong/stale/malformed never
satisfies it); and make I3 include every pre-resume member state other
than `T` after identity match. Then define `ACK_PENDING` as the exact
remaining state and reproduce the deadline/ack race table.

#### M4. The during-pass A3 statement still claims a promoted-byte hash

Loci: v2.1.3 §U1.1, §U1.2 during-pass row, and §U1.3 A3-R1.

§U1.1 correctly says the hash describes the byte stream read during the
pass and makes no later-instant claim. A3-R1 then contradicts it:

```text
the recorded hash still truthfully describes the promoted bytes
```

During a concurrent same-inode equal-size overwrite, successive
`pread` chunks may come from different content states. The resulting
hash can describe a mixed stream that never existed as the final file
and does not equal the bytes later renamed into promotion. Length and
EOF checks can still pass.

Smallest bounded repair: split the completed-before-pass and
concurrent-during-pass cases. In all cases claim only that the hash
describes the exact read stream. State explicitly that during-pass and
post-pass A3 changes can make `result_sha256` differ from the promoted
bytes and that this is unobservable, procedural, non-citable, and has
no `HASH` route.

### Minor

#### m1. The signed timestamp line's documented byte count is off by one

Locus: v2.1.3 §U7.3.

The literal line

```text
signed_utc: 2026-07-30T00:00:00.000000000Z\n
```

is **43 bytes**, not the documented 44: 10-byte key + colon + space +
30-byte timestamp + LF. The equality rule and the earlier 504-byte
decision-file hash remain correct.

Smallest bounded repair: change only “44 bytes incl. LF” to
“43 bytes incl. LF.”

## Trace 1 — A3/K1 write/hash and residual windows

For each nonempty output frame:

1. Header grammar, uniqueness, path/depth/count limits, strict positive
   `content_bytes`, and reservation arithmetic are checked before
   creation.
2. The supervisor opens write `w` and held read `r`.
3. Exactly `content_bytes` are written once, with integer counters
   only; no hash object exists.
4. EOF, status counts, and group death are checked.
5. The sole pass re-resolves `v`, verifies device/inode/link/size,
   then hashes every content byte exactly once.
6. The in-memory `{relative_path, byte_length, content_sha256}` tuples
   feed metadata hashes only. Manifest, settlement, rename, status,
   delivery, capacity, and custody paths never read content.

| Window/anomaly | Mechanical result |
|---|---|
| Bad grammar/count/ceiling before frame | No file/frame byte; transport/quarantine route. |
| Inode replacement | Device/inode mismatch ⇒ `HASH`. |
| Hardlink | `st_nlink != 1` ⇒ `HASH`. |
| Truncate/extend, wrong read length/EOF | Size/length/EOF mismatch ⇒ `HASH`. |
| Equal-size same-inode change completed before pass | Undetected; sole hash describes modified bytes read. |
| Equal-size same-inode change during pass | Undetected if length/EOF stable; hash describes the read stream, **not necessarily the promoted bytes** (M4). |
| Change after pass before settlement/rename | Undetected; no future-immutability claim is legal. |
| Directory name swap before `os.replace` | Undetected A3-R3. |
| Crash before/during/after pass, pre-settlement | `SUPERVISOR_CRASH`; no resume/respawn/promotion. |

All undetectable windows are same-UID A3 procedural,
T-development-only, permanently non-citable, and have no scientific or
validity meaning. Literal K1 counts remain one write/one hash.

## Trace 2 — spawn/bootstrap cuts

| Cut | Identity/gate | Required continuation | Result |
|---|---|---|---|
| Before c1 | none | acquire bounded | Correct. |
| c1/c2 | `SPAWNING` | preflight under held lock | **Contradictory order (M2).** |
| c4→c7 | m0 rel1 gate; no record | EOF/EAGAIN/bound ⇒ exit | Concept sound, but EAGAIN is not pinned (C1). |
| after c7 | `SPAWNING_MIDDLE` | pre-group `kill(pid)` only | Correct. |
| after rel1 | m2 `setsid`, m3 kernel self-check | report only after true SID/PGID | Correct. |
| c9/c10 | group report | bounded boot read and kernel verify | **Boot fd is blocking (C1).** |
| after c11 | verified `SPAWNING_GROUP` | post-group `killpg` only | Correct. |
| m5 | rel2 gate | bounded EAGAIN/EOF handling | EAGAIN branch unstated (C1). |
| m7→m8 | grandchild g0; middle reporting | c13 bounded report | **Ordinary middle death deadlocks blocking c13 (C1).** |
| c15 | `SPAWNING_CHILD` | child identity before rel3 | Correct. |
| g0 | blocking rel3; CLI sole writer | EOF on CLI death, byte on release | Correct; middle closed rel3 write before fork. |
| g1/g2 | child record durable | scrub, endpoints, watchdog, bounded first ack | Correct. |
| first-ack failure | child/group records | kill watchdog/group; ordered cleanup | Correct modulo unspecified release-write errors. |
| identity install/g3 | lock retained | identity durable; child→group→middle→spawning removal; close | Correct. |
| PID reuse | tier start mismatch | never kill | Correct. |
| stale/malformed/conflicting singleton | P1/P2/P3 | refuse/adopt/remove exactly | Correct after M2's lock order is fixed. |
| stuck holder | s1→s5 | child, verified group, then middle-only kill | Correct; deliberately stopped unrecorded m0/CLI remain named A3 residuals. |

The two middle gates and grandchild gate repair the false PGID claim,
but the blocking report channel leaves an ordinary lock-holding
deadlock, so spawn is not total.

## Trace 3 — C1 replacement state machine

| State/cut | Derived continuation |
|---|---|
| Watchdog death, group already overdue | §W3.3 witness/fallback; invalid all-live route. |
| Non-overdue classification | Swap-only stop; no witness/fallback; `REPLACEMENT_FREEZE` only. |
| Record before replacement ack | `ACK_PENDING`; group stays T. |
| Exact current ack, all members T, no I condition | `.resumed.json` before `SIGCONT`; idempotent resume. |
| Deadline wins ack race | I1 invalid marker, then signed invalid route. |
| Exact-ack absence bound wins | Intended I2 invalid route. |
| Crash after resume marker | Relaxed T/running check, reissue `SIGCONT`. |
| Crash after invalid marker | Resume invalid automaton without reclassification. |
| Supervisor loss | I7/phase 2A; never resume across generations. |
| Witness/fallback appears | I4 invalid route. |
| Multiple I facts | **No singular marker priority (M3).** |
| Stale/wrong ack but no exact ack | **I2 says “any table_seq”; bound can fail (M3).** |
| S1 true, member running before resume marker | **No stated partition branch (M3).** |

I-before-S correctly makes equality/overdue dominate a simultaneous
valid ack, and the watchdog still cannot settle or select a terminal.
The fallback/witness authority remains supervisor-only at settlement.
The three-state partition needs M3's exact repair.

## Trace 4 — B1/GC across all eight commands

`N(i)` is explicit `NEW`; `R(i)` explicit `RETRY`. Prefix-first
classification and the frontier rules carry unchanged.

| Command | Exactly-once/retry-stable effect | G3 authority |
|---|---|---|
| `CLAIM` | one sequence/claim; retry cached | process terminal archival commit |
| `START` | one event/lease; retry cached | process terminal archive |
| `HEARTBEAT` | one recorded cursor/charge; retry never samples | archive covering charge |
| `CLOSE` | one close automaton; own terminal cannot self-ack | close archive |
| `PAUSE` | one checkpoint/pause; own terminal excluded | pause archive |
| `RESUME` | one pinned checkpoint automaton | resume archive or exact no-event predicate |
| `OPERATION_ADMIT` | one operation/reservation/worker | terminal plus settling-charge archive |
| `OPERATION_STATUS` | each observation `NEW` cached; `RETRY` byte-stable; ack form writes once | observation vacuous; ack form delivery+terminal |

Shared traces:

| Attack/cut | Result |
|---|---|
| Null ack hash | No ack; classify. |
| Exact frontier + `N(m+1)` | `SUCCESSOR_OCCURRENCE` before allocation. |
| Exact frontier + `R(m)` | `CLIENT_ECHO`; prefix-first `ALREADY_ACKNOWLEDGED`. |
| Wrong/stale/no-frontier non-null hash | `INVALID/REPLAY_BYTES`; no state movement. |
| Lost request | Re-send `N` if unallocated; `R` never allocates. |
| Lost reply / generation change | `R` returns cached effect in current envelope. |
| Concurrent `NEW` | Lock serializes; loser re-anchors. |
| Non-contiguous supervisor ack | Prefix stops at first gap; frontier drains it. |
| Ack before archive | Prefix advances; files retained until G3. |
| Retry before/during/after GC | Prefix-first identical `ALREADY_ACKNOWLEDGED`. |
| D0→D1 crash | all files; reverify. |
| D1 crash | accepted gone; other three present | **G3 command/effect identity unavailable (M1).** |
| D2/D3 crash | still lacks accepted | Same defect, despite ack present. |
| D5 crash | empty directory | Prefix-only empty-directory completion is sound. |
| Post-GC replay | Prefix refusal; no reducer/effect. |
| 64 unacked | `UNRESOLVED_JOURNAL`; frontier drain remains. |

B1 application and owed-reply semantics remain correct. The physical
retention proof is not executable at the D1–D4 prefixes.

## Trace 5 — result manifest and complete K1 custody

### Forward manifest construction

The sole pass produces in-memory sorted tuples. They generate:

```text
entries canonical length: 265 bytes
result_sha256:
5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3

RESULT_MANIFEST canonical length: 638 bytes
result_manifest_sha256:
e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed
```

Both documented hashes reproduce exactly. The empty entries array
reproduces:

```text
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

The normal promoted DAG is forward and total:

```text
sole pass tuples → entries/result_sha256
                 → manifest bytes/result_manifest_sha256
                 → settlement → rename/token/verifier
```

### Custody/accounting trace

| Phase | Custody / metadata | Accounted |
|---|---|---|
| Reservation/live/pending | L1 source | `bytes_reserved` |
| Successful pass | in-memory tuples, then manifest | `bytes_reserved` |
| Normal settlement/pre-rename | manifest+settlement; L1 | `bytes_reserved` |
| Promotion | L1→L3 atomic rename | `bytes_reserved` |
| Quarantine before pass/manifest | L1, no manifest | `bytes_reserved`; V6 legal |
| Crash after manifest/pre-settlement | L1, orphan manifest, quarantine | `bytes_reserved`; **disposition impossible under V2/V6 (C2)** |
| Delivery ack | L3 unchanged | `bytes_reserved` |
| Temp/unknown op-name | L4/L5 | `bytes_reserved`; refuse |
| Author removes all custody | P1–P7 paired proof | still reserved until disposition+disposed |
| Disposed | all classes absent, authority verifies | release exactly `bytes_reserved` once |

`actual_bytes` never reduces accounting. The L2 allowed set correctly
includes `RESULT_MANIFEST.json`; proof summaries cannot replace P1–P7.
The orphan-manifest branch must be repaired for complete K1 release.

## Trace 6 — spawn-record lifecycle

The four singleton records are
`SPAWNING`, `SPAWNING_MIDDLE`, `SPAWNING_GROUP`, and
`SPAWNING_CHILD`.

| Preflight/install case | Required result |
|---|---|
| Absent | Install. |
| Malformed/nonregular/symlink/nlink | Nonretryable `BOOTSTRAP`; no unlink/kill. |
| Same live attempt, byte-identical | Adopt. |
| Same id, different bytes | Retryable conflict; no unlink/kill. |
| Different live attempt | Retryable conflict; aged kill only through s2–s4. |
| PID absent | Prove; ordered cleanup; continue. |
| Matching zombie | Prove/reap if own; cleanup. |
| PID reused | Never kill; treat stale; cleanup. |
| `EEXIST` P3 | Cleanup, retry once; second collision refuses. |
| Crash mid-cleanup | Resume child→group→middle→spawning, `ENOENT` tolerant. |
| Takeover | Same discipline; no runtime/journal/capacity/output unlink. |

This table is deterministic, but only after acquiring `SPAWN.lock`.
The c1/§U6.1 order conflict (M2) must be removed.

## Trace 7 — author authority and proof summary

The inherited forward authority reproduces:

```text
disposition preimage: 396 bytes
disposition_id:
e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

eight-line decision file: 504 bytes
author_decision_sha256:
0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f
```

Path → id → exact decision bytes → file hash → disposition object →
disposed record remains acyclic. Extra content, wrong path/id,
cross-operation substitution, stale activation/generation, wrong
terminal/parent, partial object, replay, and custody-present cases all
refuse. The decision file cannot add result-responsive prose.

§U7 binds `authorized_utc` to line-8 `signed_utc` byte-for-byte. The
timestamp is canonical and real-date checked. Its illustrative line is
43 bytes including LF (m1), while the value compared is correctly 30
bytes.

The proof-class array and roots are fixed. The documented operation
directory enumeration reproduces:

```text
3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc
```

An empty enumeration reproduces the canonical empty hash above. The
summary is diagnostic and cannot narrow actual custody absence.

## Trace 8 — no regression and exactness

| Surface | Result |
|---|---|
| Acyclic disposition | Preserved; literal hashes reproduce. |
| Complete custody L1–L5/P1–P7 | Preserved, including manifest in L2; C2 blocks one legitimate terminal's verifier, not the physical absence proof. |
| Fallback witness | Preserved: immutable rejected object, disjoint supervisor fallback, historical/current separation. |
| FD remap | Preserved across `(3,4)`, `(4,3)`, overlaps, outside targets, failure cleanup, inheritance, directions, self-stop, and `execv`. |
| Ack priority | Preserved: null/exact/wrong/stale cases disjoint and pre-allocation. |
| Absent defaults | next=1, prefix=0. |
| Canonical empty result | `SHA-256(b"[]\n")` reproduced. |
| **A3** | Before/during/after-pass and directory-swap residuals named and non-citable; M4 removes the remaining promoted-byte overclaim. |
| **B1** | Exactly-once/retry-stable/generation-total effects preserved for all eight; M1 affects GC completion/retention. |
| **C1** | Watchdog remains witness/freezer only and supervisor solely settles; M3 leaves replacement state/marker selection non-total. |
| **D1** | No idle exit; C1 leaves an ordinary bootstrap lock deadlock. |
| **K1** | Five constants and no-replenishment preserved; one write/one hash preserved; C2 makes complete-absence release impossible for an admitted quarantine state. |
| Scientific/resource fields | No signed value moved; manifest and proof fields are mechanical. |
| Invalidity fields | Existing cause/terminal surfaces unchanged, but M3 leaves the new `invalid_condition` selection discretionary. |
| Generic harness v2.3.1 | Head/cache and inline meter-evidence corrections unchanged. |
| Batch amendment v1.1.1 | All-live settlement, `ARCHIVE` before `RESOLVED`, arithmetic, and two-token order unchanged. |
| Signed events/schemas/roots/T bands | No signed movement; added objects are control-plane only. |
| Q/C boundary | Every new object and residual remains T-development-only and permanently non-citable. |

No scientific, resource, or lifecycle choice is needed to repair these
bytes. The current text does leave invalid-condition choice and several
ordinary lifecycle cuts to implementer inference, so it cannot be
confirmed.

## Author cells

No genuinely new author cell is required. The smallest repairs are
mechanical:

- make the report channel actually nonblocking and totalize all pipe
  errno branches;
- bind orphan manifests in quarantined terminals and give them an exact
  verifier branch;
- retain or replace the G3 authority throughout GC;
- acquire `SPAWN.lock` before singleton preflight;
- totalize replacement-ack/state/invalid-condition priority;
- state that a during-pass hash describes only its read stream;
- correct one illustrative byte count.

The signed A3/B1/C1/D1/K1 cells already determine the policy.

## Authorization boundary

Because the verdict is `REVISE`, Kirill's informed signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable**.

The repaired bytes require another independent X/Y check. This review
authorizes no implementation, code/test edit, commit, T activation,
entropy, runtime construction, supervisor/controller/worker/watchdog/
adapter, endpoint, pipe, FIFO, journal, spawn record, result manifest,
capability, lease, batch, operation, capacity artifact, custody
disposition, promoted object, author decision file, world, learner,
candidate, Q attempt, Q/C object, datum, outcome, scientific work,
E1/E2/E3 spend, or claim movement.

## Static custody and programme state

No existing file was changed. Exactly this one new review file was
created. No repository code, test, probe, supervisor, controller,
worker, watchdog, adapter, endpoint, smoke, or Officina process ran.
No T/Q/C, runtime, capacity, custody, result-manifest, or scientific
artifact was created. All pre-existing dirty and untracked paths were
preserved.

Static inspection confirms `successor/officina/runtime/` contains only
`T_RUNTIME.lock`, `successor/officina/runtime_control/` is absent, and
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
T remains `NOT_ACTIVATED`. The programme claim remains `OPEN`.
