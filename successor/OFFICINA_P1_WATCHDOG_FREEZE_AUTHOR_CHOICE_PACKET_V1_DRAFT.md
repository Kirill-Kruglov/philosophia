# Officina P1 watchdog-freeze mechanism — author choice packet v1 (draft)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This packet selects nothing.**

**No token here is signable** until a bounded independent X-line and Y-line
review confirms this packet on identical bytes. `T` is `NOT_ACTIVATED`; the
programme claim is `OPEN`. This document creates nothing executable and
authorizes no implementation, activation, resource spend, T/Q/C datum, outcome,
Proof or claim movement.

---

## §1. The blocker, independently proved

The reporting author (myself, in the identity packet §6) is treated as
untrusted. The blocker is re-established from the contracts below. **It is
confirmed, and it is stronger than reported** — there are four independent
mechanisms, any one of which is sufficient, and the reporting author named only
two of them.

### §1.1 What a freeze mechanically requires

§W3.3, `…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:744-770`, is the one
mechanical evidence path, and the P1 binding routes to it verbatim
(`…V2_1_10_4_P1_BINDING.md:627-633`: "freezes all known groups per §W3.3"):

```text
1. verify /proc/<leader>/stat start identity matches      needs a numeric pid
2. killpg(pgid, SIGSTOP)                                  needs a signal syscall
                                                          and a numeric pgid
3. prove quiescence by enumerating /proc                  needs numeric pids
4. killpg(pgid, SIGKILL) after the first failed pass      needs a signal syscall
5. sample freeze_ns, set quiescence
6. write WATCHDOG/FREEZE/<witness_id>.json itself         needs the runtime root
```

So a freeze requires, irreducibly: **a numeric process-group id**, **the
`killpg` syscall**, and **filesystem reach into the runtime root**.

### §1.2 Mechanism 1 — the composite's own verifier forbids it

v1.2 §P1-14.6 rule `S-12`, at line 2601 of the selected composite:

> `S-12  subprocess, Popen, fork, waitpid, kill, killpg and system appear on no
> path of generic_harness.py`

The watchdog's role entry **is** in `generic_harness.py`: `A-13` calls "exactly
one pinned entry function, selected by `argv[7]` from a closed four-entry
mapping", and `A-10` imports `philosophia.officina.generic_harness` as the only
import. Therefore `killpg` **cannot appear on the watchdog's path**, and a build
in which it does is rejected by the verifier of the selected composite.

**This alone is dispositive.** The blocker is not an inference about
descriptors; it is a rule the selected architecture already enforces.

### §1.3 Mechanism 2 — the signed authority sentence

`…V2_1_10_4_P1_BINDING.md:150-153`: the PCS "is the sole caller of `fork`,
`posix_spawn`, `kill`, `killpg` and every `wait`-family primitive." A watchdog
`killpg` contradicts the signed selection directly, independently of `S-12`.

### §1.4 Mechanism 3 — no endpoint, and none can be added without cost

v1.2 §P1-6.2: the watchdog's slot set is `{3,4,5,7,8,9,10}` — update read, ack
write, harness source, role-bootstrap source, `src` dir, interpreter, package
root. **Slot 6 is "not used; explicitly closed by a file action"**, and §P1-6.4
makes that closure explicit in the `WATCHDOG` file-action vector. The watchdog
holds **no PCS socket**, and §P1-9.2 property 6 states it "communicates only
over its two sealed pipes at slots 3 and 4".

It also holds **no runtime-root directory descriptor** — the PCS's
`T_PCB_FD_RUNTIME_ROOT` is its own fd 5, and role slot 5 is the harness source.

### §1.5 Mechanism 4 — no relay exists at the only moment it is needed

The trigger is update-pipe EOF, which occurs precisely because the supervisor
has died and the kernel closed its update-write end. There is therefore no
supervisor to relay a request to, by construction. The PCS holds **no write end
on the watchdog update pipe** — §P1-8.7's ownership rule has it close its copies
of the supervisor's ends after the send — so the PCS cannot speak to the
watchdog either.

**A load-bearing corollary, which constrains every option below.** The PCS
*must not* retain a write end on the watchdog update pipe. If it did, the pipe
would never reach EOF on supervisor death, and update-pipe EOF is the **single
remaining supervisor-death detector** under P1 (§P1-9.2 property 10; the
`getppid()` detector was deliberately deleted). **Any design that gives the PCS
a channel to the watchdog by retaining that write end destroys C1's only
detector and is inadmissible.**

