# Officina supervisor and control-channel amendment — v2.1.7 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1 through
v2.1.6. It is **not** an independent X-line or Y-line review of its own bytes
and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain is an untrusted self-assessment; none of their claims is
used as evidence here.

**Review state of v2.1.6, recorded exactly.** **Both** independent lines
returned `REVISE_OFFICINA_SUPERVISOR_V2_1_6`. The Y line raised C1 (Critical),
M1 and M2 (Major); the X line raised X216-M1 (Major) and X216-m1 (Minor). The
findings are complementary and **all govern**. There is no v2.1.6 confirmation
of any kind, and there was no formal X verdict for v2.1.5. **v2.1.7 requires a
fresh X-line review and a fresh Y-line review**; no earlier confirmation of any
version carries across.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md`
(v2.1.6), which layers over v2.1.5, v2.1.4, v2.1.3, v2.1.2, v2.1.1, v2.1, and
v2 — all eight preserved unedited as review evidence. **Everything not named in
the §V217.0 replacement index carries forward verbatim.**

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged**, including every repair both
lines confirmed: the `CLOSE_OWNED` primitive and its application at every close
site including both lock closes (§V216.2, confirmed by both lines);
physical-presence dominance and the `MALFORMED`-first rule ordering (§V216.1.2's
rule structure, confirmed by both lines, repaired only in its *observation*
binding); death-before-unlink for every record naming a process other than the
CLI (§V216.3, confirmed by both lines); the corrected `boot_w` EOF provenance
and the eight-end audit (§V216.5, confirmed by both lines); the narrowed
pipe-only bootstrap invariant and replaced rows 121/126 (§V216.4.1's
replacement text and §V216.4.3, confirmed by the Y line); the three branch
bodies `B-P`/`B-QM`/`B-QN` and §V214.2.4's custody/accounting reconciliation;
the nonblocking channels and bounded helpers; the GC order with `accepted.json`
last and `D6`; the lock-first preflight and non-mutating stuck-holder route; the
total watchdog partition; the four-residual A3 distinction; and the whole
carried §V215/§V214/§U/§N/§Z/§W/§V2 chain.

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
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
e395da8b6366b35da19dfeaf28a0fb25bedd9e07245ffb97b60f7f3b870ad9db  reviews/opus_officina_supervisor_control_channel_v2_1_6_final_confirmation.md
b38488cfeb422f16eda48561d5706d160ca7dc25969533e32265fa8a31c648c8  reviews/sol_officina_supervisor_control_channel_v2_1_6_final_confirmation.md
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

## Engineering constants

**Zero new constants, durable objects, paths, durable schemas, schema keys,
wire enum tokens, refusal or `INVALID` tokens, public commands, signed events,
resource values, roots, or archival-set changes. Zero import-allowlist delta.**
The selector observation record of §V217.1 is **in-memory only**: never
persisted, never transmitted, never a durable schema. The syscall-result enums
of §V217.2 and the `CLOSE_OWNED` outcome labels are likewise internal
control-plane labels. §V217.3 installs no new record class — it reuses the
already-signed `SPAWNING_MIDDLE.json`. This layer uses only `os.close`,
`os.open`, `os.stat`, `os.fstat`, `os.pread`, `os.listdir`, `os.kill`,
`os.waitpid`, `os.unlink`, `os.fsync`, `os.getpid`, `hashlib`, and `json` — all
inside allowlisted modules; `select`, `selectors`, `signal`, `ctypes`, and
`sys` remain outside.

---

## V217.0. Exact replacement index (v2.1.6 → v2.1.7)

**Nothing else moves.** Everything in v2.1.6 and in every layer it carries — in
particular §V216.1.2's rule *structure* and `MALFORMED` dominance, §V216.1.3's
sub-routing and cross-product, §V216.2 in full, §V216.3.1, §V216.3.3's cut
identification, §V216.4.1's replacement text, §V216.4.3, §V216.5 in full, and
the entire carried §V215/§V214/§U/§N/§Z/§W/§V2 chain — carries forward verbatim
except at the rows below.

| v2.1.6 (or carried) locus (exact sentence / clause / table row) | Action in v2.1.7 |
|---|---|
| §V216.1.1's observation paragraph "All observations are taken in **one held `T_RUNTIME.lock` epoch**, from one directory-fd enumeration … plus one `follow_symlinks=False` `stat` per canonical name" and its `PS`/`PQ`/`PF`, `VS`/`VQ`/`VF`, `B`, `HS`, `HQ` definitions | **replaced** by §V217.1.1–§V217.1.3 (one closed object-bound observation record per name; every predicate consumes only that record) |
| §V216.1.2's three numbered properties, in particular property 3's clause "this makes the malformed-opposite-terminal release impossible by **two independent conjuncts**" | **replaced** by §V217.1.5 (the two conjuncts bind the *observed* state; the post-barrier window is named as the signed A3 procedural residual and is **not** claimed impossible) |
| §V216.1.2's rule block (entry into `B-P`/`B-QM`/`B-QN`) | **extended** by §V217.1.4 (revalidation barrier 1 immediately before branch entry) |
| §N1.5 conjunct 12 / §V214.2's `.disposed.json` install step, as carried | **extended** by §V217.1.4 (revalidation barrier 2 immediately before the install and any release) |
| §V216.3.2 `STAGE_M_ROUTE` steps `2a`–`2f` | **replaced** by §V217.2.1–§V217.2.2 (closed `/proc` stat result enum; `UNREADABLE`/`UNPARSABLE`/`ERROR` are not identity-safe) |
| §V216.3.2 step 2's clause "`os.kill(pid_mid, SIGTERM)`, then `os.kill(pid_mid, SIGKILL)`" | **replaced** by §V217.2.3 (closed signal-result enum with `ESRCH`/`EINTR`/`EPERM`/other routes and pinned SIGTERM→SIGKILL timing) |
| §V216.3.2 step 3's death proof | **replaced** by §V217.2.4 (closed `waitpid` result enum; `waitpid` is the authoritative, `/proc`-independent proof) |
| §V216.3.2's `FAIL-CLOSED CONTINUATION` block `F1`–`F5` | **replaced** by §V217.3.2–§V217.3.4 (three exhaustive terminals; the CLI always removes its own `SPAWNING.json`; `SPAWNING_MIDDLE.json` is installed when identity is known) |
| §V216.3.2 step 5's clause "remove ONLY records belonging to THIS attempt" | **extended** by §V217.3.1 (the death-proved-only boundary is stated precisely: it governs the three records naming processes **other than the CLI**) |
| §V216.3.3's `c6` row cell "absent ⇒ `2b` death by absence, **no kill**; else `2d`" | **replaced** by §V217.2.5 (the five-way stat result mapping) |
| §V216.3.4's crash-prefix table | **replaced** by §V217.3.5 (restated over the three terminals) |
| §V216.4.1's sentence "Consequently no statement anywhere asserts that no bootstrap syscall can outlive a deadline, or that every healthy launch releases within the grandchild gate bound" | **replaced** by §V217.4.1 (a scoped, reproducible claim; the false universal is deleted) |
| §V216.4.2's sentence "An exhaustive search of the operative chain for `no blocking syscall`, `healthy bootstrap`, `healthy launch`, and `always releases` yields exactly these five loci; there are no others." | **replaced** by §V217.4.2 (a declared search-term set, six stale loci, and a retained-statement table; the false completeness claim is deleted) |
| carried v2.1.2 §N3.5 sentence "Every CLI wait in this contract is bounded — … so a contract-following CLI always releases within that arithmetic sum (30 s + 10 s + 10 s + bounded proof)." | **replaced** by §V217.4.3 |
| carried v2.1.2 §N11 crash-cut row cell "every contract-following CLI wait is bounded" | **replaced** by §V217.4.3 |
| carried v2.1.2 §N12 test row **86** | **replaced** by §V217.4.4 |
| carried v2.1.3 §U2.4 sentence "Total CLI bound: `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` + 3 × `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` + bounded kill/death proof (30 s + 30 s + bounded), all reusing existing constants. No wait is unbounded." | **replaced** by §V217.4.3 |
| carried v2.1.3 §U2.7 residual-1 clause "every contract-following CLI wait is bounded (§U2.4's arithmetic)" | **replaced** by §V217.4.3 |
| §V216.7 crash-cut matrix | **extended** by §V217.5 (twenty-eight added rows) |
| §V216.6 test-obligation rows 165–184 | **extended** by §V217.6 (rows 185–212); rows 181 and 184 are **replaced** |

---

## V217.1. Object-bound selector observation and revalidation (R1)

Closes Sol C1. §V216.1.2's rule structure and `MALFORMED` dominance, §V216.1.3's
sub-routing and cross-product, the three branch bodies, §N2.3's P1–P7 custody
proof, and every §N1.5 conjunct are **unchanged**. What changes is how the
predicates obtain their facts, and that they are re-obtained at two barriers.

### V217.1.1 One closed observation record per canonical name

In-memory only — never persisted, never transmitted, never a durable schema:

```text
observation record (per canonical name), fields exactly:
  epoch_id            the selector snapshot id (§V217.1.3)
  canonical_name      one of SETTLEMENT.json | QUARANTINE.json |
                      RESULT_MANIFEST.json
  enumerated          bool — the name appeared in THIS epoch's single
                      os.listdir(op_dirfd)
  lstat_result        ABSENT | PRESENT
  lstat_type          REG | DIR | LNK | CHR | BLK | FIFO | SOCK | UNKNOWN,
                      or null when ABSENT
  lstat_dev, lstat_ino, lstat_nlink, lstat_size    or null when ABSENT
  fd_opened           bool
  fstat_dev, fstat_ino, fstat_nlink, fstat_size    or null
  bytes_sha256        SHA-256 of the exact bytes read THROUGH the opened
                      descriptor, or null
  decode_result       NOT_ATTEMPTED | VALID | INVALID
  decoded             the decoded object (in memory) or null
  absence_paired      bool — ENOENT from lstat AND non-membership in the
                      enumeration
