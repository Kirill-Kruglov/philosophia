READY_FOR_OFFICINA_P1_WATCHDOG_V2_4_INDEPENDENT_XY_CONFIRMATION

# Author closure — Officina P1 watchdog-freeze author choice, v2.4

**Author:** Claude Code Opus 5, **specification author only**. I authored v2.3
and v2.4 and therefore **cannot** be their X-line or Y-line reviewer. **This
closure is an untrusted self-assessment.** The token above is a readiness
statement for review — not an acceptance, not a confirmation, and not evidence
that the repairs are complete.

**This closure is normative for nothing.** The complete handoff is stated in the
governing files themselves, at amendment §A9 and composite §P1-14.8. That is the
repair for `Y23-3`; a closure that carried normative content would reintroduce
the defect.

**Kirill's watchdog author-choice token remains UNAUTHORIZED.** See §C8.

---

## §C1. Custody — the four new files

```text
ce68b810611304b3877b6ecc227ce5c7a02e3d7b939183089a90d188c1d0ab6f
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md

ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
    GOVERNING SURFACE 1 — peer-layer behaviour.

c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md
    GOVERNING SURFACE 2 — P1 interface, execution, writer, predicate, invariant.
    3379 lines, mechanically derived from v1.3.

  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_4_closure.md
    This document. Normative for nothing.
```

```text
THE v2.3 PAIR, WHOLLY REPLACED, BYTES UNTOUCHED, JOINING PROVENANCE:
  380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858  amendment v1
  b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54  composite v1.3

THE REVIEWS THIS ROUND ANSWERS:
  654261d9a94f321680ca31ccb345f6ff409036e34efa2882a8516848ec99ceb0  X v2.3
  reviews/sol_officina_p1_watchdog_v2_3_final_y_confirmation.md     Y v2.3

HISTORICAL BYTES: `git status --porcelain successor/` reports ZERO modified
files. Composite v1.2 still hashes 2c857fa8…; …V2_1_CORRECTION.md still hashes
9f1d018e…. This round created four new files and modified none.
```

---

## §C2. One-to-one disposition of every X finding

| # | Finding | Disposition |
|---|---|---|
| `X23-B1` | quiescence constants existed only in immutable history; §A3.3's loop bound and §A3.4's strict-progress branch were not constructible | **CLOSED.** Amendment §A3.0 `QC-1`..`QC-5`: max passes `8`, interval `100_000_000 ns`, update-ack timeout `1_000_000_000 ns`. `QC-4` distinguishes `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` as **already governed** by composite §P1-2 — named, not restated. `QC-5` states these are restatements reproducing the historical values exactly: no value moves, no constant is introduced, no cell is opened. |
| `X23-B2` | forbidden dispositions lost; the accepted harness positively assigns `T_PROCESS_RESOURCE_STOP` to an overrun-bearing transition | **CLOSED, and this was the materially unsafe one.** Amendment §A3.6 `FD-1` forbids `T_PROCESS_CLOSED`, `T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE` and `T_PROCESS_RESOURCE_STOP` on a deadline freeze **and on a swap-only freeze**, and forbids any valid close, exhaustion, pause or review terminal from an overrun. `FD-2` expressly retains the ordinary harness P3→P4 resource stop and states that removing it would be nonconforming. `FD-3` fixes cause single-valued `PROCESS`. `FD-4` restates PROVED/UNKNOWN routing in full. |
| `X23-B3` | ack semantics undefined ⇒ both route triggers unevaluable | **CLOSED.** Amendment §A8.1 `AK-1`..`AK-7`: the `t-watchdog-ack.v1` key set, `healthy(table_seq)`, `dead`, `updated_monotonic_ns` and `ack_monotonic_ns` defined as whose clock each is, old deadline authoritative until ack, and `AK-6` giving the **exact meaning of `ACKED`** used by `ROUTE-D`'s precondition and by `S1`. |
| `X23-B4` | `G-10` matched its own definition and could never be satisfied | **CLOSED — and the X diagnosis was incomplete.** The Y line found that `G-10` was *already taken* by the §P1-14.3 authoring discipline, with test 76 exercising the other meaning. v2.4 adopts the fuller Y diagnosis: the discipline is **renamed `AD-1`**, `G-10` is reserved **uniquely**, its patterns move to §P1-17 GUARDDATA as class `VARIANT_MARKER` outside `AD-1`'s range, and `G-10`'s definition paraphrases. Test 76 renamed; **test 102 rewritten to paraphrase**, since a quoting test row reproduced the same self-match. |
| `X23-M1` | swap-only carve-out not constructible | **CLOSED.** Amendment §A7.1 (total overdue/non-overdue split), §A7.2 (the `replacement_freeze_id` domain-tagged preimage and the exact key sets of `t-replacement-freeze.v1`, `t-replacement-resume.v1` and `t-replacement-invalidation.v1`), §A7.3 (`I1`..`I7`, `S1`, `S2`, `ACK_PENDING` with its bound and its no-marker rule), `RF-1`..`RF-3`. **No historical lookup is required.** |
| `X23-M2` | cross-class consumption order absent | **CLOSED.** Amendment §A6.1 `TO-1`..`TO-5`: production on first failing conjunct ascending, `EEXIST` duplicate rule, the conflict rule for differing `rejected_object_sha256_or_null`, the **one total order across all three classes**, and `TO-5` fallback priority. |
| `X23-M3` | lease-table publication rule absent | **CLOSED.** `AK-1`, and restated standalone at §A8.2 `PUB-1`..`PUB-4` as the mandate required — deliberately redundant so the ordering cannot be read as incidental to the liveness rule. |
| `X23-M4` | `112` not reproducible; double-counted | **CLOSED.** Packet §3.1 states exactly why (double count of the C1 masthead, undercount of four masthead edits, and no counting rule at all). §3.2 gives a counting rule with a definition of "one locus", an explicit exclusion list, disjointness by construction and mechanical reproducibility. §3.3 derives **180**. `112` is withdrawn and is **not** replaced by a number computed under the same absent rule. |

