REVISE_OFFICINA_SUPERVISOR_V2_1_2

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.2

Date: 2026-07-30
Reviewer line: X (adversarial Linux / process / crash / hash-construction semantics)
Review base: commit `011aa28` (HEAD), at or after required commit `9743d1f`.
Working tree dirty exactly as handed over; **nothing modified by this review.**

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.2 was authored
by **Claude Code Opus 5 in the specification-author role** (Fable 5
unavailable); the same author line wrote v2.1/v2.1.1. Shared model-family
identity is not review continuity — I re-derived every disposition from the
v2.1.2 bytes. I read `reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md`
**only as an untrusted authored self-assessment** and used none of its claims
as evidence. I do not inherit my own v2.1.1 X-line authority; the X211 findings
are re-stated from the v2.1.1 bytes and re-tested here.

## Recomputed hashes (all verified)

```text
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md   (== expected)
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
b5b5614166488bc8dca0856bf6963d84bd701757df153acaf868212687a2d797  reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
640305647c9c03d44f40899bf2434c089afb5cbbbf8286e9673852aa795cc6b1  reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The v2.1.2 digest matches the expected committed value exactly, and every
inherited surface and both v2.1.1 review files are byte-identical to what
v2.1.2 cites in its governing-hash block (author-note `ae9c440…` and
harness-signature `8c47da35…` also match). The review base is precise: v2.1.2
dispositions the two v2.1.1 confirmations whose hashes it records, and those
are the files I hold.

**Method.** Static and read-only. No process, test, probe, supervisor,
controller, worker, watchdog, adapter, or endpoint ran. Two documented
digests and one canonical-form hash were **recomputed from the literal
documented bytes** (permitted): the §N1.8 forward construction and §N9.2's
empty-result value (see the Hash-DAG trace). Import-allowlist facts are cited
from `src/philosophia/officina/verification.py:35-38`
(`ALLOWED_ABSOLUTE_IMPORTS` = `{__future__, ast, dataclasses, datetime, enum,
fcntl, hashlib, hmac, json, os, pathlib, re, subprocess, time, typing,
weakref}`; `select`/`selectors`/`signal`/`ctypes`/`sys` outside it), so every
primitive v2.1.2 names (`os.dup`, `os.dup2`, `os.set_inheritable`, `os.fstat`,
`os.pread`, `os.read`, `os.write`, `os.listdir`, `os.open(dir_fd=…)`,
`fcntl.flock`, `fcntl.fcntl` `F_GETFL`, `time.clock_gettime_ns`, `hashlib`,
`json`, `re`, `pathlib`) is inside it with **zero delta**.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_V2_1_2
```

v2.1.2 is an excellent, near-total correction. It **closes X211-C1** — I
reproduced §N1.8's digests exactly and confirmed the dependency DAG is acyclic
and forward-computable — and it soundly closes **X211-m1, X211-m2, and every
converged Sol v2.1.1 finding (C1, C2, C3, C4, M1, M2, M3, M4, M5, m1)** that
intersects X-line process/crash/hash semantics, in each case with exact,
executable, non-circular text that I could not refute.

