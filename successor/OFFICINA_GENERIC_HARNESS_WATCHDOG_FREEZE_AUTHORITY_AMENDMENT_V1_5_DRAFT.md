# Officina generic-harness — watchdog freeze-authority amendment, version 1.5 (draft)

**This document WHOLLY REPLACES version 1.4 (`f845b98d…`), which wholly replaced
version 1.3 (`c3da2a7d…`), which wholly replaced version 1.2 (`058c119c…`),
which wholly replaced version 1.1 (`ec5ddff8…`), which wholly replaced version 1
(`380b87f0…`).** It is not a delta over any of them, does not require any of
them to be read, and after acceptance all five are provenance.
It is the **sole live peer-layer authority** for watchdog liveness, freeze
execution, freeze evidence, freeze-evidence acceptance, the swap-only carve-out
and the joint installation. **It is written to be read without opening any
historical supervisor/control-channel document.**

**Author.** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This document selects nothing.**

**Status.** `NOT_ACCEPTED`.
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5` is
**not signable** and is not made signable here. It becomes signable only after a
bounded independent X-line and Y-line confirmation round on identical bytes,
performed by reviewers that did not author v2.3 through v2.8, and only jointly
with P1 operative composite v1.8 under the single atomic handoff of §A9.
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
      P1 operative composite versions 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 and 1.7,
      and versions 1, 1.1, 1.2, 1.3 and 1.4 of this amendment, are historical
      evidence only. NO implementer, verifier or reviewer opens any of them to
      determine behaviour or to verify a build.

DA-2  IMMUTABILITY ATTACHES TO DOCUMENTS, NOT TO PARAGRAPHS. There is no
      file-internal split by which some sections of a historical document remain
      operative while others are provenance. A cross-reference from one
      historical document to another does not reactivate either.

DA-3  THIS AMENDMENT DOES NOT EDIT HISTORY. It restates, in its own bytes, every
      peer rule that must be live. Their bytes remain exactly as committed.

DA-4  THE TWO LIVE SPECIFICATION SURFACES ARE EXACTLY TWO:
        this amendment (v1.5)               — peer-layer behaviour
        P1 operative composite v1.8         — P1 interface, execution, writer,
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
      same bytes are carried identically in **composite v1.8 §P1-14.8 and
      §P1-14.4**. **v1's `H-4`, which deferred the full list to a closure, is
      WITHDRAWN.** No closure adds, removes or reorders a step.
```

### §A0.3 What v1.5 adds, and why

```text
v1.4 WAS CONFIRMED BY THE INDEPENDENT X LINE FOR AUTHOR SELECTION, with NO
blocking and NO major finding. That line reproduced the fourteen-row bootstrap
closure FROM SCRATCH on the pinned interpreter and reported no difference in any
row, kind, transitive-import array or boolean, and reproduced the canonical
length and digest. THOSE FOURTEEN ROWS ARE CARRIED FORWARD BYTE-IDENTICALLY AT
MS-11.1 AND ARE NOT REOPENED.

THE Y LINE RETURNED REVISE ON THREE BLOCKING DEFECTS AND ONE REPOSITORY-STATE
CORRECTION. v1.5 repairs exactly those four and nothing else.

  Y27-B1  THE PRECEDENCE ORDER WAS NOT TOTAL. VP-3's table and VP-4's ordering
          did not make the first failure single-valued for MULTI-FAULT states,
          because ORDERING A PREDICATE IS NOT THE SAME AS CREATING THE OBJECT IT
          READS.
          (a) CK-2 ran A1..A17, including the M4-dependent A15, A16(a) and A17,
              BEFORE any check established that M4 exists, parses as JSON, is an
              object, or carries the required keys and types. On a valid Stage A
              with an absent or unparseable M4 one verifier could return
              STAGE_A_PRESELECTION_MISMATCH, another MEMBER_OMITTED, and a third
              had no specified mapping at all.
          (b) The install record is NOT one of the members, yet its structural
              validation lived inside the same check as the members' and VP-4
              ordered only the members. A malformed sole record together with an
              absent or stale member had two defensible first codes.
          (c) Two ownership duplications contradicted the exactly-one-owner
              claim: CK-7 was told to evaluate "every MS-12 relation" while VP-3
              assigned nine of those relations to CK-2, and CK-13 re-asserted an
              M2/M3 byte identity already fatal at CK-6.
          → TS-2 is SPLIT into TS-2A, clauses A1..A14, which read ONLY the
            Stage-A file, and TS-2B, clauses A15..A17, every one of which reads
            the manifest and which therefore runs only after M4 is present and
            structurally valid. VP-1 states S1..S8 with S1..S5 named as the
            PREREQUISITE SUB-PHASE. VP-4 is now a LITERAL TOPOLOGICAL ORDER of
            fifteen checks in which the record is located (CK-5), then
            structurally validated (CK-6), then the members are proved to exist
            and are hashed (CK-7), then M4 and M7 are structurally validated
            (CK-8), and only then does anything semantic run. CK-10 evaluates
            exactly the eleven MS-12 rows TS-2B does not own. The M2/M3 relation
            is owned once, at CK-7, where it raises HISTORICAL_BYTE_MOVED, and
            MEMBER_STALE is owned once, at CK-13. Six multi-fault states are
            named with their single first code, and rows 105, 106(d), 109, 111
            and 113 carry them as fixtures.

  Y27-B2  MS-11'S DENOTATION LEFT AN UNGUARDED ROLE-IMPORT ROUTE. v1.4 excluded
          src/philosophia/officina/generic_harness.py on the premise that it
          "runs under the nineteen-member global default in caller context".
          THIS CONTRACT SAYS THE OPPOSITE IN TWO OPERATIVE PLACES: §P1-3.2 gives
          that file its OWN scoped allowlist and a file with an entry gets
          EXACTLY that entry, and §P1-7.4 A-10 imports it INSIDE the SUPERVISOR,
          WATCHDOG, CONTROLLER and WORKER role bootstraps. root_source_sha256
          proves only which root bytes were installed; S-1..S-24b constrain root
          ASTs; neither enumerates the transitive modules executed during that
          role import, and the role path does not repeat P-c, P-d or P-g after
          A-10.
          → MS-11 is REDENOTED to the import-time closure of ALL THREE scoped
            allowlists and MS-11.1 carries the full EIGHTY-NINE-ROW value, with
            the fourteen confirmed bootstrap rows preserved exactly. The audit
            is stated at MS-11.3 as three independent derivations that agree.
            AND THE AUDIT FOUND A REAL DEFECT, WHICH IS WHY THIS IS NOT MERELY A
            LONGER LIST: with subprocess in that allowlist the closure contains
            threading, signal, select and selectors — four names §P1-3.2 itself
            calls permitted in no file — and threading's module-level code CALLS
            os.register_at_fork, in every role process including the WATCHDOG.
            MS-11.5 therefore REMOVES subprocess from that one scoped allowlist,
            reducing it from seventeen names to sixteen. THE REMOVAL IS NOT A NEW
            AUTHOR DECISION: S-12, test 8 and the future-edit surface already
            forbid subprocess on every path of that file, and an allowlist may
            not authorize an import that no conforming build may perform. After
            the reduction the closure contains no module that starts a task,
            registers an at-fork callback or installs a handler at import, and a
            runtime differential confirms it: no signal disposition changes, the
            live thread-frame count is 1 before and 1 after, and no trace or
            profile function is installed.

  Y27-B3  THE GRAPH STILL OMITTED AN EDGE. Stage B's selected_option_token must
          equal Stage A's, enforced at B14, and TR-2 lists an option mismatch
          between the two stages as a closed proper-subset case; but IR-4, the
          summaries and row 115 omitted it while calling the graph complete.
          → The edge Stage B --selected_option_token equality (B14)--> Stage A
            is added to IR-4, to composite §P1-14.5, to the packet summary and
            to row 115. IR-4 now states that it re-derives the graph over every
            relation bearing a PATH, a DIGEST, an ID, a SIGNATURE, AN OPTION
            TOKEN, a KEY or KEY ID, a MEMBER COUNT or an ASSERTION — v1.4
            derived over digest-, path- and signature-bearing fields only, which
            is exactly how an option-bearing relation escaped it. A9's
            intra-object pairing inside Stage A is named as deliberately not an
            edge, so its absence cannot be mistaken for a second omission.

  Y27-R   REPOSITORY STATE WAS STATED WRONGLY. v1.4 said "two of the five
          production roots do not exist". At the reviewed commit only
          scripts/officina_activate_t.py and scripts/verify_officina_active.py
          are tracked; BOTH bootstraps AND generic_harness.py are absent, so
          THREE of five are absent and TWO exist. A file named
          generic_harness.py exists only as unrelated untracked work in the live
          worktree; it is not evidence, is not governing, is not adopted and is
          not edited.
          → Corrected at MS-11.3, MS-11.6, composite §P1-18 and the packet.
            MS-11.6 additionally states that MS-11.1 is a PROSPECTIVE
            CONFORMANCE CONSTRAINT and is not evidence that an implementation
            exists.

ALSO PRESERVED, EXPLICITLY: the §A0.4 anchor as an honest acyclic cross-file
commitment and not a freshness claim; the fourteen confirmed bootstrap rows;
M4's peer and pre-selection anchors and the rollback-qualified digest language of
the composite preamble, G-6 and G-7; FS-1..FS-5; the two-clause TR-2 including
complete coherent rollback; row 106(i)'s expected PASS;
PROCEDURE_VIOLATION_OBSERVED; and the stated ABSENCE of any external freshness,
monotonicity, recency or rollback-resistance property. NO HARDWARE SECURITY
MODULE, EXTERNAL SERVICE, TIMESTAMP ORACLE, NOTARY, TRANSPARENCY LOG,
MONOTONIC-COUNTER DEVICE OR NEW SCIENTIFIC GATE IS ADDED, PERMITTED OR IMPLIED.
W-A and W-B behaviour, symmetry and recommendation are byte-preserved and
NEITHER IS SELECTED.

ALSO RECORDED, AND NOT AN AUTHORITY HERE: Kirill signed the P1 process-claim
identity selection, Option A, on 2026-08-04. XS-1 records its path and digest and
states that it accepts P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 not at all,
that it is a member of no class, that it is not scientific evidence, and that it
makes nothing here operative. NOTHING IN v1.5 ACCEPTS THAT TOKEN OR ANY BOUNDED
WEAKENING OF THE IDENTITY OBSERVATION UNDER ANY NAME.

NOTHING ELSE CHANGED. Every rule of v1.4 not named above — QC, FD, AK, PUB, RF,
TO, F, KW, FB, NS, WA, TIMING, DA, the §A5 conjuncts, ROUTE-D and ROUTE-W, the
swap-only state machine and every negative destination — is carried forward here
unchanged in substance. NO WATCHDOG MECHANISM, EVIDENCE CLASS, TREATMENT,
SCIENTIFIC CELL OR AUTHOR OPTION IS ADDED, REMOVED OR MOVED, AND NO AUTHOR CELL
IS OPENED. The two-stage authentication remains PROCESS INTEGRITY ONLY.
```

### §A0.4 The pre-selection composite anchor — one line, and why it is here

**This subsection exists because of one physical fact and one prohibition.**
`OR-4` resolves every variant block in the composite and deletes the branch that
was not signed, so the composite bytes the independent X and Y lines reviewed —
the PRE-SELECTION bytes — **exist nowhere on disk after `OR-4`** and can be
recomputed by no one. And a file cannot carry its own digest without a fixed
point, which `§P1-14.5` forbids and which is impossible in any case. So the one
pre-selection digest that can be neither recomputed nor self-declared is
anchored **here**, in the other governing file, whose own bytes are pinned by
`peer_amendment_sha256`, by `M1` membership in the install record, and through
`install_record_id` by the Stage-B signature.

The anchor is **exactly one line** of this file. `TS-2B` `A16(d)` states the
extraction rule: the whole line, after stripping a trailing `0x0A` and with no
other leading or trailing byte, is the token
`P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256`, then one `0x20`, one `0x3D`,
one `0x20`, then exactly 64 characters each one of `0123456789abcdef`. **The
count of lines matching that grammar in this file must be exactly one**; zero
and two or more both fail closed with `STAGE_A_PRESELECTION_MISMATCH`, exactly
as the composite's sentinel-cardinality rule fails. A mention of the token in
prose that is not followed by that exact separator and exactly 64 hexadecimal
characters is not an anchor line and is not counted — which is why the token may
be, and is, named in prose here and in the joint block without disturbing the
count.

The anchor line, and it is the only one in this file:

```text
P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256 = 6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176
```

