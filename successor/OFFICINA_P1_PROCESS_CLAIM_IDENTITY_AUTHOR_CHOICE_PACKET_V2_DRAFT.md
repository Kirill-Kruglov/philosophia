# Officina P1 process-claim identity — author choice packet v2 (draft)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This packet selects nothing.** It
states a bounded choice for Kirill and the mechanical consequences of each
branch, so that the selection can be made on evidence rather than on prose.

**No token in this packet is signable.** Every token below becomes signable only
after a bounded independent X-line and Y-line confirmation round on identical
bytes. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`. This document
creates nothing executable and authorizes no implementation.

**Status.** v2 is a **self-contained replacement** for
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`.
It is not a patch and is not read alongside v1. v1 and both review files are
preserved byte-untouched as the evidentiary record of what was wrong.

**Bounded repair mandate.** v2 exists to close, one-to-one, the findings of two
independent reviews, both treated here as **binding defect reports**:

```text
X-line, reviews/opus_officina_p1_process_claim_identity_choice_review.md
        M-1, M-2, m-1, m-2, m-3
Y-line, reviews/sol_officina_p1_process_claim_identity_choice_review.md
        Y-C1, Y-C2, Y-M1, Y-M2, Y-m1
```

Nothing else in v1 was reopened. Where a review disproved a v1 sentence, v2
**withdraws** that sentence in the text rather than quietly restating it.

---

## §0. What v2 changes, and where

| Finding | Class | v2 locus | Nature of the repair |
|---|---|---|---|
| X M-1 | Major | §2.8, §2.10, §5.1, §5.4, §5.5, §7.1 | durable `J4` operand vector, byte-identical replay, journal schema added to A's blast radius and handoff; the "exactly as `start_identity` already is" premise **withdrawn** |
| X M-2 | Major | §2.5 | `S-25d` taint-completeness reliance **withdrawn**; replaced by a closed syntactic occurrence whitelist with a decidable verifier |
| X m-1 | Minor | §2.3 `A-P4` | fresh `getpgid` pinned authoritative; stored `pgid_or_null` pinned as a mandatory cross-check; single-valued |
| X m-2 | Minor | §2.2 | `PID_MAX_LIMIT = 4194304` pinned as provenance; explicit fail-closed on 8 digits and on any value above the limit |
| X m-3 | Minor | §6 | the two freeze inabilities separated by actor, trigger and citation |
| Y-C1 | Critical | §2.6 | "only durable sinks" **withdrawn**; restricted identity class, closed persistent-consumer whitelist, centralized accessors, recomputed schema-reader audit |
| Y-C2 | Critical | §2.8 | complete replayable representation and its `J4` durability made explicit; journal surface moved into the blast radius |
| Y-M1 | Major | §2.10 | post-claim PCS death retains the claim; `EEXIST` converges only after verified identity; invalidity dominance made record-first |
| Y-M2 | Major | §3.2, §5 | Option B's blast radius **recomputed**; the `t-process-record.v1` key-inheritance claim **withdrawn as false** |
| Y-m1 | Minor | §1.5, §4 | the argv-deletion rationale corrected to its actual scope; the route's unauthorized status re-grounded on reasons that hold |

**Withdrawn v1 sentences, named explicitly.** Four v1 statements are withdrawn
as unsupported or false. They are listed at §8.2 so that a reviewer can check
that none of them survives anywhere in v2 in paraphrase.

---

## §1. The conflict, re-derived independently

The v1.2 closure's diagnosis was treated as untrusted and re-established from
the accepted contracts. **The conflict is confirmed**, and both reviews
independently confirmed it. It remains real and loud.

### §1.1 Signed requirement A — the claim needs two integers

`philosophia.officina.t-process-claim.v1` has exactly twenty keys, fixed by the
T activation protocol
(`successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238`), among
them:

```text
controller_pid            integer
controller_start_identity integer
process_group_id          integer
```

Path: `successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json`
(same file, `:78-86`). Written by the generic-harness peer layer executing in
the supervisor process, after `AWAIT_STOP` returns `STOPPED`
(composite §P1-13.2 row 2, `…P1_OPERATIVE_COMPOSITE_V1_2.md:2098-2128`).

`process_group_id` is load-bearing, not decorative. The freeze-evidence
acceptance predicate dereferences it — §Z4.6 conjunct 7,
`…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md:1047`:

> `pgid == the claim's process_group_id and start_identity == the claim's …`

`t-active-lease.v1` is defined as "the claim keys plus" five more
(`…ACTIVATION_PROTOCOL_V2_CORRECTION.md:241-246`), so both integers propagate
into the lease. **This propagation is a signed requirement, not a leak**; v1
misdescribed it and §2.6 repairs that.

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

Recomputed from the signed opcode table at composite §P1-8.3
(`…P1_OPERATIVE_COMPOSITE_V1_2.md:1218-1228`), not from v1's table:

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

The composite states the same closure literally at `:1240`: "No field of any
request or response carries a PID, a descriptor number, a path, a target argv,
a signal number, a symbol, a callback, or an unbounded integer."

`start_identity` is the kernel start-time field, not a pid. `pgid_is_leader` is
a predicate over `{0,1}`: it decides whether the group id equals the process id
and **names neither**. Knowing the two are equal is worthless when neither is
available. The X line recomputed this enumeration independently and found it
exhaustive.

### §1.4 Every other candidate route, tested and excluded

