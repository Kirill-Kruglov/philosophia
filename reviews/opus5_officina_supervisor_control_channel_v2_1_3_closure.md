READY_FOR_OFFICINA_SUPERVISOR_V2_1_3_FINAL_XY_CONFIRMATION

# Officina supervisor/control-channel v2.1.3 — author closure

Date: 2026-07-30.

**Provenance, stated literally.** This closure and
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md`
were written by **Claude Code Opus 5 acting only as the specification
author**, because Claude Code Fable 5 was unavailable. The same author line
wrote v2.1, v2.1.1, and v2.1.2. Neither file is independent review evidence:
the author line cannot confirm its own bytes, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every prior
author closure is an untrusted self-assessment and none of their claims is
used as evidence here; every disposition below is re-derived from the v2.1.2
bytes and the two independent reviews.

## Verdict

```text
READY_FOR_OFFICINA_SUPERVISOR_V2_1_3_FINAL_XY_CONFIRMATION
```

Every finding of both independent v2.1.2 reviews — Opus X212-M1, X212-m1 and
Sol C1, C2, M1, M2, M3, M4, m1, m2 — is closed by exact, executable,
discretion-free text in the v2.1.3 bytes. No repair needed a new author-choice
cell and none was found to be unavoidable; both independent lines said the same
and I agree on re-derivation. All independently accepted v2.1.2 and earlier
closures are carried forward unchanged and are named as frozen in the
correction's header.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **not signable**, and this closure does not make it signable.

**One consequence stated plainly, because it is a reduction and not only a
repair.** §U1 removes a mechanical defence that v2.1.1 had: v2.1.1 detected
same-inode equal-size in-place content substitution by comparing an inline
write-pass hash against a verification-pass hash. Signed K1 says the supervisor
"writes and hashes each byte once", so that second hash was the violation Sol
C4 identified, and v2.1.2's deletion of it was the compliance. The detection
loss is therefore an **entailment of a choice the author already signed**, not
a new choice, which is why both reviewers classified the repair as mechanical
truthfulness. §U1.5 records the tension normatively: no later layer may restore
detection by adding a second content hash or a content-derived stored
reference **without a new author decision on K1**. If the author ever prefers
detection over hash-once, that is where the decision lives; this document does
not make it and does not default it.

## Artifacts and recomputed hashes

```text
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md   (new; 1428 lines)
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md   (unedited; == pinned)
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md   (unedited)
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md     (unedited)
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md            (unedited)
aa25b28cedd813fbd2da36e0087cc9773be86b21a96c828bde57778953933dc7  reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md        (X-line; == pinned)
22e2fb392c5758d7bab6840cafd711a9e4fa74b19b60bd5b05aebbde9b66c878  reviews/sol_officina_supervisor_control_channel_v2_1_2_final_confirmation.md         (Y-line; == pinned)
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

All three pinned hashes verified equal. Review base: at/after commit `dbd148a`
(HEAD `2c1e608`).

Method: static authorship. The inactive implementation was read **read-only**
only where the contract had to stay implementable —
`ALLOWED_ABSOLUTE_IMPORTS` (`src/philosophia/officina/verification.py:35-38`)
and the canonical-JSON definition (`src/philosophia/officina/canonical.py:10-20`).
Nothing was edited, run, probed, or started. The §U5.6, §U7.3, and §U8.3
digests were computed by hashing literal byte strings in a scratch directory
outside the repository; no repository code, test, or Officina process was
executed.

---

## 1. Exact v2.1.2 → v2.1.3 replacement index (summary; the exact index is §U0)

§U0 names **every** superseded sentence, clause, and table row — 38 rows,
quoted at clause level — and lists by name the v2.1.2 and inherited sections
that carry forward verbatim.

| Area | v2.1.2 loci replaced / extended | New locus |
|---|---|---|
| Hash-once honesty | §N4.2's step-3 comment and its "fully retained" sentence; §N4.4's content row and its named-residual paragraph | §U1.1–§U1.5 |
| Bootstrap | §N3.2 `c3`/`c5`/`c6` and its closing sentence; §N3.3 `m1`–`m6` and its closing paragraph; §N3.5 `c7`–`c12`, the three-tier table, `s1`–`s4`, and the "s3 covers every cut" sentence; §N3.6's whole table | §U2.1–§U2.7 |
| Watchdog swap | §N5.6's opening sentence and "Pinned:" block, `R1`–`R6`, the "any conjunct fails" paragraph, its crash table, and the `t-replacement-freeze.v1` key list | §U3.1–§U3.4 |
| GC | §N8.3 consequence 2's arbitrary-order clause; §N8.4's crash-cut bullet | §U4.1–§U4.3 |
| Result metadata | §N1.6's `content_sha256`-in-`SETTLEMENT.json` clause; the carried §W6.1 `SETTLEMENT.json` key list; §W6.1's promotion order; §N2.2 L2's closed record set | §U5.1–§U5.6 |
| Singleton records | §N3.2 `c2` and §N3.5 `c9` (no `EEXIST` rule); §N3.5 `c7`'s removal clause; §N3.6's first-ack row; §Z3.5 `g3`'s unlink clause; §W2.9 phase-1 step 3's list | §U6.1–§U6.5 |
| Author timestamp | §N1.5 conjunct 8d (extended) | §U7.1–§U7.4 |
| Custody proof summary | §N2.5's `custody_locations_proved` key | §U8.1–§U8.3 |
| Tables | §N10.1 (four objects added, three rows replaced); §N11 (26 rows); §N12 rows 81 and 90 replaced, 97–120 added; §N10.3 | §U9.1, §U10, §U11, §U9.4 |

