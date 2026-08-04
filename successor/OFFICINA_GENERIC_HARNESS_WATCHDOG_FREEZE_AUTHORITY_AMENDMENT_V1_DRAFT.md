# Officina generic-harness — watchdog freeze-authority amendment, version 1 (draft)

**This document is a new, separately reviewable amendment to the accepted
generic-harness contract chain.** It is the **sole live peer-layer authority**
for watchdog liveness, freeze execution, freeze evidence and freeze-evidence
acceptance. It is written to be read without opening any historical
supervisor/control-channel document.

**Author.** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This document selects nothing.**

**Status.** `NOT_ACCEPTED`. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1`
is **not signable** and is not made signable here. It becomes signable only
after a bounded independent X-line and Y-line final confirmation round on
identical bytes, and only jointly with the P1 operative composite v1.3 under
the single atomic handoff of §A9. This document creates nothing executable and
authorizes no implementation, activation, process control, resource spend,
T/Q/C datum, outcome, Proof or claim movement. `T` is `NOT_ACTIVATED`; the
programme claim is `OPEN`.

---

## §A0. What this document is, and what it replaces

### §A0.1 Position in the accepted chain

```text
ACCEPTED GENERIC-HARNESS CHAIN, byte-intact, carried forward in full except
where §A2 replaces it:

  64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71
    successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
  6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077
    successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
  624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f
    successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
  b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154
    successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
  724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0
    successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md   ← chain end
  8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a
    successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md

THIS AMENDMENT IS AN ADDITION TO THAT CHAIN. It edits none of those bytes.
Where this amendment and any of them differ, THIS AMENDMENT GOVERNS, and the
only such difference is the one named at §A2.1.
```

### §A0.2 The document-level authority rule this amendment obeys

```text
DA-1  THE SUPERVISOR/CONTROL-CHANNEL HISTORICAL CHAIN IS IMMUTABLE PROVENANCE,
      IN WHOLE, AT DOCUMENT GRANULARITY. Every earlier supervisor/control-channel
      draft, every correction v2.1 through v2.1.10.7, the v2.1.10.4 P1 binding,
      and P1 operative composite versions 1, 1.1 and 1.2 are historical evidence
      only. NO implementer, verifier or reviewer opens any of them to determine
      behaviour or to verify a build.

DA-2  IMMUTABILITY ATTACHES TO DOCUMENTS, NOT TO PARAGRAPHS. There is no
      file-internal split by which some sections of a historical document remain
      operative while others are provenance. A cross-reference from one
      historical document to another does not reactivate either.

DA-3  THIS AMENDMENT DOES NOT EDIT HISTORY. It restates, in its own bytes, every
      peer rule that must be live, so that the historical sections named at §A2
      never have to be opened. Their bytes remain exactly as committed.

DA-4  THE TWO LIVE AUTHORITY SURFACES FOR THIS REPAIR ARE EXACTLY TWO:
        this amendment                     — peer-layer behaviour
        P1 operative composite v1.3        — P1 interface, execution, writer,
                                             predicate and invariant surface
      Nothing else is opened for behaviour. §A9 lands them together or not at
      all.
```

**Why this rule and not the tier-1/tier-2 split of the withdrawn v2.2 packet.**
The withdrawn approach classified individual sections inside historical
documents as operative and others as immutable, then directed replacements into
the operative ones. Both independent review lines rejected it. The Y line held
that the composite's immutability is categorical and attaches to documents. The
X line found, independently, that the split had already failed on its own terms:
a governing locus (historical §W6.5) that satisfied the split's own operative
test was omitted from the enumeration, and the enumeration method could not have
found it. **A classification that cannot be enumerated reliably is not an
authority rule.** `DA-1`..`DA-4` remove the need to enumerate at all: nothing
historical is live, so nothing historical can hide a live authority.

---

## §A1. The rule, stated once, before any mechanism

```text
WA-1  ONE FREEZE EXECUTOR. The SUPERVISOR role process executes every freeze in
      this contract. It reaches every group stop through the P1 `SIGNAL_GROUP`
      opcode and executes no group stop in its own address space.

WA-2  ONE FREEZE-EVIDENCE WRITER. The SUPERVISOR role process is the only writer
      of `philosophia.officina.t-freeze-observation.v1`, on every route, at
      every deadline, under `T_RUNTIME.lock`.

