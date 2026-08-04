READY_FOR_OFFICINA_P1_WATCHDOG_V2_3_FINAL_XY_CONFIRMATION

# Author closure — Officina P1 watchdog-freeze author choice, v2.3

**Author:** Claude Code Opus 5, **specification author only**. I authored the
historical chain and the documents closed here, and therefore **cannot** be
their independent X-line or Y-line reviewer. **This closure is an untrusted
self-assessment.** The verdict token above is a readiness statement for review,
not an acceptance and not a confirmation.

**Kirill's watchdog author-choice token remains UNAUTHORIZED** and is not made
signable here. See §C7.

---

## §C1. What was produced

Four new files. **No existing file was modified. Nothing was committed.**

```text
4244e331dc7530dad743c640ae16ada048aed7cd2ec58822bf2d0dde77c8ffcc
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md
    The correction. Withdraws v2.2's repair architecture, states the
    document-level authority rule, rebuilds the inventory, disposes the
    provenance occurrences.

380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md
    LIVE AUTHORITY SURFACE 1 — peer-layer behaviour. New amendment to the
    accepted generic-harness chain. 12 sections, 46 named rules, a 10-conjunct
    acceptance predicate, a 6-step sequence, 2 named entry routes.

b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md
    LIVE AUTHORITY SURFACE 2 — P1 interface, execution, writer, predicate and
    invariant surface. A full replacement for v1.2, self-contained, 3228 lines.

  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_3_closure.md
    This document.
```

### §C1.1 How composite v1.3 was constructed, and why that matters for review

**v1.3 was not hand-transcribed. It was derived from v1.2's exact bytes by
anchored replacement, mechanically.** Thirty-seven replacements were applied;
the generator asserted that **each anchor occurred exactly once** in v1.2 and
refused on any other count. This is stated so the X and Y lines can verify the
delta rather than re-reading 3228 lines:

```text
SOURCE      composite v1.2, 2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d
RESULT      composite v1.3, b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54
LINES       2892 → 3228
ANCHORS     37, each matched exactly once, no fuzzy or regex matching
SENTINELS   six, in order, at 214 / 3104 / 3106 / 3141 / 3143 / 3223 — the
            region scheme is intact and one occurrence each
EVERY BYTE NOT NAMED BY AN ANCHOR IS v1.2's BYTE, UNCHANGED.

A reviewer can reproduce the delta exactly with:
  diff <(cat …COMPOSITE_V1_2.md) <(cat …COMPOSITE_V1_3.md)
```

**Independent verification performed after generation.** A sweep of v1.3 for
`watchdog` within 80 characters of
`freez|writ|observ|witness|settle|execut|kill|quiesc` — the **corrected**
alphabet, including the `execut` token whose absence caused the v2.2 miss —
returns no sentence assigning the watchdog freeze execution, quiescence proof or
evidence writing. Every remaining occurrence is one of: the amended negative
statements, the retained schema enum, transport/descriptor rows, the retained
`WATCHDOG/` path strings, or the option-variant blocks.

---

## §C2. The document-level authority proof

**Claim.** Every earlier supervisor/control-channel document is provenance in
whole, and exactly two files carry live authority for this repair.

