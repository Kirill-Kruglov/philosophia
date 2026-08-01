# Officina supervisor and control-channel amendment — v2.1.6 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1 through
v2.1.5. It is **not** an independent X-line or Y-line review of its own bytes
and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain is an untrusted self-assessment; none of their claims is
used as evidence here.

**Review state of v2.1.5, recorded exactly.** The independent Y line returned
`REVISE_OFFICINA_SUPERVISOR_V2_1_5` with C1, M1, M2, M3, and m1. **That verdict
governs.** The X line **produced no formal review of v2.1.5**: the saved chat
trace
(`reviews/opus_officina_supervisor_control_channel_v2_1_5_final_confirmation_chat_response.md`,
`f4a4f1d6…`) stopped at the sentence "Let me mark the chapter and write the
deliverable" and the review file was never created. **There is therefore no
X verdict for v2.1.5** — not a confirmation and not a revision — and the
in-progress opinions recorded in that trace (including its provisional view
that the disposition selector "holds", which Sol C1 refutes) are **not review
evidence** and are not relied on anywhere in this document. v2.1.6 consequently
requires a **fresh X-line and a fresh Y-line review**; no earlier confirmation
of any version carries across.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md`
(v2.1.5), which layers over v2.1.4, v2.1.3, v2.1.2, v2.1.1, v2.1, and v2 — all
seven preserved unedited as review evidence. **Everything not named in the
§V216.0 replacement index carries forward verbatim.**

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged** — every v2.1.5 repair not
implicated by the five Y findings, and every earlier independently confirmed
closure: the `B-P`/`B-QM`/`B-QN` branch **bodies** and §V214.2.4's
custody/retention/accounting reconciliation; the ordered `c3` construction with
per-step ownership bookkeeping and the `c4`/`m7` fork routes
(§V215.2.3, §V215.2.5, §V215.2.6); the `REFUSAL_SEQUENCE` step order
(§V215.2.4); the anti-wedge policy statement and its expiry/non-citability
route (§V215.3); the seven-row provenance map (§V215.4); the nonblocking
channel flags and the two bounded helpers (§V214.1.1's flags, §V214.1.3,
§V214.1.4); the quarantine manifest binding and record-first reducer
(§V214.2.1, §V214.2.2); the GC order with `accepted.json` last and its `D6`
finalization (§V214.3); the lock-first preflight and non-mutating stuck-holder
route (§V214.4); the total watchdog partition (§V214.5); the four-residual A3
distinction (§V214.6); the 43-byte timestamp example (§V214.7); and the whole
carried §U/§N/§Z/§W/§V2 chain.

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature, review,
prompt, or runtime artifact. Starts no process, endpoint, pipe, FIFO, journal,
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
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md
f4a4f1d693131360c14d0e42919dbddca81effd688840f20f3c1603e6fe48a70  reviews/opus_officina_supervisor_control_channel_v2_1_5_final_confirmation_chat_response.md   (INCOMPLETE — no X verdict)
4bb6961b21bb010745ab5093cf25545a4ea6440dacff238d53cbc089fda13625  reviews/opus_officina_supervisor_control_channel_v2_1_4_final_confirmation.md
0e20212d7258b4462a23a67750fa886aca8a82a4f5a0cb62f55205f5b8ef7310  reviews/sol_officina_supervisor_control_channel_v2_1_4_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

## Engineering constants

**Zero new constants, objects, paths, schemas, schema keys, wire enum tokens,
refusal or `INVALID` tokens, public commands, signed events, resource values,
roots, or archival-set changes. Zero import-allowlist delta.** The four
`CLOSE_OWNED` outcome names of §V216.2 are **internal control-plane outcome
labels**: they are never transmitted, never persisted, never members of any
schema enum, and never appear in a reply. This layer uses only `os.close`,
`os.stat`, `os.listdir`, `os.kill`, `os.waitpid`, `os.unlink`, `os.fsync`,
`os._exit`, `os.getpid`, `hashlib`, and `json` — all inside allowlisted
modules; `select`, `selectors`, `signal`, `ctypes`, and `sys` remain outside.

---

## V216.0. Exact replacement index (v2.1.5 → v2.1.6)

**Nothing else moves.** Everything in v2.1.5 and in every layer it carries —
in particular §V215.1.2's three branch **bodies** by reference, §V215.2.3,
§V215.2.4's step order, §V215.2.5, §V215.2.6, §V215.3, §V215.4, §V215.5,
§V215.8, and the entire carried §V214/§U/§N/§Z/§W/§V2 chain — carries forward
verbatim except at the rows below.

| v2.1.5 (or carried) locus (exact sentence / clause / table row) | Action in v2.1.6 |
|---|---|
| §V215.1.1's definitions of `S`, `Q`, `F` and of `MALFORMED`, and the paragraph "…`S`, `Q`, and `F` are **presence-and-validity** predicates: a present-but-malformed object makes its predicate **false**…" | **replaced** by §V216.1.1 (separate physical-presence `PS`/`PQ`/`PF` and valid-decoded `VS`/`VQ`/`VF`; `MALFORMED` computed over every physically present canonical object) |
| §V215.1.2's five-row selector table (rows 1–5, using `S`/`Q`) | **replaced** by §V216.1.2 (six rules; Rule 0 `MALFORMED` dominates; every releasing rule requires `¬MALFORMED` and physical absence of the opposite terminal) |
| §V215.1.3's sub-rule `5a` ("`MALFORMED` ⇒ record-first invalidity…") | **promoted** to §V216.1.2's dominant Rule 0 and **deleted** from the row-5 sub-routing |
| §V215.1.3's sub-rules `5b`–`5h` and their fourteen-row truth table | **replaced** by §V216.1.3 (restated over `PS`/`PQ`/`PF`; the full cross-product, including every malformed counterexample) |
| §V215.2.1's `BOOTSTRAP_FD_CLEANUP` body, and its sentence "The `SPAWN.lock` descriptor is **not** a bootstrap channel end and is never closed by this routine; it is released by its own pinned step or by process exit." | **replaced** by §V216.2.1–§V216.2.2 (one `CLOSE_OWNED` primitive used everywhere including the lock; the cleanup routine becomes a fixed-order loop over it) |
| §V215.2.2's sentence "every close is either a pinned normal step or a pinned cleanup invocation" and its "Normal close" column semantics | **replaced** by §V216.2.3 (every named close site invokes `CLOSE_OWNED`, with its `CLOSED_ERROR` continuation pinned) |
| §V215.2.2's `rel3_r` row cell "middle ⇒ cleanup (this is what makes `c13` see EOF at `m7` failure)" | **replaced** by §V216.5.1 (the annotation moves to the `boot_w` row; the `rel3_r` row becomes ownership cleanup only) |
| §V215.2.7's table row "`c5`–`c7` failure (identity read, record install) \| CLI's four remaining ends closed \| all four removed \| released \| middle is at `m0`; its bound or EOF exits it" | **replaced** by §V216.3.2–§V216.3.4 (three individual routes with kill and death proof before any record removal; the false EOF claim and the false "released" claim are **deleted**) |
| §V215.2.4's invocation list, clause "`c1b` preflight refusals, every `c3` construction cut, the `c4` first-fork failure" | **extended** by §V216.3.1 (adds the `c5`, `c6`, `c7` routes explicitly, each with a stage and a kill authority) |
| carried v2.1.4 §V214.1.1 sentence "Both ends of all four are `O_NONBLOCK`, so **no blocking syscall exists anywhere in the bootstrap** and every gate, report, and release can evaluate its deadline." | **replaced** by §V216.4.1 (the narrower true invariant) |
| carried v2.1.4 §V214.1.5 sentence "**Invariants restated and now executable.** No blocking syscall exists in the bootstrap, so every deadline is evaluable at every instruction." | **replaced** by §V216.4.1 (same narrowing; the remainder of that paragraph is unchanged) |
| carried v2.1.4 §V214.10 test row **121** | **replaced** by §V216.4.2 |
| carried v2.1.4 §V214.10 test row **126** | **replaced** by §V216.4.2 |
| §V215.7's sentence "§V214.10 rows 121–144 carry forward unchanged" | **replaced** by §V216.4.3 (rows 121 and 126 are replaced; 122–125 and 127–144 carry forward) |
| §V215.7 test rows 150, 154, 157 | **replaced** by §V216.6 (restated over `CLOSE_OWNED`; row 154's EOF attribution named to `boot_w`) |
| §V215.6 crash-cut matrix | **extended** by §V216.7 (twenty-two added rows) |
| §V215.7 test-obligation rows 145–164 | **extended** by §V216.6 (rows 165–184) |

---

## V216.1. Physical presence dominates validated terminal state (R1)

Closes Sol C1. The three branch **bodies** (`B-P`'s `P1`–`P5`, `B-QM`'s
`QM1`–`QM6`, `B-QN`'s `QN1`–`QN4`), §V214.2.4's custody/retention/accounting
reconciliation, the no-content-reread rule, the complete-custody P1–P7 proof,
and every §N1.5 conjunct are **unchanged**. Only the selector changes.

### V216.1.1 Physical presence, validity, and `MALFORMED`

All observations are taken in **one held `T_RUNTIME.lock` epoch**, from one
directory-fd enumeration of `operations/<operation_id>/` plus one
`follow_symlinks=False` `stat` per canonical name, with `O_NOFOLLOW`
throughout and **no output content file opened**.

```text
PS ≜ operations/<op>/SETTLEMENT.json is PHYSICALLY PRESENT at its canonical
     name: os.stat(name, dir_fd=op_fd, follow_symlinks=False) does not raise
     ENOENT, AND the name appears in the same epoch's directory-fd enumeration.
     Presence is decided WITHOUT decoding: any file type, any link count, any
     content, any size — a symlink, a directory, a zero-byte file, or a
     truncated file is PRESENT.
