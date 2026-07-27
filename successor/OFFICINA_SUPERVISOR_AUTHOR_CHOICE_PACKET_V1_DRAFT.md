# Officina supervisor author-choice packet — v1 draft

Status: `CANDIDATE_FOR_AUTHOR_SELECTION_NOT_AUTHORIZED`.
Review-evidence commit: `913dc69`. Converged X/Y verdict:
`REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1`. The existing token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not
signable**.

This packet presents only the choices that cannot be selected
mechanically. It does **not** write the v2 correction. After Kirill
selects exact tokens below, a separate task will apply those selections
together with every mechanical F3–F15 / Sol repair into one
self-contained v2 draft.

Creates nothing executable. Edits no code, test, signature, runtime
artifact, or existing review. Starts no supervisor/controller/worker.
Creates no entropy, authorization, manifest, or spend. T remains
`NOT_ACTIVATED`.

---

## Platform audit (read-only; no Officina process started)

Observed on this host at packet authorship (current-platform facts,
**not** portable contract guarantees unless a selected option makes
them preflight conditions):

| Fact | Observed |
|---|---|
| Kernel | Linux 7.0.0-28-generic (Ubuntu 24.04 lineage) |
| `/proc/sys/kernel/yama/ptrace_scope` | `1` (restricted; non-parent same-UID ptrace attach refused) |
| `ptrace_scope` writable by current process | no (sysctl read-only here) |
| `/proc` mount flags | `rw,nosuid,nodev,noexec,relatime` — **no `hidepid=`** |
| Python | 3.12.3 |
| `os.pipe2` / `os.O_TMPFILE` / `os.memfd_create` / `os.pidfd_open` | present |
| `os.pidfd_getfd` | **absent** |
| `os.setns` / `os.unshare` / `CLONE_NEWUSER|NEWNS|NEWPID` | present |
| `os.fpathconf(fd, "PC_PIPE_BUF")` on a pipe | `4096` |
| `systemd` / `systemd-run` | present; `systemctl --user is-system-running` → `offline` |
| cgroup2 | mounted at `/sys/fs/cgroup` with `nsdelegate` |
| Audit process `CapEff` / `NoNewPrivs` / `Seccomp` | `0` / `1` / `2` (sandboxed audit shell — not the deployment model) |

Import allowlist (`verification.py` `ALLOWED_ABSOLUTE_IMPORTS`) already
contains `os`, `fcntl`, `subprocess`, `time`, `hashlib`, `json`,
`pathlib`. **`memfd_create` / `O_TMPFILE` / `pipe2` need no allowlist
delta.** `socket`, `select`, `signal`, `sys`, `threading`,
`multiprocessing`, `ctypes` remain absent and unauthorized.

Distinction: a sysctl or mount flag observed here is a
**current-platform fact**. A portable contract guarantee exists only
when a selected option requires a **reproducible preflight refusal**
before any capability, claim, or worker exists.

---

## Choice A — result confinement and endpoint roles

v1 same-UID `0700`/`0000` named paths are rejected (Opus F2; Sol C1/C2).
Every option below **must** also close endpoint roles:

- CLI commands (`CLAIM`…`RESUME`) accepted only on the CLI request
  endpoint;
- controller commands (`OPERATION_ADMIT`, `OPERATION_STATUS`) accepted
  only on the bound inherited per-controller channel of a live claimed
  controller;
- workers have **no** control endpoint (no FIFO path, no inherited
  request/reply channel, no right to open the CLI endpoint).

These role checks are mechanical once the compartment is chosen; they
are not a separate author choice.

### A1 — Kernel-enforced same-login compartment (anonymous custody + Yama preflight)

**Mechanism.** No named pre-settlement output path exists under any
controller-enumerable directory. Worker→supervisor transport is only
anonymous `os.pipe2(O_CLOEXEC)` (status) plus, for large/checkpoint
bytes, supervisor-held unnamed storage: `os.memfd_create` or
`open(…, O_TMPFILE|O_RDWR|O_CLOEXEC)` on a supervisor-private tmpfs
directory whose path is never published. The supervisor alone holds
those FDs, hashes by descriptor after the worker group is proved dead,
then atomically promotes into `T_PROMOTED/` only after the charge.
Controller and worker receive no pathname and no FD to pre-settlement
bytes.