**Zero new constants. Zero new refusal or `INVALID` tokens. Zero new public
commands. Zero import-allowlist delta. Zero signed-event, resource, root, or
archival-set movement.** Every bound introduced reuses an existing constant.

---

## 2. One-to-one disposition of every v2.1.2 finding

### Opus 4.8 X-line

| Finding | Class | Disposition | v2.1.3 locus | What exactly changed |
|---|---|---|---|---|
| **X212-M1** the hash-once repair over-claims an equal-size content-substitution defence it cannot provide | Major, **required** | **closed** | §U1.1–§U1.4 | The step-3 comment `# equal-size content substitution defence` is **deleted**; the "fully retained" sentence is replaced by an explicit statement that with one hash and no earlier trusted reference the case **cannot** be detected. §U1.2 is a twelve-row truth table separating what is mechanical (inode identity via the descriptor held since before the first byte, `st_nlink == 1`, size, read-length, EOF-at-offset, path grammar, counts, and the fact that `content_sha256` truthfully describes the bytes read during the pass) from what is not. §U1.3 names the case as A3-R1, a signed-A3 procedural, T-only, permanently non-citable residual with **no route** — not `HASH`, not any signal. §U1.4 re-labels the surviving step-3 row as a length/EOF anomaly rather than content-substitution detection. Literal K1 counts are untouched: still one write and one hash per content byte |
| **X212-m1** the "hash-once vs detection" tension is fundamental and should be recorded | Minor, **observation** | **closed as recorded** | §U1.5 | Recorded normatively rather than as prose: detecting A3-R1 requires either a second content hash or a content-derived stored reference, both of which violate the signed provider, so the goals are mutually exclusive and the residual statement is the resolution. §U1.5 then **forbids** any later layer from restoring detection that way without a new author decision on K1 — which is exactly the future-proofing the reviewer asked for |

### GPT-5.6 Sol Y-line

| Finding | Class | Disposition | v2.1.3 locus | What exactly changed |
|---|---|---|---|---|
| **Sol C1** the first-fork record is not a valid process-group identity before `setsid()` | Critical, **required** | **closed** | §U2.1–§U2.7 | Exactly the two-stage protocol the reviewer specified. `SPAWNING_MIDDLE.json` (CLI, at `c7`) makes **no** pgid or session claim; `SPAWNING_GROUP.json` with `group_verified: true` is installable only after `c10` proves `getsid(pid_mid) == getpgid(pid_mid) == pid_mid` from the kernel. `killpg` is **forbidden** before that install (only `kill(middle_child_pid)` after start-identity validation), removing the "names a group that need not exist" defect. The middle child's literal first instruction is a bounded gate read on a CLI-owned `O_NONBLOCK` release pipe, so the `c4`→`c7` window — the reviewer's second failing cut — is total **without needing any record**: CLI death gives EOF, and the bound expires regardless. The middle child performs no filesystem write at all, and the ordering the reviewer said was unenforced is now enforced by two release bytes |
| **Sol C2** the non-overdue watchdog-replacement resume is unreachable and dual-valued | Critical, **required** | **closed** | §U3.1–§U3.4 | §W3.5's dead-watchdog action is **explicitly replaced** for non-overdue groups: a swap-only freeze writes **only** the `REPLACEMENT_FREEZE` record and **no** §W3.3 witness, so R4's forbidden witness no longer exists and the happy path is reachable. The "any failed conjunct ⇒ invalidity" rule is **deleted** and replaced by three mutually exclusive states with I-before-S precedence: `ACK_PENDING` (frozen, explicitly not invalidity, bounded by `min(deadline, updated + absence timeout)`), `RESUMABLE`, `INVALID` (I1–I7). One immutable no-replace marker per transition (`.resumed.json`, `.invalidated.json` naming the exact condition) makes every transition crash-completable without mutation. A healthy group with ≥ ~11 s of remaining lease is provably never invalidated by a swap |
| **Sol M1** crash-mid-GC is not completable if `ack.json` is deleted first | Major, **required** | **closed** | §U4.1–§U4.3 | Exactly the reviewer's first option: the pinned order `accepted → committed → reply → ack (last)`, with eligibility (G1/G2/G3) verified **before** the first unlink and two directory `fsync`s. The claim "GC needs no particular deletion order" is **deleted**. §U4.2 proves every cut: before D5 the eligibility witness survives so a later epoch resumes at D1; at or after D5 all phase files are already gone and the explicit **empty-directory completion rule** — the one step that needs no G1 — finishes the hygiene `rmdir`. No state is permanently non-GC-able |
| **Sol M2** the authority refers to durable per-file hashes that do not exist | Major, **required** | **closed** | §U5.1–§U5.6 | Exactly the reviewer's first option: one immutable `RESULT_MANIFEST.json` with sorted `{relative_path, byte_length, content_sha256}` entries, built from the sole pass's **in-memory** tuples with zero additional content reads, bound into `SETTLEMENT.json` by a single added key `result_manifest_sha256`. `result_sha256` keeps §N4.3's definition exactly and is now recomputable from a durable object; the empty case still yields §N9.2's `37517e5f…`. §N1.6's identifier set is re-pointed at the manifest, and §U5.4's V1–V6 verifier resolves it without opening any output content file. Two mandatory reconciliations are made: L2's allowed record set gains `RESULT_MANIFEST.json` (else every promoted operation's own disposition would refuse), and test row 90 is replaced |
| **Sol M3** spawn-record conflicts and failure cleanup are incomplete | Major, **required** | **closed** | §U6.1–§U6.5 | §U6.1 extends the `SPAWN.lock` preflight to all four singleton records with the reviewer's exact four outcomes (byte-identical live ⇒ idempotent; dead/stale ⇒ removable only after exact pid/start/death proof; conflicting live ⇒ `BOOTSTRAP` with no unlink; malformed ⇒ fail-closed, nothing unlinked, nothing killed, no process released). §U6.2 pins `EEXIST` at all four no-replace installs. §U6.3 pins the removal order **child → group → middle → spawning** with a parent-directory `fsync` after each unlink, applied by **every** death-proved route — closing the omission of `SPAWNING_CHILD.json` from v2.1.2's `c7`. §U6.4 extends the takeover stale-endpoint list under the same discipline, and §U9.1 updates the removal actors |
| **Sol M4** the decision file's signed timestamp is not bound to the disposition object | Major, **required** | **closed** | §U7.1–§U7.4 | Conjunct 8e requires `authorized_utc == signed_utc` **byte-for-byte**; any difference refuses and releases nothing. §U7.2 pins the 30-character grammar plus a real-date check (no leap second, no alternative offset spelling). I chose equality over the reviewer's alternative rename because renaming would alter a key list both reviewers verified in place and would ripple through §Z6.4/§N1.5 — the prompt's "if that does not create a wider schema change" condition is not met. §U7.4 states that no other timestamp confers authority |
| **Sol m1** `custody_locations_proved` cannot literally list exact L1–L5 strings | Minor, **required** | **closed** | §U8.1–§U8.3 | Exactly the reviewer's suggested enum plus the root/enumeration hashes: `custody_proof_classes` is the fixed five-token array in a **literally pinned order** (always all five, never a subset, so the empty-set case cannot arise), `custody_proof_roots` names the two fixed roots, and `custody_proof_enumerations` carries three canonical enumeration hashes with pinned `null` semantics for a proved-absent directory. §U8.2 states the non-narrowing rule: the field is diagnostic and a well-formed summary with a failed P-step releases nothing |
| **Sol m2** the post-verification in-place modification residual is not named beside the directory swap | Minor, **required** | **closed** | §U1.3 | Three residuals are now named together: A3-R1 (before/during the pass), A3-R2 (after the pass, before durable settlement/promotion), A3-R3 (the carried directory-name swap). §U1.1 explicitly withdraws any claim that the pass proves future immutability |