**What this anchor is not.** It is not a freshness property, not a monotonic
counter, not an external witness and not a rollback defence. `TR-2(b)` is
unchanged by it: under a complete coherent rollback of an entire earlier
generation this amendment, this line, the packet, the manifest, Stage A, Stage
B, the detached signature and the sole install record are all restored together,
every clause passes on the restored bytes, and nothing refuses. The anchor
closes exactly one PROPER-SUBSET case — a pre-selection composite digest that
Stage A and the manifest agree on and that matches the reviewed bytes of no
generation — and it closes nothing else.

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
      composite v1.8 §P1-2 as 60_000_000_000 (60 s) and is NOT restated here.
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
COMPLETE and is stated IDENTICALLY in composite v1.8 §P1-14.8; its ordered steps
are `OR-1` through `OR-11` of §A10 below, which composite v1.8 carries
byte-identically at §P1-14.4. Neither copy defers to a closure, and no closure
adds a step.**

**The cross-reference audit, re-run on the v2.8 pair and stated so that a
reviewer can re-run it mechanically:**

- composite v1.8's highest numbered section is §P1-18, and composite v1.8
  contains the string `P1-19` **zero** times. The v1.1 amendment's locator
  "composite v1.4 §P1-19" named a section that never existed; it was corrected
  in v1.2 and the string survives in this amendment only inside this audit note,
  where it identifies the withdrawn locator, and as a locator nowhere;
- every `§P1-…` reference in this amendment names a section that exists as a
  heading in composite v1.8: §P1-2, §P1-3.1, §P1-3.2, §P1-3.3, §P1-7.1, §P1-7.2,
  §P1-7.4, §P1-12.4, §P1-13.2, §P1-14.4, §P1-14.6, §P1-14.8 and §P1-18;
- every `§A…` reference in composite v1.8 names a section that exists as a
  heading in this amendment: §A0.4, §A2, §A9 and §A10;
- no reference in either file names a section the other does not have, and no
  reference in either file names a version of the other that is not the version
  it is jointly accepted with.

```text
H-1  ONE UNIT. The v1.5 amendment and composite v1.8 are ONE indivisible
     acceptance unit. Neither is operative alone. Accepting one without the
     other is NOT a conforming state and NOT a partial success. THE v1.4
     AMENDMENT AND COMPOSITE v1.7 ARE WHOLLY REPLACED, not amended, and every
     earlier amendment and composite remains wholly replaced.

H-2  THE ORDERED STEPS ARE `OR-1` THROUGH `OR-11` OF §A10, STATED THERE IN FULL,
     AND THEY ARE NOT RESTATED IN A SECOND FORM ANYWHERE. There is exactly ONE
     statement of the ordering in these governing bytes, carried
     byte-identically in this file and in composite v1.8 §P1-14.4, so no two
     statements of it can disagree.
     THE ORDER IS A MANDATORY OPERATOR OBLIGATION, NOT A VERIFIED PROPERTY.
     `OR-1` and `FS-3` state the obligation; `FS-2` states that the final-state
     gate cannot distinguish identical final bytes produced in a forbidden
     order and withdraws every version-1.2 sentence that claimed otherwise,
     and version 1.4 narrows none of that;
     `FS-4` fails closed when a violation is observed while it occurs; `FS-5`
     places an unobserved violation inside the residual of `TR-2`.
     ALL STEPS LAND TOGETHER OR NONE DOES.

H-3  NO PARTIAL LANDING IS CONFORMING OR OPERATIVE. §A10's pre-production check
     is the enforcement point, it is `CK-1`..`CK-12`, and it runs before any
     production entry point. Composite v1.6 guard `G-11` is the same check
     stated on the P1 side; THE TWO ARE ONE RULE WITH TWO STATEMENTS and the
     normative block is byte-identical in both files.
     A partial landing that is STILL PARTIAL when the gate runs is refused by a
     named check whose code `VP-3` makes single-valued and whose position
     `VP-4` fixes topologically. A violation of ORDER that nevertheless leaves the exact valid
     final bytes is a governance violation the gate cannot see, and `FS-2` says
     so rather than pretending otherwise.

H-4  EXISTING HISTORY REMAINS BYTE-IDENTICAL. Zero historical bytes are edited
     by any step of `OR-1`..`OR-11`. `OR-11` and `CK-12` verify this and refuse
     on any difference with HISTORICAL_BYTE_MOVED.
```

---

## §A10. The install record and the two-stage author authorization

**Closes `Y23-5.3`, the v2.4 Y findings `Y24-1`..`Y24-3`, the v2.5 Y findings
`Y25-1`..`Y25-3`, the v2.6 Y findings `Y26-B1`..`Y26-B4`, and the v2.7 Y
findings `Y27-B1` (the precedence order was not total), `Y27-B2` (MS-11's
denotation left the role import surface of generic_harness.py unguarded) and
`Y27-B3` (the graph still omitted the B14 option edge), together with the v2.7
repository-state correction and the v2.6 X LOW and INFO notes.**

**THE NORMATIVE BLOCK BELOW IS CARRIED BYTE-IDENTICALLY AT §P1-14.4 `G-11` OF
COMPOSITE v1.8.** The install gate is ONE RULE WITH TWO STATEMENTS: this section
is the peer-layer statement and `G-11` is the P1 statement. A reviewer may
extract the two delimited spans and compare them directly; any difference
between them is a defect in this indivisible pair.

The block defines, in order: the canonical encoding (`MS-0`); the seven literal
member classes with exact cardinalities, paths, schemas, key sets, value
grammars and digest rules (`MS-1`..`MS-7`); the total member cardinality
(`MS-8`); the pairwise-disjointness proof (`MS-9`); the one `created_utc`
grammar and validator (`MS-10`); the one canonical eighty-nine-row
`reachable_closure` value covering the role import surface, with its audit
basis, its kind mapping, its derived booleans, the scoped-allowlist reduction it
depends on and its change rule (`MS-11`); the field-by-field semantic source of every manifest key (`MS-12`);
the install record's identity, path, schema and the complete directed integrity
graph (`IR-1`..`IR-12`); the two-stage author authorization with exhaustive
field-by-field verification algorithms (`TS-1`..`TS-6`); the mandatory
construction order, which is an operator obligation (`OR-1`..`OR-11`); the
structural and semantic validation phases with the total
relation-to-owner-to-code table and the literal topological predicate order
(`VP-1`..`VP-4`); the final-state pre-production check (`CK-1`..`CK-15`); the
closed failure-code set (`FC-1`); the exact boundary
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
        successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
        successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
      Both are taken in their POST-SELECTION bytes: the composite after every
      variant block has been resolved to the signed branch and the other
      branch deleted (OR-4), the amendment as installed. The digest of each is
      the SHA-256 of the whole file's bytes as found on disk, with no
      normalization and no exclusion of any region.
      NO OTHER PATH IS IN M1, AND NEITHER OF THESE TWO PATHS IS IN ANY OTHER
      CLASS.

MS-2  M2 IMMUTABLE PROVENANCE SET. CARDINALITY EXACTLY 51. THE LIST BELOW IS
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
        c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
        6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
        e334d7e4a93979f07a8d651a1dd32039027d0536e2d6259ae5a6ec36dc09a363  reviews/fable_officina_p1_watchdog_v2_6_independent_x_confirmation.md
        283666b75dc7fee8af7cde90ab761a734cc554aceca1f5b124c318d2ce8115b9  reviews/sol_officina_p1_watchdog_v2_6_final_y_confirmation.md
        f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md
        5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md
        4855020e522228eeb0625fba1efb78941bc547c124da2d1dbb754b548d3057cc  reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md
        0b33108e885fec97ab11e2de5c6ac3ba6ceeb8e98283bb29a09c70ce1c574780  reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md
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

      THE TABLE ABOVE IS THE STRUCTURAL PHASE AND IS NOT THE WHOLE PREDICATE.
      It fixes JSON types, lexical grammars and the two mandatory literals
      (schema, version) and NOTHING ELSE. EVERY OTHER VALUE ABOVE ALSO HAS A
      SEMANTIC SOURCE, and a value that is well typed but factually wrong is
      NOT admissible: MS-12 states the semantic source of every one of the
      twenty keys field by field, VP-3 names its single owning clause and its
      single failure code, and CK-9 and CK-10 evaluate them. Version 1.3 stated the
      types and left five of the twenty semantic relations unchecked; those
      five are peer_amendment_sha256, the three pre_selection_*_sha256 values
      and reachable_closure, and MS-11, MS-12, CK-9 and CK-10 close all five.

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
      THE SHAPE ABOVE IS NOT THE VALUE, AND VERSION 1.3 PINNED ONLY THE SHAPE.
      A structurally valid, internally closed, sorted array whose modules,
      kinds, transitive imports or booleans are factually wrong satisfied every
      version-1.3 rule. MS-11 fixes THE ONE CANONICAL EXPECTED VALUE, literally
      and completely, and CK-7 requires equality with it.

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
        M1 2 + M2 51 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 65
      The install record's member list has exactly 65 entries. A list of any
      other length fails before a single digest is compared.

MS-9  PAIRWISE DISJOINTNESS, PROVED BY PATH RATHER THAN ASSERTED.
      Every member is identified by one repository-relative path. Two classes
      are disjoint if and only if their path sets share no element. Write
      P(Mi) for the path set of class Mi:
        P(M1) the two literal strings of MS-1
        P(M2) the 51 literal strings of MS-2
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
          60 literal strings above.
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
          M1 against M2: M1's two strings end in _V1_5_DRAFT.md and
          _COMPOSITE_V1_8.md. MS-2's list carries the amendment at
          _V1_DRAFT.md, _V1_1_DRAFT.md, _V1_2_DRAFT.md, _V1_3_DRAFT.md and
          _V1_4_DRAFT.md, and the composite at _V1, _V1_1, _V1_2, _V1_3, _V1_4,
          _V1_5, _V1_6 and _V1_7, and carries no _V1_5_DRAFT amendment and no
          _V1_8 composite. Disjoint.
          M1 against M3: MS-3's seven strings are the harness contract chain,
          the harness signature and the batch-settlement amendment v1.1.1;
          none is an amendment-v1.5 or composite-v1.8 path. Disjoint.
          M2 against M3: MS-2 and MS-3 are two literal lists, and the
          intersection of the 51 strings with the 7 strings is empty.
      Twelve plus six plus three is twenty-one, so every pair is settled. The
      union of the seven sets has 2+51+7+1+1+2+1 = 65 distinct paths, equal to
      MS-8, so no path is counted twice and no member is unassigned. THE SEVEN
      CLASSES ARE PAIRWISE DISJOINT AND THEIR UNION IS THE COMPLETE INSTALLED
      SET. There is no eighth class.
      THE PACKET IS NOT A MEMBER AND DOES NOT DISTURB THIS PROOF. TS-2 A16(b)
      recomputes the SHA-256 of the bytes at TS-1's literal packet path. That
      path is in none of the seven literal lists above, it is added to none of
      them, and hashing a file is not making it a member (IR-12, N-14). CK-4
      still enumerates 65 members from MS-1..MS-7 alone.

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

