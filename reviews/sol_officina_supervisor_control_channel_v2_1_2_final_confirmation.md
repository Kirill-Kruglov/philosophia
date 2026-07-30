REVISE_OFFICINA_SUPERVISOR_V2_1_2

# Independent clean-context Y-line review

Date: 2026-07-30

Reviewer line: Y

## Review base, custody, and recomputed hashes

Review base: commit
`011aa2813a33463b4db397f3c52a86c445cd9ba9`, verified to descend from
required commit `9743d1f`.

I read the required correction chain, signatures, inherited harness/batch
corrections, and both v2.1.1 independent reviews in full. I treated
`reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md`
only as an untrusted author claim. None of its dispositions is evidence
for this review.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
640305647c9c03d44f40899bf2434c089afb5cbbbf8286e9673852aa795cc6b1  reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
b5b5614166488bc8dca0856bf6963d84bd701757df153acaf868212687a2d797  reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
be36dc8319567d301d19c131eb875655be07f5ec2f6a1f4015d561f5d1fa935e  reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md
```

The correction digest exactly matches the expected
`2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373`.

This was a static review. I ran no repository code, test, probe,
Officina command, supervisor, controller, worker, watchdog, adapter,
endpoint, or smoke. I used only read-only file-display, Git and SHA-256
utilities, plus SHA-256 of the documented literal examples. I altered no
existing file and created only this review.

## Answer

No. v2.1.2 correctly repairs the circular disposition identifier, the
one-name custody proof, literal K1 write-once/hash-once, the rejected
witness namespace, fd remapping, acknowledgement priority, absent-scope
defaults, and the canonical empty-result hash. It is nevertheless not
exact or total:

1. `SPAWNING_GROUP.json` records `middle_child_pid` as the process-group
   id before the middle child has necessarily executed `setsid()`.
   Parent and child run concurrently, so the asserted group may not
   exist when the kill route needs it; an unrecorded/stopped middle child
   can still retain the fork-shared lock.
2. The carried dead-watchdog rule creates a §W3.3 freeze observation for
   every group, while the new non-overdue resume rule requires that no
   freeze witness exist. Its happy path is therefore unreachable, and
   its general “any failed conjunct ⇒ invalidity” rule also contradicts
   its own pending-ack “hold frozen” row.
3. Later GC requires `ack.json` to remain durable, but the correction
   claims no deletion order is needed. A crash after deleting
   `ack.json` and before deleting the other phases leaves the remainder
   permanently ineligible for GC.
4. The authority verifier requires per-file content hashes “in
   `SETTLEMENT.json`,” and the test matrix says the result is
   reproducible from that object, but the carried exact
   `SETTLEMENT.json` schema contains neither the metadata list nor any
   per-file hash.
5. The exact eight-line author decision's `signed_utc` is not required
   to equal the disposition object's `authorized_utc`.
6. Singleton spawn-record no-replace conflicts and several failure-path
   removals are not totalized.

These are bounded mechanical repairs. No new scientific/resource choice
or author cell is required, but the current token must remain
unavailable.

## One-to-one disposition of the v2.1.1 Y-line findings

| Finding | v2.1.2 disposition | Independent result |
|---|---|---|
| **C1** circular custody-disposition id | **Closed** | §N1.1–§N1.3 gives a one-way dependency DAG. The path and id precede the decision bytes; the decision-file hash is a sink. |
| **C2** one-name rather than complete-custody proof | **Closed for protocol-created custody** | §N2.1–§N2.6 derives source/quarantine, operation-directory, promoted, temporary, and unknown operation-named locations and proves them under one lock. Minor record exactness remains below. |
| **C3** earliest supervisor identity / lock-holder cut | **Not closed** | §N3 gates the grandchild, but the first-fork middle child is not gated before `setsid()` and the record falsely treats its PID as an already-existing PGID. |
| **C4** output bytes hashed twice | **Closed** | §N4 deletes the inline hash; counters govern writes and one pre-settlement pass computes the sole content hash. |
| **M1** rejected witness cannot be replaced / zero-member `UNKNOWN` | **Closed at the fallback object level** | §N5.1–§N5.5 gives a disjoint fallback namespace and separates historical uncertainty from current membership. The new replacement-resume automaton has a separate Critical defect. |
| **M2** fd overlap/crossing | **Closed** | §N6 duplicates both sources outside `{3,4}` before either target is overwritten and verifies type, direction, inheritance, closure, and post-stop state. |
| **M3** wrong ack hash has two continuations | **Closed** | §N7.2 gives a disjoint pre-allocation priority rule: null, exact `NEW`, exact `RETRY`, and every mismatch each have one result. |
| **M4** ack-before-archival cannot later GC | **Not fully closed** | Later-epoch GC is now allowed and per-command archival predicates are stated, but crash-mid-GC is not physically completable if `ack.json` is removed first. |
| **M5** author file admits arbitrary scientific prose | **Closed** | §N1.4 is byte-exact and content-closed: exactly eight lines and no extra byte. |
| **m1** absent tombstone defaults implicit | **Closed** | §N9.1 fixes next=1 and prefix=0. |

## New findings

### Critical

#### C1. The first-fork record is not a valid process-group identity before `setsid()`

Loci: v2.1.2 §N3.2 c4–c5, §N3.3 m1–m3, §N3.5 c7/s3, and
§N3.6's cuts after c4.

After `pid_mid = os.fork()`, the CLI and middle child run concurrently.
The CLI's c5 record states:

```text
middle_child_pid is also the grandchild's pgid and session id
```

but the middle child does not become a session/process-group leader until
m2 calls `os.setsid()`. The parent has no ordering edge proving m2
preceded c5. There are two failing cuts:

- if c7 times out while the middle child is still before or failed at
  `setsid()`, `killpg(middle_child_pid, ...)` names a process group that
  need not exist;
- if the CLI dies after the first fork but before c5 while the middle
  child is stopped before m1/m2, the middle child still owns the
  fork-shared lock and the release-pipe write end. No grandchild exists
  to observe EOF, no group record exists, and a later client has no
  identity-safe kill handle.

The claim that `SPAWNING_GROUP.json` exists before the grandchild exists
is also not enforced: the middle child can execute m1–m3 before the CLI is
scheduled for c5.

This is not cured by the named “wedged CLI” residual; the problematic
holder is the middle child and the recorded group identity is false at
the relevant cut.

Smallest bounded repair: add a **middle-child gate**. The middle child
must report its pid/start identity, execute `setsid()`, report and allow
the CLI to verify `pgid == pid_mid`, then block on a CLI-controlled
release byte. Only after the CLI durably installs
`SPAWNING_GROUP.json` may the middle child fork the grandchild. Before
verified `setsid()`, failure kills the middle child by
`kill(pid_mid)` plus start identity, not `killpg`; after it, failure may
use the verified group. Pin both EOF and record-conflict routes.

#### C2. The non-overdue watchdog-replacement resume is unreachable and dual-valued

Loci: carried v2.1 §W3.5 line 831, extended—not replaced—by v2.1.2
§N5.6; §N5.6 R4, its general failure paragraph, and its first two crash
rows.

The carried dead-watchdog rule says the supervisor:

```text
freezes all live groups itself per §W3.3 with killer = SUPERVISOR
```

§W3.3 writes a `FREEZE/<witness_id>.json` observation for each such
freeze. The new resume predicate R4 requires:

```text
no freeze witness and no fallback exists for that process
```

Therefore every non-overdue group frozen through the carried rule has a
witness and fails R4. It is routed to invalidity rather than resumed.
The amendment says §W3.5 is only “extended,” so it never suppresses the
§W3.3 witness for a swap-only freeze.

There is a second contradiction. The normative paragraph says **any**
failed conjunct—including a missing or stale ack—takes the signed
invalid route. The crash table says a replacement record with no ack
must instead “hold frozen” until either ack or deadline. The same
non-overdue pending-ack state thus has two continuations.

This can manufacture process invalidity from a healthy, non-overdue
group during ordinary watchdog replacement, exactly the fail-closed
misclassification the prompt forbids.

Smallest bounded repair: explicitly replace the carried §W3.5 action for
non-overdue groups. A swap-only freeze writes
`REPLACEMENT_FREEZE`, **not** a §W3.3 deadline-freeze witness. Define
three states: `ACK_PENDING` (hold frozen until the bounded ack/deadline
race resolves), `RESUMABLE` (all R predicates pass), and `INVALID`
(deadline passed, definitive identity/member/evidence mismatch, watchdog
replacement failure, or unresolved invalidity). Only the last enters
the invalid route.

### Major

#### M1. Crash-mid-GC is not completable if `ack.json` is deleted first

Loci: v2.1.2 §N8.1 G1, §N8.3 consequence 2, §N8.4 crash cuts, and
§N11's crash-mid-GC row.

Every later GC epoch requires:

```text
G1. ack.json for i is durable and immutable
```

The correction simultaneously says any subset of the four phase files
may be missing, no deletion order is needed, and a later epoch completes
the deletion. If the first GC epoch deletes `ack.json` and crashes before
deleting `accepted`, `committed`, or `reply`, G1 can never again pass.
Prefix-first classification preserves exactly-once semantics, but the
remaining files are permanently non-GC-able, contradicting the claimed
bounded retention and idempotent completion.

Smallest bounded repair: require an exact deletion order with
`ack.json` **last**, or change later completion eligibility to the
never-deleted prefix plus a durable GC-intent/eligibility marker written
before deletion. Then prove each crash cut against that order.

#### M2. The new authority refers to durable per-file hashes that do not exist

Loci: v2.1.2 §N1.6 lines 327–336, §N4.3, and test obligation 90;
carried v2.1 §W6.1 lines 1269–1274.

§N1.6 says the supervisor checks:

```text
every content_sha256 in SETTLEMENT.json
```

and says it already holds those hashes durably. Test row 90 says
`result_sha256` is reproducible from `SETTLEMENT.json`. But the exact
carried schema is:

```text
schema, scientific_outcome, operation_id, charge_event_sha256,
result_sha256, promoted_relative_paths, bound_sha256, actual_bytes,
settled_utc
```

It contains no per-file `content_sha256`, no byte length per path, and
no canonical result-metadata list. Thus the required content check and
reproduction test are impossible from the named durable authority.
Two implementations must either retain undeclared in-memory state,
re-read output (violating hash-once), or silently skip the check.

Smallest bounded repair: add one immutable, exact result-manifest object
containing the sorted `{relative_path, byte_length, content_sha256}`
tuples and bind its SHA-256 in `SETTLEMENT.json`, or extend the
settlement schema with that exact tuple list. The disposition verifier
must resolve this durable manifest; no output byte may be re-read.

#### M3. Spawn-record conflicts and failure cleanup are incomplete

Loci: v2.1.2 §N3.2 c5, §N3.5 c9/c7, §N3.6 first-ack timeout,
§N10.1 removal actors, and inherited client takeover.

Both `SPAWNING_GROUP.json` and `SPAWNING_CHILD.json` are singleton
no-replace paths reused across attempts, but neither c5 nor c9 states an
`EEXIST` equality/conflict continuation. The c7 kill/refuse route unlinks
`SPAWNING_GROUP.json` and `SPAWNING.json` but omits
`SPAWNING_CHILD.json`. A grandchild dying after c9 can therefore leave a
stale child record that makes the next c9 collide. The carried client
takeover stale-endpoint list does not expressly add the new group record,
and §N10.1's removal-actor table does not supply the missing ordered
algorithm.

Smallest bounded repair: under `SPAWN.lock`, validate and remove all
dead `SPAWNING_CHILD`/`SPAWNING_GROUP` records before c2; at c5/c9,
define `EEXIST`: byte-identical live same-attempt record is idempotent,
dead/stale is removed only after proof, and conflicting live identity is
`BOOTSTRAP` with no unlink. Every death-proved failure route must unlink
child, group, and spawning records in child→group→spawning order.

#### M4. The decision file's signed timestamp is not bound to the disposition object

Loci: v2.1.2 §N1.4 line 8, §N1.5 object key list and conjunct 8d.

The exact decision file signs `signed_utc`, while the disposition object
contains `authorized_utc`. Conjunct 8d compares the token, activation
hash, operation id, disposition id, and destination, but omits the two
timestamps. The author can therefore sign one time while the object
asserts another, leaving `authorized_utc` outside the content-closed
authority.

Smallest bounded repair: require
`authorized_utc == decision_file.signed_utc` byte-for-byte, or use one
field name in both objects.

### Minor

#### m1. `custody_locations_proved` cannot literally list “exact L1–L5 strings”

Loci: v2.1.2 §N2.2, §N2.5, and test obligation 81.

L1–L3 are concrete paths, but L4 and L5 are grammars/sets (“every temp
name” and “any entry whose name contains operation_id”), not single exact
location strings. When no such entry exists there is no finite
operation-specific path to list as an observed absence. The field is
diagnostic and does not weaken the proof, but two implementations can
serialize different strings.

Smallest bounded repair: replace the list with a fixed closed enum of
proof classes `{SOURCE, OPERATION_DIRECTORY, PROMOTED, TEMP_GRAMMAR,
UNKNOWN_NAME_SCAN}` plus the two root hashes/enumeration hashes, or state
the five exact canonical grammar-description literals.

#### m2. The post-verification in-place modification residual is not named beside the directory swap

Locus: v2.1.2 §N4.2–§N4.4.

The sole hash detects substitutions present during its read, but a
deliberate same-UID process can modify the verified inode after the pass
and before `SETTLEMENT.json`/rename without changing size, inode, or link
count. The inherited A3 procedural residual covers this generally, so it
is not a mechanical K1 failure. The text nevertheless names only
same-name directory substitution at that cut while describing the
equal-size defence as fully retained.

Smallest bounded repair: name both the post-pass in-place-content window
and the directory-name swap as A3 procedural, non-citable residuals; do
not claim the pass proves future immutability.

## Trace 1 — acyclic authority

### Forward construction and reproduced hashes

For the documented synthetic activation hash `a`×64 and operation id
`b`×64:

1. Derived path:

```text
successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb_SIGNATURE.md
```

2. Canonical 396-byte id preimage:

```text
{"activation_record_sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","author_decision_path":"successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb_SIGNATURE.md","operation_id":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","schema":"philosophia.officina.t-output-custody-disposition-id.v1"}
```

with the trailing newline hashes to:

```text
e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd
```

3. The exact eight-line, 504-byte decision file hashes to:

```text
0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f
```

4. The disposition object is then installed at
`runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json`, binding
the decision path/hash, activation, operation, terminal, reservation,
actual bytes, custody parent, destination and author token.

5. Only after all authority and custody predicates pass does the
supervisor install `CAPACITY/<operation_id>.disposed.json`, binding the
exact disposition-object hash and releasing exactly `bytes_reserved`.

The graph is acyclic: path → id → decision bytes → decision hash →
disposition object → disposed record.

### Attack results

| Attack/cut | Result |
|---|---|
| Extra byte, prose, blank, CRLF, reordered/re-cased line | Exact eight-line parser refuses. |
| Wrong decision path or operation segment | Derived path and id recomputation refuse. |
| Wrong disposition id | Recompute/filename check refuses. |
| Decision for operation X used for Y | Path, operation line, id and object bindings refuse. |
| Stale activation or admission generation | Conjunct 3/5 refuses. |
| Wrong terminal or custody-parent hash | Durable terminal/parent check refuses. |
| Truncated decision/object | Exact schema/byte checks refuse; no disposed record. |
| Partial `.disposed` install | No durable disposed record means reservation remains; later retry revalidates. |
| Replay after durable disposed record | No-replace single use; releases nothing again. |
| Forged same-UID authority | Named A3 procedural residual, not a cryptographic claim. |
| Outcome-responsive extra text | Impossible under exact eight lines. |
| Variable control value equals a durable result/content identifier | Must refuse, but M2 supplies no durable per-file hash set as written. |
| `authorized_utc` differs from signed line 8 | **Accepted as written; M4.** |

## Trace 2 — complete K1 custody

| Phase/location | Custody | Accounted contribution |
|---|---|---|
| Admission reservation | Capacity record, no output yet | `bytes_reserved` |
| Live source output | L1 `operations/<op>/out/` | `bytes_reserved` |
| Pending settlement | L1 | `bytes_reserved` |
| Quarantine/failure | L1 remains the defined quarantine custody | `bytes_reserved` |
| Settlement before promotion rename | L1 present, L3 absent | `bytes_reserved`; P2/P3 refuse disposition |
| Atomic promotion rename | custody moves L1→L3 without a copy | `bytes_reserved` |
| Promoted | L3 `runtime/T_PROMOTED/<op>/` | `bytes_reserved`; P4 refuses disposition |
| Delivery acknowledgement | L3 unchanged | `bytes_reserved`; no release |
| Crash temporary | L4 or an extra entry in L2 | `bytes_reserved`; P2/P5 refuse |
| Unknown operation-named entry under either fixed root | L5 | `bytes_reserved`; P6 refuses |
| Unreadable/symlinked level | custody unknown | Refuse; never assume absence |
| Author removes/moves every custody location outside T | L1/L3/L4/L5 absent; L2 contains only allowed immutable control records | Still `bytes_reserved` until same-lock proof and disposed install |
| Same-lock proof succeeds | Paired no-follow stat/enumeration over both roots | Install disposed once; contribution becomes zero |

Pre-rename and post-rename premature release are closed. `actual_bytes`
never changes admission arithmetic. Settlement, quarantine, failure,
rename, promotion, unused reservation and delivery acknowledgement
release nothing. Protocol-created custody locations are exhaustively
covered; deliberately renamed, operation-unidentifiable same-UID custody
remains the signed A3 procedural residual. The diagnostic proof-list
serialization needs m1's exactness repair.

## Trace 3 — spawn/bootstrap cuts

| Cut | Required state/continuation | Derived result |
|---|---|---|
| Before lock | No spawn state | Correct. |
| Lock acquired, before first fork | `SPAWNING.json`; CLI bounded | Correct. CLI death releases lock. |
| First fork returns in CLI, before group record | Middle PID known, but no durable record yet | **Not total if middle child is stopped before closing its inherited release writer/`setsid`; CLI death does not force its exit and no later kill record exists.** |
| c5 races m2 | Record claims PID=PGID/session | **False until `setsid()` has completed; `killpg(pid_mid)` can address no group.** |
| Middle child after verified `setsid` | PID is PGID/session | Group kill would be valid, but the verification/order is absent. |
| Second fork, grandchild g0 | Grandchild blocks on release read | Correct once the group actually exists. CLI death eventually EOFs after every other release writer closes. |
| Middle dies before boot report | CLI timeout, identity-safe termination | Not total before verified PGID; correct afterward. |
| Boot report received | Grandchild pid/start/pgid checked | Correct. |
| `SPAWNING_CHILD` durable, before release | Grandchild still gated | Correct. |
| Release byte, grandchild scrub/endpoints/watchdog | Durable child identity exists | Correct. |
| First watchdog ack timeout | Kill watchdog, grandchild exits | Process exit releases lock, but stale child/group cleanup is incomplete (M3). |
| Identity installed | Singleton lock held through install | Correct. |
| PID reuse | Start-identity mismatch means no kill | Correct. |
| `SPAWNING_GROUP`/`SPAWNING_CHILD` no-replace conflict | Must be idempotent/stale/conflicting | **No exact continuation (M3).** |
| Later lock timeout with verified live supervisor | Do not kill, ordinary client | Correct. |
| Stuck live child/group older than max age | Kill only by valid recorded identity | Correct only after the missing pre-`setsid` ordering is repaired. |

The grandchild gate is sound, but the middle-child/PGID race means C3 is
not closed.

## Trace 4 — K1 byte accounting

For each accepted output frame:

1. Header, path, type, uniqueness, depth, component/path length, file
   count and reservation arithmetic are validated before creation.
2. The supervisor opens the write and held read descriptors.
3. It copies exactly `content_bytes` while updating only integer byte and
   frame counters. No hash object exists in the write path.
4. Worker status counts cross-check those counters; mismatch can only
   quarantine.
5. After EOF/status/group-death, the supervisor re-resolves the file,
   checks device/inode/link/size against the held descriptor and counters,
   and reads it once with `pread`, updating exactly one SHA-256.
6. `result_sha256` hashes the canonical metadata tuples, not content
   bytes. Promotion is rename-only; delivery/capacity/custody paths do
   not read content.

| Attack/cut | Result |
|---|---|
| Bound crossed before a frame | No frame byte written; kill/quarantine. |
| Short/long content, bad EOF | Transport or hash quarantine. |
| Path/count/grammar violation | Refuse before file creation. |
| Equal-size substitution present during verification | Sole hash captures different content; comparison to no inline hash is unavailable, but the result hash is computed from the verified bytes. |
| Inode/name substitution | Held descriptor identity check refuses. |
| Crash before/during/after sole pass but before settlement | `SUPERVISOR_CRASH`; no reusable partial hash; no promotion. |
| Modification after pass, before settlement/rename | A3 procedural residual; m2 requires it to be named honestly. |

Each content byte is written exactly once and hashed exactly once. The
ceilings remain enforceable through counters. M2 concerns durable
metadata availability after the pass, not the once-hash provider itself.

## Trace 5 — C1 evidence authority

| Required case | Derived result |
|---|---|
| Malformed current witness | First failing conjunct selects deterministic fallback id/path; original remains immutable. |
| Missing witness | `ABSENT` sentinel fallback. |
| Replayed/stale generation witness | Validation refuses; current fallback/UNKNOWN route. |
| Occupied witness no-replace path | Fallback uses a disjoint domain/path. |
| Historical instant unknown, current unresolved count zero | Legal fallback: `FREEZE_INSTANT_UNKNOWN`, zero, `PROVED`; no timestamp synthesized. |
| Duplicate identical fallback | `EEXIST` consumes existing object. |
| Conflicting fallback hashes for same tuple | Record-first invalidity; no valid terminal. |
| Consumption order | Current generation, table, process, fallback-before-freeze, id; fallback dominates its pair. |
| Watchdog witness authority | Witness only; no lock/capability/runtime write/ledger append/settlement. |
| Supervisor fallback authority | Supervisor-written under runtime lock; routes only to invalid all-live settlement. |
| Strict overrun/equality | Strict progress or `UNKNOWN`; no zero/valid terminal. |
| Replacement watchdog, non-overdue group | Intended durable freeze/resume path. **Unreachable as written because carried §W3.3 creates the witness forbidden by R4.** |
| Replacement ack not yet received | **Dual-valued:** general rule says invalid, crash row says hold frozen. |
| Deadline passes / identity or member mismatch / unresolved invalidity | Signed invalid route is appropriate. |
| Supervisor loss | Prior-generation replacement record cannot resume; validity-first phase 2A settles before reduction. |

The fallback repair closes the old collision/count defect and preserves
sole supervisor settlement authority. The replacement-resume extension
must be repaired before C1 is total.

## Trace 6 — fd remap

The algorithm duplicates both sources before writing either target,
keeps rejected low-number temporaries open while re-duping, selects two
distinct temporaries outside `{3,4}`, sets inheritance, performs the two
`dup2`s, closes originals/temporaries except targets, verifies FIFO type
and `O_ACCMODE`, closes forbidden descriptors, and re-verifies.

| Source class | Result |
|---|---|
| `(3,4)` | Both source descriptions preserved in temporaries; correct. |
| `(4,3)` | Crossing safe because both descriptions are duplicated first. |
| `(3,k)` / `(k,3)` | Any temporary landing on 4 is held/re-duped; correct. |
| `(4,k)` / `(k,4)` | Any temporary landing on 3 is held/re-duped; correct. |
| `(j,k)`, neither target | Temporaries landing on 3/4 are held/re-duped; correct. |
| equal, negative, malformed, missing source | Cleanup and `_exit(4)`. |
| non-pipe source | Cleanup and `_exit(4)`. |
| wrong direction/role | Cleanup and `_exit(4)`. |
| allocation/dup/fcntl failure | Failure cleanup closes adapter-opened descriptors, then `_exit(4)`; process exit closes inherited remainder. |
| forbidden fd survives | `_exit(4)`. |
| successful remap | Controller: write/read; worker: write/write; fds 3/4 inheritable through `execv`. |
| self-stop and termination | No signal disposition; self-stop after remap/preflight; supervisor bounded wait, group kill, death proof and reap on failure. |

M2 is closed without an import or author choice.

## Trace 7 — B1 across all eight commands

`N(i)` means explicit `NEW`; `R(i)` means explicit `RETRY`. The frontier
is the lowest durable reply without an ack.

| Command | `NEW` / `RETRY` and lost reply | Ordinary ack sources | Later-GC predicate |
|---|---|---|---|
| `CLAIM` | `N` allocates one claim/sequence; `R` returns its cached bytes and never claims again. | exact frontier `NEW(m+1)`, exact frontier `RETRY(m)`, eligible process terminal | owning process terminal archival commit |
| `START` | `N` starts once; `R` returns one cached lease. | same | owning process terminal archival commit |
| `HEARTBEAT` | `N` uses one recorded reading/charge; `R` never samples again. Concurrent `N`s serialize to disjoint cursor intervals. | same | archival commit covering the charge |
| `CLOSE` | `N` runs one close; `R` redelivers record/stopped hashes. Own terminal cannot self-ack. | successor or `CLIENT_ECHO` only | close archival commit |
| `PAUSE` | `N` runs one pause; `R` redelivers. Own terminal excluded. | successor or `CLIENT_ECHO` only | pause archival commit |
| `RESUME` | `N` runs one pinned checkpoint automaton; `R` never selects another. | successor, `CLIENT_ECHO`, eligible process terminal | resume archival predicate, including stated no-event case |
| `OPERATION_ADMIT` | `N` creates one operation/reservation/worker; `R` returns the same id with no second cursor/capacity. | successor, `CLIENT_ECHO`, eligible process terminal | operation terminal plus settling-charge archive |
| `OPERATION_STATUS` | Observation `N` is a new cached poll; observation `R` is stable across promotion/delivery ack. Ack form writes one delivery ack. | successor, `CLIENT_ECHO`; ack form also has delivery trigger | observation vacuous after commit/reply; ack form requires delivery ack and terminal |

Shared attack table:

| Trace | Result |
|---|---|
| Null ack hash | No ordinary ack; classification continues. |
| Exact frontier hash + `NEW(m+1)` | One `SUCCESSOR_OCCURRENCE` ack before allocation/classification. |
| Exact frontier hash + `RETRY(m)` | One `CLIENT_ECHO` ack; prefix-first then returns `ALREADY_ACKNOWLEDGED`. |
| Exact hash with any other mode/index | `INVALID/REPLAY_BYTES`, no state movement. |
| Wrong or stale-but-genuine non-frontier hash | One result: `INVALID/REPLAY_BYTES`, before allocation. |
| No frontier + non-null hash | `INVALID/REPLAY_BYTES`. |
| Lost request | Re-send `N(i)` if unallocated; one allocation. `R(i)` never allocates. |
| Lost reply | `R(i)` with null echo first returns cached effect bytes and frontier; a later exact echo acknowledges. |
| Concurrent same-scope `NEW` | One wins the lock; the other re-anchors to authoritative next. |
| Non-contiguous supervisor ack (terminal/delivery trigger) | Ack may exist above a gap; prefix stops at the first gap and frontier publishes it. |
| Ack before archival | Prefix advances, no reply remains owed; physical phase files stay until G3 later becomes true. |
| Later archival | Any held-lock epoch may begin GC. |
| Retry before or after GC | Prefix-first `ALREADY_ACKNOWLEDGED`; timing invisible. |
| Crash mid-GC with ack still present | Later epoch can finish. |
| Crash mid-GC after ack was deleted | **Cannot finish under G1; M1.** Exactly-once still safe because prefix is permanent. |
| Post-GC replay | Prefix-first refusal; no reducer/effect. |
| Missing directory with `prefix < i < next` | Impossible compliant layout → record-first invalidity. |
| Absent scope | next=1, prefix=0; `N(1)` allocates. |
| 64 unacked | `UNRESOLVED_JOURNAL`, but frontier drain remains available. |

B1 effect semantics for all eight commands are retry-stable and
generation-total. M1 prevents confirmation of the claimed physical
retention bound, not exactly-once safety.

## Trace 8 — exactness and no regression

### Literal examples and fixed arithmetic

Independent literal hashing reproduced:

```text
disposition preimage length: 396 bytes
disposition_id:
e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

decision-file length: 504 bytes
author_decision_sha256:
0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f

SHA-256(b"[]\n"):
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

The older no-newline value is correctly rejected.

### Schema/path/enum exactness

| Surface | Result |
|---|---|
| Absent tombstone | Exactly next=1, prefix=0. |
| Decision path | Derived from 64-lowercase-hex operation id; one path. |
| Decision bytes | Exact eight-line ASCII grammar; no hidden prose/judgment. |
| Disposition object | Exact inherited key set, but M4 leaves its time unbound. |
| Disposed record | Exact keys, but m1 requires a canonical representation of proof classes. |
| Custody roots | Fixed operations/promoted roots; quarantine reconciled to source `out/`. |
| Fallback id/schema | Domain-separated rejected-path/hash binding; ABSENT sentinel. |
| Replacement freeze | Exact object and resumed marker, but C2's automaton conflicts. |
| FD roles | Exact FIFO type/direction and fixed fds 3/4. |
| Reply envelope | Two frontier fields added; still within 2048 bytes. |
| Refusal/invalid enums | No new token; existing sets remain closed. |
| Empty result | Canonical `[]\n` digest verified. |
| New constants | None. |
| Signed five K1 constants | Unchanged. |

### No-regression table

| Signed cell/surface | Result |
|---|---|
| **A3** | Preserved. Same-UID deliberate forgery, arbitrary rename, stopped client, timing/metadata and post-verification mutation remain procedural and non-citable. m2 requires complete honesty about the last window. |
| **B1** | Exactly-once/retry-stable journal semantics for all eight remain intact. Ack priority is closed. M1 leaves a storage-GC completion defect, not reapplication. |
| **C1** | Watchdog remains witness/freezer only; supervisor alone settles. Fallback is supervisor authority. C2 can nevertheless manufacture invalidity for healthy non-overdue replacement freezes. |
| **D1** | No idle exit. C1's middle-child race leaves a pre-identity lock-holder cut not mechanically recoverable. |
| **K1** | No replenishment preserved; complete protocol-location proof and write-once/hash-once provider repaired. M2 leaves required durable result metadata absent. |
| Scientific/resource fields | No value moved. Exact decision grammar blocks prose. M4 leaves one control timestamp unbound; M2 leaves a verifier input undeclared. |
| Invalidity fields | Causes and precedence unchanged. C2's contradictory pending/resume rule leaves invalidity selection non-total. |
| Generic harness v2.3.1 | Inherited head/cache and inline meter-evidence surfaces unchanged. |
| Batch amendment v1.1.1 | All-live batch, `ARCHIVE` before `RESOLVED`, arithmetic and two-token order unchanged. |
| Signed events/schemas/roots/T bands | No intentional movement. New objects are control-plane/author-authority only. |
| Stream ownership/concurrency | Unchanged. |
| Import allowlist/frozen files | Zero intended delta. |
| Q/C boundary | New objects remain T-development-only and non-citable; no scientific outcome is authorized. |

## Author cells

No genuinely new author cell is required. Each repair is mechanical:

- gate and verify the middle child before treating its pid as a PGID;
- distinguish swap-only replacement freezes from deadline witnesses and
  totalize the pending-ack state;
- pin GC deletion order or add a durable GC marker;
- persist the already-computed result metadata;
- bind the two authority timestamps;
- totalize singleton record conflicts/removal;
- canonicalize the diagnostic custody proof field;
- name the complete A3 post-verification residual.

The signed A3/B1/C1/D1/K1 choices already determine every policy.

## Authorization boundary

Because the verdict is `REVISE`, Kirill's informed signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable**.

The bounded repaired bytes require another independent X/Y check. This
review authorizes no implementation, code/test edit, commit, T
activation, entropy, runtime construction, supervisor/controller/
worker/watchdog/adapter, endpoint, pipe, FIFO, journal, spawn record,
capability, lease, batch, operation, capacity artifact, custody
disposition, promoted object, author decision file, world, learner,
candidate, Q attempt, Q/C object, datum, outcome, scientific work,
E1/E2/E3 spend, or claim movement.

## Static custody and programme state

No existing file was changed. Exactly this one new review file was
created. No repository code, test, probe, supervisor, controller, worker,
watchdog, adapter, endpoint, smoke, or Officina process ran. No T/Q/C,
capacity, disposition, runtime, or scientific artifact was created. All
pre-existing dirty and untracked files were preserved.

Static inspection confirms `successor/officina/runtime/` contains only
`T_RUNTIME.lock`, `successor/officina/runtime_control/` is absent, and
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
T remains `NOT_ACTIVATED`. The programme claim remains `OPEN`.