### Independently closed v2.1.2 findings, carried forward and **not reopened**

Both reviewers independently closed these; the correction's header names them as
frozen and no clause of v2.1.3 modifies them:

| Finding | Carried locus |
|---|---|
| Opus X211-C1 / Sol C1 (v2.1.1): circular `disposition_id` | §N1.1–§N1.3, §N1.7, §N1.8 — both reviewers reproduced the §N1.8 digests |
| Sol C2 (v2.1.1): complete protocol-created custody set | §N2.1–§N2.4, §N2.6 (§U5.5 only **adds** one allowed L2 record name) |
| Sol C4 (v2.1.1): literal write-once/hash-once **counts** | §N4.1–§N4.3 (§U1 corrects only the detection claim) |
| Sol M1 (v2.1.1): rejected-witness fallback object and `unknown_reason` separation | §N5.1–§N5.5 |
| Sol M2 (v2.1.1) / Opus: collision-safe fd remap | §N6.1–§N6.3 |
| Sol M3 (v2.1.1) / Opus X211-m1: single acknowledgement priority and published frontier | §N7.1–§N7.3 |
| Sol M5 (v2.1.1): byte-exact content-closed decision file | §N1.4, §N1.6 (identifier set re-pointed only) |
| Sol m1 (v2.1.1): absent-scope defaults | §N9.1 |
| Reconciled canonical empty-result hash | §N9.2 |
| Opus X211-m2: grandchild gate; §N3.1/§N3.4 | unchanged; §U2 preserves the EOF property by keeping the middle child's `rel3` write-end close before the second fork |
| Every accepted v2.1.1 surface (§Z1–§Z13), v2.1 surface, v2 surface | unchanged |

---

## 3. Truth table: what the sole hash pass detects and cannot detect

| Anomaly | Detected? | By exactly what |
|---|---|---|
| inode substitution (unlink+recreate, rename-over, new file at the same name) | **yes** | `(st_dev, st_ino)` of the re-resolved descriptor vs the `r` descriptor held since before the first byte existed |
| hard-link introduction | **yes** | `st_nlink == 1` |
| truncation / extension (any size change) | **yes** | `st_size == bytes_written[rel]`, read-length equality, EOF-at-offset |
| short read, long read, wrong-offset EOF (an unstable read during the pass) | **yes** | the pass's length and EOF requirements |
| path grammar, depth, uniqueness, lengths, file count, per-frame and cumulative ceilings | **yes** | write-path header validation, before anything is created |
| worker frame/byte counts disagreeing with the supervisor's counters | **yes**, fail-closed only | `TRANSPORT` quarantine |
| that `content_sha256` describes the bytes read during the pass | **yes, by construction** | the hash is over exactly those bytes through exactly that descriptor |
| **same-inode equal-size in-place modification before the pass** (A3-R1) | **NO** | nothing — no earlier trusted reference, no second hash |
| **same-inode equal-size in-place modification during the pass**, not perturbing length or EOF (A3-R1) | **NO** | ditto |
| **same-inode equal-size in-place modification after the pass**, before settlement/promotion (A3-R2) | **NO** | the pass proves nothing about any later instant |
| same-name substitution of the `out/` directory after the pass (A3-R3) | **NO** | the kernel offers no rename-by-descriptor |

