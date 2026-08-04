# Officina generic-harness — watchdog freeze-authority amendment, version 1.3 (draft)

**This document WHOLLY REPLACES version 1.2 (`058c119c…`), which wholly replaced
version 1.1 (`ec5ddff8…`), which wholly replaced version 1 (`380b87f0…`).** It
is not a delta over any of them, does not require any of them to be read, and
after acceptance all three are provenance.
It is the **sole live peer-layer authority** for watchdog liveness, freeze
execution, freeze evidence, freeze-evidence acceptance, the swap-only carve-out
and the joint installation. **It is written to be read without opening any
historical supervisor/control-channel document.**

**Author.** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This document selects nothing.**

**Status.** `NOT_ACCEPTED`.
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3` is
**not signable** and is not made signable here. It becomes signable only after a
bounded independent X-line and Y-line confirmation round on identical bytes,
performed by reviewers that did not author v2.3, v2.4, v2.5 or v2.6, and only
jointly with P1 operative composite v1.6 under the single atomic handoff of §A9.
The token is VERSION-BUMPED ONLY: it opens no option and selects nothing. This
document creates nothing executable and authorizes no implementation,
activation, process control, resource spend, T/Q/C datum, outcome, Proof or
claim movement. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`.

---

## §A0. Position, authority rule, and what changed from v1

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
  b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9
    successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md

THIS AMENDMENT IS AN ADDITION TO THAT CHAIN. It edits none of those bytes.
Where this amendment and any of them differ, THIS AMENDMENT GOVERNS, and the
only such difference is the one named at §A2.1.
```

### §A0.2 The document-level authority rule

```text
DA-1  THE SUPERVISOR/CONTROL-CHANNEL HISTORICAL CHAIN IS IMMUTABLE PROVENANCE,
      IN WHOLE, AT DOCUMENT GRANULARITY. Every earlier supervisor/control-channel
      draft, every correction v2.1 through v2.1.10.7, the v2.1.10.4 P1 binding,
      P1 operative composite versions 1, 1.1, 1.2, 1.3, 1.4 and 1.5, and
      versions 1, 1.1 and 1.2 of this amendment, are historical evidence only. NO implementer, verifier or reviewer opens any of them to
      determine behaviour or to verify a build.

DA-2  IMMUTABILITY ATTACHES TO DOCUMENTS, NOT TO PARAGRAPHS. There is no
      file-internal split by which some sections of a historical document remain
      operative while others are provenance. A cross-reference from one
      historical document to another does not reactivate either.

DA-3  THIS AMENDMENT DOES NOT EDIT HISTORY. It restates, in its own bytes, every
      peer rule that must be live. Their bytes remain exactly as committed.

DA-4  THE TWO LIVE SPECIFICATION SURFACES ARE EXACTLY TWO:
        this amendment (v1.3)               — peer-layer behaviour
        P1 operative composite v1.6         — P1 interface, execution, writer,
                                              predicate and invariant surface
      Nothing else is opened for behaviour. The install record of §A10 is a
      GENERATED ARTIFACT, not a specification surface: it carries digests and
      no rules. THE STAGE-A AND STAGE-B AUTHORIZATION ARTIFACTS OF §A10 ARE
      LIKEWISE GENERATED ARTIFACTS AND ARE NOT SPECIFICATION SURFACES: they
      carry values, a key and a signature, and no rules.

DA-5  NO NORMATIVE DEPENDENCY ON ANY AUTHOR CLOSURE. Every author closure is an
      untrusted self-assessment. No rule, list, digest set or handoff step of
      this amendment is stated only in a closure. The COMPLETE handoff is at
      §A9 of this file, whose ordered steps are `OR-1`..`OR-11` of §A10, and the
      same bytes are carried identically in **composite v1.6 §P1-14.8 and
      §P1-14.4**. **v1's `H-4`, which deferred the full list to a closure, is
      WITHDRAWN.** No closure adds, removes or reorders a step.
```

### §A0.3 What v1.3 adds, and why

```text
v1.2 WAS CONFIRMED BY THE INDEPENDENT X LINE. Opus 4.8, in a fresh session,
returned OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION
on all ten bounded items and found no blocking condition. THAT CONFIRMATION IS
PRESERVED HERE IN FULL: the literal enumeration, the cardinalities, the
disjointness proof, the digests, the two-stage Ed25519 format, the option
symmetry and non-selection, and the behavioural surface are carried forward
unchanged except where the Y line required a correction.

THE Y LINE RETURNED REVISE ON THREE THINGS. v1.3 repairs exactly those and
nothing else.

  Y25-1  GENERATED-SCHEMA COMPLETENESS. MS-4 did not define the JSON type,
         entry shape or ordering of reachable_closure, and composite §P1-3.3 is
         a prose table, not a canonical value. MS-4, MS-7 and IR-3 gave no
         value grammar for created_utc and did not state the mandatory value of
         the schema key. TS-1 described the three pre-selection paths in words
         without stating them as literal strings. TS-2 and TS-5 checked the key
         set and selected bindings but never expressly checked schema, version,
         author, signature_algorithm, the embedded pre-selection paths,
         threat_model or created_utc, leaving it ambiguous whether those
         normative values are validated at all. Two independent implementations
         could not derive the same bytes or the same validity predicate.
         → MS-4 now gives every top-level value type, one canonical JSON shape
           for reachable_closure with an exact element key set, element types,
           sort key, uniqueness rule and closure rule, and three literal
           pre-selection path fields. MS-7 and IR-3 give exact mandatory schema
           values, versions, nested shapes, types and array orders. MS-10 gives
           one exact created_utc grammar and semantic validator used everywhere
           the field appears. TS-1 states the three pre-selection paths as
           literal repository-relative strings. TS-2 and TS-5 are rewritten as
           EXHAUSTIVE FIELD-BY-FIELD ALGORITHMS — A1..A17 and B1..B18 — in which
           every mandatory literal and every derived relation is checked and NO
           FIELD IS SATISFIED BY MERE PRESENCE.

  Y25-2  FALSE RETROSPECTIVE ORDER AND REPLAY CLAIMS. OR-1..OR-11 stated one
         mandatory construction procedure, but the artifacts and CK-1..CK-12
         authenticate only the final byte state. Given the exact valid final
         bytes, no check can tell an early record, a pre-test M7, a pre-manifest
         id computation or a late Stage A from the conforming history. The Y
         line also showed that a COMPLETE COHERENT ROLLBACK of a previously
         valid generation passes every check, so TR-2's claim to close "every
         post-hoc substitution" was false.
         → FS-1 states exactly what G-11 proves. FS-2 states what it cannot
           prove and withdraws every contrary sentence, including OR-11's early
           record claim and test 106(h)'s retrospective refusal claim. FS-3
           keeps OR-1..OR-11 a mandatory operator obligation. FS-4 fails closed
           with PROCEDURE_VIOLATION_OBSERVED on a contemporaneously observed
           violation. FS-5 places an unobserved violation inside the residual.
           TR-2 gains clause (b), complete coherent rollback, and replaces the
           "every post-hoc substitution" claim with the exact eleven
           proper-subset cases actually closed. Test 106 gains an explicit
           coherent-rollback fixture classified OUTSIDE THE GUARANTEE, which
           must PASS rather than be falsely refused.
         NO HARDWARE SECURITY MODULE, EXTERNAL SERVICE, TIMESTAMP ORACLE,
         NOTARY, TRANSPARENCY LOG OR NEW SCIENTIFIC GATE IS ADDED. The honest
         procedural route is taken instead, and FS-5 says so.

  Y25-3  FALSE UNIQUE-ATTESTER WORDING. IR-4 said every member is attested by
         exactly one other object and test row 115 said by the record "and by
         nothing else". Both were false: M4 carries the M1 digests and the
         Stage-A binding, and M7 carries the M5 and M6 digests.
         → IR-4 now states the ACTUAL DIRECTED INTEGRITY GRAPH edge by edge,
           says the redundant edges are intentional and are not
           self-attestation, and claims no uniqueness of attester and no
           uniqueness of external attester. Row 115 is rewritten to assert the
           redundant edges positively and to fail any fixture claiming
           uniqueness.

ALSO RECORDED, AND NOT AN AUTHORITY HERE: Kirill signed the P1 process-claim
identity selection, Option A, on 2026-08-04. XS-1 records its path and digest,
states that it does NOT accept P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1,
that it is a member of no class, that it is not scientific evidence, that it
makes nothing here operative, and exactly what the later combined binding must
do with it.

NOTHING ELSE CHANGED. Every rule of v1.2 not named above — QC, FD, AK, PUB, RF,
TO, F, KW, FB, NS, WA, TIMING, DA, the §A5 conjuncts, ROUTE-D and ROUTE-W, the
swap-only state machine and every negative destination — is carried forward here
verbatim in substance. NO WATCHDOG MECHANISM, EVIDENCE CLASS, TREATMENT,
SCIENTIFIC CELL OR AUTHOR OPTION IS ADDED, REMOVED OR MOVED. The two-stage
authentication remains PROCESS INTEGRITY ONLY.
```

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
      class, no new namespace and no new schema. The install record of §A10 is a
      generated control-plane artifact, is never scientific evidence, and is
      never an input to any acceptance predicate.
```

---

## §A2. Supersession of the historical texts, by meaning, without editing them

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

ITS TWO COMPANION LOCI, likewise provenance and likewise not edited:
  …V2_1_CORRECTION.md:88          the §V2.0 replacement-index row
  …V2_1_CORRECTION.md:1582-1586   the §W11 compatibility classification

ITS TEN CARRYING REFERENCES, likewise provenance and likewise not edited:
  …V2_1_1_CORRECTION.md:124, :125   …V2_1_2_CORRECTION.md:106
  …V2_1_3_CORRECTION.md:1382        …V2_1_4_CORRECTION.md:1114
  …V2_1_5_CORRECTION.md:663         …V2_1_6_CORRECTION.md:776
  …V2_1_7_CORRECTION.md:836         …V2_1_8_CORRECTION.md:1414
  …V2_1_9_CORRECTION.md:1194        …V2_1_10_CORRECTION.md:1457

SUPERSEDED — THE ACTOR. Every clause of the historical section that makes the
  watchdog the executor of the sequence, the prover of quiescence, or the
  recorder of the proved-freeze instant is superseded in whole by `WA-1`,
  `WA-2` and `WA-3`. No reading restores a watchdog executor, quiescence proof
  or evidence writer.

RETAINED — THE TIMING WEAKENING, restated at §A2.3 in this document's own bytes.

THE HISTORICAL SECTION IS NOT AUTHORITY FOR ANYTHING. Under `DA-1` it is not
opened for behaviour. §A2.3 is the live statement.
```

### §A2.3 The timing guarantee, stated honestly, with the actor corrected

```text
TIMING-1  NO PHYSICAL AT-OR-BEFORE GUARANTEE IS CLAIMED. No claim is made that
          an ordinary scheduled userspace process physically executes at or
          before a monotonic deadline under every host schedule, cgroup throttle
          or runnable-queue delay.

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

### §A3.0 Constants this section requires — RESTATEMENTS, NOT CHOICES

**Closes `X23-B1`.** v1 used these names without defining them; their values
lived only in immutable provenance, so §A3.3's loop bound and §A3.4's
strict-progress branch were not constructible from governing bytes.

```text
QC-1  T_WATCHDOG_QUIESCE_MAX_PASSES       = 8
QC-2  T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS = 100_000_000      # 100 ms
QC-3  T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS    = 1_000_000_000    # 1 s
QC-4  T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS is ALREADY GOVERNED: it is defined by
      composite v1.6 §P1-2 as 60_000_000_000 (60 s) and is NOT restated here.
      It is named here only as a reference. THIS IS THE ONLY ONE OF THE FOUR
      THAT WAS ALREADY IN GOVERNING BYTES.
QC-5  QC-1 THROUGH QC-3 ARE RESTATEMENTS, NOT CHOICES. Each reproduces exactly
      the value the historical chain carried. NO VALUE MOVES, no constant is
      introduced, and no author cell is opened by them. They appear here because
      §A3.3, §A3.4, §A7 and §A8.1 require them and no live document else defines
      them. A reviewer may confirm the values against provenance without
      granting provenance any authority: confirming a restatement is not opening
      a document for behaviour.
```

### §A3.1 The two entry routes, total and explicit

**These two routes are exhaustive. There is no third entry to §A3, and no other
process enters it on any path.**

