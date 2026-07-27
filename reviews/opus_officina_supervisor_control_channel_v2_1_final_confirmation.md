REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1

# Opus 4.8 X-line: independent final check of Officina supervisor/control-channel v2.1

Date: 2026-07-27
Reviewer line: X (adversarial Linux / process / crash semantics)
Review base: commit `25854a2` (working tree dirty exactly as handed over;
nothing modified by this review).

**Independence.** I am Claude Opus 4.8, reviewing on a clean context. Per
`reviews/officina_supervisor_v2_1_authorship_note.md`, both
`…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md` and
`reviews/fable_officina_supervisor_control_channel_v2_1_closure.md` were
written by Claude Code Opus 5; the internal "Fable 5" heading and the
`fable_` filename are template residue. I have treated that closure as an
**authored self-assessment of the correction**, not as review evidence,
and re-derived every disposition from the v2.1 bytes. I also do not
inherit the v2 X-line review's authority: `bc731d96…` is cited by the
capacity signature and its findings are re-tested here from the text.

Artifacts read (hashes recomputed):

```text
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
82ae6cdc5c3ebe6fc91ad44fafc536bcfc70bef7fb81e2e4eb8ec7a1dfad1aca  reviews/fable_officina_supervisor_control_channel_v2_1_closure.md
bc731d96d13c8bc6741a94d320ed51ae35cfcbdc38417fedee3ddf3684cec9b2  reviews/opus_officina_supervisor_control_channel_v2_review.md
edfbef915246080a6e022ec5e95e177603c83e542f4068dc1f3ad8d367fcf591  reviews/sol_officina_supervisor_control_channel_v2_review.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
9db9f263ebcf705c2e8b5486bc6673104f94f6d8b59fd764e92bd946e5245168  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
```

Also read in full: the output-capacity selection signature, the
generic-harness signature, the signed composite (harness v2 + v2.1/v2.2/
v2.3/v2.3.1), the batch-settlement amendment chain, the activation
protocol's §B archival/clean-HEAD rules, and — read-only — the
uncommitted `generic_harness.py`, its tests, `ledger.py`, and
`verification.py`.

**Method.** Static and read-only. No process, test, supervisor,
controller, worker, watchdog, pipe, FIFO, journal, endpoint, or smoke was
started; no probe script was executed. Two implementability facts are
cited from source rather than from execution:
`AppendOnlyLedger` sets `head_sha256` to the last entry's `entry_sha256`
(`src/philosophia/officina/ledger.py:146`), and
`ALLOWED_ABSOLUTE_IMPORTS` contains `os`/`fcntl`/`subprocess`/`time`/
`hashlib` but not `select`/`selectors`/`signal`/`ctypes`
(`src/philosophia/officina/verification.py:35-39`). Kernel semantics
(`/proc/<pid>/cmdline` after `fork` without `exec`; `flock` on a
fork-shared open file description; CPython's startup `SIG_IGN` for
`SIGPIPE` and its inheritance across `exec`) are stated as documented
behavior, not as probe results.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1
```

v2.1 is a substantial and largely successful correction. Of my six v2
Criticals, four are genuinely closed and two are closed in substance with
residue; ten of eleven Majors and all seven Minors are closed; §W6.5 is
exactly the explicit supersession I asked for; and the K1 write-path
architecture closes the output-work cascade **at the source** rather than
by mitigation, which is better than the `statvfs`-plus-chunking repair I
proposed. The two-level `intent_scope` + `occurrence_index` identity is
also strictly better than the `SHA-256(command, arguments)` derivation I
recommended, which would have collapsed successive heartbeats.

But the correction is not yet executable. Five **Critical** and eight
**Major** defects remain. Three of them sit inside the repairs themselves:
the `spawn_intent_id` that closes my X-C2 is **circularly defined and
cannot be computed** (X21-C1); the `/proc` marker that discovers a
half-initialized supervisor **cannot exist**, because v2.1's own §W2.1
removed the `exec` that would create it (X21-C2); and the watchdog lease
table has **lost its renewal-publication trigger**, so an ordinary
heartbeating process is frozen at a stale deadline and, by §W3.4's own
single route, that freeze is necessarily a fabricated invalidity
(X21-C3).

All repairs below are mechanical against v2.1's own text. **No repair
reopens A3, B1, C1, D1, or K1**, and none needs a new author cell.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **not signable**.

---

## Critical findings

### X21-C1 — `spawn_intent_id` is circularly defined; the X-C2 repair cannot be computed

§W2.3 fixes the derivation:

```text
spawn_intent_id = SHA-256({supervisor_generation_sha256, role,
                           process_sequence, argv_sha256, created_utc})
