REVISE_OFFICINA_P1_WATCHDOG_V2_4

# Officina P1 watchdog-freeze v2.4 — independent X-line confirmation

**Reviewer.** Claude Code, model `claude-opus-4-8` (Opus 4.8), fresh session.
Bounded independent engineering audit. No redesign performed. Existing files
were not modified and nothing was committed.

**Verdict.** `REVISE_OFFICINA_P1_WATCHDOG_V2_4`. The two v2.4 governing
specifications are behaviourally complete, constructible, and — within every
guard's own scan region — internally non-self-refusing. One material internal
defect blocks confirmation: peer amendment §A9 locates its indivisible twin's
identical handoff at a **nonexistent composite section (§P1-19)**, in the exact
clause that closes `Y23-3`/`DA-5`. The fix is a single-token correction
(§P1-19 → §P1-14.8) and is non-blocking to constructibility, so the verdict is
`REVISE`, not `BLOCKED`. **The watchdog author-choice token is NOT authorized.**

---

## 1. Exact-byte custody — all four recomputed and matched

```text
packet     ce68b810611304b3877b6ecc227ce5c7a02e3d7b939183089a90d188c1d0ab6f  MATCH
amendment  ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390  MATCH
composite  c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1  MATCH
closure    1e230432a6e81c8b7705257168a9e8fa192a634afce076e568d3be422ed856d9  MATCH
```

Cross-check of the cited review custody:
- v2.3 X report `opus_officina_p1_watchdog_v2_3_final_x_confirmation.md` recomputes
  to `654261d9…`, matching the packet §0.1 citation. Verdict `REVISE`.
- v2.3 Y report `sol_officina_p1_watchdog_v2_3_final_y_confirmation.md`. Verdict `REVISE`.
- The packet's quotation of both finding sets (`X23-B1..M4`, `Y23-1..7`) is
  faithful to the source reports.

## 2. Independence attestation

v2.3 and v2.4 — both author-choice packets, the v1.1 peer amendment, and
composite v1.4 — were authored by the **Opus 5** specification-author instance.
The v2.3 X-line confirmation was produced by that same instance (the independence
defect §7 records honestly). **I am Opus 4.8, a distinct model in a fresh
session; I did not author v2.3 or v2.4 and am not the Opus 5 instance.** I am an
admissible independent X-line reviewer. The author closure
(`opus5_…_v2_4_closure.md`) was treated as untrusted and was not relied on for
any conclusion below; every fact was recomputed from the two governing files.

---

## 3. Bounded-audit results (independently recomputed)

### Item 1 — historical→governing restatement checklist: CONFIRMED, fully constructible
Every rule the v2.3 restatement dropped is now present in governing bytes and
buildable without opening any historical document:

| Required construct | Governing locus | Constructible from bytes alone |
|---|---|---|
| quiescence constants `QC-1..QC-5` (8 passes, 100 ms, 1 s; 60 s named as reference) | amend. §A3.0 | yes |
| forbidden dispositions / single-valued cause / routing `FD-1..FD-4` | amend. §A3.6 | yes |
| ack frame + predicates + timing `AK-1..AK-7`, ack schema keys | amend. §A8.1 (§A8.2 restates PUB) | yes |
| lease-table publication `PUB-1..PUB-4` | amend. §A8.2 | yes |
| replacement-freeze/resume/invalidation objects, `I1..I7`, `S1/S2`, `ACK_PENDING`, three states w/ precedence | amend. §A7.2–§A7.3 | yes |
| total cross-class consumption / duplicate / conflict / fallback priority `TO-1..TO-5` | amend. §A6.1 | yes |
| strict-progress branch (no zero-overrun, no tolerance) | amend. §A3.4 | yes |

`QC-5` and `N-9` correctly frame `QC-1..QC-3` as restatements, not new
constants; `ACK_PENDING` needs no marker record (it is exactly the state where
the `REPLACEMENT_FREEZE` record exists and neither transition marker does) and is
bounded by `min(deadline_ns, updated+ACK_ABSENCE_TIMEOUT)`; the `I1..I7` /
`RESUMABLE` / `ACK_PENDING` precedence is total and mutually exclusive.

### Item 2 — ordinary stop legal; freeze terminals forbidden; cause single-valued: CONFIRMED
- Ordinary harness P3→P4 `T_PROCESS_RESOURCE_STOP` is fully retained and is **not**
  a freeze of this amendment (`FD-2`; a build removing it is nonconforming).
