# Officina P1 process-claim identity — author choice packet v1 (draft)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This packet selects nothing.** It
states a bounded choice for Kirill and the mechanical consequences of each
branch, so that the selection can be made on evidence rather than on prose.

**No token in this packet is signable.** Every token below becomes signable only
after a bounded independent X-line and Y-line review confirms this packet on
identical bytes. T is `NOT_ACTIVATED`; the programme claim is `OPEN`. This
document creates nothing executable and authorizes no implementation.

---

## §1. The conflict, re-derived independently

The v1.2 closure's diagnosis was treated as untrusted and re-established from
the accepted contracts. **The conflict is confirmed**, with one correction to
how v1.2 stated it (§1.5).

### §1.1 Signed requirement A — the claim needs two integers

`philosophia.officina.t-process-claim.v1` has exactly twenty keys, fixed by the
T activation protocol
(`successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:233-238`), among
them:

```text
controller_pid            integer
controller_start_identity integer
process_group_id          integer
```

Path: `successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json`
(same file, line 83). Written by the generic-harness peer layer executing in
the supervisor process, after `AWAIT_STOP` returns `STOPPED`.

`process_group_id` is load-bearing, not decorative. The freeze-evidence
acceptance predicate dereferences it — §Z4.6 conjunct 7,
`…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md:1047`:

> `pgid == the claim's process_group_id and start_identity == the claim's …`

`t-active-lease.v1` is defined as "the claim keys plus" five more
(`…ACTIVATION_PROTOCOL_V2_CORRECTION.md:240-245`), so both integers propagate
into the lease and into every route that reads it.

### §1.2 Signed requirement B — the supervisor holds no numeric identity

Kirill's signature,
`successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26`:

> "The contaminated supervisor receives opaque handles only. It cannot express
> a PID and does not call `fork`, `Popen`, `waitpid`, `kill`, or `killpg` on a
> result-bearing path."

Derived mechanically in the binding,
`…V2_1_10_4_P1_BINDING.md:156-158`:

> "**The supervisor holds opaque handles only.** `t-pcs.v1` has no PID field,
> so the supervisor cannot express a PID…"

### §1.3 The protocol exposes no number — exhaustive

Every response operand of all nine signed opcodes:

| Opcode | Response operands | Any numeric process identity? |
|---|---|---|
| `SPAWN_ROLE` | `handle_id` | no — an opaque handle |
| `SPAWN_WATCHDOG` | `handle_id` | no |
| `AWAIT_STOP` | `outcome`, `start_identity`, `pgid_is_leader` | **no** — see below |
| `SIGNAL_ROLE` | `result` token | no |
| `SIGNAL_GROUP` | `result` token | no |
| `REAP_ROLE` | one of six classifier tokens | no |
| `RELEASE_HANDLE` | none | no |
| `SHUTDOWN` | none | no |
| `PING` | `pcs_uptime_ticks` | no |

Source for the `AWAIT_STOP` row: `…V2_1_10_2_CORRECTION.md:366`, carried
byte-identically into v1 §C10.3, v1.1 §P1-8.3 and v1.2 §P1-8.3.

`start_identity` is the kernel start-time field, not a pid. `pgid_is_leader` is
a predicate over `{0,1}`: it decides whether the group id equals the process id
and **names neither**. Knowing the two are equal is worthless when neither is
available.

### §1.4 Every other candidate route, tested and excluded

| Candidate source | Verdict |
|---|---|
| the four singleton spawn records of §P1-5.1 | they name the PCS, the middle and the supervisor. **No controller or worker pid appears in any of them.** |
| `t-fork-child.v1` at `WATCHDOG/WATCHDOG_CHILD.json` | records the pid of a **supervisor-forked** watchdog. Under P1 the supervisor never forks, so this record is itself P1-orphaned; and it never named a controller or worker. |
| the worker status pipe | the role self-stops at `A-12` **before any target behaviour and before writing anything**, and the claim must be written before the role resumes. Nothing has been written at claim time. |
| `os.getpgid` in the supervisor | requires a pid argument. Circular. |
| **§Z3.4 `/proc/*/cmdline` marker discovery** | **the only serious candidate; excluded — see §1.5** |