```

and fixes the intent's `argv` key as "the complete argv **including the
appended supervisor tokens**", with §W2.4 repeating: "`argv` and
`argv_sha256` in the intent are over the **complete** argv." The appended
tokens are `--officina-spawn-intent <spawn_intent_id_hex>` (§W2.4).

So `argv_sha256` contains `spawn_intent_id`, and `spawn_intent_id` is a
function of `argv_sha256`. The definition is unsatisfiable — no
implementation can produce a conforming intent. v2 had explicitly avoided
this ("compute id from `{generation, role, argv_sha256, created_utc}`
once … without the id field circularity", §V2.1.4); v2.1 reintroduced it
by folding the marker into the hashed argv.

A second, independent defect on the same key: the appended
`--officina-ctrl-fds <req_write_fd>,<rep_read_fd>` embeds **generation-local
descriptor numbers** in the hashed argv. Two §W1.5 reducer rows then
become inexecutable — `CLAIM`: "intent + live child, no claim ⇒ … spawn
afresh **under the same intent**", and `OPERATION_ADMIT`: "a live unbound
worker is killed and respawned **under the same intent**" — because a new
generation's pipes will not land on the recorded fd numbers, so the
recorded argv cannot be reproduced without changing the intent id.

**Minimal repair.** Hash only the client-supplied prefix:
`argv_prefix_sha256` over the `CLAIM` argv (or, for a worker, the fixed
worker argv) **excluding both appended token pairs**;
`spawn_intent_id = SHA-256({supervisor_generation_sha256, role,
process_sequence, argv_prefix_sha256, created_utc})`; the intent records
`argv_prefix` and `argv_prefix_sha256`; the complete argv is a derived
function of the prefix plus the two token pairs. Pin the control
descriptors to fixed numbers via `dup2` (e.g. 3 and 4) so the completed
argv is generation-stable, and keep `complete_argv_sha256` — already a
`CLAIM` `effect_plan` key in §W1.4 — as the separate record of what was
actually executed.

### X21-C2 — the `spawning_id` marker cannot exist in the grandchild's `cmdline`; a hung grandchild wedges the singleton permanently

§W2.1 makes the supervisor grandchild and the watchdog **in-process
post-fork** entries: "the grandchild **calls the serve function
in-process** (no `exec`, no new argv)". On Linux, `/proc/<pid>/cmdline`
reads the argv memory region established by the last `exec`; a process
that only `fork`s shows its parent's argv. Rewriting it from Python
requires `ctypes`/`setproctitle`, both outside
`ALLOWED_ABSOLUTE_IMPORTS`.

Therefore the grandchild's `cmdline` is the CLI's own
(`python -m philosophia.officina.generic_harness claim …`) and **can never
contain `spawning_id`**. Every rule that depends on it is inexecutable:

- §W2.2: "On timeout it kills the grandchild by the `spawning_id` marker
  (§W2.4)";
- §W2.4: "The same predicate, with `spawning_id`, discovers a
  half-initialized supervisor grandchild";
- §W2.9 phase 1 step 2: "identity-kill every discoverable stale child and
  **grandchild** by the §W2.4 predicate";
- §W8 row 1: "next `SPAWN.lock` holder finds no live grandchild by the
  `spawning_id` marker".

The consequence is not merely a missing kill. §W2.2 deliberately has the
grandchild **retain** the `SPAWN.lock` fd until its identity is installed,
and §W8 row 2 makes a second CLI "block on the lock". So a grandchild that
hangs anywhere before identity install — most plausibly in §W2.2's own
"awaits the watchdog's first ack", which has no timeout — holds the
singleton lock forever while being undiscoverable and unkillable, and
every subsequent CLI blocks indefinitely. The contract offers no operator
route out (§W2.9 phase 1 never runs, because it runs *under* the lock).
This is the one place where v2.1 is strictly worse than v2, and it was
introduced by combining two otherwise-correct repairs (X-M1 and X-M6).

**Minimal repair.** Make the grandchild self-record instead of
self-advertise: immediately after the second `fork`, **before** creating
endpoints, forking the watchdog, or awaiting any ack, the grandchild
installs `T_SUPERVISOR/SPAWNING_CHILD.json` (atomic no-replace; keys
`schema, scientific_outcome, spawning_id, supervisor_pid,
supervisor_start_identity, boot_identity, created_utc`). Discovery of a
half-initialized grandchild reads that record and kills by recorded
pid + start identity — never by `cmdline`. Add a bounded timeout to the
watchdog first-ack wait inside the grandchild (reuse
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`), on expiry exit without serving. Have
the CLI take `SPAWN.lock` with `LOCK_EX|LOCK_NB` plus a bounded retry so
no client blocks forever, with `REFUSED`/`BOOTSTRAP` on expiry. The
`/proc` marker predicate remains correct and should be retained **only**
for the `exec`ing children (controller and worker), where it works.

