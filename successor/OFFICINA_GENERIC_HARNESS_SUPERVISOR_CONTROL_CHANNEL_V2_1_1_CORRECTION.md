# Officina supervisor and control-channel amendment — v2.1.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance.** This correction was written by **Claude
Code Opus 5 acting as the specification author**, because Claude Code
Fable 5 was unavailable. It is **not** independent review evidence and
**must not** be counted as an X-line or Y-line review of its own bytes,
exactly as `reviews/officina_supervisor_v2_1_authorship_note.md` records
for v2.1. Its only next authorization is independent v2.1.1 X/Y
confirmation on the v2.1.1 bytes themselves.

This document is a **precise replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
(v2) and
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
(v2.1), both preserved unedited as review evidence. Everything in v2 and
v2.1 not named in the §Z0 replacement index carries forward **verbatim**.
It dispositions every Critical, Major, and Minor finding of the two
independent v2.1 reviews
(`reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md`,
`reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md`).
It is not commentary, and it is not a silent rewrite: every superseded
clause, sentence, and table row is named below.

Signed author cells embedded, **none reopened, weakened, or
reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

K1 is implemented **literally**, including the clause v2.1 violated:
aggregate custody includes live reservations, pending settlement,
quarantine, and retained `runtime/T_PROMOTED/**`; **rename, promotion,
settlement, failure, and unused reservation replenish nothing**; capacity
is released only after an authorized disposition proves custody absent
(`successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
lines 32–36).

Author token candidate, still **not signable**, and not made signable by
this document:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature,
review, or runtime artifact. Starts no process, endpoint, pipe, FIFO,
journal, watchdog, worker, or output transport. Creates no entropy,
activation, capability, world, learner, candidate, datum, Q/C object, or
outcome. Authorizes no implementation. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.

## Governing hashes (recomputed for this correction)

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
cf4fab454e27f0c4c2ad6a7583c70a79a7aff8ed1711bf279c13683b85f74c60  reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md
c97f98a0c0050f28e0849dc1782f9a403b4c99f58ee64636215dab114a47b1cd  reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
cf0f1bd85fc9bdc4b8f7bfd8393eedddc4dc89633687224f73a8024e0dee2e21  reviews/opus5_officina_supervisor_control_channel_v2_1_1_repair_prompt.md
```

## Engineering constants (control plane only; no scientific or resource cell)

Unchanged from v2.1 except the rows marked. The five `T_OUTPUT_*` values
are author-signed and **immovable**.

```text
T_CONTROL_FRAME_MAX_BYTES               = 4096
T_CONTROL_READ_BUFFER_MAX_BYTES         = 8192
T_CONTROL_READ_TIMEOUT_SECONDS          = 10
T_CLIENT_REPLY_TIMEOUT_SECONDS          = 30
T_SUPERVISOR_POLL_INTERVAL_NS           = 50_000_000
T_WATCHDOG_POLL_INTERVAL_NS             = 100_000_000
T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS        = 1_000_000_000
T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS       = 60_000_000_000
T_WATCHDOG_QUIESCE_MAX_PASSES           = 8
T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS     = 100_000_000
T_SPAWN_SELF_STOP_TIMEOUT_NS            = 10_000_000_000
T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS        = 10_000_000_000
T_MIN_HEARTBEAT_INTERVAL_NS             = 1_000_000_000   # normative rule: §Z9.1
T_ARGV_MAX_ELEMENTS                     = 32              # replaces 64  (§Z9.2)
T_ARGV_MAX_BYTES                        = 768             # replaces 4096 (§Z9.2)
T_REQUEST_ENVELOPE_MAX_BYTES            = 1536            # new (§Z9.2)
T_ARGUMENTS_MAX_BYTES                   = 2560            # new (§Z9.2)
T_REPLY_MAX_BYTES                       = 2048            # new (§Z9.2)
T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS         = 30_000_000_000  # new (§Z3.5)
T_SPAWN_BOOTSTRAP_MAX_AGE_NS            = 60_000_000_000  # new (§Z3.5)
T_MAX_UNACKED_OCCURRENCES_PER_SCOPE     = 64              # new (§Z1.9)
T_CTRL_FD_LOW                           = 3               # new (§Z3.3)
T_CTRL_FD_HIGH                          = 4               # new (§Z3.3)
T_OUTPUT_PER_STREAM_MAX_BYTES           = 67_108_864      # signed K1
T_OUTPUT_AGGREGATE_MAX_BYTES            = 34_359_738_368  # signed K1
T_OUTPUT_FS_SAFETY_MARGIN_BYTES         = 8_589_934_592   # signed K1
T_OUTPUT_COPY_CHUNK_BYTES               = 4_194_304       # signed K1
T_OUTPUT_PATH_MAX_BYTES                 = 1_024
T_OUTPUT_PATH_COMPONENT_MAX_BYTES       = 255
SIGCONT = 18; SIGSTOP = 19; SIGKILL = 9; SIGTERM = 15; SIGNAL_0 = 0
```

Every new constant is a control-plane bound. None is a scientific
estimand, resource envelope, E1/E2/E3 value, or K1 ceiling.

---

## Z0. Exact replacement index (v2.1 → v2.1.1)

Everything in v2 + v2.1 not named here carries forward verbatim,
including all of §V2.8, §V2.1.1, §V2.1.3, §V2.1.7, §V2.2.1 (as already
amended by §W6.4), §V2.7.5, §V2.9.2, §V2.9.4, §V2.14, §W2.6, §W3.1,
§W4.1, §W4.2 (except the one preflight line named below), §W5.3, §W5.4
(except the two lines named below), §W6.1, §W6.3, §W6.4, §W6.5, §W6.6,
and §W11's compatibility classification.

| v2.1 locus (exact clause / sentence / table row) | Action in v2.1.1 |
|---|---|
| §W1.1 entire section, including the four numbered client-allocation steps and the "highest `n` has **no** sibling … ⇒ this invocation is a **retry**" rule | **replaced** by §Z1.1–§Z1.4 (explicit `NEW`/`RETRY` mode; supervisor-authoritative allocation) |
| §W1.1 bullet "a **retry** re-reads the unfinished slot ⇒ the identical key" and the bullet "while an occurrence is unfinished the client cannot intend a *second* one in the same scope" | **deleted** (§Z1.1) |
| §W1.1 paragraph "A client that skips the durable slot damages only its own ability to re-read a cached reply…" | **replaced** by §Z1.8 (client files are convenience only, deletable at any time, never runtime authority) |
| §W1.2 request key list ("Request keys **exactly**: …") | **replaced** by §Z10.1 (adds `occurrence_mode`; `idempotency_key` → `idempotency_key_or_null`) |
| §W1.2 sentence "`request_sha256` … survives **only** as the reply's transport binding" | **extended** by §Z10.2 (reply envelope adds four control identifiers) |
| §W1.2 journal decision case 1 ("journal hit on `idempotency_key` with **equal** `semantic_request_sha256` ⇒ run the reducer") | **replaced** by §Z1.5's six-row classification (adds the allocating-claimant test) |
| §W1.3 `t-request-accepted.v1` key list | **replaced** by §Z10.3 (adds `occurrence_mode`, `allocating_client_start_identity`, `allocating_client_boot_identity`) |
| §W1.4 sentence "A `REFUSED` outcome is a legitimate terminal effect with **empty** event and artifact tuples" | **replaced** by §Z1.7 (a refusal terminal records exactly the artifacts that became durable; only pre-artifact refusals have empty tuples) |
| §W1.4 `effect_plan` row `HEARTBEAT` | **replaced** by §Z4.2 (adds `watchdog_table_seq`) |
| §W1.4 `effect_plan` row `CLOSE` | **replaced** by §Z4.2 (adds `watchdog_table_seq`) |
| §W1.4 `effect_plan` row `PAUSE` | **replaced** by §Z4.2 (adds `watchdog_table_seq`) |
| §W1.4 `effect_plan` row `CLAIM` | **replaced** by §Z3.2 (`argv_template_sha256` replaces the circular `argv_sha256` binding; `complete_argv_sha256` retained) |
| §W1.4 `effect_plan` row `OPERATION_ADMIT` | **replaced** by §Z5.1 (adds `running_path`) |
| §W1.4 `effect_plan` row `OPERATION_STATUS` ("(ack form only)") | **replaced** by §Z1.6 (both forms are planned; observation form has an empty effect tuple) |
| §W1.5 guard `head_ok := current_ledger_head ∈ {pre_ledger_head_sha256} ∪ {plan's declared event hashes}` and the line `if not head_ok → record-first invalidity naming the plan` | **replaced** by §Z2.1–§Z2.3 (descendant-aware admission; four routes) |
| §W1.5 branch `if reply.json exists → re-wrap effect_reply in a fresh envelope` | **replaced** by §Z5.2 (must probe `running_path` first for `OPERATION_ADMIT`) |
| §W1.5 probe row `CLAIM` ("… ⇒ kill by marker (§W2.4), reap, then spawn afresh under the same intent") | **replaced** by §Z2.4 (behavioral completion only within the accepting generation) |
| §W1.5 probe row `START` | **replaced** by §Z4.2 (publication+ack step retained; cross-generation behavior forbidden) |
| §W1.5 probe row `OPERATION_ADMIT` ("a live unbound worker is killed and respawned under the same intent") | **replaced** by §Z5.2 + §Z2.4 |
| §W1.5 paragraph "`OPERATION_STATUS` in its **observation** form (`ack_delivery = false`) has no plan, no journal entry, and no effect" | **deleted and replaced** by §Z1.6 |
| §W1.6 sentence "`ack.json` with `ack_source = SUCCESSOR_OCCURRENCE` is written when a request in the same `intent_scope_sha256` with `occurrence_index = n+1` is admitted" | **replaced** by §Z1.7 (successor must carry the exact prior `effect_reply_sha256`) |
| §W1.6 clause "or with `ack_source = PROCESS_TERMINAL` when the owning process's final process record becomes durable (closing every scope bound to that `process_id`)" | **replaced** by §Z1.7 (own-terminal scopes excluded; `CLOSE` cannot acknowledge its own reply) |
| §W1.6 `ack_source` enum `{SUCCESSOR_OCCURRENCE, PROCESS_TERMINAL, DELIVERY_ACK}` | **replaced** by §Z10.4 (`{SUCCESSOR_OCCURRENCE, PROCESS_TERMINAL, DELIVERY_ACK, CLIENT_ECHO}`) |
| §W1.7 `t-request-tombstone.v1` key list, including `acknowledged_high_water_occurrence` and `last_effect_reply_sha256` | **replaced** by §Z1.9 (`next_occurrence_index` + `acknowledged_prefix_occurrence`; the reply-hash key is deleted) |
| §W1.7 disposition table rows 3 and 4 ("equal recorded `last_effect_reply_sha256` scope" / "mismatching derivation") | **replaced** by §Z1.5 (decidable from the incoming frame and retained authority alone) |
| §W1.7 GC rule ("GC may delete … only when all three hold") | **replaced** by §Z1.9 (contiguous acknowledged prefix; same lock epoch as the ack) |
| §W1.7 "**Growth bound.**" paragraph | **replaced** by §Z1.9 (per-scope unacknowledged-occurrence ceiling) |
| §W2.1 sentence "There is no private argv entry surface to guard." | **replaced** by §Z3.3 (exactly one refusal-first adapter token `--officina-bootstrap`) |
| §W2.1 bullet "**Watchdog:** the supervisor calls `os.fork()`…" (identity by `getppid()` and pipe checks only) | **extended** by §Z3.6 (durable fork-child record) |
| §W2.2 sentence "The grandchild **scrubs every inherited descriptor except the `SPAWN.lock` fd and its own sealed pipes**, redirects stdio …, creates endpoints, forks the watchdog, awaits the watchdog's first ack, installs `SUPERVISOR_IDENTITY.json` …" | **replaced** by §Z3.5 (bootstrap pipe + `SPAWNING_CHILD.json` first; bounded first-ack wait) |
| §W2.2 sentence "On timeout it kills the grandchild by the `spawning_id` marker (§W2.4)" | **replaced** by §Z3.5 (kill by recorded pid + start identity; never by `cmdline`) |
| §W2.2 first sentence "Under `flock(LOCK_EX)` on `SPAWN.lock`" | **replaced** by §Z3.5 (`LOCK_EX\|LOCK_NB` with bounded retry) |
| §W2.3 `t-spawn-intent.v1` key list and `spawn_intent_id` preimage (`argv`, `argv_sha256` over the complete argv) | **replaced** by §Z3.2 (`argv_template`, `argv_template_sha256`; role enum loses `WATCHDOG`) |
| §W2.3 role enum `(CONTROLLER\|WORKER\|WATCHDOG)` | **replaced** by §Z3.2 (`CONTROLLER\|WORKER`) + §Z3.6 (fork-child record) |
| §W2.4 sentence "`argv` and `argv_sha256` in the intent are over the **complete** argv." | **deleted** (§Z3.2) |
| §W2.4 four appended tokens and their order | **replaced** by §Z3.3 (thirteen fixed leading elements; fixed marker index) |
| §W2.4 sentence "The same predicate, with `spawning_id`, discovers a half-initialized supervisor grandchild." | **deleted** (§Z3.5); the `/proc` predicate is retained **only** for `exec`ing children |
| §W2.4 discovery predicate "scan `/proc/*/cmdline`, NUL-split, and select every process whose argv contains that exact `spawn_intent_id_hex`" | **replaced** by §Z3.4 (fixed-index match) |
| §W2.5 handshake ("Controllers and workers use the identical handshake") | **extended** by §Z3.3 (adapter root, target preflight) |
| §W2.8 process/FD table rows Supervisor, Controller, Worker, Freezer watchdog | **replaced** by §Z10.6 |
| §W2.9 phase 1 step 2 ("identity-kill every discoverable stale child and grandchild by the §W2.4 predicate") | **replaced** by §Z3.5 / §Z3.6 (record-based for grandchild and watchdog) |
| §W2.9 phase 2 numbered order (1 capacity, 2 reducer, 3 settle, 4 intents, 5 serve) | **replaced** by §Z2.5 (validity-first phases 2A/2B) |
| §W3.2 sentence "…are published **before** the first `SIGCONT`, before any capability becomes usable, and before any operation admission." | **replaced** by §Z4.1 (publication trigger restored: after **every** successful locked claim-start, renew, and remove) |
| §W3.2 sentence "**On renewal the old deadline remains authoritative until the successor table is acked.**" | **retained and completed** by §Z4.1–§Z4.3 (drain-before-freeze; `WATCHDOG_UNACKED` continuation) |
| §W3.3 step 4 ("on the pass that proves every member stopped/dead, sample `freeze_ns` … `quiescence = PROVED`") | **replaced** by §Z4.4 (strict-progress requirement and bounded later sampling) |
| §W3.3 `t-freeze-observation.v1` path `WATCHDOG/FREEZE/<process_id>.json` | **replaced** by §Z4.5 (`WATCHDOG/FREEZE/<witness_id>.json`) |
| §W3.3 sentence "This is the one mechanical evidence path" | **extended** by §Z4.6 (supervisor acceptance predicate; unverifiable evidence is never evidence) |
| §W3.3 sentence "`quiescence = PROVED` … the whole declared tree is proved stopped/dead" | **qualified** by §Z4.4 (a process-tree fact, not a backend fact) |
| §W3.4 clause "⇒ `overrun_ns = freeze_ns − deadline_ns` (> 0 by construction)" | **replaced** by §Z4.4 (strict progress proved, not asserted) |
| §W3.5 row "Renewal not yet acked" | **replaced** by §Z4.3 |
| §W3.5 row "Freeze observation present at supervisor start" | **replaced** by §Z4.6 (acceptance predicate first) |
| §W4.2 preflight line `require st_dev(operations root) == st_dev(runtime/T_PROMOTED root)` | **replaced** by §Z9.4 (`st_dev(successor/officina/runtime/)`) |
| §W4.2 preflight block | **extended** by §Z9.5 (interpreter argv0 existence/executability) |
| §W4.4 nine-step admission order (steps 7–9) | **replaced** by §Z5.1 (ten steps; `RUNNING.json` before `SIGCONT`, reply after) |
| §W4.5 sentence "**updates one streaming SHA-256 per file in the same pass**. Each byte is read exactly once; there is no second pass and no post-exit hash pass." | **replaced** by §Z8.3 (each byte is *written* once; one bounded pre-settlement verification pass) |
| §W4.5 cut-table row "EOF exactly at a frame boundary **and** worker status `exit_reason = COMPLETED` **and** group proved dead" | **replaced** by §Z7.3 (zero-frame case decided; status-frame absence added) |
| §W4.5 cut-table row "a chunk would cross `bytes_reserved` … (the worker's next `write` takes `EPIPE`/`SIGPIPE`)" | **replaced** by §Z7.4 (termination is guaranteed by `killpg` + proved death, not by the close) |
| §W4.6 `accounted_total` formula | **replaced** by §Z6.1 |
| §W4.6 table row `<operation_id>.settled.json` ("**re-measures the same custody** … releases only the over-declaration") | **replaced** by §Z6.2 (`actual_bytes` diagnostic only; releases nothing) |
| §W4.6 table row `<operation_id>.disposed.json` key list | **replaced** by §Z6.4 |
| §W4.6 crash-reconstruction steps 1–4 | **replaced** by §Z6.3 |
| §W4.6 paragraph "**Retention and disposal.** … Disposal requires a signed author disposition artifact naming operation ids, kinds, terminals, byte counts, and destination" | **replaced** by §Z6.4–§Z6.6 (the complete closed authority) |
| §W4.8 transition rows `PENDING_SETTLEMENT → PROMOTED`, `any → QUARANTINED`, `PROMOTED → ALREADY_DELIVERED`, `any retained → released` | **replaced** by §Z6.7 |
| §W4.8 transition row `ADMITTED → RUNNING` durable trigger "worker `SIGCONT`" | **replaced** by §Z5.1 (`RUNNING.json`) |
| §W5.1 sentence "The reply's construction and its transport path do not branch on worker output, path count, byte count, exit reason, or internal phase, so the transition time between internal phases reveals nothing." | **replaced** by §Z8.1 (honest A3 boundary) |
| §W5.2 reply matrix header row and `REFUSED` row | **extended** by §Z10.2 (envelope carries `next_occurrence_index`; the `detail` key sets are unchanged) |
| §W5.2 closed refusal token list | **replaced** by §Z10.5 (adds `OCCURRENCE_INDEX`, `SUPERSEDED_PLAN`) |
| §W5.4 bullet "`T_CLIENT_REPLY_TIMEOUT_SECONDS` continuation … leaves its intent slot **unfinished**, and the next invocation of the same command is a retry by §W1.1" | **replaced** by §Z1.8 (the next invocation is an explicit `RETRY` of the recorded handle) |
| §W5.5 argv bound values | **replaced** by §Z9.2 |
| §W6.2 sentence "The supervisor holds each output file's `O_WRONLY` descriptor … any mismatch is the `HASH` quarantine class." and the sentence "A deliberate same-UID modification of `out/` between write and settle **is detected** by this check but is not *prevented*" | **replaced** by §Z8.2–§Z8.3 |
| §W7 durable-object table rows: Spawn intent, Journal accepted, Scope tombstone, Client intent slot, Client intent terminal, Freeze observation, Capacity settled, Capacity disposition, Worker status | **replaced** by §Z10.7 |
| §W7 table (missing rows) | **extended** by §Z10.7 (`SPAWNING_CHILD.json`, `WATCHDOG_CHILD.json`, `RUNNING.json`, author custody disposition) |
| §W8 crash-cut rows: "Grandchild alive, identity not installed, CLI dies", "Spawn intent durable, no child", "Child stopped, no claim", "Key ≤ tombstone high water", "Lease installed, watchdog not acked", "Freeze observation durable, settlement pending", "Bound + admission durable, no worker" | **replaced** by §Z11 |
| §W8 (missing rows) | **extended** by §Z11 (release-locator cuts, allocation cuts, verification-pass cuts, disposition cuts) |
| §W9 finding-disposition table, every row reading "closed" without qualification | **replaced** by §Z12.1 (each inherited closure is marked *closed in v2.1, confirmation pending v2.1.1*) |
| §W10 acceptance matrix | **extended** by §Z12.2 (rows 51–74; no row is an implementation authorization) |
| §W11 "**Two-implementer determinacy.**" paragraph | **extended** by §Z13 (the new determinacy claims) |

---

## Z1. Explicit occurrence allocation and total B1 semantics (R1)

Closes X21-C1(B1 residue), X21-C5, X21-M5, X21-M6, Sol C1 (items 1–5),
and Sol's eight-row B1 trace table.

### Z1.1 Two explicit modes; inference is deleted

The frame declares which of the two things it is. Nothing is inferred
from client-side state:

- **`occurrence_mode = NEW`** — an intent to produce a *new* exactly-once
  effect in the scope. It names the occurrence index it intends to
  allocate. The supervisor allocates it, or refuses and tells the client
  the authoritative next index (§Z1.5). The returned reply envelope
  carries the allocated occurrence: **that envelope is the durable
  occurrence handle** (§Z10.2).
- **`occurrence_mode = RETRY`** — an intent to re-address exactly one
  already-allocated occurrence, named by `(intent_scope_sha256,
  occurrence_index)`. It never allocates and never applies a second
  effect.

§W1.1's inference rule — an unfinished highest local slot silently making
every later invocation a retry — is **deleted**. No unfinished, missing,
stale, deleted, duplicated, or foreign client file can convert a `NEW`
into a `RETRY` or a `RETRY` into a `NEW`, because neither the client's
slot files nor its counters are read by the supervisor at any point.

### Z1.2 Identity derivations (unchanged shapes, supervisor-recomputed)

`intent_scope_sha256` and `idempotency_key` keep exactly the §W1.1
derivations:

```text
intent_scope_sha256 = SHA-256(canonical {
  schema: "philosophia.officina.t-intent-scope.v1",
  activation_record_sha256, command, arguments_sha256 })

idempotency_key = SHA-256(canonical {
  schema: "philosophia.officina.t-intent-key.v1",
  intent_scope_sha256, occurrence_index })            # 64 lowercase hex
```

`semantic_request_sha256` keeps exactly the §W1.2 derivation. All three
are **recomputed and checked by the supervisor** from the frame's own
`command`, `arguments`, `intent_scope_sha256`, and `occurrence_index`; a
mismatch is `INVALID`/`INTENT_KEY` with no state movement. On a `NEW`
frame `idempotency_key_or_null` may be `null` (the client may not know
which index it will receive if it is refused and re-anchored); on a
`RETRY` frame it is **required** and must equal the recomputed value.

### Z1.3 The allocator (supervisor-authoritative, one lock epoch)

The scope's authoritative allocation state is the **scope tombstone**
(§Z1.9), which is never deleted, plus the present journal directories.
Client state is never consulted.

```text
next(scope) := max( tombstone(scope).next_occurrence_index ,
                    1 + max{ i : JOURNAL/<key(scope,i)>/accepted.json exists } ,
                    1 )
```

Allocation of index `i` for a `NEW` frame, under `T_RUNTIME.lock`, in one
lock epoch, in exactly this order:

```text
1. recompute the derivations; refuse/invalidate per §Z1.5 unless i == next(scope)
2. install JOURNAL/<key(scope,i)>/accepted.json                  (no-replace)
3. atomically replace TOMBSTONES/<scope>.json with
   next_occurrence_index = i + 1 (monotone; a lowering replace is
   record-first invalidity)
```

Atomicity, locks, and `EEXIST` continuations:

- steps 2 and 3 occur inside one `T_RUNTIME.lock` epoch; no frame is
  served between them;
- `EEXIST` at step 2 means another epoch already allocated `i` (only
  reachable after a crash between 2 and 3, or an A3-procedural writer):
  the supervisor re-reads the existing `accepted.json` and re-enters
  §Z1.5 from row 2 with it — it never overwrites, merges, or deletes;
- crash **between 2 and 3** leaves `next_occurrence_index = i` while
  index `i` exists. The `max` in `next(scope)` repairs it at the next
  generation start or at the next allocation in that scope, and the
  repaired value is written back under the lock. No index is ever
  reused, because the journal scan dominates the tombstone;
- crash **before 2** leaves nothing: the same `NEW(i)` is re-sendable and
  allocates once;
- crash **after 3** is the ordinary open-plan case (§Z2).

Because allocation is a supervisor action under the single runtime lock,
**two concurrent `NEW` frames in one scope cannot receive the same
occurrence**: one wins step 2, the other is refused with the
authoritative next index and re-anchors (§Z1.5 row 3). Client files,
counters, `.done` markers, PIDs, clocks, and generations enter the
allocation nowhere.

### Z1.4 Client-side state is convenience only

The client's durable slot is redefined as an **optional cache of the
handle it received**, written *after* the reply, never before, and
readable only by the client:

```text
runtime_control/T_CLIENT_INTENTS/<intent_scope_sha256>.<occurrence_index>.json
  schema philosophia.officina.t-client-intent.v1, keys exactly:
  schema, scientific_outcome, activation_record_sha256, command,
  arguments_sha256, intent_scope_sha256, occurrence_index,
  idempotency_key, occurrence_mode ("NEW"), recorded_utc
runtime_control/T_CLIENT_INTENTS/<intent_scope_sha256>.<occurrence_index>.done.json
  schema philosophia.officina.t-client-intent-terminal.v1, keys exactly:
  schema, scientific_outcome, intent_scope_sha256, occurrence_index,
  effect_reply_sha256, completed_utc
```

Normative consequences, all required:

- the client may delete, truncate, or lose **any or all** of these files
  at any time with **no** effect on exactly-once semantics, on allocation,
  or on forward progress. A client with an absent
  `T_CLIENT_INTENTS/` directory sends `NEW(1)`, is refused with the
  authoritative next index if the scope has history, and re-anchors
  (§Z1.5 row 6). X21-C5's permanent loss of forward progress is
  structurally impossible;
- the only thing a lost slot costs is the client's own ability to
  *re-address* an occurrence whose reply it never saw. That occurrence's
  effect still applied exactly once, and it remains redeliverable to any
  frame that names it;
- these files are never runtime authority, never evidence, never cited,
  and never read by the supervisor.

### Z1.5 Total classification of an incoming frame

Decidable from the incoming frame plus retained supervisor authority
alone. No unavailable old reply hash appears in any predicate (X21-M5,
Sol C1.5). Let `i = occurrence_index`, `S = intent_scope_sha256`,
`T = tombstone(S)`, `D = JOURNAL/<key(S,i)>/`.

| # | Mode | Condition | Result |
|---|---|---|---|
| 1 | `NEW` | `D` absent ∧ `i == next(S)` | allocate (§Z1.3); open the plan |
| 2 | either | `D` present ∧ equal `semantic_request_sha256` ∧ (mode `RETRY`, **or** mode `NEW` with `allocating_client_start_identity` and `allocating_client_boot_identity` equal to the frame's) | run the reducer (§Z2); no second effect |
| 3 | `NEW` | `D` present ∧ equal `semantic_request_sha256` ∧ a different allocating client | `REFUSED`/`OCCURRENCE_INDEX`, `retryable = true`; envelope carries `next_occurrence_index`; no effect |
| 4 | either | `D` present ∧ different `semantic_request_sha256` | `INVALID`/`REPLAY_BYTES`; **no ledger append, no state movement, no G5** |
| 5 | either | `D` absent ∧ `i ≤ T.acknowledged_prefix_occurrence` | `REFUSED`/`ALREADY_ACKNOWLEDGED`, `retryable = false`; envelope carries `next_occurrence_index`; no effect |
| 6 | `NEW` | `D` absent ∧ `i > next(S)` | `REFUSED`/`OCCURRENCE_INDEX`, `retryable = true`; envelope carries `next_occurrence_index`; no effect |
| 7 | `RETRY` | `D` absent ∧ `i ≥ next(S)` | `REFUSED`/`OCCURRENCE_INDEX`, `retryable = false` (a never-allocated handle can never become this occurrence) |
| 8 | either | `D` absent ∧ `T.acknowledged_prefix_occurrence < i < next(S)` | record-first invalidity naming the scope and `i`: an impossible durable layout, because §Z1.9 permits GC only at or below the acknowledged prefix. Not client-triggerable except through the A3 same-UID procedural residual, which is named, not claimed away |

Rows 5–7 are the complete post-GC classification, and they need only two
integers from the tombstone. `STALE_GENERATION` is returned only for a
frame naming a generation that is neither current nor recorded in the
occurrence's `accepted.json` (unchanged from §W1.2).

### Z1.6 Both `OPERATION_STATUS` forms are journaled (Sol C1.3)

Observation-form `OPERATION_STATUS` (`ack_delivery = false`) is journaled
and cached exactly like the other seven commands, with an **empty effect
tuple**:

| Form | `effect_plan` keys exactly |
|---|---|
| `ack_delivery = false` | `operation_id, plan_kind ("OBSERVATION")` |
| `ack_delivery = true` | `operation_id, plan_kind ("DELIVERY_ACK"), delivery_ack_path, acknowledged_release_token_sha256, acknowledged_effect_reply_sha256` |

For the observation form:

- `committed.json` carries **empty** `effect_event_sha256s` and **empty**
  `effect_artifact_sha256s`, and `post_ledger_head_sha256` /
  `post_state_sha256` equal the pre values;
- `reply.json` caches the observed reply object — including the
  `release_token` bytes when the observation fell after promotion;
- **a new poll is a new occurrence**: `NEW(i+1)` observes current durable
  state;
- **an explicit `RETRY(i)` returns byte-identical effect-reply and
  release-token bytes even if the operation's current state has moved
  since** (a `PENDING` observation stays `PENDING` on retry after
  promotion; a `PROMOTED` observation's token bytes stay identical after
  the delivery ack). This is what makes B1 total for the eighth command
  and it is the exact defect Sol C1 named;
- the observation form's plan is **non-behavioral**, so it is completable
  by a cross-generation reducer (§Z2.5).

### Z1.7 Acknowledgement: four sources, each proving observation

`ack.json` (schema `philosophia.officina.t-request-effect-ack.v1`, keys
unchanged except the enum) is installed under `T_RUNTIME.lock` by exactly
one of:

| `ack_source` | Precondition (all mandatory) |
|---|---|
| `SUCCESSOR_OCCURRENCE` | a frame in the same scope with `occurrence_index = i+1` is admitted **and** carries `acked_effect_reply_sha256_or_null` equal to occurrence `i`'s recorded `effect_reply_sha256`. A successor that carries `null` or any other value acknowledges **nothing** (Sol C1.4; §W1.6's unconditional successor ack is deleted) |
| `CLIENT_ECHO` | any frame in the scope carries `acked_effect_reply_sha256_or_null = h` and `h` equals the recorded `effect_reply_sha256` of the **highest unacknowledged** occurrence in that scope. A mismatch is `INVALID`/`REPLAY_BYTES` with no state movement. A `RETRY(i)` carrying `h` both returns the cached bytes and acknowledges them: this is the explicit, one-round-trip delivery acknowledgement for terminal-effect scopes, and it adds no command |
| `PROCESS_TERMINAL` | the owning process's final process record is durable, **and** the scope's own `effect_plan` does **not** name that terminal. Scopes whose plan names `process_record_path`, `stopped_event_sha256`, or `pause_event_sha256` — in particular **every `CLOSE` scope, which produces its own terminal** — are **excluded** and require `SUCCESSOR_OCCURRENCE` or `CLIENT_ECHO`. §W1.6's "closing every scope bound to that `process_id`" is deleted, closing X21-M6 |
| `DELIVERY_ACK` | the release-token delivery ack of §W1.6 (`ack_delivery = true` form) is durable. Unchanged, including "the ack is durable **before** any `ALREADY_DELIVERED` is returned" and "the supervisor never writes the ack before emitting the token" |

A refusal terminal is a legitimate cached effect. §W1.4's "with **empty**
event and artifact tuples" is replaced by: **`committed.json` records
exactly the events and artifacts that became durable under that plan.**
A refusal decided before any durable artifact has empty tuples; a
refusal decided after a partially applied plan (for example §Z4.3's
`WATCHDOG_UNACKED` after a durable charge) records exactly what became
durable. A refusal is never re-evaluated against moved state.

### Z1.8 Client continuations (exact)

| Client event | Exact continuation |
|---|---|
| about to intend a new effect | send `NEW(i)` with `i` = the highest `next_occurrence_index` it has been told, else `1` |
| `REFUSED`/`OCCURRENCE_INDEX`, `retryable = true` | re-anchor to the envelope's `next_occurrence_index` and send `NEW` once more; at most two such re-anchorings per intent, then exit `4` |
| `REFUSED`/`ALREADY_ACKNOWLEDGED` | the occurrence is closed and its bytes are no longer owed: re-anchor to the envelope's `next_occurrence_index` and, if a new effect is still intended, send `NEW` there. Never treat it as a failure of the effect |
| reply timeout `T_CLIENT_REPLY_TIMEOUT_SECONDS` | exit `3`. The next invocation sends `RETRY(i)` for the recorded handle if it has one, otherwise `NEW(next)`. §W5.4's "leaves its intent slot **unfinished** … is a retry by §W1.1" is replaced by this explicit rule |
| observed a terminal reply | may write `.done.json`; `EEXIST` with an equal `effect_reply_sha256` ⇒ continue silently (idempotent); `EEXIST` with a different value ⇒ exit `5`, send nothing further, delete nothing (a foreign same-UID writer; A3 procedural). This closes Opus minor 6 |
| wants to acknowledge explicitly | send `RETRY(i)` (or the next `NEW`) carrying `acked_effect_reply_sha256_or_null` = the reply envelope's `effect_reply_sha256` |

### Z1.9 Tombstone, contiguous prefix, and bounded GC

```text
runtime_control/T_SUPERVISOR/JOURNAL/TOMBSTONES/<intent_scope_sha256>.json
schema philosophia.officina.t-request-tombstone.v1, keys exactly:
schema, scientific_outcome, intent_scope_sha256,
next_occurrence_index (int ≥ 1),
acknowledged_prefix_occurrence (int ≥ 0),
updated_utc
```

`last_effect_reply_sha256` is **deleted** (it was never a decidable
discriminator). Both integers are monotone non-decreasing; a replace that
would lower either is record-first invalidity. This remains the one
control-plane object installed by atomic replace rather than no-replace.

- `next_occurrence_index` advances only in the allocating lock epoch
  (§Z1.3).
- `acknowledged_prefix_occurrence` advances **only** in the same lock
  epoch that installs an `ack.json`, and only to the largest `m` such
  that occurrences `1..m` all have durable `ack.json`. The prefix is
  therefore **contiguous by construction**: an unacknowledged occurrence
  blocks every later one from being GC-eligible.
- **GC** of `accepted/committed/reply/ack` for occurrence `i` is
  permitted only when all three hold, in the same lock epoch that
  installed the ack that advanced the prefix: (a) the owning transition's
  archival commit exists; (b) `ack.json` for `i` is durable; (c)
  `i ≤ acknowledged_prefix_occurrence`. No TTL, no size pressure, no
  outcome-derived deletion. The tombstone is never deleted, so no key can
  ever re-apply an effect (§Z1.5 row 5).
- **Growth bound.** A `NEW` allocation is refused
  `REFUSED`/`UNRESOLVED_JOURNAL` (`retryable = true`) when the scope
  already holds `T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64`
  unacknowledged occurrences. A polling or heartbeating client keeps the
  count at one by echoing the previous reply's `effect_reply_sha256`
  (§Z1.7 `CLIENT_ECHO`/`SUCCESSOR_OCCURRENCE`). Scopes are bounded as in
  §W1.7: one `HEARTBEAT` scope per process, a fixed handful of
  `CLAIM`/`START`/`CLOSE`/`PAUSE`/`RESUME` scopes per process, processes
  bounded by E1, one `OPERATION_STATUS` observation scope per operation,
  and operations bounded by the signed 32 GiB envelope. Journal growth is
  therefore bounded by (scopes × 64) and is **not** a function of polling
  frequency, which was Sol C2's requirement.

### Z1.10 Complete eight-command B1 trace table

Cut columns: **K1** lost request before `accepted.json`; **K2** lost
reply after `reply.json`; **K3** client crash after observing the reply,
before its local `.done`; **K4** supervisor generation change between
send and re-address; **K5** effect partially applied before
`committed.json`; **K6** ack + GC + old re-address; **K7** two concurrent
same-scope clients; **K8** repeated intent/poll in the scope. Every cell
is single-valued.

| Command | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 |
|---|---|---|---|---|---|---|---|---|
| `CLAIM` | `NEW(i)` re-sent; `i == next`; one claim, one `process_sequence` | `RETRY(i)` ⇒ cached `process_id`/`process_claim_sha256` bytes; no second claim | occurrence unacked; `RETRY(i)` identical; `NEW(i+1)` is a *second* claim with a fresh id and sequence (never reuse) | same key; §Z2.5 forbids cross-generation spawn ⇒ cached `SUPERSEDED_PLAN` refusal or, if the claim is durable, the cached positive reply | same generation: resume at the first missing locator (intent → child → claim) by §Z3.4 discovery; cross-generation: child killed in phase 2A, plan closed | row 5 ⇒ `ALREADY_ACKNOWLEDGED`; no second claim | one wins allocation; loser re-anchors to `next` and claims a distinct occurrence ⇒ two distinct claims, no collision | each `NEW` is a distinct claim; `process_sequence` non-reuse enforced at claim validation (§V2.1.7) |
| `START` | `NEW(i)` re-sent; one `T_PROCESS_STARTED` | `RETRY(i)` ⇒ cached `lease_sha256`; no second lease | as K2 plus: `NEW(i+1)` on a started process is refused `NOT_LIVE`/`BUSY` per signed §2c, cached as that refusal | cached reply re-wrapped; accepted-only plans are non-resumable across the loss (lease install and `SIGCONT` are behavior) ⇒ closed invalid terminal | resume: append missing event → install missing lease → publish+await `watchdog_table_seq` → `SIGCONT`, in that order; cross-generation ⇒ frozen/settled, never continued | `ALREADY_ACKNOWLEDGED` | distinct occurrences; the second is refused by signed single-lease rules and cached as that refusal | repeated `NEW` ⇒ each is evaluated against signed state; no lease is ever installed twice |
| `HEARTBEAT` | `NEW(i)` re-sent; exactly one charge event | `RETRY(i)` ⇒ cached `charge_event_sha256`, `cumulative_charge_ns`; **never a fresh reading** | `RETRY(i)` identical; `NEW(i+1)` is a genuinely new heartbeat charging only the new cursor interval — never a double charge (charge = `end − start`) | cached reply re-wrapped in the current generation; `STALE_GENERATION` is not returned | resume with the **recorded** `cursor_reading_ns`: append event → install successor lease → publish+ack table → cache; cross-generation ⇒ the process is frozen/settled, plan closed | `ALREADY_ACKNOWLEDGED`; the charge is not re-applied | distinct occurrences ⇒ two heartbeats, two disjoint cursor intervals, no collapse (Sol C1 defect closed) | rate-limited by §Z9.1 (`BUSY`, no charge, no publication) |
| `CLOSE` | `NEW(i)` re-sent; one final charge, one record, one stopped event | `RETRY(i)` ⇒ cached record/stopped bytes | `RETRY(i)` identical; **`PROCESS_TERMINAL` cannot ack this scope** (§Z1.7), so the bytes stay redeliverable until `CLIENT_ECHO` or a successor carrying the hash | cached reply re-wrapped | resume at the first missing step of signed §2c.6, archival last; cross-generation ⇒ non-behavioral completion only (record/archival/cache), never a new charge | `ALREADY_ACKNOWLEDGED` — reachable only after the client proved observation, closing X21-M6 | distinct occurrences; the second is `NOT_FOUND`, cached as that refusal | repeated `NEW` after close ⇒ `NOT_FOUND` terminals, each cached once |
| `PAUSE` | `NEW(i)` re-sent; one checkpoint, one pause event | `RETRY(i)` ⇒ cached `pause_event_sha256`, `checkpoint_sha256` | as `CLOSE` (own-terminal scope, excluded from `PROCESS_TERMINAL`) | cached reply re-wrapped | resume at the first missing signed §6a condition; an unmeetable condition ⇒ the signed pause-failure route cached as that refusal; cross-generation ⇒ non-behavioral only | `ALREADY_ACKNOWLEDGED` | distinct occurrences; the second finds G3 and is cached as the signed refusal | repeated `NEW` in G3 ⇒ signed refusal terminals |
| `RESUME` | `NEW(i)` re-sent; one automaton run | `RETRY(i)` ⇒ cached `phase`, `ledger_head_sha256` | `RETRY(i)` identical; `NEW(i+1)` re-evaluates signed §6b state | cached reply re-wrapped | resume the signed §6b / v2.1 §C.1–C.2 automaton at the first missing artifact; **never selects a different checkpoint**; cross-generation ⇒ non-behavioral only | `ALREADY_ACKNOWLEDGED` | distinct occurrences; the second sees G1/G4 and is cached as the signed refusal | repeated `NEW` ⇒ signed refusals |
| `OPERATION_ADMIT` | `NEW(i)` re-sent; one `operation_id`, one reservation, one worker | `RETRY(i)` ⇒ cached `operation_id`; **no second worker, cursor, capacity record, or reservation** | `RETRY(i)` identical; `NEW(i+1)` is a *second* operation with its own reservation, refused `NO_CAPACITY` if the envelope cannot hold it | cached reply re-wrapped; success is cacheable only after the §Z5.1 release locator, so a cached `ADMITTED` always has a released worker in its own generation | resume the §Z5.1 order at the first missing locator with the **recorded** `pre_operation_reading_ns` and `operation_id`; cross-generation ⇒ worker frozen/settled, plan closed, capacity retained | `ALREADY_ACKNOWLEDGED` | distinct occurrences ⇒ two operations, disjoint stream subsets required, second refused if the subset is busy | each `NEW` is a distinct operation bounded by the signed aggregate |
| `OPERATION_STATUS` | `NEW(i)` re-sent; one observation | `RETRY(i)` ⇒ cached phase and token bytes | `RETRY(i)` identical; `NEW(i+1)` observes current state | cached observation re-wrapped; the observation plan is non-behavioral ⇒ completable across generations | observation form: only `committed`/`reply` can be missing, both written from the recorded observation; ack form: install the missing `DELIVERY_ACK.json`, then `ALREADY_DELIVERED` | `ALREADY_ACKNOWLEDGED` | distinct occurrences ⇒ two independent observations | **each poll is a new occurrence; a retry of one poll is byte-stable across promotion and delivery ack**; ≤ 64 unacknowledged per scope (§Z1.9) |

---

## Z2. Descendant-aware reducer and validity-first takeover (R2)

Closes Sol C2 and the reducer half of Sol C1.

### Z2.1 Chain membership (exact)

The ledger is append-only and `head_sha256` is the last entry's
`entry_sha256`. Define, over the **raw statically parsed** durable ledger
(the §V2.8 discipline, unchanged):

```text
entries      := the durable ordered list of entries
index(h)     := the position of the unique entry with entry_sha256 == h,
                or 0 if h is the pre-genesis head sentinel, else ⊥
in_chain(h)  := index(h) ≠ ⊥
descendant(h):= in_chain(h)          # every recorded entry precedes the head
ordered(hs)  := in_chain(h) for all h in hs, and index() is strictly
                increasing in the plan's declared order
```

"Later valid history is not invalidity" is realized exactly by using
`in_chain`/`ordered` instead of equality with a stale head.

### Z2.2 Admission of a committed or replied plan

```text
if reply.json or committed.json exists:
    require in_chain(post_ledger_head_sha256)
        and ordered(committed.effect_event_sha256s)
        and index(post_ledger_head_sha256) ≥ index(last declared event)
    ⇒ ACCEPT: the current head is a verified descendant of the recorded
      post-head chain; serve the cached effect reply re-wrapped in a
      fresh envelope, writing reply.json first if only committed.json
      exists.
    otherwise ⇒ record-first invalidity naming the plan, the recorded
      post-head, and the current head (a genuinely impossible durable
      layout: a recorded post-head that is not in the durable chain).
```

An acknowledged, completed request followed by any amount of ordinary
later history is therefore **accepted**, not routed to G5. §W1.5's
`head_ok` set-membership guard, which produced Sol C2's spurious G5, is
deleted.

### Z2.3 Admission of an accepted-only plan

```text
require in_chain(pre_ledger_head_sha256)                       # exact legal prefix
suffix := entries strictly after index(pre_ledger_head_sha256)
conflicting(e) := e is not one of the plan's declared event hashes AND
                  ( e is state-bearing for the plan's process_id or
                    operation_id, OR e is T_RUNTIME_INVALID, OR e appears
                    before a declared event that the plan orders earlier )

route:
  A. not in_chain(pre_ledger_head_sha256)
       ⇒ record-first invalidity naming the plan (impossible layout)
  B. suffix contains no conflicting entry, and the declared events present
     in it are a prefix of the plan's declared order
       ⇒ RESUME at the first missing locator (§Z2.4)
  C. suffix contains a conflicting entry, and **no** locator of the plan
     is present
       ⇒ the plan is void: cache the closed terminal
         REFUSED / SUPERSEDED_PLAN (retryable = false, empty tuples);
         the client re-intends a NEW occurrence. This is ordinary later
         history, never invalidity
  D. suffix contains a conflicting entry, and **some** locator of the plan
     is present
       ⇒ record-first invalidity naming the plan and the intervening entry
         (a genuinely impossible durable layout)
```

### Z2.4 Behavioral versus non-behavioral completion

A locator step is **behavioral** iff it can start, continue, extend, or
release work: `Popen`, `SIGCONT`, lease install or renewal, watchdog table
publication that extends a deadline, operation admission, worker release,
or any charge/event append that presupposes live behavior. Everything
else — writing `committed.json`/`reply.json` from recorded identities,
installing an already-recorded record or checkpoint artifact, archival
commits, cache completion under the signed §D1 authority, and observation
caching — is **non-behavioral**.

```text
behavioral completion is permitted iff
   accepted.supervisor_generation_sha256_at_accept == current generation
```

Otherwise only non-behavioral completion is permitted, and an
accepted-only plan whose remaining first step is behavioral is closed as
the terminal produced by §Z2.5 phase 2A for its process/stream — the
signed invalid route when that stream was settled invalid, else
`REFUSED`/`SUPERSEDED_PLAN`. **Across a supervisor loss no reducer ever
spawns, `SIGCONT`s, renews, admits, installs a lease, or otherwise
continues behavior.**

### Z2.5 Validity-first takeover (replaces §W2.9 phase 2's order)

Phase 1 (client, control plane only) is unchanged except for the
discovery repairs of §Z3.5/§Z3.6.

**Phase 2A — prove and freeze old-generation process state, then settle.**
By the new generation, under `T_RUNTIME.lock`, after installing its
identity and receiving the watchdog's first ack, **before any reducer step
and before serving any frame**:

```text
1. reconstruct the capacity ledger (§Z6.3) — read-only accounting
2. for every durable claim, lease, worker binding, spawn intent, and
   fork-child record of a prior generation: decide live/dead by pid +
   start identity; killpg(SIGSTOP) every live group; prove quiescence
   (§W6.4 / §W3.3, unchanged); killpg(SIGKILL) and prove death for any
   group that cannot be proved quiescent
3. write the supervisor's own freeze observations (killer = SUPERVISOR,
   §Z4.5) for every affected lease, and consume every pending observation
   through the §Z4.6 acceptance predicate
4. settle EVERY affected live stream through the signed all-live invalid
   route (§2c.12 / §2c.12b / §4d), and drive any unresolved batch
   authority to its signed terminal, ARCHIVE before RESOLVED
5. resolve unresolved spawn intents: kill by §Z3.4 discovery, prove death,
   never respawn
```

**Phase 2B — non-behavioral reducer work only.**

```text
6. run the §Z2.2/§Z2.3 reducer over every open plan, restricted by §Z2.4
7. only then serve
```

Within one generation (no supervisor loss) the reducer is unrestricted by
§Z2.4 and completes behavioral steps idempotently by locator, exactly as
§W1.5 intended. Validity-first dominance is therefore mechanical: no
effect can survive a supervisor loss that should have invalidated its
live set.

---

## Z3. Constructible spawn and bootstrap identity (R3)

Closes X21-C1, X21-C2, X21-M4, and Sol C3 items 1–4.

### Z3.1 The circularity is removed by construction

Two hashes over two explicit domains:

```text
argv_prefix        := for CONTROLLER, the client-supplied CLAIM `argv`
                      (printable ASCII, §Z9.2 bounds);
                      for WORKER, the supervisor-derived prefix of §Z3.7
argv_template      := the thirteen fixed adapter elements of §Z3.3 with the
                      two literal placeholder tokens
                      "<SPAWN_INTENT_ID>" and "<CTRL_FDS>",
                      followed by "--" and argv_prefix
argv_template_sha256 := SHA-256(canonical JSON array of argv_template)
                        # contains the placeholders, never a derived marker

spawn_intent_id    := SHA-256(canonical {
                        supervisor_generation_sha256, role,
                        process_sequence, argv_template_sha256,
                        created_utc })

complete_argv      := argv_template with
                      "<SPAWN_INTENT_ID>" → spawn_intent_id (64 lowercase hex)
                      "<CTRL_FDS>"        → "<low>,<high>" (the actual
                                             inherited descriptor numbers)
complete_argv_sha256 := SHA-256(canonical JSON array of complete_argv)
```

`spawn_intent_id` depends only on the **template**, which contains no
derived marker and no descriptor number, so the definition is
satisfiable and deterministic. `complete_argv_sha256` is a separate
record of what was actually executed, kept in the `CLAIM` effect plan and
in the durable binding. Because the descriptor numbers are excluded from
the template, a re-`Popen` under the **same intent** inside the accepting
generation reproduces the same `spawn_intent_id` with whatever descriptor
numbers the new pipes receive — closing X21-C1's second defect, which
made two §W1.5 reducer rows inexecutable. (Cross-generation respawn is
forbidden outright by §Z2.4.)

### Z3.2 Spawn intent record (replaces §W2.3)

```text
CHILDREN/<spawn_intent_id>.json
schema philosophia.officina.t-spawn-intent.v1, keys exactly:
schema, scientific_outcome, supervisor_generation_sha256,
spawn_intent_id, role ∈ {CONTROLLER, WORKER}, process_sequence,
argv_template (nonempty list[str], containing both placeholders),
argv_template_sha256, created_utc
```

`WATCHDOG` is **removed** from the role enum: it is an in-process fork
with no `exec` and no new argv, and pretending otherwise was
unsatisfiable (X21-M4, Sol C3.3). Its exact record is §Z3.6.
`process_sequence` remains the §V2.1.7 value from complete durable
history and `created_utc` remains canonical UTC at exactly nanosecond
precision, so two identical-template children in one tick cannot collide
(X-M10 regression preserved). The `CLAIM` effect plan becomes:

```text
CLAIM: process_sequence, process_id, spawn_intent_id,
       argv_template_sha256, complete_argv_sha256, claim_path
```

### Z3.3 The bootstrap adapter is the executable root (Sol C3.4)

An arbitrary target program cannot be assumed to parse Officina tokens,
close descriptors, or self-stop. Therefore the **actual executable root
of every controller and worker is the fixed, reviewed, supervisor-owned
bootstrap adapter inside the sole module root**
`src/philosophia/officina/generic_harness.py`. `complete_argv` has this
exact layout, by index:

```text
 0  interpreter_argv0        # element 0 of the supervisor's own /proc/self/cmdline
 1  "-m"
 2  "philosophia.officina.generic_harness"
 3  "--officina-bootstrap"
 4  "--officina-role"
 5  "CONTROLLER" | "WORKER"
 6  "--officina-spawn-intent"
 7  <spawn_intent_id hex>            # "<SPAWN_INTENT_ID>" in the template
 8  "--officina-ctrl-fds"
 9  "<low>,<high>"                   # "<CTRL_FDS>" in the template
10  "--officina-target-argc"
11  <N decimal>                      # N == len(complete_argv) - 13, N ≥ 1
12  "--"
13… the target argv (argv_prefix)
```

`--officina-bootstrap` is the **only** private argv entry surface, and it
is refusal-first. §W2.1's sentence "There is no private argv entry
surface to guard." is replaced by: *the supervisor and watchdog have no
argv entry surface (they are in-process forks); the controller and worker
share exactly one, which refuses unless every inherited token verifies.*
The six public CLI commands, the unknown-command exit `2` rule, the sole
module root, and the zero allowlist delta are unchanged;
`--officina-supervisor-serve` and `--officina-watchdog-serve` remain
deleted.

**Per-role descriptor order is pinned** (closing Opus minor 3). The
adapter's ordered duties, executed before any target behavior:

```text
1. verify the exact index layout above; verify N == len(argv) - 13 and N ≥ 1;
   verify argv[7] is 64 lowercase hex; else os._exit(4)
2. parse argv[9] as exactly two decimal ints (low, high); os.dup2 them to
   T_CTRL_FD_LOW = 3 and T_CTRL_FD_HIGH = 4; close the originals if
   different; os.fstat both and require S_ISFIFO; else os._exit(4)
      CONTROLLER: fd 3 = control-request write, fd 4 = control-reply read
      WORKER:     fd 3 = worker-status write,  fd 4 = framed-output write
3. close every other inherited descriptor except 0, 1, 2, 3, 4, by a bounded
   enumeration of /proc/self/fd (os.listdir)
4. re-verify that argv[13] exists, is a regular file, and is executable
   (os.stat, os.access(X_OK)); else os._exit(4)
5. install NO signal disposition (§W2.6 invariant, unchanged), then
   os.kill(os.getpid(), SIGSTOP)
6. after SIGCONT: re-verify fds 3 and 4 are still pipes, then
   os.execv(argv[13], argv[13:])
```

The adapter never imports the target, so the import allowlist is
untouched; the target inherits exactly fds 0–4 with the pinned per-role
meaning; and no capability, lease, or write authority exists before
`SIGCONT` (§W2.6's normative invariant, carried forward verbatim).
`os._exit(4)` is observed by the supervisor as the §W2.5 `BOOTSTRAP`
route.

### Z3.4 Discovery predicate for `exec`ing children (replaces §W2.4's)

For every `CHILDREN/<id>.json` without a resolved claim/binding, read each
`/proc/<pid>/cmdline`, NUL-split, drop the trailing empty element, and
select the process iff **all** hold at fixed indices:

```text
len(cmdline) ≥ 13
cmdline[3] == "--officina-bootstrap"
cmdline[6] == "--officina-spawn-intent"
cmdline[7] == <spawn_intent_id hex>
```

Because the marker is matched at a **fixed index** that precedes the
`--` separator, a client-supplied target argv (index ≥ 13) cannot spoof
another intent's marker; only a process that itself `exec`s a forged argv
can, which is the named A3 procedural residual. Kill by
`killpg(SIGTERM)` then `killpg(SIGKILL)`; prove death by
`/proc/<pid>/stat` absence or state `Z`; `os.waitpid` only for
own-generation children. The predicate is used **only** for `exec`ing
children (controller, worker) — never for the supervisor grandchild or
the watchdog, which never `exec` and therefore never carry it.

### Z3.5 Grandchild bootstrap identity: sealed pipe + immediate record

Closes X21-C2 and Sol C3.2. The `spawning_id`-in-`cmdline` predicate is
**deleted** everywhere.

```text
CLI, before the first fork:
  acquire SPAWN.lock with flock(LOCK_EX | LOCK_NB), retrying at
  T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS;
  on expiry: see the stuck-holder route below
  create bootstrap_pipe = os.pipe2(0)   # inherited across fork; no exec occurs
  install SPAWNING.json (unchanged keys, §W2.2)
  fork → middle child setsid() → fork → grandchild

Grandchild, as its FIRST actions, before creating any endpoint, forking the
watchdog, or awaiting anything:
  a. scrub every inherited descriptor except the SPAWN.lock fd, the
     bootstrap-pipe write end, and its own sealed pipes; stdio → os.devnull
  b. install T_SUPERVISOR/SPAWNING_CHILD.json (atomic no-replace, §3
     durability), schema philosophia.officina.t-supervisor-spawning-child.v1,
     keys exactly:
       schema, scientific_outcome, spawning_id, supervisor_pid,
       supervisor_start_identity, supervisor_pgid, boot_identity, created_utc
  c. write ONE canonical ASCII JSON line ≤ 4096 bytes on the bootstrap pipe,
     schema philosophia.officina.t-supervisor-bootstrap.v1, keys exactly:
       schema, scientific_outcome, spawning_id, supervisor_pid,
       supervisor_start_identity, supervisor_pgid, boot_identity,
       reported_monotonic_ns
     then close the write end
  d. create endpoints; fork the watchdog and write its fork-child record
     (§Z3.6); await the watchdog's first ack, BOUNDED by
     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
  e. install SUPERVISOR_IDENTITY.json (atomic no-replace); unlink
     SPAWNING_CHILD.json and SPAWNING.json; close the SPAWN.lock fd
```

Both identity facts the CLI needs are now **kernel-verifiable and
non-circular**: the pipe delivers pid + start identity + pgid, and the
durable record persists them for a later takeover.

```text
CLI wait: read the bootstrap line within T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS,
  then poll for a live-verified identity within the same bound.
  - EOF without a line, malformed line, or timeout ⇒ kill by the RECORDED
    pid + start identity (killpg on the recorded pgid, SIGTERM then SIGKILL),
    prove death by /proc absence or state Z, unlink SPAWNING_CHILD.json and
    SPAWNING.json, release the lock, return REFUSED / BOOTSTRAP
    (retryable = false)
  - pid live but start identity mismatched ⇒ do not kill; treat as absent;
    same refusal
Grandchild first-ack timeout (step d) ⇒ kill the watchdog by its fork-child
  record, prove death, unlink SPAWNING_CHILD.json, os._exit(3) WITHOUT
  installing an identity and WITHOUT serving
Stuck-holder route (SPAWN.lock acquisition expiry, taken WITHOUT the lock):
  read SPAWNING_CHILD.json; if it exists, its recorded process is live by
  pid + start identity, SUPERVISOR_IDENTITY.json is absent or not
  live-verified, and the record is older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS,
  then killpg the recorded pgid (SIGTERM, SIGKILL), prove death — which
  closes its lock fd — and retry the bounded acquisition exactly once;
  otherwise return REFUSED / BOOTSTRAP
Identity-install no-replace collision: the loser exits immediately without
  serving, writing nothing, unlinking nothing (unchanged)
```

D1 therefore cannot be wedged indefinitely: the grandchild has its own
bounded internal timeout, the CLI's wait is bounded, the lock acquisition
is bounded and non-blocking, and a half-initialized holder is
discoverable and killable by recorded identity rather than by a `cmdline`
marker that cannot exist. §W2.2's retained fork-shared `flock` semantics
and the `O_CLOEXEC` exception for the grandchild's lock fd are otherwise
unchanged.

### Z3.6 Fork-child record (the watchdog's exact identity)

```text
WATCHDOG/WATCHDOG_CHILD.json
schema philosophia.officina.t-fork-child.v1, atomic no-replace,
written by the supervisor immediately after os.fork() returns in the
parent and before awaiting the first ack, keys exactly:
schema, scientific_outcome, supervisor_generation_sha256,
role ("WATCHDOG"), child_pid, child_start_identity, child_pgid,
boot_identity, created_utc
```

No argv field exists, because no `exec` occurred. Takeover and the CLI
discover and kill a stale or half-initialized watchdog by this record
(pid + start identity + pgid), never by `cmdline`. This also gives a
prior generation's watchdog a discoverable identity, which X21-M2
required. The watchdog's own `getppid()`/parent-start-identity check and
its sealed-pipe checks are unchanged.

### Z3.7 Worker argv prefix (stated, not invented)

The worker's `argv_prefix` is **not** client-supplied at admission time.
It is exactly the `argv` prefix recorded in the owning process's durable
claim (already hashed and validated at `CLAIM`), followed by exactly two
supervisor-appended target tokens:

```text
argv_prefix(WORKER) := claim.argv  +  ["--officina-operation", <operation_id>]
```

The worker therefore executes the same claim-declared, claim-hashed
behavior root as its controller, under the same adapter, with no new
client-supplied surface and no new author-facing field. This selects no
scientific content: `behavior_source_sha256`, `config_sha256`,
`stack_sha256`, `numerical_mode_sha256`, and `device_identity` were all
fixed and hashed at `CLAIM`.

---

## Z4. Watchdog renewals and evidence acceptance (R4)

Closes X21-C3, X21-M1, X21-M2, Sol C4 residue, and Sol M3.

### Z4.1 Publication trigger restored (X21-C3)

§W3.2's publication sentence is replaced by, verbatim normative:

> After **every** successful locked claim-start, renew, and remove, the
> supervisor atomically replaces `WATCHDOG/LEASES.json` with a strictly
> increasing `table_seq` and writes the identical payload on the update
> pipe, and it must observe the watchdog's ack of that exact `table_seq`
> before the corresponding behavior is authorized. Publication and ack
> precede the first `SIGCONT`, any capability becoming usable, and any
> operation admission.

`LEASES.json`'s key set and the ack frame's key set are unchanged.

### Z4.2 `watchdog_table_seq` in the effect plans and the reducer

Replaced `effect_plan` rows (keys exactly):

| Command | `effect_plan` keys exactly |
|---|---|
| `START` | `process_id, claim_sha256, start_event_sha256, lease_path, lease_sha256, watchdog_table_seq` (unchanged) |
| `HEARTBEAT` | `process_id, pre_lease_sha256, cursor_reading_ns, charge_event_sha256, successor_lease_path, successor_lease_sha256, watchdog_table_seq, post_state_sha256` |
| `CLOSE` | `process_id, pre_lease_sha256, cursor_reading_ns, final_charge_event_sha256, process_record_path, process_record_sha256, stopped_event_sha256, watchdog_table_seq, archive_set ("close")` |
| `PAUSE` | `checkpoint_path, checkpoint_payload_sha256, pause_event_sha256, watchdog_table_seq, post_state_sha256, archive_set ("pause")` |

Reducer probe/action rows (added to §W1.5's table):

| Command | Added probe | Single next action |
|---|---|---|
| `HEARTBEAT` | watchdog ack of `watchdog_table_seq` | publish the recorded `table_seq` (idempotent atomic replace + pipe write) and await its ack per §Z4.3; only then cache |
| `CLOSE` | watchdog ack of `watchdog_table_seq` (lease **removal**) | publish and await the ack before the archival step; the removal never extends a deadline, so a missing ack cannot authorize behavior |
| `PAUSE` | watchdog ack of `watchdog_table_seq` (all leases removed) | as `CLOSE` |

Exact `HEARTBEAT` order: capture the recorded `cursor_reading_ns` →
append `charge_event_sha256` → install `successor_lease_path` → publish
`table_seq` → await the ack → `committed.json` → `reply.json` (`OK`).

### Z4.3 The renewal window is total (X21-C3, Opus Q2's symmetric gap)

Three normative rules, jointly single-valued:

1. **The old deadline is authoritative until the successor table is
   acked.** No unacknowledged update ever extends behavior; the
   supervisor caches no positive `HEARTBEAT` reply before the ack.
2. **The watchdog drains before it freezes.** On reaching
   `now_ns ≥ deadline_ns` for a row, the watchdog first drains its update
   pipe nonblocking and re-reads `LEASES.json`; if a strictly greater
   `table_seq` is available, it acks that `table_seq` and re-evaluates
   against the newest row it has acked. Only if no newer table is
   available does it proceed to §W3.3 step 1. A legitimately renewed
   lease therefore cannot be frozen against a superseded deadline, and
   the freeze decision is always taken against the newest table the
   watchdog can observe at that instant.
3. **Ack absence never fabricates a later valid renewal.** If the ack of
   the current `table_seq` has not arrived within
   `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`, the supervisor re-publishes the
   same `table_seq` once per `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS`. If
   `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` elapses since
   `updated_monotonic_ns` with no ack, the watchdog is declared dead:
   §W3.5's dead-watchdog continuation runs (the supervisor freezes all
   live groups itself with `killer = SUPERVISOR`, refuses admissions,
   forks a new watchdog, awaits its ack, and settles every overdue lease
   through §W3.4 **against the supervisor's own current durable lease
   deadlines**), and the pending occurrence's cached terminal is
   `REFUSED`/`WATCHDOG_UNACKED` (`retryable = true`) whose
   `committed.json` records exactly the artifacts that became durable
   (§Z1.7). No later valid renewal, no fabricated deadline, and no
   fabricated invalidity from a healthy heartbeat path.

Because `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` (60 s) exceeds
`T_CLIENT_REPLY_TIMEOUT_SECONDS` (30 s), a client whose heartbeat waits
on a dying watchdog times out, exits `3`, and re-addresses the same
occurrence later to collect its cached terminal (§Z1.8).

### Z4.4 Strict progress, not asserted progress (Sol M3)

§W3.3 step 4 and §W3.4's "(> 0 by construction)" are replaced:

```text
on the pass that proves every reachable member absent / T / Z:
    sample s = clock_gettime_ns(CLOCK_MONOTONIC)
    if s > deadline_ns:
        freeze_ns = s; quiescence = PROVED; overrun_ns = s - deadline_ns  (> 0)
    else:                       # s == deadline_ns, or a non-monotonic sample
        take up to T_WATCHDOG_QUIESCE_MAX_PASSES further samples at
        T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS, RE-PROVING quiescence each pass;
        the first sample with s > deadline_ns and quiescence still proved
        ⇒ PROVED with overrun_ns = s - deadline_ns
        exhausted without strict progress
        ⇒ freeze_ns = null; overrun_ns = null; quiescence = UNKNOWN
```

There is no zero-overrun branch, no tolerance constant, and no valid
terminal reachable from any freeze. `quiescence = PROVED` is a
**process-tree** fact — every recorded group member and every `/proc`
process whose session id or parent chain reaches a recorded member is
absent, `T`, or `Z` — and explicitly **not** a backend fact; signed §4d
step 3's backend synchronization remains the supervisor's settlement
obligation (Opus Q2's requested qualification). A doubly detached
descendant is outside the enumeration by construction and remains the A3
procedural residual named in §W6.4.

### Z4.5 Freeze-witness naming and ordering (X21-M2)

```text
witness_id = SHA-256(canonical {
  supervisor_generation_sha256, process_id, table_seq })

WATCHDOG/FREEZE/<witness_id>.json
schema philosophia.officina.t-freeze-observation.v1, atomic no-replace,
keys exactly:
schema, scientific_outcome, supervisor_generation_sha256, witness_id,
process_id, pgid, start_identity, deadline_ns, freeze_ns_or_null,
quiescence ∈ {PROVED, UNKNOWN}, overrun_ns_or_null,
killer ∈ {WATCHDOG, SUPERVISOR}, unresolved_member_count (int),
table_seq, created_utc
```

- **Production order:** the writer re-reads `SUPERVISOR_IDENTITY.json`
  and refuses to write on generation mismatch; then writes the file
  (same-directory temp → file `fsync` → atomic no-replace → parent
  `fsync`); **then** emits the pipe event. A no-replace `EEXIST` means an
  identical `(generation, process_id, table_seq)` witness already exists:
  the writer emits the event and writes nothing further.
- **Consumption order:** the supervisor consumes witnesses sorted by
  `(generation == current) desc, table_seq asc, process_id asc`, and the
  **earliest `table_seq`** for a process in the current generation is
  authoritative; later same-process witnesses are retained as
  duplicates, not consumed twice. A prior-generation witness fails the
  §Z4.6 predicate and takes the `UNKNOWN` route.
- Removal: by the supervisor, after the settlement's archival commit
  (unchanged). Stale cross-generation collision on a no-replace path is
  now impossible, because the generation is inside the name.

### Z4.6 Supervisor acceptance predicate for freeze evidence (X21-M1)

Under `T_RUNTIME.lock`, an observation becomes evidence **only if every
conjunct holds**:

```text
1. it validates against t-freeze-observation.v1 exactly: key set, types,
   strict int, enums, recursive scientific-field rejection
2. witness_id recomputes exactly from (generation, process_id, table_seq)
   and equals the filename
3. supervisor_generation_sha256 == the current generation
4. table_seq is the supervisor's current watchdog table sequence for that
   lease, or an earlier sequence whose row for this process_id carried an
   IDENTICAL deadline_ns
5. process_id names a durable claim whose lease was live at that table_seq
6. deadline_ns equals BOTH that table row's deadline and the supervisor's
   current durable lease deadline for that process
7. pgid == the claim's process_group_id and start_identity == the claim's
   controller_start_identity
8. killer == WATCHDOG only if the current generation's watchdog was live
   by its §Z3.6 fork-child record and ack history at the recorded instant;
   otherwise killer must be SUPERVISOR
9. quiescence == PROVED ⇒ freeze_ns is int, freeze_ns > deadline_ns,
   overrun_ns == freeze_ns - deadline_ns, unresolved_member_count == 0
   quiescence == UNKNOWN ⇒ freeze_ns is null, overrun_ns is null,
   unresolved_member_count ≥ 1
10. the supervisor independently proves the group quiescent NOW (§W6.4)
```

**Any** malformed, missing, conflicting, or unverifiable fact — including
a planted or stale file, an A3-procedural forgery, a generation or
`table_seq` mismatch, an inconsistent member count, or a
`freeze_ns ≤ deadline_ns` — makes the object **not evidence**. The
supervisor then writes its own replacement witness with
`quiescence = UNKNOWN`, `freeze_ns = null`, `overrun_ns = null`,
`killer = SUPERVISOR`, and the member count it observes itself, and routes
to §W3.4's `UNKNOWN` / all-live invalid route with the §4c(c)/§4d
unknowable pool. It never becomes valid evidence, never yields a valid
terminal, and never contributes an accepted timestamp.

**C1 is strengthened, not altered.** The watchdog remains a control-plane
witness with **no** runtime lock, **no** capability, **no** right to
write anything under `runtime/`, **no** ledger append, **no** settlement,
and **no** validity authority. Adding supervisor-side validation of its
witness makes the sole supervisor the only authority that can turn an
observation into a settlement, which is exactly the signed C1 shape. No
watchdog fact is ever a second runtime authority.

---

## Z5. Admission release is durable before success (R5)

Closes X21-C4 and Sol C4.

### Z5.1 The release locator and the ten-step admission plan

```text
operations/<operation_id>/RUNNING.json
schema philosophia.officina.t-operation-release.v1, atomic no-replace,
written by the supervisor under T_RUNTIME.lock, keys exactly:
schema, scientific_outcome, supervisor_generation_sha256, operation_id,
worker_spawn_intent_id, worker_pid, worker_start_identity, worker_pgid,
release_attempted (true), attempted_utc
```

The `OPERATION_ADMIT` `effect_plan` gains `running_path` (keys exactly:
`operation_id, pre_operation_reading_ns, capacity_path, bound_path,
admission_path, worker_spawn_intent_id, running_path,
declared_stream_indexes`). The admission order becomes, under
`T_RUNTIME.lock`, each step keyed by its recorded locator:

```text
 1. capture pre_operation_reading_ns; derive operation_id;
    JOURNAL/<key>/accepted.json                              (no-replace)
 2. CAPACITY/<operation_id>.json                              (no-replace)
 3. operations/<operation_id>/BOUND.json                      (no-replace)
 4. operations/<operation_id>/OPERATION.json                  (no-replace)
 5. CHILDREN/<worker_spawn_intent_id>.json                    (no-replace)
 6. create out/ (supervisor-owned), the status pipe, and the output pipe;
    Popen the adapter (§Z3.3); bounded self-stop handshake (§W2.5);
    durable worker binding
 7. operations/<operation_id>/RUNNING.json                    (no-replace)
 8. os.kill(worker_pid, SIGCONT)                              # idempotent release
 9. JOURNAL/<key>/committed.json
10. JOURNAL/<key>/reply.json → OK / {operation_id, phase "ADMITTED",
                                     bound_sha256}
```

`ADMITTED` therefore becomes cacheable only after the exact bound worker
has a **durable same-generation release/start-attempt locator** and the
release has been attempted in that same generation. §W4.8's
`ADMITTED → RUNNING` durable trigger cell becomes `RUNNING.json`; a
signal is not a durable object and can no longer appear as one.

### Z5.2 Idempotent reducer and crash table

The reducer's `reply.json`-exists branch is no longer a short circuit for
this command: it must probe `running_path` first.

| Cut | Same generation | After supervisor loss |
|---|---|---|
| after 7, before 8 | recorded worker alive with matching start identity and state `T` ⇒ complete step 8 (idempotent), then 9, 10 | R2/§Z2.5 governs: the worker is frozen and settled through the signed all-live invalid route; **never resumed**; the plan is closed as that invalid terminal; capacity stays at `bytes_reserved` |
| after 7, before 8, worker absent or identity mismatched | kill by intent (§Z3.4), prove death, `WORKER_FAILED` quarantine + signed invalid route; cache that terminal | as above |
| after 8, before 9 | write `committed.json`, then `reply.json`; serve | non-behavioral completion is permitted: `committed`/`reply` written from recorded identities, but the worker is already frozen/settled by phase 2A, so the cached terminal is that invalid route |
| after 9, before 10 | write `reply.json` from recorded identities; serve | as above |
| `reply.json` exists, `RUNNING.json` present | probe: worker alive+stopped ⇒ complete step 8, then serve the cached reply; worker dead ⇒ the quarantine/invalid route already applies and is served | non-behavioral only; never `SIGCONT` |
| `reply.json` exists, `RUNNING.json` absent | record-first invalidity naming both paths (impossible durable layout) | same |

---

## Z6. K1 accounting and the disposition authority (R6)

Closes Sol C5, Sol M1, and X21-M8. This is a **mechanical realization of
signed K1**, not a new author choice: it deletes v2.1's replenishment and
completes the authority K1 already selected.

### Z6.1 Accounted total (replaces §W4.6's formula)

```text
accounted_total =
    Σ bytes_reserved  over every operation with a durable
                      CAPACITY/<op>.json and NO durable
                      CAPACITY/<op>.disposed.json
  + Σ T_OUTPUT_PER_STREAM_MAX_BYTES × 4          # 268_435_456, the full
                      per-operation ceiling, for every custody directory
                      found under operations/**/out/, the quarantine root,
                      or runtime/T_PROMOTED/** that has NO capacity record
```

`actual_bytes` **never** enters `accounted_total`. Every
over-declaration release and unused-reservation release is **removed**.
`bytes_reserved` remains the accounted contribution through `ADMITTED`,
`RUNNING`, `PENDING_SETTLEMENT`, `QUARANTINED`, and `PROMOTED` custody,
and through every rename and promotion, until an authorized
custody-absence disposition is fully verified (§Z6.5). A one-byte
promoted result from a 256 MiB reservation therefore replenishes
**nothing**, which is exactly the signed clause v2.1 violated.

### Z6.2 Capacity artifacts (replaced rows)

| Artifact | Schema | Keys exactly | Effect on `accounted_total` |
|---|---|---|---|
| `CAPACITY/<op>.json` | `philosophia.officina.t-operation-capacity.v1` | `schema, scientific_outcome, supervisor_generation_sha256, operation_id, process_id, active_lease_sha256, declared_stream_indexes, bytes_reserved, created_utc` (unchanged) | **adds** `bytes_reserved` |
| `CAPACITY/<op>.settled.json` | `philosophia.officina.t-operation-capacity-settled.v1` | `schema, scientific_outcome, operation_id, terminal ∈ {PROMOTED, QUARANTINED}, actual_bytes, custody_root, settled_utc` | **none.** `actual_bytes` is a **diagnostic custody fact only**; it may never reduce the accounted total, relax a predicate, or authorize an admission. `custody_root` is updated; nothing is released |
| `CAPACITY/<op>.disposed.json` | `philosophia.officina.t-capacity-disposition.v1` | `schema, scientific_outcome, operation_id, disposition_id, author_disposition_sha256, released_bytes (== bytes_reserved), custody_absent (true), custody_proof_root, proof_epoch_utc, disposed_utc` | **the one and only release**, of exactly `bytes_reserved` |

`SETTLEMENT.json`, `QUARANTINE.json`, the promotion `os.replace`, any
rename, `DELIVERY_ACK.json`, and every failure class **release nothing**.

### Z6.3 Crash reconstruction (replaces §W4.6's steps 1–4)

Under `T_RUNTIME.lock`, before the first admission:

```text
1. read every CAPACITY/*; per operation take
     disposed present ⇒ 0
     else            ⇒ bytes_reserved            # never actual_bytes
2. enumerate operations/**/out/, the quarantine root, and
   runtime/T_PROMOTED/** with directory-fd + O_NOFOLLOW, solely to detect
   custody with no capacity record; each such operation counts the full
   268_435_456 ceiling
3. never lower any operation's contribution from a measurement; a partially
   written tree is never re-measured at all
4. any accounted path that cannot be opened, read, or enumerated ⇒ refuse
   every admission with NO_CAPACITY; never assume zero
```

### Z6.4 The author custody-absence disposition (one immutable object)

**Canonical path grammar, outside the supervisor control plane:**

```text
successor/officina/runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json
disposition_id = SHA-256(canonical {
  activation_record_sha256, operation_id, author_decision_sha256 })
```

The three-field preimage removes any self-reference. The supervisor
**never creates, replaces, renames, or removes** anything under this
directory; it opens it read-only with a directory fd and `O_NOFOLLOW`.

```text
schema philosophia.officina.t-output-custody-disposition.v1
keys exactly:
  schema, scientific_outcome, disposition_id,
  activation_record_sha256,
  settlement_generation_sha256,          # == OPERATION.json's generation
  operation_id,
  operation_terminal ∈ {PROMOTED, QUARANTINED},
  bytes_reserved, actual_bytes,
  custody_root,
  custody_parent_sha256,                 # SETTLEMENT.json or QUARANTINE.json
  custody_destination ∈ {DELETED_OUTSIDE_T, MOVED_OUTSIDE_REPOSITORY},
  author_token, author_decision_path, author_decision_sha256,
  authorized_utc
```

**Author token and signature representation.** `author_token` is exactly
the literal

```text
I_AUTHORIZE_OFFICINA_T_OUTPUT_CUSTODY_ABSENCE
```

and `author_decision_path` must match the pinned grammar

```text
successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_[A-Z0-9_]{1,64}_SIGNATURE.md
```

a **tracked** repository file whose SHA-256 equals
`author_decision_sha256` and which contains, each as an exact standalone
line, the `author_token`, the `operation_id`, and the `disposition_id`.
This spelling is the mechanical realization of the authority K1 already
selected; it introduces no new author choice, grants no implementation or
activation authority, and is per-disposition, so signing one can never
release another.

### Z6.5 Verifier (fail-closed; every conjunct mandatory)

Under `T_RUNTIME.lock`, in one lock epoch:

```text
 1. canonical ASCII JSON + trailing newline; exact key set;
    scientific_outcome: false; recursive scientific-field rejection;
    type(bytes_reserved) is int and type(actual_bytes) is int (bool refused);
    no free-text field exists by schema
 2. disposition_id recomputes exactly and equals the filename stem
 3. activation_record_sha256 == the current durable activation record's hash
 4. operation_id names a durable operation; operation_terminal == PROMOTED iff
    SETTLEMENT.json is durable, == QUARANTINED iff QUARANTINE.json is durable;
    custody_parent_sha256 == that record's canonical-byte SHA-256
 5. settlement_generation_sha256 == OPERATION.json's
    supervisor_generation_sha256 for that operation
 6. bytes_reserved == CAPACITY/<op>.json's value exactly;
    actual_bytes == CAPACITY/<op>.settled.json's value exactly (a mismatch
    refuses and releases nothing; actual_bytes never changes any total)
 7. custody_root equals the exact recorded custody root for that terminal;
    path grammar: repository-relative, non-empty, no absolute prefix, no NUL,
    no "." or ".." component, and no symlink component — proved by an
    O_DIRECTORY|O_NOFOLLOW dir-fd walk from the repository root
 8. author_token is exactly the pinned literal; author_decision_path matches
    the pinned grammar and is tracked at HEAD; the file's SHA-256 equals
    author_decision_sha256; the file contains author_token, operation_id, and
    disposition_id each as an exact standalone line
 9. NO value anywhere in the record equals the operation's result_sha256, its
    promoted content hashes, any learner/candidate/Q/C identifier, or any
    judgement about output content; the recursive scientific-field rejection
    applies at every depth (the prohibition is recursive, not top-level)
10. CUSTODY-ABSENCE PROOF, in this same lock epoch, descriptor-safe:
      open the parent of custody_root with O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC;
      os.stat(name, dir_fd=parent_fd, follow_symlinks=False) must raise ENOENT;
      AND the named component must be absent from os.listdir(parent_fd);
      if the parent itself is absent, prove the parent absent in ITS parent by
      the same two checks, recursing up to the repository root;
      any component that exists (of any type), or any level that cannot be
      opened or enumerated, ⇒ REFUSE and release nothing
11. single use: CAPACITY/<op>.disposed.json is atomic no-replace. A second
    disposition for the same operation after a durable .disposed.json
    releases nothing; if its bound facts contradict the first, record-first
    invalidity naming both paths
12. only then install CAPACITY/<op>.disposed.json (§Z6.2) with
    author_disposition_sha256 = SHA-256 of the exact author-disposition file
    bytes and released_bytes = bytes_reserved
```

### Z6.6 Mismatch, stale, substitution, and replay routes

| Condition | Route (all release nothing) |
|---|---|
| any schema/key/type/enum failure | refuse; the object is not an authority |
| `disposition_id` does not recompute, or the filename differs | refuse |
| stale `activation_record_sha256` | refuse |
| `operation_terminal` disagrees with the durable records | refuse |
| `custody_parent_sha256` names a different or absent record | refuse (substitution) |
| `bytes_reserved` ≠ the reservation record | refuse |
| `author_decision_path` untracked, mis-grammared, or hash-mismatched | refuse |
| `author_token` differs by a single byte | refuse |
| the named custody exists, or any level is unreadable | refuse (this is the replay/premature case) |
| a second disposition naming the same operation | releases nothing; contradiction ⇒ record-first invalidity |
| a disposition naming an operation with no capacity record | refuse; the operation is already counted at the full ceiling (§Z6.1) |

**A3 honesty (required by §Z8's discipline).** The author-disposition
file is same-UID writable, so its authority is **mechanical** against
accident, stale facts, substitution of a different operation or terminal,
premature release while custody exists, replay after a durable
disposition, and every schema/grammar error — and **procedural** against
a deliberate same-UID forger, exactly as the signed A3 residual states.
It is not a cryptographic or kernel authority, and this contract does not
claim it is. Raising `T_OUTPUT_AGGREGATE_MAX_BYTES` still requires a new
signed author capacity amendment, is forbidden while any operation is
live or any invalidity is unresolved, may never be enacted in response to
a `NO_CAPACITY` refusal or an `ENOSPC`, and the supervisor can never
raise it (§W4.6, unchanged). Outputs are retained for the whole of T; no
TTL, class-based deletion, or size-pressure eviction exists; nothing is
ever deleted to make room.

### Z6.7 Capacity/custody transition table (replaces §W4.8's rows)

| Transition | Durable trigger | Accounted contribution | Releases? |
|---|---|---|---|
| — → `ADMITTED` | `CAPACITY/<op>.json` | `bytes_reserved` | no |
| `ADMITTED` → `RUNNING` | `RUNNING.json` (§Z5.1) | `bytes_reserved` | no |
| `RUNNING` → `PENDING_SETTLEMENT` | worker + group proved dead, transport closed | `bytes_reserved` | no |
| `PENDING_SETTLEMENT` → `PROMOTED` | `SETTLEMENT.json`, then `<op>.settled.json` (`PROMOTED`) | `bytes_reserved` | **no** |
| any → `QUARANTINED` | `QUARANTINE.json`, then `<op>.settled.json` (`QUARANTINED`) | `bytes_reserved` | **no** |
| `out/` → `T_PROMOTED/<op>/` rename | `os.replace` | `bytes_reserved` | **no** |
| `PROMOTED` → `ALREADY_DELIVERED` | `DELIVERY_ACK.json` | `bytes_reserved` | no |
| any retained → released | `<op>.disposed.json` after §Z6.5 verifies | `0` | **yes — the only release** |

---

## Z7. Worker status and output cuts (R7)

Closes X21-M3 and Opus minor 5.

### Z7.1 `t-worker-status.v1`, exactly

```text
philosophia.officina.t-worker-status.v1   (status pipe; one canonical
ASCII JSON line ≤ T_CONTROL_FRAME_MAX_BYTES terminated by "\n")
keys exactly:
schema, scientific_outcome, operation_id, exit_reason ∈ {COMPLETED, FAILED},
frame_count (int ≥ 0), total_content_bytes (int ≥ 0)
```

`output_relative_paths` is **not restored**: under K1 the supervisor
derives every path from the framed headers it validates itself, and a
worker-supplied path is never trusted for anything. `frame_count` and
`total_content_bytes` are **fail-closed cross-checks only**: if they
disagree with what the supervisor itself wrote, the operation takes the
`TRANSPORT` quarantine class. They may never increase accounted bytes,
relax a check, supply a path, select a valid terminal, or influence
promotion.

### Z7.2 Status-frame validation

A status frame is accepted only if it validates exactly (key set, types,
strict `int`, enum, recursive scientific-field rejection) and its
`operation_id` equals the operation's. Anything else — malformed, extra
key, missing key, wrong `operation_id`, oversize line, or a second status
frame — is the `TRANSPORT` quarantine class.

### Z7.3 Total EOF and completion rows (replaces §W4.5's boundary rows)

| Cut | Single continuation |
|---|---|
| EOF at a frame boundary, valid status `COMPLETED`, `frame_count ≥ 1` and both cross-checks agree, group proved dead | proceed to §Z8.3 verification, then §W6.1 settlement |
| **EOF at a frame boundary, valid status `COMPLETED`, `frame_count == 0`, `total_content_bytes == 0`, group proved dead** | **canonical empty result**: promote with `promoted_relative_paths = []`, `result_sha256 = SHA-256(b"[]")` (the canonical JSON of the empty array), `actual_bytes = 0`. This is not a failure: zero frames is a transport fact, and turning it into an invalidity would derive a route from an output property, which the signed composite forbids. Capacity still stays at `bytes_reserved` until a disposition, so no incentive or exhaustion asymmetry arises |
| EOF at a frame boundary with `exit_reason = FAILED` | `WORKER_FAILED` quarantine (unchanged) |
| **EOF at a frame boundary with NO status frame** (status pipe EOF without a valid status line — worker killed, crashed, or exited silently) | `WORKER_FAILED` quarantine + the signed record-first live-process invalidity route, public cause `PROCESS`. This is X21-M3's missing reachable row |
| status frame present but output pipe still open at worker death | `TRANSPORT` quarantine |
| cross-check mismatch (`frame_count` or `total_content_bytes` ≠ what the supervisor wrote) | `TRANSPORT` quarantine |

### Z7.4 Termination is by `killpg`, not by the close (Opus Q3)

§W4.5's parenthetical "(the worker's next `write` takes
`EPIPE`/`SIGPIPE`)" is replaced by the honest mechanism: closing the read
end releases a worker already blocked in `write` and makes its **next**
write fail, and because CPython sets `SIGPIPE` to `SIG_IGN` at
interpreter startup — and `SIG_IGN` survives `exec` — a Python worker
observes `BrokenPipeError` rather than dying. **Termination is therefore
guaranteed by the `killpg` and proved death that the same row already
requires**, never by the close. The supervisor still never writes to the
output pipe, so it can take no `SIGPIPE` from this transport.

---

## Z8. Honest A3 leakage and the TOCTOU boundary (R8)

Closes Sol M2 and X21-M7.

### Z8.1 Fixed reply bytes; no timing secrecy

§W5.1's fixed pre-terminal shape is **retained verbatim**: every
pre-terminal `OPERATION_STATUS` observation returns exactly
`status = OK`, `detail` keys exactly `{operation_id, phase: "PENDING"}`;
`ADMITTED`, `RUNNING`, and `PENDING_SETTLEMENT` never appear in a reply;
`PROMOTED` appears only after `SETTLEMENT.json` is durable;
`QUARANTINED` is reported as `FAILED` only after the complete signed
invalid terminal set is durable. Its timing claim is replaced by the
exact honest boundary, normative:

> Official pre-terminal reply **bytes** are fixed to `PENDING`. Reply
> latency, FIFO and pipe backpressure, filesystem and endpoint metadata,
> path existence, worker timing, scheduling variability, and every other
> same-UID observation are **not** mechanically confidential under signed
> A3. They are T-process procedural facts only. They are permanently
> **non-citable**, and they may not enter selection, Q, C, C1–C6, any
> blinding claim, any candidate or learner judgement, or any scientific
> interpretation. This is the same-UID procedural residual the author
> selected; it is stated, not claimed away.

The same-UID residual of §W5.3 (a deliberate process reporting a live
unrelated PID, or escaping into an untracked session) and of §W6.4
(escaped children) is unchanged.

### Z8.2 What the descriptor checks do and do not prove

§W6.2's assertion that a deliberate same-UID modification of `out/` "is
detected" by re-verifying `st_size`, `st_ino`, and `st_nlink` is
**withdrawn**: an equal-size content substitution changes the promoted
bytes and leaves all three unchanged. Those three checks prove exactly
size, inode identity, and link count — nothing about content.

### Z8.3 Bounded pre-settlement verification pass

§W4.5's "Each byte is read exactly once; there is no second pass and no
post-exit hash pass" is replaced by: **each byte is *written* exactly
once, and exactly one bounded verification pass re-reads the written
bytes immediately before the settle step.**

```text
at file creation, through the held out/ directory fd, the supervisor opens
BOTH:
   w = os.open(rel, O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, dir_fd=out_fd)
   r = os.open(rel, O_RDONLY|O_NOFOLLOW|O_CLOEXEC,                 dir_fd=out_fd)
and holds both; the inline streaming SHA-256 is computed during the single
write pass, exactly as before.

immediately before the settle step, per file, in sorted path order:
1. v = os.open(rel, O_RDONLY|O_NOFOLLOW|O_CLOEXEC, dir_fd=out_fd)   # re-resolve
2. require (st_dev, st_ino) of v == those of r, and st_nlink == 1,
   and st_size == the bytes written                       # inode substitution
3. re-read the whole file through v with os.pread in
   T_OUTPUT_COPY_CHUNK_BYTES chunks and recompute content_sha256
4. require it to equal the inline hash                    # content substitution
any failure ⇒ the HASH quarantine class (§W4.7, unchanged)
```

The pass is bounded by the same signed ceiling: at most
`268_435_456 / 4_194_304 = 64` chunks per operation, and **one watchdog
step and one control-frame step are serviced between chunks**, exactly as
§W3.2 requires of every bounded long loop. It never resumes across a
crash: a crash mid-verification is the `SUPERVISOR_CRASH` quarantine
terminal at the conservative `bytes_reserved`, with no resumed offset and
no respawned worker (§W6.2's deletion of the false resume claim stands).

**Named residual.** Equal-size content substitution and inode
substitution are now **mechanically detected**. What remains is
same-name substitution of the `out/` **directory** between the
verification pass and the promotion `os.replace`, because the kernel
offers no rename-by-descriptor: `os.replace` resolves `out` by name in
the held parent directory fd. That residual is A3 **procedural**, is
named here rather than claimed closed, and is not a Q/C or blinding
claim.

---

## Z9. Remaining exactness repairs (R9)

### Z9.1 `T_MIN_HEARTBEAT_INTERVAL_NS` gets a normative rule (Opus minor 1)

> A `HEARTBEAT` occurrence whose captured `cursor_reading_ns` is less
> than `T_MIN_HEARTBEAT_INTERVAL_NS` after the owning lease's
> `last_charged_reading_ns` is `REFUSED`/`BUSY` (`retryable = true`) as a
> terminal effect with **empty** tuples: no charge event, no successor
> lease, no watchdog publication, no ledger append.

This is a control-plane append-rate bound. It changes **no** E1
arithmetic: charging is the cursor difference `end − start`, so a refused
heartbeat loses no device time and the full interval is charged at the
next accepted heartbeat. It moves no signed constant and creates no new
scientific or resource cell.

### Z9.2 Frame arithmetic that is jointly satisfiable (Opus minor 2)

```text
T_CONTROL_FRAME_MAX_BYTES        = 4096   (unchanged)
T_REQUEST_ENVELOPE_MAX_BYTES     = 1536   (bound on every envelope field
                                           other than "arguments")
T_ARGUMENTS_MAX_BYTES            = 2560   (= 4096 − 1536)
T_ARGV_MAX_ELEMENTS              = 32     (was 64)
T_ARGV_MAX_BYTES                 = 768    (was 4096; raw UTF-8 bytes summed
                                           over the argv elements)
argv character class             = printable ASCII 0x20–0x7E only
T_REPLY_MAX_BYTES                = 2048
```

Worst-case arithmetic, stated so both implementers compute the same
bound. The envelope's fixed cost is at most 1536 bytes: one 44-byte
schema string, `scientific_outcome`, five 64-hex fields (generation,
activation record, intent scope, idempotency key, acked reply hash), the
command, `occurrence_mode`, `occurrence_index`, `client_pid`,
`client_start_identity`, `client_boot_identity`, `client_monotonic_ns`,
and the pinned `reply_fifo` (≤ 200 bytes), with keys, quotes, colons, and
commas. The largest `arguments` object is `CLAIM`'s: five 64-hex fields,
`device_units`, `device_identity`, and `argv`. With printable ASCII only,
JSON escaping expands at most ×2 (`"` and `\`), so the serialized argv is
at most `2 × 768 + 3 × 32 + 10 = 1642` bytes, and the whole `CLAIM`
arguments object is at most `1642 + 640 = 2282 ≤ 2560`. The frame check
remains authoritative and fail-closed: any frame exceeding
`T_CONTROL_FRAME_MAX_BYTES`, or any argv exceeding either argv bound, or
any argv element containing a byte outside 0x20–0x7E, is
`INVALID`/`FRAME_LENGTH` or `INVALID`/`SCHEMA` respectively. No legal
reply exceeds `T_REPLY_MAX_BYTES`: the largest is the `PROMOTED`
observation — six 64-hex release-token fields, `settlement_sha256`,
`operation_id`, `phase` — plus the reply envelope of §Z10.2, at most
about 1500 bytes.

### Z9.3 Per-role `--officina-ctrl-fds` order (Opus minor 3)

Pinned in §Z3.3: `CONTROLLER` = (control-request write, control-reply
read); `WORKER` = (worker-status write, framed-output write); both
`dup2`'d by the adapter to `T_CTRL_FD_LOW = 3` and
`T_CTRL_FD_HIGH = 4` in that order, verified to be pipes, and re-verified
after `SIGCONT`.

### Z9.4 Serve preflight device identity (Opus minor 4)

```text
require st_dev(successor/officina/runtime_control/T_SUPERVISOR/operations)
     == st_dev(successor/officina/runtime)
and, if runtime/T_PROMOTED/ already exists,
     == st_dev(successor/officina/runtime/T_PROMOTED)
```

`successor/officina/runtime/` is an existing root (it holds the tracked
immutable `T_RUNTIME.lock`), so the comparison no longer depends on a
lazily created promoted directory. A mismatch ⇒ **no serve**, so `EXDEV`
still cannot arise at promotion time and no cross-device fallback exists
(§W6.3, otherwise unchanged).

### Z9.5 Target and interpreter preflight

At serve preflight: `interpreter_argv0` (element 0 of the supervisor's own
`/proc/self/cmdline`) must be an existing regular file with `X_OK`;
otherwise no supervisor serves. At `CLAIM` acceptance, before the spawn
intent is written: `argv[0]` of the client-supplied prefix must be an
existing regular file with `X_OK`; otherwise `REFUSED`/`BOOTSTRAP`
(`retryable = false`), with no intent, no child, and no claim. The
adapter re-checks at its step 4 and `os._exit(4)`s on failure, which the
supervisor observes as the `BOOTSTRAP` route.

### Z9.6 Concurrent client `.done` `EEXIST` (Opus minor 6)

Structurally, §Z1.3 gives concurrent clients distinct occurrences, so two
clients no longer converge on one `.done.json`. The continuation is
pinned anyway in §Z1.8: equal `effect_reply_sha256` ⇒ continue silently;
different ⇒ exit `5`, send nothing further, delete nothing.

### Z9.7 Namespace and reference reconciliation

| Namespace | v2.1.1 status |
|---|---|
| `runtime_control/T_SUPERVISOR/` | `SPAWN.lock`, `SPAWNING.json`, `SPAWNING_CHILD.json` (new), `SUPERVISOR_IDENTITY.json`, `REQUEST.fifo`, `REPLY/`, `CHILDREN/`, `JOURNAL/` (per-key dirs + `TOMBSTONES/`), `WATCHDOG/` (`LEASES.json`, `WATCHDOG_CHILD.json` (new), `FREEZE/<witness_id>.json`), `CAPACITY/`, `operations/` |
| `runtime_control/T_CLIENT_INTENTS/` | client convenience cache only (§Z1.4); freely deletable; never authority |
| `JOURNAL/<key>/` | `accepted.json`, `committed.json`, `reply.json`, `ack.json` — four immutable predecessor-bound no-replace phases, unchanged in shape |
| `runtime/T_PROMOTED/` | unchanged; archival-excluded; untracked; released only by §Z6.5 |
| `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/` | **new**; author-installed only; supervisor read-only; archival-excluded and untracked, inheriting the exclusion of the `T_PROMOTED` custody it disposes, so **no signed activation-protocol §B archival set changes** |
| `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_*_SIGNATURE.md` | **tracked** author signature file; must be committed before use, so the clean-HEAD rule is respected |
| deleted names | `ALREADY_DELIVERED` as an operation state is retained; `spawning_id`-in-`cmdline` discovery, `WATCHDOG` spawn-intent role, `last_effect_reply_sha256`, `acknowledged_high_water_occurrence`, `output_relative_paths`, and every over-declaration release are **deleted** |

Every reference in v2 and v2.1 to a deleted name resolves to its
replacement above. No free-form decision value enters any scientific,
resource, or invalidity field anywhere in this correction: every new
field is a hash, an identity, a bounded integer, a closed enum, a
canonical path, or a canonical UTC timestamp.

---

## Z10. Envelopes, schemas, enums, and the authority table

### Z10.1 Request envelope (replaces §W1.2's key list)

```text
schema ("philosophia.officina.t-control-request.v1"),
scientific_outcome, supervisor_generation_sha256, command,
activation_record_sha256, intent_scope_sha256, occurrence_mode,
occurrence_index, idempotency_key_or_null,
acked_effect_reply_sha256_or_null, arguments,
client_pid, client_start_identity, client_boot_identity,
client_monotonic_ns, reply_fifo
```

`occurrence_mode ∈ {NEW, RETRY}`; `occurrence_index` is an `int ≥ 1`;
`idempotency_key_or_null` may be `null` only when
`occurrence_mode = NEW`. `semantic_request_sha256` is unchanged and still
excludes every transport field. Everything else in §W1.2 — the
authenticated-but-excluded field list, the three journal cases as amended
by §Z1.5, and the generation-total retry rule — is unchanged.

### Z10.2 Reply envelope (replaces §W1.2's transport-binding sentence)

```text
schema ("philosophia.officina.t-control-reply.v1"),
scientific_outcome, supervisor_generation_sha256, request_sha256,
intent_scope_sha256, occurrence_index, idempotency_key,
effect_reply_sha256, next_occurrence_index, status, detail
```

The four added control identifiers make the reply the **durable
occurrence handle** (§Z1.1), hand the client the exact hash it must echo
to acknowledge (§Z1.7), and give it the authoritative next index without
touching §W5.2's closed `detail` key sets — which is Opus's X21-C5 repair
(c) realized in the envelope rather than in the `REFUSED` detail.
`next_occurrence_index` and `occurrence_index` are control integers, never
outcomes. `detail` remains exactly §W5.2's matrix.

### Z10.3 `t-request-accepted.v1` (replaces §W1.3's key list)

```text
schema, scientific_outcome, idempotency_key, intent_scope_sha256,
occurrence_index, occurrence_mode, semantic_request_sha256, command,
arguments_sha256, activation_record_sha256,
supervisor_generation_sha256_at_accept, allocating_client_start_identity,
allocating_client_boot_identity, pre_ledger_head_sha256, pre_state_sha256,
process_id_or_null, lease_sha256_or_null, effect_plan, created_utc
```

`committed.json`, `reply.json`, and the predecessor-binding rule are
unchanged; `ack.json` changes only in its `ack_source` enum.

### Z10.4 `ack_source` enum

```text
SUCCESSOR_OCCURRENCE, PROCESS_TERMINAL, DELIVERY_ACK, CLIENT_ECHO
```

with the preconditions of §Z1.7.

### Z10.5 Closed enums (replaces §W5.2's token lists)

```text
refusal tokens:
STALE_GENERATION, UNRESOLVED_BATCH, UNRESOLVED_JOURNAL, G5_BLOCKED,
E3_DUE, NO_CAPACITY, NOT_LIVE, DEADLINE_FREEZE, BUSY, NOT_FOUND,
BOOTSTRAP, ALREADY_ACKNOWLEDGED, WATCHDOG_UNACKED,
OCCURRENCE_INDEX, SUPERSEDED_PLAN

INVALID tokens:
ROLE, SCHEMA, IDENTITY, REPLAY_BYTES, GENERATION, BOUND,
FRAME_LENGTH, INTENT_KEY
```

Exactly two refusal tokens are added. No free text; no result hash before
`PROMOTED`; no learner field anywhere.

### Z10.6 Process / FD / lock table (replaces §W2.8's rows)

| Process | Created by | Session | `T_RUNTIME.lock` | `SPAWN.lock` | Capability | Endpoints | Inherited FDs | Exec? |
|---|---|---|---|---|---|---|---|---|
| CLI client | user shell | caller | never | `LOCK_EX\|LOCK_NB`, bounded retry, held from before the first fork until the identity is live-verified | never | `REQUEST.fifo` + own reply FIFO + bootstrap-pipe read end | none of the supervisor's | — |
| Supervisor | CLI `fork`→`setsid`→`fork`, in-process entry | own | yes (epochs) | retained until the identity is installed, then closed | sole issuer | owns FIFO + every pipe | all scrubbed except `SPAWN.lock`, the bootstrap-pipe write end (closed at step c), and its own sealed pipes | **no** |
| Freezer watchdog | supervisor `fork`, in-process entry, recorded by `WATCHDOG_CHILD.json` | own | **never** | never | **never** | sealed update/ack pipes only | those pipes only | **no** |
| Bootstrap adapter → controller | supervisor `Popen` of the adapter root | own | never | never | never | control pipes at pinned fds 3 (request write) and 4 (reply read) | exactly 0,1,2,3,4 after step 3 | yes (adapter `exec`s the target after `SIGCONT`) |
| Bootstrap adapter → worker | supervisor `Popen` of the adapter root | own | never | never | never | **no control endpoint**; fd 3 status write, fd 4 framed-output write | exactly 0,1,2,3,4 after step 3 | yes |

### Z10.7 Durable object, authority, and retention table (replaces/extends §W7)

Every `runtime_control/**` object still uses the signed §3 durability
sequence, is canonical ASCII JSON with a trailing newline,
`scientific_outcome: false`, recursively scientific-field-rejecting,
strict `int`, archival-excluded, untracked, and has exactly one legal
layout. **Authority column:** `convenience` = never read by the
supervisor; `transport` = frames, never at rest; `witness` = control-plane
evidence that must pass an acceptance predicate; `runtime` = supervisor
authority; `author` = author authority.

| Object | Path (under `successor/officina/`) | Schema | Install | Writer / lock | Authority | Removed by |
|---|---|---|---|---|---|---|
| Spawning marker | `runtime_control/T_SUPERVISOR/SPAWNING.json` | `t-supervisor-spawning.v1` | no-replace | CLI under `SPAWN.lock` | runtime | supervisor after identity live-verified, or next lock holder |
| Spawning child record | `…/SPAWNING_CHILD.json` | `t-supervisor-spawning-child.v1` | no-replace | grandchild, first action | runtime | grandchild at identity install, or the killing CLI |
| Bootstrap frame | bootstrap pipe (no file) | `t-supervisor-bootstrap.v1` | — | grandchild | transport | — |
| Supervisor identity | `…/SUPERVISOR_IDENTITY.json` | `t-supervisor-identity.v1` | no-replace | grandchild under `SPAWN.lock` | runtime | client takeover phase 1 |
| Spawn intent | `…/CHILDREN/<spawn_intent_id>.json` | `t-spawn-intent.v1` (§Z3.2) | no-replace | supervisor under `T_RUNTIME.lock` | runtime | supervisor after process terminal + archival |
| Fork-child record | `…/WATCHDOG/WATCHDOG_CHILD.json` | `t-fork-child.v1` | no-replace | supervisor under lock | runtime | supervisor at generation end / takeover |
| Child log dir | `…/CHILDREN/<spawn_intent_id>/` → `…/CHILDREN/<process_id>/` | (bytes) | mandatory atomic rename | supervisor | runtime | supervisor after terminal + archival |
| Journal accepted | `…/JOURNAL/<key>/accepted.json` | `t-request-accepted.v1` (§Z10.3) | no-replace | supervisor under lock | runtime | GC per §Z1.9 |
| Journal committed / reply / ack | `…/JOURNAL/<key>/{committed,reply,ack}.json` | `t-request-committed.v1` / `t-request-reply.v1` / `t-request-effect-ack.v1` | no-replace | supervisor under lock | runtime | GC per §Z1.9 |
| Scope tombstone | `…/JOURNAL/TOMBSTONES/<scope>.json` | `t-request-tombstone.v1` (§Z1.9) | **atomic replace**, both integers monotone | supervisor under lock | runtime | **never** |
| Client intent slot / terminal | `runtime_control/T_CLIENT_INTENTS/<scope>.<n>[.done].json` | `t-client-intent.v1` / `t-client-intent-terminal.v1` | no-replace | the client | **convenience** | the client, at any time, with no correctness effect |
| Watchdog lease table | `…/WATCHDOG/LEASES.json` | `t-watchdog-lease-table.v1` | atomic replace | supervisor under lock | runtime | generation end |
| Watchdog ack frame | ack pipe (no file) | `t-watchdog-ack.v1` | — | watchdog | transport | — |
| Freeze observation | `…/WATCHDOG/FREEZE/<witness_id>.json` | `t-freeze-observation.v1` (§Z4.5) | no-replace | **watchdog** (or supervisor when the watchdog is dead) | **witness** — evidence only after §Z4.6 | supervisor after the settlement's archival commit |
| Capacity reservation / settled / disposed | `…/CAPACITY/<op>[.settled\|.disposed].json` | §Z6.2 | no-replace | supervisor under lock | runtime | never |
| Output bound / admission / release / settlement / quarantine / delivery ack | `…/operations/<op>/{BOUND,OPERATION,RUNNING,SETTLEMENT,QUARANTINE,DELIVERY_ACK}.json` | `t-operation-output-bound.v1`, `t-operation-admission.v1`, `t-operation-release.v1` (§Z5.1), `t-operation-settlement.v1`, `t-operation-quarantine.v1`, `t-delivery-ack.v1` | no-replace | supervisor under lock | runtime | never |
| Worker output frame / status | output and status pipes (no file) | `t-worker-output-frame.v1` / `t-worker-status.v1` (§Z7.1) | — | worker | transport (untrusted) | — |
| Promoted tree | `runtime/T_PROMOTED/<op>/` | (bytes) | atomic `os.replace` | supervisor under lock | runtime | only after §Z6.5 |
| **Author custody disposition** | `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json` | `t-output-custody-disposition.v1` (§Z6.4) | author-installed, no-replace, single use | **the author**; the supervisor never writes here | **author** | never (the supervisor never removes it) |
| Author signature file | `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_*_SIGNATURE.md` | (tracked markdown; §Z6.4 grammar) | tracked commit | the author | **author** | never |
| Request / reply frames | `…/REQUEST.fifo`, `…/REPLY/<…>.fifo` | `t-control-request.v1` / `t-control-reply.v1` | — | client / supervisor | transport | client on terminal; supervisor at takeover |
| Computed identities | (never stored alone) | `t-semantic-request.v1`, `t-intent-scope.v1`, `t-intent-key.v1` | — | — | — | — |

---

## Z11. Crash-cut matrix (replaces and extends §W8)

Replaced and added rows; every other §W8 row carries forward verbatim.

| Cut | Single continuation |
|---|---|
| `SPAWNING.json` durable, CLI dies before fork | next `SPAWN.lock` holder finds no `SPAWNING_CHILD.json`, unlinks the marker, spawns |
| Grandchild alive, identity not installed, CLI dies | `SPAWN.lock` still held by the grandchild's retained fd; a second CLI's bounded `LOCK_NB` retry expires, takes the §Z3.5 stuck-holder route, kills by the recorded pid + start identity, proves death, and retries once. **No client blocks forever and D1 is not wedged** |
| Grandchild hangs before identity install (including the watchdog first-ack wait) | its own bounded `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` expires ⇒ it kills its watchdog by record, unlinks `SPAWNING_CHILD.json`, and `_exit(3)`s without serving |
| Grandchild dies before identity install | CLI's bounded bootstrap read/poll expires ⇒ `REFUSED`/`BOOTSTRAP`; lock released on CLI exit |
| Spawn intent durable, no child | resolve the intent by the §Z3.4 predicate finding nothing; **within the accepting generation** an open plan may spawn afresh under the same intent; across generations the plan is closed (§Z2.4) |
| Child stopped, no claim | discovered at fixed index by §Z3.4; killed by group; death proved; intent resolved |
| Watchdog forked, record durable, first ack absent | grandchild's bounded wait ⇒ kill by record, prove death, exit without serving |
| Prior-generation watchdog still live at takeover | killed by its `WATCHDOG_CHILD.json` record in phase 1/2A; its witnesses fail §Z4.6 conjunct 3 ⇒ `UNKNOWN` route |
| Allocation: `accepted.json` durable, tombstone not advanced | `next(scope)`'s `max` repairs the tombstone under the lock; no index is reused |
| Allocation: `EEXIST` on `accepted.json` | re-read the existing plan and re-enter §Z1.5 row 2; never overwrite |
| `NEW(i)` with `i > next` or a foreign allocator | `REFUSED`/`OCCURRENCE_INDEX`; envelope carries `next_occurrence_index`; client re-anchors |
| `RETRY(i)` for a never-allocated occurrence | `REFUSED`/`OCCURRENCE_INDEX`, `retryable = false` |
| Occurrence `i` GC'd, old frame arrives | `i ≤ acknowledged_prefix` ⇒ `REFUSED`/`ALREADY_ACKNOWLEDGED`; otherwise record-first invalidity (§Z1.5 row 8) |
| Client intent files deleted or absent entirely | no effect: `NEW(1)` → re-anchor → `NEW(next)`; forward progress always available |
| Head moved by ordinary later history under a committed/replied plan | §Z2.2 accepts the verified descendant and serves the cached reply; **no G5** |
| Intervening conflicting entry, no locator applied | `REFUSED`/`SUPERSEDED_PLAN` cached; the client re-intends a `NEW` occurrence |
| Intervening conflicting entry, some locator applied | record-first invalidity naming the plan and the entry |
| Supervisor loss with accepted-only behavioral plans | phase 2A freezes and settles every affected stream through the signed all-live invalid route **before** any reducer step; phase 2B completes non-behavioral work only |
| Lease renewed, table published, ack absent | old deadline authoritative; watchdog drains before freezing so a renewed lease is not frozen at a superseded deadline; absence timeout ⇒ §W3.5 dead-watchdog route with the occurrence cached as `REFUSED`/`WATCHDOG_UNACKED` recording the durable charge |
| Freeze witness present at supervisor start | run §Z4.6; accepted ⇒ §W3.4 route; rejected ⇒ supervisor-written `UNKNOWN` witness ⇒ unknowable all-live invalid settlement |
| Proved-quiescent sample equals the deadline | bounded later monotonic sampling with re-proved quiescence; no strict progress ⇒ `UNKNOWN`; **never a valid zero-overrun branch** |
| `RUNNING.json` durable, `SIGCONT` not sent, same generation | complete the idempotent release, then commit and cache |
| `RUNNING.json` durable, `SIGCONT` not sent, supervisor lost | worker frozen and settled; never resumed; plan closed as that invalid terminal |
| `reply.json` durable, `RUNNING.json` absent | record-first invalidity naming both paths |
| Zero output frames with a valid `COMPLETED` status | canonical empty result: promote with `result_sha256 = SHA-256(b"[]")`, `actual_bytes = 0` |
| Output pipe EOF at a boundary with no status frame | `WORKER_FAILED` quarantine + signed invalid route, cause `PROCESS` |
| Verification pass detects a content or inode mismatch | `HASH` quarantine class; no promotion; capacity retained |
| Crash during the verification pass | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; no resumed offset; no respawned worker |
| Settlement, quarantine, rename, promotion, or delivery ack durable | **capacity unchanged**; nothing released |
| Author disposition present, custody still exists | refuse; release nothing; admissions still governed by the full `accounted_total` |
| Author disposition verified, `.disposed.json` install crashes | no release recorded; the operation still counts `bytes_reserved`; the same disposition re-verifies and installs idempotently by no-replace |
| Second author disposition for one operation | releases nothing; contradiction ⇒ record-first invalidity naming both paths |

No cut exposes promoted results without `SETTLEMENT.json`. No cut
double-charges a cursor. No cut releases retained capacity without a
verified author disposition **and** a same-lock-epoch descriptor-safe
custody-absence proof. No cut continues behavior across a supervisor
loss. No cut converts a healthy heartbeat into an invalidity.

---

## Z12. Disposition of prior closures and the test delta

### Z12.1 Inherited closures are qualified, not asserted

Every row of §W9 that read "closed" now reads **"closed in v2.1;
confirmation pending independent v2.1.1 X/Y"**, and the three rows Opus
minor 7 named are further qualified:

| §W9 row | v2.1.1 reading |
|---|---|
| X-C2 spawn intent / `waitpid` | closed **subject to** §Z3.1–§Z3.4 (the v2.1 id was uncomputable) |
| X-C6 durable-object contradictions / undefined schemas | closed **subject to** §Z7.1 (`t-worker-status.v1`) and §Z10.7 |
| X-M1 entry surface | closed **subject to** §Z3.3 (one refusal-first adapter token) and §Z3.5 (the grandchild marker could not exist) |
| X-M10 intent-id collision | closed **subject to** §Z3.1 (the preimage is now computable) |
| all other §W9 rows | closed in v2.1; **no v2.1.1 finding reopens them**; confirmation pending |

No finding in this document is claimed closed by author assertion. The
author line cannot confirm its own bytes (see the authorship note); only
the independent v2.1.1 X-line and Y-line reviews can.

### Z12.2 Implementation and test obligations (delta; **no implementation authorization**)

§W10's rows 1–50 carry forward. Added obligations, each a **test
obligation only** — this document authorizes no implementation, no
commit, no host change, and no signature:

| # | Test | Covers |
|---|---|---|
| 51 | `NEW` with a fresh index allocates; `NEW` with the same index by the same client is idempotent; by a different client ⇒ `OCCURRENCE_INDEX` + `next_occurrence_index` | Z1.3, Z1.5, X21-C5 |
| 52 | two concurrent same-scope `NEW`s receive distinct occurrences under every interleaving | Sol C1.1, Z1.3 |
| 53 | `T_CLIENT_INTENTS/` deleted entirely, mid-scope: forward progress in ≤ 2 round trips; no wedge; no reuse | X21-C5, Sol C1.2 |
| 54 | crash between `accepted.json` and the tombstone advance ⇒ `next(scope)` repairs; no index reused | Z1.3 |
| 55 | observation-form `OPERATION_STATUS` is journaled with empty tuples; a `RETRY` of a `PENDING` poll stays `PENDING` after promotion and after the delivery ack | Sol C1.3, Z1.6 |
| 56 | successor occurrence without the exact prior `effect_reply_sha256` acknowledges nothing; with it, acks exactly once | Sol C1.4, Z1.7 |
| 57 | `CLOSE` cannot acknowledge its own reply; its bytes stay redeliverable until `CLIENT_ECHO`; a lost `CLOSE` reply is recoverable | X21-M6 |
| 58 | GC only over a contiguous acknowledged prefix, in the ack's lock epoch; an unacked occurrence blocks every later one | X21-M5, Z1.9 |
| 59 | post-GC classification decided from the frame plus two tombstone integers; no old reply hash is consulted | X21-M5, Sol C1.5 |
| 60 | 64 unacknowledged occurrences in one scope ⇒ `UNRESOLVED_JOURNAL`; echoing the hash restores admission | Z1.9 |
| 61 | committed/replied plan with a verified descendant head is served, not invalidated, for arbitrary later history | Sol C2 |
| 62 | accepted-only plan: legal prefix resumes; conflicting suffix with no locator ⇒ `SUPERSEDED_PLAN`; with a locator ⇒ record-first invalidity; absent pre-head ⇒ record-first invalidity | Sol C2, Z2.3 |
| 63 | across a supervisor loss no reducer spawns, `SIGCONT`s, renews, admits, or installs a lease; phase 2A settles before phase 2B runs, at every injected cut | Sol C2, Z2.5 |
| 64 | `spawn_intent_id` computable and stable: template hash excludes both markers; complete argv hashed separately; respawn in-generation reproduces the intent | X21-C1, Sol C3.1 |
| 65 | grandchild bootstrap: pipe line + `SPAWNING_CHILD.json` before endpoints; hang at each of the five pre-identity cuts ⇒ bounded timeout, kill by record, no wedge; stuck-holder route kills and recovers | X21-C2, Sol C3.2 |
| 66 | watchdog has no spawn intent and no argv; its fork-child record identifies and kills it, including a prior generation's | X21-M4, X21-M2, Sol C3.3 |
| 67 | adapter: exact index layout, `dup2` to 3/4 per role, forbidden descriptors closed, target preflight, no signal disposition, self-stop before dispatch, `exec` only after `SIGCONT`; an arbitrary non-Officina target works unmodified | Sol C3.4, Z3.3 |
| 68 | renewal publication after every claim-start/renew/remove; `watchdog_table_seq` in the four plans; a process heartbeating every 30 s is **never** frozen or invalidated | X21-C3 |
| 69 | drain-before-freeze: a renewed lease is never frozen at a superseded deadline; ack absence ⇒ dead-watchdog route with `WATCHDOG_UNACKED` recording the durable charge | X21-C3, Opus Q2 |
| 70 | freeze acceptance predicate: each of the ten conjuncts violated singly ⇒ `UNKNOWN` route, never valid evidence; a planted witness never settles | X21-M1 |
| 71 | `freeze_ns == deadline_ns` ⇒ bounded later sampling; no strict progress ⇒ `UNKNOWN`; no valid zero-overrun branch exists | Sol M3 |
| 72 | `RUNNING.json` before `SIGCONT`; crash between every pair of the ten admission steps; a stopped worker never sits behind a cached `ADMITTED` in its own generation; after a loss it is settled, never resumed | X21-C4, Sol C4 |
| 73 | settlement, quarantine, rename, promotion, and delivery ack release **nothing**; only a verified disposition with a same-lock custody-absence proof releases exactly `bytes_reserved`; each of the twelve verifier conjuncts violated singly refuses | Sol C5, Sol M1, X21-M8 |
| 74 | `t-worker-status.v1` exact keys; no status frame ⇒ `WORKER_FAILED`; zero-frame `COMPLETED` ⇒ empty promotion with `SHA-256(b"[]")`; equal-size content substitution and inode substitution detected by the verification pass; the directory-swap residual documented, not claimed closed; no timing-secrecy claim survives | X21-M3, X21-M7, Sol M2, Opus minor 5 |

---

## Z13. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** Occurrence allocation is
one CAS against one supervisor integer under one lock (§Z1.3); frame
classification is an eight-row total table over the frame plus two
tombstone integers (§Z1.5); acknowledgement has four sources with exact
preconditions (§Z1.7); the reducer has four routes decided by chain
membership (§Z2.2–§Z2.3); takeover has two ordered phases with a fixed
behavioral/non-behavioral partition (§Z2.4–§Z2.5); spawn identity is two
hashes over two explicitly stated domains (§Z3.1); the adapter argv is a
thirteen-index layout with a fixed marker index (§Z3.3); the grandchild
has one sealed pipe, one durable record, and three bounded timeouts
(§Z3.5); the watchdog has one publication trigger, one drain-before-freeze
rule, one strict-progress rule, one witness name, and one ten-conjunct
acceptance predicate (§Z4); admission is ten ordered steps with a durable
release locator (§Z5.1); capacity has one accounted formula, three
artifacts, and exactly one release governed by a twelve-conjunct verifier
(§Z6); the worker status frame has one key set and the transport has a
total EOF table (§Z7); the frame arithmetic is stated numerically
(§Z9.2). No clause resolves to "as reviewed", "as appropriate", or "at
the implementer's discretion".

**Compatibility classification.** Unchanged from §W11: an
engineering/control amendment surface over the signed harness composite,
containing no protocol amendment except §W6.5's explicitly named
supersession of harness §5a's physical at-or-before-deadline sentence.
The K1 envelope constants are author-signed and unmoved and are now
implemented literally, including the no-replenishment clause. No signed
archival set changes; no `.gitignore` or configuration change is
authorized; the import allowlist delta remains **none** (every primitive
used — `os.fork`, `os.pipe2`, `os.dup2`, `os.execv`, `os.pread`,
`os.listdir`, `os.open` with `dir_fd`, `os.stat`/`os.access`,
`os.statvfs`, `os.killpg`, `os.waitpid`, `fcntl.flock`,
`subprocess.Popen` with `start_new_session` and `pass_fds`,
`time.clock_gettime_ns`, `hashlib`, `json`, `re`, `pathlib`, `enum`,
`dataclasses` — is inside the pinned allowlist, and `select`,
`selectors`, `signal`, `ctypes`, and `sys` remain outside it, which is
why the poll is `time`-paced and why `interpreter_argv0` is read from
`/proc/self/cmdline`).

**No author cell is reopened.** A3 keeps its procedural same-UID residual
and gains only honesty (§Z8) — it is still not a security boundary. B1
keeps journaled exactly-once effects and retry-stable replies; §Z1
repairs their allocation, acknowledgement, and GC, not their policy. C1
keeps a watchdog that witnesses and freezes and never holds runtime
authority or settles; §Z4.6 adds **supervisor-side** validation, which
strengthens C1's single-authority shape rather than creating a second
one. D1 keeps no idle exit, and §Z3.5's bounded timeouts protect it from
being wedged. K1 keeps its five signed constants and is now implemented
literally, including no replenishment at settlement, rename, promotion,
failure, or unused reservation. **No new author-choice token is proposed,
and none was found to be unavoidable.**

**Negative space.** This correction creates nothing executable and
authorizes no implementation, commit, host change, process, supervisor,
controller, worker, watchdog, adapter, endpoint, pipe, FIFO, journal
instance, spawn intent, operation, output bound, promoted object,
capacity artifact, custody disposition, capability, lease, batch,
activation artifact, production call-graph manifest, entropy, E1/E2/E3
spend, world, learner, candidate, Q attempt, Q/C object, datum, outcome,
Proof, or claim movement. It moves no E1/E2/E3 constant, none of the nine
signed events, no runtime schema, no roots tuple, no batch arithmetic, no
import allowlist entry, and no T/Q/C boundary. It predicts no
qualification and no C1–C6 outcome. Process invalidity, resource
exhaustion, and missing evidence remain infrastructure facts and are
never scientific evidence. New artifacts are control-plane,
T-development-only, archival-excluded, untracked, and permanently
non-citable for Q/C.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable by this document. Its only next
authorization step is independent bounded X/Y confirmation of the
**v2.1.1 bytes**. `successor/officina/runtime/` contains only
`T_RUNTIME.lock`; `successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
