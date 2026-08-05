# Officina P1 W-B post-selection binding v1 (draft)

**Author:** Claude Code Opus 5, **post-selection binding author only**. Not an
independent X-line or Y-line reviewer. **This draft selects nothing, accepts
nothing, installs nothing and executes nothing.**

This document is a **plan and contract for a transformation, not the
transformation itself.** It creates no resolved amendment, no resolved
composite, no key, no Stage A, no Stage B, no manifest, no attestation, no
signature and no install record. `T` is `NOT_ACTIVATED`; the programme claim is
`OPEN`.

---

## §0. Position and inputs

### §0.1 What is already signed

Kirill signed, on 2026-08-05, at selection base commit `176d609`:

```text
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
```

```text
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
```

That signature completes **`OR-2` and only `OR-2`**. `OR-3` through `OR-11`
remain unauthorized.

### §0.2 The governing bytes this binding reads

Every digest below was recomputed from disk at authoring time and matched the
value carried in the selection signature's own governing-hash block.

```text
06aa44fbe3221c9d41484e14fa2a31df42ce58ae17c8b899278b0bf6c5608e9d  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_10_CORRECTION.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
```

Recorded as **external author state, not as a member and not as authority
here**, exactly as `XS-1` of the peer amendment records it:

```text
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

### §0.3 What this document is not

```text
IT IS NOT the resolved amendment and NOT the resolved composite. It creates
  neither, and §2A below states the exact boundary against OR-3 and OR-4.
IT IS NOT the LATER COMBINED BINDING named at XS-1(a)..(d) of the peer
  amendment. It does not resolve the process-claim identity cell, does not
  bind the identity signature into any member class, and does not re-derive
  any identity field. §3 states this in full and it is load-bearing.
IT IS NOT an amendment acceptance. The v1.7 acceptance token remains unsigned.
IT IS NOT an implementation authorization, an install authorization or an
  activation authorization.
IT IS NOT an X-line or Y-line verdict, and it is normative for nothing. Every
  author closure is an untrusted self-assessment.
```

---

## §1. `B1` — the one operative branch

### §1.1 The selected branch, stated once

```text
SELECTED, AND THERE IS NO OTHER:
  option token          I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  option amendment      P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1

REJECTED, NON-SELECTED, AND TO BE DELETED AT OR-4:
  option token          I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  option amendment      P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
```

The five operative consequences, each traced to the governing locus that states
it, with no addition and no widening:

```text
S1  TOPOLOGY. The watchdog holds TWO SEALED PIPES and no socket: the update
    READ end at descriptor slot 3 and the ack WRITE end at slot 4. SLOT 6 IS
    EXPLICITLY CLOSED BY A FILE ACTION. The watchdog holds no freeze-request
    socket and no transport-request capability of any kind.
      composite §P1-13.2 P1-invariant row, [W-B] branch
      composite §P1-15 row 99, [W-B] branch — /proc/self/fd is exactly
        {0,1,2} together with {3,4,5,7,8,9,10}, slot 6 absent

S2  WATCHDOG ON EOF. Update-pipe EOF is the SINGLE supervisor-death detector.
    On EOF the watchdog WRITES NOTHING, FREEZES NOTHING, SIGNALS NOTHING,
    SENDS NOTHING, settles nothing, and exits.
      composite §P1-9.2 property 12, [W-B] branch — "It sends nothing"
      composite §P1-10.6, [W-B] branch — "No further operation of any kind is
        permitted"
      amendment §A3.5 — "NOTHING", on the supervisor-death path

S3  PCS AS DETECTOR AND SOLE EXECUTOR FOR THIS ROUTE. Loss of the peer control
    endpoint is detected by the Process-Control Server. The PCS runs the
    §P1-10.7 freeze classifier RECORD-FIRST, in the PCS root, and is the sole
    executor of the resulting group stops.
      composite §P1-10.7 TRIGGER, [W-B] branch — "loss of the peer control
        endpoint, record-first"
      composite §P1-15 row 89, [W-B] branch — site (b) reachable only from
        the endpoint-loss trigger site

S4  NO TRANSPORT FRAME EXISTS ON THIS BRANCH. No t-wd-freeze.v1 record is
    emitted, received, accepted, journalled or witnessed on any path. The
    bounded service window of W-A does not exist on this branch.
      composite §P1-9.2 property 12 and §P1-10.6, [W-A] branches deleted
      selection signature — "may emit no t-wd-freeze.v1 transport frame"

S5  NO DURABLE OBJECT, NO EVIDENCE, NO SCIENTIFIC INPUT. The watchdog produces
    no durable object of any class, is therefore a witness in no sense, and
    supplies no input to any scientific predicate. The classifier's own journal
    state is P1-owned process-control material and never reaches a peer
    artifact, an acceptance predicate, a qualification, a comparison, a Q or C
    fact, or any published record.
      composite §P1-10.6 and §P1-10.7 publication boundary
      composite §P1-15 row 89 — L8, ND-1..ND-3
```

### §1.2 The one peer-layer operation that survives, unchanged by the choice

```text
The watchdog performs EXACTLY ONE peer-layer operation, and it is REQUIRED
under BOTH options and therefore unchanged by this binding: the READ-ONLY
verification of the supervisor identity record of §P1-13.2 row 3, required by
§P1-9.2 property 8 and invariant 87, and NEVER by any parent relationship.

A read installs nothing, decides nothing, creates no durable object, and is
invisible to every acceptance predicate and to SW-1..SW-5. IT IS NOT AN
AUTHORITY. "Role-entry only" means no write, no decision and no execution; it
does not mean no read.

