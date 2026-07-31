# Officina supervisor and control-channel amendment — v2.1.4 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1, v2.1.1,
v2.1.2, and v2.1.3. It is **not** an independent X-line or Y-line review of its
own bytes and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every prior
author closure is an untrusted self-assessment; none of their claims is used as
evidence here. The only next authorization step is independent bounded X/Y
confirmation of the **v2.1.4 bytes**.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md`
(v2.1.3), which layers over v2.1.2, v2.1.1, v2.1, and v2 — all five preserved
unedited as review evidence. **Everything not named in the §V214.0 replacement
index carries forward verbatim.** Nothing earlier is rewritten or silently
reinterpreted. It repairs exactly the findings of the two independent v2.1.3
reviews
(`reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md`,
which **confirmed** v2.1.3 on the X line while recording two Minors, and
`reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md`,
which required revision) and the exact references those repairs affect.

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged**, each independently confirmed by
the X line and, where noted, by the Y line, and **not reopened here**: the
acyclic content-closed custody-disposition authority (§N1.1–§N1.4, §N1.7,
§N1.8); the complete protocol-created custody-location set and its paired
absence observations (§N2.1–§N2.4, §N2.6, §U5.5's L2 set); literal K1
write-once/hash-once **counts** (§N4.1–§N4.3, §U1.5's normative bar); the
rejected-witness fallback namespace (§N5.1–§N5.5); the collision-safe fd remap
(§N6.1–§N6.3); the acknowledgement priority rule and published frontier
(§N7.1–§N7.3); the per-command archival predicates (§N8.2); prefix-first
classification (§N8.3); absent-scope defaults (§N9.1); the canonical
empty-result hash (§N9.2); the two-stage middle-child gate and verified group
identity (§U2.2–§U2.7, repaired only in its channel mechanics); the swap-only
versus deadline freeze split (§U3.1); the immutable per-transition markers
(§U3.3); the durable result manifest and its `SETTLEMENT.json` binding
(§U5.1–§U5.3, §U5.6); the singleton-record preflight semantics (§U6.1–§U6.5,
reordered only with respect to the lock); the byte-bound author timestamp
(§U7.1, §U7.2, §U7.4); and the deterministic custody-proof summary (§U8).

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
6cc52972e6229005f98d15db0fac113a77d2c2382133cc745f387fced845b008  reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
214ac0d5fb1cecf873e8b91ca95079dc67df8018762a18df46e94cb912d7df75  reviews/sol_officina_supervisor_control_channel_v2_1_3_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

## Engineering constants

**Zero new constants.** Every constant carries forward unchanged, including
the five immovable author-signed `T_OUTPUT_*` values,
`T_CONTROL_FRAME_MAX_BYTES = 4096`,
`T_CONTROL_READ_BUFFER_MAX_BYTES = 8192`,
`T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000`,
`T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS = 1_000_000_000`,
`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS = 60_000_000_000`,
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS = 10_000_000_000`,
`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS = 30_000_000_000`, and
`T_SPAWN_BOOTSTRAP_MAX_AGE_NS = 60_000_000_000`. The one new bound in this
layer — the grandchild gate's — is the **arithmetic** `2 ×
T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, not a new tunable. The import-allowlist
delta remains **none**: this layer uses only `os.pipe2` with `os.O_NONBLOCK`,
`os.read`, `os.write`, `os.close`, `os.unlink`, `os.rmdir`, `os.fsync`,
`os.fpathconf`, `time.clock_gettime_ns`, `hashlib`, and `json` — all inside
`os`/`time`/`hashlib`/`json`, which are in `ALLOWED_ABSOLUTE_IMPORTS`;
`select`, `selectors`, `signal`, `ctypes`, and `sys` remain outside it.

---

## V214.0. Exact replacement index (v2.1.3 → v2.1.4)

Everything else carries forward verbatim, including v2.1.3 §U1.4, §U1.5,
§U2.3 (`m0`–`m9` step order), §U2.5 (tiers and kill discipline), §U2.7, §U3.1,
§U3.3 (except one added key), §U3.4, §U4.3, §U5.1–§U5.3, §U5.5, §U5.6,
§U6.2–§U6.5, §U7.1, §U7.2, §U7.4, §U8, §U9, and every v2/v2.1/v2.1.1/v2.1.2
section those sections carry.

| v2.1.3 locus (exact sentence / clause / table row) | Action in v2.1.4 |
|---|---|
| §U1.1's replacement sentence "…`content_sha256` accurately describes the bytes read through the inode-verified descriptor during that pass." | **replaced** by §V214.6.1 (the hash describes exactly the byte **stream read**, which need not equal any single file state) |
| §U1.2 row "that `content_sha256` describes the bytes read during the pass \| **yes, by construction**" | **replaced** by §V214.6.2 (row restated as "the exact byte stream read", with three new NO rows separating stream / final inode / promoted bytes) |
| §U1.2 rows "same-inode equal-size in-place modification **before** the pass" and "…**during** the pass" | **replaced** by §V214.6.2 (split into A3-R1a and A3-R1b with distinct consequences) |
| §U1.3's `A3-R1` block, in particular the clause "Nothing is inconsistent — the recorded hash still truthfully describes the promoted bytes — but the bytes are not provably the worker's." | **replaced** by §V214.6.3 (`A3-R1a` / `A3-R1b`; the promoted-byte claim is **deleted**) |
| §U1.3's `A3-R2` block clause "The pass establishes no future immutability, and this contract does not claim it does." | **extended** by §V214.6.3 (adds that `result_sha256` can therefore differ from the promoted bytes) |
| §U2.1 line `boot_pipe = os.pipe2(0)` | **replaced** by §V214.1.1 (`os.pipe2(os.O_NONBLOCK)`) |
| §U2.1 line `rel3 = os.pipe2(0)` and the sentence "`rel3` keeps v2.1.2's blocking-read + EOF design **unchanged**…" | **replaced** by §V214.1.1 (`os.pipe2(os.O_NONBLOCK)` with a derived bound; every EOF property is preserved and is now an early-exit rather than the sole guarantee) |
| §U2.1 ownership table | **replaced** by §V214.1.2 (complete descriptor/flag/errno ownership table) |
| §U2.2 step `c1` ("§U6.1 singleton preflight, then acquire SPAWN.lock…") | **replaced** by §V214.4.1 (`c1a` acquire, `c1b` preflight under the acquired lock) |
| §U2.2 step `c8`, §U2.4 steps `c9`, `c12`, `c13`, `c16` (each stating a read or write without an errno branch set) | **replaced** by §V214.1.3–§V214.1.4 (every stage read/write is one pinned helper invocation with a named stage route) |
| §U2.3 steps `m0`, `m4`, `m5`, `m8` (each stating a read or write without an errno branch set) | **replaced** by §V214.1.3–§V214.1.4 (same helpers; `_exit(3)` routes) |
| §U2.6 row "after `c4`, before `c7`", clause "**CLI death:** its `rel1` write end closes ⇒ `m0` sees EOF ⇒ `_exit(3)`" | **replaced** by §V214.1.5 (the middle child holds its own `rel1` write copy until `m1`, so the governing guarantee is the `m0` bound; EOF is an additional early exit only once every writer has closed) — closes Opus X213-m2 |
| §U2.6 row "after `m7`, before `m8`", clause "middle death ⇒ no EOF (the grandchild holds a `boot` write copy) ⇒ `c13`'s bound expires ⇒ stage-2 route" | **replaced** by §V214.1.5 (the bound is now executable because `boot` is nonblocking; the row previously asserted a timeout that a blocking `os.read` could never reach) |
| §U2.6 automaton table (every row referencing a stage read or write) | **replaced** by §V214.1.5 |
| §U3.2 condition `I2` ("…or no ack of any `table_seq` within…") | **replaced** by §V214.5.2 (no **valid** ack of the **exact current** `table_seq` by the bound; stale, wrong-table, wrong-generation, and malformed acks never satisfy it) |
| §U3.2 condition `I3` | **replaced** by §V214.5.2 (includes every pre-resume member state other than exactly `T` after identity match) |
| §U3.2 clause "`INVALID` if **ANY** of:" and "⇒ install `<replacement_freeze_id>.invalidated.json` (§U3.3) naming the exact triggering condition" | **replaced** by §V214.5.1 (pinned priority `I1 → I2 → … → I7`; the marker records the **first true** condition plus a sorted diagnostic set) |
| §U3.2 `RESUMABLE` clause `S2` | **replaced** by §V214.5.3 (exactly `T`; its negation is I3, so no S1-true/S2-false gap remains) |
| §U3.2 `ACK_PENDING` paragraph "…i.e. not INVALID, and S1 not yet satisfied" | **replaced** by §V214.5.3 (the exact remaining state of an exhaustive, disjoint partition) |
| §U3.3 `t-replacement-invalidation.v1` key list | **replaced** by §V214.5.4 (adds `diagnostic_conditions`) |
| §U4.1 block `D0`–`D8` (the whole deletion order) | **replaced** by §V214.3.1 (`committed → reply → ack → accepted` last, with a finalization rule) |
| §U4.1 "**Empty-directory completion rule**" paragraph | **replaced** by §V214.3.1 (unchanged in effect, but reachable only after `accepted.json` is gone) |
| §U4.2 crash-cut table and its closing paragraph "**Why `ack.json` last is exactly sufficient.**" | **replaced** by §V214.3.2–§V214.3.3 (the prefix proof now uses only the files present after each cut) |
| §U5.2 crash row "crash after the manifest, before `SETTLEMENT.json`" | **extended** by §V214.2.2 (the record-first reducer installs a quarantined terminal that **binds** the orphan manifest) |
| §U5.4 verifier block `V1`–`V6` | **replaced** by §V214.2.3 (three exclusive branches: `B-P`, `B-QM`, `B-QN`) |
| §W4.7 `t-operation-quarantine.v1` key list, as carried | **replaced** by §V214.2.1 (adds `result_manifest_sha256_or_null`) |
| §U6.1 opening sentence "Under `SPAWN.lock`, **before `c2`**, for each record…" | **replaced** by §V214.4.1 (under the **acquired** lock, at `c1b`, before `c2`) |
| §U2.5 stuck-holder steps `s2`, `s3`, `s4`, each clause "remove records per §U6.3, retry the bounded acquisition exactly once" | **replaced** by §V214.4.2 (the unlocked stuck-holder route **kills but removes nothing**; removal happens at `c1b` under the acquired lock) |
| §U7.3 line "decision file, line 8 (44 bytes incl. LF):" | **replaced** by §V214.7 (**43** bytes incl. LF) |
| §U9.1 durable-object table rows for the quarantine record and the invalidation marker | **extended** by §V214.8.1 |
| §U10 crash-cut matrix | **extended** by §V214.9 (twenty-four added or replaced rows) |
| §U11 test-obligation rows 97–120 | **extended** by §V214.10 (rows 121–144); rows 101, 105, 112, 113, and 117 are **replaced** |
| §U9.4 inherited-closure qualification | **extended** by §V214.8.3 (v2.1.3 closures marked *confirmation pending v2.1.4*) |

