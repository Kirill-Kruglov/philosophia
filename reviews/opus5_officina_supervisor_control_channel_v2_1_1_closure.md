READY_FOR_OFFICINA_SUPERVISOR_V2_1_1_FINAL_XY_CONFIRMATION

# Officina supervisor/control-channel v2.1.1 — author closure

Date: 2026-07-30.

**Provenance, stated literally.** This closure and
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
were written by **Claude Code Opus 5 acting as the specification author**,
because Claude Code Fable 5 was unavailable. Neither file is labelled as
Fable 5 work, and **neither counts as independent review evidence**. As
`reviews/officina_supervisor_v2_1_authorship_note.md` already records for
v2.1, the author line must not be counted as an X-line reviewer of its own
text. This closure is an authored self-assessment. The only next
authorization is independent bounded X/Y confirmation of the **v2.1.1
bytes**, not of this closure.

## Verdict

```text
READY_FOR_OFFICINA_SUPERVISOR_V2_1_1_FINAL_XY_CONFIRMATION
```

Every Critical, Major, and Minor finding of both independent v2.1 reviews
is closed by an exact mechanical repair in the v2.1.1 bytes. No repair
required discretion in a scientific, resource, or invalidity field; no new
author-choice token was found to be unavoidable; A3, B1, C1, D1, and K1 are
implemented literally and none is reopened, weakened, or reinterpreted. K1
in particular is now implemented as **signed** — settlement, rename,
promotion, failure, and unused reservation replenish nothing.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **not signable**, and this closure does not make it signable.

## Artifacts

```text
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md   (new; 1893 lines)
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md     (unedited)
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md            (unedited)
cf4fab454e27f0c4c2ad6a7583c70a79a7aff8ed1711bf279c13683b85f74c60  reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md          (X-line, unedited)
c97f98a0c0050f28e0849dc1782f9a403b4c99f58ee64636215dab114a47b1cd  reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md           (Y-line, unedited)
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
cf0f1bd85fc9bdc4b8f7bfd8393eedddc4dc89633687224f73a8024e0dee2e21  reviews/opus5_officina_supervisor_control_channel_v2_1_1_repair_prompt.md
```

Method: static authorship. The frozen/inactive implementation was read
**read-only** only where the contract had to stay implementable
(`ALLOWED_ABSOLUTE_IMPORTS` in `src/philosophia/officina/verification.py`;
the `t-recovery-disposition.v1` path/validator pattern and
`author_decision_sha256` convention in
`src/philosophia/officina/generic_harness.py`). Nothing was edited, run,
probed, or started.

---

## 1. One-to-one disposition of every v2.1 finding

### Opus 4.8 X-line Criticals