```

### V217.1.2 The observation algorithm

```text
OBSERVE(canonical_name, op_dirfd, epoch_id):
 O1. enumerated := canonical_name ∈ THIS epoch's single os.listdir(op_dirfd)
 O2. lstat := os.stat(canonical_name, dir_fd=op_dirfd, follow_symlinks=False)
       ENOENT            ⇒ lstat_result := ABSENT
       any other OSError ⇒ OBSERVATION_INCONCLUSIVE
       success           ⇒ lstat_result := PRESENT; record type/dev/ino/
                           nlink/size
 O3. if ABSENT:
       absence_paired := ¬enumerated
       if enumerated (name listed but ENOENT ⇒ the entry changed mid-epoch)
                         ⇒ OBSERVATION_INCONCLUSIVE
       fd_opened := false; decode_result := NOT_ATTEMPTED; return
 O4. if lstat_type ≠ REG or lstat_nlink ≠ 1:
       fd_opened := false; decode_result := INVALID; return
       — PRESENT AND INVALID. A symlink, directory, device, FIFO, socket,
         or multiply-linked file is NEVER absence.
 O5. fd := os.open(canonical_name, O_RDONLY|O_NOFOLLOW|O_CLOEXEC,
                   dir_fd=op_dirfd)
       ELOOP (a symlink appeared between O2 and O5)
                         ⇒ decode_result := INVALID; return
       ENOENT (removed between O2 and O5)
                         ⇒ OBSERVATION_INCONCLUSIVE
       any other OSError ⇒ OBSERVATION_INCONCLUSIVE
       success           ⇒ fd_opened := true
 O6. fstat := os.fstat(fd); record dev/ino/nlink/size/type
       require (fstat_dev, fstat_ino) == (lstat_dev, lstat_ino)
           and fstat_nlink == 1 and the type is REG
       mismatch          ⇒ OBSERVATION_INCONCLUSIVE
                            (the name was replaced between O2 and O5)
 O7. read the ENTIRE object THROUGH fd with os.pread from offset 0 in
     T_OUTPUT_COPY_CHUNK_BYTES chunks until EOF
       require total length == fstat_size and EOF exactly at that offset
       length/EOF anomaly ⇒ OBSERVATION_INCONCLUSIVE
       bytes_sha256 := SHA-256(those exact bytes)
 O8. decode those exact bytes canonically against the name's exact schema
       success ⇒ decode_result := VALID; decoded := the object
       failure ⇒ decode_result := INVALID
 O9. the descriptor is RETAINED OPEN for the whole selector epoch — it pins the
     inode so a barrier can re-`fstat` the same open description — and is closed
     through CLOSE_OWNED at the end of the epoch
```

**`OBSERVATION_INCONCLUSIVE`** at any step aborts the whole selector run to
**record-first refusal/invalidity naming the canonical path and the failing
step**; it releases nothing and enters no branch. It is never treated as
absence and never as validity.

### V217.1.3 The snapshot and the predicates

One selector snapshot is one `epoch_id`, produced inside one held
`T_RUNTIME.lock` epoch from **one** `os.listdir(op_dirfd)`, with `OBSERVE` run
for all three canonical names and **no frame served between them**. All three
records carry that `epoch_id`; a mixed-epoch record set is a contract violation,
not a route.

Every predicate consumes **only** these records:

```text
PS ≜ ¬record[SETTLEMENT.json].absence_paired
PQ ≜ ¬record[QUARANTINE.json].absence_paired
PF ≜ ¬record[RESULT_MANIFEST.json].absence_paired
VS ≜ record[SETTLEMENT.json].decode_result == VALID
VQ ≜ record[QUARANTINE.json].decode_result == VALID
VF ≜ record[RESULT_MANIFEST.json].decode_result == VALID
MALFORMED ≜ (PS ∧ ¬VS) ∨ (PQ ∧ ¬VQ) ∨ (PF ∧ ¬VF)
B  ≜ VQ ∧ record[QUARANTINE.json].decoded.result_manifest_sha256_or_null ≠ null
HS ≜ VS ∧ VF ∧ record[RESULT_MANIFEST.json].bytes_sha256
              == record[SETTLEMENT.json].decoded.result_manifest_sha256