All three undetectable cases are signed-A3 procedural, T-only, permanently
non-citable residuals with **no route**: never `HASH`, never signalled, never
cited. Detected anomalies keep the `HASH` quarantine class, relabelled as the
anomaly they actually are.

---

## 4. Two-stage middle-child / group / grandchild automaton, every cut

```text
CLI                                  middle child                grandchild
c1 preflight + bounded LOCK_NB
c2 SPAWNING.json
c3 boot, rel1(O_NONBLOCK),
   rel2(O_NONBLOCK), rel3
c4 fork ─────────────────────────►   m0 BOUNDED GATE READ(rel1)
c5 close rel1/2/3-read, boot-write      ← literal first instruction
c6 verify pid_mid live + start id
c7 SPAWNING_MIDDLE.json  (no group claim)
c8 release b"\x01" ──────────────►   m1 close rel1*, rel2-w, rel3-w, boot-r
                                     m2 setsid()
                                     m3 verify sid==pgid==pid
c9  read group report ◄──────────    m4 group report
c10 verify getsid/getpgid == pid_mid
c11 SPAWNING_GROUP.json (group_verified: true)
c12 release b"\x02" ─────────────►   m5 BOUNDED GATE READ(rel2)
                                     m6 close rel2-read
                                     m7 fork ──────────────────► g0 GATED READ(rel3)
c13 read bootstrap ◄─────────────    m8 bootstrap report
c14 verify gc pid/start/pgid         m9 _exit(0)
c15 SPAWNING_CHILD.json
c16 release b"\x01" ──────────────────────────────────────────►  g1 scrub fds
c17 bounded identity poll                                        g2 endpoints,
c18 release SPAWN.lock                                              watchdog, ack
                                                                 g3 IDENTITY,
                                                                    remove records,
                                                                    close lock fd
```

| Cut | Middle / grandchild | Continuation |
|---|---|---|
| after `c4`, before `c7` (**no record**) | middle at `m0` | CLI death ⇒ `rel1` write closes ⇒ EOF ⇒ `_exit(3)`; CLI slow ⇒ `m0`'s bound expires ⇒ `_exit(3)`. Total **without any record** — Sol C1's second failing cut |
| after `c7`, before `c8` | middle at `m0` | `SPAWNING_MIDDLE.json` durable ⇒ `s4` kills by pid + start identity, **`kill` only** |
| after `c8`, before `m2` | middle at `m1`/`m2` | CLI death ⇒ `m5`'s gate EOFs or its bound expires ⇒ `_exit(3)`; `killpg` still forbidden |
| `m3` inequality | middle exiting | `_exit(3)`; `c9` gets EOF (middle was the only `boot` writer) ⇒ stage-1 route ⇒ `kill(pid_mid)`, death proved, ordered removal |
| after `m4`, before `c11` | middle at `m5` | report received but group not yet durable ⇒ `s4` governs; `killpg` forbidden |
| after `c11`, before `c12` | middle at `m5` | `group_verified: true` durable ⇒ `s3` may `killpg(process_group_id)`, now a **true** group |
| after `c12`, before `m7` | middle at `m6` | no grandchild; middle death ⇒ `c13` EOF ⇒ stage-2 route |
| after `m7`, before `m8` | grandchild at `g0` | grandchild executes **nothing** but its gated read; middle death ⇒ no EOF (grandchild holds a `boot` writer) ⇒ `c13`'s bound expires ⇒ stage-2 `killpg` reaches both |
| after `m8`, before `c15` | grandchild at `g0` | CLI death ⇒ `rel3` write closes ⇒ `g0` EOF ⇒ `_exit(3)`; CLI wedge ⇒ `s3` |
| after `c15`, before `c16` | grandchild at `g0` | `SPAWNING_CHILD.json` durable ⇒ `s2` kills precisely |
| after `c16` | grandchild initializing | `s2`; the grandchild's own bounded first-ack wait exits it on failure |
| first-ack wait expires | grandchild | kill the watchdog by record, prove death, ordered removal, `_exit(3)` ⇒ lock released |
| identity-install collision | one serving | loser exits writing nothing (unchanged) |
| PID reuse at any tier | — | start-identity mismatch ⇒ **no kill**, treat as absent |

**Invariant.** No process executes an unrecorded action while retaining the
fork-shared lock: the middle child's only pre-record instruction is a bounded
non-blocking gate read that writes nothing and changes no shared state; its
`setsid`/report actions follow `SPAWNING_MIDDLE.json`; its `fork` follows a
kernel-verified `SPAWNING_GROUP.json`; the grandchild's only pre-record
instruction remains its own gated read. Total CLI bound: 30 s + 3 × 10 s +
bounded proof, all existing constants. Two residuals named, not claimed away:
a deliberately stopped CLI (carried) and a deliberately stopped middle child
inside the bounded `m0` window (new, strictly narrower than v2.1.2's unbounded
exposure). D1 is unaffected — no supervisor waits on `SPAWN.lock`.

---

## 5. Exclusive watchdog replacement state machine and the deadline/ack race

```text
watchdog dies ⇒ per live group, against its CURRENT durable lease row:
  now_ns ≥ deadline_ns  ⇒ DEADLINE FREEZE: §W3.3 witness (or §N5 fallback) +
                          §W3.4 invalid route            [unchanged]
  now_ns <  deadline_ns ⇒ SWAP-ONLY FREEZE: SIGSTOP, prove quiescence, and
                          install ONLY REPLACEMENT_FREEZE (swap_only: true).
                          NO witness. NO freeze_ns as evidence. NO overrun_ns.
                          NO fallback.
```