THE getppid() PROHIBITION IS UNCHANGED AND IS NOT WEAKENED. Under W-B its
retained rationale is the [W-B] one: the watchdog executes no freeze on any
path, so the prohibition stands because THE INFERENCE IS FALSE, not because of
what it would trigger (§P1-9.2 property 11).
```

### §1.3 The four common amendments, bound without changing their meaning

Each is bound **by reference to its owning governing locus**. This binding
restates scope and adds nothing; where this document and an owning clause could
be read to differ, **the owning clause governs and this document is the
defect.**

```text
P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1
  OWNING LOCI  amendment §A6, FB-1..FB-5; §A6.1 TO-1..TO-5
  WHAT IT BINDS  the t-freeze-fallback-observation.v1 object under
    WATCHDOG/FREEZE_FALLBACK/, its domain-tagged fallback_witness_id, its
    seventeen-key set, rejection_conjunct 0..10 with 0 as the ABSENT sentinel,
    unknown_reason in {EVIDENCE_ABSENT, EVIDENCE_UNVERIFIABLE,
    FREEZE_INSTANT_UNKNOWN}, and the separate key
    current_unresolved_member_count.
  THE NULLABLE PART, EXACTLY  on the ABSENT sentinel,
    rejected_witness_path_or_null and rejected_object_sha256_or_null are null
    and rejection_conjunct = 0. process_id IS MANDATORY AND NON-NULL ON EVERY
    FALLBACK BRANCH INCLUDING THAT ONE (FB-4).
  UNCHANGED BY W-B  FB-5 — the watchdog has no path here, before or after the
    amendment. The choice does not touch this object.

P1_PCS_FREEZE_CLASSIFIER_V1
  OWNING LOCI  composite §P1-10.7; §P1-15 row 89 site (b)
  WHAT IT BINDS  the PCS's own classifier as the SECOND of exactly two signed
    freeze-EXECUTION sites; actor the PCS in the PCS root; scope computed from
    the PCS's own handle table; no SIGNAL_GROUP mediation because it IS the
    PCS; no evidence of any peer class; journal terminal, per-group tokens and
    freeze_ns as P1-owned process-control facts only.
  WHAT W-B FIXES  the TRIGGER, and only the trigger: loss of the peer control
    endpoint, record-first. The W-A trigger — an ACCEPTED t-wd-freeze.v1
    record inside a bounded service window, with no freeze on window end — is
    deleted.
  UNCHANGED  the PCS remains the SOLE CALLER of fork, posix_spawn, kill,
    killpg and every wait-family primitive. Two execution SITES are not two
    CALLERS. S-12 is retained unchanged.
  SEE §5, FINDING F2  the scope predicate this amendment names, KV-1..KV-6, is
    not defined anywhere in the governing pair.

P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1
  OWNING LOCI  composite §P1-1.3; §P1-13.2 and its "one writer, two routes"
    discussion; §P1-13.9 ROUTE-D and ROUTE-W; amendment §A2, §A3.1, §A3.3
  WHAT IT BINDS  the freezer and witness role moves from the watchdog to the
    SUPERVISOR. The supervisor is the sole writer of
    t-freeze-observation.v1 under WATCHDOG/FREEZE/, on exactly two triggers of
    ONE procedure, reaching every group stop through the SIGNAL_GROUP opcode,
    with killer == SUPERVISOR on every reachable path.
  EXPLICITLY  this reassignment is COMMON TO BOTH OPTIONS and is NOT itself a
    choice (composite Cell 2 preamble). Binding W-B neither strengthens nor
    weakens it.
  IT DOES NOT  revoke, re-run or reopen the signed selection token that
    retains a dedicated watchdog PROCESS.

P1_FREEZE_PUBLICATION_L6_L9_V1
  OWNING LOCI  amendment §A8.1; §A8.2 PUB-1..PUB-4
  WHAT IT BINDS  PUB-1 WATCHDOG/LEASES.json is atomic-replace with strictly
    increasing table_seq; PUB-2 the IDENTICAL payload is published on the
    update pipe; PUB-3 BOTH happen BEFORE the first SIGCONT of the affected
    group and before any admission of that table_seq; PUB-4 ADMISSION IS
    REFUSED UNTIL THE ACK OF THAT EXACT table_seq IS OBSERVED.
  UNCHANGED BY W-B  the watchdog's acknowledgement duty (§P1-9.2 property 9)
    and the ack-absence timeout are option-independent. W-B removes no ack and
    adds none.
```

### §1.4 What this binding does **not** touch

```text
NB-1  IT DOES NOT REOPEN THE OTHER FIVE SIGNED CHOICES of §P1-1.3.
NB-2  IT DOES NOT MOVE THE reachable_closure. The 89-row value, its 29/13/2/45
      kind counts, its 76 transitive names, its 39 empty arrays, its 267 false
      booleans, its fourteen-row bootstrap subset, its seven unexecuted
      branches, its CANON length 20534 and its digest
      aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee
      are untouched by the selection and by this binding.
NB-3  IT ADDS NO MEMBER, NO MEMBER CLASS, NO PRODUCTION ROOT, NO AUTHOR CELL,
      NO SELECTION TOKEN, NO AMENDMENT TOKEN, NO FAILURE CODE AND NO TEST ROW.
NB-4  IT DOES NOT NARROW THE killer ENUM. {WATCHDOG, SUPERVISOR} is RETAINED;
      the WATCHDOG value is unreachable BY CONSTRUCTION rather than by
      deletion, so a legacy, stale or forged object is REJECTED at conjunct 8
      rather than being unparseable (KW-1, KW-2).
NB-5  IT CLAIMS NO TEMPORAL, FRESHNESS, MONOTONICITY OR ROLLBACK-RESISTANCE
      PROPERTY, and adds no notary, transparency log, timestamp oracle,
      monotonic-counter device or hardware security module.