---

## V214.1. Actually bounded pipe protocol and every errno branch (R1)

Closes Sol C1 and Opus X213-m2.

### V214.1.1 All four channels are nonblocking

```text
boot_pipe = os.pipe2(os.O_NONBLOCK)   # reports → CLI; CLI holds the read end
rel1      = os.pipe2(os.O_NONBLOCK)   # stage-1 release, CLI → middle child
rel2      = os.pipe2(os.O_NONBLOCK)   # stage-2 release, CLI → middle child
rel3      = os.pipe2(os.O_NONBLOCK)   # stage-3 release, CLI → grandchild
```

Both ends of all four are `O_NONBLOCK`, so **no blocking syscall exists
anywhere in the bootstrap** and every gate, report, and release can evaluate
its deadline. At creation the CLI verifies
`os.fpathconf(fd, "PC_PIPE_BUF") ≥ T_CONTROL_FRAME_MAX_BYTES` on each of the
four write ends, exactly as §V2.4.1 already requires of control endpoints;
failure ⇒ no spawn attempt, `REFUSED`/`BOOTSTRAP` (retryable = false).

**What changes and what is preserved.** v2.1.3 left `boot_pipe` and `rel3`
blocking. Sol C1 showed the consequence: at `c13` the CLI could block forever
on a descriptor that can never reach EOF (the grandchild retains a `boot`
write copy) while the grandchild waits for a release the blocked CLI cannot
send — an ordinary cut that retains the fork-shared lock indefinitely. Making
the read ends nonblocking makes the already-specified bounds executable.

Every previously confirmed property is preserved exactly:

- `rel3`'s **EOF-on-CLI-death** property is unchanged: the middle child still
  closes its `rel3` write copy at `m1`, before the second fork, so the CLI
  remains the grandchild's **sole** `rel3` writer and its death still delivers
  EOF. EOF is now an *early exit* rather than the only guarantee.
- The grandchild's **literal first instruction is still its `rel3` gate read**
  (§N3.4/§U2.3, unchanged): it executes nothing else — not even a descriptor
  close — before `SPAWNING_CHILD.json` is durable.
- The middle child's literal first instruction is still its `m0` gate read.
- The grandchild's inherited `boot` **write** copy is **not** closed early. It
  is scrubbed at `g1` with every other inherited descriptor, exactly as
  confirmed. §V214.1.5 proves that the CLI's nonblocking bound alone makes
  every cut total, so **no route depends on EOF from `boot`**; EOF, when it
  happens, is only an earlier exit from the same route.

**Grandchild gate bound.** The `rel3` gate is bounded by
`2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` (a derived arithmetic bound, not a new
constant), measured from the grandchild's own first monotonic sample. The
factor two is required and sufficient: between `m7` (when the grandchild
begins waiting) and `c16` (the release) the CLI performs at most one bounded
`boot` read (`c13`, ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`) plus `c14`'s
`/proc` verification and `c15`'s atomic install, so a healthy bootstrap always
releases well inside the bound, while a wedged one is exited by it. On expiry,
EOF, or any error the grandchild takes `os._exit(3)`, releasing its lock
reference.

### V214.1.2 Descriptor, flag, ownership, and errno table

| Channel / end | Created | Flags | Held by | Closed by / when | Direction | Errno set handled |
|---|---|---|---|---|---|---|
| `boot` read | CLI, pre-fork | `O_NONBLOCK` | CLI | CLI after `c13` | CLI reads at `c9`, `c13` | `EAGAIN`/`EWOULDBLOCK`, `EINTR`, EOF, other |
| `boot` write | CLI, pre-fork | `O_NONBLOCK` | middle child (from `c4`); grandchild inherits a copy at `m7` | CLI at `c5`; middle child at `m8`; grandchild at `g1` scrub | middle child writes at `m4`, `m8` | `EAGAIN`, `EINTR`, `EPIPE`, other |
| `rel1` read | CLI, pre-fork | `O_NONBLOCK` | middle child | CLI at `c5`; middle child at `m1` | middle child reads at `m0` | `EAGAIN`, `EINTR`, EOF, other |
| `rel1` write | CLI, pre-fork | `O_NONBLOCK` | CLI **and** middle child until `m1` | CLI at `c8` (after the release); middle child at `m1` | CLI writes at `c8` | `EAGAIN`, `EINTR`, `EPIPE`, other |
| `rel2` read | CLI, pre-fork | `O_NONBLOCK` | middle child | CLI at `c5`; middle child at `m6` | middle child reads at `m5` | as `rel1` read |
| `rel2` write | CLI, pre-fork | `O_NONBLOCK` | CLI; middle child closes its copy at `m1` | CLI at `c12` | CLI writes at `c12` | as `rel1` write |
| `rel3` read | CLI, pre-fork | `O_NONBLOCK` | grandchild (inherited via the middle child) | CLI at `c5`; middle child at `m1`? **no** — the middle child retains `rel3` **read** for inheritance and closes it only if it never forks; grandchild closes it at `g1` | grandchild reads at `g0` | as `rel1` read |
| `rel3` write | CLI, pre-fork | `O_NONBLOCK` | **CLI only** after `m1` | CLI at `c16`; middle child at `m1` (**before** the second fork) | CLI writes at `c16` | as `rel1` write |
| `SPAWN.lock` fd | CLI, `c1a` | — | CLI, middle child, grandchild (fork-shared) | CLI at `c18`; middle child at `m9` (`_exit`); grandchild at `g3` | — | — |

Because the middle child closes `rel3` **write** at `m1` and retains `rel3`
**read** for the grandchild to inherit, the CLI is the grandchild's sole `rel3`
writer for the gate's whole lifetime — the confirmed property, unchanged.

### V214.1.3 The one bounded read helper (used by `c9`, `c13`, `m0`, `m5`, `g0`)

```text
BOUNDED_READ(fd, deadline_ns, expect ∈ {FRAME, RELEASE_BYTE}, route):
  buf = b""
  loop:
    now_ns = time.clock_gettime_ns(CLOCK_MONOTONIC)          # one sample/iteration
    if now_ns ≥ deadline_ns                     → route(DEADLINE)
    try: chunk = os.read(fd, T_CONTROL_READ_BUFFER_MAX_BYTES - len(buf))
    except BlockingIOError                      → paced retry: re-enter the loop
                                                   only once
                                                   T_SUPERVISOR_POLL_INTERVAL_NS
                                                   of monotonic time has elapsed
                                                   since this iteration's sample
    except InterruptedError (EINTR)             → retry immediately; the
                                                   deadline is unchanged
    except OSError (any other errno)            → route(READ_ERROR)
    if chunk == b"" (EOF)                       → route(EOF_INCOMPLETE)
    buf += chunk
    if expect is RELEASE_BYTE:
        if len(buf) != 1                        → route(TRAILING_BYTES)
        if buf != the exact expected byte       → route(MALFORMED)
        return
    # expect is FRAME
    if b"\n" not in buf and len(buf) > T_CONTROL_FRAME_MAX_BYTES
                                                → route(FRAME_LENGTH)
    if b"\n" in buf:
        line, rest = buf.split(b"\n", 1)
        if rest != b""                          → route(TRAILING_BYTES)
        if len(line) + 1 > T_CONTROL_FRAME_MAX_BYTES
                                                → route(FRAME_LENGTH)
        if line is not canonical ASCII JSON with the stage's exact schema id,
           exact key set, exact types/enums/hex/timestamp grammars
                                                → route(MALFORMED)
        return the validated object
```

- **`EAGAIN`/`EWOULDBLOCK`** is the ordinary case and is a **paced retry**
  against the same deadline — never an error and never an exit.
- **EOF before a complete frame** is `EOF_INCOMPLETE`, routed to the stage's
  failure cleanup. EOF is therefore an *earlier* arrival at the same route the
  deadline would reach, never a distinct outcome.
- **A second frame, or any trailing byte, in the same stage read** is
  `TRAILING_BYTES` ⇒ fail-closed. Exactly one frame per stage is legal, and
  this is sound because the write order makes concurrent frames impossible:
  the middle child writes `m4`'s group report, then **blocks at `m5`** until
  the CLI has read it (`c9`) and released `rel2` (`c12`), so `m8`'s bootstrap
  report cannot exist before `c9` has completed.
- **Malformed, overlong, or duplicate** report bytes are fail-closed.
- **Every other read error** is fail-closed cleanup.

### V214.1.4 The one bounded write helper (used by `c8`, `c12`, `c16`, `m4`, `m8`)

```text
BOUNDED_WRITE(fd, payload, deadline_ns, route):
  # payload is either one canonical ASCII JSON line ending in b"\n" with
  # len(payload) ≤ T_CONTROL_FRAME_MAX_BYTES, or one release byte.
  # Because len(payload) ≤ PIPE_BUF (verified at creation) and the fd is
  # O_NONBLOCK, POSIX guarantees the write is ALL-OR-EAGAIN: a partial write
  # cannot occur. The length check below is a fail-closed assertion.
  loop:
    now_ns = time.clock_gettime_ns(CLOCK_MONOTONIC)
    if now_ns ≥ deadline_ns                     → route(DEADLINE)
    try: n = os.write(fd, payload)
    except BlockingIOError                      → paced retry at
                                                   T_SUPERVISOR_POLL_INTERVAL_NS
    except InterruptedError (EINTR)             → retry immediately
    except BrokenPipeError (EPIPE)              → route(PEER_GONE)
    except OSError (any other errno)            → route(WRITE_ERROR)
    if n != len(payload)                        → route(WRITE_ERROR)
    return
```

CPython sets `SIGPIPE` to `SIG_IGN` at interpreter startup, so `EPIPE` is
raised as `BrokenPipeError` and never kills the writer — the fact this chain
has relied on since v2.1.

### V214.1.5 Stage routes, deadlines, and every cut

Each stage's deadline is `stage_start_ns + T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`
(the grandchild's gate: `+ 2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, §V214.1.1),
sampled from `CLOCK_MONOTONIC` at the stage's first instruction.

