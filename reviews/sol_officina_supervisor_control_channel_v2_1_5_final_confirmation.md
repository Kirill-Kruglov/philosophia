REVISE_OFFICINA_SUPERVISOR_V2_1_5

# Independent clean-context Y-line review

Date: 2026-07-31

Reviewer line: Y

## Review base, method, and recomputed hashes

Review base: `c26ddb104ee395d3fb4f6a2dd357a1c6021f067b`, proved to
descend from the required commit
`36b458ae721d9fb5d0cd4f822949e77dc6385962`.

I read the complete supervisor v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4/
v2.1.5 chain, both signed author selections, the inherited generic-harness
and batch-settlement corrections, and both independent v2.1.4 reviews. I
treated the v2.1.5 correction closure and chat response as untrusted author
self-assessment and used neither as review evidence.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
0e20212d7258b4462a23a67750fa886aca8a82a4f5a0cb62f55205f5b8ef7310  reviews/sol_officina_supervisor_control_channel_v2_1_4_final_confirmation.md
4bb6961b21bb010745ab5093cf25545a4ea6440dacff238d53cbc089fda13625  reviews/opus_officina_supervisor_control_channel_v2_1_4_final_confirmation.md
```

The v2.1.5 digest exactly matches the expected committed value.

This was a static contract review. The only literal computations were
SHA-256 over documented bytes and byte-length arithmetic. No repository code,
test, probe, smoke, or Officina process ran.

## Answer

No. v2.1.5 makes real progress: it makes the valid terminal branch predicates
exclusive, totally accounts for partial `pipe2`/`fpathconf` construction,
pins both fork-failure routes, supplies a Linux-correct no-retry cleanup rule,
recasts the grandchild deadline as policy, and corrects the seven-row
provenance map.

The governing bytes nevertheless leave four blocking defects:

1. `¬S` and `¬Q` mean “not valid,” not “physically absent.” A malformed
   opposite terminal therefore counts as absent and a valid B-P/B-QM/B-QN
   row can release capacity, contradicting the mandatory `MALFORMED` route.
2. The cleanup routine handles `close` errors only after a failure. Normal
   close sites, including the separate `SPAWN.lock` close, have no EINTR/
   EBADF/other-errno ownership transition and can fall into exactly the fd
   reuse ambiguity the routine warns against.
3. The claimed c5–c7 failure row removes singleton records while the middle
   child may still be live at m0 and still holds the fork-shared lock; no
   stage/kill/death-proof rule is assigned to that row.
4. The old “no blocking syscall anywhere” and “healthy bootstrap always
   releases inside the bound” obligations remain operative because v2.1.5
   carries v2.1.4 rows 121–144 and the relevant §V214.1 invariants unchanged.
   They directly contradict §V215.3 and new row 159.

These are mechanical defects; no new author choice is necessary. The token
must remain unavailable.

## One-to-one disposition of the v2.1.4 Y findings

| Finding | v2.1.5 intended repair | Independent disposition |
|---|---|---|
| **M1** overlapping terminal selector | §V215.1 adds valid-object predicates and explicit `¬Q`/`¬S` branch conjuncts | **Not closed.** Valid branches are exclusive only if every canonical object is valid or absent. A malformed opposite terminal makes Q/S false and can enable release (new C1). |
| **M2** construction/fork/fd cleanup not total | §V215.2 adds ordered construction, ownership, cleanup, refusal sequence, and fork routes | **Not closed.** Partial construction and fork failures are fixed, and the cleanup routine itself uses the correct Linux no-retry rule. Normal closes and c5–c7 failure remain non-total (new M1/M2). |
| **m1** universal sufficiency claim for the grandchild bound | §V215.3 calls it anti-wedge policy and pins expiry | **Not closed.** The new section is correct, but carried §V214.1 text and test rows 121/126 retain the rejected claims (new M3). |
| **m2** wrong six-row provenance map | §V215.4 replaces it with seven exact rows | **Closed.** The map is exact and no stale mapping remains operative; old wording appears only in the superseded v2.1.4 bytes and quotations identifying the replacement. |

## Trace 1 — exhaustive M1 selector

Reviewer notation distinguishes physical presence from validity, which the
contract's `S/Q/F` notation does not:

```text
PS/PQ/PF = a canonical-name object is physically present
S/Q/F    = that object is physically present and passes regular-file,
           nlink, no-symlink, and exact-schema validation
