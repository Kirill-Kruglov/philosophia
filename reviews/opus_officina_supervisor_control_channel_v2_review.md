REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2

# Opus X-line: Officina supervisor/control-channel v2 review

Date: 2026-07-27
Reviewer line: X (adversarial Linux / process / crash semantics)
Review base: commit `56173c7e880446cbc1b8f362a0d46ef7715500b1` (working
tree dirty exactly as handed over; nothing modified by this review).

Artifacts read (hashes recomputed here):

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9ab9ae65d7ddc98164118275dfbf84cc2e188202f606d4239a65abf2861d9f96  reviews/fable_officina_supervisor_control_channel_v2_closure.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
```

Also read: the v1 supervisor draft, the author-choice packet, both v1
X/Y confirmations, the Codex implementation review, the signed
generic-harness composite (v2 + v2.1/v2.2/v2.3/v2.3.1), the signed
batch-settlement amendment chain, the activation-protocol §B archival
correction, and — read-only, to separate paper design from
implementable contract — the uncommitted `generic_harness.py` and its
tests.

**Method note.** This pass was static and read-only. No process was
started, no probe script was executed, no FIFO/journal/endpoint was
created, and no file was written except this review. Where a Linux
semantic is load-bearing below I state it as a documented kernel/POSIX
semantic rather than as a probe result; the three probe facts I rely on
(`/proc` field-22 parse, `PIPE_BUF == 4096`, same-UID `chmod` defeat)
were established by the v1 X-line pass and the author-choice packet on
this host and are unchanged.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2
```

v2 is a large, real advance: the eight-command argument/detail tables,
the single promotion commit point, the reparented-zombie rules, the
archival exclusions, A3's honesty about mode bits, and the §S6 carry
are genuinely closed (list in §"Closed" below). But six **Critical**
and eleven **Major** defects remain, and they are not stylistic: as
written, the two headline selections do not execute. B1 turns the exact
lost-reply retry it was chosen to fix into a runtime invalidity (X-C1);
the operation surface cannot be entered at all because the output bound
is unreachable (X-C3); the pre-claim orphan gap that Opus F4 / Sol C4
opened is **still open** because the spawn-intent bytes contain no child
identity (X-C2); and C1's freeze does not have one exact continuation
(X-C4).

Every repair below is bounded and mechanical against v2's own text and
the already-signed composite. **No new author choice is required**, with
one conditional exception stated in §"Repair scope".

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **not signable**. A3/B1/C1/D1 are not reopened by anything here.

---

## Critical findings

### X-C1 — B1 is inverted: every real retry is `REPLAY_BYTES`, and that route is a client-triggerable G5

`successor/…V2_DRAFT.md:387-392` keys the journal decision on
`request_sha256` byte-identity: hit with **byte-identical**
`request_sha256` → cached reply; "same key, different bytes → `INVALID`
/ `REPLAY_BYTES` + record-first invalidity naming the journal path".

But `request_sha256` is the hash of the **whole frame**
(:300-325), which contains `supervisor_generation_sha256`,
`client_pid`, `client_start_identity`, `client_boot_identity`,
`client_monotonic_ns`, and `reply_fifo`. Every one of those changes on
a real retry:

- a CLI retry is a **new process** → new `client_pid` and
  `client_start_identity`, and necessarily a new `reply_fifo` if the
  path encodes identity;
- `client_monotonic_ns` is required to be non-decreasing (:311-313), so
  a retry cannot reuse the first value in general;
- after a takeover the client must send the **new**
  `supervisor_generation_sha256` or be refused `STALE_GENERATION`
  (:363) — so rule 4's "survives supervisor generations" (:394-395) is
  *unreachable*: a cross-generation retry always has different bytes.

Therefore the canonical Opus F1 / Sol C3 trace — `claim` commits, reply
is lost, user re-runs `claim` with the same `idempotency_key` — lands in
`INVALID`/`REPLAY_BYTES` **plus record-first invalidity**. Record-first
invalidity is signed §2c.12/§2c.13: it appends `T_RUNTIME_INVALID`,
invalid-closes every live sibling (§2c.12b), and parks the runtime in G5
until a signed recovery disposition exists. So B1's headline case
produces a worse outcome than v1's double-claim, and any same-UID
contract-following client that reuses a key by mistake can force G5 at
will.

The packet's own B1 wording is the fix and v2 dropped one word from it:
"same key + byte-identical **semantic** request".

**Minimal repair.** (a) Define `semantic_request_sha256` over exactly
`{command, arguments_sha256, process_id_or_null,
lease_sha256_or_null}` — excluding generation, all four `client_*`
fields, and `reply_fifo` — and make rules 1/2 key on it; keep
`request_sha256` solely as the reply binding of §V2.4.2. (b) Pin the
`idempotency_key` derivation (it is currently only "client-generated,
retry-stable", :310-311, with no rule, so two implementers' clients are
not interoperable): `idempotency_key = SHA-256(canonical
{command, arguments})`, which is automatically retry-stable and
recomputable by a fresh CLI process. (c) Demote key-reuse-with-different
semantics from record-first invalidity to the plain reply
`INVALID`/`REPLAY_BYTES` — a client protocol error must not be able to
drive global runtime state. This is textual and touches no signed event.

### X-C2 — the spawn intent carries no child identity, so F4/Sol C4 pre-claim discovery is still absent; and the claim path can block the supervisor forever

`:128-136` fixes the intent keys **exactly**:
`schema, scientific_outcome, supervisor_generation_sha256,
spawn_intent_id, role, argv_sha256, created_utc`. There is no
`controller_pid`, no `start_identity`, no session id — and not even
`argv`, only its hash.