### §1.5 The correction to v1.2's diagnosis — §Z3.4

v1.2's closure asserted the peer layer "cannot obtain" the values. That is too
strong as stated, and this packet corrects it.

The accepted chain **does** contain a route by which a supervisor could obtain a
controller or worker pid without asking the PCS: §Z3.4, "Discovery predicate for
`exec`ing children" (`…V2_1_1_CORRECTION.md:758-778`), which scans
`/proc/<pid>/cmdline` and selects at fixed indices:

```text
len(cmdline) >= 13
cmdline[3] == "--officina-bootstrap"
cmdline[6] == "--officina-spawn-intent"
cmdline[7] == <spawn_intent_id hex>
```

**It is nevertheless not a live source, for two independent reasons.**

1. **Its fixed indices do not match the selected P1 argv layout, so it selects
   nothing.** v1.2 §P1-7.4 fixes the controller/worker argv as index 3 = `-E`,
   index 6 = `--officina-role`, index 12 = `--officina-spawn-intent`, index 13 =
   the hex. §Z3.4 requires `--officina-bootstrap` at index 3 and the marker
   keyword at index 6. Against any P1 role the predicate matches zero
   processes. §Z3.4 is a stale peer rule written against a pre-P1 argv.
2. **Its evidentiary basis was doctrinally deleted.** v2.1.10 removed argv as
   evidence outright (`…V2_1_10_CORRECTION.md:188`): "**No layer of this
   contract henceforth treats argv as evidence of a clean image, of a fresh
   `execve`, or of the executor set.**" Binding a durable claim's identity
   fields to a self-read `cmdline` is argv-as-evidence.

**Corrected statement of the conflict, which this packet uses throughout:**

> The signed P1 protocol exposes no numeric process identity to the peer layer,
> and the only other route in the accepted chain is stale against the selected
> argv layout and rests on an evidentiary basis the chain deleted. Therefore no
> **authorized, non-stale** source of `controller_pid` and `process_group_id`
> exists for the layer that must write them.

That §Z3.4 is stale against P1 is a **separate defect** in the peer chain. It is
recorded here and is not repaired by this packet.

### §1.6 Why neither contract can absorb the other silently

- **The PCS cannot write the claim.** It has no access to
  `activation_record_sha256`, `behavior_source_sha256`, `config_sha256`,
  `stack_sha256`, `numerical_mode_sha256`, `device_identity` or `device_units`
  — peer-layer science and configuration data. This is infeasible, not merely
  undecided.
- **The supervisor cannot obtain the numbers**, per §1.3 and §1.5.
- **Writing a sentinel** into a signed record that a freeze-acceptance predicate
  dereferences would be a fabrication.

---

## §2. Option A — observation-only, PCS-attested identity response

**`t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1` and §Z4.6
conjunct 7 are all left byte-untouched.** The P1 wire gains two read-only
attested integers whose sole authorized sink is the two existing claim keys.

### §2.1 Which response carries the tuple, and on which outcomes

`AWAIT_STOP`, and **only** when `outcome == STOPPED`. On `EXITED`, `TIMEOUT`,
and on every `REFUSED` / `INVALID` / `REPLAYED`-without-a-recorded-stop status,
both fields are the literal absent token `-`.

**Why only `STOPPED`:** only that branch authorizes a process claim. Emitting
numbers on a branch with no authorized consumer would create a data sink with no
purpose, which is exactly the surface an audit must minimise. This is a
deliberate minimality property, and test `A-T6` enforces it.

No other opcode gains any field. `SPAWN_ROLE`, `SPAWN_WATCHDOG`, `SIGNAL_ROLE`,
`SIGNAL_GROUP`, `REAP_ROLE`, `RELEASE_HANDLE`, `SHUTDOWN` and `PING` are
byte-identical to v1.2.