HQ ≜ B  ∧ VF ∧ record[RESULT_MANIFEST.json].bytes_sha256
              == record[QUARANTINE.json].decoded.result_manifest_sha256_or_null
```

Two consequences, each required:

- **Presence is the negation of *paired* absence.** A name that is enumerated,
  or that `lstat`s successfully, is present. Only the conjunction of `ENOENT`
  and non-membership is absence. A symlink, directory, device, FIFO, socket,
  multiply-linked, zero-byte, truncated, partially written, or replaced object
  is therefore **present and invalid**, never absence.
- **The hash predicates consume the bytes actually read through the pinned
  descriptor** (`bytes_sha256`), not a re-read of the name. The manifest cannot
  be swapped between the hash computation and its use.

§V216.1.2's rules and §V216.1.3's sub-routing and cross-product are unchanged
and now operate on these bound facts.

### V217.1.4 Two revalidation barriers

Both use the **same** `OBSERVE` algorithm over all three names, produce a fresh
`epoch_id`, and run inside the same held `T_RUNTIME.lock` epoch as the selector
and the branch.

```text
BARRIER(kind ∈ {BRANCH_ENTRY, DISPOSITION}) :
  re-run O1–O8 for ALL THREE canonical names ⇒ a fresh record set
  require, for EACH name:
    R-a. absence_paired unchanged — a name observed absent must still satisfy
         BOTH ENOENT and non-enumeration
    R-b. if present: (lstat_dev, lstat_ino) unchanged; nlink still 1; the
         RETAINED descriptor's (fstat_dev, fstat_ino) still equal the fresh
         lstat's; bytes_sha256 unchanged; decode_result unchanged
  require the CROSS-OBJECT relation unchanged: B, HS, HQ evaluate as before,
         and the SAME rule of §V216.1.2 fires on the fresh record set
  any difference, any OBSERVATION_INCONCLUSIVE, or a different rule
    ⇒ record-first refusal/invalidity naming the changed path and the failing
      requirement; release nothing; no branch entered, and if already inside a
      branch, no disposition installed
```

**Barrier 1 — `BRANCH_ENTRY`**: immediately before entering `B-P`, `B-QM`, or
`B-QN`, after the rule has been selected. A terminal installed after its
original presence observation is now **enumerated and present** at the barrier,
so `PQ` (or `PS`) becomes true, the releasing rule no longer fires, and the
barrier's "same rule" requirement fails ⇒ nothing is released.

**Barrier 2 — `DISPOSITION`**: immediately before installing
`CAPACITY/<op>.disposed.json` and before any capacity is released, and after
§N2.3's P1–P7 complete-custody proof, which must itself still hold in the same
epoch. This catches a mutation introduced between branch entry and disposition —
including the case the Y line named, where `QUARANTINE.json` is an allowed L2
control record and therefore invisible to the custody proof.

### V217.1.5 The honest residual (replacing the "impossible" claim)

§V216.1.2's property-3 clause "impossible by **two independent conjuncts**" is
**deleted** and replaced by:

> The `¬MALFORMED` and opposite-terminal-absence conjuncts make the **observed**
> state unable to release, and the two barriers of §V217.1.4 re-establish that
> observation immediately before branch entry and immediately before any
> release. A deliberate same-UID mutation performed **after the final
> `DISPOSITION` barrier** is **not** prevented: it is the already-signed **A3
> procedural residual**, exactly like the four output residuals of §V214.6 and
> the bootstrap residuals of §U2.7. It is T-development-only, permanently
> **non-citable**, forbidden from selection, Q, C, C1–C6, any blinding claim,
> and any scientific or resource interpretation, and it is **not** claimed
> impossible. `T_RUNTIME.lock` serializes contract actors; it is not a
> same-UID filesystem exclusion mechanism, and this contract asserts no such
> mechanism and invents no security boundary.

### V217.1.6 Complete mutation-cut table

For each window, what catches a create, remove, rename, replace, or content
change of a canonical object.

| Mutation window | Caught by | Outcome |
|---|---|---|
| before `O1` | ordinary observation | the mutated state is what is observed; the rules apply to it |
| between `O1` and `O2` — name listed, then removed | `O3`'s `enumerated ∧ ENOENT` test | `OBSERVATION_INCONCLUSIVE` |
| between `O1` and `O2` — name created after the listing | `O2` `lstat` succeeds ⇒ PRESENT ⇒ `enumerated=false, lstat=PRESENT` ⇒ `absence_paired=false` ⇒ **present** | present, and validity decides the rule |
| between `O2` and `O5` — replaced by a symlink | `O5` `ELOOP` | `INVALID` (present) |
| between `O2` and `O5` — removed | `O5` `ENOENT` | `OBSERVATION_INCONCLUSIVE` |
| between `O2` and `O5` — replaced by a different regular file | `O6` `(dev, ino)` mismatch | `OBSERVATION_INCONCLUSIVE` |
| between `O5` and `O7` — content rewritten in place | `O7` reads through the **pinned descriptor**; the length/EOF check and `bytes_sha256` describe exactly what was read; a size change is caught by `fstat_size` | either a coherent bound observation, or `OBSERVATION_INCONCLUSIVE` |
| between `O7` and `O8` | the decode operates on the **bytes already read**, not a re-read | unaffected |
| between the snapshot and **barrier 1** — opposite terminal created | barrier `R-a` (absence no longer paired) and the "same rule" requirement | refusal/invalidity; **no branch entered** — the exact Y-line attack |
| between the snapshot and barrier 1 — a present object replaced | barrier `R-b` (`ino` or `bytes_sha256` changed) | refusal/invalidity |
| between the snapshot and barrier 1 — a present object removed | barrier `R-b`/`R-a` | refusal/invalidity |
| between barrier 1 and **barrier 2** — any create/remove/rename/replace/content change | barrier 2, which re-runs the identical algorithm | refusal/invalidity; **no `.disposed.json`, no release** |
| between barrier 2's observation and the `.disposed.json` install | **not prevented** | the named **A3 procedural residual** of §V217.1.5; non-citable; not claimed impossible |
| a `.tmp` or extra `operation_id`-bearing entry at any time | not a canonical name ⇒ changes no predicate; L4/L5 custody classes | §N2.3 P5/P6 refuse |

---

## V217.2. Total syscall-result state machine for stage M (R2)

Closes Sol M1 and Opus X216-m1. Every syscall in `STAGE_M_ROUTE` is mapped to a
closed result enum; **no exception may escape**, and an escaping exception is a
contract violation, not a route.

### V217.2.1 `/proc` stat observation

```text
STAT_OBSERVE(pid) → ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE | ERROR
  read /proc/<pid>/stat in full:
    ENOENT / ESRCH        ⇒ ABSENT
    EACCES / EPERM        ⇒ UNREADABLE
    EINTR                 ⇒ bounded retry at T_SUPERVISOR_POLL_INTERVAL_NS
                            until the step's existing signed deadline; on
                            expiry ⇒ ERROR
    any other OSError     ⇒ ERROR
  parse per §V2.1.3 — the 20th whitespace-separated token after the FINAL ')'
  (kernel starttime), plus the state field and ppid:
    no final ')', short token list, non-integer field, or any parse failure
                          ⇒ UNPARSABLE
    success               ⇒ PRESENT_VALID with (start_identity, ppid, state)