```

---

## §2. The complete option-resolution table

### §2.1 The mechanical census, recomputed from the governing bytes

```text
MARKER-BEARING LINES, composite v1.10           20
MARKER-BEARING LINES, amendment v1.7             0
  the amendment contains the two-character-class strings ZERO times; every
  variant block lives in the composite, and OR-4 therefore edits ONE file
"[W-A]" OCCURRENCES, composite                  13
"[W-B]" OCCURRENCES, composite                  13
```

The twenty lines are **not one population**. They fall into three regions with
three different obligations, and conflating them is the single most likely way
to produce a non-conforming `OR-4`. The composite's region sentinels sit at:

```text
OFFICINA-P1-BODY-BEGIN         line  248
OFFICINA-P1-BODY-END           line 6461
OFFICINA-P1-GUARDDATA-BEGIN    line 6463
OFFICINA-P1-GUARDDATA-END      line 6504
OFFICINA-P1-PROVENANCE-BEGIN   line 6506
OFFICINA-P1-PROVENANCE-END     line 6696
```

```text
REGION      LINES  A   B   OBLIGATION AT OR-4
  PREAMBLE      3   2   2   outside G-10's match range; RESOLVE AND DELETE
    (1..247)                anyway — these are notation and a discharged
                            blocking notice, not two operative branches
  BODY         16  10  10   G-10's exclusive match range; RESOLVE each to the
    (249..6460)             [W-B] branch and DELETE the [W-A] branch
  GUARDDATA     1   1   1   THE PATTERN SOURCE. RETAIN BYTE-IDENTICAL. It is
    (6464..6503)            never a match target, and deleting it destroys
                            G-10 and changes H_GUARDDATA
  ---------------------------------------------------------------------------
  TOTAL        20  13  13
```

### §2.2 The locus-by-locus table

`RESOLVE` = retain the `[W-B]` text inline, without its marker, and delete the
`[W-A]` text. `DELETE` = remove the line or block outright, there being no
operative branch to retain. `RETAIN` = leave the bytes untouched.

```text
#   LINE  REGION     OWNING SECTION                       ACTION   NOTE
 1    79  PREAMBLE   Cell 2 blocking notice               DELETE   notation example, not a branch
 2    80  PREAMBLE   Cell 2 blocking notice               DELETE   notation example, not a branch
 3    83  PREAMBLE   Cell 2 blocking notice               DELETE   the sentence defining the convention
 4   302  BODY       §P1-1.3 six signed choices           RESOLVE  W-A "additionally signals the loss by requesting the freeze" deleted
 5   303  BODY       §P1-1.3 six signed choices           RESOLVE  W-B "The watchdog requests nothing" retained
 6  1653  BODY       §P1-9.2 property 11                  RESOLVE  W-B rationale retained: it executes no freeze on any path
 7  1656  BODY       §P1-9.2 property 11                  RESOLVE  W-A G-1/PEER_ENDPOINT_LIVE rationale deleted
 8  1663  BODY       §P1-9.2 property 12                  RESOLVE  W-A "sends exactly one t-wd-freeze.v1 on slot 6" deleted
 9  1667  BODY       §P1-9.2 property 12                  RESOLVE  W-B "It sends nothing" retained
10  1904  BODY       §P1-10.6 negative surface            RESOLVE  W-A "one further P1-layer operation is permitted" deleted
11  1907  BODY       §P1-10.6 negative surface            RESOLVE  W-B "No further operation of any kind is permitted" retained
12  1929  BODY       §P1-10.7 classifier TRIGGER          RESOLVE  W-B "loss of the peer control endpoint, record-first" retained
13  1930  BODY       §P1-10.7 classifier TRIGGER          RESOLVE  W-A ACCEPTED-record-in-bounded-window trigger deleted
14  2277  BODY       §P1-13.0 residence matrix            RESOLVE  one line carries BOTH markers; W-A slot-6 socket clause deleted, W-B "It holds no socket" retained
15  2560  BODY       §P1-13.2 P1-invariant row            RESOLVE  W-B TWO SEALED PIPES, slot 6 explicitly closed, retained
16  2566  BODY       §P1-13.2 P1-invariant row            RESOLVE  W-A THREE SEALED ENDPOINTS block deleted, socketpair and FD_CLOEXEC clause with it
17  6363  BODY       §P1-15 test row 61                   RESOLVE  both markers on one line; W-B classifier-and-terminal clause retained
18  6391  BODY       §P1-15 test row 89                   RESOLVE  both markers on one line; site (b) trigger fixed to the endpoint-loss site
19  6402  BODY       §P1-15 test row 99                   RESOLVE  both markers on one line; descriptor set fixed to {0,1,2}+{3,4,5,7,8,9,10}, slot 6 closed
20  6501  GUARDDATA  §P1-17 VARIANT_MARKER class          RETAIN   the two pattern strings; NEVER a match target; H_GUARDDATA must not move
```

Four body lines — 2277, 6363, 6391, 6402 — carry **both** markers on a single
line. A line-deletion strategy is therefore wrong on its face: those four must
be **edited in place**, not removed.

### §2.3 Two obligations `OR-4` states loosely, made exact here

```text
E-1  OR-4 says "EVERY VARIANT BLOCK IN THE COMPOSITE IS RESOLVED to the signed
     branch and the other branch is DELETED. After this step G-10 finds zero
     markers." Lines 79, 80 and 83 are NOT variant blocks: they are the
     definition of the notation and the Cell-2 blocking notice that the
     signature discharges. There is no branch there to resolve to. A literal
     reading of OR-4 leaves them in place. Because they sit at lines 79..83,
     BEFORE OFFICINA-P1-BODY-BEGIN at 248, G-10 STILL FINDS ZERO MARKERS and
     OR-4's stated success condition is met WITH THE NOTATION STILL PRESENT.
     THAT IS NOT A CONFORMING RESULT: the resolved file would still tell its
     reader that the cell is unsigned and that the document is not operative,
     and H_FILE would cover that text. THIS BINDING THEREFORE STATES THE
     OBLIGATION EXPLICITLY, and it is carried into the handoff as a checked
     item rather than left to inference.