### §1.6 The numeric-identity half, and its relation to the other open cell

Even granting a signal mechanism, §W3.3 step 2 needs a numeric `pgid`, and the
witness record carries `process_id`, `pgid` and `start_identity`. The watchdog
learns lease rows over the update pipe from the supervisor — which under P1 has
no numeric identity either. This is the **same root cause** as the concurrent
cell `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`.

**Both options below are specified so that they do not depend on that cell**
(§5.3). A *variant* of either that preserves a watchdog-written numeric witness
would depend on it, and those variants are named and excluded here rather than
left implicit.

### §1.7 Verdict

**The blocker is PROVED.** Under the selected P1 architecture, update-pipe EOF
is observable and no specified route can execute the freeze. The reporting
author's account was correct and understated: `S-12` and the sole-caller
sentence each independently forbid it, before any descriptor argument is
reached.

---

## §2. Rejected route families

The round directs that these be rejected absent an explicit signed acceptance.
Each is rejected here with its reason, so the search is auditable.

| Family | Rejected because |
|---|---|
| give the watchdog numeric PID/PGID knowledge | reopens the identity cell inside this one, and puts numeric identity in a second contaminated-adjacent process for no gain over §3/§4 |
| give the watchdog direct signal syscalls | contradicts `S-12` and the sole-caller sentence; deletes the P1 authority model at its centre |
| give the watchdog a general PCS client | a general client is a general capability: it would let a compromised watchdog reach `SPAWN_ROLE`, `SIGNAL_ROLE` and `REAP_ROLE`. Only a single-opcode, target-free capability is admissible (§3) |
| relay through the supervisor after supervisor death | impossible by construction: the trigger *is* the supervisor's death (§1.5) |
| have the PCS retain a write end on the update pipe | **inadmissible** — destroys the single supervisor-death detector (§1.5 corollary) |
| abandon the freeze and terminate leased roles instead | this deletes signed C1 rather than implementing it, and destroys the `freeze_ns` evidence that §W3.4 settlement consumes. It is a C1 replacement requiring a fresh selection, not a mechanism repair |

---

## §3. Option W-A — watchdog requests, PCS executes

The watchdog holds **no PID**, and after update EOF sends **one** request on a
dedicated, single-opcode, target-free capability. The PCS executes the freeze.

### §3.1 Endpoint and slot

```text
The PCS creates, immediately before the SPAWN_WATCHDOG posix_spawn:
    _socketpair(_AF_UNIX, _SOCK_SEQPACKET, 0)
The WATCHDOG file-action vector's explicit (CLOSE, 6) is REMOVED and replaced
by (DUP2, h[6], 6). The watchdog's slot 6 becomes the freeze-capability socket.
The PCS retains the other end with FD_CLOEXEC set.

Watchdog slot set becomes {3,4,5,6,7,8,9,10}, identical in shape to
SUPERVISOR and CONTROLLER/WORKER. A-5's post-exec assertion is updated to that
set. No other role's slot map changes.
```

**Descriptor leak proof.** The added descriptor is created by `_socketpair`,
whose descriptors CPython creates non-inheritable, so the PCS's retained end
carries `FD_CLOEXEC` and is closed by every later role's `execve` — the §P1-6.4
proof stands with one more member in the "every other PCS descriptor has
`FD_CLOEXEC` set" set. The watchdog's end reaches slot 6 by `DUP2`, which clears
`FD_CLOEXEC` on the destination, exactly as for slots 3 through 10 today. No
controller, worker or supervisor receives it, because file actions are
per-role. The socket is point-to-point, so no third process can join it.

### §3.2 Request grammar — closed, target-free

```text
0  "philosophia.officina.t-wd-freeze.v1"    literal
1  "1"                                       version
2  generation_id                             64 lowercase hex
3  request_seq                               decimal, 1..6 digits, no leading
                                             zero, strictly increasing
4  "FREEZE_ALL_LEASED"                       the ONLY opcode token
5  table_seq                                 decimal, 1..19 digits — the lease
                                             table sequence the watchdog last
                                             acked
```