```

**Only `ABSENT` and `PRESENT_VALID` may contribute to an identity or death
conclusion.** `UNREADABLE`, `UNPARSABLE`, and `ERROR` are **not identity-safe**:
they authorize no kill, no unlink, and no death conclusion, and they route to
§V217.3's terminal selection.

### V217.2.2 Identity-safety (replacing `2a`–`2e`)

```text
IDENTITY_SAFE(pid_mid) :
  s := STAT_OBSERVE(pid_mid)
  ABSENT        ⇒ not present; no signal is needed or sent; go directly to
                  WAIT_PROVE (§V217.2.4) — absence alone NEVER proves death
  PRESENT_VALID ∧ a start identity was already captured (c6 or c7 completed)
                ∧ it MATCHES               ⇒ IDENTITY-SAFE
  PRESENT_VALID ∧ no start identity captured yet
                ∧ s.ppid == os.getpid()    ⇒ capture s.start_identity now;
                                             IDENTITY-SAFE
  PRESENT_VALID ∧ a captured start identity MISMATCHES  ⇒ NOT identity-safe
                  (PID reuse); no kill; go to §V217.3
  UNREADABLE | UNPARSABLE | ERROR          ⇒ NOT identity-safe; no kill;
                                             go to §V217.3
```

### V217.2.3 Signal attempts

```text
SIGNAL_ATTEMPT(pid, sig) → SENT | GONE | INTERRUPTED | DENIED | ERROR
  os.kill(pid, sig)
    success           ⇒ SENT
    ESRCH             ⇒ GONE — the pid names no process. This ALONE NEVER
                        proves death (it is also what a reaped or reused pid
                        looks like). Proceed to WAIT_PROVE.
    EINTR             ⇒ INTERRUPTED ⇒ retry the SAME signal at
                        T_SUPERVISOR_POLL_INTERVAL_NS until the step's existing
                        signed deadline; on expiry ⇒ ERROR
    EPERM             ⇒ DENIED ⇒ send no further signal, unlink nothing, go to
                        §V217.3
    any other OSError ⇒ ERROR ⇒ same route as DENIED
```

**SIGTERM → SIGKILL timing**, inside the one existing signed deadline, with no
new constant:

```text
t0 := the step's monotonic start; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
 1. SIGNAL_ATTEMPT(pid_mid, SIGTERM)
 2. poll WAIT_PROVE at T_SUPERVISOR_POLL_INTERVAL_NS until t0 + D/2
 3. if not PROVED_DEAD by t0 + D/2: SIGNAL_ATTEMPT(pid_mid, SIGKILL)
 4. poll WAIT_PROVE until t0 + D
 5. at t0 + D without PROVED_DEAD ⇒ go to §V217.3
Deadline edge: a poll whose sample is exactly t0 + D/2 or exactly t0 + D is
treated as EXPIRED (the comparison is ≥), so no edge is ambiguous.
```

### V217.2.4 The authoritative death proof

```text
WAIT_PROVE(pid_mid) → PROVED_DEAD | NOT_YET | INCONCLUSIVE
  os.waitpid(pid_mid, WNOHANG)
    returns (pid_mid, status) ⇒ PROVED_DEAD
    returns (0, 0)            ⇒ NOT_YET — the child exists and has not
                                terminated (it may be running or stopped)
    ECHILD                    ⇒ PROVED_DEAD
    EINTR                     ⇒ bounded retry at T_SUPERVISOR_POLL_INTERVAL_NS
                                until the step's deadline; on expiry
                                ⇒ INCONCLUSIVE
    any other OSError         ⇒ INCONCLUSIVE
```

**Why these two outcomes prove death, exactly.**

- `waitpid` returning `pid_mid` is the **strongest possible** proof: the CLI is
  this process's parent by construction (`c4`'s `os.fork` return), the child has
  terminated, and the kernel has now reaped it in this call.
- `ECHILD` means the caller has no such child. For a pid this CLI itself forked,
  that can only be true if the child has already terminated **and been reaped**.
  This contract installs **no signal disposition** anywhere (`signal` is outside
  `ALLOWED_ABSOLUTE_IMPORTS`), so `SIGCHLD` keeps its default disposition and
  children are **never auto-reaped**; the only reaper is this route. `ECHILD`
  therefore means this route already reaped it, and the child is dead.
- **This proof is independent of `/proc`.** An `UNREADABLE`, `UNPARSABLE`, or
  `ERROR` stat never blocks it.

**PID reuse.** While the terminated child is unreaped it is a zombie and its pid
**cannot** be reassigned, so every signal and stat before `PROVED_DEAD` targets
this child or nothing. After `PROVED_DEAD` the pid may be reused, so the route
**never signals, stats, or waits on `pid_mid` again** once `PROVED_DEAD` is
returned.

**Ordinary-exit races.** SIGTERM `SENT`, child exits, SIGKILL returns `GONE` ⇒
`WAIT_PROVE` returns `PROVED_DEAD`. Child exits before any signal ⇒ first
`SIGNAL_ATTEMPT` returns `GONE` ⇒ `WAIT_PROVE` ⇒ `PROVED_DEAD`. Child exits
between the two polls ⇒ the next poll returns `PROVED_DEAD`.

### V217.2.5 The `c5`/`c6`/`c7` cut mapping (replacing §V216.3.3's cell)

| Cut | `STAT_OBSERVE` result | Continuation |
|---|---|---|
| `c5`, `c6`, or `c7` abandonment | `ABSENT` | no signal; `WAIT_PROVE` decides |
| any | `PRESENT_VALID`, identity matches or `ppid == getpid()` | identity-safe ⇒ the §V217.2.3 signal sequence, then `WAIT_PROVE` |
| any | `PRESENT_VALID`, captured identity mismatches | PID reuse ⇒ no kill ⇒ §V217.3 terminal selection |
| **`c6` unreadable stat** | `UNREADABLE` | not identity-safe ⇒ **no kill, no unlink** ⇒ §V217.3 (this is Opus X216-m1's exact gap) |
| **`c6` unparsable stat** | `UNPARSABLE` | identical |
| any host fault | `ERROR` | identical |

---

## V217.3. Executable SPAWNING-only terminal without a long-lived-CLI wedge (R3)

Closes Sol M2. **No new record class, schema, path, or stuck-holder tier is
introduced**; the route reuses the already-signed `SPAWNING_MIDDLE.json` and the
existing `s4` tier.

### V217.3.1 The death-proved-only boundary, stated precisely

§U6.3's protection exists to prevent unlinking a record that is the **only
durable handle on a process which may still act**. Applied exactly:

| Record | Names | Protected by death-before-unlink? |
|---|---|---|
| `SPAWNING_CHILD.json` | the grandchild | **yes** — it is the sole handle on a process that may still act |
| `SPAWNING_GROUP.json` | the verified session/group | **yes** |
| `SPAWNING_MIDDLE.json` | the middle child | **yes** |
| `SPAWNING.json` | **this CLI itself** | **no** — see below |

> **`SPAWNING.json` names only the CLI.** It is never a handle on the middle
> child, the group, or the grandchild, so removing it can orphan nothing and
> can disrupt no continuing action. Once the CLI has decided to abandon the
> attempt it will, by construction, perform no further action in that attempt.
> **The abandoning CLI therefore always removes its own `SPAWNING.json`, on
> every route, while still holding `SPAWN.lock`.** The death-proved-only
> boundary continues to govern the other three records without exception.

This is what removes the Y-line wedge at its root: a live long-running CLI can
never leave behind a `SPAWNING.json` naming itself, so the next attempt's P2b
can never be triggered by it.

**Two-supervisor safety, proved.** Removing `SPAWNING.json` while the middle
child may still live cannot yield a second supervisor: the middle child must
pass its `m5` stage-2 gate to fork the grandchild, that gate is released only by
the CLI's `c12` write on `rel2_w`, and the abandoning CLI has closed `rel2_w`
through `CLOSE_OWNED` — so `m5` observes **EOF** (the middle closed its own
`rel2_w` copy at `m1`, making the CLI the sole remaining writer) and exits, or
its bound expires first. A middle child that never passes `m5` never forks a
grandchild and never installs `SUPERVISOR_IDENTITY.json`.

### V217.3.2 Three exhaustive terminals

Every `STAGE_M_ROUTE` exit takes exactly one:

```text
S1. CLOSE_OWNED cleanup of the CLI's bootstrap ends (§V216.2.2)