### §2.2 Exact field order and grammar

The two fields are **appended** after the existing operands, so every existing
parse position is stable and an old parser reading a fixed field count fails
closed rather than mis-parsing:

```text
AWAIT_STOP response, field order, exact:
  0  "philosophia.officina.t-pcs.v1"          literal
  1  "1"                                       protocol version
  2  generation_id                             64 lowercase hex
  3  request_id                                decimal, 1..19 digits, no
                                               leading zero
  4  status                                    OK | REFUSED | INVALID | REPLAYED
  5  detail                                    one token of §P1-2.6
  6  handle_id                                 decimal, or "-"
  7  fds_redelivered                           "0" | "1"
  8  outcome                                   STOPPED | EXITED | TIMEOUT
  9  start_identity                            decimal, 1..20 digits
 10  pgid_is_leader                            "0" | "1"
 11  attested_pid                              decimal, or "-"        NEW
 12  attested_pgid                             decimal, or "-"        NEW

attested_pid / attested_pgid grammar when present:
  bytes drawn from [0-9] only; 1..7 digits; no leading zero; value >= 1
  the two fields are either BOTH "-" or BOTH present. A response with exactly
  one present is TRANSPORT_STRUCTURAL and is never accepted.
```

**Frame-size impact.** Worst case adds `2 x 7` payload bytes plus two `0x20`
separators = **16 bytes**. `T_CONTROL_FRAME_MAX_BYTES` is 4096 and the
`AWAIT_STOP` response is far below it, so no frame may be pushed over the
ceiling by this change. `SOCK_SEQPACKET` record semantics are untouched.

**Relationship to the existing operands.**

| Existing operand | Relationship |
|---|---|
| `handle_id` | remains the **only addressable name**. Nothing in the request grammar changes. `attested_pid` is never a selector. |
| `start_identity` | unchanged in meaning. Invariant: `attested_pid` is exactly the pid whose `/proc` start identity equals this field. |
| `pgid_is_leader` | **retained**, and becomes a redundancy check with a free cross-field invariant: `pgid_is_leader == "1"` if and only if `attested_pid == attested_pgid`. A response violating it is `TRANSPORT_STRUCTURAL`. Retaining it also keeps wire compatibility for any consumer that only needs the predicate. |

### §2.3 The PCS proof obligation

At the instant the PCS constructs a response carrying the tuple, **every**
conjunct must hold, evaluated in this order. Any failure emits `outcome` by the
normal classifier with both identity fields `-`. **A partial tuple is never
emitted.**

```text
A-P1. the handle's ownership is OWNED — never CONTRADICTED, never REAPED
A-P2. the single status-consuming site of S-24a — the targeted
      _waitpid(pid, WNOHANG|WUNTRACED) on the PCS's own direct child —
      returned exactly that pid with WIFSTOPPED true
A-P3. attested_pid is the value the PCS's OWN _posix_spawn returned for this
      handle. It is never read from /proc, never parsed from cmdline, and never
      taken from any peer artifact.
A-P4. attested_pgid is os.getpgid(attested_pid), read by the PCS immediately
      after A-P2. Because controllers and workers are spawned with setsid=True,
      attested_pgid == attested_pid MUST hold; any inequality is
      STRUCTURAL_VIOLATION, ownership becomes CONTRADICTED, and no tuple is
      emitted.
A-P5. STAT_OBSERVE(attested_pid) is PRESENT_VALID, its start identity equals
      the emitted start_identity, and its state field is T
A-P6. attested_pid is a direct child of the PCS. This follows from A-P3 plus
      TI-1 and is not re-derived from /proc.
```

**What A-P1 through A-P6 jointly prove:** both integers name the same stopped,
unreaped, direct-child process that the opaque handle denoted at this operation,
and its process group, at an instant at which that process provably holds its
pid. The attestation is the PCS's own construction record, not an observation
the contaminated supervisor could have influenced.

