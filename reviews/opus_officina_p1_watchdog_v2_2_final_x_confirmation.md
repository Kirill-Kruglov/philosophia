REVISE_OFFICINA_P1_WATCHDOG_V2_2

# Final X-line confirmation — Officina P1 watchdog-freeze author choice, v2.2

**Reviewer:** Claude Code Opus, independent X-line adversarial reviewer.

**Scope.** Bounded final confirmation of the v2.2 correction on identical bytes.
Not a new design round. I read the v1, v2, v2.1 and v2.2 watchdog packets, the
v2/v2.1/v2.2 closures, all prior Opus and Sol watchdog reviews and
confirmations, the signed supervisor-control chain (v2 draft through
v2.1.10.7), the P1 binding, the P1 operative composite v1.2, the accepted
generic-harness contract chain, the batch-settlement chain, and the supervisor
author-choice packet and signature. **No existing file was modified. Nothing was
committed.** No process, socket, pipe, fork, exec, signal, freeze, spend, datum,
outcome, Proof or claim movement was authorized or performed.

**Reading of the verdict tokens.** The bounded question instructs that an
omitted live governing locus be treated as blocking. I found one, and the
author choice is therefore **blocked on the present bytes**. I emit
`REVISE_OFFICINA_P1_WATCHDOG_V2_2` rather than `BLOCKED_…` because the smallest
exact replacement is available below, lands inside the existing common token
`P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, and requires no new mechanism, no
new author cell and no new token. `BLOCKED_…` is reserved for a defect the
freeze cell has no authority to repair. This is not that.

---

## Custody — recomputed, not accepted

```text
651dba04592b16ee2899cfd3e3368ecbf0dd462b371b87644968acf5737c77f4
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
  RECOMPUTED AND MATCHES the digest stated in the bounded question.

947ed6a954f87eb3971218f9fa2bfa6461999a9a099eb182bc0a09b2f505eed2
  …_V2_1_CORRECTION.md — matches v2.2 §0.1's BASE digest.
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505
  …_V2_DRAFT.md — matches v2.2 §0.1's BASE digest.

ALL TWENTY-FIVE digests of v2.2 §1.8 were recomputed. All reproduce
byte-for-byte. No custody discrepancy anywhere in the peer chain.
```

**Citation slip in the bounded question itself, recorded and immaterial.** The
governing-material list names
`successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_CORRECTION.md`.
No such file exists. The v2 document is `…_V2_DRAFT.md`
(`72212a98…`), which v2.2 §0.1 cites correctly and which I read in full. **No
finding in this confirmation turns on the slip.**

---

## Determination

### X22-C1 — BLOCKING, NEW, X-LINE ONLY. §W6.5 is a forty-first tier-1 governing locus, it is omitted from the declared forty, and it assigns the watchdog both freeze **execution** and freeze **recording**

This is the locus the bounded question asked the X line to look for. It exists.

**Where it is.**
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
(`9f1d018e…`) `:1331-1342` — the file v2.2 declares tier 1 and edits at fourteen
loci `PW1`..`PW14`. §W6.5 is not one of them.

**What it says, verbatim on the committed bytes (`:1331-1342`):**

```text
### W6.5 Explicit supersession of the signed predecessor sentence (X-M9i)

Signed harness §5a reads: "The watchdog owns the deadline and **executes
the v2.1 §1 sequence at or before it**." That sentence is **explicitly
superseded** by §W3.1/§W3.3/§W3.4: on non-real-time Linux the watchdog
owns the deadline and executes the sequence **as soon as it is
scheduled after the deadline**, records the conservative proved-freeze
instant, and every positive overrun is routed to the signed
invalid/recovery destinations with full §4c charging. The signed
sentence is not contradicted by silence; it is named, superseded, and
its guarantee replaced by a weaker, true, fail-closed one. Nothing else
in §5a moves.
```

**This is not a quotation locus.** The first sentence quotes §5a. The second
sentence is the **operative supersession rule**, and its replacement text
re-assigns the executor to the watchdog in the post-supersession formulation:
*"the watchdog owns the deadline and executes the sequence … records the
conservative proved-freeze instant."* That is a freeze **executor** assignment
and a freeze **evidence-recording** assignment in one sentence — precisely the
two authorities `PA-1` and `PA-5` claim to have removed everywhere.

**It passes v2.2's own `AUTH-2` test more strongly than any of the declared
forty.** `AUTH-2` makes a section operative iff a currently governing document
carries or references it as a live rule and no later document replaces it.
§W6.5 is carried by name, as a live rule, in at least ten places, and is
replaced nowhere:

```text
…V2_1_1_CORRECTION.md:124   §Z0's carry-forward list names "§W6.1, §W6.3,
                            §W6.4, §W6.5, §W6.6" as carrying "forward verbatim"