---

## §C3. One-to-one disposition of every Y finding

| # | Finding | Disposition |
|---|---|---|
| `Y23-1` | killer re-entry audit passes | **PRESERVED.** §A5 conjunct 8, `KW-1`..`KW-3`, tests 93–94, fallback fixed literal. |
| `Y23-2` | historical content gains no force | **PRESERVED.** `DA-1`..`DA-3`; §A2 quotes for identification only and is followed by complete governing replacements; composite §P1-10.6, row 4, §P1-13.9. |
| `Y23-3` | installation depended on a third, untrusted file — amendment `H-4` deferred the full list to the author closure | **CLOSED.** `H-4` **withdrawn**. The complete handoff is at amendment §A9 and identically at composite §P1-14.8. `DA-5` forbids any normative dependency on any closure, and **this closure carries no normative content**. |
| `Y23-4` | routes pass | **PRESERVED.** §A3.1; composite §P1-13.9, row 4, `SW-2`, §P1-13.7, §P1-13.8, invariant 89, test 95. |
| `Y23-5.1` | §P1-14.1's one-file rule and `G-11` cannot both be implemented | **CLOSED.** §P1-14.1 narrowed: `G-1`..`G-9`, `AD-1` and `G-10` are one-file body/wording guards; `G-11` is the **one explicit exception** with a closed seven-class input set, no wildcard, no directory scan, and the statement that hashing is not opening for behaviour. |
| `Y23-5.2` | the verifier is pinned as provenance while the future-edit table permits only `G-1`..`G-10` "and nothing else" ⇒ `G-11` cannot be installed without self-refusal | **CLOSED.** The `verification.py` provenance digest is labelled a **NON-ENFORCED PRE-INSTALL BASELINE**, is **excluded from `M2`**, and is not compared by `G-11`. The future-edit table now expressly permits and *requires* the post-handoff verifier implementing `G-1`..`G-11` and `AD-1`, pinned as member `M5`. The provenance note states the circularity being resolved and that this is the **only** exception. |
| `Y23-5.3` | `G-11` bound no post-handoff verifier, manifest or test bundle as an authenticated unit | **CLOSED.** Amendment §A10 and composite `G-11`: seven pairwise-disjoint member classes binding both governing files, the exact provenance set, the accepted peer and batch chains, the manifest schema/version/bytes, the verifier bytes, the test bundle rows 92–115, and the passing attestation — with step 7 requiring the attestation to reference the verifier and bundle digests **actually found on disk**. |
| `Y23-5.4` | `G-10` not uniquely specified; tests 76 and 102 exercised two meanings | **CLOSED**, as under `X23-B4`. `G-10` is now unique; the composite states so explicitly; `G-10` and `G-11` are declared independent, neither a precondition of the other. |
| `Y23-6` | retained reads and PCS journal pass | **PRESERVED.** Composite property 8 and invariant 87 carried **verbatim** — no anchor touches them; `WA-4`, `NS-2`; §P1-10.7, invariant 89, test 101. |
| `Y23-7` | recommendation and status pass | **PRESERVED.** Packet §5; nothing in v2.4 is asymmetric; 24 markers balanced 12/12. |
| Y repair 1 | move the handoff into both governing files, delete `H-4` | **DONE.** |
| Y repair 2 | narrow the one-file rule, state the closed input set | **DONE.** |
| Y repair 3 | label the verifier digest a non-enforced baseline; permit and pin the post-handoff verifier | **DONE.** |
| Y repair 4 | one externally anchored install record; fixtures for every class; no self-attestation | **DONE.** §A10; tests 104–115. |
| Y repair 5 | reserve `G-10`, rename the discipline, keep the marker check independent of the joint-install guard | **DONE.** |