### X21-C3 — the watchdog lease table has no renewal-publication trigger, so a compliant heartbeat produces a fabricated invalidity

§W0 replaces §V2.6.3 — which carried "Supervisor, after every locked
renew/remove/claim-start, atomically replaces `WATCHDOG/LEASES.json` …
and writes the same payload on the update pipe" — with §W3.2. §W3.2
states publication only "**before** the first `SIGCONT`, before any
capability becomes usable, and before any operation admission". The word
"renewal" survives in exactly one sentence — "On renewal the old deadline
remains authoritative until the successor table is acked" — which
presupposes a publication that no longer has any stated trigger.
`LEASES.json` appears nowhere else in v2.1 except the §W7 row.

The §W1.4 `effect_plan` key lists are "keys exactly", and the `HEARTBEAT`
row has **no** `watchdog_table_seq`, while the `START` row does. So an
implementer cannot bind the successor table to a heartbeat even if they
infer the intent, and §W1.5's reducer — whose `START` row correctly says
"publish+await the missing ack" — has no corresponding step for
`HEARTBEAT`.

The result is not a benign fail-closed gap. The watchdog keeps freezing
against the table it last acked, i.e. the **original** deadline. A
process that heartbeats correctly every 30 s is frozen at its first
deadline; §W3.4 then gives that freeze exactly one route — record-first
live-process invalidity, cause `PROCESS`, all-live batch under §2c.12b,
with every sibling lease invalid-closed and the runtime parked in G5. The
contract as written converts the most-travelled healthy path into a
manufactured invalid ending, which is precisely the relabelling the signed
composite forbids.

**Minimal repair.** Restore the trigger in §W3.2 verbatim ("after every
successful locked renew, remove, or claim-start"), add
`watchdog_table_seq` to the `HEARTBEAT`, `CLOSE`, and `PAUSE`
`effect_plan` key lists, add the matching reducer probe/action rows, and
state that the successor lease's deadline governs only once its
`table_seq` is acked — refusing `HEARTBEAT` with the existing
`REFUSED`/`WATCHDOG_UNACKED` if the ack does not arrive within
`T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`, so the old deadline never silently
outlives a legitimate renewal.

### X21-C4 — no durable locator proves worker start; `ADMITTED` can be returned for a permanently stopped worker

§W4.4 orders step 8 `JOURNAL/<key>/reply.json` → `OK/{…, "ADMITTED", …}`
and step 9 `SIGCONT the worker`. §W1.5's reducer short-circuits before any
locator probe:

```text
if reply.json exists  → re-wrap effect_reply in a fresh envelope
```

and the `OPERATION_ADMIT` `effect_plan` (keys exactly: `operation_id,
pre_operation_reading_ns, capacity_path, bound_path, admission_path,
worker_spawn_intent_id, declared_stream_indexes`) contains **no locator
for step 9**. So a crash between 8 and 9 is single-valued in the wrong
direction: the worker stays `SIGSTOP`ped forever, `OPERATION_STATUS`
returns the fixed `PENDING` shape forever (§W5.1), `bytes_reserved` stays
charged against the 32 GiB envelope, and the only exit is the lease
deadline → watchdog freeze → invalidity. §W8 has no row for this cut, and
§W4.8 compounds it by naming a **signal** — "worker `SIGCONT`" — as the
*durable trigger* of `ADMITTED → RUNNING`, which is not a durable object
at all.

**Minimal repair.** Add `running_path` to the `OPERATION_ADMIT`
`effect_plan`; insert step 8a — `operations/<operation_id>/RUNNING.json`,
no-replace, under the lock, keys `schema, scientific_outcome,
operation_id, worker_pid, worker_start_identity, continued_utc` —
immediately **before** `SIGCONT`; make §W1.5's reply-exists branch probe
`running_path` before serving, completing step 9 when the recorded worker
is alive and stopped, or killing and respawning under the same intent
(the ADMIT probe row already carries that verb) when it is not. Replace
§W4.8's trigger cell with `RUNNING.json`.

### X21-C5 — client intent-slot GC contradicts allocation and permanently loses forward progress

§W1.1 allocates by enumerating `<intent_scope_sha256>.<n>.json` and taking
the highest `n`. §W7 authorizes deletion of exactly those files: the slot
is "Removed by: **the client** after its `.done.json`", and the terminal
marker is "Removed by: **the client**".

Take the sanctioned sequence: the client completes occurrence `n`, writes
`.done.json`, and removes `<scope>.<n>.json`. The next invocation
enumerates, finds a lower highest (or none), and allocates an index that
has already been used. That key's journal directory has been GC'd, so
§W1.7 answers `REFUSED`/`ALREADY_ACKNOWLEDGED` with `retryable = false`.
§W5.2 fixes the `REFUSED` detail to `token, retryable` **exactly**, so the
supervisor cannot return the high water; §W1.1 gives the client no other
way to learn it; and no client continuation is defined for
`ALREADY_ACKNOWLEDGED` anywhere in v2.1. The client re-allocates the same
index on every subsequent attempt. Deleting `.done.json` instead is no
better: the slot then looks unfinished, so every new intended heartbeat
becomes a retry returning the stale cached reply.

The same trap catches any client whose `T_CLIENT_INTENTS/` is simply
absent — it is untracked control plane under `runtime_control/`, outside
every archival set, and a fresh client starts at occurrence 1 against a
high water of 50. Because `HEARTBEAT`'s scope is one per process (its only
argument is `process_id`), the outcome is that the process can never
heartbeat again: deadline → freeze → invalidity.