…V2_1_1_CORRECTION.md:125   also carries "§W11's compatibility classification"
                            verbatim — the paragraph that names §W6.5 again
…V2_1_2_CORRECTION.md:106   carry-forward list names "§W6.1, §W6.3–§W6.6"
…V2_1_3_CORRECTION.md:1382  "except §W6.5's explicitly named supersession of
                             harness §5a's physical …"
…V2_1_4_CORRECTION.md:1114  same sentence
…V2_1_5_CORRECTION.md:663   same sentence
…V2_1_6_CORRECTION.md:776   same sentence
…V2_1_7_CORRECTION.md:836   same sentence
…V2_1_8_CORRECTION.md:1414  same sentence
…V2_1_9_CORRECTION.md:1194  "Protocol amendments: §W6.5's carried supersession
                             of harness §5a; …"
…V2_1_10_CORRECTION.md:1457 "Protocol amendments: §W6.5's carried supersession
                             of harness §5a; …"

A grep of the whole chain for a REPLACEMENT of §W6.5 returns nothing. Every
occurrence is a CARRY.
```

§W6.5 is not merely operative under `AUTH-2`. It is **the single named protocol
amendment that the entire correction chain declares itself to make over the
signed harness composite.** Eight successive corrections define their own
compatibility classification by reference to it. If any peer-chain section is
tier 1, this one is.

**Why it is blocking, not cosmetic.** `PH1` replaces harness §5a with *"The
watchdog owns the deadline and OBSERVES it. It executes no step of the v2.1 §1
sequence. The SUPERVISOR executes that sequence …"*. After the §7 item 6c
handoff lands, the two texts stand in direct opposition:

```text
harness §5a as amended by PH1  the watchdog executes NO step; the supervisor
                               executes the sequence and writes the observation
§W6.5, unamended               §5a's sentence "is explicitly superseded" by a
                               rule under which "the watchdog owns the deadline
                               and executes the sequence … records the
                               conservative proved-freeze instant"
```

§W6.5 is not a peer of §5a — it is **the supersession rule over §5a**. A reader
who follows the chain's own compatibility classification reaches §5a *through*
§W6.5 and therefore reaches the watchdog-executes reading. `PH1`'s stated
justification — *"this is the only sentence in the accepted harness contract
that names a freeze executor"* — is true of the harness contract and does not
close the §5a surface, because the sentence that governs §5a's supersession
lives in the control-channel chain and is untouched. **This is a live historical
authority and a hidden second executor/writer, which is exactly what the bounded
question asks to be excluded.**

**Why the author's method missed it, stated so the method can be fixed rather
than merely the locus.** `O-9` declares the search method: grep `watchdog`
within 80 characters of `freez|writ|observ|witness|settle`. §W6.5's executor
assignment uses the verb **`executes`** and the noun **`records`**, and the
subject and verb straddle a line break (`:1335` ends "…the watchdog", `:1336`
begins "owns the deadline and executes the sequence"). No token of the five-word
action alphabet falls inside either window. **The alphabet has a structural
blind spot for `execut`, `kill` and `quiesc`.** Re-running the identical method
with the alphabet extended to
`freez|writ|observ|witness|settle|execut|kill|quiesc` surfaces §W6.5
immediately; that is how I found it.

The gap is compounded by a second omission. §1.6 closes the audit "in both
directions" by listing sections checked and confirmed clean — but its list
enumerates `§Z1, §Z2, §Z3, §Z5..§Z9, §N1..§N4, §N6..§N9, §U1, §U2, §U4..§U6`
and **names no §W section at all.** §W6 is therefore neither tier 1, nor tier 2,
nor checked-and-retained. It fell through the classification entirely.

**Two companion loci in the same file, same defect class, same file, same
step.** Both are the §W6.5 sentence restated where the chain records its own
amendments:

```text
:88         §V2.0 replacement-index row —
            "| §V2.0 replacement index | **extended** by §W6.5: signed harness
              §5a's 'executes the v2.1 §1 sequence **at or before it**' is
              explicitly superseded |"
            This is the SAME CLASS of locus as PW10 (:113), which v2.2 does
            replace. Replacing one index row and not the other is not defensible
            on any rule stated in the packet.

:1582-1586  §W11 compatibility classification —
            "It contains no protocol amendment to the signed composite except
             the **explicitly named** supersession of harness §5a's physical
             at-or-before-deadline sentence (§W6.5), which replaces an
             unattainable guarantee with a weaker, true, fail-closed one …"
            Carried verbatim by …V2_1_1_CORRECTION.md:125.