**Kernel property claimed for byte secrecy.** With
`yama/ptrace_scope ≥ 1`, a non-parent same-UID process cannot
`PTRACE_ATTACH` and therefore cannot open another process's
`/proc/<pid>/mem` or duplicate its `/proc/<pid>/fd/N` links. Combined
with (a) no named pre-settlement inode and (b) workers/controllers never
being parents of the supervisor, the controller cannot read
supervisor-held pipe/memfd/O_TMPFILE **contents**.

**Mandatory preflight (else refuse all admission).** Before any claim
or capability: read `ptrace_scope` and refuse unless `≥ 1`; verify
`fpathconf(PC_PIPE_BUF) ≥ 4096` on the control pipe; verify
`memfd_create` or `O_TMPFILE` works with a throwaway FD that is
immediately closed. Preflight failure → no supervisor serve, no claim.

**Large output.** Not memory-only: stream into supervisor-held
`memfd`/`O_TMPFILE`; hash by descriptor; promote by linking/copying
from that FD into `T_PROMOTED/` under the settle lock. No in-memory
size bound is invented; hashing/promotion must complete under the
ordinary lease/watchdog rules (overrun → §4c(b)), see mechanical
bounds below.

**Guarantee.** Named-path and mode-bit bypasses of v1 are closed for
**result bytes**. Endpoint roles closed as above.

**Residual risk.** Same-UID timing, scheduling, and (on a `/proc`
without `hidepid=2`) possibly `/proc/<pid>/fdinfo` size metadata remain
observable. That is a **current-platform residual**, not closed by
Yama alone. Sol C2's full observation contract is therefore only
partially met. `ptrace_scope` is a mutable sysctl: without the
preflight it is not a portable guarantee.

**Deployment cost.** None beyond the preflight. One login account.

**Threat-model effect.** Strengthens v1 toward mechanical byte secrecy
against the adaptive controller; does **not** claim full Sol C2
metadata blindness.

**Allowlist/frozen-file delta.** None (`os.memfd_create` /
`os.O_TMPFILE` / `os.pipe2`).

**Selection token:**

```text
I_SELECT_SUPERVISOR_CONFINEMENT_A1_ANON_YAMA_PREFLIGHT
```

### A2 — Separate OS credential / service boundary

**Mechanism.** Supervisor runs as a dedicated OS user
(`officina-t-supervisor`), installed as a systemd system (or lingering
user) service. The login user never holds that UID. CLI processes of
the login user speak only to a supervisor-owned CLI endpoint whose
directory permissions grant write to the login group/ACL and ownership
to the supervisor user. Controllers and workers are children of the
supervisor and, before `exec`, the supervisor `setuid`/
`setresuid`s them to a second dedicated user
(`officina-t-controller`) so they never share the supervisor credential.
Workers likewise run as the controller user (or a third worker user)
and inherit no supervisor-owned path that is readable by that UID.

**Deployment prerequisite.** Package/unit that creates the two (or
three) users; a systemd unit running the sole harness module image as
the supervisor user with the repository path granted; CLI invocation
by the login user that only opens the ACL'd endpoint (no supervisor
credential in the login environment). Capability to `setuid` to the
controller user is held only by the supervisor service (systemd
`CapabilityBoundingSet` / ambient caps), never by the CLI or
controller.

**Guarantee.** Kernel DAC (and optional namespace/cgroup confinement of
the unit) makes pre-settlement supervisor state, endpoints, and worker
output unreadable/unmodifiable by controller/worker principals.
Endpoint roles follow from credential + inherited FDs: a controller UID
cannot open the supervisor-owned CLI endpoint if permissions deny it;
workers get no control FD.

**Residual risk.** Misconfigured unit/ACL re-collapses to same-UID.
Operational complexity. Does not claim resistance to a privileged
malicious host operator (signed §5a residual unchanged).

**Deployment cost.** High: users, unit, ACL, install review, activation
preflight that the live supervisor UID ≠ controller UID ≠ login UID.

**Threat-model effect.** Delivers literal signed §5b against the
adaptive controller as a distinct OS principal.