M        = any physically present canonical object fails that validation
```

For valid-or-absent objects, the new rows are exclusive and correct:

| Physical/valid state | Binding/hash | Selected continuation |
|---|---|---|
| S and Q | any manifest/binding/hash | row 1, record-first both-terminal invalidity; release nothing |
| S, Q absent, F, `HS` | settlement binding matches | row 2, B-P only |
| S, Q absent, F, `¬HS` | settlement hash mismatch | 5e REFUSE; release nothing |
| S, Q absent, F absent | impossible settlement-without-manifest | 5d invalidity |
| Q non-null, S absent, F, `HQ` | quarantine binding matches | row 3, B-QM only |
| Q non-null, S absent, F, `¬HQ` | mismatch | 5g REFUSE |
| Q non-null, S absent, F absent | binding without retained file | 5f invalidity |
| Q null, S absent, F absent | no-manifest quarantine | row 4, B-QN only |
| Q null, S absent, F | orphan file without binding | 5h invalidity |
| S/Q/F all absent | ordinary not-yet-terminal operation | 5b REFUSE, not invalidity |
| F valid, S/Q absent | reducer-incomplete orphan manifest | 5c invalidity |
| canonical `.tmp` | no canonical predicate changes | L4 custody refusal |
| extra operation-bearing name | no canonical predicate changes | L5 custody refusal |

The malformed cases refute structural totality:

| Attack | Predicate result | Governing conflict |
|---|---|---|
| valid settlement + **malformed quarantine** + valid matching manifest | `S=1,Q=0,F=1,HS=1,M=1` | row 2 is true and row 5 is false, so B-P can release; 5a/table row 12 say any malformed object must invalidate |
| **malformed settlement** + valid non-null quarantine + valid matching manifest | `S=0,Q=1,B=1,F=1,HQ=1,M=1` | row 3 enters B-QM and can release instead of 5a |
| malformed settlement + valid null quarantine + manifest absent | `S=0,Q=1,B=0,F=0,M=1` | row 4 enters B-QN and can release instead of 5a |
| valid settlement + valid quarantine + malformed manifest | `S=1,Q=1,F=0,M=1` | outer row 1 and truth-table row 12 prescribe differently named invalidity routes; both retain capacity but the advertised literal partition is false |
| valid settlement + malformed quarantine + valid mismatching manifest | row 2 false; outer row 5 | 5a can run; this neighboring state shows the release depends on hash coincidence rather than malformed dominance |

The same-lock observation prevents an object from changing after selection,
but it cannot repair predicates that equate malformed presence with absence.
Both-valid-terminal and ordinary no-terminal histories are correctly distinct;
the malformed cross-products are not.

Bindings remain hash-bound and immutable. Wrong hash, absent retained
manifest, null/non-null mismatch, replayed disposition, wrong operation or
parent, partial author file, prohibited scientific value, and custody still
present all release nothing. The defect is specifically the missing
`¬MALFORMED`/physical-absence condition on rows 1–4.

## Trace 2 — M2 ordered construction

c2 installs this attempt's `SPAWNING.json` under the acquired lock. c3 then
creates channels in the fixed order boot, rel1, rel2, rel3 and verifies the
four write-end `PIPE_BUF` values.

| Failed operation | Per-process `owned` immediately before cleanup | Required continuation | Independent result |
|---|---:|---|---|
| boot `pipe2` | 0 | empty cleanup; ordered singleton cleanup; release | exact |
| rel1 `pipe2` | 2 | close boot pair once | exact |
| rel2 `pipe2` | 4 | close boot+rel1 ends once | exact |
| rel3 `pipe2` | 6 | close six ends once | exact |
| first/second/third/fourth `fpathconf` raises | 8 | close all eight | exact |
| any `PIPE_BUF < 4096` | 8 | close all eight, nonretryable host refusal | exact |
| c4 first fork raises | 8 in CLI; no child exists | stage 0, no kill, close all, remove records, release | exact |

At construction cuts only `SPAWNING.json` can belong to the attempt;
child/group/middle unlink steps are ENOENT and the final spawning unlink is
performed under the still-held lock, each with the inherited parent fsync.
`pipe2` failure adds no pair; successful return adds both ends atomically to
the local ownership set. No destructor, GC, or caller exit is needed on these
ordinary failure paths. A second cleanup invocation receives an empty set.

After a successful fork, each process has its own copy of the ownership set.
Normal closes are supposed to remove that process's copy; failure cleanup
must close exactly its remaining copies. The construction-prefix accounting
is sound, but the normal-close exception transition is missing (Trace 3).

## Trace 3 — M2 close/errno and fd reuse

For `BOOTSTRAP_FD_CLEANUP` itself, the pinned Linux rule is correct:

| `os.close(fd)` result | Kernel ownership fact on pinned Linux | Correct action |
|---|---|---|
| success | fd released | remove from `owned`; never revisit |
| `EBADF` | no open descriptor existed at that number at the syscall | treat as no remaining owned fd; do not retry |
| `EINTR` | Linux releases the descriptor before reporting EINTR | remove from `owned`; **never retry**, because the number may already be reused |
| another close error such as deferred `EIO` | Linux has released the descriptor | remove; continue; never retry |

The fixed iteration plus removal after every case prevents a retry from
closing a newly reused descriptor. Partial ownership closes only members; a
second invocation with the resulting empty set is a no-op. The routine never
depends on finalizers or caller exit.

The rule is not applied to normal close sites. Carried c5, m1, m6, c8, c12,
c13's boot close, m8, c16, g1 scrub, g3 lock close, and c18 lock release are
only named as “normal close” points. §V215.2.1's exception state machine is a
failure cleanup routine, and the `SPAWN.lock` fd is expressly excluded.
Therefore a normal close returning EINTR/EBADF/other errno has no rule saying:

- whether the fd is removed from `owned`;
- whether the bootstrap continues or takes a stage refusal;
- whether cleanup receives the already-released fd;
- whether the lock close is ever retried; or
- how a long-lived caller avoids closing a reused number on a later cleanup.

The assertion that “every close … removes one end” is not an executable
exception handler. New test row 157's claim that every syscall site is pinned
is consequently false. M2 is not closed for the exact close/errno attack the
task requires.

## Trace 4 — M2 forks, helpers, and process deaths

| Cut | Descriptor/identity fact | Continuation |
|---|---|---|
| c4 fork failure | failed fork creates no child | stage 0; no kill; cleanup 8 CLI ends; ordered records; lock close |
| m7 fork failure | no grandchild; middle owns boot_w and rel3_r | cleanup both, boot_w was last boot writer, `_exit(3)`; c13 sees boot EOF and takes stage 2 |
| c8 write failure | pre-group middle identity known | stage 1 `kill(pid)` only, prove, fd cleanup, records, lock |
| c9 read/c10 verify/c11 install failure | no accepted group until c11 | stage 1, never pre-verification `killpg` |
| c12 write/c13 read failure | verified group record durable | stage 2 `killpg`, prove every member dead, cleanup |
| middle death before m7 | no grandchild boot writer | c13 EOF, stage 2 |
| middle death m7→m8 | grandchild holds boot_w | c13 nonblocking deadline, stage-2 `killpg` reaches grandchild |
| m8 write failure with grandchild gated | grandchild keeps boot writer until g1 | c13 deadline, then stage 2; CLI rel3 close makes g0 EOF if kill has not already ended it |
| c14/c15/c16 failure | verified group, grandchild gated | stage 2, then cleanup |
| g0 EOF/error/deadline | grandchild cleanup then `_exit(3)` | c17 fails, CLI stage 2 |
| g1/g2/first-ack failure | child identity durable | kill watchdog/group by exact identity, prove death, ordered records, exit |
| PID reuse | start identity mismatch | never kill; recorded process treated absent |

`BOUNDED_READ` and `BOUNDED_WRITE` still cover EAGAIN, EINTR, EOF,
EPIPE, malformed/overlong/trailing frames, partial-write assertion, deadline,
and every other read/write errno. Kill precedes record deletion and uses the
records it is about to remove; `waitpid` is limited to own children.

One construction-to-stage gap remains. §V215.2.7 groups “c5–c7 failure,” says
all records are removed, and says the middle child at m0 exits later by its
bound or EOF. At m0 the middle retains its own rel1 writer, so CLI cleanup does
not deliver EOF. If `SPAWNING_MIDDLE.json` was installed and its durability
step then reports failure, the table removes a live identity record before
the middle has died. Even without a durable middle record, the child retains
the fork-shared `SPAWN.lock` until its bound, so the table's immediate “lock
released” conclusion is false. §V215.2.4's exhaustive invocation list does
not assign c5/c6/c7 a stage or a kill/death proof. This is new M2.

## Trace 5 — crash prefixes

For stage-1/stage-2 paths that have a pinned stage, the order is safe:

| Crash cut | Durable/process state | Restart continuation |
|---|---|---|
| before kill | identity record survives; target may live | process crash closes that process's copies; child gate/deadline and next holder's tier discipline govern; no record was removed |
| after signal, before death proof | records survive | later holder revalidates identity, never kills PID-reused process, and proves live/dead before removal |
| after death proof, before fd cleanup | exact process dead; records survive | next held-lock preflight P3 may remove; no live unlink |
| between cleanup closes | ordinary path uses the owned set; a process crash releases that process's remaining fds | next invocation sees records and performs P1/P2/P3; no normal failure may rely on this crash behavior |
| after fd cleanup, before first unlink | dead identities and all records survive | P3 ordered removal |
| after child unlink, before/after fsync | child may reappear or stay absent after crash | child→group→middle→spawning order resumes, ENOENT-tolerant |
| after group unlink/fsync | only lower tiers remain | same ordered continuation |
| after middle unlink/fsync | spawning remains | remove spawning, fsync |
| after spawning unlink, before lock close | no singleton survives | next holder starts at P0 after lock release/crash |
| after lock close, before refusal return | attempt state absent | second invocation starts clean |

The order never removes a live identity on a properly assigned stage because
kill and death proof precede singleton removal. Construction stage 0 has no
child. The c5–c7 row is the exception: it expressly allows the middle to
remain live at m0 while claiming the record set is already gone. That prefix
has neither the stated “no live identity record removed” property nor an
immediately free lock.

## Trace 6 — m1 slow-bound policy

The new governing paragraph is honest in isolation:

1. g0 measures a fixed `2 × 10 s` anti-wedge deadline.
2. c14 `/proc` work and c15 file/parent fsync have no duration bound.
3. An otherwise valid slow launch may therefore expire.
4. The grandchild closes rel3_r/boot_w and exits; c17 cannot verify identity;
   the CLI performs stage 2, cleanup, ordered records, and refusal.
5. No supervisor identity, ledger entry, witness, fallback, invalidity,
   capacity/custody object, result, or datum is installed.
6. The refusal is T-development-only, non-citable, and bounded by the existing
   re-anchoring rule; it is policy, not scientific/resource evidence or an
   outcome-shopping state.

But the full carried contract says all of the following at once:

- carried §V214.1.1: “no blocking syscall exists anywhere in the bootstrap”;
- carried §V214.1.5 invariant: the same universal no-blocking assertion;
- carried test row 121: assert no blocking syscall exists in the bootstrap;
- carried test row 126: a healthy bootstrap always releases inside the bound;
- §V215.3.1: c14/c15 fsyncs have no executable duration bound and the
  universal sufficiency assertion is deleted; and
- new row 159: assert that no text contains the healthy-launch sufficiency
  claim.

§V215.0 does not replace the two old invariants, and §V215.7 explicitly says
rows 121–144 carry forward unchanged. Thus m1 is not closed in the composite
bytes: implementations cannot satisfy rows 126 and 159 together, and the
no-blocking assertions are false for c15's acknowledged unbounded fsyncs.

## Trace 7 — m2 provenance

The operative seven-row mapping is exact:

```text
C1 → §V214.1    C2 → §V214.2    M1 → §V214.3
M2 → §V214.4    M3 → §V214.5    M4 → §V214.6
m1 → §V214.7
```

The full-chain search found the bad six-row table only in the preserved
v2.1.4 evidence and in v2.1.5 quotations that identify it as replaced. No
later operative reconciliation remaps those findings. The surrounding
authorization history correctly records X-confirmed/Y-revised v2.1.4 and the
need for fresh v2.1.5 X/Y. This provenance-only finding is closed.

## Trace 8 — no regression in unnamed repairs

The documented literal hashes reproduce:

```text
disposition preimage (396 bytes)
e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