**Why it cannot express an arbitrary target.** *The request contains no target
field of any kind* — no pid, no pgid, no handle, no role, no index. The freeze
scope is computed entirely from PCS-side state (§3.4). A watchdog that is wholly
compromised can request exactly one thing: "freeze the set the PCS already
knows". It cannot name, narrow, widen or redirect that set.

**Why it cannot express another opcode.** Field 4 is drawn from a one-element
closed set. Any other value is `UNKNOWN_OPCODE` → `INVALID`, no action, no state
change. There is no second opcode to reach, and this socket is not connected to
the `t-pcs.v1` handler at all: it is a separate accept path with its own
one-opcode dispatch table.

### §3.3 Generation and handle binding, reply, ack, timeout, replay

```text
BINDING: field 2 must equal the PCS's current generation_id, else INVALID with
  WRONG_GENERATION, no action. Field 5 must be a table_seq the PCS has recorded
  as published; a value it never published is INVALID with REQUEST_MALFORMED.
  No handle is named by the watchdog, ever.

REPLY, on the same SOCK_SEQPACKET socket, exactly one record per request:
  0  "philosophia.officina.t-wd-freeze.v1"
  1  "1"
  2  generation_id  echoed
  3  request_seq    echoed
  4  status         OK | REFUSED | INVALID | REPLAYED
  5  detail         one token of §P1-2.6
  6  frozen_handles decimal count, or "-"
  7  unresolved     decimal count, or "-"
  NO pid, NO pgid, NO handle_id, NO path. The reply is a receipt, not evidence.

ACK: none. The reply IS the ack; SOCK_SEQPACKET makes it one record or nothing.

TIMEOUT: the watchdog waits at most T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
  (60_000_000_000) for the reply, polling at T_SUPERVISOR_POLL_INTERVAL_NS.
  On expiry it writes nothing and exits. It NEVER retries with a second
  request_seq, because a freeze is not idempotent in its side effects on a
  live tree and the PCS journal is the authority on whether it happened.

REPLAY / IDEMPOTENCY: the PCS journals the request under the autonomous
  keyspace of §3.6 before acting. A repeat of an already-journalled
  (generation_id, request_seq) returns the recorded reply with status REPLAYED
  and performs NO syscall — identical in shape to the J1-J6 rule of §P1-8.6.
```

### §3.4 PCS action and freeze scope

```text
On a valid FREEZE_ALL_LEASED:
  SCOPE := every handle h in the current generation with
             h.role in {CONTROLLER, WORKER} and
             h.state in {SPAWNED, RUNNING} and
             h.ownership == OWNED
  in ascending handle_id order, for each h:
    a. IDENTITY_OBSERVE(h.pid); if the result is not row I-1 or I-3, skip and
       record SKIPPED_IDENTITY
    b. _killpg(h.pgid, 19)                      SIGSTOP
    c. quiescence passes per §W3.3 steps 3-5, over the PCS's OWN recorded
       member set, with _killpg(h.pgid, 9) after the first failed pass
    d. record freeze_ns_or_null, quiescence, unresolved_member_count
  The PCS never widens SCOPE, never freezes the supervisor's group, and never
  freezes a WATCHDOG handle — both signal opcodes already refuse a watchdog
  handle at every state and that rule is retained verbatim.
```

### §3.5 Who writes the witness — and what W-A does *not* do

The PCS's reply carries **no numeric identity** (§3.3), so the watchdog cannot
write a schema-valid `t-freeze-observation.v1`, whose key set requires
`process_id`, `pgid` and `start_identity`.

**W-A therefore specifies: the watchdog writes no freeze observation.** The
freeze facts live in the PCS journal (§3.6). For the peer layer the witness is
**absent**, and the already-signed absent-witness route applies: §N5.1's
`ABSENT` sentinel with `rejected_witness_path_or_null = null`, producing a
supervisor-written fallback at the next takeover with `unknown_reason =
EVIDENCE_ABSENT`, routing to the signed `UNKNOWN` invalid route.

**The excluded variant, named rather than left implicit.** A W-A in which the
PCS returns per-handle numeric evidence so the watchdog can write the witness
**is not offered**, because it hands numeric identity to the watchdog — a
rejected family (§2) — and because it would make this cell depend on
`AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`, which this packet is required to
keep separate.

### §3.6 Journal, B1 and crash cuts

