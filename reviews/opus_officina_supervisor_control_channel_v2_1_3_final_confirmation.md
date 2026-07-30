CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.3

Date: 2026-07-30
Reviewer line: X (adversarial Linux / process / crash / hash-construction semantics)
Review base: commit `20fd212` (HEAD), at or after required commit `45f30f6`.
Working tree dirty exactly as handed over; **nothing modified by this review.**

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.3 was authored
by **Claude Code Opus 5 in the specification-author role** (Fable 5
unavailable); the same author line wrote v2.1/v2.1.1/v2.1.2. Shared
model-family identity is not review continuity — I re-derived every disposition
from the v2.1.3 bytes. I read
`reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md` **only as
an untrusted authored self-assessment** and used none of its claims as
evidence. I do not inherit my own v2.1.2 X-line authority; the X212 findings
are re-stated from the v2.1.2 bytes and re-tested here.

## Recomputed hashes (all verified)

```text
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md   (== expected)
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
aa25b28cedd813fbd2da36e0087cc9773be86b21a96c828bde57778953933dc7  reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
22e2fb392c5758d7bab6840cafd711a9e4fa74b19b60bd5b05aebbde9b66c878  reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The v2.1.3 digest matches the expected committed value exactly. Every
inherited surface and both v2.1.2 review files are byte-identical to what
v2.1.3 cites (author-note `ae9c440…` and harness-signature `8c47da35…` also
match), so the review base is precise: v2.1.3 dispositions the two v2.1.2
confirmations whose hashes it records, and those are the files I hold.

**Method.** Static and read-only. No process, test, probe, or Officina process
ran. Four documented digests were **recomputed from the literal documented
bytes** (permitted): §U5.6's `result_sha256` (`5359c361…`, entries canonical
265 B) and `result_manifest_sha256` (`e4ec3182…`, manifest canonical 638 B),
§U8.3's operation-directory enumeration (`3f8e1c99…`), and the empty-enumeration
value (`37517e5f…` = `SHA-256(b"[]\n")`) — **all four reproduce exactly**.
Import-allowlist facts are cited from
`src/philosophia/officina/verification.py:35-38`; every primitive v2.1.3 adds
(`os.pipe2` `O_NONBLOCK`, `os.getsid`, `os.getpgid`, `os.unlink`, `os.rmdir`,
`os.fsync`) is under `os`, in the allowlist, with **zero delta**; `select`/
`selectors`/`signal`/`ctypes`/`sys` remain out.

## VERDICT

```text
CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X
```

v2.1.3 closes **X212-M1, X212-m1, and every converged Sol v2.1.2 finding (C1,
C2, M1, M2, M3, M4, m1, m2)** with exact, executable, non-circular text that I
re-derived and, where digests are given, **reproduced from the bytes**. It
introduces **no new Critical and no new Major**. It **weakens no fail-closed
behavior by a new v2.1.3 choice** — §U1 corrects a false *claim* while leaving
the hash-once *behavior* unchanged; §U3 *reduces* spurious invalidation; §U4
makes GC crash-safe; §U5 adds durable metadata. It **promotes no watchdog or
replacement fact into a second runtime authority** (§U3.3's three records are
supervisor-only objects in a namespace the watchdog cannot reach, none a freeze
instant). It **reopens no A3/B1/C1/D1/K1 cell**, and §U1.5 adds a normative bar
against any future layer silently re-violating literal hash-once.

I found two **Minor** defects (X213-m1, X213-m2), both fail-closed and
non-blocking, recorded below with bounded repairs for a future housekeeping
pass. Under the confirmation standard (no surviving Critical or Major, and the
required question satisfied), the correction is confirmable.

Accordingly, the X-line authorizes Kirill's informed author signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` — see the exact
Authorization boundary below (it becomes signable only once the independent
Y-line also confirms these same v2.1.3 bytes, and it authorizes nothing beyond
the signature).

---

## One-to-one disposition

### Opus X212