WA-3  THE WATCHDOG OBSERVES AND NOTHING ELSE. The watchdog role process is a
      control-plane LIVENESS SENSOR. On no path does it:
        execute a freeze          prove quiescence        send any signal
        call `killpg` or `kill`   write freeze evidence   write under `runtime/`
        append the ledger         settle anything         hold a runtime lock
        hold a capability         exercise validity authority
      It owns a deadline as a DATUM it publishes an acknowledgement for. It
      never owns a deadline as an ACTION.

WA-4  EXACTLY ONE READ. The watchdog performs exactly one peer-layer operation
      on a peer-owned object: the READ-ONLY verification of the supervisor
      identity record, and never any inference from a parent relationship. A
      read installs nothing, decides nothing, and enters no acceptance
      predicate. `WA-3` is not weakened by it.

WA-5  `killer == SUPERVISOR` ON EVERY ADMISSIBLE OBJECT. The schema enum
      `killer ∈ {WATCHDOG, SUPERVISOR}` is RETAINED byte-unchanged so that
      legacy and forged objects can be REJECTED rather than fail to parse. The
      value `WATCHDOG` has no admissible writer and is unreachable by
      construction. §A5 conjunct 8 rejects it.

WA-6  NO SECOND WRITER AND NO NEW EVIDENCE CLASS. This amendment removes an
      executor and an evidence writer. It adds neither. It creates no new record
      class, no new namespace and no new schema.
```

---

## §A2. The supersession of the historical texts, by meaning, without editing them

### §A2.1 Accepted harness §5a — the one difference from the accepted chain

```text
THE SUPERSEDED SENTENCE, quoted for identification only, from
OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md §5a (64b8d3f6…), which is NOT
edited by this amendment and whose bytes remain exactly as committed:

  "The watchdog owns the deadline and executes the v2.1 §1 sequence at or
   before it (revoke → freeze/terminate → backend synchronize → prove
   quiescence → durably settle actual E1 per §4c)."

THE GOVERNING RULE THAT REPLACES ITS MEANING:

  The watchdog owns the deadline and OBSERVES it. It executes no step of the
  sequence. The SUPERVISOR executes the sequence — revoke → freeze/terminate →
  backend synchronize → prove quiescence → durably settle actual E1 per §4c —
  reaching every group stop through `SIGNAL_GROUP`, and writing the one freeze
  observation itself. The TIMING guarantee is separately weakened by §A2.3.

NOTHING ELSE IN §5a MOVES. §4b's and §4c's "watchdog deadline" remain DURATION
NAMES and name no actor. §4d's batch names no actor and runs in a runtime-lock
epoch only the supervisor holds. §1 item 5's "a missed deadline invokes §5a
quiescence" names no actor and is unaffected.
```

### §A2.2 Historical §W6.5 — superseded in meaning, not edited

**This section exists because the X line found that historical §W6.5 assigns the
watchdog both freeze execution and freeze recording, is carried by name as a
live rule in ten later historical documents, and was omitted from the withdrawn
v2.2 enumeration.** Under `DA-1` it is now provenance and is not edited. Its
meaning is superseded here so that no reader can reach it as authority.

```text
THE HISTORICAL TEXT, quoted for identification only, from
…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:1331-1342 (9f1d018e…), whose
bytes remain exactly as committed:

  "### W6.5 Explicit supersession of the signed predecessor sentence (X-M9i)
   Signed harness §5a reads: 'The watchdog owns the deadline and executes the
   v2.1 §1 sequence at or before it.' That sentence is explicitly superseded by
   §W3.1/§W3.3/§W3.4: on non-real-time Linux the watchdog owns the deadline and
   executes the sequence as soon as it is scheduled after the deadline, records
   the conservative proved-freeze instant, and every positive overrun is routed
   to the signed invalid/recovery destinations with full §4c charging. …"

ITS TWO CARRIED COMPANION LOCI, likewise provenance and likewise not edited:
  …V2_1_CORRECTION.md:88          the §V2.0 replacement-index row
  …V2_1_CORRECTION.md:1582-1586   the §W11 compatibility classification