```text
JOURNAL KEY: the autonomous keyspace (generation_id, "WDFREEZE", request_seq),
  disjoint from the (generation_id, request_id) keyspace of §P1-8.6 by its
  middle member, so no collision is expressible.
ORDER: J1 receive/validate; J2 append ACCEPTED + fsync; J3 perform the freeze;
  J4 append COMPLETED with per-handle results + fsync; J5 send the reply.
  There is no J6: the reply is the terminus and no descriptor is transferred.
```

| Cut | Continuation |
|---|---|
| watchdog dies before sending | **no freeze occurs at all**; the named liveness residual of §5.5 |
| crash after `J2`, before `J3` | `ACCEPTED` ⇒ inconclusive ⇒ whole-generation invalidity; no PCS may adopt |
| crash mid-`J3` | partial freeze, entry still `ACCEPTED` ⇒ inconclusive ⇒ invalidity; some groups stopped, some not |
| crash after `J4`, before `J5` | freeze durable; a replay returns the recorded reply and performs no syscall |
| watchdog dies after `J3`, before reading the reply | the freeze happened and is journalled; nothing depends on the watchdog reading it |
| PCS dies at any point | §P1-11.4 unchanged: whole-generation invalidity, no adoption; any unfrozen role is orphaned and keeps running |
| both die | no freeze; invalidity; §5.5 residual |

### §3.7 Amendment to "the watchdog holds no capability"

**This is a real weakening and W-A does not present it otherwise.**

```text
SIGNED TODAY (v1.2 §P1-9.2 properties 1, 2, 6):
  "it holds no lock of any kind"; "it holds no capability object";
  "it communicates only over its two sealed pipes at slots 3 and 4"

PROPOSED UNDER W-A:
  "it holds no lock of any kind; it holds no capability object other than a
   single-opcode, target-free freeze-request socket at slot 6, which can
   express exactly one request naming no target and can reach no other
   operation; it communicates only over its three sealed endpoints at slots
   3, 4 and 6."

TOKEN: P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
```

**Does it remain the dedicated freezer in the scientifically meaningful sense?**
Partly, and the packet is explicit about which part. It remains the process that
**decides** a freeze is due and **triggers** it — the C1 role that matters for
evidence, since the decision is what binds the freeze to the deadline it
observed. It ceases to be the process that **executes** the stop, and it ceases
to be the **witness of record**, since it writes no observation (§3.5). C1's
sentence "the watchdog writes `WATCHDOG/FREEZE/<witness_id>.json` observations"
is **not** retained under W-A.

---

## §4. Option W-B — the PCS freezes on supervisor `PEER_EOF`

The PCS detects loss of the supervisor channel and executes the freeze itself.
The watchdog becomes a pure liveness sensor.

### §4.1 Topology — unchanged

**W-B adds no descriptor, no socket, no slot and no opcode.** The watchdog's
slot set stays `{3,4,5,7,8,9,10}` with slot 6 explicitly closed. The §P1-6.4
descriptor leak proof and the §P1-6.2 map are **byte-unchanged**, and so is the
`A-5` post-exec assertion. This is W-B's principal structural property.

### §4.2 Exact ordering

```text
E-1. The PCS's _recvmsg on the protocol socket returns a zero-length record
     with no ancillary data ⇒ PEER_EOF. The supervisor's end was closed by the
     kernel at its exit, so this is a kernel fact, not a report.
E-2. The PCS marks the generation SUPERVISOR_LOST. It accepts no further
     request, because no peer exists to send one.
E-3. The PCS executes the freeze over exactly the SCOPE of §3.4, in ascending
     handle_id order, with the same steps a-d.
E-4. The PCS appends ONE journal entry under the autonomous keyspace
     (generation_id, "PEEREOF", 1) with the per-handle results, and fsyncs.
E-5. The PCS holds every live handle in the non-returning reaper state of
     §P1-11.4 and frees the singleton for no one.

INDEPENDENTLY, and with NO ordering relation to E-1..E-5:
W-1. The watchdog observes update-pipe EOF — the same kernel fact, delivered
     on a different descriptor.
W-2. It writes NO freeze observation, because it can prove nothing: it has no
     numeric identity, no signal authority and no channel to the PCS.
W-3. It exits. The PCS reaps it on the next REAP_ROLE, or its adopter does if
     the PCS is already gone.
```

**The two EOFs are the same kernel event observed on two descriptors.** Neither
process waits for the other and no ordering between them is asserted or needed —
which is why no race between them exists.

