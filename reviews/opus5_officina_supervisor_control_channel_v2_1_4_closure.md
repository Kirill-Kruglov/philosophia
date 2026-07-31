READY_FOR_OFFICINA_SUPERVISOR_V2_1_4_FINAL_XY_CONFIRMATION

# Officina supervisor/control-channel v2.1.4 — author closure

Date: 2026-07-31.

**Provenance, stated literally.** This closure and
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md`
were written by **Claude Code Opus 5 acting only as the specification
author**, because Claude Code Fable 5 was unavailable. The same author line
wrote v2.1, v2.1.1, v2.1.2, and v2.1.3. Neither file is independent review
evidence: the author line cannot confirm its own bytes, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every prior
author closure is an untrusted self-assessment and none of their claims is used
as evidence here; every disposition below is re-derived from the v2.1.3 bytes
and the two independent v2.1.3 reviews.

## Verdict

```text
READY_FOR_OFFICINA_SUPERVISOR_V2_1_4_FINAL_XY_CONFIRMATION
```

Every finding of both independent v2.1.3 reviews — Sol C1, C2, M1, M2, M3, M4,
m1 and Opus X213-m1, X213-m2 — is closed by exact, executable,
discretion-free text in the v2.1.4 bytes. No repair needed a new author-choice
cell and none was found to be unavoidable; both independent lines said the same
and I agree on re-derivation. Every independently confirmed v2.1.3 closure is
carried forward unchanged and is named as frozen in the correction's header.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **not signable**, and this closure does not make it signable.

**The authorization state, recorded accurately.** The X line **confirmed**
v2.1.3 (`CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X`) and authorized the token to
become signable *only once the independent Y line also confirmed those same
bytes*. The Y line returned `REVISE_OFFICINA_SUPERVISOR_V2_1_3`, so that
condition was never met and the token never became signable. The X review also
recorded two non-blocking Minors and stated that "if the author elects to patch
them, the patched bytes would take a fresh confirmation." This layer patches
both Minors along with the Y line's seven findings, so **v2.1.4 requires a
fresh X-line and a fresh Y-line confirmation**; the earlier X confirmation does
not carry over to these bytes and is not claimed to.

## Artifacts and recomputed hashes

```text
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md   (new; 1159 lines)
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md   (unedited; == pinned)
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md   (unedited)
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md   (unedited)
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md     (unedited)
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md            (unedited)
6cc52972e6229005f98d15db0fac113a77d2c2382133cc745f387fced845b008  reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md        (X-line; == pinned)
214ac0d5fb1cecf873e8b91ca95079dc67df8018762a18df46e94cb912d7df75  reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md         (Y-line; == pinned)
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

All three pinned hashes verified equal. Review base: at/after commit `3b7d9e6`
(HEAD `2022b7a`).

Method: static authorship. The inactive implementation was read **read-only**
only where the contract had to stay implementable (`ALLOWED_ABSOLUTE_IMPORTS`,
`src/philosophia/officina/verification.py:35-38`; the canonical-JSON
definition, `src/philosophia/officina/canonical.py:10-20`). Nothing was edited,
run, probed, or started. Sol m1's byte count was checked by measuring the
literal line in a scratch directory outside the repository: `"signed_utc"` (10)
+ `":"` + `" "` + 30 + LF = **43**, and the eight §N1.4 lines still sum to
**504**, so no digest in the chain moves.

---

## 1. Exact v2.1.3 → v2.1.4 replacement index (summary; the exact index is §V214.0)

§V214.0 names **every** superseded sentence, clause, and table row — 30 rows,
quoted at clause level — and lists by name the v2.1.3 and inherited sections
that carry forward verbatim.

| Area | v2.1.3 loci replaced / extended | New locus |
|---|---|---|
| Pipe protocol | §U2.1's `boot_pipe`/`rel3` creation lines, its `rel3` blocking sentence and ownership table; §U2.2 `c8`; §U2.4 `c9`/`c12`/`c13`/`c16`; §U2.3 `m0`/`m4`/`m5`/`m8`; §U2.6's whole table incl. the "`m0` sees EOF" and "`c13`'s bound expires" rows | §V214.1.1–§V214.1.5 |
| Orphan manifest | §W4.7's carried `QUARANTINE.json` key list; §U5.2's crash row; §U5.4's `V1`–`V6` | §V214.2.1–§V214.2.4 |
| GC | §U4.1's `D0`–`D8` and its empty-directory paragraph; §U4.2's table and closing proof | §V214.3.1–§V214.3.3 |
| Lock order | §U2.2 `c1`; §U6.1's opening sentence; §U2.5's `s2`/`s3`/`s4` removal clauses | §V214.4.1–§V214.4.3 |
| Watchdog priority | §U3.2's `I2`, `I3`, the "if **ANY** of" clause, `S2`, and the `ACK_PENDING` paragraph; §U3.3's invalidation key list | §V214.5.1–§V214.5.5 |
| A3 statement | §U1.1's final clause; §U1.2's during/before rows and its "yes, by construction" row; §U1.3's `A3-R1` block and part of `A3-R2` | §V214.6.1–§V214.6.3 |
| Timestamp example | §U7.3's "44 bytes incl. LF" | §V214.7 |
| Tables | §U9.1 (two rows extended); §U10 (24 rows); §U11 rows 101/105/112/113/117 replaced, 121–144 added; §U9.4 | §V214.8.1, §V214.9, §V214.10, §V214.8.3 |