eight-line decision file (504 bytes; line 8 = 43 bytes including LF)
0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f

canonical entries (265 bytes)
5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3

canonical RESULT_MANIFEST.json (638 bytes)
e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed

operation-directory enumeration
3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc

canonical empty array (`[]\n`)
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

| Surface | Independent re-test |
|---|---|
| **A3/K1 write-hash** | One supervisor write and one descriptor-based hash per content byte; inode/nlink/size/EOF detections unchanged; before/during/after-pass and directory-swap residuals remain honest, unobservable, and non-citable. |
| **Spawn gates** | Four nonblocking channel pairs, bounded helpers, m0/m5/g0 gates, verified `setsid`, pre-group `kill(pid)` and post-group `killpg`, PID reuse protection, and the m7→m8 deadlock repair carry. New close/c5–c7 defects are isolated above. |
| **C1 replacement** | Overdue witness versus swap-only record, I1→I7 priority, exact-current ack, all non-T pre-resume states in I3, marker-before-SIGCONT, supervisor-loss I7, and supervisor-only settlement all carry. |
| **B1/GC** | All eight commands remain exactly-once and retry-stable; `NEW` allocates and explicit `RETRY` never does; CLIENT_ECHO/successor ack remain disjoint; prefix-first classification and `committed→reply→ack→accepted` GC with D6 survive every crash prefix. |
| **Manifest/custody** | Sole-pass tuples, immutable manifest, B-P/B-QM/B-QN bodies, L1–L5/P1–P7 absence, `bytes_reserved` accounting, no replenishment, and no content reread carry. New C1 compromises malformed selector entry, not branch bodies. |
| **Singleton lifecycle** | Lock-first preflight, mutation-free stuck-holder route, P0–P3, EEXIST, PID reuse, and child→group→middle→spawning cleanup carry. New M2 contradicts the live-removal boundary at c5–c7. |
| **Author authority** | Canonical path, acyclic id, exact eight lines, timestamp equality, prohibited-content check, disposition object, and disposed no-replace remain deterministic. |
| **Fallback/fd remap** | Rejected-witness fallback remains disjoint and supervisor-validated; collision-safe fd remap, direction/CLOEXEC checks, self-stop, failure cleanup, and exec remain unchanged. |
| **Harness/batch** | Generic harness v2.3.1 §J1–§J3 and batch v1.1.1 §D1/§D2, nine events, E1/E2/E3, roots, T bands, and archival order are unchanged. |
| **Q/C boundary** | New routines and facts remain control-plane only; no result-responsive, validity-shopping, scientific, Q, or C authority is introduced. |