MS-11 THE CANONICAL reachable_closure VALUE — LITERAL, COMPLETE, AND THE ONLY
      ADMISSIBLE ONE. This closes the content, not merely the shape, and in
      version 1.5 it closes the ROLE import surface as well.

      WHAT THE FIELD DENOTES, RESTATED AND WIDENED. reachable_closure is the set
      of Python modules resident, by direct or transitive module-scope import,
      in a ROLE PROCESS of this contract at the instant §P1-7.4 `A-10` returns,
      on the platform of §P1-2.1 under the launch of §P1-7.1, together with the
      three audited per-module properties. It is the import-time closure of the
      union of THREE literal scoped allowlists of §P1-3.2:
        scripts/officina_process_control_bootstrap.py  os sys _signal time
                                                       fcntl _socket
        scripts/officina_role_bootstrap.py             os sys fcntl
        src/philosophia/officina/generic_harness.py    the sixteen names of
                                                       MS-11.5, after the
                                                       reduction stated there
      THE UNION OF THE THREE DIRECT SETS IS EIGHTEEN NAMES.

      WHY generic_harness.py IS INCLUDED, AND WHY VERSION 1.4 WAS WRONG TO
      EXCLUDE IT. Version 1.4 said that root "runs under the nineteen-member
      global allowlist in the caller context". THAT STATEMENT IS WITHDRAWN AS
      FALSE OF THIS CONTRACT'S OWN OPERATIVE TEXT. §P1-3.2 gives
      generic_harness.py its OWN scoped entry, and a file with an entry gets
      EXACTLY that entry and never the union with the default; and §P1-7.4
      `A-10` imports philosophia.officina.generic_harness INSIDE the SUPERVISOR,
      WATCHDOG, CONTROLLER and WORKER role bootstraps, after the `A-9` sys.path
      replacement and before any pinned entry function runs. That module is
      therefore role code on every role path, and the import-time task, at-fork,
      handler, signal-state and origin effects of everything it pulls are
      directly material to the watchdog and control claims. root_source_sha256
      proves only WHICH ROOT BYTES were installed; `S-1`..`S-24b` constrain root
      ASTs and selected call and topology properties; NEITHER enumerates or pins
      the transitive standard-library modules executed during that role import,
      and the role path does not repeat `P-c`, `P-d` or `P-g` after `A-10`.

      WHAT IT STILL DOES NOT DENOTE, and the argument is stated accurately this
      time: it is NOT the closure of scripts/officina_activate_t.py or
      scripts/verify_officina_active.py. Those two execute ONLY in caller
      tooling — they are never imported by any role bootstrap, appear at no step
      of §P1-7.4, and hold no descriptor, handle, capability or lock of this
      contract. They are pinned by root_source_sha256 and by `S-1`..`S-24b`, and
      they take the nineteen-member global default of §P1-3.2 because neither
      has a scoped entry. NO CLOSURE CLAIM IS MADE FOR THEM AND NONE IS NEEDED,
      because no process that this contract creates ever imports them.

      THE KIND MAPPING, EXACT AND TOTAL. kind records the module's IMPORT-SYSTEM
      ORIGIN on the pinned interpreter build, and nothing else:
        BUILTIN      the module is compiled into the interpreter binary and is
                     listed in sys.builtin_module_names; its import-system
                     origin is the exact string "built-in"
        FROZEN       the module's code object is frozen into the interpreter
                     binary; its origin is the exact string "frozen". A .py
                     file of the same name may also exist on disk; it is NOT
                     what is loaded, and its presence does not make the module
                     PURE_PYTHON
        EXTENSION    the origin is a filesystem path whose final component ends
                     in the platform's dynamic-extension suffix
        PURE_PYTHON  the origin is a filesystem path whose final component ends
                     in ".py"
      The four are mutually exclusive and, on the pinned build, total over the
      closure. ALL FOUR ARE NOW IN USE. §P1-3.3's human vocabulary is NOT the
      kind vocabulary: "built-in" there means BUILTIN here, and os's "Python
      wrapper over built-in posix" describes its implementation and delegation,
      not its load origin, which on the pinned build is FROZEN.

      THE transitive_imports RULE, EXACT. transitive_imports is the TRANSITIVE
      closure of module-scope import EDGES THAT ARE ACTUALLY EXECUTED on the
      pinned build, EXCLUDING the element's own module name. An import written
      inside a function body, a method body or a class body is NOT a module-scope
      import and is excluded; a module-scope import inside a branch that does not
      execute is excluded and is listed at MS-11.3. Import cycles are permitted
      and are resolved by the exclusion of self.
      A `from __future__ import ...` STATEMENT IS BOTH A COMPILER DIRECTIVE AND
      A REAL RUNTIME IMPORT of the ordinary module `__future__`, which is why
      `__future__` is row 1 and not an omission; the compiler directive it also
      carries has no import-time effect of any kind.

      THE THREE BOOLEANS, DERIVED AND PINNED. Each is true if and only if
      EXECUTING THE MODULE'S TOP-LEVEL CODE does the named thing:
        starts_task        creates a thread, a task, a process or an
                           interpreter-level concurrent execution context
        registers_at_fork  CALLS os.register_at_fork or any equivalent at-fork
                           registration. DEFINING such a function is not
                           calling it: os defines register_at_fork and never
                           calls it at import, so its value is false
        installs_handler   installs or replaces a process-wide signal handler,
                           an atexit hook, an audit hook, a trace or profile
                           function, an import hook or a sys hook
      INTERPRETER-STARTUP INITIALIZATION IS EXCLUDED BY DEFINITION. Whatever
      Py_Initialize does before any production root executes is not an
      import-time effect of any module below, and §P1-7.2 `P-g` governs
      inherited and startup signal state separately. IN THE CANONICAL VALUE ALL
      TWO HUNDRED AND SIXTY-SEVEN BOOLEANS ARE false. Their audit basis is
      MS-11.3, and `P-c`, `P-d` and `P-g` independently re-establish the
      corresponding runtime facts before any fork.

MS-11.1 THE CANONICAL VALUE. reachable_closure has EXACTLY the eighty-nine
      elements below, in exactly this order, with exactly these values. Every
      element's starts_task, registers_at_fork and installs_handler is the JSON
      literal false and is not repeated per row. Line wrapping inside a
      transitive_imports cell is presentation only and introduces no element.

        #   module                          kind      transitive_imports
        1   __future__                      PURE_PYTHON (empty)
        2   _abc                            BUILTIN   (empty)
        3   _ast                            BUILTIN   (empty)
        4   _blake2                         BUILTIN   (empty)
        5   _codecs                         BUILTIN   (empty)
        6   _collections                    BUILTIN   (empty)
        7   _collections_abc                FROZEN    _abc abc sys
        8   _datetime                       BUILTIN   (empty)
        9   _frozen_importlib               FROZEN    (empty)
       10   _frozen_importlib_external      FROZEN    _imp _io _warnings marshal posix sys
       11   _functools                      BUILTIN   (empty)
       12   _hashlib                        EXTENSION (empty)
       13   _imp                            BUILTIN   (empty)
       14   _io                             BUILTIN   (empty)
       15   _json                           EXTENSION (empty)
       16   _opcode                         BUILTIN   (empty)
       17   _operator                       BUILTIN   (empty)
       18   _signal                         BUILTIN   (empty)
       19   _socket                         BUILTIN   (empty)
       20   _sre                            BUILTIN   (empty)
       21   _stat                           BUILTIN   (empty)
       22   _thread                         BUILTIN   (empty)
       23   _tokenize                       BUILTIN   (empty)
       24   _typing                         BUILTIN   (empty)
       25   _warnings                       BUILTIN   (empty)
       26   _weakref                        BUILTIN   (empty)
       27   _weakrefset                     PURE_PYTHON _weakref sys types
       28   abc                             FROZEN    _abc
       29   ast                             PURE_PYTHON _abc _ast _collections _collections_abc _functools _operator
                                                        _sre _stat _thread _weakref abc builtins collections
                                                        contextlib copyreg enum functools genericpath itertools
                                                        keyword operator os posix posixpath re re._casefix
                                                        re._compiler re._constants re._parser reprlib stat sys types
       30   builtins                        BUILTIN   (empty)
       31   codecs                          FROZEN    _codecs builtins encodings encodings.aliases sys
       32   collections                     PURE_PYTHON _abc _collections _collections_abc _operator _thread
                                                        _weakref abc builtins itertools keyword operator reprlib sys
       33   collections.abc                 PURE_PYTHON _abc _collections_abc abc sys
       34   contextlib                      PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _stat _thread _weakref abc builtins collections functools
                                                        genericpath itertools keyword operator os posix posixpath
                                                        reprlib stat sys types
       35   copy                            PURE_PYTHON _abc _collections_abc _weakref _weakrefset abc copyreg
                                                        itertools sys types weakref
       36   copyreg                         PURE_PYTHON (empty)
       37   dataclasses                     PURE_PYTHON _abc _ast _codecs _collections _collections_abc
                                                        _frozen_importlib _frozen_importlib_external _functools _imp
                                                        _io _opcode _operator _sre _stat _thread _tokenize _warnings
                                                        _weakref _weakrefset abc ast builtins codecs collections
                                                        collections.abc contextlib copy copyreg dis encodings
                                                        encodings.aliases enum functools genericpath importlib
                                                        importlib.machinery inspect io itertools keyword linecache
                                                        marshal opcode operator os posix posixpath re re._casefix
                                                        re._compiler re._constants re._parser reprlib stat sys token
                                                        tokenize types warnings weakref
       38   datetime                        PURE_PYTHON _datetime
       39   dis                             PURE_PYTHON _abc _collections _collections_abc _io _opcode _operator
                                                        _thread _weakref abc builtins collections io itertools
                                                        keyword opcode operator reprlib sys types
       40   encodings                       PURE_PYTHON _codecs builtins codecs encodings.aliases sys
       41   encodings.aliases               PURE_PYTHON (empty)
       42   encodings.utf_8                 PURE_PYTHON _codecs builtins codecs encodings encodings.aliases sys
       43   enum                            PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections functools
                                                        itertools keyword operator reprlib sys types
       44   errno                           BUILTIN   (empty)
       45   fcntl                           BUILTIN   (empty)
       46   fnmatch                         PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _stat _thread _weakref abc builtins collections copyreg enum
                                                        functools genericpath itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types
       47   functools                       PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections itertools keyword
                                                        operator reprlib sys types
       48   genericpath                     FROZEN    _abc _collections_abc _stat abc os posix posixpath stat sys
       49   hashlib                         PURE_PYTHON _hashlib
       50   hmac                            PURE_PYTHON _hashlib _operator _warnings hashlib sys warnings
       51   importlib                       PURE_PYTHON _frozen_importlib _frozen_importlib_external _imp _io
                                                        _warnings marshal posix sys warnings
       52   importlib.machinery             FROZEN    _frozen_importlib _frozen_importlib_external _imp _io
                                                      _warnings importlib marshal posix sys warnings
       53   inspect                         PURE_PYTHON _abc _ast _codecs _collections _collections_abc
                                                        _frozen_importlib _frozen_importlib_external _functools _imp
                                                        _io _opcode _operator _sre _stat _thread _tokenize _warnings
                                                        _weakref abc ast builtins codecs collections collections.abc
                                                        contextlib copyreg dis encodings encodings.aliases enum
                                                        functools genericpath importlib importlib.machinery io
                                                        itertools keyword linecache marshal opcode operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys token tokenize types warnings
       54   io                              FROZEN    _abc _io abc
       55   ipaddress                       PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections functools
                                                        itertools keyword operator reprlib sys types
       56   itertools                       BUILTIN   (empty)
       57   json                            PURE_PYTHON _abc _codecs _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins codecs
                                                        collections copyreg encodings encodings.aliases enum
                                                        functools itertools json.decoder json.encoder json.scanner
                                                        keyword operator re re._casefix re._compiler re._constants
                                                        re._parser reprlib sys types
       58   json.decoder                    PURE_PYTHON _abc _codecs _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins codecs
                                                        collections copyreg encodings encodings.aliases enum
                                                        functools itertools json json.encoder json.scanner keyword
                                                        operator re re._casefix re._compiler re._constants
                                                        re._parser reprlib sys types
       59   json.encoder                    PURE_PYTHON _abc _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins collections
                                                        copyreg enum functools itertools keyword operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types
       60   json.scanner                    PURE_PYTHON _abc _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins collections
                                                        copyreg enum functools itertools keyword operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types
       61   keyword                         PURE_PYTHON (empty)
       62   linecache                       PURE_PYTHON _abc _codecs _collections _collections_abc _functools _io
                                                        _operator _sre _stat _thread _tokenize _weakref abc builtins
                                                        codecs collections copyreg encodings encodings.aliases enum
                                                        functools genericpath io itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys token tokenize types
       63   marshal                         BUILTIN   (empty)
       64   math                            BUILTIN   (empty)
       65   ntpath                          FROZEN    _abc _collections_abc _stat abc genericpath os posix
                                                      posixpath stat sys
       66   opcode                          PURE_PYTHON _opcode
       67   operator                        PURE_PYTHON _operator builtins
       68   os                              FROZEN    _abc _collections_abc _stat abc genericpath posix posixpath
                                                      stat sys
       69   pathlib                         PURE_PYTHON _abc _collections _collections_abc _functools _io _operator
                                                        _sre _stat _thread _warnings _weakref abc builtins
                                                        collections copyreg enum errno fnmatch functools genericpath
                                                        io ipaddress itertools keyword math operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types urllib urllib.parse
                                                        warnings
       70   posix                           BUILTIN   (empty)
       71   posixpath                       FROZEN    _abc _collections_abc _stat abc genericpath os posix stat
                                                      sys
       72   re                              PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re._casefix
                                                        re._compiler re._constants re._parser reprlib sys types
       73   re._casefix                     PURE_PYTHON (empty)
       74   re._compiler                    PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re re._casefix
                                                        re._constants re._parser reprlib sys types
       75   re._constants                   PURE_PYTHON _sre
       76   re._parser                      PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re re._casefix
                                                        re._compiler re._constants reprlib sys types
       77   reprlib                         PURE_PYTHON _thread builtins itertools
       78   stat                            FROZEN    _stat
       79   sys                             BUILTIN   (empty)
       80   time                            BUILTIN   (empty)
       81   token                           PURE_PYTHON (empty)
       82   tokenize                        PURE_PYTHON _abc _codecs _collections _collections_abc _functools _io
                                                        _operator _sre _thread _tokenize _weakref abc builtins
                                                        codecs collections copyreg encodings encodings.aliases enum
                                                        functools io itertools keyword operator re re._casefix
                                                        re._compiler re._constants re._parser reprlib sys token
                                                        types
       83   types                           PURE_PYTHON sys
       84   typing                          PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _stat _thread _typing _warnings _weakref abc builtins
                                                        collections collections.abc contextlib copyreg enum
                                                        functools genericpath itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types warnings
       85   urllib                          PURE_PYTHON (empty)
       86   urllib.parse                    PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _warnings _weakref abc builtins collections copyreg
                                                        enum functools ipaddress itertools keyword math operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types warnings
       87   warnings                        PURE_PYTHON _warnings sys
       88   weakref                         PURE_PYTHON _abc _collections_abc _weakref _weakrefset abc itertools sys
                                                        types
       89   zipimport                       FROZEN    _frozen_importlib _frozen_importlib_external _imp _io
                                                      _warnings marshal posix sys time

      CARDINALITY 89. KIND COUNTS: BUILTIN 29, FROZEN 13, EXTENSION 2,
      PURE_PYTHON 45. The 76 distinct names occurring in any transitive_imports
      are each themselves a module row, so the CLOSURE rule of MS-4 is satisfied
      BY THIS VALUE; 39 rows have an empty transitive_imports array.
      THE FOURTEEN-ROW BOOTSTRAP SUBSET OF VERSION 1.4 IS PRESERVED EXACTLY.
      Rows _abc, _collections_abc, _signal, _socket, _stat, abc, fcntl,
      genericpath, os, posix, posixpath, stat, sys and time carry the SAME kind
      and the SAME transitive_imports array, element for element, that the
      independent X line reproduced from scratch against version 1.4. Widening
      the denotation adds rows; it changes no confirmed row, because an
      element's transitive_imports depends only on that element's own outgoing
      edges, which no new root can alter.