Precedence: **I-conditions first**, then S, else `ACK_PENDING`.

| State | Entry condition | Records | Exit |
|---|---|---|---|
| `ACK_PENDING` | not INVALID and S1 unsatisfied | `REPLACEMENT_FREEZE` only | → `RESUMABLE` on the exact current-table ack; → `INVALID` at `min(deadline_ns, updated_monotonic_ns + T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS)` |
| `RESUMABLE` | not INVALID, S1 (live + exact-table ack) and S2 (identity/member/state) | `.resumed.json` **before** `SIGCONT` | resumed; records removed after the terminal + archival commit |
| `INVALID` | any of I1 deadline passed, I2 replacement failed/timed out, I3 definitive identity/member mismatch, I4 witness/fallback exists, I5 unresolved invalidity, I6 lease superseded, I7 prior generation | `.invalidated.json` naming the exact condition | signed all-live invalid route |

Race resolution: `ACK_PENDING` is explicitly **not** invalidity, which removes
the dual-valued state Sol C2 found (the general rule said invalid, the crash row
said hold frozen). A healthy non-overdue group is never mechanically forced
into invalidity: the replacement path is bounded by
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS + T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`
(10 s + 1 s), so any lease with more remaining time resolves to `RESUMABLE`;
a shorter one takes I1, an honest overdue deadline. `supervisor_stop_monotonic_ns`
is the supervisor's own sample for swap bookkeeping — never an `overrun_ns`
input, never a §W3.3/§W3.4 witness, never citable. All three records are
supervisor objects in a namespace the watchdog cannot reach, so nothing here
becomes a second watchdog or runtime authority, and none can select a valid
terminal. Crash cuts, including both-markers-present and prior-generation
records, are tabulated in §U3.4.

---

## 6. GC deletion-prefix proof with `ack.json` last

```text
D0 verify G1(ack durable) ∧ G2(i ≤ prefix) ∧ G3(archival predicate)
D1 unlink accepted.json     D2 unlink committed.json     D3 unlink reply.json
D4 fsync(key dir)           D5 unlink ack.json  ← LAST   D6 fsync(key dir)
D7 rmdir(key dir)           D8 fsync(JOURNAL)
```

| Cut | Durable state | Completable? | How |
|---|---|---|---|
| before D1 | all four | yes | re-verify G1–G3, start at D1 |
| D1→D2 | committed, reply, ack | yes | **ack present ⇒ G1 holds**; resume at D1 (ENOENT-tolerant) |
| D2→D3 | reply, ack | yes | same |
| D3→D5 | ack only | yes | same |
| D5→D7 | empty directory | yes | the **empty-directory completion rule** — the one step needing no G1 — `rmdir`s in any later epoch |
| after D7 | absent | done | nothing to do |

**Proof.** Every prefix of the sequence that stops before D5 leaves the
eligibility witness (`ack.json`) durable, so the next epoch can re-derive
G1–G3 and complete. Every prefix that stops at or after D5 has already removed
all phase files, so no eligibility question remains. There is no cut at which a
surviving phase file lacks its witness — the permanently-non-GC-able state Sol
M1 identified. At **every** cut the tombstone is intact, so §N8.3's prefix-first
classification answers `ALREADY_ACKNOWLEDGED` for `i ≤ prefix` regardless of
which files exist: exactly-once is preserved and no reducer can run. `errno`:
`unlink` `ENOENT` ⇒ continue; `rmdir` `ENOENT` ⇒ done; `rmdir` `ENOTEMPTY` ⇒
record-first invalidity; any other ⇒ abandon this GC, delete nothing further,
record-first invalidity. GC and frame service serialize under
`T_RUNTIME.lock`, so a retry before, during, or after a GC epoch receives the
identical answer. Per-command archival predicates carry forward verbatim from
§N8.2, including the explicitly vacuous observation-form case.

---

## 7. Result manifest, `SETTLEMENT.json`, and the forward hash DAG

```text
runtime_control/T_SUPERVISOR/operations/<op>/RESULT_MANIFEST.json
schema philosophia.officina.t-operation-result-manifest.v1, no-replace, §3
keys exactly: schema, scientific_outcome, supervisor_generation_sha256,
              operation_id, entry_count, total_byte_length, entries, created_utc
entries: array of {relative_path, byte_length, content_sha256}, sorted
         ascending by relative_path bytes, unique, strict int lengths

operations/<op>/SETTLEMENT.json   (exactly one key added)
keys exactly: schema, scientific_outcome, operation_id, charge_event_sha256,
              result_sha256, result_manifest_sha256, promoted_relative_paths,
              bound_sha256, actual_bytes, settled_utc
```

```text
sole hash pass (in-memory tuples only — zero extra content reads)
   ├─► canonical entries array ──► result_sha256
   └─► RESULT_MANIFEST.json bytes ──► result_manifest_sha256
                                          └──► SETTLEMENT.json ──► token /
                                                                   promotion /
                                                                   verifier
```

Every edge forward; nothing downstream feeds back. `result_sha256` keeps
§N4.3's definition unchanged and is now recomputable from a durable object;
the empty case still yields §N9.2's `37517e5f…` because an empty `entries`
array canonicalizes to `[]\n`. Verifier V1–V6 (§U5.4) resolves the manifest
through an `O_NOFOLLOW` dir-fd walk, checks both hashes, checks
`entry_count`/`total_byte_length`/sortedness/uniqueness/`promoted_relative_paths`,
applies recursive scientific-field rejection, runs the prohibited-value check
over the manifest-derived identifier set, and **never opens an output content
file**; V6 makes a manifest-less `QUARANTINED` terminal legal and never
evidence. Reproducible worked example (§U5.6, patterned synthetic):

```text
entries canonical (265 B) → result_sha256          = 5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3
manifest canonical (638 B) → result_manifest_sha256 = e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed
empty entries "[]\n"       → result_sha256          = 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