## New findings

### Critical

#### C1. Malformed opposite terminal is treated as absence and can reach a releasing branch

Loci: v2.1.5 §V215.1.1 definitions of `S`, `Q`, `F`, and `MALFORMED`;
§V215.1.2 rows 2–4; §V215.1.3 5a and truth-table row 12.

The branch predicates use `¬Q`/`¬S`, but Q/S include validation. Therefore
negation means absent **or malformed**. With a valid settlement, valid
matching manifest, and malformed quarantine at its canonical name, row 2 is
true and row 5 is false; B-P can complete the author disposition and release
`bytes_reserved`. Symmetric malformed-settlement histories reach B-QM or
B-QN. This contradicts 5a and row 12, which require every malformed canonical
object to take record-first invalidity.

This is not rescued by row order: the releasing row is selected before row 5
because its literal predicate is true. It is not rescued by takeover validity
first: the selector claims same-epoch totality, and same-UID procedural
interference can create the state after earlier validation. It violates K1's
complete, mechanically verified release authority.

Smallest bounded repair: define physical-presence predicates `PS/PQ/PF`.
Evaluate `MALFORMED` first and make it dominate every other row. Require
`¬MALFORMED` and physical absence (`¬PQ` for B-P; `¬PS` for B-QM/B-QN) in
every releasing predicate. Make the both-terminal test physical or run it
after malformed dominance, and rebuild the complete cross-product table.