```

#### The smallest exact replacement — three loci, one file, no broadening

These are additions to `§1.4`'s `PW` block. **No new mechanism, no new option,
no new author cell, no new token, no schema change, no test-matrix mechanism
change.** They are carried by the existing
`P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` exactly as `PW1`..`PW14` are.

```text
PW15  :1331-1342  §W6.5 body — REPLACE (the heading and its X-M9i attribution
      are RETAINED byte-unchanged):

      "Signed harness §5a AS AMENDED BY PH1 reads: 'The watchdog owns the
       deadline and OBSERVES it. It executes no step of the v2.1 §1 sequence.
       The SUPERVISOR executes that sequence …'. The residual PHYSICAL TIMING
       guarantee — that the sequence completes at or before the monotonic
       deadline — is **explicitly superseded** by §W3.1/§W3.3 AS AMENDED/§W3.4:
       on non-real-time Linux the SUPERVISOR executes the sequence **as soon as
       it is scheduled after the deadline**, records the conservative
       proved-freeze instant ITSELF, and every positive overrun is routed to the
       signed invalid/recovery destinations with full §4c charging. THE
       SUPERSESSION IS OF THE TIMING GUARANTEE ONLY. The ACTOR is fixed by PH1
       under `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, and no reading of this
       section restores a watchdog executor, a watchdog quiescence proof or a
       watchdog evidence writer. The signed sentence is not contradicted by
       silence; it is named, superseded, and its guarantee replaced by a weaker,
       true, fail-closed one. Nothing else in §5a moves."

PW16  :88  §V2.0 replacement-index row — REPLACE:

      "| §V2.0 replacement index | **extended** by §W6.5 AS AMENDED: signed
        harness §5a's 'executes the v2.1 §1 sequence **at or before it**' is
        explicitly superseded AS TO TIMING; its ACTOR is reassigned from the
        watchdog to the supervisor by PH1 under
        `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` |"

PW17  :1582-1586  §W11 compatibility classification — REPLACE the clause:

      "… except the **explicitly named** supersession of harness §5a's physical
       at-or-before-deadline sentence (§W6.5 AS AMENDED), which replaces an
       unattainable TIMING guarantee with a weaker, true, fail-closed one AND,
       under `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, reassigns that
       sentence's ACTOR from the watchdog to the supervisor; it moves no
       constant, event, schema, root, or scientific cell."
```

**Consequential bookkeeping, stated exactly so the author does not have to
re-derive it** (valid under the packet's own authority partition; see `X22-C2`,
which may change the membership rule again):

```text
§1.4 PW block        fourteen  →  SEVENTEEN
§1.7 peer tier-1     40        →  43   (1 PH + 17 PW + 7 PZ + 5 PN + 3 PU + 10 PB)
§1.7 peer reopened   45        →  48   (43 reassignment + 5 rename)
§1.7 governing       62        →  65   (22 composite + 43 peer)
§8 blast-radius rows "forty-five / forty-five" → "forty-eight / forty-eight";
                     the row still falls IDENTICALLY on W-A and W-B — none of
                     PW15..PW17 has an option variant, so THE RECOMMENDATION
                     DOES NOT MOVE.
§1.9 test 106        "enumerates the sixty-two replaced loci" → "sixty-five",
                     and its static-check scope must add §W6 and §W11 to the
                     enumerated sections.
§1.6                 add a §W checked-and-clean list. §W3.1 (:701-704) and
                     §W3.2 (:706-742) I verified independently: ack,
                     publication and liveness only, NO executor or
                     evidence-writer statement. Clean.
§6 O-9               the stated method's action alphabet must read
                     `freez|writ|observ|witness|settle|execut|kill|quiesc`.
                     The five-word alphabet is what produced this miss and
                     re-running it would reproduce the miss.