MS-11.2 THE SCOPED-ALLOWLIST REDUCTION THIS VALUE DEPENDS ON — see MS-11.5.
      Without it the closure additionally contains subprocess, threading,
      signal, select, selectors, _posixsubprocess, locale and _locale, and
      threading's module-level code CALLS os.register_at_fork, which would make
      registers_at_fork TRUE for a module resident in every role process
      including the WATCHDOG. THE REDUCTION IS NOT COSMETIC AND IS NOT OPTIONAL.

MS-11.3 HOW EVERY ROW WAS AUDITED, AND AGAINST WHAT.
      THE AUDIT BASIS IS THREE MUTUALLY INDEPENDENT DERIVATIONS THAT AGREE, NONE
      OF WHICH IMPORTS, EXECUTES OR COMPILES ANY PHILOSOPHIA PRODUCTION MODULE —
      none of the five roots is opened for behaviour by the audit, and at the
      reviewed commit three of the five do not exist as tracked files:
        (a) RESIDENCY. In a fresh interpreter launched with the exact isolation
            flags of §P1-7.1 and an empty environment, the eighteen union
            allowlist names are imported and the resulting module table is
            recorded. This is the operative question — what is resident in a
            role process after A-10 — answered directly.
        (b) STATIC SOURCE AND CODE-OBJECT PARSE. For every resident module with
            a Python top-level code object, every module-scope IMPORT_NAME
            operand, its relative-import level and its fromlist are read from
            the code object ACTUALLY LOADED, resolving relative imports against
            the package. Function, method and class bodies are not descended
            into.
        (c) RUNTIME DIFFERENTIAL FOR THE BOOLEANS. Signal dispositions for every
            signal number, the live thread-frame count, sys.gettrace and
            sys.getprofile are sampled before and after the eighteen imports.
            RESULT: NO SIGNAL DISPOSITION CHANGED; THE THREAD-FRAME COUNT WAS 1
            BEFORE AND 1 AFTER; NO TRACE OR PROFILE FUNCTION WAS INSTALLED. A
            module-level scan for register_at_fork, start_new_thread, Thread,
            Popen, fork, posix_spawn, system, signal, setitimer, set_wakeup_fd,
            settrace, setprofile, addaudithook, excepthook, unraisablehook and
            atexit across all 89 top-level code objects returned ZERO hits.
      THREE NORMALIZATIONS ARE APPLIED, AND THEY ARE THE ONLY THREE:
        ALIAS ENTRIES. A module table key that denotes the SAME module object
          under a second name is not a second row. There are exactly three:
          os.path is posixpath, importlib._bootstrap is _frozen_importlib, and
          importlib._bootstrap_external is _frozen_importlib_external. The
          canonical name is the module's own spec name, which is why
          _collections_abc is a row under that name even though its __name__
          attribute is rebound to collections.abc.
        PSEUDO-MODULE ENTRIES. A module-table key whose value is not a module
          object is not a row. There are exactly two: typing.io and typing.re,
          which on the pinned build are deprecated class objects registered in
          the module table by typing.
        UNEXECUTED MODULE-SCOPE BRANCHES. Six, each with its reason:
          os --> nt          the Windows branch; the posix branch is taken
          os --> ntpath      the same Windows branch. ntpath IS a row, because
                             pathlib imports it unconditionally, but the edge
                             from os does not exist
          ntpath --> nt, _winapi                    Windows-only
          _frozen_importlib_external --> nt, winreg Windows-only
          abc --> _py_abc    the try importing _abc succeeds, so the except
                             branch never runs
          hashlib --> logging  reached only from an except ValueError handler
                             taken when a hash constructor is unavailable; on
                             the pinned build every constructor is available
      ONE DISCLOSURE, RECORDED RATHER THAN OMITTED. The module-level code of
      _collections_abc performs many calls to the abstract-base-class virtual
      subclass registration method, and io, collections, encodings, pathlib and
      weakref do the same. That is abstract-base-class bookkeeping inside those
      modules' own class objects. It is not an at-fork registration, not an
      atexit registration and not a handler installation.
      A SECOND DISCLOSURE, AND IT CORRECTS A RATIONALE IN §P1-3.2. The built-in
      module _thread is a row. It is reached by an executed edge from functools
      and from reprlib, AND IT IS ALSO RESIDENT BEFORE ANY CONTRACT IMPORT RUNS:
      on the pinned build the interpreter's own start-up module table already
      contains it. §P1-3.2's sentence explaining that signal is permitted in no
      file "because its import closure pulls functools and hence _thread" is
      therefore factually obsolete as a REASON. THE RULE IS UNCHANGED AND IS NOT
      WEAKENED: signal, threading, _thread, select, selectors, socket,
      multiprocessing, concurrent, asyncio, ctypes, array, struct, atexit and gc
      remain permitted in NO allowlist, and none of them is in any. What changes
      is only that no honest reader may now infer that _thread's absence from a
      process is achievable by an allowlist choice. Importing _thread starts no
      thread: its three booleans are false, and derivation (c) measured the
      thread-frame count as 1 before and 1 after.
      THE AUDITED BUILD:
        CPython 3.12.3, x86_64 Linux, GCC 13.3.0, build stamp
        "Python 3.12.3 (main, Jun 19 2026, 12:46:00)"
      on which fcntl and _socket are compiled into the interpreter binary rather
      than loaded as dynamic extensions, and on which 13 rows are frozen.
      THE LAUNCH FLAGS ARE ALREADY CLOSED: §P1-7.1's argv is the exact
      six-element vector -I -S -E -P with no -X option, the environment is empty,
      §P1-7.2 P-b reads the flags back, and test 1 is byte-exact on the argv, so
      the frozen-module set cannot be altered by an interpreter option.

MS-11.4 THE EQUALITY REQUIREMENT — VALUE, NOT SHAPE.
      M4's reachable_closure must EQUAL the value of MS-11.1 as a JSON value:
      the same eighty-nine elements, the same order, the same module strings,
      the same kind literals, the same transitive_imports arrays in the same
      order, and all 267 booleans false. A DIFFERENT VALUE THAT SATISFIES EVERY
      MS-4 SHAPE RULE IS REFUSED.
      THE MECHANICAL FORM OF THE CHECK, so that two implementations cannot
      differ: let CLOSURE_BYTES be CANON(M4.reachable_closure) as MS-0 defines
      CANON, INCLUDING its single trailing 0x0A byte. Then
        len(CLOSURE_BYTES) is exactly 20534, and
        SHA-256(CLOSURE_BYTES) is exactly
          aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee
      Both conjuncts are required, AND NEITHER REPLACES THE JSON-VALUE
      COMPARISON: the direct comparison with the MS-11.1 literal is the primary
      check and the length and digest are corroboration, so that the predicate
      does not rest on collision resistance alone. THIS IS NOT A SELF-HASH: it
      is the digest of a VALUE carried by a generated artifact, it appears in no
      file whose own digest it is, and no file below hashes itself.
      THE OWNING CLAUSE IS CK-10 AND THE CODE IS MANIFEST_VALUE_MISMATCH. A
      malformed closure — wrong JSON type, wrong element key set, unsorted,
      duplicated, or not closed under itself — is a STRUCTURAL failure, is owned
      earlier by CK-8, and is refused with MEMBER_SUBSTITUTED. The two cases
      never contend: VP-3 gives each exactly one owner.

MS-11.5 THE SCOPED-ALLOWLIST REDUCTION, STATED IN FULL WITH ITS AUTHORITY.
      §P1-3.2's scoped entry for src/philosophia/officina/generic_harness.py
      LOSES EXACTLY ONE NAME, subprocess, and gains none. It becomes the SIXTEEN
      names
        __future__ ast dataclasses datetime enum fcntl hashlib hmac json os
        pathlib re time typing weakref _socket
      THE REMOVED NAME AND THE REASON, and this is not a new author decision:
      THIS CONTRACT ALREADY FORBIDS subprocess IN THAT FILE, in three operative
      places that version 1.4's allowlist contradicted.
        `S-12` of §P1-14.6 CHANGE 3: "subprocess, Popen, fork, waitpid, kill,
          killpg and system appear on no path of generic_harness.py";
        test 8 of §P1-15: "the launcher performs no fork, no Popen, no
          preexec_fn and no shell, statically and dynamically";
        the future-edit surface row for that path: "removal of every subprocess,
          fork, wait, kill and group-kill call".
      A name that no conforming build may use cannot remain in the allowlist
      that authorizes its import. THE REDUCTION RECONCILES §P1-3.2 WITH RULES
      ALREADY IN THESE GOVERNING BYTES; it decides nothing new.
      WHAT IT REMOVES FROM THE CLOSURE, exactly eight modules: subprocess,
      threading, signal, select, selectors, _posixsubprocess, locale and
      _locale. FOUR OF THE EIGHT — threading, signal, select and selectors —
      are named by §P1-3.2 itself as permitted in no file, and version 1.4's
      denotation concealed the fact that they were transitively resident in
      every role process. threading's module-level code CALLS
      os.register_at_fork.
      WHAT IT DOES NOT TOUCH. The nineteen-member global default of §P1-3.2 is
      UNCHANGED and still contains subprocess, so scripts/officina_activate_t.py
      and scripts/verify_officina_active.py are unaffected. The two bootstrap
      scoped entries are UNCHANGED. No other allowlist, no other root and no
      other rule moves.
      WHAT IT COSTS THE FUTURE IMPLEMENTATION. Nothing that this contract does
      not already require: §P1-7.1 launches through the bound `_posix_spawn`
      primitive of §P1-3.4, never through subprocess, and `S-11`, `S-12` and
      test 8 already require exactly that. A build of generic_harness.py that
      imports subprocess was already nonconforming; after this reduction it is
      also outside the allowlist and is refused earlier.
      IT MOVES NO SCIENTIFIC CELL. It adds, removes and renames no watchdog
      option, treatment, evidence class, covariate, endpoint, qualification
      input, comparison input, Q fact or C fact; it is option-independent and
      identical under W-A and W-B; and it opens no author cell.

MS-11.6 A CHANGED GRAPH IS A NEW REVIEWED GENERATION, NEVER A RECOMPUTATION.
      If the standard library, the interpreter build, the allowlists of §P1-3.2
      or any production root changes so that any row of MS-11.1 becomes false,
      THE MANIFEST IS NOT SILENTLY REGENERATED AGAINST THE NEW GRAPH. MS-11.1 is
      a constant of these governing bytes; changing it changes M1, and a new M1
      requires a new independently reviewed generation of this pair, a new
      install record and a new Stage-B authorization. NO BUILD, SCRIPT, TEST OR
      VERIFIER MAY RECOMPUTE A DIFFERENT ACCEPTED VALUE AT INSTALL TIME. A
      verifier that derived the closure from the live interpreter and accepted
      whatever it found would defeat the check entirely and is expressly
      forbidden.
      THIS VALUE IS A PROSPECTIVE CONFORMANCE CONSTRAINT AND IS NOT EVIDENCE
      THAT AN IMPLEMENTATION EXISTS. At the reviewed commit three of the five
      production roots are absent as tracked files. The root-level import sets
      come from §P1-3.2's literal allowlists, not from files; the transitive
      edges, kinds and booleans are audited against the extant standard library
      and the pinned interpreter; and correspondence to the eventual root bytes
      is enforced later, by the scoped-allowlist rule, by root_source_sha256, by
      `S-1`..`S-24b`, by the matrix, by M7 and by CK-10 at install.