### Major

#### M1. Normal close sites are outside the only pinned close/errno state machine

Loci: v2.1.5 §V215.2.1 (failure cleanup routine and exclusion of
`SPAWN.lock`), §V215.2.2 normal-close column and exhaustive claim, inherited
c5/m1/m6/c8/c12/c13/m8/c16/g1/g3/c18 close sites, and test row 157.

The Linux claim inside `BOOTSTRAP_FD_CLEANUP` is sound: after close returns
EINTR or another non-EBADF error the fd number must not be retried, because it
has been released and may be reused. But normal closes do not call that
routine and have no equivalent exception rule. An implementer may propagate,
retry, continue without removing ownership, or feed an already-released
number to later cleanup. The lock descriptor is explicitly outside the
routine. This leaves fd reuse, record cleanup, and lock release discretionary
and fails the long-lived-caller/no-GC requirement.

Smallest bounded repair: define one single-fd `CLOSE_OWNED` transition with
the existing Linux errno rule and use it at **every** normal and cleanup close,
including the lock fd. Pin whether a reported non-EBADF close error continues
or enters the appropriate refusal after removing ownership; never retry the
number. Then make the multi-fd routine a fixed-order loop over that primitive.

#### M2. The c5–c7 failure row removes records before the middle child is dead

Loci: v2.1.5 §V215.2.4 exhaustive invocation list and
§V215.2.7 row “c5–c7 failure”; inherited §U2.2 c5–c8 and §U2.3 m0/m1.