Crash cuts: after the pass before the manifest ⇒ `SUPERVISOR_CRASH`, nothing
promotes; after the manifest before `SETTLEMENT.json` ⇒ `SUPERVISOR_CRASH`, the
manifest is an **orphan immutable record** that never promotes, never releases,
is never rewritten, is never removed, and is never "completed" by a reread or
respawn; after `SETTLEMENT.json` ⇒ unchanged. Two reconciliations made:
§N2.2 L2's allowed set gains `RESULT_MANIFEST.json` (without which every
promoted operation's own disposition would refuse), and test row 90 is
replaced.

---

## 8. Singleton spawn-record `EEXIST` / death / cleanup table

Preflight and every no-replace install apply P1/P2/P3 to all four records
(`SPAWNING`, `SPAWNING_MIDDLE`, `SPAWNING_GROUP`, `SPAWNING_CHILD`):

| Record state | Live? | Continuation |
|---|---|---|
| absent | — | install |
| malformed (schema/keys/types/grammar/not-regular/`nlink`≠1/symlink) | irrelevant | **fail-closed** `BOOTSTRAP` (non-retryable); **nothing unlinked, nothing killed, no process released** |
| same `spawning_id`, byte-identical | live | **idempotent**: adopt, do not rewrite, continue |
| same `spawning_id`, differing bytes | live | conflicting live identity ⇒ `BOOTSTRAP` (retryable); nothing unlinked |
| different `spawning_id` | live | conflicting live identity ⇒ `BOOTSTRAP` (retryable); nothing unlinked |
| pid absent from `/proc` | dead | prove absence; remove per order; continue |
| state `Z`, identity matches | dead | prove; reap if own child; remove; continue |
| pid live, start identity differs (PID reuse) | not the recorded process | **never kill**; treat as not live; remove; continue |
| aged past `T_SPAWN_BOOTSTRAP_MAX_AGE_NS`, recorded process live | live | only `s2`–`s4` may kill, by that tier's permitted signal (`killpg` for child/group, `kill` only for middle), then remove |
| `EEXIST` at `c2`/`c7`/`c11`/`c15` | — | re-read and apply P1/P2/P3; on P3 retry the install **exactly once** |