```

---

### X22-C2 — BLOCKING. `AUTH-3` classifies the P1 binding as tier-1 operative text, but the composite makes it provenance; and three later chain documents are unaccounted for entirely

I reached this independently and it **concurs with the Y line's determination 1**,
which states the general form. I record the specific bytes that decide it for the
binding, because the binding is where the packet's own carve-out fails on its own
terms.

**On the bytes.** Composite v1.2 `:42-49`, level 3: *"Every earlier
supervisor/control-channel document — the two drafts, the corrections v2.1
through v2.1.10.7, and versions 1 and 1.1 of this composite — is immutable
historical and provenance evidence only. … They appear in §P1-18's provenance
region by path and digest and nowhere else."*

`…V2_1_10_4_P1_BINDING.md` appears in composite `:2851` — inside §P1-18
PROVENANCE, by path and digest — **and nowhere else in the composite.** That is
exactly the disposition level 3 assigns to a historical document.

**`AUTH-1`'s carve-out cannot rescue it.** `AUTH-1` argues that level 3 is about
the P1 boundary and not the peer boundary, and that §W/§Z/§N/§U survive because
the peer contracts "own functionality outside the P1 boundary". Whatever its
merit for the peer sections, **the binding is entirely P1-boundary text** — its
sections are §P1B.7.1, §P1B.8.2, §P1B.9, §P1B.13, and its invariants are 451,
452, 453, 458. It is the precise class of document `AUTH-1` concedes level 3
governs. `AUTH-3` nonetheless lists it as OPERATIVE tier 1 and calls it "the
current P1 binding".

**It is not even the last P1 document of the historical chain.** Three later
documents exist and are named in level 3's own range:

```text
…V2_1_10_5_P1_PRE_XY_REPAIR.md            702 lines, composite :2852
…V2_1_10_6_PRE_XY_REPAIR.md               513 lines, composite :2853
…V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md   520 lines, composite :2854
```

**None of the three is mentioned anywhere in v2, v2.1 or v2.2** — not as tier 1,
not as tier 2, not in §1.6's checked list, not in §1.8's custody block. I swept
all three: their watchdog occurrences are a signed-token recital
(`C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER`, the class of `T2-18`),
a PCS reap/first-ack-timeout row, and a `_killpg` call-site reachability
sentence — **no freeze-executor or evidence-writer assignment.** So this is a
completeness defect in the inventory, not a further hidden executor. But it
falsifies the claim that 10.4 is "the current" P1 binding, and it shows the
enumeration did not reach the end of the chain it classifies.

**The operational contradiction.** `AUTH-4` states that editing tier-2 historical
evidence "would destroy the evidentiary record and would itself be a defect", and
`N-9` restates it. Yet §7 items 6b and 6c **mandate ten replacements inside the
binding**, and item 10 mandates recomputing the composite's §P1-18 provenance
digests to match — which is the definition of destroying the evidentiary bytes
`AUTH-4` claims to protect. The packet cannot both forbid and require the edit.

**Consequence for the accounting.** The arithmetic reproduces exactly — I
verified it — but it is a list cardinality, not an authority cardinality:

```text
1 PH + 14 PW + 7 PZ + 5 PN + 3 PU + 10 PB          = 40   reproduces
40 + 5 rename (K1..K5)                             = 45   reproduces
22 composite + 40 peer                             = 62   reproduces
T2-1 .. T2-18                                      = 18   reproduces
K1..K5 (:866,:900,:906,:1370,:1416) vs
  PN1..PN5 (:130,:883-886,:890-894,:1318,:1353)    DISJOINT — verified
six peer files carrying tier-1 text, seven with
  the composite                                    reproduces
```

If the binding is provenance, `PB1`..`PB10` are not governing replacements and
the figures become 30 / 35 / 52 / 28. **Both readings are internally coherent;
the packet asserts one and violates it.** This must be settled by a stated
document-level rule before any count can be confirmed, and before an author
choice can rest on the claim that the surface is exhaustively repaired.

**Minor, same class:** §1.8's custody block omits
`…V2_1_10_2_CORRECTION.md`, although `AUTH-3` and `T2-10` both cite it at
`:925`. Add its digest.

---

### X22-C3 — BLOCKING. `PH1` and `PW2` open an ordinary-deadline supervisor write route that `R2`/`R9`/`R10` and `PA-1` do not admit

Independently verified; **concurs with the Y line's determination 3.** I record
the confirmation because it bears directly on the "hidden second writer"
question and because the X and Y lines agreeing on it removes any doubt.

```text
PW2 :746   "When the SUPERVISOR's clock shows `now_ns ≥ deadline_ns` for a
            lease row, under `T_RUNTIME.lock`:"
              — this fires at EVERY lease deadline, with the watchdog alive.

PH1 §5a    "The SUPERVISOR executes that sequence … AT OR BEFORE THE DEADLINE
            … and writing the one freeze observation itself."
              — likewise an ordinary-deadline route.

versus

v2.1 R10   the freeze-witness function is "called from the supervisor's
            dead-watchdog route ONLY"          (verified verbatim in v2.1 §2.4)
v2.1 R9    row 4's executing process is the supervisor "on the signed
            dead-watchdog route"
PA-1       written "on the signed dead-watchdog route"
PW11/PZ5/  writer cell: "on the dead-watchdog route; the watchdog has no path
PN5         here"
PA-5       "exactly the two of v2.1 R21" — and neither is classified as an
            ordinary-deadline entry