The row says the CLI closes its ends, removes all four records, releases the
lock, and leaves the middle at m0 to exit by EOF or its bound. At m0 the
middle still owns its rel1 write copy, so CLI close does not cause EOF. It
also owns the fork-shared lock. If the middle record was installed before a
durability error, removing it before death proof violates §U6.3's
death-proved-only boundary; in every case the lock remains held until m0's
bound. The exhaustive refusal list does not assign c5/c6/c7 a stage or exact
kill identity.

Smallest bounded repair: split c5, c6, and c7. For every post-fork failure,
pin the exact in-memory/durable identity available, kill the current middle
with pre-group `kill(pid)` where identity-safe, prove death, then close fds,
remove only records owned by this attempt under P1/P2/P3, and release the lock.
Do not claim EOF at m0 while its own writer exists.

#### M3. Carried no-blocking and healthy-bound obligations contradict the new policy

Loci: carried v2.1.4 §V214.1.1 and §V214.1.5 invariants; carried §V214.10
test rows 121 and 126; v2.1.5 §V215.0, §V215.3.1, §V215.7 carry-forward
sentence, and new row 159.

§V215.3 correctly admits that c15's file and parent fsync have no duration
bound and deletes universal sufficiency. Yet §V215.0 leaves the two universal
“no blocking syscall” assertions operative, and §V215.7 explicitly carries
rows 121–144 unchanged. Row 126 still requires every healthy bootstrap to
release inside the bound, while row 159 requires that no such text exist.
Both tests cannot pass. This is the exact stale operative language m1's repair
needed to remove.

