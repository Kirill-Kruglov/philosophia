# Officina supervisor and control-channel amendment — v2.1.5 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1, v2.1.1,
v2.1.2, v2.1.3, and v2.1.4. It is **not** an independent X-line or Y-line
review of its own bytes and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain is an untrusted self-assessment; none of their claims is
used as evidence here. The only next authorization step is independent bounded
X/Y confirmation of the **v2.1.5 bytes**.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md`
(v2.1.4), which layers over v2.1.3, v2.1.2, v2.1.1, v2.1, and v2 — all six
preserved unedited as review evidence. **Everything not named in the §V215.0
replacement index carries forward verbatim.** Nothing earlier is rewritten or
silently reinterpreted.

**Authorization state, recorded exactly.** The X line **confirmed** v2.1.4
(`CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_X`) and made the token conditional on the
Y line confirming the same bytes. The Y line returned
`REVISE_OFFICINA_SUPERVISOR_V2_1_4` with two Major and two Minor findings, so
that condition was never met and the token never became signable. **The Y
verdict governs.** This layer repairs exactly those four findings and the exact
references they affect. Because the bytes change, **v2.1.5 requires a fresh
X-line and a fresh Y-line confirmation**; the v2.1.4 X confirmation applies to
the v2.1.4 bytes only and is not claimed to carry across.

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged** — every closure the X line
independently confirmed and every v2.1.4 repair not implicated by the four Y
findings: the nonblocking channel protocol and its two bounded helpers
(§V214.1.1's flags, §V214.1.3, §V214.1.4) and the stage-route map
(§V214.1.5's routing), including the `m7`→`m8` deadlock repair; the quarantine
manifest binding and the record-first reducer (§V214.2.1, §V214.2.2); the three
branch bodies `B-P`/`B-QM`/`B-QN` and the custody/retention/accounting
reconciliation (§V214.2.3's branch bodies, §V214.2.4); the GC order with
`accepted.json` last and its `D6` finalization (§V214.3); the lock-first
preflight order and the non-mutating stuck-holder route (§V214.4); the total
watchdog partition, `I1→I7` priority, exact-current-table `I2`, `I3`
absorption, and the fifteen-row race table (§V214.5); the four-residual A3
stream/inode/promoted distinction (§V214.6); the corrected 43-byte timestamp
example (§V214.7); and the whole carried v2/v2.1/v2.1.1/v2.1.2/v2.1.3 chain
(§N, §U, §W, §Z, §V2 surfaces) named as frozen in those layers.

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
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
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

**Zero new constants, zero new objects, zero new paths, zero new schemas, zero
new schema keys, zero new enum tokens, zero new refusal or `INVALID` tokens,
zero new public commands, zero new signed events, zero new resource values,
zero import-allowlist delta.** Every constant carries forward unchanged,
including the five immovable author-signed `T_OUTPUT_*` values,
`T_CONTROL_FRAME_MAX_BYTES = 4096`,
`T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000`,
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS = 10_000_000_000`,
`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS = 30_000_000_000`, and
`T_SPAWN_BOOTSTRAP_MAX_AGE_NS = 60_000_000_000`. The grandchild gate's
`2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` remains a derived arithmetic bound, not
a tunable. This layer uses only `os.close`, `os.pipe2`, `os.fork`,
`os.fpathconf`, `os.unlink`, `os.fsync`, `os._exit`, `os.stat`, `os.listdir`,
`hashlib`, and `json` — all inside `os`/`hashlib`/`json`, which are in
`ALLOWED_ABSOLUTE_IMPORTS`; `select`, `selectors`, `signal`, `ctypes`, and
`sys` remain outside it.

---

## V215.0. Exact replacement index (v2.1.4 → v2.1.5)

**No other text moves.** Everything in v2.1.4 and in every layer it carries —
in particular §V214.1.1's channel flags and `fpathconf` requirement,
§V214.1.2's ownership rows, §V214.1.3, §V214.1.4, §V214.1.5's stage-route map,
§V214.2.1, §V214.2.2, §V214.2.3's three branch bodies, §V214.2.4, §V214.3,
§V214.4, §V214.5, §V214.6, §V214.7, §V214.8.1, §V214.8.2, §V214.9, §V214.10,
§V214.11, and the entire carried §U/§N/§Z/§W/§V2 chain — carries forward
verbatim.

