# Opus X-line: Officina supervisor/control-channel v1 confirmation

Date: 2026-07-27
Reviewer line: X (adversarial implementability / Linux control-path)
Candidate commit: `9b05da09a1a45ac79368ed7abba09eb029db94fe`
Artifacts (hashes recomputed and matched the prompt):
`746bcf36…` supervisor/control-channel draft;
`2285ae09…` Fable closure.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1
```

The draft picks one topology and closes most of the formerly blocked
surface well — but an adversarial trace against real Linux semantics
finds **2 Critical** and **10 Major** determinacy/safety gaps that let
two compliant implementers build materially different (or unsafe)
process trees. The token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is **not ready** for Kirill's signature. Most corrections are
mechanical against the draft's own text; two (F1 idempotency binding,
F2 same-UID confinement) require a **bounded author choice** and are
called out as such below.

## What was checked against real Linux, not prose

- `/proc/self/stat` field 22 (`starttime`) **is** the 20th
  whitespace token after the final `)` (§S1.4 correct):
  `20th-token == naive-field-22` on probe.
- The pinned `verification.py:35` `ALLOWED_ABSOLUTE_IMPORTS` contains
  `os, fcntl, subprocess, time` (and `hashlib/json/pathlib/…`); it does
  **not** contain `socket/select/signal/sys/threading/multiprocessing`.
  The verifier keys on the top-level module name (`:184`), so every
  `os.fork/pipe2/mkfifo/killpg/waitpid`, `subprocess.Popen(...)`,
  `fcntl.flock`, `time.*` primitive passes with **zero allowlist delta**
  (point 18 — confirmed true).
- `PIPE_BUF == 4096`; the ≤4096-byte single-line frame is therefore an
  atomic, non-interleaving pipe/FIFO write (§S2.3 sound).
- **Same-UID confinement defeat (crux):** a same-UID process
  `os.chmod(opdir, 0o0700)` on a supervisor `0000` quarantine
  **succeeds** and reads the pre-settlement bytes; owner enumerates a
  `0700` dir freely. Mode bits confine nothing against the adaptive
  controller (F2).
- **Reparented-zombie reaping (crux):** a killed reparented process is
  state `Z`; `os.kill(zpid, 0)` still **succeeds**; `os.waitpid` on a
  non-child raises `ChildProcessError`/ECHILD. Takeover's "reap via
  `os.waitpid`" and "group-empty = `killpg(0)` → `ProcessLookupError`"
  are both wrong for reparented groups (F7).

All probes ran in `/tmp`; no repository state was touched.

## Critical findings

### F1 — CLAIM (and mutating commands) are not idempotent under a committed-but-lost reply (points 12, 2)

§S2.3 asserts "idempotence comes from the durable state, so a retried
request is re-validated, never re-applied." This is **false for
`CLAIM`.** `CLAIM` (§S1.3) spawns a controller, freezes it, and writes a
durable `t-process-claim.v1` with a **fresh** `process_id`, then replies.
If the reply is lost after that durable effect (supervisor exits, reply
FIFO gone, client timeout → the CLI "exits with the refusal exit code"),
a re-run of `claim` carries a **new** `client_monotonic_ns` (the draft
*requires* it to strictly increase for replay defense, §S2.3), so it is
a genuinely new request that the supervisor cannot distinguish from a
legitimate second claim — it spawns a **second controller and a second
durable claim/stream** for the one intended process. The replay rule
(strictly increasing monotonic) and retry-idempotency (stable identity
across retries) are in direct tension, and the draft resolves it toward
replay defense, leaving `CLAIM` doubly-applicable.

**Smallest correction:** add a client-generated, retry-stable
`idempotency_key` to the request frame (distinct from the freshness
`client_monotonic_ns`), and a generation-durable request→committed-reply
cache the supervisor consults before applying any state-creating command
(`CLAIM` at minimum; audit `START/PAUSE/RESUME`). A retried key returns
the cached reply without re-applying. **This changes the frame schema
and the CLI retry contract → needs an author choice** (which commands
are idempotency-keyed; whether the cache is durable or generation-local;
whether the CLI queries "did request K commit?" instead of blind re-run).

### F2 — Same-UID mode-based confinement does not satisfy §5b against the adaptive controller (points 8, 14)

§S3.3/§S3.4 confine the worker's pre-settlement output with directory
modes `0700`/`0000` under `runtime_control/T_SUPERVISOR/operations/`.
The controller runs under the **same UID** as the supervisor, so it
**owns** those inodes: it can `chmod` the `0000` quarantine back to
`0700`, `opendir` the operations tree, and read the worker's
pre-settlement bytes (probe: `chmod 0000→0700` then read succeeds).
§5b requires those buffers/paths be "neither readable nor writable by
the adaptive controller"; mode bits deliver **no** such property here,
and the draft's claim that the residual is "tightened by §S3.6's `0000`
quarantine mode" is affirmatively **wrong** (the owner defeats it).

The signed §5a threat model excludes "a privileged malicious operator"
as a procedural residual — but §5b names **the adaptive controller** as
the confined party, and under one UID the controller is de-facto
privileged over these files. So the draft either over-claims §5b or
silently re-scopes it.

**Smallest corrections (choose one; both are bounded):**
(a) *Mechanical:* the worker output never materializes at a
controller-traversable path — the worker streams bytes back through a
supervisor-held pipe/fd and the supervisor holds them in its own memory
(or a path outside any controller-reachable directory) until the atomic
promotion; nothing pre-promotion is written under a same-UID-owned,
controller-enumerable directory. (Bounded for oracle/update results;
may be impractical for large checkpoints — state the size rule.)
(b) *Author-acknowledged re-scope:* state honestly that mode-based
confinement defends only the §5a **accidental-fault / process-escape**
threat, that a **deliberate** same-UID controller read is exactly the
§5a procedural residual, and that full isolation requires a separate UID
supplied at activation/deployment. **Route (b) is a meaning change to
§5b → needs an explicit author choice.** As written the draft does
neither cleanly and must not be signed on the current confinement claim.

## Major findings (each blocks two-implementer determinacy or a signed invariant)

**F3 — SIGSTOP exec→stop race (point 1).** §S1.3 spawns the controller
with `subprocess.Popen(start_new_session=True)` then "immediately
freezes it (`os.kill(pid, 19)`)". Between `exec` and the external
`SIGSTOP` the controller runs arbitrary code (unbounded under load).
It is T-safe (no capability exists pre-lease, so it cannot perform a
behavior-capable operation), but "the controller performs no work while
stopped" does not establish "no work **before** the stop," and two
implementers differ observably (race window vs none). *Correction:* pin
a race-free handshake — the reviewed adapter's controller entry-point's
first action is `os.kill(os.getpid(), SIGSTOP)` (self-stop before any
work), or a pre-`exec` sync-pipe gate the supervisor opens only after
the lease+capability exist. State it exactly; do not leave the external
race.

**F4 — Pre-claim spawn orphan breaks single automatic continuation
(points 2, 4).** §S1.3 admits that a crash after spawn but before the
durable claim leaves a frozen controller "recorded nowhere durable …
terminated by the operator route or dies at boot." The takeover scan
(§S1.6) enumerates only **durable** claims/leases, so it cannot
identity-kill this orphan; it reparents to init, stays `SIGSTOP`ed, and
neither the operator route nor boot is the signed **single automatic
continuation**. The idle-exit (§S1.1) has the same hole for a
claimed-but-unstarted frozen controller. *Correction:* under the spawn
lock, before spawning, write a **generation child registry** entry
(control-plane, non-durable-evidence, keyed by
`supervisor_generation`) recording `controller_pid` + start-identity;
takeover reads it to identity-kill orphaned pre-claim spawns; idle-exit
refuses while any registry entry lacks a resolved durable claim. This
alters **no signed runtime evidence** and needs no author choice.

**F5 — Two concurrent supervisors possible (point 3).** §S1.2 spawns
under `flock(SPAWN.lock)` but does not state the lock is **held until
`SUPERVISOR_IDENTITY.json` is durably written and verified live.** If it
releases after the double-fork but before the grandchild writes the
record, a second client acquires the lock, sees no live record, and
spawns a **second** supervisor. Also: the double-forked grandchild
inherits the `flock` fd across `os.fork()` (CLOEXEC does not fire
without `exec`); it must close that fd. *Correction:* pin "hold
SPAWN.lock across takeover → double-fork → until the new
`SUPERVISOR_IDENTITY.json` is written and `os.kill(pid,0)`+start-identity
verified, then release"; pin the grandchild's close of every inherited
descriptor including the spawn-lock fd (§S1.2 already says "closes every
inherited descriptor" — make the ordering vs the identity-record write
explicit).

**F6 — Watchdog "at or before the deadline" is unbounded under
in-epoch work (point 5; Opus Q1).** §S1.5's firing rule
`now + poll ≥ deadline` accounts for the ≤100 ms **sleep**, not for a
single loop work item (request handling, filesystem I/O, **Git
archival**, output hashing, another settlement) exceeding the deadline
margin. A lease deadline can pass by seconds while the supervisor runs a
batch `ARCHIVE`. The "genuinely persistent, not lazy" claim is therefore
over-stated. It is not a safety breach (a missed deadline is settled in
full by §4c case (b)), but the draft must **make that explicit and
single-valued**: any deadline crossed during a long in-epoch operation
is settled per §4c(b) (actual interval, full overrun, may cross E1), not
treated as an error and not silently extended. Without this two
implementers diverge on the mid-archival miss.

**F7 — Takeover reaping is wrong for reparented groups (point 7).**
§S1.6/§S1.5 "reap via `os.waitpid`" and "group-empty proof =
`os.killpg(pgid, 0)` raising `ProcessLookupError`." Probes show a new
supervisor **cannot** `waitpid` a reparented orphan (ECHILD), and a
killed-but-unreaped orphan is a `Z` zombie that `kill(0)` still
**succeeds** on — so `killpg(0)` reports the group non-empty until init
reaps the zombies, and the proof can hang. *Correction:* takeover proves
group-empty by polling `/proc/<pid>/stat` per recorded member and
treating state `Z` (or `ProcessLookupError`) as dead; `os.waitpid` is
used **only** for own-generation children. Pin this explicitly (it is a
different code path from the in-generation watchdog).

**F8 — Controller stdout/stderr location undefined before `process_id`
exists (point 9).** §S1.3 redirects controller stdout/stderr "to
controller log files under the process's runtime_control operations
directory," but `process_id` is the claim hash, unknown until **after**
spawn+freeze+claim-write. The exact pre-`process_id` canonical path is
unspecified → divergence. *Correction:* name the pre-claim log/spawn
directory by the F4 generation-child-registry key, and pin the rename
(if any) to the `process_id` directory after the durable claim.

**F9 — Request `arguments` and reply `detail` are not byte-enumerated
(point 11).** §S2.3 says `arguments` is "the command's exact closed key
set (the six CLI commands take exactly their signed CLI arguments)" and
`detail` is "closed fact classes (v2 §F) … fixed refusal tokens" — but
**no** per-command `arguments` key/type set and **no** per-status
`detail` schema is written. `request_sha256` (used for replay and any
reply binding) is then **not reproducible** across implementers, and the
channel is not actually closed. *Correction:* enumerate, for each of the
eight commands, the exact `arguments` keys/types/enums, and for each
`status` the exact `detail` keys — as tables, like every other signed
schema.

**F10 — Peer role not enforced; a controller can issue CLI commands
(points 8, 13).** Endpoint separation helps (controllers use their
inherited pipe for `OPERATION_ADMIT`; CLI uses `REQUEST.fifo`), but a
same-UID controller can also `open(REQUEST.fifo, O_WRONLY)` (mode `0600`,
same owner) and send a well-formed `CLAIM`/`START`/… frame with its own
`client_pid`/start-identity. §S2.3 lists per-role command sets but pins
no mechanism to **classify the peer**. *Correction:* the supervisor
refuses any CLI command whose `client_pid`+start-identity matches a live
controller in the F4 registry, and refuses `OPERATION_ADMIT`/
`OPERATION_STATUS` arriving on `REQUEST.fifo` (accepted only on the
per-controller pipe). Bind command set to **endpoint and verified peer
identity**, explicitly.

**F11 — Promotion output-path safety not pinned (point 15).** §S3.4
"opens and hashes the exact output bytes itself" and "`os.replace` of
the output set," but a same-UID worker can plant symlinks/hardlinks in
`out/`, and the multi-file case is not pinned to one atomic directory
rename. *Correction:* pin an exact `output_relative_paths` grammar (no
`..`, no absolute, no `/`-escape), `O_NOFOLLOW` + regular-file + within-
`out/` checks on every path, a bounded output set, a deterministic
hashing order, and **one** atomic `os.replace` of the whole `out/`
directory into `T_PROMOTED/<operation_id>/`.

**F12 — Promotion commit boundary is ambiguous (point 16; Opus Q2).**
§S3.4 orders "`os.replace` into `T_PROMOTED/…` → write
`SETTLEMENT.json`," but §S3.6's cut table routes "`SETTLEMENT.json`
absent or promotion rename incomplete → quarantine + §6c, **no
promotion**." A crash between the rename and `SETTLEMENT.json` leaves a
**durable promoted artifact** that the failure route says to treat as
unpromoted — a contradiction, not a single continuation. *Correction:*
make one artifact the atomic commit point — e.g., write `SETTLEMENT.json`
(no-replace) as the commit, with the `T_PROMOTED` rename idempotently
completable from it — so every cut has exactly one continuation.
(The rest of Q2 is sound: never-reissuing a lost token is the correct
fail-closed terminal, and no cut double-charges — each charge is one
§2c.5 cursor-delta settlement and recovery settles the same cursor once
via §4c.)

## Minor findings

- **F13 (point 10):** pin that the supervisor holds a keep-open
  `O_WRONLY|O_CLOEXEC` handle on `REQUEST.fifo` so `read` returns EAGAIN
  (never a spurious EOF when all clients close), and define client
  behavior on a full FIFO (blocking write vs its reply timeout).
- **F14 (point 19):** state explicitly that `runtime_control/` and
  `runtime/T_PROMOTED/` are excluded from **every** signed archival set
  (activation protocol §B) and require no manifest/allowlist change;
  `T_PROMOTED/` placement *under* `runtime/` needs an explicit exclusion
  because archival stages named subdirs of `runtime/`.
- **F15 (point 17):** pin how a per-operation subset settlement
  (`declared_stream_indexes`) charges against the lease's single cursor
  when the lease has `k>1` streams and the operation occupies a subset.

## Confirmed correct (no change needed)

- `/proc/stat` field-22 start-identity parse (§S1.4) — exact.
- Zero import/allowlist/frozen-file delta (§S5/closure §5) — verified
  against `verification.py`; `runtime.py/ledger.py/checkpoint.py/
  verification.py/activation.py` remain byte-unchanged and need no edit.
- The §S6 repair ledger faithfully carries every prior X/Y finding
  (C1–C4/M1–M6, Sol C3/M7) with none weakened; in particular §S6.5's
  "raw statically parsed ledger suffix" is the correct fix for my earlier
  C4 (it bypasses `AppendOnlyLedger._verify_head`'s refusal on a lagging
  external head), §S6.4 restores `ARCHIVE`-before-`RESOLVED`, and §S6.6
  scopes G5 to "since the last admission." The closing confirmations —
  `charge_batch_settlement`'s caller-supplied current-head keyword
  **remains required**, and batch archival is **implementation-only** —
  match both prior reviews (point 20 satisfied).

## Answers to Fable's two Opus questions

**Q1 — Does §S1.5's poll-loop satisfy "at or before the deadline," and
is supervisor-death correctly the §4c route?** Partly. The
supervisor-death treatment **is** correctly the signed §4c
process-loss/reboot route (no process exists that could act; conservative
settlement at the next lock entry) — that half is proved. But the
persistent watchdog does **not** guarantee "at or before the deadline"
in every non-fault execution: the firing rule bounds the *sleep*, not a
long in-epoch operation (Git archival, hashing, a settlement), so a
deadline can be crossed mid-operation (F6). The draft must pin that such
a crossing is settled per §4c(b), after which the claim is honest.

**Q2 — Are the promotion/crash-cut rules single-valued at every cut?**
Almost. Never-reissuing a lost token is the correct fail-closed terminal,
and no cut double-charges. But the promote-then-`SETTLEMENT.json`
ordering yields one **ambiguous** cut (durable `T_PROMOTED` with no
`SETTLEMENT.json` is both "promoted" and "route to quarantine"); F12
fixes it by making one artifact the atomic commit.

## Smallest-path to signature and author-choice dependencies

Fix F3–F15 as mechanical corrections to the draft (they touch no signed
runtime schema/event/constant and need no author choice). F1 and F2
require **bounded author choices** before the token is signable:
- F1: the idempotency-key/reply-cache scheme and which commands it
  covers (and whether the cache is durable);
- F2: either accept the memory/non-enumerable-only output custody rule
  (mechanical, with a checkpoint-size caveat) **or** author-acknowledge
  the §5b re-scoping to the §5a same-UID procedural residual.

After those two author decisions are recorded and F3–F15 are pinned, one
further bounded X/Y pass can confirm the corrected draft; the token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not ready**
now.

## Custody confirmation

No implementation, activation, manifest, supervisor process, control
endpoint, FIFO, operation, promoted object, capability, claim, lease,
batch, entropy, spend, datum, or outcome was created. T remains
`NOT_ACTIVATED` (`runtime/` holds only `T_RUNTIME.lock`;
`T_ENVELOPE.json: "activated": false`). All probes ran in disposable
`/tmp` dirs and created no production-compatible artifact. Only this one
review file is added; no code, contract, test, signature, runtime
artifact, or existing review was edited; nothing was committed. The four
uncommitted Cursor files and every unrelated dirty/untracked file are
preserved unmodified.
