CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_X

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.4

Date: 2026-07-31
Reviewer line: X (adversarial Linux / process / crash / hash-construction semantics)
Review base: commit `f98e7bb` (HEAD), whose parent is the required
`d6be6b246e853dacb2ce209b2341dfd0d5313da0`. Working tree dirty exactly as
handed over; **nothing modified by this review.**

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.4 was authored
by **Claude Code Opus 5 in the specification-author role** (Fable 5
unavailable); the same author line wrote v2.1/v2.1.1/v2.1.2/v2.1.3. Shared
model-family identity is not review continuity — I re-derived every disposition
from the v2.1.4 bytes. I read
`reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md` **only as
an untrusted authored self-assessment** and used none of its claims as
evidence.

**Disclosure of my own prior miss.** On the X line I *confirmed* v2.1.3 while
recording only two Minors; the independent Y line (Sol) correctly **revised**
it, catching a Critical I missed — `boot_pipe`/`rel3` were created **blocking**
(`os.pipe2(0)`) while c9/c13 claimed a bounded nonblocking poll, so the
middle-death/grandchild-live cut at c13 deadlocked with `SPAWN.lock` held. The
two-reviewer system worked. I have therefore re-traced the bootstrap-pipe area
of v2.1.4 with particular care, from the raw descriptor/flag ownership, and
independently reproduced the timestamp arithmetic Sol corrected.

## Recomputed hashes (all verified)

```text
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md   (== expected)
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
6cc52972e6229005f98d15db0fac113a77d2c2382133cc745f387fced845b008  reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
214ac0d5fb1cecf873e8b91ca95079dc67df8018762a18df46e94cb912d7df75  reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The v2.1.4 digest matches the expected value exactly. Every inherited surface
and both v2.1.3 review files are byte-identical to what v2.1.4 cites
(author-note `ae9c440…` and harness-signature `8c47da35…` also match). The
review base is precise: v2.1.4 dispositions the two v2.1.3 confirmations whose
hashes it records, and those are the files I hold.

**Method.** Static and read-only. No process, test, probe, smoke, or Officina
process ran. I recomputed the §V214.7 decision-file arithmetic from the literal
bytes: line 8 = **43** bytes incl. LF, per-line lengths `[53,58,60,91,79,81,39,43]`,
total **504**, hashing to `0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f`
(**unchanged** — v2.1.3's "44" was a documentation error over an already-correct
504-byte file). The carried §N1.8 / §U5.6 / §U8.3 digests are unchanged by
v2.1.4 and I reproduced them in the v2.1.2/v2.1.3 reviews. Import-allowlist
facts are cited from `verification.py:35-38`; every primitive v2.1.4 adds
(`os.pipe2` `O_NONBLOCK`, `os.read`, `os.write`, `os.close`, `os.unlink`,
`os.rmdir`, `os.fsync`, `os.fpathconf`) is under `os`, in the allowlist, **zero
delta**; `select`/`selectors`/`signal`/`ctypes`/`sys` remain out.

## VERDICT

```text
CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_X
```

v2.1.4 closes **X213-m1, X213-m2, and every v2.1.3 Y-line finding (Sol C1, C2,
M1, M2, M3, M4, m1)** with exact, executable, non-circular text that I
re-derived and, where arithmetic is given, reproduced from the bytes. **Every
v2.1.3 closure I independently confirmed is carried forward unmodified** except
at the precise loci that carried a residual defect; those changes are
completions/corrections, not regressions (§V214.0's replacement index is exact
and I checked each row). It introduces **no new Critical and no new Major**. It
**weakens no fail-closed behavior** (the A3 statement becomes strictly more
honest; §V214.2 *restores* a K1 release route v2.1.3 had made impossible; GC
now *preserves* the G3 authority; the lock order is disambiguated; the watchdog
partition is *totalized*). It **promotes no watchdog or replacement fact into a
second runtime authority** (§V214.5.4's marker fields are supervisor bookkeeping
in a namespace the watchdog cannot reach, and `diagnostic_conditions` is proved
routing-irrelevant). It **reopens no A3/B1/C1/D1/K1 cell**.

Accordingly the X-line authorizes Kirill's informed author signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` — see the exact
Authorization boundary (it becomes signable only once the independent Y-line
also confirms these same v2.1.4 bytes, and it authorizes nothing beyond the
signature).

---

## One-to-one disposition

### Opus X213 (my v2.1.3 Minors)