PQ ≜ the same test for QUARANTINE.json
PF ≜ the same test for RESULT_MANIFEST.json

VS ≜ PS ∧ the object is a regular file ∧ st_nlink == 1 ∧ it resolved with no
     symlink component ∧ its exact bytes decode as canonical ASCII JSON that
     validates against t-operation-settlement.v1 exactly (key set, types, hex
     grammars, enum tokens, scientific_outcome false, recursive
     scientific-field rejection)
VQ ≜ the same for t-operation-quarantine.v1
VF ≜ the same for t-operation-result-manifest.v1

MALFORMED ≜ (PS ∧ ¬VS) ∨ (PQ ∧ ¬VQ) ∨ (PF ∧ ¬VF)
```

`MALFORMED` is computed from **every** physically present canonical object
**before any releasing predicate is eligible**. v2.1.5's `S`/`Q`/`F` conflated
presence with validity, so `¬Q` and `¬S` meant "absent **or malformed**" — the
exact defect Sol C1 identified. The binding and hash predicates are unchanged
in content and are now stated over the validated forms:

```text
B  ≜ VQ ∧ QUARANTINE.json's result_manifest_sha256_or_null ≠ null
HS ≜ VS ∧ VF ∧ SHA-256(the manifest file's exact canonical bytes)
          == SETTLEMENT.json's result_manifest_sha256
HQ ≜ B  ∧ VF ∧ SHA-256(the manifest file's exact canonical bytes)
          == QUARANTINE.json's result_manifest_sha256_or_null
```

A partially written object cannot appear at a canonical name (every install is
`same-directory temp → file fsync → atomic no-replace rename → parent-directory
fsync`); a surviving `.tmp` is not at a canonical name, so it changes no
predicate above and is caught as custody by the §N2.2 L4 temp-grammar class.
Any additional `operation_id`-bearing entry is caught by the L5 unknown-name
scan. Both remain §N2.3 P5/P6 custody refusals.

### V216.1.2 The total selector, with `MALFORMED` as the first effective rule

```text
Rule 0  MALFORMED
        ⇒ record-first invalidity naming EVERY physically present malformed
          canonical path; release nothing; NO branch is entered
Rule 1  ¬MALFORMED ∧ PS ∧ PQ
        ⇒ record-first invalidity naming both terminal paths; release nothing;
          no branch entered
Rule 2  ¬MALFORMED ∧ PS ∧ ¬PQ ∧ PF ∧ HS          ⇒ B-P only
Rule 3  ¬MALFORMED ∧ ¬PS ∧ PQ ∧ B ∧ PF ∧ HQ      ⇒ B-QM only
Rule 4  ¬MALFORMED ∧ ¬PS ∧ PQ ∧ ¬B ∧ ¬PF         ⇒ B-QN only
Rule 5  ¬MALFORMED ∧ none of Rules 1–4           ⇒ the §V216.1.3 sub-routing
```

Three properties, each required:

1. **`MALFORMED` dominates.** Rule 0 is the first effective rule and every
   other rule carries `¬MALFORMED` as an explicit conjunct, so no malformed
   canonical object can ever coexist with a branch entry. Rules 0 and 1 have
   the **same continuation class** — record-first invalidity, release nothing —
   differing only in which paths the record names, so their relative order can
   change no outcome; Rule 0 is nevertheless stated first so the naming is
   deterministic when both conditions hold.
2. **Both-terminal presence is physical.** Rule 1 tests `PS ∧ PQ`, not
   `VS ∧ VQ`, so a both-terminal layout is caught even when one of the two is
   unreadable.
3. **Every releasing rule requires physical absence of the opposite
   terminal.** Rule 2 requires `¬PQ`; Rules 3 and 4 require `¬PS`. Combined
   with `¬MALFORMED`, this makes the malformed-opposite-terminal release
   impossible by **two independent conjuncts**.

Under `¬MALFORMED`, every physically present canonical object is valid, so
`PS ⟺ VS`, `PQ ⟺ VQ`, and `PF ⟺ VF` throughout Rules 1–5. The sub-routing of
§V216.1.3 is therefore the v2.1.5 sub-routing restated over the physical
predicates, with no change of meaning in the well-formed sub-space.

### V216.1.3 Row 5 sub-routing and the complete cross-product

```text
5b  ¬PS ∧ ¬PQ ∧ ¬PF               ⇒ REFUSE (retryable = false): no terminal
                                    exists yet — an ordinary non-terminal
                                    operation, not a defect
5c  ¬PS ∧ ¬PQ ∧ PF                ⇒ record-first invalidity: after the
                                    §V214.2.2 record-first reducer, which runs
                                    under the lock before any frame is served,
                                    a manifest without a terminal cannot exist
5d  PS ∧ ¬PQ ∧ ¬PF                ⇒ record-first invalidity: the manifest is
                                    never removed, so a settlement whose
                                    binding names an absent manifest is an
                                    impossible layout
5e  PS ∧ ¬PQ ∧ PF ∧ ¬HS           ⇒ REFUSE (retryable = false): hash mismatch
5f  ¬PS ∧ PQ ∧ B ∧ ¬PF            ⇒ record-first invalidity: binding without
                                    file
5g  ¬PS ∧ PQ ∧ B ∧ PF ∧ ¬HQ       ⇒ REFUSE (retryable = false): hash mismatch
5h  ¬PS ∧ PQ ∧ ¬B ∧ PF            ⇒ record-first invalidity: orphan file
                                    without binding (the state §V214.2.2 Q3
                                    already names)
```

**Exhaustiveness and disjointness of Rules 1–5 under `¬MALFORMED`**, by the
decision tree on `(PS, PQ)`:

```text
PS ∧ PQ                  → Rule 1
PS ∧ ¬PQ  : ¬PF          → 5d
             PF ∧ HS     → Rule 2
             PF ∧ ¬HS    → 5e
¬PS ∧ PQ  : B ∧ ¬PF      → 5f
             B ∧ PF ∧ HQ → Rule 3
             B ∧ PF ∧ ¬HQ→ 5g
             ¬B ∧ ¬PF    → Rule 4
             ¬B ∧ PF     → 5h
¬PS ∧ ¬PQ : ¬PF          → 5b
             PF          → 5c
```

Every leaf is reached by exactly one path, and the four `(PS, PQ)` quadrants
partition the space, so each state satisfies **exactly one** rule.

**Complete cross-product truth table.** Columns: physical presence
`PS`/`PQ`/`PF`; whether any present object is malformed; the binding; the hash.
`—` means the column is not free in that row.

| # | `PS` | `PQ` | `PF` | malformed | `B` | hash | Rule | Single continuation |
|---|---|---|---|---|---|---|---|---|
| **1** | any | any | any | **yes** | any | any | **0** | **record-first invalidity naming every malformed path; no branch; release nothing** |
| 2 | 1 | 1 | any | no | any | any | 1 | record-first invalidity (both terminals); release nothing |
| 3 | 1 | 0 | 1 | no | — | `HS` | 2 | `B-P` only; on full success release exactly `bytes_reserved` |
| 4 | 1 | 0 | 1 | no | — | ¬`HS` | 5e | REFUSE; release nothing |
| 5 | 1 | 0 | 0 | no | — | — | 5d | record-first invalidity; release nothing |
| 6 | 0 | 1 | 1 | no | 1 | `HQ` | 3 | `B-QM` only; on full success release exactly `bytes_reserved` |
| 7 | 0 | 1 | 1 | no | 1 | ¬`HQ` | 5g | REFUSE; release nothing |
| 8 | 0 | 1 | 0 | no | 1 | — | 5f | record-first invalidity; release nothing |
| 9 | 0 | 1 | 0 | no | 0 | — | 4 | `B-QN` only; on full success release exactly `bytes_reserved` |
| 10 | 0 | 1 | 1 | no | 0 | — | 5h | record-first invalidity; release nothing |
| 11 | 0 | 0 | 0 | no | — | — | 5b | REFUSE (no terminal yet); release nothing |
| 12 | 0 | 0 | 1 | no | — | — | 5c | record-first invalidity; release nothing |
| 13 | any | any | any | no | any | any | — | a canonical `.tmp` changes no predicate; it is L4 custody ⇒ §N2.3 P5 refuses; release nothing |
| 14 | any | any | any | no | any | any | — | an extra `operation_id`-bearing entry changes no predicate; it is L5 custody ⇒ §N2.3 P6 refuses; release nothing |

### V216.1.4 The five Sol C1 counterexamples, re-run

| Sol counterexample | v2.1.5 outcome | v2.1.6 outcome |
|---|---|---|
| valid settlement + **malformed quarantine** + valid matching manifest | row 2 true (`Q=0` because malformed) ⇒ `B-P` could **release** | `PQ = 1` and `MALFORMED` ⇒ **Rule 0**; Rule 2 is also false by its `¬PQ` conjunct ⇒ **blocked twice**; release nothing |
| **malformed settlement** + valid non-null quarantine + valid matching manifest | row 3 true ⇒ `B-QM` could **release** | `PS = 1` and `MALFORMED` ⇒ **Rule 0**; Rule 3 is also false by its `¬PS` conjunct ⇒ release nothing |
| **malformed settlement** + valid null quarantine + manifest absent | row 4 true ⇒ `B-QN` could **release** | `PS = 1` and `MALFORMED` ⇒ **Rule 0**; Rule 4 is also false by `¬PS` ⇒ release nothing |
| valid settlement + valid quarantine + **malformed manifest** | outer row 1 and truth-table row 12 named **two differently named** invalidity routes | `MALFORMED` ⇒ **Rule 0** alone fires and names the malformed manifest path; Rule 1 carries `¬MALFORMED` and is false. Exactly one rule, one record, one continuation |
| valid settlement + **malformed quarantine** + valid **mismatching** manifest | row 2 false, outer row 5 ⇒ 5e REFUSE (release depended on hash coincidence) | `MALFORMED` ⇒ **Rule 0** regardless of the hash; malformed dominance no longer depends on any hash outcome |

In all five, and in every row of §V216.1.3, **nothing is released**. Rows 3, 6,
and 9 of the truth table remain the only releasing rows, and each still
releases exactly `bytes_reserved` exactly once, only after its unchanged branch
body **and** §N2.3's P1–P7 complete-absence proof **and** every §N1.5 conjunct
succeed in the same lock epoch. K1 accounting is unchanged: `bytes_reserved`
remains the accounted contribution in every non-releasing row.

---

## V216.2. One close transition everywhere (R2)

Closes Sol M1.

### V216.2.1 The `CLOSE_OWNED` primitive

Exactly one single-fd transition, stated once and used at **every** normal,
cleanup, and lock close site. `owned(owner)` is the invoking process's
in-memory ownership set.

```text
CLOSE_OWNED(owner, fd, context) → one of {CLOSED, CLOSED_ABSENT,
                                          CLOSED_ERROR, NOT_OWNED}

  0. if fd ∉ owned(owner):
        perform NO syscall; return NOT_OWNED; continue the caller's flow.
        This is what makes a second call unable to close a REUSED number: the
        number is no longer owned, so no close is attempted.
  1. attempt os.close(fd)
  2. classify the outcome exactly:
        success                       ⇒ CLOSED
        OSError, errno EBADF          ⇒ CLOSED_ABSENT
            (no open description existed at that number at the instant of the
             call; NOTHING was closed, so nothing can have been closed wrongly)
        OSError, errno EINTR          ⇒ CLOSED_ERROR
            (on the pinned Linux target the descriptor is RELEASED before EINTR
             is reported; CPython does not retry close() for exactly this
             reason)
        OSError, any other errno      ⇒ CLOSED_ERROR
            (e.g. EIO from a deferred flush; Linux has released the descriptor
             regardless)
  3. OWNERSHIP REMOVAL — unconditional, exactly once, for EVERY outcome of
     step 2, and BEFORE step 4:
        owned(owner) := owned(owner) \ {fd}
  4. THE NUMBER IS NEVER USED AGAIN by this owner: never retried, never
     re-closed, never passed to a later cleanup, never compared. The kernel may
     have reassigned it to an unrelated open description.
  5. context routing, strictly after step 3:
        CLOSED         ⇒ continue the caller's normal flow
        CLOSED_ABSENT  ⇒ continue the caller's normal flow
        CLOSED_ERROR   ⇒ the context's pinned continuation from §V216.2.3
        NOT_OWNED      ⇒ continue the caller's normal flow
```

**Diagnostics.** If an implementation records an outcome, the record is a
**closed control-plane fact** — one of the four outcome labels plus the errno
integer — that may never enter selection, Q, C, C1–C6, custody, capacity, an
author decision, an invalidity cause, or any scientific or resource
interpretation, and may never alter routing beyond §V216.2.3's table. The four
labels are internal: never transmitted, never persisted in any schema, never
members of any enum.

**Forked copies are distinct ownership.** After `os.fork` each process has its
**own** `owned` set, initialized as a copy of the parent's at the fork instant.
`CLOSE_OWNED` acts only on the invoking process's set; a close in one process
never removes ownership in another. The same fd number held by two processes is
two distinct ownerships, closed independently, and a pipe end is released to
the kernel only when the **last** owner closes it.

**Restart behavior.** `owned` is in-memory only and does not survive a process
crash; a crash releases that process's descriptors by kernel action. **No
non-crash route may rely on that**: every non-crash path closes through
`CLOSE_OWNED`. No exception, destructor, garbage collector, finalizer, caller
exit, or unspoken POSIX convention owns any close transition; an exception
propagating out of a close site is a **contract violation, not a route**.

### V216.2.2 The multi-fd cleanup is only a loop over the primitive

```text
BOOTSTRAP_FD_CLEANUP(owner):
    for fd in the fixed order
          [boot_r, boot_w, rel1_r, rel1_w, rel2_r, rel2_w, rel3_r, rel3_w]:
        CLOSE_OWNED(owner, fd, context = "cleanup")
    # postcondition: owned(owner) contains no bootstrap end
```

No separate close semantics survive anywhere: v2.1.5's inline errno handling
inside the routine is **deleted** and replaced by these eight calls. Its
exclusion of `SPAWN.lock` is also deleted — the lock is closed by
`CLOSE_OWNED(owner, spawn_lock_fd, context = "lock-release")`, with the lock fd
tracked in the same `owned` set.

### V216.2.3 Every close site, by name, with its `CLOSED_ERROR` continuation

**Uniform justification.** On the pinned Linux target the descriptor is
released in **every** outcome except `EBADF` (where nothing was open) and
`NOT_OWNED` (where nothing was attempted). The observable pipe state — the
number of remaining readers and writers, and therefore every EOF and `EPIPE`
consequence — is **identical to the success case** after any `CLOSED_ERROR`.
Consequently the pinned continuation is `CONTINUE` at every site: no site's
correctness depends on the *return value* of a close, only on the release,
which is unconditional. A `CLOSED_ERROR` inside an already-failing refusal path
does not alter that refusal; the refusal proceeds unchanged.

| Site | Owner | Descriptors closed | Outcome routing |
|---|---|---|---|
| `c5` | CLI | `rel1_r`, `rel2_r`, `rel3_r`, `boot_w` (4 calls) | CONTINUE |
| `c8` | CLI | `rel1_w` (after the stage-1 release write) | CONTINUE |
| `c12` | CLI | `rel2_w` (after the stage-2 release write) | CONTINUE |
| `c13` | CLI | `boot_r` (after the bootstrap report read) | CONTINUE |
| `c16` | CLI | `rel3_w` (after the stage-3 release write) | CONTINUE |
| `c18` | CLI | `spawn_lock_fd` | CONTINUE (the attempt has already succeeded; the flock is released in every outcome) |
| `m1` | middle | `rel1_r`, `rel1_w`, `rel2_w`, `rel3_w`, `boot_r` (5 calls) | CONTINUE |
| `m6` | middle | `rel2_r` | CONTINUE |
| `m8` | middle | `boot_w` (after the bootstrap report write) | CONTINUE |
| `g1` | grandchild | `rel3_r`, `boot_w` through `CLOSE_OWNED`; every other inherited descriptor through the already-signed §W2.2/§Z3.5 scrub, applying the same errno classification and never retrying a number | CONTINUE |
| `g3` | grandchild | `spawn_lock_fd` | CONTINUE |
| `BOOTSTRAP_FD_CLEANUP` | any | the eight bootstrap ends, fixed order | CONTINUE per call |
| `REFUSAL_SEQUENCE` step 4 | CLI | `spawn_lock_fd` | CONTINUE; the refusal is returned regardless |
| `STAGE_M_ROUTE` step 6 | CLI | `spawn_lock_fd` | CONTINUE; the refusal is returned regardless |

### V216.2.4 Ownership, errno, fd-reuse, and second-call traces

| Trace | Result |
|---|---|
| normal close, success | `CLOSED`; ownership removed once; flow continues |
| normal close, `EBADF` | `CLOSED_ABSENT`; ownership removed once; **nothing was closed**, so no reused number can have been harmed; flow continues |
| normal close, `EINTR` | `CLOSED_ERROR`; the descriptor **was released**; ownership removed once; **never retried**; flow continues |
| normal close, `EIO` or other | `CLOSED_ERROR`; identical handling |
| second `CLOSE_OWNED` on the same fd | `NOT_OWNED`; **no syscall**; a number reused by an unrelated open description cannot be closed |
| cleanup after a normal close of the same fd | the fd is no longer owned ⇒ `NOT_OWNED` ⇒ no syscall |
| fork, then each process closes "the same" fd | two distinct ownerships; each removal is local; the pipe end is released only when the last owner closes |
| process crash mid-cleanup | the kernel releases that process's remaining descriptors; the in-memory `owned` set is gone; the next attempt starts empty; **no non-crash route relies on this** |
| an implementation that lets a close exception propagate | contract violation, not a route |

---

## V216.3. Kill and prove death before `c5`–`c7` record removal (R3)

Closes Sol M2. §V215.2.4's four-step `REFUSAL_SEQUENCE` is unchanged for the
cuts it already governed; what is added is an exact stage for `c5`, `c6`, and
`c7`, which v2.1.5 grouped into one row with two false claims.

### V216.3.1 Why the two v2.1.5 claims were false

At `m0` the middle child reads `rel1_r`. The writers of `rel1` are the CLI's
`rel1_w` **and the middle child's own inherited `rel1_w` copy**, which it does
not close until `m1` — after the gate. EOF on a pipe requires **every** writer
to be closed. Therefore:

- **EOF at `m0` is impossible in principle** while the middle child is in its
  gate, no matter what the CLI closes. v2.1.5's "its bound or EOF exits it" is
  replaced: at `m0` the middle child exits **by its bound** (or by a kill).
- **The lock is not released** by the CLI's own close while the middle child
  lives: the middle holds a fork-shared reference to the same open file
  description, so the `flock` persists until that reference is also closed —
  at `m1`'s successors or at process exit. v2.1.5's "released" cell is replaced
  by an explicit statement of when the singleton actually becomes free.

### V216.3.2 `STAGE_M_ROUTE` — the post-first-fork, pre-verified-group stage

Used by every failure at `c5`, `c6`, and `c7`. The stage is **stage M**: after
the first fork, before `SPAWNING_GROUP.json` exists, so `killpg` is **forbidden**
(no verified group exists before `c11`) and only `kill(pid_mid)` is permitted,
exactly as the inherited §U2.5 pre-group discipline requires.

```text
STAGE_M_ROUTE(cut):

 1. IDENTITY — the strongest exact identity available at this instruction:
      in memory, always: pid_mid, the return value of c4's os.fork()
      in memory, if c6 completed: start_identity(pid_mid) from
                                  /proc/<pid_mid>/stat
      durable, if c7 completed:  SPAWNING_MIDDLE.json's middle_child_pid and
                                  middle_child_start_identity
 2. KILL, only if identity-safe:
      2a. read /proc/<pid_mid>/stat.
      2b. ABSENT ⇒ the process is already gone; record "death proved by
          absence" and go to step 4.
      2c. PRESENT and a start identity was already captured (c6 or c7
          completed) and it MATCHES ⇒ identity-safe.
      2d. PRESENT and no start identity was captured yet (failure at c5, or at
          c6 before the read completed) ⇒ capture it now, and additionally
          require the stat's ppid field to equal os.getpid() — the CLI is the
          middle child's parent until it exits — ⇒ identity-safe.
      2e. PRESENT and a previously captured start identity MISMATCHES ⇒ PID
          reuse: the recorded process is gone and this is an unrelated
          process. Do NOT kill. Go to the FAIL-CLOSED CONTINUATION.
      2f. identity-safe ⇒ os.kill(pid_mid, SIGTERM), then os.kill(pid_mid,
          SIGKILL). NEVER killpg at this stage.
 3. PROVE DEATH under the signed identity rules: /proc/<pid_mid>/stat absent,
    or present in state Z with a matching start identity; then
    os.waitpid(pid_mid, WNOHANG) to reap the own child. Poll at
    T_SUPERVISOR_POLL_INTERVAL_NS, bounded by
    T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS. On expiry ⇒ FAIL-CLOSED CONTINUATION.
 4. FDs: BOOTSTRAP_FD_CLEANUP(CLI)                              (§V216.2.2)
 5. RECORDS: remove ONLY records belonging to THIS attempt — matched by
    spawning_id — under the inherited P1/P2/P3 discipline, in the §U6.3 order
    SPAWNING_CHILD → SPAWNING_GROUP → SPAWNING_MIDDLE → SPAWNING, each unlink
    followed by fsync(T_SUPERVISOR/), ENOENT tolerated, WHILE STILL HOLDING
    SPAWN.lock. A record whose spawning_id differs is NEVER unlinked here.
 6. LOCK + REFUSE: CLOSE_OWNED(CLI, spawn_lock_fd, "lock-release"); return
    REFUSED / BOOTSTRAP.
    Because step 3 proved the middle child dead, no fork-shared reference to
    the lock survives, so the singleton is free when the CLI's reference
    closes.

 FAIL-CLOSED CONTINUATION (2e PID reuse, or step 3's bound expired):
    F1. remove NO singleton record: any of them may name a live process, and
        §U6.3's death-proved-only boundary forbids unlinking it.
    F2. BOOTSTRAP_FD_CLEANUP(CLI)
    F3. CLOSE_OWNED(CLI, spawn_lock_fd, "lock-release")
    F4. return REFUSED / BOOTSTRAP (retryable = false)
    F5. STATED HONESTLY: the CLI's own lock reference is released at F3, but
        if the middle child is still live it retains its fork-shared reference,
        so the SINGLETON is not free until that child exits — at the latest
        when its own m0/m5 bound expires (≤ T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS).
        The surviving records are then governed by the inherited §U6.1 P0–P3
        preflight and the §U2.5 stuck-holder route s1–s5 at the NEXT attempt,
        which are the only paths permitted to act on a record whose process is
        live or aged.
```

### V216.3.3 The three cuts, individually

| Cut | What failed | Identity available | Kill authority | Records installed by this attempt | Continuation |
|---|---|---|---|---|---|
| **`c5`** | one of the four `CLOSE_OWNED` calls — **note**: by §V216.2.3 every outcome is `CONTINUE`, so `c5` has **no** close-derived failure route; this row governs an abandonment at `c5` for any other reason | `pid_mid` in memory only | `kill(pid_mid)` after 2d's ppid + freshly captured start identity | `SPAWNING.json` only | `STAGE_M_ROUTE` |
| **`c6`** | `/proc/<pid_mid>/stat` unreadable, absent, or its parse fails | `pid_mid` in memory; a start identity only if the read partially succeeded | absent stat ⇒ 2b death by absence, no kill; otherwise 2d | `SPAWNING.json` only | `STAGE_M_ROUTE` |
| **`c7`** | `SPAWNING_MIDDLE.json` install fails (`EEXIST` unresolvable under P1/P2b, `ENOSPC`, `EIO`, or a durability-step error after the temp write) | `pid_mid` **and** `start_identity(pid_mid)` in memory from `c6`; durable only if the rename completed | 2c (captured identity matches) | `SPAWNING.json`, and `SPAWNING_MIDDLE.json` **iff** its atomic rename completed | `STAGE_M_ROUTE`; step 5 removes the middle record **only after** step 3 proved death, which is exactly §U6.3's boundary |

### V216.3.4 Every prefix within `STAGE_M_ROUTE`

| Crash / abandonment prefix | Durable state | Live state | Continuation |
|---|---|---|---|
| before step 2 | this attempt's records survive | middle may be live at `m0` | a CLI crash releases the CLI's fd and lock reference; the middle exits at its own `m0` bound; the next attempt's §U6.1 preflight sees the records and applies P0–P3 (which may only remove a death-proved record) |
| after `SIGTERM`, before death proof | records survive | middle may be dying | no record has been removed; a later holder revalidates identity, never kills a PID-reused process, and proves live/dead before any removal |
| after death proof, before step 4 | records survive | middle dead | next held-lock preflight P3 may remove them; no live unlink is possible |
| between the eight cleanup calls | records survive | middle dead | each `CLOSE_OWNED` removed ownership exactly once; a re-invocation is `NOT_OWNED` throughout |
| after step 4, before the first unlink | records survive | middle dead | step 5's ordered removal resumes |
| after the child unlink, before/after its `fsync` | lower tiers survive | middle dead | `child → group → middle → spawning`, ENOENT-tolerant, resumes |
| after the group unlink | middle + spawning survive | middle dead | same ordered continuation |
| after the middle unlink | spawning survives | middle dead | remove spawning, `fsync` |
| after the spawning unlink, before step 6 | no singleton survives | middle dead | the next holder starts at P0 once the lock is free |
| after step 6 | nothing of this attempt | — | a second invocation starts clean |
| FAIL-CLOSED F1–F4 | **all** records survive | middle possibly live | nothing was unlinked; the singleton becomes free when the middle exits at its bound; the next attempt's preflight and stuck-holder route govern |

No route removes a record while its process may be live, and no route claims
EOF at `m0` or an immediately free lock while the middle child lives.

---

## V216.4. Removal of the contradictory universal bound language (R4)

Closes Sol M3. The two carried universal assertions and two carried test rows
are **replaced**, not merely extended.

### V216.4.1 The accurate narrower invariant

Both carried assertions are replaced by exactly this text:

> Both ends of all four channels are `O_NONBLOCK`, so **no bootstrap pipe read
> or write can block past its bounded helper deadline** (§V214.1.3,
> §V214.1.4), and every gate, report, and release can evaluate its deadline.
> That is the exact and complete claim. The bootstrap also performs `/proc`
> reads, canonical file installs, and file and parent-directory `fsync`s;
> **none of these has an executable duration bound in any signed text**, and
> this contract makes **no claim** about their duration. Consequently no
> statement anywhere asserts that no bootstrap syscall can outlive a deadline,
> or that every healthy launch releases within the grandchild gate bound;
> §V215.3.1's fixed anti-wedge policy is the governing rule for that gate.

The remainder of §V214.1.5's "Invariants restated" paragraph — the pipe-cycle
statement, the cleanup discipline, and the two named §U2.7 A3 residuals —
is unchanged.

### V216.4.2 Search-and-replacement table for every stale assertion

An exhaustive search of the operative chain for `no blocking syscall`,
`healthy bootstrap`, `healthy launch`, and `always releases` yields exactly
these five loci; there are no others.

| # | Locus | Stale text | Action |
|---|---|---|---|
| 1 | v2.1.4 §V214.1.1 | "so **no blocking syscall exists anywhere in the bootstrap**" | **replaced** by §V216.4.1 |
| 2 | v2.1.4 §V214.1.5 | "**Invariants restated and now executable.** No blocking syscall exists in the bootstrap, so every deadline is evaluable at every instruction." | **replaced** by §V216.4.1 |
| 3 | v2.1.4 §V214.10 row **121** | "assert **no blocking syscall** exists in the bootstrap" | **replaced** — new row 121 below |
| 4 | v2.1.4 §V214.10 row **126** | "a healthy bootstrap always releases inside it" | **replaced** — new row 126 below |
| 5 | v2.1.4 §V214.1.1 "Grandchild gate bound" paragraph, "so a healthy bootstrap always releases well inside the bound" | already **replaced** by §V215.0/§V215.3.1; recorded here for completeness, no further action | — |

```text
new row 121 | all four bootstrap pipes are O_NONBLOCK on both ends and
              PC_PIPE_BUF ≥ 4096 is verified per write end; assert that no
              bootstrap PIPE READ OR WRITE can block past its bounded helper
              deadline; assert that no test and no contract sentence asserts a
              duration bound for /proc reads, canonical installs, or fsyncs
              | R1, Sol C1; R4, Sol M3

new row 126 | the grandchild's gate bound is 2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
              and is a fixed anti-wedge POLICY: inject a deliberately slow but
              otherwise valid c14/c15 that exceeds it and assert the
              deterministic refusal — grandchild CLOSE_OWNED cleanup then
              _exit(3), CLI stage 2, whole attempt fails closed, no identity
              installed, no partial supervisor serves — and assert the refusal
              is non-citable: no ledger entry, witness, fallback, capacity,
              custody, manifest, invalidity, or datum is created. Also assert
              the rel3 EOF property still holds because the middle child closed
              rel3-write at m1 | R3; R4, Sol M3
```

### V216.4.3 Rows 121, 126, and 159–162 reconciled

§V215.7's sentence "§V214.10 rows 121–144 carry forward unchanged" is replaced
by: **rows 121 and 126 are replaced as above; rows 122–125 and 127–144 carry
forward unchanged.** The resulting four-row cluster is jointly satisfiable and
non-overlapping in obligation:

| Row | Obligation | Relation to the others |
|---|---|---|
| 121 | the narrow pipe-only non-blocking fact, and the absence of any duration-bound claim | supplies the premise row 159 audits |
| 126 | the deterministic slow-valid refusal **and** its non-citability | the behavioural test; no longer asserts sufficiency |
| 159 | no text anywhere claims the bound is sufficient for every healthy launch | now **satisfiable**, because rows 121 and 126 no longer make that claim |
| 160 | the same slow-valid injection, asserted on identity/serve state | the state complement of 126 |
| 161 | the expiry creates no artifact of any listed class | the artifact complement of 126 |
| 162 | repetition reaches no different class of outcome and adopts no foreign record | the repetition complement of 126 |

No carried sentence re-asserts sufficiency or universal non-blocking, so no two
rows of the test contract are in conflict.

---

## V216.5. Correct EOF provenance and the descriptor annotation audit (R5)

Closes Sol m1.

### V216.5.1 The two corrected cells

| Row | v2.1.5 cell | v2.1.6 cell |
|---|---|---|
| `boot_w` | (no causal annotation) | "middle ⇒ cleanup — **closing the last `boot_w` copy is what makes `c13` observe EOF on `boot_r`**, which is why the `m7` fork-failure route (§V215.2.6) yields an immediate EOF rather than a deadline; grandchild ⇒ cleanup" |
| `rel3_r` | "middle ⇒ cleanup (this is what makes `c13` see EOF at `m7` failure); grandchild ⇒ cleanup" | "middle ⇒ cleanup; grandchild ⇒ cleanup" — **ownership cleanup only, no causal annotation**; closing a read end can never produce EOF on any read |

### V216.5.2 Complete descriptor annotation audit

For each end: what closing the **last** copy of it actually causes, and where.

| End | Kind | Closing the last copy causes | Observed at | Correctly annotated in the chain? |
|---|---|---|---|---|
| `boot_w` | write | **EOF on `boot_r`** | `c9`, `c13` | now annotated here (§V216.5.1); §V215.2.6 already stated it correctly |
| `boot_r` | read | `EPIPE` on a subsequent `boot_w` write | `m4`, `m8` | consistent — §V214.1.5 routes `m4`/`m8` `EPIPE` to `_exit(3)` |
| `rel1_w` | write | **EOF on `rel1_r`** | `m0` | **impossible during `m0`**, because the middle owns its own `rel1_w` copy until `m1` (§V216.3.1); the governing guarantee at `m0` is the bound — already corrected as X213-m2 |
| `rel1_r` | read | `EPIPE` on a subsequent `c8` write | `c8` | consistent — `c8` routes `EPIPE` to stage 1 |
| `rel2_w` | write | **EOF on `rel2_r`** | `m5` | correct in the carried v2.1.4 cut table ("CLI dies `c9`→`c12` ⇒ `m5` EOF, all `rel2` writers closed"), because the middle closed its copy at `m1` |
| `rel2_r` | read | `EPIPE` on a subsequent `c12` write | `c12` | consistent — `c12` routes `EPIPE` to stage 2 |
| `rel3_w` | write | **EOF on `rel3_r`** | `g0` | correct in the carried cut table ("CLI dies `c12`→`c16` ⇒ `g0` EOF, CLI was sole writer"), because the middle closed its copy at `m1` |
| `rel3_r` | read | `EPIPE` on a subsequent `c16` write | `c16` | now annotated correctly: the `rel3_r` row carries **no** EOF claim |

Two further loose attributions are tightened to name the causal end
explicitly, with no behavioural change: §V215.2.7's `m7` row and §V215.7's test
row 154 both attribute the `c13` EOF to the pair `boot_w`/`rel3_r`; both now
name **`boot_w`** as the cause, with `rel3_r` listed only as ownership cleanup.
No other causal annotation in the chain attributes an EOF or `EPIPE` to the
wrong end of a pair.

---

## V216.6. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host
change, process, signature, activation, entropy, T/Q/C work, E1/E2/E3 spend, or
scientific execution is permitted, and no later gate is authorized.
Obligations become due only after both fresh independent v2.1.6 reviews confirm
the bytes **and** the author signs the amendment token.

§W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–96, §U11 rows 97–120,
§V214.10 rows 122–125 and 127–144 (rows 121 and 126 **replaced** by §V216.4.2),
and §V215.7 rows 145–149, 151–153, 155–156, 158–164 carry forward. Replaced:

- **row 150 replaced:** `CLOSE_OWNED` removes ownership exactly once for every
  one of `CLOSED`/`CLOSED_ABSENT`/`CLOSED_ERROR`, performs no syscall on
  `NOT_OWNED`, never retries a number, and never raises;
  `BOOTSTRAP_FD_CLEANUP` is exactly eight calls to it in the fixed order.
- **row 154 replaced:** `m7` fork failure closes `boot_w` and `rel3_r` through
  `CLOSE_OWNED` and `_exit(3)`s; the CLI's `c13` observes **EOF caused by the
  last `boot_w` closing** (not by `rel3_r`, and not a deadline) and completes
  stage 2.
- **row 157 replaced:** every close site named in §V216.2.3 invokes
  `CLOSE_OWNED`; assert that no bootstrap lifecycle transition — including
  every close and the lock release — is owned by an uncaught exception, process
  exit, finalizer, or garbage collector.

Added:

| # | Test | Covers |
|---|---|---|
| 165 | every row of the §V216.1.3 cross-product yields exactly the tabulated continuation; assert no state satisfies two rules | R1, Sol C1 |
| 166 | each of the five §V216.1.4 counterexamples releases nothing; assert `Rule 0` fires and no branch is entered | R1, Sol C1 |
| 167 | presence is decided without decoding: a symlink, a directory, a zero-byte file, and a truncated file at a canonical name each set `P*` true and `V*` false | R1 |
| 168 | `Rule 2` fails on `PQ`, and `Rule 3`/`Rule 4` fail on `PS`, independently of `MALFORMED` — the double block | R1 |
| 169 | the legitimate `B-P`, `B-QM`, and `B-QN` releases still complete end to end after the selector rewrite | R1, K1 |
| 170 | `CLOSE_OWNED` errno matrix: success, `EBADF`, `EINTR`, other errno, and `NOT_OWNED` each give the pinned outcome, ownership effect, and continuation | R2, Sol M1 |
| 171 | a second `CLOSE_OWNED` on a closed fd performs **no syscall**; a number reused by an unrelated description cannot be closed | R2 |
| 172 | forked copies are distinct ownerships: closing in one process does not remove ownership in the other, and the pipe end is released only on the last close | R2 |
| 173 | every site in §V216.2.3 — `c5`, `c8`, `c12`, `c13`, `c16`, `c18`, `m1`, `m6`, `m8`, `g1`, `g3`, cleanup, both refusal sequences — invokes `CLOSE_OWNED`, including both lock closes | R2 |
| 174 | a `CLOSED_ERROR` at any site leaves the observable pipe state identical to success (same reader/writer counts, same EOF/`EPIPE` consequences) | R2 |
| 175 | `c5`, `c6`, and `c7` failures each take `STAGE_M_ROUTE` with the identity available at that instruction; `killpg` is never issued at stage M | R3, Sol M2 |
| 176 | the `c7` route removes `SPAWNING_MIDDLE.json` **only after** death is proved; a test that kills the proof step must leave the record intact | R3 |
| 177 | PID reuse at `2e` and death-proof expiry at step 3 each take the fail-closed continuation: **no record unlinked**, fds cleaned, lock reference released, `retryable = false` | R3 |
| 178 | assert that at `m0` no CLI action can produce EOF on `rel1_r` while the middle owns its own `rel1_w` copy; the middle exits by its bound or by the kill | R3, Sol M2 |
| 179 | assert the singleton is **not** free after a fail-closed `c5`–`c7` refusal while the middle child lives, and becomes free when its bound expires | R3 |
| 180 | every prefix of §V216.3.4 resumes correctly and never unlinks a live-identity record | R3 |
| 181 | the contract text contains **no** universal "no blocking syscall" or "healthy launch releases inside the bound" assertion; rows 121, 126, and 159 are jointly satisfiable | R4, Sol M3 |
| 182 | new row 126's deterministic slow-valid refusal and non-citability pass together with rows 160–162 | R4 |
| 183 | the `boot_w` row carries the EOF annotation and the `rel3_r` row carries none; assert every causal annotation names the correct end of its pair | R5, Sol m1 |
| 184 | no v2.1.5 or v2.1.4 executable rule changed as a side effect: diff every non-replaced section body against the carried text | R1–R5 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## V216.7. Crash-cut matrix (extends §V215.6)

Every §V215.6 row carries forward except where §V216.0 names a replacement.
Added rows:

| Cut | Single continuation |
|---|---|
| any physically present canonical object fails validation | **Rule 0**: record-first invalidity naming every malformed path; no branch; release nothing |
| valid settlement + malformed quarantine (± any manifest/hash state) | Rule 0; Rule 2 also blocked by `¬PQ` |
| malformed settlement + valid quarantine (non-null or null) | Rule 0; Rules 3 and 4 also blocked by `¬PS` |
| valid settlement + valid quarantine + malformed manifest | Rule 0 alone; exactly one record naming the malformed manifest |
| both terminals physically present, both valid | Rule 1; release nothing |
| a canonical object present as a symlink, directory, or zero-byte file | present for `P*`, invalid for `V*` ⇒ Rule 0 |
| normal close returns `EBADF` | `CLOSED_ABSENT`; ownership removed; nothing was closed; flow continues |
| normal close returns `EINTR` or another errno | `CLOSED_ERROR`; the descriptor was released; ownership removed; **never retried**; flow continues |
| a close is attempted on an unowned fd | `NOT_OWNED`; **no syscall**; no reused number can be closed |
| the lock close returns any error | ownership removed; the flock is released regardless; the refusal or success path proceeds |
| `c5` abandonment | `STAGE_M_ROUTE`: `kill(pid_mid)` after ppid + freshly captured start identity, prove death, cleanup, ordered removal, lock release |
| `c6` failure, `/proc` stat absent | `2b` death by absence, **no kill**, then cleanup, ordered removal, lock release |
| `c6` failure, stat present | `2d` identity-safe kill, prove death, then the rest |
| `c7` failure after the middle record's rename completed | death proved **before** the middle record is unlinked (§U6.3 boundary respected) |
| `c7` failure before the rename completed | only `SPAWNING.json` belongs to the attempt; the ordered removal is ENOENT-tolerant for the other three |
| PID reuse detected at `2e` | **no kill, no unlink**; fds cleaned; lock reference released; `retryable = false`; the next attempt's preflight and stuck-holder route govern |
| death proof exceeds its bound | identical fail-closed continuation |
| fail-closed continuation with the middle child still live | the singleton is **not** free until that child exits at its own bound — stated, not concealed |
| CLI crash anywhere in `STAGE_M_ROUTE` | the kernel releases the CLI's fds and its lock reference; no record was removed before death proof; the next attempt's P0–P3 governs |
| any assertion that a bootstrap syscall cannot outlive its deadline | **deleted**; only pipe reads and writes are bounded by their helper deadlines |
| slow-but-valid `c14`/`c15` exceeding the grandchild gate | deterministic refusal, whole attempt fails closed, non-citable, creates nothing |
| a causal EOF annotation naming a read end | **deleted**; closing a read end can only cause `EPIPE` on the paired write |

---

## V216.8. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The disposition selector is six
rules over three physical-presence and three validity predicates, with a
fourteen-row cross-product and five named counterexamples (§V216.1); every
close in the bootstrap is one primitive with four outcomes, an unconditional
ownership removal, a never-retry rule, and a per-site continuation table
(§V216.2); `c5`, `c6`, and `c7` each have an identity source, a kill authority,
a death proof, and an eleven-row prefix table, with an explicit fail-closed
continuation that unlinks nothing (§V216.3); the bound language is replaced at
five named loci with a four-row test reconciliation (§V216.4); and every
descriptor's causal consequence is audited end by end (§V216.5). No clause
resolves to "as reviewed", "as appropriate", or implementer discretion.

**Compatibility classification.** Unchanged: an engineering/control amendment
surface over the signed harness composite, containing no protocol amendment
except §W6.5's explicitly named supersession of harness §5a's physical
at-or-before-deadline sentence. The signed generic-harness contract
(v2/v2.1/v2.2/v2.3/v2.3.1) and the signed batch-settlement amendment
(v1/v1.1/v1.1.1, including §D1 head/cache completion and §D2 inline
`meter_evidence`) are referenced unchanged. No signed archival set, event,
runtime schema, root, constant, resource value, T band, or Q/C boundary moves.
The import-allowlist delta remains **none**.

**No author cell is reopened.** A3 is untouched: the four write/hash residuals,
their non-citability, and the absence of a `HASH` route carry forward, and
§V216.2's close diagnostics are explicitly non-citable control-plane facts. B1
is untouched: no journal, acknowledgement, frontier, prefix, GC, or
classification rule changes. C1 is untouched: the watchdog remains a
witness/freezer holding no lock or capability, writing nothing under
`runtime/`, appending no ledger, and settling nothing. D1 is untouched and
strengthened in practice: §V216.2 and §V216.3 remove the last close and
pre-group-cleanup constructions that were left to implementer discretion, and
§V216.3.2 no longer claims a lock is free when it is not. K1 is untouched:
five constants unmoved, no replenishment, literal write-once/hash-once counts,
`bytes_reserved` accounted until a verified disposition, the three branch
bodies unchanged, and §V216.1 **removes** the only path by which a malformed
impossible layout could have released capacity. **No new author-choice token is
proposed, and none was found to be unavoidable.**

**Negative space.** This correction creates nothing executable and authorizes
no implementation, commit, host change, process, supervisor, controller,
worker, watchdog, adapter, middle child, endpoint, pipe, FIFO, journal
instance, tombstone, spawn record, lease, capability, operation, output bound,
framed transport, result manifest, quarantine record, promoted object, capacity
artifact, custody disposition, author decision file, freeze witness, fallback
witness, replacement-freeze record, entropy, E1/E2/E3 spend, world, learner,
candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim movement. It
predicts no qualification and no C1–C6 outcome. Process invalidity, resource
exhaustion, and missing evidence remain infrastructure facts and are nowhere
treated as scientific evidence. No example in this document was written to any
file.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Its only next authorization step is a
**fresh independent X-line review and a fresh independent Y-line review of the
v2.1.6 bytes**; there is no X verdict for v2.1.5, and no earlier confirmation
of any version carries across. `successor/officina/runtime/` contains only
`T_RUNTIME.lock`; `successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