| Finding | v2.1.3 locus | Verdict | Basis (re-derived) |
|---|---|---|---|
| **X212-M1** hash-once repair over-claimed equal-size content-substitution detection | §U1.1–§U1.4 | **CLOSED** | The `# equal-size content substitution defence` comment and the "fully retained" sentence are **deleted** (§U1.1). §U1.2 is an honest detection truth table: inode substitution, hard-link, truncation/extension, short/long read and wrong-offset EOF are detected (each by the exact held-descriptor/length/EOF check), and same-inode equal-size in-place modification **before, during, and after** the pass is marked **NO — nothing**, with the reason stated (no earlier trusted reference; the second hash literal K1 forbids). §U1.4 relabels the step-3 anomaly as `LENGTH`/`EOF`, never content-substitution. Literal hash-once counts are unchanged (§N4 carried), so no fail-closed behavior is newly weakened; the previously-silent weakening is now the honestly named A3-R1 residual. |
| **X212-m1** the hash-once/detection tension must be recorded so no later layer silently re-violates it | §U1.5 | **CLOSED** | §U1.5 states the tension and adds a **normative consequence**: "No later layer may re-introduce equal-size content-substitution detection by adding a second hash of any output content byte, or by storing a content-derived reference computed outside the sole pass, without a new author decision on K1." Exactly the recorded bar X212-m1 asked for. |

### Sol v2.1.2

| Finding | v2.1.3 locus | Verdict | Basis |
|---|---|---|---|
| **Sol C1** first-fork record is not a valid PGID before `setsid()` | §U2.1–§U2.7 | **CLOSED** | A two-stage gate is inserted. `SPAWNING_MIDDLE.json` (c7) makes **no** group claim; `SPAWNING_GROUP.json` with `group_verified:true` (c11) is installable **only after** c10's kernel proof (`getsid`/`getpgid(middle_child_pid)==middle_child_pid`). Pre-`setsid` kill is `kill(pid_mid)` **only** — `killpg` is forbidden until c11 (§U2.5), removing the "kill an unrelated group / `ESRCH`" defect. The `c4→c7` pre-record window is covered by the middle child's literal-first-instruction bounded gate read (`m0`, `O_NONBLOCK`, bounded by `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`), which writes nothing and changes no shared state, so it self-exits with **no record needed**. The residual (a *deliberately* `SIGSTOP`ed middle child inside the sub-second-to-10 s `m0` window) is honestly named A3 procedural and is strictly narrower than v2.1.2's unbounded exposure. |
| **Sol C2** non-overdue watchdog-replacement resume is unreachable and dual-valued | §U3.1–§U3.4 | **CLOSED** | The carried §W3.5 action is **explicitly replaced** for non-overdue groups: a swap-only freeze writes **only** a `REPLACEMENT_FREEZE` record and **no** §W3.3 witness and no fallback (§U3.1), removing the unreachability (the witness R4 forbade no longer exists). Three **mutually exclusive** states with `INVALID`-before-`RESUMABLE` precedence (§U3.2) replace the "any failed conjunct ⇒ invalidity" rule; `ACK_PENDING` is an explicit non-invalid held-frozen state bounded by `min(deadline, updated+absence_timeout)`, resolving the dual-valued pending-ack contradiction. No healthy non-overdue group with ≥ ~11 s remaining lease is invalidated; only a genuine deadline miss (I1) during the bounded replacement invalidates — an honest infrastructure invalidity that is *narrower* than v2.1.2, not a new forced-invalid. |
| **Sol M1** crash-mid-GC not completable if `ack.json` deleted first | §U4.1–§U4.3 | **CLOSED** | Exact deletion order with **`ack.json` last** (D1 accepted → D2 committed → D3 reply → D4 fsync → D5 ack → D6 fsync → D7 rmdir → D8 fsync), eligibility verified before the first unlink; the "no deletion order needed" claim is deleted. Every pre-D5 cut keeps `ack.json` so G1 re-derives and the later epoch resumes at D1 (ENOENT-tolerant); every post-D5 cut leaves an empty directory completed by the explicit empty-directory `rmdir` rule. No state is permanently non-GC-able (§U4.2). `rmdir ENOTEMPTY`/other `errno` route to record-first invalidity. |
| **Sol M2** authority refers to per-file hashes not in `SETTLEMENT.json` | §U5.1–§U5.6 | **CLOSED** | A durable immutable `RESULT_MANIFEST.json` carries the sorted `{relative_path, byte_length, content_sha256}` tuples, built from the sole-pass **in-memory** tuples (zero content reread), installed **before** `SETTLEMENT.json`, which gains exactly one key `result_manifest_sha256`. The verifier (V1–V6) resolves the manifest without opening any content file; the DAG is forward. I **reproduced** `result_sha256=5359c361…` and `result_manifest_sha256=e4ec3182…` from the bytes. The L2 allowed-record set gains `RESULT_MANIFEST.json` (§U5.5) so a promoted operation's own disposition is not refused. |
| **Sol M3** singleton spawn-record conflicts/cleanup incomplete | §U6.1–§U6.5 | **CLOSED** | Preflight P0–P3 (absent / malformed-fail-closed / live-idempotent-or-conflict / dead-remove), `EEXIST` continuations at all four no-replace installs (§U6.2), and one exact **child→group→middle→spawning** ordered removal with `fsync`s, ENOENT-tolerant, that **never omits `SPAWNING_CHILD.json`** (the v2.1.2 `c7` wedge). Malformed records are fail-closed (nothing unlinked, nothing killed); PID reuse ⇒ never kill. Child-first order makes every crash-mid-removal prefix-consistent. |
| **Sol M4** author `signed_utc` not bound to `authorized_utc` | §U7.1–§U7.4 | **CLOSED** | Conjunct 8e: `authorized_utc == signed_utc` **byte-for-byte** (30 ASCII chars), plus a pinned grammar and real-date check (no leap second). No independent timestamp remains outside the content-closed authority; other timestamps are supervisor-observed, non-authority (§U7.4). |
| **Sol m1** `custody_locations_proved` cannot list exact L4/L5 strings | §U8.1–§U8.3 | **CLOSED** | Replaced by a fixed five-token `custody_proof_classes` array (pinned order), two fixed `custody_proof_roots`, and `custody_proof_enumerations` (root/operation-directory enumeration hashes with exact `null` semantics). Diagnostic only; never narrows P1–P7 (§U8.2). I **reproduced** the enumeration hash `3f8e1c99…`. |
| **Sol m2** post-verification in-place window not named beside the directory swap | §U1.3 | **CLOSED** | §U1.3 names **three** A3 procedural residuals: A3-R1 (before/during pass), A3-R2 (after pass, before settlement/rename), A3-R3 (directory swap). None is claimed detected; none routed to `HASH`; the pass never claims future immutability. |