---

## §C4. Restatement checklist — every behavioural rule, and where it now lives

**The v2.3 defect class was omitted restatement. This is the checklist that
should have accompanied v2.3.** Each row names a rule the historical chain
carried and the governing locus that now carries it.

| Historical rule | New governing locus | Status |
|---|---|---|
| freeze sequence, steps 1–6 | amendment §A3.3 | restated |
| quiescence pass loop and its bound | §A3.3 step 3 + `QC-1`, `QC-2` | **restored in v2.4** |
| strict-progress branch | §A3.4 + `QC-1`, `QC-2` | **constructible in v2.4** |
| `freeze_ns` conservative-sample rule | §A3.3 closing | restated |
| doubly-detached descendant residual | §A3.3 closing | restated |
| forbidden dispositions on a freeze | §A3.6 `FD-1` | **restored in v2.4** |
| ordinary P3→P4 resource stop preserved | §A3.6 `FD-2` | **stated in v2.4** |
| single-valued cause `PROCESS` | §A3.6 `FD-3` | **restored in v2.4** |
| PROVED / UNKNOWN routing | §A3.6 `FD-4` | restated and completed |
| witness id preimage, path, key set | §A4 | restated |
| production order, `EEXIST` rule | §A4 `F-3` | restated |
| consumption order within class | §A4 `F-4` | restated |
| replay naming, removal | §A4 `F-5`, `F-6` | restated |
| ten acceptance conjuncts | §A5 | restated |
| `killer` rejection and non-re-entry | §A5 conjunct 8, `KW-1`..`KW-3` | restated |
| fallback id preimage, key set, routing | §A6 | restated |
| fallback count-key separation | §A6 `FB-3` | restated |
| production / duplicate / conflict order | §A6.1 `TO-1`..`TO-3` | **restored in v2.4** |
| total order across three classes | §A6.1 `TO-4` | **restored in v2.4** |
| fallback priority | §A6.1 `TO-5` | **restored in v2.4** |
| overdue / non-overdue split | §A7.1 | restated |
| replacement-freeze id preimage | §A7.2 | **restored in v2.4** |
| three record key sets | §A7.2 | **restored in v2.4** |
| `I1`..`I7` invalid conditions | §A7.3 | **restored in v2.4** |
| `S1`, `S2` resumable conditions | §A7.3 | **restored in v2.4** |
| `ACK_PENDING`, its no-marker rule and bound | §A7.3 | **restored in v2.4** |
| `supervisor_stop_monotonic_ns` never evidence | §A7 `RF-2` | restated |
| watchdog negative surface | §A8 `NS-1`..`NS-4` | restated |
| lease-table publication ordering | §A8.1 `AK-1`, §A8.2 `PUB-1`..`PUB-4` | **restored in v2.4** |
| ack frame schema and keys | §A8.1 `AK-3` | **restored in v2.4** |
| `healthy` / `dead` predicates | §A8.1 `AK-4` | **restored in v2.4** |
| whose clock each sample is | §A8.1 `AK-5` | **restored in v2.4** |
| the meaning of `ACKED` | §A8.1 `AK-6` | **restored in v2.4** |
| client timeout ordering | §A8.1 `AK-7` | **restored in v2.4** |