| Step | Operation | Route on **any** of DEADLINE / EOF_INCOMPLETE / MALFORMED / FRAME_LENGTH / TRAILING_BYTES / READ_ERROR / WRITE_ERROR / PEER_GONE |
|---|---|---|
| `c8` | `BOUNDED_WRITE(rel1_w, b"\x01")` | §U2.5 **stage-1** route (`SPAWNING_MIDDLE.json` is durable; `kill(middle_child_pid)` only, never `killpg`) |
| `c9` | `BOUNDED_READ(boot_r, FRAME)` — group report | §U2.5 **stage-1** route |
| `c12` | `BOUNDED_WRITE(rel2_w, b"\x02")` | §U2.5 **stage-2** route (`group_verified: true` is durable; `killpg(process_group_id)`) |
| `c13` | `BOUNDED_READ(boot_r, FRAME)` — bootstrap report | §U2.5 **stage-2** route |
| `c16` | `BOUNDED_WRITE(rel3_w, b"\x01")` | §U2.5 **stage-2** route |
| `m0` | `BOUNDED_READ(rel1_r, RELEASE_BYTE)` | `os._exit(3)` |
| `m4` | `BOUNDED_WRITE(boot_w, group report)` | `os._exit(3)` |
| `m5` | `BOUNDED_READ(rel2_r, RELEASE_BYTE)` | `os._exit(3)` |
| `m8` | `BOUNDED_WRITE(boot_w, bootstrap report)` | `os._exit(3)` |
| `g0` | `BOUNDED_READ(rel3_r, RELEASE_BYTE)` | `os._exit(3)` |

Every stage-1 and stage-2 route ends with the §U6.3 ordered record removal
(child → group → middle → spawning, each with a parent-directory `fsync`) and
the already-signed identity/kill discipline: kill only after exact
`pid + start identity` validation, prove death by `/proc` absence or state `Z`,
`os.waitpid` only for own children, and **never** kill on a start-identity
mismatch (PID reuse). No route introduces a new signal, a new record, or a new
identity source.