---

## The eight required attack traces

### 1. Hash truthfulness

I searched the carried chain for any surviving equal-size same-inode detection
or future-immutability claim. §N4.2's over-claim comment and sentence are the
only such statements, and both are deleted/replaced (§U0, §U1.1). §U1.2's truth
table matches §N4's actual behavior exactly, row by row: step 2's `(st_dev,
st_ino)`/`st_nlink`/`st_size` against the held `r`, step 3's read-length and
EOF-offset, and §N4.1's pre-creation header validation. The three residual
windows (A3-R1/R2/R3, §U1.3) precisely cover the un-detected cases and are
non-citable A3 procedural, never routed to `HASH`. §U1.5 forbids any future
second-hash re-introduction without a new K1 decision. **Truthful and total.**

### 2. Two-stage spawn

Traced every cut in §U2.6. Four sealed channels; `rel1`/`rel2` are `O_NONBLOCK`
on both ends so the middle child's `m0`/`m5` gates are bounded by
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` regardless of write-end copies; `rel3` keeps
v2.1.2's blocking-read + EOF design, sound because the middle child closes its
`rel3` write copy at `m1` **before** the second fork, so the CLI is the
grandchild's only `rel3` writer. Pre/post-`setsid` is separated: `m2` `setsid`,
`m3` self-verify `getsid==getpgid==getpid`, `c10` independent kernel
re-verification before `group_verified:true`. Kill discipline is per-tier:
`kill(pid_mid)` only before c11, `killpg(process_group_id)` only after the
kernel-proved group (§U2.5); PID reuse ⇒ start-identity mismatch ⇒ no kill.
Every lock reference is released by bounded self-exit, proved kill against a
durable record, or process death (§U2.6 invariant). No unbounded `flock` wait
and no deadlock (the boot pipe carries two ordered reports read at c9/c13; each
gate is released by the CLI after it reads the prior report). Residuals (wedged
CLI; deliberately-`SIGSTOP`ed middle child in the bounded `m0` window) are
honestly named A3 procedural, and D1 never depends on a client. **No unkillable
lock holder, no deadlock** (one prose imprecision noted as X213-m2).

### 3. Watchdog replacement

Overdue vs swap-only are disjoint by construction (§U3.1): overdue ⇒ the
existing §W3.3/§W3.4 witness+invalid route; non-overdue ⇒ swap-only, **no**
witness, no `freeze_ns`, no `overrun_ns`, no fallback. `INVALID` (I1–I7) is
evaluated **before** `RESUMABLE` (I-before-S), and `ACK_PENDING` is the only
remaining state (§U3.2). Totality: a healthy non-overdue group is
`ACK_PENDING`→`RESUMABLE`; the only reachable invalidity from a swap is a real
deadline miss (I1) or replacement-watchdog failure (I2), each bounded by
`min(deadline, updated+absence_timeout)`; every I1–I7 writes an immutable
`.invalidated.json` naming the exact condition, and crash after it resumes the
signed route with no re-classification (§U3.4). No freeze instant is invented
(`supervisor_stop_monotonic_ns` is never an `overrun_ns` and never a witness,
§U3.3). No supervisor-loss resume (I7 ⇒ INVALID ⇒ phase 2A). All three records
are **supervisor**-written under the lock in a namespace the watchdog cannot
reach ⇒ **no second authority**. **Disjoint, total, and healthy-safe.**

### 4. GC

Eligibility (G1 ack durable, G2 `i ≤ prefix`, G3 archival predicate) is
verified **before** the first deletion (§U4.1 D0), then the exact order
accepted→committed→reply→(fsync)→**ack**→(fsync)→rmdir→(fsync). Every crash
prefix is proved (§U4.2): before D5 keeps `ack.json` (G1 re-derives); at/after
D5 the directory is empty and the predicate-free empty-directory rule completes
it. Retry concurrency serializes under `T_RUNTIME.lock` and prefix-first
classification (§N8.3) makes GC timing invisible. Empty-directory completion is
the one GC step not requiring G1, and it is safe because "ack absent ⟺ all
phase files already deleted" (ack is last). No owed reply or eligibility
witness is lost (the tombstone is never deleted; §N8.3 answers
`ALREADY_ACKNOWLEDGED` at every cut). **Crash-completable and total.**

### 5. Result manifest

Schema/order/DAG verified: sole-pass in-memory tuples → canonical `entries` →
`result_sha256`; manifest bytes → `result_manifest_sha256`; both bound in
`SETTLEMENT.json` (the sole commit point), installed **after** the manifest
(§U5.2). Zero content rereads anywhere (§U5.4 V1–V6 open no output file;
§N4.4's "why no later path hashes content" list carries forward with the
manifest as a metadata-only reader). Empty case → `37517e5f…`; quarantined-with
-no-manifest → V6 reduced set. **I reproduced `5359c361…`, `e4ec3182…`, and the
empty value exactly.** One narrow crash-state disposition gap (QUARANTINED
*with* an orphan manifest) is X213-m1 below — fail-closed, Minor.

### 6. Singleton records

Preflight over spawning/middle/group/child in child→group→middle→spawning order
(§U6.1); every `EEXIST` branch resolved by re-reading + P1/P2/P3 (§U6.2, never
overwrite); ten record states tabulated (§U6.5) covering absent, malformed
(fail-closed, nothing killed/unlinked), live-idempotent, live-conflict,
dead/absent/Z, PID-reused (never kill), and aged. Ordered removal with
per-step `fsync` and ENOENT tolerance, never omitting `SPAWNING_CHILD.json`
(§U6.3). Takeover extends the stale-endpoint list under the same discipline
(§U6.4), unlinking no durable `runtime/`/journal/capacity/promoted evidence. No
live unlink and no stale wedge. **Total.**

### 7. Authority summaries

Timestamp equality is byte-for-byte with a pinned 30-char grammar and a
real-date check (§U7). The custody-proof summary is a fixed five-token class
array in pinned order with fixed root strings and enumeration hashes (`null`
exactly when a root/directory is proved absent), diagnostic-only and
non-narrowing of P1–P7 (§U8.2). The scientific-field exclusion runs over the
whole manifest and the operation-bound identifier set (§U5.4 V4–V5). **I
reproduced the enumeration hash `3f8e1c99…` and the empty enumeration
`37517e5f…`.** Deterministic.

### 8. No regression

Every independently closed prior repair carries forward verbatim (§U0's carried
list: §N1.1–1.4/1.7/1.8, §N2, §N4.1/4.3, §N5.1–5.5, §N6, §N7, §N8.2, §N9, and
the whole v2/v2.1/v2.1.1 chain). Zero new constants; five signed `T_OUTPUT_*`
unmoved; nine signed events, E1/E2/E3, roots, T bands, Q/C boundary unchanged;
import-allowlist delta **none** (verified). Signed generic-harness
(v2.3.1) and batch-settlement (v1.1.1, §D1/§D2) referenced unchanged. No signed
archival set changes (all new objects archival-excluded/untracked). T inactive.

---

## New findings (both Minor, non-blocking)

### X213-m1 (Minor) — the result-manifest verifier does not cleanly cover a QUARANTINED terminal that carries an orphan manifest

**Locus.** §U5.4 V6 ("for a QUARANTINED terminal **with no manifest**…"),
against §U5.2 / §U10's own "crash after `RESULT_MANIFEST.json`, before
`SETTLEMENT.json` ⇒ `SUPERVISOR_CRASH` quarantine; the manifest is an orphan
immutable record."

**Gap.** A `SUPERVISOR_CRASH` between the manifest install and `SETTLEMENT.json`
(one lock epoch, two consecutive no-replace installs) yields a **QUARANTINED**
operation that **has** a `RESULT_MANIFEST.json` but **no** `SETTLEMENT.json`. A
later capacity disposition of that operation hits V2/V3, which bind the manifest
to `SETTLEMENT.json`'s `result_manifest_sha256`/`result_sha256` — absent for a
quarantined terminal — while V6's reduced path requires "no manifest," which is
false here. Neither branch matches, so the verifier refuses.

**Failure scenario.** After such a crash, the author removes the operation's
`out/` custody and offers a valid disposition; the verifier cannot resolve the
orphan manifest and refuses, so the operation's `bytes_reserved` (up to
268 MiB) can never be released. This is **fail-closed** (no wrong release, no
accounting corruption, no exactly-once impact) and narrow (a crash in that exact
intra-epoch window), but it strands capacity for such operations, and enough of
them could in principle press the 32 GiB aggregate.

**Smallest bounded repair.** Extend V6 to: "for a QUARANTINED terminal, any
present `RESULT_MANIFEST.json` is an **orphan** not bound to a settlement; V2/V3
are skipped, the manifest's own bytes need not match any settlement, and the
prohibited-value set is `{charge_event_sha256, lease_sha256}` plus every
`content_sha256`/`relative_path` in the orphan manifest **if present**." One
clause; no new constant, import, or author choice; keeps the scientific-field
exclusion total.

### X213-m2 (Minor, prose) — the `m0` "sees EOF" crash-row phrasing is inaccurate; the governing rule (the bound) is correct

**Locus.** §U2.6 row "after `c4`, before `c7`": "CLI death: its `rel1` write end
closes ⇒ `m0` sees EOF ⇒ `_exit(3)`."

**Observation.** During `m0` the middle child still holds its **own** inherited
`rel1` write copy (it does not close it until `m1`, which is after `m0`), so it
is a writer on `rel1` and CLI death alone does **not** deliver EOF to the `m0`
read. The actual liveness guarantee is `m0`'s `O_NONBLOCK` bound, which §U2.1
correctly designates as primary ("the bound, not EOF, is its primary liveness
guarantee"). So the outcome (`_exit(3)` within
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`) is correct and total; only the stated
mechanism in that one cell is imprecise. Contrast `g0`/`rel3`, where EOF *is*
reliable because the middle child closes `rel3`'s write end at `m1` before the
second fork. **Smallest repair:** in that row, replace "sees EOF" with "sees EOF
or (holding its own `rel1` write copy until `m1`) hits the `m0` bound," so the
mechanism matches §U2.1. No behavioral change.