ITS TEN CARRYING REFERENCES, likewise provenance and likewise not edited:
  …V2_1_1_CORRECTION.md:124, :125   …V2_1_2_CORRECTION.md:106
  …V2_1_3_CORRECTION.md:1382        …V2_1_4_CORRECTION.md:1114
  …V2_1_5_CORRECTION.md:663         …V2_1_6_CORRECTION.md:776
  …V2_1_7_CORRECTION.md:836         …V2_1_8_CORRECTION.md:1414
  …V2_1_9_CORRECTION.md:1194        …V2_1_10_CORRECTION.md:1457

WHAT IS SUPERSEDED, EXACTLY, AND WHAT IS NOT:

  SUPERSEDED — THE ACTOR. Every clause of the historical section that makes the
    watchdog the executor of the sequence, the prover of quiescence, or the
    recorder of the proved-freeze instant is superseded in whole by `WA-1`,
    `WA-2` and `WA-3` of this amendment. No reading of the historical section
    restores a watchdog executor, a watchdog quiescence proof or a watchdog
    evidence writer.

  RETAINED — THE TIMING WEAKENING, RE-STATED AT §A2.3 IN THIS DOCUMENT'S OWN
    BYTES. The historical section's honest engineering point — that no ordinary
    scheduled userspace process can be guaranteed to execute AT OR BEFORE a
    monotonic deadline on non-real-time Linux — is correct, is not withdrawn,
    and is carried forward here with the actor corrected.

  THE HISTORICAL SECTION IS NOT AUTHORITY FOR ANYTHING. Under `DA-1` it is not
    opened for behaviour. §A2.3 is the live statement. This subsection exists so
    that a reviewer who encounters the historical text in the provenance
    inventory can see, without opening it, exactly what happened to it.
```

### §A2.3 The timing guarantee, stated honestly, with the actor corrected

```text
TIMING-1  NO PHYSICAL AT-OR-BEFORE GUARANTEE IS CLAIMED. No claim is made that
          an ordinary scheduled userspace process physically executes at or
          before a monotonic deadline under every host schedule, cgroup throttle
          or runnable-queue delay. This is retained from the historical
          engineering finding and is not weakened.

TIMING-2  WHAT IS GUARANTEED. The SUPERVISOR executes the §A3 sequence AS SOON
          AS IT IS SCHEDULED AFTER the deadline is observed, records the
          conservative proved-freeze instant itself, and never synthesizes a
          timestamp it did not sample.

TIMING-3  EVERY POSITIVE OVERRUN IS ROUTED, NOT ABSORBED. `overrun_ns` is
          strictly positive by construction (§A3.4), and every positive overrun
          routes to the signed invalid/recovery destinations with full §4c
          charging. There is no zero-overrun branch, no tolerance constant, and
          none may be introduced.

TIMING-4  THE WEAKENING IS OF THE GUARANTEE, NOT OF THE OBLIGATION. The
          supervisor may not defer the sequence, batch it, or let a deadline
          pass unserved; it must enter §A3 at the first scheduling opportunity
          after the deadline is observed under the lock.
```

---

## §A3. The freeze sequence — one procedure, two named entry routes

**This section is self-contained. It restates the sequence in this document's
own bytes so that no historical section is opened.**

### §A3.1 The two entry routes, total and explicit

**These two routes are exhaustive. There is no third entry to §A3, and no other
process enters it on any path.**

```text
ROUTE-D  ORDINARY LEASE-DEADLINE ENTRY.
         TRIGGER    Under `T_RUNTIME.lock`, the SUPERVISOR's own clock shows
                    `now_ns ≥ deadline_ns` for a live lease row, and the
                    watchdog is NOT declared dead.
         ACTOR      the supervisor role process
         PRECONDITION  the §A3.2 drain, which is mandatory on this route
         killer     `SUPERVISOR`
         EVIDENCE   one `t-freeze-observation.v1`, supervisor-written
         MEDIATION  every group stop through `SIGNAL_GROUP`
         NOTE       This is the ORDINARY route. It is the route taken while the
                    watchdog is alive and healthy. The watchdog contributes its
                    acknowledgement state to the §A3.2 drain and contributes
                    nothing else.

