# Officina supervisor and control-channel amendment — v2.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. This
correction carries the complete v2 draft
(`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`,
preserved unedited as review evidence) forward **verbatim except for
the exact replacements in §W0**. It applies every Critical, Major, and
Minor finding of the two formal reviews
(`reviews/opus_officina_supervisor_control_channel_v2_review.md`,
`reviews/sol_officina_supervisor_control_channel_v2_review.md`) and
embeds the signed output-capacity selection.

Signed author cells embedded, none reopened:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

Author token candidate, still **not signable** until both fresh X/Y
confirmations accept this v2.1:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature,
review, or runtime artifact. Starts no process, endpoint, pipe, FIFO,
journal, watchdog, worker, or output transport. Creates no entropy,
activation, capability, world, learner, datum, or outcome. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9ab9ae65d7ddc98164118275dfbf84cc2e188202f606d4239a65abf2861d9f96  reviews/fable_officina_supervisor_control_channel_v2_closure.md
bc731d96d13c8bc6741a94d320ed51ae35cfcbdc38417fedee3ddf3684cec9b2  reviews/opus_officina_supervisor_control_channel_v2_review.md
edfbef915246080a6e022ec5e95e177603c83e542f4068dc1f3ad8d367fcf591  reviews/sol_officina_supervisor_control_channel_v2_review.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
9db9f263ebcf705c2e8b5486bc6673104f94f6d8b59fd764e92bd946e5245168  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
9e3871a0287982efd94f48ca3428606143c69728020a5920a0710b6e38ca3bac  reviews/fable_officina_supervisor_output_capacity_author_choice_packet_v1.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

## Engineering constants (control plane only; no scientific or resource cell)

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
T_MIN_HEARTBEAT_INTERVAL_NS             = 1_000_000_000
T_ARGV_MAX_ELEMENTS                     = 64
T_ARGV_MAX_BYTES                        = 4096
T_OUTPUT_PER_STREAM_MAX_BYTES           = 67_108_864
T_OUTPUT_AGGREGATE_MAX_BYTES            = 34_359_738_368
T_OUTPUT_FS_SAFETY_MARGIN_BYTES         = 8_589_934_592
T_OUTPUT_COPY_CHUNK_BYTES               = 4_194_304
T_OUTPUT_PATH_MAX_BYTES                 = 1_024
T_OUTPUT_PATH_COMPONENT_MAX_BYTES       = 255
SIGCONT = 18; SIGSTOP = 19; SIGKILL = 9; SIGTERM = 15; SIGNAL_0 = 0
```

The five `T_OUTPUT_*` values are the author-signed envelope of
`successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
and may not be changed by any implementation decision.

---

## W0. Complete replacement index (v2 → v2.1)

Everything in v2 not named here carries forward verbatim.