`:157-158` nevertheless asserts "Crash after spawn intent + child,
before claim: takeover kills by registry identity (§V2.1.6)", and
`:186-190` says takeover, "For each recorded controller/worker/watchdog
identity: if start identity matches live PID, `killpg`/`kill`…". **No
such recorded identity exists for a pre-claim child.** The bridge Fable
claims is not in the bytes. Two further Linux facts make this worse
rather than benign:

- the child self-`SIGSTOP`s (:143-147) and is a session leader in its
  own new session (`start_new_session=True`). When the supervisor dies,
  the kernel's orphaned-process-group `SIGHUP`+`SIGCONT` wake-up
  (POSIX; Linux `kill_orphaned_pgrp` in `exit_notify`) is evaluated for
  the **exiting** process's group, and the child's group was already
  orphaned at `setsid` time rather than newly orphaned by the exit. So
  the stopped pre-claim child is neither continued nor reaped: it
  reparents to `init`/the nearest subreaper and stays in state `T`
  indefinitely, holding its inherited control-pipe ends open;
- it is invisible to every durable scan v2 defines, so §V2.11's
  "Child stopped, no claim | takeover kills by intent identity"
  (:671) has no executable meaning.

**A durable, race-free bridge does exist and v2 should pin it.** Embed
`spawn_intent_id` as a fixed argv element of the child (the intent is
durable *before* `fork`, and argv is fixed at `exec`), and define
takeover discovery as: for every `CHILDREN/<id>.json` without a
resolved claim, scan `/proc/*/cmdline` for a process whose NUL-split
argv contains that `spawn_intent_id`; kill it by group, prove death via
`/proc/<pid>/stat` absence or `Z`; then resolve the intent. This is
race-free in both directions: a child that has not yet `exec`ed will
still `exec` (the `fork` already happened; `Popen` `_exit`s the child on
exec failure), and the token is unique per intent so PID reuse cannot
mis-target. It needs no new schema key beyond adding the token to the
recorded argv, and no author choice.

**Second, independent defect on the same path.** `:149-150` requires
`os.waitpid(pid, WUNTRACED)` and `WIFSTOPPED`. `argv` is
**client-supplied** (:331) and the "reviewed adapter" property is not
mechanically checkable by the supervisor, so:

- an argv that never self-stops and never exits blocks `waitpid`
  **indefinitely** inside the claim transaction, i.e. inside a
  `T_RUNTIME.lock` epoch. There is no timeout, no watchdog coverage
  (no lease exists yet), and the whole runtime is wedged;
- if the child instead exits, `WIFSTOPPED` is false and v2 defines **no
  continuation** — the closed refusal enum (:363-365) has no
  bootstrap-failure token.

**Minimal repair.** Add one control-only constant (e.g.
`T_SPAWN_SELF_STOP_TIMEOUT_NS`), poll with
`os.waitpid(pid, WNOHANG|WUNTRACED)`, and on timeout-or-exit `SIGKILL`
the group, prove death, resolve the intent, and reply with one new
closed refusal token (e.g. `BOOTSTRAP`). Single-valued, bounded.

### X-C3 — the output bound is unreachable through any command path, and the "reservation" reserves nothing

Three separate blockers, all in `:499-522` and `:342-346`:

1. **No command installs `BOUND.json`.** The channel has exactly eight
   commands; none of them is a bound-install. `:345-346` requires the
   controller's `OPERATION_ADMIT` to carry `output_bound_sha256` = the
   hash of a bound "**already installed** for this admit intent", while
   §V2.3 gives the bound's owner as the **supervisor** (:273). So the
   controller must hash a supervisor-owned file that no reachable
   request can cause to exist. `OPERATION_ADMIT` is therefore
   total-refuse (`INVALID`/`BOUND`) and the entire operation surface —
   the only path to behavior — is dead.
2. **Direct self-contradiction on who supplies the value.**
   `:512-514` says `max_total_output_bytes` is "controller-supplied via
   the admit path **after** bound install", yet it is a key **of** the
   installed bound (:506-510), and the bound also contains a
   supervisor-chosen `created_utc` the controller cannot predict — so
   even given a bound-install command, the controller could not compute
   `output_bound_sha256` before the reply.
3. **`<pending_op_key>` is undefined** (:503-504) and inconsistent with
   §V2.3's `operations/<op>/BOUND.json` (:273) and with the post-admit
   `operations/<operation_id>/out/` (:555-556). No installation,
   migration, or removal rule exists for the pre-`operation_id`
   directory.

**Minimal repair (no ninth command, so B1's "eight commands" scope is
untouched).** Make `OPERATION_ADMIT` itself the bound installer:
`arguments` carry `max_total_output_bytes` and drop
`output_bound_sha256`; under the lock the supervisor derives and
installs `BOUND.json` at `operations/<operation_id>/BOUND.json` from the
admit arguments plus its own `created_utc` **before** any worker exists,
and returns `bound_sha256` in the `OK` detail. `operation_id` then binds
the bound's *content* fields (which it already does — `:548-552`
includes `max_total_output_bytes`), so `output_bound_sha256` must be
dropped from the `operation_id` preimage to remove the circularity.

**Fourth blocker — storage is named, not reserved.** `:517-521` records
`bytes_reserved = max_total_output_bytes` and then argues concurrency is
already `≤ MAX_CONCURRENT_LEASES`. That is arithmetic against nothing:
the bound is a **controller-declared positive int with no ceiling and no
comparison to real capacity**, and the controller is exactly the
adaptive party A3 declines to trust. A declared 2⁵⁰ produces, by v2's
own rules, up to 2⁵⁰ bytes of accepted output that the supervisor must
enumerate, `st_size`-sum, and **hash in full** (:534-541) before it may
refuse anything — and sparse counting (:537-538), correct as a bound
rule, does not help because the read still happens. The consequence
cascades into C1: while the supervisor is inside a multi-hour hash it
cannot service watchdog acks (X-M5), so live groups get frozen and, per
§V2.6.5, invalidated.