ROUTE-W  DEAD-WATCHDOG RECOVERY ENTRY.
         TRIGGER    Under `T_RUNTIME.lock`, the ack pipe has been drained and
                    `now_ns − updated_monotonic_ns > T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS`
                    with no ack for that `table_seq` — the watchdog is declared
                    dead — and one or more groups are live.
         ACTOR      the supervisor role process
         PRECONDITION  none beyond the declaration; the drain is vacuous because
                    there is no live acknowledger
         killer     `SUPERVISOR`
         EVIDENCE   one `t-freeze-observation.v1` per affected group,
                    supervisor-written
         MEDIATION  every group stop through `SIGNAL_GROUP`
         AFTER      the supervisor refuses admissions, obtains a replacement
                    watchdog, awaits its acknowledgement, then settles every
                    overdue lease per §A4. The overdue / non-overdue split of
                    §A7 applies unchanged.

BOTH ROUTES ARE THE SAME PROCEDURE WITH THE SAME ACTOR, THE SAME MEDIATION, THE
SAME EVIDENCE CLASS, THE SAME NAMESPACE, THE SAME WRITER AND THE SAME `killer`
VALUE. They differ only in trigger and in what follows the freeze. THIS IS NOT
TWO WRITERS AND NOT TWO EVIDENCE CLASSES.
```

**Why both must be named.** The withdrawn v2.2 packet stated the supervisor's
entry as "the dead-watchdog route" everywhere, while simultaneously making the
supervisor's own clock the trigger at an ordinary lease deadline. Both review
lines found the contradiction. Removing the watchdog as executor necessarily
makes the ordinary deadline a supervisor entry; the honest repair is to name it,
not to hide it inside a recovery route it is not.

### §A3.2 The drain, mandatory on `ROUTE-D`

```text
Before entering §A3.3 on `ROUTE-D`, the supervisor:
  1. drains the watchdog ack pipe nonblocking;
  2. re-reads its own durable `LEASES.json`;
  3. if a strictly greater `table_seq` is durable AND acked, re-evaluates
     against the newest acked row and does not freeze against the superseded
     deadline;
  4. only if no newer acked table exists does it proceed to §A3.3.

A legitimately renewed lease therefore cannot be frozen against a superseded
deadline, and the freeze decision is always taken against the newest table the
SUPERVISOR can prove acked at that instant.

ON RENEWAL the old deadline remains authoritative until the successor table is
acked. No unacknowledged update ever extends behaviour.
```

### §A3.3 The sequence — steps 1 through 6

```text
Executed by the SUPERVISOR role process, under `T_RUNTIME.lock`, identically on
`ROUTE-D` and `ROUTE-W`:

1. verify `/proc/<leader>/stat` start identity matches the claim's
   `controller_start_identity`; on mismatch, SKIP this group — PID reuse means
   the stream is lost and routes to §4c(c);

2. stop the group: `SIGSTOP` to the process group, REACHED THROUGH THE
   `SIGNAL_GROUP` OPCODE. The supervisor executes no `killpg` and no `kill` in
   its own address space, on this or any step;

3. PROVE QUIESCENCE: enumerate the recorded group members and every `/proc`
   process whose session id or parent chain reaches a recorded member; require
   each to be absent or in state `T` or `Z`. Repeat at
   `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS` up to `T_WATCHDOG_QUIESCE_MAX_PASSES`,
   issuing `SIGKILL` to the process group THROUGH `SIGNAL_GROUP` after the first
   failed pass;

4. on the pass that proves every reachable member absent, `T` or `Z`, apply the
   STRICT-PROGRESS rule of §A3.4;

5. if the passes are exhausted, or a reachable process is neither stopped, dead
   nor absent, set `freeze_ns = null`, `overrun_ns = null`,
   `quiescence = UNKNOWN`;

6. the SUPERVISOR writes `WATCHDOG/FREEZE/<witness_id>.json` (§A4), atomic
   no-replace, file `fsync`, parent-directory `fsync`, then emits the event on
   the pipe.

`quiescence = PROVED` is a PROCESS-TREE fact — every recorded group member and
every `/proc` process whose session id or parent chain reaches a recorded member
is absent, `T` or `Z` — and explicitly NOT a backend fact. Signed §4d step 3's
backend synchronization remains the supervisor's separate settlement obligation.

`freeze_ns` is the conservative monotonic observation at which the whole
declared tree is proved stopped or dead. IT IS NEVER THE SIGNAL-SEND TIME.