**Twenty of thirty-four rows were restored or made constructible in v2.4.** That
ratio is the measure of how incomplete v2.3's restatement was.

---

## §C5. The counting proof

```text
RULE. A GOVERNING LOCUS is one NORMATIVE UNIT BEARING ITS OWN IDENTIFIER inside
one of the two governing specification files. Masthead, status, blocking
notices, prose framing, the provenance region and negative space are DOCUMENT
METADATA and are not governing loci. (v2.3 counted some of these and not
others, with no rule saying which — that is the whole of its discrepancy.)

DISJOINTNESS. Each identifier family appears in exactly one category. The
identifier sets were compared pairwise and the intersection is empty. One tag
collision introduced during authoring — the fallback rules `S-1`..`S-5` against
the resumable conditions `S1`, `S2` — was found by this check and repaired by
renaming the fallback rules to `FB-1`..`FB-5`.

FILE 1 — amendment v1.1, ec5ddff8…
  A tagged rules   96 = DA 5 + WA 6 + TIMING 4 + QC 5 + FD 4 + F 8 + KW 3
                      + FB 5 + TO 5 + RF 3 + NS 4 + AK 7 + PUB 4 + H 4
                      + IR 12 + M 7 + N 10
  B conjuncts      10        C steps 6        D routes 2
  E swap units     12  (I1..I7, S1, S2, and the three states)
  FILE-1                                                              126

FILE 2 — composite v1.4, c904ec43…
  F carried repairs 23  (R1..R22 + invariant 60)
  G new sections     4  (§P1-10.6, §P1-10.7, §P1-13.9, §P1-14.8)
  H guards           3  (G-10 redefined, G-11 new, AD-1 renamed)
  I test rows       24  (92..115)
  FILE-2                                                               54

  TOTAL GOVERNING LOCI                                                180
  GOVERNING SPECIFICATION FILES                                         2
  HISTORICAL LOCI WITH GOVERNING FORCE                                  0
  HISTORICAL BYTES EDITED                                               0

SEPARATELY, AND NOT SUMMED INTO THE ABOVE:
  provenance occurrence inventory                          76 loci + 6 documents
  the generated install record            NEITHER a governing locus NOR a
                                          provenance occurrence: a generated
                                          artifact carrying digests and no rules
```

---

## §C6. Partial-install state table — no runnable subset

**Every row is refused before any production entry point. There is no partial
mode, no warning mode and no override.**

| # | State | Detected by | Reason code | Runnable? |
|---|---|---|---|---|
| 1 | amendment v1.1 present, composite v1.4 absent | `G-11` step 6 | `MEMBER_OMITTED` | **no** |
| 2 | composite v1.4 present, amendment v1.1 absent | `G-11` step 6 | `MEMBER_OMITTED` | **no** |
| 3 | amendment v1 with composite v1.4 (mixed generation) | `G-11` step 5 | `INSTALL_RECORD_UNAUTHORIZED` | **no** |
| 4 | amendment v1.1 with composite v1.3 (mixed generation) | `G-11` step 5 | `INSTALL_RECORD_UNAUTHORIZED` | **no** |
| 5 | both governing files, no install record | `G-11` step 4 | `INSTALL_RECORD_ABSENT` | **no** |
| 6 | record present, filename ≠ recomputed id | `G-11` step 4 | `INSTALL_RECORD_NAME_MISMATCH` | **no** |
| 7 | record self-consistent but id not in trust root | `G-11` step 5 | `INSTALL_RECORD_UNAUTHORIZED` | **no** |
| 8 | any `M2` provenance file omitted | `G-11` step 6 | `MEMBER_OMITTED` | **no** |
| 9 | any extra file added to any class | `G-11` step 6 | `MEMBER_EXTRA` | **no** |
| 10 | any member stale (earlier version of itself) | `G-11` step 6 | `MEMBER_STALE` | **no** |
| 11 | pre-install baseline verifier (`G-1`..`G-9` only) | `G-11` step 6 | `MEMBER_SUBSTITUTED` | **no** |
| 12 | verifier with `G-10` but not `G-11`, or the reverse | `G-11` step 6 | `MEMBER_SUBSTITUTED` | **no** |
| 13 | manifest right schema, wrong version or bytes | `G-11` step 6 | `MEMBER_SUBSTITUTED` | **no** |
| 14 | test bundle missing any row 92–115 | `G-11` step 6 | `MEMBER_SUBSTITUTED` | **no** |
| 15 | tests present but never run (no `M7`) | `G-11` step 6 | `MEMBER_OMITTED` | **no** |
| 16 | attestation from a different verifier or bundle | `G-11` step 7 | `ATTESTATION_MISMATCH` | **no** |
| 17 | any historical byte moved | `G-11` step 2 / §P1-14.8 `H-4` | `HISTORICAL_BYTE_MOVED` | **no** |
| 18 | unresolved variant marker present | `G-10` | guard `G-10` fires | **no** |
| 19 | everything correct, author cells unsigned | blocking notice | not operative by status | **no** |
| 20 | everything correct, both cells signed, record authorized | — | — | **yes** |