### §4.3 Which process proves what

| Fact | Proved by | How |
|---|---|---|
| the supervisor is gone | **PCS** | `PEER_EOF` on its own socket end |
| the supervisor is gone | **watchdog** | EOF on its own update read end |
| each leased group is stopped or dead | **PCS** | its own `killpg` plus the §W3.3 quiescence passes over its own recorded member set |
| the freeze instant | **PCS** | `freeze_ns` sampled on the proving pass |
| the generation is invalid | the next takeover | from the absent witness, per §4.5 |

**No fact is proved by a process that lacks the authority to establish it** —
which is the property the current specification violates.

### §4.4 Races with PCS death

| Race | Outcome |
|---|---|
| PCS dies before `E-1` | no freeze; whole-generation invalidity; leased roles orphaned and still running — the named residual of §5.5 |
| PCS dies between `E-1` and `E-3` | as above; nothing journalled |
| PCS dies mid-`E-3` | partial freeze; entry not `COMPLETED` ⇒ inconclusive ⇒ invalidity |
| PCS dies after `E-4` | the freeze facts are durable in the journal; the generation is still invalid and no adoption occurs |
| PCS and supervisor die together | no freeze; invalidity; residual as above |
| watchdog dies before or during any of it | **no effect** — W-B does not depend on the watchdog at any step |

### §4.5 The witness, and the settlement route

The watchdog writes no observation and the PCS writes no peer-owned record —
preserving v1.2 §P1-13.2 row 4's ownership, since no P1 root gains an install
site for a peer artifact.

For that generation the witness is therefore **absent**, and the already-signed
absent-witness route applies unchanged: §N5.1's `ABSENT` sentinel
(`rejected_witness_path_or_null = null`,
`rejected_object_sha256_or_null = null`), a supervisor-written
`t-freeze-fallback-observation.v1` at the next takeover with `unknown_reason =
EVIDENCE_ABSENT`, and §N5.3's routing: record-first live-process invalidity, the
all-live batch, public cause `PROCESS`, full charging, no synthesized freeze
instant and no `overrun_ns`.

**W-B invents no settlement route.** It routes an absent witness exactly where
the signed chain already routes one.

### §4.6 B1, journal and replay

The freeze is journalled once under `(generation_id, "PEEREOF", 1)`. Because
`PEER_EOF` is terminal and the key is a constant within a generation, the entry
is naturally singular: a second detection in the same generation finds the key
present and performs no syscall. No reply is sent and no descriptor is
transferred, so B1's descriptor-non-redelivery narrowing is untouched.

### §4.7 The one genuinely new thing in W-B, named

**The PCS acts without a request.** Today every PCS action is request-driven.
`E-3` is the first autonomous PCS side effect in this architecture. It is
bounded by construction: it is triggered by exactly one kernel fact, it operates
on exactly the pre-existing handle scope, it happens at most once per
generation, and it cannot be induced by any request. But it is new initiative
and a reviewer should weigh it as such rather than as a routine extension.

### §4.8 Amendment to C1

```text
SIGNED TODAY (v1.2 §P1-9.2 properties 7, 12; C1's "dedicated freezer"):
  the watchdog "physically emits freeze observations"; "on observing
  update-pipe EOF it freezes the groups it knows, writes their observations,
  and exits"

PROPOSED UNDER W-B:
  "The watchdog is the dedicated supervisor-liveness sensor. It observes
   update-pipe EOF and exits, writing nothing. It neither executes nor
   witnesses a freeze; the PCS executes the freeze on its own PEER_EOF and
   records it in the process-control journal, and the absent peer witness
   routes through the signed ABSENT-sentinel fallback."

TOKEN: P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1
```

C1's "dedicated" and "holds no lock, no capability, no `runtime/` write, no
ledger append, settles nothing" survive **strengthened** — the watchdog holds
strictly less than before. What is lost is its *freezer* and *witness* role.

---

## §5. Comparative audit

### §5.1 Surface