| Finding | Disposition | v2.1.1 locus | What exactly changed |
|---|---|---|---|
| **X21-C1** `spawn_intent_id` circular; generation-local fds in the hashed argv make two reducer rows inexecutable | **closed** | §Z3.1, §Z3.2, §Z0 rows for §W2.3/§W2.4/§W1.4 `CLAIM` | Two hashes over two explicit domains: `argv_template_sha256` over a template holding the literal placeholders `<SPAWN_INTENT_ID>` and `<CTRL_FDS>` (no derived marker, no descriptor number), and `complete_argv_sha256` over what was executed. `spawn_intent_id = SHA-256({generation, role, process_sequence, argv_template_sha256, created_utc})` is computable. In-generation respawn under the same intent reproduces the template with new fd numbers; cross-generation respawn is forbidden outright (§Z2.4) |
| **X21-C2** the `spawning_id` `cmdline` marker cannot exist; a hung grandchild wedges the singleton forever | **closed** | §Z3.5, §Z0 rows for §W2.2/§W2.4, §Z11 rows 2–4 | Marker predicate deleted for non-`exec`ing processes. The grandchild's first actions are `SPAWNING_CHILD.json` (atomic no-replace) and one sealed-bootstrap-pipe line carrying pid/start identity/pgid. Kill is by recorded identity. Three bounded timeouts: grandchild first-ack wait, CLI bootstrap read/poll, and `LOCK_EX\|LOCK_NB` acquisition with a bounded retry; plus an identity-proved stuck-holder route. D1 cannot be wedged |
| **X21-C3** no renewal-publication trigger ⇒ a compliant heartbeat is frozen and invalidated | **closed** | §Z4.1, §Z4.2, §Z4.3 | Trigger restored verbatim ("after **every** successful locked claim-start, renew, and remove"); `watchdog_table_seq` added to the `HEARTBEAT`, `CLOSE`, and `PAUSE` effect plans with matching reducer probe/action rows; the watchdog **drains before it freezes** so a renewed lease is never frozen at a superseded deadline (Opus Q2's symmetric gap); ack absence routes to §W3.5 with `REFUSED`/`WATCHDOG_UNACKED`, never to a fabricated later renewal |
| **X21-C4** no durable locator proves worker start; `ADMITTED` cacheable behind a permanently stopped worker | **closed** | §Z5.1, §Z5.2, §Z6.7 | `RUNNING.json` (`t-operation-release.v1`) is step 7 of a ten-step plan, before `SIGCONT` (8) and before `committed`/`reply` (9, 10); `running_path` is in the effect plan; the reducer's reply-exists branch **must** probe it; §W4.8's signal-as-durable-trigger cell is replaced by `RUNNING.json` |
| **X21-C5** client intent-slot GC contradicts allocation and permanently loses forward progress | **closed** | §Z1.1–§Z1.5, §Z1.8, §Z10.2 | Allocation moved entirely to the supervisor (CAS against the tombstone's `next_occurrence_index` under `T_RUNTIME.lock`). Client files are convenience only and **freely deletable with no correctness effect**. The reply envelope carries `next_occurrence_index`, so a client with a lost or absent slot directory re-anchors in ≤ 2 round trips — Opus's repair (c) realized in the envelope, leaving §W5.2's closed `REFUSED` detail set intact |

### Opus 4.8 X-line Majors

| Finding | Disposition | v2.1.1 locus | What exactly changed |
|---|---|---|---|
| **X21-M1** no supervisor acceptance predicate for freeze observations | **closed** | §Z4.6 | Ten-conjunct predicate (schema, recomputed `witness_id`, generation, `table_seq`, lease liveness, deadline agreement with both the table row and the current durable lease, `pgid`/`start_identity`, `killer` consistency with the fork-child record, quiescence/`freeze_ns`/`overrun_ns`/member-count consistency, independent present-tense quiescence proof). Any failure ⇒ supervisor-written `UNKNOWN` witness ⇒ all-live invalid route. Never valid evidence |
| **X21-M2** stale-generation witnesses collide on a no-replace path | **closed** | §Z4.5 | Path becomes `FREEZE/<witness_id>.json` with `witness_id = SHA-256({generation, process_id, table_seq})`; writer re-reads `SUPERVISOR_IDENTITY.json` and refuses on generation mismatch; production order (file then event) and consumption order (`generation == current` desc, `table_seq` asc, earliest authoritative) pinned; `EEXIST` has a defined continuation |
| **X21-M3** `t-worker-status.v1` undefined; EOF at a boundary with no status frame has no row | **closed** | §Z7.1–§Z7.3 | Keys exactly `schema, scientific_outcome, operation_id, exit_reason, frame_count, total_content_bytes`; `output_relative_paths` not restored (paths derive from framed headers only); the two worker integers are fail-closed cross-checks that can only quarantine; the missing row added ⇒ `WORKER_FAILED` quarantine + signed invalid route |
| **X21-M4** the `WATCHDOG` spawn-intent role is unsatisfiable | **closed** | §Z3.2, §Z3.6 | Role enum becomes `{CONTROLLER, WORKER}`; the watchdog gets `t-fork-child.v1` (`WATCHDOG/WATCHDOG_CHILD.json`) with pid/start identity/pgid and **no argv field** |
| **X21-M5** tombstone advance trigger unspecified; two disposition rows not well-formed | **closed** | §Z1.5, §Z1.9 | Tombstone keys become `next_occurrence_index` + `acknowledged_prefix_occurrence`; `last_effect_reply_sha256` deleted; both advance only in named lock epochs (allocation; the ack install); the disposition table is eight rows decidable from the frame plus two integers, with `INTENT_KEY`/`REPLAY_BYTES` separated from `ALREADY_ACKNOWLEDGED` |
| **X21-M6** `PROCESS_TERMINAL` does not prove observation (`CLOSE` acks its own reply) | **closed** | §Z1.7 | Scopes whose own plan names `process_record_path`, `stopped_event_sha256`, or `pause_event_sha256` are **excluded** from `PROCESS_TERMINAL`; a successor acks only when it carries the exact prior `effect_reply_sha256`; a new `CLIENT_ECHO` source lets `RETRY(i)` carrying that hash both collect and acknowledge the bytes in one round trip, adding no command |
| **X21-M7** §W6.2 over-claims TOCTOU detection | **closed** | §Z8.2, §Z8.3 | The false "is detected" claim is withdrawn; a bounded pre-settlement pass re-resolves each path through the held `out/` dir-fd, requires `(st_dev, st_ino)` identity against a read descriptor held since creation, and **re-hashes** with `os.pread` in 4 MiB chunks (≤ 64 per operation, one watchdog and one control step between chunks). Equal-size content substitution and inode substitution are now mechanically detected; the remaining same-name directory swap between verification and `os.replace` is named as an A3 procedural residual |
| **X21-M8** the sole capacity-release artifact is under-specified | **closed** | §Z6.4–§Z6.6, §Z10.7 | One immutable author object at `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json` outside the control plane, with a non-circular `disposition_id`, an exact 15-key set, a pinned author token literal, a tracked signature-file grammar and hash/line verifier, activation + settlement-generation + operation + custody-parent bindings, no-replace single use, a twelve-conjunct fail-closed verifier, and a **same-lock descriptor-safe custody-absence proof** (`ENOENT` under `O_NOFOLLOW` dir-fd **and** absence from the enumeration, recursing upward). Every mismatch/stale/substitution/replay route releases nothing |

### Opus 4.8 X-line Minors (all seven)

| Minor | Disposition | v2.1.1 locus |
|---|---|---|
| 1 `T_MIN_HEARTBEAT_INTERVAL_NS` has no rule | **closed** — given a normative control-plane rule: a heartbeat inside the interval is `REFUSED`/`BUSY` with empty tuples, no charge, no lease, no publication; E1 arithmetic unchanged because charging is the cursor difference | §Z9.1 |
| 2 `T_ARGV_MAX_BYTES` jointly unsatisfiable | **closed** — `T_ARGV_MAX_ELEMENTS = 32`, `T_ARGV_MAX_BYTES = 768`, printable-ASCII-only argv, `T_REQUEST_ENVELOPE_MAX_BYTES = 1536`, `T_ARGUMENTS_MAX_BYTES = 2560`, `T_REPLY_MAX_BYTES = 2048`, with the worst-case arithmetic written out | §Z9.2 |
| 3 `--officina-ctrl-fds` overloaded, no per-role order | **closed** — controller (request write, reply read), worker (status write, output write), both `dup2`'d to pinned fds 3 and 4 by the adapter and re-verified after `SIGCONT` | §Z3.3, §Z9.3 |
| 4 preflight compares against a lazily created directory | **closed** — compares `st_dev` against the existing `successor/officina/runtime/` root, plus `T_PROMOTED` when it already exists | §Z9.4 |
| 5 zero-output completion undefined | **closed** — canonical empty result: promote with `promoted_relative_paths = []`, `result_sha256 = SHA-256(b"[]")`, `actual_bytes = 0`; capacity still retained | §Z7.3 |
| 6 concurrent `.done.json` `EEXIST` | **closed** — structurally (distinct occurrences) plus a pinned client continuation: equal hash ⇒ silent idempotent continue; different ⇒ exit 5, send nothing, delete nothing | §Z1.8, §Z9.6 |
| 7 §W9 overstates closure | **closed** — every inherited row now reads "closed in v2.1; confirmation pending v2.1.1 X/Y", with X-C2, X-C6, X-M1, X-M10 further marked "closed **subject to**" their v2.1.1 repairs | §Z12.1 |

### GPT-5.6 Sol Y-line Criticals and Majors

| Finding | Disposition | v2.1.1 locus | What exactly changed |
|---|---|---|---|
| **Sol C1** new-vs-retry inferred; STATUS unjournaled; successor ack without proof; tombstone recovery incomplete; reducer rejects descendant heads | **closed on all five mandated items** | §Z1.1–§Z1.9, §Z2.1–§Z2.3 | (1) explicit `occurrence_mode ∈ {NEW, RETRY}`; the reply envelope **is** the durable handle; unfinished state is never consulted. (2) allocation is supervisor-authoritative from tombstone + journal; client deletion or relabelling can neither reuse nor block `next`. (3) observation-form `OPERATION_STATUS` is journaled and cached with **empty** effect tuples; a new poll is a new occurrence and a retry is byte-stable across promotion and delivery ack. (4) successor acknowledgement requires the exact cached prior `effect_reply_sha256`; the separate delivery ack is kept. (5) a contiguous, supervisor-derived acknowledged-prefix tombstone whose classification needs no old reply hash; GC only over that prefix, in the ack's lock epoch |
| **Sol C2** reducer turns later history into G5; takeover is not validity-first | **closed** | §Z2.1–§Z2.5 | Chain membership (`in_chain`/`ordered`) replaces head equality: a committed/replied plan is accepted whenever the current head is a verified descendant. Accepted-only plans require the exact legal prefix and no conflicting intervening suffix, with four exhaustive routes (accept / resume / `SUPERSEDED_PLAN` / record-first invalidity for genuinely impossible layouts). Takeover splits into phase 2A (prove, freeze, settle every affected stream through the signed all-live invalid route, complete unresolved batch authority, resolve intents) and phase 2B (non-behavioral reducer work only). Across a supervisor loss no reducer may spawn, `SIGCONT`, renew, admit, install a lease, or otherwise continue behavior |
| **Sol C3** spawn identity not constructible or total (four contradictions) | **closed on all four** | §Z3.1–§Z3.7 | (1) template/complete two-hash construction with explicit domains. (2) sealed bootstrap pipe + immediate no-replace `SPAWNING_CHILD.json` + three bounded timeouts + kill-by-recorded-identity; no `cmdline` claim for a process that never `exec`s. (3) `WATCHDOG` removed from the argv-bearing intent; exact no-argv fork-child record instead. (4) the fixed reviewed supervisor-owned bootstrap adapter is the **actual executable root**: it verifies the thirteen-index layout, `dup2`s and type-checks the descriptors, closes forbidden descriptors, preflights the target, installs no signal disposition, self-stops, and `os.execv`s the target only after `SIGCONT` — so an arbitrary non-Officina target needs no Officina awareness |
| **Sol C4** `OPERATION_ADMIT` caches success before the worker is runnable | **closed** | §Z5.1, §Z5.2 | Durable `RUNNING.json` release locator precedes `SIGCONT`, and both precede `committed`/`reply`; a same-generation reducer completes the idempotent release before success is cacheable; after a supervisor loss §Z2.5 freezes and settles the worker and never resumes it |
| **Sol C5** v2.1 replenishes capacity at settlement, contrary to signed K1 | **closed** | §Z6.1, §Z6.2, §Z6.7 | `accounted_total` is `Σ bytes_reserved` over undisposed operations plus the full ceiling for record-less custody. `actual_bytes` is diagnostic only and may never reduce the 32 GiB total. Every over-declaration/unused-reservation release is removed; settlement, quarantine, rename, promotion, and delivery ack release nothing; only a verified disposition releases, and it releases exactly `bytes_reserved` |
| **Sol M1** the author-disposition authority is not an executable closed contract | **closed** | §Z6.4–§Z6.6 | See X21-M8: path grammar, schema, exact key set, author token/signature representation and verifier, activation/settlement-generation/operation bindings, reserved and actual byte facts, custody destination and parent/hash bindings, atomic no-replace single use, recursive scientific-field prohibition, supervisor disposition bound to the exact author-file hash, same-lock descriptor-safe absence proof, and the complete mismatch/stale/substitution/replay table |
| **Sol M2** fixed reply bytes but a false timing-secrecy claim | **closed** | §Z8.1 | §W5.1's "reveals nothing" is replaced by the honest boundary: fixed `PENDING` bytes retained; latency, backpressure, filesystem/endpoint metadata, path existence, worker timing, and every same-UID observation are T-process procedural facts, permanently non-citable, and forbidden from selection, Q/C, C1–C6, blinding claims, and any scientific interpretation |
| **Sol M3** strictly-positive overrun lacks a total equality case | **closed** | §Z4.4 | A proving pass whose sample is not strictly greater than the deadline takes bounded later monotonic samples with quiescence re-proved each pass; without strict progress ⇒ `freeze_ns = null`, `quiescence = UNKNOWN`, the all-live invalid route. No valid zero-overrun branch is restored and no tolerance constant exists |

### Sol's eight required B1 traces

| Trace | Required result | v2.1.1 result |
|---|---|---|
| Lost request before `accepted.json` | same explicit occurrence may retry; no effect | `NEW(i)` re-sent while `i == next(scope)` allocates and applies exactly once; the lost frame left nothing (§Z1.5 row 1) |
| Lost reply after `reply.json` | identical cached effect reply across generations | `RETRY(i)` ⇒ row 2 ⇒ cached effect-reply and token bytes re-wrapped in a fresh envelope; all eight commands (§Z1.6 adds the eighth) |
| Client crash after seeing the reply, before `.done` | cached old reply remains available; a separately declared new occurrence remains possible | `RETRY(i)` returns identical bytes; `NEW(i+1)` is a distinct effect; `.done` is convenience only and is never read by the supervisor (§Z1.4) |
| Generation change | same semantic occurrence, new transport wrapper | unchanged from v2.1 and now total for the eighth command; `STALE_GENERATION` is not returned for a journal-recorded generation |
| Effect before `committed.json` | one command-specific reducer continuation | one continuation per command with C2/C3/C4 repaired: locator-keyed resume within the accepting generation, non-behavioral-only completion across a loss (§Z2.4, §Z1.10 column K5) |
| Ack then GC then old retry | no reapplication; closed acknowledged response | `REFUSED`/`ALREADY_ACKNOWLEDGED` decided from `occurrence_index ≤ acknowledged_prefix_occurrence` alone; no old reply hash needed (§Z1.5 row 5) |
| Concurrent same-scope clients | distinct new occurrences; same occurrence only for explicit retry | the CAS gives distinct occurrences under every interleaving; the loser re-anchors on the envelope's `next_occurrence_index` (§Z1.3, §Z1.5 row 3) |
| Repeated STATUS | new observation gets a new occurrence; retry of one observation is stable | exactly that, with ≤ `T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64` unacknowledged per scope keeping growth bounded (§Z1.6, §Z1.9) |

The full 8 × 8 command/cut matrix is §Z1.10 of the correction.

---

## 2. Replacement index v2.1 → v2.1.1 (summary; the exact index is §Z0)

§Z0 of the correction names **every** superseded v2.1 clause, sentence,
and table row — 68 rows, quoted at the clause or sentence level. Summary
by section:

| v2.1 section | Rows replaced / extended / deleted | New locus |
|---|---|---|
| §W1.1 | whole section, two bullets, one paragraph | §Z1.1–§Z1.4, §Z1.8 |
| §W1.2 | request key list, journal case 1, transport-binding sentence | §Z10.1, §Z10.2, §Z1.5 |
| §W1.3 | `t-request-accepted.v1` key list | §Z10.3 |
| §W1.4 | the empty-tuple refusal sentence; five `effect_plan` rows | §Z1.7, §Z3.2, §Z4.2, §Z5.1, §Z1.6 |
| §W1.5 | head guard, reply-exists branch, three probe rows, the observation paragraph | §Z2.1–§Z2.4, §Z5.2, §Z1.6 |
| §W1.6 | successor-ack sentence, `PROCESS_TERMINAL` clause, `ack_source` enum | §Z1.7, §Z10.4 |
| §W1.7 | tombstone key list, rows 3–4, the GC rule, the growth-bound paragraph | §Z1.5, §Z1.9 |
| §W2.1–§W2.5 | the no-private-surface sentence, the watchdog bullet, four §W2.2 sentences, the intent key list and role enum, the four appended tokens, the discovery predicate, the `spawning_id` sentence | §Z3.1–§Z3.6 |
| §W2.8, §W2.9 | the process/FD table, phase 1 step 2, phase 2's order | §Z10.6, §Z2.5, §Z3.5, §Z3.6 |
| §W3.2–§W3.5 | publication sentence, step 4, witness path, the "one mechanical evidence path" sentence, the `PROVED` sentence, the "> 0 by construction" clause, two table rows | §Z4.1–§Z4.6 |
| §W4.2–§W4.8 | one preflight line, the preflight block, steps 7–9, two §W4.5 sentences, two cut rows, the accounted formula, two capacity rows, reconstruction steps 1–4, the retention paragraph, four transition rows | §Z5.1, §Z6.1–§Z6.7, §Z7.3, §Z7.4, §Z8.3, §Z9.4, §Z9.5 |
| §W5.1–§W5.5 | the timing sentence, the reply matrix header/`REFUSED` row, the refusal enum, the reply-timeout bullet, the argv bounds | §Z8.1, §Z10.2, §Z10.5, §Z1.8, §Z9.2 |
| §W6.2 | two sentences | §Z8.2, §Z8.3 |
| §W7 | nine rows replaced, four rows added | §Z10.7 |
| §W8 | seven rows replaced, twenty-two added | §Z11 |
| §W9, §W10, §W11 | the disposition table's unqualified rows; the matrix extended by rows 51–74; the determinacy paragraph extended | §Z12.1, §Z12.2, §Z13 |
| §V2.8, §V2.1.1, §V2.1.3, §V2.1.7, §V2.2.1, §V2.7.5, §V2.9.2, §V2.9.4, §V2.14, §W2.6, §W3.1, §W4.1, §W5.3, §W6.1, §W6.3–§W6.6 | **unchanged and carried forward verbatim** | — |

---

## 3. State and authority table

Which filesystem object is what kind of thing. Nothing in the
`convenience` or `transport` rows can ever move runtime state; nothing in
the `witness` row can settle; only the `author` rows can release signed
capacity.

| Object | Class |
|---|---|
| `T_CLIENT_INTENTS/<scope>.<n>.json`, `…done.json` | **convenience** — never read by the supervisor; freely deletable at any time with no correctness effect |
| `REQUEST.fifo` / `REPLY/<…>.fifo` frames, watchdog update/ack frames, the bootstrap-pipe line, worker output frames, worker status frames | **transport** — validated on arrival, never authority at rest; worker claims are never trusted for paths, bytes, or terminals |
| `WATCHDOG/FREEZE/<witness_id>.json` | **control witness** — becomes evidence only after the ten-conjunct §Z4.6 predicate; otherwise it is replaced by a supervisor `UNKNOWN` witness and routed to all-live invalidity |
| `WATCHDOG/LEASES.json`, `WATCHDOG/WATCHDOG_CHILD.json` | **control witness / control record** — the table binds deadlines the supervisor published; neither is a settlement or validity authority |
| `SPAWNING.json`, `SPAWNING_CHILD.json`, `SUPERVISOR_IDENTITY.json`, `CHILDREN/*`, `JOURNAL/**`, `JOURNAL/TOMBSTONES/*`, `CAPACITY/*`, `operations/**` (`BOUND`, `OPERATION`, `RUNNING`, `SETTLEMENT`, `QUARANTINE`, `DELIVERY_ACK`), `runtime/T_PROMOTED/**` | **runtime authority** — written only by the sole supervisor under `T_RUNTIME.lock` (or `SPAWN.lock` for the two spawn markers), one legal layout each, one removal actor each |
| `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json`, `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_*_SIGNATURE.md` | **author authority** — installed by the author, never written by the supervisor, single use, and the only path that can release K1 capacity |
| signed harness/batch artifacts under `runtime/` (`T_LEDGER.md`, claims, leases, records, invalidities, batch claims/overrides, recovery dispositions, checkpoints) | **runtime authority, signed surface** — untouched by this amendment |

---

## 4. Worked crash traces, including both reviews' counterexamples

### 4.1 B1 — Sol's collapsed-concurrent-heartbeat counterexample

Two CLI processes `P` and `Q` heartbeat process `p`. Scope `S` (its only
argument is `process_id`) has `next = 7`, `acknowledged_prefix = 5`.

```text
P: NEW(7)  → lock → row 1 → accepted.json(7) → next := 8 → charge → lease →
             publish table_seq s → ack → committed → reply
             envelope: occurrence_index 7, effect_reply_sha256 h7, next 8
Q: NEW(7)  → lock → row 3 (equal semantic hash, different allocating client)
             → REFUSED/OCCURRENCE_INDEX, retryable true, envelope next 8
             → NO effect, NO charge, NO publication
Q: NEW(8)  → lock → row 1 → its own occurrence, its own disjoint cursor
             interval
```

In v2.1 both collapsed onto the highest unfinished slot and `Q`'s
legitimate heartbeat was lost. Here they are distinct by construction.

### 4.2 B1 — Opus's forward-progress counterexample

`T_CLIENT_INTENTS/` is deleted entirely while `S` has `next = 51`,
`acknowledged_prefix = 50`.

```text
client: NEW(1)  → row 5 (1 ≤ 50) → REFUSED/ALREADY_ACKNOWLEDGED, envelope next 51
client: NEW(51) → row 1 → allocated, effect applied exactly once
```

Two round trips, no wedge, no reuse, no deadline miss. In v2.1 this client
could never heartbeat again.

### 4.3 B1 — lost `CLOSE` reply (Opus X21-M6)

```text
NEW(i) CLOSE → final charge, process record, stopped event, archival, reply
reply lost on the wire
PROCESS_TERMINAL does NOT ack this scope (its own plan names the terminal)
⇒ ack.json absent ⇒ GC ineligible ⇒ bytes still redeliverable
RETRY(i) → row 2 → identical record/stopped bytes
RETRY(i) with acked_effect_reply_sha256 = h_i → identical bytes AND
          ack.json (CLIENT_ECHO) → prefix advances → GC now eligible
```

### 4.4 Reducer / takeover — Sol's ordinary-later-history counterexample

```text
occurrence i: committed + reply durable, post_ledger_head = H_i, acked
later ordinary events append; current head = H_now ≠ H_i
supervisor restarts before GC
v2.1: head_ok fails ⇒ record-first invalidity ⇒ G5 from ordinary history
v2.1.1: in_chain(H_i) ∧ ordered(declared events) ∧ index(H_i) ≤ index(H_now)
        ⇒ ACCEPT, serve the cached reply, no G5 (§Z2.2)
```

And the validity-first counterexample:

```text
supervisor dies with accepted-only OPERATION_ADMIT (bound + admission durable,
no worker) and a live controller past its deadline
v2.1: phase 2 ran the reducer first ⇒ could spawn a worker before the
      process-loss invalidity was durable
v2.1.1: phase 2A proves/freezes the old generation, writes witnesses, settles
        every affected stream through the signed all-live invalid route, drives
        the batch to its signed terminal, resolves intents; only then phase 2B
        completes non-behavioral work, and this plan's terminal is that invalid
        route — no spawn, no SIGCONT, no lease, no admission (§Z2.4, §Z2.5)
```

### 4.5 Spawn / bootstrap — Opus's wedged-grandchild counterexample

```text
CLI: flock(SPAWN.lock, LOCK_EX|LOCK_NB) (bounded retry) → pipe2 → SPAWNING.json
     → fork → setsid → fork
grandchild: scrub fds → SPAWNING_CHILD.json (no-replace) → bootstrap line
            (pid, start identity, pgid) → endpoints → fork watchdog +
            WATCHDOG_CHILD.json → await first ack, BOUNDED
grandchild hangs in the first-ack wait:
  its own T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS expires ⇒ kill watchdog by record,
  prove death, unlink SPAWNING_CHILD.json, _exit(3), lock fd closed
CLI dies first instead:
  second CLI's bounded LOCK_NB retry expires ⇒ stuck-holder route reads
  SPAWNING_CHILD.json, confirms pid+start identity live, identity absent, age
  > T_SPAWN_BOOTSTRAP_MAX_AGE_NS ⇒ killpg recorded pgid, prove death (lock
  released) ⇒ retry acquisition once ⇒ one supervisor, D1 intact
```

In v2.1 the marker could not exist, so this grandchild was invisible,
unkillable, and held the singleton forever.

### 4.6 Spawn identity — Opus's uncomputable-preimage counterexample

```text
template = [argv0,-m,module,--officina-bootstrap,--officina-role,CONTROLLER,
            --officina-spawn-intent,<SPAWN_INTENT_ID>,
            --officina-ctrl-fds,<CTRL_FDS>,
            --officina-target-argc,<N>,--, *target argv]
argv_template_sha256 = SHA-256(that array, placeholders intact)
spawn_intent_id      = SHA-256({generation, CONTROLLER, process_sequence,
                                argv_template_sha256, created_utc})   # computable
complete_argv        = template with both placeholders substituted
complete_argv_sha256 = SHA-256(complete_argv)                          # separate
discovery            = cmdline[3] == --officina-bootstrap ∧
                       cmdline[6] == --officina-spawn-intent ∧
                       cmdline[7] == spawn_intent_id                   # fixed index
```

### 4.7 Watchdog — Opus's frozen-healthy-heartbeat counterexample

```text
lease deadline D1; controller heartbeats at D1 − 30 s
v2.1: no publication trigger ⇒ watchdog still enforces the ORIGINAL table ⇒
      freeze at D1 ⇒ §W3.4's single route ⇒ fabricated invalidity + all-live
      batch + G5 for a compliant process
v2.1.1: the heartbeat plan appends the charge, installs the successor lease,
        publishes table_seq s (trigger restored), and awaits the ack before
        caching OK; if the watchdog reaches D1 first it DRAINS and re-reads
        LEASES.json, acks s, adopts D2, and does not freeze
dead watchdog instead: no ack within 60 s ⇒ §W3.5 route; the supervisor becomes
        the freezer and settles overdue leases against ITS OWN current durable
        deadlines; the occurrence's cached terminal is REFUSED/WATCHDOG_UNACKED
        whose committed tuples record exactly the durable charge
planted or stale witness: §Z4.6 rejects it on generation, table_seq, deadline,
        identity, member-count, or ordering ⇒ supervisor UNKNOWN witness ⇒
        unknowable all-live invalidity; never valid evidence, never a timestamp
freeze_ns == deadline_ns: bounded later sampling with re-proved quiescence; no
        strict progress ⇒ UNKNOWN (Sol M3); no valid zero-overrun branch
```

### 4.8 Admission — Sol's stranded-worker counterexample

```text
steps 1–6 durable, worker stopped and bound
v2.1: committed → reply(ADMITTED) → SIGCONT; a crash between reply and SIGCONT
      left a stopped worker behind a durable success forever: PENDING forever,
      bytes_reserved charged forever, exit only via deadline → freeze
v2.1.1: 7 RUNNING.json → 8 SIGCONT → 9 committed → 10 reply
  crash after 7, same generation  ⇒ reducer probes running_path, finds the
                                    worker alive and stopped, completes the
                                    idempotent SIGCONT, then commits and caches
  crash after 7, supervisor lost  ⇒ phase 2A freezes and settles the worker;
                                    never resumed; plan closed as that invalid
                                    terminal; capacity retained at bytes_reserved
  reply present, RUNNING absent    ⇒ record-first invalidity naming both paths
```

### 4.9 K1 — Sol's replenishment counterexample

```text
reservation 268_435_456; the worker emits ONE byte; promotion succeeds
v2.1: <op>.settled.json re-measured to actual_bytes = 1 and released
      268_435_455 bytes with no disposition — contrary to signed K1
v2.1.1: accounted_total keeps bytes_reserved = 268_435_456 through
      PENDING_SETTLEMENT, SETTLEMENT.json, <op>.settled.json (actual_bytes = 1,
      DIAGNOSTIC ONLY), the os.replace into T_PROMOTED, and DELIVERY_ACK.json.
      Release requires:
        author signature file tracked and hashed
        → author disposition object verified on all twelve conjuncts
        → same-lock O_NOFOLLOW dir-fd proof that the named custody is ENOENT
          and absent from the enumeration, recursing upward
        → CAPACITY/<op>.disposed.json (no-replace) releasing exactly
          bytes_reserved
      custody still present, stale activation, wrong terminal, substituted
      parent hash, forged token, untracked signature, or a second disposition
      ⇒ release nothing (§Z6.6)
```

### 4.10 Output substitution — Opus's equal-size counterexample

```text
supervisor writes out/a.bin (10 MiB) and hashes inline; holds w and r
attacker (same UID) rewrites a.bin in place with different 10 MiB content
v2.1: st_size, st_ino, st_nlink all unchanged ⇒ v2.1 claimed detection but had
      none; result_sha256 would not describe the promoted bytes
v2.1.1: the pre-settlement pass re-resolves a.bin through the held out/ dir-fd,
      requires (st_dev, st_ino) == r's and st_nlink == 1, then re-reads with
      os.pread in 4 MiB chunks and recomputes the hash ⇒ MISMATCH ⇒ HASH
      quarantine ⇒ no promotion. Inode substitution fails the identity check.
      Same-name substitution of the out/ DIRECTORY between verification and
      os.replace remains an A3 procedural residual and is named as such
```

---

## 5. No-regression table

### Author cells

| Cell | Signed meaning | v2.1.1 status |
|---|---|---|
| **A3** | procedural confinement against a deliberate same-UID principal; mechanical against accident; never Q/C confidentiality | **unchanged and more honest.** Still not a security boundary. Timing/metadata secrecy claims deleted (§Z8.1); the TOCTOU over-claim withdrawn and replaced by real mechanical checks plus one named residual (§Z8.2–§Z8.3); escaped children, foreign-PID reporting, forged argv, planted witnesses, and author-file forgery are each named as procedural residuals, not claimed closed |
| **B1** | all eight commands use a durable, retry-stable, exactly-once-effect journal; identical replies and token bytes redeliverable until a durable acknowledgement records the one-use effect | **unchanged in policy, now total.** The eighth command is journaled (§Z1.6); acknowledgement always proves observation (§Z1.7); allocation, GC, and post-GC classification are supervisor-authoritative and decidable (§Z1.3–§Z1.9). No mechanism was weakened to gain liveness: every new refusal is fail-closed and re-anchorable |
| **C1** | a dedicated watchdog/freezer may stop groups independently while the sole supervisor remains the only runtime writer and later settles | **unchanged and strengthened.** The watchdog holds no lock, no capability, writes nothing under `runtime/`, appends no ledger entry, chooses no terminal, and settles nothing. §Z4.6 adds supervisor-side validation, so a watchdog fact can never become a second runtime authority; unverifiable evidence degrades to `UNKNOWN` invalidity |
| **D1** | no idle timeout; persists until a signed terminal, pause, blocked, crash, or author-stop route | **unchanged and protected.** No `IDLE_EXIT`; and the bounded bootstrap timeouts plus the stuck-holder route ensure a hung pre-identity grandchild cannot wedge D1 or the singleton indefinitely (§Z3.5) |
| **K1** | supervisor-mediated framed transport; the five ceilings; custody includes live/pending/quarantine/promoted; rename, promotion, settlement, failure do not replenish; release only after an authorized custody-absence disposition | **implemented literally for the first time.** All five constants unmoved; no worker writable path or descriptor; the write-path ceiling unchanged; **all replenishment removed** (§Z6.1, §Z6.7); the disposition authority fully specified with a same-lock absence proof (§Z6.4–§Z6.6) |

### Already-signed surfaces

| Surface | Status |
|---|---|
| Harness composite v2 + v2.1/v2.2/v2.3/v2.3.1 | unchanged; the only named supersession remains §W6.5's harness §5a at-or-before-deadline sentence, carried forward from v2.1 unchanged |
| Batch-settlement amendment v1 + v1.1/v1.1.1 (§D1 head/cache completion; §D2 inline `meter_evidence`) | unchanged and referenced only; §Z2.5 phase 2A explicitly requires unresolved batch authority to be driven to its signed terminal with `ARCHIVE` before `RESOLVED` |
| Nine signed events; every runtime schema; E1/E2/E3 constants and arithmetic; `MAX_CONCURRENT_LEASES = 4`; roots tuple; invalidity precedence `HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE`; §2c orders; §4c/§4d settlement; §6a/§6b/§6c; G0–G7 | unchanged |
| §V2.8 in full (boundary batch wiring, event/artifact-backed terminals, raw statically parsed ledger-suffix D1 completion, G5 since last valid admission, one lock epoch for close, private claim-backed `BatchSettlementAuthority`, strict `type(x) is int`, pre-review-head acyclicity, caller-supplied current head, Codex §S6 items 1–13) | unchanged and not weakened |
| §V2.7.5 stream ownership; §V2.9.4 archival exclusions; §V2.10 module root, six public commands, exit 2, byte-frozen files | unchanged. The one added argv entry token `--officina-bootstrap` is refusal-first, is not a public command, and adds no `scripts/*.py` and no seventh public command |
| Import allowlist | **zero delta**; `select`, `selectors`, `signal`, `ctypes`, `sys` remain outside it, which is why the poll stays `time`-paced and why `interpreter_argv0` is read from `/proc/self/cmdline` |
| Signed activation-protocol §B archival sets and the clean-HEAD rule | unchanged. `runtime_control/**`, `runtime/T_PROMOTED/**`, and the new `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/**` are archival-excluded and untracked; the author signature file is a tracked path that must be committed before use; no `.gitignore` or configuration change is authorized |
| Q/C boundary | unchanged. Every new artifact is T-development-only, `scientific_outcome: false`, recursively scientific-field-rejecting, and permanently non-citable for Q/C and C1–C6 |

---

## 6. Implementation and test obligations (no implementation authorization)

**No implementation is authorized by this closure or by the correction.**
No code, test, commit, host change, or process is permitted. The
obligations below become due only after both independent v2.1.1
confirmations accept the bytes **and** the author signs the amendment
token.

Implementation obligations, in the order the contract makes them
verifiable:

1. Occurrence allocation as one CAS under `T_RUNTIME.lock`, with the
   tombstone's two monotone integers, the `max` reconstruction, and the
   eight-row classification table.
2. Four immutable predecessor-bound journal phases, unchanged in shape,
   plus the four acknowledgement sources with their exact preconditions,
   plus prefix-only GC in the ack's lock epoch.
3. The descendant-aware reducer (`in_chain`/`ordered`) with its four
   routes, and the behavioral/non-behavioral partition keyed on
   `supervisor_generation_sha256_at_accept`.
4. Two-phase takeover with phase 2A strictly before phase 2B.
5. The two-hash spawn identity, the thirteen-index adapter argv, the
   fixed-index discovery predicate, the sealed bootstrap pipe,
   `SPAWNING_CHILD.json`, `WATCHDOG_CHILD.json`, and the three bounded
   timeouts plus the stuck-holder route.
6. The bootstrap adapter's six ordered duties, including `dup2` to fds 3
   and 4 per role, forbidden-descriptor closure, target preflight,
   self-stop, and `os.execv` only after `SIGCONT`.
7. Watchdog publication on every claim-start/renew/remove;
   `watchdog_table_seq` in four effect plans; drain-before-freeze; the
   strict-progress sampling rule; `witness_id` naming with pinned
   production and consumption order; the ten-conjunct acceptance
   predicate.
8. `RUNNING.json` before `SIGCONT` and before the cached success, with the
   six-row crash table.
9. K1 accounting with `bytes_reserved` retained throughout; the three
   capacity artifacts; the author disposition object, its twelve-conjunct
   verifier, and the same-lock descriptor-safe absence proof.
10. `t-worker-status.v1`; the total EOF/status table including the
    zero-frame empty-result case; the bounded pre-settlement verification
    pass with inode identity and re-hashing.
11. The frame arithmetic of §Z9.2 enforced as stated, with the frame check
    authoritative.

Test obligations: §W10 rows 1–50 carry forward; §Z12.2 adds rows 51–74,
which include at least one test per Critical and Major of both v2.1
reviews and per Minor. All tests use disposable roots, fake clocks and
meters, no production-compatible real-T artifact, and create no
capability, world, learner, entropy, or scientific object.

---

## 7. Bounded confirmation prompts

Each reviewer must read the **actual v2.1.1 bytes**
(`ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635`)
together with v2, v2.1, both signatures, and their own v2.1 review. **Do
not trust this closure**: it was written by the author line, is not review
evidence, and its disposition table must be re-derived from the
correction's text. Answer the single literal question, then justify per
finding.

### 7.1 X-line — independent clean-context Claude Opus 4.8

> Reading only the v2.1.1 correction bytes, the unedited v2 and v2.1
> documents, the two author signatures, and your own v2.1 review — and
> treating
> `reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md`
> as an untrusted authored self-assessment rather than as evidence:
>
> **Are all five of your Criticals (X21-C1..C5), all eight of your Majors
> (X21-M1..M8), and all seven of your Minors closed by exact, executable,
> non-circular text in v2.1.1, with no repair introducing a new defect,
> no fail-closed behavior weakened to obtain liveness, no watchdog fact
> turned into a second runtime authority, and no author cell (A3, B1, C1,
> D1, K1) reopened — yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_1_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_1`. Then, per finding, state closed /
> not closed with the exact clause you relied on. Give particular
> adversarial attention to: the two-hash spawn construction and whether
> `spawn_intent_id` is now computable and stable across an in-generation
> respawn; whether the sealed bootstrap pipe plus `SPAWNING_CHILD.json`
> plus the three bounded timeouts and the stuck-holder route make every
> pre-identity cut total without wedging `SPAWN.lock` or D1; whether
> drain-before-freeze plus the restored publication trigger removes every
> reachable schedule in which a compliant heartbeat is frozen or
> invalidated; whether `RUNNING.json` makes a cached `ADMITTED` impossible
> without a same-generation release; whether occurrence allocation is
> total, reuse-free, and wedge-free under client-file loss, concurrency,
> and post-GC replay; and whether the pre-settlement verification pass
> plus the named directory-swap residual is an honest and complete
> statement of the A3 output-substitution boundary. Do not run code,
> tests, probes, or any Officina process; edit nothing.

### 7.2 Y-line — independent clean-context GPT-5.6 Sol

> Reading only the v2.1.1 correction bytes, the unedited v2 and v2.1
> documents, the two author signatures, and your own v2.1 review — and
> treating the author's closure as an untrusted self-assessment:
>
> **Does v2.1.1 implement signed A3, B1, C1, D1, and K1 literally — with
> exactly-once, retry-stable, generation-total semantics for all eight
> commands including observation-form `OPERATION_STATUS`; validity-first
> dominance at takeover; a constructible and total spawn/bootstrap
> identity with a reviewed adapter as the executable root; no capacity
> replenishment at settlement, rename, promotion, failure, or unused
> reservation; a closed and executable author custody-absence authority;
> and an honest A3 leakage boundary — with no scientific, resource, or
> invalidity field left to implementer discretion and no author cell
> reopened, yes or no?**
>
> Answer on line 1 with exactly one of
> `CONFIRM_OFFICINA_SUPERVISOR_V2_1_1_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_1`. Then re-run your eight-row B1
> trace table, your C1 evidence-authority checklist, and your K1 trace
> against the v2.1.1 text, and state per row whether the required result
> is now achieved. Give particular adversarial attention to: whether
> supervisor-authoritative allocation plus the contiguous
> acknowledged-prefix tombstone is total under client-file deletion,
> concurrency, and post-GC replay without any unavailable old reply hash;
> whether the descendant-aware reducer can still turn ordinary later
> history into G5; whether any reducer path can continue behavior across
> a supervisor loss; whether `bytes_reserved` is genuinely retained
> through every terminal and rename; whether the author-disposition
> verifier and its same-lock absence proof can be satisfied by a stale,
> substituted, or replayed object; and whether any residual timing or
> metadata claim survives that should be stated as a procedural,
> non-citable A3 residual. Do not run code, tests, probes, or any
> Officina process; edit nothing.

Neither confirmation authorizes implementation. The author token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes eligible
only if **both** confirmations explicitly accept the corrected bytes, and
signing it remains the author's act alone.

---

## 8. Custody and negative-space confirmation

This work created **exactly two** new files:

```text
successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md
```

No existing file was altered. v2, v2.1, both author signatures, the
authorship note, both v2.1 reviews, the harness contract chain, the
batch-settlement amendment chain, the frozen/inactive implementation, its
tests, and every unrelated dirty or untracked file are preserved
byte-unmodified. Nothing was committed or staged.

I created no code, process, supervisor, controller, worker, watchdog,
bootstrap adapter, endpoint, pipe, FIFO, journal instance, tombstone,
spawn intent, lease, capability, operation, output bound, framed
transport, promoted object, capacity artifact, custody disposition,
entropy, T activation, scientific datum, Q attempt, Q/C artifact,
candidate, learner, world, E1/E2/E3 spend, or outcome. I started no
process, ran no test, executed no probe or smoke command, and issued no
Officina command. I authorized no implementation and no signature token,
and I predicted no qualification and no C1–C6 outcome. Process
invalidity, resource exhaustion, and missing evidence remain
infrastructure facts and are nowhere treated as scientific evidence.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