```text
ROUTE-D  ORDINARY LEASE-DEADLINE ENTRY.
         TRIGGER    Under `T_RUNTIME.lock`, the SUPERVISOR's own clock shows
                    `now_ns ≥ deadline_ns` for a live lease row, and the
                    watchdog is NOT declared dead (§A8.1 `AK-5`).
         ACTOR      the supervisor role process
         PRECONDITION  the §A3.2 drain, mandatory on this route
         killer     `SUPERVISOR`
         EVIDENCE   one `t-freeze-observation.v1`, supervisor-written
         MEDIATION  every group stop through `SIGNAL_GROUP`
         NOTE       This is the ORDINARY route, taken while the watchdog is
                    alive and healthy. The watchdog contributes its
                    acknowledgement state to the §A3.2 drain and nothing else.

ROUTE-W  DEAD-WATCHDOG RECOVERY ENTRY.
         TRIGGER    Under `T_RUNTIME.lock`, `dead` holds per §A8.1 `AK-4`, and
                    one or more groups are live.
         ACTOR      the supervisor role process
         PRECONDITION  none beyond the declaration; the drain is vacuous
                    because there is no live acknowledger
         killer     `SUPERVISOR`
         EVIDENCE   one `t-freeze-observation.v1` per OVERDUE group,
                    supervisor-written. NON-OVERDUE groups take the §A7
                    swap-only carve-out and NO witness is written for them.
         MEDIATION  every group stop through `SIGNAL_GROUP`
         AFTER      refuse admissions, obtain a replacement watchdog, await its
                    acknowledgement, then settle every overdue lease. The
                    overdue / non-overdue split of §A7 is TOTAL.

BOTH ROUTES ARE THE SAME PROCEDURE WITH THE SAME ACTOR, THE SAME MEDIATION, THE
SAME EVIDENCE CLASS, THE SAME NAMESPACE, THE SAME WRITER AND THE SAME `killer`
VALUE. They differ only in trigger and in what follows. THIS IS NOT TWO WRITERS
AND NOT TWO EVIDENCE CLASSES.
```

### §A3.2 The drain, mandatory on `ROUTE-D`

```text
Before entering §A3.3 on `ROUTE-D`, the supervisor:
  1. drains the watchdog ack pipe nonblocking;
  2. re-reads its own durable `WATCHDOG/LEASES.json`;
  3. if a strictly greater `table_seq` is durable AND `ACKED` in the exact sense
     of §A8.1 `AK-6`, re-evaluates against the newest acked row and does not
     freeze against the superseded deadline;
  4. only if no newer acked table exists does it proceed to §A3.3.

A legitimately renewed lease therefore cannot be frozen against a superseded
deadline, and the freeze decision is always taken against the newest table the
SUPERVISOR can prove acked at that instant.
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
   `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS` (`QC-2`) up to
   `T_WATCHDOG_QUIESCE_MAX_PASSES` (`QC-1`) passes, issuing `SIGKILL` to the
   process group THROUGH `SIGNAL_GROUP` after the first failed pass;

4. on the pass that proves every reachable member absent, `T` or `Z`, apply the
   STRICT-PROGRESS rule of §A3.4;

5. if the passes are exhausted, or a reachable process is neither stopped, dead
   nor absent, set `freeze_ns = null`, `overrun_ns = null`,
   `quiescence = UNKNOWN`;

6. the SUPERVISOR writes `WATCHDOG/FREEZE/<witness_id>.json` (§A4), atomic
   no-replace, file `fsync`, parent-directory `fsync`, then emits the event on
   the pipe.

`quiescence = PROVED` is a PROCESS-TREE fact and explicitly NOT a backend fact.
Signed §4d step 3's backend synchronization remains the supervisor's separate
settlement obligation.

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
        take up to T_WATCHDOG_QUIESCE_MAX_PASSES (QC-1) further samples at
        T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS (QC-2), RE-PROVING quiescence each
        pass;
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
NOTHING. On update-pipe EOF — the single supervisor-death detector — it WRITES
NOTHING, FREEZES NOTHING, SIGNALS NOTHING, and exits, settling nothing. No
freeze occurs on the supervisor-death path, because the only freeze executor is
the now-dead supervisor; every affected group is settled by the next supervisor
takeover through the signed invalid route.

A lost observation is NEVER reconstructed. There is exactly one writer and it is
the supervisor, so the object is absent only when the supervisor did not write
it. On absence the supervisor takes the §A6 `ABSENT` fallback route.
```

### §A3.6 Forbidden dispositions and single-valued cause

**Closes `X23-B2`.** v1 stated the routing destination but never stated which
terminals are forbidden. That omission was materially unsafe: the **accepted,
live** harness contract at `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`
§V-7 assigns `T_PROCESS_RESOURCE_STOP` to an overrun-bearing P3→P4 transition,
so an implementer reading only governing bytes saw a permission and no
prohibition, and a valid terminal became reachable from a deadline freeze.