**Allowlist/frozen-file delta.** Prefer zero Python delta:
`os.setuid`/`os.setresuid` are `os` members; service launch is outside
the harness (systemd). If a helper script were added it would be a
**forbidden new root** — not authorized; the unit must exec
`python -m philosophia.officina.generic_harness` as the supervisor user
with an exact internal serve entry already implied by v1 double-fork,
re-expressed as service start. No `verification.py` change if only
`os`/`subprocess` are used. **Frozen-file note:** packaging/unit files
are deployment artifacts, not Officina runtime schemas; they still need
author ops review before activation.

**Selection token:**

```text
I_SELECT_SUPERVISOR_CONFINEMENT_A2_SEPARATE_CREDENTIAL_SERVICE
```

### A3 — Explicit same-UID procedural re-scope

**Mechanism.** Keep one login UID. State honestly that §5b's
"neither readable nor writable by the adaptive controller" is, under
one UID, enforceable only against **contract-following and accidental**
controllers (wrong FD inheritance, escaped children, honest path
mistakes). **Deliberate** same-UID inspection/chmod of supervisor paths
is exactly the signed §5a procedural residual (privileged-over-own-files
operator/agent), not a kernel compartment. Named custody may remain
only inside supervisor-private directories **after** this re-scope is
signed; endpoint-role binding (CLI endpoint vs inherited controller
channel; workers have none) remains mechanical and mandatory.

**Guarantee.** Honest threat model; accidental escape and wrong-endpoint
command paths closed; no false mode-bit secrecy claim.

**Residual risk.** A deliberate adaptive controller under the same UID
can read pre-settlement bytes if any named or `/proc`-reachable residue
exists — accepted as procedural, not mechanical.

**Deployment cost.** None.

**Threat-model effect.** Narrows §5b to match what same-UID Linux can
honestly promise; aligns residual with already-signed §5a.

**Allowlist/frozen-file delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
```

### Choice A recommendation

**Recommend A3.**

Reasoning: Opus/Sol rejected v1 because it **over-claimed**. A1 can
preflight byte-content secrecy via anonymous FDs + `ptrace_scope≥1`, but
on this host `/proc` has no `hidepid`, so Sol C2 metadata/timing channels
are not closed; elevating A1 with `hidepid=2` or user namespaces becomes
deployment-equivalent to A2. A2 delivers literal §5b but adds a large
credential/service surface before any Officina science moves. A3 is the
only option that is both **executable without new host policy** and
**epistemically honest** relative to the already-signed §5a residual.
If Kirill instead requires mechanical secrecy against a deliberate
same-UID adaptive controller, select **A2**, not A1.

A1 is listed as executable but **not recommended** under the mandate
rule: full promised §5b+Sol C2 observation is not mechanically closed on
the present platform without deployment primitives that collapse into A2.

---

## Choice B — durable idempotency and release delivery

No option may permit blind re-execution after timeout (Opus F1; Sol C3).
Byte schemas land in v2; this choice is semantic policy only.

### B1 — Durable exactly-once-effect journal for all eight commands; repeatable reply until durable acknowledgement

**Scope.** All eight: `CLAIM`, `START`, `HEARTBEAT`, `CLOSE`, `PAUSE`,
`RESUME`, `OPERATION_ADMIT`, `OPERATION_STATUS`.

**Journal.** Durable under `runtime_control/` (non-archival control
plane), survives supervisor generations. Keyed by client-generated
retry-stable `idempotency_key` (distinct from freshness
`client_monotonic_ns`). Same key + byte-identical semantic request →
resume or return the identical closed reply; same key + different bytes
→ record-first invalidity. Committed-but-lost reply → re-query returns
the cached reply; never re-applies. `OPERATION_ADMIT` retry with the
same key reuses the existing admission/`operation_id`/meter cursor; **no
second worker**. Release token: identical token bytes redeliverable on
`OPERATION_STATUS` until a durable acknowledgement/redemption record
exists; acknowledgement consumes the one-use effect exactly once.

**Guarantee.** Exactly-once effect; at-least-once observed delivery of
the release token; total continuation across generations without
inspecting output.

**Residual risk.** Token may be delivered more than once **as bytes**
before ack; effect remains one-use. Journal growth bounded by
acknowledgement + archival of the owning transition (mechanical
formula below) — no separate TTL tunable.

**Deployment cost.** Control-plane disk for the journal.

**Threat-model effect.** None scientific; closes lost-reply double-claim
and lost-token holes.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
```