| Finding | v2.1.4 locus | Verdict | Basis |
|---|---|---|---|
| **X213-m1** result-manifest verifier did not cover a QUARANTINED terminal carrying an orphan manifest (fail-closed capacity strand) | §V214.2 | **CLOSED** | `QUARANTINE.json` gains `result_manifest_sha256_or_null` (non-null iff a durable manifest exists at install, §V214.2.1); a record-first reducer installs the bound terminal for the crash-after-manifest state (§V214.2.2 Q1–Q4, idempotent no-replace); the verifier splits into three exclusive branches (§V214.2.3) — `B-P` settled, `B-QM` quarantined-with-manifest (the new, previously-missing branch), `B-QN` quarantined-no-manifest. An orphan-manifest quarantine is now disposable via `B-QM` (release exactly `bytes_reserved` after the P1–P7 absence proof, no settlement, no content reread). This is the Critical Sol independently rated C2. |
| **X213-m2** `m0` "sees EOF" crash-row prose was imprecise (the middle child holds its own `rel1` write copy until `m1`) | §V214.1.5 | **CLOSED** | The row is replaced to state that the governing guarantee at that cut is the `m0` **bound**, not EOF, and the descriptor ownership table (§V214.1.2) makes the `rel1`-write dual-ownership explicit. |

### Sol v2.1.3

| Finding | v2.1.4 locus | Verdict | Basis (re-derived) |
|---|---|---|---|
| **Sol C1** `boot_pipe`/`rel3` blocking ⇒ c13 deadlock; unpinned pipe errno branches | §V214.1 | **CLOSED** | All four channels are now `os.pipe2(os.O_NONBLOCK)` (§V214.1.1) with `PC_PIPE_BUF ≥ 4096` verified per write end; two pinned helpers `BOUNDED_READ`/`BOUNDED_WRITE` cover every errno (`EAGAIN` paced retry, `EINTR` retry, `EOF_INCOMPLETE`, `MALFORMED`, `FRAME_LENGTH`, `TRAILING_BYTES`, `READ_ERROR`, `WRITE_ERROR`, `PEER_GONE`) with an exact stage-route map for `c8/c9/c12/c13/c16/m0/m4/m5/m8/g0` (§V214.1.3–§V214.1.5). **I re-traced Sol's exact deadlock cut**: middle dies between `m7` and `m8` with the grandchild holding a `boot` write copy ⇒ no EOF, but `c13`'s bound is now *executable* on the nonblocking descriptor ⇒ stage-2 `killpg(process_group_id)` reaches the grandchild (same verified group) ⇒ death proved ⇒ ordered removal ⇒ lock released. No deadlock. The confirmed EOF properties (`rel3` sole-CLI-writer, `rel2` post-`m1` closure) are preserved and become early exits; the `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` grandchild-gate bound is a derived arithmetic, not a new constant. |
| **Sol C2** orphan-manifest quarantine could never satisfy the disposition verifier | §V214.2 | **CLOSED** | as X213-m1 above — the `B-QM` branch restores the signed K1 release route without settlement or content reread. |
| **Sol M1** GC deleted `accepted.json` first, destroying the command/`effect_plan` needed to re-select the G3 predicate | §V214.3 | **CLOSED** | Order is now `committed → reply → ack → accepted` (accepted **last**, §V214.3.1) with a `D6` finalization step. The permanent tombstone prefix (`i ≤ acknowledged_prefix_occurrence`) is the durable acknowledgement proof, so `ack.json` may precede `accepted.json`; `accepted.json` survives to last so the per-command G3 binding (§V214.3.3 table) is always re-selectable. §V214.3.2 proves every crash prefix re-derives eligibility from only the files then present plus the permanent tombstone — resolving both the v2.1.2 (ack) and v2.1.3 (accepted) forms of this defect. No owed reply is deleted before acknowledgement (`reply` at `D2`, strictly after `D0` proved `i ≤ prefix`). |
| **Sol M2** singleton preflight was ordered both "under `SPAWN.lock`" and "before acquiring" it | §V214.4 | **CLOSED** | Single order: `c1a` acquire, `c1b` preflight under the acquired lock, `c2` install (§V214.4.1). The unlocked stuck-holder route now **kills but removes nothing** (§V214.4.2); every mutating P2a/P3 and every `EEXIST` continuation runs under the held lock (§V214.4.3). No unlocked mutation can race the current holder. |
| **Sol M3** watchdog replacement partition/marker not total (priority, I2 "any table_seq", S1-true/S2-false gap) | §V214.5 | **CLOSED** | Pinned priority `I1→I7`, first-true recorded plus a routing-irrelevant sorted `diagnostic_conditions` (§V214.5.1, §V214.5.4); `I2` now requires a *valid* ack of the *exact current* `table_seq` (stale/wrong-table/wrong-generation/malformed never satisfies; `os.fork` failure fires it immediately, §V214.5.2); `I3` absorbs every pre-resume member state other than exactly `T`, so `¬S2 ⇒ I3` and the three-step partition (§V214.5.3) is exhaustive and disjoint. I checked all fifteen race rows (§V214.5.5): each yields exactly one state, none zero or two. |
| **Sol M4** A3-R1 still claimed a during-pass hash "describes the promoted bytes" | §V214.6 | **CLOSED** | `A3-R1` is split into `A3-R1a` (completed-before-pass) and `A3-R1b` (concurrent-with-pass); the promoted-byte claim is **deleted**. §V214.6.1: the hash claims only "the exact byte stream read," with no claim it equals any single file state or the promoted bytes. `A3-R1b` explicitly names the mixed-stream possibility. All four residuals are A3-procedural, non-citable, no `HASH` route; literal hash-once counts unchanged. |
| **Sol m1** decision-file line-8 documented as 44 bytes | §V214.7 | **CLOSED** | Corrected to **43** incl. LF; **I reproduced** the per-line lengths, the 504-byte total, and the unchanged hash `0773f29c…`. |