E-2  THE GUARD DATA MUST SURVIVE. Line 6501 is the SOURCE of the two
     VARIANT_MARKER patterns. §P1-14.1 makes the guard data region a
     non-target, and §P1-17 states the region exists "so that they are never
     matched against themselves". An implementer told "delete every marker"
     deletes G-10's patterns, after which G-10 can never fire again AND
     H_GUARDDATA changes, which G-6 refuses against the manifest value.
     THE CORRECT ACTION AT LINE 6501 IS TO CHANGE NOTHING.
```

### §2.4 The mechanical post-`OR-4` invariant

Stated so that it is a total function of the resolved file's bytes.

```text
PO-1  MARKER ELIMINATION, BODY. Extract REGION(BODY) by the §P1-14.0 algorithm,
      apply §P1-14.2 NORMALIZE, and count occurrences of each pattern of the
      §P1-17 VARIANT_MARKER class.
        REQUIRED: 0 and 0.
      This is exactly G-10 and it is the only one of these checks the shipped
      verifier performs.

PO-2  MARKER ELIMINATION, WHOLE FILE OUTSIDE GUARD DATA. Count the same two
      patterns over the whole file MINUS the GUARDDATA region.
        REQUIRED: 0 and 0.
      This is STRICTLY STRONGER than PO-1 and is what closes E-1. It is not
      G-10 and must not be described as G-10.

PO-3  GUARD DATA PRESERVED. Recompute H_GUARDDATA over the extracted guard data
      region.
        REQUIRED: exactly
        faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
      unchanged from the pre-OR-4 value. The two VARIANT_MARKER patterns are
      still present there, exactly once each.

PO-4  REJECTED-BRANCH CAPABILITY ABSENCE, BY NAME. Over the whole resolved
      file, each of the following must occur ZERO times:
        the W-A option token
          I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
        the W-A option amendment token
          P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
        the transport-frame schema name  t-wd-freeze.v1
        the strings  slot 6  /  SOCK_SEQPACKET  /  socketpair
          in any clause granting the watchdog an endpoint
      EXCEPT that slot 6 MUST still occur in its CLOSED sense — the §P1-13.2
      "Slot 6 is not used and is explicitly closed by a file action" clause and
      the row-99 descriptor set — so PO-4 is a check on GRANTING clauses, not a
      blanket string ban. The handoff states the exact permitted occurrences.

PO-5  W-B INVARIANTS POSITIVELY PRESENT. Each of the following must be
      derivable from the resolved bytes with no variant marker anywhere in the
      derivation:
        a. the watchdog descriptor set is {0,1,2} + {3,4,5,7,8,9,10}, slot 6
           absent, two sealed pipes  (row 99)
        b. §P1-9.2 property 12 reads: writes nothing, freezes nothing, signals
           nothing, sends nothing, exits
        c. §P1-10.6 reads: no further operation of any kind is permitted
        d. §P1-10.7 TRIGGER reads: loss of the peer control endpoint,
           record-first
        e. row 89 site (b) is reachable only from the endpoint-loss trigger

PO-6  SELECTION-TOKEN BINDING. The resolved state must carry the W-B token as
      the value bound across the two stages at B14, and TS-1's two literal
      option tokens must remain BOTH present as the option SET that B14 selects
      from. RESOLVING THE COMPOSITE DOES NOT DELETE THE OPTION SET; deleting
      the non-selected token from TS-1 would break IR-13 row 47.

PO-7  DIGEST CONSEQUENCES, STATED SO THEY ARE NOT DISCOVERED LATE.
        H_GUARDDATA   UNCHANGED   (PO-3)
        H_BODY        CHANGES
        H_NORMATIVE   CHANGES
        H_FILE        CHANGES
      The composite H_FILE changes, therefore the §A0.4 pre-selection anchor
      value in the amendment — which equals the PRE-selection composite H_FILE
      86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f —
      is NOT the post-OR-4 composite digest and must never be updated to it.
      IR-11 and MS-12 already state this: OR-4 changes the composite's bytes
      and does not change the amendment's, which is exactly why the
      amendment's two digests are equal and the composite's are not.

PO-8  AMENDMENT UNCHANGED BY MARKER RESOLUTION. The v1.7 amendment contains
      zero markers, so OR-4's marker work does not touch it. OR-4's separate
      clause "the amendment is installed" concerns MS-1's second literal path
      and nothing else. SEE §5 FINDING F3.
```

---

## §2A. `B2` — the dry-run oracle, and its boundary against `OR-3`/`OR-4`

A **test-only, in-memory transformation oracle** may be implemented and
unit-tested **before** the amendment is accepted and before any handoff step is
authorized. It exists so that §2.2's table and §2.4's invariants can be
mechanically checked without touching a governing or runtime path.

### §2A.1 What the oracle is

```text
O-1  INPUT. Byte copies of the v1.7 amendment and composite v1.10, read from
     their literal paths in read-only mode and held in memory. It opens neither
     for behaviour; it hashes and rewrites bytes and interprets no rule.
O-2  IT SELECTS W-B IN MEMORY, from a test-only enum with exactly two members,
     and produces a candidate resolved byte string as a RETURN VALUE.
O-3  IT CHECKS PO-1 THROUGH PO-6 of §2.4 against that in-memory string, and
     reports each as a pass or a fail with the locus that failed.