A doubly detached descendant is outside the enumeration by construction and
remains the A3 procedural residual. No cgroup, PID namespace or
`PR_SET_CHILD_SUBREAPER` is available, so a controller's own new-session child
leaves the frozen group; the fail-closed quiescence scan detects it and routes
to unknown recovery rather than pretending the group stop covered it.
```

### §A3.4 Strict progress, not asserted progress

```text
on the pass that proves every reachable member absent / T / Z:
    sample s = clock_gettime_ns(CLOCK_MONOTONIC)
    if s > deadline_ns:
        freeze_ns = s; quiescence = PROVED; overrun_ns = s - deadline_ns  (> 0)
    else:                       # s == deadline_ns, or a non-monotonic sample
        take up to T_WATCHDOG_QUIESCE_MAX_PASSES further samples at
        T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS, RE-PROVING quiescence each pass;
        the first sample with s > deadline_ns and quiescence still proved
        ⇒ PROVED with overrun_ns = s - deadline_ns
        exhausted without strict progress
        ⇒ freeze_ns = null; overrun_ns = null; quiescence = UNKNOWN

There is no zero-overrun branch, no tolerance constant, and no valid terminal
reachable from any freeze.

The clock is `CLOCK_MONOTONIC`, pinned by the platform constant
`_CLOCK_MONOTONIC`. No other clock is sampled for this purpose on any path.
```

### §A3.5 What the watchdog does at a deadline

```text
NOTHING. The watchdog acknowledges published lease tables and observes its
update pipe. At a deadline it takes no action of any kind. On update-pipe EOF —
which is the single supervisor-death detector — it WRITES NOTHING, FREEZES
NOTHING, SIGNALS NOTHING, and exits, settling nothing. No freeze occurs on the
supervisor-death path, because the only freeze executor is the now-dead
supervisor; every affected group is settled by the next supervisor takeover
through the signed invalid route.

A lost observation is NEVER reconstructed. There is exactly one writer and it is
the supervisor, so the object is absent only when the supervisor did not write
it. On absence the supervisor takes the §A6 `ABSENT` fallback route. Any rule
that conditioned a supervisor write on WATCHDOG DEATH is withdrawn in meaning:
after this amendment there is no other writer to be dead.
```

---

## §A4. The freeze-evidence object — naming, identity, ordering

```text
witness_id = SHA-256(canonical {
  supervisor_generation_sha256, process_id, table_seq })

PATH   successor/officina/runtime_control/T_SUPERVISOR/WATCHDOG/FREEZE/<witness_id>.json

SCHEMA philosophia.officina.t-freeze-observation.v1, atomic no-replace,
KEYS EXACTLY:
  schema, scientific_outcome, supervisor_generation_sha256, witness_id,
  process_id, pgid, start_identity, deadline_ns, freeze_ns_or_null,
  quiescence ∈ {PROVED, UNKNOWN}, overrun_ns_or_null,
  killer ∈ {WATCHDOG, SUPERVISOR}, unresolved_member_count (int),
  table_seq, created_utc
```

```text
F-1  THE FILENAME QUESTION IS CLOSED AND IS NOT AN AUTHOR CHOICE. The witness
     path is `<witness_id>.json`. Any document presenting `<process_id>.json`
     versus `<witness_id>.json` as an open question is wrong. The `<process_id>`
     spelling belonged to a historical predecessor sentence that a later
     historical correction expressly replaced before this cell existed.

F-2  `process_id` IS A MEMBER OF THE PREIMAGE AND A MANDATORY RECORD FIELD. It
     is NOT the filename and it is NOT a PID. It remains a CONSTRUCTIBLE OPAQUE
     CLAIM IDENTIFIER. The process-claim identity cell is neither selected nor
     repaired by this amendment.

F-3  PRODUCTION ORDER. The SUPERVISOR — the sole writer of this object —
     re-reads the supervisor identity record and REFUSES TO WRITE on generation
     mismatch; then writes the file (same-directory temp → file `fsync` → atomic
     no-replace → parent `fsync`); THEN emits the pipe event. A no-replace
     `EEXIST` means an identical `(generation, process_id, table_seq)` witness
     already exists: the writer emits the event and writes nothing further.