**Zero new constants** (the grandchild gate's bound is the arithmetic
`2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`). **Zero new objects, paths, refusal or
`INVALID` tokens, public commands, signed events, resource values, roots, or
archival-set changes. Zero import-allowlist delta.** Two schemas gain one key
each; four channels change flags.

---

## 2. One-to-one disposition of every v2.1.3 finding

### GPT-5.6 Sol Y-line

| Finding | Class | Disposition | v2.1.4 locus | What exactly changed |
|---|---|---|---|---|
| **Sol C1** the supposedly bounded boot reports use a blocking descriptor | Critical, required | **closed** | §V214.1.1–§V214.1.5 | All four bootstrap channels are now `os.pipe2(os.O_NONBLOCK)`, so **no blocking syscall exists in the bootstrap** and every deadline is evaluable at every instruction. Two pinned helpers (`BOUNDED_READ`, `BOUNDED_WRITE`) give one continuation for `EAGAIN`/`EWOULDBLOCK` (paced retry against the same deadline), `EINTR`, EOF-before-a-complete-frame, malformed/overlong/duplicate/trailing bytes, every other read error, `EPIPE`, and every other write error; each of `c8`, `c9`, `c12`, `c13`, `c16`, `m0`, `m4`, `m5`, `m8`, `g0` is mapped to one named stage route. Frames are ≤ `T_CONTROL_FRAME_MAX_BYTES` ≤ `PIPE_BUF` (verified per write end at creation), so a nonblocking write is all-or-`EAGAIN` and cannot be partial. The exact deadlocking cut Sol named — middle child dies between `m7` and `m8` while the grandchild holds a `boot` write copy — now resolves: `c13`'s bound fires, stage-2 `killpg(process_group_id)` reaches the grandchild, death is proved, records are removed, the lock is released |
| **Sol C2** an orphan-manifest quarantine can never satisfy the disposition verifier | Critical, required | **closed** | §V214.2.1–§V214.2.4 | Exactly the repair Sol specified. `QUARANTINE.json` gains `result_manifest_sha256_or_null`, non-null exactly when a durable manifest exists at install. The record-first crash reducer completes the signed invalid terminal set and installs that binding (Q1–Q4, idempotent, no-replace, `EEXIST`-resolved). The verifier splits into three exclusive branches selected by durable objects alone: `B-P` (settled, resolve through `SETTLEMENT.json`), `B-QM` (quarantined with manifest, resolve through `QUARANTINE.json`, validate the manifest standalone, use its identifiers for the content prohibition, **no settlement required, no output reread**), `B-QN` (quarantined with no manifest, require null **and** physical absence; manifest checks vacuous only here). Every other combination — orphan file without binding, binding without file, hash mismatch, both terminals, neither, duplicate or partial — refuses and releases nothing. The signed K1 custody-absence release is restored for all admitted quarantine states with **no** weakening of `bytes_reserved` accounting |
| **Sol M1** GC loses the authority required to re-prove G3 | Major, required | **closed** | §V214.3.1–§V214.3.3 | Exactly the order the repair prompt pins: `committed → reply → ack → accepted (last)`, with G1/G2/G3 verified before the first deletion and G3 **selected and bound by `accepted.json`'s `command` and `effect_plan`**. A dedicated `D6` finalization rule re-verifies the permanent tombstone prefix plus the G3 authority still readable in `accepted`, then deletes `accepted` last; only then is the predicate-free empty-directory completion legal. Deleting `ack.json` before `accepted` is sound because the tombstone's `acknowledged_prefix_occurrence` is permanent and, by §Z1.9's contiguous construction, `i ≤ prefix` **is** the durable proof of acknowledgement. The nine per-command G3 bindings are tabulated, including the observation form's vacuous case, whose vacuity is still *selected* from `accepted` |
| **Sol M2** singleton preflight is simultaneously before and under the lock | Major, required | **closed** | §V214.4.1–§V214.4.3 | One order: `c1a` bounded acquire (or the stuck-holder route), `c1b` full §U6.1 preflight **under the acquired lock**, then `c2`. A normative rule forbids any preflight read that can lead to adoption, removal, kill, or mutation before `c1a`. The unlocked stuck-holder route is corrected too: `s2`/`s3`/`s4` may read, validate, kill (tier-permitted, identity-proved), prove death, and retry — but **remove nothing**; removal happens at `c1b`. All four `EEXIST` continuations are evaluated inside the same held lock epoch |
| **Sol M3** the watchdog replacement partition and invalid marker are not total | Major, required | **closed on all three gaps** | §V214.5.1–§V214.5.5 | (1) I1–I7 are evaluated in pinned numeric priority; the marker records the **first true** condition plus a sorted `diagnostic_conditions` set, whose routing irrelevance is *proved* (every I routes to the identical signed all-live invalid route and no clause reads `invalid_condition`). (2) I2 becomes "no **valid** acknowledgement of the **exact current** `table_seq` by the bound", with validity pinned (schema, generation, exact table); stale, wrong-table, wrong-generation, and malformed acks never satisfy it, so the bound always fires. (3) I3 absorbs every pre-resume member state other than exactly `T` after identity match, so `S2 ≡ ¬I3` and the S1-true/S2-false gap vanishes. The partition becomes a three-step evaluation that is exhaustive and disjoint, with a fifteen-row race table in which every row has exactly one continuation |
| **Sol M4** the during-pass A3 statement still claims a promoted-byte hash | Major, required | **closed** | §V214.6.1–§V214.6.3 | The clause "the recorded hash still truthfully describes the promoted bytes" is **deleted**. `A3-R1` splits into `A3-R1a` (completed before the pass — a real single file state) and `A3-R1b` (concurrent with the pass — successive `pread` chunks may come from different content states, so the hash can describe a **mixed stream that never existed as any single file state** and need not equal the final inode or the promoted bytes). `A3-R2` gains the explicit consequence that `result_sha256` can differ from the promoted bytes. The normative claim is reduced to exactly one: the hash describes the **byte stream read**. All four residuals are procedural, T-only, permanently non-citable, unobservable under literal hash-once, and have **no `HASH` route** |
| **Sol m1** the signed timestamp line's byte count is off by one | Minor, required | **closed** | §V214.7 | 44 → **43** bytes including LF, with the arithmetic shown (10 + 1 + 1 + 30 + 1). I verified it independently. The equality rule, the grammar and real-date check, the 504-byte total, and the decision-file hash `0773f29c…` are all unchanged, and the eight line lengths `53+58+60+91+79+81+39+43` are re-derived to 504 |