O-4  IT MAY REPORT DIGESTS, and every reported digest MUST be emitted with the
     literal tag
       test-only/non-installed/non-authoritative
     adjacent to the value, in the same string, so that no transcript, log line
     or test output can be quoted as an install digest.
O-5  IT IS TOTAL AND DETERMINISTIC. Same inputs, same output bytes, on every
     run, on any host. It samples no clock, draws no entropy and reads no
     environment variable.
```

### §2A.2 What the oracle may never do

```text
O-6   IT WRITES NO FILE TO ANY GOVERNING OR RUNTIME PATH. It writes nothing
      under successor/, nothing under successor/officina/, nothing under any
      INSTALL directory, and nothing to either MS-1 literal path. If it writes
      at all it writes only under a per-test temporary root it created and
      removes.
O-7   IT CREATES NO KEY AND NO ENTROPY. No Ed25519 key pair, no key_id, no
      public_key_hex, no seed of any kind.
O-8   IT CREATES NO STAGE A AND NO STAGE B, no detached signature, no M4
      manifest, no M7 attestation, no member list, no install record and no
      install_record_id.
O-9   ITS OUTPUT IS NOT PRODUCTION INPUT. The resolved byte string is a return
      value and a test fixture. No function that writes a governing path may
      accept it, and the oracle module must export no writer that could.
O-10  IT IS NOT OR-4 EVIDENCE. A passing oracle run proves nothing about the
      install, satisfies no OR step, and may not be cited in any acceptance,
      authorization, attestation or install record. FS-2 already says the
      final-state gate cannot reconstruct history; an oracle run is not even
      part of that history.
O-11  IT RUNS NO PROCESS-CONTROL OPERATION. No fork, exec, posix_spawn, signal,
      wait, killpg, socket, pipe, prctl or /proc read against any live process.
```

### §2A.3 What later authorized `OR-4` does that the oracle does not

Stated as a difference list, so the boundary is not a matter of tone.

```text
                                        ORACLE      AUTHORIZED OR-4
  produces resolved bytes                in memory   ON DISK at MS-1's second
                                                     literal path
  requires the acceptance token          no          YES — v1.7 accepted first
  requires a completed OR-3              no          YES — Stage A exists and
                                                     is verified A1..A14, and
                                                     the key pair was generated
  requires an implementation and a       no          YES, both
    one-shot handoff authorization
  installs the amendment (MS-1 path 1)   no          YES
  fixes M1 and its two digests           no          YES — "M1 is now final and
                                                     its two digests are fixed"
  is a precondition of OR-5..OR-11       no          YES
  its digests may be recorded in M4      NEVER       YES, at OR-6
  is subject to G-10 in the shipped      no          YES
    verifier
  changes H_BODY, H_NORMATIVE, H_FILE    of nothing  of the real composite
    of a real governing file              on disk
  is reversible                          n/a         NO — it lands with
                                                     OR-3..OR-11 or none does

THE SINGLE SENTENCE THAT SEPARATES THEM: the oracle rewrites a copy and returns
it; OR-4 rewrites the governing file and every later step depends on the result.
```

**The resolved-byte files are not created by this task.** Neither this binding,
nor the handoff, nor the oracle produces
`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md`
in post-selection form at any path.

---

## §3. `B3` — the gate ledger, and the identity disposition

### §3.1 The total ledger, current state through `T`

```text
#   GATE                                          STATE            AUTHORIZES NEXT?
 1  W-B author selection (OR-2)                   COMPLETE         yes — this binding only
      token I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
      signature ffcb4116…a7dc, 2026-08-05, base 176d609

 2  This post-selection binding                   DRAFT            no
      awaiting bounded X/Y review

 3  Watchdog authority amendment v1.7 acceptance  NOT ACCEPTED     no
      token I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7
      unsigned; §4 states exactly what it will and will not do

 4  Process identity Option A selection           COMPLETE         no
      token I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
      signature 7a8ab2da…3d1f, 2026-08-04
      recorded at XS-1 as external author state, member of no class

 5  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1  NOT ACCEPTED     no
      required to be reviewed and accepted SEPARATELY before Option A can
      become operative; §3.2 states the disposition in full

 6  The LATER COMBINED BINDING of XS-1            DOES NOT EXIST   no
      the single reviewed specification that binds the identity selection
      together with the watchdog option and resolves §P1-13.2 row 2.
      STATE: BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW, by XS-1(b)

 7  Inactive code/test implementation             CANDIDATE        no
                                                  ELIGIBILITY ONLY
      the handoff draft is a scope contract. No code may be written under it
      until gate 8 exists.

 8  Implementation authorization                  NOT GRANTED      —
      a separate author act, after gates 3 and 7 and after this binding
      survives X/Y review

 9  OR-3 key generation and Stage A               NOT AUTHORIZED   —
10  OR-4 variant resolution and amendment install NOT AUTHORIZED   —
11  OR-5..OR-9 verifier, tests, M4, M7, member list NOT AUTHORIZED —
12  OR-10 Stage B and detached signature          NOT AUTHORIZED   —
13  OR-11 install record, no-replace, last        NOT AUTHORIZED   —
14  One-shot atomic-handoff authorization         NOT GRANTED      —
      a separate author act; OR-3..OR-11 land together or none does (H-1..H-3)
15  T activation                                  NOT AUTHORIZED   —

