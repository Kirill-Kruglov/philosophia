# Officina supervisor and control-channel amendment — v2.1.3 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1, v2.1.1,
and v2.1.2. It is **not** an independent X-line or Y-line review of its own
bytes and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every prior
author closure is an untrusted self-assessment; none of their claims is used
as evidence here. The only next authorization step is independent bounded X/Y
confirmation of the **v2.1.3 bytes**.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md`
(v2.1.2), which itself layers over v2.1.1, v2.1, and v2 — all four preserved
unedited as review evidence. **Everything not named in the §U0 replacement
index carries forward verbatim.** Nothing earlier is rewritten or silently
reinterpreted. It dispositions every finding of the two independent v2.1.2
reviews
(`reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md`,
`reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md`).

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged**, each independently accepted by
both v2.1.2 reviewers and **not reopened here**: the acyclic, content-closed
custody-disposition authority (§N1.1–§N1.3, §N1.4's byte-exact eight-line
decision file, §N1.7–§N1.8); the complete protocol-created custody-location
set and its paired absence observations (§N2.1–§N2.4, §N2.6); literal K1
write-once/hash-once **counts** (§N4.1–§N4.3); the rejected-witness fallback
object and its `unknown_reason` separation (§N5.1–§N5.5); the collision-safe
fd remap (§N6.1–§N6.3); the single acknowledgement priority rule and published
frontier (§N7.1–§N7.3); the absent-scope defaults (§N9.1); the canonical
empty-result hash (§N9.2); and every accepted v2.1.1 surface (§Z1–§Z13 as
carried), v2.1 surface, and v2 surface.

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature, review,
or runtime artifact. Starts no process, endpoint, pipe, FIFO, journal,
watchdog, worker, adapter, or transport. Creates no entropy, activation,
capability, world, learner, candidate, datum, Q/C object, capacity artifact,
custody disposition, result manifest, or outcome. Authorizes no
implementation. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed for this correction)

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
aa25b28cedd813fbd2da36e0087cc9773be86b21a96c828bde57778953933dc7  reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
22e2fb392c5758d7bab6840cafd711a9e4fa74b19b60bd5b05aebbde9b66c878  reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

## Engineering constants

**Zero new constants.** Every constant of v2.1.1's block carries forward
unchanged, including the five immovable author-signed `T_OUTPUT_*` values,
`T_CTRL_FD_LOW = 3`, `T_CTRL_FD_HIGH = 4`,
`T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000`,
`T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS = 1_000_000_000`,
`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS = 60_000_000_000`,
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS = 10_000_000_000`,
`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS = 30_000_000_000`,
`T_SPAWN_BOOTSTRAP_MAX_AGE_NS = 60_000_000_000`, and
`T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64`. Every bound introduced below
reuses one of these. The import-allowlist delta remains **none**: this layer
additionally uses only `os.pipe2` with `os.O_NONBLOCK`, `os.getsid`,
`os.getpgid`, `os.unlink`, `os.rmdir`, and `os.fsync` — all inside `os`, which
is in `ALLOWED_ABSOLUTE_IMPORTS`; `select`, `selectors`, `signal`, `ctypes`,
and `sys` remain outside it.

---

## U0. Exact replacement index (v2.1.2 → v2.1.3)

Everything else carries forward verbatim, including v2.1.2 §N1.1–§N1.3,
§N1.4, §N1.7, §N1.8, §N2.1, §N2.3 (P1–P7), §N2.4, §N2.6, §N3.1, §N3.4,
§N4.1, §N4.3, §N5.1–§N5.5, §N6.1–§N6.3, §N7.1–§N7.3, §N8.2, §N9.1, §N9.2,
and every v2/v2.1/v2.1.1 section those sections carry.

| v2.1.2 locus (exact sentence / clause / table row) | Action in v2.1.3 |
|---|---|
| §N4.2 code-block step-3 comment `# equal-size content substitution defence` | **deleted** (§U1.1) |
| §N4.2 closing sentence "The equal-size and inode substitution defences are fully retained, because step 2 compares against a descriptor held since before the first byte existed and step 3 hashes the freshly re-resolved, inode-verified descriptor." | **replaced** by §U1.1–§U1.3 (honest detection truth table and two named A3 residuals) |
| §N4.4 crash-table row "content mismatch at step 3 (short read, long read, or EOF at the wrong offset)" | **replaced** by §U1.4 (the row is retained for the anomalies it really covers and re-labelled `LENGTH`/`EOF`, never as content-substitution detection) |
| §N4.4 paragraph "**Named residual, unchanged and not enlarged.** Same-name substitution of the `out/` **directory** …" | **replaced** by §U1.3 (two windows named, the directory swap retained verbatim as the third) |
| §N3.2 step `c5` in full, including the sentence "The recorded `middle_child_pid` is also the grandchild's pgid and session id, because the middle child's only action before forking is `setsid()` (§N3.3)." | **replaced** by §U2.2 (`SPAWNING_MIDDLE.json` with **no** group claim; `SPAWNING_GROUP.json` only after verified `setsid`) |
| §N3.2 step `c3` ("create boot_pipe and release_pipe") and `c6` | **replaced** by §U2.2 (four sealed channels; explicit close discipline) |
| §N3.2 closing sentence "`SPAWNING_GROUP.json` gives every later client a durable, kernel-verifiable kill handle for the whole spawn group before the grandchild is created." | **replaced** by §U2.6 (the group record now carries a *verified* group; the pre-`setsid` window is covered by `SPAWNING_MIDDLE.json` plus a bounded middle-child gate) |
| §N3.3 steps `m1`–`m6` in full | **replaced** by §U2.3 (`m0`–`m9`: two-stage gate, verified `setsid`, group report) |
| §N3.3 closing paragraph "The middle child performs no filesystem write, holds no lock epoch, and its whole lifetime is two `/proc` reads and one non-blocking pipe write. It cannot wedge." | **replaced** by §U2.3 (bounded gates make the claim true; the honest residual is named in §U2.7) |
| §N3.5 steps `c7`–`c12` in full | **replaced** by §U2.4 (`c9`–`c18`) |
| §N3.5 "Three-tier durable identity set" table | **replaced** by §U2.5 (four tiers; pre-`setsid` kill is `kill(pid_mid)` only, never `killpg`) |
| §N3.5 stuck-holder route `s1`–`s4` | **replaced** by §U2.5 (`s1`–`s5`, adding the middle tier) |
| §N3.5 sentence "Because `SPAWNING_GROUP.json` is installed immediately after the first fork, s3 covers **every** cut in which a grandchild or middle child exists, including the pre-`SPAWNING_CHILD` window." | **replaced** by §U2.5 (s3 covers the verified-group window; s4 covers the pre-`setsid` window) |
| §N3.6 automaton table (all rows referring to `c5`–`c12`) | **replaced** by §U2.6 |
| §N5.6 opening sentence "§W3.5's dead-watchdog row freezes **all** live groups." and the whole "Pinned:" block | **replaced** by §U3.1 (explicit replacement of the carried §W3.5 action: overdue ⇒ witness route; non-overdue ⇒ swap-only, **no** §W3.3 witness) |
| §N5.6 resume predicate block `R1`–`R6` | **replaced** by §U3.2 (three exclusive states with precedence) |
| §N5.6 paragraph "If **any** conjunct fails … Nothing is resumed on doubt." | **replaced** by §U3.2 (the "any failed conjunct ⇒ invalidity" rule is **deleted**; a still-pending bounded ack is `ACK_PENDING`, not invalidity) |
| §N5.6 six-row crash table | **replaced** by §U3.4 |
| §N5.6 `t-replacement-freeze.v1` key list | **extended** by §U3.3 (`swap_only (true)`; plus two immutable transition markers) |
| §N8.1 bullet "No TTL, no size pressure, no outcome-derived deletion, and the tombstone is never deleted." | **retained**, and the deletion mechanics replaced by §U4.1 |
| §N8.3 consequence 2, clause "GC therefore needs no particular deletion order, and a crash mid-GC is completed idempotently in a later epoch." | **replaced** by §U4.1–§U4.2 (an exact order with `ack.json` last; the arbitrary-order claim is **deleted**) |
| §N8.4 bullet "**Crash cuts.** Crash mid-GC ⇒ a partial phase set at or below the prefix ⇒ step 1 answers; a later epoch completes the deletion idempotently." | **replaced** by §U4.2 (per-cut proof against the pinned order, including the empty-directory completion rule) |
| §N1.6 identifier-set clause "every `content_sha256` in `SETTLEMENT.json`" and the sentence "all of which the supervisor already holds durably" | **replaced** by §U5.4 (the durable `RESULT_MANIFEST.json`, resolved by `result_manifest_sha256`) |
| §W6.1 `SETTLEMENT.json` key list, as carried by v2.1.1/v2.1.2 (`schema, scientific_outcome, operation_id, charge_event_sha256, result_sha256, promoted_relative_paths, bound_sha256, actual_bytes, settled_utc`) | **replaced** by §U5.3 (adds exactly one key, `result_manifest_sha256`) |
| §W6.1 promotion-order block, at the step `→ settle under T_RUNTIME.lock` | **extended** by §U5.2 (`RESULT_MANIFEST.json` is installed after the sole hash pass and before `SETTLEMENT.json`) |
| §N2.2 table row L2's closed control-record set `{BOUND.json, OPERATION.json, RUNNING.json, SETTLEMENT.json, QUARANTINE.json, DELIVERY_ACK.json}` | **replaced** by §U5.5 (adds `RESULT_MANIFEST.json`) |
| §N2.5 key `custody_locations_proved (sorted list of the exact L1–L5 location strings proved absent in this epoch)` | **replaced** by §U8.1 (`custody_proof_classes`, `custody_proof_roots`, `custody_proof_enumerations`) |
| §N1.5 conjunct 8d | **extended** by §U7.1 (conjunct 8e: `authorized_utc == signed_utc` byte-for-byte) |
| §N3.2 step `c2` and §N3.5 step `c9` (no-replace installs without an `EEXIST` continuation) | **replaced** by §U6.2 (`EEXIST` continuation at every no-replace singleton install) |
| §N3.5 step `c7` kill route, clause "unlink `SPAWNING_GROUP.json` and `SPAWNING.json`" | **replaced** by §U6.3 (the exact child → group → middle → spawning removal order with parent-directory `fsync`s) |
| §N3.6 row "grandchild's first-ack wait expires", clause "unlink `SPAWNING_CHILD.json`" | **replaced** by §U6.3 (same ordered removal) |
| §Z3.5 grandchild step `g3` clause "unlink `SPAWNING_CHILD.json`, `SPAWNING_GROUP.json`, and `SPAWNING.json`" (as carried) | **replaced** by §U6.3 (adds `SPAWNING_MIDDLE.json`; pins order and `fsync`s) |
| §W2.9 phase-1 step 3 stale-endpoint list (`REQUEST.fifo`, `REPLY/*`, `SPAWNING.json`, `SUPERVISOR_IDENTITY.json`) | **extended** by §U6.4 (adds the three new singleton records under the §U6.1 discipline) |
| §N10.1 durable-object table | **extended** by §U9.1 (four added objects; three replaced rows) |
| §N11 crash-cut matrix | **extended** by §U10 (twenty-six added or replaced rows) |
| §N12 test-obligation rows 75–96 | **extended** by §U11 (rows 97–120); row 81 and row 90 are **replaced** |
| §N10.3 inherited-closure qualification | **extended** by §U9.4 (v2.1.2 closures marked *confirmation pending v2.1.3*) |