### B2 — Durable exactly-once-effect journal plus fail-closed at-most-once release delivery

**Scope.** Same eight-command durable journal and reuse/invalidity rules
as B1 for effects.

**Release difference.** Token delivery is **at most once**. After the
first successful write of token bytes to a client reply (or a durable
"delivery attempted" mark), the token is never re-issued on the channel.
If the client did not observe it, the sole destination is a named
signed recovery path (existing §6c recovery disposition family), which
may reveal the already-settled release binding without creating a second
effect. No blind re-exec; no second worker; committed-but-lost
non-release replies still redeliver from the journal.

**Guarantee.** Exactly-once effect; at-most-once channel delivery of
release bytes; lost release → recovery only.

**Residual risk.** Higher operational rate of recovery dispositions for
routine reply loss; callers cannot rely on STATUS retry for tokens.

**Deployment cost.** Same journal + recovery UX.

**Threat-model effect.** Stricter channel secrecy for token bytes after
first send attempt; more author/recovery traffic.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_IDEMPOTENCY_B2_DURABLE_JOURNAL_FAILCLOSED_RELEASE
```

### Choice B recommendation

**Recommend B1.**

Reasoning: the load-bearing defect is double-effect and lost-reply
uncertainty, not double-observation of an already-settled one-use token.
B1 makes continuation total for controllers without multiplying recovery
dispositions; one-use **effect** remains bindable by durable
acknowledgement. B2 is available if Kirill prefers fail-closed release
visibility over retry UX.

---

## Choice C — watchdog topology

v1's serial 100 ms promise is false during blocking work (Opus F6;
Sol C5). The watchdog must **not** become a second runtime writer.

### C1 — Dedicated freezer watchdog process; sole supervisor settles later

**Topology.** At supervisor serve start, the supervisor spawns exactly
one child **watchdog/freezer** (`subprocess.Popen`,
`start_new_session=True`, reviewed argv inside the same module image,
no new root). Parentage: supervisor is parent; watchdog holds **no**
`T_RUNTIME.lock`, **no** capability, **no** right to write
`runtime/` or append the ledger. The watchdog receives a sealed
inherited channel carrying only: generation hash, and for each live
lease the `{pgid, start_identity, deadline_ns}` triple, updated by the
supervisor after every successful locked renew/remove.

**Deadline action.** When `now ≥ deadline`, the watchdog **only**
identity-verifies and freezes the controller group (`killpg` SIGSTOP /
SIGKILL as pinned in v2 mechanical text). It does not charge, claim, or
archive. The sole supervisor, on its next loop or via a non-blocking
wake, observes the freeze, takes `T_RUNTIME.lock`, and performs the
signed revoke→synchronize→§4c/§4d settlement.

**Death/handoff.** Watchdog death → supervisor refuses new admissions,
freezes all live groups itself, settles conservatively, respawns one
watchdog. Supervisor death → watchdog freezes all known groups and
exits; next CLI takeover (§S1.6 mechanical) settles via §4c. Watchdog
never writes durable runtime evidence.

**Guarantee.** No lease deadline can pass with the controller group
still running behavior: the freezer is scheduled independently of
supervisor archival/hash/Git work.

**Residual risk.** Freeze-to-settlement gap still accrues E1 (settled in
full per §4c(b)); that is already signed. Two processes to reason about.

**Deployment cost.** One extra OS process per generation.

**Threat-model effect.** Makes the signed "at or before the deadline"
stop-behavior guarantee true; settlement remains sole-writer.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
```

### C2 — Quiesce-and-settle before every potentially blocking operation; bounded event loop

**Topology.** Single supervisor process. Before any operation that is
not proved bounded by a hard millisecond cap (durable fsync batches,
Git archival, large hashing, backend sync waits, blocking FIFO open),
the supervisor first revokes/quiesces and conservatively settles **all**
live liabilities (full-live batch if required) so that **zero** behavior
is running when blocking work begins. The serve loop then only performs
bounded non-blocking poll steps while leases are live.

**Guarantee.** Vacuously: no deadline can pass with behavior running
during blocking work, because no live behavior exists then.