**Minimal repair.** (a) At admission, under the lock, refuse unless
`max_total_output_bytes + Σ(live reservations) ≤ os.statvfs(...)
f_bavail * f_frsize` measured on the operations filesystem — a real
fail-closed reservation with no new constant. (b) Require the
enumerate/hash/copy loop to be chunked with a mandatory
watchdog-ack-service step between chunks. Both are mechanical.

### X-C4 — C1's positive overrun has neither one cause, one disposition, nor an establishable freeze time

`:467-483` is the load-bearing validity pin, and it is three-way
under-determined.

1. **Disposition is not single-valued.** It forbids
   `T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_CLOSED`,
   `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE` — and is silent about
   the one signed valid disposition that was *designed* for an
   overrun: §2c.7 `T_PROCESS_RESOURCE_STOP`, "actual overrun recorded
   in full, never clipped". One implementer reads "must settle on the
   invalid/recovery route"; another reads the closed forbidden list and
   routes a cleanly-frozen overrun to the signed resource-stop close.
   Both are defensible from the text. *Repair:* name
   `T_PROCESS_RESOURCE_STOP` as forbidden for a watchdog-driven freeze
   (it is unreachable anyway — §2c.7 requires the cooperative
   quiesce→charge→record order, which a non-heartbeating controller
   cannot supply) and state that explicitly.
2. **Cause is not single-valued.** "`PROCESS` or `CLOCK` per §2a
   precedence" (:472-473) is not a resolution: §2a precedence
   (`HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE`) orders
   *simultaneous observed* causes, so applying it mechanically labels
   every scheduling overrun `CLOCK` and contaminates genuine
   clock-fault semantics. *Repair:* pin `PROCESS` as the sole cause of
   a positive watchdog overrun; `CLOCK` only when a monotonic anomaly
   is independently observed, in which case §2a precedence resolves the
   pair.