### §2.4 The sole allowed data sink

```text
The ONLY authorized consumers of attested_pid and attested_pgid are:
    t-process-claim.v1  key  controller_pid      <- attested_pid
    t-process-claim.v1  key  process_group_id    <- attested_pgid
There is no second sink. The values may not be logged, echoed into any other
record, placed in any frame the supervisor sends, compared against any handle,
used to select anything, or retained past the claim write.
```

### §2.5 The request grammar stays PID-free — restated as a closed rule

```text
A-R1. No request field of any of the nine opcodes may carry a PID or a PGID.
      The request grammar of v1.2 §P1-8.3 is byte-unchanged under Option A.
A-R2. Handle selection is by handle_id and by nothing else.
A-R3. Every signal target is a handle_id. No signal path accepts a number.
A-R4. The journal key is the pair (generation_id, request_id). No pid enters a
      journal key.
A-R5. The retry / replay key is the same pair. No pid enters a retry key.
A-R6. No author decision, selection, Q, C, blinding claim, or scientific or
      resource interpretation consumes either value.
```

### §2.6 Static, dataflow and runtime tests that the values cannot escape

New verifier rules, additions to the `S-` family:

```text
S-25a  each of the two response fields is parsed at exactly ONE site into
       exactly one plain Name binding; those two names are assigned once and
       never rebound
       ⇒ "S-25a: attested identity parsed at multiple sites"
S-25b  neither name, and no expression reading either name, appears as an
       argument to _kill, _killpg, _waitpid, os.kill, os.killpg, os.waitpid,
       or to any request-builder function
       ⇒ "S-25b: attested identity reaches a process-control primitive"
S-25c  neither name appears in a journal key, a retry key, a handle-table key,
       a handle-selection comparison, or any frame the supervisor sends
       ⇒ "S-25c: attested identity reaches a control-plane key"
S-25d  DATAFLOW: taint both names at their parse sites and propagate through
       assignment, arithmetic, formatting and container insertion. The taint
       set's only sink is the claim-record constructor's controller_pid and
       process_group_id arguments. Any other sink is a violation.
       ⇒ "S-25d: attested identity flows to an unauthorized sink"
       This is decidable because the supervisor's code lives in one reviewed
       root and both values are plain ints, never containers or callables.
```

New behavioural obligations:

```text
A-T1  the tuple is emitted on STOPPED and on no other outcome
A-T2  A-P1..A-P6 each reject a bit-exact negative fixture; a fixture in which
      getpgid disagrees with the spawn-time pid yields STRUCTURAL_VIOLATION and
      no tuple
A-T3  a response with exactly one of the two fields present is
      TRANSPORT_STRUCTURAL
A-T4  the cross-field invariant of §2.2 holds on every accepted response
A-T5  FAULT INJECTION: a build that passes attested_pid to a request builder,
      to a signal path, or to os.kill is REJECTED STATICALLY by S-25b/S-25d,
      and the test asserts the rejection rather than the absence of an effect
A-T6  no response for any opcode other than AWAIT_STOP carries either field
A-T7  frame size: the largest legal AWAIT_STOP response is under
      T_CONTROL_FRAME_MAX_BYTES with margin, computed and asserted
```

### §2.7 Replay and B1

```text
The tuple is part of the recorded response of the J4 COMPLETED journal entry,
exactly as start_identity already is.

REPLAY of a COMPLETED or ACKED entry:
  return the RECORDED tuple bytes, with status REPLAYED and fds_redelivered 0.
  The PCS MUST NOT re-evaluate A-P1..A-P6 on replay. A replay is a redelivery
  of a recorded reply, NEVER a fresh observation.
  This is required, not merely economical: after the handle reaches REAPED,
  re-running A-P2 would violate WAIT_ONE's precondition, and getpgid on a
  reaped pid may name an unrelated process.

REPLAY of an ACCEPTED entry (crash between J2 and J4):
  INVALID with OPERATION_INCONCLUSIVE, and NO TUPLE. No claim can be written
  from an inconclusive stop.
```