- Exactly **five** dispositions are forbidden on both the deadline freeze and the
  swap-only freeze (`FD-1`): `T_PROCESS_CLOSED`, `T_PROCESS_VOLUNTARY_STOP`,
  `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE`, `T_PROCESS_RESOURCE_STOP`. No
  valid terminal is reachable from any freeze (§A3.4: "no valid terminal
  reachable from any freeze"; §A5 conjunct 9 binds `PROVED`/`UNKNOWN` shapes).
  This closes `X23-B2`/X-C4.1.
- Cause is single-valued `PROCESS` on `ROUTE-D` and `ROUTE-W` alike (`FD-3`).

### Item 3 — ROUTE-D/W exhaustive, one procedure, one writer: CONFIRMED
§A3.1 makes the two routes exhaustive ("no third entry … no other process enters
it on any path") and the SAME procedure/actor/mediation/evidence-class/namespace/
writer/`killer`. One evidence writer (`WA-2`, composite §P1-13.7, invariant 89).
Every group stop through `SIGNAL_GROUP` (`WA-1`). The PCS §P1-10.7 classifier is
the separate signed P1 execution site and writes **no** `t-freeze-observation.v1`
(invariant 89(b)), so single-writer is preserved.

### Item 4 — G-10 uniqueness / no self-match; AD-1 distinct: CONFIRMED (with a bounded scope note)
- `G-10` is reserved uniquely for the `VARIANT_MARKER` guard (§P1-14.4:
  "No other rule … carries the identifier `G-10`"). The §P1-14.3 authoring
  discipline is renamed `AD-1` and ranges over `G-1..G-5` only; `VARIANT_MARKER`
  is outside `AD-1`'s range → the two never range over the same class. Closes
  `X23-B4`/`Y23-5.4`.
- **No self-match inside G-10's scan region.** `G-10` matches `NORMALIZE(REGION(BODY))`
  (composite lines 221–3242). Within that region: `G-10`'s own definition (§P1-14.4,
  lines 2840–2857) and test 102 (line 3196) contain **zero** literal markers
  (verified: the definition states "THE PATTERN STRINGS ARE NOT REPRODUCED HERE";
  test 102 paraphrases). The literal patterns `"[W-A]"`/`"[W-B]"` live once in
  `GUARDDATA` (§P1-17, line 3282), which is a separate region and never a match
  target.
- Marker census (whole file): 13 `[W-A]` + 13 `[W-B]` = 26. Balance holds: 12/12
  outside `GUARDDATA` and 1/1 inside it.
- **Scope note (non-blocking):** the closure's "24 body markers … all inside
  variant blocks" conflates two things. Only **20** markers (10/10) sit inside
  `REGION(BODY)`, all in resolvable variant blocks (§P1-1.3, §P1-9.2, §P1-10.5/6,
  §P1-13.2, tests 61/89/99). The other **4** (lines 62/63/66) sit in the
  *normative preamble* blocking notice, which lies outside all three regions and
  is covered by `H_FILE`/`G-7` but **not** scanned by `G-10`. Those four are a
  definitional legend describing the variant scheme, carried unchanged since v1.3
  and accepted by the prior architecture confirmations — not operative variant
  branches. They do not let an operative variant escape the gate, and they cannot
  cause `G-10` to self-match (out of scan range). This is an observation on the
  closure's wording, not a governing-file defect.

### Item 5 — G-11 seven-class set, install order, non-circular trust; handoff in both files: **DEFECT (see §4)**
- Seven pairwise-disjoint, exhaustive member classes `M1..M7` with no wildcard /
  directory scan (amend. §A10.1, composite §P1-14.4). Content-addressed id;
  external trust root (author signature file — not a member, pre-existing,
  written by no handoff step); no self-attestation (`IR-4`, test 115); baseline
  verifier excluded from `M2` and post-handoff verifier pinned as `M5`
  (§P1-18 exception resolves the "gate forbids its own installation" circularity);
  stale/substituted verifier caught (`MEMBER_STALE`/`MEMBER_SUBSTITUTED`, tests
  109/110); mixed generation rejected (`IR-11`, test 114). Install order
  (`IR-6`/`IR-9`) is non-circular and self-consistent. **All CONFIRMED.**
- The complete handoff **is** stated in both governing files, not in a closure:
  amend. §A9 (`H-1..H-4`, ten ordered steps) and composite §P1-14.8 carry
  byte-equivalent content, and both explicitly refuse to defer to any closure
  (`DA-5`, §A9/§P1-14.8 headers). Substantively `Y23-3` is closed.
- **BUT the peer amendment mis-locates the composite copy** — see §4. This is why
  item 5 is not fully clean and the round is `REVISE`.

### Item 6 — counting rule and 180 = 126 + 54: CONFIRMED, reproducible
Recomputed independently from the two files:
- File 1 (amendment): tagged rules **96** (DA5+WA6+TIMING4+QC5+FD4+F8+KW3+FB5+
  TO5+RF3+NS4+AK7+PUB4+H4+IR12+M7+N10 = 96) + §A5 conjuncts **10** + §A3.3 steps
  **6** + routes **2** + swap-only units **12** (I1..I7 + S1/S2 + 3 states) = **126**.
- File 2 (composite): behavioural repairs **23** (R1..R22 + invariant 60) + new
  sections **4** (§P1-10.6, §P1-10.7, §P1-13.9, §P1-14.8) + guard rules **3**
  (G-10 redefined, G-11 new, AD-1 renamed) + new test rows 92..115 **24** = **54**.
- Total **180**. Categories are pairwise disjoint (`I1..I7`/`S1`/`S2`/states appear
  only in the swap-only family, not in the tagged families). The three accountings
  are kept distinct (§3.4): governing loci (180), provenance occurrences (76 + the
  named chain additions), and the generated install record (neither). Confirmed
  distinct.

### Item 7 — partial-install fixtures; sole runnable row; no partial runnable state: CONFIRMED
Rows 104–115 exhaustively exercise the gate; 107/108/109 are seven fixtures each
(one per class), so omission/extra/staleness are covered per-class, not sampled:
absent (104), name-mismatch (105), unauthorized (106), omitted×7 (107), extra×7
(108), stale×7 (109), substituted verifier incl. baseline and G-10-xor-G-11 (110),
substituted manifest (111), substituted/omitted/never-run test bundle (112),
attestation mismatch (113), mixed generation (114), no self-attestation (115).
Manifest, verifier, attestation and test-bundle substitutions are each attempted
and each refuses. Fail-closed with no partial/warning/override mode
(`IR-10`, §P1-14.4). **Exactly one state is runnable** — the fully-correct,
authorized, matching install — and no perturbed/partial state reaches a
production entry point.

### Item 8 — W-A/W-B unresolved; recommendation and scientific boundaries unchanged: CONFIRMED
Both options remain unselected and non-operative (blocking notice; `G-10` refuses
any surviving marker; `N-1` amendment, `§8` packet). `W-B` remains recommended on
the same five criteria with nothing asymmetric between options (packet §5,
amend. `N-2`). Prior accepted boundaries preserved: blocker proved on four
mechanisms, PCS never retains the update-pipe write end, PCS sole caller of the
wait/kill family (two sites are not two callers), PCS journal scientifically
invisible, identity cell neither selected nor repaired, signed tokens not
revoked, zero historical bytes edited, `T = NOT_ACTIVATED`, claim `OPEN`
(amend. `N-1..N-10`, packet `N-1..N-11`, invariants 87/89).

---

## 4. The single blocking-to-confirmation finding

**`FX24-1` — peer amendment §A9 cites a nonexistent composite section for the
identical handoff.**

```text
amendment  OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
           line 890–891, §A9 header:
             "This list is COMPLETE and is stated IDENTICALLY in
              composite v1.4 §P1-19."
```

- Composite v1.4 has **no §P1-19**. Its highest section is §P1-18 (Provenance),
  and the identical handoff lives at **§P1-14.8** (verified: a full-file search
  for "P1-19" in the composite returns zero occurrences).
- Every other locator in the pair is correct and names §P1-14.8:
  composite line 128 ("stated IN FULL at §P1-14.8 of this file and identically at
  §A9 of that amendment"), composite §P1-14.8 line 3049 ("identically at §A9 of
  the peer amendment"), and packet §2/§3.3 (which enumerate §P1-14.8 as the
  handoff section). Only the amendment's own §A9 header is wrong.

**Why this matters, and why it is `REVISE` not a nit.** §A9 is the clause that
closes `Y23-3`/`DA-5`: its guarantee is that the complete handoff is present and
cross-checkable in *both* governing files, deferring to no closure. That
guarantee is precisely what a reader is invited to verify — and a reader
following §A9's own pointer to "composite §P1-19" finds nothing, so the
anti-closure/mutual-presence property the section asserts cannot be confirmed
from the amendment's stated locator. A governing byte that makes a provably false
structural claim about its indivisible twin is an internal-consistency defect,
and this is exactly the mis-citation class (cf. the `G-10` identifier collision)
that self-review under-detects and an independent pass exists to catch (§7).

**Why not `BLOCKED`.** The handoff *content* is fully present and byte-equivalent
in both files (§A9 and §P1-14.8), so the pair remains constructible and no guard,
count, predicate or behaviour depends on the "§P1-19" string. Nothing self-
refuses. The defect is bounded and mechanical.

**Bounded fix (author only; this review changes nothing).** In amendment §A9,
replace "composite v1.4 §P1-19" with "composite v1.4 §P1-14.8". Re-issue on
identical-bytes for a fresh independent X/Y round.

---

## 5. Disposition

- `REVISE_OFFICINA_P1_WATCHDOG_V2_4`.
- The two governing specifications are behaviourally complete, constructible, and
  non-self-refusing within each guard's scan region; the count `180 = 126 + 54`
  is reproducible; `G-10` is unique and does not self-match; `G-11`'s trust is
  non-circular with no partial runnable state; all prior accepted scientific
  boundaries are unchanged.
- Confirmation is withheld solely on `FX24-1`.
- **Kirill's watchdog author-choice token is NOT authorized.** No token is signed,
  minted, revoked or predicted. No option is selected. No file was modified and
  nothing was committed. `T` remains `NOT_ACTIVATED`; the programme claim remains
  `OPEN`.

REVISE_OFFICINA_P1_WATCHDOG_V2_4
