REVISE_OFFICINA_SUPERVISOR_V2_1_1

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.1

Date: 2026-07-30
Reviewer line: X (adversarial Linux / process / crash / hash-construction semantics)
Review base: commit `30e0210` (HEAD), which is at or after `9a60ca5`. Working
tree dirty exactly as handed over; **nothing modified by this review**.

**Independence.** I am Claude Opus 4.8 on a clean context. Per
`reviews/officina_supervisor_v2_1_authorship_note.md` and v2.1.1's own header,
v2.1.1 was authored by **Claude Code Opus 5 in the specification-author role**
while Fable 5 was unavailable. Shared model-family identity is **not** review
continuity: I re-derived every disposition from the v2.1.1 bytes. I read
`reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md` **only as
an untrusted authored self-assessment** and used none of its claims as
evidence. I also did not inherit my own v2.1 X-line authority: the X21 findings
below are re-stated from the v2.1 bytes and each disposition is re-tested
against the v2.1.1 text.

## Recomputed hashes (all verified equal to the committed / cited values)

```text
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md   (== expected)
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

The v2.1.1 hash matches the expected committed value **exactly**. Every review
file v2.1.1 cites is byte-identical to what it cites, so the review base is
precise: v2.1.1 dispositions the two v2.1 final confirmations whose hashes it
records, and those are the files I hold.

**Method.** Static and read-only. No process, test, supervisor, controller,
worker, watchdog, adapter, pipe, FIFO, journal, endpoint, or smoke was started;
no probe was executed. Implementability facts are cited from source:
`ALLOWED_ABSOLUTE_IMPORTS` = `{__future__, ast, dataclasses, datetime, enum,
fcntl, hashlib, hmac, json, os, pathlib, re, subprocess, time, typing,
weakref}` (`src/philosophia/officina/verification.py:35-38`) — so every
primitive v2.1.1 §Z13 names (`os.dup2`, `os.execv`, `os.pread`, `os.listdir`,
`os.open(dir_fd=…)`, `os.fork`, `os.pipe2`, `fcntl.flock`, `subprocess.Popen`,
`time.clock_gettime_ns`, `hashlib`, `json`, `re`, `pathlib`, `enum`,
`dataclasses`) is inside the allowlist, and `select`/`selectors`/`signal`/
`ctypes`/`sys` are outside it, with **zero delta**. Kernel facts
(`/proc/<pid>/cmdline` shows the last-`exec` argv; `flock` on a fork-shared
open file description; CPython's startup `SIGPIPE`→`SIG_IGN` surviving `exec`)
are stated as documented behavior, not probe results.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_V2_1_1
```

v2.1.1 is a strong, near-total correction. It genuinely closes **all five**
X21 Criticals, **all eight** X21 Majors, **all seven** Minors, and the parallel
Sol C1–C5 / M1–M3 set, with exact, executable, non-circular text in every case
I could refute — **except one**. The repair that closes X21-M8 / Sol M1 (the
capacity-release authority) reintroduces, in a different place, the **exact
defect class** the document eliminates for spawn in §Z3.1: the sole
capacity-release authority's identifier is defined as a **circular SHA-256
fixed point** and cannot be constructed (**X211-C1**, new). Because the required
question forbids "a repair introducing a new defect" and demands "exact,
executable, non-circular text," and because an uncomputable release authority
also fails Sol M1's requirement that the authority be an *executable closed
contract*, the answer to the required question is **no** and the token remains
unavailable.