**Minimal repair.** (a) §W1.1 step 1 must enumerate both
`<scope>.<n>.json` **and** `<scope>.<n>.done.json` and take the highest
`n` over the union; (b) §W7 must forbid removing the terminal marker of
the highest occurrence in a scope (removal of any lower pair is then
harmless); (c) add `high_water` to the `ALREADY_ACKNOWLEDGED` refusal
detail — a control integer, not an outcome — and pin the client rule
"on `ALREADY_ACKNOWLEDGED`, re-anchor to `high_water + 1` and retry
once". (c) is what makes a client with a lost slot directory recoverable
without probing.

---

## Major findings

**X21-M1 — the freeze observation has no supervisor acceptance
predicate.** §W3.3 correctly moves the write to the watchdog, and I
confirm this is **compatible with C1**: `WATCHDOG/**` is control plane,
the watchdog still holds no lock, no capability, writes nothing under
`runtime/`, and never appends the ledger, so it is a witness rather than a
second durable runtime authority. But the observation drives a signed
invalidity and a §4c charge, and no rule requires the supervisor to
validate it: nothing checks `supervisor_generation_sha256` against the
current generation, `table_seq` against the current table, `deadline_ns`
against the supervisor's own lease record, `pgid`/`start_identity` against
the claim, `freeze_ns ≥ deadline_ns`, or `unresolved_member_count`
consistency with `quiescence`; and §W3.5's "consumed under the lock" gives
no continuation for a mismatch. Under A3 a deliberate same-UID process can
also plant one — procedural, but the contract-following validation is
missing regardless. *Repair:* pin the acceptance predicate and make any
mismatch the `UNKNOWN`/unknowable route rather than an accepted timestamp.

**X21-M2 — stale-generation freeze observations collide on a no-replace
path.** `WATCHDOG/FREEZE/<process_id>.json` carries no generation or
`table_seq` in its **name**, is no-replace, and is removed only after the
settlement's archival commit (§W7). A previous generation's watchdog is
undiscoverable (X21-C2) and exits only via its own `getppid()`/EOF check,
so it can write an observation for a `process_id` the new supervisor has
already written — `EEXIST`, with no defined continuation. *Repair:* name
the file `<process_id>.<table_seq>.json`, require the writer to re-read
`SUPERVISOR_IDENTITY.json` and refuse on generation mismatch, and pin
consumption order by `(generation, table_seq)` with the earliest
authoritative.

**X21-M3 — `t-worker-status.v1` is again a named-but-undefined schema, and
one reachable transport cut has no row.** §W0 replaces §V2.7.3, which held
the only key list for the worker status frame; §W4.3/§W4.4 do not restate
it; §W7 lists the schema with no keys. Its v2 key `output_relative_paths`
is incoherent under K1, where the supervisor derives paths from frame
headers. This is the same defect class as X-C6, which §W9 marks closed.
Separately, §W4.5's cut table covers EOF-at-boundary with `COMPLETED` and
with `FAILED`, but **not** EOF at a frame boundary with **no status frame
at all** — a worker killed or crashed after clean output — which is
reachable and undefined. *Repair:* enumerate the keys (`schema,
scientific_outcome, operation_id, exit_reason`) and add the missing row
(⇒ `WORKER_FAILED` quarantine).

**X21-M4 — the `WATCHDOG` spawn-intent role is unsatisfiable.** §W2.3's
schema requires `argv` (nonempty, "the complete argv") and `argv_sha256`
for every role including `WATCHDOG`, but §W2.1 forks the watchdog
in-process with no argv, and no clause says where or when a watchdog
intent is written. *Repair:* drop `WATCHDOG` from the role enum — the
supervisor knows its watchdog by the `fork` return value plus §W2.1's
parent check — or define a distinct no-argv intent shape for it.