F-4  CONSUMPTION ORDER. Witnesses are consumed sorted by
     `(generation == current) desc, table_seq asc, process_id asc`. The earliest
     `table_seq` for a process in the current generation is authoritative; later
     same-process witnesses are retained as duplicates, not consumed twice.

F-5  REPLAY NAMING. The generation is INSIDE the name, so a stale
     cross-generation collision on a no-replace path is impossible. A
     prior-generation witness fails §A5 conjunct 3 and takes the `UNKNOWN` route.

F-6  REMOVAL. By the supervisor, after the settlement's archival commit. Never
     by any other actor and never to make room.

F-7  NOTHING ABOUT THE WRITER MOVES `F-1`..`F-6`. Object identity, replay key and
     evidence filename are functions of `(generation, process_id, table_seq)`
     alone. This amendment changes WHO writes, not WHAT is named.

F-8  THE `WATCHDOG/` NAMESPACE IS RETAINED AND IS NOT RENAMED. `WATCHDOG/**`
     remains control plane and archival-excluded. Renaming it would move every
     `witness_id` path, every archival-exclusion rule and every settlement
     locator for cosmetic gain. THE NAME IS HISTORICAL AND CARRIES NO AUTHORITY:
     no rule of this amendment reads the namespace string to decide who may
     write. A reader must not infer a watchdog writer from the namespace name.
```

---

## §A5. The acceptance predicate — the indisputably governing bytes

**This is the single live acceptance predicate for freeze evidence. It is
stated here and nowhere else.** Under `T_RUNTIME.lock`, an observation becomes
evidence **only if every conjunct holds**:

```text
 1. it validates against `t-freeze-observation.v1` exactly: key set, types,
    strict int, enums, recursive scientific-field rejection;

 2. `witness_id` recomputes exactly from
    `(supervisor_generation_sha256, process_id, table_seq)` and equals the
    filename;

 3. `supervisor_generation_sha256 == the current generation`;

 4. `table_seq` is the supervisor's current watchdog table sequence for that
    lease, or an earlier sequence whose row for this `process_id` carried an
    IDENTICAL `deadline_ns`;

 5. `process_id` names a durable claim whose lease was live at that `table_seq`;

 6. `deadline_ns` equals BOTH that table row's deadline AND the supervisor's
    current durable lease deadline for that process;

 7. `pgid == the claim's process_group_id` and
    `start_identity == the claim's controller_start_identity`;

 8. `killer == SUPERVISOR`.
    THE WATCHDOG ROLE PROCESS WRITES NO RECORD OF THIS CLASS ON ANY PATH, SO AN
    OBSERVATION CARRYING `killer == WATCHDOG` HAS NO ADMISSIBLE WRITER. It fails
    this conjunct on every path, is PERMANENTLY NON-EVIDENCE, and routes to the
    §A6 fallback with `rejection_conjunct = 8`. The schema enum
    `killer ∈ {WATCHDOG, SUPERVISOR}` is RETAINED UNCHANGED — the peer schema is
    not reopened — and the `WATCHDOG` value is unreachable BY CONSTRUCTION
    rather than by deletion, so that a legacy, stale or forged object is
    REJECTED rather than unparseable;

 9. `quiescence == PROVED` ⇒ `freeze_ns` is int, `freeze_ns > deadline_ns`,
    `overrun_ns == freeze_ns - deadline_ns`, `unresolved_member_count == 0`;
    `quiescence == UNKNOWN` ⇒ `freeze_ns` is null, `overrun_ns` is null,
    `unresolved_member_count ≥ 1`.
    THIS CONJUNCT BINDS THIS OBJECT ONLY. It does not bind the §A6 fallback,
    whose `current_unresolved_member_count` is a different key with a different
    meaning;

10. the supervisor independently proves the group quiescent NOW, by the §A3.3
    step-3 enumeration.
```

```text
KW-1  `killer == WATCHDOG` CANNOT RE-ENTER BY ANY MECHANISM. There is no
      default, no migration, no compatibility shim, no recovery path, no
      archival re-import, no takeover re-derivation and no test fixture that may
      set, coerce, infer or grandfather the value `WATCHDOG` into an admissible
      object. Conjunct 8 is evaluated on every path, before any settlement
      effect, with no exception clause of any kind.