T = NOT_ACTIVATED.  PROGRAMME CLAIM = OPEN.
```

Gates 9 through 13 are **not fourteen independent permissions**. `H-1` makes
the amendment and the composite one indivisible acceptance unit; `H-2` and
`H-3` make `OR-1`..`OR-11` a mandatory operator obligation that lands together
or not at all. They are enumerated separately here only so that a reader can
see that none of them is open.

### §3.2 The identity-token disposition, resolved from the bytes

**The question:** may the inactive implementation include observation-only
identity code while `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` is
unaccepted?

**The answer, and it is stricter than the fail-closed minimum:**

```text
NO CODE. NOT DISABLED CODE, NOT GATED CODE, NOT DUMMY-TESTED CODE. THE
IDENTITY-OBSERVATION SURFACE IS OUT OF SCOPE FOR THIS IMPLEMENTATION
ENTIRELY, AND THE REASON IS NOT CAUTION — IT IS THAT THE GOVERNING PAIR DOES
NOT DEFINE IT.
```

The exact clauses, and the mechanical fact that settles it:

```text
C-1  THE MECHANICAL FACT. The strings attested_pid and attested_pgid occur
     ZERO times in composite v1.10 and zero times in amendment v1.7. There is
     no schema, no key, no type, no carrier, no consumer and no destination for
     an identity observation anywhere in the governing pair. An implementer
     cannot write conforming identity-observation code from these bytes,
     because these bytes say nothing about it.

C-2  composite §P1-13.2 row 2, quoted at the composite's own Cell 1:
     "The layer that must write those two keys therefore cannot obtain their
     values." The composite states TWO coherent repairs exist, that choosing
     between them CHANGES SIGNED MEANING, and — verbatim — "This document
     chooses neither and invents no value." Writing identity-observation code
     now would choose one of the two. THAT IS THE INVENTION THE CELL FORBIDS.

C-3  composite Cell 1 blocking notice: "This version is not acceptable as an
     operative object until the author cell
     AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is signed." The Option A
     signature "does not unblock this cell and does not make this version
     operative." THE BLOCKING NOTICE STANDS UNCHANGED.

C-4  amendment XS-1(b): the later combined binding MUST "record the separate
     review and acceptance of P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1,
     OR REFUSE TO PROCEED." That obligation attaches to the COMBINED BINDING.

C-5  amendment N-13 and N-4: this amendment "neither selects nor repairs the
     process-claim identity fields", and "does not become operative because an
     identity option was selected."

C-6  identity selection signature, outstanding gates: the bounded weakening
     "must be reviewed and accepted separately before Option A can become
     operative."
```

**Why this does not block the W-B binding.** The W-B route needs no identity
field. `§P1-10.7` computes the classifier's scope **from the PCS's own handle
table**, and row 89 confirms it: site (b) runs "against the scope computed from
the PCS's own handle table". The opaque `handle_id` remains the only
addressable process name under the signed Option A contract. **The W-B
implementation surface is identity-free by construction**, so excluding
identity code costs the W-B implementation nothing and invents nothing.

**The disposition, stated as three separable states so that neither is
smuggled into the other:**

```text
D-A  THE W-B POST-SELECTION BINDING          not blocked by identity
D-B  THE W-B INACTIVE IMPLEMENTATION SCOPE   identity-observation code EXCLUDED
                                             — no code, no dummy test, no
                                             disabled path, no enum value, no
                                             schema key
D-C  THE LATER COMBINED BINDING OF XS-1      BLOCKED_PENDING_IDENTITY_
                                             WEAKENING_REVIEW, by C-4
```

`D-C` is a **ledger state of a document that does not exist**, recorded here so
that it is auditable rather than silent. **It is not this document's closure
token.** The closure token is stated once, in the companion closure, and this
sentence does not state it.

**What no future step may do without a separate accepted token.** No install
path, no activation path, no verifier configuration, no manifest field and no
test fixture may make an identity observation operative, may set or default an
`attested_pid` or `attested_pgid`, or may treat the Option A signature as
having accepted the bounded weakening. The verifier's behaviour if such a
surface is ever added is stated in the handoff: **refuse, before any production
action.**

---

## §4. `B6` — the acceptance and authorization boundary

The only watchdog amendment acceptance token available after a bounded X/Y
review round is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7
```

### §4.1 What that future token accepts

```text
A-1  THE TWO GOVERNING FILES AS ONE INDIVISIBLE UNIT — the v1.7 amendment and
     composite v1.10, at the exact digests of §0.2, per H-1. Neither is
     operative alone and accepting one without the other is not a conforming
     state.
A-2  THE 155 TAGGED NORMATIVE RULES, the 10 acceptance-predicate conjuncts, the
     6 freeze-sequence steps, the 2 named entry routes and the 12 swap-only
     state-machine units of file 1; the 23 carried behavioural repairs, the 4
     new normative sections, the 3 guard rules and the 24 test rows of file 2.
     239 governing loci, delta zero from v2.9.
A-3  THE FIXED ACCOUNTING — MS-2 at 55, MS-3 at 7, MS-8 at 69, member classes
     7, closed failure codes 25, pre-production checks 15, M4 key set 21,
     IR-13 at 50 rows, MS-13 element keys 6 with 8 effect booleans each, 32
     effect assertions all false, 4 project-import dependencies, 7 unexecuted
     module-scope branches, 63 composite provenance rows, the 16-member
     generic_harness.py scoped allowlist, and the 89-row reachable_closure at
     CANON length 20534.
A-4  THE OBLIGATION SHAPE OF OR-1..OR-11 — that this is the sole conforming
     construction procedure, and that it is an operator obligation the
     final-state gate does not reconstruct (FS-1..FS-5).
```

### §4.2 What that future token does **not** authorize