3. **The zero-overrun branch is unreachable, which makes the rule read
   as an invitation to invent a tolerance.** The watchdog acts only
   after observing `now_ns >= deadline_ns`, then verifies `/proc`
   identity, then `killpg`, and *then* samples `freeze_ns` (:447-452).
   `freeze_ns > deadline_ns` therefore holds by construction, so
   `overrun_ns > 0` always and ":481-483" ("Zero overrun … may still
   continue ordinary watchdog settlement") is dead text. An implementer
   wanting ordinary behavior will reintroduce a grace window — a
   tunable v2 does not authorize. *Repair:* delete the zero-overrun
   branch, or define an explicit control-only tolerance constant and
   compare `freeze_ns - deadline_ns` against it. Either is bounded;
   silence is not.
4. **The actual freeze time cannot be established when the event is
   lost.** `:464-465` says the supervisor "re-derives by sampling
   stopped/dead group vs durable deadline". A later sample cannot
   recover `freeze_ns`; it can only produce a larger number, and it
   does not say what to write into the hash-bound observation, whether
   `killer` becomes `SUPERVISOR`, or what bounds the error. Since
   `overrun_ns` drives the *validity* of a T process (point 1), the
   classification of a signed ending becomes a function of a lossy pipe
   read. Group quiescence has the same problem: the observation records
   `pgid` and nothing proves the sample was taken at freeze time.
   *Repair (preferred):* the watchdog writes
   `WATCHDOG/FREEZE/<process_id>.json` itself, atomically and
   no-replace, at sample time; the supervisor validates and consumes
   it. This keeps C1 intact — the watchdog still holds no lock, no
   capability, and writes nothing under `runtime/` or the ledger, and
   `WATCHDOG/**` is archival-excluded control plane. *Repair
   (fallback, if the author reads C1's "only runtime writer" as
   covering all durable objects):* a lost event is recorded as
   `freeze_ns = null` with a fixed `FREEZE_TIME_UNKNOWN` marker and
   routes unconditionally to invalidity with the §4c(c)/§4d unknown
   pool — fail-closed and single-valued.

### X-C5 — takeover authority is dual-valued, and one reading makes a CLI client a runtime writer

`:184-196` places the whole of takeover "Under `SPAWN.lock`, **before a
new supervisor serves**" and ends "Then spawn." The lock holder at that
moment is the **CLI client** (:99-102). But takeover includes "Settle
affected streams per §4c/§4d and honor unresolved batch + journal"
(:194-195) — ledger appends, invalidity records, charges — i.e. exactly
the runtime writing that §V2.1.1 forbids clients ("clients never take
the lock, never write `runtime/` evidence, and never hold a capability
object", :76-77) and that the signed composite reserves to the
supervisor (harness §1 ownership pins). §V2.9.1 contradicts §V2.1.6 by
listing `TAKEOVER` as a **supervisor generation state**
(`LIVE → TAKEOVER → LIVE`, :625-626).

**Minimal repair.** Split takeover explicitly: (i) client phase, under
`SPAWN.lock`, control-plane only — load intents/claims/leases/journal
*read-only*, identity-kill by the X-C2 bridge, prove death, unlink only
stale control endpoints; then double-fork. (ii) supervisor phase, by the
new generation as its first action, under `T_RUNTIME.lock`, before any
admission — journal replay, §4c/§4d settlement, unresolved batch. Then
§V2.9.1's `TAKEOVER` state and §V2.1.1's sole-writer invariant agree.

### X-C6 — the durable-object rules contradict themselves, and four named schemas do not exist

`:260-263` imposes "atomic no-replace **unless noted**" globally. The
objects whose whole purpose is a phase change are not noted:

- `JOURNAL/<key>.json` is written three times — `ACCEPTED`, then
  `COMMITTED`, then `REPLY_CACHED` (:391-393) — at one path, with one
  `phase` key (:383), under no-replace. The second write must fail.
  *Repair:* either mark the journal entry replace-with-monotone-phase
  (with the §3 temp-write → `fsync` → `os.replace` → dir-`fsync`
  discipline named explicitly), or — better for crash cuts — split it
  into three no-replace files (`.accepted.json`, `.committed.json`,
  `.reply.json`) and define `phase` as the highest present file. Pick
  one.
- The operation state ladder `ADMITTED → RUNNING → PENDING_SETTLEMENT →
  PROMOTED|FAILED` (:637) is asserted with no object to carry it, and
  `:543-544` speaks of a "`phase=FAILED` journal/admission **update**"
  against the same no-replace rule.

Named-but-undefined schemas (§V2.3 lists them; nothing enumerates
keys):

- `t-operation-admission.v1` (`OPERATION.json`, :274) — no keys, though
  spawn is gated on its durability (:521-522);
- `t-request-ack.v1` (:270) — no keys, **and** §V2.5.6 offers it "**or**
  a dedicated `delivery_ack`" (:399-403): two mechanisms, one of them
  keyed by `idempotency_key` and the other by `operation_id`, which is
  not single-valued and is the one object the one-use release effect
  hangs on;
- the `FAILED`/quarantine record (:543-544, :676-677, and §V2.11's
  repeated "quarantine") — no path, no schema, no owner, no retention,
  no disposal binding to §6c;
- the spawn-registry successor `CHILDREN/<process_id>/` is introduced as
  an "**optional** rename … (atomic)" (:155-156) — optional means two
  legal on-disk layouts and two takeover scans.

Also unresolved at the object level: §V2.11's first cut is
"delete/**refuse** intent" (:670) — two different verbs for one cut —
and no retention/removal *actor* is named for any `CHILDREN/*`,
`JOURNAL/*`, or `FREEZE/*` object ("until … archived ∧ ack" says when,
never who, nor under which lock).

---

## Major findings

**X-M1 — the private entry surface is self-contradictory, and parentage
cannot close it for the supervisor.** `:105-108` says the supervisor is
created by "Double-fork from the CLI (**same module image; no new argv
command, script, or daemon executable**)" — i.e. `fork` without `exec`,
which has *no* argv of its own. `:653-656` simultaneously defines
`--supervisor-serve` / `--watchdog-serve` argv tokens "used only by
double-fork/spawn … refusal-first if invoked without supervisor
parentage checks". Two implementers therefore build different process
trees (fork+function vs re-exec), and the mitigation named is
impossible for the supervisor: after a double-fork the middle child has
exited, so the grandchild's `getppid()` is `1` — there is no parent to
check. For the watchdog a parentage check *is* sound (`getppid()` plus
the parent's start-identity equal to `SUPERVISOR_IDENTITY.json`, plus
proof that the sealed pipe FDs are pipes), but it buys nothing that
in-process entry does not.

Answering the prompt's question directly: **in-process post-fork
function entry is the smaller mechanically safe mechanism, and the argv
tokens should be deleted.** Fork-without-exec for both the supervisor
grandchild and the watchdog removes the entry surface entirely rather
than guarding it, keeps `os.fork` inside the already-allowlisted `os`,
and is safe for the watchdog specifically because it is spawned at
endpoint creation (:107-108) **before** any `RealTCapability` exists, so
the inherited address space contains no capability. Only the
*controller* needs `Popen`/`exec`, because only its argv is
client-supplied. This is an implementation-contract repair, not a new
author choice. One consequence must be pinned in the same edit: with
`pass_fds` the controller inherits fixed fd numbers but v2 never says
how it **learns** them (no argv convention — argv is client-supplied —
and no environment rule), so the inherited-pipe role credential of
§V2.2.2 is currently undiscoverable by its own peer.

**X-M2 — legal frames can exceed `T_CONTROL_FRAME_MAX_BYTES`, with no
continuation.** The one-write ≤4096-byte rule (:293-295) is sound
against interleaving, but two frames in the closed matrix can exceed it.
`OK`/`OPERATION_STATUS` with `phase=PROMOTED` carries a six-field
`release_token` (~500 bytes of hex) **plus** `promoted_relative_paths`,
a sorted list of up to `16 * device_units` = 64 paths (:531) with **no
per-path byte bound**; 64 × 64-byte names alone exceeds 4096. And
`CLAIM.arguments.argv` is an unbounded `list[str]` (:331). So a
perfectly legal operation can be unreplyable and a legal claim
unsendable, with no defined refusal on either side. *Repair:* bound
total path bytes explicitly (or drop `promoted_relative_paths` from the
reply and let `SETTLEMENT.json` + `result_sha256` carry it), bound
`argv` bytes, and add one closed `INVALID` token for a frame that would
exceed the maximum.

**X-M3 — framing and reply-path validation (Sol M2 not fully closed).**
v2 pins `PC_PIPE_BUF ≥ 4096`, one-write frames, `EAGAIN`, and the
keep-open writer, but never states the **frame delimiter** or the
reader's buffering rule, so a supervisor reading a 4096-byte buffer
containing two concatenated frames (or a tail) has no defined split.
Sol M2's "define bounded read buffering across writers" is unanswered.
Separately, `reply_fifo` is a **client-supplied path** (:307) with no
canonical form; `:296-297`'s directory-fd/`O_NOFOLLOW`/type/ownership
checks constrain the inode but not *which* inode, so one client can name
another client's reply FIFO and the supervisor will write reply bytes
there. *Repair:* pin frames as one canonical ASCII JSON line terminated
by `\n` with a reader that splits on `\n` and refuses any line >4096;
pin `reply_fifo` to exactly
`REPLY/<hex(client_start_identity)>.<idempotency_key>.fifo`, rejecting
every other value, and define the `ENXIO`/dead-client case (cache the
reply, no re-apply).

**X-M4 — "escaped children" is claimed as mechanical but nothing binds
behavior to the frozen `pgid`.** §V2.2.1 lists "escaped children" among
the *mechanical* guarantees (:213-215) and §V2.1.5 repeats it, while the
entire freeze mechanism is `killpg(pgid, …)` (:450-452). A controller
that starts its own subprocess with a new session — an ordinary,
non-malicious pattern, and the same pattern the supervisor itself uses —
leaves the frozen group, and v2 has no cgroup, no PID namespace, no
`PR_SET_CHILD_SUBREAPER` (unavailable: `signal`/`ctypes` are outside
`ALLOWED_ABSOLUTE_IMPORTS`, verified at
`src/philosophia/officina/verification.py:35-39`), and no descendant
scan. Signed §2c.4/§4c already route "escaped/unclassifiable work" to
recovery, so the safety net exists — but v2's *claim* of mechanical
coverage does not, and C1's guarantee is stated over the group only.
*Repair:* keep §V2.6.4's `killpg` as the action, add a fail-closed
quiescence proof (`/proc` walk over recorded members plus any process
whose session or parent chain reaches a recorded member; anything
unknown ⇒ §4c(c)/§4d unknowable), and move "escaped children" out of
§V2.2.1's mechanical list into the A3 procedural residual for the
deliberate case.

**X-M5 — ack freshness is measured on the wrong side, so a busy
supervisor kills a healthy watchdog.** `:441-443` requires the watchdog
to acknowledge `table_seq` within `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS`
(1 s) "or is treated dead", and §V2.6.6's consequence is severe:
freeze **all** live groups, refuse admissions, then (per §V2.6.5)
invalidate anything overdue. The supervisor can only observe the ack
when it next reads the pipe, and v2 explicitly contemplates the
supervisor being inside hash/`fsync`/Git archival for far longer than
1 s (§V2.6.1, §V2.12 row 9). Nothing says the deadline is evaluated
against the watchdog's own sample rather than the supervisor's read
time, so the mass-freeze path fires on a healthy watchdog. Two related
gaps: no supervisor poll cadence is defined anywhere (there is a
`T_WATCHDOG_POLL_INTERVAL_NS` but no supervisor equivalent), and since
`select`/`selectors` are **not** in the import allowlist the serve loop
must be a nonblocking `time`-paced poll — implementable, but unstated,
and the ack timeout is meaningless without it. *Repair:* the ack frame
carries the watchdog's `table_seq` and its own
`clock_gettime_ns(CLOCK_MONOTONIC)`; liveness is judged on
`ack_monotonic_ns` versus the update's `updated_monotonic_ns`; add the
supervisor poll-cadence constant and require an ack-service step inside
every long loop (see X-C3(b)).

**X-M6 — the singleton lock has no bounded wait and no discoverable
half-initialized grandchild.** The hold-through-identity rule and the
grandchild's close of the inherited lock fd (:99-108) are correct — and
`flock` semantics make them work, since the fd copy the grandchild
closes shares the CLI's open file description, so the lock persists.
What is missing: (i) how and for how long the CLI waits for
`SUPERVISOR_IDENTITY.json` (the middle child is reaped immediately and
the CLI has no relationship to the grandchild); (ii) the continuation if
the grandchild dies before installing the identity — the CLI holds the
lock on nothing; (iii) if the **CLI** dies in that window the kernel
releases the `flock`, a second CLI sees no live identity, runs takeover
— and the first grandchild is invisible to takeover for exactly the
X-C2 reason, so two supervisors can serve; (iv) the identity file is
atomic **no-replace**, so the loser's install fails with no defined
route. *Repair:* apply the X-C2 bridge one level up — write a durable
`SPAWNING.json` under the lock **before** the double-fork and give the
grandchild that id as its discoverable marker; pin a bounded CLI wait
with one closed refusal token; and pin "identity install collision ⇒
the loser exits without serving, writing nothing".

**X-M7 — the hash path is not restartable as claimed, and the
bound-check→hash→promote window is a TOCTOU.** `:540-541` says the
loop is "restartable from descriptor offset **after crash** without
re-spawning the worker". Neither half survives Linux: descriptors die
with the process, and streaming SHA-256 state is not serializable, so
after a crash the hash must restart at zero. Meanwhile `:526-536`
stats sizes, then hashes, then §V2.7.4 renames — and "revoke output
authority" (:568) is named with no mechanism, so under A3 the bytes
remain same-UID writable throughout. *Repair:* delete the
after-crash-offset clause and state that a crashed hash restarts from
zero (bounded by the frozen bound); hold `O_RDONLY|O_NOFOLLOW`
descriptors opened at enumeration time through hashing and promotion,
re-verify `st_size`/`st_ino`/`nlink` from the held descriptor
immediately before the settle step, and fail closed on any mismatch —
with the deliberate-modification residual named as A3 procedural.

**X-M8 — the promotion rename has three unrouted `errno` cases.**
`:570` is "idempotent `os.replace` of `out/` into
`T_PROMOTED/<operation_id>/`". `os.replace` of a directory fails with
`ENOTEMPTY`/`EEXIST` onto a non-empty destination, with `ENOENT` when
the source is already gone (the idempotent-completion case, which
therefore needs an explicit *test* — what proves the completed state?),
and with `EXDEV` if `runtime/` and `runtime_control/` are on different
filesystems or one is a mount/symlink. A cross-device copy fallback
would also re-open the X-C3 unbounded-work path. *Repair:* require a
same-filesystem preflight (`st_dev` equality checked at endpoint
creation, refuse otherwise), define the idempotent completion predicate
(destination exists ∧ `SETTLEMENT.json` durable ⇒ promoted, do nothing),
and state the creation/mode rule for `runtime/T_PROMOTED/`.

**X-M9 — two silent frictions with the signed composite.** (i) §V2.6.1
deletes the physical at-or-before-deadline claim, but the signed
harness §5a sentence "The watchdog owns the deadline and **executes the
v2.1 §1 sequence at or before it**" is not listed in the §V2.0
replacement index (:51-60), which touches §5a only for the "separate
supervisor" sentence. The re-scope is right; its traceability is
missing, and a signed sentence must not be contradicted by silence.
(ii) X-C1's record-first-invalidity-on-key-reuse expands the signed G5
surface to a client-triggerable event, which no signed text
contemplates. Both are text repairs.

**X-M10 — `spawn_intent_id` can collide, with no route.** The id is
SHA-256 over `{generation, role, argv_sha256, created_utc}` (:137-140)
with no timestamp resolution pinned and no sequence component, so two
legitimate controllers with identical argv inside one `created_utc` tick
produce one id; the "atomic no-replace" write then fails and v2 defines
nothing. *Repair:* include the reserved `process_sequence` (§V2.1.7
already computes it from complete durable history) in the id preimage,
and pin `created_utc` resolution.

**X-M11 — `ALREADY_DELIVERED` is outside its own enum.** §V2.4.5
returns `phase = ALREADY_DELIVERED` (:361) while that row's `phase`
enum is `{ADMITTED, RUNNING, PENDING_SETTLEMENT, PROMOTED, FAILED}` and
§V2.9.3's operation states omit it. In a document whose whole method is
"keys exactly", this breaks the closure it asserts. *Repair:* add it to
both enums (or return `phase=PROMOTED` with a separate
`delivered: true`), and pin which of the two the §V2.11 cut
"Ack durable | `ALREADY_DELIVERED`" means.

---

## Minor findings

1. `:145-146` requires the adapter to "install signal dispositions only
   as required to not defeat stop" — in CPython that means the `signal`
   module, which is outside `ALLOWED_ABSOLUTE_IMPORTS`
   (`verification.py:35-39`) while §V2.10 asserts "Allowlist delta:
   **none**". Since `SIGSTOP` disposition cannot be changed and
   `SIGCONT`'s default is what is wanted, pin the honest form:
   "installs **no** signal dispositions before the self-stop".
2. "Behavior-capable" is load-bearing in the bootstrap ordering claim
   (:143-145) and is never defined in this document. The interpreter,
   `site`, and the adapter's own import chain necessarily execute before
   any adapter statement, so the literal "first executable actions"
   claim is false; the true and sufficient invariant is that **no
   capability exists before `SIGCONT`** (:159-163). State that as the
   invariant and the self-stop as the mechanism, referencing the signed
   §A functional boundary for "behavior-capable".
3. `T_CLIENT_REPLY_TIMEOUT_SECONDS = 30` has no client-side
   continuation (exit code, journal query, or retry rule).
4. `REPLY/` has no creation, mode, ownership, or GC rule; the endpoint
   directory list (:94-95) names it and nothing else does.
5. The §3 durability discipline (temp → file `fsync` → atomic install →
   parent-dir `fsync`) is scoped in the signed composite to runtime
   transactions; v2 says "atomic" and "durable" for control-plane
   objects without restating it. One sentence adopting §3's discipline
   for `runtime_control/**` closes every crash-cut argument in §V2.11.
6. §V2.2.1's mechanical list should carry the truthfulness qualifier
   §V2.2.2 uses correctly (:239-242): the REQUEST.fifo role check
   defeats a controller that reports its **own** identity, not one that
   reports a live unrelated PID it read from `/proc`. That forgery is
   deliberate, hence squarely inside A3's procedural residual — but
   §V2.2.1 currently reads as though it were mechanically closed.
7. `runtime_control/**` and `runtime/T_PROMOTED/**` must also stay
   **untracked** for the activation-protocol clean-HEAD rule ("no
   source, configuration, manifest, authorization, or other tracked
   path may be dirty or staged") to hold; v2 says only "never stage".
   State that they remain untracked and that no `.gitignore` or config
   change is authorized by this amendment.

---

## Prior findings genuinely closed by v2

These I re-attacked and could not break; they should not be reopened in
v2.1:

- **F7 (reparented zombies)** — `:187-191`: death proved by
  `/proc/<pid>/stat` absence or state `Z`, `os.waitpid` restricted to
  own-generation children, and `kill(0)` explicitly refused as
  group-empty proof. Exactly right.
- **F12 (one promotion commit point)** — `:562-583`:
  `SETTLEMENT.json` (no-replace) is the commit; both crash directions
  have one continuation each; "only the charge-event captured in the
  same settle step is written into `SETTLEMENT.json`" closes the
  wrong/old/sibling-charge promotion. Modulo X-M8's `errno` cases, this
  is the correct fix and the reasoning is sound.
- **F13 (FIFO EOF/backpressure)** — keep-open `O_WRONLY|O_CLOEXEC`
  writer plus `EAGAIN`/partial-write ⇒ no action + journal retry.
- **F14 (archival exclusions)** — §V2.9.4 plus the activation
  protocol's *enumerated* staged sets: no signed set can capture these
  paths. Closed.
- **F10 (endpoint roles), controller half** — binding
  `OPERATION_ADMIT`/`OPERATION_STATUS` to the per-controller inherited
  pipe makes the **pipe itself** the credential, which is a real
  mechanical proof rather than a self-report. This is the strongest
  single mechanism in v2 (its one gap is X-M1's fd discovery).
- **F11 / Sol M3 (output grammar)** — regular-file, `nlink == 1`,
  `O_NOFOLLOW`, directory-fd traversal, relative/no-`..`/no-NUL,
  depth ≤ 2, count ≤ `16 * device_units`, sorted hashing order,
  worker-reported paths untrusted, and the sparse-file rule counting
  full logical `st_size`. Correct and fail-closed.
- **F15 / Sol M4 (streams)** — §V2.7.5's canonical `1..k` indexes,
  exclusive live ownership, sorted-unique-nonempty subsets, release
  points, subset-charges-its-own-streams summed into one process event,
  and all-live batch over the complete frozen set (amendment F1).
  Consistent with signed §2c.5/§4c/§4d.
- **F8 (pre-claim logs)** — a named path now exists
  (`CHILDREN/<spawn_intent_id>/controller.stdout.log`); only the
  "optional" rename is defective (X-C6).
- **F5, half** — the hold-through-identity rule and the grandchild's
  descriptor scrub are correct; the residue is X-M6.
- **F6 / Sol C5, honesty half** — §V2.6.1's disclaimer plus the
  dedicated freezer is the right shape for non-RT Linux; the residue is
  X-C4, not the topology.
- **F9 / Sol M1 (byte protocol)** — the per-command `arguments` tables,
  the exhaustive `detail` matrix, the closed refusal/invalid enums, and
  `PROMOTED` as `detail.phase` rather than a fourth status are a real
  closure of the largest v1 hole. The residue is the four undefined
  schemas (X-C6) and X-M2/X-M11.
- **Sol M5 / D1** — idle exit and `T_SUPERVISOR_IDLE_EXIT_SECONDS` are
  gone, with an explicit persistence list. Closed.
- **A3 honesty (F2 / Sol C1)** — mode-bit secrecy is declared void, the
  residual is aligned to the signed §5a operator residual, and the
  "must not be cited, inherited, or relied upon as Q/C
  confidentiality" bar (:223-225) is exactly right. Closed as an
  author-signed re-scope.
- **Codex §S6 / C1–C4, M1–M6** — all present in §V2.8 and traceably
  mapped in §V2.13: boundary batch wiring with no fabricated successor
  reservation, event/artifact-backed terminals only, `ARCHIVE` before
  `RESOLVED` with the registry blocking until archival commit, raw
  statically-parsed ledger-suffix D1 completion, G5 scoped to
  invalidities since the last valid admission, close in one lock epoch,
  private claim-backed `BatchSettlementAuthority`, strict
  `type(x) is int`, both review-record bindings to the durable
  pre-review head with the acyclicity regression, and the retained
  caller-supplied current head on `charge_batch_settlement`. The §V2.10
  argv rule (find the first `("-m", "philosophia.officina.generic_harness")`
  pair in `/proc/self/cmdline`) is the correct fix for Codex M5. None of
  these weakens the signed batch-settlement amendment or the harness
  composite; §V2.14's negative space is accurate.

## Answers to Fable's three Opus questions

**Q1 — Is the self-stop + `WIFSTOPPED` + spawn-intent path free of a
behavior-capable window and of undiscoverable pre-claim orphans under
crash between every pair of steps in §V2.1.4?**

**No, on the orphan half; qualified yes on the window.** The window: a
Python adapter cannot make self-`SIGSTOP` its literally first
executable action — interpreter startup, `site`, and the adapter module's
own import chain necessarily precede it — so the contract's ordering
claim is not literally satisfiable, and "behavior-capable" is undefined
here (Minor 2). What *is* true, and is the invariant that matters, is
that no `RealTCapability` exists until after the durable claim, lease,
and `SIGCONT` (:159-163), so the pre-stop instructions cannot perform a
signed behavior-capable operation. Restate the claim in those terms and
the window is closed honestly. The orphan half is **not** closed: the
intent bytes contain no PID, start identity, session, or argv, so
takeover's "kill by registry identity" has no referent (X-C2); the
stopped child is neither continued nor reaped by the kernel after
supervisor death and persists indefinitely; and the same discovery gap
recurs for the half-initialized supervisor grandchild (X-M6). The
argv-embedded `spawn_intent_id` + `/proc/*/cmdline` scan is a durable,
race-free bridge and needs no author choice. Independently, the crash
cut is not the only failure on this path: `waitpid(WUNTRACED)` on
client-supplied argv can block the runtime forever, and `¬WIFSTOPPED`
has no continuation.

**Q2 — Under §V2.6, can any reachable schedule leave a controller group
runnable past deadline without a freeze observation and, if
`overrun_ns > 0`, without forcing the invalid/recovery route?**

**Yes, several.** (i) The watchdog is descheduled or cgroup-throttled
past the deadline: no observation exists until it runs, and no
independent supervisor deadline check is defined — the group stays
runnable and the eventual freeze silently inflates `overrun_ns`.
(ii) The watchdog freezes correctly but dies before emitting the event:
§V2.6.6 routes to ack-timeout handling, and the true `freeze_ns` is
gone, so the observation is fabricated by a later sample (X-C4.4).
(iii) The event is lost on the pipe: same, and the *validity* of the
process now depends on a lossy read. (iv) Group membership changes: a
controller's own new-session child is never in `pgid`, so `killpg`
leaves it runnable and nothing detects it (X-M4). (v) The supervisor is
inside hash/`fsync`/Git work: the ack is judged on read time, so a
healthy watchdog is declared dead and *all* groups are frozen and
invalidated — a fail-closed cascade rather than a correct continuation
(X-M5). And even when a freeze is observed, `overrun_ns > 0` does **not**
force one route: `T_PROCESS_RESOURCE_STOP` is not excluded, the cause is
left as "`PROCESS` or `CLOCK`", and the unreachable zero-overrun branch
invites an unauthorized tolerance (X-C4.1–3). I am not asking for an
RT guarantee; I am asking for fail-closed detection with one
continuation, and v2 does not yet have it.

**Q3 — Is every promotion/journal/watchdog-death cut in §V2.11
single-valued on real Linux (including reparented `Z` and
SETTLEMENT-vs-rename ordering)?**

**No.** Genuinely single-valued: reparented `Z` and group-empty proof;
both `SETTLEMENT.json`-vs-rename directions; token redelivery until ack
(as an *effect* rule); "worker done, bound exceeded ⇒ FAILED before any
content hash". Not single-valued: "Spawn intent, no child |
**delete/refuse** intent" (two verbs, and see X-C2 for the child case);
"Journal ACCEPTED, effect incomplete | resume effect from phase" —
unreachable while the journal is no-replace, and its resume-versus-cache
decision is the one X-C1 breaks; "Reply lost | return cached reply for
same key" — false for every real retry (X-C1); "Freeze observed, settle
pending" — depends on an unestablishable `freeze_ns`; "Hash done, no
SETTLEMENT | quarantine" — quarantine has no object; "Watchdog dead
mid-live" — can fire on a healthy watchdog; "Supervisor dead | takeover"
— dual-valued authority (X-C5). The rename cut is also incomplete for
`EXDEV`/`ENOTEMPTY`/`ENOENT` (X-M8).

## Repair scope, and whether a new author choice is needed

**Bounded: yes.** Every repair above is a text change inside this
amendment — schema key lists, one or two control-only engineering
constants, a `/proc`-scan discovery rule, a semantic-request definition,
an entry-mechanism deletion, and explicit `errno`/actor/ordering
statements. Nothing requires touching E1/E2/E3 constants, the nine
events, the signed runtime schemas, the roots tuple, the import
allowlist, batch arithmetic, or any scientific cell. A3/B1/C1/D1 stay
exactly as signed; in two places (B1's "semantic" request, C1's
"dedicated freezer") the repair is literally the restoration of the
selected token's own wording.

**New author choice: not required, with one conditional.** The output-
byte DoS (X-C3) is closable mechanically by an admission-time
`os.statvfs` reservation plus a chunked, ack-servicing hash loop, which
introduces no numeric policy cell. **If** the author instead prefers a
hard signed ceiling on `max_total_output_bytes`, that *is* the
additional author cell the choice packet already flagged as outside
A–D, and it would need a token. Similarly, if the author reads C1's
"sole runtime writer" as forbidding the watchdog any durable write at
all, then X-C4.4 must take the fail-closed
`FREEZE_TIME_UNKNOWN ⇒ invalidity` variant — still no new token.

I recommend one v2.1 correction pass over §V2.1.2/§V2.1.4/§V2.1.6,
§V2.3, §V2.4.1/§V2.4.4/§V2.4.5, §V2.5, §V2.6.3–§V2.6.6,
§V2.7.1–§V2.7.4, §V2.10, and §V2.11, then one further bounded X/Y
confirmation. No token becomes eligible from this review.

## Contract defects versus dirty-implementation deviations

Everything above is a **contract** defect in the v2 draft. The
uncommitted Cursor implementation is not the source of any of them and
does not repair any: `generic_harness.py` still contains no supervisor,
no control channel, no FIFO, no journal, no operations tree, no
watchdog, and no promotion of confined output — `SubprocessProcessOps`
(`src/philosophia/officina/generic_harness.py:407-427`) is the only
process primitive present, `run_isolated_operation` (:2285) still
executes a caller-supplied callback in the harness interpreter, and
there is no `--supervisor-serve`/`--watchdog-serve` surface at all. Codex
C1–C4 / M1–M6 therefore stand unchanged as implementation findings, and
the v2 draft must not be read as evidence about them in either
direction. Two implementability facts I did confirm statically and that
v2 should state: `select`/`selectors`/`signal`/`ctypes` are absent from
`ALLOWED_ABSOLUTE_IMPORTS` (`verification.py:35-39`), so the serve loop
must be a `time`-paced nonblocking poll and no `prctl`-based
child-subreaper containment is available (X-M4, X-M5); everything else
v2 asks for (`os.fork`, `pipe2`, `mkfifo`, `flock`, `killpg`, `waitpid`,
`statvfs`, `clock_gettime_ns`, `subprocess` with `start_new_session`)
is available with **zero** allowlist delta, so §V2.10's zero-delta claim
survives.

## Custody confirmation

No code, test, contract, signature, prior review, or runtime artifact
was edited. No Officina supervisor, controller, worker, watchdog, FIFO,
journal, endpoint, operation, promoted object, smoke, or test process
was started; no probe script was run; no process was created by this
review at all. Nothing was committed and nothing was staged. This pass
created exactly one new file — this review. The four uncommitted Cursor
files and every unrelated dirty or untracked file are preserved
unmodified.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent; no capability, claim,
lease, batch, operation, entropy, E1/E2/E3 spend, world, learner,
candidate, Q/C object, datum, or outcome exists. T remains
`NOT_ACTIVATED` and the programme claim remains `OPEN`.