MS-12 THE M4 FIELD-BY-FIELD SEMANTIC SOURCE. Twenty keys, twenty sources. No
      key is satisfied by presence, by type, or by agreement with another copy
      of itself.
        KEY                            SEMANTIC SOURCE OF ITS VALUE
        schema                         the literal string at MS-4 (structural)
        version                        the integer 1 at MS-4 (structural)
        roots                          the five literal paths of §P1-3.1, in
                                       that section's order
        root_source_sha256             key set equal to those five paths; each
                                       value the SHA-256 of that root's bytes
                                       on disk (CHANGE 5)
        reachable_closure              the canonical value of MS-11.1, by the
                                       equality of MS-11.4
        p1_composite_sha256            H_FILE of the M1 composite on disk (G-7)
        p1_composite_body_sha256       H_BODY of the M1 composite (G-6)
        p1_composite_guarddata_sha256  H_GUARDDATA of the M1 composite (G-6)
        p1_composite_normative_sha256  H_NORMATIVE of the M1 composite (G-6)
        peer_amendment_sha256          the SHA-256 of the whole bytes of the M1
                                       AMENDMENT at MS-1's first literal path,
                                       recomputed from disk. IT IS NOT MERELY
                                       64 HEX CHARACTERS, and an arbitrary
                                       well-formed value does not pass. It must
                                       additionally equal Stage B's
                                       governing_amendment_sha256 (B18) and the
                                       manifest's own
                                       pre_selection_amendment_sha256
        pre_selection_packet_path      the literal packet path of TS-1
        pre_selection_packet_sha256    the SHA-256 of the whole bytes found at
                                       that literal path, recomputed from disk
        pre_selection_amendment_path   the literal amendment path of TS-1
        pre_selection_amendment_sha256 the SHA-256 of the whole bytes found at
                                       that literal path, recomputed from disk;
                                       equal to peer_amendment_sha256 because
                                       OR-4 does not change the amendment
        pre_selection_composite_path   the literal composite path of TS-1
        pre_selection_composite_sha256 THE ONE VALUE THAT CANNOT BE RECOMPUTED
                                       FROM ANY SURVIVING BYTES, and this is
                                       stated rather than disguised: it is the
                                       digest of the composite AS REVIEWED,
                                       before OR-4 deleted one branch of every
                                       variant block, and those bytes exist
                                       nowhere after OR-4. It is anchored
                                       instead to the PRE-SELECTION COMPOSITE
                                       ANCHOR LINE of §A0.4 of the M1
                                       amendment, whose own bytes are pinned by
                                       peer_amendment_sha256, by the install
                                       record and by Stage B's signature. The
                                       extraction rule is TS-2B A16(d). It is
                                       not a literal of the composite, because
                                       a file cannot carry its own digest
                                       (§P1-14.5, IR-4)
        stage_a_path                   TS-1's literal Stage-A path (A17)
        stage_a_sha256                 the SHA-256 of the Stage-A file (A17)
        stage_a_key_id                 Stage A's key_id (A17)
        created_utc                    MS-10 grammar and validator; compared
                                       with no other timestamp, orders nothing
      OWNERSHIP, AND VERSION 1.4'S DUPLICATION IS REMOVED. The six
      pre_selection_* rows and the three stage_a_* rows are owned by TS-2B,
      evaluated at CK-9, and CK-10 DOES NOT EVALUATE THEM. Version 1.4 told CK-7
      to evaluate "every MS-12 relation" while VP-3 assigned nine of them to
      CK-2; the two sentences contradicted each other. CK-10 now evaluates
      EXACTLY the eleven rows that TS-2B does not own, and VP-3 is the single
      authority on which is which.

IR-1  IDENTITY OF THE INSTALL RECORD.
        install_record_id = SHA-256( CANON( {
          "schema": "philosophia.officina.t-watchdog-authority-install-id.v1",
          "members": [ {"class": ..., "path": ..., "sha256": ...}, ... ]
        } ) )
      The preimage object has EXACTLY the two keys schema and members. "schema"
      is the STRING "philosophia.officina.t-watchdog-authority-install-id.v1",
      exactly. "members" is an ARRAY of exactly the 65 entries of MS-8. Each
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
        install_record_id  64-char lowercase hex STRING
        members            ARRAY of exactly 65 OBJECTS, each with EXACTLY the
                           three keys class, path and sha256 as IR-1 defines
                           them, IN IR-1's ORDER
        created_utc        STRING satisfying MS-10
      THE ABOVE IS THE STRUCTURAL PHASE ONLY. VERSION 1.3 ALSO WROTE INTO THIS
      VALUE GRAMMAR that install_record_id equals the IR-1 digest of the
      object's own members array and equals the filename stem. THAT SENTENCE IS
      WITHDRAWN FROM THE GRAMMAR — not from the gate. Those two equalities are
      SEMANTIC, CROSS-OBJECT relations; they are owned by CK-8 and CK-9 and are
      refused with INSTALL_RECORD_NAME_MISMATCH, exactly as test row 105
expects. Version 1.3 made them part of a value grammar that a single
      structural check was told to enforce with MEMBER_SUBSTITUTED, so two
      conforming verifiers could return different first codes for one record;
      VP-1, VP-2 and VP-3 remove that ambiguity. Equality of the record's
      members array with the enumerated set is likewise semantic and is owned
      by CK-13.
      THE RECORD IS NOT A MEMBER, AND VERSION 1.4 LEFT ITS STRUCTURAL POSITION
      UNSTATED. It is structurally validated at CK-6, which runs AFTER CK-5 has
      established that exactly one record exists and BEFORE any member is
      touched at CK-7. VP-4 states that order literally and VP-3 gives every
      record field its single owner.
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
      VERSION 1.3 THEN CALLED ITS OWN GRAPH COMPLETE WHILE OMITTING THREE REAL
      EDGES. Stage A's governing_pre_selection carries a path and a digest for
      the packet, the amendment and the composite; those are three directed
      integrity edges from Stage A, parallel to M4's three, and neither IR-4,
      nor the packet's summary, nor §P1-14.5, nor row 115 listed them. They are
      added below. A fourth edge, from the M1 amendment's anchor line to the
      pre-selection composite bytes, is new in version 1.4 and is listed too.
      THE ACTUAL GRAPH, COMPLETE, with every edge labelled by what it binds:
        install record  --digest-->  each of the 65 members
                                     (M1 2, M2 51, M3 7, M4 1, M5 1, M6 2, M7 1)
        M4 manifest     --digest-->  the M1 composite, by p1_composite_sha256
                        --digest-->  the M1 amendment, by peer_amendment_sha256.
                                     THIS EDGE WAS CLAIMED IN VERSION 1.3 AND
                                     ENFORCED BY NOTHING; MS-12 and CK-10 make it
                                     real
                        --digest-->  the five production roots
                        --digest-->  the three composite region digests and the
                                     composite file digest
                        --path+digest-->  the three pre-selection inputs
                        --path+digest+key id-->  Stage A
        Stage A         --path+digest-->  the pre-selection packet
                        --path+digest-->  the pre-selection amendment
                        --path+digest-->  the pre-selection composite
                                     (THE THREE EDGES VERSION 1.3 OMITTED)
                        --key pin-->  the one key under which Stage B verifies
        M1 amendment    --anchor line digest-->  the pre-selection composite
                                     bytes, per §A0.4 and TS-2 A16(d)
        M7 attestation  --digest-->  M5
                        --digest-->  each of the two M6 modules
                        --digest-->  the M6 canonical bundle digest
                        --assertion-->  that the matrix ran and every row of
                                     92..115 passed
        Stage B         --path+digest+key id-->  Stage A
                        --selected_option_token equality (B14)-->  Stage A
                                     (THE EDGE VERSION 1.4 OMITTED. It is the
                                     link that makes the option token inside the
                                     SIGNED Stage-B bytes agree with the option
                                     the author selected in Stage A, and TR-2
                                     lists an option mismatch between the two
                                     stages as a closed proper-subset case. A
                                     graph that carries the key pin, the member
                                     count and the M7 assertions cannot exclude
                                     an option equality and still call itself
                                     complete.)
                        --id+path+count-->  the install record and the member set
                        --digest-->  the two M1 members
        detached sig    --Ed25519-->  the exact canonical Stage-B bytes
      THE GRAPH ABOVE WAS RE-DERIVED EDGE BY EDGE FROM EVERY RELATION OF MS-4,
      MS-7, IR-1, IR-3, TS-1, TS-3 AND TS-4 THAT BEARS A PATH, A DIGEST, AN ID,
      A SIGNATURE, AN OPTION TOKEN, A KEY OR KEY ID, A MEMBER COUNT OR AN
      ASSERTION, AND NO SUCH RELATION OF THOSE SEVEN IS LEFT WITHOUT AN EDGE.
      Version 1.4 derived over digest-, path- and signature-bearing fields only,
      which is exactly why the option-bearing B14 relation escaped it. That
      derivation, not an assertion, is why the graph is called complete.
      ONE RELATION IS DELIBERATELY NOT AN EDGE AND IS NAMED SO THAT ITS ABSENCE
      IS NOT MISTAKEN FOR AN OMISSION: A9's pairing of Stage A's
      selected_option_amendment_token with its own selected_option_token is an
      INTRA-OBJECT consistency constraint inside Stage A, not a relation between
      two objects, so it is a clause of TS-2A and not an edge of this graph.
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

IR-9  THE CHECK is exactly CK-2 through CK-15, executed in that order,
      fail-closed at the first failure. THE MEMBER ENUMERATION IS CK-4 AND
      DRAWS ONLY ON MS-1..MS-7. The checks are partitioned into the two phases
      of VP-1 and VP-2; VP-3 gives every field and every cross-object relation
      of every generated object exactly one owning clause and exactly one code;
      and VP-4 states the literal topological order in which the prerequisites
      of every predicate are established before that predicate runs.

IR-10 FAIL-CLOSED RECOVERY is exactly FC-1.

IR-11 MIXED GENERATIONS ARE REJECTED BY CONSTRUCTION. MS-1 names two literal
      paths. The v1.4 amendment installed with composite v1.8, the v1.5
      amendment installed with composite v1.7, and any other mixture of a
      v2.7-era with a v2.8-era governing file, leave one of MS-1's two literal
      paths absent or carrying bytes that produce a different digest, so the
      set fails at CK-7 or CK-13 and, if a record is rebuilt around the
      mixture, at B15 of TS-5.

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
                         successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md
                       amendment
                         successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
                       composite
                         successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
                     THE THREE sha256 VALUES ARE THE PRE-SELECTION DIGESTS:
                     the bytes the independent X and Y lines confirmed BEFORE
                     any variant block was resolved. The amendment path and the
                     composite path are the same literal strings as MS-1's two
                     paths, but the composite's PRE-SELECTION digest is not its
                     M1 digest, because OR-4 changes the composite's bytes; the
                     amendment's two digests are equal only because OR-4 does
                     not change the amendment.
                     EACH OF THE THREE HAS AN EXTERNAL ANCHOR, AND VERSION 1.3
                     HAD NONE. Version 1.3 required only that Stage A's three
                     digests equal the manifest's three, so a coordinated
                     arbitrary triple written into both artifacts passed. TS-2
                     A16, now a clause of TS-2B, requires each of the three to
                     equal a value derived from named repository bytes at
                     validation time:
                     A16(b) recomputes the packet digest from the bytes at the
                     literal packet path; A16(c) recomputes the amendment
                     digest from the bytes at the literal amendment path; and
                     A16(d) reads the composite's pre-selection digest from the
                     unique anchor line of §A0.4 of the M1 amendment, because
                     the pre-selection composite bytes do not survive OR-4 and
                     no file may carry its own digest. EQUALITY OF STAGE A WITH
                     M4 ALONE IS NO LONGER SUFFICIENT FOR ANY OF THE THREE.
        threat_model STRING equal, byte for byte, to the exact string quoted
                     at TR-2
        created_utc  STRING satisfying MS-10

      STAGE A IS CREATED ONLY AFTER KIRILL HAS EMITTED ONE EXPLICIT OPTION
      TOKEN. NEITHER THE KEY PAIR, NOR THE ENTROPY THAT PRODUCES IT, NOR THIS
      ARTIFACT IS AUTHORIZED BY THE DRAFTING ROUND THAT PRODUCED THESE BYTES.