```text
B-1   IT DOES NOT START OR-3. No key pair, no entropy draw, no Stage A.
B-2   IT DOES NOT EXECUTE OR-4. No variant block is resolved by accepting the
      amendment; the composite's bytes do not move.
B-3   IT DOES NOT INSTALL CODE. No verifier at MS-5's path, no test module at
      either MS-6 path, no edit to any production root.
B-4   IT DOES NOT WRITE M4, M7, THE MEMBER LIST, STAGE B, THE DETACHED
      SIGNATURE OR THE INSTALL RECORD.
B-5   IT DOES NOT RUN THE TEST MATRIX. OR-7 is a separate step.
B-6   IT DOES NOT ACTIVATE T, open a candidate, draw a datum, produce an
      outcome, move a Proof or move the programme claim.
B-7   IT DOES NOT ACCEPT P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, make it
      signable, or predict it. It does not resolve §P1-13.2 row 2 and it is not
      the combined binding of XS-1.
B-8   IT DOES NOT RETROACTIVELY VALIDATE ANY EXISTING WORKING-TREE CODE. See
      the handoff's audit obligation.

TWO FURTHER AUTHOR ACTS ARE REQUIRED AFTER IT, AND THEY ARE SEPARATE FROM EACH
OTHER:
  (i)  an IMPLEMENTATION AUTHORIZATION, permitting inactive code and tests to
       be written at the handoff's allowed paths;
  (ii) a ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION, permitting OR-3..OR-11 to run
       once, together, in order.
NEITHER IS GRANTED BY THE ACCEPTANCE TOKEN, AND NEITHER IS GRANTED HERE.
```

---

## §5. `B5` and the residual findings

### §5.1 The provenance residual — the four deferred `MS-2` rows

The confirmed v2.10 ruling is carried **unchanged**: the four rows are
**bounded accounting, not a fail-open.**

```text
WHAT IS TRUE NOW. Every earlier supersession added four rows to MS-2 — the
replaced amendment, the replaced composite, and the two independent
confirmations of the round that replaced them. v2.10 ADDED NONE, BY A DECLARED
SCOPE DECISION recorded at packet §0.2 and in the governing bytes at N-14.

  MS-2                55   MS-3   7   MS-8   69
  TS-3 member_count literal          69
  composite provenance region        63 rows

WHY IT IS NOT A FAIL-OPEN. MS-2 states that its literal list IS M2 — never that
it contains every superseded document. DA-1's historical-evidence rule governs
what is NOT OPENED FOR BEHAVIOUR, not what is a member. Nothing is admitted
that would otherwise be refused; the four documents are not opened for
behaviour either way. The omission is DECLARED at N-14 with the digests the
rows will carry, so it is auditable rather than silent.

THE FOUR ROWS, WITH THE DIGESTS THEY WILL CARRY:
  d5e1d4dbd7731bd6a154c423b36f41e60de771d5ff635423b608bba02d88640f  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md
  3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md
  588fe8a23fd56a4366f920d4b1463d00ee3e7bd8bbc4cc1cbaca61b89a12f489  reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md
  6d83e9b2f082354917b134955d35b8b8f1fdf76761b368c8d34ffae3cd99cf66  reviews/sol_officina_p1_watchdog_v2_9_final_y_confirmation.md
```

**Where they enter, decided here without editing historical `MS-2`:**

```text
PR-1  THEY DO NOT ENTER AT OR-4, OR-6, OR-9 OR OR-11 OF THIS GENERATION.
      This generation's install enumerates 69 members from MS-1..MS-7 alone,
      with MS-2 at its literal 55 and the TS-3 member_count literal at 69.
      Adding a row during the handoff would break CK-4's enumeration, CK-13's
      D1/D2 partition, B7's member_count-is-69 structural check and B17's
      external count binding at CK-14. THE HANDOFF DOES NOT TOUCH THEM.

PR-2  THEY ENTER AT THE FIRST ACTUAL POST-SELECTION GENERATIONAL ROUND — the
      next round that REPLACES the governing pair rather than resolving it.
      Resolving variant blocks at OR-4 is NOT such a round: OR-4 produces the
      post-selection bytes of the SAME generation at MS-1's SAME two literal
      paths, and replaces no document.

PR-3  AT THAT ROUND THEY ENTER TOGETHER WITH THAT ROUND'S OWN FOUR ROWS, not
      alone. A round that replaces v1.7/v1.10 adds the v1.7 amendment, the
      v1.10 composite and its own two independent confirmations, PLUS these
      four. MS-2 would go 55 -> 59 -> 63 in one step if both sets land
      together; the arithmetic must be done once, in that round's own bytes,
      and this document does not perform it.

PR-4  THE IMPLEMENTATION HANDOFF MUST NOT PRETEND THEY ARE MEMBERS. No fixture,
      no test row, no manifest field and no member enumeration in the inactive
      implementation may include any of the four. A fixture that enumerates 59
      or 73 members FAILS against this generation. This is stated as a negative
      test obligation in the handoff.

PR-5  NO HISTORICAL BYTE IS EDITED BY ANY OF THIS. MS-2's literal list is
      byte-unchanged from v1.6, and this document changes nothing in it.
```

### §5.2 Findings against the governing pair, raised not resolved

These were found while building the bridge. **This document repairs none of
them**, proposes no regeneration, and is not an independent review. They are the
first items of the companion closure's bounded X/Y question set.