**Carry-forward integrity.** Every closure I confirmed in v2.1.3 (X212-M1/m1
and the whole carried v2/v2.1/v2.1.1/v2.1.2 chain) is preserved: the acyclic
disposition authority, complete custody set, fallback namespace, fd remap,
acknowledgement priority, absent defaults, empty-result hash, two-stage-gate
*structure*, swap-only/deadline split, result-manifest object, singleton
preflight *semantics*, and byte-bound timestamp are all carried verbatim, with
changes confined to §V214's named loci (I verified §V214.0 row-by-row against
the replacement index).

---

## The eight required attack traces

### 1. Bootstrap pipes and spawn cuts

All four channels `O_NONBLOCK` at creation (§V214.1.1); `PC_PIPE_BUF ≥ 4096`
verified per write end. Every read/write errno has one continuation via the two
pinned helpers (§V214.1.3–§V214.1.4): `EAGAIN` = paced retry against the same
deadline (never an error), `EINTR` = immediate retry, EOF-incomplete /
malformed / overlong / trailing / other-errno = the stage's fail-closed route,
`EPIPE` = `PEER_GONE`. I re-ran death at every instruction (§V214.1.5 table)
against the descriptor ownership table (§V214.1.2): no inherited descriptor
wedges the lock, because for each gate the guarantee is either a guaranteed EOF
(`rel2`/`rel3`, where the middle child closed its write copy at `m1`) or the
bound (`rel1`/`m0` and `boot`/`c13`, where a writer copy persists). **The
middle-death/grandchild-live `c13` cut is closed**: nonblocking `boot` makes the
bound executable ⇒ stage-2 `killpg` reaches the grandchild ⇒ ordered removal ⇒
lock released. The two named A3 residuals (deliberately stopped CLI / middle
child in the bounded `m0` window) are unchanged and not enlarged. *(Inherited,
non-blocking, not a v2.1.4 finding: `c17`'s identity poll and the grandchild's
`g2` first-ack wait share the 10 s bound; a spurious `c17` expiry is fail-closed
`REFUSED`/`BOOTSTRAP`, and the in-process watchdog acks in ~ms, so it is not
reachable in practice; v2.1.4 changes neither.)*

### 2. Manifest quarantine branches