It introduces **one new Major, X212-M1**: the write-once/**hash-once** repair
(§N4, closing Sol C4) removes v2.1.1's inline hash and therefore has **no
stored reference to compare against**, yet §N4.2 claims "the equal-size and
inode substitution defences are **fully retained**." A single hash cannot
detect a same-inode, equal-size, in-place content substitution — v2.1.1's
`HASH`-quarantine on exactly that case is silently gone, and the claim is
false. This reintroduces the X21-M7 / Sol-M2 over-claim class over a signed-A3
boundary and weakens a fail-closed behavior v2.1.1 had. The required question
forbids "a new Major" and "weaken[ing] fail-closed behavior," so the answer is
**no** and the token stays unavailable.

X212-M1 is a single, bounded **truthfulness** repair (state the case honestly
as an A3 procedural residual; keep hash-once). It reopens no author cell and
needs no new author choice. Everything else stands on re-derivation.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT   — NOT signable
```

---

## New finding

### X212-M1 (Major) — the hash-once repair over-claims an equal-size content-substitution defense it cannot provide

**Locus.** §N4.2 (lines 758–776), especially the step-3 comment
`# equal-size content substitution defence` and the closing sentence "The
equal-size and inode substitution defences are **fully retained** …"; the
deletion of v2.1.1 §Z8.3 step 4 ("require it to equal the inline hash") per
§N0; and the worker-status/output matrix reliance on it.

**Why the claim is false.** v2.1.1 computed an inline streaming hash during the
write pass (over the bytes the supervisor itself wrote) and, in the
verification pass, re-read the file and **required equality with that inline
hash** — that comparison is what detected an equal-size in-place content
substitution (re-read ≠ inline ⇒ `HASH` quarantine). To satisfy literal signed
K1 ("writes and hashes each byte once", output-capacity signature lines 22–24;
Sol C4), §N4.1 **deletes the inline hash**, leaving §N4.2 step 3 as the *only*
hash. Step 3 hashes the current bytes and checks that the read length equals
`bytes_written[rel]` with EOF at that offset — a **size** check, not a content
comparison, because there is now no known-good reference hash anywhere:

- the held `r` descriptor (opened before any byte existed) is not a snapshot —
  reading it returns the *current* (possibly substituted) inode content;
- the worker-supplied `frame_count`/`total_content_bytes` are untrusted counts,
  not a content hash;
- `result_sha256` is *produced by* step 3, so it cannot be the reference for
  step 3.

Therefore step 2's `(st_dev, st_ino)`/`st_nlink`/size check detects **inode**
substitution (unlink+recreate ⇒ new inode ≠ held `r`) — that part is real — but
a **same-inode, equal-size, in-place overwrite before the verification pass is
not detected**: step 2 passes (same inode, same size), step 3 hashes the
substituted bytes with nothing to compare, and the operation is **promoted**,
where v2.1.1 would have `HASH`-quarantined it.

**Failure scenario.** An A3 same-UID process overwrites, in place, one output
file of a completed operation with different bytes of identical length before
the supervisor's verification pass. v2.1.1: re-read ≠ inline ⇒ `HASH`
quarantine (fail-closed). v2.1.2: passes every check, `result_sha256` is
computed over the substituted bytes, and the substituted tree is promoted — no
quarantine — while §N4.2 asserts the defense is "fully retained."

**Severity.** Major, not Critical: capacity accounting is untouched, no
capacity is wrongly released, and `result_sha256` still accurately describes
the promoted tree (it is computed at verification, and promotion is a rename),
so there is no internal inconsistency and no accounting corruption. But it (a)
states a **false** mechanical-detection claim over a signed-A3 boundary — the
exact over-claim class X21-M7 and Sol M2 exist to catch — and (b) removes a
fail-closed `HASH`-quarantine v2.1.1 had, which the required question
explicitly gates on.

**Smallest bounded repair (no author cell, keeps hash-once).** In §N4.2 delete
the `# equal-size content substitution defence` comment and the "fully
retained" sentence; state instead that with a single content hash and no stored
reference, a **same-inode equal-size in-place content substitution occurring
before the verification pass is within the signed A3 procedural residual and is
not mechanically detected** — only **inode** substitution (via the held
`O_RDONLY` descriptor opened before the first byte), size/length anomalies, and
`st_nlink` are mechanically detected — alongside the already-named
directory-swap residual of §N4.4. This aligns the prose with the behavior,
keeps literal K1 (hash once), reopens no author cell, and moves no constant. It
must then receive another independent X/Y check.

### X212-m1 (Minor, observation) — the "hash-once vs. detection" tension is fundamental and should be recorded

Detecting an equal-size in-place substitution *requires* either two hashes
(v2.1.1) or a trusted stored reference; literal K1 forbids the second hash of a
content byte. These goals are mutually exclusive, so the honest resolution is
X212-M1's residual statement, not a mechanism. Recording this prevents a future
layer from "re-adding detection" in a way that silently re-violates hash-once.
No action beyond X212-M1.

No other new Critical, Major, or Minor survived re-derivation.

---

## One-to-one disposition of the v2.1.1 findings

### Opus X211

| Finding | v2.1.2 locus | Verdict | Basis (re-derived) |
|---|---|---|---|
| **X211-C1** circular `disposition_id` (unconstructible release authority) | §N1.1–§N1.5, §N1.8 | **CLOSED** | `disposition_id = SHA-256({domain tag, activation_record_sha256, author_decision_path(operation_id), operation_id})`; `author_decision_sha256` removed from the preimage; the decision path is **derived** from `operation_id`; the decision file (which contains `disposition_id`) is written after `disposition_id` is computed, and `author_decision_sha256` is a **sink** bound only in the object/verifier. I recomputed §N1.8: preimage 396 B → `e330a384…`; file 504 B (= Σ line-lengths + 8) → `0773f29c…` — **both reproduce exactly**, and S1→S4 is forward-computable with no step needing a later value. Acyclic and content-closed. |
| **X211-m1** over-aggressive `CLIENT_ECHO` `REPLAY_BYTES` | §N7.1–§N7.3 | **CLOSED** | The acknowledgement **frontier** (lowest unacked occurrence with a durable reply) is published in every reply envelope, so a client never guesses; §N7.2's single pre-allocation rule (A0–A3) gives one deterministic result per case. The prior ambiguity is removed by construction, and a stale-but-genuine hash has one result (A3 `INVALID/REPLAY_BYTES`, before any state movement). |
| **X211-m2** dead-watchdog: non-overdue groups' resume unstated | §N5.6 | **CLOSED** | A group frozen only for a watchdog swap gets a durable `REPLACEMENT_FREEZE` record and a six-conjunct resume predicate (live+acked replacement watchdog, still non-overdue, all members alive/`T`, no witness/fallback, no unresolved invalidity, `.resumed.json` before `SIGCONT` for idempotence). Any doubt ⇒ signed invalid route; never crosses a supervisor loss (prior-generation record fails R1 ⇒ phase 2A settles it). This is the only path that `SIGCONT`s a frozen group and never applies to a deadline freeze. |

### Sol (converged v2.1.1 findings)

| Finding | v2.1.2 locus | Verdict | Basis |
|---|---|---|---|
| **Sol C1** (= X211-C1) circular id | §N1 | **CLOSED** | as above (digests reproduced). |
| **Sol C2** custody-absence proof checked one name, not the full set | §N2.1–§N2.6 | **CLOSED** | The proof target is the derived complete location set L1–L5 (source/quarantine `out/`, the operation dir as a control-record subset, promoted dir, `.tmp` temporaries, any `<op>`-named stray), each proved absent by **two** independent observations (`follow_symlinks=False` stat `ENOENT` **and** dir-fd enumeration) in one lock epoch; both `os.replace` sides caught (P2/P3 source, P4 destination); unreadable ⇒ refuse; `custody_root` demoted to diagnostic (§N2.4). No existing byte can coexist with release. |
| **Sol C3** earliest grandchild lock-holder cut | §N3.1–§N3.6 | **CLOSED** | The grandchild's **literal first instruction** is a gated `os.read` on a release pipe whose only write end is the CLI's; it executes nothing else (not even the descriptor scrub) until the CLI has installed `SPAWNING_GROUP.json` (immediately after the first fork, before the grandchild exists) and `SPAWNING_CHILD.json`. Every cut yields a killable durable record or a process whose death releases the lock (CLI death ⇒ EOF ⇒ `_exit(3)`). The middle child cannot wedge (two `/proc` reads + one non-blocking pipe write). The one residual — a **deliberately** `SIGSTOP`ed/wedged same-UID CLI holding the lock — is honestly named A3 procedural, and D1 is unaffected (no supervisor waits on `SPAWN.lock`). |
| **Sol C4** literal K1 hash-once | §N4.1–§N4.4 | **CLOSED (hash count) — but see X212-M1** | The write path computes **no** content hash (integer counters only); the sole content hash is the pre-settlement verification pass, so each byte is written once and hashed once — literal K1. The **detection claim** attached to that pass over-reaches (X212-M1). |
| **Sol M1** rejected-witness fallback path collision + `UNKNOWN` count | §N5.1–§N5.5 | **CLOSED** | A separate `FREEZE_FALLBACK` namespace with `fallback_witness_id` binding the rejected object's path+SHA-256 always has a free no-replace target; the rejected witness is never overwritten; `unknown_reason` is separated from `current_unresolved_member_count`, so `UNKNOWN` + zero current members + `supervisor_quiescence = PROVED` is legal (historical instant unknowable) without weakening the route. The fallback is a **supervisor** fact in a namespace the watchdog cannot reach ⇒ no second watchdog authority. |
| **Sol M2** fd remap not total on overlapping/crossed sources | §N6.1–§N6.3 | **CLOSED** | Both sources are `os.dup`'d to temporaries outside `{3,4}` **before** either target is written (bounded ≤ 8 iterations, never closing a held temporary), then `dup2` to 3/4, then role/direction (`F_GETFL & O_ACCMODE`) and `S_ISFIFO` verified and re-verified post-`SIGCONT`. The `(4,3)` case is now correct; the seven-class table is exhaustive; the remap precedes self-stop. |
| **Sol M3** two incompatible ack continuations | §N7.2 | **CLOSED** | `SUCCESSOR_OCCURRENCE` (`NEW` at m+1) and `CLIENT_ECHO` (`RETRY` at m) are made **disjoint** over the published frontier `m`; a non-null mismatch is the single result `INVALID/REPLAY_BYTES` before allocation. No frame has two continuations. |
| **Sol M4** GC tied to the ack-install epoch (could strand acknowledged records) | §N8.1–§N8.4 | **CLOSED** | GC is decoupled from ack: permitted in **any later** locked epoch once ack durable, prefix satisfied, and the per-command archival predicate holds (§N8.2, with the observation form **explicitly vacuous**). Classification tests the prefix **first** (§N8.3), so GC timing is invisible and partial GC harmless; the two-part retention bound is now executable and polling-independent. |
| **Sol M5** tracked decision file not content-closed | §N1.4, §N1.6 | **CLOSED** | The file is a **byte-exact eight-line** grammar (fixed literals + five pinned-class variable values, total length = Σ line-lengths + 8); no other byte may exist, so it cannot carry a result hash, judgement, or prose "by exhaustion." Conjunct 9 further rejects any of the five values equalling `result_sha256`/`content_sha256`/etc. over the operation-bound identifier set. |
| **Sol m1** absent-scope tombstone default implicit | §N9.1 | **CLOSED** | `tombstone_next(absent) := 1`, `acknowledged_prefix(absent) := 0`, pinned and threaded into §N8.3 step 1. |

---

## The eight required attack traces

### 1. Hash DAG

I reproduced §N1's dependency order and both illustrative digests from the
literal bytes: the 396-byte canonical preimage
`{activation_record_sha256, author_decision_path, operation_id, schema-tag}`
hashes to `e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd`
(matches), and the 504-byte eight-line decision file hashes to
`0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f` (matches);
`504 == Σ(line lengths)+8` (matches). Searching every id/path/file-hash
binding: `disposition_id` depends only on `{activation, derived-path,
operation_id}`; `author_decision_path = f(operation_id)`; the decision file
depends on `disposition_id` (already computed); `author_decision_sha256 =
SHA-256(file)` is a **sink** bound only downstream. **No direct or transitive
self-reference.** Path substitution (X→Y) fails at conjuncts 2 and 8a (path
derived, id binds it); extra author bytes fail conjunct 8c (byte-exact length);
stale parent fails conjunct 4; replay fails conjunct 11 (no-replace) and §N2.3;
wrong operation fails 2/8a; partial install leaves `bytes_reserved` accounted
and re-verifies idempotently. **Acyclic, forward-computable, content-closed.**

### 2. Custody set

L1–L5 (§N2.2) are derived from the immutable `operation_id` and the two fixed
roots only — no record field is trusted to name custody. They cover source/
quarantine `out/` (L1; §N2.1 defines quarantine as staying at L1), the
operation directory as a **subset** of the closed control-record set (L2, so
any stray or surviving `out`/`.tmp` refuses), promoted custody (L3), every §3
durability temporary (L4), and any `<op>`-named stray under either root (L5).
Both `os.replace` sides are covered: pre-rename ⇒ P2/P3 find `out` ⇒ refuse;
post-rename ⇒ P4 finds `T_PROMOTED/<op>/` ⇒ refuse (§N2.6). Absence is always
two observations (stat `ENOENT` **and** enumeration); any unreadable level
refuses; every crash direction in §N2.6 refuses while bytes exist. The only
locations outside L1–L5 are those an A3 process could fabricate by copying bytes
to an arbitrary path — the named procedural residual, since the **protocol**
creates custody only at L1/L3/L4. **No existing byte can coexist with release.**

### 3. Earliest fork cut

Traced §N3.6 cut by cut. Literal first grandchild instruction = gated read
(g0); both sealed channels correct (CLI holds release-write + boot-read; middle
child holds release-read + boot-write, closes the opposite pair in m1;
grandchild inherits release-read + boot-write). `SPAWNING_GROUP.json` (first
fork, CLI, pgid = `middle_child_pid` = setsid leader) exists before the
grandchild does; middle-child report (m5) is non-blocking (≤ PIPE_BUF, reader
present, `EPIPE` handled); CLI-installed `SPAWNING_CHILD.json` (c9) precedes the
release byte (c10). PID/start/PGID proof present at each tier. CLI death ⇒
release-write closes ⇒ g0 EOF ⇒ `_exit(3)` ⇒ lock released; middle-child death
before report ⇒ bounded `c7` timeout ⇒ `killpg(middle_child_pid)` ⇒ death
proved; every `SPAWN.lock` route (s1–s4) is bounded and non-blocking. **No
unkillable lock holder and no deadlock**, except the honestly-named deliberately
-wedged-CLI A3 residual, which cannot arise from an accidental crash (a crashed
CLI closes its `flock` fd) and never touches a running supervisor or D1.

### 4. Write/hash once

Accounted every content-byte operation: write path (§N4.1) reads from the pipe
and writes each byte once with only integer counters — **no hash**; the sole
content hash is the verification pass (§N4.2 step 3); `result_sha256` (§N4.3)
hashes canonical **metadata** only; promotion is a rename; `SETTLEMENT.json`,
the release token, `OPERATION_STATUS`, `DELIVERY_ACK`, the capacity ledger, the
custody-absence proof, and crash reconstruction never re-read a content byte
(§N4.4 enumerates this). Each content byte is thus **written once and hashed
once** — literal K1, and crash routing (before/during/after the pass) is
`SUPERVISOR_CRASH` with no partial hash and no resume. **The substitution
defense does not fully survive**, however: with the inline hash deleted there
is no stored reference, so same-inode equal-size in-place substitution before
the pass is undetected and promoted — the basis of **X212-M1**. Inode
substitution (held `r`) and size/link anomalies do survive.

### 5. Watchdog

Rejected-witness fallback has its own namespace and id binding the rejected
path+SHA-256, so the no-replace install always has a target and the rejected
object is never overwritten (§N5.1–§N5.2); `UNKNOWN` with zero current
unresolved members and `supervisor_quiescence = PROVED` is legal and routes to
all-live invalidity **with no synthesized freeze instant** (§N5.4); consumption
is one total order with `FREEZE_FALLBACK` before `FREEZE` and a fallback making
every witness for that pair non-evidence (§N5.5); the non-overdue
replacement-resume is fully conjunctive with a `.resumed.json` idempotence
marker and settles on any doubt (§N5.6). No freeze instant is invented and no
supervisor-loss resume is possible (prior-generation `REPLACEMENT_FREEZE` fails
R1 ⇒ phase 2A). The fallback is a **supervisor** fact in a path the watchdog
cannot reach ⇒ **no second watchdog authority**; the watchdog still holds no
lock/capability, writes no `runtime/`, appends no ledger, settles nothing.

### 6. FD remap

Simulated §N6.1: `(3,4)` temporaries land ≥ 5, `dup2` no-op-equivalent, close
only temporaries; `(4,3)` both descriptions duplicated to ≥ 5 **before** either
target is written, so `dup2(t_low,3)` cannot destroy the original 3 (held at
`t_high`) — the swap is correct (the case v2.1.1 got wrong); `(3,k)`/`(k,3)`/
`(4,k)`/`(k,4)` reject temporaries that land on 3/4 and re-`dup` while keeping
them open (bounded ≤ 8 because at most `{3,4,low,high}` occupy the low range);
`(j,k)` outside `{3,4}` may land temporaries on 3/4, rejected then overwritten
safely. `low==high`, non-int, absent source, non-pipe, wrong direction, and a
surviving forbidden fd each `os._exit(4)` ⇒ `BOOTSTRAP` (steps 0/6/7/8).
Inheritability set before `execv`; direction/role verified before and after
`SIGCONT`; remap precedes self-stop; failure cleanup closes every adapter-opened
fd. **Total and terminating.**

### 7. B1/GC

The priority rule (§N7.2) evaluates `a` before allocation: null ⇒ no ack;
non-null with null frontier ⇒ `INVALID`; exact frontier hash with `NEW`@m+1 ⇒
`SUCCESSOR_OCCURRENCE`, with `RETRY`@m ⇒ `CLIENT_ECHO`; any other or stale-but-
genuine ⇒ `INVALID/REPLAY_BYTES` — one result, no state movement on error. The
frontier is published on every reply, so all eight commands drain in prefix
order (≤ 64 frames) without retaining old replies. Prefix advances atomically
with ack install (§N8.1); GC is any later locked epoch after ack+prefix+archival
(§N8.2, observation form vacuous); classification tests the prefix **first**
(§N8.3), so a retry before or after GC gets the identical `ALREADY_ACKNOWLEDGED`
and a crash mid-GC completes idempotently; ack-before-archival no longer strands
GC (Sol M4). Owed replies are preserved until the acknowledged prefix records
the one-use effect (signed B1 exactly), and retention is bounded by 64 unacked +
open-transition-bounded acknowledged-unarchived, independent of polling
frequency.

### 8. Reconciliations

Absent-scope defaults pinned (§N9.1), threaded so an absent tombstone can never
make an occurrence `ALREADY_ACKNOWLEDGED` (`0 < 1 ≤ i`). Canonical empty-result
hash reconciled to `SHA-256(b"[]\n") = 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
— I recomputed it and the rejected `SHA-256(b"[]") = 4f53cda1…b945`; **both
match**, so §W4.5's canonical form (trailing newline) is now consistent.
Schemas/enums/path grammars/object ownership (§N9.3, §N10.1) add no signed
event, no constant, no resource value, no refusal/`INVALID` token; every new
object is control-plane, `scientific_outcome:false`, archival-excluded,
untracked. Import-allowlist delta **none** (verified). Signed inherited surfaces
(generic-harness v2/v2.1/v2.2/v2.3/v2.3.1; batch-settlement v1/v1.1/v1.1.1 §D1/
§D2) referenced unchanged. The one new contradiction found is X212-M1 (§N4's
detection over-claim); no other new contradiction across §N1–§N9.

---

## No-regression table

| Signed cell / surface | Status under v2.1.2 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **Not reopened; one honesty regression (X212-M1)** | New residuals honestly named (wedged CLI §N3.5, forgery §N1.5, fallback conflict §N5.5, directory swap §N4.4) — **but** §N4.2 over-claims equal-size content-substitution detection, an A3-boundary over-claim that must be corrected. |
| **B1** durable-journal ack redelivery | **Not reopened; allocation/ack/GC repaired** | §N7 frontier + §N8 later-GC repair acknowledgement priority and GC timing, not policy; §N8.3 realizes "until a durable acknowledgement" exactly. |
| **C1** dedicated freezer | **Not reopened; strengthened** | The fallback is a supervisor fact in a watchdog-unreachable namespace; §N5.6 resumes only on the supervisor's own conjunctive proof. No watchdog fact becomes a second runtime authority. |
| **D1** no idle exit | **Not reopened** | §N3 removes the last pre-identity wedge with no unbounded `flock` wait; the supervisor never waits on `SPAWN.lock`. |
| **K1** mediated transport, fixed ceiling, no replenishment | **Not reopened; hash-once now literal; complete-custody release** | §N4 write-once/hash-once, §N2 complete-set absence, five constants unmoved, no replenishment — the release authority is now constructible (§N1). The only issue is the §N4.2 detection **claim**, not the accounting. |
| Signed generic-harness composite / batch-settlement amendment | **Unchanged** | No F1–F4/R1–R4 reopened; §D1/§D2 referenced verbatim; no archival set moves. |
| Nine signed events, schemas, roots, T bands, E1/E2/E3, Q/C boundary | **Unchanged** | §N13 negative space; zero constant/event/root/token delta; import-allowlist delta none. |

**Required no-weakening conditions:** no watchdog fact is promoted to a second
authority; no A3/B1/C1/D1/K1 cell is reopened. **One fail-closed behavior is
weakened** — v2.1.1's `HASH`-quarantine on same-inode equal-size substitution
is gone (X212-M1) — which is the basis of the REVISE.

## Is a new author cell required?

**No.** X212-M1 is a bounded truthfulness edit in §N4.2 (name the case as an A3
procedural residual; keep hash-once). It introduces no constant, import,
provider, host change, or author choice, and realizes the K1/A3 cells Kirill
already signed. No new author-choice token is required, and none is unavoidable.

## Authorization boundary

Because the verdict is **REVISE**, the informed author signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **unavailable**
and is not made signable by this review. This review authorizes **no**
implementation, no commit of the untracked/dirty implementation, no T
activation, no entropy, no runtime construction (supervisor, controller,
worker, watchdog, adapter, endpoint, pipe, FIFO, journal, spawn intent,
operation, capacity artifact, custody disposition, author decision file,
capability, lease, batch), and no scientific work (world, learner, candidate, Q
attempt, Q/C object, datum, outcome, Proof, or claim movement). The smallest
correction (the §N4.2 honesty repair) must be prepared as a bounded v2.1.3
layer and receive **another independent X/Y check** on its own bytes before any
acceptance token can be considered; the author line cannot confirm its own
bytes.

## Contract versus implementation

Every finding and closure above is a property of the v2.1.2 **contract**. The
implementation is unchanged from the state prior reviews recorded:
`src/philosophia/officina/generic_harness.py` is **untracked** and contains no
supervisor, control channel, adapter, journal, operations tree, watchdog,
capacity ledger, or output transport; it neither causes nor cures any v2.1.2
contract finding.

## Custody confirmation

No process, test, or probe ran; no supervisor, controller, worker, watchdog,
adapter, endpoint, pipe, FIFO, journal, or smoke was started; this review
started no process of its own. The two recomputations were `hashlib` over
literal documented bytes in the scratchpad, touching no repository code or
runtime state. No code, test, contract, signature, prior review, or runtime
artifact was edited; nothing was committed or staged; the dirty and untracked
handover files are preserved unmodified. Exactly one new file was created —
this review. No runtime or scientific artifact was created.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. No
capability, claim, lease, batch, operation, entropy, E1/E2/E3 spend, world,
learner, candidate, Q/C object, datum, or outcome exists. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