**X21-M5 — the tombstone's advance trigger is unspecified and two of its
disposition rows are not well-formed.** §W1.7 makes
`acknowledged_high_water_occurrence` load-bearing for GC eligibility and
for the `ALREADY_ACKNOWLEDGED` route, but never states when it advances or
how that write is ordered against `ack.json` (§W7 names the writer and the
lock, not the trigger). Rows 3 and 4 of its disposition table — "equal
recorded `last_effect_reply_sha256` scope" and "mismatching derivation" —
are not decidable predicates over an incoming frame, and they are the only
discriminator between a post-GC replay and a protocol error. *Repair:*
pin "the tombstone is replaced in the same lock epoch that installs
`ack.json`, to `max(current, that occurrence)`", and restate rows 3–4 as
`INTENT_KEY` (derivation mismatch) versus `ALREADY_ACKNOWLEDGED` (correct
derivation, `occurrence_index ≤ high_water`).

**X21-M6 — `PROCESS_TERMINAL` acknowledgement does not prove the reply was
observed.** §W1.6 writes `ack.json` with `ack_source = PROCESS_TERMINAL`
"when the owning process's final process record becomes durable, closing
every scope bound to that `process_id`". For `CLOSE` the final process
record **is** its own effect, so its reply is acknowledged at the instant
it is created — before any client could observe it. After the close
archival commit, §W1.7 then permits GC of that journal, and a client that
lost the `CLOSE` reply receives `ALREADY_ACKNOWLEDGED` with no reply bytes
and no route; the per-scope tombstone retains only
`last_effect_reply_sha256`, so nothing older is recoverable either. This
is the one place where B1's "identical replies remain redeliverable until
a durable acknowledgement records the one-use effect" is not delivered.
The `SUCCESSOR_OCCURRENCE` source, by contrast, **does** prove
observation for a contract-following client, because §W1.1 allocates
`n+1` only after `.done.json`, which is written on observing the terminal
reply. *Repair:* exclude the scope whose own effect produced the terminal
from `PROCESS_TERMINAL` acking, and require for those scopes either a
successor occurrence or the client's explicit
`acked_effect_reply_sha256_or_null` — a field the envelope already
carries.

**X21-M7 — §W6.2 over-claims TOCTOU detection.** It re-verifies `st_size`,
`st_ino`, and `st_nlink` from a held `O_WRONLY` descriptor and then
asserts that "a deliberate same-UID modification of `out/` between write
and settle **is detected** by this check". It is not: an equal-size
content substitution changes the promoted bytes and leaves all three
unchanged, so `result_sha256` — computed inline during the copy — no
longer describes the promoted tree. Under A3 the deliberate case is
exactly the one at issue. *Repair:* state the honest scope (size, inode,
and link count only) and either name equal-size substitution as A3
procedural residual or re-hash from a held `O_RDONLY` descriptor before
the settle step, which is bounded by the same 64 chunks.

**X21-M8 — the sole capacity-release artifact is under-specified.**
`<operation_id>.disposed.json` carries `author_disposition_sha256` — a
referenced hash with no schema name, no path, no key list, no
signature-verification rule, and no stated relation to §6c's signed
recovery-disposition class (for which the codebase already has
`validate_recovery_disposition`). `custody_absent: true` is asserted in
the record rather than proved by an enumeration under the lock. This is
the **only** path that can ever release the signed 32 GiB envelope, so it
is the one an adversary would forge. *Repair:* give the signed artifact a
schema, a path outside the control plane, an exact key list, the same
author-signature verification discipline as §6c, and require
`custody_absent` to be re-proved by a directory-fd enumeration in the same
lock epoch.

---

## Minor findings

1. `T_MIN_HEARTBEAT_INTERVAL_NS` is declared in the constants block and
   referenced nowhere in the document — a normative constant with no rule.
2. `T_ARGV_MAX_BYTES = 4096` equals `T_CONTROL_FRAME_MAX_BYTES`, but a
   `CLAIM` frame must also carry ~1 KiB of envelope (ten 64-hex fields, a
   ~160-byte `reply_fifo`, schema strings) plus JSON escaping. The two
   bounds are jointly unsatisfiable and the effective argv bound is left
   to the implementer. Fail-closed (`INVALID`/`FRAME_LENGTH`), but pin
   `T_ARGV_MAX_BYTES` strictly below the frame maximum minus the maximum
   envelope.