TS-2  STAGE A VERIFICATION — AN EXHAUSTIVE FIELD-BY-FIELD ALGORITHM IN TWO
      STAGES, SPLIT BY WHAT EACH CLAUSE IS ALLOWED TO READ. EVERY MANDATORY
      LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS SATISFIED BY
      MERE PRESENCE. Each stage is executed in the order written, fail-closed at
      the first failure.
      TS-2A, THE SELF-CONTAINED STAGE, clauses A1..A14. IT READS ONLY THE
        STAGE-A FILE AND THE LITERAL CONSTANTS OF THESE GOVERNING BYTES. It
        reads no manifest, no member, no record and no Stage-B artifact, so
        every prerequisite it needs is a constant or a byte it has itself
        validated. It is evaluable from OR-3 onward and is evaluated at CK-2.
      TS-2B, THE M4-DEPENDENT STAGE, clauses A15..A17. EVERY CLAUSE OF THIS
        STAGE READS THE M4 MANIFEST. IT MAY THEREFORE RUN ONLY AFTER M4 HAS BEEN
        PROVED TO EXIST, TO PARSE AS JSON, TO BE AN OBJECT, TO CARRY EXACTLY
        MS-4's KEY SET WITH EXACTLY MS-4's TYPES, AND TO SATISFY EVERY
        STRUCTURAL PREDICATE OF VP-1. It is evaluable from OR-7 onward and is
        evaluated at CK-9, which VP-4 places after CK-7 and CK-8.
      WHY THE SPLIT EXISTS, STATED PLAINLY. Version 1.4 ran A1..A17 as one stage
      at CK-2, BEFORE any check had established that M4 exists or parses. A15,
      A16(a) and A17 read manifest fields, so on a state with a valid Stage A
      and an absent, unparseable, non-object or missing-key M4 those clauses had
      no defined value to read: one implementation could map the failed read to
      STAGE_A_PRESELECTION_MISMATCH, another could defer to the member checks
      and return MEMBER_OMITTED, and a third had no specified mapping at all.
      ORDERING PREDICATES IS NOT THE SAME AS CREATING THE OBJECT THEY NEED. The
      split creates it. NO CLAUSE OF TS-2B MAY READ AN ABSENT, INVALID-JSON,
      NON-OBJECT, MISSING-KEY OR WRONGLY TYPED M4, because every one of those
      states is fatal at CK-7 or CK-8 with its own single code before TS-2B is
      reached.
      --- TS-2A, SELF-CONTAINED: READS ONLY THE STAGE-A FILE ---
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
      --- TS-2B, M4-DEPENDENT: EVERY CLAUSE BELOW READS THE MANIFEST, AND
          RUNS ONLY AFTER CK-7 AND CK-8 HAVE PROVED M4 PRESENT, PARSEABLE, AN
          OBJECT, EXACTLY KEYED, EXACTLY TYPED AND STRUCTURALLY VALID ---
        A15  the three path values of governing_pre_selection equal,
             respectively, the manifest's pre_selection_packet_path,
             pre_selection_amendment_path and pre_selection_composite_path.
                                            else STAGE_A_PRESELECTION_MISMATCH
        A16  THE THREE PRE-SELECTION DIGESTS ARE ANCHORED, NOT MERELY MUTUALLY
             EQUAL. Four sub-clauses, evaluated in this order, each fail-closed,
             each raising STAGE_A_PRESELECTION_MISMATCH:
             A16(a) the three sha256 values of governing_pre_selection equal,
                    respectively, the manifest's pre_selection_packet_sha256,
                    pre_selection_amendment_sha256 and
                    pre_selection_composite_sha256. THIS CONJUNCT ALONE IS NOT
                    SUFFICIENT AND NEVER WAS: it compares two author-written
                    copies of one value with each other and anchors neither.
             A16(b) the packet value equals the SHA-256 of the whole bytes
                    found at TS-1's literal packet path, recomputed at
                    validation time. If no file exists at that path the clause
                    FAILS; there is no absent-file exemption.
             A16(c) the amendment value equals the SHA-256 of the whole bytes
                    found at TS-1's literal amendment path, recomputed at
                    validation time, and therefore also equals the M1 amendment
                    digest and the manifest's peer_amendment_sha256.
             A16(d) the composite value equals the PRE-SELECTION COMPOSITE
                    ANCHOR of the M1 amendment, extracted by this exact rule
                    and no other: split the M1 amendment's bytes on 0x0A; a
                    line is an ANCHOR LINE if and only if the whole line, after
                    stripping a trailing 0x0A and with no other leading or
                    trailing byte, consists of the literal token
                    P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256 followed by
                    exactly one 0x20, one 0x3D, one 0x20, and then exactly 64
                    characters each one of 0123456789abcdef. THE COUNT OF
                    ANCHOR LINES MUST BE EXACTLY ONE — zero and two or more
                    both FAIL, exactly as the sentinel-cardinality rule of the
                    composite's extraction algorithm fails — and the 64
                    characters of that one line are the anchor value. A prose
                    mention of the token that is not followed by that exact
                    separator and exactly 64 hexadecimal characters is not an
                    anchor line and is not counted.
                    WHY THIS ONE IS ANCHORED DIFFERENTLY, STATED PLAINLY: OR-4
                    deletes one branch of every variant block, so the reviewed
                    pre-selection composite bytes exist NOWHERE on disk after
                    OR-4 and cannot be recomputed by anyone; and the composite
                    cannot carry the value as a literal, because a file cannot
                    contain its own digest without a fixed point and §P1-14.5
                    forbids it. The amendment can and does, because OR-4 does
                    not change the amendment, and the amendment's own bytes are
                    pinned by peer_amendment_sha256, by its M1 membership in
                    the install record, and through install_record_id by Stage
                    B's signature. THIS IS AN ANCHOR, NOT A PROOF OF
                    FRESHNESS, AND TR-2(b) IS UNCHANGED BY IT: when an entire
                    coherent generation is restored, the amendment, its anchor
                    line, the packet, the manifest, Stage A, Stage B, the
                    signature and the record are all restored together and
                    every clause here passes on the restored bytes.
        A17  the SHA-256 of the whole Stage-A file equals the manifest's
             stage_a_sha256; TS-1's path equals the manifest's stage_a_path;
             and key_id equals the manifest's stage_a_key_id.
                                            else STAGE_A_BINDING_MISMATCH
      NO CLAUSE OF TS-2B READS AN ABSENT, INVALID-JSON, NON-OBJECT,
      MISSING-KEY OR WRONGLY TYPED MANIFEST. Each of those five states is
      already fatal, with its own single code, at CK-7 (MEMBER_OMITTED for an
      absent M4) or at CK-8 (MEMBER_SUBSTITUTED for an M4 that does not parse,
      is not an object, has the wrong key set or has a wrongly typed value).
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
        member_count               INTEGER, exactly 65
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
      first failure. Clauses B1..B13 run at CK-3 and are SELF-CONTAINED: they
      read only the two Stage-B paths and the Stage-A file, which CK-2 has
      already validated, and no manifest, member or record. Clauses B14..B18 run
      at CK-14, because they depend on the recomputed id, the member digests and
      the matched record.
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
        B7   member_count is the INTEGER 65.         else STAGE_B_MALFORMED
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
        B15  install_record_id equals the id recomputed at CK-11 from the
             members found on disk.                  else STAGE_B_INSTALL_ID_MISMATCH
        B16  install_record_path names the one record file established at CK-5
             and matched at CK-12.                   else STAGE_B_INSTALL_ID_MISMATCH
        B17  member_count equals the enumerated member count, 65.
                                                     else STAGE_B_INSTALL_ID_MISMATCH
        B18  governing_amendment_sha256 and governing_composite_sha256 equal
             the digests of the two M1 members found on disk at CK-7, and
             governing_amendment_sha256 additionally equals the manifest's
             peer_amendment_sha256, which CK-10 has already anchored to the same
             bytes.                                  else STAGE_B_GOVERNING_MISMATCH

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
      THE PRE-SELECTION PACKET IS LIKEWISE OUTSIDE M1..M7. TS-2 A16(b) reads
      the bytes at TS-1's literal packet path in order to hash them. That makes
      the packet a HASH-READ TARGET of one clause and nothing else: it adds no
      member, adds no class, changes no cardinality, supplies no path to CK-4,
      and is not opening a document for behaviour (IR-12, N-14). Its integrity
      requirement is discharged by the clause itself — a changed packet fails
      A16(b) with STAGE_A_PRESELECTION_MISMATCH.
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
       is verified per TS-2A, clauses A1 through A14, which read only the
       Stage-A file. TS-2B's clauses A15 through A17 are not yet evaluable
       because M4 does not exist; they are evaluated at OR-7 and, at every
       production entry point thereafter, at CK-9.

OR-4   EVERY VARIANT BLOCK IN THE COMPOSITE IS RESOLVED to the signed branch and
       the other branch is DELETED; the v1.3 amendment is installed. After this
       step G-10 finds zero markers. M1 is now final and its two digests are
       fixed.

OR-5   THE M5 VERIFIER AND THE TWO M6 MODULES ARE INSTALLED at their literal
       paths of MS-5 and MS-6.

OR-6   THE M4 MANIFEST IS WRITTEN at MS-4's literal path, with all twenty keys,
       the canonical eighty-nine-row reachable_closure VALUE of MS-11.1, the
       semantic source of
       every field per MS-12 — including peer_amendment_sha256 recomputed from
       the M1 amendment bytes — the three pre-selection path and digest pairs
       anchored as TS-2 A16 requires, and the three Stage-A binding fields.

OR-7   THE FULL TEST MATRIX RUNS against the M5 verifier and the M6 bundle and
       EVERY row passes. The placeholder audit and the guard fires are run; the
       required placeholder count and guard-fire count are ZERO. TS-2B is now
       evaluable and TS-2A and TS-2B are together evaluated in full, A1 through
       A17.

OR-8   THE M7 ATTESTATION IS WRITTEN at MS-7's literal path, binding the M5
       digest and the two M6 digests found on disk and the bundle digest
       recomputed from them.

OR-9   THE CANONICAL 65-MEMBER LIST IS BUILT FROM MS-1..MS-7 ALONE and
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
       fact. THE WITHDRAWAL IS UNCHANGED IN VERSION 1.4 AND IS NOT NARROWED BY
       ANY REPAIR IN IT.

VP-1  THE STRUCTURAL VALIDATION PHASE, AND ITS EXACT RANGE. A STRUCTURAL
      PREDICATE IS ONE THAT CAN BE DECIDED FROM THE OBJECT'S OWN BYTES ALONE,
      WITHOUT READING ANY OTHER OBJECT AND WITHOUT RECOMPUTING ANY DIGEST.
      Exactly these, in exactly this order, for the install record, M4 and M7:
        S1  the file exists at its literal path;
        S2  its bytes parse as JSON;
        S3  the top-level value is an OBJECT;
        S4  its key set is EXACTLY the key set that IR-3, MS-4 or MS-7 states —
            no extra key, no missing key;
        S5  the JSON type of every value is the type stated for its key;
        S6  the bytes are byte-identical to CANON of the parsed value, the
            trailing 0x0A included (MS-0);
        S7  the mandatory schema literal equals the exact string stated for that
            object, and version is the INTEGER 1 — not "1", not 1.0. THESE TWO
            ARE THE ONLY MANDATORY LITERALS THE STRUCTURAL PHASE OWNS. Every
            other literal in those sections names a value belonging to some
            other object or to §P1-3.1, and is therefore semantic;
        S8  every array satisfies its stated CARDINALITY, its stated element
            SHAPE, its stated ORDER or sortedness, and its stated pairwise
            distinctness; every lexical grammar holds — a digest string is
            exactly 64 characters each one of 0123456789abcdef, a created_utc
            value satisfies BOTH the grammar and the semantic validator of
            MS-10, and every enumerated literal is one of its stated literals;
            and every string required to be a literal CONCATENATION of constants
            and another field of the SAME object satisfies that concatenation.
      S1 THROUGH S5 ARE THE PREREQUISITE SUB-PHASE. They are stated separately
      and ordered first because every later predicate over that object — S6, S7,
      S8, and every semantic clause of VP-2 — presupposes that the object exists,
      parses, is an object, and has a value of the right type under the key it
      is about to read. VERSION 1.4 DID NOT SEPARATE THEM, WHICH IS WHY TS-2's
      M4-DEPENDENT CLAUSES COULD BE ORDERED BEFORE THE OBJECT THEY READ EXISTED.
      NOTHING ELSE IS STRUCTURAL. In particular the structural phase does NOT
      decide whether a digest equals anything, whether an id equals a filename or
      a recomputation, whether a path equals another section's literal path,
      whether reachable_closure equals MS-11.1, or whether rows_attested,
      row_count or all_rows_passed agree with the bundle installed. Every one of
      those is semantic and is owned in VP-2.
      MEMBER EXISTENCE AND MEMBER DIGESTS ARE NOT PART OF THIS PHASE. They are
      CK-7, which runs between the record's structural validation and the
      members' structural validation, and which owns MEMBER_OMITTED and
      HISTORICAL_BYTE_MOVED.
      STAGE A AND STAGE B ARE NOT VALIDATED HERE AND ARE NOT MEMBERS. Their
      clauses are single-owner chains — TS-2A A1..A14, TS-2B A15..A17 and TS-5
      B1..B18 — with their own codes, run at CK-2, CK-9, CK-3 and CK-14, and no
      clause of theirs is restated in this phase.