| v2.1.4 locus (exact sentence / clause / table row) | Action in v2.1.5 |
|---|---|
| §V214.2.3 opening sentence "Branch selection is decided by durable objects alone, **in this order**, and exactly one branch may apply:" | **replaced** by §V215.1.1 (a total ordered selector whose row predicates are literally exclusive, not an ordered prose implication) |
| §V214.2.3 selector code block (`B-P` / `B-QM` / `B-QN` lines and the `REFUSE … including:` list) | **replaced** by §V215.1.2 (five literal rows; the both-terminal row is tested first and dominates) |
| §V214.1.1 sentence "At creation the CLI verifies `os.fpathconf(fd, "PC_PIPE_BUF") ≥ T_CONTROL_FRAME_MAX_BYTES` on each of the four write ends … failure ⇒ no spawn attempt, `REFUSED`/`BOOTSTRAP` (retryable = false)." | **replaced** by §V215.2.3 (exact construction order, per-cut ownership, cleanup invocation, and the retryable distinction) |
| §V214.1.1 "**Grandchild gate bound.**" paragraph, in particular "The factor two is **required and sufficient**: … so a healthy bootstrap always releases well inside the bound" | **replaced** by §V215.3.1 (a fixed anti-wedge policy; the universal sufficiency claim is **deleted**) |
| §V214.1.2 descriptor table caption and scope ("normal" close points only) | **extended** by §V215.2.2 (the same rows plus a failure-path owner and the cleanup invocation, making the normal and failure tables jointly exhaustive) |
| §V214.1.5 stage-route paragraph "Every stage-1 and stage-2 route ends with the §U6.3 ordered record removal … and the already-signed identity/kill discipline." | **replaced** by §V215.2.4 (the exact four-step refusal sequence: kill/prove → fd cleanup → singleton removal → lock release) |
| §U2.2 step `c3` ("create the four channels of §U2.1"), as carried | **replaced** by §V215.2.3 (ordered creation with per-step ownership bookkeeping and per-failure routing) |
| §U2.2 step `c4` (`pid_mid = os.fork()`), as carried | **extended** by §V215.2.5 (the first-fork failure route: stage 0, no kill) |
| §U2.3 step `m7` (`pid_gc = os.fork()`), as carried | **extended** by §V215.2.6 (the second-fork failure route: middle-owned cleanup then `_exit(3)`, so `c13` observes EOF and takes stage 2) |
| §V214.8.3 sentence "The **six** v2.1.3 rows this layer repairs are re-read as:" and its six-row table | **replaced** by §V215.4 (the exact seven-row mapping) |
| §V214.9 crash-cut matrix | **extended** by §V215.6 (nineteen added rows) |
| §V214.10 test-obligation rows 121–144 | **extended** by §V215.7 (rows 145–164) |

---

## V215.1. Mutually exclusive terminal disposition branches (R1)