---

## U1. Honest hash-once A3 boundary (R1)

Closes Opus X212-M1 and X212-m1, and Sol m2. Literal signed K1 is preserved
exactly: **each output content byte is written once (§N4.1 step 3) and hashed
once (§N4.2 step 3).** No count changes. What changes is only the truthfulness
of what that single hash is claimed to prove.

### U1.1 The over-claim is deleted

§N4.2's step-3 comment `# equal-size content substitution defence` is
**deleted**, and its closing sentence is replaced by:

> With a single content hash and no earlier trusted content reference, the pass
> **cannot** detect a same-inode, equal-size, in-place content modification.
> v2.1.1 detected that case only because it computed a second hash of the same
> bytes (an inline hash during the write pass) and compared the two; literal
> signed K1 forbids that second hash. The pass therefore hashes the bytes it
> reads and makes exactly one claim about them: `content_sha256` accurately
> describes the bytes read through the inode-verified descriptor during that
> pass. It makes **no** claim that those bytes equal what the worker sent, and
> **no** claim about the bytes at any later instant.

### U1.2 Truth table: what the sole hash pass does and does not detect

| Anomaly | Detected? | By exactly what |
|---|---|---|
| inode substitution (unlink + recreate, rename-over, new file at the same name) | **yes** | §N4.2 step 2: `(st_dev, st_ino)` of the freshly re-resolved `v` must equal those of the `r` descriptor held since before the first byte existed |
| hard-link introduction | **yes** | §N4.2 step 2: `st_nlink == 1` |
| truncation or extension (any size change) | **yes** | §N4.2 step 2: `st_size == bytes_written[rel]`, plus step 3's read-length equality and EOF-at-offset requirement |
| short read, long read, or EOF at the wrong offset (an unstable read during the pass) | **yes** | §N4.2 step 3's length and EOF requirements |
| path grammar, depth, uniqueness, component/path length, file count, per-frame and cumulative byte ceilings | **yes** | §N4.1's header validation, before anything is created |
| worker-reported frame/byte counts disagreeing with the supervisor's own counters | **yes** (fail-closed only) | §Z7.1's cross-check ⇒ `TRANSPORT` quarantine |
| that `content_sha256` describes the bytes read during the pass | **yes, by construction** | the hash is computed from exactly those bytes, through exactly that descriptor |
| **same-inode, equal-size, in-place content modification before the pass** | **NO** | nothing: there is no earlier trusted content reference and no second hash |
| **same-inode, equal-size, in-place content modification during the pass**, when it does not perturb length or EOF | **NO** | ditto |
| **same-inode, equal-size, in-place content modification after the pass**, before `SETTLEMENT.json` and the promotion rename | **NO** | the pass proves nothing about any later instant |
| same-name substitution of the `out/` **directory** after the pass, before `os.replace` | **NO** | the kernel offers no rename-by-descriptor (§N4.4, carried) |

### U1.3 The three named residuals

All three are signed-**A3 procedural** residuals: T-development-only,
permanently **non-citable**, and forbidden from selection, Q, C, C1–C6, any
blinding claim, and any scientific interpretation. None is routed to `HASH`,
because none is observable; none is claimed closed.

```text
A3-R1  Same-inode, equal-size, in-place content modification occurring BEFORE
       or DURING the sole hash pass, when it is not caught as a length or EOF
       anomaly. Consequence: content_sha256 and the result manifest describe
       the modified bytes, and the tree promotes. Nothing is inconsistent —
       the recorded hash still truthfully describes the promoted bytes — but
       the bytes are not provably the worker's.

A3-R2  Any in-place modification of a verified inode AFTER the pass and before
       durable settlement/promotion. The pass establishes no future
       immutability, and this contract does not claim it does.

A3-R3  Same-name substitution of the out/ directory between the pass and the
       promotion os.replace (carried verbatim from §N4.4).
```

### U1.4 Crash/anomaly routing, corrected labels

§N4.4's crash table is otherwise unchanged. Its content row is replaced:

| Cut / anomaly | Continuation |
|---|---|
| inode, `st_nlink`, or `st_size` mismatch at step 2 | `HASH` quarantine class (§W4.7, unchanged) |
| step 3 read length ≠ `bytes_written[rel]`, or EOF not exactly at that offset (a length/EOF anomaly, **not** a content comparison) | `HASH` quarantine class |
| A3-R1, A3-R2, A3-R3 | **no route exists, because no observation exists.** These are never signalled, never quarantined, and never invoked as evidence of anything |
| crash before, during, or after the pass but before `SETTLEMENT.json` | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; no partial hash retained; no resume; no respawn (unchanged) |

### U1.5 The fundamental tension, recorded (X212-m1)