This is a single, bounded, mechanical defect in §Z6.4 / §Z6.5. Its repair
reopens no author cell and needs no new author choice. Everything else in
v2.1.1 stands on re-derivation.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT   — NOT signable
```

---

## New findings (ordered)

### X211-C1 (Critical) — the custody-disposition id is a circular SHA-256 fixed point; the sole capacity-release authority is not constructible

**Locus.** §Z6.4 (lines 1201–1246) and §Z6.5 conjuncts 2 and 8 (lines
1257–1274).

**The loop.** Three clauses are jointly unsatisfiable:

1. `disposition_id = SHA-256(canonical {activation_record_sha256,
   operation_id, author_decision_sha256})` (§Z6.4);
2. `author_decision_sha256` is "the file's SHA-256" of the author signature
   file (§Z6.5 conjunct 8: "the file's SHA-256 equals `author_decision_sha256`");
3. that same signature file "contains, each as an exact standalone line, the
   `author_token`, the `operation_id`, and **the `disposition_id`**" (§Z6.4;
   re-required by §Z6.5 conjunct 8).

From (3), the signature bytes are a function of `disposition_id`. From (2),
`author_decision_sha256 = SHA-256(bytes(disposition_id, …))`. From (1),
`disposition_id = SHA-256(…, SHA-256(bytes(disposition_id, …)))`, i.e.
`disposition_id = G(disposition_id)` for a SHA-256-derived `G`. Producing such
a fixed point is exactly the preimage/fixed-point search SHA-256 is designed to
make infeasible. No author — not even Kirill with full authority — can write a
signature file whose hash feeds an id that the file must already contain. The
`<disposition_id>.json` object cannot be named, either, since its filename
**is** `disposition_id` (§Z6.4 path grammar; §Z6.5 conjunct 2 "equals the
filename stem").

**Failure scenario (concrete).** Any T run reaches its first custody
disposition. Under §Z6.1 every admitted/quarantined/promoted operation retains
`bytes_reserved` (the full 268,435,456-byte ceiling for a custody directory
with no capacity record) until "an authorized disposition proves custody
absent." Because no authorized disposition can be constructed, **capacity is
never released**. Aggregate custody rises monotonically to
`T_OUTPUT_AGGREGATE_MAX_BYTES` (32 GiB), after which every `OPERATION_ADMIT`
is refused `NO_CAPACITY` with no recovery: raising the ceiling is forbidden
here and the supervisor can never raise it (§Z6.6). The one path K1 designates
for release is dead.

**Why this is the prohibited class, not a safe fail-closed.** It is fail-closed
against *false* release, but it is not "closed" in Sol M1's sense — Sol M1
required "one immutable canonical author-disposition object … and a fail-closed
verifier," i.e. an authority that *can be exercised by the author and refused
otherwise*. An authority that can never be exercised is broken in the opposite
direction and defeats the closure. It is also precisely the "circularly
defined … cannot be computed" defect I raised as X21-C1 and that §Z3.1 claims
to have removed "by construction"; the document reintroduced it in the K1
authority while removing it from spawn.

**Smallest bounded repair (no new author cell).** Break the loop by removing
`disposition_id` from the signature file's required content, keeping only the
two lines that already bind it — the `author_token` and the `operation_id`
(a signature naming the operation cannot be replayed onto another operation,
which is the only property the third line was meant to add). Equivalently, and
just as small: drop `author_decision_sha256` from the `disposition_id`
preimage — `disposition_id = SHA-256({activation_record_sha256, operation_id,
author_decision_path})` — and keep `author_decision_sha256` as a separately
verified field (§Z6.5 conjunct 8 still binds the file's hash). Either edit is
one clause, introduces no constant, import, provider, or author choice, and
leaves every other conjunct of §Z6.5 intact. This is the same shape of fix as
§Z3.1's `argv_template_sha256` split. The corrected clause must receive another
independent X/Y check.

### X211-m1 (Minor, observation) — CLIENT_ECHO of a stale-but-valid reply hash is `INVALID/REPLAY_BYTES`

**Locus.** §Z1.7 `CLIENT_ECHO` row (line 401). A frame whose
`acked_effect_reply_sha256_or_null = h` where `h` is a genuine prior reply hash
in the scope but **not** the highest unacknowledged occurrence's hash is
`INVALID/REPLAY_BYTES`. This is fail-closed and non-lossy — the reply stays
redeliverable via `RETRY(i)`, and a correct echo or `SUCCESSOR_OCCURRENCE`
still acknowledges — so B1 is not violated. But a legitimately confused
single-threaded client cannot always know which occurrence is "highest
unacknowledged," and an `INVALID` result (no `retryable`) reads more severe than
the situation warrants. *Optional* repair: treat an echo that equals *any*
recorded `effect_reply_sha256` at or above the acknowledged prefix as a no-op
acknowledgement of that specific occurrence rather than `INVALID`. Not a
blocker.

### X211-m2 (Minor, observation, inherited) — dead-watchdog freeze of non-overdue groups

**Locus.** §Z4.3 rule 3 invoking carried-forward §W3.5 row "Ack absent past
`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS`" (v2.1
`…V2_1_CORRECTION.md:831`). On watchdog death the supervisor "freezes all live
groups itself … then settles every overdue lease." v2.1.1 correctly pins that
settlement to "the supervisor's own **current** durable lease deadlines," so a
*renewed* lease is not settled at a stale deadline — that half is a real
improvement and closes the X21-C3 symmetric gap. What the inherited text still
does not state explicitly is whether a **non-overdue** healthy group, once
`SIGSTOP`ed during the watchdog swap, is `SIGCONT`ed after the replacement
watchdog acks, or is left to drift to its deadline and then be settled invalid.
Because a watchdog crash is a genuine infrastructure fault (legitimate process
invalidity, not a manufactured relabelling of a healthy heartbeat), this does
not rise to the X21-C3 class and it is **not introduced by v2.1.1**; both v2.1
reviews accepted §W3.5. I record it so the next pass can add one sentence
("non-overdue groups are `SIGCONT`ed once the replacement watchdog's first ack
is observed") and remove the ambiguity. Not a blocker for this verdict.

No other new Critical, Major, or Minor survived re-derivation.

---

## One-to-one disposition of the v2.1 findings

### X21 Criticals

| Finding | v2.1.1 locus | Verdict | Basis (re-derived) |
|---|---|---|---|
| **X21-C1** circular `spawn_intent_id`; two reducer rows inexecutable | §Z3.1, §Z3.2 | **CLOSED** | `argv_template_sha256` is over a template holding the literal placeholders `"<SPAWN_INTENT_ID>"`/`"<CTRL_FDS>"`, never a derived marker or descriptor number; `spawn_intent_id = SHA-256({generation, role, sequence, argv_template_sha256, created_utc})` is satisfiable and deterministic; `complete_argv_sha256` is a separate record. A re-`Popen` under the same intent in-generation reproduces the id with fresh descriptor numbers, so the two §W1.5 rows are executable (and cross-generation respawn is forbidden outright by §Z2.4). Genuinely non-circular. |
| **X21-C2** `/proc` marker cannot exist for the grandchild; hung grandchild wedges the singleton | §Z3.5, §Z3.6, §Z3.4 | **CLOSED** | The `spawning_id`-in-`cmdline` predicate is deleted for the grandchild/watchdog (they never `exec`); it is retained only for `exec`ing children at a fixed argv index (§Z3.4). The grandchild self-**records** (`SPAWNING_CHILD.json`) and reports pid/start/pgid over a sealed bootstrap pipe as its first actions; the first-ack wait is bounded (`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`); the CLI's `LOCK_EX\|LOCK_NB` acquire is bounded (`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`) with a stuck-holder route that kills by recorded identity. No pre-identity step has an unbounded wait. D1 cannot be wedged. |
| **X21-C3** watchdog lease table lost its renewal-publication trigger ⇒ manufactured invalidity | §Z4.1, §Z4.2, §Z4.3 | **CLOSED** | Publication trigger restored verbatim ("after **every** successful locked claim-start, renew, and remove"); `watchdog_table_seq` added to `HEARTBEAT`/`CLOSE`/`PAUSE` effect plans and to the reducer probe/action rows; drain-before-freeze (§Z4.3 rule 2) guarantees a renewed lease is evaluated against the newest acked table; ack-absence routes to the dead-watchdog path with a `WATCHDOG_UNACKED` terminal recording the durable charge. A process heartbeating every 30 s is never frozen or invalidated. |
| **X21-C4** no durable locator proves worker start; `ADMITTED` cacheable for a stopped worker | §Z5.1, §Z5.2 | **CLOSED** | `RUNNING.json` (release/start-attempt locator) is added to the `OPERATION_ADMIT` effect plan and written **before** `SIGCONT`; the reply is step 10, after. The reducer's `reply.json`-exists branch must probe `running_path` first. `ADMITTED` is cacheable only after a durable same-generation release locator; §W4.8's signal-as-trigger cell is replaced by `RUNNING.json`. After a loss the worker is settled, never resumed (§Z2.5). |
| **X21-C5** client intent-slot GC contradicts allocation; forward progress permanently lost | §Z1.1–§Z1.5, §Z1.8, §Z1.9 | **CLOSED** | Allocation is supervisor-authoritative from the never-deleted tombstone ∪ journal scan; client files are convenience-only and read by the supervisor nowhere. A client with an absent `T_CLIENT_INTENTS/` sends `NEW(1)`, is refused `OCCURRENCE_INDEX` carrying `next_occurrence_index`, and re-anchors in ≤ 2 round trips. `next_occurrence_index` is delivered in the reply envelope (§Z10.2), not squeezed into the closed `REFUSED` detail set. Permanent loss of forward progress is structurally impossible. |

### X21 Majors

| Finding | v2.1.1 locus | Verdict | Basis |
|---|---|---|---|
| **X21-M1** freeze observation has no supervisor acceptance predicate | §Z4.6 | **CLOSED** | Ten-conjunct acceptance predicate under the lock (schema/type/enum; `witness_id` recompute; current generation; `table_seq`/deadline agreement with the durable lease; pgid/start-identity vs the claim; killer consistency; PROVED/UNKNOWN field coherence; independent NOW-quiescence). Any malformed/missing/conflicting/unverifiable fact ⇒ **not evidence** ⇒ supervisor-written `UNKNOWN` witness ⇒ all-live invalid route. Never an accepted timestamp. |
| **X21-M2** stale-generation freeze observations collide on a no-replace path | §Z4.5 | **CLOSED** | `WATCHDOG/FREEZE/<witness_id>.json` with `witness_id = SHA-256({generation, process_id, table_seq})`; producer re-reads identity and refuses on generation mismatch; consumption ordered by `(generation==current desc, table_seq asc, process_id asc)`, earliest authoritative; a prior-generation witness fails §Z4.6 conjunct 3. Cross-generation `EEXIST` collision is impossible because the generation is in the name. |
| **X21-M3** `t-worker-status.v1` undefined; missing EOF-no-status-frame row | §Z7.1, §Z7.3 | **CLOSED** | Keys pinned exactly `{schema, scientific_outcome, operation_id, exit_reason∈{COMPLETED,FAILED}, frame_count, total_content_bytes}`; `output_relative_paths` not restored (never trusted under K1). The missing reachable cut "EOF at a boundary with **no** status frame" is added ⇒ `WORKER_FAILED` quarantine + signed record-first `PROCESS` invalidity. |
| **X21-M4** `WATCHDOG` spawn-intent role unsatisfiable | §Z3.2, §Z3.6 | **CLOSED** | `WATCHDOG` removed from the role enum (`{CONTROLLER, WORKER}`); the watchdog's identity is the argv-free `t-fork-child.v1` record (`WATCHDOG_CHILD.json`). No unsatisfiable nonempty-argv requirement survives. |
| **X21-M5** tombstone advance trigger unspecified; rows 3–4 undecidable | §Z1.9, §Z1.5 | **CLOSED** | `last_effect_reply_sha256` deleted; tombstone carries two monotone integers (`next_occurrence_index`, `acknowledged_prefix_occurrence`), each advanced in a named lock epoch (allocation resp. ack). §Z1.5's eight-row classification is decidable from the incoming frame plus those two integers — no unavailable old reply hash appears in any predicate. |
| **X21-M6** `PROCESS_TERMINAL` ack does not prove observation (`CLOSE` self-ack) | §Z1.7 | **CLOSED** | Own-terminal scopes (plan naming `process_record_path`/`stopped_event_sha256`/`pause_event_sha256`, incl. every `CLOSE`) are **excluded** from `PROCESS_TERMINAL`; they require `SUCCESSOR_OCCURRENCE` (carrying the exact prior hash) or the new `CLIENT_ECHO`. A lost `CLOSE` reply stays redeliverable. §W1.6's "closing every scope" is deleted. |
| **X21-M7** §W6.2 over-claims TOCTOU detection | §Z8.2, §Z8.3 | **CLOSED** | The false "is detected" claim is withdrawn; a bounded pre-settlement verification pass (one `O_RDONLY` re-open per file, `(st_dev,st_ino)` + `st_nlink==1` + size, whole-file re-hash in ≤ 64 chunks with a watchdog/control step between chunks) now **mechanically** detects equal-size content substitution and inode substitution. The remaining `out/`-directory-swap-by-name residual is named honestly as A3 procedural, not claimed closed. |
| **X21-M8** capacity-release artifact under-specified | §Z6.4, §Z6.5, §Z6.6 | **CLOSED IN INTENT, BLOCKED BY X211-C1** | The artifact now has a schema, a path outside the control plane, an exact key list, an author token/signature-file discipline, a twelve-conjunct fail-closed verifier, and a same-lock-epoch descriptor-safe custody-absence proof — this is the completeness X21-M8 asked for. **But** the `disposition_id` that names it is the circular fixed point of X211-C1, so the completed authority is not constructible. The M8 *specification gap* is closed; the M8 *executability requirement* is not, pending the X211-C1 one-clause fix. |

### Seven Minors

| # | Subject | v2.1.1 locus | Verdict |
|---|---|---|---|
| 1 | `T_MIN_HEARTBEAT_INTERVAL_NS` unused | §Z9.1 | **CLOSED** — a normative append-rate rule (`REFUSED/BUSY`, empty tuples, no charge, no ledger append); E1 arithmetic unchanged because charging is the cursor difference. |
| 2 | `T_ARGV_MAX_BYTES == T_CONTROL_FRAME_MAX_BYTES` jointly unsatisfiable | §Z9.2 | **CLOSED** — `T_ARGV_MAX_BYTES=768`, `T_ARGV_MAX_ELEMENTS=32`, printable-ASCII, with worst-case arithmetic shown (`CLAIM` args ≤ 2282 ≤ `T_ARGUMENTS_MAX_BYTES=2560`); frame check stays authoritative. Legal frames fit with margin. |
| 3 | `--officina-ctrl-fds` overloaded, no per-role order | §Z3.3, §Z9.3 | **CLOSED** — pinned: `CONTROLLER=(req-write, rep-read)`, `WORKER=(status-write, output-write)`, `dup2` to fds 3/4 in that order, verified `S_ISFIFO`, re-verified after `SIGCONT`. |
| 4 | §W4.2 preflight compares against lazily-created `T_PROMOTED` | §Z9.4 | **CLOSED** — compares `st_dev` against `successor/officina/runtime/` (an existing root holding `T_RUNTIME.lock`), so no lazy dir; `EXDEV` still cannot arise at promotion. |
| 5 | zero-output completion undefined | §Z7.3 | **CLOSED** — canonical empty result: `promoted_relative_paths=[]`, `result_sha256=SHA-256(b"[]")`, `actual_bytes=0`, capacity still retained at `bytes_reserved`; explicitly not an invalidity (would derive a route from an output property). |
| 6 | concurrent `.done` `EEXIST` no continuation | §Z1.8, §Z9.6 | **CLOSED** — structurally concurrent clients get distinct occurrences (§Z1.3), and the continuation is pinned anyway: equal hash ⇒ silent; different ⇒ exit 5, delete nothing (A3 procedural). |
| 7 | §W9 marks closures without "closed subject to" | §Z12.1 | **CLOSED** — every §W9 row is re-read as "closed in v2.1; confirmation pending independent v2.1.1 X/Y," with X-C2/X-C6/X-M1/X-M10 further qualified "subject to" the naming repairs; no closure asserted by author fiat. |

---

## The eight required attack traces

### 1. B1 occurrence semantics (allocation total, reuse-free, wedge-free)

Traced against §Z1.1–§Z1.10. **Concurrent `NEW`:** one wins step 2 under the
single `T_RUNTIME.lock`; the loser is `REFUSED/OCCURRENCE_INDEX` carrying
`next_occurrence_index` and re-anchors (§Z1.5 row 3) — no shared occurrence.
**Explicit `RETRY`:** never allocates, returns byte-identical cached
effect+token bytes (§Z1.1, §Z1.5 row 2). **Lost request (K1):** `NEW(i)`
re-sendable, allocates once. **Lost reply (K2):** the client knows the `i` it
chose, so `RETRY(i)` (or a same-identity `NEW(i)` via §Z1.5 row 2) returns the
cached effect — no second effect. **Client-state deletion:** convenience files
are never read by the supervisor; deletion costs only the client's own
re-addressing and forces at most a re-anchored `NEW(next)` (§Z1.4). **Reply
observed before `.done`, then crash (K3):** occurrence unacked; `RETRY(i)`
identical; a genuinely amnesiac client makes a *distinct* new occurrence — the
honest at-least-once-under-total-amnesia case B1 permits. **Generation change
(K4):** cached reply re-wrapped in the current generation; behavioral
cross-generation continuation forbidden (§Z2.4) ⇒ `SUPERSEDED_PLAN` or the
cached positive. **Successor ack with/without prior hash:**
`SUCCESSOR_OCCURRENCE` acks **only** when `n+1` carries the exact prior
`effect_reply_sha256`; otherwise it acks nothing (§Z1.7) — Sol C1.4 closed.
**Own-terminal `CLOSE`:** excluded from `PROCESS_TERMINAL`; bytes stay
redeliverable until `CLIENT_ECHO`/successor (X21-M6 closed). **Contiguous GC /
old retry after GC:** `acknowledged_prefix_occurrence` advances only over a
contiguous acked prefix in the ack's lock epoch; the tombstone is never
deleted, so a GC'd key ≤ prefix ⇒ `ALREADY_ACKNOWLEDGED`, and the impossible
band `prefix < i < next` with `D` absent ⇒ record-first invalidity (§Z1.5 rows
5,8). **Both STATUS forms:** observation form is journaled with an empty effect
tuple; `NEW` = new observation, `RETRY` = byte-stable across promotion and
delivery-ack (§Z1.6). Allocation is supervisor-authoritative, total, reuse-free
(the journal scan dominates the tombstone `max`), and wedge-free (≤ 64 unacked
per scope; growth bounded by scopes×64, not polling frequency). **Total.**

### 2. Reducer / takeover (validity-first)

Traced against §Z2.1–§Z2.5. A committed/replied plan followed by arbitrary
later ledger history is **accepted** as a verified descendant
(`in_chain`/`ordered`, §Z2.2) — the spurious-G5 equality guard is deleted (Sol
C2 closed). Every accepted-only prefix resumes at the first missing locator
(route B); a conflicting suffix with no locator ⇒ `SUPERSEDED_PLAN` (ordinary
later history, not invalidity); with a locator ⇒ record-first invalidity;
absent pre-head ⇒ record-first invalidity (routes A/C/D, §Z2.3). **Supervisor
death at each point:** §Z2.5 phase 2A proves/freezes old-generation process
state, writes supervisor freeze observations, and settles **every** affected
live stream through the signed all-live invalid route and drives the batch to
its signed terminal (ARCHIVE before RESOLVED) **before** any reducer step and
before serving; phase 2B does non-behavioral reducer work only. The
behavioral/non-behavioral partition (§Z2.4) makes it mechanical that across a
loss no reducer spawns, `SIGCONT`s, renews, admits, or installs a lease.
Validity-first dominance holds. **Total.**

### 3. Spawn / bootstrap

Template and complete-argv identities recomputed by hand from §Z3.1/§Z3.3: the
thirteen-element layout with placeholders at indices 7 and 9 makes
`argv_template_sha256` independent of both the derived marker and the
descriptor numbers, so `spawn_intent_id` is non-circular and stable across an
in-generation re-`Popen` (X21-C1 closed). Fixed fds (`dup2`→3/4) and per-role
order pinned (§Z3.3, minor 3). Every pre-identity cut is bounded: CLI
`LOCK_NB`+timeout; grandchild first-ack wait timeout; stuck-holder kill by
recorded pid/start/pgid; `SPAWNING_CHILD.json` written as the first action so
the holder is always discoverable (X21-C2 closed). PID/start/PGID death proof
by `/proc` absence or state `Z`; `os.waitpid` only for own-generation children.
Adapter self-stop precedes any target behavior; target preflight (`X_OK`) at
`CLAIM`, at serve, and re-checked at adapter step 4; the watchdog's separate
no-argv `t-fork-child.v1` record (§Z3.6) closes X21-M4/M2. **Constructible and
total.**

### 4. Watchdog

Publication on every claim-start/renew/remove restored (§Z4.1); ack of the
exact `table_seq` gates behavior. Drain-before-freeze (§Z4.3 rule 2) prevents
freezing a renewed lease at a superseded deadline; the old deadline is
authoritative until the successor is acked; ack absence ⇒ dead-watchdog route
against **current** deadlines with `WATCHDOG_UNACKED` recording the durable
charge (X21-C3 and Opus-Q2 symmetric gap closed — modulo the inherited,
non-blocking X211-m2 observation on non-overdue groups). Stale
tables/generations rejected by §Z4.5 ordering and §Z4.6 conjuncts 3–4. Witness
naming carries the generation (§Z4.5). The ten-conjunct acceptance predicate
(§Z4.6) rejects missing/contradictory/planted/stale evidence into the `UNKNOWN`
route; equality at the deadline is resolved by bounded strict-progress sampling
(§Z4.4), never a valid zero-overrun. The C1 boundary is explicit: the watchdog
holds no lock, no capability, writes nothing under `runtime/`, appends no
ledger, settles nothing; supervisor-side validation makes the supervisor the
sole authority. **No watchdog fact becomes a second runtime authority.**

### 5. Admission

Ten ordered steps (§Z5.1); `RUNNING.json` at step 7 before `SIGCONT` at 8, reply
at 10. Every cut before/after `RUNNING.json`, `SIGCONT`, `committed`, and a
cached `ADMITTED` is single-valued in §Z5.2: same-generation completes the
idempotent release then serves; post-loss freezes/settles and never resumes;
`reply.json` present with `RUNNING.json` absent ⇒ record-first invalidity
(impossible layout). Same-generation idempotence holds (locator-keyed); a
stopped worker can never sit behind a cached success in its own generation, and
after a loss it is settled, never resumed behind success (X21-C4 / Sol C4
closed). **Total.**

### 6. K1

Reserve → output → settlement → failure → quarantine → promotion → delivery ack
→ author disposition → release traced against §Z6.1–§Z6.7. `bytes_reserved`
remains the accounted contribution through `ADMITTED`/`RUNNING`/
`PENDING_SETTLEMENT`/`QUARANTINED`/`PROMOTED` and through every rename and
promotion; `actual_bytes` is diagnostic only and never enters `accounted_total`;
settlement, quarantine, rename, promotion, delivery ack, and unused reservation
release **nothing** (§Z6.7) — Sol C5 closed, K1 implemented literally. The five
signed `T_OUTPUT_*` constants are present and unmoved. Stale/substituted/
replayed/forged/partially-installed disposition objects each route to "refuse,
release nothing" (§Z6.6), and the same-lock descriptor-safe custody-absence
proof (§Z6.5 conjunct 10) blocks premature release. **However**, the *only*
release path is gated by the circular `disposition_id` of **X211-C1**, so no
valid disposition can be constructed and `bytes_reserved` can never be released
by any actor. The accounting is correct and fail-closed; the release authority
is uncomputable. **Not total — the single blocking defect.**

### 7. Output / A3

Worker status/EOF totality: §Z7.3 now decides zero-frame `COMPLETED` (canonical
empty result), status-frame absence (`WORKER_FAILED` + `PROCESS` invalidity),
`FAILED`, output-pipe-open-at-death (`TRANSPORT`), and cross-check mismatch
(`TRANSPORT`) — no reachable EOF cut is undefined (X21-M3 closed). Bounded
rehash and inode/content substitution are mechanically detected by the §Z8.3
verification pass; the directory-swap-by-name residual and all timing/metadata
leakage are stated as honest, non-citable A3 procedural residue (§Z8.1, §Z8.3
"Named residual") — every residual is procedural and non-citable, none
claimed away. **Honest and total.**

### 8. Exactness

Frame/argv arithmetic (§Z9.2) recomputed: envelope ≤ 1536, `CLAIM` arguments
≤ 2282 ≤ 2560, argv 768 ≪ 4096; frame check authoritative and fail-closed.
Schemas/enums/paths: request/reply envelopes (§Z10.1–§Z10.2), `ack_source`
(§Z10.4), the two added refusal tokens `OCCURRENCE_INDEX`/`SUPERSEDED_PLAN`
(§Z10.5), and the durable-object table (§Z10.7) are internally consistent and
close every enum. No-replace ownership and `EEXIST` continuations are pinned
(§Z1.3, §Z4.5, §Z5.2, §Z6.5 conjunct 11). Retention/GC is contiguous-prefix
only (§Z1.9). Target/interpreter preflight is `X_OK` at three points (§Z9.5).
Compatibility with the signed generic-harness (`…CONTRACT_V2_3_1…`) and
batch-settlement (`…AMENDMENT_V1_1_1…`) surfaces holds: the import allowlist
delta is **none** (verified against `verification.py`), no signed event/schema/
constant/root/archival set moves, and §W6.5's named §5a supersession is the
only protocol amendment. **Exact — with the one §Z6.4 arithmetic-of-hashes
exception (X211-C1).**

---

## No-regression table

| Signed cell / surface | Status under v2.1.1 | Evidence |
|---|---|---|
| **A3** same-UID procedural rescope | **Not reopened; strengthened only in honesty** | §Z8 states the timing/metadata/directory-swap residuals as procedural, non-citable T-facts; still not a security boundary; §Z6.6 states the disposition authority is mechanical-then-procedural, not cryptographic. |
| **B1** durable-journal ack redelivery | **Not reopened; allocation/ack/GC repaired, policy intact** | §Z1: journaled exactly-once effects and retry-stable replies preserved for all eight commands; only allocation, acknowledgement, and GC mechanics changed. |
| **C1** dedicated freezer | **Not reopened; single-authority shape strengthened** | §Z4.6 adds *supervisor-side* validation; the watchdog still holds no lock/capability, writes nothing under `runtime/`, appends no ledger, settles nothing. No watchdog fact promoted to a second runtime authority. |
| **D1** no idle exit | **Not reopened** | §Z3.5's bounded timeouts protect D1 from a bootstrap wedge; no idle-exit route added. |
| **K1** supervisor-mediated transport, fixed ceiling, no replenishment | **Not reopened; implemented literally — but the release authority is uncomputable (X211-C1)** | Five constants unmoved; §Z6 removes every replenishment; the one release path is defined but circular. The *policy* is untouched; the *mechanism* is blocked. |
| Signed generic-harness composite (v2/v2.1/v2.2/v2.3/v2.3.1) | **Unchanged** | No F1–F4/R1–R4 reopened; §D1 head/cache and inline `meter_evidence` inherited verbatim; import allowlist delta none. |
| Signed batch-settlement amendment (v1/v1.1/v1.1.1) | **Unchanged** | Two-token order, all-live invalid route, §2c/§4c/§4d referenced, not altered. |
| Signed nine events, schemas, roots, T bands, E1/E2/E3 | **Unchanged** | §Z13 negative space; no constant, event, root, or boundary moved. |

**Verdict on the required no-weakening conditions:** no fail-closed behavior is
weakened to obtain liveness (indeed X211-C1 is over-strong, blocking a
legitimate release); no watchdog fact is promoted to a second authority; no
signed author cell A3/B1/C1/D1/K1 is reopened.

## Is a new author cell genuinely required?

**No.** The single blocking defect (X211-C1) is a one-clause hash-construction
error in §Z6.4/§Z6.5; its fix (remove `disposition_id` from the signature
file's required lines, or remove `author_decision_sha256` from the
`disposition_id` preimage) introduces no new constant, import, provider, host
change, resource value, or author choice, and it realizes the *same* K1
authority Kirill already signed — exactly as §Z6 intends. The two Minor
observations need no author action. **No new author-choice token is required,
and none is unavoidable.**

## Authorization boundary

Because the verdict is **REVISE**, the informed author signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **unavailable**
and is not made signable by this review. This review authorizes **no**
implementation, no commit of the untracked/dirty implementation, no T
activation, no entropy, no runtime construction (supervisor, controller,
worker, watchdog, adapter, endpoint, pipe, FIFO, journal, spawn intent,
operation, capacity artifact, custody disposition, capability, lease, batch),
and no scientific work (world, learner, candidate, Q attempt, Q/C object, datum,
outcome, Proof, or claim movement). The smallest correction (the §Z6.4/§Z6.5
de-circularization, optionally the two Minor tidy-ups) must be prepared as a
bounded v2.1.2 layer and must receive **another independent X/Y check** on its
own bytes before any acceptance token can be considered; the author line cannot
confirm its own bytes.

## Contract versus implementation

Every finding above is a defect (or closure) of the v2.1.1 **contract**. The
implementation is unchanged from the state both v2 and my v2.1 review recorded:
`src/philosophia/officina/generic_harness.py` is **untracked** and contains no
supervisor, control channel, adapter, FIFO, journal, operations tree, watchdog,
capacity ledger, or output transport; `SubprocessProcessOps`
(`generic_harness.py:407`) is the only process primitive and
`run_isolated_operation` (`generic_harness.py:2285`) still runs a caller-supplied
callback in the harness interpreter; no `--officina-bootstrap` entry and no
`occurrence_mode` exist. The implementation neither causes nor cures any v2.1.1
contract finding.

## Custody confirmation

No process, test, probe, supervisor, controller, worker, watchdog, adapter,
pipe, FIFO, journal, endpoint, operation, capacity artifact, promoted object, or
smoke ran; this review started no process of its own. No code, test, contract,
signature, prior review, or runtime artifact was edited; nothing was committed
or staged; the dirty and untracked files handed over are preserved unmodified.
Exactly one new file was created — this review. No runtime or scientific
artifact was created. `successor/officina/runtime/` contains only
`T_RUNTIME.lock`; `successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. No capability,
claim, lease, batch, operation, entropy, E1/E2/E3 spend, world, learner,
candidate, Q/C object, datum, or outcome exists. **T remains `NOT_ACTIVATED`;
the programme claim remains `OPEN`.**