```text
FD-1  FORBIDDEN DISPOSITIONS ON A DEADLINE FREEZE — the freeze §A3 performs on
      either route, and the swap-only freeze of §A7. NONE of the following may
      be selected, on any path, from any freeze of this amendment:
        T_PROCESS_CLOSED           T_PROCESS_VOLUNTARY_STOP
        T_PROCESS_E1_EXHAUSTED     T_PROCESS_E3_DUE
        T_PROCESS_RESOURCE_STOP    — named explicitly, and this is the closure
                                     of X-C4.1. It is unreachable anyway,
                                     because the signed cooperative
                                     quiesce → charge → record order cannot be
                                     supplied by a non-heartbeating controller.
      NO VALID CLOSE, EXHAUSTION, PAUSE OR REVIEW TERMINAL MAY ARISE FROM AN
      OVERRUN.

FD-2  THE ORDINARY HARNESS TRANSITION IS UNTOUCHED. `FD-1` binds the DEADLINE
      FREEZE and the SWAP-ONLY FREEZE only. The accepted harness contract's
      ordinary P3→P4 resource stop — cooperative order, disposition
      `T_PROCESS_RESOURCE_STOP`, actual overrun recorded in full and never
      clipped — is fully retained and is NOT a freeze of this amendment. A
      build that removed it would be nonconforming.

FD-3  CAUSE IS SINGLE-VALUED. A positive confirmed overrun has public cause
      `PROCESS` and no other, on `ROUTE-D` and on `ROUTE-W` alike.

FD-4  ROUTING, restated in full so that no historical section is opened:
        quiescence = PROVED  ⇒ overrun_ns = freeze_ns − deadline_ns  (> 0)
                             ⇒ signed record-first live-process invalidity,
                               all-live batch, public cause PROCESS,
                               full §4c charging
        quiescence = UNKNOWN ⇒ the same invalid route with the §4c(c)/§4d
                               unknowable pool; NO timestamp is synthesized
      The zero-overrun branch is DELETED and no tolerance constant exists.
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
     versus `<witness_id>.json` as open is wrong.

F-2  `process_id` IS A MEMBER OF THE PREIMAGE AND A MANDATORY RECORD FIELD. It
     is NOT the filename and it is NOT a PID. It remains a CONSTRUCTIBLE OPAQUE
     CLAIM IDENTIFIER. The process-claim identity cell is neither selected nor
     repaired by this amendment.

F-3  PRODUCTION ORDER. The SUPERVISOR — the sole writer — re-reads the
     supervisor identity record and REFUSES TO WRITE on generation mismatch;
     then writes the file (same-directory temp → file `fsync` → atomic
     no-replace → parent `fsync`); THEN emits the pipe event. A no-replace
     `EEXIST` means an identical `(generation, process_id, table_seq)` witness
     already exists: the writer emits the event and writes nothing further.

F-4  CONSUMPTION ORDER within this class: witnesses are consumed sorted by
     `(generation == current) desc, table_seq asc, process_id asc`; the earliest
     `table_seq` for a process in the current generation is authoritative; later
     same-process witnesses are retained as duplicates, not consumed twice. The
     TOTAL order ACROSS classes is at §A6 `TO-3`.

F-5  REPLAY NAMING. The generation is INSIDE the name, so a stale
     cross-generation collision on a no-replace path is impossible. A
     prior-generation witness fails §A5 conjunct 3 and takes the `UNKNOWN` route.

F-6  REMOVAL. By the supervisor, after the settlement's archival commit. Never
     by any other actor and never to make room.

F-7  NOTHING ABOUT THE WRITER MOVES `F-1`..`F-6`. Object identity, replay key
     and evidence filename are functions of `(generation, process_id,
     table_seq)` alone.

F-8  THE `WATCHDOG/` NAMESPACE IS RETAINED AND IS NOT RENAMED. `WATCHDOG/**`
     remains control plane and archival-excluded. THE NAME IS HISTORICAL AND
     CARRIES NO AUTHORITY: no rule reads the namespace string to decide who may
     write. A reader must not infer a watchdog writer from the namespace name.
```

---

## §A5. The acceptance predicate — the indisputably governing bytes

Under `T_RUNTIME.lock`, an observation becomes evidence **only if every conjunct
holds**:

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
    `killer ∈ {WATCHDOG, SUPERVISOR}` is RETAINED UNCHANGED and the `WATCHDOG`
    value is unreachable BY CONSTRUCTION rather than by deletion, so that a
    legacy, stale or forged object is REJECTED rather than unparseable;

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

KW-2  A FIXTURE THAT NARROWS THE ENUM FAILS. The enum retains both values.

KW-3  ANY malformed, missing, conflicting or unverifiable fact — a planted or
      stale file, an A3-procedural forgery, a generation or `table_seq`
      mismatch, an inconsistent member count, a `freeze_ns ≤ deadline_ns` —
      makes the object NOT EVIDENCE. It never becomes valid evidence, never
      yields a valid terminal, and never contributes an accepted timestamp. The
      rejected object is NEVER overwritten, truncated, renamed or deleted to
      make room.
```

---

## §A6. The fallback, and the total order across all three object classes

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
FB-1 SEPARATE OBJECT. The fallback is NOT of the §A4 class, is NOT written by
     §A4's writer acting in §A4's capacity, and is NOT installed in §A4's
     namespace. Its id is domain-tagged and cannot collide with `witness_id`.

FB-2 SEPARATE ROUTING, SAME DESTINATION FAMILY. A fallback drives exactly the
     signed route for `UNKNOWN`: record-first live-process invalidity, the
     all-live batch with the unknowable pool, public cause `PROCESS`, and full
     §4c charging. `FD-1` binds it: no fallback can select a valid terminal, a
     zero-overrun branch, a synthesized freeze instant or an `overrun_ns`.

FB-3 SEPARATE COUNT KEY. `current_unresolved_member_count` is the fallback's own
     key and is never the §A4 object's `unresolved_member_count`. The two are
     never equated, never renamed into one another, and never substituted.

FB-4 NULLABLE ABSENT VALUES. On the `ABSENT` sentinel,
     `rejected_witness_path_or_null` and `rejected_object_sha256_or_null` are
     null and `rejection_conjunct = 0`. `process_id` is MANDATORY AND NON-NULL
     ON EVERY FALLBACK BRANCH, including this one.

FB-5 THE WATCHDOG HAS NO PATH HERE, before or after this amendment.
```

### §A6.1 The total production / duplicate / conflict / consumption order

**Closes `X23-M2`.** v1 ordered witnesses only; the interaction of the three
object classes was defined nowhere in governing bytes.

```text
TO-1  PRODUCTION. Validate the witness per §A5. On the FIRST failing conjunct in
      ASCENDING order, compute `fallback_witness_id`, install the fallback
      no-replace, then consume it. THE REJECTED OBJECT IS LEFT BYTE-INTACT.

TO-2  DUPLICATE. `EEXIST` at the fallback path means an identical rejection for
      the identical rejected bytes is already durable ⇒ consume the existing
      object and write nothing.

TO-3  CONFLICT. Two fallbacks for the same
      `(generation, process_id, table_seq)` with DIFFERENT
      `rejected_object_sha256_or_null` values imply the immutable witness bytes
      changed between reads — reachable only through the A3 same-UID procedural
      residual ⇒ record-first invalidity naming BOTH fallbacks and the witness
      path. Fail-closed; no valid terminal.

TO-4  CONSUMPTION, ONE TOTAL ORDER ACROSS ALL THREE CLASSES — freeze witnesses,
      freeze fallbacks and replacement-freeze records:
        (generation == current) desc,
        table_seq asc,
        process_id asc,
        object class: FREEZE_FALLBACK before FREEZE,
        fallback_witness_id / witness_id asc

TO-5  FALLBACK PRIORITY. For a given `(generation, process_id)`: IF ANY FALLBACK
      EXISTS, THE FALLBACK IS AUTHORITATIVE and every witness for that pair is
      permanently non-evidence. Otherwise the earliest `table_seq` witness is
      authoritative. Later same-pair objects are retained as duplicates and are
      never consumed twice.
```

---

## §A7. The swap-only carve-out — fully constructible

**Closes `X23-M1`.** v1 named the objects but supplied no preimage, no key sets,
no companions and no resume predicate, so the carve-out could not be built.
**No historical lookup is required by anything below.**

### §A7.1 The overdue / non-overdue split, total

```text
On watchdog death (`ROUTE-W`), the supervisor classifies EACH live group under
`T_RUNTIME.lock`, against that group's CURRENT DURABLE LEASE row, at the instant
it freezes it:

  overdue     (now_ns ≥ deadline_ns)  ⇒ DEADLINE FREEZE: the §A3.3 sequence with
                killer = SUPERVISOR, a FREEZE/<witness_id>.json witness (or an
                §A6 fallback when that evidence is rejected), and the §A3.6
                invalid route.

  non-overdue (now_ns <  deadline_ns) ⇒ SWAP-ONLY FREEZE: SIGSTOP to the group
                through SIGNAL_GROUP; prove quiescence by the §A3.3 step-3
                enumeration; install ONLY the §A7.2 REPLACEMENT_FREEZE record.
                NO §A4 witness is written. NO freeze_ns is sampled as evidence.
                NO overrun_ns exists. NO fallback is written.

THE SPLIT IS TOTAL AND MUTUALLY EXCLUSIVE: every live group falls in exactly one
branch.
```

### §A7.2 The three immutable records — one object per transition

```text
WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json
  replacement_freeze_id = SHA-256(canonical {
    "schema": "philosophia.officina.t-replacement-freeze-id.v1",   # domain tag
    "supervisor_generation_sha256": …, "process_id": …, "table_seq": … })
  schema philosophia.officina.t-replacement-freeze.v1, atomic no-replace,
  supervisor under T_RUNTIME.lock, KEYS EXACTLY:
    schema, scientific_outcome, supervisor_generation_sha256,
    replacement_freeze_id, process_id, pgid, start_identity, table_seq,
    deadline_ns, swap_only (true), overdue (false),
    supervisor_stop_monotonic_ns, created_utc

WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.resumed.json
  schema philosophia.officina.t-replacement-resume.v1, atomic no-replace,
  KEYS EXACTLY: schema, scientific_outcome, replacement_freeze_id,
    acked_table_seq, resume_monotonic_ns, resumed_utc

WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.invalidated.json
  schema philosophia.officina.t-replacement-invalidation.v1, atomic no-replace,
  KEYS EXACTLY: schema, scientific_outcome, replacement_freeze_id,
    invalid_condition ∈ {I1,I2,I3,I4,I5,I6,I7},
    observed_monotonic_ns, invalidated_utc

NO RECORD IS EVER MUTATED. The state machine is a set of immutable no-replace
installs, so every transition is crash-completable.
```

### §A7.3 Three mutually exclusive states, with precedence

```text
Evaluated under `T_RUNTIME.lock` at every serve step, in THIS ORDER — INVALID
conditions FIRST, then RESUMABLE, else ACK_PENDING.

INVALID  if ANY of:
  I1. now_ns ≥ deadline_ns of the group's current durable lease row
      (the deadline passed while the group was frozen)
  I2. the replacement watchdog failed definitively: a fork error, or no ack of
      any table_seq within T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS of the replacement
      table's updated_monotonic_ns
  I3. definitive identity/member mismatch: any recorded member's pid +
      start identity differs, or any member is absent, Z, or in an
      unclassifiable state
  I4. an §A4 deadline-freeze witness or an §A6 fallback exists for that process
      in the current generation
  I5. an unresolved invalidity blocks: G5 not clear, or the record-first
      ordering not satisfied
  I6. the recorded lease is no longer the current durable lease
  I7. the REPLACEMENT_FREEZE record's supervisor_generation_sha256 differs from
      the current generation
  ⇒ install <replacement_freeze_id>.invalidated.json naming the EXACT triggering
    condition, then take the signed all-live invalid route, public cause
    PROCESS, with the §4c(c)/§4d unknowable pool when any member state is
    unknowable. FD-1 binds this route.

RESUMABLE if NOT INVALID and BOTH:
  S1. the replacement watchdog is live by its fork-child record AND has durably
      acked the EXACT current table_seq whose table contains this group's row
  S2. every recorded member's pid + start identity matches and every member is
      in state T  (relaxed to "T or running" once .resumed.json is durable)
  ⇒ install <replacement_freeze_id>.resumed.json (no-replace) BEFORE issuing
    SIGCONT to the group through SIGNAL_GROUP; the SIGCONT is idempotent and
    re-issuable.

ACK_PENDING otherwise — not INVALID, and S1 not yet satisfied:
  the group REMAINS FROZEN. This is NOT invalidity, NOT a terminal, and NOT
  evidence of anything. ACK_PENDING NEEDS NO MARKER RECORD: it is exactly the
  state in which the REPLACEMENT_FREEZE record exists and neither transition
  marker does. Re-evaluate at each T_SUPERVISOR_POLL_INTERVAL_NS serve step.
  The state is BOUNDED: it must resolve to RESUMABLE or INVALID by
    min( deadline_ns ,
         replacement_table.updated_monotonic_ns
           + T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS )
  whichever is earlier, because I1 or I2 fires at that bound.
```

```text
RF-1  NO HEALTHY NON-OVERDUE GROUP IS MECHANICALLY FORCED INTO INVALIDITY. For a
      healthy group I1..I7 are all false, so the group is ACK_PENDING and then
      RESUMABLE. The only invalidity reachable from a swap is an honest
      infrastructure race — a lease whose remaining time is shorter than the
      replacement path — which is I1, a real overdue deadline, not a relabelled
      healthy heartbeat. NO NEW CONSTANT IS INTRODUCED; the bound is the
      arithmetic of two existing ones.

RF-2  `supervisor_stop_monotonic_ns` IS NEVER EVIDENCE. It is never used to
      compute `overrun_ns`, never consumed as an §A4/§A5 witness, and never
      citable. `REPLACEMENT_FREEZE/**` is unreachable by the watchdog on every
      path.

RF-3  ORDERING. Replacement-freeze records participate in the §A6.1 `TO-4` total
      order as their own object class, after FREEZE_FALLBACK and FREEZE for the
      same `(generation, process_id, table_seq)`.
```

---

## §A8. Negative surface, publication, acknowledgement and liveness

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
      a witness in any sense.

NS-4  Liveness is judged on the watchdog's OWN sample, per `AK-4`.
```

### §A8.1 Publication, acknowledgement and liveness — restated in full

**Closes `X23-B3`.** v1's route triggers turned on "acked" and
`updated_monotonic_ns`, neither of which was defined in any file an implementer
is permitted to open. **Both route triggers were unevaluable.**

```text
AK-1  THE LEASE TABLE AND ITS PUBLICATION. `WATCHDOG/LEASES.json` is written
      ATOMIC-REPLACE with `table_seq` STRICTLY INCREASING, and the identical
      payload is published on the update pipe, BEFORE the first `SIGCONT`,
      BEFORE any capability becomes usable, and BEFORE any operation admission.
      The supervisor must observe the watchdog's ack of that exact `table_seq`
      first; otherwise it refuses `START` and `OPERATION_ADMIT` with
      `REFUSED`/`WATCHDOG_UNACKED`.

AK-2  ON RENEWAL the old deadline remains authoritative until the successor
      table is acked. NO UNACKNOWLEDGED UPDATE EVER EXTENDS BEHAVIOUR.

AK-3  ACK FRAME KEYS EXACTLY:
        schema ("philosophia.officina.t-watchdog-ack.v1"), scientific_outcome,
        supervisor_generation_sha256, table_seq, ack_monotonic_ns

AK-4  LIVENESS IS JUDGED ON THE WATCHDOG'S OWN SAMPLE, never on the supervisor's
      read time:
        healthy(table_seq) ⇔ ack_monotonic_ns − updated_monotonic_ns
                             ≤ T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS   (QC-3)
        dead               ⇔ the supervisor has drained the ack pipe and
                             now_ns − updated_monotonic_ns
                             > T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS  (QC-4)
                             with no ack for that table_seq
      A supervisor busy inside a bounded chunk therefore cannot declare a
      healthy watchdog dead.

AK-5  `updated_monotonic_ns` is the SUPERVISOR's monotonic sample at the instant
      it published that `table_seq`. `ack_monotonic_ns` is the WATCHDOG's own
      monotonic sample at the instant it acknowledged that `table_seq`. Neither
      is ever the other's clock and neither is ever a settlement timestamp.

AK-6  `ACKED`, as used by `ROUTE-D`'s precondition (§A3.2 step 3) and by `S1`
      (§A7.3), means EXACTLY: an ack frame for that `table_seq` has been drained
      from the ack pipe AND `healthy(table_seq)` holds.

AK-7  BECAUSE `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` (60 s) EXCEEDS
      `T_CLIENT_REPLY_TIMEOUT_SECONDS` (30 s), a client whose heartbeat waits on
      a dying watchdog times out, exits 3, and re-addresses the same occurrence
      later to collect its cached terminal.
```

### §A8.2 The lease-table publication rule, stated standalone

**Closes `X23-M3`. Deliberately redundant with `AK-1`.** It is restated alone so
that no reader can treat the publication ordering as an incidental clause of the
liveness rule.

```text
PUB-1  `WATCHDOG/LEASES.json` is atomic-replace. `table_seq` is STRICTLY
       INCREASING and never reused within a generation.
PUB-2  The identical payload is published on the update pipe.
PUB-3  BOTH happen BEFORE the first `SIGCONT` of the affected group, BEFORE any
       capability becomes usable, and BEFORE any operation admission.
PUB-4  ADMISSION IS REFUSED UNTIL THE ACK OF THAT EXACT `table_seq` IS OBSERVED.
       `START` and `OPERATION_ADMIT` refuse with `REFUSED`/`WATCHDOG_UNACKED`.
       NOTHING IN GOVERNING BYTES PERMITS ADMITTING AN OPERATION AGAINST AN
       UNACKNOWLEDGED LEASE TABLE.
```

---

## §A9. The complete atomic handoff — stated here, not in any closure

**Closes `Y23-3`, `DA-5` and the X-line finding `FX24-1`. This handoff is
COMPLETE and is stated IDENTICALLY in composite v1.6 §P1-14.8; its ordered steps
are `OR-1` through `OR-11` of §A10 below, which composite v1.6 carries
byte-identically at §P1-14.4. Neither copy defers to a closure, and no closure
adds a step.**

**The cross-reference audit, re-run on the v2.6 pair and stated so that a
reviewer can re-run it mechanically:**

- composite v1.6's highest numbered section is §P1-18, and composite v1.6
  contains the string `P1-19` **zero** times. The v1.1 amendment's locator
  "composite v1.4 §P1-19" named a section that never existed; it was corrected
  in v1.2 and the string survives in this amendment only inside this audit note,
  where it identifies the withdrawn locator, and as a locator nowhere;
- every `§P1-…` reference in this amendment names a section that exists as a
  heading in composite v1.6: §P1-2, §P1-3.1, §P1-3.3, §P1-12.4, §P1-13.2,
  §P1-14.4, §P1-14.8 and §P1-18;
- every `§A…` reference in composite v1.6 names a section that exists as a
  heading in this amendment: §A2, §A9 and §A10;
- no reference in either file names a section the other does not have, and no
  reference in either file names a version of the other that is not the version
  it is jointly accepted with.

```text
H-1  ONE UNIT. The v1.3 amendment and composite v1.6 are ONE indivisible
     acceptance unit. Neither is operative alone. Accepting one without the
     other is NOT a conforming state and NOT a partial success. THE v1.2
     AMENDMENT AND COMPOSITE v1.5 ARE WHOLLY REPLACED, not amended, and every
     earlier amendment and composite remains wholly replaced.

H-2  THE ORDERED STEPS ARE `OR-1` THROUGH `OR-11` OF §A10, STATED THERE IN FULL,
     AND THEY ARE NOT RESTATED IN A SECOND FORM ANYWHERE. There is exactly ONE
     statement of the ordering in these governing bytes, carried
     byte-identically in this file and in composite v1.6 §P1-14.4, so no two
     statements of it can disagree.
     THE ORDER IS A MANDATORY OPERATOR OBLIGATION, NOT A VERIFIED PROPERTY.
     `OR-1` and `FS-3` state the obligation; `FS-2` states that the final-state
     gate cannot distinguish identical final bytes produced in a forbidden
     order and withdraws every version-1.2 sentence that claimed otherwise;
     `FS-4` fails closed when a violation is observed while it occurs; `FS-5`
     places an unobserved violation inside the residual of `TR-2`.
     ALL STEPS LAND TOGETHER OR NONE DOES.

H-3  NO PARTIAL LANDING IS CONFORMING OR OPERATIVE. §A10's pre-production check
     is the enforcement point, it is `CK-1`..`CK-12`, and it runs before any
     production entry point. Composite v1.6 guard `G-11` is the same check
     stated on the P1 side; THE TWO ARE ONE RULE WITH TWO STATEMENTS and the
     normative block is byte-identical in both files.
     A partial landing that is STILL PARTIAL when the gate runs is refused by a
     named check. A violation of ORDER that nevertheless leaves the exact valid
     final bytes is a governance violation the gate cannot see, and `FS-2` says
     so rather than pretending otherwise.

H-4  EXISTING HISTORY REMAINS BYTE-IDENTICAL. Zero historical bytes are edited
     by any step of `OR-1`..`OR-11`. `OR-11` and `CK-12` verify this and refuse
     on any difference with HISTORICAL_BYTE_MOVED.
```

---

## §A10. The install record and the two-stage author authorization

**Closes `Y23-5.3`, the v2.4 Y findings `Y24-1`..`Y24-3`, and the v2.5 Y
findings `Y25-1` (generated-schema completeness), `Y25-2` (false retrospective
order and replay claims) and `Y25-3` (false unique-attester wording).**

**THE NORMATIVE BLOCK BELOW IS CARRIED BYTE-IDENTICALLY AT §P1-14.4 `G-11` OF
COMPOSITE v1.6.** The install gate is ONE RULE WITH TWO STATEMENTS: this section
is the peer-layer statement and `G-11` is the P1 statement. A reviewer may
extract the two delimited spans and compare them directly; any difference
between them is a defect in this indivisible pair.

The block defines, in order: the canonical encoding (`MS-0`); the seven literal
member classes with exact cardinalities, paths, schemas, key sets, value
grammars and digest rules (`MS-1`..`MS-7`); the total member cardinality
(`MS-8`); the pairwise-disjointness proof (`MS-9`); the one `created_utc`
grammar and validator (`MS-10`); the install record's identity, path, schema and
the complete directed integrity graph (`IR-1`..`IR-12`); the two-stage author
authorization with exhaustive field-by-field verification algorithms
(`TS-1`..`TS-6`); the mandatory construction order, which is an operator
obligation (`OR-1`..`OR-11`); the final-state pre-production check
(`CK-1`..`CK-12`); the closed failure-code set (`FC-1`); the exact boundary
between what the final-state gate proves and what it cannot prove about history
(`FS-1`..`FS-5`); the trust proof and the two-clause named residual (`TR-1`,
`TR-2`); and the external author state that is deliberately not a member
(`XS-1`).

**Read `FS-1`, `FS-2` and `TR-2` before any summary of this section.** They fix
the outer boundary of every claim in this pair, and no sentence anywhere —
here, in the composite, in any packet or in any closure — may exceed them.

```text
--- BEGIN JOINT INSTALL AND AUTHORIZATION BLOCK - BYTE-IDENTICAL IN BOTH GOVERNING FILES ---

MS-0  CANONICAL ENCODING, ONE DEFINITION, USED BY EVERY ARTIFACT BELOW.
      CANON(v) := the bytes obtained by serializing the JSON value v with
        object keys sorted ascending by Unicode code point;
        no whitespace anywhere outside string literals;
        the one-character separators "," between items and ":" between a key
        and its value;
        every character outside printable ASCII escaped as \uXXXX, so the
        output is pure ASCII;
        no NaN, no Infinity and no floating-point number of any kind;
        every integer written in decimal with no exponent and no decimal
        point;
      followed by exactly one 0x0A byte and nothing after it.
      ARRAY ORDER IS PART OF THE VALUE AND IS NEVER SORTED BY CANON. Wherever
      an array appears below, its required order is stated with it; a
      differently ordered array is a DIFFERENT value with a different digest.
      THIS INTRODUCES NO NEW ENCODING. It reproduces exactly the canonical
      form Officina already uses for every hashed artifact.
      A file whose bytes are required to be canonical is REJECTED unless its
      bytes are byte-identical to CANON of the value they parse to. Parsing a
      file and re-serializing it is not a repair: the bytes on disk are the
      artifact.
      Every SHA-256 value in every artifact below is written as exactly 64
      characters, each one of 0123456789abcdef. Every path is
      repository-relative, uses the 0x2F separator, and is compared byte for
      byte. Every boolean is the JSON literal true or false. Every integer is
      a JSON number with no fractional part and no exponent.

MS-1  M1 GOVERNING SPECIFICATION. CARDINALITY EXACTLY 2. The two literal
      paths, and no others:
        successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
        successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
      Both are taken in their POST-SELECTION bytes: the composite after every
      variant block has been resolved to the signed branch and the other
      branch deleted (OR-4), the amendment as installed. The digest of each is
      the SHA-256 of the whole file's bytes as found on disk, with no
      normalization and no exclusion of any region.
      NO OTHER PATH IS IN M1, AND NEITHER OF THESE TWO PATHS IS IN ANY OTHER
      CLASS.

MS-2  M2 IMMUTABLE PROVENANCE SET. CARDINALITY EXACTLY 43. THE LIST BELOW IS
      LITERAL, EXHAUSTIVE, AND IS THE ONLY SOURCE OF M2. The provenance region
      of the composite is NOT read to construct M2, no directory is scanned,
      no adjective is interpreted, and no path is taken from the install
      record, from the manifest or from any future-edit table. An omission and
      an extra member are equally fatal. Each row is a recorded SHA-256
      followed by two spaces followed by the literal path; the recorded digest
      is the value that member MUST still have on disk.
        746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
        bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
        9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
        ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
        2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
        72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
        cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
        7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
        e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
        789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
        33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
        1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
        2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
        2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
        c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
        02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
        6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
        798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
        8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
        66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
        d2975d19c553d9f9338bacff9d0a2af1855af45881e305a8706c110820896935  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md
        90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md
        2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
        b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md
        380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md
        40a26dc1a7d2e6a8b9c122b7e09599a7b03470b0e98c86964bc4389ea4b0e5b3  reviews/opus5_officina_supervisor_p1_operative_composite_v1_1_closure.md
        6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
        c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
        4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
        4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
        3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
        ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
        70df01e8af25303600425434353a707571354e385fff78e1663f30494cf4b7ac  reviews/opus_officina_supervisor_p1_final_xy_review.md
        75002efea91c3960adb5bc2bfa4dcdacecdb45a1add14f3f2fc1dd300e591b1b  reviews/sol_officina_supervisor_p1_final_xy_review.md
        daeef9b3a349aba48b126957ff027d946b7ad094e5c03c3c2ede717f27a660e6  successor/officina/T_ENVELOPE.json
        ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
        c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md
        bd8147a5085096c6a08ec0fec40ad22df23d55f23f77e3349218b3da93b6b2ba  reviews/fable_officina_p1_watchdog_v2_4_independent_x_confirmation.md
        3fab1b09e2724534b2b5a080fbfeb98cc861cbe3b9764790084dfec050944a05  reviews/sol_officina_p1_watchdog_v2_4_final_y_confirmation.md
        058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
        8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md
        c2e9ddb2e6270f2b870986b01d1114ea68d5f3e1db466f165ee2f47a0f256427  reviews/fable_officina_p1_watchdog_v2_5_independent_x_confirmation.md
        80d42229b2e9b32e51a5448c10af410640e2088f777334fa4431f29e4e840c81  reviews/sol_officina_p1_watchdog_v2_5_final_y_confirmation.md
      M2 CONTAINS NONE OF THE SEVEN M3 PATHS AND DOES NOT CONTAIN
      src/philosophia/officina/verification.py. M2 IS A LITERAL LIST, NOT THE
      PROVENANCE REGION MINUS AN EXCEPTION, so no later provenance row can
      silently enter it.

MS-3  M3 ACCEPTED PEER CHAIN. CARDINALITY EXACTLY 7. The five generic-harness
      contract files, the generic-harness signature and the effective
      batch-settlement amendment, as literal paths with recorded digests:
        64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
        6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
        624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
        b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
        724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
        8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
        b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
      THE EFFECTIVE BATCH-SETTLEMENT AMENDMENT IS v1.1.1 AND ONLY v1.1.1. The
      v1 and v1.1 batch-settlement documents are provenance and are in M2, not
      in M3.

MS-4  M4 PRODUCTION MANIFEST. CARDINALITY EXACTLY 1. Literal path:
        successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the
      twenty keys below — no extra key, no missing key — with exactly these
      types and value grammars:

        schema              STRING, exactly
                            "philosophia.officina.t-production-call-graph.v1"
        version             INTEGER, exactly 1
        roots               ARRAY of exactly 5 STRINGS, each a literal
                            production-root path of §P1-3.1 of the composite,
                            IN THAT SECTION'S ORDER, pairwise distinct. The
                            array is NOT sorted; its order is §P1-3.1's order.
        root_source_sha256  OBJECT whose key set is EXACTLY the five strings
                            of "roots" and whose every value is a 64-character
                            lowercase hexadecimal STRING
        reachable_closure   ARRAY, see the canonical shape below
        p1_composite_sha256            64-char lowercase hex STRING
        p1_composite_body_sha256       64-char lowercase hex STRING
        p1_composite_guarddata_sha256  64-char lowercase hex STRING
        p1_composite_normative_sha256  64-char lowercase hex STRING
        peer_amendment_sha256          64-char lowercase hex STRING
        pre_selection_packet_path      STRING, exactly TS-1's packet path
        pre_selection_packet_sha256    64-char lowercase hex STRING
        pre_selection_amendment_path   STRING, exactly TS-1's amendment path
        pre_selection_amendment_sha256 64-char lowercase hex STRING
        pre_selection_composite_path   STRING, exactly TS-1's composite path
        pre_selection_composite_sha256 64-char lowercase hex STRING
        stage_a_path        STRING, exactly TS-1's Stage-A path
        stage_a_sha256      64-char lowercase hex STRING
        stage_a_key_id      64-char lowercase hex STRING
        created_utc         STRING satisfying MS-10

      reachable_closure — ONE CANONICAL JSON SHAPE, REPLACING THE PROSE TABLE.
      Composite §P1-3.3 is a human-readable audit table and is NOT a canonical
      value; this is. reachable_closure is an ARRAY of OBJECTS. It is
      non-empty. Every element has EXACTLY these six keys:
        module              STRING, a Python module name as it appears in an
                            import, of one or more characters from
                            0-9 A-Z a-z _ . and beginning with a letter or _
        kind                STRING, exactly one of the four literals
                            "BUILTIN", "FROZEN", "EXTENSION", "PURE_PYTHON"
        transitive_imports  ARRAY of STRINGS, each a module name of the same
                            grammar, SORTED ASCENDING by Unicode code point,
                            PAIRWISE DISTINCT, possibly empty
        starts_task         BOOLEAN
        registers_at_fork   BOOLEAN
        installs_handler    BOOLEAN
      ARRAY ORDER: the elements are SORTED ASCENDING by the "module" value
      compared byte for byte. UNIQUENESS: the "module" values are pairwise
      distinct across the array. CLOSURE: every string occurring in any
      element's transitive_imports also occurs as the "module" value of some
      element of the same array — the closure is closed under itself.
      Two independent implementations given the same audited closure therefore
      emit the same bytes, because the element key set, the element order, the
      inner array order and the canonical encoding are all fixed.

      THE MANIFEST CARRIES NO DIGEST OF ITSELF. The four p1_composite_* fields
      carry exactly the meanings CHANGE 5 already assigns them and nothing
      about them moves; the three pre_selection_* path/digest pairs and the
      three stage_a_* fields are the bindings TS-2 checks.

MS-5  M5 POST-HANDOFF VERIFIER. CARDINALITY EXACTLY 1. Literal path:
        src/philosophia/officina/verification.py
      DIGEST RULE: the SHA-256 of the entire file's bytes exactly as found on
      disk — no normalization, no line-ending translation, no whitespace
      stripping, no comment stripping, no compilation, and no exclusion of any
      region. The digest is of bytes, never of an abstract syntax tree.
      The bytes at this path BEFORE the handoff are the non-enforced
      pre-install baseline named in the provenance region; they are NOT M5.
      M5 is the bytes at this path after OR-5. The baseline digest appears in
      MS-2 nowhere and is compared by nothing.

MS-6  M6 TEST BUNDLE. CARDINALITY EXACTLY 2, IN THIS FIXED ORDER, which is not
      sorted and is not re-derived:
        1. tests/test_officina_p1_freeze_authority.py     carries rows 92..103
        2. tests/test_officina_p1_install_integrity.py    carries rows 104..115
      MEMBERSHIP RULE FOR ROWS 92..115, EXACT AND MECHANICAL:
        for every integer r with 92 <= r <= 115 there is EXACTLY ONE
        module-scope function, in EXACTLY ONE of the two modules, whose name
        begins with "test_p1_row_" followed by r written as three decimal
        digits with a leading zero where needed, followed by "_";
        rows 92 through 103 occur only in module 1;
        rows 104 through 115 occur only in module 2;
        no function name of that form exists for any integer outside 92..115;
        no row number occurs twice within a module or across the two;
        the count of such functions is therefore exactly 24, twelve per module.
      Each module is its own member with its own SHA-256 over its whole bytes,
      so M6 contributes exactly two entries to the member list.
      CANONICAL BUNDLE DIGEST — used only by M7 and never as a member digest:
        test_bundle_digest = SHA-256( CANON( {
          "schema": "philosophia.officina.t-p1-test-bundle-digest.v1",
          "modules": [ {"path": <module 1 path>, "sha256": <module 1 digest>},
                       {"path": <module 2 path>, "sha256": <module 2 digest>} ]
        } ) )
      "modules" is an ARRAY of exactly two OBJECTS, each with EXACTLY the two
      keys path and sha256, both STRINGS, in the order above. Swapping them
      produces a different digest and is a refusal, not a normalization.

MS-7  M7 PASSING ATTESTATION. CARDINALITY EXACTLY 1. Literal path:
        successor/officina/runtime_control/INSTALL/T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the ten
      keys below, with exactly these types and value grammars:

        schema               STRING, exactly
                             "philosophia.officina.t-watchdog-authority-test-attestation.v1"
        version              INTEGER, exactly 1
        verifier_path        STRING, exactly MS-5's literal path
        verifier_sha256      64-char lowercase hex STRING, the digest of the
                             M5 bytes FOUND ON DISK
        test_bundle_modules  ARRAY of exactly 2 OBJECTS, each with EXACTLY the
                             two keys path and sha256, both STRINGS, the
                             sha256 being 64 lowercase hex characters. The
                             array order is MS-6's fixed order: element 0 is
                             module 1, element 1 is module 2. It is NOT sorted.
                             Each path equals MS-6's corresponding literal
                             path; each sha256 is the digest of that module's
                             bytes FOUND ON DISK.
        test_bundle_digest   64-char lowercase hex STRING, equal to MS-6's
                             canonical bundle digest recomputed from the two
                             entries of test_bundle_modules
        rows_attested        ARRAY of exactly 24 INTEGERS, strictly ascending,
                             first element 92, last element 115, each element
                             one greater than its predecessor — that is,
                             exactly 92,93,94,...,115
        row_count            INTEGER, exactly 24, and equal to the length of
                             rows_attested
        all_rows_passed      BOOLEAN, exactly true. The value false is not
                             installable and no other value validates.
        created_utc          STRING satisfying MS-10

      THE ATTESTATION CARRIES NO DIGEST OF ITSELF AND NAMES NO INSTALL RECORD.
      It therefore cannot attest the set that contains it.

MS-8  TOTAL MEMBER CARDINALITY, EXACT:
        M1 2 + M2 43 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 57
      The install record's member list has exactly 57 entries. A list of any
      other length fails before a single digest is compared.

MS-9  PAIRWISE DISJOINTNESS, PROVED BY PATH RATHER THAN ASSERTED.
      Every member is identified by one repository-relative path. Two classes
      are disjoint if and only if their path sets share no element. Write
      P(Mi) for the path set of class Mi:
        P(M1) the two literal strings of MS-1
        P(M2) the 43 literal strings of MS-2
        P(M3) the 7 literal strings of MS-3
        P(M4) { successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json }
        P(M5) { src/philosophia/officina/verification.py }
        P(M6) { tests/test_officina_p1_freeze_authority.py ,
                tests/test_officina_p1_install_integrity.py }
        P(M7) { successor/officina/runtime_control/INSTALL/T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json }
      There are twenty-one unordered pairs. They are settled in three groups.
        GROUP 1, twelve pairs, {M1,M2,M3} against {M4,M5,M6,M7}.
          Every element of P(M1), P(M2) and P(M3) begins with the eight bytes
          "reviews/" or with the nineteen bytes "successor/OFFICINA_" or is
          exactly the string successor/officina/T_ENVELOPE.json. No other form
          occurs in those three lists, and this is checkable by inspecting the
          52 literal strings above.
          Every element of P(M4) and P(M7) begins with the thirty-five bytes
          "successor/officina/runtime_control/". That prefix is not
          "successor/OFFICINA_" — their eleventh bytes are 0x6F and 0x4F and
          differ — is not "reviews/", and is not the T_ENVELOPE string, which
          has no runtime_control component.
          Every element of P(M5) begins with "src/" and every element of P(M6)
          begins with "tests/"; neither prefix occurs in the first three lists.
          All twelve pairs are therefore disjoint.
        GROUP 2, six pairs, among {M4,M5,M6,M7}.
          P(M5) begins with "src/", P(M6) with "tests/", P(M4) and P(M7) with
          "successor/", so M5 and M6 are disjoint from each other and from M4
          and M7 — five of the six pairs.
          For the sixth, M4 against M7: after the shared prefix
          "successor/officina/runtime_control/" the M4 remainder begins with
          the byte 0x50 ("P") and the M7 remainder with the byte 0x49 ("I"),
          so the two strings differ at that position and the sets are
          disjoint.
        GROUP 3, three pairs, among {M1,M2,M3}.
          M1 against M2: M1's two strings end in _V1_3_DRAFT.md and
          _COMPOSITE_V1_6.md. MS-2's list carries the amendment at
          _V1_DRAFT.md, _V1_1_DRAFT.md and _V1_2_DRAFT.md, and the composite
          at _V1, _V1_1, _V1_2, _V1_3, _V1_4 and _V1_5, and carries no
          _V1_3_DRAFT amendment and no _V1_6 composite. Disjoint.
          M1 against M3: MS-3's seven strings are the harness contract chain,
          the harness signature and the batch-settlement amendment v1.1.1;
          none is an amendment-v1.3 or composite-v1.6 path. Disjoint.
          M2 against M3: MS-2 and MS-3 are two literal lists, and the
          intersection of the 43 strings with the 7 strings is empty.
      Twelve plus six plus three is twenty-one, so every pair is settled. The
      union of the seven sets has 2+43+7+1+1+2+1 = 57 distinct paths, equal to
      MS-8, so no path is counted twice and no member is unassigned. THE SEVEN
      CLASSES ARE PAIRWISE DISJOINT AND THEIR UNION IS THE COMPLETE INSTALLED
      SET. There is no eighth class.

MS-10 THE created_utc GRAMMAR AND ITS VALIDATOR, ONE DEFINITION USED WHEREVER
      THE FIELD APPEARS — MS-4, MS-7, IR-3, TS-1 and TS-3.
      GRAMMAR, exact: the value is a STRING of EXACTLY 20 ASCII characters
      matching
        YYYY "-" MM "-" DD "T" hh ":" mm ":" ss "Z"
      where YYYY is four decimal digits and MM, DD, hh, mm and ss are each two
      decimal digits, and the six literal separators are exactly the bytes
      0x2D, 0x2D, 0x54, 0x3A, 0x3A and 0x5A in those positions. THERE IS NO
      FRACTIONAL PART, no offset other than the literal Z, no lowercase t or
      z, no space, and no leading or trailing byte.
      SEMANTIC VALIDATOR, exact:
        2000 <= YYYY <= 2999
        1 <= MM <= 12
        1 <= DD <= the number of days in month MM of year YYYY under the
          proleptic Gregorian calendar, where YYYY is a leap year if and only
          if it is divisible by 4 and not by 100, or is divisible by 400
        0 <= hh <= 23
        0 <= mm <= 59
        0 <= ss <= 59 — NO LEAP SECOND IS ACCEPTED; ss equal to 60 is invalid
      A value failing the grammar or the validator makes its artifact invalid
      and is refused with that artifact's own failure code.
      created_utc IS PROVENANCE ONLY AND IS NOT TRUSTED TEMPORAL-ORDER
      EVIDENCE. NO CHECK ANYWHERE compares two created_utc values, orders
      artifacts by them, derives a construction sequence from them, refuses on
      their relative values, or treats one as earlier or later than another.
      A verifier that ordered artifacts by created_utc would be trusting an
      unauthenticated author-supplied string. FS-1 and FS-2 state exactly what
      the final bytes do and do not prove.

IR-1  IDENTITY OF THE INSTALL RECORD.
        install_record_id = SHA-256( CANON( {
          "schema": "philosophia.officina.t-watchdog-authority-install-id.v1",
          "members": [ {"class": ..., "path": ..., "sha256": ...}, ... ]
        } ) )
      The preimage object has EXACTLY the two keys schema and members. "schema"
      is the STRING "philosophia.officina.t-watchdog-authority-install-id.v1",
      exactly. "members" is an ARRAY of exactly the 57 entries of MS-8. Each
      entry is an OBJECT with EXACTLY the three keys class, path and sha256,
      all three STRINGS. "class" is one of the seven literals "M1", "M2", "M3",
      "M4", "M5", "M6", "M7". "path" is the member's literal repository-
      relative path. "sha256" is 64 lowercase hexadecimal characters.
      ARRAY ORDER, and it is part of the value: ascending by "class" compared
      byte for byte, then by "path" compared byte for byte. The order is NOT
      re-derived by CANON, which sorts object keys only.
      The result is 64 lowercase hexadecimal characters.

IR-2  PATH.
        successor/officina/runtime_control/INSTALL/<install_record_id>.json
      THE RECORD IS CONTENT-ADDRESSED: its name IS a function of its members,
      so it cannot misdescribe them without changing its own name.

IR-3  THE INSTALL RECORD OBJECT. Installed atomic no-replace; file bytes
      exactly CANON of the object (MS-0). The top-level value is a JSON object
      whose key set is EXACTLY the five keys below, with exactly these types
      and value grammars:
        schema             STRING, exactly
                           "philosophia.officina.t-watchdog-authority-install.v1"
        version            INTEGER, exactly 1
        install_record_id  64-char lowercase hex STRING, equal to the IR-1
                           digest of this object's own members array and equal
                           to the filename stem
        members            ARRAY of exactly 57 OBJECTS, each with EXACTLY the
                           three keys class, path and sha256 as IR-1 defines
                           them, IN IR-1's ORDER
        created_utc        STRING satisfying MS-10
      IT CARRIES DIGESTS AND NO RULES. It is a generated artifact, never a
      specification surface, never scientific evidence, never a covariate, and
      never an input to any acceptance predicate.

IR-4  THE DIRECTED INTEGRITY GRAPH, STATED AS IT ACTUALLY IS.
      VERSION 1.2 SAID "EVERY MEMBER IS ATTESTED BY EXACTLY ONE OTHER OBJECT",
      AND ITS TEST ROW 115 SAID "BY THE RECORD AND BY NOTHING ELSE". BOTH
      STATEMENTS WERE FALSE AND ARE WITHDRAWN. M4 carries the two M1 digests
      and the Stage-A binding; M7 carries the M5 and M6 digests; and the
      record carries every member digest. There are therefore members with more
      than one inbound integrity edge.
      THE ACTUAL GRAPH, COMPLETE, with every edge labelled by what it binds:
        install record  --digest-->  each of the 57 members
                                     (M1 2, M2 43, M3 7, M4 1, M5 1, M6 2, M7 1)
        M4 manifest     --digest-->  the two M1 members
                        --digest-->  the five production roots
                        --digest-->  the three composite region digests and the
                                     composite file digest
                        --path+digest-->  the three pre-selection inputs
                        --path+digest+key id-->  Stage A
        M7 attestation  --digest-->  M5
                        --digest-->  each of the two M6 modules
                        --digest-->  the M6 canonical bundle digest
                        --assertion-->  that the matrix ran and every row of
                                     92..115 passed
        Stage B         --path+digest+key id-->  Stage A
                        --id+path+count-->  the install record and the member set
                        --digest-->  the two M1 members
        detached sig    --Ed25519-->  the exact canonical Stage-B bytes
        Stage A         --key pin-->  the one key under which Stage B verifies
      THESE ADDITIONAL EDGES ARE INTENTIONAL AND ARE NOT SELF-ATTESTATION.
      Redundant inbound edges make a partial substitution fail in more than one
      place; they never let an object vouch for itself.
      WHAT REMAINS TRUE, AND IS THE ACTUAL PROPERTY: NO OBJECT ATTESTS ITSELF.
      The record is not a member of itself and install_record_id is not in its
      own preimage; no member carries its own digest; Stage A carries no digest
      of itself; Stage B carries no signature of itself; the manifest carries
      no digest of itself; the attestation does not attest itself; the
      composite carries none of its own digests.
      NO UNIQUENESS OF ATTESTER IS CLAIMED, AND NO RULE DEPENDS ON ONE. NO
      UNIQUENESS OF EXTERNAL ATTESTER IS CLAIMED EITHER: Stage A is the only
      key pin these bytes define, and nothing here asserts that it is the only
      object that could ever vouch for a member.

IR-5  THE TRUST ROOT IS EXTERNAL TO THE INSTALLED SET AND IS THE TWO-STAGE
      AUTHENTICATED PROTOCOL OF TS-1..TS-6. Version 1.1's formulation — "the
      author signature file that carries the watchdog-freeze selection" — is
      WITHDRAWN as underspecified: it named no path, no schema, no key set, no
      signature algorithm, no signer-key identifier and no verification rule,
      so a substituted file could authorize a different internally consistent
      record. Nothing replaces it except TS-1..TS-6, and no other object of any
      kind authorizes an install. What that protocol does and does not achieve
      is stated exactly at TR-1, TR-2 and FS-1..FS-5, and no section may claim
      more.

IR-6  CREATION ORDER is exactly OR-1 through OR-11 and no other order is
      CONFORMING. CONFORMING IS NOT THE SAME AS MECHANICALLY DISTINGUISHABLE:
      FS-1 states what the final-state gate proves, FS-2 states what it cannot
      prove, and FS-3 keeps the order a mandatory obligation regardless.

IR-7  NO-REPLACE. An EEXIST at the record path means an identical installed set
      is already recorded. THE RECORD IS NEVER OVERWRITTEN, TRUNCATED, RENAMED
      OR DELETED. A changed installed set produces a DIFFERENT name, so a new
      install never collides with an old one and an old one is never silently
      reinterpreted.

IR-8  WHEN THE CHECK RUNS is exactly CK-1.

IR-9  THE CHECK is exactly CK-2 through CK-12, executed in that order,
      fail-closed at the first failure. THE MEMBER ENUMERATION IS CK-4 AND
      DRAWS ONLY ON MS-1..MS-7.

IR-10 FAIL-CLOSED RECOVERY is exactly FC-1.

IR-11 MIXED GENERATIONS ARE REJECTED BY CONSTRUCTION. MS-1 names two literal
      paths. The v1.2 amendment installed with composite v1.6, the v1.3
      amendment installed with composite v1.5, and any other mixture of a
      v2.5-era with a v2.6-era governing file, leave one of MS-1's two literal
      paths absent or carrying bytes that produce a different digest, so the
      set fails at CK-5 or CK-8 and, if a record is rebuilt around the mixture,
      at B15 of TS-5.

IR-12 VERIFYING A DIGEST IS NOT OPENING A DOCUMENT FOR BEHAVIOUR. The
      document-level authority rule is not weakened by M2 or M3: the check
      reads those bytes to hash them and never interprets any of them as a
      rule.

TS-1  STAGE A — WATCHDOG OPTION SELECTION AND KEY PIN. Literal path:
        successor/officina/authorization/P1_WATCHDOG_FREEZE_SELECTION_V1.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the eleven
      keys below, with exactly these types and value grammars:

        schema       STRING, exactly
                     "philosophia.officina.t-p1-watchdog-freeze-selection.v1"
        version      INTEGER, exactly 1
        author       STRING, exactly "Kirill Kruglov"
        selected_option_token
                     STRING, EXACTLY ONE of the two EXISTING option tokens,
                     and no other value validates:
                       I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
                       I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
                     NO THIRD OPTION EXISTS AND NONE IS CREATED HERE.
        selected_option_amendment_token
                     STRING, the EXISTING option-specific amendment token
                     paired with the value above, and no other:
                       P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1 pairs with the
                         token whose name contains _FREEZE_A_
                       P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1   pairs with the
                         token whose name contains _FREEZE_B_
                     A crossed pair does not validate.
        signature_algorithm
                     STRING, exactly "Ed25519"
        public_key_hex
                     STRING of EXACTLY 64 characters, each one of
                     0123456789abcdef, decoding to the 32-byte Ed25519 public
                     key of RFC 8032
        key_id       STRING of EXACTLY 64 characters, each one of
                     0123456789abcdef, equal to the SHA-256 of the 32 RAW key
                     bytes — not of the hexadecimal text
        governing_pre_selection
                     OBJECT with EXACTLY the three keys packet, amendment and
                     composite. Each value is an OBJECT with EXACTLY the two
                     keys path and sha256, both STRINGS, the sha256 being 64
                     lowercase hexadecimal characters. THE THREE path VALUES
                     ARE THESE EXACT LITERAL REPOSITORY-RELATIVE STRINGS:
                       packet
                         successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_6_CORRECTION.md
                       amendment
                         successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
                       composite
                         successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
                     THE THREE sha256 VALUES ARE THE PRE-SELECTION DIGESTS:
                     the bytes the independent X and Y lines confirmed BEFORE
                     any variant block was resolved. The amendment path and the
                     composite path are the same literal strings as MS-1's two
                     paths, but the composite's PRE-SELECTION digest is not its
                     M1 digest, because OR-4 changes the composite's bytes; the
                     amendment's two digests are equal only because OR-4 does
                     not change the amendment.
        threat_model STRING equal, byte for byte, to the exact string quoted
                     at TR-2
        created_utc  STRING satisfying MS-10

      STAGE A IS CREATED ONLY AFTER KIRILL HAS EMITTED ONE EXPLICIT OPTION
      TOKEN. NEITHER THE KEY PAIR, NOR THE ENTROPY THAT PRODUCES IT, NOR THIS
      ARTIFACT IS AUTHORIZED BY THE DRAFTING ROUND THAT PRODUCED THESE BYTES.

TS-2  STAGE A VERIFICATION — AN EXHAUSTIVE FIELD-BY-FIELD ALGORITHM. EVERY
      MANDATORY LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS
      SATISFIED BY MERE PRESENCE. Executed in this order, fail-closed at the
      first failure. Clauses A1..A14 are evaluable from OR-3 onward; A15..A17
      require the M4 manifest and are evaluated from OR-7 onward and at every
      production entry point.
        A1   a file exists at TS-1's exact literal path. No other path is
             consulted, and a well-formed selection artifact anywhere else is
             not Stage A.                            else STAGE_A_ABSENT
        A2   the file bytes parse as JSON and are byte-identical to CANON of
             the parsed value, trailing 0x0A included.
                                                     else STAGE_A_MALFORMED
        A3   the top-level value is an OBJECT whose key set is EXACTLY TS-1's
             eleven keys — no extra key, no missing key.
                                                     else STAGE_A_MALFORMED
        A4   schema is a STRING equal to
             "philosophia.officina.t-p1-watchdog-freeze-selection.v1".
                                                     else STAGE_A_MALFORMED
        A5   version is the INTEGER 1 — not the string "1", not 1.0.
                                                     else STAGE_A_MALFORMED
        A6   author is a STRING equal to "Kirill Kruglov".
                                                     else STAGE_A_MALFORMED
        A7   signature_algorithm is a STRING equal to "Ed25519".
                                                     else STAGE_A_MALFORMED
        A8   selected_option_token is a STRING equal to one of TS-1's two
             literal option tokens and to no other value.
                                                     else STAGE_A_OPTION_INVALID
        A9   selected_option_amendment_token is a STRING equal to the token
             TS-1 pairs with the value found at A8, and to no other value.
                                                     else STAGE_A_OPTION_INVALID
        A10  public_key_hex is a STRING of exactly 64 characters, each one of
             0123456789abcdef, decoding to exactly 32 bytes.
                                                     else STAGE_A_KEY_MALFORMED
        A11  key_id is a STRING of exactly 64 characters, each one of
             0123456789abcdef, and equals the SHA-256 of the 32 raw bytes
             decoded at A10.                         else STAGE_A_KEY_MALFORMED
        A12  governing_pre_selection is an OBJECT whose key set is EXACTLY
             {packet, amendment, composite}; each value is an OBJECT whose key
             set is EXACTLY {path, sha256}; each sha256 is a STRING of exactly
             64 characters, each one of 0123456789abcdef.
                                                     else STAGE_A_MALFORMED
        A13  the three path values equal, respectively, TS-1's three literal
             pre-selection path strings, byte for byte.
                                                     else STAGE_A_MALFORMED
        A14  threat_model is a STRING equal, byte for byte, to the exact
             string quoted at TR-2, and created_utc satisfies the grammar AND
             the semantic validator of MS-10. THE created_utc VALUE IS NOT
             COMPARED WITH ANY OTHER TIMESTAMP AND ORDERS NOTHING.
                                                     else STAGE_A_MALFORMED
        A15  the three path values of governing_pre_selection equal,
             respectively, the manifest's pre_selection_packet_path,
             pre_selection_amendment_path and pre_selection_composite_path.
                                            else STAGE_A_PRESELECTION_MISMATCH
        A16  the three sha256 values of governing_pre_selection equal,
             respectively, the manifest's pre_selection_packet_sha256,
             pre_selection_amendment_sha256 and pre_selection_composite_sha256.
                                            else STAGE_A_PRESELECTION_MISMATCH
        A17  the SHA-256 of the whole Stage-A file equals the manifest's
             stage_a_sha256; TS-1's path equals the manifest's stage_a_path;
             and key_id equals the manifest's stage_a_key_id.
                                            else STAGE_A_BINDING_MISMATCH
      A17 IS WHAT MAKES A SUBSTITUTED STAGE-A FILE FAIL WITHOUT A MATCHING
      SUBSTITUTION OF M4, and M4 is a member whose digest enters
      install_record_id, which Stage B signs. TR-1 and TR-2 state exactly how
      far that reaches.

TS-3  STAGE B — INSTALL-ID AUTHORIZATION. TWO literal paths:
        successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.json
        successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.sig
      ENCODING: the .json file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the
      thirteen keys below, with exactly these types and value grammars:

        schema                     STRING, exactly
                                   "philosophia.officina.t-p1-watchdog-authority-install-authorization.v1"
        version                    INTEGER, exactly 1
        stage_a_path               STRING, exactly TS-1's literal path
        stage_a_sha256             64-char lowercase hex STRING, the SHA-256 of
                                   the whole Stage-A file
        key_id                     64-char lowercase hex STRING, equal to
                                   Stage A's key_id
        selected_option_token      STRING, equal to Stage A's
                                   selected_option_token
        install_record_id          64-char lowercase hex STRING, the id
                                   computed at OR-9
        install_record_path        STRING, exactly IR-2's path for that id:
                                   the literal prefix
                                   successor/officina/runtime_control/INSTALL/
                                   followed by install_record_id followed by
                                   the five bytes ".json"
        member_count               INTEGER, exactly 57
        governing_amendment_sha256 64-char lowercase hex STRING, the digest of
                                   the M1 amendment bytes
        governing_composite_sha256 64-char lowercase hex STRING, the digest of
                                   the M1 composite bytes AFTER variant
                                   resolution
        signature_algorithm        STRING, exactly "Ed25519"
        created_utc                STRING satisfying MS-10
      THE STAGE-B ARTIFACT CARRIES NO SIGNATURE INSIDE ITSELF. The signature is
      detached, at the .sig path, and is TS-4.

TS-4  CANONICAL SIGNED MESSAGE, ALGORITHM AND DETACHED SIGNATURE ENCODING.
      THE SIGNED MESSAGE IS EXACTLY THE BYTE SEQUENCE OF THE STAGE-B .json
      FILE, which MS-0 requires to equal CANON of its object, the trailing 0x0A
      included. There is no prefix, no suffix, no domain separator added at
      signing time, no re-serialization, and no hash applied before signing:
      Ed25519 of RFC 8032 in its pure form is applied to those bytes directly.
      The pre-hashed variant is not permitted and does not validate.
      THE DETACHED SIGNATURE FILE at the .sig path contains EXACTLY 128
      characters, each one of 0123456789abcdef — the 64-byte Ed25519 signature
      — with NO trailing newline and no other byte. Any other length, any
      uppercase character, any other encoding and any trailing byte is a
      malformed signature and fails closed. THE SIGNATURE FILE CONTAINS NO KEY,
      NO IDENTIFIER AND NO ALGORITHM NAME: the algorithm is fixed by TS-3 and
      the key by TS-1.

TS-5  STAGE B VERIFICATION — AN EXHAUSTIVE FIELD-BY-FIELD ALGORITHM. EVERY
      MANDATORY LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS
      SATISFIED BY MERE PRESENCE. Executed in this order, fail-closed at the
      first failure. Clauses B1..B13 run at CK-3; clauses B14..B18 run at CK-9,
      because they depend on the recomputed id and the member digests.
        B1   both TS-3 paths exist.                  else STAGE_B_ABSENT
             If the .json exists and the .sig does not,
                                                     STAGE_B_SIGNATURE_ABSENT
        B2   the .json bytes parse as JSON and are byte-identical to CANON of
             the parsed value, trailing 0x0A included.
                                                     else STAGE_B_MALFORMED
        B3   the top-level value is an OBJECT whose key set is EXACTLY TS-3's
             thirteen keys — no extra key, no missing key.
                                                     else STAGE_B_MALFORMED
        B4   schema is a STRING equal to
             "philosophia.officina.t-p1-watchdog-authority-install-authorization.v1".
                                                     else STAGE_B_MALFORMED
        B5   version is the INTEGER 1.               else STAGE_B_MALFORMED
        B6   created_utc satisfies the grammar AND the semantic validator of
             MS-10. ITS VALUE IS NOT COMPARED WITH ANY OTHER TIMESTAMP AND
             ORDERS NOTHING.                         else STAGE_B_MALFORMED
        B7   member_count is the INTEGER 57.         else STAGE_B_MALFORMED
        B8   install_record_id, stage_a_sha256, key_id,
             governing_amendment_sha256 and governing_composite_sha256 are
             each a STRING of exactly 64 characters, each one of
             0123456789abcdef.                       else STAGE_B_MALFORMED
        B9   install_record_path is a STRING equal to the concatenation of the
             literal prefix
             successor/officina/runtime_control/INSTALL/ , the value of
             install_record_id, and ".json".         else STAGE_B_MALFORMED
        B10  signature_algorithm is a STRING equal to "Ed25519".
                                                     else STAGE_B_ALGORITHM_INVALID
        B11  the .sig bytes are exactly 128 characters, each one of
             0123456789abcdef, and nothing else.
                                                     else STAGE_B_MALFORMED
        B12  Ed25519 verification of that 64-byte signature over the exact
             .json bytes SUCCEEDS AGAINST THE 32-BYTE PUBLIC KEY OF STAGE A
             AND AGAINST NO OTHER KEY. There is no key list, no key discovery,
             no fallback key, no unsigned acceptance, no algorithm negotiation
             and no downgrade.                       else STAGE_B_SIGNATURE_INVALID
        B13  stage_a_path is a STRING equal to TS-1's literal path;
             stage_a_sha256 equals the SHA-256 of the Stage-A file found at
             that path; and key_id equals Stage A's key_id.
                                                     else STAGE_B_STAGE_A_MISMATCH
        B14  selected_option_token equals Stage A's selected_option_token.
                                                     else STAGE_B_OPTION_MISMATCH
        B15  install_record_id equals the id recomputed at CK-6 from the
             members found on disk.                  else STAGE_B_INSTALL_ID_MISMATCH
        B16  install_record_path names the record file that CK-7 matched.
                                                     else STAGE_B_INSTALL_ID_MISMATCH
        B17  member_count equals the enumerated member count, 57.
                                                     else STAGE_B_INSTALL_ID_MISMATCH
        B18  governing_amendment_sha256 and governing_composite_sha256 equal
             the digests of the two M1 members found on disk at CK-5.
                                                     else STAGE_B_GOVERNING_MISMATCH

TS-6  STAGE A, STAGE B, THE DETACHED SIGNATURE AND THE PUBLIC KEY ARE OUTSIDE
      M1..M7, AND NEITHER STAGE IS SELF-ATTESTED.
      The three artifact paths all begin with the thirty-five bytes
      "successor/officina/authorization/P1", which is a prefix of no member
      path and equals no literal member path, so by the same argument as MS-9
      none of them is a member of any class. The public key exists only inside
      Stage A and has no path of its own.
      Stage A is attested by the manifest binding of TS-2 A17 and by the
      author's act of creating it; it does not attest itself. Stage B is
      attested by the Stage-A key, which Stage B does not contain; it does not
      attest itself.
      NEITHER STAGE IS A SPECIFICATION SURFACE. Both carry values and no rules,
      exactly as the install record does.
      THE PRIVATE KEY IS NEVER STORED IN THIS REPOSITORY, IS NEVER A MEMBER,
      AND IS NAMED BY NO PATH IN ANY GOVERNING BYTE.
      NO PERMANENT FALLBACK AND NO UNSIGNED PROCEDURAL SHORTCUT EXISTS. There
      is no mode, flag, environment variable, build profile, migration path,
      recovery path, grace period or test hook in which the gate admits a state
      with Stage A absent, Stage B absent, the signature absent, the signature
      unverified, or the signature verified against any key other than Stage
      A's.

OR-1   THE ORDER BELOW IS THE SOLE CONFORMING CONSTRUCTION PROCEDURE AND IS A
       MANDATORY OPERATOR OBLIGATION. A step may not begin before every earlier
       step is complete and verified. NO STEP IS OPTIONAL, REORDERABLE OR
       SKIPPABLE, AND NO STEP HAS AN ALTERNATE PATH. There is exactly one
       conforming sequence and it is OR-2 through OR-11.
       IT IS AN OBLIGATION ON THE OPERATOR AND THE PROCEDURAL DRIVER, NOT A
       PROPERTY THE FINAL-STATE GATE VERIFIES. G-11 checks the exact final
       state and nothing else. FS-1 states what that proves, FS-2 states what
       it cannot prove, FS-3 keeps this obligation binding regardless, FS-4
       states what happens when a violation is observed while it occurs, and
       FS-5 places an unobserved violation inside the declared residual of
       TR-2. NO CLAUSE ANYWHERE MAY ASSERT THAT G-11 RECONSTRUCTS THE ORDER IN
       WHICH IDENTICAL FINAL BYTES CAME TO EXIST.

OR-2   KIRILL EMITS EXACTLY ONE OF THE TWO EXISTING OPTION TOKENS. This precedes
       everything else. It is authorized by nothing in these bytes and is
       predicted by nothing in them.

OR-3   STAGE A IS CREATED — including generation of the Ed25519 key pair — and
       is verified per TS-2 clauses A1 through A14. Clauses A15 through A17 are
       not yet evaluable because M4 does not exist; they are evaluated at OR-7
       and at every production entry point thereafter.

OR-4   EVERY VARIANT BLOCK IN THE COMPOSITE IS RESOLVED to the signed branch and
       the other branch is DELETED; the v1.3 amendment is installed. After this
       step G-10 finds zero markers. M1 is now final and its two digests are
       fixed.

OR-5   THE M5 VERIFIER AND THE TWO M6 MODULES ARE INSTALLED at their literal
       paths of MS-5 and MS-6.

OR-6   THE M4 MANIFEST IS WRITTEN at MS-4's literal path, with all twenty keys,
       the canonical reachable_closure shape, the three pre-selection path and
       digest pairs, and the three Stage-A binding fields.

OR-7   THE FULL TEST MATRIX RUNS against the M5 verifier and the M6 bundle and
       EVERY row passes. The placeholder audit and the guard fires are run; the
       required placeholder count and guard-fire count are ZERO. TS-2 is now
       evaluable in full and is evaluated in full, A1 through A17.

OR-8   THE M7 ATTESTATION IS WRITTEN at MS-7's literal path, binding the M5
       digest and the two M6 digests found on disk and the bundle digest
       recomputed from them.

OR-9   THE CANONICAL 57-MEMBER LIST IS BUILT FROM MS-1..MS-7 ALONE and
       install_record_id is computed per IR-1.

OR-10  THE STAGE-B ARTIFACT AND ITS DETACHED SIGNATURE ARE CREATED and are
       verified per TS-5, all eighteen clauses, BEFORE anything is written under
       the INSTALL directory other than the M7 attestation of OR-8.

OR-11  THE INSTALL RECORD IS INSTALLED no-replace at its content-addressed path,
       LAST; then every M2 and M3 member is verified byte-identical to the
       digest recorded at MS-2 and MS-3.
       VERSION 1.2 ADDED HERE THAT "a record installed before OR-10 completes is
       an ordering violation and is refused at CK-3 or CK-9". THAT SENTENCE IS
       WITHDRAWN AS FALSE OF THE FINAL STATE. It holds only while Stage B is
       still absent, which is a contemporaneous fact covered by FS-4; once the
       exact valid final bytes exist, FS-2 applies and no final-state check
       distinguishes the two histories. Writing the record early remains a
       violation of OR-1; it is simply not one this gate can detect after the
       fact.

CK-1   WHEN. Before ANY production entry point — before any process is created,
       any handle is allocated, any freeze route is reachable, any evidence is
       accepted and any settlement runs. This check is the FIRST thing a
       production entry point does; nothing precedes it and no work is performed
       in parallel with it.

CK-2   VERIFY STAGE A per TS-2, clauses A1 through A17, in order.

CK-3   VERIFY STAGE B per TS-5, clauses B1 through B13 — every clause that does
       not depend on the recomputed id or the member digests.

CK-4   ENUMERATE THE 57 MEMBERS FROM MS-1 THROUGH MS-7 ALONE. No wildcard, no
       directory scan, no glob, no adjective, no path taken from the install
       record, no path taken from the manifest, no path taken from the
       provenance region and no path taken from any future-edit table. THE
       ENUMERATION IS A CONSTANT OF THESE GOVERNING BYTES and is identical in
       the two governing files.

CK-5   RECOMPUTE THE SHA-256 OF EVERY ENUMERATED MEMBER from its bytes on disk.
       For M2 and M3 additionally require each recomputed digest to equal the
       digest recorded literally at MS-2 and MS-3. For M4, M7 and the install
       record additionally require the bytes to satisfy their full schema and
       value grammars — MS-4, MS-7 and IR-3 — including every literal schema
       value, every type, every nested shape, every array order and every
       created_utc grammar and validator. A member that hashes correctly but
       violates its schema is refused with MEMBER_SUBSTITUTED.

CK-6   RECOMPUTE install_record_id per IR-1 from what was found on disk.

CK-7   REQUIRE THE RECOMPUTED ID TO EQUAL THE INSTALL RECORD'S FILENAME.

CK-8   REQUIRE THE RECORD'S MEMBERS LIST TO EQUAL THE ENUMERATED SET EXACTLY:
       the same cardinality 57, the same class labels, the same paths, the same
       digests, and the same order. An omission, an extra member, a stale digest
       and a substituted member each fail here.

CK-9   COMPLETE STAGE B VERIFICATION: TS-5 clauses B14 through B18.

CK-10  MULTIPLICITY. Require that EXACTLY ONE file directly under
       successor/officina/runtime_control/INSTALL/ has a name consisting of 64
       lowercase hexadecimal characters followed by ".json". Zero fails with
       INSTALL_RECORD_ABSENT; two or more fail with INSTALL_RECORD_REPLAYED, and
       a retained record from an earlier install generation ALONGSIDE the
       current one is exactly that case. THIS IS NOT A MEMBER ENUMERATION: it
       reads no member, takes no path into the member set, and is a uniqueness
       predicate over one directory whose only two admissible name forms are
       that hexadecimal form and MS-7's literal attestation name.
       A RECORD FROM AN EARLIER GENERATION PRESENTED ALONE AGAINST THE CURRENT
       MEMBERS STILL FAILS: the id recomputed at CK-6 from the members now on
       disk does not equal it, so CK-7 refuses and B15 refuses.
       WHAT THIS DOES NOT CATCH: a COMPLETE COHERENT ROLLBACK, in which the
       members themselves are also restored to the earlier generation, so that
       the sole record, Stage A, Stage B and the signature all match each other.
       TR-2 clause (b) states that case exactly and does not claim to refuse it.

CK-11  REQUIRE THE M7 ATTESTATION to name the M5 digest and the two M6 digests
       found at CK-5, in MS-6's order, and to carry the bundle digest recomputed
       from them per MS-6, with rows_attested exactly the 24 integers 92..115
       ascending, row_count exactly 24 and all_rows_passed exactly the boolean
       true. A passing attestation produced against a different verifier or a
       different test bundle is rejected here.

CK-12  REQUIRE EVERY M2 AND M3 MEMBER to be byte-identical to its recorded
       digest — already forced by CK-5 — and refuse with HISTORICAL_BYTE_MOVED
       on any difference. THE WHOLE CHECK IS FAIL-CLOSED AT THE FIRST FAILURE
       AND HAS NO PARTIAL MODE, NO WARNING MODE AND NO OVERRIDE.

FC-1  THE CLOSED FAILURE-CODE SET. On ANY failure of CK-1 through CK-12, or on
      an observed procedure violation under FS-4, REFUSE with
      "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE" and exactly one reason code
      naming the first failing check and the offending path. The set has 25
      codes, is closed, and no build may add, rename or merge one:
        STAGE_A_ABSENT                 STAGE_A_MALFORMED
        STAGE_A_OPTION_INVALID         STAGE_A_KEY_MALFORMED
        STAGE_A_PRESELECTION_MISMATCH  STAGE_A_BINDING_MISMATCH
        STAGE_B_ABSENT                 STAGE_B_MALFORMED
        STAGE_B_SIGNATURE_ABSENT       STAGE_B_SIGNATURE_INVALID
        STAGE_B_ALGORITHM_INVALID      STAGE_B_STAGE_A_MISMATCH
        STAGE_B_OPTION_MISMATCH        STAGE_B_INSTALL_ID_MISMATCH
        STAGE_B_GOVERNING_MISMATCH
        INSTALL_RECORD_ABSENT          INSTALL_RECORD_NAME_MISMATCH
        INSTALL_RECORD_REPLAYED
        MEMBER_OMITTED                 MEMBER_EXTRA
        MEMBER_STALE                   MEMBER_SUBSTITUTED
        ATTESTATION_MISMATCH           HISTORICAL_BYTE_MOVED
        PROCEDURE_VIOLATION_OBSERVED
      PROCEDURE_VIOLATION_OBSERVED is the FS-4 code and is the only code that
      can be raised by a contemporaneous observation rather than by a predicate
      over final bytes. It routes to the ordinary process/control invalidity
      disposition. Version 1.1's INSTALL_RECORD_UNAUTHORIZED remains WITHDRAWN,
      replaced by the nine STAGE_B_ codes.
      ON REFUSAL no process is created, no handle is allocated, no freeze route
      is reachable, no evidence is accepted, no settlement runs, and NOTHING
      DEGRADES TO A PRIOR BEHAVIOUR. Recovery is to complete OR-1 through OR-11
      and re-run the check; there is no other recovery.

FS-1  WHAT G-11 PROVES. G-11 IS A FINAL-STATE VERIFIER. On success it proves,
      of the bytes present on disk at the moment it runs, exactly this and no
      more:
        a. Stage A exists at its exact literal path, its bytes are canonical,
           and every one of its eleven fields satisfies TS-2 A1..A17;
        b. Stage B and its detached signature exist at their exact literal
           paths, the .json bytes are canonical, every one of its thirteen
           fields satisfies TS-5 B1..B18, and the signature verifies under the
           key pinned in Stage A and under no other key;
        c. all 57 members exist at their literal paths; every digest matches;
           every M2 and M3 digest additionally equals the value recorded
           literally at MS-2 and MS-3; and M4, M7 and the record satisfy their
           full schemas;
        d. install_record_id recomputed from those bytes equals the record's
           filename and equals Stage B's install_record_id;
        e. M7 binds the M5 digest and the two M6 digests actually found;
        f. exactly one content-addressed record exists directly under the
           INSTALL directory.
      THAT IS THE WHOLE OF WHAT IT PROVES. It is a predicate over a byte state,
      evaluated at one instant.

FS-2  WHAT G-11 DOES NOT PROVE, STATED SO THAT NO SECTION MAY IMPLY OTHERWISE.
      G-11 OBSERVES NO EVENT AND RECONSTRUCTS NO HISTORY. The artifacts carry
      no trusted monotonic counter, no append-only predecessor chain, no
      externally checked sequence number, no notarized time, no witness outside
      this repository and no evidence of any kind about the order in which
      files came to exist. created_utc is author-supplied, unauthenticated and
      compared with nothing (MS-10).
      THEREFORE, GIVEN THE EXACT VALID FINAL BYTES, G-11 CANNOT DISTINGUISH
      ANY OF THE FOLLOWING PAIRS. In each pair the final bytes are identical,
      so no predicate over final bytes separates them:
        the record written at OR-11        the identical record written before
                                           Stage B existed
        an M7 written after the matrix ran the identical M7 written before the
                                           matrix ran
        an id computed after M4 was        the identical id computed from
          written                          planned M4 bytes before M4 existed
        a Stage A created before OR-4      the identical Stage A created after
                                           variant resolution
      EVERY VERSION-1.2 STATEMENT TO THE CONTRARY IS WITHDRAWN: OR-11's claim
      that an early record is refused at CK-3 or CK-9; test 106(h)'s claim that
      the gate refuses each forbidden ordering; and every summary sentence
      asserting that any deviation from OR-1..OR-11 is refused. What was true
      in each of those cases is the CONTEMPORANEOUS fact of FS-4, not a
      property of the final state.

FS-3  OR-1..OR-11 REMAINS A MANDATORY OPERATOR OBLIGATION AND THE SOLE
      CONFORMING CONSTRUCTION PROCEDURE. An operator or driver that departs
      from it has produced a NONCONFORMING installation whether or not any
      check can say so, and the departure is a governance violation on its own
      terms. FS-2 withdraws a false claim about detection; it withdraws no
      obligation, weakens no step and permits no alternate route.

FS-4  A CONTEMPORANEOUSLY DISCOVERED PROCEDURE VIOLATION FAILS CLOSED. If the
      procedural driver, an operator, a review, a crash-recovery pass or any
      check observes a departure from OR-1..OR-11 WHILE IT IS OCCURRING, or
      while an intermediate state still exhibits it — a hex-named record
      present under the INSTALL directory while Stage B is absent; an M7
      present with no recorded matrix run; a manifest written after the id was
      computed; a Stage A whose creation follows OR-4 in the driver's own
      recorded state; a driver whose own step counter is out of order — then
      the installation is REFUSED with PROCEDURE_VIOLATION_OBSERVED, routes to
      the ordinary process/control invalidity disposition, AND NO PRODUCTION
      ENTRY POINT RUNS.
      This refusal is a CONTROL-PLANE fact. It is never scientific evidence and
      enters no acceptance predicate, qualification, comparison, endpoint, Q or
      C fact.

FS-5  AN UNDISCOVERED PROCEDURE VIOLATION IS INSIDE THE DECLARED PROCEDURAL
      RESIDUAL OF TR-2 AND IS NOT CLAIMED TO BE CAUGHT. This is stated rather
      than hidden. It is the honest consequence of having no trusted external
      order anchor.
      NO SUCH ANCHOR IS INTRODUCED, PERMITTED OR IMPLIED BY THIS AMENDMENT: no
      hardware security module, no external service, no timestamp oracle, no
      notary, no transparency log, no monotonic counter device and no new
      scientific gate. Adding one would be a new design round with its own
      author cell, and it is out of scope here.

TR-1  NON-CIRCULARITY, PROVED BY THE ORDER OF DETERMINATION.
        the 57 members determine install_record_id            (IR-1)
        install_record_id determines the record's filename     (IR-2)
        Stage B names that id and is signed over its own canonical bytes
                                                               (TS-3, TS-4)
        the Ed25519 key that verifies Stage B is pinned in Stage A
                                                               (TS-1, TS-5 B12)
        Stage A is created at OR-3, before any M1 byte is final at OR-4, and is
        written by no later step
      NO OBJECT IN THIS CHAIN ATTESTS ITSELF; IR-4 states the complete directed
      integrity graph, including the intentional redundant edges from M4 and
      M7, and claims no uniqueness of attester. Each link is verified by a link
      above it, and the chain terminates OUTSIDE the installed set at an
      artifact the author created. THERE IS NO CYCLE.
      NON-CIRCULARITY IS A STATEMENT ABOUT THE DEPENDENCY GRAPH, NOT ABOUT
      TIME. It does not imply that the construction order is verifiable; FS-2
      governs that.

TR-2  THE NAMED RESIDUAL — PROCEDURAL, STATED, NOT CLOSED. It has TWO clauses
      and both are load-bearing.
      (a) FULL-CHAIN SUBSTITUTION AT OR BEFORE STAGE-A CREATION. Stage A's
          authenticity rests on author custody: it is a tracked repository file
          created by Kirill, its exact digest is bound into the manifest by
          TS-2 A17, and that digest is recorded by the independent X and Y
          confirmations of the selection round. An actor able to write this
          repository at or before Stage-A creation can substitute Stage A,
          Stage B, the signature, the manifest and the record together and
          produce an internally consistent install.
      (b) COMPLETE COHERENT ROLLBACK OF A PREVIOUSLY VALID GENERATION, AT ANY
          LATER TIME. After a newer generation exists, an actor able to replace
          the whole repository control set can RESTORE an earlier generation
          in full — its Stage A, all of its members, its Stage B, its detached
          signature and its sole content-addressed record. On those restored
          bytes every check of FS-1 passes: Stage A matches the restored M4;
          the old signature verifies under the restored Stage-A key; the old id
          matches the restored members and the sole record name; CK-10 sees
          exactly one hex-named record; every digest and the attestation match.
          NO NEW SIGNATURE AND NO PRIVATE KEY ARE NEEDED. THIS REACHES A
          RUNNABLE STATE AND IS NOT REFUSED. It is outside the guarantee, and
          the coherent-rollback fixture of test 106 classifies it as such
          rather than pretending it fails.
      WHAT THE TWO STAGES DO CLOSE — exactly these PROPER-SUBSET cases, and
      this list is the whole of the claim:
        Stage A replaced while the manifest is not          A17
        the manifest replaced while Stage A is not          A17, CK-5, CK-8
        the signature replaced, removed or malformed        B11, B12
        Stage B replaced while the signature is not         B12
        the record replaced while the members are not       CK-6, CK-7, B15
        the members replaced while the record is not        CK-5, CK-8
        M7 replaced while M5 or M6 is not                   CK-11
        an old record presented against current members     CK-7, B15
        an old record retained beside the current one       CK-10
        a mixed-generation pair of governing files          CK-5, CK-8, B15
        an option mismatch between the two stages           A9, B14
        an unsigned install of any shape                    B1, B12 — no route
                                                            admits one
      NO SENTENCE IN THESE GOVERNING BYTES, IN ANY PACKET AND IN ANY CLOSURE
      MAY CLAIM: that every post-hoc substitution is closed; that complete
      coherent rollback is resisted, detected or refused; that custody is
      immutable or external to this repository; or that any cryptographic
      freshness, monotonicity, recency or liveness property holds.
      THE ED25519 CHAIN AUTHENTICATES STAGE B RELATIVE TO THE STAGE-A KEY AND
      CLOSES PARTIAL SUBSTITUTION UNDER THE PROCEDURAL ROOT. IT CREATES NO
      FRESHNESS. A signature proves who signed a message, never when, and
      never that no earlier signed message is still available.
      Both residual clauses are procedural, are of the same kind as the A3
      same-UID residual already named in the composite's named-residuals
      section (§P1-12.4), are infrastructure facts and not scientific evidence,
      and are citable in no Q or C fact.
      THE EXACT threat_model STRING STAGE A MUST CARRY, byte for byte, is the
      following. It contains no newline: each line break in this presentation
      stands for exactly one space, and there is no leading or trailing space.
        Stage A is the external trust root for the P1 watchdog-freeze
        install. Its authenticity rests on author custody of this
        repository. An actor able to write this repository before Stage A
        exists can substitute the whole authorization chain, and an actor
        able to replace the whole repository control set at any later time
        can restore a complete earlier valid generation; both residuals are
        procedural, are named, and are not closed by these bytes.

XS-1  EXTERNAL AUTHOR STATE THAT IS NOT A MEMBER AND IS NOT AUTHORITY HERE.
        successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
        7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f
      WHAT IT IS. Kirill's signed selection of the P1 process-claim identity
      architecture, Option A, token
      I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY, dated 2026-08-04.
      It is recorded here as CURRENT AUTHOR STATE so that no reader has to
      infer it, and for no other purpose.
      WHAT IT IS NOT. Every clause here is load-bearing:
        it does NOT sign, accept or authorize the separately named token
          P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, which the identity
          packet requires to be reviewed and accepted SEPARATELY before Option
          A can become operative. That token is NOT ACCEPTED, and this
          amendment does not accept it, make it signable, or predict it;
        it does NOT select, move or influence the watchdog-freeze cell, which
          remains NOT SELECTED;
        it does NOT make this amendment, the composite, or any P1 composite
          operative, and it resolves no blocking notice;
        it is NOT a member of M1..M7 and its digest is in no install record;
        it is NOT scientific evidence, not a covariate, not an endpoint, not a
          qualification or comparison input, and not an input to any acceptance
          predicate. It is a control-plane author-state fact.
      WHY IT IS NOT A MEMBER. Binding it into M1..M7 would make the watchdog
      install depend on a selection whose own enabling token is unaccepted, and
      would import an unreviewed prerequisite into a gate whose entire point is
      that its inputs are literal, closed and reviewed.
      WHERE IT MUST BE ACCOUNTED FOR INSTEAD. The LATER COMBINED BINDING — the
      single reviewed specification that binds the signed identity selection
      together with the signed watchdog option, and which is what resolves the
      process-claim identity cell stated at composite §P1-13.2 row 2 — MUST:
        a. record this signature's literal path and its exact digest;
        b. record the separate review and acceptance of
           P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, or refuse to proceed;
        c. state whether this signature becomes a member of that binding's own
           closed set and, if so, in which class and with what cardinality;
        d. re-derive the identity fields of the process-claim record, which
           this amendment neither selects nor repairs (F-2, N-4).
      UNTIL THAT BINDING EXISTS AND HAS BEEN INDEPENDENTLY REVIEWED, THE
      IDENTITY CELL IS RECORDED AS SELECTED, THE IDENTITY BOUNDED-WEAKENING
      TOKEN AS NOT ACCEPTED, AND NEITHER FACT MOVES ANYTHING IN THIS PAIR.

--- END JOINT INSTALL AND AUTHORIZATION BLOCK ---
```

---

## §A11. What this amendment does not do

```text
N-1   IT SELECTS NO OPTION. Neither `W-A` nor `W-B` is selected. The
      watchdog-freeze author cell remains OPEN.
N-2   IT MOVES NO RECOMMENDATION. `W-B` remains recommended on the same five
      criteria, and nothing here is asymmetric between the options.
N-3   IT OPENS NO NEW AUTHOR CELL and adds, removes and renames no selection
      token.
N-4   IT DOES NOT REOPEN THE PROCESS-CLAIM IDENTITY CELL.
N-5   IT REVOKES NO SIGNED SELECTION.
      `I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER` is not revoked, not
      re-run and not reopened. C1 retains a dedicated watchdog PROCESS; its
      freezer and witness content is amended.
N-6   IT EDITS NO HISTORICAL BYTE.
N-7   IT REOPENS NO PEER SCHEMA.
N-8   IT CREATES NO NEW RECORD CLASS, NAMESPACE OR SCHEMA. The install record is
      a generated control-plane artifact under an existing control-plane root,
      is never scientific evidence, and enters no predicate.
N-9   IT INTRODUCES NO NEW CONSTANT. `QC-1`..`QC-3` are restatements of values
      the historical chain already carried.
N-10  IT INTRODUCES NO SCIENTIFIC CELL, no implementation authority and no
      activation authority. The two-stage authentication of §A10 is PROCESS
      INTEGRITY ONLY: it adds no watchdog mechanism, no treatment, no evidence
      class, no covariate and no author option, and it is an input to no
      acceptance predicate, qualification, comparison or Q/C fact.
N-11  IT GENERATES NOTHING. No key pair, no entropy, no Stage-A selection
      artifact, no Stage-B authorization artifact, no detached signature, no
      manifest, no attestation and no install record is created, requested,
      predicted or made creatable by these bytes. Stage A is created only after
      Kirill's future explicit option token, and by Kirill.
N-12  IT CLAIMS NO TEMPORAL PROPERTY. `G-11` verifies a final byte state. It
      reconstructs no creation history, trusts no timestamp, and provides no
      freshness, monotonicity, recency or liveness guarantee. `FS-1` states what
      it proves; `FS-2` states what it cannot; `TR-2` states the two residual
      clauses, including complete coherent rollback, that it does not close. NO
      HARDWARE SECURITY MODULE, EXTERNAL SERVICE, TIMESTAMP ORACLE, NOTARY,
      TRANSPARENCY LOG OR MONOTONIC-COUNTER DEVICE IS ADDED, PERMITTED OR
      IMPLIED, AND NO NEW SCIENTIFIC GATE IS CREATED.
N-13  IT DOES NOT BIND THE SIGNED PROCESS-CLAIM IDENTITY SELECTION. `XS-1`
      records that selection as current author state and as a member of no
      class. This amendment does not accept
      `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, does not make it signable,
      does not predict it, and does not become operative because an identity
      option was selected. The identity cell's resolution belongs to the later
      combined binding named at `XS-1`, and `N-4` is unchanged: this amendment
      neither selects nor repairs the process-claim identity fields.
```

---

## §A12. Negative space

This amendment creates nothing executable and authorizes no selection, X/Y
verdict, acceptance, implementation, commit, verifier or manifest edit, process,
socket, pipe, fork, exec, signal, wait or `prctl` operation, supervisor, PCS,
controller, worker or watchdog, capability, world, learner, entropy, candidate,
trajectory, capacity artifact, custody disposition, result manifest, spend,
datum, outcome, Proof or claim movement. No freeze was executed, requested,
journalled or witnessed. No install record was created. No key pair, entropy,
Stage-A selection artifact, Stage-B authorization artifact or detached signature
was generated, requested or predicted. No identity token was accepted and no
identity bounded weakening was authorized. No `/proc` was read
against any live process. No clock was sampled for any contract purpose. It
predicts no qualification and no comparison outcome. It modified no existing
file. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