**Complete re-run of `c4`→`c18`, `m0`→`m9`, `g0`→identity, for death at every
instruction** (this replaces §U2.6's table):

| Death / stall point | Who holds a lock reference | Single continuation |
|---|---|---|
| CLI dies between `c4` and `c7` | CLI (released on exit), middle | middle is at `m0`; it holds its own `rel1` write copy until `m1`, so EOF is **not** guaranteed — the `m0` **bound** fires at ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` ⇒ `_exit(3)`. (This is Opus X213-m2's correction: the bound, not EOF, is the guarantee here.) |
| CLI dies between `c7` and `c8` | CLI, middle | as above; additionally `SPAWNING_MIDDLE.json` is durable, so `s4` can `kill(middle_child_pid)` |
| CLI dies between `c8` and `c9` | CLI, middle | middle proceeds to `m4`; its `BOUNDED_WRITE` takes `EPIPE` (no reader) ⇒ `_exit(3)`. If it reaches `m5` first, that gate's bound or EOF fires ⇒ `_exit(3)` |
| CLI dies between `c9` and `c12` | CLI, middle | middle is at `m5`; the CLI's `rel2` write end closed at exit and the middle child closed its copy at `m1`, so **EOF is guaranteed** ⇒ immediate `_exit(3)` |
| CLI dies between `c12` and `c16` | CLI, middle, grandchild | middle at `m8` takes `EPIPE` ⇒ `_exit(3)`; grandchild at `g0` gets **EOF** on `rel3` (the CLI was its sole writer) ⇒ `_exit(3)` |
| CLI dies after `c16`, before `c18` | grandchild | grandchild proceeds normally; its own bounded first-ack wait governs; `s2` applies to later clients |
| middle dies at `m0` (before any report) | CLI, middle gone | `c9`'s bounded read sees **EOF** (the middle child was the only `boot` writer; the grandchild does not exist) ⇒ stage-1 route ⇒ `kill(pid_mid)` on an already-dead pid, death proved, ordered removal, `REFUSED`/`BOOTSTRAP` |
| middle dies between `m1` and `m4` | CLI | as above: EOF at `c9` ⇒ stage-1 route |
| middle fails `m3` (`sid ≠ pgid ≠ pid`) | CLI | `_exit(3)` ⇒ EOF at `c9` ⇒ stage-1 route |
| middle dies between `m4` and `m7` | CLI | `c9` already returned; `c13`'s bounded read sees **EOF** (no grandchild yet) ⇒ stage-2 route ⇒ `killpg(process_group_id)` on the verified group |
| **middle dies between `m7` and `m8`** (Sol C1's cut) | CLI, grandchild | the grandchild holds a `boot` write copy, so **no EOF arrives** — `c13`'s **bound** fires at ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` (executable because `boot` is now nonblocking) ⇒ stage-2 route ⇒ `killpg(process_group_id)`, which reaches the grandchild (same session/group) ⇒ death proved ⇒ ordered removal ⇒ lock released. **No deadlock.** |
| middle dies after `m8`, before `m9` | CLI, grandchild | ordinary: `c13` already returned; the bootstrap proceeds |
| grandchild dies at `g0` | CLI | `c17`'s bounded identity poll expires ⇒ stage-2 route ⇒ `killpg` (already dead) ⇒ death proved ⇒ ordered removal |
| grandchild stalls at `g0` because `c16` never runs | CLI, grandchild | the `g0` bound (`2 ×`) fires ⇒ `_exit(3)` ⇒ lock reference released |
| grandchild dies between `g1` and `g3` | CLI (until `c18`) | `c17` expires ⇒ stage-2 route; or the grandchild's own bounded first-ack wait exits it, removing records in §U6.3 order |
| grandchild's first-ack wait expires | grandchild | kill the watchdog by `WATCHDOG_CHILD.json`, prove death, ordered removal, `_exit(3)` ⇒ lock released |
| any writer takes `EPIPE` at `c8`/`c12`/`c16` | CLI | the corresponding stage route (1 / 2 / 2) |
| any read returns malformed, overlong, duplicate, or trailing bytes | CLI or child | the same stage route as a deadline — fail-closed, never a partial acceptance |
| PID reuse at any tier | — | start-identity mismatch ⇒ **no kill**; treat as absent; ordered removal under the acquired lock |

**Invariants restated and now executable.** No blocking syscall exists in the
bootstrap, so every deadline is evaluable at every instruction. No pipe cycle
can retain `SPAWN.lock`: each of the three gates and each of the five
report/release operations terminates by success, EOF, error, or its own bound.
Every cleanup uses only the already-signed identity/kill discipline. The two
named A3 residuals of §U2.7 (a deliberately stopped CLI; a deliberately stopped
middle child inside the bounded `m0` window) are unchanged and are not
enlarged.

---

## V214.2. Orphan-manifest quarantine as a valid K1 disposition branch (R2)

Closes Sol C2 and Opus X213-m1.

### V214.2.1 `QUARANTINE.json` binds the orphan manifest

The carried §W4.7 schema gains exactly one key:

```text
operations/<operation_id>/QUARANTINE.json
schema philosophia.officina.t-operation-quarantine.v1, atomic no-replace,
supervisor under T_RUNTIME.lock, keys exactly:

  schema, scientific_outcome, supervisor_generation_sha256, operation_id,
  process_id, failure_class ∈ {BOUND_EXCEEDED, GRAMMAR, TRANSPORT,
    WORKER_FAILED, PARTIAL_OUTPUT, FILESYSTEM, HASH, SUPERVISOR_CRASH},
  bytes_accounted, custody_root, result_manifest_sha256_or_null,
  invalidity_event_sha256, created_utc
```

```text
result_manifest_sha256_or_null is NON-NULL exactly when a durable
RESULT_MANIFEST.json exists for this operation at the instant QUARANTINE.json
is installed, and then equals SHA-256 of that manifest file's exact canonical
bytes (a metadata hash; no output content byte is read).
It is NULL exactly when no RESULT_MANIFEST.json exists at that instant.
No third case exists: the field is computed from a directory-fd observation in
the same lock epoch that installs the record.
```

### V214.2.2 The record-first crash reducer installs the bound terminal

§U5.2's "crash after the manifest, before `SETTLEMENT.json`" row is extended
with an exact duty. At generation start and at every takeover, under
`T_RUNTIME.lock`, before serving (the §Z2.5 phase-2A discipline, unchanged):

```text
for each operations/<op>/ with a durable RESULT_MANIFEST.json and NO durable
SETTLEMENT.json:
  Q1. if QUARANTINE.json is absent:
        complete the signed invalid terminal set for that operation
        (failure_class = SUPERVISOR_CRASH, §W4.7 route, unchanged), then
        install QUARANTINE.json with
          result_manifest_sha256_or_null = SHA-256(manifest bytes)
        (atomic no-replace, §3 durability)
  Q2. if QUARANTINE.json is present with a NON-NULL value:
        verify it equals SHA-256(the manifest's current bytes);
        equal ⇒ nothing to do; unequal ⇒ record-first invalidity naming both
        paths (the manifest is immutable, so inequality is an impossible
        durable layout reachable only through the A3 procedural residual)
  Q3. if QUARANTINE.json is present with a NULL value while a manifest exists:
        record-first invalidity naming both paths (an impossible layout)
  Q4. EEXIST at Q1's install ⇒ re-read and apply Q2/Q3; never overwrite
```

Crash cuts: a crash between the invalid terminal set and `QUARANTINE.json`
leaves the manifest plus a durable invalidity event; the next epoch re-derives
and installs idempotently by no-replace. A crash after `QUARANTINE.json` is the
ordinary quarantined state. Nothing is ever rewritten, and no output byte is
read at any step.

### V214.2.3 Three exclusive verifier branches (replaces §U5.4's `V1`–`V6`)

Branch selection is decided by durable objects alone, in this order, and
exactly one branch may apply:

```text
B-P   SETTLEMENT.json durable                                  ⇒ settled branch
B-QM  QUARANTINE.json durable ∧ result_manifest_sha256_or_null ≠ null
                                                    ⇒ quarantined-with-manifest
B-QN  QUARANTINE.json durable ∧ result_manifest_sha256_or_null = null
                                                      ⇒ quarantined-no-manifest
REFUSE (release nothing) for every other combination, including:
   both SETTLEMENT.json and QUARANTINE.json durable   (record-first invalidity:
                                                       an impossible layout)
   neither durable                                    (no terminal exists yet)
   B-QM selected but RESULT_MANIFEST.json physically absent
   B-QN selected but RESULT_MANIFEST.json physically present
   any hash mismatch, duplicate, or partially installed object
```

**Branch `B-P` — settled/promoted** (unchanged from §U5.4 `V1`–`V5`):

```text
P1. read RESULT_MANIFEST.json through an O_DIRECTORY|O_NOFOLLOW dir-fd walk;
    regular file; st_nlink == 1; no symlink component
P2. its exact canonical bytes hash to SETTLEMENT.json's result_manifest_sha256
P3. SHA-256(canonical entries) == SETTLEMENT.json's result_sha256; entry_count
    and total_byte_length agree with entries; entries sorted and unique;
    promoted_relative_paths matches the path list
P4. recursive scientific-field rejection over the whole manifest object
P5. prohibited-value set =
      { result_sha256, result_manifest_sha256,
        every content_sha256 in the manifest,
        every relative_path in the manifest,
        charge_event_sha256, lease_sha256 }
```

**Branch `B-QM` — quarantined with an orphan manifest** (new; this is the
branch whose absence made the signed K1 release impossible for an ordinary
crash state):

```text
QM1. read RESULT_MANIFEST.json through an O_DIRECTORY|O_NOFOLLOW dir-fd walk;
     regular file; st_nlink == 1; no symlink component
QM2. its exact canonical bytes hash to QUARANTINE.json's
     result_manifest_sha256_or_null  — the binding is to the QUARANTINE
     record; NO settlement exists and none is required
QM3. the manifest validates standalone: exact schema id, exact key set and
     types, operation_id == this operation, entry_count == len(entries),
     total_byte_length == Σ byte_length, entries sorted ascending by
     relative_path bytes and unique; compute
       orphan_result_sha256 = SHA-256(canonical entries)
     for the prohibited-value set only — it is compared against no settlement
     field, because none exists
QM4. recursive scientific-field rejection over the whole manifest object
QM5. prohibited-value set =
      { orphan_result_sha256, result_manifest_sha256_or_null,
        every content_sha256 in the manifest,
        every relative_path in the manifest,
        charge_event_sha256, lease_sha256 }
QM6. no output content byte is read at any step
```

**Branch `B-QN` — quarantined with no manifest**:

```text
QN1. QUARANTINE.json's result_manifest_sha256_or_null is null
QN2. RESULT_MANIFEST.json is proved physically ABSENT by the paired test the
     same lock epoch already performs (§N2.3 P2's directory-fd enumeration of
     the operation directory plus a follow_symlinks=False stat raising ENOENT)
QN3. manifest-dependent checks are vacuous ONLY here
QN4. prohibited-value set = { charge_event_sha256, lease_sha256 }
```

Every other §N1.5 conjunct (1, 3, 4, 5, 6, 8a–8e, 11) is unchanged and applies
to all three branches. Conjunct 4's terminal test is satisfied by whichever of
`SETTLEMENT.json` / `QUARANTINE.json` selected the branch, and
`custody_parent_sha256` binds that same record's canonical bytes.

### V214.2.4 Custody, retention, accounting, and K1 release

- **Custody-set interaction.** `RESULT_MANIFEST.json` is already inside the L2
  closed control-record set (§U5.5), so an orphan manifest never blocks
  §N2.3's P2 subset test and never counts as custody. The absence predicate
  P1–P7 is unchanged in every branch.
- **Accounting.** `bytes_reserved` remains the accounted contribution in every
  branch until a verified disposition installs `.disposed.json`; `actual_bytes`
  and the manifest's `total_byte_length` remain diagnostic and never reduce the
  accounted total. This repair **restores a legitimate release route; it
  weakens no accounting rule**.
- **Retention.** The manifest and the quarantine record are never removed
  (§U9.1, unchanged), so `B-QM` remains resolvable for the whole lifetime of
  the operation's capacity accounting, including after release.
- **Release trace.** For an operation quarantined with an orphan manifest: the
  author removes every custody location outside T → §N2.3's P1–P7 prove all
  five classes absent in one lock epoch → the §N1.5 conjuncts plus branch
  `B-QM` verify → `.disposed.json` installs once, releasing exactly
  `bytes_reserved`. Before this layer, that operation's reservation could never
  be released by any actor.

---

## V214.3. GC that preserves the G3 authority throughout (R3)

Closes Sol M1. §N8.1's eligibility conditions, §N8.2's per-command archival
predicates, and §N8.3's prefix-first classification are unchanged.

### V214.3.1 The exact deletion order (replaces §U4.1's `D0`–`D8`)

`accepted.json` is the **only** phase file that records `command`,
`effect_plan`, and the process/lease identities that §N8.2's predicate needs,
so it must survive until last. `ack.json` may be deleted before it, because the
**tombstone's `acknowledged_prefix_occurrence` is permanent and never
deleted**, and by §Z1.9's contiguous-prefix construction `i ≤ prefix` **is** the
durable proof of acknowledgement — `ack.json` is a per-key witness of the same
fact.

```text
D0. verify, in this epoch, for occurrence i:
      G1  ack.json for i is durable and immutable
      G2  i ≤ acknowledged_prefix_occurrence          (from the tombstone)
      G3  the §N8.2 command-specific archival predicate holds, SELECTED AND
          BOUND by accepted.json's `command` and `effect_plan`
    any failure ⇒ delete nothing
D1. unlink committed.json     (ENOENT ⇒ already done, continue)
D2. unlink reply.json         (ENOENT ⇒ continue)
D3. fsync the key directory
D4. unlink ack.json           (ENOENT ⇒ continue)
D5. fsync the key directory
D6. FINALIZATION: re-verify, in this epoch, from the files actually present:
      F1  i ≤ acknowledged_prefix_occurrence          (permanent tombstone)
      F2  the §N8.2 predicate, re-selected and re-bound from accepted.json's
          `command` and `effect_plan`
      F3  committed.json, reply.json, and ack.json are all absent
    any failure ⇒ stop; delete nothing further; the directory remains
    GC-eligible in a later epoch by this same rule
D7. unlink accepted.json      ← LAST
D8. fsync the key directory
D9. rmdir the key directory   (ENOENT ⇒ already done;
                               ENOTEMPTY ⇒ record-first invalidity naming the
                               directory — nothing is ever deleted blindly)
D10. fsync the JOURNAL parent directory
```

**Empty-directory completion rule** (carried in effect, now reachable only
after `D7`): a key directory containing **no phase file**, whose occurrence
index satisfies `i ≤ acknowledged_prefix_occurrence`, may be `rmdir`ed in any
later held-lock epoch with no further predicate, because nothing remains whose
eligibility could be in question and the prefix is permanent.

### V214.3.2 Prefix proof, using only the files present after each cut

| Cut | Files present | Eligibility re-derivable? | Continuation |
|---|---|---|---|
| before `D1` | accepted, committed, reply, ack | **yes**: G1 from ack, G2 from the tombstone, G3 from accepted | re-verify `D0`, start at `D1` |
| `D1`→`D2` | accepted, reply, ack | **yes**: same three sources | resume at `D1` (ENOENT-tolerant) |
| `D2`→`D4` | accepted, ack | **yes**: same three sources | resume at `D1` |
| `D4`→`D7` | **accepted only** | **yes**: F1 from the permanent tombstone, F2 from accepted; F3 holds | resume at `D6` (the finalization rule) |
| `D7`→`D9` | none (empty directory) | not needed | empty-directory completion `rmdir` |
| after `D9` | directory absent | — | complete |
| any cut | the tombstone is **never** deleted | — | §N8.3 step 1 answers `REFUSED`/`ALREADY_ACKNOWLEDGED` for `i ≤ prefix` regardless of which files exist, so exactly-once holds and no reducer can run |

**Why this order is exactly sufficient.** At every cut before `D7`,
`accepted.json` is present, so the command-specific G3 predicate can always be
re-selected and re-bound — the information Sol M1 showed was destroyed by
deleting `accepted` first. At every cut at or after `D7`, no semantic phase
remains and only the predicate-free `rmdir` is outstanding. The two authorities
that survive longest are the **permanent tombstone** (acknowledgement) and
**`accepted.json`** (which predicate applies), which are precisely the two facts
the finalization rule needs.

**No owed reply is deleted before durable acknowledgement:** `reply.json` is
removed at `D2`, strictly after `D0` proved `i ≤ acknowledged_prefix_occurrence`
— i.e. after the one-use effect was durably acknowledged, which is signed B1's
exact boundary. Deleting `committed.json` before `reply.json` is likewise safe:
prefix-first classification answers before any reducer inspects phases, so no
"highest present phase" inference can be drawn from an intermediate state.

### V214.3.3 `errno`, fsyncs, concurrency, and the per-command G3 binding

- **`fsync`s** at `D3`, `D5`, `D8`, and `D10` as pinned above; each precedes
  the next deletion class so no reordering can make a cut unrecoverable.
- **`errno`.** `unlink` `ENOENT` ⇒ continue (idempotent); `rmdir` `ENOENT` ⇒
  done; `rmdir` `ENOTEMPTY` ⇒ record-first invalidity naming the directory; any
  other `errno` on any step ⇒ abandon this GC in this epoch, delete nothing
  further, record-first invalidity naming the path. **There is no `EEXIST` in
  GC**, which creates nothing.
- **Concurrency.** GC and frame service both hold `T_RUNTIME.lock` and
  therefore serialize. A retry evaluated before, in the same epoch as, or after
  any GC step receives the identical `REFUSED`/`ALREADY_ACKNOWLEDGED` answer
  (§N8.3), so GC timing remains invisible to clients.
- **G3 binding, per command.** §N8.2's table is unchanged; the applicable row is
  **selected by `accepted.json`'s `command`**, and its proof identities come
  from `accepted.json`'s `effect_plan`:

| `command` in `accepted.json` | Identities read from `effect_plan` | §N8.2 predicate |
|---|---|---|
| `CLAIM` | `process_id`, `claim_path` | the owning process's terminal archival commit |
| `START` | `process_id`, `start_event_sha256`, `lease_path` | the same terminal archival commit |
| `HEARTBEAT` | `charge_event_sha256`, `process_id` | the archival commit covering that charge (process terminal set, or the batch-settlement commit) |
| `CLOSE` | `process_record_path`, `stopped_event_sha256`, `archive_set "close"` | the signed §2c.6 close archival commit |
| `PAUSE` | `checkpoint_path`, `pause_event_sha256`, `archive_set "pause"` | the signed §6a pause archival commit |
| `RESUME` | `verified_checkpoint_sha256`, `first_event_sha256_or_null`, `target_phase` | the resume archival commit, or the exact no-event predicate |
| `OPERATION_ADMIT` | `operation_id`, `running_path` | a durable operation terminal **and** the archival commit covering its settling charge |
| `OPERATION_STATUS`, `plan_kind = "DELIVERY_ACK"` | `operation_id`, `delivery_ack_path` | `DELIVERY_ACK.json` durable **and** the operation terminal durable |
| `OPERATION_STATUS`, `plan_kind = "OBSERVATION"` | `operation_id`, `plan_kind` | **vacuous** — but the vacuity is still *selected* from `accepted.json`, which is why `accepted` must survive to `D6` |

---

## V214.4. Acquire `SPAWN.lock` before singleton preflight (R4)

Closes Sol M2.

### V214.4.1 The single-valued order

§U2.2's `c1` and §U6.1's opening sentence are replaced by one order:

```text
c1a. bounded acquire: flock(SPAWN.lock, LOCK_EX|LOCK_NB), retrying at
     T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS.
     On expiry take the §V214.4.2 stuck-holder route.
c1b. WHILE HOLDING THE ACQUIRED LOCK: run the full §U6.1 preflight (P0–P3)
     over the four singleton records in the child → group → middle → spawning
     order, including every adoption (P2a), every conflict refusal (P2b),
     every malformed fail-close (P1), and every death-proved removal (P3) with
     its §U6.3 ordered unlinks and parent-directory fsyncs.
c2.  install SPAWNING.json (§W2.2 keys unchanged; §3 durability; §U6.2 EEXIST
     continuation, itself resolved by P1/P2/P3 under this same held lock)
```

**Normative rule.** No preflight read that can lead to adoption, removal, kill,
or any mutation may occur before `c1a` completes. Every `EEXIST` continuation
of §U6.2, at `c2`, `c7`, `c11`, and `c15`, is likewise evaluated **under the
held lock**, because all four installs occur inside the lock epoch that began
at `c1a` and ends at `c18`.

### V214.4.2 The unlocked stuck-holder route kills but never mutates

§U2.5's `s1`–`s5` are unchanged **except** that the clause "remove records per
§U6.3, retry the bounded acquisition exactly once" is replaced in `s2`, `s3`,
and `s4` by:

```text
… prove death, then retry the bounded acquisition exactly once; on success,
c1b's preflight — now under the acquired lock — performs the §U6.3 ordered
removal of the records the kill made stale.
```

The stuck-holder route therefore performs **only**: reads of the four records,
identity and age validation, a kill of one aged identity-proved process by its
tier's permitted signal (`killpg` for child/group, `kill` only for middle), a
death proof, and one retry. It performs **no** unlink, no adoption, no install,
and no read-modify-write of any record, so no mutation can race the current
lock holder. Killing is the only way to break a stuck holder and mutates no
contract artifact.

### V214.4.3 Order, `EEXIST`, and cleanup reconciliation

| Step | Lock state | Permitted actions |
|---|---|---|
| before `c1a` | not held | none on any singleton record |
| stuck-holder `s1`–`s5` | **not held** | read, validate, kill (tier-permitted, identity-proved), prove death, retry acquisition — **no unlink, no adopt, no install** |
| `c1a` | acquiring | none |
| `c1b` | **held** | full P0–P3: adopt, refuse, and remove with §U6.3 order and `fsync`s |
| `c2`, `c7`, `c11`, `c15` | **held** | install; on `EEXIST` re-read and apply P1/P2/P3 under the same held lock; P3 ⇒ ordered removal then retry the install exactly once |
| stage-0/1/2 failure routes | **held** | kill per tier, prove death, §U6.3 ordered removal, release the lock |
| `g3` success path | held by the grandchild | §U6.3 ordered removal, then close the lock fd |
| client takeover (§W2.9 phase 1, §U6.4) | **held** (`SPAWN.lock`, unchanged) | the same P1/P2/P3 discipline over the four records; unlinks no durable `runtime/` evidence, `JOURNAL/*`, `CAPACITY/*`, quarantined output, or `T_PROMOTED/**` |

---

## V214.5. Total watchdog replacement priority (R5)

Closes Sol M3. §U3.1's swap-only/deadline split, §U3.3's records, and §U3.4's
crash table are otherwise unchanged.

### V214.5.1 Pinned priority and the first-true rule

The invalid conditions are evaluated in the **exact numeric order
`I1 → I2 → I3 → I4 → I5 → I6 → I7`** within one locked observation. The first
true condition is the `invalid_condition` recorded in
`<replacement_freeze_id>.invalidated.json`.

**Routing irrelevance of the diagnostic set, proved.** Every one of I1–I7
routes to the **identical** signed all-live invalid route (§2c.12/§2c.12b/§4d,
public cause `PROCESS`, with the §4c(c)/§4d unknowable pool when any member
state is unknowable). No routing decision anywhere in the contract reads
`invalid_condition`. It is therefore safe — and, for determinacy, **required**
— to record the complete set of conditions observed true in that same locked
observation as a sorted array `diagnostic_conditions`; it cannot affect
routing, and pinning it removes the "which one did you record" ambiguity.

### V214.5.2 The exact conditions (replacing `I2` and `I3`)

```text
I1. now_ns ≥ deadline_ns of the group's current durable lease row
I2. the replacement watchdog has NOT delivered a VALID acknowledgement of the
    EXACT CURRENT table_seq by the bound, where:
      valid ⇔ the ack frame validates against t-watchdog-ack.v1 exactly (key
              set, types, strict int), AND its supervisor_generation_sha256
              equals the current generation, AND its table_seq equals the
              EXACT current table_seq whose table contains this group's row;
      the bound ⇔ replacement_table.updated_monotonic_ns
                  + T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS;
      an os.fork failure of the replacement watchdog makes I2 true immediately;
      a stale, wrong-table, wrong-generation, or malformed ack NEVER satisfies
      the acknowledgement and therefore never prevents I2 from firing at the
      bound
I3. identity or member-state defect, evaluated BEFORE .resumed.json is durable:
      any recorded member's pid + start identity differs, OR
      any recorded member is absent, Z, or in ANY state other than exactly T
      (including R, S, D, or an unclassifiable state).
    AFTER .resumed.json is durable the relaxed rule applies: only identity
    mismatch, absence, or Z makes I3 true; T and running are both legal.
I4. a §W3.3 deadline-freeze witness or a §N5 fallback exists for that process
    in the current generation
I5. an unresolved invalidity blocks: G5 not clear, or the record-first
    ordering / v2.1 §B.4 not satisfied
I6. the recorded lease is no longer the current durable lease
I7. the REPLACEMENT_FREEZE record's supervisor_generation_sha256 differs from
    the current generation
```

### V214.5.3 The exhaustive, disjoint partition

```text
one locked observation, one monotonic sample now_ns, all /proc member reads
inside the same lock epoch:

  step 1: evaluate I1..I7 in priority order.
          if any is true ⇒ INVALID, invalid_condition = the FIRST true one,
          diagnostic_conditions = the sorted set of ALL true ones
  step 2: else if a VALID ack of the EXACT current table_seq is durably
          observed (the S1 predicate, with "valid" as defined in I2)
          ⇒ RESUMABLE
             S2 need not be tested separately: ¬S2 ⇒ I3 ⇒ step 1 already
             returned INVALID. S2's content is exactly ¬I3.
  step 3: else ⇒ ACK_PENDING
```

**Totality and disjointness.** Step 1 covers every state in which any I holds.
Step 2 covers the remaining states with the exact ack. Step 3 covers the
remaining states without it. Exactly one branch applies to any observation, and
none is empty of continuation. The v2.1.3 gap — S1 true, S2 false because a
member was running before a resume marker, matching no branch — is closed by
making that condition part of I3, so it now resolves to `INVALID` at step 1.

`ACK_PENDING` remains an explicitly **non-invalid**, non-terminal, evidence-free
held-frozen state, re-evaluated at each `T_SUPERVISOR_POLL_INTERVAL_NS` serve
step and bounded by
`min(deadline_ns, replacement_table.updated_monotonic_ns +
T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS)`, at which point I1 or I2 fires. **No
healthy non-overdue group is invalidated merely by a pending ack**: for such a
group I1–I7 are all false until the bound, and the replacement watchdog forks
and acks the exact current table within
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS + T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`
(10 s + 1 s at worst), so it transitions `ACK_PENDING → RESUMABLE`.

### V214.5.4 The invalidation marker

```text
WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.invalidated.json
schema philosophia.officina.t-replacement-invalidation.v1, atomic no-replace,
supervisor under T_RUNTIME.lock, keys exactly:
  schema, scientific_outcome, replacement_freeze_id,
  invalid_condition ∈ {I1,I2,I3,I4,I5,I6,I7},          # the FIRST true one
  diagnostic_conditions (sorted array over the same closed token set, always
                         containing invalid_condition),
  observed_monotonic_ns, invalidated_utc
```

`observed_monotonic_ns` is the single `now_ns` sample of that locked
observation. It is bookkeeping only: it is never an `overrun_ns` input, never a
§W3.3/§W3.4 witness, never a freeze instant, and permanently non-citable —
unchanged from §U3.3.

### V214.5.5 Race truth table

`ack` = a valid ack of the exact current `table_seq`; `members` = every
recorded member's identity matches and state is exactly `T` (pre-resume) or
`T`/running (post-`.resumed.json`); `now ≥ dl` = I1; `bound` = the I2 absence
bound.

| # | `now ≥ dl` | `ack` | `members` | witness/fallback | generation | lease current | state | `invalid_condition` |
|---|---|---|---|---|---|---|---|---|
| 1 | no | yes | yes | none | current | yes | **RESUMABLE** | — |
| 2 | no | no, before bound | yes | none | current | yes | **ACK_PENDING** | — |
| 3 | no | no, bound passed | yes | none | current | yes | **INVALID** | I2 |
| 4 | **yes** | yes | yes | none | current | yes | **INVALID** | I1 (deadline dominates a simultaneous valid ack) |
| 5 | **yes** | no | yes | none | current | yes | **INVALID** | I1 |
| 6 | no | yes | **no** (a member is R/S/D) | none | current | yes | **INVALID** | I3 (the v2.1.3 gap; now covered) |
| 7 | no | no, before bound | **no** | none | current | yes | **INVALID** | I3 |
| 8 | **yes** | no, bound passed | **no** | none | current | yes | **INVALID** | I1 (first true) — `diagnostic_conditions = [I1,I2,I3]` |
| 9 | no | yes | yes | **witness present** | current | yes | **INVALID** | I4 |
| 10 | no | yes | yes | none | current | yes, but **G5 blocked** | **INVALID** | I5 |
| 11 | no | yes | yes | none | current | **superseded** | **INVALID** | I6 |
| 12 | no | yes | yes | none | **prior** | yes | **INVALID** | I7 |
| 13 | no | **stale/wrong-table/malformed only**, before bound | yes | none | current | yes | **ACK_PENDING** | — (the invalid ack neither resumes nor defeats I2) |
| 14 | no | **stale/wrong-table/malformed only**, bound passed | yes | none | current | yes | **INVALID** | I2 (the v2.1.3 gap; now covered) |
| 15 | no | replacement `os.fork` failed | yes | none | current | yes | **INVALID** | I2 (immediate) |

Every row has exactly one continuation; no row has zero or two.

---

## V214.6. The corrected during-pass A3 statement (R6)

Closes Sol M4. Literal K1 counts are untouched: one write and one hash per
output content byte.

### V214.6.1 What the sole hash actually claims

§U1.1's final clause is replaced by:

> The pass hashes the bytes it reads and makes exactly one claim about them:
> `content_sha256` accurately describes **the exact byte stream read** through
> the inode-verified descriptor during that pass. It makes **no** claim that
> the stream equals what the worker sent, **no** claim that it equals any
> single coherent state of the file, and **no** claim about the bytes at any
> later instant — in particular **no** claim that it describes the bytes later
> promoted by `os.replace`.

`result_sha256` and the result manifest inherit exactly this meaning: they are
the identity of the read stream and of its metadata, and nothing more. Every
downstream use is unaffected, because no clause anywhere in the contract
requires `result_sha256` to equal a hash of the promoted bytes — the release
token carries it as the operation's result identity, and promotion is a rename
that reads nothing.

### V214.6.2 Truth table, with the stream / inode / promoted distinction

| Anomaly | Detected? | What the recorded hash then describes |
|---|---|---|
| inode substitution | **yes** (`(st_dev, st_ino)` vs the held `r`) | — quarantined, never promoted |
| hard-link introduction | **yes** (`st_nlink == 1`) | — |
| truncation / extension | **yes** (size, read length, EOF offset) | — |
| short read, long read, wrong-offset EOF | **yes** | — |
| path grammar, depth, uniqueness, lengths, counts, ceilings | **yes** (pre-creation) | — |
| worker count cross-check mismatch | **yes**, fail-closed ⇒ `TRANSPORT` | — |
| **A3-R1a**: same-inode equal-size modification **completed before** the pass | **NO** | the modified bytes — a real, single file state, which is also what would be promoted if nothing further changes |
| **A3-R1b**: same-inode equal-size modification **concurrent with** the pass, length and EOF stable | **NO** | a **mixed byte stream** assembled from successive `os.pread` chunks that may come from different content states. It **need not equal any single file state that ever existed**, and it **need not equal the final inode content or the later promoted bytes** |
| **A3-R2**: modification **after** the pass, before settlement/promotion | **NO** | the pre-modification stream, which **can differ from the promoted bytes** |
| **A3-R3**: same-name `out/` directory swap after the pass | **NO** | — the promoted tree may be entirely unrelated |
| nothing anomalous | — | the exact byte stream read, which in the absence of A3-R1a/R1b/R2/R3 is also the promoted content |

### V214.6.3 The four named residuals (replaces §U1.3's `A3-R1`)

```text
A3-R1a  Same-inode, equal-size, in-place modification COMPLETED BEFORE the
        sole hash pass. The hash describes the modified bytes. The bytes are
        not provably the worker's.

A3-R1b  Same-inode, equal-size, in-place modification CONCURRENT WITH the
        pass, not caught as a length or EOF anomaly. Successive pread chunks
        may be drawn from different content states, so the hash can describe a
        mixed stream that never existed as a single file state and that need
        not equal the final inode content or the bytes later promoted.

A3-R2   Any in-place modification of a verified inode AFTER the pass and
        before durable settlement/promotion. The pass establishes no future
        immutability, and this contract does not claim it does; result_sha256
        can therefore differ from the promoted bytes.

A3-R3   Same-name substitution of the out/ directory between the pass and the
        promotion os.replace (carried verbatim from §N4.4).
```

All four are signed-**A3 procedural** residuals: T-development-only,
permanently **non-citable**, forbidden from selection, Q, C, C1–C6, any
blinding claim, and any scientific interpretation. All four are **unobservable
under literal K1 hash-once** — detecting them would require a second content
hash or a content-derived stored reference, which §U1.5 forbids without a new
author decision on K1 — and **none has a `HASH` route**: they are never
signalled, never quarantined, and never invoked as evidence of anything. The
detected anomalies of §U1.4 keep the `HASH` class exactly as carried.

---

## V214.7. The corrected timestamp example (R7)

Closes Sol m1. §U7.3's example is corrected in **one number**; the equality
rule (§U7.1 conjunct 8e), the grammar and real-date check (§U7.2), the
already-verified 504-byte decision-file length, and its hash
`0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f` are
**unchanged**.

```text
decision file, line 8 (43 bytes including LF):
signed_utc: 2026-07-30T00:00:00.000000000Z

  arithmetic: "signed_utc" (10) + ":" (1) + " " (1) + timestamp (30) + LF (1)
              = 43

disposition object fragment (canonical JSON member):
"authorized_utc":"2026-07-30T00:00:00.000000000Z"

compared bytes (30 ASCII characters, identical in both):
2026-07-30T00:00:00.000000000Z
```

The eight §N1.4 lines with their LFs are therefore
`53 + 58 + 60 + 91 + 79 + 81 + 39 + 43 = 504` bytes, exactly the length whose
hash both independent lines reproduced. No other derived length or digest in
the chain changes.

---

## V214.8. Object table, authority, and reconciliation

### V214.8.1 Durable-object table delta (extends §U9.1)

| Object | Path (under `successor/officina/`) | Schema | Install | Writer / lock | Authority | Removed by |
|---|---|---|---|---|---|---|
| **Quarantine record** *(keys extended)* | `…/operations/<op>/QUARANTINE.json` | `t-operation-quarantine.v1` (+ `result_manifest_sha256_or_null`) | no-replace, §3 durability | supervisor under `T_RUNTIME.lock` | runtime | **never** |
| **Replacement invalidation marker** *(keys extended)* | `…/WATCHDOG/REPLACEMENT_FREEZE/<id>.invalidated.json` | `t-replacement-invalidation.v1` (+ `diagnostic_conditions`) | no-replace | supervisor under lock | runtime | supervisor after the process's durable terminal + archival commit |
| Result manifest *(unchanged; now also resolvable via `QUARANTINE.json`)* | `…/operations/<op>/RESULT_MANIFEST.json` | `t-operation-result-manifest.v1` | no-replace | supervisor under lock | runtime | never |
| Bootstrap channels *(flags changed)* | `boot`, `rel1`, `rel2`, `rel3` pipes (no file) | — | `os.pipe2(os.O_NONBLOCK)` ×4 | CLI, pre-fork | transport | closed per §V214.1.2 |

No object is added or removed by this layer; two key sets grow by one key each,
and four channel flag sets change. Every object remains control-plane,
`scientific_outcome: false`, recursively scientific-field-rejecting,
archival-excluded, and untracked. No signed activation-protocol §B archival set
changes.

### V214.8.2 Reconciliation of every affected item

| Item | Reconciled state |
|---|---|
| Schemas changed | `t-operation-quarantine.v1` (+1 key), `t-replacement-invalidation.v1` (+1 key) |
| Schemas added | none |
| Paths added | none |
| Channel flags | all four bootstrap pipes `O_NONBLOCK`; `PC_PIPE_BUF ≥ 4096` verified on each write end at creation |
| Verifier duties | §V214.2.3's three branches replace §U5.4's `V1`–`V6`; §V214.3.1's `D0`/`D6` replace §U4.1's `D0`; §V214.5.3's three-step partition replaces §U3.2's |
| Constants | **none added, none moved**; the grandchild gate's bound is the arithmetic `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` |
| Enums | `invalid_condition`'s closed token set is unchanged; `diagnostic_conditions` ranges over the same set; no refusal or `INVALID` token is added |
| Public commands | unchanged: six CLI, two controller, one refusal-first `--officina-bootstrap`, unknown ⇒ exit 2 |
| Signed events, resource values, roots, T bands | none added, none moved |
| Q/C surface | none added; every object and residual remains T-development-only and permanently non-citable |
| Worked examples | §V214.7 (43-byte line, 504-byte total); §U5.6's manifest digests and §U8.3's enumeration digests are **unchanged** and still reproduce |
| Test obligations | §V214.10 rows 121–144; §U11 rows 101, 105, 112, 113, 117 replaced |
| Free text / hidden judgement | none: every new field is a closed enum token, a sorted array over that closed set, or a 64-hex hash-or-null |

### V214.8.3 Inherited-closure qualification

Every closure recorded in §U9.4, §N10.3, §Z12.1, and every prior author closure
now reads **"closed in v2.1.3 (or earlier); confirmation pending independent
v2.1.4 X/Y"**. The X-line confirmation of v2.1.3 is recorded accurately: it
**confirmed** those bytes and recorded X213-m1 and X213-m2 as non-blocking
Minors; this layer closes both anyway, and the patched bytes therefore require
a fresh confirmation exactly as that review itself stated. The six v2.1.3 rows
this layer repairs are re-read as:

| v2.1.3 row | v2.1.4 reading |
|---|---|
| Sol C1 / §U2 bootstrap | closed **subject to** §V214.1 (the channel was blocking) |
| Sol C2 / §U3 replacement states | closed **subject to** §V214.5 (priority, I2's exactness, the S1/S2 gap) |
| Sol M1 / §U4 GC order | closed **subject to** §V214.3 (G3 authority must survive) |
| Sol M2 / §U5 manifest | closed **subject to** §V214.2 (the orphan-manifest branch) |
| Sol M3 / §U6 singleton records | closed **subject to** §V214.4 (lock before preflight) |
| Sol m2 / §U1.3 residuals | closed **subject to** §V214.6 (the promoted-byte claim) |

No closure in this document is asserted by author fiat; the author line cannot
confirm its own bytes.

---

## V214.9. Crash-cut matrix (extends §U10)

Every §U10 row carries forward except where §V214.0 names a replacement. Added
and replaced rows:

| Cut | Single continuation |
|---|---|
| `EAGAIN` on any stage read or write | paced retry at `T_SUPERVISOR_POLL_INTERVAL_NS` against the same stage deadline — never an error, never an exit |
| EOF before a complete frame on `boot` | the stage's failure route (stage-1 at `c9`, stage-2 at `c13`) |
| EOF on `rel1`/`rel2`/`rel3` at a gate | `os._exit(3)` — the same route the bound would reach |
| malformed, overlong, duplicate, or trailing report bytes | the stage's failure route; never a partial acceptance |
| `EPIPE` at `c8` / `c12` / `c16` | stage-1 / stage-2 / stage-2 route |
| any other read or write `errno` | the stage's failure route (fail-closed) |
| **middle child dies between `m7` and `m8`** | `c13`'s bound fires (now executable) ⇒ stage-2 `killpg(process_group_id)` reaches the grandchild ⇒ death proved ⇒ ordered removal ⇒ lock released. **No deadlock** |
| CLI dies between `c4` and `c7` | `m0`'s **bound** fires (the middle child holds its own `rel1` write copy until `m1`, so EOF is not guaranteed here) ⇒ `_exit(3)` |
| CLI dies between `c9` and `c12` | `m5` sees **EOF** (all `rel2` writers closed) ⇒ immediate `_exit(3)` |
| CLI dies between `c12` and `c16` | `g0` sees **EOF** on `rel3` (the CLI is its sole writer) ⇒ `_exit(3)` |
| grandchild stalls at `g0` with the CLI alive but not releasing | the `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` gate bound fires ⇒ `_exit(3)` ⇒ lock reference released |
| crash after `RESULT_MANIFEST.json`, before `SETTLEMENT.json` | the record-first reducer completes the signed invalid terminal set and installs `QUARANTINE.json` with `result_manifest_sha256_or_null` = the manifest's hash (§V214.2.2 Q1) |
| `QUARANTINE.json` present with a non-null value that does not match the manifest bytes | record-first invalidity naming both paths |
| `QUARANTINE.json` present with a null value while a manifest exists | record-first invalidity naming both paths |
| manifest absent while `QUARANTINE.json` binds a non-null value | **REFUSE** the disposition; release nothing |
| both `SETTLEMENT.json` and `QUARANTINE.json` durable | record-first invalidity; release nothing |
| disposition offered for a quarantined operation **with** an orphan manifest | branch `B-QM` verifies it against the quarantine binding; on success, release exactly `bytes_reserved` once |
| disposition offered for a quarantined operation **with no** manifest | branch `B-QN`; manifest checks vacuous **only** here |
| GC crash between `D1` and `D4` | `accepted.json` present ⇒ G3 re-selectable; `ack.json` present ⇒ G1 holds ⇒ re-verify `D0`, resume at `D1` |
| GC crash between `D4` and `D7` | only `accepted.json` remains ⇒ the **finalization rule** `D6` re-verifies prefix + G3 from `accepted` and deletes it |
| GC crash between `D7` and `D9` | empty directory ⇒ predicate-free empty-directory completion |
| GC `rmdir ENOTEMPTY` / other `errno` | record-first invalidity naming the path; nothing deleted blindly |
| singleton record inspected before `c1a` | **forbidden**: no preflight read that can lead to adoption, removal, kill, or mutation may occur before the lock is acquired |
| stuck-holder route kills a stale holder | it removes **nothing**; `c1b` performs the §U6.3 ordered removal under the acquired lock |
| two or more I-conditions true in one observation | `invalid_condition` = the **first** in `I1→I7` order; `diagnostic_conditions` = the sorted set of all true ones; routing is identical either way |
| valid exact-table ack and a passed deadline in one observation | `INVALID` with `invalid_condition = I1` (I-before-S, single `now_ns` sample) |
| only a stale or wrong-table ack, bound passed | `INVALID` with `invalid_condition = I2` |
| exact ack present, a member in state `R`/`S`/`D` pre-resume | `INVALID` with `invalid_condition = I3` |
| A3-R1a / A3-R1b / A3-R2 / A3-R3 | **no observation, no route, no signal**; the recorded hash describes only the read stream |

---

## V214.10. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host
change, process, signature, activation, entropy, T/Q/C work, or scientific
execution is permitted. Obligations become due only after both independent
v2.1.4 confirmations accept these bytes **and** the author signs the amendment
token.

§W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–96, and §U11 rows 97–120 carry
forward, with five replacements:

- **row 101 replaced:** CLI death at each cut between `c4` and `c16` ⇒ the
  stage's bound **or** EOF (whichever the descriptor ownership table predicts
  for that cut) ⇒ `_exit(3)` ⇒ every lock reference released.
- **row 105 replaced:** `m3` inequality and middle-child death at each of the
  six cuts (`m0`, `m1`–`m4`, `m4`–`m7`, `m7`–`m8`, `m8`–`m9`) each have one
  continuation and remove records in §U6.3 order under the acquired lock.
- **row 112 replaced:** GC deletes in exactly
  `committed → reply → ack → accepted` order with the four pinned `fsync`s and
  the `D6` finalization step.
- **row 113 replaced:** crash injected between every pair of `D0`–`D10`: every
  pre-`D7` cut re-selects G3 from `accepted.json`; the `D4`–`D7` cut uses the
  finalization rule; post-`D7` uses the empty-directory rule; no state is
  permanently non-GC-able and no G3 predicate is unidentifiable.
- **row 117 replaced:** an orphan manifest without `SETTLEMENT.json` is bound
  by `QUARANTINE.json` and disposable through branch `B-QM`; a quarantine with
  no manifest is disposable through `B-QN`; neither promotes, and both retain
  `bytes_reserved` until a verified disposition.

Added:

| # | Test | Covers |
|---|---|---|
| 121 | all four bootstrap pipes are `O_NONBLOCK` on both ends and `PC_PIPE_BUF ≥ 4096` is verified per write end; assert **no blocking syscall** exists in the bootstrap | R1, Sol C1 |
| 122 | `BOUNDED_READ`: `EAGAIN` paced retry, `EINTR` retry, EOF-incomplete, malformed, overlong, trailing/duplicate frame, and other-`errno` each take the pinned branch | R1 |
| 123 | `BOUNDED_WRITE`: `EAGAIN` retry, `EINTR` retry, `EPIPE` ⇒ `PEER_GONE`, other-`errno`, and the all-or-EAGAIN `PIPE_BUF` property (no partial write) | R1 |
| 124 | **middle child dies between `m7` and `m8`**: `c13`'s bound fires, stage-2 `killpg` reaches the grandchild, death proved, records removed, lock released — the exact v2.1.3 deadlock is gone | R1, Sol C1 |
| 125 | exactly one frame per stage read is enforced, and the `m4`→`m5`→`c9`→`c12`→`m8` ordering makes two concurrent frames impossible | R1 |
| 126 | the grandchild's gate bound is `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`; a healthy bootstrap always releases inside it; the `rel3` EOF property still holds because the middle child closed `rel3`-write at `m1` | R1 |
| 127 | the grandchild's literal first instruction is still its `rel3` gate read; no descriptor close or other syscall precedes it | R1 (accepted closure preserved) |
| 128 | `QUARANTINE.json` binds `result_manifest_sha256_or_null` exactly when a manifest exists at install; Q1–Q4 of the record-first reducer are idempotent under crash injection | R2, Sol C2 |
| 129 | branch selection `B-P`/`B-QM`/`B-QN` is exclusive; every other combination refuses and releases nothing | R2 |
| 130 | an orphan-manifest quarantine with every custody location absent **can be disposed** through `B-QM`, releasing exactly `bytes_reserved` once — the route that was impossible in v2.1.3 | R2, Sol C2 |
| 131 | `B-QM` performs no settlement comparison, opens no output content file, and runs the prohibited-value check over the orphan identifier set | R2 |
| 132 | `B-QN` requires both the null binding and physical manifest absence; manifest-dependent checks are vacuous only there | R2 |
| 133 | GC order `committed → reply → ack → accepted`, with G3 re-selected from `accepted.json`'s `command`/`effect_plan` at `D0` and again at `D6` | R3, Sol M1 |
| 134 | after `D4`, with only `accepted.json` present, the finalization rule completes GC using the permanent tombstone plus `accepted` | R3 |
| 135 | every one of the nine per-command G3 bindings is selected correctly from `accepted.json`, including the observation form's vacuous case | R3 |
| 136 | no `reply.json` is deleted before `i ≤ acknowledged_prefix_occurrence`; retry before/during/after GC returns the identical `ALREADY_ACKNOWLEDGED` | R3, B1 |
| 137 | `SPAWN.lock` is acquired before any preflight read that can adopt, remove, kill, or mutate; an implementation that preflights first fails the test | R4, Sol M2 |
| 138 | the stuck-holder route reads, validates, kills, proves death, and retries — and removes **nothing**; the removal happens at `c1b` under the acquired lock | R4 |
| 139 | `EEXIST` at `c2`/`c7`/`c11`/`c15` is resolved under the held lock by P1/P2/P3 | R4 |
| 140 | I1–I7 are evaluated in pinned priority; `invalid_condition` is the first true one and `diagnostic_conditions` the sorted set; routing is identical for every condition | R5, Sol M3 |
| 141 | I2 fires at the bound when only a stale, wrong-table, wrong-generation, or malformed ack was seen; a valid exact-table ack prevents it | R5 |
| 142 | every one of the fifteen race-table rows yields exactly the tabulated state and condition; no row has zero or two continuations | R5 |
| 143 | no text anywhere in the chain claims the recorded hash describes the promoted bytes; A3-R1a/R1b/R2/R3 have no `HASH` route and are never signalled | R6, Sol M4 |
| 144 | the decision file's line 8 is 43 bytes including LF and the total is 504; the §N1.8 digests and the §U5.6/§U8.3 digests all still reproduce | R7, Sol m1 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object.

---

## V214.11. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The bootstrap now has one
descriptor/flag/ownership table, two pinned helper state machines covering
every `errno`, and a stage-route mapping for every read and write
(§V214.1.2–§V214.1.5); the disposition verifier has three exclusive branches
selected by durable objects alone (§V214.2.3); GC has an eleven-step order with
a finalization rule and a per-cut proof that uses only the files then present
(§V214.3.1–§V214.3.3); the lock/preflight order is single-valued with an
explicit non-mutating unlocked route (§V214.4); the watchdog partition is a
three-step evaluation over a pinned condition priority with a fifteen-row race
table (§V214.5); and the A3 statement distinguishes read stream, final inode,
and promoted bytes (§V214.6). No clause resolves to "as reviewed", "as
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

**No author cell is reopened.** A3 gains only honesty: §V214.6 removes the last
promoted-byte over-claim and names four residuals instead of three, with no new
route. B1 is untouched: §V214.3 changes only the physical deletion order, and
prefix-first classification — signed B1's "until a durable acknowledgement"
boundary — is preserved, with no owed reply deleted before acknowledgement. C1
keeps a watchdog that witnesses and freezes and never holds runtime authority
or settles; §V214.5's marker fields are supervisor bookkeeping in a namespace
the watchdog cannot reach, and `ACK_PENDING` still creates no evidence and no
terminal. D1 keeps no idle exit, and §V214.1 removes the last construction in
which a bootstrap participant could retain the shared lock without a
deadline. K1 keeps its five signed constants, its no-replenishment rule, its
complete-custody release condition, and its literal write-once/hash-once
counts; §V214.2 **restores** a legitimate release route that v2.1.3 made
unreachable, without weakening `bytes_reserved` accounting anywhere. **No new
author-choice token is proposed, and none was found to be unavoidable.**

**Negative space.** This correction creates nothing executable and authorizes
no implementation, commit, host change, process, supervisor, controller,
worker, watchdog, adapter, middle child, endpoint, pipe, FIFO, journal
instance, tombstone, spawn record, lease, capability, operation, output bound,
framed transport, result manifest, promoted object, capacity artifact, custody
disposition, author decision file, freeze witness, fallback witness,
replacement-freeze record, quarantine record, entropy, E1/E2/E3 spend, world,
learner, candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim
movement. It predicts no qualification and no C1–C6 outcome. Process
invalidity, resource exhaustion, and missing evidence remain infrastructure
facts and are nowhere treated as scientific evidence. No example in this
document was written to any file, and every illustrative value is patterned
synthetic content that cannot correspond to a real generation, operation, or
activation record.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Its only next authorization step is
independent bounded X/Y confirmation of the **v2.1.4 bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