This preserves B1 exactly as signed: the byte record is redeliverable, and
nothing about the descriptor-non-redelivery narrowing changes, because this
response carries no descriptors.

### §2.8 PID reuse and start-identity binding

The tuple is emitted only while ownership is `OWNED` and the target is an
unreaped stopped direct child. By the §P1-10.1 reuse proof — `SIGCHLD` was
normalized to `SIG_DFL` with neither `SIG_IGN` nor `SA_NOCLDWAIT` **before the
child existed**, so the task holds its pid until the PCS's own targeted reap —
the pid cannot be reassigned between attestation and use.

**No new predicate is needed downstream.** The claim records
`controller_start_identity` beside `controller_pid`, and §Z4.6 conjunct 7
already compares **both** pgid and start identity. A recycled pid therefore
fails the existing predicate unchanged.

### §2.9 Crash cuts

| Cut | Continuation |
|---|---|
| crash after `J2`, before `J3` | `ACCEPTED` ⇒ inconclusive ⇒ no tuple ⇒ no claim; generation invalidity |
| crash after `J3`, before `J4` | `ACCEPTED` ⇒ as above, and the role may be stopped; the generation is invalid and no claim is written |
| crash after `J4`, before `J5` | `COMPLETED` durable; a redelivery returns the recorded tuple with no re-observation |
| crash after `J5`, before the peer's claim write | redelivery returns the recorded tuple; the claim install is no-replace, so the peer converges |
| crash after the claim write, before the ack | the claim is durable; redelivery returns the same tuple; the second install is an `EEXIST` no-op |
| PCS death at any point | whole-generation invalidity per §P1-11.4; no claim is written and no tuple survives outside the journal |
| supervisor death holding the tuple | the values die with the address space; they were never durable outside the journal and the claim |

### §2.10 The exact amendment to the signed sentence

**This is a bounded weakening. It is not equivalent to the old phrase and this
packet does not present it as such.**

```text
SIGNED TODAY (…PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26):
  "The contaminated supervisor receives opaque handles only. It cannot express
   a PID and does not call fork, Popen, waitpid, kill, or killpg on a
   result-bearing path."

PROPOSED UNDER OPTION A:
  "The contaminated supervisor receives opaque handles only. It cannot
   ADDRESS, SELECT, or COMMAND a process by PID, and no process-control
   request contains a PID. It may receive a PCS-attested numeric PID/PGID
   tuple ONLY as read-only evidence for the already signed process-claim
   fields; those values have no authorized control-plane sink. It does not
   call fork, Popen, waitpid, kill, or killpg on any path."

TOKEN FOR THE WEAKENING:
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

**What is given up, stated plainly.** Today the property is *lexical*: no PID
exists anywhere in the supervisor, checkable by a single static rule. After A
the property becomes a *dataflow* property: PIDs exist and are proved to reach
exactly one sink. A dataflow property is strictly harder to verify and strictly
easier to regress. **That, and not any change in kernel capability, is the real
cost of Option A** (see §5).

---

## §3. Option B — identity remains behind the P1 boundary

### §3.1 The single coherent specification

Numeric identity never enters the supervisor. The claim carries an opaque handle
plus a digest of a PCS-written binding artifact.

```text
NEW peer schema:  philosophia.officina.t-process-claim.v2
  the twenty v1 keys, with
      controller_pid        REMOVED
      process_group_id      REMOVED
  and
      controller_handle_id      decimal, the P1 handle
      identity_binding_sha256   64 lowercase hex
  added, giving twenty keys again.

NEW P1-owned artifact:
  runtime_control/T_SUPERVISOR/IDENTITY_BINDINGS/<identity_binding_sha256>.json
  schema philosophia.officina.t-process-identity-binding.v1
  atomic no-replace, written by the PCS, keys exactly:
    schema, scientific_outcome, supervisor_generation_sha256, handle_id,
    pid, pgid, start_identity, created_utc
  identity_binding_sha256 = SHA-256 of the canonical bytes without that field.