T1  WAIT_PROVE returned PROVED_DEAD
    ⇒ ordered removal of ALL FOUR of this attempt's records in the §U6.3 order
      SPAWNING_CHILD → SPAWNING_GROUP → SPAWNING_MIDDLE → SPAWNING, each unlink
      followed by fsync(T_SUPERVISOR/), ENOENT tolerated, matched by
      spawning_id, while still holding SPAWN.lock
    ⇒ CLOSE_OWNED(spawn_lock_fd); REFUSED / BOOTSTRAP, retryable = true
    ⇒ NO record survives; the next attempt starts at P0

T2  not PROVED_DEAD, and a PRESENT_VALID stat was obtained at some point in
    this route (so pid + start identity + ppid are known)
    ⇒ install SPAWNING_MIDDLE.json for this attempt if it is not already
      durable, with the already-signed §U2.2 c7 key set (schema,
      scientific_outcome, spawning_id, cli_pid, cli_start_identity,
      middle_child_pid, middle_child_start_identity, boot_identity,
      created_utc), under the §U6.2 EEXIST discipline. Every field is known;
      nothing is fabricated.
    ⇒ remove ONLY SPAWNING.json (§V217.3.1), with its fsync
    ⇒ CLOSE_OWNED(spawn_lock_fd); REFUSED / BOOTSTRAP, retryable = true
    ⇒ the surviving handle is SPAWNING_MIDDLE.json, which the EXISTING s4 tier
      resolves (see §V217.3.3)

T3  not PROVED_DEAD, and no PRESENT_VALID stat was ever obtained
    (UNREADABLE / UNPARSABLE / ERROR throughout, or DENIED signals)
    ⇒ install NOTHING — no field may be fabricated, and no record naming
      another process may be removed
    ⇒ remove ONLY SPAWNING.json (§V217.3.1), with its fsync
    ⇒ CLOSE_OWNED(spawn_lock_fd); REFUSED / BOOTSTRAP, retryable = false —
      the explicitly named terminal "bootstrap abandoned; middle-child identity
      unprovable"
    ⇒ at c5/c6 no other record of this attempt exists, so NO record survives
      and the next attempt starts at P0. At c7-after-rename,
      SPAWNING_MIDDLE.json survives and §V217.3.3 governs it.