No new Critical or Major survived re-derivation.

---

## No-regression table

| Signed cell / surface | Status under v2.1.3 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **Not reopened; honesty gained** | §U1.3 names three procedural residuals where v2.1.2 over-claimed one detection; §U2.7 names the two bootstrap residuals. Still not a security boundary. |
| **B1** durable-journal ack redelivery | **Not reopened** | §U4 changes only the physical deletion order; §N8.3 prefix-first classification (signed B1's "until a durable acknowledgement") is untouched. |
| **C1** dedicated freezer | **Not reopened; strengthened** | §U3's three replacement records are supervisor objects the watchdog cannot reach; none is a freeze instant; `ACK_PENDING` creates no evidence and no terminal. No second runtime authority. |
| **D1** no idle exit | **Not reopened** | §U2 removes the last unrecorded lock-holder window with no unbounded wait; no supervisor waits on `SPAWN.lock`. |
| **K1** mediated transport, fixed ceiling, no replenishment | **Not reopened** | Five constants unmoved; no replenishment; literal write-once/hash-once **counts** unchanged; §U1 corrects only the *claim*; §U1.5 bars a future second-hash re-violation; §U5 durable metadata rereads no content byte. |
| Signed generic-harness composite / batch-settlement amendment | **Unchanged** | Referenced verbatim; no F1–F4/R1–R4 reopened; §D1/§D2 intact. |
| Nine signed events, schemas, roots, T bands, E1/E2/E3, Q/C boundary, imports | **Unchanged** | §U12 negative space; zero constant/event/root/token/import delta. |

**Required no-weakening conditions:** no fail-closed behavior is weakened by a
new v2.1.3 choice (X213-m1 is *more* fail-closed); no watchdog/replacement fact
is promoted to a second authority; no A3/B1/C1/D1/K1 cell is reopened; no
healthy non-overdue group is forced invalid by a new choice (v2.1.3 *reduces*
the invalidation scope relative to v2.1.2).

## Author-cell determination

**No new author cell is required, and none is unavoidable.** Every §U repair is
mechanical over the already-signed A3/B1/C1/D1/K1 policy: a truthful detection
boundary that keeps literal hash-once (§U1); a middle-child gate and verified
group identity (§U2); a swap-only/deadline split with three exclusive states
(§U3); an ordered crash-completable GC (§U4); a durable result manifest built
from the sole pass (§U5); totalized singleton-record lifecycle (§U6); a
byte-bound author timestamp (§U7); and a deterministic diagnostic proof summary
(§U8). §U1.5's normative bar makes explicit that the *only* way to reintroduce
equal-size content-substitution detection would be a new K1 author decision —
which this correction does not take and does not need.

## Authorization boundary

This is the **X-line** confirmation. It authorizes **only** that Kirill's
informed author signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

may be signed **once the independent Y-line confirmation of these same v2.1.3
bytes is also on record** (the programme requires both X and Y; the authorship
note pins X = Opus 4.8, Y = GPT-5.6 Sol). It authorizes **nothing else**: no
implementation, no commit of the untracked/dirty implementation, no T
activation, no entropy, no runtime construction (supervisor, controller,
worker, watchdog, adapter, endpoint, pipe, FIFO, journal, spawn record, result
manifest, replacement-freeze record, operation, capacity artifact, custody
disposition, author decision file, capability, lease, batch, promoted object),
and no scientific work (world, learner, candidate, Q attempt, Q/C object, datum,
outcome, Proof, or claim movement). Signing the amendment token does **not** by
itself activate T or authorize any spend; those remain behind their own signed
gates. The two Minor findings (X213-m1, X213-m2) are non-blocking and are
recommended for a future bounded housekeeping pass; neither requires an X/Y
re-review cycle on its own, but if the author elects to patch them, the patched
bytes would take a fresh confirmation.

## Contract versus implementation

Every finding and closure above is a property of the v2.1.3 **contract**. The
implementation is unchanged from the state prior reviews recorded:
`src/philosophia/officina/generic_harness.py` is **untracked** and contains no
supervisor, control channel, adapter, journal, operations tree, watchdog,
capacity ledger, result manifest, or output transport; it neither causes nor
cures any v2.1.3 contract finding, and it remains uncommittable.

## Custody confirmation

No process, test, or probe ran; no supervisor, controller, worker, watchdog,
adapter, endpoint, pipe, FIFO, journal, or smoke was started; this review
started no process of its own. The four recomputations were `hashlib`/`json`
over literal documented bytes in the scratchpad, touching no repository code or
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