**Residual risk.** Sibling processes cannot remain live across another
process's archival; throughput collapses under concurrency. Defining the
"bounded" allowlist of loop steps is easy to get wrong.

**Deployment cost.** None extra, but operational cost is high.

**Threat-model effect.** Preserves sole process; changes scheduling
policy aggressively.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_WATCHDOG_C2_SETTLE_BEFORE_BLOCKING
```

### Choice C recommendation

**Recommend C1.**

Reasoning: C2 conflicts with ordinary multi-lease operation (one close's
archival would force sibling settlement). C1 keeps the sole supervisor
as the only runtime writer, makes stop-at-deadline true under load, and
leaves §4c(b) as the signed accounting residual for the freeze-to-
settle gap. Watchdog death/supervisor death handoffs are closed without
a second writer.

---

## Choice D — idle supervisor lifetime

### D1 — Remove idle exit

Supervisor persists until pause (G3), terminal state (G6/G7), G5 blocked
awaiting disposition, power loss/crash, or signed author stop. No
60-second idle exit.

**Guarantee.** Smaller state space; no drain/replay handoff cut.

**Residual risk.** Long-lived process while G1/G2 idle with zero leases.

**Deployment cost.** One idle OS process (negligible vs C1 watchdog).

**Threat-model effect.** None.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
```

### D2 — Retain idle exit only with a fully specified durable drain

Idle exit after `T_SUPERVISOR_IDLE_EXIT_SECONDS` remains, but only after
a closed drain: cease new admission; resolve or refuse every opened or
pending request from the durable journal; unlink endpoints only under
the generation lock when no eligible client remains; hand off the
durable request journal to the next generation; refuse exit while any
live lease, pending operation, unresolved batch/recovery/journal entry,
or frozen claim exists. Stale clients receive one deterministic
no-action `STALE_GENERATION` result.

**Guarantee.** Idle exit without v1's unresolved cuts.

**Residual risk.** Larger protocol surface; easy to under-specify again.

**Deployment cost.** Drain implementation and test matrix.

**Threat-model effect.** None scientific.

**Allowlist delta.** None.

**Selection token:**

```text
I_SELECT_SUPERVISOR_LIFETIME_D2_IDLE_EXIT_WITH_DURABLE_DRAIN
```

### Choice D recommendation

**Recommend D1.**

Reasoning: mandate preference for the smaller state space; no concrete
resource reason on this host requires idle exit; D2 re-introduces the
exact class of generation handoff bugs Sol M5 / Opus idle-exit notes
already hit.

---

## Mechanical repairs (not author choices)

The later v2 draft must pin all of the following without new options.
They absorb Opus F3–F15 and Sol C4/M1–M4 (and related) as mechanical
text:

1. Race-free controller bootstrap: reviewed entry self-`SIGSTOP`s before
   any behavior-capable import/input/thread/backend; supervisor observes
   `WIFSTOPPED` + exact start identity before writing the claim
   (equivalent kernel no-exec handshake permitted only if identical
   observables).
2. Discoverable pre-claim spawn intent / generation child registry;
   automatic takeover identity-kill; idle-exit (if D2) refuses while
   unresolved registry entries exist.
3. Singleton `SPAWN.lock` held through verified
   `SUPERVISOR_IDENTITY.json` installation; grandchild closes inherited
   spawn-lock fd before serve.
4. Own-child vs reparented-zombie handling: `waitpid` only for own
   children; group-empty via `/proc/<pid>/stat` with state `Z` or absence
   treated dead (never `kill(0)` alone on reparented zombies).
5. Exact pre-claim log/spawn directory keyed by registry id; rename to
   `process_id` after durable claim if required.
6. Exact per-command request `arguments` and per-status reply `detail`
   schemas for all eight commands; resolve `PROMOTED` as a closed
   `detail` variant under an allowed status (or amend the status enum
   mechanically to include it — one determinate table, no choice).
7. Exact identity→path encoding (lowercase hex of canonical identity
   bytes), FIFO open order, `PC_PIPE_BUF` verify, one-write frames,
   partial/EAGAIN = no action + closed retry state; keep-open writer on
   `REQUEST.fifo`.
8. Endpoint role checks (CLI endpoint vs controller inherited channel;
   workers none) — present under every Choice A option.