```text
STEP 1 — THE RULE IS IN THE COMPOSITE'S OWN BYTES.
  composite v1.2 :42-49, authority level 3:
    "Every earlier supervisor/control-channel document — the two drafts, the
     corrections v2.1 through v2.1.10.7, and versions 1 and 1.1 of this
     composite — is immutable historical and provenance evidence only. No
     implementer, verifier or reviewer opens any of them for behaviour or for
     verification. They appear in §P1-18's provenance region by path and digest
     and NOWHERE ELSE."

STEP 2 — THE RULE ATTACHES TO DOCUMENTS. It enumerates DOCUMENTS, not sections.
  It states the disposition of a whole document ("appear … by path and digest").
  No sentence of it admits a file-internal split.

STEP 3 — THE BINDING IS INSIDE THE RULE'S RANGE AND ITS PROVENANCE REGION.
  …V2_1_10_4_P1_BINDING.md appears at composite v1.2 :2851 — inside §P1-18
  PROVENANCE, by path and digest — and NOWHERE ELSE in the composite. Its
  sections are §P1B.*, i.e. entirely P1-boundary text. v2.2's AUTH-1 carve-out
  ("level 3 is about the P1 boundary, not the peer boundary") therefore cannot
  reach it: it IS P1-boundary text.

STEP 4 — THE RULE'S RANGE EXTENDS PAST THE BINDING, AND v2.2 DID NOT NOTICE.
  Three documents postdate the binding and are named in level 3's own range:
    v2.1.10.5 (798d0cbd…), v2.1.10.6 (8f806e33…), v2.1.10.7 (66dc6fdc…),
  at composite v1.2 :2852-2854. None appears anywhere in v2, v2.1 or v2.2 — not
  as tier 1, not as tier 2, not in the checked list, not in custody. v2.2's
  description of v2.1.10.4 as "the current P1 binding" is false on the bytes.

STEP 5 — THE ALTERNATIVE FAILED EMPIRICALLY, NOT MERELY THEORETICALLY.
  v2.2's AUTH-2 made a section operative iff a currently governing document
  carried it as a live rule and no later document replaced it. Historical §W6.5
  satisfies that test more strongly than ANY of the forty declared loci: carried
  by name at …V2_1_1:124 and :125, at …V2_1_2:106, and named as "§W6.5's
  explicitly named supersession of harness §5a" or "§W6.5's carried
  supersession" at …V2_1_3:1382, …V2_1_4:1114, …V2_1_5:663, …V2_1_6:776,
  …V2_1_7:836, …V2_1_8:1414, …V2_1_9:1194 and …V2_1_10:1457 — ten carries,
  replaced nowhere — and it assigns the watchdog BOTH freeze execution AND
  freeze recording. IT WAS OMITTED FROM THE FORTY. The declared method could not
  find it: the grep alphabet `freez|writ|observ|witness|settle` has no token for
  `execut`, and §W6.5 reads "executes the sequence … records the conservative
  proved-freeze instant", with subject and verb straddling a line break.

STEP 6 — CONCLUSION. A classification whose membership test the author cannot
  execute reliably is not an authority rule. The document-level rule requires no
  enumeration at all: nothing historical is live, so nothing historical can hide
  a live authority. THE FORTY, THE FORTY-FIRST, THE EIGHTEEN AND THE TEN CARRIES
  ARE ALL PROVENANCE, AND NONE IS EDITED.
```

**The residual obligation this creates, and how it is discharged.** If nothing
historical is live, the peer behaviour those sections carried must be restated
in governing bytes or it is lost. That is the entire purpose of the peer
amendment: §A3 restates the freeze sequence, §A4 the evidence object, §A5 the
acceptance predicate, §A6 the fallback, §A7 the swap-only carve-out, §A8 the
negative surface — **each self-contained, so that no implementer opens a
historical document to obtain them.**

---

## §C3. One-to-one disposition of every X and Y finding

### X-line findings