| v2 locus | Action |
|---|---|
| §V2.0 replacement index | **extended** by §W6.5: signed harness §5a's "executes the v2.1 §1 sequence **at or before it**" is explicitly superseded |
| §V2.1.2 "grandchild closes **every** inherited descriptor including the spawn-lock fd **before** writing the identity record" | **replaced** by §W2.2 (spawn-lock fd retained through identity install; every other inherited fd scrubbed) |
| §V2.1.2 "Double-fork from the CLI (same module image…)" | **replaced** by §W2.1 (in-process post-fork function entry; no exec, no argv) |
| §V2.1.4 spawn-intent key list | **replaced** by §W2.3 (adds `process_sequence`, `argv`, `created_utc` resolution) |
| §V2.1.4 "Crash after spawn intent + child, before claim: takeover kills by registry identity" | **replaced** by §W2.4 (argv-embedded `spawn_intent_id` + `/proc/*/cmdline` discovery) |
| §V2.1.4 "`os.waitpid(pid, WUNTRACED)` and requires `WIFSTOPPED`" | **replaced** by §W2.5 (bounded nonblocking wait, `BOOTSTRAP` refusal, kill/reap route) |
| §V2.1.4 "install signal dispositions only as required to not defeat stop" | **replaced** by §W2.6 ("installs **no** signal dispositions before the self-stop") |
| §V2.1.4 "**first** executable actions, before any behavior-capable import" | **replaced** by §W2.6 (capability invariant; the literal first-instruction claim is withdrawn) |
| §V2.1.4 "optional rename of log dir to `CHILDREN/<process_id>/`" | **replaced** by §W2.7 (**mandatory** rename; one on-disk layout) |
| §V2.1.4 start/lease step "then `SIGCONT` the controller" | **replaced** by §W3.2 (watchdog table publication + ack precede `SIGCONT`) |
| §V2.1.5 process/FD table | **replaced** by §W2.8 |
| §V2.1.6 takeover (single-phase) | **replaced** by §W2.9 (client control-plane phase / supervisor runtime phase) |
| §V2.2.1 mechanical list incl. "escaped children" | **replaced** by §W6.4 (escaped children move to the A3 procedural residual; truthfulness qualifier added) |
| §V2.2.2 endpoint-role table peer proof | **replaced** by §W5.3 (group members and descendants rejected) |
| §V2.2.3 pre-settlement observation | **replaced** by §W5.1 (one fixed `PENDING` shape) |
| §V2.3 durable-object table and "atomic no-replace unless noted" | **replaced** by §W7 (complete table; every object's owner, lock, durability, retention, and removal actor) |
| §V2.4.1 transport | **extended** by §W5.4 (newline framing, bounded buffering, canonical `reply_fifo`, dead-reader route) |
| §V2.4.2 request envelope keys | **replaced** by §W1.2 (adds `activation_record_sha256`, `intent_scope_sha256`, `occurrence_index`, `acked_effect_reply_sha256_or_null`) |
| §V2.4.2 "`idempotency_key`: client-generated, retry-stable" | **replaced** by §W1.1 (pinned, supervisor-checkable derivation) |
| §V2.4.3 `CLAIM` argument row | **extended** by §W5.5 (`argv` element/byte bounds) |
| §V2.4.4 `OPERATION_ADMIT` / `OPERATION_STATUS` argument rows | **replaced** by §W4.3 / §W1.6 |
| §V2.4.5 reply `detail` matrix | **replaced** by §W5.2 |
| §V2.4.5 closed refusal / `INVALID` enums | **replaced** by §W5.2 (adds `BOOTSTRAP`, `ALREADY_ACKNOWLEDGED`, `WATCHDOG_UNACKED`, `FRAME_LENGTH`, `INTENT_KEY`) |
| §V2.5 entire section (one mutable journal file; rules 1–8) | **replaced** by §W1.3–§W1.7 |
| §V2.6.3 lease table / ack | **replaced** by §W3.2 (publish-and-ack before behavior; watchdog-sampled ack liveness) |
| §V2.6.4 freeze sequence and "supervisor re-derives by sampling" | **replaced** by §W3.3 (proved quiescence, watchdog-written observation, no synthesized timestamp) |
| §V2.6.5 overrun rule incl. the zero-overrun paragraph | **replaced** by §W3.4 (single route; `PROCESS` cause; zero-overrun branch deleted) |
| §V2.6.6 death/restart table | **replaced** by §W3.5 |
| §V2.7.1 bound install and "reserve/refuse" | **replaced** by §W4.2–§W4.4 |
| §V2.7.2 byte-accounting rules incl. "restartable from descriptor offset after crash" and the two release terminals | **replaced** by §W4.5–§W4.7 |
| §V2.7.3 `operation_id` preimage and worker context | **replaced** by §W4.3 (drops `output_bound_sha256`) and §W4.4 (no writable output path) |
| §V2.7.4 promotion order | **replaced** by §W6.1–§W6.3 |
| §V2.9.1 generation states | **replaced** by §W2.9 (two takeover phases) |
| §V2.9.3 operation states | **replaced** by §W4.8 |
| §V2.10 "internal serve / watchdog entry points … `--supervisor-serve` / `--watchdog-serve` tokens" | **replaced** by §W2.1 (tokens **deleted**) |
| §V2.11 crash-cut matrix | **replaced** by §W8 |
| §V2.12 acceptance matrix | **replaced** by §W10 |
| §V2.13 disposition map | **replaced** by §W9 |
| §V2.8 (metering, boundaries, §S6 carry) | **unchanged and closed** — carried forward verbatim; both reviews confirmed it |
| §V2.1.1, §V2.1.3, §V2.1.7, §V2.7.5, §V2.9.2, §V2.9.4, §V2.14 | **unchanged** |

---

## W1. Generation-total B1: intent identity, journal, reducer, acknowledgement

### W1.1 Semantic intent identity and its allocation (X-C1b, Sol C1.5)

Two identical `HEARTBEAT` arguments may be two distinct intended
effects or one retry of a lost effect. The identity below separates
them without entropy, without a clock, and without a ninth command.

**Intent scope** (the "what", excluding the occurrence):

```text
intent_scope_sha256 = SHA-256(canonical {
  schema: "philosophia.officina.t-intent-scope.v1",
  activation_record_sha256,
  command,
  arguments_sha256          # SHA-256 of the canonical arguments object
})
```

**Idempotency key** (the "which occurrence"):

```text
idempotency_key = SHA-256(canonical {
  schema: "philosophia.officina.t-intent-key.v1",
  intent_scope_sha256,
  occurrence_index          # int ≥ 1
})                          # 64 lowercase hex
```

Both derivations are **recomputed and checked by the supervisor** from
the frame's own `command`, `arguments`, `intent_scope_sha256`, and
`occurrence_index`. A mismatch is `INVALID`/`INTENT_KEY` with no state
movement. The key is therefore not "client-generated" in any sense the
supervisor must trust, and two independent client implementations
produce byte-identical keys.

**Client-side durable intent slot.** Clients own
`successor/officina/runtime_control/T_CLIENT_INTENTS/` (mode `0700`,
control plane, archival-excluded, untracked). Before its **first**
send a client must, under `flock(LOCK_EX)` on
`T_CLIENT_INTENTS/ALLOC.lock`:

1. enumerate `<intent_scope_sha256>.<n>.json`;
2. if the highest `n` has **no** sibling
   `<intent_scope_sha256>.<n>.done.json`, that occurrence is
   **unfinished** ⇒ this invocation is a **retry**: reuse it, allocate
   nothing;
3. otherwise allocate `n+1` and write
   `<intent_scope_sha256>.<n+1>.json`, schema
   `philosophia.officina.t-client-intent.v1`, keys exactly
   `schema, scientific_outcome, activation_record_sha256, command,
   arguments_sha256, intent_scope_sha256, occurrence_index,
   idempotency_key, created_utc`, atomic no-replace, file `fsync`,
   parent-directory `fsync`;
4. release the allocation lock and only then send.

On observing a terminal reply (and, for a release-token delivery, after
its durable acknowledgement of §W1.6) the client writes
`<intent_scope_sha256>.<n>.done.json`, schema
`philosophia.officina.t-client-intent-terminal.v1`, keys exactly
`schema, scientific_outcome, intent_scope_sha256, occurrence_index,
effect_reply_sha256, completed_utc`.

Consequences, each required by the mandate:

- a **new** intended heartbeat/status allocates a new
  `occurrence_index` ⇒ a different key ⇒ a distinct effect;
- a **retry** re-reads the unfinished slot ⇒ the identical key ⇒ the
  identical effect;
- a fresh short-lived CLI process recomputes everything from the
  durable slot: no PID, clock, or generation enters the key;
- a supervisor generation change is invisible to the key;
- **no entropy** is drawn and no scientific or control command is added;
- while an occurrence is unfinished the client cannot intend a *second*
  one in the same scope — an unresolved exactly-once effect must be
  resolved before a new one is intended. This is fail-closed and is the
  intended behavior.

A client that skips the durable slot damages only its own ability to
re-read a cached reply; the effect remains exactly-once because the
supervisor's journal, not the client's file, is authoritative. That
residual is A3 procedural and is stated as such.

### W1.2 Transport envelope and the semantic request (X-C1a, Sol C1.1)

Request keys **exactly**:

```text
schema ("philosophia.officina.t-control-request.v1"),
scientific_outcome, supervisor_generation_sha256, command,
activation_record_sha256, intent_scope_sha256, occurrence_index,
idempotency_key, acked_effect_reply_sha256_or_null, arguments,
client_pid, client_start_identity, client_boot_identity,
client_monotonic_ns, reply_fifo
```

```text
semantic_request_sha256 = SHA-256(canonical {
  schema: "philosophia.officina.t-semantic-request.v1",
  activation_record_sha256, command, arguments_sha256, idempotency_key
})
```

Excluded from the semantic hash, **required and authenticated on every
delivery**: `supervisor_generation_sha256`, `client_pid`,
`client_start_identity`, `client_boot_identity`, `client_monotonic_ns`,
`reply_fifo`. `request_sha256` (SHA-256 of the whole canonical frame)
survives **only** as the reply's transport binding.

Journal decision, exactly three cases:

1. journal hit on `idempotency_key` with **equal**
   `semantic_request_sha256` ⇒ run the reducer (§W1.5); no second
   effect;
2. journal hit with **different** `semantic_request_sha256` ⇒ reply
   `INVALID`/`REPLAY_BYTES`. **No record-first invalidity, no ledger
   append, no state movement, no G5.** A client protocol error can
   never drive global runtime state (X-C1c, X-M9ii);
3. miss ⇒ open a plan (§W1.3).

A retry after takeover carries the **new** generation and new client
fields, hits case 1, and receives the identical cached effect reply and
release-token bytes wrapped in a fresh current-generation envelope
(§W1.5). B1 is therefore generation-total; `STALE_GENERATION` is
returned only for a frame naming a generation that is neither current
nor recorded in the journal entry's accept record.

### W1.3 Immutable predecessor-bound journal phases (X-C6, Sol C1.3)

One directory per key, four no-replace files, `phase` = the highest
present file. No file is ever rewritten. Every write uses the signed §3
durability sequence (same-directory temp → file `fsync` → atomic
no-replace install → parent-directory `fsync`).

```text
runtime_control/T_SUPERVISOR/JOURNAL/<idempotency_key>/accepted.json
runtime_control/T_SUPERVISOR/JOURNAL/<idempotency_key>/committed.json
runtime_control/T_SUPERVISOR/JOURNAL/<idempotency_key>/reply.json
runtime_control/T_SUPERVISOR/JOURNAL/<idempotency_key>/ack.json
```

`philosophia.officina.t-request-accepted.v1` keys exactly:

```text
schema, scientific_outcome, idempotency_key, intent_scope_sha256,
occurrence_index, semantic_request_sha256, command, arguments_sha256,
activation_record_sha256, supervisor_generation_sha256_at_accept,
pre_ledger_head_sha256, pre_state_sha256, process_id_or_null,
lease_sha256_or_null, effect_plan, created_utc
```

`philosophia.officina.t-request-committed.v1` keys exactly:

```text
schema, scientific_outcome, idempotency_key, predecessor_sha256,
effect_event_sha256s (sorted tuple, possibly empty),
effect_artifact_sha256s (sorted tuple, possibly empty),
post_ledger_head_sha256, post_state_sha256, committed_utc
```

`philosophia.officina.t-request-reply.v1` keys exactly:

```text
schema, scientific_outcome, idempotency_key, predecessor_sha256,
effect_reply (object, keys exactly: status, detail),
effect_reply_sha256, cached_utc
```

`philosophia.officina.t-request-effect-ack.v1` keys exactly:

```text
schema, scientific_outcome, idempotency_key, predecessor_sha256,
acknowledged_effect_reply_sha256, ack_source
  ∈ {SUCCESSOR_OCCURRENCE, PROCESS_TERMINAL, DELIVERY_ACK}, acked_utc
```

`predecessor_sha256` is the SHA-256 of the immediately preceding phase
file's canonical bytes; `accepted.json`'s predecessor is
`pre_ledger_head_sha256`. Tuples — not single fields — carry the
multi-artifact effects of `CLOSE`, `PAUSE`, `RESUME`, and
`OPERATION_ADMIT` (Sol C1's "one event/artifact field cannot describe
the multi-artifact automata").

The cached `effect_reply` is transport-free. On any redelivery the
supervisor emits a **fresh** envelope carrying the current
`supervisor_generation_sha256` and the current `request_sha256`, with
`status`/`detail` byte-identical to the cached object. "Identical
reply" means identical effect-reply and release-token bytes, never an
impossible stale transport envelope (Sol C1.2).

### W1.4 Effect plans (deterministic locators bound at ACCEPTED)

`effect_plan` is written under `T_RUNTIME.lock` **after** capturing
every reading the effect needs and **before** any artifact exists, so
every locator is content-derived and probeable. Ledger event hashes are
computable at accept time because `pre_ledger_head_sha256` pins the
chain. Keys exactly, per command:

| Command | `effect_plan` keys exactly |
|---|---|
| `CLAIM` | `process_sequence, process_id, spawn_intent_id, complete_argv_sha256, claim_path` |
| `START` | `process_id, claim_sha256, start_event_sha256, lease_path, lease_sha256, watchdog_table_seq` |
| `HEARTBEAT` | `process_id, pre_lease_sha256, cursor_reading_ns, charge_event_sha256, successor_lease_path, successor_lease_sha256, post_state_sha256` |
| `CLOSE` | `process_id, pre_lease_sha256, cursor_reading_ns, final_charge_event_sha256, process_record_path, process_record_sha256, stopped_event_sha256, archive_set ("close")` |
| `PAUSE` | `checkpoint_path, checkpoint_payload_sha256, pause_event_sha256, post_state_sha256, archive_set ("pause")` |
| `RESUME` | `verified_checkpoint_sha256, pending_checkpoint_path_or_null, target_phase ∈ {G1,G4}, first_event_sha256_or_null` |
| `OPERATION_ADMIT` | `operation_id, pre_operation_reading_ns, capacity_path, bound_path, admission_path, worker_spawn_intent_id, declared_stream_indexes` |
| `OPERATION_STATUS` (ack form only) | `operation_id, delivery_ack_path, acknowledged_release_token_sha256, acknowledged_effect_reply_sha256` |

A `REFUSED` outcome is a legitimate terminal effect with **empty**
event and artifact tuples; it is committed and cached exactly like a
positive effect, so a refusal is never re-evaluated against moved
state.

### W1.5 The eight-command recovery reducer (Sol C1.4)

Run under `T_RUNTIME.lock` at every generation start, after every
takeover, and before serving any frame whose key has an open plan.

```text
head_ok := current_ledger_head ∈ {pre_ledger_head_sha256}
                              ∪ {plan's declared event hashes}
if not head_ok                     → record-first invalidity naming the plan
if reply.json exists               → re-wrap effect_reply in a fresh envelope
elif committed.json exists         → write reply.json from the recorded
                                     identities; re-wrap; serve
else:                                # accepted.json only
    for each locator in effect_plan, in the pinned per-command order:
        probe it by its content-derived path/hash
    if no locator is present       → apply the whole effect from step 1
    elif all are present+verified  → write committed.json, then reply.json
    else                           → execute exactly the missing steps,
                                     in order, each idempotent by locator
                                     (no-replace create, or verified-existing)
```

Every step is keyed by a content-derived locator, so no step can run
twice and no scan by approximate time or arguments exists. Per-command
probes and the one legal next action:

| Command | Probe at `ACCEPTED` | Single next action |
|---|---|---|
| `CLAIM` | `CHILDREN/<spawn_intent_id>.json`; `/proc/*/cmdline` containing `spawn_intent_id`; `claim_path` | missing intent ⇒ write it; intent + live child, no claim ⇒ kill by marker (§W2.4), reap, then spawn afresh under the same intent; intent + dead child, no claim ⇒ spawn; claim present ⇒ verify and cache |
| `START` | `start_event_sha256` in the ledger; `lease_path`; watchdog ack of `watchdog_table_seq` | append the missing event; install the missing lease; publish+await the missing ack; `SIGCONT` only after all three (§W3.2) |
| `HEARTBEAT` | `charge_event_sha256` in the ledger; `successor_lease_path` | event absent ⇒ append it with the **recorded** `cursor_reading_ns` (never a fresh reading); event present, lease absent ⇒ install the recorded successor lease; both present ⇒ cache |
| `CLOSE` | `final_charge_event_sha256`; `process_record_path`; `stopped_event_sha256`; lease absence; archival commit | resume at the first missing step in the signed §2c.6 order; archival is the last step; cache only after post-verify of the record |
| `PAUSE` | `checkpoint_path`; `pause_event_sha256`; head/cache equality; archival | resume at the first missing signed §6a condition; a condition that cannot now be met ⇒ the signed pause-failure route, cached as that refusal |
| `RESUME` | `pending_checkpoint_path_or_null`; `first_event_sha256_or_null` | resume the signed §6b / v2.1 §C.1–C.2 automaton at the first missing artifact; never select a different checkpoint |
| `OPERATION_ADMIT` | `capacity_path`; `bound_path`; `admission_path`; worker spawn intent + `/proc` marker | create exactly the missing artifacts in the §W4.4 order with the **recorded** `pre_operation_reading_ns` and `operation_id`; a live unbound worker is killed and respawned under the same intent; never a second cursor, capacity record, or `operation_id` |
| `OPERATION_STATUS` (ack) | `delivery_ack_path` | write the missing ack; then `ALREADY_DELIVERED` |

`OPERATION_STATUS` in its **observation** form (`ack_delivery = false`)
has no plan, no journal entry, and no effect: its reply is a
deterministic function of durable state, recomputed on every request.
Unbounded polling therefore grows nothing (Sol C2).

### W1.6 Two distinct acknowledgements (Sol C2)

**Ordinary effect-reply acknowledgement — implicit, mechanical, no
command.** `ack.json` with `ack_source = SUCCESSOR_OCCURRENCE` is
written when a request in the same `intent_scope_sha256` with
`occurrence_index = n+1` is admitted, or with
`ack_source = PROCESS_TERMINAL` when the owning process's final process
record becomes durable (closing every scope bound to that
`process_id`). The optional envelope field
`acked_effect_reply_sha256_or_null` lets a client acknowledge
explicitly; a mismatch against the cached `effect_reply_sha256` is
`INVALID`/`REPLAY_BYTES` with no state movement.

**Release-token delivery acknowledgement — explicit, one artifact.**
`OPERATION_STATUS` carries `ack_delivery` and has **exactly two** legal
argument key sets:

| `ack_delivery` | `arguments` keys exactly |
|---|---|
| `false` | `operation_id, ack_delivery` |
| `true` | `operation_id, ack_delivery, acknowledged_release_token_sha256, acknowledged_effect_reply_sha256` |

The `true` form is admitted **only** after the token was actually
emitted, and only when both supplied hashes equal the supervisor's own
recorded values — proof that the client observed and validated the
bytes. It then writes, no-replace under the lock,
`operations/<operation_id>/DELIVERY_ACK.json`, schema
`philosophia.officina.t-delivery-ack.v1`, keys exactly:

```text
schema, scientific_outcome, operation_id, delivery_intent_scope_sha256,
delivery_occurrence_index, acknowledged_release_token_sha256,
acknowledged_effect_reply_sha256, redeemed_utc
```

The ack is durable **before** any `ALREADY_DELIVERED` is returned.
Token bytes redeliver identically on every observation until that file
exists; afterwards every observation returns
`OK` / `{operation_id, phase: "ALREADY_DELIVERED"}`. The supervisor
never writes the ack before emitting the token, so a lost reply can
never be mistaken for observed delivery. The two supplied hashes are
compared for **identity only**; no journal state or refusal is ever
selected from output bytes.

### W1.7 Tombstones and bounded GC (Sol C2)

Permanent, compact replay proof, one file per **scope** (not per key):

```text
runtime_control/T_SUPERVISOR/JOURNAL/TOMBSTONES/<intent_scope_sha256>.json
```

`philosophia.officina.t-request-tombstone.v1`, keys exactly:

```text
schema, scientific_outcome, intent_scope_sha256,
acknowledged_high_water_occurrence (int ≥ 0),
last_effect_reply_sha256, updated_utc
```

This is the **one** control-plane object written by atomic replace
rather than no-replace; `acknowledged_high_water_occurrence` is
strictly monotone non-decreasing and a replace that would lower it is
record-first invalidity.

Disposition of an incoming key, exactly:

| Condition | Result |
|---|---|
| journal directory present, equal semantic hash | reducer (§W1.5) |
| journal directory present, different semantic hash | `INVALID`/`REPLAY_BYTES`, no effect |
| journal directory absent, `occurrence_index ≤ high_water`, equal recorded `last_effect_reply_sha256` scope | `REFUSED`/`ALREADY_ACKNOWLEDGED`, `retryable = false`, no effect |
| journal directory absent, `occurrence_index ≤ high_water`, mismatching derivation | `INVALID`/`REPLAY_BYTES`, no effect |
| journal directory absent, `occurrence_index > high_water` | new plan |

GC may delete `accepted/committed/reply/ack` for a key **only** when
all three hold: the owning transition's archival commit exists;
`ack.json` is durable; the scope tombstone's high water ≥ that
occurrence. No TTL, no size pressure, no outcome-derived deletion. The
tombstone is never deleted, so key reuse can never re-apply an effect.

**Growth bound.** Tombstone count = number of distinct intent scopes.
`HEARTBEAT` has exactly **one** scope per process (its only argument is
`process_id`), so an entire process's heartbeat history is one file
holding one integer. `CLAIM`/`START`/`CLOSE`/`PAUSE`/`RESUME`
contribute at most a fixed handful per process; processes are bounded
by E1; `OPERATION_ADMIT` scopes are bounded by the signed 32 GiB output
envelope (≤ 128 maximum-size operations, ≤ 1 333 checkpoint-sized
ones). The control plane therefore cannot grow without bound, and its
growth is not a function of polling.

---

## W2. Spawn, singleton, entry surface, and takeover

### W2.1 Entry surface: in-process post-fork function entry (X-M1)

The argv tokens `--supervisor-serve` and `--watchdog-serve` are
**deleted**. There is no private argv entry surface to guard.

- **Supervisor:** the CLI calls `os.fork()`; the middle child calls
  `os.setsid()` and forks again; the grandchild **calls the serve
  function in-process** (no `exec`, no new argv). The middle child
  `os._exit(0)`s and is reaped by the CLI.
- **Watchdog:** the supervisor calls `os.fork()`; the child calls the
  watchdog function in-process. It is forked at endpoint creation,
  **before any `RealTCapability` exists**, so the inherited address
  space contains no capability. It additionally verifies
  `getppid()` and the parent's start identity against
  `SUPERVISOR_IDENTITY.json`, and that both sealed FDs are pipes.
- **Controller and worker:** the only `exec`ing children
  (`subprocess.Popen(..., start_new_session=True, shell=False)`),
  because only a controller's argv prefix is client-supplied.

`os.fork` is inside the already-allowlisted `os`; the allowlist delta
remains **none**. `getppid()` is **not** used for the supervisor
grandchild (after the double fork its parent is `1`); its identity is
established by §W2.2 instead.

### W2.2 Singleton lock retained through identity installation (X-M6, Sol C5)

Under `flock(LOCK_EX)` on `SPAWN.lock`, **before** the first fork, the
CLI writes `T_SUPERVISOR/SPAWNING.json` (atomic no-replace), schema
`philosophia.officina.t-supervisor-spawning.v1`, keys exactly:

```text
schema, scientific_outcome, spawning_id, cli_pid, cli_start_identity,
boot_identity, created_utc
```

`spawning_id` = SHA-256 of the canonical record without that field.

The grandchild **scrubs every inherited descriptor except the
`SPAWN.lock` fd and its own sealed pipes**, redirects stdio to
`os.devnull`, creates endpoints, forks the watchdog, awaits the
watchdog's first ack, installs `SUPERVISOR_IDENTITY.json` (atomic
no-replace), and **only then closes its `SPAWN.lock` fd**. Because the
fd is a fork-shared open file description, the `flock` survives the
CLI's death; the lock releases only when **both** holders have closed
it. The fd is deliberately **not** `O_CLOEXEC` for the grandchild —
which is safe precisely because §W2.1 removed the grandchild's `exec`.

The CLI waits at most `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, polling at
`T_SUPERVISOR_POLL_INTERVAL_NS`, for a live-verified identity
(record present ∧ `os.kill(pid,0)` ∧ start identity match ∧ boot-id
match). On timeout it kills the grandchild by the `spawning_id` marker
(§W2.4), proves death, unlinks `SPAWNING.json`, releases the lock, and
returns `REFUSED`/`BOOTSTRAP`. **Identity-install collision:** the
loser of a `no-replace` race exits immediately without serving, writing
nothing, after unlinking nothing.

`SPAWNING.json` is unlinked by the supervisor as the first action after
its identity is live-verified, or by the next `SPAWN.lock` holder
during client takeover.

### W2.3 Spawn intent with a discoverable binding (X-C2, X-M10, Sol C5)

`CHILDREN/<spawn_intent_id>.json`, schema
`philosophia.officina.t-spawn-intent.v1`, keys **exactly**:

```text
schema, scientific_outcome, supervisor_generation_sha256,
spawn_intent_id, role (CONTROLLER|WORKER|WATCHDOG), process_sequence,
argv (nonempty list[str], the complete argv including the appended
      supervisor tokens), argv_sha256, created_utc
```

```text
spawn_intent_id = SHA-256(canonical {
  supervisor_generation_sha256, role, process_sequence,
  argv_sha256, created_utc })
```

`process_sequence` is the §V2.1.7 value derived from complete durable
history, so two identical-argv controllers in one clock tick cannot
collide. `created_utc` is canonical UTC with **exactly nanosecond
precision**, `YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ`.

### W2.4 Controller/worker exec convention and pre-claim discovery (X-C2, X-M1)

The supervisor appends **exactly four** tokens to the client-supplied
argv prefix, as its last four elements, in this order:

```text
--officina-spawn-intent <spawn_intent_id_hex>
--officina-ctrl-fds <req_write_fd>,<rep_read_fd>
```

`argv` and `argv_sha256` in the intent are over the **complete** argv.
The child learns its inherited FD numbers from `--officina-ctrl-fds`
(closing X-M1's undiscoverable credential) and carries its intent
marker in a place fixed at `exec` (closing X-C2). `pass_fds` carries
exactly those two descriptors; every other supervisor descriptor is
`O_CLOEXEC`. Workers receive the status pipe and the §W4.4 output pipe
by the same convention and **no** control pipe.

**Discovery predicate (both takeover phases and the §W1.5 reducer):**
for every `CHILDREN/<id>.json` without a resolved claim/binding, scan
`/proc/*/cmdline`, NUL-split, and select every process whose argv
contains that exact `spawn_intent_id_hex`. Kill each by
`killpg(SIGTERM)` then `killpg(SIGKILL)`; prove death by
`/proc/<pid>/stat` absence or state `Z`; `os.waitpid` only for
own-generation children. The token is unique per intent, so PID reuse
cannot mis-target, and a child that has not yet `exec`ed still will
(the `fork` already happened; `Popen` `_exit`s on exec failure). The
same predicate, with `spawning_id`, discovers a half-initialized
supervisor grandchild.

### W2.5 Bounded self-stop handshake (X-C2 second defect)

Controllers and workers use the identical handshake:

```text
Popen(complete_argv, start_new_session=True, shell=False,
      pass_fds=(...), close_fds=True)
loop at T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_SELF_STOP_TIMEOUT_NS:
    pid_, status = os.waitpid(pid, WNOHANG | WUNTRACED)
    if pid_ == pid and WIFSTOPPED(status): → read start identity,
                                             write the durable binding
    if pid_ == pid and (WIFEXITED or WIFSIGNALED): → BOOTSTRAP route
on timeout: → BOOTSTRAP route
BOOTSTRAP route: killpg(SIGKILL); prove death; reap own child;
                 resolve the spawn intent; reply REFUSED / BOOTSTRAP
                 (retryable = false); no claim, no lease, no capability
```

No unbounded `waitpid` occurs inside a `T_RUNTIME.lock` epoch, so a
client-supplied argv that never stops cannot wedge the runtime.

### W2.6 Capability invariant, not a first-instruction claim (X minors 1–2)

The reviewed controller adapter entry **installs no signal
dispositions** (the `signal` module is outside
`ALLOWED_ABSOLUTE_IMPORTS`; `SIGSTOP` disposition cannot be changed and
`SIGCONT`'s default is what is required) and calls
`os.kill(os.getpid(), SIGSTOP)` before any input read, thread, backend,
or controller logic.

The contract **does not claim** that CPython executes no interpreter,
`site`, or import-chain code before that call. The true and sufficient
invariant, stated as the normative one:

> No `RealTCapability` object exists, and no behavior authorization is
> issued, until after the durable claim, the durable lease, the durable
> watchdog-acked lease table, and `SIGCONT`.

"Behavior-capable" retains exactly the signed §A functional-boundary
meaning; nothing before `SIGCONT` can perform a signed behavior-capable
operation because no capability exists to perform it with.

### W2.7 One on-disk child layout (X-C6)

The rename of `CHILDREN/<spawn_intent_id>/` to
`CHILDREN/<process_id>/` is **mandatory**, atomic, and part of the
`CLAIM` effect plan. Pre-claim logs live at
`CHILDREN/<spawn_intent_id>/controller.stdout.log` and `.stderr.log`.
There is exactly one legal layout at rest and exactly one takeover
scan. `CHILDREN/*` objects are removed by the **supervisor**, under
`T_RUNTIME.lock`, after the owning process reaches a durable terminal
and its archival commit exists.

### W2.8 Process / FD / lock / topology table (replaces §V2.1.5)

| Process | Created by | Session | `T_RUNTIME.lock` | `SPAWN.lock` | Capability | Control endpoints | Inherited FDs | Exec? |
|---|---|---|---|---|---|---|---|---|
| CLI client | user shell | caller | never | held from before fork until identity live-verified | never | `REQUEST.fifo` + own reply FIFO | none of the supervisor's | — |
| Supervisor | CLI `fork`→`setsid`→`fork`, in-process entry | own | yes (epochs) | retained until identity installed, then closed | sole issuer | owns FIFO + every pipe | all scrubbed except `SPAWN.lock` and own pipes | **no** |
| Freezer watchdog | supervisor `fork`, in-process entry | own | **never** | never | **never** | sealed update/ack pipes only | those pipes only | **no** |
| Controller | supervisor `Popen` | own | never | never | never | inherited control pipes only, numbers from `--officina-ctrl-fds` | req-write, rep-read | yes |
| Worker | supervisor `Popen` | own | never | never | never | **none** | status-write, output-write | yes |

Every supervisor-created descriptor is `O_CLOEXEC` except the exact
`pass_fds` cleared for a child and the grandchild's `SPAWN.lock` fd
(§W2.2).

### W2.9 Two-phase takeover (X-C5)

**Phase 1 — client takeover, control plane only.** Under `SPAWN.lock`,
by the CLI, **before** any fork:

1. read-only load of `SPAWNING.json`, `SUPERVISOR_IDENTITY.json`,
   `CHILDREN/*`, claims, leases, journal, `WATCHDOG/*`, `CAPACITY/*`;
2. identity-kill every discoverable stale child and grandchild by the
   §W2.4 predicate; prove death;
3. unlink **only** stale control endpoints (`REQUEST.fifo`, `REPLY/*`,
   `SPAWNING.json`, `SUPERVISOR_IDENTITY.json`) — never durable
   `runtime/` evidence, never `JOURNAL/*`, `CAPACITY/*`, quarantined
   output, or `T_PROMOTED/**`;
4. fork.

The CLI **writes no `runtime/` evidence, appends no ledger entry,
performs no settlement, and holds no capability**, exactly as §V2.1.1
requires of clients.

**Phase 2 — supervisor takeover, runtime plane.** By the new
generation, as its first action after installing its identity and
receiving the watchdog's first ack, under `T_RUNTIME.lock`, before any
admission:

1. reconstruct the capacity ledger (§W4.6);
2. run the §W1.5 reducer over every open journal plan;
3. settle affected streams per signed §4c/§4d and honor unresolved
   batch records (§V2.8, unchanged);
4. resolve unresolved spawn intents;
5. only then serve.

Generation states become
`ABSENT → SPAWNING(lock held) → TAKEOVER(runtime, lock held) →
LIVE(watchdog acked) → TERMINAL_DRAIN`. There is no `IDLE_EXIT` (D1).

---

## W3. Watchdog C1: registration before behavior, honest freeze evidence

### W3.1 What is still not claimed

§V2.6.1 stands verbatim: no claim is made that an ordinary scheduled
userspace process physically executes at or before a monotonic deadline
under every host schedule, cgroup throttle, or runnable-queue delay.

### W3.2 Publication and acknowledgement precede behavior (Sol C4, X-M5)

`WATCHDOG/LEASES.json` (atomic replace, `table_seq` strictly
increasing) and the identical payload on the update pipe are published
**before** the first `SIGCONT`, before any capability becomes usable,
and before any operation admission. The supervisor must observe the
watchdog's ack of that exact `table_seq` first; otherwise it refuses
`START` and `OPERATION_ADMIT` with `REFUSED`/`WATCHDOG_UNACKED`.

**On renewal the old deadline remains authoritative until the successor
table is acked.** No unacknowledged update ever extends behavior.

Ack frame keys exactly:

```text
schema ("philosophia.officina.t-watchdog-ack.v1"), scientific_outcome,
supervisor_generation_sha256, table_seq, ack_monotonic_ns
```

**Liveness is judged on the watchdog's own sample**, never on the
supervisor's read time:

```text
healthy(table_seq) ⇔ ack_monotonic_ns − updated_monotonic_ns
                     ≤ T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS
dead ⇔ the supervisor has drained the ack pipe and
       now_ns − updated_monotonic_ns > T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
       with no ack for that table_seq
```

A supervisor busy inside a bounded chunk therefore cannot declare a
healthy watchdog dead. The serve loop is a `time`-paced nonblocking
poll at `T_SUPERVISOR_POLL_INTERVAL_NS` (`select`/`selectors` are
outside the allowlist), and **every** bounded long loop — the §W4.5
output copy, hashing, enumeration, and archival — services one watchdog
step and one control-frame step between chunks.

### W3.3 Freeze evidence: proved quiescence, watchdog-written (X-C4.4, Sol C4)

When the watchdog's clock shows `now_ns ≥ deadline_ns` for a lease row:

1. verify `/proc/<leader>/stat` start identity matches; on mismatch,
   skip (PID reuse → stream lost, §4c(c));
2. `killpg(pgid, SIGSTOP)`;
3. **prove quiescence**: enumerate the recorded group members and every
   `/proc` process whose session id or parent chain reaches a recorded
   member; require each to be absent or in state `T` or `Z`. Repeat at
   `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS` up to
   `T_WATCHDOG_QUIESCE_MAX_PASSES`, issuing `killpg(pgid, SIGKILL)`
   after the first failed pass;
4. **on the pass that proves every member stopped/dead**, sample
   `freeze_ns = clock_gettime_ns(CLOCK_MONOTONIC)` and set
   `quiescence = PROVED`;
5. if the passes are exhausted, or a reachable process is neither
   stopped, dead, nor absent, set `freeze_ns = null`,
   `quiescence = UNKNOWN`;
6. write `WATCHDOG/FREEZE/<process_id>.json` **itself**, atomic
   no-replace, file `fsync`, parent-directory `fsync`, then emit the
   event on the pipe.

`freeze_ns` is therefore the conservative monotonic observation at
which the whole declared tree is proved stopped/dead — never the
signal-send time. This is the one mechanical evidence path, and it is
consistent with C1: the watchdog still holds no lock, no capability, no
right to write anything under `runtime/`, and no right to append the
ledger. `WATCHDOG/**` is control plane and archival-excluded.

`philosophia.officina.t-freeze-observation.v1` keys exactly:

```text
schema, scientific_outcome, supervisor_generation_sha256, process_id,
pgid, start_identity, deadline_ns, freeze_ns_or_null,
quiescence ∈ {PROVED, UNKNOWN}, overrun_ns_or_null,
killer ∈ {WATCHDOG, SUPERVISOR}, unresolved_member_count (int),
table_seq, created_utc
```

**A lost observation is never reconstructed.** If the file is absent
and the watchdog is dead or the event was lost, the supervisor writes
its own observation with `freeze_ns = null`,
`quiescence = UNKNOWN`, `killer = SUPERVISOR`. v2's "re-derives by
sampling stopped/dead group vs durable deadline" is **deleted**: a
later sample cannot recover an earlier instant, and calling it
re-derived was false.

### W3.4 One route for every freeze (X-C4.1–3, Sol C4)

```text
quiescence = PROVED  ⇒ overrun_ns = freeze_ns − deadline_ns  (> 0 by construction)
                     ⇒ signed record-first live-process invalidity (§2c.12),
                       all-live batch (§2c.12b / §4d), public cause PROCESS
quiescence = UNKNOWN ⇒ the same invalid route with the §4c(c)/§4d
                       unknowable pool; no timestamp is synthesized
```

- The **zero-overrun branch is deleted.** Quiescence is proved strictly
  after the deadline is observed, so `overrun_ns > 0` always. No
  tolerance constant exists and none may be introduced.
- **Forbidden dispositions on a watchdog freeze:** `T_PROCESS_CLOSED`,
  `T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_E1_EXHAUSTED`,
  `T_PROCESS_E3_DUE`, and — named explicitly, closing X-C4.1 —
  **`T_PROCESS_RESOURCE_STOP`**, which is unreachable anyway because
  signed §2c.7 requires the cooperative quiesce→charge→record order
  that a non-heartbeating controller cannot supply. No valid close,
  exhaustion, pause, or review terminal may arise from an overrun.
- **Cause is single-valued:** a positive confirmed watchdog overrun has
  public cause `PROCESS`. `CLOCK` applies only when a monotonic
  fault/non-monotonicity is independently verified, in which case the
  signed §2a precedence `HASH > FILESYSTEM > CLOCK > PROCESS >
  RESOURCE` resolves the co-observed pair. This is a mechanical mapping
  onto already-signed destinations, not a new cause and not an author
  cell.
- E1 charging follows signed §4c in full: the actual interval is
  retained, never clipped; numeric E1/E3 facts are retained in the
  invalid post-state per v2.1 §B.4. No automatic retry, scheduling
  tweak, or device switch is authorized. Platform scheduling
  variability is transparent process validity, never a tunable.

### W3.5 Watchdog state / failure table (replaces §V2.6.6)

| Event | Detection | Single continuation |
|---|---|---|
| Healthy update | ack with matching `table_seq` within `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS` of `updated_monotonic_ns` | new deadlines authoritative |
| Renewal not yet acked | no matching ack | **old deadline remains authoritative**; behavior continues under it; `START`/`ADMIT` refused `WATCHDOG_UNACKED` |
| Ack absent past `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` | pipe drained, no ack | watchdog declared dead: supervisor freezes all live groups itself per §W3.3 with `killer = SUPERVISOR`, refuses admissions, forks a new watchdog, awaits its ack, then settles every overdue lease per §W3.4 |
| Watchdog exits / identity mismatch | `waitpid` on own child, or parent-check failure | as above |
| Stale or wrong-generation update | `table_seq` ≤ last, or generation mismatch | watchdog ignores it; the supervisor treats a missing ack for the current `table_seq` by the absence rule |
| Watchdog fork failure | `os.fork` error | no serve; every command refused `WATCHDOG_UNACKED` |
| Supervisor death | watchdog's `getppid()` ≠ recorded, or update pipe EOF | watchdog freezes all known groups per §W3.3, writes their observations, exits; it **settles nothing**; the next supervisor takeover (§W2.9 phase 2) settles |
| PID reuse on a controller | start-identity mismatch at step 1 | freeze skipped; stream lost → §4c(c)/batch |
| Freeze observation present at supervisor start | file exists | consumed under the lock, routed per §W3.4; the file is removed only after the settlement's archival commit |

---

## W4. K1 output capacity and the operation transaction

### W4.1 Enforcement architecture (signed K1)

A contract-following worker receives **no writable output pathname and
no writable output descriptor**. `operations/<operation_id>/out/` is
created and held by the supervisor alone. Bytes are stopped in the data
path, not counted after exit. A plain integer ledger and a bare
`statvfs` check are **accounting**, never enforcement.

### W4.2 The envelope (signed constants, unchanged)

```text
per-operation ceiling = T_OUTPUT_PER_STREAM_MAX_BYTES
                        × len(declared_stream_indexes)      ≤ 268_435_456
aggregate ceiling     = T_OUTPUT_AGGREGATE_MAX_BYTES        = 34_359_738_368
filesystem margin     = T_OUTPUT_FS_SAFETY_MARGIN_BYTES     = 8_589_934_592
copy/hash chunk       = T_OUTPUT_COPY_CHUNK_BYTES           = 4_194_304
```

Only the per-operation ceiling scales, and with the declared stream
subset — not with `device_units`, `E1`, or concurrency. Maximum
simultaneous live reservation is `4 × 268_435_456 = 1_073_741_824`
bytes; maximum chunks in one operation's copy loop is `64`.

**Serve preflight** (fail-closed, before any frame is served, any
claim, capability, lease, or worker):

```text
require os.pipe2 available and fpathconf(fd, PC_PIPE_BUF) ≥ 4096
require st_dev(operations root) == st_dev(runtime/T_PROMOTED root)
require out/ creatable and writable by the supervisor
reconstruct accounted_total (§W4.6)
require free_bytes ≥ (AGGREGATE − accounted_retained) + FS_MARGIN
```

Failure ⇒ **no supervisor serves**; every command is refused.

### W4.3 `OPERATION_ADMIT` is the sole bound installer (X-C3.1–3, Sol C3.1)

`arguments` keys **exactly**:

```text
process_id, operation_kind ∈ {ORACLE_QUERY, LEARNER_UPDATE, CHECKPOINT_WRITE},
input_spec (keys exactly: input_sha256),
declared_stream_indexes (sorted unique nonempty ints in 1..device_units),
max_total_output_bytes (positive int)
```

`output_bound_sha256` is **removed** from the arguments and from the
`operation_id` preimage, deleting the circularity. There is **no ninth
command** and **no `<pending_op_key>`**: every artifact lives under
`operations/<operation_id>/`, whose id is derived inside the accepted
plan before any artifact exists.

```text
operation_id = SHA-256(canonical {
  activation_record_sha256, process_id, active_lease_sha256,
  operation_kind, input_spec, declared_stream_indexes,
  max_total_output_bytes, pre_operation_reading_ns })
```

Admission refuse/reserve predicate, under `T_RUNTIME.lock`, before any
artifact:

```text
admit iff type(max_total_output_bytes) is int and > 0
     and max_total_output_bytes ≤ T_OUTPUT_PER_STREAM_MAX_BYTES
                                  × len(declared_stream_indexes)
     and accounted_total + max_total_output_bytes ≤ T_OUTPUT_AGGREGATE_MAX_BYTES
     and free_bytes ≥ max_total_output_bytes + T_OUTPUT_FS_SAFETY_MARGIN_BYTES
     and the declared stream subset is free (§V2.7.5, unchanged)
     and the watchdog has acked the current table_seq
else REFUSED / NO_CAPACITY (retryable = false)
```

### W4.4 One crash-reducible admission plan

Under `T_RUNTIME.lock`, in exactly this order, every step keyed by a
locator recorded in `accepted.json` (§W1.4):

```text
1. capture pre_operation_reading_ns; derive operation_id;
   write JOURNAL/<key>/accepted.json                       (no-replace)
2. CAPACITY/<operation_id>.json                            (no-replace)
3. operations/<operation_id>/BOUND.json                    (no-replace)
4. operations/<operation_id>/OPERATION.json                (no-replace)
5. CHILDREN/<worker_spawn_intent_id>.json                  (no-replace)
6. create out/ (supervisor-owned), the status pipe, and the output pipe;
   Popen the worker; bounded self-stop handshake (§W2.5); durable
   worker binding
7. JOURNAL/<key>/committed.json
8. JOURNAL/<key>/reply.json  →  OK / {operation_id, phase: "ADMITTED",
                                      bound_sha256}
9. SIGCONT the worker
```

`t-operation-output-bound.v1` keys exactly:

```text
schema, scientific_outcome, process_id, active_lease_sha256,
operation_kind, input_sha256, declared_stream_indexes,
max_total_output_bytes, operation_id, created_utc
```

`philosophia.officina.t-operation-admission.v1` (`OPERATION.json`) keys
exactly:

```text
schema, scientific_outcome, supervisor_generation_sha256, operation_id,
idempotency_key, semantic_request_sha256, process_id,
active_lease_sha256, operation_kind, input_sha256,
declared_stream_indexes, max_total_output_bytes, bytes_reserved,
pre_operation_reading_ns, bound_sha256, worker_spawn_intent_id,
created_utc
```

`bytes_reserved` is present (Sol M2) and equals
`max_total_output_bytes`. The admission binds the idempotency key and
the semantic request hash needed by the §W1.5 reducer (Sol M2).

### W4.5 The K1 framed transport and its exact parser

The worker's only output channel is an inherited `os.pipe2(O_CLOEXEC)`
write end, learned from `--officina-ctrl-fds`. Wire format, repeated
until EOF:

```text
<one canonical ASCII JSON line, ≤ 4096 bytes, terminated by "\n">
<exactly content_bytes raw bytes>
```

`philosophia.officina.t-worker-output-frame.v1` keys exactly:

```text
schema, scientific_outcome, operation_id, relative_path, content_bytes
```

Supervisor read loop: read end set `O_NONBLOCK`; at most
`T_OUTPUT_COPY_CHUNK_BYTES` consumed per pass; one watchdog step and
one control-frame step serviced between passes; header buffer bounded
by `T_CONTROL_READ_BUFFER_MAX_BYTES`.

Header validation happens **before anything is created**: relative,
non-empty, no `.`/`..`, no absolute prefix, no NUL, unique within the
operation, depth ≤ 2, component ≤ `T_OUTPUT_PATH_COMPONENT_MAX_BYTES`,
full path ≤ `T_OUTPUT_PATH_MAX_BYTES`, file count ≤
`16 × device_units`, `type(content_bytes) is int`, `> 0`, and
`bytes_written + content_bytes ≤ bytes_reserved`.

The supervisor then opens the file itself —
`os.open(relative_path, O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,
dir_fd=out_dirfd)` — copies in chunks, and **updates one streaming
SHA-256 per file in the same pass**. Each byte is read exactly once;
there is no second pass and no post-exit hash pass.

Parser cuts, each single-valued:

| Cut | Continuation |
|---|---|
| header line exceeds `T_CONTROL_FRAME_MAX_BYTES` without `\n`, or buffer overflow | close read end; `killpg`; prove death; quarantine terminal (§W4.7) |
| malformed JSON, unknown/missing key, wrong `operation_id`, bad path grammar, duplicate path, count exceeded | same |
| `content_bytes` non-int, `bool`, ≤ 0, or would exceed the reservation | same, and **no byte of that frame is written** |
| a chunk would cross `bytes_reserved` | write nothing further; close the read end (the worker's next `write` takes `EPIPE`/`SIGPIPE`); `killpg`; prove death; quarantine terminal |
| EOF mid-header or mid-content | partial output ⇒ quarantine terminal; the written prefix is accounted at bytes actually written |
| EOF exactly at a frame boundary **and** worker status `exit_reason = COMPLETED` **and** group proved dead | proceed to §W6.1 settlement |
| EOF at a frame boundary with `exit_reason = FAILED` | quarantine terminal |
| pipe full | the worker blocks in `write`; this is ordinary backpressure and is covered by the C1 deadline |
| `ENOSPC` on a supervisor write | §W4.7 `FILESYSTEM` route |

The supervisor never writes to the output pipe, so no `SIGPIPE` can
reach it from this transport.

```text
result_sha256 = SHA-256(canonical [
  {relative_path, content_sha256, byte_length} …
] sorted by relative_path)
```

Sparse files cannot arise, because the supervisor writes sequentially
and never seeks. Worker-reported paths are never trusted for anything
but the grammar check the supervisor itself performs.

### W4.6 Capacity accounting, records, and crash reconstruction (Sol C3.2–3.3)

```text
accounted_total =  Σ bytes_reserved  over ADMITTED / RUNNING / PENDING_SETTLEMENT
                 + Σ actual_bytes    over QUARANTINED
                 + Σ actual_bytes    over PROMOTED retained under runtime/T_PROMOTED/**
                 − Σ released_bytes  over operations with a durable disposition
```

All under `runtime_control/T_SUPERVISOR/CAPACITY/`, no-replace, written
only by the supervisor under `T_RUNTIME.lock`, `scientific_outcome:
false`, recursive scientific-field rejection, `type(x) is int`:

| Artifact | Schema | Keys exactly | Effect |
|---|---|---|---|
| `<operation_id>.json` | `philosophia.officina.t-operation-capacity.v1` | `schema, scientific_outcome, supervisor_generation_sha256, operation_id, process_id, active_lease_sha256, declared_stream_indexes, bytes_reserved, created_utc` | **adds** `bytes_reserved` |
| `<operation_id>.settled.json` | `philosophia.officina.t-operation-capacity-settled.v1` | `schema, scientific_outcome, operation_id, terminal ∈ {PROMOTED, QUARANTINED}, actual_bytes, custody_root, settled_utc` | **re-measures the same custody**: contribution becomes `actual_bytes`; releases only the over-declaration `bytes_reserved − actual_bytes` |
| `<operation_id>.disposed.json` | `philosophia.officina.t-capacity-disposition.v1` | `schema, scientific_outcome, operation_id, author_disposition_sha256, released_bytes, custody_absent (true), disposed_utc` | **the one artifact that releases retained capacity** |

`SETTLEMENT.json`, the `FAILED`/quarantine record, the promotion
`os.replace`, and any rename **release nothing**. Promotion changes the
recorded `custody_root` and nothing else.

**Crash reconstruction**, under the lock, before the first admission:

1. read every `CAPACITY/*`; per operation take `disposed → 0`, else
   `settled → actual_bytes`, else `admitted → bytes_reserved`;
2. enumerate `runtime/T_PROMOTED/**` and the quarantine root with
   directory-fd + `O_NOFOLLOW`, summing
   `max(st_size, st_blocks × 512)` per operation;
3. per operation use `max(recorded, enumerated)` — never the smaller;
4. an operation directory with **no** capacity record counts as the
   full `268_435_456` until a settled or disposition record exists;
5. any accounted path that cannot be read or enumerated ⇒ refuse every
   admission with `NO_CAPACITY`; never assume zero.

A partially written tree is never re-measured downward while its
operation is non-terminal.

**Retention and disposal.** Outputs are retained for the whole of T.
There is no TTL, no class-based deletion, no size-pressure eviction.
Disposal requires a signed author disposition artifact naming operation
ids, kinds, terminals, byte counts, and destination; it may not cite
result bytes, result hashes, learner state, candidate identity, or any
judgement that an output looks promising, failed usefully, or helps a
desired candidate. Raising `T_OUTPUT_AGGREGATE_MAX_BYTES` requires a
new signed author capacity amendment, is forbidden while any operation
is live or any invalidity is unresolved, and may never be enacted in
response to a `NO_CAPACITY` refusal or an `ENOSPC`. The supervisor can
never raise it.

### W4.7 Quarantine, `FAILED`, and the signed invalidity route (Sol C3.4)

`operations/<operation_id>/QUARANTINE.json`, schema
`philosophia.officina.t-operation-quarantine.v1`, atomic no-replace,
under the lock, keys exactly:

```text
schema, scientific_outcome, supervisor_generation_sha256, operation_id,
process_id, failure_class ∈ {BOUND_EXCEEDED, GRAMMAR, TRANSPORT,
  WORKER_FAILED, PARTIAL_OUTPUT, FILESYSTEM, HASH, SUPERVISOR_CRASH},
bytes_accounted, custody_root, invalidity_event_sha256, created_utc
```

A control-plane `FAILED` label never replaces a signed terminal. Every
failure class maps to exactly one already-signed route:

| `failure_class` | Signed route |
|---|---|
| `BOUND_EXCEEDED`, `GRAMMAR`, `TRANSPORT`, `PARTIAL_OUTPUT`, `WORKER_FAILED` | record-first live-process invalidity (§2c.12), all-live batch (§2c.12b/§4d), public cause `PROCESS` |
| `FILESYSTEM` (`ENOSPC`, write error) | same, public cause `FILESYSTEM` |
| `HASH` (descriptor revalidation mismatch, §W6.2) | same, public cause `HASH` |
| `SUPERVISOR_CRASH` (copy interrupted) | same, public cause `PROCESS`; accounted at `bytes_reserved` until a disposition |

`invalidity_event_sha256` is written only after the signed invalid
terminal set is durable. **No live process silently resumes after an
invalid operation**; G5 and the record-first ordering apply unchanged;
no valid exhaustion, stop, pause, or review event is appended while any
invalidity is unresolved (v2.1 §B.4).

`ENOSPC`, `EDQUOT`, `EFBIG`, and quota exhaustion all take the
`FILESYSTEM` route: stop writing, kill the group, prove death, record
the conservative reservation, and refuse all further admission until a
signed disposition exists. **Nothing is ever deleted to make room.**

### W4.8 Operation states and capacity/custody transitions

Operation states (replaces §V2.9.3):

```text
ADMITTED → RUNNING → PENDING_SETTLEMENT → PROMOTED | QUARANTINED
PROMOTED → ALREADY_DELIVERED           (after the durable delivery ack)
```

| Transition | Durable trigger | Accounted contribution | Releases? |
|---|---|---|---|
| — → `ADMITTED` | `CAPACITY/<op>.json` | `bytes_reserved` | no |
| `ADMITTED` → `RUNNING` | worker `SIGCONT` | `bytes_reserved` | no |
| `RUNNING` → `PENDING_SETTLEMENT` | worker+group proved dead, transport closed | `bytes_reserved` | no |
| `PENDING_SETTLEMENT` → `PROMOTED` | `SETTLEMENT.json` then `<op>.settled.json` (`PROMOTED`) | `actual_bytes` | only the over-declaration |
| any → `QUARANTINED` | `QUARANTINE.json` then `<op>.settled.json` (`QUARANTINED`) | `actual_bytes` | only the over-declaration |
| `out/` → `T_PROMOTED/<op>/` rename | `os.replace` | unchanged | **no** |
| `PROMOTED` → `ALREADY_DELIVERED` | `DELIVERY_ACK.json` | `actual_bytes` | no |
| any retained → released | `<op>.disposed.json` with `custody_absent: true` | `0` | **yes — the only release** |

---

## W5. Observation, transport, roles, and closed schemas

### W5.1 One fixed pre-terminal shape (Sol M1)

Every pre-terminal `OPERATION_STATUS` observation returns exactly:

```text
status = OK, detail keys exactly {operation_id, phase: "PENDING"}
```

`ADMITTED`, `RUNNING`, and `PENDING_SETTLEMENT` remain internal
operation states and **never** appear in a reply. The reply's
construction and its transport path do not branch on worker output,
path count, byte count, exit reason, or internal phase, so the
transition time between internal phases reveals nothing. `PROMOTED`
becomes visible only after `SETTLEMENT.json` is durable;
`QUARANTINED` is reported as `FAILED` only after the complete signed
invalid terminal set is durable.

### W5.2 Reply matrix and closed enums (replaces §V2.4.5)

| status | context | `detail` keys exactly |
|---|---|---|
| `REFUSED` | any | `token`, `retryable` (bool) |
| `INVALID` | any | `token` |
| `OK` | `CLAIM` | `process_id, process_claim_sha256, process_sequence` |
| `OK` | `START` | `process_id, lease_sha256, started (true)` |
| `OK` | `HEARTBEAT` | `process_id, charge_event_sha256, cumulative_charge_ns` |
| `OK` | `CLOSE` | `process_id, process_record_sha256, stopped_event_sha256` |
| `OK` | `PAUSE` | `pause_event_sha256, checkpoint_sha256` |
| `OK` | `RESUME` | `phase ∈ {G1,G4}, ledger_head_sha256` |
| `OK` | `OPERATION_ADMIT` | `operation_id, phase ("ADMITTED"), bound_sha256` |
| `OK` | `OPERATION_STATUS` | `operation_id, phase ∈ {PENDING, PROMOTED, FAILED, ALREADY_DELIVERED}`; **iff** `PROMOTED`: `release_token` (keys exactly `activation_record_sha256, process_id, lease_sha256, operation_id, result_sha256, charge_event_sha256`) and `settlement_sha256` |

`promoted_relative_paths` is **removed** from every reply (X-M2);
`SETTLEMENT.json` and `result_sha256` carry the path set. The largest
legal reply is therefore a fixed six-hex-field token plus two hashes,
well under `T_CONTROL_FRAME_MAX_BYTES`.

Closed refusal tokens:

```text
STALE_GENERATION, UNRESOLVED_BATCH, UNRESOLVED_JOURNAL, G5_BLOCKED,
E3_DUE, NO_CAPACITY, NOT_LIVE, DEADLINE_FREEZE, BUSY, NOT_FOUND,
BOOTSTRAP, ALREADY_ACKNOWLEDGED, WATCHDOG_UNACKED
```

Closed `INVALID` tokens:

```text
ROLE, SCHEMA, IDENTITY, REPLAY_BYTES, GENERATION, BOUND,
FRAME_LENGTH, INTENT_KEY
```

`ALREADY_DELIVERED` appears in both the reply phase enum and §W4.8's
operation states (X-M11). No free text; no result hash before
`PROMOTED`; no learner field anywhere.

### W5.3 Endpoint roles including descendants (Sol M1, X-M4)

| Command set | Authorized endpoint | Peer proof |
|---|---|---|
| `CLAIM` `START` `HEARTBEAT` `CLOSE` `PAUSE` `RESUME` | `REQUEST.fifo` only | client PID + start identity live, **and** the PID is neither a registered controller/worker/watchdog **nor a member or descendant of any registered group** — proved by a `/proc` walk over recorded members plus every process whose session id or parent chain reaches a recorded member |
| `OPERATION_ADMIT` `OPERATION_STATUS` | per-controller inherited pipe only | the pipe **is** the credential; the peer must be the claimed controller identity for that pipe |
| (none) | workers | any control frame from a worker identity → `INVALID`/`ROLE` |

**Truthfulness qualifier (X minor 6).** The `REQUEST.fifo` check
defeats a controller or descendant that reports its own identity. A
deliberate same-UID process that reports a live unrelated PID it read
from `/proc`, or that escapes into a new untracked session, is inside
the signed A3 **procedural** residual and is not mechanically excluded.
This is stated rather than claimed away.

### W5.4 Framing, buffering, reply path, dead reader (X-M3, Sol M2)

- One frame = one canonical ASCII JSON line terminated by `\n`.
- The reader keeps one buffer per endpoint, bounded by
  `T_CONTROL_READ_BUFFER_MAX_BYTES`; it splits on `\n`; any line
  exceeding `T_CONTROL_FRAME_MAX_BYTES`, or a buffer that fills without
  a `\n`, is `INVALID`/`FRAME_LENGTH` and the buffer is reset to the
  byte after the next `\n`.
- One `write` per complete frame ≤ `T_CONTROL_FRAME_MAX_BYTES`;
  `fpathconf(fd, PC_PIPE_BUF) ≥ 4096` verified at endpoint creation;
  partial write or `EAGAIN` ⇒ no action + closed retry via the journal.
- Supervisor keeps a keep-open `O_WRONLY|O_CLOEXEC` on `REQUEST.fifo`
  so readers see `EAGAIN`, not spurious EOF.
- **`reply_fifo` is pinned** to exactly
  `REPLY/<hex(client_start_identity)>.<idempotency_key>.fifo`
  (lowercase hex of the UTF-8 identity bytes). Any other value is
  `INVALID`/`SCHEMA`. One client can therefore never name another
  client's reply FIFO.
- `REPLY/` is created by the supervisor at endpoint creation, mode
  `0700`; each reply FIFO is created by the **client** before
  publishing its request, opened read-nonblocking first, and unlinked
  by the client on terminal; the supervisor unlinks orphaned reply
  FIFOs during client takeover only.
- **Dead reader:** `ENXIO` or `EPIPE` on the reply write ⇒ the reply is
  already cached in `JOURNAL/<key>/reply.json`; the supervisor performs
  **no re-apply, no retry, no state movement**, and the client's next
  retry receives the cached effect reply in a fresh envelope.
- `T_CLIENT_REPLY_TIMEOUT_SECONDS` continuation (X minor 3): the CLI
  exits with status `3`, leaves its intent slot **unfinished**, and the
  next invocation of the same command is a retry by §W1.1.
- Directory-fd, `O_NOFOLLOW`, type, and ownership checks precede every
  endpoint use.

### W5.5 Byte bounds (X-M2)

```text
client-supplied argv:  ≤ T_ARGV_MAX_ELEMENTS elements,
                       ≤ T_ARGV_MAX_BYTES total UTF-8 bytes
output relative path:  ≤ T_OUTPUT_PATH_MAX_BYTES,
                       component ≤ T_OUTPUT_PATH_COMPONENT_MAX_BYTES
any control frame:     ≤ T_CONTROL_FRAME_MAX_BYTES
```

A `CLAIM` whose argv exceeds either bound is `INVALID`/`SCHEMA`. No
legal reply can exceed the frame maximum, because §W5.2 removed the
only variable-length reply field.

---

## W6. Promotion, hashing, membership, and non-regression

### W6.1 Promotion order and the single commit

```text
admission plan durable (§W4.4) → worker SIGCONT
→ framed transport consumed, files written and hashed in ONE pass (§W4.5)
→ transport closed; worker exit observed; group quiescence proved (§W6.4)
→ held-descriptor revalidation (§W6.2)
→ settle under T_RUNTIME.lock (one §2c.5 charge for occupied streams)
→ SETTLEMENT.json (atomic no-replace)  = THE COMMIT POINT
→ CAPACITY/<op>.settled.json (PROMOTED, actual_bytes)
→ idempotent os.replace of out/ into runtime/T_PROMOTED/<operation_id>/
→ release token delivered on OPERATION_STATUS observation
```

`SETTLEMENT.json` keys exactly:

```text
schema, scientific_outcome, operation_id, charge_event_sha256,
result_sha256, promoted_relative_paths, bound_sha256, actual_bytes,
settled_utc
```

Only the charge event captured in the same settle step is written into
it, so a wrong, old, sibling, or caller-named charge cannot promote.

### W6.2 Hashing, held descriptors, TOCTOU (X-M7)

v2's "restartable from descriptor offset after crash without
re-spawning the worker" is **deleted**: descriptors die with the
process and streaming SHA-256 state is not serializable. Under K1 there
is no post-exit hash pass at all — hashing is inline with the single
copy — so a crash mid-copy yields the `SUPERVISOR_CRASH` quarantine
terminal at the conservative `bytes_reserved`, never a resumed offset
and never a respawned worker.

The supervisor holds each output file's `O_WRONLY` descriptor from
creation and, immediately before the settle step, re-verifies
`st_size`, `st_ino`, and `st_nlink` from the **held** descriptor
against what it wrote; any mismatch is the `HASH` quarantine class. A
deliberate same-UID modification of `out/` between write and settle is
detected by this check but is not *prevented*; that residual is A3
procedural and is named here rather than claimed closed.

### W6.3 Rename `errno` routes and preflight (X-M8)

- `st_dev(operations root) == st_dev(runtime/T_PROMOTED root)` is a
  serve preflight (§W4.2); a mismatch means **no serve**, so `EXDEV`
  cannot arise at promotion time and no cross-device copy fallback
  exists.
- `runtime/T_PROMOTED/` is created by the supervisor at first use, mode
  `0700`, parent-directory `fsync`.
- `ENOENT` on the source **and** destination present **and**
  `SETTLEMENT.json` durable ⇒ the rename already completed: do nothing;
  this is the idempotent-completion predicate.
- `ENOTEMPTY`/`EEXIST` on a non-empty destination without a durable
  `SETTLEMENT.json` ⇒ record-first invalidity naming both paths; never
  merge, never overwrite.
- Any other `errno` ⇒ `FILESYSTEM` quarantine class.

### W6.4 Group quiescence and escaped work (X-M4)

`killpg(pgid, …)` remains the action. Quiescence is **proved**, not
assumed: enumerate the recorded group members plus every `/proc`
process whose session id or parent chain reaches a recorded member;
each must be absent or in state `T`/`Z`; `os.waitpid` only for
own-generation children; `kill(0)` is never group-empty proof.
Anything found that cannot be classified ⇒ the signed §4c(c)/§4d
unknowable route.

**"Escaped children" moves out of §V2.2.1's mechanical list into the
A3 procedural residual.** No cgroup, PID namespace, or
`PR_SET_CHILD_SUBREAPER` is available (`signal`/`ctypes` are outside
`ALLOWED_ABSOLUTE_IMPORTS`), so a controller's own new-session child
leaves the frozen group; the fail-closed quiescence scan detects it and
routes to unknown recovery rather than pretending `killpg` covered it.

### W6.5 Explicit supersession of the signed predecessor sentence (X-M9i)

Signed harness §5a reads: "The watchdog owns the deadline and **executes
the v2.1 §1 sequence at or before it**." That sentence is **explicitly
superseded** by §W3.1/§W3.3/§W3.4: on non-real-time Linux the watchdog
owns the deadline and executes the sequence **as soon as it is
scheduled after the deadline**, records the conservative proved-freeze
instant, and every positive overrun is routed to the signed
invalid/recovery destinations with full §4c charging. The signed
sentence is not contradicted by silence; it is named, superseded, and
its guarantee replaced by a weaker, true, fail-closed one. Nothing else
in §5a moves.

### W6.6 Non-regression (unchanged surfaces)

Carried forward unchanged and not weakened: §V2.8 in full (boundary
batch wiring, event/artifact-backed terminals, `ARCHIVE` before
`RESOLVED`, raw statically-parsed ledger-suffix D1 completion, G5 since
last valid admission, one lock epoch for close, private claim-backed
`BatchSettlementAuthority`, strict `type(x) is int`, pre-review-head
acyclicity, caller-supplied current head on `charge_batch_settlement`,
the complete Codex §S6 items 1–13); §V2.7.5 stream ownership; A3's
T-development-only, Q/C-non-citable boundary; D1; E1/E2/E3 and their
constants; the nine signed events; every signed runtime schema; the
roots tuple; batch arithmetic; sole supervisor capability custody;
`MAX_CONCURRENT_LEASES = 4`; the zero import-allowlist delta and the
byte-frozen files of §V2.10 (`runtime.py`, `ledger.py`,
`checkpoint.py`, `verification.py`, `activation.py`).

`runtime_control/**` and `runtime/T_PROMOTED/**` are excluded from
every signed archival set **and remain untracked**, so the
activation-protocol clean-HEAD rule ("no source, configuration,
manifest, authorization, or other tracked path may be dirty or
staged") holds. This amendment authorizes no `.gitignore` or
configuration change (X minor 7).

---

## W7. Durable object, schema, path, owner, and retention table

Every `runtime_control/**` object uses the signed §3 durability
sequence: same-directory temp write → file `fsync` → atomic install →
parent-directory `fsync` (X minor 5). All are canonical ASCII JSON with
trailing newline, `scientific_outcome: false`, recursive
scientific-field rejection, `type(x) is int` (`bool` refused). All are
archival-excluded and untracked. **No object has an optional layout.**

| Object | Path (under `successor/officina/`) | Schema | Install | Writer / lock | Removed by |
|---|---|---|---|---|---|
| Spawning marker | `runtime_control/T_SUPERVISOR/SPAWNING.json` | `t-supervisor-spawning.v1` | no-replace | CLI under `SPAWN.lock` | supervisor after identity live-verified, or next `SPAWN.lock` holder |
| Supervisor identity | `…/SUPERVISOR_IDENTITY.json` | `t-supervisor-identity.v1` | no-replace | supervisor grandchild under `SPAWN.lock` | client takeover phase 1 |
| Spawn intent | `…/CHILDREN/<spawn_intent_id>.json` | `t-spawn-intent.v1` | no-replace | supervisor under `T_RUNTIME.lock` | supervisor after process terminal + archival |
| Child log dir | `…/CHILDREN/<spawn_intent_id>/` → `…/CHILDREN/<process_id>/` | (bytes) | mandatory atomic rename | supervisor | supervisor after process terminal + archival |
| Journal accepted | `…/JOURNAL/<key>/accepted.json` | `t-request-accepted.v1` | no-replace | supervisor under `T_RUNTIME.lock` | GC per §W1.7 |
| Journal committed | `…/JOURNAL/<key>/committed.json` | `t-request-committed.v1` | no-replace | supervisor under lock | GC per §W1.7 |
| Journal reply | `…/JOURNAL/<key>/reply.json` | `t-request-reply.v1` | no-replace | supervisor under lock | GC per §W1.7 |
| Journal ack | `…/JOURNAL/<key>/ack.json` | `t-request-effect-ack.v1` | no-replace | supervisor under lock | GC per §W1.7 |
| Scope tombstone | `…/JOURNAL/TOMBSTONES/<intent_scope_sha256>.json` | `t-request-tombstone.v1` | **atomic replace**, monotone | supervisor under lock | **never** |
| Client intent slot | `runtime_control/T_CLIENT_INTENTS/<scope>.<n>.json` | `t-client-intent.v1` | no-replace | the client, under `ALLOC.lock` | the client after its `.done.json` |
| Client intent terminal | `…/T_CLIENT_INTENTS/<scope>.<n>.done.json` | `t-client-intent-terminal.v1` | no-replace | the client | the client |
| Watchdog lease table | `…/WATCHDOG/LEASES.json` | `t-watchdog-lease-table.v1` | atomic replace | supervisor under lock | generation end |
| Watchdog ack frame | update/ack pipes (no file) | `t-watchdog-ack.v1` | — | watchdog | — |
| Freeze observation | `…/WATCHDOG/FREEZE/<process_id>.json` | `t-freeze-observation.v1` | no-replace | **watchdog** (or supervisor when the watchdog is dead) | supervisor after the settlement's archival commit |
| Capacity reservation | `…/CAPACITY/<operation_id>.json` | `t-operation-capacity.v1` | no-replace | supervisor under lock | never (superseded, not removed) |
| Capacity settled | `…/CAPACITY/<operation_id>.settled.json` | `t-operation-capacity-settled.v1` | no-replace | supervisor under lock | never |
| Capacity disposition | `…/CAPACITY/<operation_id>.disposed.json` | `t-capacity-disposition.v1` | no-replace | supervisor under lock, only under a signed author disposition | never |
| Output bound | `…/operations/<operation_id>/BOUND.json` | `t-operation-output-bound.v1` | no-replace | supervisor under lock | never |
| Admission | `…/operations/<operation_id>/OPERATION.json` | `t-operation-admission.v1` | no-replace | supervisor under lock | never |
| Settlement commit | `…/operations/<operation_id>/SETTLEMENT.json` | `t-operation-settlement.v1` | no-replace | supervisor under lock | never |
| Quarantine record | `…/operations/<operation_id>/QUARANTINE.json` | `t-operation-quarantine.v1` | no-replace | supervisor under lock | never |
| Delivery ack | `…/operations/<operation_id>/DELIVERY_ACK.json` | `t-delivery-ack.v1` | no-replace | supervisor under lock | never |
| Worker output frame | output pipe (no file) | `t-worker-output-frame.v1` | — | worker | — |
| Worker status | status pipe (no file) | `t-worker-status.v1` | — | worker | — |
| Promoted tree | `runtime/T_PROMOTED/<operation_id>/` | (bytes) | atomic `os.replace` | supervisor under lock | only a signed disposition |
| Request / reply frames | `…/REQUEST.fifo`, `…/REPLY/<…>.fifo` | `t-control-request.v1` / `t-control-reply.v1` | — | client / supervisor | client on terminal; supervisor at takeover |
| Semantic request | (computed, never stored alone) | `t-semantic-request.v1` | — | — | — |
| Intent scope / key | (computed, never stored alone) | `t-intent-scope.v1` / `t-intent-key.v1` | — | — | — |

`SUPERVISOR_IDENTITY.json` keys exactly (unchanged from §V2.3):
`schema, scientific_outcome, activation_record_sha256, supervisor_pid,
supervisor_start_identity, boot_identity, request_fifo, created_utc`;
`supervisor_generation_sha256` = SHA-256 of that file's canonical bytes.

---

## W8. Crash-cut matrix (replaces §V2.11)

| Cut | Single continuation |
|---|---|
| `SPAWNING.json` durable, CLI dies before fork | next `SPAWN.lock` holder finds no live grandchild by the `spawning_id` marker, unlinks the marker, spawns |
| Grandchild alive, identity not installed, CLI dies | `SPAWN.lock` **still held** by the grandchild's retained fd (§W2.2); a second CLI blocks on the lock; no second supervisor |
| Grandchild dies before identity install | CLI's bounded wait expires → `REFUSED`/`BOOTSTRAP`; lock released on CLI exit |
| Identity-install no-replace collision | loser exits without serving, writes nothing, unlinks nothing |
| Spawn intent durable, no child | reducer/takeover finds no `/proc` marker → resolve the intent and (for an open plan) spawn afresh; **one verb, not "delete/refuse"** |
| Child stopped, no claim | discovered by the argv `spawn_intent_id` marker; killed by group; death proved; intent resolved |
| Child never self-stops | bounded wait → `BOOTSTRAP` route (§W2.5) |
| Claim durable, no start | signed orphan-claim invalidity; registry retains the binding; no id or sequence reuse |
| `accepted.json` durable, effect incomplete | §W1.5 reducer completes exactly the missing steps by locator; never a second effect |
| `committed.json` durable, `reply.json` absent | write `reply.json` from the recorded identities, then serve |
| Reply lost on the wire | cached effect reply re-wrapped in a fresh envelope for the same key, across generations |
| Same key, changed semantics | `INVALID`/`REPLAY_BYTES`, no effect, **no G5** |
| Key ≤ tombstone high water | `REFUSED`/`ALREADY_ACKNOWLEDGED`, no effect |
| Lease installed, watchdog not acked | no `SIGCONT`; `START` refused `WATCHDOG_UNACKED`; the old deadline governs any existing lease |
| Freeze observation durable, settlement pending | supervisor consumes it under the lock → §W3.4 invalid route |
| Freeze evidence lost / watchdog dead | supervisor writes `freeze_ns = null`, `quiescence = UNKNOWN` → unknowable all-live invalid settlement; **no timestamp is synthesized** |
| Capacity record durable, bound absent | reducer creates `BOUND.json` with the recorded `operation_id` |
| Bound + admission durable, no worker | reducer spawns the worker under the recorded spawn intent; never a second cursor or `operation_id` |
| Transport frame would exceed the reservation | nothing further written; read end closed; group killed; `BOUND_EXCEEDED` quarantine |
| EOF mid-frame | `PARTIAL_OUTPUT` quarantine at bytes written |
| Supervisor crash mid-copy | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; no resumed offset; no respawned worker |
| `ENOSPC` on a supervisor write | `FILESYSTEM` quarantine + invalidity; admissions refused until a signed disposition; nothing deleted |
| Copy complete, `SETTLEMENT.json` absent | quarantine; charge stands per §4c; §6c for disposal; capacity retained |
| `SETTLEMENT.json` durable, rename incomplete | complete the rename idempotently; never re-charge; capacity unchanged |
| Rename complete, source `ENOENT`, settlement durable | already promoted: do nothing |
| Destination non-empty, no settlement | record-first invalidity naming both paths |
| Token emitted, no delivery ack | identical token redelivers on every observation |
| Delivery ack durable | `ALREADY_DELIVERED` on every further observation |
| Capacity ledger unreadable at start | every admission refused `NO_CAPACITY`; never assume zero |
| Watchdog dead mid-live | §W3.5 |
| Supervisor dead | §W2.9 two-phase takeover |
| Batch mid-automaton | signed prefix automaton + amendment D1 (§V2.8, unchanged) |

No cut exposes promoted results without `SETTLEMENT.json`. No cut
double-charges a cursor. No cut releases retained capacity without a
signed disposition.

---

## W9. Finding disposition (both formal reviews, complete)

| Finding | Verdict | v2.1 locus |
|---|---|---|
| X-C1 inverted B1 / `REPLAY_BYTES` on every retry / client-triggerable G5 | closed | §W1.1–§W1.3, §W1.7 |
| X-C2 spawn intent carries no child identity; unbounded `waitpid`; no `¬WIFSTOPPED` route | closed | §W2.3–§W2.5 |
| X-C3 bound unreachable; who supplies the value; undefined pending key; reservation reserves nothing | closed | §W4.3–§W4.6 |
| X-C4 overrun disposition/cause/zero-branch/freeze-time | closed | §W3.3–§W3.4 |
| X-C5 dual-valued takeover authority | closed | §W2.9 |
| X-C6 self-contradictory durable-object rules; four undefined schemas; optional layout; missing actors | closed | §W1.3, §W4.4, §W4.7, §W2.7, §W7 |
| X-M1 private entry surface; parentage impossible; fd discovery | closed | §W2.1, §W2.4 |
| X-M2 legal frames exceed the maximum | closed | §W5.2, §W5.5 |
| X-M3 framing, buffering, `reply_fifo` | closed | §W5.4 |
| X-M4 escaped children claimed mechanical | closed (re-scoped, not claimed away) | §W6.4, §W5.3 |
| X-M5 ack freshness measured on the wrong side; no poll cadence | closed | §W3.2 |
| X-M6 singleton lock: wait, half-init grandchild, CLI death, collision | closed | §W2.2 |
| X-M7 hash not restartable; bound-check→hash→promote TOCTOU | closed | §W6.2 |
| X-M8 rename `errno` cases | closed | §W6.3 |
| X-M9 (i) §5a traceability, (ii) client-triggerable G5 | closed | §W6.5, §W1.2 |
| X-M10 `spawn_intent_id` collision | closed | §W2.3 |
| X-M11 `ALREADY_DELIVERED` outside its enum | closed | §W4.8, §W5.2 |
| X minor 1 signal dispositions vs allowlist | closed | §W2.6 |
| X minor 2 "behavior-capable" / first-instruction claim | closed | §W2.6 |
| X minor 3 client reply-timeout continuation | closed | §W5.4 |
| X minor 4 `REPLY/` creation/mode/GC | closed | §W5.4, §W7 |
| X minor 5 §3 durability for control plane | closed | §W7 |
| X minor 6 truthfulness qualifier on the mechanical list | closed | §W5.3 |
| X minor 7 untracked control paths | closed | §W6.6 |
| Sol C1 generation-total B1; unrepresentable phases; no reducer; key allocation | closed | §W1.1–§W1.5 |
| Sol C2 ack/redemption/retention inconsistency; unbounded polling; GC replay proof | closed | §W1.5–§W1.7 |
| Sol C3 circular bound; no aggregate/write-time capacity; quarantine release; undefined `FAILED` | closed | §W4.2–§W4.7 |
| Sol C4 registration before behavior; freeze evidence; `PROCESS or CLOCK` | closed | §W3.2–§W3.4 |
| Sol C5 pre-claim takeover; singleton under spawning-client death; controller bootstrap mode | closed | §W2.2–§W2.6 |
| Sol M1 status leakage; descendant role proof | closed | §W5.1, §W5.3 |
| Sol M2 seven named schema/field gaps | closed | §W4.4 (`bytes_reserved`), §W4.7 (`FAILED` artifact), §W1.3 (ack keys), §W5.2 (`ALREADY_DELIVERED`), §W4.4 (admission binds key + semantic hash), §W2.3 (intent binds child), §W5.5 (length bounds) |
| Sol eight-command B1 trace (all 8 rows) | closed | §W1.4–§W1.5 |
| Sol validity/scientific non-regression list | preserved unchanged | §W6.6 |
| Opus "prior findings genuinely closed by v2" (F5 half, F6 half, F7, F8, F9/Sol M1, F10 controller half, F11/Sol M3, F12, F13, F14, F15/Sol M4, Sol M5/D1, A3 honesty, Codex §S6 C1–C4/M1–M6) | **not reopened**; carried verbatim | §V2.1.7, §V2.7.5, §V2.8, §V2.9.4, §V2.14 |

---

## W10. Finite implementation test matrix (replaces §V2.12)

Disposable roots only; fake clocks/meters; no production-compatible
real-T artifact; no test creates a capability, world, learner, entropy,
or scientific object.

| # | Test | Covers |
|---|---|---|
| 1 | intent-key derivation recomputed by the supervisor; forged `intent_scope_sha256` or `occurrence_index` → `INVALID`/`INTENT_KEY` | X-C1b |
| 2 | successive intended heartbeats allocate distinct occurrences; a lost-reply retry reuses the unfinished slot; both across a fresh CLI process | X-C1, Sol C1.5 |
| 3 | retry across a supervisor generation change: identical cached effect reply and token bytes in a fresh envelope; never `REPLAY_BYTES`, never `STALE_GENERATION` | X-C1, Sol C1.1–C1.2 |
| 4 | same key with changed semantics → `INVALID`/`REPLAY_BYTES`, no ledger append, no G5 | X-C1c, X-M9ii |
| 5 | four immutable journal phases; predecessor binding; second write of any phase refused | Sol C1.3, X-C6 |
| 6 | reducer for all eight commands: crash injected between every pair of plan steps; exactly one effect; head-moved-outside-plan → record-first invalidity | Sol C1.4 |
| 7 | implicit effect-ack by successor occurrence and by process terminal; explicit delivery ack with both hashes; ack durable before `ALREADY_DELIVERED`; ack-before-token impossible | Sol C2 |
| 8 | unbounded `OPERATION_STATUS` observation creates no journal entry; tombstone high-water bounds; post-GC key → `ALREADY_ACKNOWLEDGED`; tombstone never deleted; monotone-lowering replace → invalidity | Sol C2 |
| 9 | pre-claim orphan discovered by the argv `spawn_intent_id` marker after supervisor death at each of the five spawn cuts | X-C2, Sol C5 |
| 10 | argv that never self-stops → bounded wait → `BOOTSTRAP`, group killed, reaped, intent resolved; argv that exits → same | X-C2 |
| 11 | CLI death after fork, before identity install: `SPAWN.lock` still held by the grandchild; second CLI blocks; one supervisor | X-M6, Sol C5 |
| 12 | identity-install collision: loser exits writing nothing | X-M6 |
| 13 | client takeover writes no `runtime/` byte and appends no ledger entry; supervisor takeover performs every settlement under `T_RUNTIME.lock` | X-C5 |
| 14 | no `--supervisor-serve`/`--watchdog-serve` token is accepted; in-process fork entry for supervisor and watchdog; controller learns its FDs from `--officina-ctrl-fds` | X-M1 |
| 15 | adapter installs no signal disposition; no capability exists before `SIGCONT` at every injected cut | X minors 1–2 |
| 16 | `SIGCONT` refused until the watchdog acks the exact `table_seq`; unacked renewal leaves the old deadline authoritative | Sol C4 |
| 17 | ack liveness judged on `ack_monotonic_ns`: supervisor busy for ≫ 1 s inside chunked work does not declare a healthy watchdog dead | X-M5 |
| 18 | freeze quiescence proof over recorded members + parent/session chain; `freeze_ns` sampled only at the proving pass; exhausted passes → `UNKNOWN` | Sol C4, X-M4 |
| 19 | lost freeze evidence → `freeze_ns = null`, unknowable all-live settlement; no synthesized timestamp; supervisor-written observation when the watchdog is dead | X-C4.4 |
| 20 | every watchdog freeze routes to invalidity with cause `PROCESS`; `T_PROCESS_RESOURCE_STOP` and every valid terminal refused; independently verified clock fault → `CLOCK` under §2a precedence | X-C4.1–2, Sol C4 |
| 21 | watchdog death, supervisor death, stale `table_seq`, PID reuse, fork failure — one continuation each | X-C4, §W3.5 |
| 22 | `OPERATION_ADMIT` installs the bound; no pre-existing `BOUND.json`; no ninth command; `operation_id` free of circularity | X-C3.1–3, Sol C3.1 |
| 23 | admission refused `NO_CAPACITY` on each predicate clause: per-operation ceiling, aggregate ceiling, filesystem margin, unreadable ledger | X-C3.4, Sol C3.2 |
| 24 | worker holds no writable output path or descriptor; a worker attempt to `open` `out/` under a contract-following path finds none | K1 |
| 25 | framed parser: oversize header, malformed JSON, bad grammar, duplicate path, count exceeded, non-int/`bool`/negative `content_bytes`, EOF mid-header, EOF mid-content, EOF at boundary with `COMPLETED` and with `FAILED` | K1, Sol C3.5 |
| 26 | ceiling reached mid-chunk: nothing further written, read end closed, worker sees `EPIPE`, group killed, `BOUND_EXCEEDED` quarantine, bytes accounted exactly | X-C3.4 |
| 27 | one watchdog step and one control step serviced between every 4 MiB chunk; ≤ 64 chunks per maximum operation | X-C3.4b, X-M5 |
| 28 | quarantine keeps consuming capacity; `SETTLEMENT`, `FAILED`, rename, and promotion release nothing; only `<op>.disposed.json` with `custody_absent` releases | Sol C3.3 |
| 29 | crash reconstruction takes `max(recorded, enumerated)`; an operation directory without a capacity record counts the full per-operation ceiling; unreadable path → refuse | Sol C3.2 |
| 30 | every `failure_class` maps to its signed route; no valid event under unresolved invalidity; no live process resumes after an invalid operation | Sol C3.4 |
| 31 | `ENOSPC` mid-copy → `FILESYSTEM` invalidity, admissions refused, nothing deleted | §W4.7 |
| 32 | supervisor crash mid-copy → `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; no offset resume; no worker respawn | X-M7 |
| 33 | held-descriptor revalidation detects a same-UID modification of `out/` before settle → `HASH` class | X-M7 |
| 34 | `st_dev` preflight refuses to serve on a split filesystem; `ENOENT`/`EEXIST`/`ENOTEMPTY` rename routes | X-M8 |
| 35 | `SETTLEMENT.json` is the sole commit; wrong/old/sibling charge cannot promote; rename-vs-settlement cuts single-valued | F12 regression |
| 36 | every pre-terminal status reply is byte-identical `{operation_id, phase: "PENDING"}`; no timing or shape varies with output | Sol M1 |
| 37 | controller descendant and group member refused on `REQUEST.fifo`; CLI frame on a controller pipe refused; worker control frame refused | Sol M1, X-M4 |
| 38 | newline framing: two concatenated frames, a tail, an oversize line, a buffer overflow — each single-valued | X-M3 |
| 39 | non-canonical `reply_fifo` refused; a client cannot name another client's reply FIFO; `ENXIO` dead reader caches without re-apply | X-M3 |
| 40 | argv element/byte bounds; no legal reply exceeds `T_CONTROL_FRAME_MAX_BYTES` | X-M2, X-M5 |
| 41 | every schema in §W7 validated for exact keys, strict `int` (`True` refused), recursive scientific-field rejection, and one legal on-disk layout | X-C6, Sol M2 |
| 42 | `spawn_intent_id` collision impossible with identical argv in one nanosecond tick (distinct `process_sequence`) | X-M10 |
| 43 | mandatory `CHILDREN/<process_id>/` rename; exactly one takeover scan | X-C6, F8 |
| 44 | `k > 1` stream exclusive ownership; subset charge; all-live batch over the complete frozen set | F15/Sol M4 regression |
| 45 | heartbeat E1/E3 → automatic signed batch; no fabricated reservation; event-backed G7/G2; `ARCHIVE` before `RESOLVED` | §V2.8 regression |
| 46 | raw ledger-suffix D1 completion; G5 scoped since last valid admission; close in one lock epoch; sequence non-reuse across a closed generation | §V2.8 regression |
| 47 | real `python -m philosophia.officina.generic_harness` six commands, refusal-first; unknown command → exit 2 | §V2.10 regression |
| 48 | quarantine verifier: zero new imports beyond the allowlist; `verification.py` byte-unchanged | §V2.10 regression |
| 49 | `runtime_control/**` and `runtime/T_PROMOTED/**` never staged and never tracked; clean-HEAD rule holds | X minor 7 |
| 50 | proof that no invalid process, operation, or programme ending can be recorded as any valid terminal | signed relabelling regression |

Rows 1–35 include at least one test for **every** Critical and Major
finding of both reviews; the mapping is §W9.

---

## W11. Governance, determinacy, and negative space

**Two-implementer determinacy.** Intent keys and semantic hashes are
fully derived and supervisor-checked (§W1.1–§W1.2); journal phases are
four fixed files with fixed keys (§W1.3); every effect is a fixed
locator list with one probe order (§W1.4–§W1.5); spawn, singleton, and
takeover have one lock discipline and one discovery predicate
(§W2.2–§W2.9); the watchdog has one evidence path, one freeze
predicate, one cause, and one route (§W3); the operation transaction is
nine ordered steps with content-derived paths (§W4.4); the transport
has one wire format and an exhaustive cut table (§W4.5); capacity has
three artifacts and one release (§W4.6); replies are an exhaustive
matrix over closed enums (§W5.2); every durable object has one path,
one schema, one installer, one lock, and one removal actor (§W7). No
clause resolves to "as reviewed".

**Compatibility classification.** This is an engineering/control
amendment surface over the signed harness composite. It contains no
protocol amendment to the signed composite except the **explicitly
named** supersession of harness §5a's physical at-or-before-deadline
sentence (§W6.5), which replaces an unattainable guarantee with a
weaker, true, fail-closed one and moves no constant, event, schema,
root, or scientific cell. The K1 envelope constants are author-signed,
not chosen here.

**Negative space.** This correction creates nothing executable and
authorizes no implementation, commit, host change, process, endpoint,
pipe, FIFO, journal instance, spawn intent, operation, output bound,
promoted object, capability, lease, batch, activation artifact,
production call-graph manifest, entropy, E1/E2/E3 spend, world,
learner, candidate, Q attempt, Q/C object, datum, outcome, Proof, or
claim movement. It moves no E1/E2/E3 constant, none of the nine signed
events, no runtime schema, no roots tuple, no batch arithmetic, no
import allowlist entry, and no T/Q/C boundary. New artifacts are
control-plane, T-development-only, archival-excluded, untracked, and
permanently non-citable for Q/C.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** until both fresh bounded X/Y confirmations accept this
v2.1. `successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