| | W-A | W-B |
|---|---|---|
| descriptors added | 1 socketpair; watchdog slot 6 reopened | **none** |
| leak proof | must be re-proved with one more member (§3.1) | **byte-unchanged** |
| opcodes / grammars added | one request, one reply, one dispatch path | **none** |
| capability surface of the watchdog | one single-opcode, target-free socket | **strictly reduced** |
| autonomous PCS action | no | **yes** — the new thing (§4.7) |
| P1 sentences amended | "holds no capability", "two sealed pipes", `A-5` slot set | **none** |
| C1 sentences amended | freezer-executor and witness roles | freezer and witness roles |
| peer contracts reopened | **none** — absent-witness route reused | **none** — same |
| verifier rules | `S-12` retained; new rules for the one-opcode dispatch and target-free grammar | `S-12` retained unchanged; one rule that the autonomous path is reachable only from `PEER_EOF` |
| tests | endpoint, grammar, replay, timeout, scope, crash cuts | ordering, scope, crash cuts, absent-witness routing |
| manifest | composite digests only | composite digests only |

### §5.2 Supervisor death versus PCS death

Identical in both: PCS death is whole-generation invalidity with no adoption
(§P1-11.4, untouched). The difference is supervisor death — under W-A the freeze
requires a live, correct watchdog; under W-B it requires only the PCS.

### §5.3 Independence from the concurrent identity cell

**Both options as specified are independent of
`AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`**, because neither writes a
numeric peer witness: both route the absent witness through §N5's signed
`ABSENT` sentinel. Neither choice is conditioned on that cell's outcome, and
that cell's outcome does not change which of W-A or W-B is better on any
criterion in §5.1.

**Coexistence.** Both W-A and W-B coexist with either identity outcome:

| | identity Option A | identity Option B |
|---|---|---|
| W-A | compatible; no interaction | compatible; no interaction |
| W-B | compatible; no interaction | compatible; no interaction |

The one place they touch is a **future** possibility, stated so it is not
mistaken for a dependency: if identity Option A is signed, a later amendment
*could* let the peer layer publish numeric lease rows, which would make a
watchdog-written numeric witness constructible again. That would be a **new
cell**, is not proposed here, and neither option in this packet assumes it.

### §5.4 First and replacement watchdog symmetry

| | W-A | W-B |
|---|---|---|
| symmetry | preserved: the replacement receives the same slot-6 socket from the same `SPAWN_WATCHDOG`, with the same one-opcode grammar | preserved trivially: no watchdog participates in freezing, so first and replacement are indistinguishable |

### §5.5 Residual liveness under A3, and publication wording

Both options leave a liveness residual; neither is citable.

```text
W-A residual: the freeze requires a live, unwedged watchdog. Under A3 a
  same-UID actor may SIGSTOP the watchdog, after which no freeze is ever
  requested. This is a NEW liveness dependency on a process the architecture
  did not previously depend on for this outcome.
W-B residual: the freeze requires a live PCS. Under A3 a same-UID actor may
  SIGSTOP the PCS. This is NOT a new dependency: D1 already makes PCS loss an
  unrecoverable whole-generation invalidity, so the architecture depends on
  the PCS for everything already.
BOTH: if the freeze does not occur, leased roles keep running as orphans until
  their adopter or the host reclaims them. That is an infrastructure fact and
  never a scientific or resource outcome.
```

**Required publication wording, both options** — an addition to the `L1`–`L5`
non-guarantee list:

> **L6.** That a freeze occurs, or that freeze evidence becomes available,
> after supervisor death. No route guarantees it, and its absence settles
> through the signed `UNKNOWN` invalid route with no synthesized instant.

### §5.6 Interaction with the generic harness, batch settlement and invalidity

Identical for both, and **no peer contract is reopened by either**: the absent
witness is an input the peer layer already handles by §N5. Batch settlement sees
an ordinary `PROCESS`-caused invalidity. Archival ordering, capacity accounting
and custody dispositions are untouched. No scientific or resource interpretation
changes under either option; a freeze or its absence is an infrastructure fact.

### §5.7 Counterexample prevented, residual created

| | W-A | W-B |
|---|---|---|
| **prevents** | an implementation that cannot execute its signed C1 obligation at all, and the worse alternative in which an implementer adds `killpg` to `generic_harness.py` and silently fails `S-12`, or ships with the rule relaxed | the same |
| **new residual** | a compromised watchdog can force one freeze of all leased groups per generation — a denial-of-progress, not a capability escape, and bounded to a set it cannot choose | the PCS takes an action no request authorized; a future editor could widen the autonomous path if the reachability rule is not enforced |

---

## §6. Recommendation