Closes Sol M1. The three branch **bodies** (`B-P`'s `P1`–`P5`, `B-QM`'s
`QM1`–`QM6`, `B-QN`'s `QN1`–`QN4`), §V214.2.4's custody/retention/accounting
reconciliation, the no-content-reread rule, and every §N1.5 conjunct are
**unchanged**. Only the selector changes.

### V215.1.1 The five literal predicates

All five are evaluated in **one held `T_RUNTIME.lock` epoch**, on one set of
directory-fd observations of the operation directory, with `O_NOFOLLOW`
throughout and no output content file opened. Define, over physical durable
objects:

```text
S  ≜ operations/<op>/SETTLEMENT.json is present as a regular file with
      st_nlink == 1, resolves with no symlink component, and validates against
      t-operation-settlement.v1 exactly (key set, types, hex grammars)
Q  ≜ operations/<op>/QUARANTINE.json satisfies the same three conditions
      against t-operation-quarantine.v1
B  ≜ Q ∧ QUARANTINE.json's result_manifest_sha256_or_null ≠ null
F  ≜ operations/<op>/RESULT_MANIFEST.json is present as a regular file with
      st_nlink == 1, resolves with no symlink component, and validates against
      t-operation-result-manifest.v1 exactly
HS ≜ S ∧ F ∧ SHA-256(the manifest file's exact canonical bytes)
          == SETTLEMENT.json's result_manifest_sha256
HQ ≜ B ∧ F ∧ SHA-256(the manifest file's exact canonical bytes)
          == QUARANTINE.json's result_manifest_sha256_or_null
MALFORMED ≜ any of SETTLEMENT.json, QUARANTINE.json, RESULT_MANIFEST.json is
      present at its canonical name but fails its regular-file / st_nlink /
      no-symlink / exact-schema test
```

`S`, `Q`, and `F` are **presence-and-validity** predicates: a present-but-
malformed object makes its predicate **false** and sets `MALFORMED`, so it can
never satisfy a branch. A partially written object cannot appear at a canonical
name, because every install is `same-directory temp → file fsync → atomic
no-replace rename → parent-directory fsync`; a surviving `.tmp` is not at a
canonical name and is caught as custody by the §N2.2 L4 temp-grammar class.
Duplicates are impossible at a single canonical path; any additional
`operation_id`-bearing entry is caught by the L5 unknown-name scan.

### V215.1.2 The total ordered selector

Exactly one row matches any state. The row predicates are **literally
disjoint**, so the ordering is a presentation aid rather than the semantics;
the both-terminal row is nevertheless stated first because it dominates.

| # | Literal predicate | Continuation |
|---|---|---|
| 1 | `S ∧ Q` | **record-first invalidity** naming both terminal paths; **release nothing**; no branch is entered |
| 2 | `S ∧ ¬Q ∧ HS` | **`B-P` only** (its `P1`–`P5` body, unchanged) |
| 3 | `¬S ∧ Q ∧ B ∧ HQ` | **`B-QM` only** (its `QM1`–`QM6` body, unchanged) |
| 4 | `¬S ∧ Q ∧ ¬B ∧ ¬F` | **`B-QN` only** (its `QN1`–`QN4` body, unchanged) |
| 5 | every other state — i.e. `¬(1) ∧ ¬(2) ∧ ¬(3) ∧ ¬(4)` | **release nothing**, by the §V215.1.3 sub-routing: an *impossible durable layout* takes **record-first invalidity**; an *ordinary not-yet-terminal* state takes **`REFUSE`** |

`B-P` now requires `¬Q`, and `B-QM`/`B-QN` now require `¬S`. The overlap Sol M1
identified — a both-terminal layout satisfying `B-P` *and* one `Q` branch while
the same paragraph also ordered `REFUSE` — is therefore impossible: row 1's
predicate is true and rows 2–4 are false by their own `¬Q` / `¬S` conjuncts.
There is exactly one continuation, and it releases nothing.

### V215.1.3 Row 5 sub-routing, and the complete truth table

Row 5 is single-valued by this literal partition:

```text
5a. MALFORMED                          ⇒ record-first invalidity naming the
                                         malformed path (an immutable
                                         no-replace object cannot legally be
                                         malformed)
5b. ¬S ∧ ¬Q ∧ ¬F                       ⇒ REFUSE (retryable = false): the
                                         operation has no terminal yet; this is
                                         an ordinary non-terminal state, not a
                                         defect
5c. ¬S ∧ ¬Q ∧ F                        ⇒ record-first invalidity: after the
                                         §V214.2.2 record-first reducer, which
                                         runs under the lock before any frame is
                                         served, a manifest without a terminal
                                         cannot exist
5d. S ∧ ¬Q ∧ ¬F                        ⇒ record-first invalidity: the manifest
                                         is never removed, so a settlement whose
                                         binding names an absent manifest is an
                                         impossible layout
5e. S ∧ ¬Q ∧ F ∧ ¬HS                   ⇒ REFUSE (retryable = false): hash
                                         mismatch; release nothing
5f. ¬S ∧ Q ∧ B ∧ ¬F                    ⇒ record-first invalidity: binding
                                         without file (the manifest is never
                                         removed)
5g. ¬S ∧ Q ∧ B ∧ F ∧ ¬HQ               ⇒ REFUSE (retryable = false): hash
                                         mismatch; release nothing
5h. ¬S ∧ Q ∧ ¬B ∧ F                    ⇒ record-first invalidity: orphan file
                                         without binding — the exact state
                                         §V214.2.2 Q3 already names
```

**Complete truth table.** Every reachable combination of the six predicates,
each with exactly one continuation. `—` means the predicate is not free in that
row (it is fixed by an earlier column).

| # | `S` | `Q` | `B` | `F` | hash | malformed | Row | Continuation |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | any | any | any | no | 1 | record-first invalidity (both terminals); release nothing |
| 2 | 1 | 0 | — | 1 | `HS` | no | 2 | **`B-P`**; on full success release exactly `bytes_reserved` |
| 3 | 1 | 0 | — | 1 | ¬`HS` | no | 5e | REFUSE; release nothing |
| 4 | 1 | 0 | — | 0 | — | no | 5d | record-first invalidity; release nothing |
| 5 | 0 | 1 | 1 | 1 | `HQ` | no | 3 | **`B-QM`**; on full success release exactly `bytes_reserved` |
| 6 | 0 | 1 | 1 | 1 | ¬`HQ` | no | 5g | REFUSE; release nothing |
| 7 | 0 | 1 | 1 | 0 | — | no | 5f | record-first invalidity; release nothing |
| 8 | 0 | 1 | 0 | 0 | — | no | 4 | **`B-QN`**; on full success release exactly `bytes_reserved` |
| 9 | 0 | 1 | 0 | 1 | — | no | 5h | record-first invalidity; release nothing |
| 10 | 0 | 0 | — | 0 | — | no | 5b | REFUSE (no terminal yet); release nothing |
| 11 | 0 | 0 | — | 1 | — | no | 5c | record-first invalidity; release nothing |
| 12 | any | any | any | any | any | **yes** | 5a | record-first invalidity naming the malformed path; release nothing |
| 13 | any | any | any | any | any | no | — | a surviving `.tmp` of any object: not at a canonical name, so it changes no predicate above; it is custody under the L4 temp-grammar class, so §N2.3's P5 refuses the disposition on custody grounds; release nothing |
| 14 | any | any | any | any | any | no | — | an additional `operation_id`-bearing entry under either fixed root: L5 unknown-name scan ⇒ §N2.3's P6 refuses; release nothing |

Rows 2, 5, and 8 are the only rows that can release, and each releases exactly
`bytes_reserved` exactly once, only after the branch body **and** §N2.3's
P1–P7 complete-absence proof **and** every §N1.5 conjunct succeed in the same
lock epoch. The legitimate `B-QM` K1 release restored in v2.1.4 is preserved
intact (row 5). No branch reads or rehashes an output content byte; every
custody, retention, accounting, and no-reread constraint of §V214.2.4 is
unchanged, and `bytes_reserved` remains the accounted contribution in every row
until a verified disposition installs `.disposed.json`.

---

## V215.2. Total bootstrap construction and cleanup (R2)

Closes Sol M2. §V214.1.1's flags, §V214.1.3's `BOUNDED_READ`, §V214.1.4's
`BOUNDED_WRITE`, and §V214.1.5's stage-route *map* are unchanged; what is added
is a total resource-lifecycle discipline around them.

### V215.2.1 The idempotent bootstrap-fd cleanup routine

Exactly one routine, parameterized only by the invoking process's current
ownership set (the §V215.2.2 table row for that process at that instant):

```text
BOOTSTRAP_FD_CLEANUP(owned):
  # `owned` is the set of bootstrap-channel descriptors this process still owns.
  # It is maintained by exactly two operations: a successful pipe2 ADDS both of
  # its ends; every close (normal or by this routine) REMOVES one end.
  for fd in the fixed order
        [boot_r, boot_w, rel1_r, rel1_w, rel2_r, rel2_w, rel3_r, rel3_w]:
      if fd ∉ owned: continue                  # never created, or already closed
      try:
          os.close(fd)
      except OSError with errno EBADF:
          # already closed: SUCCESS, not an error
          pass
      except OSError with errno EINTR:
          # On Linux close() releases the descriptor even when it returns EINTR.
          # The descriptor is therefore treated as CLOSED and is NEVER retried:
          # a retry could close a descriptor another part of the process has
          # since opened at the same number.
          pass
      except OSError with any other errno (e.g. EIO from a deferred flush):
          # the descriptor is released regardless; treat as CLOSED
          pass
      owned := owned \ {fd}
  # postcondition: owned == ∅
```

Normative properties: the routine **never raises**, **never leaves an owned
descriptor**, treats already-closed as success, closes each descriptor **at most
once**, and is **idempotent** — a second invocation with the resulting empty
set is a no-op. It touches no filesystem object, takes no lock, and kills
nothing. The `SPAWN.lock` descriptor is **not** a bootstrap channel end and is
never closed by this routine; it is released by its own pinned step or by
process exit.

### V215.2.2 Ownership, normal close, and failure owner — jointly exhaustive

The §V214.1.2 rows are unchanged and are extended with a failure-path column.
At **every instant** each of the eight ends is in exactly one of three states:
**(a)** not yet created (its `pipe2` has not returned successfully), **(b)**
owned by exactly the processes listed, or **(c)** closed. There is no fourth
state and no unowned open end.

| End | Added to `owned` when | Owners after `c5` | Normal close | Failure-path owner and closer |
|---|---|---|---|---|
| `boot_r` | `pipe2` #1 returns | CLI | CLI after `c13` | CLI ⇒ `BOOTSTRAP_FD_CLEANUP` |
| `boot_w` | `pipe2` #1 returns | middle; grandchild inherits a copy at `m7` | CLI at `c5`; middle at `m8`; grandchild at `g1` scrub | before `c4`: CLI ⇒ cleanup. middle ⇒ cleanup then `_exit(3)`. grandchild ⇒ cleanup then `_exit(3)` |
| `rel1_r` | `pipe2` #2 returns | middle | CLI at `c5`; middle at `m1` | as `boot_w` |
| `rel1_w` | `pipe2` #2 returns | CLI **and** middle until `m1` | CLI at `c8`; middle at `m1` | each owner ⇒ its own cleanup |
| `rel2_r` | `pipe2` #3 returns | middle | CLI at `c5`; middle at `m6` | as `boot_w` |
| `rel2_w` | `pipe2` #3 returns | CLI (middle closes its copy at `m1`) | CLI at `c12` | CLI ⇒ cleanup |
| `rel3_r` | `pipe2` #4 returns | middle (retained for inheritance), then grandchild | CLI at `c5`; grandchild at `g1` | middle ⇒ cleanup (this is what makes `c13` see EOF at `m7` failure); grandchild ⇒ cleanup |
| `rel3_w` | `pipe2` #4 returns | **CLI only** after `m1` | CLI at `c16`; middle at `m1` | CLI ⇒ cleanup |

Because the normal close points and the failure-path closers together cover
every end in every phase, and because `BOOTSTRAP_FD_CLEANUP` empties the
owning set, **no descriptor leak is reachable**. No uncaught language
exception, eventual process exit, garbage collection, finalizer, or implementer
convention owns any lifecycle transition: every close is either a pinned normal
step or a pinned cleanup invocation, and an exception propagating out of the
bootstrap is a **contract violation, not a route**.

### V215.2.3 Ordered construction, and every construction cut

`c3` is replaced by an ordered construction with explicit bookkeeping:

```text
c3.1 boot = os.pipe2(os.O_NONBLOCK)   ⇒ owned += {boot_r, boot_w}
c3.2 rel1 = os.pipe2(os.O_NONBLOCK)   ⇒ owned += {rel1_r, rel1_w}
c3.3 rel2 = os.pipe2(os.O_NONBLOCK)   ⇒ owned += {rel2_r, rel2_w}
c3.4 rel3 = os.pipe2(os.O_NONBLOCK)   ⇒ owned += {rel3_r, rel3_w}
c3.5 for fd in [boot_w, rel1_w, rel2_w, rel3_w] in that order:
        v = os.fpathconf(fd, "PC_PIPE_BUF")
        require v ≥ T_CONTROL_FRAME_MAX_BYTES
```

| Construction cut | Owned at the cut | Continuation |
|---|---|---|
| `c3.1` `pipe2` fails | ∅ | §V215.2.4 refusal sequence with an empty `owned`; `REFUSED`/`BOOTSTRAP`, **retryable = true** (a transient descriptor/memory condition: `EMFILE`, `ENFILE`, `ENOMEM`) |
| `c3.2` fails | `{boot_r, boot_w}` | same sequence; the routine closes exactly those two; retryable = true |
| `c3.3` fails | 4 ends | same; closes exactly those four; retryable = true |
| `c3.4` fails | 6 ends | same; closes exactly those six; retryable = true |
| `c3.5` `fpathconf` raises `OSError` | 8 ends | same; closes all eight; retryable = true |
| `c3.5` returns `v < T_CONTROL_FRAME_MAX_BYTES`, or a non-integer/`None` result | 8 ends | same; **retryable = false** — a host property that will not change between attempts |

### V215.2.4 The refusal sequence, invoked by **every** CLI failure path

```text
REFUSAL_SEQUENCE(stage, owned, records_installed):
  1. if the stage requires a kill (stage 1: kill(middle_child_pid) only;
     stage 2: killpg(process_group_id)): perform it under the already-signed
     identity discipline — validate pid + start identity first, never kill on a
     start-identity mismatch, then prove death by /proc absence or state Z, and
     os.waitpid only for own children.
     The kill precedes step 3 because it reads the very records step 3 removes.
  2. BOOTSTRAP_FD_CLEANUP(owned)                       (§V215.2.1; idempotent)
  3. if c2 completed (SPAWNING.json was installed by this attempt): the §U6.3
     ordered singleton removal — SPAWNING_CHILD.json → SPAWNING_GROUP.json →
     SPAWNING_MIDDLE.json → SPAWNING.json — each unlink followed by an fsync of
     T_SUPERVISOR/, ENOENT tolerated at every step, performed WHILE STILL
     HOLDING SPAWN.lock.
  4. release SPAWN.lock (close the lock fd).
  5. return REFUSED / BOOTSTRAP with the retryable value pinned by the cut.
```

This sequence is invoked by **every** CLI path that abandons the attempt:
`c1a` acquisition expiry (with an empty `owned` and no records of this
attempt), `c1b` preflight refusals, every `c3` construction cut, the `c4`
first-fork failure, every stage-1 and stage-2 helper route at
`c8`/`c9`/`c12`/`c13`/`c16`, and the `c17` identity-poll expiry. §V214.1.5's
sentence naming only the record removal and the kill discipline is replaced by
this four-step sequence, so **no live or partial singleton and no owned
descriptor can remain** on any refusal path.

### V215.2.5 First-fork (`c4`) failure

```text
c4 pid_mid = os.fork()          # raises OSError on EAGAIN/ENOMEM
   failure ⇒ NO child exists (a failed fork creates no process)
           ⇒ REFUSAL_SEQUENCE(stage 0, owned = all eight ends,
                              records_installed = {SPAWNING.json})
             — stage 0 performs NO kill, because there is nothing to kill and
               no identity has been recorded
           ⇒ REFUSED / BOOTSTRAP, retryable = true
```

### V215.2.6 Second-fork (`m7`) failure

```text
m7 pid_gc = os.fork()           # in the middle child; raises OSError
   failure ⇒ NO grandchild exists
           ⇒ BOOTSTRAP_FD_CLEANUP(middle-owned = {boot_w, rel3_r})
             — closing boot_w removes the LAST boot writer, because no
               grandchild exists to hold a copy
           ⇒ os._exit(3)         # the SPAWN.lock reference is released by exit
   consequence at the CLI: c13's BOUNDED_READ observes EOF immediately (not a
   deadline expiry), routes to stage 2, and REFUSAL_SEQUENCE(stage 2, …) kills
   the verified group (already dead), proves death, cleans its own fds, removes
   the four singleton records in order, and releases the lock.
```

This is the exact route Sol M2 required, and it is strictly faster than the
deadline path because the EOF is immediate.

### V215.2.7 Re-run: `c2`→`c18`, `m0`→`m9`, `g0`→identity, for every construction, fork, helper, and cleanup cut

| Cut | fds after cleanup | Singleton records after | Lock | Pipe cycle? |
|---|---|---|---|---|
| `c1a` expiry (stuck-holder route taken) | none created | untouched (the unlocked route mutates nothing) | not held | none |
| `c1b` preflight refusal (P1 malformed / P2b conflict) | none created | untouched — P1/P2b unlink nothing | released at step 4 | none |
| `c1b` P3 removal then refusal | none created | removed in §U6.3 order | released | none |
| `c2` install `EEXIST` unresolvable | none created | per P1/P2/P3 | released | none |
| `c3.1`–`c3.4` `pipe2` failure | **all owned closed** (0, 2, 4, or 6 ends) | all four removed in order | released | none |
| `c3.5` `fpathconf` failure or short `PIPE_BUF` | **all eight closed** | all four removed | released | none |
| `c4` fork failure | **all eight closed** | all four removed | released | none |
| `c5`–`c7` failure (identity read, record install) | CLI's four remaining ends closed | all four removed | released | middle is at `m0`; its bound or EOF exits it |
| `c8` write failure (`EPIPE`/deadline/other) | CLI ends closed after the stage-1 kill | all four removed | released | middle exits by `m0`/`m5` bound or EOF |
| `c9` read failure | as `c8` | all four removed | released | none |
| `c10` verification failure | as `c8` (stage 1) | all four removed | released | none |
| `c11` install failure | as `c8` (stage 1) | all four removed | released | none |
| `c12` write failure | stage-2 kill, then CLI ends closed | all four removed | released | middle killed by `killpg` |
| `c13` read failure (EOF or deadline) | stage-2 kill, then CLI ends closed | all four removed | released | grandchild, if any, killed by `killpg` |
| `c14`/`c15` failure | stage 2 | all four removed | released | as `c13` |
| `c16` write failure | stage 2 | all four removed | released | grandchild also EOFs on `rel3` |
| `c17` identity-poll expiry | stage 2 | all four removed | released | grandchild killed or self-exited |
| `c18` | normal path: CLI ends already closed at their normal points | records removed by the grandchild at `g3` | released | none |
| `m0`/`m5` gate failure | middle cleanup then `_exit(3)` | CLI removes them on its own route | released by exit | none |
| `m1`–`m4` failure | middle cleanup then `_exit(3)`; `c9` sees EOF | CLI removes | released by exit | none |
| `m7` fork failure | middle cleanup (`boot_w`, `rel3_r`) then `_exit(3)`; `c13` sees EOF | CLI removes | released by exit | none |
| `m8` write failure | middle cleanup then `_exit(3)` | CLI removes | released by exit | grandchild EOFs on `rel3` when the CLI cleans up |
| `m9` normal exit | middle's ends already closed at `m1`/`m6`/`m8` | — | released by exit | none |
| `g0` gate failure (EOF, error, or the §V215.3 bound) | grandchild cleanup then `_exit(3)` | CLI removes on its own route | released by exit | none |
| `g1`–`g2` failure (scrub, endpoints, watchdog, first-ack) | grandchild cleanup then `_exit(3)` after killing its watchdog by record and proving death | grandchild removes in §U6.3 order | released by exit | none |
| `g3` success | all bootstrap ends already closed at `g1` | grandchild removes all four in order | closed at `g3` | none |

In every row: no descriptor leak (the cleanup routine empties `owned`), no live
or partial `SPAWNING` conflict (step 3 removes all four in order, `ENOENT`
tolerated), no pipe cycle (each gate terminates by EOF, error, or its bound),
and no retained `SPAWN.lock` (step 4, or process exit).

---

## V215.3. Honest grandchild anti-wedge bound (R3)

Closes Sol m1. The bound's **value** is unchanged, and the signed constants are
untouched.

### V215.3.1 The bound is a fixed policy, not a proof

§V214.1.1's "**Grandchild gate bound.**" paragraph is replaced by:

> **Grandchild gate bound.** The `rel3` gate is bounded by
> `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, a derived arithmetic bound (no new
> constant), measured from the grandchild's own first monotonic sample. This
> is a **fixed anti-wedge policy, not a sufficiency proof.** `c14`'s `/proc`
> verification and `c15`'s atomic install — including its file `fsync` and its
> parent-directory `fsync` — have **no executable duration bound in any signed
> text**, so this contract makes **no claim** that every healthy launch
> completes inside the bound. The universal-sufficiency assertion of v2.1.4 is
> **deleted**. Expiry is therefore a **permitted fail-closed bootstrap
> refusal**, which may occur even for an otherwise valid but slow install; the
> attempt fails closed rather than wedging, which is the property the bound
> exists to guarantee.

### V215.3.2 The expiry route

```text
grandchild at g0, bound expires:
  BOOTSTRAP_FD_CLEANUP(grandchild-owned = {rel3_r, boot_w})
  os._exit(3)                    # the SPAWN.lock reference is released by exit
CLI consequence:
  c17's bounded identity poll finds no live-verified SUPERVISOR_IDENTITY.json
  ⇒ REFUSAL_SEQUENCE(stage 2, …): killpg(process_group_id) — the grandchild is
    already dead, and death is proved — then fd cleanup, then the §U6.3 ordered
    singleton removal, then lock release
  ⇒ REFUSED / BOOTSTRAP, retryable = true
Net state: no SUPERVISOR_IDENTITY.json is installed, no partial supervisor
  serves, no singleton record survives, no descriptor leaks, and SPAWN.lock is
  free.
```

### V215.3.3 The expiry is not evidence and is not a retry-shopping channel

- **Not evidence.** A bootstrap expiry is a control-plane refusal. It appends
  no ledger entry, installs no witness, fallback, replacement-freeze, capacity,
  custody, manifest, or invalidity object, and creates no datum. It is
  **T-development-only and permanently non-citable**: it may not enter
  selection, Q, C, C1–C6, any blinding claim, or any scientific or resource
  interpretation. It is not a `PROCESS`, `CLOCK`, or any other signed
  invalidity cause, because no process claim, lease, or capability exists at
  `g0`.
- **Not retry-shopping.** The refusal has **exactly one** continuation, so
  there is nothing to select between. `REFUSAL_SEQUENCE` removes every
  singleton record of the attempt, so **no state carries from one attempt to
  the next**: a repeated invocation starts from the same clean precondition and
  cannot accumulate partial state, adopt a foreign record, or reach a different
  class of outcome. The bootstrap creates no scientific, resource, capacity, or
  validity object at all, so no number of repetitions can obtain one. Client
  repetition remains bounded exactly as §Z1.8 already bounds it (at most two
  re-anchorings per intent, then exit `4`), and `retryable = true` here means
  only that a later attempt is *permitted*, never that a different outcome is
  *available*.

---

## V215.4. Corrected v2.1.3 provenance mapping (R4)

Closes Sol m2. §V214.8.3's sentence "The **six** v2.1.3 rows this layer repairs
are re-read as:" and its six-row table are replaced by the exact **seven**-row
mapping. This is **provenance repair only**: it changes no executable rule, no
predicate, and no section body, and it relabels no finding.

| v2.1.3 Y-line finding | Repaired by |
|---|---|
| **C1** blocking `boot_pipe`/`rel3` and unpinned pipe errno branches | **§V214.1** |
| **C2** orphan-manifest quarantine undisposable | **§V214.2** |
| **M1** GC destroys the G3 authority | **§V214.3** |
| **M2** singleton preflight ordered both before and under the lock | **§V214.4** |
| **M3** watchdog replacement partition / ack / condition selection not total | **§V214.5** |
| **M4** false promoted-byte claim for a during-pass mixed stream | **§V214.6** |
| **m1** decision-file line-8 byte miscount | **§V214.7** |

The v2.1.4 table it replaces mapped C2 to the replacement-state section, shifted
M2 and M3 by one section each, labelled **M4** as "m2", omitted **m1**
entirely, and called seven repairs "six rows". The operative sections and the
§V214.0 replacement index were and remain correct; only that summary table was
wrong.

The surrounding qualification is restated for v2.1.5: every closure recorded in
§V214.8.3, §U9.4, §N10.3, §Z12.1, and every prior author closure now reads
**"closed in v2.1.4 (or earlier); confirmation pending independent v2.1.5
X/Y"**. The X line **confirmed** the v2.1.4 bytes and the Y line **revised**
them; **the Y verdict governs the authorization state**, the token never became
signable, and because v2.1.5 changes the bytes, **the v2.1.4 X confirmation
does not carry across** — a fresh X-line and a fresh Y-line confirmation are
required. No closure in this document is asserted by author fiat; the author
line cannot confirm its own bytes.

---

## V215.5. Object, authority, and reconciliation delta

**No object, path, schema, schema key, enum token, refusal token, constant,
command, event, resource value, root, or import changes in this layer.**
§V214.8.1's durable-object table and §V214.8.2's reconciliation table carry
forward verbatim. The four repairs are:

| Repair | Nature of change |
|---|---|
| §V215.1 | predicate rewrite of one selector; three branch bodies unchanged |
| §V215.2 | one new *routine* and one new *sequence*, both defined entirely over existing descriptors and existing records; no artifact is created or removed that was not already governed |
| §V215.3 | deletion of one claim and pinning of the already-existing expiry route |
| §V215.4 | correction of one summary table |

Every new statement is a literal predicate, a fixed-order loop over existing
descriptors, a closed `errno` disposition, or a mapping row. No free text, no
implementer discretion, no hidden author judgment, and no scientific, resource,
or invalidity value is introduced.

---

## V215.6. Crash-cut matrix (extends §V214.9)

Every §V214.9 row carries forward except where §V215.0 names a replacement.
Added rows:

| Cut | Single continuation |
|---|---|
| both `SETTLEMENT.json` and `QUARANTINE.json` durable | selector row 1: record-first invalidity naming both paths; **no branch is entered**; release nothing |
| settlement durable, quarantine absent, manifest present, hash matches | `B-P` only |
| settlement durable, quarantine absent, manifest present, hash mismatches | REFUSE (5e); release nothing |
| settlement durable, quarantine absent, manifest absent | record-first invalidity (5d) |
| quarantine durable, settlement absent, binding non-null, manifest present, hash matches | `B-QM` only |
| quarantine durable, settlement absent, binding non-null, hash mismatches | REFUSE (5g) |
| quarantine durable, settlement absent, binding non-null, manifest absent | record-first invalidity (5f) |
| quarantine durable, settlement absent, binding null, manifest absent | `B-QN` only |
| quarantine durable, settlement absent, binding null, manifest present | record-first invalidity (5h) |
| neither terminal, no manifest | REFUSE (5b); an ordinary non-terminal operation |
| neither terminal, manifest present | record-first invalidity (5c) |
| any terminal or the manifest present but malformed | record-first invalidity naming that path (5a) |
| `pipe2` failure at creation 1, 2, 3, or 4 | close exactly the ends created so far, remove all four singleton records in order, release the lock, `REFUSED`/`BOOTSTRAP` retryable = true |
| `fpathconf` raises, or returns `< T_CONTROL_FRAME_MAX_BYTES` | close all eight ends, remove all four records, release the lock; retryable = **false** (host property) for the short-`PIPE_BUF` case, true for the raise |
| `c4` first `os.fork` failure | stage 0: **no kill**; close all eight; remove all four; release; retryable = true |
| `m7` second `os.fork` failure | middle closes `boot_w` and `rel3_r`, then `_exit(3)`; the CLI's `c13` sees **EOF immediately** and takes the stage-2 sequence |
| any close in the cleanup routine returns `EBADF` | treated as success; the routine continues and never raises |
| any close returns `EINTR` or another `errno` | the descriptor is treated as **closed** and is **never retried**; the routine continues |
| the cleanup routine is invoked twice on one path | the second invocation is a no-op (its `owned` set is already empty) |
| grandchild gate bound expires during a slow but otherwise valid `c14`/`c15` | grandchild cleanup then `_exit(3)`; the CLI's `c17` expiry takes stage 2; the whole attempt fails closed; the expiry is non-citable and creates nothing |

---

## V215.7. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host
change, process, signature, activation, entropy, T/Q/C work, E1/E2/E3 spend, or
scientific execution is permitted. Obligations become due only after both
fresh independent v2.1.5 confirmations accept these bytes **and** the author
signs the amendment token.

§W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–96, §U11 rows 97–120, and
§V214.10 rows 121–144 carry forward unchanged. Added:

| # | Test | Covers |
|---|---|---|
| 145 | every row of the §V215.1.3 truth table yields exactly the tabulated continuation; assert that no state satisfies two rows | R1, Sol M1 |
| 146 | a both-terminal layout enters **no** branch and takes record-first invalidity; assert no release path is reachable from it | R1 |
| 147 | `B-P` requires `¬Q` and `B-QM`/`B-QN` require `¬S`; a test that installs the opposite terminal after selection begins still cannot release (the selector and branch share one lock epoch) | R1 |
| 148 | the legitimate `B-QM` release still works end-to-end after the selector rewrite: orphan manifest + complete custody absence ⇒ exactly one release of exactly `bytes_reserved` | R1, K1 |
| 149 | present-but-malformed settlement, quarantine, or manifest ⇒ record-first invalidity naming that path; a surviving `.tmp` ⇒ custody refusal via L4; an extra `operation_id`-bearing entry ⇒ L5 refusal | R1 |
| 150 | `BOOTSTRAP_FD_CLEANUP` closes each owned end exactly once, treats `EBADF` as success, treats `EINTR` and other errno as closed without retry, never raises, and is a no-op on a second invocation | R2, Sol M2 |
| 151 | `pipe2` failure injected at each of the four creations closes exactly the ends created so far and leaks none | R2 |
| 152 | `fpathconf` raise and short-`PIPE_BUF` each close all eight ends and yield the pinned `retryable` value | R2 |
| 153 | `c4` fork failure performs **no kill**, closes all eight, removes all four records in order with fsyncs, and releases the lock | R2 |
| 154 | `m7` fork failure closes `boot_w`/`rel3_r` and `_exit(3)`s; the CLI's `c13` observes **EOF** (not a deadline) and completes stage 2 | R2 |
| 155 | every CLI refusal path executes the four-step `REFUSAL_SEQUENCE` in order, with the kill before the record removal | R2 |
| 156 | after every cut in §V215.2.7: zero leaked descriptors, zero surviving singleton records, `SPAWN.lock` free, and no live pipe cycle | R2 |
| 157 | assert that no bootstrap lifecycle transition is owned by an uncaught exception, process exit, or finalizer: every syscall site has a pinned route | R2 |
| 158 | a long-lived caller repeating failed attempts accumulates no descriptors and no records across attempts | R2 |
| 159 | the contract text contains **no** claim that `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` is sufficient for every healthy launch | R3, Sol m1 |
| 160 | a deliberately slow but valid `c14`/`c15` that exceeds the gate ⇒ grandchild `_exit(3)`, CLI stage 2, whole attempt fails closed, no identity installed, no partial supervisor serves | R3 |
| 161 | the expiry creates no ledger entry, witness, fallback, capacity, custody, manifest, invalidity, or datum, and is not citable | R3 |
| 162 | repeated attempts after an expiry cannot reach a different class of outcome and cannot adopt a foreign record | R3 |
| 163 | the §V215.4 provenance table maps exactly C1→§V214.1, C2→§V214.2, M1→§V214.3, M2→§V214.4, M3→§V214.5, M4→§V214.6, m1→§V214.7 — seven rows | R4, Sol m2 |
| 164 | no v2.1.4 executable rule changed as a side effect of the provenance repair: diff every §V214 body against the carried text | R4 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## V215.8. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The disposition selector is
five literal predicates over six named observations, with a fourteen-row truth
table in which the both-terminal row dominates (§V215.1); the bootstrap has one
idempotent cleanup routine with a closed `errno` disposition, one four-step
refusal sequence invoked by every failure path, an ordered construction with
per-step ownership bookkeeping, and a jointly exhaustive normal/failure
ownership table (§V215.2); the grandchild bound is stated as a policy with its
expiry route, non-evidence status, and non-shopping property pinned (§V215.3);
and the provenance mapping is exact (§V215.4). No clause resolves to "as
reviewed", "as appropriate", or implementer discretion.

**Compatibility classification.** Unchanged: an engineering/control amendment
surface over the signed harness composite, containing no protocol amendment
except §W6.5's explicitly named supersession of harness §5a's physical
at-or-before-deadline sentence. The signed generic-harness contract
(v2/v2.1/v2.2/v2.3/v2.3.1) and the signed batch-settlement amendment
(v1/v1.1/v1.1.1, including §D1 head/cache completion and §D2 inline
`meter_evidence`) are referenced unchanged. No signed archival set, event,
runtime schema, root, constant, resource value, T band, or Q/C boundary moves.
The import-allowlist delta remains **none**.

**No author cell is reopened.** A3 is untouched: the four residuals, their
non-citability, and the absence of a `HASH` route are carried verbatim, and
§V215.3.3 adds one more explicitly non-citable control-plane fact rather than a
new claim. B1 is untouched: no journal, acknowledgement, prefix, GC, or
classification rule changes. C1 is untouched: the watchdog remains a
witness/freezer that holds no lock, writes nothing under `runtime/`, appends no
ledger, and settles nothing. D1 is untouched and strengthened in practice:
§V215.2 removes the last constructions in which a bootstrap participant could
leak a descriptor or leave a singleton record, and no supervisor waits on
`SPAWN.lock`. K1 is untouched: five constants unmoved, no replenishment,
literal write-once/hash-once counts, `bytes_reserved` accounted until a
verified disposition, and §V215.1 **preserves** the `B-QM` release route while
removing the ambiguity that could have released capacity in an invalid layout.
**No new author-choice token is proposed, and none was found to be
unavoidable.**

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
signable** and is not made signable here. Its only next authorization step is
independent bounded X/Y confirmation of the **v2.1.5 bytes**, by a fresh
X-line and a fresh Y-line; no earlier confirmation carries across.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