VP-2  THE SEMANTIC AND CROSS-OBJECT VALIDATION PHASE. A SEMANTIC PREDICATE IS
      ONE THAT REQUIRES READING ANOTHER OBJECT, READING A LITERAL OF THESE
      GOVERNING BYTES, OR RECOMPUTING A DIGEST. Its owners and codes are exactly:
        CK-9   TS-2B A15, A16(a)..(d), A17 — Stage A against M4
                                                  STAGE_A_PRESELECTION_MISMATCH,
                                                  STAGE_A_BINDING_MISMATCH
        CK-10  the eleven M4 relations of MS-12 that TS-2B does not own
                                                  MANIFEST_VALUE_MISMATCH
        CK-12  the record's id equals its filename and equals the IR-1
               recomputation of CK-11             INSTALL_RECORD_NAME_MISMATCH
        CK-13  the record's members array equals the enumerated set
                                                  MEMBER_EXTRA, MEMBER_STALE,
                                                  MEMBER_SUBSTITUTED
        CK-14  TS-5 B14..B18                      the STAGE_B_ codes named
        CK-15  every M7 relation                  ATTESTATION_MISMATCH
      NO SEMANTIC PREDICATE IS EVALUATED IN THE STRUCTURAL PHASE, AND NO
      STRUCTURAL PREDICATE IS RE-EVALUATED IN THE SEMANTIC PHASE. NO RELATION
      APPEARS UNDER TWO OWNERS. Version 1.4 broke that twice — CK-7 claimed
      "every MS-12 relation" while VP-3 gave nine of them to CK-2, and CK-13
      re-asserted an M2/M3 byte identity already fatal at CK-6 — and both
      duplications are removed here: MS-12's nine Stage-A-owned rows are excised
      from CK-10's range by name, and the M2/M3 recorded-digest relation is owned
      once, at CK-7, where it raises HISTORICAL_BYTE_MOVED.

VP-3  THE ORDERED RELATION-TO-OWNER-TO-CODE TABLE. Every field of every
      generated object, and every cross-object relation, appears exactly once.
      The OWNER column names the ONE EARLIEST clause that can refuse it; the
      CODE column names the ONE code it raises.

      INSTALL RECORD — five keys, validated at CK-6, BEFORE any member is read
        existence and uniqueness of the file  CK-5 / INSTALL_RECORD_ABSENT,
                                              INSTALL_RECORD_REPLAYED
        parse, object, key set, types         CK-6 S2,S3,S4,S5 / MEMBER_SUBSTITUTED
        schema, version                       CK-6 S7 / MEMBER_SUBSTITUTED
        CANON identity                        CK-6 S6 / MEMBER_SUBSTITUTED
        members array shape/order/64-hex      CK-6 S8 / MEMBER_SUBSTITUTED
        created_utc grammar                   CK-6 S8 / MEMBER_SUBSTITUTED
        install_record_id 64-hex              CK-6 S8 / MEMBER_SUBSTITUTED
        install_record_id = IR-1 digest       CK-12 / INSTALL_RECORD_NAME_MISMATCH
        install_record_id = filename stem     CK-12 / INSTALL_RECORD_NAME_MISMATCH
        members = enumerated set              CK-13 / MEMBER_EXTRA, MEMBER_STALE,
                                              MEMBER_SUBSTITUTED

      MEMBERS — existence and bytes
        a member absent from its literal path CK-7 / MEMBER_OMITTED
        an M2 or M3 member whose recomputed
          digest differs from the value
          recorded literally at MS-2 or MS-3  CK-7 / HISTORICAL_BYTE_MOVED
        every other member digest             recomputed at CK-7, compared at
                                              CK-11 through CK-13

      M4 PRODUCTION MANIFEST — twenty keys
        FIELD                          STRUCTURAL   SEMANTIC OWNER / CODE
        schema                         CK-8 S4,S7   —
        version                        CK-8 S4,S7   —
        roots                          CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        root_source_sha256             CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        reachable_closure              CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_sha256            CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_body_sha256       CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_guarddata_sha256  CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_normative_sha256  CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        peer_amendment_sha256          CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        pre_selection_packet_path      CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_packet_sha256    CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_amendment_path   CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_amendment_sha256 CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_composite_path   CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_composite_sha256 CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        stage_a_path                   CK-8 S5      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        stage_a_sha256                 CK-8 S8      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        stage_a_key_id                 CK-8 S8      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        created_utc                    CK-8 S8      — (compared with nothing)
      THE NINE STAGE-A-OWNED ROWS ARE OWNED AT CK-9 AND ARE NOT RE-RAISED AT
      CK-10. CK-9 PRECEDES CK-10, AND BOTH PRECEDE NOTHING THAT READS M4 EARLIER,
      BECAUSE CK-7 AND CK-8 HAVE ALREADY MADE M4 PRESENT AND STRUCTURALLY VALID.
      That is the whole of the version-1.4 prerequisite defect and its repair.

      M7 PASSING ATTESTATION — ten keys
        schema                         CK-8 S4,S7   —
        version                        CK-8 S4,S7   —
        verifier_path                  CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        verifier_sha256                CK-8 S8      CK-15 / ATTESTATION_MISMATCH
        test_bundle_modules            CK-8 S5,S8   CK-15 / ATTESTATION_MISMATCH
        test_bundle_digest             CK-8 S8      CK-15 / ATTESTATION_MISMATCH
        rows_attested                  CK-8 S5,S8   CK-15 / ATTESTATION_MISMATCH
        row_count                      CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        all_rows_passed                CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        created_utc                    CK-8 S8      —

      STAGE A — eleven keys
        TS-2A: schema A4 · version A5 · author A6 · signature_algorithm A7 ·
          selected_option_token A8 · selected_option_amendment_token A9 ·
          public_key_hex A10 · key_id A11 · governing_pre_selection shape A12
          and literal paths A13 · threat_model A14 · created_utc A14.
        TS-2B: governing_pre_selection against the manifest A15, A16(a)..(d);
          the Stage-A binding fields A17.
        Codes exactly as those clauses name them.

      STAGE B — thirteen keys
        TS-5 B1..B13 at CK-3; B14..B18 at CK-14. schema B4 · version B5 ·
        created_utc B6 · member_count B7 then B17 · stage_a_path B13 ·
        stage_a_sha256 B8 then B13 · key_id B8 then B13 ·
        selected_option_token B14 · install_record_id B8 then B15 ·
        install_record_path B9 then B16 · governing_amendment_sha256 B8 then
        B18 · governing_composite_sha256 B8 then B18 · signature_algorithm B10.
        The detached signature is B1, B11 and B12. Where a field appears twice
        the EARLIER clause owns a malformed value and the LATER clause owns a
        well-formed but disagreeing value; the two cases are disjoint.