### Opus 4.8 X-line (which **confirmed** v2.1.3)

| Finding | Class | Disposition | v2.1.4 locus | What exactly changed |
|---|---|---|---|---|
| **X213-m1** the result-manifest verifier does not cleanly cover a QUARANTINED terminal carrying an orphan manifest | Minor, non-blocking observation | **closed** | §V214.2.1–§V214.2.3 | Same defect the Y line raised as its C2, and the repair is the stronger of the two suggestions: rather than only widening V6's exemption, the orphan manifest is **bound** in `QUARANTINE.json` and gets its own exclusive verified branch `B-QM`, so the disposition is not merely permitted but *cryptographically anchored* to the quarantine record. The reviewer's stated consequence — up to 268 MiB per affected operation stranded forever against the 32 GiB aggregate — is removed |
| **X213-m2** the `m0` "sees EOF" crash-row phrasing is inaccurate | Minor, prose | **closed** | §V214.1.5 | The row is replaced: during `m0` the middle child still holds its own inherited `rel1` write copy (closed only at `m1`), so CLI death alone does not deliver EOF; the governing guarantee is the `m0` **bound**, exactly as §U2.1 designates. The descriptor/errno ownership table now makes each cut's mechanism explicit per channel, so EOF is asserted only where a sole-writer argument supports it (`rel2` after `m1`, `rel3` throughout, `boot` before the second fork) |

### Independently confirmed v2.1.3 closures, carried forward and **not reopened**

The X line confirmed all of these on re-derivation and reproduced four digests
from the bytes; the Y line independently agreed on each row marked "Closed" in
its disposition table. The correction's header names them as frozen:

| Closure | Carried locus | Reproduced digests |
|---|---|---|
| X212-M1 / X212-m1: truthful hash-once boundary and the normative bar | §U1.4, §U1.5 | — |
| Sol C1 (v2.1.2): two-stage middle-child gate, verified group identity, per-tier kill discipline | §U2.2–§U2.5, §U2.7 (mechanics repaired in §V214.1, semantics untouched) | — |
| Sol C2 (v2.1.2): swap-only vs deadline freeze split; immutable per-transition markers | §U3.1, §U3.3 | — |
| Sol M2 (v2.1.2): durable result manifest and its `SETTLEMENT.json` binding | §U5.1–§U5.3, §U5.6 | `5359c361…`, `e4ec3182…` |
| Sol M3 (v2.1.2): singleton preflight P0–P3, `EEXIST`, ordered removal | §U6.1–§U6.5 (order relative to the lock repaired in §V214.4) | — |
| Sol M4 (v2.1.2): byte-bound author timestamp | §U7.1, §U7.2, §U7.4 | — |
| Sol m1 (v2.1.2): deterministic custody-proof summary | §U8 | `3f8e1c99…`, `37517e5f…` |
| Acyclic content-closed disposition authority | §N1.1–§N1.4, §N1.7, §N1.8 | `e330a384…`, `0773f29c…` |
| Complete custody set L1–L5 / P1–P7, incl. `RESULT_MANIFEST.json` in L2 | §N2, §U5.5 | — |
| Literal K1 write-once/hash-once counts | §N4.1–§N4.3 | — |
| Fallback witness namespace; fd remap; ack priority and frontier; absent defaults; canonical empty hash; per-command archival predicates; prefix-first classification | §N5, §N6, §N7, §N8.2, §N8.3, §N9 | — |

---

## 3. Pipe descriptor / errno ownership table and every bootstrap cut

**Channels** (all four `os.pipe2(os.O_NONBLOCK)`, `PC_PIPE_BUF ≥ 4096`
verified per write end at creation):