```

The reassignment removes the watchdog executor but leaves the supervisor's
**ordinary-deadline** entry unnamed in every writer/executing-process/function
table and in invariant 89. Either that entry is admitted and bounded in
`R2`/`R9`/`R10`/`R17`/`R21` and the execution-site count restated, or `PH1`/`PW2`
must not open it. As it stands the object written at an ordinary deadline has no
stated admissibility, no stated route and no governing execution-site invariant.

---

## What I confirm, without qualification

### 3 — `killer == WATCHDOG` is unreachable on every new-contract path (subject to X22-C2's authority question)

I enumerated **every** occurrence of `killer` across the harness chain, the
supervisor/control chain, the binding and the composite, and traced each.

```text
WRITER SIDE — closed.
  R10 (retained verbatim)  the peer freeze-witness function has EXACTLY ONE
                           caller, "the supervisor's dead-watchdog route only",
                           "setting `killer` from its caller" ⇒ SUPERVISOR
  PA-1 / PW4 / PZ2 /       one writer, named, on every table row
  PW11 / PZ5 / PN5
  PW9 (:831)               the supervisor's route sets `killer = SUPERVISOR`
  PB1..PB10, PW6, PW8      every watchdog path is now WRITE-NOTHING-AND-EXIT
  ⇒ no code path constructs a record with killer == WATCHDOG.

PREDICATE SIDE — closed.
  PZ3   §Z4.6 conjunct 8, currently "killer == WATCHDOG only if the current
        generation's watchdog was live by its §Z3.6 fork-child record …"
        (verified verbatim at …V2_1_1:1049-1051), is REPLACED by
        "killer == SUPERVISOR", with WATCHDOG given no admissible writer,
        made permanently non-evidence, and routed to §N5 with
        rejection_conjunct = 8.

DEFAULTING / RECOVERY / MIGRATION — none found.
  I searched the archival, recovery, takeover, replay and settlement surfaces
  for any clause that DEFAULTS, COERCES, MIGRATES or GRANDFATHERS a killer
  value. There is none. §Z11's prior-generation row (…V2_1_1:1729) routes a
  prior-generation witness to UNKNOWN via conjunct 3 — a REJECTION, permitted
  by the bounded question's own rule. The fallback object carries a fixed
  literal killer ("SUPERVISOR") at …V2_1_2:868 and cannot carry the other value.

ENUM RETENTION — correct and correctly justified.
  The enum survives at …V2_1:780, …V2_1_1:1010 and composite :2245. N-10 and
  PA-2 keep it deliberately, and test 104 fails a fixture that narrows it to
  {SUPERVISOR}. Retaining a value that every validity rule rejects is the
  stronger discipline: it preserves the ability to REJECT legacy evidence
  rather than failing to parse it. This matches the bounded question's rule
  exactly — the legacy value remains only where validity rules reject it or
  provenance requires it.
```

**One residual, non-blocking, recorded for completeness.**
`…V2_1_1_CORRECTION.md:1729` reads *"its witnesses fail §Z4.6 conjunct 3"* — a
presupposition that a watchdog HAS witnesses, which after the reassignment it
never does. It grants no authority (it rejects), so it is not blocking. But it
is the same class as `PW12` and `PW13`, which v2.2 does replace. If the author
opens the file for `PW15`..`PW17`, re-pointing it costs nothing and removes the
last sentence in the §Z layer that reads as if watchdog witnesses exist.

### 4 — The retained-read cluster: 22 replaced plus exactly four retained reads. `R8` grants identity observation only

All four sites reproduce verbatim at the cited composite lines:

```text
RD-1  §P1-9.2 property 8        :1452-1453  "it verifies the supervisor's
                                             identity against the supervisor
                                             identity record of §P1-13.2 row 3
                                             and never by any parent
                                             relationship"
RD-2  §P1-13.2 row 3 reader (b) :2210-2212  present verbatim
RD-3  §P1-13.7 read row         :2366       "read the supervisor identity record
                                             in the watchdog | … | peer,
                                             executing in a P1-created role |
                                             READ ONLY"
RD-4  invariant 87              :2756       a POSITIVE obligation: "a build in
                                             which the watchdog does not read
                                             it … fails"