| Candidate source | Verdict |
|---|---|
| the four singleton spawn records of §P1-5.1 (`:560-590`) | they name the **PCS** (`cli_pid`), the **middle** (`middle_child_pid`, and a `process_group_id` that §P1-5.2 `:604` defines as *the middle's* group), and the **supervisor** (`supervisor_pid`, `supervisor_pgid`). **No controller or worker pid appears in any of them.** See §2.6.5 on why the shared key *name* is not a shared value. |
| `t-fork-child.v1` at `WATCHDOG/WATCHDOG_CHILD.json` | records the pid of a **supervisor-forked** watchdog. Under P1 the supervisor never forks, so this record is itself P1-orphaned; and it never named a controller or worker. |
| the worker status pipe | the role self-stops at `A-12` **before any target behaviour and before writing anything**, and the claim must be written before the role resumes. Nothing has been written at claim time. |
| `os.getpgid` in the supervisor | requires a pid argument. Circular. |
| **§Z3.4 `/proc/*/cmdline` marker discovery** | **the only serious candidate; excluded — see §1.5** |

### §1.5 The correction to v1.2's diagnosis — §Z3.4, with the rationale repaired

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

**It is nevertheless not an authorized source.** v1 gave two reasons; the second
was **stated more broadly than its source supports**, and the Y line was right
to say so (`Y-m1`). v2 withdraws the overbroad form and states four reasons
that hold on the committed bytes:

```text
R-1  STALE INDICES. Composite §P1-7.4 (:961-990) fixes the role argv as
     index 3 = "-E", index 6 = "--officina-role", index 12 =
     "--officina-spawn-intent", index 13 = the hex. §Z3.4 requires
     "--officina-bootstrap" at 3 and the marker keyword at 6. Against any P1
     role the predicate matches ZERO processes. §Z3.4 is a stale peer rule
     written against a pre-P1 argv.

R-2  UNATTESTED SELF-SCAN. The value would be the contaminated supervisor's own
     observation, with no PCS proof binding the discovered pid to the handle
     that denotes the process. Nothing in the chain converts a self-scan into
     an ownership-bound identity.

R-3  AUTHORITY BYPASS. §Z3.4's own text (:773-776) kills by
     killpg(SIGTERM)/killpg(SIGKILL) on the discovered pid. Under P1, all
     numeric process authority is the PCS's (composite §P1-13.0, :1993-1995),
     handle selection is the only addressing (§P1-8.3, :1240), and the peer
     layer reaches P1 only through the nine opcodes (R-L4, :2022-2027).
     Re-indexing §Z3.4 would revive a direct pid-to-killpg route outside that
     interface.

R-4  NARROWED EVIDENTIARY BASIS. v2.1.10 (…V2_1_10_CORRECTION.md:188) deletes
     argv as evidence "of a clean image, of a fresh execve, or of the executor
     set". THAT IS THE EXACT SCOPE OF THE DELETION. It does not literally
     delete every argv-derived identity use, and v2 does not claim it does.
     What it removes is the corroboration §Z3.4's fixed-index anti-spoof
     argument leans on, so R-4 weakens the route rather than closing it alone.
     R-1, R-2 and R-3 close it independently of R-4.
```

**Corrected statement of the conflict, which this packet uses throughout:**

> The signed P1 protocol exposes no numeric process identity to the peer layer,
> and the only other route in the accepted chain is stale against the selected
> argv layout, unattested, and outside P1's handle-only, PCS-mediated authority.
> Therefore no **authorized, non-stale** source of `controller_pid` and
> `process_group_id` exists for the layer that must write them.

That §Z3.4 is stale against P1 is a **separate defect** in the peer chain. It is
recorded here and is not repaired by this packet. Both reviews agreed on this
disposition.

### §1.6 Why neither contract can absorb the other silently

- **The PCS cannot write the claim.** It has no access to
  `activation_record_sha256`, `behavior_source_sha256`, `config_sha256`,
  `stack_sha256`, `numerical_mode_sha256`, `device_identity` or `device_units`
  — peer-layer science and configuration data. Composite row 2 states it
  directly (`:2119`): "fields P1 reads: none. The P1 layer opens this record on
  no path." This is infeasible, not merely undecided.
- **The supervisor cannot obtain the numbers**, per §1.3 and §1.5.
- **Writing a sentinel** into a signed record that a freeze-acceptance predicate
  dereferences would be a fabrication, and would silently fail §Z4.6 conjunct 7
  for every freeze witness in the generation.

---

## §2. Option A — observation-only, PCS-attested identity response

**`t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1` and §Z4.6
conjunct 7 are all left byte-untouched.** The P1 wire gains two read-only
attested integers. Their admission is governed by two distinct boundaries,
which v1 conflated into one and which v2 separates:

```text
IMMEDIATE-USE BOUNDARY   (§2.5)  what the two parsed wire Names may syntactically
                                 do, before anything is durable
PERSISTENT-USE BOUNDARY  (§2.6)  what the two DURABLE KEYS, and every reload or
                                 alias of them, may do afterwards
```

Conflating them is what made v1's §2.4 false. They are now specified
separately, with separate rules and separate verifiers.

### §2.1 Which response carries the tuple, and on which outcomes

`AWAIT_STOP`, and **only** when `outcome == STOPPED`. On `EXITED`, `TIMEOUT`,
and on every `REFUSED` / `INVALID` / `REPLAYED`-without-a-recorded-stop status,
both fields are the literal absent token `-`.

**Why only `STOPPED`:** only that branch authorizes a process claim (composite
row 2 `:2120`, "written only after AWAIT_STOP returns STOPPED"). Emitting
numbers on a branch with no authorized consumer would create a data sink with no
purpose, which is exactly the surface an audit must minimise. This is a
deliberate minimality property, and test `A-T1` enforces it.

No other opcode gains any field. `SPAWN_ROLE`, `SPAWN_WATCHDOG`, `SIGNAL_ROLE`,
`SIGNAL_GROUP`, `REAP_ROLE`, `RELEASE_HANDLE`, `SHUTDOWN` and `PING` are
byte-identical to v1.2.

### §2.2 Exact field order, grammar, and the pinned numeric bound

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
```

**Grammar and bound for the two new fields (repairs `X m-2`).**

```text
G-1  bytes drawn from [0-9] only; no sign, no whitespace, no leading zero
G-2  length in 1..7 bytes inclusive
G-3  integer value V satisfies  1 <= V <= 4194304
G-4  the two fields are either BOTH "-" or BOTH present. A response with
     exactly one present is TRANSPORT_STRUCTURAL and is never accepted.
G-5  a token of 8 or more digits FAILS CLOSED as TRANSPORT_STRUCTURAL. It is
     never truncated, never parsed with a wider field, and never accepted.
G-6  a 7-digit token whose value exceeds 4194304 FAILS CLOSED the same way.
```

**Provenance of the bound, pinned rather than assumed.** On Linux the kernel
constant `PID_MAX_LIMIT` is `0x400000 = 4194304`, and `/proc/sys/kernel/pid_max`
is refused above it. The maximum pid is therefore seven decimal digits, and
`G-2` is exactly adequate rather than a field-width guess. `G-3`, `G-5` and
`G-6` make the packet fail closed if that premise is ever false on some
deployment, instead of silently truncating. **This is a stated platform
premise of Option A**: if `PID_MAX_LIMIT` were ever raised, `G-2`/`G-3` must be
re-derived before any implementation, and the fail-closed rules guarantee the
failure is loud.

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
      (§P1-10.1, composite :1519-1538)
A-P2. the single status-consuming site of S-24a — the targeted
      _waitpid(pid, WNOHANG|WUNTRACED) on the PCS's own direct child —
      returned exactly that pid with WIFSTOPPED true
A-P3. attested_pid is the value the PCS's OWN _posix_spawn returned for this
      handle, as recorded in the handle table's `pid` field (§P1-8.5, :1256).
      It is never read from /proc, never parsed from cmdline, and never taken
      from any peer artifact.
A-P4. attested_pgid is os.getpgid(attested_pid), READ FRESH BY THE PCS
      IMMEDIATELY AFTER A-P2. See the single-valued rule below.
A-P5. STAT_OBSERVE(attested_pid) is PRESENT_VALID (§P1-10.3, :1600-1626), its
      start identity equals the emitted start_identity, and its state field is T
A-P6. attested_pid is a direct child of the PCS. This follows from A-P3 plus
      TI-1 and is not re-derived from /proc.
```

**`A-P4` is single-valued (repairs `X m-1`).** The handle table already holds
`pgid_or_null` (§P1-8.5, `:1256-1262`). Two candidate sources therefore exist,
and an implementer must not be free to choose. v2 pins:

```text
A-P4a  THE FRESH READ IS AUTHORITATIVE. attested_pgid is exactly the return of
       os.getpgid(attested_pid) evaluated in the PCS immediately after A-P2,
       while ownership is OWNED and the child is stopped and unreaped.
       WHY: the durable claim binds identity AT THE STOP INSTANT, and it is
       that value against which §Z4.6 conjunct 7 will later compare a freeze
       witness. The stored pgid_or_null is (i) nullable by its own name, so it
       is not always available, and (ii) recorded at an earlier instant that
       the schema does not tie to the stop. An authoritative value must be
       read at the instant it is attested.
A-P4b  THE STORED VALUE IS A MANDATORY CROSS-CHECK WHEN NON-NULL. If
       pgid_or_null is not null and differs from the fresh read, the result is
       STRUCTURAL_VIOLATION, ownership becomes CONTRADICTED, and NO TUPLE is
       emitted. A null stored value is not a failure and imposes no check.
A-P4c  THE setsid EQUALITY IS ALSO MANDATORY. Controllers and workers are
       spawned with setsid=True (composite :480-481), so
       attested_pgid == attested_pid MUST hold; any inequality is
       STRUCTURAL_VIOLATION, ownership becomes CONTRADICTED, and no tuple is
       emitted.
A-P4d  NO OTHER SOURCE EXISTS. No implementation may substitute the stored
       value for the fresh read, take the pgid from /proc, or infer it from
       pgid_is_leader.
```

`A-P4c` is not subvertible by the payload: the role self-stops at `A-12`
**before** any target argv runs (§P1-7.4), so the contaminated target cannot
have called `setpgid` before the attestation instant. The X line verified this
ordering independently and found that it *strengthens* the proof.

**What `A-P1` through `A-P6` jointly prove:** both integers name the same
stopped, unreaped, direct-child process that the opaque handle denoted at this
operation, and its process group, at an instant at which that process provably
holds its pid. The attestation is the PCS's own construction record, not an
observation the contaminated supervisor could have influenced.

### §2.4 The v1 sole-sink rule is withdrawn

```text
WITHDRAWN, v1 §2.4, verbatim:
  "The ONLY authorized consumers of attested_pid and attested_pgid are:
       t-process-claim.v1  key  controller_pid      <- attested_pid
       t-process-claim.v1  key  process_group_id    <- attested_pgid
   There is no second sink. The values may not be logged, echoed into any other
   record, placed in any frame the supervisor sends, compared against any
   handle, used to select anything, or retained past the claim write."

WHY IT IS FALSE: the signed activation protocol defines t-active-lease.v1 as
"the claim keys plus" five (:241-246), so a VALID LEASE NECESSARILY REPEATS
BOTH KEYS — that is a second durable location, mandated by signature. And §Z4.6
conjunct 7 (:1047) READS process_group_id from the durable claim after the
write, so "retained past the claim write" is not merely permitted but required.
The Y line established both points and v2 accepts them without reservation.
```

The correct specification is two boundaries, §2.5 and §2.6.

### §2.5 Immediate-use boundary — a closed syntactic whitelist (repairs `X M-2`)

```text
WITHDRAWN, v1 §2.6 rule S-25d and its justification:
  the dataflow/taint rule, and the sentence "This is decidable because the
  supervisor's code lives in one reviewed root and both values are plain ints,
  never containers or callables."

WHY IT IS INSUFFICIENT: the enumerated propagation classes (assignment,
arithmetic, formatting, container insertion) are not closed under Python
semantics. Function/lambda application, iterable unpacking, comprehension
binding, and builtin round-trips such as int(str(x)) all produce a fresh
binding outside those four classes. Asserting completeness is not proving it,
and Option A's whole safety delta rested on it.
```

v2 does not attempt a sound taint analysis. It replaces the obligation with a
**positional occurrence whitelist**: each governed Name may appear in the parsed
AST in exactly the enumerated positions and in no other, and the verifier
**counts occurrences** rather than classifying propagation. A construct that
was never anticipated is rejected **because it is not in the list**, not
because it appears in a list of prohibitions. That is what makes the rule
closed; the prohibition catalogue at §2.5.4 is illustrative and normatively
redundant.

#### §2.5.1 The two zones

```text
ZONE 1 — THE PARSE SITE. Exactly one function in
  src/philosophia/officina/generic_harness.py:
      _identity_from_await_stop(fields) -> (int, int) | (None, None)
  It is the ONLY place either wire token is read, validated, or converted.

ZONE 2 — EVERYWHERE ELSE. The two ints returned by Zone 1 are bound to exactly
  two plain Names, each assigned once and never rebound, and each appears in
  exactly ONE further syntactic position: as the value of its named keyword
  argument of the single process-claim constructor call.
```

#### §2.5.2 Zone 1 — the exact closed operation list

Inside `_identity_from_await_stop`, the two raw byte tokens are bound once to
the plain Names `raw_pid` and `raw_pgid` from the field vector. Those two Names
may appear **only** in the following expression forms, and each form only for
the mandatory structural or cross-field validation it names. This is the
complete list of exceptions the packet grants:

```text
V-1  raw_pid == b"-"                    absent-token test         (both-or-neither)
V-2  raw_pgid == b"-"                   absent-token test         (both-or-neither)
V-3  _BUILTIN_len(raw_pid) and _BUILTIN_len(raw_pgid), each compared against
     the integer literals 1 and 7                                 (G-2)
V-4  a membership test of each byte of the token against the literal byte set
     b"0123456789", expressed as a bounded index loop over range(len(...))
     whose only other operand is that literal                     (G-1)
V-5  raw_pid[0:1] == b"0" and raw_pgid[0:1] == b"0"               (G-1, leading zero)
V-6  int(raw_pid) and int(raw_pgid), EACH APPEARING EXACTLY ONCE  (the sole cast)
V-7  the two ints from V-6 compared against the integer literals 1 and 4194304
                                                                  (G-3, G-6)
V-8  the two ints from V-6 compared to each other for equality, and that boolean
     compared against pgid_is_leader                              (cross-field §2.2)
V-9  the two ints from V-6 compared against the emitted start_identity's
     companion checks ONLY as the tuple returned to Zone 2; no further operation
```

```text
Z1-R1  raw_pid and raw_pgid appear in V-1..V-5 and NOWHERE ELSE.
Z1-R2  int() is applied to each raw token exactly once, at V-6, and is the only
       cast, coercion or conversion applied to either token anywhere.
Z1-R3  the two ints appear in V-7, V-8, and the single return tuple, and
       NOWHERE ELSE inside Zone 1.
Z1-R4  the function returns either (int, int) or (None, None). It never returns
       a partial pair, never raises past its own validation, and never returns a
       container, mapping, string, or object other than that 2-tuple.
Z1-R5  the function performs no I/O, no os call, no logging call, no formatting,
       and constructs no record.
Z1-R6  any validation failure returns (None, None) and drives the caller to the
       TRANSPORT_STRUCTURAL route of §2.10; it never returns a defaulted,
       clamped, truncated or substituted number.
```

#### §2.5.3 Zone 2 — exactly one position each

```text
Z2-R1  the return of _identity_from_await_stop is unpacked at exactly ONE call
       site, into exactly two plain Names, `attested_pid` and `attested_pgid`.
Z2-R2  each Name is the target of exactly one Assign, and of no AugAssign,
       AnnAssign, Del, for-target, with-target, except-target, parameter,
       comprehension target, or Starred target.
Z2-R3  each Name occurs on the right-hand side exactly TWICE in the whole
       production closure: once in the mandatory None-guard comparison
       `attested_pid is None` (respectively `attested_pgid is None`), and once
       as the VALUE of its named keyword argument of the single
       process-claim constructor call:
           controller_pid   = attested_pid
           process_group_id = attested_pgid
Z2-R4  the total occurrence count of each Name in the parsed AST is therefore
       EXACTLY THREE — one binding occurrence and two load occurrences — and the
       verifier asserts the number three, the node types, and the positions.
Z2-R5  ANY OTHER OCCURRENCE, IN ANY SYNTACTIC POSITION WHATSOEVER, IS A STATIC
       VIOLATION. No further enumeration is required for a construct to be
       rejected: absence from Z2-R3 is sufficient.
```

#### §2.5.4 The prohibition catalogue — redundant, stated for the record

Each of the following is already excluded by `Z2-R4`/`Z2-R5` counting. It is
enumerated so that the intent is unmistakable and so that a reviewer can check
the counting rule against concrete evasions. **There is no "and similar"
category**: the counting rule, not this list, is the closure.

```text
arithmetic (BinOp, UnaryOp, AugAssign, divmod, abs); formatting (JoinedStr,
FormattedValue, %-format, .format, str(), repr(), bytes(), encode/decode);
calls and lambdas (any Call whose args or keywords carry the Name other than
the two Z2-R3 positions; any Lambda — already banned outright by S-2); casts
and coercions of any kind outside V-6; comparisons other than the Z2-R3 None
guard; container insertion (List, Tuple, Set, Dict literal element or key or
value; append, add, insert, extend, update; Subscript assignment);
comprehensions and generator expressions of any form; unpacking (Starred, a
tuple/list Assign target, * or ** in a call); aliasing (any Assign whose value
is or contains the Name); logging or diagnostic emission of any kind; request
construction for any of the nine opcodes; any addressing, selection, or
handle-table operation; any capacity, custody, spend, or settlement expression;
any qualification, comparison, blinding, Q or C expression; any scientific
datum, outcome, or evidence expression; any return, yield, or global
assignment other than the Zone 1 return tuple.
```

#### §2.5.5 Why this is decidable

```text
D-1  the governed Names are introduced at exactly one site (Z2-R1) and are
     never parameters, attributes, or dict keys, so name resolution is local and
     no import, alias or attribute chain can rename them
D-2  the rule is an OCCURRENCE COUNT plus a POSITION MATCH over the parsed AST
     of a fixed, enumerated production root set (§P1-3.1, five roots). Both are
     computed by a single AST walk with no fixpoint, no call-graph, and no
     inter-procedural reasoning
D-3  no soundness assumption about value flow is made anywhere. A laundering
     construct such as int(str(attested_pid)) is rejected at the moment the
     Name occurs in a fourth position, before any question of what the
     construct does with it arises
D-4  the existing rules S-2 (no Lambda anywhere) and S-4 (every bound name
     assigned exactly once, never rebound, deleted, parameterized, or passed to
     setattr) already hold on the P1 roots (:2565-2578) and compose with the
     above rather than being relied on in their place
```

### §2.6 Persistent-use boundary — the restricted identity class (repairs `Y-C1`)

The two integers become durable, by signature, in two record classes. From that
moment the question is no longer "can they escape the parse site" but "what may
any reader of those keys do with them, including a reader that reloads them
from disk in a later process." v1 had no answer. v2 gives one.

#### §2.6.1 The class

```text
RESTRICTED_PROCESS_IDENTITY is the class containing exactly:
  (a) the two wire tokens of §2.2 and the two ints of §2.5;
  (b) the value of key `controller_pid` of any philosophia.officina.
      t-process-claim.v1 object, however obtained;
  (c) the value of key `process_group_id` of any t-process-claim.v1 object,
      however obtained;
  (d) the values of the same two keys of any philosophia.officina.
      t-active-lease.v1 object, however obtained;
  (e) every alias, copy, reload, deserialization, cached form, or in-memory
      binding of any of (a) through (d).

"However obtained" is literal: from the wire, from the constructor, from a
fresh read of the durable file, from a lease reload after a restart, from an
archived copy, or from any future route. THERE IS NO DECLASSIFYING OPERATION.
A write-then-reload does not launder the value; a reload is (e).
```

#### §2.6.2 The closed persistent-consumer whitelist

Exactly four consumers exist. Every one of them is already signed; v2 invents
none and permits none beyond them.

| # | Consumer | Keys | Operation permitted | Signed authority |
|---|---|---|---|---|
| **C-1** | the process-claim constructor | both | **write** the two keys, from the §2.5 Zone 2 positions and from nowhere else | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238`; composite row 2 `:2098-2128` |
| **C-2** | the active-lease constructor | both | **whole-mapping copy** of the claim key set into the lease; the two keys are never individually bound to a Name at this site | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:241-246` ("the claim keys plus" five) |
| **C-3** | the claim/lease immutability check | both | **equality comparison** of the lease's value against the claim's own recorded value; yields a boolean only | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:300-305` ("argv, and process group are immutable while open") |
| **C-4** | the §Z4.6 freeze-evidence acceptance predicate | `process_group_id` only | **equality comparison** of a witness's `pgid` against the claim's `process_group_id`; yields a conjunct boolean only | `…V2_1_1_CORRECTION.md:1047` (conjunct 7); composite row 2 readers line `:2116-2118` |

```text
P-R1  C-1..C-4 IS THE COMPLETE LIST. Any other read, in any production root, of
      key "controller_pid" or key "process_group_id" from any mapping is a
      static violation and, at runtime, an unreachable state.
P-R2  C-3 and C-4 produce BOOLEANS ONLY. Neither may return, store, print,
      transmit, or otherwise surface the integer itself. The compared value is
      consumed inside the comparison expression and does not outlive it.
P-R3  C-2 copies a MAPPING, not two numbers. No Name is bound to either value
      at the lease-construction site, so the lease copy adds no new occurrence
      of either value in the Name namespace.
P-R4  NO CONSUMER MAY ROUTE EITHER VALUE TO: a process-control primitive
      (_kill, _killpg, _waitpid, os.kill, os.killpg, os.waitpid); a request
      builder for any of the nine opcodes; a handle-table key, a handle
      selection, or any addressing; a journal key or a retry key; a capacity
      observation, a custody disposition, a spend fact, or a settlement input;
      a selection, qualification, comparison, blinding, Q or C input; a
      scientific datum, outcome, evidence, or Proof; a log, diagnostic, frame,
      or any record class other than the claim and the lease.
P-R5  EVERY OTHER OUTCOME IS PROCESS INVALIDITY. A claim or lease whose
      identity keys fail validation, whose two keys disagree between claim and
      lease, or which is reached by a route not in C-1..C-4 is routed
      RECORD-FIRST to the process-invalidity disposition of §P1-11.6 and
      §P1-13.5 (composite :1849-1866, :2323-2330), with invalidity dominant.
      It is NEVER a completion, a capacity fact, a custody disposition, a spend
      fact, or an input to qualification or comparison.
```

#### §2.6.3 The centralized verified accessor surface

`P-R1` is enforced by making bare access syntactically impossible outside three
named functions:

```text
ACC-1  _identity_from_await_stop(fields)      -> (int, int) | (None, None)
       the §2.5 Zone 1 parse site; the only reader of the wire tokens
ACC-2  _claim_identity_pair(claim_mapping)    -> (int, int)
       the only reader of claim["controller_pid"] and claim["process_group_id"]
ACC-3  _lease_identity_pair(lease_mapping)    -> (int, int)
       the only reader of the same two keys of a lease mapping

ACC-R1  a Subscript, .get, .pop, ChainMap, or any other access whose key operand
        is the string literal "controller_pid" or "process_group_id" appears in
        the production roots ONLY inside ACC-2 and ACC-3, and inside the C-1
        constructor's own keyword names and the C-2 whole-mapping copy.
ACC-R2  the return of ACC-2 and ACC-3 is unpacked ONLY at the C-3 and C-4
        comparison sites, and each unpacked Name occurs exactly once, inside
        the comparison expression, per the same occurrence-count discipline as
        §2.5.3.
ACC-R3  no accessor returns a mutable container, caches its result, stores it on
        an attribute, or has a default, fallback, or coercing branch. A missing
        or non-int key is a validation failure routed by P-R5.
ACC-R4  ACC-1..ACC-3 are the complete accessor set. A fourth accessor is a
        static violation.
```

**A reload does not declassify.** `ACC-2` and `ACC-3` do not care whether the
mapping came from the constructor, from a fresh file read, or from a reload
after restart: every value they return is class member (e) of §2.6.1 and is
bound by `ACC-R2` to a single comparison position. The specific evasion the Y
line described — write the claim, reopen it, bind `claim["controller_pid"]` to
a fresh name, feed it onward — is now a violation of `ACC-R1` at the reopen and
of `ACC-R2` at the fresh name, and is rejected statically at both points.

#### §2.6.4 The schema-reader audit, recomputed key-by-key

Recomputed from the exact key sets of the governing schemas, not from generic
taint reasoning:

| Schema | Contains `controller_pid`? | Contains `process_group_id`? | Source |
|---|---|---|---|
| `philosophia.officina.t-process-claim.v1` | **yes** | **yes** | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238` |
| `philosophia.officina.t-active-lease.v1` | **yes**, by "the claim keys plus" five | **yes**, same | `:241-246` |
| `philosophia.officina.t-process-record.v1` | **no** | **no** — it carries `process_claim_sha256` | `:248-257` |
| `philosophia.officina.t-review-record.v1` | no | no | `:262-268` |
| `philosophia.officina.t-runtime-invalidity.v1` | no | no | `:269-276` |
| `philosophia.officina.t-activation-claim.v1` | no | no | `:134-144` |
| `philosophia.officina.t-freeze-observation.v1` | no | no — it has its **own** `pgid` key, compared against the claim's value at conjunct 7 | composite `:2236-2245`; `…V2_1_1_CORRECTION.md:1047` |
| the four §P1-5.1 singleton spawn records | no | **a key of that name exists in `SPAWNING_GROUP.json`, but see §2.6.5** | composite `:560-590`, `:596-612` |
| `t-pcs.v1` request grammar | no | no | composite `:1240` |

**Therefore exactly two durable schemas carry the restricted values, and exactly
one signed predicate reads one of them.** That is the complete durable surface,
computed rather than asserted.

#### §2.6.5 A name collision that is not a value flow

`SPAWNING_GROUP.json` has a key literally named `process_group_id`. §P1-5.2
`:604` defines it as "the middle's process-group id after its `setsid`, equal to
`middle_child_pid`". It is a **different value about a different process**, with
its own already-signed provenance (`c10`'s kernel proof), and it predates this
packet. It is **not** in `RESTRICTED_PROCESS_IDENTITY` and this packet neither
constrains nor relaxes it.

Because `ACC-R1` keys on the string literal, the accessor rule would also
capture that record's reads. v2 resolves the collision explicitly rather than
leaving it to an implementer:

```text
NC-1  ACC-R1 is scoped by SCHEMA, not by key name alone: it governs reads of
      those two keys from a t-process-claim.v1 or t-active-lease.v1 object. A
      read of SPAWNING_GROUP.json's process_group_id is outside this packet.
NC-2  The verifier discriminates by the schema literal present at the reading
      site, which is decidable because each of the four singleton records is
      opened at exactly one enumerated site under §P1-13.7 (:2357-2368).
NC-3  This packet asserts nothing new about the middle's group id, the
      supervisor's pgid, or any of the four singleton records.
```

#### §2.6.6 What the Y line asked for, and where each part is

| Y-C1 requirement | v2 locus |
|---|---|
| withdraw the false "only durable sinks" claim | §2.4, verbatim withdrawal |
| enumerate the legitimate persistent flow exactly | §2.6.2 `C-1`..`C-4` |
| claim-to-lease copy justified by "lease contains all claim keys" | `C-2`, cited to `:241-246` |
| the signed freeze-predicate read of `process_group_id` | `C-4`, cited to `:1047` |
| any other governing read proved from the contracts | `C-3`, the immutability check, cited to `:300-305`. **No fifth read is provable**; §2.6.7 states why the admission-time group-membership check is not one |
| every direct or reloaded read/alias stays in the restricted class | §2.6.1 (e); §2.6.3 "a reload does not declassify" |
| closed whitelist **or** centralized verified accessor | **both**: §2.6.2 whitelist, §2.6.3 accessors |
| every other consumer routes deterministically to process invalidity | `P-R5`, record-first, invalidity dominant |
| recompute all relevant schema readers | §2.6.4, key-by-key |

#### §2.6.7 The one read that looks like a fifth and is not

The activation protocol says (`:300-303`): "The controller owns one declared
process group. Every child worker must remain in that group and under the same
lease; child creation and membership are checked at every admission."

That could be read as a fifth consumer — an admission-time membership check
against `process_group_id`. Under P1 it is **not**, and the reason is signed:

```text
M-1  P1 records a KERNEL-VERIFIED GROUP for a handle, and SIGNAL_GROUP's
     precondition is exactly "a kernel-verified group is recorded for the
     handle" (composite :1223). Group determination is P1's, keyed by HANDLE.
M-2  The peer layer has no authorized route to observe a live process's group
     membership: it holds no pid, and §P1-8.3 (:1240) forbids a pid in any
     request. Attempting to re-derive membership from the claim's number would
     be exactly the addressing P1 removed.
M-3  What the peer layer may check from the durable numbers is the IMMUTABILITY
     of the declared group across the lease's life — which is C-3, an equality
     against its own recorded value, producing a boolean.
M-4  Any membership question P1 cannot answer through a handle is a control
     outcome that cannot be established, and routes to §P1-11.6 with
     invalidity dominant.
```

This is a scope statement, not a new author cell: it consumes only already
signed text and opens nothing.

### §2.7 The request grammar stays PID-free — restated as a closed rule

```text
A-R1. No request field of any of the nine opcodes may carry a PID or a PGID.
      The request grammar of v1.2 §P1-8.3 is byte-unchanged under Option A.
A-R2. Handle selection is by handle_id and by nothing else.
A-R3. Every signal target is a handle_id. No signal path accepts a number.
A-R4. The journal key is the pair (generation_id, request_id). No pid enters a
      journal key.
A-R5. The retry / replay key is the same pair. No pid enters a retry key.
A-R6. No author decision, selection, Q, C, blinding claim, or scientific or
      resource interpretation consumes either value, at any distance, including
      from a durable reload.
A-R7. No value of RESTRICTED_PROCESS_IDENTITY is placed in any frame the
      supervisor sends, in either direction, on any opcode.
A-R8. R-L4 is unchanged: the peer layer reaches P1 only through the nine
      opcodes, and P1 opens no peer artifact (composite :2022-2027, row 2
      "fields P1 reads: none", :2119).
```

### §2.8 Durable journal record and replay (repairs `X M-1` and `Y-C2`)

#### §2.8.1 The withdrawn premise

```text
WITHDRAWN, v1 §2.7, verbatim:
  "The tuple is part of the recorded response of the J4 COMPLETED journal
   entry, exactly as start_identity already is."

WHY IT IS UNSUPPORTED: the committed composite records at J4 exactly
  { ..., state: COMPLETED, outcome, handle_id, fd_vector_len }      (:1289)
and its replay rows return
  "the recorded status, detail and handle, with status REPLAYED,
   fds_redelivered 0, and no descriptors"                     (:1301, :1303)
NEITHER names start_identity, NEITHER names pgid_is_leader. The premise that
start_identity is already journaled and already redelivered is therefore NOT
ESTABLISHED BY THE CITED BYTES, and v1 leaned on it for its whole B1 argument.

WHAT v2 SAYS INSTEAD: Option A MAKES start_identity's journal durability
EXPLICIT, together with the new tuple. It does not inherit it. Whether v1.2
intended the full payload to be durable is not decidable from its text, and v2
does not guess; it specifies.
```

Both reviews reached this independently (`X M-1`, `Y-C2`). v2 accepts it fully.

#### §2.8.2 The amended `J4` record

```text
J4 for AWAIT_STOP records the COMPLETE RESPONSE OPERAND VECTOR, in this exact
key order, one canonical ASCII JSON object per journal line:

  1  generation_id      64 lowercase hex
  2  request_id         decimal, 1..19 digits, no leading zero
  3  opcode             "AWAIT_STOP"
  4  state              "COMPLETED"
  5  status             OK | REFUSED | INVALID
  6  detail             one token of §P1-2.6
  7  handle_id          decimal, or "-"
  8  fd_vector_len      decimal (0 for AWAIT_STOP)
  9  outcome            STOPPED | EXITED | TIMEOUT, or "-"
 10  start_identity     decimal 1..20 digits, or "-"
 11  pgid_is_leader     "0" | "1", or "-"
 12  attested_pid       decimal per §2.2 G-1..G-3, or "-"
 13  attested_pgid      decimal per §2.2 G-1..G-3, or "-"

ENCODING, PINNED:
  E-1  each value is stored as the EXACT ASCII BYTE TOKEN the response frame
       carries or would carry. No re-encoding, no numeric normalization, no
       re-derivation from an int.
  E-2  an absent operand is stored as the one-byte string "-", never as null,
       never as 0, never omitted.
  E-3  key order is exactly 1..13 above; the object is canonical (sorted-free,
       fixed-order, no insignificant whitespace) so that the record's bytes are
       a function of the response's bytes alone.
  E-4  the record is fsynced before J5, exactly as v1.2 requires (:1289-1291).

GENERALIZATION, STATED HONESTLY: the same rule — "J4 records the complete
response operand vector of its opcode" — is applied to the other eight opcodes,
whose vectors are their existing operand sets. This REPAIRS A PRE-EXISTING
UNDER-ENUMERATION in v1.2's "{ ..., state: COMPLETED, outcome, handle_id,
fd_vector_len }" that Option A would otherwise inherit. It is a broader edit
than Option A strictly needs, and v2 says so rather than hiding it inside an
AWAIT_STOP-only change. It is counted in the blast radius at §5.
```

#### §2.8.3 Replay, byte-identical, with no re-observation

```text
REPLAY of a COMPLETED or an ACKED entry for AWAIT_STOP, exact construction:

  field 0  the schema literal                        constant
  field 1  the version literal                       constant
  field 2  generation_id                             from the journal key
  field 3  request_id                                from the journal key
  field 4  status                                    the literal "REPLAYED"
  field 5  detail                                    recorded key 6, VERBATIM
  field 6  handle_id                                 recorded key 7, VERBATIM
  field 7  fds_redelivered                           the literal "0"
  field 8  outcome                                   recorded key 9,  VERBATIM
  field 9  start_identity                            recorded key 10, VERBATIM
  field 10 pgid_is_leader                            recorded key 11, VERBATIM
  field 11 attested_pid                              recorded key 12, VERBATIM
  field 12 attested_pgid                             recorded key 13, VERBATIM

"VERBATIM" means the recorded bytes are emitted unchanged. Fields 4 and 7 are
overridden exactly as v1.2's replay rows already require (:1301, :1303); every
other operand is a byte-for-byte redelivery.

R-P1  THE PCS MUST NOT RE-EVALUATE A-P1..A-P6 ON REPLAY.
R-P2  THE PCS MUST NOT, WHILE CONSTRUCTING A REPLAY: read /proc for any pid;
      call getpgid, getpid, getppid, waitpid or any wait variant; consult the
      handle table for pid, start_identity, pgid_or_null, state or ownership;
      inspect any child's existence, state or exit status; or consult any
      artifact other than the journal record itself.
R-P3  THE JOURNAL RECORD IS THE SOLE SOURCE. If the record is missing, short,
      malformed, or fails its own canonical re-read, the PCS returns INVALID
      with OPERATION_INCONCLUSIVE and NO TUPLE. It never reconstructs, never
      defaults, and never observes.
R-P4  A replay is a redelivery of a recorded reply, NEVER a fresh observation.
      This is required, not merely economical: after the handle reaches REAPED,
      re-running A-P2 would violate WAIT_ONE's precondition (:1566), and
      getpgid on a reaped pid may name an unrelated process.

REPLAY of an ACCEPTED entry (crash between J2 and J4):
  INVALID with OPERATION_INCONCLUSIVE, and NO TUPLE. No claim can be written
  from an inconclusive stop.
```

This preserves B1 at its earned strength: the byte record is redeliverable
because it is specified to be recorded, and nothing about the
descriptor-non-redelivery narrowing changes, because this response carries no
descriptors.

### §2.9 PID reuse and start-identity binding

The tuple is emitted only while ownership is `OWNED` and the target is an
unreaped stopped direct child. By the §P1-10.1 reuse proof (composite
`:1541-1550`) — `SIGCHLD` was normalized to `SIG_DFL` with neither `SIG_IGN` nor
`SA_NOCLDWAIT` **before the child existed**, so the task holds its pid until the
PCS's own targeted reap — the pid cannot be reassigned between attestation and
use.

**No new predicate is needed downstream.** The claim records
`controller_start_identity` beside `controller_pid`, and §Z4.6 conjunct 7
already compares **both** pgid and start identity. A recycled pid therefore
fails the existing predicate unchanged.

### §2.10 Crash, collision, and invalidity dominance (repairs `Y-M1`)

#### §2.10.1 The withdrawn row

```text
WITHDRAWN, v1 §2.9, verbatim:
  "| PCS death at any point | whole-generation invalidity per §P1-11.4; no claim
    is written and no tuple survives outside the journal |"

WHY IT IS FALSE: the same table's own previous row contemplates a crash AFTER
the claim write. A durable claim cannot be made nonexistent by prose. The
activation protocol is explicit that "Recovery cannot delete/reuse a claim or
process id" (…ACTIVATION_PROTOCOL_V2_CORRECTION.md:338-341). The operative rule
is whole-generation PROCESS INVALIDITY with invalidity DOMINANT over completion,
capacity, custody, spend, qualification, comparison and science (composite
§P1-11.6 :1849-1866, §P1-13.5 :2323-2330).
```

#### §2.10.2 The crash matrix, keyed to the exact durable boundary

Each row names the last durable boundary crossed, so that no row can be
inconsistent with the one before it.

| Last durable boundary crossed | State of the tuple | State of the claim | Single continuation |
|---|---|---|---|
| none (crash before `J2` fsync) | never existed | absent | nothing happened; a redelivery is a fresh request |
| `J2` fsync (`ACCEPTED`) | not produced | absent | `OPERATION_INCONCLUSIVE`; no syscall re-performed; whole-generation invalidity, never a silent retry |
| `J3` syscall performed, `J4` not fsynced | produced in memory, **not durable** | absent | `ACCEPTED` on replay ⇒ inconclusive ⇒ no tuple ⇒ no claim; possibly-live orphan routed by §P1-11.4; generation invalid |
| `J4` fsync (`COMPLETED`) | **durable in the journal**, §2.8.2 | absent | a redelivery returns the recorded vector byte-identically (§2.8.3) with no re-observation; the peer may then write the claim |
| `J5` sent, supervisor has not parsed | durable | absent | as above; redelivery is byte-identical |
| supervisor parsed, claim **not** durable | durable in the journal; in-memory copy lost with the address space | absent | redelivery reproduces the tuple; the peer writes the claim; no re-observation occurs at any point |
| **claim durable**, `J6` `ACKED` not written | durable | **present and retained forever** | a second install attempt is an `EEXIST` collision resolved ONLY by §2.10.3; the claim is never removed |
| claim durable, lease not yet installed | durable | present | the lease is constructed by `C-2` from the durable claim; if it cannot be, the process settles invalid with the claim retained |
| lease durable | durable | present | normal operation |
| **PCS death after the claim is durable** | the journal survives or does not; either way it is not consulted for a claim that already exists | **present and retained** | whole-generation invalidity per §P1-11.4 (`:1757-1785`), settled through the **signed invalid-process route** of §P1-11.6/§P1-13.5 as `T_PROCESS_INVALID` with `invalid_cause` `PROCESS`. **The claim is never narrated as absent, never deleted, and never reused** (`…ACTIVATION_PROTOCOL_V2_CORRECTION.md:338-341`) |
| PCS death before the claim is durable | durable in the journal only if `J4` was reached; a new PCS may not adopt the generation (`:1774-1777`, `GENERATION_NOT_ADOPTABLE`) | absent | whole-generation invalidity; no claim is written; the tuple survives only inside the journal and reaches no consumer |
| supervisor death holding the tuple | in-memory copy dies with the address space | absent or present per the rows above | the durable state decides, never the lost copy |

#### §2.10.3 `EEXIST` is not convergence until identity is verified

```text
A second no-replace install at successor/officina/runtime/T_PROCESS_CLAIMS/
<process_id>.json that returns EEXIST proves ONLY that some object occupies the
path. It proves nothing about that object's content. Convergence requires ALL
of the following, under T_RUNTIME.lock, evaluated in this order:

  X-1  CANONICAL BYTES. Read the occupant's bytes. They must equal, byte for
       byte, the canonical bytes this install would have written.
  X-2  SCHEMA. The occupant validates against t-process-claim.v1 exactly: the
       twenty-key set of :231-238, exact types, strict int, and recursive
       scientific-field rejection.
  X-3  CROSS-FIELD. process_id recomputes from its signed preimage
       (:296-299) and equals the filename stem; scientific_outcome is the
       literal false; controller_pid and process_group_id equal the values of
       the REPLAYED recorded tuple (§2.8.3), not of any fresh observation;
       controller_start_identity equals the replayed start_identity; and the
       §2.2 cross-field invariant holds on those values.
  X-4  EXPECTED HASH. SHA-256 of the occupant's canonical bytes equals the
       digest this install computed for its own bytes.

  ALL FOUR HOLD  ⇒ converge: the install is an idempotent no-op, and the
                   already-durable claim stands.
  ANY FAILS      ⇒ RECORD-FIRST DOMINANT INVALIDITY:
                   1. write t-runtime-invalidity.v1 (:269-276) with
                      invalid_cause PROCESS and required_action
                      SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY;
                   2. THEN route through §P1-11.6 / §P1-13.5;
                   3. the occupant is NEVER replaced, repaired, or deleted;
                   4. no completion, capacity, custody, spend, qualification,
                      comparison or scientific interpretation is produced.

MALFORMED, PARTIAL, CONFLICTING and INCONSISTENT occupants take the same route.
Occupancy alone is never treated as agreement, and no post-outcome discretion
exists at this site.
```

#### §2.10.4 One dominant invalidity surface for every identity failure

```text
The following all bind to the SAME record-first dominant invalidity route:

  I-1  a response with exactly one identity field present            (§2.2 G-4)
  I-2  a token of 8+ digits, or a value outside 1..4194304      (G-2, G-3, G-5, G-6)
  I-3  a token with a leading zero, a sign, or a non-digit byte       (G-1)
  I-4  a violation of pgid_is_leader == 1 <=> attested_pid == attested_pgid
  I-5  a tuple present on an outcome other than STOPPED               (§2.1)
  I-6  Zone 1 returning (None, None) for any reason                   (Z1-R6)
  I-7  a replay whose journal record is missing, short or malformed   (R-P3)
  I-8  an EEXIST occupant failing X-1..X-4                            (§2.10.3)
  I-9  a lease whose identity keys disagree with its claim's          (C-3)
  I-10 any access to either key outside ACC-1..ACC-3                  (P-R1)

For I-1..I-7 the wire-level classification is TRANSPORT_STRUCTURAL and the
generation routes to §P1-11.6. For I-8..I-10 an invalidity record is written
FIRST and the process settles T_PROCESS_INVALID / invalid_cause PROCESS. In
every case invalidity DOMINATES: it is never a completion, never a capacity
fact, never a custody disposition, never a spend fact, never an input to
qualification or comparison, and never a scientific outcome.
```

### §2.11 Verifier rules and behavioural obligations

New verifier rules, additions to the `S-` family of §P1-14.6 (`:2555-2645`),
in that section's existing style. **`S-25d` of v1 is withdrawn and does not
appear here.**

```text
S-25a  the two AWAIT_STOP identity tokens are read at exactly ONE site, the
       Zone 1 function of §2.5.1, and the raw Names raw_pid / raw_pgid occur
       only in the V-1..V-5 forms
       ⇒ "S-25a: attested identity parsed outside the single parse site"
S-25b  Zone 1 conformance: Z1-R1..Z1-R6, including exactly one int() per token
       and a 2-tuple return with no partial pair
       ⇒ "S-25b: attested identity parse site violates its closed operation set"
S-25c  Zone 2 occurrence count: each of attested_pid and attested_pgid occurs
       EXACTLY THREE times in the parsed AST of the production roots — one
       Assign target, one None-guard comparison, one named keyword argument of
       the single claim constructor — and in no other position
       ⇒ "S-25c: attested identity occurs outside its whitelisted positions"
S-25d  accessor closure: a Subscript/.get/.pop whose key operand is the literal
       "controller_pid" or "process_group_id" against a t-process-claim.v1 or
       t-active-lease.v1 object appears ONLY inside ACC-2 / ACC-3, plus the C-1
       constructor keyword names and the C-2 whole-mapping copy
       ⇒ "S-25d: restricted identity key read outside the accessor surface"
S-25e  persistent-consumer closure: the returns of ACC-2 / ACC-3 are unpacked
       only at the C-3 and C-4 comparison sites, each unpacked Name occurring
       exactly once inside its comparison expression
       ⇒ "S-25e: restricted identity value used outside a whitelisted comparison"
S-25f  no value of RESTRICTED_PROCESS_IDENTITY, and no expression reading one,
       appears as an argument to _kill, _killpg, _waitpid, os.kill, os.killpg,
       os.waitpid, to any request-builder for the nine opcodes, in a journal
       key, a retry key, a handle-table key, a handle-selection comparison, or
       any frame the supervisor sends
       ⇒ "S-25f: restricted identity reaches a control-plane sink"
S-25g  no value of RESTRICTED_PROCESS_IDENTITY appears in any record
       constructor other than the claim (C-1) and the lease (C-2), and in no
       logging, formatting, capacity, custody, spend, settlement, selection,
       Q, C, blinding or scientific expression
       ⇒ "S-25g: restricted identity reaches an unauthorized record or decision"
S-25h  journal conformance: the AWAIT_STOP J4 append names all thirteen keys of
       §2.8.2 in that order, and the replay construction of §2.8.3 contains no
       call to getpgid, getpid, getppid, any wait variant, any /proc open, or
       any handle-table read
       ⇒ "S-25h: replay re-observes instead of redelivering"
```

**Decidability.** `S-25a`, `S-25b`, `S-25c`, `S-25e` and `S-25h` are occurrence
counts and position matches over a single AST walk of the five enumerated
production roots. `S-25d` and `S-25g` are literal-key and constructor-name
matches over the same walk. `S-25f` is the same syntactic reaching check v1
already specified. **No rule requires a sound taint analysis, a call graph, or
a fixpoint**, which is precisely what `X M-2` required.

New behavioural obligations:

```text
A-T1   the tuple is emitted on STOPPED and on no other outcome
A-T2   A-P1..A-P6 each reject a bit-exact negative fixture; a fixture in which
       the fresh getpgid disagrees with the spawn-time pid yields
       STRUCTURAL_VIOLATION and no tuple
A-T3   a response with exactly one of the two fields present is
       TRANSPORT_STRUCTURAL
A-T4   the cross-field invariant of §2.2 holds on every accepted response
A-T5   FAULT INJECTION: a build that passes attested_pid to a request builder,
       to a signal path, or to os.kill is REJECTED STATICALLY by S-25c/S-25f,
       and the test asserts the rejection rather than the absence of an effect
A-T6   no response for any opcode other than AWAIT_STOP carries either field
A-T7   frame size: the largest legal AWAIT_STOP response is under
       T_CONTROL_FRAME_MAX_BYTES with margin, computed and asserted
A-T8   NEW. an 8-digit token, and a 7-digit token above 4194304, are each
       refused as TRANSPORT_STRUCTURAL with no truncation and no clamping
A-T9   NEW. A LAUNDERING FIXTURE: builds containing each of
         p = (lambda v: v)(attested_pid)
         (a,) = (attested_pid,)
         [x for x in (attested_pid,)]
         p = int(str(attested_pid))
         claim2 = json.loads(open(claim_path).read())["controller_pid"]
       are EACH rejected statically — the first four by S-25c's occurrence
       count, the fifth by S-25d's accessor closure — and the test asserts the
       named rule fired
A-T10  NEW. JOURNAL DURABILITY: after a simulated crash at each of the eleven
       boundaries of §2.10.2, the continuation is exactly the one named, and a
       COMPLETED/ACKED replay reproduces operands 5,6,8,9,10,11,12
       byte-identically with no /proc read, no getpgid and no wait
A-T11  NEW. EEXIST: a conforming occupant converges; occupants that are
       byte-different, schema-invalid, cross-field-inconsistent, or
       hash-mismatched EACH produce an invalidity record FIRST and then the
       §P1-11.6 route, and NONE is treated as convergence
A-T12  NEW. POST-CLAIM PCS DEATH: the durable claim is present after the route
       completes, the disposition is T_PROCESS_INVALID with invalid_cause
       PROCESS, and no route reports the claim as absent
```

### §2.12 The exact amendment to the signed sentence

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
   fields; those values, and every durable copy or reload of them, remain in a
   restricted identity class whose complete consumer set is the claim write,
   the signed claim-to-lease copy, the lease immutability comparison, and the
   signed freeze-evidence comparison, and which has no control-plane sink. It
   does not call fork, Popen, waitpid, kill, or killpg on any path."

TOKEN FOR THE WEAKENING:
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

**What is given up, stated plainly.** Today the property is *lexical*: no PID
exists anywhere in the supervisor, checkable by a single static rule. After A
the property becomes a *syntactic occurrence* property: PIDs exist, and are
proved by occurrence counting to appear in exactly the enumerated positions.
That is weaker than a lexical absence and strictly easier to regress. **That,
and not any change in kernel capability, is the real cost of Option A**
(see §5.6).

v1 described the post-A property as a *dataflow* property. v2 does not: after
`X M-2`, the guarantee is deliberately **not** a dataflow property, because a
dataflow property would depend on taint soundness. It is a syntactic property,
which is weaker in expressiveness and stronger in decidability. **The sentence
being weakened is still weakened, and this packet still says so.**

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

### §3.2 Every reader that must change — **recomputed** (repairs `Y-M2`)

```text
WITHDRAWN, v1 §3.2, verbatim:
  "| t-process-record.v1 | the final record inherits the same key change |"

WHY IT IS FALSE: the final process record's key set is exactly
  schema, scientific_outcome, validity, disposition, invalid_cause,
  activation_record_sha256, process_claim_sha256, process_id, process_sequence,
  behavior_source_sha256, config_sha256, stack_sha256, numerical_mode_sha256,
  device_identity, device_units, started_utc, closed_utc, cumulative_charge_ns,
  final_charge_event_sha256, final_t_state_sha256, immutable_control_sha256
  (…ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257)
It contains NEITHER controller_pid NOR process_group_id. It references the
claim by process_claim_sha256. It therefore does NOT mechanically become .v2
when the claim changes, and v1 counted it against B without warrant.
```

Recomputed surface, each row justified through an explicit dependency:

| Surface | Changes under B? | Justification |
|---|---|---|
| `t-process-claim.v1` | **yes — superseded by `.v2`** | two keys removed, two added; every constructor and validator |
| `t-active-lease.v1` | **yes — mechanically** | defined as "the claim keys plus five" (`:241-246`); the claim key set changes, so the lease key set changes |
| `t-process-record.v1` | **no** | own key set; carries `process_claim_sha256`, not the two keys (`:248-257`). **Removed from the count.** |
| `t-review-record.v1`, `t-runtime-invalidity.v1`, `t-activation-claim.v1` | **no** | neither key present (`:262-276`, `:134-144`) |
| `t-freeze-observation.v1` | **no** | own `pgid` key, unaffected by the claim's key set (composite `:2236-2245`) |
| §Z4.6 conjunct 7 | **yes — a signed acceptance predicate** | it dereferences the claim's `process_group_id` (`:1047`); under B it must dereference the binding artifact instead |
| the PCS write surface | **yes — architectural** | under v1.2 the PCS writes exactly the four singleton spawn records and its journal (composite `:471`, §P1-13.7 `:2357-2368`); the binding artifact is a fifth, peer-visible, PCS-written class |
| `R-L4` | **yes — inverted** | a peer predicate opening a P1-owned artifact reverses the one-way call direction (`:2022-2027`) |
| new binding schema + validator + GC rule | **yes — new** | `t-process-identity-binding.v1` did not exist |
| `process_claim_sha256` **values** | **content only, not schema** | the claim's canonical bytes change, so every stored digest changes value. The *schema* and every *reader* of that key are digest-agnostic and need no edit. Counted as a content dependency, not a schema change. |
| batch settlement, archive, verification readers | **no schema change proved** | the archival sets are path-based ("that process claim and final record", `:88-97`), and no batch-settlement or archive surface reads either key — recomputed by exhaustive key search across the governing schemas (§2.6.4). Any such change must be justified through the `process_claim_sha256` dependency, and none is claimed here. |
| migration | **none required** | `T` is `NOT_ACTIVATED` and no production claim, lease or record exists, so there is no durable evidence to migrate. This is a genuine advantage of B and is stated as such. |

**Corrected count for B: two record schemas superseded (not three), one new
schema created, one signed acceptance predicate reopened, one architectural
rule inverted, one PCS write-surface property expanded.**

### §3.3 Why B is **NOT SELECTABLE** in this packet

B cannot be made single-valued without at least two further author decisions
that this packet must not make. **This is unchanged by the corrected blast
radius**, because it is an authority gap, not a size argument:

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
  §P1-13.0 (:2022-2027), which fixes the co-resident call direction as one-way,
  peer into P1, through the nine opcodes and nothing else. A peer predicate
  that opens a P1-owned file crosses that boundary in the opposite direction
  and needs its own signature.
```

Both reviews independently confirmed both sub-cells as genuine and separately
unresolvable inside the signed chain.

**Therefore B is presented, fully specified, and marked non-selectable.** Kirill
may still direct B; doing so opens sub-cells `B-1` and `B-2` and requires a
further packet before any composite can bind it.

---

## §4. Option C — examined and rejected, not offered

For completeness of the search: re-index §Z3.4's `/proc/*/cmdline` predicate to
the P1 argv layout and let the supervisor discover the pid itself.

**Not offered as an option**, on the corrected grounds of §1.5:

1. it makes the supervisor's own unattested observation the identity source,
   with no PCS proof that the discovered pid is the handle's process (`R-2`);
2. it revives a direct pid-to-`killpg` route outside P1's handle-only,
   PCS-mediated authority and outside the nine opcodes (`R-3`);
3. it is strictly dominated by A: same numeric exposure, weaker proof;
4. the argv-evidence deletion at `…V2_1_10_CORRECTION.md:188` removes the
   corroboration its fixed-index anti-spoof argument leans on — **within that
   rule's actual scope of clean image, fresh `execve` and executor set, and not
   more broadly** (`R-4`, corrected per `Y-m1`).

It is recorded here so the packet's search is auditable, not to create symmetry.
That §Z3.4's indices are dead under P1 remains a separate peer-chain defect.

---

## §5. Comparative audit, corrected

### §5.1 Signed sentences, schemas and durable formats touched

| | Option A | Option B |
|---|---|---|
| **amended** | one sentence of the P1 process-authority signature (§2.12) under token `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`; the `AWAIT_STOP` **response grammar**; **the `J4` journal record format and the `COMPLETED`/`ACKED` replay rows (§2.8) — NEW IN v2**; the `EEXIST` convergence rule for the claim install (§2.10.3) | `t-process-claim.v1`, `t-active-lease.v1`, §Z4.6 conjunct 7, the PCS write surface, `R-L4`; **plus a new binding schema**. `t-process-record.v1` is **NOT** touched — v1's claim that it was is withdrawn |
| **untouched** | `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1`, §Z4.6 conjunct 7, every request grammar, A3/C1/D1/K1, the descriptor surface | the P1 signature sentence; the request and response grammars; the journal record format |
| **B1 status** | preserved, but **by explicit specification of journal durability, not by inheritance** (§2.8) | preserved; the binding digest is stable and the artifact is no-replace |
| **validity predicates reopened** | **zero** | **at least one signed acceptance predicate**, plus every lease reader |

### §5.2 A3 authority and confidentiality

Answered in full at §5.6, and independently confirmed by both review lines.

### §5.3 B1 replay and crash semantics

| | Option A | Option B |
|---|---|---|
| replay | the complete operand vector is recorded at `J4` (§2.8.2) and redelivered byte-identically (§2.8.3); re-observation is prohibited and statically checked by `S-25h` | the binding digest is stable; the artifact is no-replace, so replay is naturally idempotent |
| `ACCEPTED` crash | no tuple, no claim | no binding consumed, no claim |
| post-claim PCS death | claim **retained**, settled through the signed invalid-process route (§2.10.2) | same |
| new failure mode | a replay implemented as a re-observation would violate `WAIT_ONE`'s post-`REAPED` precondition — hence the explicit prohibition and `A-T10` | a binding artifact durable with no claim, requiring a garbage-collection rule that does not yet exist |

### §5.4 Code, verifier, test and manifest surface

| | Option A | Option B |
|---|---|---|
| PCS root | build the tuple under `A-P1`..`A-P6`; **record the full operand vector at `J4` and construct replays from it alone** | write a fifth durable artifact class |
| supervisor code | one parse site; two accessors; four whitelisted consumers | new claim `.v2` constructor; dereference bindings |
| verifier | `S-25a`–`S-25h` (**eight rules, up from four**) | new schema validators for two record classes plus one new class; a new predicate for conjunct 7 |
| tests | `A-T1`–`A-T12` (**twelve, up from seven**) | full re-validation of claim and lease readers; binding lifecycle and GC |
| manifest | unchanged beyond the composite digests | unchanged beyond the composite digests |

### §5.5 Blast radius and rollback — corrected on both sides

| | Option A | Option B |
|---|---|---|
| blast radius | **one opcode's response grammar, one signature sentence, the durable `J4` record format and its two replay rows, the claim-install `EEXIST` rule, eight verifier rules, twelve tests.** v1's "one sentence and one response grammar" is **withdrawn as materially understated** | **two record schemas superseded, one new schema, one signed predicate, one architectural rule, one PCS write-surface property.** v1's "four schemas … every downstream reader" is **withdrawn as materially overstated** |
| rollback | delete two response fields, revert the `J4` key list to its v1.2 form, delete the eight rules; **no peer schema changes shape**, though the journal format is a durable format and reverting it strands any journal already written in the new shape | revert two record schemas and delete the binding class; any durable object already written in `.v2` shape is stranded |
| migration | none for peer records; **`T` is `NOT_ACTIVATED`, so no journal exists to migrate either** | none **today**, because `T` is `NOT_ACTIVATED`; after activation it would be large |

**The corrected comparison narrows the gap in both directions.** A is larger
than v1 said; B is smaller than v1 said. §7 re-evaluates the recommendation on
the corrected figures.

### §5.6 Does observing a PID grant process authority under A3?

**No.** Three things are routinely conflated and must be separated. Both review
lines independently confirmed this analysis.

**1. OS information.** A pid is a small integer that any same-UID process may
read from `/proc` at any time. Under the A3 threat model the supervisor is
same-UID with every process in this contract and **already may read every pid
on the system unilaterally**. The attested tuple therefore conveys **zero**
operating-system information the supervisor could not obtain without it. What it
adds is *provenance*: a number the PCS vouches for, rather than one the
supervisor scraped.

**2. Authorized addressing.** What P1 removed is the supervisor's *authorized*
ability to name a process as an operation target: no request field accepts a
PID (composite `:1240`), every operation is selected by a PCS-issued handle, and
every signal and wait executes in the PCS. **Option A does not touch any of
this.** It adds a response field with no request counterpart, and `A-R1`–`A-R8`
close the request side explicitly.

**3. Same-UID adversarial capability.** Under A3 a contaminated supervisor can
already call `kill(any_pid)` directly; the kernel permits it and this contract
has never claimed otherwise. §P1-12.3 states it affirmatively (`:1942`): a
same-UID actor can "stop, kill, or delay any same-UID process, with or without
adoption", and the section closes (`:1952`): "Kernel power is admitted; Officina
authorization is not conferred." **P1's guarantee was never that the supervisor
lacks the kernel power; it was that no Officina route authorizes its use and no
Officina decision consumes its result.** That guarantee is unchanged by Option
A, because the tuple carries no capability and feeds exactly the four
already-signed consumers of §2.6.2.

**The honest summary.** Option A weakens the **English sentence** in the
signature. It does **not** weaken the **safety property**, and it does not
change what a hostile same-UID actor can do. What it genuinely costs is
**testability**: an invariant that is today lexical becomes a syntactic
occurrence invariant checkable only by `S-25a`–`S-25h`. A reviewer should weigh
that cost, not a fictional capability transfer.

### §5.7 Scientific and resource interpretation

**Neither option changes any scientific or resource interpretation.** Both
integers are control-plane infrastructure facts. Under A they enter exactly two
keys of a record whose `scientific_outcome` is the literal `false` and which is
recursively scientific-field-rejecting, and are copied into a lease with the
same property. Neither is a datum, an outcome, a capacity fact, a custody
disposition, a spend fact, or an input to qualification, comparison or blinding.
`A-R6` and `P-R4` state this as closed rules, and `P-R5` routes every deviation
to dominant invalidity.

### §5.8 Counterexample prevented, residual created

| | Option A | Option B |
|---|---|---|
| **prevents** | a conforming implementation that cannot write a valid process claim at all, and the alternative failure in which an implementer invents a sentinel for `process_group_id` that then silently fails §Z4.6 conjunct 7 for every freeze witness in the generation | the same, plus any future route that could smuggle a pid into the supervisor |
| **new residual** | two integers exist in a contaminated address space and in two durable record classes. They confer nothing (§5.6), but the no-second-sink invariant becomes an occurrence-counting property over eight rules rather than a lexical absence, so a future edit that adds a consumer must be caught by `S-25c`/`S-25d`/`S-25e` rather than by reading one line | a durable P1-owned artifact that a peer predicate must dereference, inverting `R-L4` and creating a cross-layer read that did not previously exist |

---

## §6. Scope boundary — an orthogonal defect neither option resolves

While re-deriving the conflict, a **second, independent** defect of the same
root class was found. It is recorded so that it is not silently absorbed into
whichever option is selected.

### §6.1 The two freeze inabilities are different, and this packet keeps them apart (repairs `X m-3`)

```text
CASE 1 — SUPERVISOR CANNOT FREEZE AFTER PCS DEATH. Already documented.
  Actor      : the supervisor
  Trigger    : EOF on the supervisor<->PCS control socket, i.e. PCS death
  Citation   : composite §P1-11.4, line 1781 — "freeze is unavailable, because
               the quiescence proof needs SIGNAL_GROUP, which is a PCS
               operation, so no live stream has a valid continuation"
  Status     : ALREADY RECORDED IN v1.2, with a stated continuation
               (refuse admission; close the update pipe; route to §P1-11.6)

CASE 2 — WATCHDOG CANNOT FREEZE AFTER SUPERVISOR DEATH. The orthogonal defect.
  Actor      : the watchdog
  Trigger    : EOF on the watchdog's update READ end, i.e. SUPERVISOR death
  Citation   : composite §P1-9.2 property 12, line 1464 — on update-pipe EOF it
               "freezes the groups it knows, writes their observations, and
               exits"
  Why it cannot: property 6 (line 1446) confines it to "its two sealed pipes at
               slots 3 and 4"; its fdmap is {3,4,5,7,8,9,10} (lines 680, 978)
               and slot 6 — the sole supervisor<->PCS control socket (line
               1167) — is ABSENT, so it holds no PCS socket and cannot request
               SIGNAL_GROUP; under P1 all process authority is the PCS's; and
               it acts precisely when the supervisor is already dead, so no
               relay exists.
  Status     : NOT RECORDED ANYWHERE AS RESOLVED. This is the defect.

THEY ARE DIFFERENT ACTORS, DIFFERENT TRIGGERS, AND DIFFERENT SECTIONS. Case 1
is not evidence that Case 2 is handled, and Case 2 is not a restatement of
Case 1. v1's §6 risked that conflation; v2 states the distinction literally.
```

The watchdog's freeze witness also carries a numeric `pgid` key (composite
`:2241`, compared at §Z4.6 conjunct 7, `…V2_1_1_CORRECTION.md:1047`), whose
source is the same open question as the claim's `process_group_id`.

### §6.2 Neither option resolves Case 2

**Neither Option A nor Option B resolves this.** A attests numbers to the
*supervisor*, which is dead at that moment and has no channel to the watchdog. B
keeps numbers behind the boundary but supplies the watchdog with no mechanism
either. The defect is orthogonal to this choice, and selecting A or B neither
fixes nor worsens it.

It requires its own author cell, provisionally
`AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`. **It is not opened by this packet
and no option here should be read as addressing it.** It means that even with A
selected, P1 remains non-operative until that cell is resolved — a scope fact,
not a defect in this packet. Both review lines agreed with this quarantine.

---

## §7. Recommendation

### §7.1 Re-evaluated on the corrected figures

Based **only** on the three stated criteria — preserving already signed schemas,
minimizing reopened validity predicates, and keeping the authority boundary
testable — and predicting no outcome and optimizing toward no qualification:

> **Option A remains recommended.**

**The reason v1 gave is withdrawn.** v1 rested the recommendation on "A touches
**one sentence and one response grammar**, while B touches **four schemas and a
signed acceptance predicate**." After `X M-1` and `Y-M2` both halves of that
sentence are false: A also touches the durable journal record format and the
claim-install collision rule, and B touches two record schemas, not four.

**The reason that survives the correction, stated exactly:**

| Criterion | A | B |
|---|---|---|
| preserves already signed **peer** schemas | **yes — `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1` all byte-untouched** | no — claim and lease superseded |
| reopened **validity predicates** | **zero** | at least §Z4.6 conjunct 7, plus every lease reader |
| durable formats changed | **one, and it is P1's own journal** — no peer-owned durable record changes shape | **two peer-owned durable records**, plus a new P1-owned class |
| architectural rules inverted | **none** — `R-L4` holds unchanged (`A-R8`) | `R-L4` inverted; the PCS write surface expanded |
| authority boundary testable | degraded from lexical to **syntactic occurrence counting**, mechanically closed by `S-25a`–`S-25h` and the `A-T5`/`A-T9` fault injections, **without any taint-soundness assumption** | boundary stays lexical, but `R-L4` is inverted and a new cross-layer read appears |
| selectable today | yes | **no** — blocked behind sub-cells `B-1` and `B-2` |

**The decisive facts are the last three rows, and none of them moved under the
correction.** A reopens no validity predicate and inverts no architectural rule;
B does both, and remains non-selectable behind an unsigned authority gap that no
recomputation of blast radius can close. The blast-radius comparison, which is
the figure the reviews corrected, is **no longer the load-bearing argument** —
and v2 says so rather than restating a conclusion on repaired numbers.

**What the correction did cost A.** A's edit surface is materially larger than
v1 represented, and one of its edits — the `J4` record format — is a **durable**
format, which v1 explicitly denied ("nothing durable changes shape"). A reviewer
weighing A should weigh that, not v1's understatement.

**This is a recommendation on stated criteria only. The author does not select.**

### §7.2 Exact v1.3 handoff if `A` is signed

Also requires `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`. Then v1.3:

1. amends the signed sentence exactly as §2.12 renders it, and records the
   weakening token in the authority hierarchy — never presenting it as
   equivalent to the old phrase;
2. rewrites the `AWAIT_STOP` row of §P1-8.3 with operands 11 and 12 and the
   grammar and bounds of §2.2, including `G-1`..`G-6` and the pinned
   `PID_MAX_LIMIT` provenance;
3. adds `A-P1`…`A-P6`, with `A-P4a`..`A-P4d`, as a numbered subsection of
   §P1-9.1, and the cross-field invariant to §P1-8.4;
4. **completes §P1-13.2 row 2**, removing the `BLOCKED` marking and the two
   options, and setting the status line back to
   `CANDIDATE_FOR_INDEPENDENT_X_AND_Y_REVIEW_NOT_ACCEPTED`;
5. adds `A-R1`…`A-R8` to §P1-12 as a closed rule set, and
   `RESTRICTED_PROCESS_IDENTITY` with `C-1`..`C-4`, `P-R1`..`P-R5`,
   `ACC-1`..`ACC-3` and `NC-1`..`NC-3` as a new subsection of §P1-13;
6. adds `S-25a`…`S-25h` to §P1-14.6 CHANGE 3 and updates the edit surface from
   `S-1…S-24b` to `S-1…S-25h`;
7. adds `A-T1`…`A-T12` as test rows 92–103;
8. **NEW — rewrites §P1-8.6**: the `J4` append gains the thirteen-key
   AWAIT_STOP vector of §2.8.2 and the equivalent complete vector for each of
   the other eight opcodes; the `COMPLETED` and `ACKED` replay rows are
   rewritten to the byte-identical redelivery construction of §2.8.3 with
   `R-P1`..`R-P4`; and the §2.10.2 cut matrix replaces the corresponding rows
   of §P1-11.7;
9. **NEW — adds the `EEXIST` rule** `X-1`..`X-4` and the dominant-invalidity
   routing of §2.10.3 and §2.10.4 to the claim-install site named in
   §P1-13.7, cross-referenced to §P1-11.6 and §P1-13.5;
10. recomputes `H_FILE`, `H_BODY`, `H_GUARDDATA`, `H_NORMATIVE`, sentinel
    counts, the placeholder audit and guard fires; required placeholder and
    guard-fire counts remain **zero**.

### §7.3 If `B` is directed

**No v1.3 may be authored yet.** Sub-cells `B-1` and `B-2` must be signed
first, in their own packet. Only then can v1.3 bind `t-process-claim.v2`, the
binding artifact, the rewritten conjunct 7, and the lease successor.

### §7.4 If neither is signed

v1.2 stands as-is: blocked, not operative, with row 2 unfilled. No
implementation may begin, because no conforming implementation can write a valid
process claim.

---

## §8. Tokens and withdrawals

### §8.1 Tokens

Mutually exclusive. **Neither is signable until a bounded independent X-line and
Y-line confirmation round confirms this packet on identical bytes.**

```text
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
```

Selecting A additionally requires the bounded-weakening token of §2.12:

```text
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

Selecting B first requires sub-cells `B-1` and `B-2` (§3.3) and a further
packet. Until then B is **non-selectable**, and this packet says so rather than
offering a choice it cannot honour.

**No token in this packet has been selected, minted, or accepted by the
author.**

### §8.2 The four withdrawn v1 sentences, in one place

```text
W-1  v1 §2.4's sole-sink rule ("There is no second sink … not retained past the
     claim write").                              WITHDRAWN at §2.4 — false.
W-2  v1 §2.7's "exactly as start_identity already is".
                                                 WITHDRAWN at §2.8.1 — unsupported.
W-3  v1 §2.9's "PCS death at any point ⇒ no claim is written".
                                                 WITHDRAWN at §2.10.1 — false.
W-4  v1 §3.2's "t-process-record.v1 … inherits the same key change".
                                                 WITHDRAWN at §3.2 — false.

Also withdrawn: v1 §2.6's rule S-25d and its decidability justification
(§2.5); v1 §1.5 reason 2's overbroad argv-evidence claim (§1.5 R-4); v1 §5.5's
"nothing durable changes shape" and v1 §7's "A touches one sentence and one
response grammar" (§5.5, §7.1).

No withdrawn sentence is restated anywhere in v2 in paraphrase. §0's table maps
each to its repair.
```

---

## §9. Invariants this packet leaves exactly as they were

```text
N-1  The identity conflict is real and loud. §1 states it without softening.
N-2  Option A is an EXPLICIT weakening of the lexical "cannot express a PID"
     sentence, with its own token, its old and new text side by side, and a
     plain statement of what is given up (§2.12). It is not a reinterpretation.
N-3  Observing a PID/PGID does not grant authorized process-control authority.
     Only handles, the closed request grammar, and PCS execution do (§5.6,
     A-R1..A-R8).
N-4  Both-or-neither tuple semantics (G-4), the stopped/unreaped direct-child
     proof (A-P1..A-P6), the PID-reuse binding (§2.9), fail-closed absence
     (G-5, G-6, Z1-R6), and no re-observation on replay (R-P1..R-P4) all hold.
N-5  The watchdog-freeze cell is orthogonal and UNRESOLVED by this packet (§6).
N-6  T = NOT_ACTIVATED; the programme claim is OPEN.
```

---

## §10. Negative space

This packet creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no process,
socket, pipe, fork, exec, signal, wait or `prctl` operation, no supervisor, PCS,
controller, worker or watchdog, no capability, world, learner, entropy, capacity
artifact, custody disposition, result manifest, spend, datum, outcome, Proof or
claim movement. It predicts no qualification and no comparison outcome. It
selects neither option and mints no token. `T` remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.