3. `--officina-ctrl-fds` is overloaded — controller `(req_write,
   rep_read)`, worker `(status_write, output_write)` — with no per-role
   order pinned in §W2.4/§W4.5.
4. §W4.2's serve preflight compares `st_dev` of the operations root with
   `runtime/T_PROMOTED`, which §W6.3 creates only "at first use"; compare
   against `runtime/` instead.
5. Zero-output completion (EOF at a frame boundary, `COMPLETED`, no
   frames) has no stated disposition — empty promotion with
   `result_sha256` over `[]`, or a failure class.
6. Two concurrent clients that collapse onto one occurrence (§W1.1 step 2)
   both write `<scope>.<n>.done.json` no-replace; the loser's `EEXIST` has
   no client continuation.
7. §W9 marks X-C2, X-C6, and X-M1 "closed" without qualification; after
   X21-C1/C2/M3 those rows should read "closed subject to" rather than
   closed, so the disposition table does not overstate the correction to
   the author.

---

## Prior X findings: exact disposition after re-testing

| v2 finding | Disposition in v2.1 | Evidence |
|---|---|---|
| X-C1 inverted B1 | **Closed in substance**, residue X21-C5/M5/M6 | §W1.2's semantic hash excludes generation and all four `client_*` fields; case 2 is a plain `INVALID` with "no ledger append, no G5"; the two-level identity correctly separates successive heartbeats from retries — better than my proposed `SHA-256(command, arguments)` |
| X-C2 pre-claim orphan / unbounded `waitpid` | **Not closed for the id; closed for the wait** | The marker mechanism is right for `exec`ing children but its id is uncomputable (X21-C1); §W2.5's `WNOHANG\|WUNTRACED` loop, `BOOTSTRAP` refusal, kill/reap route, and "no unbounded `waitpid` inside a lock epoch" fully close the second defect |
| X-C3 unreachable bound / reservation reserving nothing | **Closed, and better than proposed** | §W4.3 makes `OPERATION_ADMIT` the sole installer and removes `output_bound_sha256` from both the arguments and the `operation_id` preimage; K1's write-path mediation stops bytes in the data path, so the unbounded-work cascade cannot arise rather than being mitigated |
| X-C4.1–3 overrun route/cause/zero-branch | **Closed** | `T_PROCESS_RESOURCE_STOP` named forbidden with the correct reason; cause pinned to `PROCESS` with `CLOCK` only on an independently verified fault under §2a precedence; the zero-overrun branch deleted outright with no tolerance constant |
| X-C4.4 unestablishable `freeze_ns` | **Closed, residue X21-M1/M2** | Watchdog-written observation, `freeze_ns` sampled only at the proving pass, `null`+`UNKNOWN` on lost evidence, "re-derives by sampling" deleted |
| X-C5 dual-valued takeover | **Closed** | §W2.9's two phases; the CLI "writes no `runtime/` evidence, appends no ledger entry, performs no settlement"; §W2.9's generation states match |
| X-C6 durable-object contradictions / undefined schemas | **Closed except X21-M3** | Four immutable predecessor-bound phase files replace the mutated no-replace file; §W7 gives every object a path, schema, install mode, writer, lock, and removal actor; the child-dir rename is mandatory |
| X-M1 entry surface | **Closed — but see X21-C2** | Tokens deleted; in-process entry; `--officina-ctrl-fds` closes the undiscoverable-credential gap. The removal of `exec` is what invalidates the grandchild marker |
| X-M2 oversize frames | **Closed** | `promoted_relative_paths` removed from every reply; largest reply is a fixed token plus two hashes (Minor 2 aside) |
| X-M3 framing / `reply_fifo` | **Closed** | Newline framing, bounded per-endpoint buffer, canonical `REPLY/<hex(identity)>.<key>.fifo`, `ENXIO`/`EPIPE` dead-reader route with no re-apply |
| X-M4 escaped children | **Closed by honest re-scoping** | Moved out of the mechanical list; fail-closed quiescence scan over recorded members plus session/parent chain; unclassifiable ⇒ §4c(c)/§4d |
| X-M5 ack freshness | **Closed** | `ack_monotonic_ns` in the ack frame; liveness judged on the watchdog's own sample; `T_SUPERVISOR_POLL_INTERVAL_NS` added; one watchdog step serviced per chunk |
| X-M6 singleton lock | **Closed except X21-C2** | The retained fork-shared `flock` fd is correct Linux semantics; bounded CLI wait; collision loser exits writing nothing |
| X-M7 hash restart / TOCTOU | **Closed except X21-M7** | The false resume-from-offset claim is deleted; no post-exit hash pass exists at all under K1 |
| X-M8 rename `errno` | **Closed** | `st_dev` serve preflight so `EXDEV` cannot arise; `ENOENT`/`EEXIST`/`ENOTEMPTY` each routed; `T_PROMOTED` creation and mode pinned |
| X-M9(i) §5a traceability | **Closed** | §W6.5 names the sentence, supersedes it explicitly, and replaces it with a weaker true rule — exactly the repair requested |
| X-M9(ii) client-triggerable G5 | **Closed** | §W1.2 case 2 |
| X-M10 intent-id collision | **Closed** | `process_sequence` in the preimage and nanosecond `created_utc` (the preimage is still uncomputable for the separate reason in X21-C1) |
| X-M11 `ALREADY_DELIVERED` enum | **Closed** | Present in both §W5.2 and §W4.8 |
| X minors 1–7 | **All closed** | §W2.6 (no signal dispositions; capability invariant replacing the first-instruction claim), §W5.4 (exit status 3; `REPLY/` creation/mode/GC), §W7 (§3 durability for the control plane), §W5.3 (truthfulness qualifier), §W6.6 (untracked control paths) |