```

`R8` as amended (§2.2) permits **exactly one** peer-layer operation and states
the negative surface explicitly: no peer-owned record emitted, no peer decision
owned, no signal, no freeze, no quiescence proof, no evidence write, no
settlement on any path. I verified this independently against the install-site
rules: a read enters no acceptance predicate, creates no durable object, and is
invisible to `SW-1`..`SW-5`, invariant 86 (wrong logical writer), invariant 88
(duplicate claim write) and §Z4.6's ten conjuncts — **all of which are stated
over install sites.** Retaining the read is also the *smaller* amendment:
deleting it would fail invariant 87 and would strand §P1-9.2 property 11's
`getppid()` prohibition, which is safe only because a record-based check exists.

Site 22 is not inflated: `R1`..`R22` cover composite `:202, 1447-1451,
1459-1465, 1469-1470, 1490, 1783-1784, 1888, 2006, 2249-2257, 2278-2287,
2337-2341, 2367, 2368, 2389-2391, 2730, 2732, 2758, 2760`; `RD-1`..`RD-4` touch
`:1452-1453, 2210-2212, 2366, 2756`, disjoint from all of them. v2.2 adds **no
twenty-third replacement**, and keeps the two classes on separate lines. §2.4's
accounting is correct. **`Y21-C2` first half is discharged. CONFIRMED.**

### 5 — `R16` process transport: three endpoints under W-A, two pipes under W-B, and the PCS never retains the update-pipe writer

Verified against the primary bytes, not against the packet's summary:

```text
W-B   composite §P1-6.2 :667-682 — the WATCHDOG column gives slot 3 "watchdog
      update pipe, READ end", slot 4 "watchdog ack pipe, WRITE end", slot 6
      "**not used; explicitly closed by a file action**", and states the slot
      set is `{3,4,5,7,8,9,10}` for WATCHDOG. TWO SEALED PIPES. Confirmed.

W-A   v2 §4.1 :574-575 — "The WATCHDOG file-action vector's explicit (CLOSE, 6)
      is REMOVED and replaced by (DUP2, h[6], 6)"; :596 gives the slot set
      `{3,4,5,6,7,8,9,10}`; :597-601 give A5W-1 (S_ISSOCK), A5W-2 (O_RDWR),
      A5W-3 (SOCK_SEQPACKET); :817 states "its three sealed endpoints at slots
      3, 4 and 6". THREE SEALED ENDPOINTS. Confirmed.

⇒ v2.1's R16 ("its two sealed descriptors", asserted for both options) IS false
  under W-A, exactly as Y21-C2 second half states, and §3.2's two variants are
  the correct minimal repair. CONFIRMED.
```

I searched specifically for the failure modes named in the bounded question —
aliasing, duplicated handles, inheritance, wrapper retention, alternate write
paths — and found none:

```text
NO ALIASING / NO DUPLICATE HANDLE
  composite :2310 — each `SPAWN_WATCHDOG` descriptor "is a pipe end whose peer
  end is held by EXACTLY THAT WATCHDOG at slots 3 and 4, AND BY NO OTHER
  PROCESS."

NO PCS RETENTION OF THE UPDATE-PIPE WRITE END  (E-D / N-2)
  composite §P1-8.7 :1396-1399 — "Immediately after a successful send the PCS
  closes its copies of the supervisor's ends UNCONDITIONALLY, in a fixed order
  … If the send raises or returns short, the PCS still holds the supervisor's
  ends AND CLOSES THEM." Both the success and the failure branch close. The
  supervisor holds the update-pipe WRITE end; the watchdog holds the READ end at
  slot 3. Update-pipe EOF — the single remaining supervisor-death detector under
  P1 (§P1-9.2 property 10, :1457-1458) — is intact under both variants.