Removal order, applied by **every** death-proved route (stage-0/1/2, `s2`–`s4`,
the grandchild's first-ack timeout, P3, and `g3`), each unlink followed by a
parent-directory `fsync`, `ENOENT` tolerated:

```text
SPAWNING_CHILD.json → SPAWNING_GROUP.json → SPAWNING_MIDDLE.json → SPAWNING.json
```

Child-first means a crash mid-removal always leaves a prefix-consistent tier
set, so the next preflight completes it idempotently. `SPAWNING_CHILD.json` is
never omitted — the stale-record wedge Sol M3 found. §W2.9 phase-1 takeover is
extended to the three new records under the same discipline, and it still
unlinks no durable `runtime/` evidence, `JOURNAL/*`, `CAPACITY/*`, quarantined
output, or `T_PROMOTED/**`.

---

## 9. Timestamp and custody-proof-summary canonical byte examples

**Timestamp binding (§U7).** Conjunct 8e requires byte-for-byte equality;
grammar `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{9}Z$`
plus a real-date check (no leap second, no alternative offset spelling):

```text
decision file line 8 (44 bytes incl. LF):
signed_utc: 2026-07-30T00:00:00.000000000Z

disposition object member:
"authorized_utc":"2026-07-30T00:00:00.000000000Z"

compared bytes (30 ASCII chars, identical):
2026-07-30T00:00:00.000000000Z
```

Mismatch by any byte ⇒ refuse, release nothing. `proof_epoch_utc`,
`disposed_utc`, and every `created_utc` are supervisor-observed facts, never
author authority, never compared.

**Custody-proof summary (§U8).** Fixed five-token array in a literally pinned
order, always all five (so no empty-set case exists), plus fixed roots and
canonical enumeration hashes with pinned `null` semantics:

```text
"custody_proof_classes":["SOURCE","OPERATION_DIRECTORY","PROMOTED","TEMP_GRAMMAR","UNKNOWN_NAME_SCAN"]

enumerated names (canonical, sorted) for the closed allowed L2 set:
["BOUND.json","DELIVERY_ACK.json","OPERATION.json","QUARANTINE.json","RESULT_MANIFEST.json","RUNNING.json","SETTLEMENT.json"]
  → 3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc

empty enumeration "[]\n"
  → 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570

"custody_proof_enumerations":{"operation_directory_sha256_or_null":"3f8e1c99…a0dc","operations_root_sha256":"<64 hex>","promoted_root_sha256":null}
```

`null` exactly when that directory was itself proved absent by the P-abs
recursion. The field is **diagnostic**: it cannot narrow §N2.3's P1–P7, and a
well-formed summary whose P-steps failed releases nothing.

---

## 10. No-regression table

| Signed cell / surface | Status under v2.1.3 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **not reopened; the over-claim removed** | §U1.3 names three output residuals (A3-R1/R2/R3) with no route; §U2.7 names the two bootstrap residuals; §U1.1 withdraws the false detection claim — an A3-boundary honesty repair, not a policy change |
| **B1** durable-journal ack redelivery | **not reopened** | §U4 changes only physical deletion order; §N8.3's prefix-first classification — which *is* signed B1's "until a durable acknowledgement" boundary — and §N7's priority rule are untouched; exactly-once holds at every GC cut |
| **C1** dedicated freezer | **not reopened; strengthened** | §U3's three records are supervisor objects in a namespace the watchdog cannot reach; `swap_only` freezes write no witness; `supervisor_stop_monotonic_ns` is never an overrun input; `ACK_PENDING` creates no evidence and no terminal; the watchdog still holds no lock/capability, writes no `runtime/`, appends no ledger, settles nothing |
| **D1** no idle exit | **not reopened; last unrecorded window removed** | §U2's bounded gates and `SPAWNING_MIDDLE.json` make every post-fork cut recoverable with no unbounded wait; no supervisor waits on `SPAWN.lock` |
| **K1** mediated transport, fixed ceilings, no replenishment | **not reopened; counts unchanged; metadata now durable** | five constants unmoved; write-once/hash-once counts identical to §N4; §U5 adds a metadata manifest built with **zero** extra content reads; §U1.5 forbids restoring detection via a second content hash without a new author decision |
| Signed generic-harness composite (v2/v2.1/v2.2/v2.3/v2.3.1) | **unchanged** | referenced only; §D1 head/cache and §J1–§J3 untouched; the only named protocol supersession remains §W6.5 |
| Signed batch-settlement amendment (v1/v1.1/v1.1.1) | **unchanged** | all-live invalid route, `ARCHIVE` before `RESOLVED`, arithmetic, inline `meter_evidence`, two-token order referenced unaltered; §U3's I-routes and §U4's `HEARTBEAT` predicate use them without weakening |
| Nine signed events | **unchanged** | none added, none moved; no new valid terminal is reachable from a swap, a freeze, a fallback, or a failed output |
| E1/E2/E3 constants and arithmetic | **unchanged** | no value moved; charging remains the cursor difference; the actual interval is never clipped |
| Roots, runtime schemas, T bands, stream ownership, `MAX_CONCURRENT_LEASES` | **unchanged** | new objects are control-plane under existing roots; one author-authority path under `runtime/` inherits `T_PROMOTED`'s archival exclusion |
| Import allowlist and frozen files | **zero delta** | only `os`/`fcntl`/`time`/`hashlib`/`json`/`re`/`pathlib` primitives; `select`/`selectors`/`signal`/`ctypes`/`sys` remain outside; `runtime.py`, `ledger.py`, `checkpoint.py`, `verification.py`, `activation.py` byte-frozen |
| Q/C and scientific boundary | **unchanged** | every new object is `scientific_outcome: false`, recursively scientific-field-rejecting, T-development-only, archival-excluded, untracked, permanently non-citable; the content-closed author authority is unchanged and its timestamp is now bound |
| Archival exclusions / clean-HEAD | **unchanged** | no signed §B set changes; no configuration change authorized |

**No-weakening check.** No fail-closed behavior is weakened *by a v2.1.3
choice*: every new route refuses, holds frozen, or invalidates rather than
releasing, resuming, or accepting. The one reduction relative to v2.1.1 —
equal-size substitution detection — was already effected by v2.1.2's
K1-compliance deletion of the second hash; v2.1.3 only stops mis-describing
it, and §U1.5 fences it. Two places gain liveness without loss: `ACK_PENDING`
(a healthy non-overdue group is no longer forced into invalidity) and the
ordered GC (acknowledged records are no longer strandable) — both gated by
strictly stronger predicates than before.

---

## 11. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this closure or by the correction.** No code, test,
commit, host change, process, signature, activation, entropy, T/Q/C work, or
scientific execution is permitted. Obligations become due only after both
independent v2.1.3 confirmations accept the bytes **and** the author signs the
amendment token.

Implementation obligations, in verification order: (1) the corrected hash-pass
prose and its exact detection set, with the residuals carrying no route; (2)
the four sealed channels with `O_NONBLOCK` stage pipes, the middle child's
bounded gate reads, `SPAWNING_MIDDLE.json` without a group claim, the
kernel-verified `SPAWNING_GROUP.json`, and the per-tier permitted kill signal;
(3) the swap-only freeze that writes no witness, the three exclusive states
with I-before-S precedence, and the two immutable transition markers; (4) the
ordered GC with `ack.json` last, the pre-deletion eligibility check, the two
directory `fsync`s, and the empty-directory completion rule; (5)
`RESULT_MANIFEST.json` built from in-memory tuples, its `SETTLEMENT.json`
binding, and the V1–V6 verifier resolution; (6) the four-record preflight,
`EEXIST` continuations, and the child→group→middle→spawning removal with
`fsync`s; (7) conjunct 8e's byte-for-byte timestamp equality with the pinned
grammar and date check; (8) the fixed custody-proof-class array, roots, and
enumeration hashes as diagnostic-only evidence.

Test obligations: §W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–96 (with
rows 81 and 90 **replaced**), and §U11 rows 97–120, which include at least one
test per Major and Minor of both v2.1.2 reviews. Disposable roots, fake clocks
and meters, no production-compatible real-T artifact, and no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## 12. Bounded final-confirmation questions

Each reviewer must **recompute the SHA-256 of the v2.1.3 bytes** and confirm it
equals
`72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888`, then read
those bytes with v2, v2.1, v2.1.1, v2.1.2, both author signatures, and their own
v2.1.2 review. **Do not trust this closure**: it is authored self-assessment,
not evidence, and every disposition must be re-derived from the correction's own
text.

### 12.1 X-line — independent clean-context Claude Opus 4.8

> Having recomputed and verified the SHA-256 of
> `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md`
> as `72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888`, and
> reading only those bytes, the unedited v2/v2.1/v2.1.1/v2.1.2 documents, the
> two author signatures, and your own v2.1.2 review — treating
> `reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md` as an
> untrusted authored self-assessment:
>
> **Is X212-M1 closed by a truthful detection boundary that keeps literal
> hash-once, is X212-m1 recorded so no later layer can silently re-violate it,
> and does v2.1.3 introduce no new Critical or Major defect, weaken no
> fail-closed behavior by any v2.1.3 choice, promote no watchdog or
> replacement fact to a second runtime authority, and reopen no author cell
> (A3, B1, C1, D1, K1) — yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_3`. Then, per finding, state closed / not
> closed with the exact clause you relied on. Give particular adversarial
> attention to: whether any claim of equal-size content-substitution detection
> survives anywhere in the chain, and whether §U1.2's truth table is complete
> and correct against §N4's steps; whether the §U2 automaton leaves any
> process executing an unrecorded action while retaining the fork-shared lock,
> and whether any `killpg` can be issued against an unverified group; whether
> §U3's three states are genuinely exclusive and total, whether `ACK_PENDING`
> can persist past its bound, and whether any healthy non-overdue group can
> still be forced into invalidity; whether §U4's ordered deletion has any cut
> at which a surviving phase file lacks its eligibility witness; whether
> §U5's manifest can be built or verified without rereading a content byte,
> and whether §U5.6's digests reproduce; and whether §U6's preflight can ever
> unlink a live or malformed record or leave a stale singleton that wedges the
> next conforming attempt. Do not run code, tests, probes, or any Officina
> process; edit nothing.

### 12.2 Y-line — independent clean-context GPT-5.6 Sol

> Having recomputed and verified the SHA-256 of the v2.1.3 correction as
> `72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888`, and
> reading only those bytes, the unedited v2/v2.1/v2.1.1/v2.1.2 documents, the
> two author signatures, and your own v2.1.2 review — treating the author's
> closure as an untrusted self-assessment:
>
> **Are all of your C1, C2, M1, M2, M3, M4, m1, and m2 closed by exact,
> executable text; are every independently closed v2.1.2 repair carried
> forward unmodified; and is every scientific, resource, invalidity, and
> lifecycle field still free of implementer discretion, hidden author
> judgment, and new author cells — yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_3`. Then re-run your eight traces — acyclic
> authority, complete K1 custody, spawn/bootstrap cuts, K1 byte accounting, C1
> evidence authority, fd remap, B1 across all eight commands, and exactness /
> no-regression — against the v2.1.3 text, and state per row whether the
> required result is now achieved. Give particular adversarial attention to:
> whether the middle child can ever be treated as a process-group leader
> before kernel verification, and whether the pre-record `m0` window is
> genuinely bounded in every cut; whether a swap-only freeze can still create
> the witness its own resume predicate forbids, and whether the pending-ack
> state has exactly one continuation; whether the ordered GC is completable at
> every crash cut and whether the empty-directory rule can delete anything
> still owed; whether `RESULT_MANIFEST.json` makes the authority's per-file
> hash check executable without a reread, whether its absence for a
> quarantined terminal is handled, and whether adding it to the allowed L2 set
> can mask real custody; whether the four-record preflight is total over
> malformed, idempotent, conflicting-live, and PID-reuse states; whether the
> bound timestamp closes every independent-time path; and whether the custody
> proof summary can narrow the actual absence predicate. Do not run code,
> tests, probes, or any Officina process; edit nothing.

Neither confirmation authorizes implementation. The author token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes eligible only
if **both** independent confirmations explicitly accept the corrected v2.1.3
bytes, and signing it remains the author's act alone.

---

## 13. Custody and negative-space confirmation

**Exactly two new files were created:**

```text
successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md
```

No existing file was altered. v2, v2.1, v2.1.1, v2.1.2, both author
signatures, the authorship note, all six prior independent reviews, the
harness-contract chain, the batch-settlement amendment chain, the
frozen/inactive implementation, its tests, and every pre-existing dirty or
untracked working-tree file are preserved byte-unmodified. Nothing was
committed or staged. No specification, signature, or review was rewritten or
reinterpreted; every change is a named replacement in §U0.

I created no code, process, supervisor, controller, worker, watchdog,
bootstrap adapter, middle child, endpoint, pipe, FIFO, journal instance,
tombstone, spawn record, spawn intent, lease, capability, operation, output
bound, framed transport, result manifest, promoted object, capacity artifact,
custody disposition, author decision file, freeze witness, fallback witness,
replacement-freeze record, entropy, T activation, scientific datum, Q attempt,
Q/C artifact, candidate, learner, world, E1/E2/E3 spend, or outcome. I started
no process, ran no test, executed no probe or smoke command, and issued no
Officina command. The §U5.6, §U7.3, and §U8.3 digests were produced by hashing
literal byte strings in a scratch directory outside the repository; the example
values are patterned synthetic hex that cannot correspond to any real
generation, operation, or activation record, and no file was written from them.
I authorized no implementation and no signature token, and I predicted no
qualification and no C1–C6 outcome. Process invalidity, resource exhaustion,
and missing evidence remain infrastructure facts and are nowhere treated as
scientific evidence.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent; no runtime, scientific,
capacity, disposition, result-manifest, entropy, or outcome artifact exists.
**T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.**