```

### V217.3.3 Forward progress, using only existing routes

| Surviving state | Next attempt's behaviour | Bound |
|---|---|---|
| nothing (T1; T3 at `c5`/`c6`) | §U6.1 P0 ⇒ install and proceed | immediate |
| `SPAWNING_MIDDLE.json`, recorded process still live (T2; T3 at `c7`) | §U6.1 P2b ⇒ `REFUSED`/`BOOTSTRAP` (retryable) — no unlink, no kill | until the record is older than `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` |
| the same, once aged | the **existing** §U2.5 `s4` tier: `kill(middle_child_pid)` **only** (never `killpg`), after start-identity validation, then proved death, then a bounded retry of the acquisition; `c1b`'s preflight P3 then removes the record under the acquired lock | bounded by `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` + the `s4` route's own bounds |
| the same, recorded process not live | §U6.1 P3 ⇒ death proved by absence/`Z`/identity mismatch ⇒ ordered removal ⇒ proceed | immediate |

No new tier, record, schema, or operator step is required, and **no route
depends on caller exit, garbage collection, a finalizer, or an unstated
operator**. The `s4` tier already exists, already targets exactly
`SPAWNING_MIDDLE.json`, and already uses `kill(pid)` with start-identity
validation.

### V217.3.4 Named residual, stated not claimed away

A middle child that is **deliberately `SIGSTOP`ed by a same-UID actor** retains
its fork-shared `SPAWN.lock` reference until it is killed. In **T2** it is
tracked by `SPAWNING_MIDDLE.json` and the `s4` tier reaches it within a bounded
time. In **T3** — where the host prevented every identity observation — it is
untracked, and the singleton stays held until that process is terminated. This
is the **signed A3 procedural residual**, the same class as the already-named
stopped-CLI and stopped-middle residuals of §U2.7 and §V216.3, it is
permanently non-citable, and it is **not** claimed impossible. It is strictly
narrower than v2.1.6's state, in which the same case *plus* every ordinary
long-lived-CLI case wedged.

### V217.3.5 Complete crash and cut table (replacing §V216.3.4)

| Cut / scenario | Continuation |
|---|---|
| **long-lived CLI**, failure at `c5`/`c6`, child proved dead | T1: all records removed; the CLI's own `SPAWNING.json` is gone, so no future P2b can name it; **no wedge** |
| **long-lived CLI**, failure at `c5`/`c6`, child not proved dead, identity known | T2: `SPAWNING_MIDDLE.json` installed, `SPAWNING.json` removed; `s4` resolves it; **no wedge** |
| **long-lived CLI**, failure at `c5`/`c6`, identity never obtainable | T3: `SPAWNING.json` removed, nothing else exists; next attempt starts at P0; **no wedge** |
| **stopped middle child** | `SIGKILL` cannot be blocked or ignored and terminates a stopped process, so `WAIT_PROVE` reaches `PROVED_DEAD` ⇒ T1 |
| middle exits **before** any signal | first `SIGNAL_ATTEMPT` ⇒ `GONE` ⇒ `WAIT_PROVE` ⇒ `PROVED_DEAD` ⇒ T1 |
| middle exits **between** SIGTERM and SIGKILL | SIGKILL ⇒ `GONE` ⇒ `WAIT_PROVE` ⇒ `PROVED_DEAD` ⇒ T1 |
| `/proc` **unreadable** or **unparsable** | not identity-safe ⇒ no kill; `WAIT_PROVE` is `/proc`-independent and usually still returns `PROVED_DEAD` ⇒ T1; otherwise T3 |
| signal `ESRCH` | `GONE` ⇒ `WAIT_PROVE` decides; never death by inference |
| signal `EPERM` (unreachable for an own child at the same UID) | `DENIED` ⇒ no further signal ⇒ T2 or T3 by identity availability |
| signal `EINTR` | bounded retry of the same signal within the existing deadline |
| `waitpid` returns `0` | `NOT_YET` ⇒ continue polling to the deadline |
| `waitpid` returns `pid_mid` | `PROVED_DEAD` ⇒ T1 |
| `waitpid` `ECHILD` | `PROVED_DEAD` (no auto-reaping exists in this contract) ⇒ T1 |
| `waitpid` `EINTR` | bounded retry; on expiry `INCONCLUSIVE` ⇒ T2/T3 |
| `waitpid` other error | `INCONCLUSIVE` ⇒ T2/T3 |
| **PID-reuse attempt** | before the reap the pid cannot be reused; a captured-identity mismatch is `2e` ⇒ no kill ⇒ T2/T3; after `PROVED_DEAD` the route never touches the pid again |
| restart **before** the middle's own bound | a CLI crash releases its fds and lock reference by kernel action; records of the attempt survive; the next attempt's P0–P3 governs; the middle exits at its own bound |
| restart **after** the middle's own bound | the middle is gone; P3 proves death by absence and removes the records |
| crash after `S1`, before any record action | no record removed; next attempt's P0–P3 governs |
| crash after the T2 `SPAWNING_MIDDLE.json` install, before the `SPAWNING.json` unlink | both records exist; the next preflight applies P1/P2/P3 to each in the child→group→middle→spawning order; a live middle is P2b-refused and later `s4`-resolved; the surviving `SPAWNING.json` names a **crashed** CLI, so P3 proves its death by absence and removes it |
| crash between the `SPAWNING.json` unlink and its `fsync` | the unlink may or may not be durable; both states are ENOENT-tolerant and identical to the next preflight |
| crash between any ordered unlink and its `fsync` in T1 | `child → group → middle → spawning` resumes, ENOENT-tolerant |
| crash after the final unlink, before the lock close | the crash releases the lock reference; no attempt state survives |
| crash after the lock close, before the refusal returns | attempt state absent; a second invocation starts clean |

**Death-before-unlink is preserved exactly**: in every row, no record naming the
grandchild, the group, or the middle child is removed without a proved death.
The only record ever removed without such a proof is `SPAWNING.json`, which
names the CLI performing the removal.

---

## V217.4. The full CLI-total-bound contradiction class (R4)

Closes Opus X216-M1.

### V217.4.1 The two false claims are deleted

§V216.4.1's sentence "Consequently no statement anywhere asserts that no
bootstrap syscall can outlive a deadline, or that every healthy launch releases
within the grandchild gate bound" is **replaced** by:

> After the replacements enumerated in §V217.4.2 and §V216.4.2, the operative
> chain contains no assertion that a bootstrap syscall cannot outlive a
> deadline, that every healthy launch releases within the grandchild gate
> bound, or that the CLI's total lifetime or lock-hold is fixed-bounded. This
> is a claim about the enumerated loci under the declared search terms of
> §V217.4.2, reproducible by any reviewer applying those terms to the operative
> documents; it is **not** an unconditional claim that no equivalent statement
> could exist in some other phrasing.

§V216.4.2's sentence "An exhaustive search of the operative chain for … yields
exactly these five loci; there are no others." is **replaced** by §V217.4.2's
table, which enumerates **six** additional stale loci that the five-locus claim
missed, including one — v2.1.2 §N11 — that neither the v2.1.6 search nor the
X-line finding enumerated.

### V217.4.2 Declared search terms and the complete locus table

**Search terms applied to every operative document** (v2 draft, v2.1, v2.1.1,
v2.1.2, v2.1.3, v2.1.4, v2.1.5, v2.1.6): `no blocking syscall`,
`healthy bootstrap`, `healthy launch`, `always releases`, `total bound`,
`Total CLI`, `No wait is unbounded`, `unbounded anywhere`, `arithmetic sum`,
`every CLI wait`, `CLI's total`, `CLI lifetime`, `total lifetime`,
`releases within`, `no unbounded`, `30 s + `, `bounded proof)`, `CLI wait`.

**Stale operative loci — the class Sol M3 required be totally eliminated:**

| # | Locus | Stale text | Action |
|---|---|---|---|
| 1 | v2.1.4 §V214.1.1 | "no blocking syscall exists anywhere in the bootstrap" | replaced in v2.1.6 §V216.4.1 |
| 2 | v2.1.4 §V214.1.5 | "No blocking syscall exists in the bootstrap…" | replaced in v2.1.6 §V216.4.1 |
| 3 | v2.1.4 test row 121 | "assert no blocking syscall exists" | replaced in v2.1.6 §V216.4.2 |
| 4 | v2.1.4 test row 126 | "a healthy bootstrap always releases inside it" | replaced in v2.1.6 §V216.4.2 |
| 5 | v2.1.4 §V214.1.1 grandchild paragraph | "a healthy bootstrap always releases well inside the bound" | replaced in v2.1.5 §V215.3.1 |
| **6** | **v2.1.2 §N3.5** | "Every CLI wait in this contract is bounded — … so a contract-following CLI **always releases within that arithmetic sum** (30 s + 10 s + 10 s + bounded proof)" | **replaced by §V217.4.3** |
| **7** | **v2.1.2 §N11 crash row** | "every contract-following CLI wait is bounded" | **replaced by §V217.4.3** — *not enumerated by v2.1.6's search and not named in the X-line finding; found by this layer's own sweep* |
| **8** | **v2.1.2 §N12 test row 86** | "no `flock` wait is unbounded anywhere; the CLI's total bound equals the stated arithmetic sum" | **replaced by §V217.4.4** |
| **9** | **v2.1.3 §U2.4** | "Total CLI bound: … (30 s + 30 s + bounded), all reusing existing constants. **No wait is unbounded.**" | **replaced by §V217.4.3** |
| **10** | **v2.1.3 §U2.7 residual 1** | "every contract-following CLI wait is bounded (§U2.4's arithmetic)" | **replaced by §V217.4.3** |

**Examined and retained — true, specific, non-universal statements** (recorded
so the search is demonstrably semantic rather than phrase-matching):

| Locus | Text | Why it is retained |
|---|---|---|
| v2.1 §W2.2 | "The CLI waits at most `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, polling at `T_SUPERVISOR_POLL_INTERVAL_NS`, for a live-verified identity" | bounds **one specific poll**, not a total; true |
| v2.1.1 §Z3.5 | "CLI wait: read the bootstrap line within `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`" | bounds **one specific pipe read**; true (and its block was already replaced by §N3.4–§N3.5) |
| v2.1.6 §V216.4.1 | "no bootstrap **pipe read or write** can block past its bounded helper deadline" | the accurate narrow invariant; retained |
| v2.1.5 §V215.3.1 | the grandchild gate as a fixed anti-wedge **policy**, with `/proc`/install/`fsync` explicitly unbounded | correct; retained |