| # | Finding | Disposition |
|---|---|---|
| `X22-C1` | §W6.5 is an omitted live governing locus assigning the watchdog freeze execution and recording; the declared method cannot find it | **CLOSED BY REMOVING THE CLASS OF DEFECT, NOT THE INSTANCE.** Under §C2 §W6.5 is provenance and governs nothing. Its meaning is superseded, without editing its bytes, at peer amendment §A2.2 (which quotes it for identification, names its two companion loci at `:88` and `:1582-1586`, and names all ten carrying references) and §A2.3 (which retains the timing weakening with the actor corrected), and at composite §P1-10.6. **X's `PW15`..`PW17` are correct as text and are deliberately NOT APPLIED**, because applying them would edit an immutable historical document; their substance is carried in governing bytes. The corrected search alphabet is recorded and was used to verify v1.3. |
| `X22-C2` | `AUTH-3` classifies the P1 binding as tier-1 although the composite makes it provenance; v2.1.10.5/.6/.7 unaccounted; §1.8 omits the v2.1.10.2 digest | **CLOSED.** `AUTH-1`..`AUTH-5` withdrawn in whole (v2.3 §0.2). `DL-4` states the binding is provenance; `PB1`..`PB10` withdrawn. `DL-5` and v2.3 §3 `P-6` classify all three later documents with their digests and record that none contains a freeze-executor or evidence-writer assignment. v2.3 §3 `P-7` supplies the omitted v2.1.10.2 digest `c7ff2777…`; `P-8` adds the two further uncarried chain digests. |
| `X22-C3` | `PH1`/`PW2` open an ordinary-deadline supervisor write route that `R2`/`R9`/`R10`/`PA-1` do not admit | **CLOSED.** Peer amendment §A3.1 names `ROUTE-D` and `ROUTE-W` and declares them exhaustive. Composite §P1-13.9 states both, and row 4's executing-process block, `SW-2`, §P1-13.7, §P1-13.8 and invariant 89 **all enumerate both routes consistently**. The rationale paragraph is retitled "Why one executing process on two routes…" and states that two triggers of one procedure are not two writers. Test 95 drives both routes in one run. |
| X item 3 | `killer == WATCHDOG` unreachable; enum correctly retained | **PRESERVED AND MOVED TO GOVERNING BYTES.** Peer amendment §A5 conjunct 8, `KW-1` (no default/migration/compatibility/recovery/re-import/re-derivation/fixture re-entry), `KW-2` (a fixture narrowing the enum fails), `KW-3`. Composite tests 93, 94. |
| X item 4 | four retained reads grant identity observation only; 22 vs 4 accounting correct | **PRESERVED, UNAMENDED BY CONSTRUCTION.** §P1-9.2 property 8 and invariant 87 are carried **verbatim** into v1.3 — no anchor touches them. §P1-13.1's watchdog row now states the read explicitly and states the negative surface. Invariant 63 records that property 8 is unamended. §P1-10.6 states that a read is not an authority. |
| X item 5 | `R16` W-A three endpoints / W-B two pipes; no aliasing, duplication, inheritance, wrapper retention or alternate write path | **PRESERVED.** Composite row 4's `P1 invariant` block carries both variants. §P1-8.7, `:2310` and the `_socketpair` non-inheritability sentence are carried byte-unchanged. Test 99. |
| X item 6 | filename and namespace conclusions correct; **atomicity NOT confirmed** | Filename and namespace **PRESERVED** (peer amendment `F-1`..`F-8`, composite test 100). **ATOMICITY CLOSED** at §C4 and by composite guard `G-11`. |
| X item 7 | no regression; no authorization | **PRESERVED.** §C6. |

### Y-line findings

| # | Finding | Disposition |
|---|---|---|
| `Y22-1` | `AUTH-1`..`AUTH-5` do not reproduce the composite's document-level rule; the file-internal split has no source; the handoff destroys the evidentiary bytes it claims to protect | **ACCEPTED IN FULL AND ADOPTED AS THE GOVERNING RULE.** §C2; v2.3 §1 `DL-1`..`DL-6`. Composite v1.3's authority level 3 now states the document-level rule explicitly, adds the binding and v1.2 to its range, and states that immutability attaches to documents and that a cross-reference reactivates neither party. Level 3a names the one new peer amendment as a live surface that is **not** a predecessor. |
| `Y22-2` | the arithmetic reproduces but memberships do not; the six-file handoff is not globally atomic | **CLOSED BOTH HALVES.** v2.3 §4 withdraws 40/45/62/18 as authority cardinalities and explains precisely why (the arithmetic was never wrong; the membership rule was). v2.3 §5 gives a new membership rule decidable by listing two file paths, with counts 64 + 48 = **112 governing loci in 2 files, 0 historical loci with governing force, 0 historical bytes edited**. §C4 states one all-or-none handoff; guard `G-11` enforces it fail-closed. |
| `Y22-3` | v2.2 creates an unaccounted ordinary-deadline writer route | **CLOSED**, identically to `X22-C3` above. Y's option "retain it and amend the governing row-4 texts" is the one taken; the alternative (remove it) was rejected because removing the supervisor's ordinary-deadline entry would leave no executor at an ordinary deadline once the watchdog is no longer one. |
| `Y22-4` | `killer == WATCHDOG` locally rejected, but global closure not established while the authority split is invalid | **CLOSED.** The predicate now lives in peer amendment §A5, an indisputably governing file under the new rule, and the re-entry audit (`KW-1`) is stated there rather than in a disputed surface. Y's requirement — "placed once in an indisputably governing peer contract, not in a file whose operative status is itself disputed" — is met literally. |
| `Y22-5` | the four identity reads and the PCS journal pass | **PRESERVED.** Reads carried verbatim; publication boundary restated at composite §P1-10.7 with test 101. |
| `Y22-6` | `R16`, namespace and witness filename pass | **PRESERVED**, as above. |
| `Y22-7` | recommendation independence and negative space intact | **PRESERVED.** v2.3 §8, §11; composite §P1-16. |
| Y repair 1 | replace `AUTH-1`..`AUTH-5` with a document-level rule; keep history byte-immutable; put peer semantics in the harness chain and P1 invariants in one new composite version; do not reactivate historical paragraphs by cross-reference | **DONE, all five clauses.** |
| Y repair 2 | recompute counts from that rule; preserve the occurrence inventory as provenance; state one all-or-none handoff | **DONE.** v2.3 §3, §4, §5; §C4. |
| Y repair 3 | reconcile the ordinary-deadline route in the governing row-4 writer/executing-process/function/invariant texts, both through `SIGNAL_GROUP`, one writer, `killer = SUPERVISOR`; update execution-route count and tests | **DONE.** Both routes appear in row 4's executing-process block, `SW-2`, §P1-13.7's writer row, §P1-13.8, §P1-13.9 and invariant 89(a); tests 95 and 96 added. The execution-**site** count remains two and is now stated as "site (a) = both routes". |
| Y repair 4 | place the `killer` rejection in the resulting governing predicate and re-run the occurrence/default/recovery audit on those bytes | **DONE** for the placement (§A5 conjunct 8, `KW-1`..`KW-3`). **The re-run of the audit on the new bytes is a reviewer obligation, not an author one**, and is the bounded Y question at §C5. |