**Row 20 is the only runnable state, and it is not reachable today: both author
cells are unsigned and no independent confirmation has been performed.**

Rows 1–17 are exercised by test rows 104–115; rows 107, 108 and 109 are seven
fixtures each, one per member class, so omission, extra membership and staleness
are exhaustive rather than sampled.

---

## §C7. Required: the next X review must be independent

**This is a precondition, not a preference.**

```text
The v2.3 X-line confirmation was produced by the SAME model instance that
authored v2.3, and that instance also authored v2.4. Its own report records the
defect and asks to be filed as an author self-audit.

THE EVIDENCE THAT SELF-REVIEW UNDER-DETECTS IS IN THIS ROUND: the independent Y
line found the G-10 IDENTIFIER COLLISION — that §P1-14.3 had already used the
label and that test 76 exercised the other meaning — which the self-review
missed entirely while examining the very same guard.

THE NEXT X REVIEW MUST BE PERFORMED BY AN AGENT THAT DID NOT AUTHOR v2.3 OR
v2.4. Preferably Claude Opus 4.8 or Fable 5. The Y line has been independent
throughout and should remain so.

Until that review exists, v2.4 has ONE independent line, not two, and MUST NOT
be treated as having survived an X-line pass.
```

**Suggested bounded X question for the independent reviewer.** v2.4 restored
twenty rules that existed only in immutable history. Re-run the completeness
audit against the two new governing files, using the historical §W3.2, §W3.3,
§W3.4, §Z4, §N5, §U3 and the binding as a checklist, and determine whether a
twenty-first behavioural rule remains reachable only from provenance — with
particular attention to what §A3.3's `SIGNAL_GROUP`-mediated steps, §A5's
conjunct 10 and §A7.3's `I5` depend on that may itself be unrestated.

**Suggested bounded Y question.** `G-11` now reads seven member classes while
§P1-14.1 confines every other guard to one file. Verify the exception is
genuinely closed — no wildcard, no directory scan, no adjective — and that the
install record's non-circularity holds: that the trust root is truly external,
that no member attests itself, and that no state exists in which the gate can be
satisfied by a set the author did not intend.

---

## §C8. Status

```text
T                            = NOT_ACTIVATED
PROGRAMME CLAIM              = OPEN
WATCHDOG-FREEZE CELL         = NOT SELECTED
PROCESS-IDENTITY CELL        = NOT SELECTED
COMPOSITE v1.4               = BLOCKED_ON_AUTHOR_CELLS_…_NOT_ACCEPTED
PEER AMENDMENT v1.1          = NOT_ACCEPTED
INSTALL RECORD               = NOT CREATED
INDEPENDENT X-LINE PASSES    = 0
INDEPENDENT Y-LINE PASSES    = 1  (on v2.3, which returned REVISE)
```

**Kirill's watchdog author-choice token remains UNAUTHORIZED.** No selection
token, no per-option amendment token, no common amendment token and no
acceptance token is signable on these bytes. Authorization requires a bounded
independent X-line confirmation **by a non-author agent** and a bounded
independent Y-line confirmation, both on the digests at §C1.

**Three REVISE verdicts preceded this round. This closure predicts no outcome
for the fourth.**

This closure authorizes nothing, modified no existing file, committed nothing,
executed no process, and created nothing executable.