Smallest bounded repair: replace, not merely extend, rows 121 and 126. Replace
both §V214.1 universal no-blocking assertions with the accurate narrower fact
that no bootstrap **pipe read or write** can block past its helper deadline.
Make row 126 test the deterministic slow-valid refusal and non-citability,
consistent with §V215.3/rows 159–162.

### Minor

#### m1. The ownership table attributes boot EOF to closing the wrong pipe end

Locus: v2.1.5 §V215.2.2 `rel3_r` failure-owner cell, against §V215.2.6.

The cell says middle cleanup of `rel3_r` “is what makes c13 see EOF at m7
failure.” c13 reads `boot_r`; EOF comes from closing the last `boot_w`, as
§V215.2.6 correctly states. Closing rel3_r affects the rel3 gate, not boot.
The routine closes both, so behavior is correct; the causal annotation is not.

Smallest repair: move that parenthetical to the `boot_w` row and leave the
`rel3_r` row as ownership cleanup only.

## No-regression table

| Signed cell/surface | Result under v2.1.5 |
|---|---|
| **A3** | Four write/hash residuals and the slow-bootstrap fact remain procedural and non-citable; no new security claim. |
| **B1** | All eight commands, acknowledgement priority, cached replies, prefix, and GC remain unchanged and exact. |
| **C1** | Dedicated watchdog/freezer and supervisor-only settlement remain unchanged; replacement state machine stays total. |
| **D1** | No idle exit is introduced. M1/M2 leave bootstrap resource/lifetime cuts non-total and must be repaired. |
| **K1** | Constants, one-write/one-hash, no replenishment, and normal B-P/B-QM/B-QN bodies remain. C1 permits release in a malformed impossible layout and is blocking. |
| **Acyclic author authority** | Preserved; all illustrative hashes reproduce. |
| **Complete custody** | L1–L5/P1–P7 and full `bytes_reserved` accounting remain; malformed selector entry is the regression. |
| **Fallback and fd remap** | Preserved unchanged. |
| **Generic harness / batch settlement** | v2.3.1 and v1.1.1 surfaces, inline meter evidence, head/cache rule, event set, and archival order unchanged. |
| **Scientific/Q/C boundary** | No new scientific or Q/C field or author judgment; all new facts remain control-plane. |

## Author-cell determination

No genuinely new author cell is required. Physical presence versus validity,
close ownership on Linux, pre-group child cleanup, and removal of stale
universal assertions are mechanical consequences of the already-signed
A3/B1/C1/D1/K1 policy. No new constant, resource quantity, scientific value,
invalidity cause, custody destination, or author token is needed.

## Authorization boundary

Because the verdict is `REVISE`, Kirill's informed signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable**. The repaired bytes require another bounded independent
X/Y review. This review authorizes no implementation, code/test edit, commit,
T activation, entropy, runtime construction, supervisor, controller, worker,
watchdog, adapter, endpoint, pipe, FIFO, journal, spawn record, result
manifest, capacity/custody artifact, author decision, E1/E2/E3 spend, Q/C
work, or scientific work.

## Static custody and programme state

No repository code, test, probe, smoke, supervisor, controller, worker,
watchdog, adapter, endpoint, or other Officina process ran. Only read-only
file display, Git ancestry/status, SHA-256, and permitted literal-example
hashing/arithmetic were used. No existing file or runtime state was changed;
exactly this review file was created. No T/Q/C, runtime, capacity, custody,
result-manifest, entropy, or scientific artifact was created. All pre-existing
modified and untracked paths were preserved.

`successor/officina/runtime/` still contains only `T_RUNTIME.lock`,
`successor/officina/runtime_control/` remains absent, and
`successor/officina/T_ENVELOPE.json` remains unactivated. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