---

## §C4. The atomic handoff — one all-or-none unit

```text
THE UNIT. Exactly two files become operative, jointly and indivisibly:
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md
NEITHER IS OPERATIVE ALONE. Accepting one without the other is NOT a partial
success and NOT a conforming state.

THE STEPS, all in one landing:
  1. install both files;
  2. resolve every [W-A]/[W-B] variant block in composite v1.3 to the signed
     branch and DELETE the other branch — twenty-eight markers today; guard
     G-10 must then find zero;
  3. recompute H_FILE, H_BODY, H_GUARDDATA, H_NORMATIVE and the six sentinel
     counts; run the placeholder audit and the guard fires. Required placeholder
     count and guard-fire count remain ZERO;
  4. record in the manifest: both governing digests, every accepted
     generic-harness chain digest, the batch-settlement digest, and every
     provenance digest;
  5. install verifier guards G-10 and G-11 and test rows 92..103;
  6. verify by digest that EVERY historical file is byte-identical to its
     recorded value.

FAIL-CLOSED BEHAVIOUR ON PARTIAL OR STALE INSTALLATION — composite guard G-11.
  Before any process is created, before any handle is allocated and before any
  freeze route is reachable, the verifier recomputes:
    (a) H_FILE of composite v1.3 against the manifest;
    (b) the digest of the peer amendment against the manifest;
    (c) every §P1-18 provenance digest against its recorded value;
    (d) every accepted peer-chain digest against the manifest.
  ANY mismatch, ANY absence, ANY extra file in the governing set, or ANY
  provenance digest that differs ⇒ REFUSE with
  WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE.
  ON REFUSAL: no process is created, no handle is allocated, no freeze route is
  reachable, no evidence is accepted, no settlement runs.
  A PARTIALLY INSTALLED STATE NEVER SATISFIES THIS CONTRACT AND NEVER SILENTLY
  DEGRADES TO THE HISTORICAL BEHAVIOUR. Verifying a digest is not opening a
  document for behaviour.

EXISTING HISTORY REMAINS BYTE-IDENTICAL. Verified: `git status` reports ZERO
modified files under successor/. This round created new files only.
```

---

## §C5. The two bounded final questions

### Bounded X question

> **The v2.2 round proved that an enumeration-based authority rule can miss a
> live governing locus, and the miss was found only because the search alphabet
> was extended. v2.3 replaces enumeration with a document-level rule and
> restates the historical peer behaviour in two new files. That substitutes a
> DIFFERENT failure mode: not an omitted live locus, but an OMITTED RESTATEMENT
> — a peer rule that historical §W3.3, §Z4, §N5, §U3 or the binding carried,
> that is genuinely needed for behaviour, and that neither the peer amendment
> nor composite v1.3 restates, so that after the handoff it exists nowhere and
> an implementer must either open a provenance document or invent the rule.**
>
> **Audit for a gap of that kind.** Work from the historical bytes as a
> checklist and ask, for each rule they carried: is it restated in governing
> bytes, deliberately dropped with a stated reason, or silently missing? Give
> particular attention to the freeze sequence's step-level detail, the witness
> ordering and consumption rules, the ten acceptance conjuncts, the fallback's
> key set and routing, the swap-only carve-out, and the strict-progress branch.
> If a required rule exists nowhere, treat it as blocking and give the smallest
> exact text that restores it **inside the two governing files**, without
> editing history and without broadening the design.