9. Safe output grammar, bounds, descriptor/`O_NOFOLLOW` hashing,
   whole-directory atomic promotion.
10. One promotion commit point (`SETTLEMENT.json` no-replace as commit;
    `T_PROMOTED` rename idempotently completable from it).
11. Stream ownership/subset table: canonical indexes, sorted unique
    nonempty subsets, exclusive live ownership, release points,
    per-stream readings; all-live batch uses the complete frozen set.
12. Archival exclusions: `runtime_control/` and `runtime/T_PROMOTED/`
    excluded from every signed archival set.
13. Operation subset settlement vs lease cursor for `k>1` (F15).
14. Closed pre-settlement observation contract consistent with the
    selected Choice A (admission/refusal + opaque handle only where A
    claims mechanical secrecy; honest residual where A3 applies).
15. All §S6 repairs carried **unchanged** (boundary batch wiring,
    event-backed terminals, stream witness, private claim-backed
    authority, `ARCHIVE` before `RESOLVED`, raw-ledger D1, G5 since
    last admission, ordinary crash cuts, one lock epoch for close,
    global sequence/id non-reuse, full registry validation, locked
    reads/capability/promotion, real `-m` CLI parsing, pre-review-head
    acyclicity, strict `type is int`).

### Numeric bounds — formula vs additional author choice

| Bound | Disposition |
|---|---|
| Max concurrent live operations | `≤ MAX_CONCURRENT_LEASES` (= 4, signed) |
| Max files per operation output set | `16 × device_units` (hence ≤ 64) |
| Max relative path depth | `2` |
| Journal retention | until owning transition is archived **and** reply acknowledgement (B1) or delivery mark (B2) exists — no TTL tunable |
| Max total output **bytes** | **not** supplied by any signed resource cap. Prefer: no new tunable; reject only on unsafe type/grammar/link rules; hashing/promotion subject to lease/watchdog (overrun → §4c(b)). **If** Kirill requires a hard byte cap for DoS, that is an additional author choice outside A–D — do **not** invent one in v2 without a token |

No additional A–D choice is opened for these formulas.

---

## Consolidated author response template

Copy, select exactly one token per choice, do not combine options:

```text
OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1

A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT

# Alternatives (replace line-for-line if desired):
# A: I_SELECT_SUPERVISOR_CONFINEMENT_A1_ANON_YAMA_PREFLIGHT
# A: I_SELECT_SUPERVISOR_CONFINEMENT_A2_SEPARATE_CREDENTIAL_SERVICE
# B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B2_DURABLE_JOURNAL_FAILCLOSED_RELEASE
# C: I_SELECT_SUPERVISOR_WATCHDOG_C2_SETTLE_BEFORE_BLOCKING
# D: I_SELECT_SUPERVISOR_LIFETIME_D2_IDLE_EXIT_WITH_DURABLE_DRAIN
```

Recommended quadruple is A3 + B1 + C1 + D1.

---

## What a later v2 correction must supersede

v2 must be a self-contained replacement of
`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md` that:

1. embeds the four selected tokens' normative text (not by open
   reference alone);
2. applies every mechanical repair listed above;
3. deletes v1 claims contradicted by the selections (same-UID mode-bit
   secrecy; serial-loop deadline promise; non-durable replay;
   parent-after-exec stop; idle exit if D1; etc.);
4. keeps zero scientific/resource-constant/event/runtime-schema movement
   except where a selection explicitly requires a control-plane schema
   (journal, spawn registry, settlement commit) already anticipated as
   generic-harness control artifacts;
5. leaves
   `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
   **still not signable** until a fresh bounded X/Y confirmation of that
   v2 accepts it.

---

## Negative authorization

This packet authorizes only Kirill's selection of exact A–D tokens and
the later drafting of v2 from those tokens plus the mechanical ledger.
It authorizes **no** implementation, commit, supervisor process, FIFO,
journal instance, credential/user creation, systemd unit install,
manifest, activation, capability, world, learner, entropy, E1/E2/E3
spend, Q/C object, datum, outcome, or claim movement. T remains
`NOT_ACTIVATED`; `successor/officina/runtime/` remains
`{T_RUNTIME.lock}` only; the programme claim remains `OPEN`.