| End | Held by | Closed by / when | Used at | Errno handled |
|---|---|---|---|---|
| `boot` read | CLI | CLI after `c13` | `c9`, `c13` reads | `EAGAIN`, `EINTR`, EOF, other |
| `boot` write | middle child; grandchild inherits a copy at `m7` | CLI at `c5`; middle at `m8`; grandchild at `g1` scrub | `m4`, `m8` writes | `EAGAIN`, `EINTR`, `EPIPE`, other |
| `rel1` read | middle child | CLI at `c5`; middle at `m1` | `m0` read | `EAGAIN`, `EINTR`, EOF, other |
| `rel1` write | CLI **and** middle child until `m1` | CLI at `c8`; middle at `m1` | `c8` write | `EAGAIN`, `EINTR`, `EPIPE`, other |
| `rel2` read | middle child | CLI at `c5`; middle at `m6` | `m5` read | as `rel1` read |
| `rel2` write | CLI (middle closes its copy at `m1`) | CLI at `c12` | `c12` write | as `rel1` write |
| `rel3` read | grandchild (inherited) | CLI at `c5`; grandchild at `g1` | `g0` read | as `rel1` read |
| `rel3` write | **CLI only** after `m1` | CLI at `c16`; middle at `m1`, before the second fork | `c16` write | as `rel1` write |

The middle child closing `rel3` **write** at `m1` while retaining `rel3`
**read** for inheritance is what makes the CLI the grandchild's sole `rel3`
writer — the confirmed EOF property, preserved exactly.

**Every bootstrap cut** (CLI / middle / grandchild death or stall at every
instruction):