### Bounded Y question

> **v2.3 asserts that `killer == WATCHDOG` cannot re-enter as admissible
> evidence on any path, and places that assertion in peer amendment §A5 conjunct
> 8 with `KW-1`..`KW-3`. That claim has not been re-run against the NEW bytes by
> an independent line — Y's own repair 4 asked for exactly that re-run, and the
> author cannot discharge it.**
>
> **Re-run the occurrence, default, migration, compatibility, recovery,
> archival-re-import and takeover-re-derivation audit against the two governing
> files only, plus the accepted peer chain.** Then answer the governance half:
> does the new document-level membership rule — governing iff inside one of two
> named files — hold without leakage? Specifically, does any sentence of the
> peer amendment or of composite v1.3 make a historical document's content
> operative again by incorporation, by quotation that functions as a rule, or by
> a cross-reference an implementer would have to follow? And is the §C4 handoff
> genuinely all-or-none, with guard `G-11` reaching every state in which a
> partial installation could otherwise run?

---

## §C6. No regression, and no authorization

```text
PRESERVED WITHOUT REOPENING, each verified against the new bytes:
  the blocker and its four mechanisms; the rejected route families
  the common freeze classifier: KV-1..KV-6, P-1..P-3, pgid_or_null, the §3.5
    scope, the sixteen closed tokens, §3.7-§3.10
  W-A in full; W-B in full; both option variants carried, neither selected
  A-ABS-1..A-ABS-6; process_id mandatory, non-null, opaque, NOT a PID
  the K1..K5 rename's substance, carried at peer amendment §A6 S-3
  SEP-1..SEP-3; the R2/R9 schema separation
  L6..L9, ND-1..ND-4, PCS journal invisibility — restated at §P1-10.7
  _CLOCK_MONOTONIC pinned; B-1..B-8; S-25
  the two signed freeze-execution sites; S-12; the sole-killpg-caller rule
  the PCS never retains the update-pipe write end — §P1-8.7 byte-unchanged
  the four retained read-only identity loci — carried VERBATIM
  the witness filename and the WATCHDOG/ namespace conclusions
  the recommendation and its five criteria — W-B remains recommended
  the six tokens; no selection token added, removed or renamed
  I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER — not revoked, not re-run,
    not reopened; C1 retains a dedicated watchdog PROCESS

AUTHORIZED BY THIS ROUND: NOTHING.
  no implementation, no commit, no verifier or manifest edit, no T activation,
  no process, socket, pipe, fork, exec, signal, wait or prctl operation, no
  supervisor, PCS, controller, worker or watchdog, no capability, world,
  learner, entropy, candidate, trajectory, capacity artifact, custody
  disposition, result manifest, spend, datum, outcome, Proof or claim movement.
  No freeze was executed, requested, journalled or witnessed. No /proc was read
  against any live process. No clock was sampled for any contract purpose.
  No option was selected and no token was accepted or minted.
```

---

## §C7. Status

```text
T                            = NOT_ACTIVATED
PROGRAMME CLAIM              = OPEN
WATCHDOG-FREEZE CELL         = NOT SELECTED
PROCESS-IDENTITY CELL        = NOT SELECTED
COMPOSITE v1.3               = BLOCKED_ON_AUTHOR_CELLS_…_NOT_ACCEPTED
PEER AMENDMENT v1            = NOT_ACCEPTED
```

**Kirill's watchdog author-choice token remains UNAUTHORIZED.** No selection
token, no per-option amendment token, no common amendment token and no
acceptance token is signable. Authorization requires **both** a bounded
independent X-line confirmation and a bounded independent Y-line confirmation,
on the identical bytes recorded at §C1, answering the two bounded questions of
§C5. **Two REVISE verdicts preceded this round; a third is possible and this
closure predicts neither outcome.**

This closure modified no existing file, committed nothing, executed no process,
and created nothing executable.