Detecting A3-R1 requires **either** a second content hash of the same bytes
(v2.1.1's inline hash) **or** a trusted stored reference produced by hashing
the content earlier — which is the same second hash under another name. Both
violate the signed provider's "writes and hashes each byte once". The two
goals are therefore **mutually exclusive**, and the honest resolution is the
residual statement of §U1.3, not a mechanism.

> **Normative consequence.** No later layer may re-introduce equal-size
> content-substitution detection by adding a second hash of any output content
> byte, or by storing a content-derived reference computed outside the sole
> pass, without a **new author decision on K1**. Any such change reopens the
> signed provider and is outside every existing authorization.

---

## U2. Two-stage middle-child gate and truthful group identity (R2)

Closes Sol C1. The grandchild's own gate (§N3.4) and the sealed-channel
principle (§N3.1) are **unchanged**; what is inserted is a two-stage gate for
the middle child and the removal of the false pre-`setsid` group claim.

### U2.1 The four sealed channels

All four are created by the CLI **before** the first fork:

```text
boot_pipe = os.pipe2(0)                 # reports → CLI; CLI holds the read end
rel1      = os.pipe2(os.O_NONBLOCK)     # stage-1 release, CLI → middle child
rel2      = os.pipe2(os.O_NONBLOCK)     # stage-2 release, CLI → middle child
rel3      = os.pipe2(0)                 # stage-3 release, CLI → grandchild
                                        #   (v2.1.2's release_pipe, unchanged)
```

`rel1` and `rel2` are created **`O_NONBLOCK` on both ends**, so the middle
child's gate reads never block indefinitely regardless of which write-end
copies exist; the bound, not EOF, is its primary liveness guarantee, and EOF
remains an additional early-exit signal. `rel3` keeps v2.1.2's blocking-read +
EOF design **unchanged**, and that design remains sound because the middle
child closes its `rel3` write-end copy at `m1`, before the second fork, so the
CLI is the only `rel3` writer for the grandchild's whole gated lifetime.

Ownership after the first fork:

| Process | Retains | Closes |
|---|---|---|
| CLI | `rel1` write, `rel2` write, `rel3` write, `boot` read | `rel1` read, `rel2` read, `rel3` read, `boot` write (at `c5`) |
| middle child | `rel1` read → then `rel2` read, `rel3` read, `boot` write | `rel1` read/write, `rel2` write, `rel3` write, `boot` read (at `m1`); `rel2` read (at `m6`) |
| grandchild | `rel3` read, `boot` write, the `SPAWN.lock` fd, stdio | everything else, at `g1` (unchanged) |

### U2.2 CLI, stages 0–1 (replaces §N3.2 `c3`–`c6`)

```text
c1. §U6.1 singleton preflight, then acquire SPAWN.lock with
    flock(LOCK_EX|LOCK_NB), retrying at T_SUPERVISOR_POLL_INTERVAL_NS until
    T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS; on expiry take the §U2.5 stuck-holder
    route
c2. install SPAWNING.json (§W2.2 keys unchanged; §3 durability; §U6.2 EEXIST
    continuation)
c3. create the four channels of §U2.1
c4. pid_mid = os.fork()
c5. in the CLI: close rel1 read, rel2 read, rel3 read, boot write
c6. verify pid_mid is live and read its kernel start identity from
    /proc/<pid_mid>/stat; not live ⇒ §U2.5 stage-0 route
c7. install T_SUPERVISOR/SPAWNING_MIDDLE.json (atomic no-replace, §3
    durability, §U6.2 EEXIST continuation), schema
    philosophia.officina.t-supervisor-spawning-middle.v1, keys exactly:
      schema, scientific_outcome, spawning_id, cli_pid, cli_start_identity,
      middle_child_pid, middle_child_start_identity, boot_identity,
      created_utc
    This record makes NO pgid or session claim, because none is true yet.
c8. write exactly one byte b"\x01" on rel1 write; close rel1 write
                                                        ← STAGE 1 RELEASE
```

### U2.3 Middle child, `m0`–`m9` (replaces §N3.3 `m1`–`m6`)

```text
m0. (THE LITERAL FIRST INSTRUCTION) read one byte from rel1 read, which is
    already O_NONBLOCK, in a loop paced at T_SUPERVISOR_POLL_INTERVAL_NS and
    bounded by T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS:
      b"\x01"                    ⇒ m1
      b"" (EOF: CLI died/closed) ⇒ os._exit(3)
      any other byte             ⇒ os._exit(3)
      bound expires              ⇒ os._exit(3)
    Nothing else is executed before this read. The loop performs no filesystem
    write, creates nothing, and changes no shared state.
m1. close rel1 read, rel1 write, rel2 write, rel3 write, boot read
      (retain rel2 read, rel3 read, boot write, the SPAWN.lock fd)
m2. os.setsid()
m3. verify os.getsid(0) == os.getpgid(0) == os.getpid(); any inequality
      ⇒ os._exit(3)
m4. write EXACTLY ONE canonical ASCII JSON line ≤ T_CONTROL_FRAME_MAX_BYTES on
    boot write, schema philosophia.officina.t-supervisor-group-report.v1, keys
    exactly:
      schema, scientific_outcome, spawning_id, middle_child_pid,
      middle_child_start_identity, session_id, process_group_id,
      boot_identity, reported_monotonic_ns
    — cannot block (one line ≤ 4096 ≤ PIPE_BUF into an empty pipe);
      EPIPE (CPython ignores SIGPIPE) ⇒ os._exit(3)
m5. read one byte from rel2 read (O_NONBLOCK) with the same bounded loop:
      b"\x02" ⇒ m6 ; EOF / other byte / bound expires ⇒ os._exit(3)
                                                        ← STAGE 2 GATE
m6. close rel2 read
m7. pid_gc = os.fork()
m8. (middle child only) read /proc/<pid_gc>/stat for the grandchild's start
    identity and /proc/sys/kernel/random/boot_id; write EXACTLY ONE
    t-supervisor-bootstrap.v1 line on boot write (keys unchanged from §Z3.5),
    then close boot write; EPIPE ⇒ os._exit(3)
m9. os._exit(0)                    # the grandchild is reparented to init
```

The middle child therefore performs **no filesystem write at all**, holds no
lock epoch, and every wait it performs is bounded by
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`. Its only pre-record instruction is the
`m0` gate read.

### U2.4 CLI, stages 2–3 (replaces §N3.5 `c7`–`c12`)

```text
c9.  read one group-report line from boot read, bounded by
     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS (nonblocking poll at
     T_SUPERVISOR_POLL_INTERVAL_NS)
       valid line ⇒ c10
       EOF, malformed line, or bound expiry ⇒ §U2.5 stage-1 route
c10. verify, from the kernel, all four facts:
       /proc/<middle_child_pid>/stat is live and its start identity equals
         SPAWNING_MIDDLE.json's middle_child_start_identity;
       os.getsid(middle_child_pid)  == middle_child_pid;
       os.getpgid(middle_child_pid) == middle_child_pid;
       the reported session_id and process_group_id both equal
         middle_child_pid
     any mismatch ⇒ §U2.5 stage-1 route
c11. install T_SUPERVISOR/SPAWNING_GROUP.json (atomic no-replace, §3
     durability, §U6.2 EEXIST continuation), schema
     philosophia.officina.t-supervisor-spawning-group.v1, keys exactly:
       schema, scientific_outcome, spawning_id, cli_pid, cli_start_identity,
       middle_child_pid, middle_child_start_identity, session_id,
       process_group_id, group_verified (true), boot_identity, created_utc
     `group_verified: true` is installable ONLY after c10's kernel proof.
c12. write exactly one byte b"\x02" on rel2 write; close rel2 write
                                                        ← STAGE 2 RELEASE
c13. read one t-supervisor-bootstrap.v1 line from boot read, bounded as c9
       EOF, malformed, or bound expiry ⇒ §U2.5 stage-2 route
c14. verify the reported supervisor_pid is live, its start identity equals the
     reported value, and os.getpgid(supervisor_pid) == process_group_id
       mismatch ⇒ §U2.5 stage-2 route
c15. install T_SUPERVISOR/SPAWNING_CHILD.json (atomic no-replace, §3
     durability, §U6.2 EEXIST continuation; keys unchanged from §N3.5 c9)
c16. write exactly one byte b"\x01" on rel3 write; close rel3 write
                                                        ← STAGE 3 RELEASE
c17. poll for a live-verified SUPERVISOR_IDENTITY.json, bounded by
     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS; on expiry ⇒ §U2.5 stage-2 route
c18. release SPAWN.lock (the grandchild's retained fd keeps the flock until g3)
```

Total CLI bound: `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` +
3 × `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` + bounded kill/death proof
(30 s + 30 s + bounded), all reusing existing constants. No wait is unbounded.

### U2.5 Four identity tiers and the exact kill discipline

| Tier | Record | Identity | Permitted kill |
|---|---|---|---|
| CLI | `SPAWNING.json` | `cli_pid`, `cli_start_identity` | **never killed by another client** (§U2.7 residual) |
| middle, pre-`setsid` | `SPAWNING_MIDDLE.json` | `middle_child_pid`, `middle_child_start_identity` | `kill(middle_child_pid, SIGTERM)` then `SIGKILL` — **`killpg` is forbidden here** |
| group, post-verified-`setsid` | `SPAWNING_GROUP.json` (`group_verified: true`) | `session_id == process_group_id == middle_child_pid` | `killpg(process_group_id, …)`, with per-member death proof |
| grandchild | `SPAWNING_CHILD.json` | `supervisor_pid`, `supervisor_start_identity`, `supervisor_pgid` | `killpg(supervisor_pgid)` or `kill(supervisor_pid)` |

**Why `killpg` is forbidden before verified `setsid`.** Until `m2` completes,
the middle child is still in the **CLI's** process group, so `middle_child_pid`
is not a process-group id. `killpg(middle_child_pid)` would then either fail
`ESRCH` or — if an unrelated group happens to carry that id after pid reuse —
kill unrelated same-UID processes. This is exactly the defect Sol C1 named, and
it is removed by making the group claim conditional on `c10`'s kernel proof.

Failure routes, each preceded by exact identity validation and followed by the
§U6.3 ordered record removal:

```text
stage-0 route (c6 fails: pid_mid not live)
  no kill is needed or attempted; remove records per §U6.3; release the lock;
  return REFUSED / BOOTSTRAP (retryable = false)

stage-1 route (c9/c10 fail: no verified group yet)
  if /proc/<middle_child_pid>/stat is live AND its start identity equals
     SPAWNING_MIDDLE.json's ⇒ kill(middle_child_pid, SIGTERM) then SIGKILL;
     prove death by /proc absence or state Z; os.waitpid(pid_mid, WNOHANG) to
     reap the own child
  if live with a DIFFERENT start identity (pid reuse) ⇒ kill NOTHING; treat as
     absent
  then remove records per §U6.3; release the lock; REFUSED / BOOTSTRAP
     (retryable = false)

stage-2 route (c13/c14/c17 fail: the group is verified and durable)
  killpg(process_group_id, SIGTERM) then SIGKILL; prove death of every member
  found by /proc absence or state Z; os.waitpid only for own-generation
  children; then remove records per §U6.3; release the lock;
  REFUSED / BOOTSTRAP (retryable = false)
```

**Stuck-holder route** (replaces §N3.5's `s1`–`s4`), taken by a later CLI
**without** the lock after `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` expires, in this
order; every step obeys §U6.1's malformed/PID-reuse rules:

```text
s1. SUPERVISOR_IDENTITY.json present and live-verified ⇒ a live supervisor
    exists; kill nothing; proceed as an ordinary client
s2. SPAWNING_CHILD.json well-formed, its recorded process live by
    pid + start identity, and older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS
    ⇒ killpg(supervisor_pgid), prove death, remove records per §U6.3, retry
      the bounded acquisition exactly once
s3. SPAWNING_GROUP.json well-formed with group_verified: true, its recorded
    group live (by leader identity or any live member), and older than
    T_SPAWN_BOOTSTRAP_MAX_AGE_NS
    ⇒ killpg(process_group_id), prove death, remove per §U6.3, retry once
s4. SPAWNING_MIDDLE.json well-formed, its recorded process live by
    pid + start identity, and older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS
    ⇒ kill(middle_child_pid) ONLY (never killpg), prove death, remove per
      §U6.3, retry once
s5. otherwise ⇒ REFUSED / BOOTSTRAP (retryable = true)
```

### U2.6 Complete automaton with every cut (replaces §N3.6)

| Cut | Lock references | Middle / grandchild state | Single continuation |
|---|---|---|---|
| before `c1` | free | absent | §U6.1 preflight, then ordinary acquisition |
| `c1` expires | — | unknown | `s1`–`s5` |
| after `c2`, CLI dies | released on CLI exit | absent | next holder's §U6.1 preflight proves `SPAWNING.json`'s pid dead and removes it |
| after `c4`, before `c7` (**no middle record yet**) | CLI + middle | middle at `m0` | **CLI death:** its `rel1` write end closes ⇒ `m0` sees EOF ⇒ `_exit(3)` ⇒ reference released. **CLI alive but slow:** `m0`'s bound expires at ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` ⇒ `_exit(3)`. **Middle dies:** `c6`/`c9` observe it and take the stage-0/1 route. In every case the middle child's lock reference is released within a bounded time **without needing any record** — this is the cut Sol C1 showed was not total |
| after `c7`, before `c8` | CLI + middle | middle at `m0` | `SPAWNING_MIDDLE.json` durable ⇒ `s4` can kill by pid + start identity; `m0`'s bound also fires |
| after `c8`, before `m2` | CLI + middle | middle at `m1`/`m2` | CLI death ⇒ `m5`'s stage-2 gate sees EOF (or its bound expires) ⇒ `_exit(3)`; `s4` applies meanwhile. **`killpg` is never used here** |
| `m3` inequality (`setsid` did not make it a leader) | CLI + middle | middle exiting | `_exit(3)`; `c9` gets EOF (the middle child was the only `boot` writer) ⇒ stage-1 route ⇒ `kill(pid_mid)` on an already-dead pid, death proved, records removed |
| after `m4`, before `c11` | CLI + middle | middle at `m5` | group report received but not yet durable ⇒ `s4` (middle tier) still governs; `killpg` remains forbidden until `c11` |
| after `c11`, before `c12` | CLI + middle | middle at `m5` | `SPAWNING_GROUP.json` with `group_verified: true` is durable ⇒ `s3` may `killpg(process_group_id)`, which is now a **true** group |
| after `c12`, before `m7` | CLI + middle | middle at `m6` | grandchild does not exist; middle death ⇒ `c13` gets EOF ⇒ stage-2 route |
| after `m7`, before `m8` | CLI + middle + grandchild | grandchild at `g0` | grandchild executes **nothing** but its gated read; middle death ⇒ no EOF (the grandchild holds a `boot` write copy) ⇒ `c13`'s bound expires ⇒ stage-2 route `killpg` reaches both |
| after `m8`, before `c15` | CLI + middle(exiting) + grandchild | grandchild at `g0` | CLI death ⇒ `rel3` write closes ⇒ `g0` EOF ⇒ `_exit(3)`; CLI wedge ⇒ `s3` |
| after `c15`, before `c16` | CLI + grandchild | grandchild at `g0` | `SPAWNING_CHILD.json` durable ⇒ `s2` kills precisely |
| after `c16` (grandchild at `g1`/`g2`) | grandchild (+CLI until `c18`) | initializing | `s2`; the grandchild's own bounded first-ack wait exits it on failure |
| grandchild first-ack wait expires | grandchild | initializing | kill the watchdog by `WATCHDOG_CHILD.json`, prove death, remove records per §U6.3, `os._exit(3)` ⇒ lock released |
| identity-install no-replace collision | both candidates | one serving | the loser exits immediately, writing nothing, unlinking nothing (§Z3.5, unchanged) |
| after `g3` | free | serving | `s1` for later clients |
| any process killed | released on exit | dead | death proved by `/proc` absence or state `Z`; PID reuse ⇒ start-identity mismatch ⇒ **no kill**, treat as absent |

**Invariant achieved.** No process executes an **unrecorded action** while
retaining the fork-shared lock: the middle child's only pre-record instruction
is a bounded, non-blocking gate read that writes nothing and changes no shared
state; its `setsid`/`/proc`/report actions occur only after
`SPAWNING_MIDDLE.json` is durable; its `fork` occurs only after
`SPAWNING_GROUP.json` is durable with a kernel-verified group; and the
grandchild's only pre-record instruction remains its own gated read (§N3.4,
unchanged). Every lock reference is released by bounded self-exit, by proved
kill against a durable record, or by process death.

### U2.7 Named residuals, stated not claimed away

1. **A wedged or `SIGSTOP`ed CLI holding the lock** — carried verbatim from
   §N3.5: its `flock` reference is released only on its own exit; every
   contract-following CLI wait is bounded (§U2.4's arithmetic); a deliberately
   stopped same-UID client is the signed A3 procedural residual and an
   operator matter. This contract does not authorize one client to kill
   another client process.
2. **A middle child deliberately `SIGSTOP`ed inside the `m0` window before
   `SPAWNING_MIDDLE.json` is durable** — a window bounded by the CLI's own
   `c4`→`c7` execution (two `/proc` reads and one atomic install) and, from the
   middle child's side, by `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`. Inside that
   window no durable record names it, so a later client has no identity-safe
   kill handle and returns `REFUSED`/`BOOTSTRAP` (retryable). This requires
   **deliberate** same-UID interference in a sub-second-to-10-second window;
   any *accidental* death releases the reference immediately, because process
   exit closes the descriptor. It is the same A3 procedural class as residual
   1, and it is strictly narrower than v2.1.2's unbounded exposure.

**D1 is unaffected** by both: no supervisor waits on `SPAWN.lock`, and the
supervisor's lifetime never depends on a client or on the middle child.

---

## U3. Total swap-only watchdog state machine (R3)

Closes Sol C2.

### U3.1 Explicit replacement of the carried §W3.5 action

§W3.5's dead-watchdog row said the supervisor "freezes all live groups itself
per §W3.3 with `killer = SUPERVISOR`". That action is **explicitly replaced**
for non-overdue groups. On watchdog death, the supervisor classifies **each**
live group under `T_RUNTIME.lock`, against that group's **current durable
lease** row, at the instant it freezes it:

```text
overdue      (now_ns ≥ deadline_ns)  ⇒ DEADLINE FREEZE, unchanged:
                the §W3.3 sequence with killer = SUPERVISOR, a
                FREEZE/<witness_id>.json witness (or a §N5 fallback when
                that evidence is rejected), and the §W3.4 invalid route.

non-overdue  (now_ns <  deadline_ns) ⇒ SWAP-ONLY FREEZE:
                killpg(pgid, SIGSTOP); prove quiescence by §W6.4; install
                ONLY the §U3.3 REPLACEMENT_FREEZE record.
                NO §W3.3 witness is written. NO freeze_ns is sampled as
                evidence. NO overrun_ns exists. NO fallback is written.
```

This removes Sol C2's unreachability: a swap-only freeze no longer creates the
witness that the resume predicate forbids. Deadline and overdue freezes retain
the existing witness route in full, unchanged.

### U3.2 Three mutually exclusive states, with precedence

Evaluated under `T_RUNTIME.lock` at every serve step, in this order —
`INVALID` conditions **first**, then `RESUMABLE`, else `ACK_PENDING`. The
v2.1.2 rule "**any** conjunct fails ⇒ the signed invalid route" is **deleted**.

```text
INVALID  if ANY of:
  I1. now_ns ≥ deadline_ns of the group's current durable lease row
      (the deadline passed while the group was frozen)
  I2. the replacement watchdog failed definitively: os.fork error, or no ack
      of any table_seq within T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS of the
      replacement table's updated_monotonic_ns
  I3. definitive identity/member mismatch: any recorded member's pid +
      start identity differs, or any member is absent, Z, or in an
      unclassifiable state
  I4. a §W3.3 deadline-freeze witness or a §N5 fallback exists for that
      process in the current generation
  I5. an unresolved invalidity blocks: G5 not clear, or the record-first
      ordering / v2.1 §B.4 not satisfied
  I6. the recorded lease is no longer the current durable lease
  I7. the REPLACEMENT_FREEZE record's supervisor_generation_sha256 differs
      from the current generation
  ⇒ install <replacement_freeze_id>.invalidated.json (§U3.3) naming the exact
    triggering condition, then take the signed all-live invalid route
    (§2c.12 / §2c.12b / §4d, public cause PROCESS; the §4c(c)/§4d unknowable
    pool when any member state is unknowable)

RESUMABLE if NOT INVALID and BOTH:
  S1. the replacement watchdog is live by its §Z3.6 WATCHDOG_CHILD.json record
      AND has durably acked the EXACT current table_seq whose table contains
      this group's row
  S2. every recorded member's pid + start identity matches and every member is
      in state T  (relaxed to "T or running" once .resumed.json is durable)
  ⇒ install <replacement_freeze_id>.resumed.json (no-replace) BEFORE
    killpg(pgid, SIGCONT); the SIGCONT is idempotent and re-issuable

ACK_PENDING otherwise — i.e. not INVALID, and S1 not yet satisfied:
  the group REMAINS FROZEN. This is NOT invalidity, NOT a terminal, and NOT
  evidence of anything. Re-evaluate at each T_SUPERVISOR_POLL_INTERVAL_NS
  serve step. The state is bounded: it must resolve to RESUMABLE or INVALID by
    min( deadline_ns ,
         replacement_table.updated_monotonic_ns
           + T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS )
  whichever is earlier, because I1 or I2 fires at that bound.
```

**No healthy non-overdue group is mechanically forced into invalidity.** For a
healthy group: I1 is false (the deadline has not passed), I2 is false (the
replacement watchdog forks and acks within
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` + `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`
= 10 s + 1 s at worst), I3–I7 are false, so the group is `ACK_PENDING` and
then `RESUMABLE`. The only invalidity reachable from a swap is an honest
infrastructure race — a lease whose remaining time is shorter than the
replacement path (≈ 11 s at worst) — which is I1, a real overdue deadline, not
a relabelled healthy heartbeat. No new constant is introduced; the bound is
the arithmetic of two existing ones.

### U3.3 Records: one immutable object per transition

```text
WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json
  replacement_freeze_id = SHA-256(canonical {
    "schema": "philosophia.officina.t-replacement-freeze-id.v1",
    "supervisor_generation_sha256": …, "process_id": …, "table_seq": … })
  schema philosophia.officina.t-replacement-freeze.v1, atomic no-replace,
  supervisor under T_RUNTIME.lock, keys exactly:
    schema, scientific_outcome, supervisor_generation_sha256,
    replacement_freeze_id, process_id, pgid, start_identity, table_seq,
    deadline_ns, swap_only (true), overdue (false),
    supervisor_stop_monotonic_ns, created_utc

WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.resumed.json
  schema philosophia.officina.t-replacement-resume.v1, atomic no-replace,
  keys exactly: schema, scientific_outcome, replacement_freeze_id,
    acked_table_seq, resume_monotonic_ns, resumed_utc

WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.invalidated.json
  schema philosophia.officina.t-replacement-invalidation.v1, atomic
  no-replace, keys exactly: schema, scientific_outcome,
    replacement_freeze_id, invalid_condition ∈ {I1,I2,I3,I4,I5,I6,I7},
    observed_monotonic_ns, invalidated_utc
```

`ACK_PENDING` needs no marker: it is exactly the state in which the
`REPLACEMENT_FREEZE` record exists and neither transition marker does. No
record is ever mutated; the state machine is a set of immutable no-replace
installs, so every transition is crash-completable.

**`supervisor_stop_monotonic_ns` is not a freeze instant.** It is the
supervisor's own monotonic sample at the moment it proved the group quiescent
for its own swap bookkeeping. It is **never** used to compute `overrun_ns`,
**never** evidence of a deadline overrun, **never** consumed as a §W3.3/§W3.4
witness, and permanently non-citable. `swap_only: true` makes the record's
class explicit on its face.

**No second authority.** All three objects are written **only** by the
supervisor under `T_RUNTIME.lock`; the watchdog has no path to
`REPLACEMENT_FREEZE/**` and never writes there. None can select a valid
terminal, none can settle, and none is evidence of a freeze instant or an
overrun. The watchdog remains a witness/freezer only: no lock, no capability,
no `runtime/` write, no ledger append, no settlement, no validity authority.

### U3.4 Transitions and every crash cut (replaces §N5.6's table)

| Cut / condition | Single continuation |
|---|---|
| non-overdue group frozen, crash **before** the `REPLACEMENT_FREEZE` record | no record ⇒ the group is not resumable; it is settled through the signed all-live invalid route (fail-closed) |
| `REPLACEMENT_FREEZE` durable, no marker, replacement ack not yet observed, deadline not passed | `ACK_PENDING`: hold frozen; re-evaluate each serve step; **no invalidity** |
| `ACK_PENDING`, ack of the exact current `table_seq` observed, S2 holds | → `RESUMABLE`: install `.resumed.json`, then `killpg(SIGCONT)` |
| `ACK_PENDING`, deadline passes first | → `INVALID` (I1): install `.invalidated.json`, then the signed invalid route |
| `ACK_PENDING`, replacement watchdog fork failure or ack absence past `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` | → `INVALID` (I2) |
| `ACK_PENDING`, a member dies or an identity mismatches | → `INVALID` (I3) |
| a witness or fallback appears for that process | → `INVALID` (I4) |
| unresolved invalidity present | → `INVALID` (I5) |
| the recorded lease is superseded | → `INVALID` (I6) |
| crash after `.resumed.json`, before `SIGCONT` | re-verify with the relaxed S2 and re-issue `killpg(SIGCONT)` idempotently |
| crash after `SIGCONT` | the group is live under a lease already inside the acked table; all three records are removed after the process's durable terminal + archival commit |
| crash after `.invalidated.json`, before the invalid terminal set is durable | resume the signed record-first invalidity route at its first missing step; the marker names the condition, so **no re-classification** occurs |
| both markers somehow present | record-first invalidity naming both paths (only reachable through the A3 same-UID procedural residual) |
| supervisor loss with a `REPLACEMENT_FREEZE` from a prior generation | I7 ⇒ `INVALID`; §Z2.5 phase 2A settles it before any reducer step; **never resumed** |

This remains the **only** path in the contract that `SIGCONT`s an
already-frozen group. It never applies to a deadline freeze (every such freeze
is invalidity by §W3.4) and never crosses a supervisor loss.

---

## U4. Crash-completable GC with `ack.json` last (R4)

Closes Sol M1. §N8.1's eligibility conditions G1–G3 and §N8.2's per-command
archival predicates are unchanged; §N8.3's prefix-first classification is
unchanged. Only the deletion mechanics change.

### U4.1 The exact deletion order

All eligibility is verified **before the first deletion**, in the same held
`T_RUNTIME.lock` epoch:

```text
D0. verify, in this epoch, for occurrence i:
      G1  ack.json for i is durable and immutable
      G2  i ≤ acknowledged_prefix_occurrence
      G3  the §N8.2 command-specific archival predicate holds
    any failure ⇒ delete nothing
D1. unlink accepted.json      (ENOENT ⇒ already done, continue)
D2. unlink committed.json     (ENOENT ⇒ continue)
D3. unlink reply.json         (ENOENT ⇒ continue)
D4. fsync the key directory
D5. unlink ack.json           ← LAST
D6. fsync the key directory
D7. rmdir the key directory   (ENOENT ⇒ already done;
                               ENOTEMPTY ⇒ record-first invalidity naming the
                               directory: an unexpected entry exists and is
                               never deleted blindly)
D8. fsync the JOURNAL parent directory
```

v2.1.2 §N8.3's clause "GC therefore needs no particular deletion order" is
**deleted**: it was false, because G1 names `ack.json` as the eligibility
witness for a later epoch.

**Empty-directory completion rule** — the one GC step that does not require
G1:

```text
a key directory containing NO phase file, whose occurrence index satisfies
i ≤ acknowledged_prefix_occurrence, may be rmdir'd in any later held-lock
epoch with no further predicate, because nothing remains whose eligibility
could be in question and the prefix is permanent and never deleted.
```

### U4.2 Crash-cut proof

| Cut | Durable state | Continuation |
|---|---|---|
| crash before D1 | all four files present | nothing deleted; a later epoch re-verifies G1–G3 and starts at D1 |
| crash between D1 and D2 | `committed`, `reply`, `ack` present | `ack.json` present ⇒ **G1 still holds** ⇒ a later epoch re-verifies G1–G3 and resumes at D1 (ENOENT-tolerant) |
| crash between D2 and D3 | `reply`, `ack` present | same: G1 holds, resume at D1 |
| crash between D3 and D5 | `ack` present only | same: G1 holds, resume at D1; D1–D3 are ENOENT no-ops |
| crash between D5 and D7 | directory present, **empty** | G1 no longer holds, but nothing remains to justify: the **empty-directory completion rule** applies, `rmdir` in any later epoch |
| crash after D7 | directory absent | complete; nothing to do |
| any cut, in every case | the tombstone (`next_occurrence_index`, `acknowledged_prefix_occurrence`) is **never** deleted | §N8.3 step 1 answers `REFUSED`/`ALREADY_ACKNOWLEDGED` for `i ≤ prefix` regardless of which phase files exist, so exactly-once is preserved at every cut and no reducer can run |

**Why `ack.json` last is exactly sufficient.** For every prefix of the
deletion sequence that stops before D5, the durable eligibility witness
(`ack.json`) is still present, so the next epoch can re-derive G1–G3 and
complete. For every prefix that stops at or after D5, all phase files are
already gone, so no eligibility question remains and the empty-directory rule
completes the hygiene step. There is no cut at which a remaining phase file
lacks its eligibility witness — which was precisely the permanently-non-GC-able
state Sol M1 identified in the unordered design.

### U4.3 Concurrency, errno, and the retention bound

- **Retry concurrency.** GC and frame service both hold `T_RUNTIME.lock` and
  therefore serialize; no interleaving exists. A retry evaluated before, during
  the same epoch as, or after a GC receives the identical
  `REFUSED`/`ALREADY_ACKNOWLEDGED` answer, because §N8.3 tests the prefix
  first. GC timing remains invisible to clients.
- **`errno`.** `unlink` `ENOENT` ⇒ continue (idempotent); `rmdir` `ENOENT` ⇒
  done; `rmdir` `ENOTEMPTY` ⇒ record-first invalidity naming the directory; any
  other `errno` on any step ⇒ abandon this GC in this epoch, delete nothing
  further, and record-first invalidity naming the path (fail-closed; the
  journal is never left in a state the next epoch cannot classify). There is no
  `EEXIST` in GC, which creates nothing.
- **Missing-prefix state.** If `i ≤ prefix` is false, GC never begins (G2). An
  absent tombstone yields `acknowledged_prefix(absent) = 0` (§N9.1), so no
  occurrence is GC-eligible and no deletion can start.
- **Retention arithmetic** (unchanged from §N8.4, now executable at every
  cut): (a) unacknowledged occurrences ≤ `T_MAX_UNACKED_OCCURRENCES_PER_SCOPE
  = 64` per scope; plus (b) acknowledged-but-unarchived occurrences, bounded by
  open transitions, themselves bounded by `MAX_CONCURRENT_LEASES = 4` and the
  signed 32 GiB operation envelope. Growth is bounded and independent of
  polling frequency.
- **Per-command archival predicates** carry forward from §N8.2 **verbatim**,
  including the explicit statement that observation-form `OPERATION_STATUS` is
  **vacuously satisfied** by durable `committed.json` and `reply.json`, because
  an empty-effect plan appends no ledger entry and owns no archival item.

---

## U5. Immutable result manifest and settlement binding (R5)

Closes Sol M2. No content byte is reread or rehashed anywhere in this section.

### U5.1 The manifest object

```text
path: runtime_control/T_SUPERVISOR/operations/<operation_id>/RESULT_MANIFEST.json
schema philosophia.officina.t-operation-result-manifest.v1
atomic no-replace, §3 durability (same-directory temp → file fsync →
no-replace rename → parent-directory fsync), written by the supervisor under
T_RUNTIME.lock, keys exactly:

  schema, scientific_outcome, supervisor_generation_sha256, operation_id,
  entry_count, total_byte_length, entries, created_utc

entries: a JSON array whose elements have keys exactly
  {relative_path, byte_length, content_sha256}
  sorted ascending by the byte values of relative_path (ASCII/UTF-8 bytes);
  relative_path unique by construction (§N4.1 enforces uniqueness at write
  time); byte_length a strict int ≥ 0; content_sha256 64 lowercase hex.
entry_count == len(entries); total_byte_length == Σ byte_length.
```

Canonical encoding throughout is the repository's canonical JSON: `sort_keys`,
`separators=(",",":")`, `ensure_ascii=True`, ASCII, exactly one trailing `\n`.
`scientific_outcome: false`; recursive scientific-field rejection; strict
`type(x) is int` (`bool` refused). Archival-excluded and untracked, like every
other `runtime_control/**` object.

**Constructed from memory, never from a reread.** Every element is the
in-memory tuple produced during the sole content-hash pass (§N4.2) — the
`relative_path` and `byte_length` from the write-path counters, the
`content_sha256` from that same pass — assembled and installed in the **same**
`T_RUNTIME.lock` epoch as the pass and the settle step (§N4.4's one-epoch
rule, unchanged).

### U5.2 Ordering inside the settle step

§W6.1's promotion order gains one step, between the verification pass and the
commit point:

```text
… → sole content-hash pass (§N4.2)
  → RESULT_MANIFEST.json                       (no-replace)   ← new
  → SETTLEMENT.json                            (no-replace)   = THE COMMIT POINT
  → CAPACITY/<op>.settled.json
  → idempotent os.replace of out/ into runtime/T_PROMOTED/<operation_id>/
  → release token delivered on OPERATION_STATUS observation
```

| Cut | Continuation |
|---|---|
| crash after the pass, before the manifest | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; no hash retained; nothing promotes (unchanged) |
| crash after the manifest, before `SETTLEMENT.json` | `SETTLEMENT.json` remains the **sole** commit point, so the operation is `SUPERVISOR_CRASH`-quarantined; the manifest is an **orphan immutable record** of a quarantined operation: it never promotes, never releases capacity, is never rewritten (no-replace), is never removed, and is retained as evidence. No reread and no respawn ever occurs to "complete" it |
| crash after `SETTLEMENT.json` | unchanged: idempotent rename completion, token delivery, capacity retained until a verified disposition |

### U5.3 `SETTLEMENT.json` — exact schema (replaces the carried §W6.1 list)

```text
schema philosophia.officina.t-operation-settlement.v1, atomic no-replace,
keys exactly:

  schema, scientific_outcome, operation_id, charge_event_sha256,
  result_sha256, result_manifest_sha256, promoted_relative_paths,
  bound_sha256, actual_bytes, settled_utc
```

Exactly one key is added: `result_manifest_sha256`. Bindings:

```text
result_manifest_sha256 = SHA-256(the RESULT_MANIFEST.json file's exact
                                 canonical bytes)
result_sha256          = SHA-256(canonical <the manifest's entries array>)
promoted_relative_paths == the manifest's relative_path values, in the same
                           sorted order (a consistency conjunct, checked
                           whenever either object is read)
actual_bytes           == the manifest's total_byte_length
```

`result_sha256` is therefore **unchanged in definition** from §N4.3 — it is the
hash of exactly the canonical array of `{byte_length, content_sha256,
relative_path}` objects sorted by `relative_path` — and it is now
**recomputable from a durable object** without touching a content byte. The
canonical empty result stays exactly §N9.2's value, because an empty `entries`
array canonicalizes to `[]\n`:

```text
entries == []  ⇒  result_sha256 =
  37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

### U5.4 Forward hash DAG and the verifier's resolution

```text
sole hash pass (in memory: relative_path, byte_length, content_sha256 tuples)
        │
        ├─► canonical entries array ──► result_sha256 ─────────┐
        │                                                      │
        └─► RESULT_MANIFEST.json bytes ──► result_manifest_sha256
                                                               │
                                                               ▼
                                                       SETTLEMENT.json
                                                               │
                                                               ▼
                                            release token / promotion / verifier
```

Every edge is forward; nothing downstream feeds back. §N1.6's identifier set
and its resolution clause are replaced by:

```text
The disposition verifier resolves the durable manifest, in the same held-lock
epoch, WITHOUT opening any output content file:
 V1. read RESULT_MANIFEST.json through an O_DIRECTORY|O_NOFOLLOW dir-fd walk;
     regular file; st_nlink == 1; no symlink component
 V2. its exact canonical bytes hash to SETTLEMENT.json's
     result_manifest_sha256; any mismatch ⇒ refuse, release nothing
 V3. SHA-256(canonical entries) == SETTLEMENT.json's result_sha256;
     entry_count and total_byte_length agree with entries; entries are sorted
     and unique; promoted_relative_paths matches the path list
 V4. recursive scientific-field rejection over the whole manifest object
 V5. the §N1.6 prohibited-value check runs against the operation-bound
     identifier set
       { result_sha256, result_manifest_sha256,
         every content_sha256 in the manifest,
         every relative_path in the manifest,
         charge_event_sha256, lease_sha256 }
     — no value of the disposition object and no value of the byte-exact
     decision file may equal any member of that set
 V6. for a QUARANTINED terminal with no manifest (no successful pass ever
     occurred), the set reduces to { charge_event_sha256, lease_sha256 } and
     V1–V4 are vacuous; the absence of a manifest is legal for that terminal
     and is never treated as evidence of anything
```

No verifier, at any point in the contract, reads or rehashes an output content
byte: the manifest is the durable metadata authority, and §N4.4's exhaustive
"why no later path hashes content again" list carries forward with
`RESULT_MANIFEST.json` added as a metadata-only reader.

### U5.5 Custody and retention reconciliation

`RESULT_MANIFEST.json` is a control-plane **record**, not custody: it holds no
output bytes. Two reconciliations are mandatory and are made here:

1. §N2.2's L2 closed control-record set becomes
   `{BOUND.json, OPERATION.json, RUNNING.json, RESULT_MANIFEST.json,
   SETTLEMENT.json, QUARANTINE.json, DELIVERY_ACK.json}`. Without this, the
   §N2.3 P2 subset test would refuse every promoted operation's own
   disposition.
2. The manifest is **never removed** (like `SETTLEMENT.json` and
   `QUARANTINE.json`), so it remains resolvable for the whole lifetime of the
   operation's capacity accounting, including after `.disposed.json` releases
   the reservation. Its presence never blocks a custody-absence proof, because
   it is inside the allowed L2 set.

### U5.6 Worked example (illustrative arithmetic only)

**Non-installable illustration**: patterned synthetic hashes; no object is
created by this document. Its purpose is that both implementers can reproduce
the arithmetic in forward order.

```text
entries (canonical, 265 bytes):
[{"byte_length":1048576,"content_sha256":"cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","relative_path":"a.bin"},{"byte_length":32,"content_sha256":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","relative_path":"sub/b.bin"}]

result_sha256 = 5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3

RESULT_MANIFEST.json (canonical, 638 bytes), with
supervisor_generation_sha256 = "d"×64 and operation_id = "b"×64:
{"created_utc":"2026-07-30T00:00:00.000000000Z","entries":[{"byte_length":1048576,"content_sha256":"cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","relative_path":"a.bin"},{"byte_length":32,"content_sha256":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","relative_path":"sub/b.bin"}],"entry_count":2,"operation_id":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","schema":"philosophia.officina.t-operation-result-manifest.v1","scientific_outcome":false,"supervisor_generation_sha256":"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd","total_byte_length":1048608}

result_manifest_sha256 = e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed
```

---

## U6. Total singleton spawn-record lifecycle (R6)

Closes Sol M3. The four singleton attempt records are `SPAWNING.json`,
`SPAWNING_MIDDLE.json`, `SPAWNING_GROUP.json`, and `SPAWNING_CHILD.json`.

### U6.1 Preflight, before any new attempt

Under `SPAWN.lock`, before `c2`, for each record in the order **child → group
→ middle → spawning**:

```text
P0. absent ⇒ nothing to do
P1. present but MALFORMED (schema id, key set, type, enum, hex, or timestamp
    grammar fails; or the file is not a regular file, or has st_nlink ≠ 1, or
    resolves through a symlink)
    ⇒ FAIL-CLOSED: REFUSED / BOOTSTRAP (retryable = false); unlink NOTHING;
      kill NOTHING; release no live process. The contract never guesses at an
      ambiguous singleton record; an operator must inspect it.
P2. present, well-formed, recorded process LIVE by pid + start identity:
    P2a. its spawning_id equals this attempt's AND the record is byte-identical
         to what this attempt would install
         ⇒ IDEMPOTENT: adopt the existing record; do not rewrite it; continue
           the attempt at the corresponding step
    P2b. otherwise (different spawning_id, or same id with differing bytes)
         ⇒ CONFLICTING LIVE IDENTITY: REFUSED / BOOTSTRAP (retryable = true);
           unlink NOTHING; kill NOTHING. The aged case is handled only by the
           §U2.5 stuck-holder route s2–s4.
P3. present, well-formed, recorded process NOT live — either /proc/<pid> is
    absent, or it is state Z with a matching identity, or it is live with a
    DIFFERENT start identity (PID reuse ⇒ treat as not live and NEVER kill)
    ⇒ DEAD/STALE: prove that exact state, then remove records per §U6.3, and
      continue the attempt
```

### U6.2 `EEXIST` at every no-replace singleton install

At `c2` (`SPAWNING.json`), `c7` (`SPAWNING_MIDDLE.json`), `c11`
(`SPAWNING_GROUP.json`), and `c15` (`SPAWNING_CHILD.json`), an `EEXIST` on the
no-replace install is resolved by re-reading the existing record and applying
§U6.1's P1/P2/P3 to it — never by overwriting, merging, or truncating:

```text
P1 ⇒ REFUSED / BOOTSTRAP (retryable = false), nothing unlinked or killed
P2a ⇒ adopt the existing record and continue at the corresponding step
P2b ⇒ REFUSED / BOOTSTRAP (retryable = true), nothing unlinked or killed
P3 ⇒ remove per §U6.3, then retry the install EXACTLY ONCE; a second EEXIST
     ⇒ REFUSED / BOOTSTRAP (retryable = true)
```

The same discipline applies to `SUPERVISOR_IDENTITY.json`'s no-replace install,
whose collision rule is unchanged (§Z3.5: the loser exits immediately, writing
nothing and unlinking nothing).

### U6.3 The exact ordered removal

**Every** death-proved failure route — §U2.5's stage-0/1/2 routes, the
stuck-holder route s2–s4, the grandchild's first-ack-timeout exit, §U6.1's P3,
and the grandchild's `g3` success path — removes records in exactly this order,
each `unlink` followed by an `fsync` of the parent directory, `ENOENT`
tolerated at every step:

```text
1. SPAWNING_CHILD.json    → fsync(T_SUPERVISOR/)
2. SPAWNING_GROUP.json    → fsync(T_SUPERVISOR/)
3. SPAWNING_MIDDLE.json   → fsync(T_SUPERVISOR/)
4. SPAWNING.json          → fsync(T_SUPERVISOR/)
```

No route may omit `SPAWNING_CHILD.json` — v2.1.2's `c7` route did, which is the
stale-record wedge Sol M3 identified. Because the order is child-first, a crash
mid-removal always leaves a **prefix-consistent** state: a surviving
lower-tier record is never orphaned by a removed higher-tier record, so the
next attempt's §U6.1 preflight sees a coherent tier set and completes the
removal idempotently.

### U6.4 Takeover reconciliation

§W2.9 phase-1 step 3's stale-endpoint list is extended: a client takeover may
unlink `REQUEST.fifo`, `REPLY/*`, `SUPERVISOR_IDENTITY.json`, `SPAWNING.json`,
`SPAWNING_MIDDLE.json`, `SPAWNING_GROUP.json`, and `SPAWNING_CHILD.json` — and
each of the four singleton records **only** under §U6.1's P1/P2/P3 discipline
(never a malformed one, never a live one, only a death-proved stale one) and
**only** in §U6.3's order. It still unlinks no durable `runtime/` evidence, no
`JOURNAL/*`, no `CAPACITY/*`, no quarantined output, and no `T_PROMOTED/**`.
§N10.1's removal-actor rows are updated accordingly in §U9.1.

### U6.5 `EEXIST` / death / cleanup table

| Record state at a new attempt | Live? | Continuation |
|---|---|---|
| absent | — | install (P0) |
| present, malformed | irrelevant | `BOOTSTRAP` (non-retryable); nothing unlinked, nothing killed (P1) |
| present, same `spawning_id`, byte-identical | live | adopt, continue (P2a) |
| present, same `spawning_id`, differing bytes | live | `BOOTSTRAP` (retryable); nothing unlinked (P2b) |
| present, different `spawning_id` | live | `BOOTSTRAP` (retryable); nothing unlinked (P2b) |
| present, pid absent from `/proc` | dead | prove absence; remove per §U6.3; continue (P3) |
| present, pid in state `Z`, identity matches | dead | prove; reap if own child; remove per §U6.3; continue (P3) |
| present, pid live, start identity differs (PID reuse) | not the recorded process | **never kill**; treat as not live; remove per §U6.3; continue (P3) |
| present and aged past `T_SPAWN_BOOTSTRAP_MAX_AGE_NS`, recorded process live | live | only the stuck-holder route s2–s4 may kill, by the tier's permitted signal, then remove per §U6.3 |
| `EEXIST` at install | — | re-read and apply P1/P2/P3; on P3 retry the install exactly once |

---

## U7. Bind the author timestamp (R7)

Closes Sol M4.

### U7.1 The binding

§N1.5 gains conjunct 8e, and the disposition object's key list is
**unchanged**:

```text
8e. disposition.authorized_utc == the byte-exact decision file's line-8
    signed_utc value, compared BYTE-FOR-BYTE over the exact ASCII bytes.
    Any difference — including a differing precision, a differing offset
    spelling, an added or removed character, or any whitespace difference —
    ⇒ REFUSE and release nothing.
```

**Why equality rather than a rename.** Renaming the disposition object's
`authorized_utc` to `signed_utc` would alter a key list that both v2.1.2
reviewers verified in place and would ripple through §Z6.4, §N1.5, and the
object tables. Byte-for-byte equality is the narrower change and is exactly as
strong: after conjunct 8e no timestamp in the authority is independent of the
content-closed signed bytes.

### U7.2 Format and parser

Both fields use the contract's canonical nanosecond UTC form, exactly 30
ASCII characters:

```text
grammar: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{9}Z$
plus a real-date check: month 01..12; day valid for that month and year
(Gregorian, with leap years); hour 00..23; minute 00..59; second 00..59
(a value of 60 is refused — no leap second is representable); the trailing
"Z" is literal and no other offset spelling is accepted.
```

A value failing the grammar or the date check refuses the whole authority
(conjunct 1 for the object's key/type validation, conjunct 8c for the decision
file's byte-exact grammar), releasing nothing.

### U7.3 Canonical byte example

The two byte sequences that must match, from §N1.8's illustration:

```text
decision file, line 8 (44 bytes incl. LF):
signed_utc: 2026-07-30T00:00:00.000000000Z

disposition object fragment (canonical JSON member):
"authorized_utc":"2026-07-30T00:00:00.000000000Z"

compared bytes (30 ASCII characters, identical in both):
2026-07-30T00:00:00.000000000Z
```

### U7.4 The rest of the authority's timestamps

`proof_epoch_utc` and `disposed_utc` in `CAPACITY/<op>.disposed.json`, and
`created_utc` in every control-plane record, are **supervisor-observed** facts,
not author authority. They are never compared against the decision file and
never confer authority; the only author timestamp is `signed_utc`, now bound to
`authorized_utc` by 8e. No independent timestamp remains outside the
content-closed authority.

---

## U8. Deterministic custody-proof summary (R8)

Closes Sol m1. This field is **diagnostic evidence** of the §N2.3 proof; it
**cannot** narrow the absence predicate, which remains exactly P1–P7.

### U8.1 The replacement fields

`CAPACITY/<operation_id>.disposed.json`'s key `custody_locations_proved` is
**replaced** by three keys; the rest of the record is unchanged:

```text
schema philosophia.officina.t-capacity-disposition.v1, atomic no-replace,
supervisor under T_RUNTIME.lock, keys exactly:

  schema, scientific_outcome, operation_id, disposition_id,
  author_disposition_sha256, released_bytes (== bytes_reserved),
  custody_absent (true),
  custody_proof_classes, custody_proof_roots, custody_proof_enumerations,
  proof_epoch_utc, disposed_utc
```

```text
custody_proof_classes: a JSON array of EXACTLY these five tokens, in EXACTLY
  this fixed order (not alphabetical — the order is pinned literally):
    ["SOURCE","OPERATION_DIRECTORY","PROMOTED","TEMP_GRAMMAR",
     "UNKNOWN_NAME_SCAN"]
  All five are always present, because §N2.3 always proves all five classes.
  The array is therefore never empty and never a subset; an absent directory is
  represented in custody_proof_enumerations, never by omitting a class.
  Mapping: SOURCE = L1, OPERATION_DIRECTORY = L2, PROMOTED = L3,
  TEMP_GRAMMAR = L4, UNKNOWN_NAME_SCAN = L5.

custody_proof_roots: object, keys exactly {operations_root, promoted_root},
  each the exact repository-relative path string of the fixed root used in
  the proof epoch:
    "successor/officina/runtime_control/T_SUPERVISOR/operations"
    "successor/officina/runtime/T_PROMOTED"

custody_proof_enumerations: object, keys exactly
  {operations_root_sha256, promoted_root_sha256,
   operation_directory_sha256_or_null}
  Each value is either 64 lowercase hex or null, where the hex is
    SHA-256(canonical <the sorted array of entry-name strings observed by the
            directory-fd enumeration in this proof epoch>)
  with entry names sorted ascending by their byte values and canonical JSON as
  everywhere else. A value is null exactly when that directory was itself
  proved ABSENT by §N2.3's P-abs recursion (so no enumeration existed):
    promoted_root_sha256 is null iff runtime/T_PROMOTED/ is absent;
    operation_directory_sha256_or_null is null iff
      operations/<operation_id>/ is absent;
    operations_root_sha256 is null iff the operations root itself is absent.
```

### U8.2 Verifier and non-narrowing rule

A later reader verifies: the class array equals the fixed five-token array
byte-for-byte and in order; each root string equals the contract's fixed root;
each enumeration value is 64 lowercase hex or `null`; and each `null` is
consistent with the recorded classes. **These checks are diagnostic only.** A
well-formed summary never substitutes for the proof: a release is legal only
because P1–P7 succeeded in that epoch, and a disposition whose summary is
well-formed but whose P-steps failed releases nothing. Conversely a malformed
summary is a record defect that refuses the install (the record is written by
the supervisor itself, so a malformed summary indicates supervisor
inconsistency and takes the record-first invalidity route).

### U8.3 Canonical byte example (illustrative)

For an operation whose directory retains exactly the seven allowed L2 control
records and whose promoted directory is absent:

```text
"custody_proof_classes":["SOURCE","OPERATION_DIRECTORY","PROMOTED","TEMP_GRAMMAR","UNKNOWN_NAME_SCAN"]

enumerated operation-directory entry names (canonical, sorted):
["BOUND.json","DELIVERY_ACK.json","OPERATION.json","QUARANTINE.json","RESULT_MANIFEST.json","RUNNING.json","SETTLEMENT.json"]
operation_directory_sha256 = 3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc

an EMPTY enumeration (canonical "[]\n") hashes to
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570

"custody_proof_enumerations":{"operation_directory_sha256_or_null":"3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc","operations_root_sha256":"<64 hex>","promoted_root_sha256":null}
```

(An operation directory never holds both `SETTLEMENT.json` and
`QUARANTINE.json`; the seven-name list above is the **closed allowed set**
used to illustrate the hash construction. A real proof epoch hashes the
actual sorted entry names it observed.)

---

## U9. Object table, authority, and reconciliation

### U9.1 Durable-object table delta (extends §N10.1)

Authority classes as in §N10.1: `convenience`, `transport`, `witness`,
`runtime`, `author`.

| Object | Path (under `successor/officina/`) | Schema | Install | Writer / lock | Authority | Removed by |
|---|---|---|---|---|---|---|
| **Spawning middle record** *(added)* | `runtime_control/T_SUPERVISOR/SPAWNING_MIDDLE.json` | `t-supervisor-spawning-middle.v1` | no-replace, §3 durability | **CLI** under `SPAWN.lock` at `c7` | runtime | grandchild at `g3`, any death-proved failure route, or a later attempt's §U6.1 P3 — always in §U6.3 order |
| **Spawning group record** *(replaced)* | `…/SPAWNING_GROUP.json` | `t-supervisor-spawning-group.v1` (now with `session_id`, `process_group_id`, `group_verified`) | no-replace, §3 durability | **CLI** under `SPAWN.lock` at `c11`, only after `c10`'s kernel proof | runtime | as above |
| **Spawning child record** *(unchanged keys; removal actors extended)* | `…/SPAWNING_CHILD.json` | `t-supervisor-spawning-child.v1` | no-replace, §3 durability | **CLI** at `c15` | runtime | as above — **never omitted** from any route |
| **Group report frame** *(added)* | boot pipe (no file) | `t-supervisor-group-report.v1` | — | middle child at `m4` | transport | — |
| **Stage release bytes** *(added)* | `rel1`, `rel2` pipes (no file) | one byte `0x01` / `0x02` | — | CLI at `c8` / `c12` | transport | — |
| **Replacement freeze** *(keys extended)* | `…/WATCHDOG/REPLACEMENT_FREEZE/<id>.json` | `t-replacement-freeze.v1` (adds `swap_only`, `supervisor_stop_monotonic_ns`) | no-replace | supervisor under `T_RUNTIME.lock` | runtime | supervisor after the process's durable terminal + archival commit |
| **Replacement resume marker** *(schema pinned)* | `…/REPLACEMENT_FREEZE/<id>.resumed.json` | `t-replacement-resume.v1` | no-replace | supervisor under lock | runtime | as above |
| **Replacement invalidation marker** *(added)* | `…/REPLACEMENT_FREEZE/<id>.invalidated.json` | `t-replacement-invalidation.v1` | no-replace | supervisor under lock | runtime | as above |
| **Result manifest** *(added)* | `…/operations/<op>/RESULT_MANIFEST.json` | `t-operation-result-manifest.v1` | no-replace, §3 durability | supervisor under lock, in the sole-hash-pass epoch | runtime | **never** |
| **Settlement commit** *(keys replaced)* | `…/operations/<op>/SETTLEMENT.json` | `t-operation-settlement.v1` (adds `result_manifest_sha256`) | no-replace | supervisor under lock | runtime | never |
| **Capacity disposed** *(keys replaced)* | `…/CAPACITY/<op>.disposed.json` | `t-capacity-disposition.v1` (§U8.1) | no-replace | supervisor under lock | runtime | never |

Every added object is control-plane, `scientific_outcome: false`, recursively
scientific-field-rejecting, strict-`int`, archival-excluded, and untracked. No
signed activation-protocol §B archival set changes.

### U9.2 Where each repaired fact now lives

| Fact | Class | Object |
|---|---|---|
| the middle child exists and is killable before `setsid` | runtime | `SPAWNING_MIDDLE.json` (no group claim) |
| the process group/session genuinely exists | runtime | `SPAWNING_GROUP.json` with `group_verified: true`, installed only after kernel proof |
| a group was frozen only for a watchdog swap | runtime | `REPLACEMENT_FREEZE.json` with `swap_only: true` |
| a swap-only group was resumed / invalidated | runtime | `.resumed.json` / `.invalidated.json` (immutable, one per transition) |
| the per-file output metadata produced by the sole hash pass | runtime | `RESULT_MANIFEST.json`, bound by `result_manifest_sha256` |
| which custody classes were proved absent | runtime, **diagnostic** | `.disposed.json`'s three proof fields |
| the author's signing instant | author | the decision file's `signed_utc`, bound to `authorized_utc` |
| what the sole hash pass proves and does not prove | contract text | §U1.2's truth table and §U1.3's three residuals |

### U9.3 Reconciliation of every affected item

| Item | Reconciled state |
|---|---|
| Schemas added | `t-supervisor-spawning-middle.v1`, `t-supervisor-group-report.v1`, `t-replacement-resume.v1`, `t-replacement-invalidation.v1`, `t-operation-result-manifest.v1` |
| Schemas changed | `t-supervisor-spawning-group.v1` (+3 keys), `t-replacement-freeze.v1` (+2 keys), `t-operation-settlement.v1` (+1 key), `t-capacity-disposition.v1` (−1 key, +3 keys) |
| Schemas whose interpretation is narrowed | none; §N4.2's *claim* is corrected, its steps are unchanged |
| Paths added | `SPAWNING_MIDDLE.json`, `REPLACEMENT_FREEZE/<id>.invalidated.json`, `operations/<op>/RESULT_MANIFEST.json` |
| Closed sets changed | §N2.2 L2's allowed control-record set gains `RESULT_MANIFEST.json` (§U5.5) |
| Constants | **none added, none moved**; the five signed `T_OUTPUT_*` values untouched |
| Enums | no refusal or `INVALID` token added; three new closed enums live only inside new schemas (`invalid_condition`, `custody_proof_classes`, plus `swap_only`/`group_verified` fixed-`true` fields) |
| Public commands | unchanged: six CLI, two controller, one refusal-first `--officina-bootstrap`, unknown ⇒ exit 2 |
| Signed events | none added, none moved (nine unchanged) |
| Resource values | none added, none moved |
| Q/C surface | none added; every new object is T-development-only and permanently non-citable |
| Verifier duties | §U1.2 (detection truth table), §U5.4 (V1–V6), §U6.1 (P1–P3), §U7.1 (8e), §U8.2 |
| Worked examples | §U5.6 (manifest DAG), §U7.3 (timestamp bytes), §U8.3 (custody summary bytes) |
| Test obligations | §U11 rows 97–120; §N12 rows 81 and 90 replaced |
| Free text / hidden judgement | none: every new field is a hash, an identity, a bounded integer, a closed enum, a fixed literal, a canonical path, or a canonical UTC timestamp |

### U9.4 Inherited-closure qualification

Every closure recorded in §N10.3, §Z12.1, and every prior author closure now
reads **"closed in v2.1.2 (or earlier); confirmation pending independent
v2.1.3 X/Y"**. The five v2.1.2 rows this layer repairs are re-read as:

| v2.1.2 row | v2.1.3 reading |
|---|---|
| Sol C4 / literal K1 hash-once | closed for the **counts**; its **detection claim** is corrected by §U1 (X212-M1) |
| Sol C3 spawn/bootstrap totality | closed for the grandchild; closed for the middle child only **subject to** §U2 |
| Sol M4 later GC | closed **subject to** §U4 (`ack.json` last) |
| Sol M1 / §N5.6 replacement resume | the fallback object is closed; the resume automaton is closed **subject to** §U3 |
| Sol C2 custody proof / M2 / m1 | closed **subject to** §U5 (durable manifest) and §U8 (proof summary) |

No closure in this document is asserted by author fiat; the author line cannot
confirm its own bytes.

---

## U10. Crash-cut matrix (extends §N11)

Every §N11 row carries forward except where §U0 names a replacement. Added and
replaced rows:

| Cut | Single continuation |
|---|---|
| A3-R1/A3-R2/A3-R3 occurs | **no observation, no route, no signal** — named procedural residuals, never `HASH`, never cited (§U1.3) |
| step-2 inode/`st_nlink`/`st_size` mismatch | `HASH` quarantine (unchanged) |
| step-3 length or EOF anomaly | `HASH` quarantine, labelled as a length/EOF anomaly, never as content-substitution detection |
| CLI dies after `c4`, before `c7` | middle child at `m0` sees EOF (or its bound expires) ⇒ `_exit(3)` ⇒ lock reference released with **no record needed** |
| CLI alive but slow between `c4` and `c8` | `m0`'s bound expires at ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` ⇒ `_exit(3)`; the attempt fails closed |
| middle child deliberately `SIGSTOP`ed inside `m0` before `c7` | named A3 procedural residual (§U2.7.2); later clients return `REFUSED`/`BOOTSTRAP` (retryable); no supervisor and no D1 guarantee is affected |
| `m3` finds `sid ≠ pgid ≠ pid` | `_exit(3)`; `c9` gets EOF ⇒ stage-1 route ⇒ `kill(pid_mid)` only, death proved, records removed in §U6.3 order |
| failure anywhere before `c11` | **`killpg` is forbidden**; only `kill(middle_child_pid)` after start-identity validation |
| failure after `c11` | `killpg(process_group_id)` is valid, because `group_verified: true` required kernel proof |
| PID reuse at any tier | start-identity mismatch ⇒ **no kill**, treat as absent, remove records per §U6.3 |
| `EEXIST` at `c2`/`c7`/`c11`/`c15` | §U6.2: P1 ⇒ non-retryable `BOOTSTRAP`; P2a ⇒ adopt; P2b ⇒ retryable `BOOTSTRAP`; P3 ⇒ remove then retry once |
| malformed singleton record found at preflight | fail-closed `BOOTSTRAP`; **nothing unlinked, nothing killed** |
| crash mid-removal of the four records | child-first order leaves a prefix-consistent tier set; the next preflight completes it idempotently |
| non-overdue group frozen for a watchdog swap | **no §W3.3 witness is written**; only `REPLACEMENT_FREEZE` with `swap_only: true` |
| swap-only group, ack not yet observed, deadline not passed | `ACK_PENDING`: remains frozen; **not invalidity**; bounded by `min(deadline, updated + absence timeout)` |
| `ACK_PENDING` resolves by ack | `RESUMABLE`: `.resumed.json` then `killpg(SIGCONT)` |
| `ACK_PENDING` resolves by deadline or absence timeout | `INVALID` (I1/I2): `.invalidated.json` then the signed all-live invalid route |
| crash after `.invalidated.json`, before the invalid terminal set | resume the signed route at its first missing step; no re-classification |
| both replacement markers present | record-first invalidity naming both (A3 residual) |
| prior-generation `REPLACEMENT_FREEZE` | I7 ⇒ `INVALID`; phase 2A settles before any reducer step |
| crash between GC's D1 and D5 | `ack.json` present ⇒ G1 holds ⇒ a later epoch re-verifies and resumes at D1 |
| crash between GC's D5 and D7 | directory empty ⇒ the empty-directory completion rule `rmdir`s it in any later epoch |
| GC `rmdir` `ENOTEMPTY` | record-first invalidity naming the directory; nothing deleted blindly |
| GC any other `errno` | abandon this GC in this epoch, delete nothing further, record-first invalidity naming the path |
| crash after `RESULT_MANIFEST.json`, before `SETTLEMENT.json` | `SUPERVISOR_CRASH` quarantine; the manifest is an orphan immutable record; **no reread, no respawn, no promotion, no release** |
| a `QUARANTINED` operation with no manifest | legal; §U5.4 V6's reduced identifier set applies; absence is never evidence |
| disposition offered with a manifest that fails V2/V3 | refuse; release nothing |
| `authorized_utc` ≠ `signed_utc` by any byte | refuse; release nothing (§U7.1 conjunct 8e) |
| a well-formed custody-proof summary with a failed P-step | release nothing; the summary is diagnostic only and never narrows P1–P7 |

---

## U11. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host
change, process, signature, activation, entropy, T/Q/C work, or scientific
execution is permitted. Obligations become due only after both independent
v2.1.3 confirmations accept these bytes **and** the author signs the amendment
token.

§W10 rows 1–50, §Z12.2 rows 51–74, and §N12 rows 75–96 carry forward, with two
replacements:

- **row 81 replaced:** `custody_proof_classes` is exactly the fixed five-token
  array in the fixed order; the roots are the fixed roots; each enumeration
  value is 64 hex or `null` with the `null` cases exactly as §U8.1 pins;
  `custody_root` is never a proof target; a well-formed summary with a failed
  P-step releases nothing.
- **row 90 replaced:** `result_sha256` is reproducible from
  `RESULT_MANIFEST.json` resolved by `result_manifest_sha256`, and no verifier
  path opens an output content file.

Added:

| # | Test | Covers |
|---|---|---|
| 97 | assert the contract text contains **no** claim of equal-size content-substitution detection; assert each row of §U1.2's truth table, including that an equal-size in-place modification before the pass is **not** signalled and does **not** quarantine | R1, X212-M1 |
| 98 | inode substitution, hard-link introduction, truncation, extension, short read, long read, and wrong-offset EOF each ⇒ `HASH`; each labelled as the anomaly it is | R1 |
| 99 | exactly one write and exactly one hash per output content byte survives the §U1 edit (counts unchanged from §N4) | R1, K1 |
| 100 | the middle child's literal first instruction is the `m0` gate read; no filesystem write, no shared-state change, and no other syscall precedes it, at every injected cut | R2, Sol C1 |
| 101 | CLI death at each cut between `c4` and `c16` ⇒ EOF or bound expiry ⇒ `_exit(3)` ⇒ every lock reference released; no record required in the `c4`→`c7` window | R2 |
| 102 | `m0`/`m5` bounds expire ⇒ `_exit(3)`; `rel1`/`rel2` are `O_NONBLOCK` at inheritance so neither gate can block indefinitely | R2 |
| 103 | `SPAWNING_MIDDLE.json` makes **no** group claim; `SPAWNING_GROUP.json` with `group_verified: true` is installable only after `c10`'s `getsid`/`getpgid` proof | R2, Sol C1 |
| 104 | `killpg` is never issued before `c11`; `kill(pid_mid)` only, and only after start-identity validation; PID reuse ⇒ no kill | R2 |
| 105 | `m3` inequality, middle-child death at each of the five cuts, and grandchild cuts each have one continuation and remove records in §U6.3 order | R2, R6 |
| 106 | the grandchild's own gate (§N3.4) is unchanged and its EOF property holds because the middle child closed `rel3`'s write end at `m1` | R2 (accepted closure preserved) |
| 107 | a swap-only freeze writes **no** §W3.3 witness and no fallback; a deadline freeze still writes its witness | R3, Sol C2 |
| 108 | the three states are mutually exclusive with I-before-S precedence; `ACK_PENDING` is reachable, is not invalidity, and always resolves by `min(deadline, updated + absence timeout)` | R3 |
| 109 | a healthy non-overdue group with ≥ 11 s of remaining lease is **never** invalidated by a watchdog swap; one with less takes I1 honestly | R3 |
| 110 | each of I1–I7 violated singly ⇒ `.invalidated.json` naming that exact condition ⇒ the signed all-live invalid route; crash after the marker resumes without re-classification | R3 |
| 111 | `supervisor_stop_monotonic_ns` is never used to compute `overrun_ns`, never consumed as a §W3.3/§W3.4 witness, and never citable; `REPLACEMENT_FREEZE/**` is unreachable by the watchdog | R3, C1 |
| 112 | GC deletes in exactly `accepted → committed → reply → ack` order with the two directory `fsync`s; eligibility is verified before the first unlink | R4, Sol M1 |
| 113 | crash injected between every pair of D0–D8: cuts before D5 leave `ack.json` and complete via G1; cuts after D5 complete via the empty-directory rule; no state is permanently non-GC-able | R4 |
| 114 | `rmdir` `ENOTEMPTY` ⇒ record-first invalidity; other `errno` ⇒ abandon + record-first invalidity; retry before/during/after GC gives the identical `ALREADY_ACKNOWLEDGED` | R4 |
| 115 | the manifest is built from the sole pass's in-memory tuples with **zero** additional content reads; assert the read count per content byte is exactly 1 across the whole operation | R5, Sol M2 |
| 116 | `result_sha256` recomputes from the manifest's `entries`; `result_manifest_sha256` from its exact bytes; `promoted_relative_paths`, `entry_count`, `total_byte_length`, and `actual_bytes` all agree; §U5.6's digests reproduce | R5 |
| 117 | orphan manifest without `SETTLEMENT.json` ⇒ quarantined, never promoted, never released, never rewritten; `QUARANTINED` with no manifest is legal (V6) | R5 |
| 118 | the L2 allowed set includes `RESULT_MANIFEST.json`, so a promoted operation's own disposition is not refused by P2 | R5, R2-custody reconciliation |
| 119 | §U6.5's ten record states each behave exactly as tabulated, including malformed ⇒ nothing unlinked/killed, and `EEXIST` at all four installs | R6, Sol M3 |
| 120 | `authorized_utc` ≠ `signed_utc` by one byte ⇒ refuse; grammar and real-date checks refuse malformed timestamps; no other timestamp confers authority | R7, Sol M4 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## U12. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The sole hash pass now has an
explicit detection truth table and three named residuals with no route
(§U1.2–§U1.4); the bootstrap is a two-stage gated automaton with four identity
tiers, a per-tier permitted signal, and an exhaustive cut table
(§U2.2–§U2.6); the watchdog swap is three mutually exclusive states with
I-before-S precedence, one immutable marker per transition, and a bounded
resolution (§U3.2–§U3.4); GC is a nine-step ordered deletion with a per-cut
proof and one explicitly predicate-free completion step (§U4.1–§U4.2); the
result metadata is one immutable manifest with a forward hash DAG, a
reproducible worked example, and a six-conjunct verifier resolution
(§U5.1–§U5.6); singleton records have a ten-row `EEXIST`/death/cleanup table
and one ordered removal (§U6.1–§U6.5); the author timestamp is bound
byte-for-byte with a pinned grammar and a byte example (§U7); and the custody
proof summary is a fixed five-token array with pinned roots, enumeration
hashes, and `null` semantics (§U8). No clause resolves to "as reviewed", "as
appropriate", or implementer discretion.

**Compatibility classification.** Unchanged: an engineering/control amendment
surface over the signed harness composite, containing no protocol amendment
except §W6.5's explicitly named supersession of harness §5a's physical
at-or-before-deadline sentence. The signed generic-harness contract
(v2/v2.1/v2.2/v2.3/v2.3.1) and the signed batch-settlement amendment
(v1/v1.1/v1.1.1, including §D1 head/cache completion and §D2 inline
`meter_evidence`) are referenced unchanged. No signed archival set, event,
runtime schema, root, constant, resource value, T band, or Q/C boundary moves.
The import-allowlist delta remains **none**.

**No author cell is reopened.** A3 gains only honesty: §U1.3 names three
procedural residuals where v2.1.2 over-claimed one detection, and §U2.7 names
the two bootstrap residuals. B1 keeps journaled exactly-once effects and
retry-stable replies; §U4 changes only the physical deletion order, and
§N8.3's prefix-first classification — which *is* signed B1's "until a durable
acknowledgement" boundary — is untouched. C1 keeps a watchdog that witnesses
and freezes and never holds runtime authority or settles; §U3's three
replacement records are supervisor objects in a namespace the watchdog cannot
reach, none is a freeze instant, and `ACK_PENDING` creates no evidence and no
terminal. D1 keeps no idle exit, and §U2 removes the last unrecorded
lock-holder window without any unbounded wait. K1 keeps its five signed
constants, its no-replenishment rule, its complete-custody release condition,
and its literal write-once/hash-once **counts** — §U1 corrects only what the
single hash is claimed to prove, and §U1.5 forbids any future layer from
restoring detection by adding a second content hash without a new author
decision. **No new author-choice token is proposed, and none was found to be
unavoidable.**

**Negative space.** This correction creates nothing executable and authorizes
no implementation, commit, host change, process, supervisor, controller,
worker, watchdog, adapter, endpoint, pipe, FIFO, journal instance, tombstone,
spawn record, lease, capability, operation, output bound, framed transport,
result manifest, promoted object, capacity artifact, custody disposition,
author decision file, freeze witness, fallback witness, replacement-freeze
record, entropy, E1/E2/E3 spend, world, learner, candidate, Q attempt, Q/C
object, datum, outcome, Proof, or claim movement. It predicts no qualification
and no C1–C6 outcome. Process invalidity, resource exhaustion, and missing
evidence remain infrastructure facts and are nowhere treated as scientific
evidence. The §U5.6, §U7.3, and §U8.3 examples are patterned synthetic
illustrations that cannot correspond to any real generation, operation, or
activation record, and no file was written from them.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Its only next authorization step is
independent bounded X/Y confirmation of the **v2.1.3 bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