KW-2  A FIXTURE THAT NARROWS THE ENUM FAILS. The enum retains both values. A
      build or fixture asserting `killer ∈ {SUPERVISOR}` fails, because
      narrowing it would make a legacy object unparseable instead of rejected,
      and rejection is the stronger discipline.

KW-3  ANY malformed, missing, conflicting or unverifiable fact — a planted or
      stale file, an A3-procedural forgery, a generation or `table_seq`
      mismatch, an inconsistent member count, a `freeze_ns ≤ deadline_ns` —
      makes the object NOT EVIDENCE. It never becomes valid evidence, never
      yields a valid terminal, and never contributes an accepted timestamp. The
      rejected object is NEVER overwritten, truncated, renamed or deleted to
      make room.
```

---

## §A6. The fallback — a distinct object, distinct namespace, distinct schema

```text
fallback_witness_id = SHA-256(canonical {
  "schema": "philosophia.officina.t-freeze-fallback-id.v1",   # domain tag
  "supervisor_generation_sha256": …,
  "process_id": …,
  "table_seq": …,
  "rejected_witness_path_or_null": …,
  "rejected_object_sha256_or_null": …
})

PATH  runtime_control/T_SUPERVISOR/WATCHDOG/FREEZE_FALLBACK/<fallback_witness_id>.json

SCHEMA philosophia.officina.t-freeze-fallback-observation.v1
atomic no-replace, written by the SUPERVISOR under `T_RUNTIME.lock`,
KEYS EXACTLY:
  schema, scientific_outcome, supervisor_generation_sha256,
  fallback_witness_id, process_id, pgid, start_identity, deadline_ns,
  table_seq, rejected_witness_path_or_null, rejected_object_sha256_or_null,
  rejection_conjunct (int 0..10; 0 == the ABSENT sentinel, else the §A5
    conjunct number that failed first, in ascending order),
  unknown_reason ∈ {EVIDENCE_ABSENT, EVIDENCE_UNVERIFIABLE,
                    FREEZE_INSTANT_UNKNOWN},
  current_unresolved_member_count (int ≥ 0),
  supervisor_quiescence ∈ {PROVED, UNKNOWN},
  killer ("SUPERVISOR"), created_utc
```

```text
S-1  SEPARATE OBJECT. The fallback is NOT of the §A4 class, is NOT written by
     §A4's writer acting in §A4's capacity, and is NOT installed in §A4's
     namespace. Its id is domain-tagged and cannot collide with `witness_id`.

S-2  SEPARATE ROUTING, SAME DESTINATION FAMILY. A fallback drives exactly the
     signed route for `UNKNOWN`: record-first live-process invalidity, the
     all-live batch with the unknowable pool, public cause `PROCESS`, and full
     §4c charging. No fallback can select a valid terminal, a zero-overrun
     branch, a synthesized freeze instant or an `overrun_ns`.

S-3  SEPARATE COUNT KEY. `current_unresolved_member_count` is the fallback's own
     key and is never the §A4 object's `unresolved_member_count`. The two are
     never equated, never renamed into one another, and never substituted.

S-4  NULLABLE ABSENT VALUES. On the `ABSENT` sentinel,
     `rejected_witness_path_or_null` and `rejected_object_sha256_or_null` are
     null and `rejection_conjunct = 0`. `process_id` is MANDATORY AND NON-NULL
     ON EVERY FALLBACK BRANCH, including this one.

S-5  THE WATCHDOG HAS NO PATH HERE. The fallback namespace is one the watchdog
     cannot reach and never writes, before and after this amendment.
```

---

## §A7. The swap-only carve-out — no witness where no deadline was reached

```text
When the supervisor freezes a group SOLELY to replace a watchdog, and that
group's lease deadline has NOT been reached:

  NO §A3 witness is written. The group is recorded by a
  `t-replacement-freeze.v1` object under
  `WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json` with
  `swap_only: true`, written by the SUPERVISOR under the runtime lock, and the
  group is resumed under the recorded resume predicate.

  `supervisor_stop_monotonic_ns` is never used to compute `overrun_ns`, is
  never consumed as a §A3/§A5 witness, and is never citable.
  `REPLACEMENT_FREEZE/**` is unreachable by the watchdog on every path.