### V217.4.3 The replacement statement for the CLI-bound class

Loci 6, 7, 9, and 10 are replaced by exactly this text:

> The CLI's `SPAWN.lock` acquisition is bounded by
> `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`, and each of its bootstrap pipe reads and
> writes is bounded by `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` through the §V214.1.3
> and §V214.1.4 helpers. The CLI's `/proc` reads and its canonical installs —
> including each file `fsync` and each parent-directory `fsync` — have **no
> executable duration bound in signed text**. Consequently the CLI's **total**
> lifetime and its **total** `SPAWN.lock` hold are **not** fixed-bounded, and
> no arithmetic sum expresses them; the previously stated sums are withdrawn.
> **D1 holds because no supervisor ever waits on `SPAWN.lock`** — the running
> supervisor's lifetime never depends on any client — and **not** because the
> CLI's total is bounded. A deliberately stopped or externally wedged same-UID
> client remains the signed A3 procedural residual and an operator matter; this
> contract does not authorize one client to kill another client process.

No unsigned deadline is introduced for `/proc` reads, installs, or `fsync`s,
and no new resource constant is created.

### V217.4.4 Replacement of test row 86, and joint satisfiability

```text
new row 86 | assert that SPAWN.lock acquisition is bounded by
             T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS and every bootstrap pipe read and
             write by T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS; assert that NO test and
             NO contract sentence asserts a fixed total CLI bound, a fixed
             arithmetic sum for CLI lifetime or lock-hold, or a duration bound
             for /proc reads, canonical installs, or fsyncs; assert that D1 is
             stated to hold because no supervisor waits on SPAWN.lock
             | R3, D1; R4, X216-M1
```

| Row | Obligation | Consistency |
|---|---|---|
| 86 (revised) | specific bounded waits + absence of any total-CLI or duration claim + D1's true ground | consistent with §V217.4.3; no longer asserts a total sum |
| 121 (v2.1.6) | pipe-only non-blocking + absence of duration-bound claims | same premise as 86; no overlap in obligation |
| 126 (v2.1.6) | deterministic slow-valid refusal + non-citability | behavioural; asserts no sufficiency |
| 159 | no text claims the grandchild bound suffices for every healthy launch | satisfiable |
| 160 / 161 / 162 | identity-state / artifact-absence / repetition complements of 126 | non-overlapping |

All six are jointly satisfiable: an implementation may leave `/proc`, installs,
and `fsync`s unbounded (as §V217.4.3 and §V216.4.1 require) while still passing
every bounded-wait assertion, because none of them now claims a total.

---

## V217.5. Crash-cut matrix (extends §V216.7)

Every §V216.7 row carries forward except where §V217.0 names a replacement.
Added rows:

| Cut | Single continuation |
|---|---|
| a canonical name is listed by the enumeration but `lstat` returns `ENOENT` | `OBSERVATION_INCONCLUSIVE` ⇒ record-first refusal/invalidity; release nothing |
| a canonical name is created after the enumeration but before its `lstat` | present (`absence_paired = false`); validity decides the rule; never absence |
| a canonical name becomes a symlink between `lstat` and `open` | `ELOOP` ⇒ `INVALID` ⇒ Rule 0 |
| a canonical name is removed between `lstat` and `open` | `OBSERVATION_INCONCLUSIVE` |
| a canonical name is replaced by a different regular file between `lstat` and `open` | `O6` `(dev, ino)` mismatch ⇒ `OBSERVATION_INCONCLUSIVE` |
| the read length or EOF offset disagrees with `fstat_size` | `OBSERVATION_INCONCLUSIVE` |
| the opposite terminal is installed after its presence observation, before branch entry | **barrier 1** ⇒ refusal/invalidity; **no branch entered**; release nothing |
| any canonical object changes between branch entry and the disposition | **barrier 2** ⇒ refusal/invalidity; **no `.disposed.json`, no release** |
| any canonical object changes after barrier 2 | **not prevented**; the named A3 procedural residual; non-citable; not claimed impossible |
| a record set spanning two `epoch_id`s | contract violation, not a route |
| `/proc` stat `EACCES`/`EPERM` | `UNREADABLE` ⇒ not identity-safe ⇒ no kill, no unlink ⇒ `WAIT_PROVE`, then T1/T2/T3 |
| `/proc` stat parse failure | `UNPARSABLE` ⇒ identical |
| `/proc` stat `EINTR` | bounded retry within the existing deadline; on expiry `ERROR` |
| `/proc` stat any other error | `ERROR` ⇒ identical to `UNREADABLE` |
| `kill` `ESRCH` | `GONE` ⇒ `WAIT_PROVE`; death is **never** inferred from `ESRCH` alone |
| `kill` `EINTR` | bounded retry of the same signal within the existing deadline |
| `kill` `EPERM` or other error | `DENIED`/`ERROR` ⇒ no further signal, no unlink ⇒ T2/T3 |
| SIGTERM sent, no death by `t0 + D/2` | SIGKILL sent; polling continues to `t0 + D` |
| a poll sample exactly at `t0 + D/2` or `t0 + D` | treated as expired (`≥`); no ambiguous edge |
| `waitpid` returns `pid_mid` | `PROVED_DEAD` ⇒ T1 |
| `waitpid` returns `0` | `NOT_YET` ⇒ continue polling |
| `waitpid` `ECHILD` | `PROVED_DEAD` — no auto-reaping exists, so a vanished child was reaped by this route |
| `waitpid` `EINTR` | bounded retry; on expiry `INCONCLUSIVE` |
| `waitpid` any other error | `INCONCLUSIVE` ⇒ T2/T3 |
| any stage-M exit | the CLI **always** removes its own `SPAWNING.json` while holding the lock |
| T2 with a live middle child | `SPAWNING_MIDDLE.json` survives as the handle; P2b refuses, then the existing `s4` tier resolves it after `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` |
| T3 at `c5`/`c6` | no record survives at all; the next attempt starts at P0 |
| a deliberately stopped middle child in T3 | named A3 procedural residual; the singleton stays held until that process is terminated; not claimed impossible |
| any claim that the CLI's total lifetime or lock-hold is fixed-bounded | **deleted**; only lock acquisition and pipe reads/writes are bounded, and D1 rests on "no supervisor waits on `SPAWN.lock`" |

---

## V217.6. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host change,
process, signature, activation, entropy, T/Q/C work, E1/E2/E3 spend, scientific
execution, or later gate is authorized. Obligations become due only after both
fresh independent v2.1.7 reviews confirm the bytes **and** the author signs the
amendment token.

§W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–85 and 87–96 (row **86**
replaced by §V217.4.4), §U11 rows 97–120, §V214.10 rows 122–125 and 127–144,
§V215.7 rows 145–149, 151–153, 155–156, 158–164, and §V216.6 rows 165–180 and
182–183 carry forward. Replaced:

- **row 181 replaced:** the contract text contains no universal "no blocking
  syscall", "healthy launch releases inside the bound", **or fixed-total-CLI
  bound** assertion; rows 86, 121, 126, and 159 are jointly satisfiable.