Two further confirmations worth recording, because both were checkable
against source rather than assumed. §W1.5's guard `head_ok :=
current_ledger_head ∈ {pre_ledger_head_sha256} ∪ {plan's declared event
hashes}` is **type-correct in this repository**: `head_sha256` is the last
entry's `entry_sha256` (`src/philosophia/officina/ledger.py:146`), so a
head equal to a declared event hash is exactly the "effect partially
applied" state and the guard admits precisely the resumable cuts. And
§W5.4's reliance on observing `EPIPE` rather than dying of `SIGPIPE` is
sound without the forbidden `signal` module, because CPython sets
`SIGPIPE` to `SIG_IGN` at interpreter startup.

## Answers to the three Opus questions in the v2.1 closure

**Q1 — Is the argv-marker plus `/proc/*/cmdline` discovery predicate,
combined with the retained `SPAWN.lock` fd, total over every crash cut
between `SPAWNING.json` and a durable claim, including a grandchild that
has forked its watchdog but not installed its identity, and a controller
that reaches `exec` after its supervisor has already died?**

**No — and the named grandchild cut is exactly where it fails.** For the
`exec`ing children the predicate is sound and the reasoning holds: the
`fork` has already happened, `Popen` `_exit`s on exec failure, the marker
is fixed in argv memory at `exec`, and it is unique per intent so PID
reuse cannot mis-target — so a controller that reaches `exec` after its
supervisor died self-stops, persists (its group was orphaned at `setsid`,
so the kernel sends no `SIGCONT`), and is found and killed by the next
takeover. That half is total, **conditional on X21-C1** making
`spawn_intent_id` computable at all. For the supervisor grandchild the
predicate is not merely incomplete but inexecutable: §W2.1 removed the
`exec` that would place the marker, so a grandchild that has forked its
watchdog and is waiting on its first ack is invisible, unkillable, and —
because §W2.2 has it retain the `SPAWN.lock` fd — holds the singleton
against every later CLI indefinitely (X21-C2). The watchdog inherits the
same invisibility (X21-M4, X21-M2).

**Q2 — Under §W3.2–§W3.4, is there any reachable schedule that yields a
freeze observation with `quiescence = PROVED` while a declared member or
backend stream is still runnable, or that leaves a lease past its deadline
with neither an observation nor the unknowable route?**

**For `PROVED`: not for anything the enumeration can reach; yes for a
detached descendant, and v2.1 says so honestly. For the second half:
yes.** `PROVED` requires every recorded member and every process whose
session id or parent chain reaches a recorded member to be absent, `T`, or
`Z` on a single pass, so a reachable runnable process cannot yield
`PROVED`. A doubly-detached descendant (its own `setsid`, reparented to
`init`, no chain back to a recorded member) is outside the enumeration by
construction; §W6.4 correctly relocates that to the A3 procedural residual
rather than claiming `killpg` covered it. Backend streams are a real gap
in a narrower sense: the predicate proves *process* quiescence only, and
§4d step 3's "synchronize every backend" remains the supervisor's
settlement obligation — since no off-CPU adapter is admitted here, that is
consistent, but §W3.3 should say that `quiescence = PROVED` is a
process-tree fact and not a backend fact. The second half is a plain yes,
by X21-C3: with no renewal-publication trigger the watchdog acts on a
stale table, so a renewed lease is frozen against a superseded deadline —
an observation exists, but it describes the wrong deadline and produces a
false `overrun_ns`, which §W3.4 then routes to a fabricated invalidity.
Under the charitable reading in which renewals do publish, the symmetric
gap remains: no rule says what happens when the old deadline passes while
the successor table is still unacked and the process is legitimately alive
under the new one.

**Q3 — Is the §W4.5 framed transport single-valued on real Linux at every
partial-read, EOF, `EPIPE`, full-pipe, and `ENOSPC` boundary, and does
closing the read end reliably stop a contract-following worker without the
supervisor itself ever taking `SIGPIPE`?**

**Almost — one reachable cut is missing, and the stop is reliable for a
different reason than stated.** The supervisor never writes to the output
pipe, so it cannot take `SIGPIPE` from this transport; that claim is
correct. Header-before-content framing with validation before creation,
the bounded header buffer, `≤ 4 MiB` per pass, the pre-write reservation
check, and the `ENOSPC`/`FILESYSTEM` route are each single-valued. The
missing cut is EOF at a frame boundary with **no status frame** (X21-M3).
On the stop: closing the read end gives `EPIPE` only on the worker's
*next* write — a worker already blocked in `write` is released
immediately, but a worker that never writes again is unaffected — and
because CPython sets `SIGPIPE` to `SIG_IGN` at startup and `SIG_IGN`
survives `exec`, a Python worker will observe `BrokenPipeError` rather
than die. Termination is therefore guaranteed by the `killpg` and proved
death that §W4.5 already requires, not by the close; the text should say
so rather than offering "`EPIPE`/`SIGPIPE`" as the terminating mechanism.

## Repair scope and author cells

**Bounded: yes.** All five Criticals and eight Majors are text repairs
inside this amendment: one hash preimage, one durable marker record and a
bounded wait, one restored publication trigger plus three `effect_plan`
keys, one durable locator file, one enumeration rule plus one refusal
detail field, one acceptance predicate, one filename component, two key
lists, one honest restatement, and one schema for an already-required
signed artifact.

**No repair reopens an author cell.** A3, B1, C1, D1, and K1 are untouched:
the K1 envelope constants do not move; the watchdog remains a freezer that
writes no `runtime/` byte and appends no ledger entry (X21-M1 adds
validation *by the supervisor*, which strengthens C1 rather than altering
it); B1's two-level identity stays, with X21-C5/M5/M6 repairing its
allocation, GC, and acknowledgement rules rather than its policy; D1's
no-idle-exit and A3's procedural residual are unchanged. No new numeric
policy value, provider, host change, command, or import is introduced by
any repair — `high_water` in a refusal detail is a control integer, and
the `RUNNING.json`/`SPAWNING_CHILD.json` locators are control-plane
objects of the kind §W7 already governs.

I recommend one further bounded correction pass over §W1.1, §W1.6–§W1.7,
§W2.1–§W2.4, §W3.2–§W3.3, §W4.4–§W4.5, §W4.6, §W6.2, §W7, §W8, and §W9,
followed by one final bounded X/Y confirmation. **No token becomes
eligible from this review**;
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains not
signable.

## Contract versus implementation

Every finding above is a defect of the v2.1 **contract**. The uncommitted
implementation neither causes nor cures any of them and is unchanged from
the state both v2 reviews recorded: `generic_harness.py` contains no
supervisor, control channel, FIFO, journal, operations tree, watchdog,
capacity ledger, or output transport; `SubprocessProcessOps`
(`src/philosophia/officina/generic_harness.py:407`) is the only process
primitive, and `run_isolated_operation`
(`src/philosophia/officina/generic_harness.py:2285`) still runs a
caller-supplied callback in the harness interpreter. Codex's C1–C4 /
M1–M6 therefore stand unchanged as implementation findings, and the four
Cursor files remain uncommittable. The implementability facts v2.1 relies
on hold: `os.fork`, `os.pipe2`, `os.open` with `dir_fd`, `os.statvfs`,
`os.killpg`, `os.waitpid`, `flock`, `subprocess` with
`start_new_session`, `time.clock_gettime_ns`, and `hashlib` are inside the
pinned allowlist with **zero delta**, while `select`, `selectors`,
`signal`, and `ctypes` are outside it — which is what makes the
`time`-paced poll necessary and what makes X21-C2 unavoidable rather than
an implementation shortcut.

## Custody confirmation

No code, test, contract, signature, prior review, or runtime artifact was
edited. No Officina supervisor, controller, worker, watchdog, pipe, FIFO,
journal, endpoint, operation, capacity artifact, promoted object, test, or
smoke was started; no probe script was executed; this review created no
process of its own. Nothing was committed or staged. Exactly one new file
was created — this review. The dirty Cursor files and every unrelated
dirty or untracked file are preserved unmodified.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent. No capability, claim,
lease, batch, operation, entropy, E1/E2/E3 spend, world, learner,
candidate, Q/C object, datum, or outcome exists. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