When the deadline HAS been reached, the group takes `ROUTE-W` of §A3.1 and a
witness IS written. The overdue / non-overdue split is total: every group in a
dead-watchdog recovery falls in exactly one branch.
```

---

## §A8. Negative surface of the watchdog role, asserted rather than described

```text
NS-1  In the watchdog role process, on every path: no signal is sent, no signal
      is received from any process of this contract, no `killpg`, no `kill`, no
      quiescence proof, no evidence write, no settlement, no `runtime/` write,
      no ledger append, no runtime lock, no capability, and no validity
      authority.

NS-2  The single permitted peer operation is the read-only supervisor-identity
      verification of `WA-4`. It is REQUIRED, not merely permitted: a build in
      which the watchdog does not perform it, or infers supervisor identity from
      any parent relationship instead, FAILS.

NS-3  The watchdog produces NO DURABLE OBJECT of any class. It is therefore not
      a witness in any sense, because there is no object for it to be a witness
      in.

NS-4  The watchdog acknowledges published lease tables on its ack pipe. Liveness
      is judged on the watchdog's OWN sample, never on the supervisor's read
      time.
```

---

## §A9. The atomic handoff — this amendment and composite v1.3, together or not at all

```text
H-1  ONE UNIT. This amendment and
     `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md`
     are ONE indivisible acceptance unit. Neither is operative alone. Accepting
     one without the other is NOT A CONFORMING STATE and is not a partial
     success.

H-2  NO HISTORICAL BYTE MOVES. Every historical supervisor/control-channel
     document, every accepted generic-harness chain file, the batch-settlement
     chain and both signatures remain BYTE-IDENTICAL. The handoff verifies this
     by digest before it may proceed.

H-3  FAIL-CLOSED ON PARTIAL OR STALE INSTALLATION. The verifier computes the
     digest of this amendment and of composite v1.3 and compares both against
     the manifest. On ANY mismatch, absence, extra file, or digest of a
     historical file that differs from its recorded value, the verifier REFUSES
     with `WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE`, and NO process is created, NO
     freeze route is reachable, NO evidence is accepted and NO settlement runs.
     A partially installed state never satisfies this contract and never
     silently degrades to the historical behaviour.

H-4  THE FULL LIST IS AT §C4 OF THE COMPANION CLOSURE and is identical in both
     documents. This section is the peer-layer half of one statement.
```

---

## §A10. What this amendment does not do

```text
N-1   IT SELECTS NO OPTION. Neither `W-A` (watchdog requests, PCS executes) nor
      `W-B` (PCS freezes on peer-endpoint loss) is selected. The watchdog-freeze
      author cell remains OPEN.
N-2   IT MOVES NO RECOMMENDATION. `W-B` remains recommended on the same five
      criteria, and nothing here is asymmetric between the options.
N-3   IT OPENS NO NEW AUTHOR CELL and adds, removes and renames no token.
N-4   IT DOES NOT REOPEN THE PROCESS-CLAIM IDENTITY CELL. `process_id` remains a
      constructible opaque claim identifier, mandatory and non-null.
N-5   IT REVOKES NO SIGNED SELECTION.
      `I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER` is not revoked, not
      re-run and not reopened. The signed selection retains a DEDICATED WATCHDOG
      PROCESS. Its freezer and witness content is amended by
      `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`.
N-6   IT EDITS NO HISTORICAL BYTE.
N-7   IT REOPENS NO PEER SCHEMA. `t-freeze-observation.v1` keeps its exact key
      set and its `killer` enum.
N-8   IT CREATES NO NEW RECORD CLASS, NAMESPACE OR SCHEMA.
```

---

## §A11. Negative space

This amendment creates nothing executable and authorizes no selection, X/Y
verdict, acceptance, implementation, commit, verifier or manifest edit, process,
socket, pipe, fork, exec, signal, wait or `prctl` operation, supervisor, PCS,
controller, worker or watchdog, capability, world, learner, entropy, candidate,
trajectory, capacity artifact, custody disposition, result manifest, spend,
datum, outcome, Proof or claim movement. No freeze was executed, requested,
journalled or witnessed. No `/proc` was read against any live process. No clock
was sampled for any contract purpose. It predicts no qualification and no
comparison outcome. It modified no existing file. `T` remains `NOT_ACTIVATED`;
the programme claim remains `OPEN`.