On the three stated criteria only — signed-authority fidelity, mechanical
testability, and minimal reopened contracts:

> **W-B is recommended.**

| Criterion | W-A | W-B |
|---|---|---|
| signed-authority fidelity | amends three P1 sentences and weakens "holds no capability"; preserves C1's *decider* role | amends **zero** P1 sentences; strengthens the watchdog's no-capability property; changes C1's actor role |
| mechanical testability | new socket, grammar, dispatch, replay and timeout — all new surface to test | **no new descriptor, opcode or capability**; the whole change is one reachability-constrained code path with a kernel-fact trigger |
| minimal reopened contracts | none reopened, but three P1 sentences amended | none reopened, one C1 role sentence amended |
| robustness of the trigger | fails if the watchdog is dead or wedged | **works whenever the PCS lives**, and the architecture already depends on the PCS for everything |

The decisive facts are that W-B changes **no descriptor topology**, so the
§P1-6.4 leak proof stands byte-unchanged, and that it introduces **no new
liveness dependency**, where W-A makes the freeze contingent on a process whose
death is itself one of the conditions C1 exists to handle. W-B's single genuine
cost — the first autonomous PCS action — is bounded by a kernel-fact trigger, a
pre-existing scope, and a once-per-generation journal key.

**This is a recommendation on the stated criteria only. The author selects
nothing and predicts no outcome.**

---

## §7. Tokens

Mutually exclusive. **Neither is signable until bounded X/Y review confirms this
packet on identical bytes.**

```text
I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_EOF
```

Selecting W-A additionally requires `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1`
(§3.7). Selecting W-B additionally requires `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1`
(§4.8). Both selections additionally require the `L6` publication wording of
§5.5.

---

## §8. Deterministic v1.3 handoff

### If W-A is signed

1. §P1-6.2: watchdog slot 6 becomes the freeze socket; slot set `{3,4,5,6,7,8,9,10}`.
2. §P1-6.4: remove `(CLOSE, 6)` from the `WATCHDOG` vector; re-state the leak proof per §3.1.
3. §P1-7.4: update `A-5`'s asserted watchdog slot set.
4. New §P1-8.9: the `t-wd-freeze.v1` channel — §3.2, §3.3, §3.4 verbatim.
5. §P1-8.6: add the autonomous keyspace of §3.6.
6. §P1-9.2: replace properties 1, 2, 6, 7 and 12 per §3.5 and §3.7.
7. §P1-11.7: add the seven cuts of §3.6.
8. §P1-12.2: add `L6`.
9. §P1-14.6: add the one-opcode dispatch and target-free grammar rules; **retain `S-12` unchanged**.
10. §P1-15: add test rows for endpoint, grammar, replay, timeout, scope, and each cut.

### If W-B is signed

1. **No change to §P1-6.2, §P1-6.4, §P1-7.4 or any descriptor rule.**
2. New §P1-11.8: the `PEER_EOF` freeze — §4.2, §4.3, §4.4 verbatim.
3. §P1-8.6: add the `(generation_id, "PEEREOF", 1)` autonomous key.
4. §P1-9.2: replace properties 7 and 12 per §4.8; strengthen 1, 2 and 6.
5. §P1-11.7: add the six races of §4.4.
6. §P1-12.2: add `L6`.
7. §P1-13.2 row 4: record that under W-B no witness is written for a
   supervisor-death generation and the `ABSENT` route applies; **row 4's
   ownership is otherwise untouched**.
8. §P1-14.6: add the rule that the autonomous freeze path is reachable **only**
   from the `PEER_EOF` site; **retain `S-12` unchanged**.
9. §P1-15: add test rows for the ordering, the scope, each race, and the
   absent-witness routing.

### If neither is signed

v1.2 stands with a second unimplementable obligation. No implementation may
begin: a conforming build cannot satisfy C1's freeze requirement, and a build
that tries fails `S-12`.

---

## §9. Negative space

This packet creates nothing executable and authorizes no selection, X/Y verdict,
implementation, commit, verifier or manifest edit, process, socket, pipe, fork,
exec, signal, wait or `prctl` operation, supervisor, PCS, controller, worker or
watchdog, capability, world, learner, entropy, capacity artifact, custody
disposition, result manifest, spend, datum, outcome, Proof or claim movement. It
predicts no qualification and no comparison outcome. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