| Death or stall point | Continuation | Mechanism |
|---|---|---|
| CLI dies `c4`→`c7` | middle `_exit(3)` | **`m0` bound** (the middle holds its own `rel1` write copy until `m1`, so EOF is not guaranteed — X213-m2's correction) |
| CLI dies `c7`→`c8` | as above, plus `s4` may `kill(middle_child_pid)` | bound + durable `SPAWNING_MIDDLE.json` |
| CLI dies `c8`→`c9` | middle `_exit(3)` at `m4` | `EPIPE` (no reader) |
| CLI dies `c9`→`c12` | middle `_exit(3)` at `m5` | **EOF** (all `rel2` writers closed) |
| CLI dies `c12`→`c16` | middle `_exit(3)` at `m8` (`EPIPE`); grandchild `_exit(3)` at `g0` | **EOF** on `rel3` (CLI was sole writer) |
| CLI dies after `c16` | grandchild proceeds; `s2` for later clients | durable `SPAWNING_CHILD.json` |
| middle dies at `m0` | `c9` **EOF** ⇒ stage-1 ⇒ `kill(pid_mid)` only | middle was the only `boot` writer |
| middle dies `m1`→`m4` | `c9` **EOF** ⇒ stage-1 | as above |
| middle fails `m3` (`sid≠pgid≠pid`) | `_exit(3)` ⇒ `c9` EOF ⇒ stage-1 | kernel self-check |
| middle dies `m4`→`m7` | `c13` **EOF** ⇒ stage-2 ⇒ `killpg(process_group_id)` | no grandchild yet |
| **middle dies `m7`→`m8`** | `c13` **bound** ⇒ stage-2 `killpg` reaches the grandchild ⇒ death proved ⇒ ordered removal ⇒ lock released | the grandchild holds a `boot` write copy so no EOF arrives; the bound is now executable — **Sol C1's deadlock is gone** |
| middle dies `m8`→`m9` | ordinary; bootstrap proceeds | `c13` already returned |
| grandchild dies at `g0` | `c17` expires ⇒ stage-2 | bounded identity poll |
| grandchild stalls at `g0`, CLI alive but not releasing | `_exit(3)` | the `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` gate bound |
| grandchild dies `g1`→`g3` | `c17` expires ⇒ stage-2; or its own bounded first-ack wait exits it | — |
| first-ack wait expires | kill watchdog by record, prove death, ordered removal, `_exit(3)` | — |
| `EPIPE` at `c8`/`c12`/`c16` | stage-1 / stage-2 / stage-2 | — |
| malformed / overlong / duplicate / trailing report bytes | the same stage route as a deadline | fail-closed, never partial acceptance |
| PID reuse at any tier | **no kill**; treat as absent; removal at `c1b` under the lock | start-identity mismatch |

No blocking syscall, no pipe cycle retaining `SPAWN.lock`, and every cleanup on
the already-signed identity/kill discipline. The two §U2.7 A3 residuals (a
deliberately stopped CLI; a deliberately stopped middle child in the bounded
`m0` window) are unchanged and not enlarged.

---

## 4. Three-branch verifier and the K1 release trace

```text
branch selection, from durable objects alone, exactly one:
  B-P   SETTLEMENT.json durable
  B-QM  QUARANTINE.json durable ∧ result_manifest_sha256_or_null ≠ null
  B-QN  QUARANTINE.json durable ∧ result_manifest_sha256_or_null = null
  every other combination ⇒ REFUSE, release nothing
```

| Branch | Manifest resolution | Settlement needed? | Prohibited-value set | Reads content? |
|---|---|---|---|---|
| `B-P` | `P1`–`P5`: hash matches `SETTLEMENT.json`'s `result_manifest_sha256`; `result_sha256` recomputes | yes | `result_sha256`, `result_manifest_sha256`, every `content_sha256`, every `relative_path`, `charge_event_sha256`, `lease_sha256` | **no** |
| `B-QM` | `QM1`–`QM6`: hash matches **`QUARANTINE.json`'s** `result_manifest_sha256_or_null`; the manifest validates standalone (schema, keys, `operation_id`, counts, sortedness, uniqueness); `orphan_result_sha256` computed for the prohibition set only | **no** | `orphan_result_sha256`, `result_manifest_sha256_or_null`, every `content_sha256`, every `relative_path`, `charge_event_sha256`, `lease_sha256` | **no** |
| `B-QN` | `QN1`–`QN4`: null binding **and** physical absence proved by the same lock epoch's paired stat/enumeration | **no** | `charge_event_sha256`, `lease_sha256` | **no** |

**K1 release trace, orphan-manifest case** (the route that was impossible in
v2.1.3):

```text
sole hash pass completes → RESULT_MANIFEST.json durable
crash before SETTLEMENT.json
  → record-first reducer completes the signed invalid terminal set
  → installs QUARANTINE.json (SUPERVISOR_CRASH) binding
    result_manifest_sha256_or_null = SHA-256(manifest bytes)
  → bytes_reserved remains fully accounted (unchanged)
author removes every custody location outside T
  → §N2.3 P1–P7 prove all five classes absent in ONE lock epoch
  → §N1.5 conjuncts 1,3,4,5,6,8a–8e,11 verify (conjunct 4's terminal is the
    quarantine record; custody_parent_sha256 binds its bytes)
  → branch B-QM verifies QM1–QM6
  → CAPACITY/<op>.disposed.json installs once, releasing exactly bytes_reserved
```

Mismatch routes, all releasing nothing: orphan file without binding; binding
without file; hash mismatch; both terminals durable (record-first invalidity);
neither durable; duplicate or partially installed object. Custody interaction:
`RESULT_MANIFEST.json` is already inside L2's closed record set, so an orphan
manifest never blocks P2 and never counts as custody. Retention: the manifest
and the quarantine record are never removed, so `B-QM` stays resolvable for the
whole lifetime of the operation's accounting.

---

## 5. GC prefix proof using only the files present after each cut

```text
D0 verify G1(ack) ∧ G2(prefix) ∧ G3(selected and bound by accepted.json's
   command and effect_plan)
D1 unlink committed.json   D2 unlink reply.json   D3 fsync
D4 unlink ack.json         D5 fsync
D6 FINALIZE: re-verify F1(prefix, permanent tombstone) ∧ F2(G3 from accepted)
   ∧ F3(committed, reply, ack all absent)
D7 unlink accepted.json ← LAST   D8 fsync   D9 rmdir   D10 fsync
```

| Cut | Files present | Eligibility re-derivable from those files? | Resume at |
|---|---|---|---|
| before `D1` | accepted, committed, reply, ack | **yes** — G1 from ack, G2 from the tombstone, G3 from accepted | `D0` |
| `D1`→`D2` | accepted, reply, ack | **yes** — same three sources | `D1` |
| `D2`→`D4` | accepted, ack | **yes** — same three sources | `D1` |
| `D4`→`D7` | **accepted only** | **yes** — F1 from the permanent tombstone, F2 from accepted, F3 holds | `D6` |
| `D7`→`D9` | none | not needed | empty-directory completion |
| after `D9` | absent | — | complete |

Two authorities survive longest and are exactly the two the finalization rule
needs: the **permanent tombstone** (acknowledgement, via `i ≤ prefix`, which by
§Z1.9's contiguous construction *is* the durable proof) and **`accepted.json`**
(which per-command predicate applies, and its identities). At every cut before
`D7` the G3 predicate is re-selectable — the information Sol M1 showed was
destroyed by deleting `accepted` first. No owed reply is deleted before
acknowledgement: `reply.json` goes at `D2`, strictly after `D0` proved
`i ≤ prefix`. `errno`: `unlink ENOENT` continue; `rmdir ENOENT` done;
`rmdir ENOTEMPTY` record-first invalidity; any other abandon + record-first
invalidity; **no `EEXIST` exists in GC**. GC and frame service serialize under
`T_RUNTIME.lock`, and prefix-first classification keeps GC timing invisible at
every cut.

---

## 6. Lock / preflight / `EEXIST` order table

| Step | Lock state | Permitted actions |
|---|---|---|
| before `c1a` | not held | **none** on any singleton record |
| stuck-holder `s1`–`s5` | **not held** | read, validate identity and age, kill (tier-permitted: `killpg` for child/group, `kill` only for middle), prove death, retry acquisition once — **no unlink, no adoption, no install, no read-modify-write** |
| `c1a` | acquiring (bounded `LOCK_EX\|LOCK_NB`) | none |
| `c1b` | **held** | full §U6.1 P0–P3 over the four records in child → group → middle → spawning order: adopt (P2a), refuse (P1, P2b), remove with §U6.3 order and `fsync`s (P3) |
| `c2`, `c7`, `c11`, `c15` | **held** | install; `EEXIST` ⇒ re-read and apply P1/P2/P3 under the same held lock; P3 ⇒ ordered removal then retry the install exactly once |
| stage-0/1/2 failure routes | **held** | tier-permitted kill, death proof, §U6.3 ordered removal, release the lock |
| `g3` success path | held by the grandchild | §U6.3 ordered removal, then close the lock fd |
| client takeover (§W2.9 phase 1, §U6.4) | **held** (`SPAWN.lock`, unchanged) | the same P1/P2/P3 discipline; unlinks no durable `runtime/` evidence, `JOURNAL/*`, `CAPACITY/*`, quarantined output, or `T_PROMOTED/**` |

---

## 7. Watchdog I-priority and the ack/deadline race truth table

Evaluation, one locked observation, one `now_ns` sample reused by every
predicate, all `/proc` member reads inside the same epoch:

```text
step 1  evaluate I1→I2→I3→I4→I5→I6→I7 in priority; first true ⇒ INVALID,
        invalid_condition = that first one,
        diagnostic_conditions = the sorted set of all true ones
step 2  else if a VALID ack of the EXACT current table_seq is durably observed
        ⇒ RESUMABLE          (S2 need not be retested: ¬S2 ⇒ I3 ⇒ step 1)
step 3  else ⇒ ACK_PENDING   (non-invalid, non-terminal, evidence-free)
```

| # | `now ≥ dl` | ack | members | witness/fallback | gen | lease | State | condition |
|---|---|---|---|---|---|---|---|---|
| 1 | no | valid exact | all `T` | none | current | current | **RESUMABLE** | — |
| 2 | no | none, pre-bound | all `T` | none | current | current | **ACK_PENDING** | — |
| 3 | no | none, bound passed | all `T` | none | current | current | **INVALID** | I2 |
| 4 | **yes** | valid exact | all `T` | none | current | current | **INVALID** | I1 |
| 5 | **yes** | none | all `T` | none | current | current | **INVALID** | I1 |
| 6 | no | valid exact | one `R`/`S`/`D` | none | current | current | **INVALID** | I3 |
| 7 | no | none, pre-bound | one `R`/`S`/`D` | none | current | current | **INVALID** | I3 |
| 8 | **yes** | none, bound passed | one dead | none | current | current | **INVALID** | I1 (diagnostics `[I1,I2,I3]`) |
| 9 | no | valid exact | all `T` | **present** | current | current | **INVALID** | I4 |
| 10 | no | valid exact | all `T` | none | current | **G5 blocked** | **INVALID** | I5 |
| 11 | no | valid exact | all `T` | none | current | **superseded** | **INVALID** | I6 |
| 12 | no | valid exact | all `T` | none | **prior** | current | **INVALID** | I7 |
| 13 | no | **stale/wrong-table/malformed only**, pre-bound | all `T` | none | current | current | **ACK_PENDING** | — |
| 14 | no | **stale/wrong-table/malformed only**, bound passed | all `T` | none | current | current | **INVALID** | I2 |
| 15 | no | replacement `os.fork` failed | all `T` | none | current | current | **INVALID** | I2 (immediate) |

Rows 6 and 13/14 are the two v2.1.3 gaps, now covered. Every row has exactly
one continuation; none has zero or two. A healthy non-overdue group is never
invalidated merely by a pending ack (row 2 → row 1 within
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS + T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`). All
three replacement records remain supervisor objects in a namespace the watchdog
cannot reach; `observed_monotonic_ns` is bookkeeping and is never an
`overrun_ns`, a witness, or a freeze instant.

---

## 8. A3 hash-stream truth table

| Anomaly | Detected? | What the recorded hash then describes |
|---|---|---|
| inode substitution | **yes** | — quarantined, never promoted |
| hard-link introduction | **yes** | — |
| truncation / extension | **yes** | — |
| short read, long read, wrong-offset EOF | **yes** | — |
| path grammar, depth, uniqueness, lengths, counts, ceilings | **yes** | — |
| worker count cross-check mismatch | **yes**, fail-closed | — |
| **A3-R1a** modification completed **before** the pass | **NO** | the modified bytes — a real single file state, also what would be promoted if nothing further changes |
| **A3-R1b** modification **concurrent with** the pass | **NO** | a **mixed stream** from different content states; need not equal any single file state, the final inode, or the promoted bytes |
| **A3-R2** modification **after** the pass, pre-settlement | **NO** | the pre-modification stream; `result_sha256` can differ from the promoted bytes |
| **A3-R3** `out/` directory swap after the pass | **NO** | — the promoted tree may be unrelated |
| nothing anomalous | — | the exact byte stream read, which absent R1a/R1b/R2/R3 is also the promoted content |

The single normative claim is that `content_sha256` describes **the exact byte
stream read**. All four residuals are procedural, T-only, permanently
non-citable, unobservable under literal hash-once (detecting them needs a second
content hash or a content-derived stored reference, which §U1.5 bars without a
new K1 author decision), and have **no `HASH` route**. Every downstream use is
unaffected: no clause requires `result_sha256` to equal a hash of the promoted
bytes; the release token carries it as the operation's result identity, and
promotion is a rename that reads nothing.

---

## 9. No-regression table

| Signed cell / surface | Status under v2.1.4 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **not reopened; last over-claim removed** | §V214.6 splits R1a/R1b and deletes the promoted-byte claim; four residuals, no route, non-citable; §U2.7's two bootstrap residuals unchanged and not enlarged |
| **B1** durable-journal ack redelivery | **not reopened** | §V214.3 changes only the physical deletion order; prefix-first classification and the frontier/priority rules are untouched; no owed reply is deleted before `i ≤ prefix` |
| **C1** dedicated freezer | **not reopened; totalized** | §V214.5's priority, exact-ack I2, and I3-absorption make the partition exhaustive and disjoint; the marker fields are supervisor bookkeeping in a watchdog-unreachable namespace; `ACK_PENDING` still creates no evidence and no terminal; the watchdog still holds no lock/capability, writes no `runtime/`, appends no ledger, settles nothing |
| **D1** no idle exit | **not reopened; last unbounded construction removed** | §V214.1 leaves no blocking syscall in the bootstrap, so no participant can retain the shared lock without an evaluable deadline; no supervisor waits on `SPAWN.lock` |
| **K1** mediated transport, fixed ceilings, no replenishment | **not reopened; a release route restored** | five constants unmoved; write-once/hash-once counts identical; §V214.2 restores the custody-absence release for orphan-manifest quarantines **without** weakening `bytes_reserved`, which remains the accounted contribution in all three branches until a verified disposition |
| Signed generic-harness composite (v2/v2.1/v2.2/v2.3/v2.3.1) | **unchanged** | referenced only; §D1 head/cache and §J1–§J3 untouched; §W6.5 remains the only named protocol supersession |
| Signed batch-settlement amendment (v1/v1.1/v1.1.1) | **unchanged** | all-live invalid route, `ARCHIVE` before `RESOLVED`, arithmetic, inline `meter_evidence`, two-token order referenced unaltered; §V214.3's `HEARTBEAT` predicate uses the batch archival commit without weakening it |
| Nine signed events | **unchanged** | none added, none moved; no new valid terminal is reachable from a swap, freeze, quarantine, or failed output |
| E1/E2/E3 constants and arithmetic | **unchanged** | no value moved; charging remains the cursor difference; the actual interval is never clipped |
| Roots, runtime schemas, T bands, stream ownership, `MAX_CONCURRENT_LEASES` | **unchanged** | two key-set extensions only; no new object or path |
| Import allowlist and frozen files | **zero delta** | only `os`/`time`/`hashlib`/`json` primitives; `select`/`selectors`/`signal`/`ctypes`/`sys` remain outside; the five byte-frozen modules untouched |
| Q/C and scientific boundary | **unchanged** | every object and residual remains `scientific_outcome: false`, recursively scientific-field-rejecting, T-development-only, archival-excluded, untracked, permanently non-citable |
| Archival exclusions / clean-HEAD | **unchanged** | no signed §B set changes; no configuration change authorized |

**No-weakening check.** Every repair is neutral or strictly stronger: §V214.1
makes existing bounds executable; §V214.2 restores a route that was unreachable
while changing no accounting rule; §V214.3 preserves an authority that was being
destroyed; §V214.4 removes a contradictory order; §V214.5 removes two gaps and
one ambiguity; §V214.6 removes an over-claim; §V214.7 corrects a count. No
fail-closed behavior is weakened, no watchdog or replacement fact is promoted to
a second runtime authority, and no A3/B1/C1/D1/K1 cell is reopened.

---

## 10. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this closure or by the correction.** No code, test,
commit, host change, process, signature, activation, entropy, T/Q/C work, or
scientific execution is permitted. Obligations become due only after both
independent v2.1.4 confirmations accept the bytes **and** the author signs the
amendment token.

Implementation obligations, in verification order: (1) four `O_NONBLOCK`
channels with `PC_PIPE_BUF` verification, the two bounded helpers, and the
per-step stage-route mapping; (2) `QUARANTINE.json`'s manifest binding, the
record-first reducer's Q1–Q4, and the three exclusive verifier branches; (3) the
GC order `committed → reply → ack → accepted` with the `D6` finalization rule
and the nine per-command G3 bindings; (4) `c1a` acquire → `c1b` preflight →
`c2`, with a non-mutating stuck-holder route; (5) the pinned I1→I7 priority,
exact-current-table I2, I3-absorption, and the three-step partition; (6) the
corrected A3 statement with four residuals and no route; (7) the 43-byte
timestamp line.

Test obligations: §W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–96, §U11 rows
97–120 (with rows 101, 105, 112, 113, 117 **replaced**), and §V214.10 rows
121–144, which include at least one test per Critical, Major, and Minor of both
v2.1.3 reviews. Disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and no capability, world, learner,
entropy, capacity artifact, custody disposition, result manifest, or scientific
object.

---

## 11. Bounded final-confirmation questions

Each reviewer must **recompute the SHA-256 of the v2.1.4 bytes** and confirm it
equals
`cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62`, then read
those bytes with v2, v2.1, v2.1.1, v2.1.2, v2.1.3, both author signatures, and
their own v2.1.3 review. **Do not trust this closure**: it is authored
self-assessment, not evidence, and every disposition must be re-derived from the
correction's own text. The earlier X-line confirmation applied to the v2.1.3
bytes only and does not carry over.

### 11.1 X-line — independent clean-context Claude Opus 4.8

> Having recomputed and verified the SHA-256 of
> `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md`
> as `cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62`, and
> reading only those bytes, the unedited v2/v2.1/v2.1.1/v2.1.2/v2.1.3
> documents, the two author signatures, and your own v2.1.3 review — treating
> `reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md` as an
> untrusted authored self-assessment:
>
> **Are X213-m1 and X213-m2 closed, is every v2.1.3 closure you confirmed
> carried forward unmodified, and does v2.1.4 introduce no new Critical or
> Major defect, weaken no fail-closed behavior, promote no watchdog or
> replacement fact to a second runtime authority, and reopen no author cell
> (A3, B1, C1, D1, K1) — yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_4`. Then, per finding, state closed / not
> closed with the exact clause you relied on. Give particular adversarial
> attention to: whether any blocking syscall survives anywhere in the bootstrap
> and whether every stage read and write has exactly one continuation for
> `EAGAIN`, `EINTR`, EOF, malformed, overlong, trailing, `EPIPE`, and other
> errno; whether the descriptor ownership table's EOF claims are each supported
> by a sole-writer argument; whether the `m7`→`m8` middle-child death now
> terminates and releases the lock; whether the three verifier branches are
> exclusive and whether any combination of durable objects escapes them;
> whether the GC order leaves any cut at which the applicable G3 predicate is
> unidentifiable from the files then present, and whether deleting `ack.json`
> before `accepted.json` can lose an owed reply; whether the I1→I7 priority and
> the three-step partition are exhaustive and disjoint over your own
> constructed races; and whether any promoted-byte hash claim survives anywhere
> in the chain. Do not run code, tests, probes, or any Officina process; edit
> nothing.

### 11.2 Y-line — independent clean-context GPT-5.6 Sol

> Having recomputed and verified the SHA-256 of the v2.1.4 correction as
> `cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62`, and
> reading only those bytes, the unedited v2/v2.1/v2.1.1/v2.1.2/v2.1.3
> documents, the two author signatures, and your own v2.1.3 review — treating
> the author's closure as an untrusted self-assessment:
>
> **Are all of your C1, C2, M1, M2, M3, M4, and m1 closed by exact, executable
> text; is every independently closed earlier repair carried forward
> unmodified; and is every lifecycle, invalidity, scientific, and resource
> field still free of implementer discretion, hidden author judgment, and new
> author cells — yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_4`. Then re-run your eight traces — A3/K1
> write-hash and residual windows, spawn/bootstrap cuts, the C1 replacement
> state machine, B1/GC across all eight commands, result manifest and complete
> K1 custody, spawn-record lifecycle, author authority and proof summary, and
> no-regression/exactness — against the v2.1.4 text, and state per row whether
> the required result is now achieved. Give particular adversarial attention
> to: whether your c13 deadlock is genuinely removed at every ordering of
> middle-child and grandchild death, and whether any new pipe cycle can retain
> `SPAWN.lock`; whether an orphan-manifest quarantine can now be disposed and
> whether the new binding can be forged, replayed, or satisfied while a
> manifest is absent or unbound; whether the GC finalization rule can delete
> `accepted.json` while any semantic phase or owed reply survives; whether the
> lock-first order leaves any mutating read outside the lock, including in the
> stuck-holder route; whether the invalid-condition priority, the exact-table
> I2, and the I3 absorption leave any state with zero or two continuations; and
> whether any text still claims the sole hash describes the promoted bytes. Do
> not run code, tests, probes, or any Officina process; edit nothing.

Neither confirmation authorizes implementation. The author token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes eligible only
if **both** independent confirmations explicitly accept the corrected v2.1.4
bytes, and signing it remains the author's act alone.

---

## 12. Custody and negative-space confirmation

**Exactly two new files were created:**

```text
successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md
```

No existing file was altered. v2, v2.1, v2.1.1, v2.1.2, v2.1.3, both author
signatures, the authorship note, all eight prior independent reviews, the
harness-contract chain, the batch-settlement amendment chain, the
frozen/inactive implementation, its tests, and every pre-existing dirty or
untracked working-tree file are preserved byte-unmodified. Nothing was
committed or staged. No specification, signature, or review was rewritten or
reinterpreted; every change is a named replacement in §V214.0.

I created no code, process, supervisor, controller, worker, watchdog, bootstrap
adapter, middle child, endpoint, pipe, FIFO, journal instance, tombstone, spawn
record, spawn intent, lease, capability, operation, output bound, framed
transport, result manifest, quarantine record, promoted object, capacity
artifact, custody disposition, author decision file, freeze witness, fallback
witness, replacement-freeze record, entropy, T activation, scientific datum, Q
attempt, Q/C artifact, candidate, learner, world, E1/E2/E3 spend, or outcome. I
started no process, ran no test, executed no probe or smoke command, and issued
no Officina command. The only computation performed was measuring the length of
a literal timestamp line and re-adding the eight documented decision-file line
lengths in a scratch directory outside the repository; every illustrative value
in the correction is patterned synthetic content that cannot correspond to any
real generation, operation, or activation record, and no file was written from
any of them. I authorized no implementation and no signature token, and I
predicted no qualification and no C1–C6 outcome. Process invalidity, resource
exhaustion, and missing evidence remain infrastructure facts and are nowhere
treated as scientific evidence.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent; no runtime, scientific,
capacity, disposition, result-manifest, entropy, or outcome artifact exists.
**T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.**