- **row 184 replaced:** no v2.1.6, v2.1.5, or earlier executable rule changed as
  a side effect — diff every non-replaced section body against the carried text,
  including §V216.1.2's rule structure, §V216.2, §V216.3.1, and §V216.5.

Added:

| # | Test | Covers |
|---|---|---|
| 185 | `OBSERVE` produces the exact record field set; every predicate reads only that record; no predicate re-`stat`s or re-reads a name | R1, Sol C1 |
| 186 | a symlink, directory, device, FIFO, socket, multiply-linked, zero-byte, truncated, and partially written canonical object each yield present + invalid, never absence | R1 |
| 187 | each of the seven `OBSERVATION_INCONCLUSIVE` triggers routes to record-first refusal/invalidity and releases nothing | R1 |
| 188 | `HS`/`HQ` consume the manifest record's `bytes_sha256` from the pinned descriptor; a swap after the read cannot change the compared value | R1 |
| 189 | **the Y-line attack**: install a canonical `QUARANTINE.json` after its presence observation and before branch entry ⇒ barrier 1 refuses; assert `B-P` is never entered and nothing is released | R1, Sol C1 |
| 190 | the symmetric attack (settlement installed after a `PS=0` observation) ⇒ barrier 1 refuses `B-QM` and `B-QN` | R1 |
| 191 | a mutation between branch entry and the disposition ⇒ barrier 2 refuses; no `.disposed.json`, no release | R1 |
| 192 | every row of the §V217.1.6 mutation-cut table behaves as tabulated | R1 |
| 193 | the contract contains no unconditional "impossible" claim for the post-barrier window; the residual is named, non-citable, and no security boundary is asserted | R1 |
| 194 | `STAT_OBSERVE` returns exactly one of the five results for each injected condition; no exception escapes | R2, Sol M1, X216-m1 |
| 195 | `UNREADABLE`, `UNPARSABLE`, and `ERROR` never authorize a kill, an unlink, or a death conclusion | R2 |
| 196 | `SIGNAL_ATTEMPT` returns exactly one of five results for success, `ESRCH`, `EINTR`, `EPERM`, and other errno; `ESRCH` alone never proves death | R2 |
| 197 | the SIGTERM→SIGKILL schedule uses `D/2` and `D` from the existing deadline; both edges are treated as expired at `≥` | R2 |
| 198 | `WAIT_PROVE` returns exactly one of three results for `pid`, `0`, `ECHILD`, `EINTR`, and other errno; `pid` and `ECHILD` prove death and nothing else does | R2 |
| 199 | assert no signal disposition is installed anywhere, so `SIGCHLD` keeps its default and no child is auto-reaped — the premise of the `ECHILD` rule | R2 |
| 200 | after `PROVED_DEAD` the route never signals, stats, or waits on `pid_mid` again | R2 |
| 201 | `WAIT_PROVE` succeeds with `/proc` made entirely unreadable, proving the death path is `/proc`-independent | R2, R3 |
| 202 | a stopped middle child is killed by SIGKILL and reaches `PROVED_DEAD` ⇒ T1 | R3, Sol M2 |
| 203 | **the Y-line wedge**: long-lived CLI, failure at `c5`/`c6`, each of T1/T2/T3 ⇒ the CLI's own `SPAWNING.json` is always removed and no future attempt is P2b-refused because of it | R3, Sol M2 |
| 204 | T2 installs `SPAWNING_MIDDLE.json` with the signed key set and no fabricated field; the existing `s4` tier resolves it after `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` | R3 |
| 205 | T3 fabricates nothing, removes only `SPAWNING.json`, and returns the named non-retryable terminal | R3 |
| 206 | death-before-unlink holds for `SPAWNING_CHILD`, `SPAWNING_GROUP`, and `SPAWNING_MIDDLE` in every terminal; only `SPAWNING.json` is removed without a proof | R3 |
| 207 | removing `SPAWNING.json` while a middle child may live cannot yield a second supervisor: `m5` sees EOF or its bound and never forks a grandchild | R3 |
| 208 | every row of §V217.3.5 — including restart before/after the middle's bound and every crash prefix — has one continuation and removes no live record | R3 |
| 209 | apply the §V217.4.2 search terms to every operative document and assert the found set equals the enumerated table; assert the retained statements are specific and true | R4, X216-M1 |
| 210 | no operative text asserts a fixed total CLI bound; §U2.4, §N3.5, §N11, §U2.7, and row 86 carry the replacement statement | R4 |
| 211 | D1's stated ground is "no supervisor waits on `SPAWN.lock`", not a CLI bound | R4, D1 |
| 212 | rows 86, 121, 126, 159, 160, 161, and 162 pass together against one implementation that leaves `/proc`, installs, and `fsync`s unbounded | R4 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## V217.7. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The selector consumes one
closed in-memory observation record per canonical name, produced by a nine-step
algorithm with seven named inconclusive triggers, and revalidated at two
barriers with a five-requirement predicate (§V217.1); every `/proc` read,
signal, and wait in stage M returns one of a closed enum with a pinned
continuation, and the death proof is `/proc`-independent (§V217.2); stage M has
three exhaustive terminals with a forward-progress table that uses only
existing routes (§V217.3); and the bound language is replaced at ten enumerated
loci under eighteen declared search terms, with the retained true statements
listed (§V217.4). No clause resolves to "as reviewed", "as appropriate", or
implementer discretion.

**Compatibility classification.** Unchanged: an engineering/control amendment
surface over the signed harness composite, containing no protocol amendment
except §W6.5's explicitly named supersession of harness §5a's physical
at-or-before-deadline sentence. The signed generic-harness contract
(v2/v2.1/v2.2/v2.3/v2.3.1) and the signed batch-settlement amendment
(v1/v1.1/v1.1.1, including §D1 head/cache completion and §D2 inline
`meter_evidence`) are referenced unchanged. No signed archival set, event,
runtime schema, root, constant, resource value, T band, or Q/C boundary moves.
The import-allowlist delta remains **none**.

**No author cell is reopened.** A3 is untouched and gains honesty: §V217.1.5
names the post-barrier selector window as a procedural, non-citable residual
instead of claiming impossibility, and §V217.3.4 names the stopped-middle
residual. B1 is untouched: no journal, acknowledgement, frontier, prefix, GC, or
classification rule changes. C1 is untouched: the watchdog remains a
witness/freezer holding no lock or capability, writing nothing under
`runtime/`, appending no ledger, and settling nothing. D1 is untouched and its
**true ground is now stated**: no supervisor waits on `SPAWN.lock`; §V217.3
also removes the wedge that could have blocked all future supervisor
construction. K1 is untouched: five constants unmoved, no replenishment,
write-once/hash-once counts unchanged, the three branch bodies unchanged, and
§V217.1's barriers **narrow** the window in which a release could be obtained
against a contradictory durable state. **No new author-choice token is
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
v2.1.7 bytes**; both lines revised v2.1.6, there was no X verdict for v2.1.5,
and no earlier confirmation of any version carries across.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