VP-4  THE LITERAL TOPOLOGICAL PREDICATE ORDER. Every predicate's prerequisites
      are established by an EARLIER check, not merely ordered before it.
        1.  CK-1   no predicate
        2.  CK-2   Stage A alone            (TS-2A A1..A14, in order)
        3.  CK-3   Stage B alone            (TS-5 B1..B13, in order)
        4.  CK-4   the member enumeration, a constant of these bytes
        5.  CK-5   exactly one install record EXISTS
        6.  CK-6   that record is STRUCTURALLY VALID   (S1..S8, in order)
        7.  CK-7   every member EXISTS and its digest is recomputed, members
                   visited in IR-1 order — ascending by class, then by path
        8.  CK-8   M4 then M7 are STRUCTURALLY VALID   (S1..S8, in order)
        9.  CK-9   Stage A against M4        (TS-2B A15, A16(a)..(d), A17)
        10. CK-10  M4 semantics              (MS-12's eleven remaining rows, in
                   MS-12's top-to-bottom order)
        11. CK-11  recompute install_record_id
        12. CK-12  id equalities
        13. CK-13  the record's members array against the enumerated set
        14. CK-14  Stage B cross-object      (TS-5 B14..B18, in order)
        15. CK-15  M7 semantics              (MS-7's key order)
      NO IMPLEMENTATION MAY HOIST A LATER CLAUSE EARLIER AS AN OPTIMIZATION OR
      DEFER AN EARLIER ONE, and one that does is nonconforming even if it accepts
      and refuses the same sets.
      THE SIX MULTI-FAULT STATES THAT VERSION 1.4 LEFT UNDEFINED, EACH NOW WITH
      EXACTLY ONE FIRST CODE:
        valid Stage A + absent M4
          CK-7  MEMBER_OMITTED          (CK-2 no longer touches M4 at all)
        valid Stage A + M4 that is not valid JSON
          CK-8  MEMBER_SUBSTITUTED      (S2; CK-9 is not reached)
        malformed sole install record + absent member
          CK-6  MEMBER_SUBSTITUTED      (the record is validated before members)
        malformed sole install record + stale member
          CK-6  MEMBER_SUBSTITUTED      (same reason)
        M4 semantic mismatch + Stage-A binding mismatch
          CK-9  STAGE_A_BINDING_MISMATCH (CK-9 precedes CK-10)
        changed M2/M3 bytes + coordinated record and member mismatch
          CK-7  HISTORICAL_BYTE_MOVED   (CK-7 precedes CK-11..CK-13)
      TWO CONFORMING IMPLEMENTATIONS PRESENTED WITH THE SAME BYTES RETURN THE
      SAME FIRST FAILURE AND THE SAME REASON CODE, IN THESE SIX STATES AND IN
      EVERY OTHER, BECAUSE VP-3 GIVES EVERY RELATION EXACTLY ONE OWNER AND THE
      ORDER ABOVE GIVES EVERY OWNER EXACTLY ONE POSITION.

CK-1   WHEN. Before ANY production entry point — before any process is created,
       any handle is allocated, any freeze route is reachable, any evidence is
       accepted and any settlement runs. This check is the FIRST thing a
       production entry point does; nothing precedes it and no work is performed
       in parallel with it.

CK-2   VERIFY STAGE A, SELF-CONTAINED STAGE: TS-2A, clauses A1 through A14, in
       order. THIS CHECK READS NO MANIFEST, NO MEMBER AND NO RECORD. Codes:
       STAGE_A_ABSENT, STAGE_A_MALFORMED, STAGE_A_OPTION_INVALID,
       STAGE_A_KEY_MALFORMED.

CK-3   VERIFY STAGE B, SELF-CONTAINED STAGE: TS-5, clauses B1 through B13, in
       order. Codes: STAGE_B_ABSENT, STAGE_B_SIGNATURE_ABSENT,
       STAGE_B_MALFORMED, STAGE_B_ALGORITHM_INVALID, STAGE_B_SIGNATURE_INVALID,
       STAGE_B_STAGE_A_MISMATCH.

CK-4   ENUMERATE THE 65 MEMBERS FROM MS-1 THROUGH MS-7 ALONE. No wildcard, no
       directory scan, no glob, no adjective, no path taken from the install
       record, no path taken from the manifest, no path taken from the
       provenance region and no path taken from any future-edit table. THE
       ENUMERATION IS A CONSTANT OF THESE GOVERNING BYTES, reads no file, and is
       identical in the two governing files.

CK-5   THE INSTALL RECORD EXISTS AND IS UNIQUE. Require that EXACTLY ONE file
       directly under successor/officina/runtime_control/INSTALL/ has a name
       consisting of 64 lowercase hexadecimal characters followed by ".json".
       Zero fails with INSTALL_RECORD_ABSENT; two or more fail with
       INSTALL_RECORD_REPLAYED, and a retained record from an earlier install
       generation ALONGSIDE the current one is exactly that case. THIS IS NOT A
       MEMBER ENUMERATION: it reads no member and takes no path into the member
       set.
       A RECORD FROM AN EARLIER GENERATION PRESENTED ALONE AGAINST THE CURRENT
       MEMBERS STILL FAILS, later, at CK-12 and B15.
       WHAT THIS DOES NOT CATCH: a COMPLETE COHERENT ROLLBACK, in which the
       members themselves are also restored to the earlier generation. TR-2
       clause (b) states that case exactly and does not claim to refuse it.

CK-6   THE INSTALL RECORD IS STRUCTURALLY VALID. Apply VP-1's S1 through S8 to
       the one record established at CK-5, in that order, and refuse a violation
       with MEMBER_SUBSTITUTED naming the record path.
       THIS CHECK RUNS BEFORE ANY MEMBER IS READ, AND VERSION 1.4 DID NOT SAY SO.
       There, the record and the members were validated inside one check whose
       internal order was stated only for the members, so a state with a
       malformed record AND an absent or stale member had two defensible first
       codes. The record is not one of the 65 members; it is the object the
       member checks are about to be compared against, so it is made
       well formed first. NO SEMANTIC RELATION IS DECIDED HERE: the id
       equalities are CK-12 and the members-set equality is CK-13.

CK-7   EVERY MEMBER EXISTS, AND EVERY MEMBER DIGEST IS RECOMPUTED. Visit the 65
       enumerated members in IR-1's order — ascending by class compared byte for
       byte, then by path compared byte for byte. For each: require a file at
       the literal path, else refuse with MEMBER_OMITTED; recompute the SHA-256
       of its bytes. For M2 and M3 additionally require the recomputed digest to
       equal the digest recorded literally at MS-2 and MS-3, and refuse a
       difference with HISTORICAL_BYTE_MOVED.
       HISTORICAL_BYTE_MOVED IS OWNED HERE AND NOWHERE ELSE. Version 1.4 raised
       the same relation twice — once as MEMBER_STALE inside its structural
       check and again as HISTORICAL_BYTE_MOVED in a later check that re-asserted
       it — which contradicted VP-2's own no-re-evaluation rule. The relation is
       evaluated once, here, with one code. MEMBER_STALE now has exactly one
       meaning and one owner: a digest recorded IN THE RECORD that differs from
       the digest recomputed here, refused at CK-13.

CK-8   M4 AND M7 ARE STRUCTURALLY VALID. Apply VP-1's S1 through S8 to the M4
       manifest and then to the M7 attestation, in that order, and refuse a
       violation with MEMBER_SUBSTITUTED naming the offending path.
       AFTER THIS CHECK, AND ONLY AFTER IT, THE MANIFEST IS KNOWN TO EXIST, TO
       PARSE, TO BE AN OBJECT, TO CARRY EXACTLY MS-4's KEY SET AND TO CARRY A
       VALUE OF THE STATED TYPE UNDER EVERY KEY. That is the prerequisite TS-2B
       needs and version 1.4 never established.

CK-9   VERIFY STAGE A AGAINST THE MANIFEST: TS-2B, clauses A15, A16(a) through
       A16(d), and A17, in that order. Codes: STAGE_A_PRESELECTION_MISMATCH,
       STAGE_A_BINDING_MISMATCH.

CK-10  THE M4 SEMANTIC CHECK. Evaluate the ELEVEN relations of the MS-12 table
       that TS-2B does not own — roots, root_source_sha256, reachable_closure,
       the four p1_composite_* digests, peer_amendment_sha256, and the schema,
       version and created_utc rows already settled structurally — in MS-12's
       top-to-bottom order, including MS-11.4's equality of reachable_closure
       with the canonical eighty-nine-row value of MS-11.1 and MS-12's
       requirement that peer_amendment_sha256 equal the SHA-256 of the M1
       amendment bytes. Any failure refuses with MANIFEST_VALUE_MISMATCH naming
       the offending key. THE NINE STAGE-A-OWNED ROWS ARE NOT EVALUATED HERE.

CK-11  RECOMPUTE install_record_id per IR-1 from the member paths and digests
       found at CK-7.

CK-12  REQUIRE THE RECOMPUTED ID TO EQUAL THE INSTALL RECORD'S FILENAME STEM AND
       TO EQUAL THE record's own install_record_id FIELD. Either inequality
       refuses with INSTALL_RECORD_NAME_MISMATCH.

CK-13  REQUIRE THE RECORD'S MEMBERS LIST TO EQUAL THE ENUMERATED SET EXACTLY:
       the same cardinality 65, the same class labels, the same paths, the same
       digests, and the same order. An extra entry refuses with MEMBER_EXTRA; a
       recorded digest differing from the digest recomputed at CK-7 refuses with
       MEMBER_STALE; a class label or path that does not match the enumeration
       refuses with MEMBER_SUBSTITUTED. An omission cannot first appear here,
       because an absent member is already fatal at CK-7.

CK-14  COMPLETE STAGE B VERIFICATION: TS-5 clauses B14 through B18, in order.

CK-15  THE M7 SEMANTIC CHECK. REQUIRE THE M7 ATTESTATION to name MS-5's literal
       verifier path, the M5 digest and the two M6 digests found at CK-7, in
       MS-6's order, and to carry the bundle digest recomputed from them per
       MS-6, with rows_attested exactly the 24 integers 92..115 ascending,
       row_count exactly 24 and all_rows_passed exactly the boolean true. Any
       failure refuses with ATTESTATION_MISMATCH. A passing attestation produced
       against a different verifier or a different test bundle is rejected here,
       and so is a well-typed attestation carrying the wrong 24 integers.
       THE WHOLE CHECK, CK-1 THROUGH CK-15, IS FAIL-CLOSED AT THE FIRST FAILURE
       AND HAS NO PARTIAL MODE, NO WARNING MODE AND NO OVERRIDE.

FC-1  THE CLOSED FAILURE-CODE SET. On ANY failure of CK-1 through CK-15, or on
      an observed procedure violation under FS-4, REFUSE with
      "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE" and exactly one reason code
      naming the first failing check and the offending path. VP-3 makes "the
      first failing check" single-valued and VP-4 makes it implementation-
      independent by establishing every prerequisite before its dependent. The
      set has 26 codes, is closed, and no build may add, rename or merge one:
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
        MANIFEST_VALUE_MISMATCH        ATTESTATION_MISMATCH
        HISTORICAL_BYTE_MOVED          PROCEDURE_VIOLATION_OBSERVED
      EVERY ONE OF THE 26 HAS EXACTLY ONE OWNING CHECK, and version 1.4's two
      duplicated owners are gone: HISTORICAL_BYTE_MOVED is owned only at CK-7,
      MEMBER_STALE only at CK-13, and MANIFEST_VALUE_MISMATCH only at CK-10.
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
        c. all 65 members exist at their literal paths; every digest matches;
           every M2 and M3 digest additionally equals the value recorded
           literally at MS-2 and MS-3; and M4, M7 and the record satisfy both
           the structural predicates of VP-1 and the semantic relations of
           VP-2;
        d. install_record_id recomputed from those bytes equals the record's
           filename, equals the record's own install_record_id field, and
           equals Stage B's install_record_id;
        e. M7 binds the M5 digest and the two M6 digests actually found;
        f. exactly one content-addressed record exists directly under the
           INSTALL directory;
        g. the manifest's reachable_closure equals the canonical eighty-nine-row
           value of MS-11.1, which covers the role import surface of all three
           scoped allowlists including generic_harness.py; its
           peer_amendment_sha256 equals the M1 amendment digest recomputed from
           disk; and its three pre-selection digests equal the values A16(b),
           A16(c) and A16(d) derive from named repository bytes, rather than
           merely equalling Stage A's copies of themselves.
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
        the 65 members determine install_record_id            (IR-1)
        install_record_id determines the record's filename     (IR-2)
        Stage B names that id and is signed over its own canonical bytes
                                                               (TS-3, TS-4)
        the Ed25519 key that verifies Stage B is pinned in Stage A
                                                               (TS-1, TS-5 B12)
        Stage A is created at OR-3, before any M1 byte is final at OR-4, and is
        written by no later step
      THE CHECK ORDER IS ALSO ACYCLIC, AND VP-4 STATES IT AS A TOPOLOGICAL
      ORDER: no check reads an object that a later check is responsible for
      making well formed.
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
          matches the restored members and the sole record name; CK-5 sees
          exactly one hex-named record; every digest and the attestation match.
          NO NEW SIGNATURE AND NO PRIVATE KEY ARE NEEDED. THIS REACHES A
          RUNNABLE STATE AND IS NOT REFUSED. It is outside the guarantee, and
          the coherent-rollback fixture of test 106 classifies it as such
          rather than pretending it fails.
      WHAT THE TWO STAGES DO CLOSE — exactly these PROPER-SUBSET cases, and
      this list is the whole of the claim:
        Stage A replaced while the manifest is not          A17
        the manifest replaced while Stage A is not          A17, CK-8, CK-13
        the signature replaced, removed or malformed        B11, B12
        Stage B replaced while the signature is not         B12
        the record replaced while the members are not       CK-11, CK-12, B15
        the members replaced while the record is not        CK-7, CK-13
        M7 replaced while M5 or M6 is not                   CK-15
        an old record presented against current members     CK-12, B15
        an old record retained beside the current one       CK-5
        a mixed-generation pair of governing files          CK-7, CK-13, B15
        an option mismatch between the two stages           A9, B14, and the
                                                            B14 edge is now
                                                            carried by IR-4
        an unsigned install of any shape                    B1, B12 — no route
                                                            admits one
        a manifest whose peer_amendment_sha256 is a
          well-formed value that is not the M1 amendment
          digest                                            CK-10
        a manifest whose reachable_closure is structurally
          valid, self-closed and factually wrong, including
          one that omits the role import surface of
          generic_harness.py                                CK-10
        a manifest whose roots, root_source_sha256 or
          composite region digests are well formed and
          wrong                                             CK-10
        a coordinated arbitrary pre-selection triple
          written identically into Stage A and the
          manifest                                          A16(b), A16(c),
                                                            A16(d)
      THE FOUR NEW ROWS ARE PROPER-SUBSET CASES LIKE THE OTHERS, AND THEY
      NARROW NOTHING AND WIDEN NOTHING ABOUT CLAUSE (a) OR CLAUSE (b). Each of
      them was open in version 1.3 and each is closed in version 1.4; none of
      them was ever claimed closed by version 1.3, and the residual itself is
      unchanged.
      NO SENTENCE IN THESE GOVERNING BYTES, IN ANY PACKET AND IN ANY CLOSURE
      MAY CLAIM: that every post-hoc substitution is closed; that complete
      coherent rollback is resisted, detected or refused; that custody is
      immutable or external to this repository; or that any cryptographic
      freshness, monotonicity, recency or liveness property holds.
      THREE WORDS IN THAT PROHIBITION ARE ALSO USED ELSEWHERE IN A DIFFERENT
      AND PERMITTED SENSE, AND THE SENSES ARE SEPARATED HERE SO THAT NO LEXICAL
      SWEEP HAS TO GUESS:
        IMMUTABLE, in DA-1, DA-2, DA-3, MS-2 and §A7.2, is a DOCUMENT-AUTHORITY
          and RECORD-MUTATION word. It says that a historical document is not
          opened for behaviour and that a durable record is never overwritten,
          truncated, renamed or deleted by a conforming actor. IT IS NOT A
          CUSTODY CLAIM: it does not say that any byte is beyond the reach of an
          actor able to write this repository, and TR-2(a) and TR-2(b) say the
          opposite;
        MONOTONIC, in TIMING, QC, AK, RF, §A3.4 and every *_monotonic_ns field,
          names CLOCK_MONOTONIC samples inside one running generation. It is a
          runtime clock word and is NEVER a property of the install chain, of
          any digest, of any signature or of any ordering across generations;
        LIVENESS, in WA, AK, NS and the watchdog sections, names the watchdog's
          own acknowledgement health inside one generation. It is never a
          cryptographic liveness or freshness property of these artifacts.
      NO OCCURRENCE OF ANY OF THE THREE, ANYWHERE IN THIS PAIR, IS A CLAIM THE
      PROHIBITION ABOVE FORBIDS.
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

N-15  IT REDUCES ONE SCOPED ALLOWLIST BY ONE NAME AND WIDENS NO OTHER. §P1-3.2's
      scoped entry for `src/philosophia/officina/generic_harness.py` loses
      `subprocess` and goes from seventeen names to sixteen, for the reasons and
      with the authority stated at `MS-11.5`. THE NINETEEN-MEMBER GLOBAL DEFAULT
      IS UNCHANGED, both bootstrap scoped entries are UNCHANGED, and no other
      allowlist, root or rule moves. THE REDUCTION OPENS NO AUTHOR CELL AND
      MOVES NO SCIENTIFIC CELL: it adds, removes and renames no watchdog option,
      treatment, evidence class, covariate, endpoint, qualification input,
      comparison input, Q fact or C fact, and it is identical under `W-A` and
      `W-B`. It removes no capability the future implementation is permitted to
      use, because `S-12`, test 8 and the future-edit surface already forbid
      `subprocess` on every path of that file and `§P1-7.1` already launches
      through the bound `_posix_spawn` primitive.

N-14  IT ADDS NO MEMBER AND NO MEMBER CLASS. The seven classes and their
      cardinalities move only by the four provenance rows `MS-2` gains, which
      are the v1.4 amendment, composite v1.7 and the two v2.7 independent
      confirmations. `TS-2B` `A16(b)` reads the bytes at the literal packet path
      IN ORDER TO HASH THEM; that makes the packet a HASH-READ TARGET of one
      clause and NOT a member, exactly as `IR-12` already says of `M2` and `M3`.
      It supplies no path to `CK-4`, is in no class, is counted in no
      cardinality, and appears in no install record.
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