```

### §3.2 Every reader that must change

| Surface | Required change |
|---|---|
| `t-process-claim.v1` | superseded by `.v2`; every constructor and validator |
| `t-active-lease.v1` | defined as "the claim keys plus five", so it **mechanically** becomes `.v2` |
| `t-process-record.v1` | the final record inherits the same key change |
| §Z4.6 conjunct 7 | must **dereference the binding artifact** instead of reading two claim keys |
| freeze witness `pgid` field | the watchdog's witness still carries a numeric `pgid`; its source is unaffected by B and remains open (§6) |
| `process_id` / lease ids / hashes | must be confirmed not to include either removed key in their preimage |
| batch settlement, archive, verification | every reader of leases and records |
| migration | **none required.** T is `NOT_ACTIVATED` and no production claim, lease or record exists, so there is no durable evidence to migrate. This is a genuine advantage of B and is stated as such. |

### §3.3 Why B is **NOT SELECTABLE** in this packet

B cannot be made single-valued without at least two further author decisions
that this packet must not make:

```text
SUB-CELL B-1: does the PCS gain a filesystem-write role for peer-visible
  artifacts?
  Under v1.2 the PCS writes exactly the four singleton spawn records and its
  own journal. The binding artifact is a fifth, peer-visible, PCS-written
  object. Granting it expands the PCS's durable-write surface, which is a
  signed property of the selected architecture. The alternative — the
  supervisor writes the binding from an attested response — COLLAPSES B INTO A
  and is therefore not an alternative at all.

SUB-CELL B-2: may a peer-owned validity predicate read a P1-owned artifact?
  Making §Z4.6 conjunct 7 dereference the binding inverts rule R-L4 of v1.2
  §P1-13.0, which fixes the co-resident call direction as one-way, peer into
  P1, through the nine opcodes and nothing else. A peer predicate that opens a
  P1-owned file crosses that boundary in the opposite direction and needs its
  own signature.