NO INHERITANCE LEAK (W-A's new descriptor)
  composite :660-663 — "Every other PCS descriptor has `FD_CLOEXEC` set by
  construction: … `_socketpair`, WHOSE DESCRIPTORS CPYTHON CREATES
  NON-INHERITABLE". E-C's leak proof therefore stands with one more member, and
  the watchdog's end reaches slot 6 by DUP2, which clears FD_CLOEXEC on the
  destination exactly as for slots 3–10 today. File actions are per-role, so no
  controller, worker or supervisor receives it; the socketpair is point-to-point,
  so no third process can join it.

NO ALTERNATE WRITE PATH
  W-A's slot-6 socket is a SEPARATE descriptor pair carrying one constant,
  target-free `t-wd-freeze.v1` frame. It gives the PCS no channel on the update
  pipe and can neither create nor suppress update-pipe EOF. It is a P1 transport
  frame, never a peer-owned record, and never evidence.

NO ENUMERATION-ORDER REGRESSION
  W-A's retained end is created AFTER `P-f`, the PCS's only enumeration and a
  pre-fork step (composite :725-740), so `P-f`'s required set
  `{0,1,2,3,4,5,6,7,8}` is byte-unchanged. E-B is correct.
```

`E-E` is also correct and worth recording: the correction removes an
understatement that **favoured W-A**, and so cannot flatter W-B. **CONFIRMED.**

### 6 — Witness filename, `WATCHDOG/` namespace, but NOT handoff atomicity

**Filename — fully confirmed, and v2.2 is right where v2 and v2.1 were wrong.**
The supersession is on the bytes, in the governing replacement index:

```text
…V2_1_1_CORRECTION.md:174, verbatim —
  "| §W3.3 `t-freeze-observation.v1` path `WATCHDOG/FREEZE/<process_id>.json`
    | **replaced** by §Z4.5 (`WATCHDOG/FREEZE/<witness_id>.json`) |"
```

`G-SEQ-1`..`G-SEQ-5` reproduce: §Z4.5 supersedes, composite `:2235-2237` agrees,
binding `:566` and `:863` agree. v2's `W-7` "corrected" v1 **backwards** against
a superseded predecessor spelling, and v2.1's `O-8` then reported the artifact of
that error as an open conflict between two signed documents. **There is no live
discrepancy and no residual author choice.** `F-1`..`F-6` hold: `witness_id` =
SHA-256(canonical `{supervisor_generation_sha256, process_id, table_seq}`) is not
a function of who writes, so nothing about the reassignment moves object
identity, the no-replace key, replay naming, consumption order or the fallback
id. **X determination 5 and `Y21-M1` are discharged. CONFIRMED.**

**`WATCHDOG/` namespace — correct, and correctly left alone.** `O-11` discloses
the naming asymmetry and declines to repair it. I agree: renaming would move
every `witness_id` path, every archival-exclusion rule and every settlement
locator for cosmetic gain. `PW5` retains "`WATCHDOG/**` is control plane and
archival-excluded". No option and no cell depends on the name. The residual
naming sites I found — the §W3 block heading (`…V2_1:699`), the "Freezer
watchdog" row labels (`…V2_1:654`, `…V2_1_1:1674`), the "watchdog freeze" term in
test row 20 (`…V2_1:1527`, whose term `PW7` retires at §W3.4), and the
`T_WATCHDOG_QUIESCE_*` constant names — are all naming, not authority. They
assign no actor. **Non-blocking**, but test row 20's term should follow `PW7` if
the file is opened.

**Atomicity — NOT confirmed.** §7 item 6c states *subset* ordering constraints
(`PW1`..`PW9` in one step; `PZ3`/`PZ4` with `PN2`/`PN3`; the three durable-object
rows agreeing byte-for-byte) and item 6c/6a/8/10 add per-file conditions. **No
rule anywhere requires the composite, the six peer files, the manifest digests
and the test rows to land all-or-none as one reviewed version.** Subset ordering
is not atomicity. This matters more than usual here because item 10 mutates the
composite's §P1-18 provenance digests: a partial landing leaves the manifest
disagreeing with the files it certifies. **Concurs with the Y line's
determination 2.** A single all-or-none handoff clause is required.

### 7 — No regression, and no authorization of anything

**No regression.** I re-checked §5.2's table against the sources rather than
accepting it:

```text
_CLOCK_MONOTONIC pin, B-1..B-8, S-25, tests 92-95      UNCHANGED
common §3 classifier: KV-1..KV-6, P-1..P-3,
  pgid_or_null, sixteen closed tokens, §3.7-§3.10      UNCHANGED (PA-3 restates
                                                       the publication boundary,
                                                       adds and removes no branch)
two signed freeze-EXECUTION sites; invariant 89 as
  rewritten; S-12; sole-killpg-caller (N-3)            UNCHANGED, subject to X22-C3
E-1..E-4 endpoint-loss semantics                       UNCHANGED
W-A G-1..G-4, one-shot grammar, T-1..T-7, §4.6 pricing UNCHANGED
W-B record-first R1..R6, §5.6 crash matrix             UNCHANGED
A-ABS-1..A-ABS-6; process_id mandatory, non-null,
  opaque, NOT a PID (N-5)                              UNCHANGED
K1..K5 rename, five loci, tests 101-102                UNCHANGED IN SUBSTANCE
                                                       (§5.1's I-1/I-2 correct two
                                                       prose phrases only; no
                                                       locus, key or biconditional
                                                       moves)
R2/R9 schema separation, SEP-1..SEP-3, R10 verbatim    UNCHANGED
publication boundary L6..L9, ND-1..ND-4, PCS journal
  invisibility (N-6)                                   UNCHANGED
O-7's _MSG_EOR re-assignment to both options           UNCHANGED
prior closed findings F2, Y-C1/C2, Y-M1/M2/M3, Y-m1,
  X determinations 2,4,5,7,8 of the v2 round           REMAIN CLOSED
```

The PCS journal boundary in particular is intact: the classifier's terminal,
per-group tokens and `freeze_ns` remain P1-owned control-plane facts, are never a
`t-freeze-observation.v1`, are never a field of a
`t-freeze-fallback-observation.v1`, and are never an input to any peer validity
predicate. Nothing in v2.2 makes PCS journal state scientifically visible.

**No authorization.** §12's negative space is complete and I verify it against
the packet's own conduct: it selects neither W-A nor W-B, mints no token, adds,
removes and renames no token, opens no author cell, and modified no existing
file. `AUTH-5` and `N-8` leave
`I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER` unrevoked and unreopened;
`T2-17`/`T2-18` are untouched by construction. The identity cell is neither
selected nor repaired. **`T` is `NOT_ACTIVATED` and the programme claim is
`OPEN`.** No implementation, T activation, process execution, capability, world,
learner, entropy, spend, datum, outcome, Proof or claim movement is authorized
by v2.2 or by this confirmation.

**The recommendation.** W-B remains recommended, and nothing in `X22-C1`,
`X22-C2` or `X22-C3` moves it. `PW15`..`PW17` have no option variant and fall
identically on W-A and W-B. The one asymmetric correction in the whole round —
`R16`'s endpoint count — moved **against** W-A. The two rows that decide,
topology/opcode changes and the new liveness dependency, are untouched. **The
defects are common authority and route defects and do not reopen W-A versus
W-B.**

---

## Summary against the seven audited items

| # | Item | Result |
|---|---|---|
| 1 | 41st tier-1 locus / live tier-2 authority | **FOUND — §W6.5 at `…V2_1_CORRECTION.md:1331-1342`, plus `:88` and `:1582-1586`. BLOCKING (`X22-C1`).** Tier-2 loci: no enumerated tier-2 occurrence controls live behaviour; but three chain documents (10.5/10.6/10.7) are unclassified (`X22-C2`). |
| 2 | Accounting 40 / 5 / 45 / 62 / 18 | Arithmetic **reproduces exactly**; `K1`..`K5` disjoint from `PN1`..`PN5` verified; six peer files verified. **Membership not confirmed** — `X22-C1` adds three, `X22-C2` disputes ten. |
| 3 | `killer == WATCHDOG` unreachable | **CONFIRMED** on the writer side, the predicate side, and the absence of any defaulting/recovery/migration clause. Enum retention correct. Global placement depends on `X22-C2`. |
| 4 | 22 replaced + exactly 4 retained reads; `R8` identity-only | **CONFIRMED.** All four sites reproduce verbatim; reads install nothing, decide nothing, enter no predicate; count is neither inflated nor deflated. |
| 5 | `R16` — W-A three endpoints, W-B two pipes, PCS never retains the update writer | **CONFIRMED** against composite §P1-6.2, §P1-8.7, `:2310`, `:660-663` and v2 §4.1/§4.7. No aliasing, duplication, inheritance, wrapper retention or alternate write path. |
| 6 | Filename, `WATCHDOG/` namespace, atomic six-file handoff | Filename **CONFIRMED**; namespace **CONFIRMED**; **atomicity NOT confirmed** — subset ordering only, no all-or-none rule. |
| 7 | No regression; no authorization | **CONFIRMED** on both counts. |

## Independent-line convergence

The Y line returned `REVISE_OFFICINA_P1_WATCHDOG_V2_2` on this same v2.2 digest.
I reached my conclusion before reading it. The lines **converge** on the
authority-partition defect (`X22-C2` / Y determination 1), on handoff atomicity
(Y determination 2), and on the ordinary-deadline writer route (`X22-C3` /
Y determination 3); and independently on the passing items — the four identity
reads, `R16`, the namespace, the filename, the PCS journal boundary,
recommendation independence and negative space.

**`X22-C1` — §W6.5 — is found by the X line only** and is the answer to the
bounded question the closure put to this line. It survives every authority
reading: under v2.2's own `AUTH-2` it is tier 1 by ten carrying references, and
under the composite's document-level rule it must be reached by whatever
governing text replaces the peer chain. **It cannot be dispositioned away by
choosing a different authority partition; it must be repaired.**

---

## Verdict

The peer replacement set is not exhaustive. A live governing locus assigns the
watchdog freeze execution and freeze recording, is carried by name as the
chain's single named protocol amendment over the signed harness composite, and
is absent from the declared forty. The author's stated search method structurally
cannot find it. Two further blocking defects — the authority classification of
the P1 binding, and an ordinary-deadline supervisor write route that no
governing writer table admits — stand alongside it.

Every repair is bounded. `PW15`..`PW17` are given exactly above. No new
mechanism, option, author cell or token is required, and the recommendation does
not move.

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_2
```

**Kirill's watchdog author-choice token is NOT authorized on these bytes.** No
selection token, no amendment token and no acceptance token is signable. No
implementation, activation or process authority follows from this document.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
PROCESS-IDENTITY CELL = NOT SELECTED
```

This confirmation modified no existing file, committed nothing, executed no
process, and created nothing executable.