```text
F1  MAJOR, FAIL-OPEN DIRECTION. THE TWO COPIES OF THE HANDOFF DISAGREE ON THE
    RANGE OF THE PRE-PRODUCTION CHECK.
      amendment §A9 H-3, line 1149:
        "§A10's pre-production check is the enforcement point, it is
         `CK-1`..`CK-12`"
      amendment §A10 itself defines CK-1 through CK-15 — fifteen rules.
      amendment line 1202: "the final-state pre-production check
        (`CK-1`..`CK-15`)"
      composite §P1-14.8 H-3: "Its fifteen checks run in the literal
        topological order of VP-4"
      packet v2.10 §6.1: "PRE-PRODUCTION CHECKS  15  UNCHANGED"
    §A9 and §P1-14.8 EACH CLAIM the handoff is stated "IN FULL and
    IDENTICALLY" in the other, and H-2 says "no two statements of it can
    disagree". They are not byte-identical and they disagree here.
    WHY IT MATTERS AND WHY IT IS NOT COSMETIC. A verifier implemented against
    §A9's range omits CK-13, CK-14 and CK-15 — the D1/D2 member partition with
    MEMBER_EXTRA retired, and CK-14, which carries B14, THE CLAUSE THAT BINDS
    THE SELECTED OPTION TOKEN ACROSS THE TWO STAGES. B14 is precisely what
    makes a signed W-B token bind, so this defect sits on the W-B critical
    path. The omission direction is FAIL-OPEN: three checks silently not run.
    NOT REPAIRED HERE. Exit discipline reserves regeneration to an independent
    reviewer's counterexample against the v2.10 bytes; this author line may
    only report it.

F2  MAJOR, BLOCKS EXACT IMPLEMENTATION OF THE W-B CLASSIFIER SCOPE.
    KV-1..KV-6 IS REFERENCED OPERATIVELY AND DEFINED NOWHERE IN THE GOVERNING
    PAIR.
      composite §P1-10.7 SCOPE: "computed from the PCS's own handle table,
        under KV-1..KV-6 re-evaluated before every _killpg"
      composite §P1-15 row 89 site (b): the same constraint
      The token "KV" occurs EXACTLY TWICE in composite v1.10 — both are these
      references — and ZERO times in amendment v1.7 and ZERO times in packet
      v2.10.
    ITS ONLY FULL DEFINITION survives at §3.4 of
      successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
    — a superseded packet draft that is a member of nothing, is not the
    governing packet, and is not opened for behaviour.
    WHY IT MATTERS FOR THIS TASK SPECIFICALLY. W-B makes the PCS classifier
    the sole group-stop executor for the endpoint-loss route. Its per-group
    kernel verification is the safety property that keeps the classifier from
    signalling the PCS's own group, a watchdog leader group or the supervisor
    group (the KV-6 GROUP_FORBIDDEN_TARGET case). An implementer working only
    from governing bytes cannot write it, and must not invent it.
    CONSEQUENCE, CARRIED INTO THE HANDOFF: the classifier scope predicate is
    marked NOT IMPLEMENTABLE and is fenced. Cursor may not reconstruct it from
    the superseded packet, from an earlier composite, or from inference.

F3  MINOR, LOG. A FIFTH GENERATION-SCOPED STRING IN AN OPERATIVE CLAUSE.
      amendment §A10 OR-4, line 3456: "the other branch is DELETED; THE V1.3
      AMENDMENT IS INSTALLED."
    MS-1 names the v1.7 amendment. §A9's audit enumerates "the four places a
    generation number appears in an OPERATIVE clause" — MS-1's two paths,
    TS-1's three pre-selection paths, the §A0.4 token and the A16(d) token —
    and OR-4's is a fifth. It is the same class as the v2.9 X-line finding B-1
    and as packet §1.4, and packet §8 item 2 predicted exactly this
    ("if v1.6 could carry two incomplete re-scopes, v1.7 could carry a third").
    WHY IT IS MINOR RATHER THAN MAJOR: OR-4 is an operator obligation that the
    final-state gate does not verify (OR-1, FS-2), and MS-1's literal paths —
    not OR-4's prose — determine which amendment is installed and are what
    CK-7 and CK-13 check. No byte state is made unsatisfiable. It is logged
    because the §A9 audit's completeness claim is falsified by it.

F4  MINOR, LOG. A §-LOCATOR POINTS AT THE WRONG SUBSECTION.
      composite line 90: "the verifier refuses it (`G-10`, §P1-14.3)"
    G-10 is defined at composite line 2982, inside §P1-14.4, which begins at
    line 2941; and composite line 2923 itself says G-10 is "the
    unresolved-variant-block guard of §P1-14.4". §A9's audit checks only that
    each §P1- reference names a section that EXISTS as a heading, which
    §P1-14.3 does, so the audit as written passes over the error. No operative
    ambiguity follows — G-10 is reserved uniquely and is unambiguous by name.
    NOTE: line 90 sits at line 90, outside REGION(BODY), so this locator is not
    covered by H_BODY or H_NORMATIVE, only by H_FILE.
```

---

## §6. Negative space

This draft creates nothing executable. It authorizes no selection, no X/Y
verdict, no amendment acceptance, no identity-token acceptance, no identity
bounded weakening, no implementation, no commit, no verifier or manifest edit,
no key generation, no entropy draw, no selection artifact, no authorization
artifact, no detached signature, no attestation, no install record, no
resolved amendment or composite bytes at any path, no process, socket, pipe,
fork, exec, signal, wait or `prctl` operation, no supervisor, PCS, controller,
worker or watchdog, no capability, world, learner, candidate, trajectory,
capacity artifact, custody disposition, result manifest, spend, datum, outcome,
Proof or claim movement.

No freeze was executed, requested, journalled or witnessed. No `/proc` was read
against any live process. No clock was sampled for any contract purpose. No
Philosophia production or project module was imported, executed or compiled.
**No existing file was modified: no historical or governing document, no code,
no test, no signature, no runtime artifact and no prior review.** The untracked
working-tree `generic_harness.py` was read only to establish the audit facts
recorded in the handoff; it was not adopted as evidence and not edited.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.7 = NOT ACCEPTED
IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This draft,
the companion handoff and every author closure are untrusted self-assessments
and are normative for nothing.