```

**Therefore B is presented, fully specified, and marked non-selectable.** Kirill
may still direct B; doing so opens sub-cells `B-1` and `B-2` and requires a
further packet before any composite can bind it.

---

## §4. Option C — examined and rejected, not offered

For completeness of the search, and because a reviewer will otherwise ask:
re-index §Z3.4's `/proc/*/cmdline` predicate to the P1 argv layout and let the
supervisor discover the pid itself.

**Not offered as an option**, for reasons that are not preference:

1. it makes the supervisor's own unattested observation the identity source,
   with no PCS proof that the discovered pid is the handle's process;
2. it is argv-as-evidence, deleted outright by `…V2_1_10_CORRECTION.md:188`;
3. it is strictly dominated by A: same numeric exposure, weaker proof;
4. it hands the contaminated supervisor a pid it discovered by its own scan,
   which is the one thing both A and B are trying to avoid authorizing.

It is recorded here so the packet's search is auditable, not to create symmetry.

---

## §5. Comparative audit

### §5.1 Signed sentences and contracts touched

| | Option A | Option B |
|---|---|---|
| **amended** | one sentence of the P1 process-authority signature (§2.10), under token `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`; the `AWAIT_STOP` response grammar | `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1`, §Z4.6 conjunct 7, the PCS write surface, `R-L4` |
| **untouched** | `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1`, §Z4.6 conjunct 7, every request grammar, A3/B1/C1/D1/K1, the whole descriptor and journal surface | the P1 signature sentence; the request and response grammars |
| **validity predicates reopened** | **zero** | **at least one signed acceptance predicate**, plus every lease and record reader |

### §5.2 A3 authority and confidentiality

Answered in full at §5.6.

### §5.3 B1 replay and crash semantics

| | Option A | Option B |
|---|---|---|
| replay | the tuple rides in the recorded `COMPLETED` response; a replay returns recorded bytes and **must not** re-observe (§2.7) | the binding digest is stable; the artifact is no-replace, so replay is naturally idempotent |
| `ACCEPTED` crash | no tuple, no claim | no binding consumed, no claim |
| new failure mode | a replay implemented as a re-observation would violate `WAIT_ONE`'s post-`REAPED` precondition — hence the explicit prohibition and test | a binding artifact durable with no claim, requiring a garbage-collection rule that does not yet exist |

### §5.4 Code, verifier, test and manifest surface

| | Option A | Option B |
|---|---|---|
| PCS root | build the tuple under `A-P1`..`A-P6` | write a fifth durable artifact class |
| supervisor code | parse two fields; pass to the claim constructor | new claim `.v2` constructor; dereference bindings |
| verifier | `S-25a`–`S-25d` | new schema validators for three record classes; a new predicate for conjunct 7 |
| tests | `A-T1`–`A-T7` | full re-validation of claim, lease, record, settlement and archive readers |
| manifest | unchanged beyond the composite digests | unchanged beyond the composite digests |

### §5.5 Blast radius and rollback

| | Option A | Option B |
|---|---|---|
| blast radius | one opcode's response, one signature sentence, four verifier rules | four schemas, one signed predicate, one architectural rule, every downstream reader |
| rollback | delete two response fields and the four rules; nothing durable changes shape | revert three record schemas; any durable object already written in `.v2` shape is stranded |
| migration | none — nothing durable changes shape | none **today**, because `T` is `NOT_ACTIVATED`; after activation it would be large |

### §5.6 Does observing a PID grant process authority under A3?

**No.** Three things are routinely conflated and must be separated.

**1. OS information.** A pid is a small integer that any same-UID process may
read from `/proc` at any time. Under the A3 threat model the supervisor is
same-UID with every process in this contract and **already may read every pid
on the system unilaterally**. The attested tuple therefore conveys **zero**
operating-system information the supervisor could not obtain without it. What it
adds is *provenance*: a number the PCS vouches for, rather than one the
supervisor scraped.

**2. Authorized addressing.** What P1 removed is the supervisor's *authorized*
ability to name a process as an operation target: no request field accepts a
PID, every operation is selected by a PCS-issued handle, and every signal and
wait executes in the PCS. **Option A does not touch any of this.** It adds a
response field with no request counterpart, and `A-R1`–`A-R6` close the request
side explicitly.

**3. Same-UID adversarial capability.** Under A3 a contaminated supervisor can
already call `kill(any_pid)` directly; the kernel permits it and this contract
has never claimed otherwise. v1.2 §P1-12.3 states it affirmatively: a same-UID
actor "can … stop, kill, or delay any same-UID process, with or without
adoption". **P1's guarantee was never that the supervisor lacks the kernel
power; it was that no Officina route authorizes its use and no Officina decision
consumes its result.** That guarantee — safety properties `S2` and `S3` — is
unchanged by Option A, because the tuple carries no capability and feeds exactly
one already-signed data sink.

**The honest summary.** Option A weakens the **English sentence** in the
signature. It does **not** weaken the **safety property**, and it does not
change what a hostile same-UID actor can do. What it genuinely costs is
**testability**: an invariant that is today lexical and checkable by one static
rule becomes a dataflow invariant checkable only by `S-25a`–`S-25d`. A reviewer
should weigh that cost, not a fictional capability transfer.

### §5.7 Scientific and resource interpretation

**Neither option changes any scientific or resource interpretation.** Both
integers are control-plane infrastructure facts. Under A they enter exactly two
keys of a record whose `scientific_outcome` is the literal `false` and which is
recursively scientific-field-rejecting. Neither is a datum, an outcome, a
capacity fact, a custody disposition, a spend fact, or an input to
qualification, comparison or blinding. `A-R6` states this as a closed rule.

### §5.8 Counterexample prevented, residual created

| | Option A | Option B |
|---|---|---|
| **prevents** | a conforming implementation that cannot write a valid process claim at all, and the alternative failure in which an implementer invents a sentinel for `process_group_id` that then silently fails §Z4.6 conjunct 7 for every freeze witness in the generation | the same, plus any future route that could smuggle a pid into the supervisor |
| **new residual** | two integers exist in a contaminated address space. They confer nothing (§5.6) but they make the no-PID invariant dataflow-checkable rather than lexical, so a future edit could add a second sink and pass a naive review | a durable P1-owned artifact that a peer predicate must dereference, inverting `R-L4` and creating a cross-layer read that did not previously exist |

---

## §6. Scope boundary — an orthogonal defect neither option resolves

While re-deriving the conflict, a **second, independent** defect of the same
root class was found. It is recorded so that it is not silently absorbed into
whichever option is selected.

```text
Under P1 the watchdog cannot execute a freeze.

  - §P1B.8.1 of the binding, and v1.2 §P1-9.2 property 12, both require that on
    update-pipe EOF the watchdog "freezes all known groups", which is a
    killpg(SIGSTOP) plus a quiescence proof;
  - P1 gives ALL process authority to the PCS;
  - the watchdog's slot map is {3,4,5,7,8,9,10} with slot 6 explicitly closed
    by a file action, so it holds NO PCS socket and cannot request
    SIGNAL_GROUP;
  - it acts precisely when the supervisor is already dead, so no relay exists.

Its freeze witness also carries a numeric `pgid` key, whose source is the same
open question as the claim's process_group_id.
```

**Neither Option A nor Option B resolves this.** A attests numbers to the
*supervisor*, which is dead at that moment and has no channel to the watchdog. B
keeps numbers behind the boundary but supplies the watchdog with no mechanism
either. The defect is orthogonal to this choice, and selecting A or B neither
fixes nor worsens it.

It requires its own author cell, provisionally
`AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`. **It is not opened by this packet
and no option here should be read as addressing it.**

---

## §7. Recommendation

Based **only** on the three stated criteria — preserving already signed schemas,
minimizing reopened validity predicates, and keeping the authority boundary
testable — and predicting no outcome and optimizing toward no qualification:

> **Option A is recommended, unless the independent audit disproves §5.6.**

| Criterion | A | B |
|---|---|---|
| preserves already signed schemas | **yes — all four untouched** | no — three record schemas superseded |
| reopened validity predicates | **zero** | at least §Z4.6 conjunct 7, plus every lease and record reader |
| authority boundary testable | degraded from lexical to dataflow, **but mechanically closed** by `S-25a`–`S-25d` plus the `A-T5` fault injection | boundary stays lexical, but `R-L4` is inverted and a new cross-layer read appears |
| selectable today | yes | **no** — blocked behind sub-cells `B-1` and `B-2` |

The recommendation rests on the fact that A touches **one sentence and one
response grammar**, while B touches **four schemas and a signed acceptance
predicate** — and that A's single genuine cost, testability, is closable by
mechanical rules whose negative fixtures are specified in §2.6.

**This is a recommendation on stated criteria only. The author does not select.**

---

## §8. Tokens

Mutually exclusive. **Neither is signable until a bounded independent X-line and
Y-line review confirms this packet on identical bytes.**

```text
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
```

Selecting A additionally requires the bounded-weakening token of §2.10:

```text
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

Selecting B first requires sub-cells `B-1` and `B-2` (§3.3) and a further
packet. Until then B is **non-selectable**, and this packet says so rather than
offering a choice it cannot honour.

---

## §9. Negative space

This packet creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no process,
socket, pipe, fork, exec, signal, wait or `prctl` operation, no supervisor, PCS,
controller, worker or watchdog, no capability, world, learner, entropy, capacity
artifact, custody disposition, result manifest, spend, datum, outcome, Proof or
claim movement. It predicts no qualification and no comparison outcome. `T`
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