`B-P`/`B-QM`/`B-QN` are selected by durable objects alone and are exclusive:
`B-P` iff `SETTLEMENT.json`; `B-QM` iff `QUARANTINE.json` with non-null binding;
`B-QN` iff `QUARANTINE.json` with null binding; every other combination REFUSES
(both durable ⇒ record-first invalidity; neither ⇒ no terminal; `B-QM` with the
manifest physically absent, or `B-QN` with it present ⇒ refuse) (§V214.2.3).
Bindings cannot be forged (both `QUARANTINE.json` and `RESULT_MANIFEST.json`
are supervisor-only, immutable no-replace), replayed (`.disposed.json`
no-replace, single use), missing (`B-QM` requires physical presence + hash
match `QM1/QM2`), or satisfied by the wrong manifest (`QM2` binds to the
quarantine record's hash; wrong bytes ⇒ mismatch ⇒ refuse). A valid
orphan-manifest quarantine releases custody via `QM1–QM6` with no settlement and
no output reread (`QM6`), after P1–P7 prove every custody class absent. Total
and exclusive over admitted states.

### 3. B1 garbage collection

Order `committed → reply → ack → accepted`, accepted last (§V214.3.1). The
permanent tombstone prefix survives every deletion and is the durable
acknowledgement authority; `accepted.json` (command + `effect_plan`) survives to
`D7` and is the durable G3-predicate authority. §V214.3.2: at every cut before
`D7`, `accepted` is present so G3 is re-selectable; at `D4→D7` the finalization
rule `D6` re-derives prefix + G3 from `accepted`; at/after `D7` the empty
directory is completed by the predicate-free `rmdir`. No command/effect
authority is lost before the last deletion; no reply survives without
`accepted`; no owed reply is deleted before `i ≤ prefix`. Prefix-first
classification (§N8.3) makes every retry `ALREADY_ACKNOWLEDGED` regardless of
which phase files exist, so exactly-once holds at every crash prefix. A fresh
not-yet-committed `accepted`-only directory is not mis-finalized because `i >
prefix` for an unacknowledged occurrence.

### 4. Singleton lock order

`c1a` acquire precedes `c1b` preflight and every mutating/adopting read
(§V214.4.1); the normative rule forbids any adoption/removal/kill/mutation
before `c1a`. The unlocked stuck-holder route (`s1`–`s5`) performs only
read/validate/kill(identity-proved, tier-permitted)/prove-death/retry and
**removes nothing** (§V214.4.2); removal happens at `c1b` under the acquired
lock. Every `EEXIST` (`c2/c7/c11/c15`), PID-reuse (never kill on start-identity
mismatch), malformed (fail-closed, nothing unlinked/killed), live/dead, and
crash/retry path is single-valued under the held lock (§V214.4.3, §U6 carried).

### 5. Watchdog partition

`I1→I7` in pinned order, first-true recorded (§V214.5.1); `I2` requires a valid
exact-current-`table_seq` ack by the bound (stale/wrong/malformed never
satisfies it; fork failure fires it immediately, §V214.5.2); `I3` absorbs every
pre-resume member state other than `T`, so no S1-true/S2-false gap remains
(§V214.5.3 proves `¬S2 ⇒ I3`). Every I routes to the identical signed all-live
invalid route; no clause reads `invalid_condition`, so the sorted
`diagnostic_conditions` set cannot affect routing (§V214.5.1). I re-ran all
fifteen race rows (§V214.5.5) including the two v2.1.3 gaps (row 6 running-member
⇒ I3; row 14 stale-ack-only ⇒ I2): each is single-valued; none zero or two. No
healthy non-overdue group is invalidated by a pending ack.

### 6. A3 hash truth

§V214.6.1: the hash claims only "the exact byte stream read," with **no** claim
it equals what the worker sent, any single file state, or the promoted bytes.
The during-pass mixed-stream case is named `A3-R1b` and explicitly need not
equal any file state or the promoted inode (§V214.6.2/§V214.6.3). I searched the
carried chain: no surviving text restores a stronger claim (the §U1.1
promoted-byte sentence is replaced; §U1.3's `A3-R1` block is replaced). All four
residuals are A3-procedural with no `HASH` route and no outcome-responsive
branch; the detected anomalies keep the `HASH` class exactly as carried
(§U1.4).

### 7. Schemas and arithmetic

Two one-key extensions only: `t-operation-quarantine.v1` gains
`result_manifest_sha256_or_null` (64-hex-or-null, three-case-free by
construction) and `t-replacement-invalidation.v1` gains `diagnostic_conditions`
(sorted array over the closed `I1–I7` set). Both are closed, canonical, and
sufficient for their verifier/marker duties. I reproduced the timestamp
arithmetic: line 8 = 43 bytes incl. LF, total 504, decision-file hash unchanged
(`0773f29c…`), compared value 30 ASCII chars — so no signed decision-file total
or digest changes.

### 8. No regression

Every independently closed prior repair is carried (header "Frozen closures"
list, verified against §V214.0). Zero new constants (the grandchild gate is the
arithmetic `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`), zero new paths, zero new
objects (two key sets +1 key each; four channel flag sets change), zero new
refusal/`INVALID` tokens, zero new imports. Signed generic-harness (v2.3.1) and
batch-settlement (v1.1.1, §D1/§D2) referenced unchanged; nine events, E1/E2/E3,
roots, T bands, Q/C boundary unchanged; T inactive.

---

## Findings by severity

**No new Critical, Major, or Minor.** I specifically re-examined the area I
missed in v2.1.3 (bootstrap pipe blocking) and confirm §V214.1 closes it from
the raw descriptor semantics. The one inherited timing characteristic noted in
Trace 1 (`c17` vs `g2`) is fail-closed, not introduced by v2.1.4, and not
reachable in practice; it is recorded as context, not a finding.

## No-regression table

| Signed cell / surface | Status under v2.1.4 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **Not reopened; more honest** | §V214.6 removes the last promoted-byte over-claim; four named residuals, no new route. |
| **B1** durable-journal ack redelivery | **Not reopened** | §V214.3 changes only the physical deletion order; prefix-first classification and "no owed reply before acknowledgement" preserved. |
| **C1** dedicated freezer | **Not reopened; totalized** | §V214.5 markers are supervisor bookkeeping the watchdog cannot reach; `diagnostic_conditions` routing-irrelevant; `ACK_PENDING` still no evidence/terminal. No second authority. |
| **D1** no idle exit | **Not reopened** | §V214.1 removes the last construction in which a bootstrap participant could retain the shared lock without a deadline; no supervisor waits on `SPAWN.lock`. |
| **K1** mediated transport, fixed ceiling, no replenishment | **Not reopened; release route restored** | Five constants unmoved; no replenishment; literal write-once/hash-once counts unchanged; §V214.2 restores a legitimate release route without weakening `bytes_reserved` accounting. |
| Signed generic-harness / batch-settlement | **Unchanged** | Referenced verbatim; no F1–F4/R1–R4 reopened; §D1/§D2 intact. |
| Nine events, schemas, roots, T bands, E1/E2/E3, Q/C, imports | **Unchanged** | §V214.11 negative space; zero constant/event/root/token/import delta. |

## Author-cell determination

**No new author cell is required, and none is unavoidable.** Every §V214 repair
is mechanical over the already-signed A3/B1/C1/D1/K1 policy: a truly nonblocking
pipe protocol with every errno pinned (§V214.1); an orphan-manifest quarantine
verifier branch that restores the K1 release K1 already selected (§V214.2); a GC
order that preserves the acknowledgement (tombstone) and predicate (`accepted`)
authorities (§V214.3); a single-valued lock/preflight order (§V214.4); a total
watchdog partition (§V214.5); an honest A3 stream/inode/promoted distinction
(§V214.6); and one corrected byte count (§V214.7). No new constant, path,
object, token, or import beyond the two declared schema keys.

## Authorization boundary

This is the **X-line** confirmation. It authorizes **only** that Kirill's
informed author signature token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

may be signed **once the independent Y-line confirmation of these same v2.1.4
bytes is also on record** (the programme requires both X and Y; v2.1.3 is the
precedent — an X confirmation alone was, correctly, not sufficient, because the
Y line found a Critical). It authorizes **nothing else**: no implementation, no
commit of the untracked/dirty implementation, no T activation, no entropy, no
runtime construction (supervisor, controller, worker, watchdog, adapter, middle
child, endpoint, pipe, FIFO, journal, spawn record, result manifest, quarantine
record, replacement-freeze record, operation, capacity artifact, custody
disposition, author decision file, capability, lease, batch, promoted object),
and no scientific / Q/C work (world, learner, candidate, Q attempt, Q/C object,
datum, outcome, Proof, or claim movement). Signing the amendment token does not
by itself activate T or authorize any spend; those remain behind their own
signed gates.

## Contract versus implementation

Every finding and closure above is a property of the v2.1.4 **contract**. The
implementation is unchanged from the state prior reviews recorded:
`src/philosophia/officina/generic_harness.py` is **untracked** and contains no
supervisor, control channel, adapter, journal, operations tree, watchdog,
capacity ledger, result manifest, or output transport; it neither causes nor
cures any v2.1.4 contract finding.

## Custody confirmation

No process, test, probe, or smoke ran; no supervisor, controller, worker,
watchdog, adapter, endpoint, pipe, FIFO, or journal was started; this review
started no process of its own. The recomputation was `hashlib` over literal
documented bytes in the scratchpad, touching no repository code or runtime
state. No code, test, contract, signature, prior review, or runtime artifact was
edited; nothing was committed or staged; the dirty and untracked handover files
are preserved unmodified. Exactly one new file was created — this review. No
runtime or scientific artifact was created. `successor/officina/runtime/`
contains only `T_RUNTIME.lock`; `successor/officina/runtime_control/` does not
exist; `successor/officina/T_ENVELOPE.json` remains `"activated": false`. No
capability, claim, lease, batch, operation, entropy, E1/E2/E3 spend, world,
learner, candidate, Q/C object, datum, or outcome exists. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
