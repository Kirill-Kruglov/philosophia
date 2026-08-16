# Essay status reconciliation — V2.1 targeted assembly repair (Claude)

Role: bounded assembly repairer. Standalone replacement for V2 — Cursor applies
this file alone and never merges it with V2. Read-only except for this response
file; no target/evidence/canonical/runtime/historical file edited, no experiment
run or resumed, no Part-B outcome inspected, no data/root/train/commit/push. The
author bundle and the seven driver-audit findings are binding; no author choice
is reopened and no new patch or placement is introduced.

---

## 1. Pin verification

All governing objects and all four targets match their pins (recomputed with
`sha256sum`).

| File | Expected | Result |
|---|---|---|
| `successor/dev/ESSAY_STATUS_RECONCILIATION_AUTHOR_DECISION_V1.md` | `0a8a24d4…cec956` | **MATCH** |
| `successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V2.md` | `f22c28b4…94c5de` | **MATCH** |
| `README.md` | `d5ae3259…f4839` | **MATCH** |
| `essay/README.md` | `9908f5c8…01346` | **MATCH** |
| `essay/REVIEW_HANDOFF.md` | `53b0448d…bccbe4` | **MATCH** |
| `essay/climbing-the-wall-of-experience.md` | `76919e8f…e55d0f` | **MATCH** |

Driver audit `ESSAY_STATUS_RECONCILIATION_V2_DRIVER_AUDIT.md` read in full; its
seven findings (Major 1–5, Minor 1–2) are treated as the exhaustive repair set.
Targets are unchanged, so every V2 `OLD_TEXT`/anchor remains byte-exact and
unique; only `NEW_TEXT`/evidence/rationale change where a finding requires it.

---

## 2. Corrected primary-source table

Re-verified live, including the full-text page (Minor 1 correction applied). The
exact parameter count **is** in the paper's full text; the abstract rounds it;
publication prose deliberately keeps the rounded form.

| Fact used in prose | Primary URL | Verified quote / finding |
|---|---|---|
| Minimo jointly poses conjectures and proves them, bootstrapping from axioms | https://arxiv.org/abs/2407.00695 | "jointly learns to pose challenging problems for itself (conjecturing) and solve them (theorem proving)"; can "bootstrap from only the axioms" |
| Minimo domains: propositional logic, arithmetic, group theory | https://arxiv.org/abs/2407.00695 | "3 axiomatic domains (propositional logic, arithmetic and group theory)" |
| Hamilton-Zero foundation model; prose uses **roughly 0.5B** parameters | https://arxiv.org/abs/2608.11911 (abstract) | abstract: "a foundation model with ∼0.5B variational parameters" |
| Exact count exists in the paper (not used verbatim in prose) | https://arxiv.org/html/2608.11911v2 (full text, Introduction) | "At 547,521,152 variational parameters, Hamilton-Zero is, to our knowledge, the largest wavefunction ansatz yet trained for spin systems." |
| Pretraining over hundreds of thousands of Hamiltonian systems varying topology, size, interaction type/strength | https://arxiv.org/abs/2608.11911 | "pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths" |
| Source released | https://github.com/simulacra-research/HamiltonZero | README: first-party "source, datasets, and released model weights are licensed under Apache-2.0" |
| Foundation checkpoint released | https://huggingface.co/simulacra-research/HamiltonZero | "the directly loadable HamiltonZero v1 foundation checkpoint at `weights/hamiltonzero_v1.eqx`" |

Meta-record correction (was wrong in V2): the exact `547,521,152` figure is
**present** in the arXiv v2 full-text Introduction and consistent with the
abstract's `∼0.5B`. The prose keeps `roughly 0.5B` for readability and does not
claim the exact count was absent.

---

## 3. Mechanical patch specification (all nine, standalone)

### Patch 1 — README successor-status paragraph (P1 carrier split + P4 currency; Major 1 scoping)

```text
PATCH_ID:    1
TARGET_FILE: README.md
ANCHOR_TEXT: > **Successor status: stopped at development gates.**
OPERATION:   REPLACE
OLD_TEXT:
> **Successor status: stopped at development gates.** The `officina` governance
> harness is frozen after terminal structural review; it is not an active route.
> The walk-world learner branch closed without competence, and the later
> equational Wall-B cell produced only 2/40 screen-qualified fresh
> presentations against a preregistered minimum of 5. No successor ACTIVE/YOKED
> comparison, scientific lock, outcome, or programme claim exists.
NEW_TEXT:
> **Successor status: stopped at development gates.** The `officina` governance
> harness is frozen after terminal structural review; it is not an active route.
> The walk-world learner branch closed without competence. In the later
> equational Wall-B cell the library carrier is `CLOSED / SPARSE` (2/40
> screen-qualified fresh presentations against a preregistered minimum of 5),
> while the candidate-ordering policy carrier is `SCREEN-VIABLE` (12/40, Wilson
> 95% [0.181, 0.454]) and was left unrun by author choice. A later MINIMO-based
> route had its Phase-2 Stage-A engineering surface accepted and its Stage-B
> L0–L3 surfaces accepted, but the Stage-R route ended at its minimum-L4 paper
> boundary and a purpose-built E2 alternative stopped at IDEA_GATE before build;
> active substrate search is now stopped. No L4 implementation or Stage-R root,
> learner/selector execution, ACTIVE/YOKED comparison, scientific lock, outcome,
> or programme claim followed.
EVIDENCE:
- WALLB_EQUATIONAL_CELL_CLOSURE.md (library CLOSED/SPARSE 2/40 vs floor 5;
  policy SCREEN-VIABLE 12/40 Wilson [0.181,0.454], ACTIVE/YOKED unrun by choice)
- WALLB_POLICY_CHANNEL_AUDIT_14B.md (12/40; Wilson [0.181,0.454])
- PHASE2_STAGE_A_DRIVER_CLOSURE_19.md (STAGE_A_ACCEPTED)
- recovery/phase2_stage_b_20260815/README.md (accepted Stage-B L0–L3 surfaces)
- stage_r/l4/STAGE_R_L4_MINIMUM_ANNEX_V1_1_DRIVER_BOUNDED_CONFIRMATION.md
  (RETURN_TO_IDEA_GATE; minimum-L4 not implementable)
- stage_r/idea_gate/STAGE_R_E2_IDEA_GATE_DRIVER_SYNTHESIS_V1.md
  (STOP_STAGE_R_E2_BEFORE_BUILD; active substrate search STOP)
RATIONALE:
Restores the second Wall-B carrier and the Stage-A/Stage-B chronology, and
scopes the closing denial to the unimplemented L4/Stage-R route so it no longer
falsely denies the Phase-1 exploratory MINIMO learner run. Status altitude only.
```

### Patch 2 — README Research route (P1 frame-gate correction + P4 currency; Major 3 Stage-B)

```text
PATCH_ID:    2
TARGET_FILE: README.md
ANCHOR_TEXT: The current route ends here. The signed
OPERATION:   REPLACE
OLD_TEXT:
The current route ends here. The signed
[`Route B author decision`](canonical/AUTHOR_ROUTE_DECISION.md) led first to the
[`Officina successor`](successor/officina/README.md), whose governance harness
is now [frozen](src/philosophia/officina/FROZEN.md). Two later non-citable
development branches also stopped before a scientific lock: the walk-world
path-manufacture axis was void by construction, and the equational Wall-B cell
failed its preregistered five-world frame gate. The registered chosen-contact
contrast remains unrun.
NEW_TEXT:
The current route ends here. The signed
[`Route B author decision`](canonical/AUTHOR_ROUTE_DECISION.md) led first to the
[`Officina successor`](successor/officina/README.md), whose governance harness
is now [frozen](src/philosophia/officina/FROZEN.md). Several later non-citable
development branches also stopped before a scientific lock, for different
reasons: the walk-world path-manufacture axis was void by construction; in the
equational Wall-B cell the library carrier failed its preregistered five-world
frame gate while the policy carrier passed its screen and was deliberately not
spent; and a later MINIMO-based route reached accepted Phase-2 Stage-A and
Stage-B L0–L3 engineering surfaces but stopped before any scientific execution,
its Stage-R route ending at a minimum-L4 paper boundary and a purpose-built E2
alternative stopping at IDEA_GATE before build. Active substrate search is now
stopped, and the registered chosen-contact contrast remains unrun.
EVIDENCE: same objects as Patch 1.
RATIONALE:
Corrects the whole-cell "failed the frame gate" claim (only the library carrier
failed) and adds the accepted Phase-2 Stage-A AND Stage-B L0–L3 engineering
surfaces, keeping the minimum-L4 and E2-before-build stops distinct.
```

### Patch 3 — Essay Introduction: Hamilton-Zero neighbour (P6; Minor 2 opening)

```text
PATCH_ID:    3
TARGET_FILE: essay/climbing-the-wall-of-experience.md
ANCHOR_TEXT: [Computational Life](https://arxiv.org/abs/2406.19108) work he co-authored shows
OPERATION:   INSERT_AFTER
OLD_TEXT:
[Computational Life](https://arxiv.org/abs/2406.19108) work he co-authored shows
self-replicating programs arising in a soup of random ones with no fitness
function imposed: structure from interaction, with nobody supplying the
structure.
NEW_TEXT:
 A different at-scale neighbouring form has now appeared:
[Hamilton-Zero](https://arxiv.org/abs/2608.11911), a foundation model with
roughly 0.5B variational parameters, is pretrained over hundreds of thousands of
generated Hamiltonian systems that vary in connection topology, system size, and
interaction type and strength, with its
[source](https://github.com/simulacra-research/HamiltonZero) and a
[foundation checkpoint](https://huggingface.co/simulacra-research/HamiltonZero)
released. Its scale makes it a stronger contemporary form of amortized learning
across generated systems than any position paper, but it is not a completed
answer to the question here: it does not isolate self-selected contact from
matched donated contact.
EVIDENCE: arXiv 2608.11911 (v2 2026-08-13; abstract "∼0.5B"; full-text
  Introduction "547,521,152 variational parameters"); github/huggingface
  simulacra-research (source + checkpoint, see §2). Prose uses the rounded
  "roughly 0.5B".
RATIONALE:
Adds Hamilton-Zero as a current neighbouring empirical system in the existing
"stronger and more current forms" discussion; the opening no longer identifies
it with the preceding emergence-from-interaction bet, and the explicit
non-isolation limit is retained.
```

### Patch 4 — Essay: TWOPRES scoped boundary (P3; unchanged)

```text
PATCH_ID:    4
TARGET_FILE: essay/climbing-the-wall-of-experience.md
ANCHOR_TEXT: What they carry forward is a constraint on any next
OPERATION:   INSERT_AFTER
OLD_TEXT:
What they carry forward is a constraint on any next
world intended to test path-manufactured structure, not a verdict on chosen
contact.
NEW_TEXT:


A separate non-citable development line reached a related boundary from the side
of representation rather than contact. Under the unpaired-stream interface
considered by that line (TWOPRES), element correspondence between two
presentations of one finite monoid is identifiable at best up to `Aut(M)`; the
line closed as `NOT_CHEAPLY_AUDITABLE` before any implementation. It is a mapped
development boundary under that interface, not an experiment and not a claim
about representations in general.
EVIDENCE: TWOPRES_LINE_CLOSURE.md (closure token NOT_CHEAPLY_AUDITABLE;
  retained finding 1: identifiable only up to Aut(M) for the unpaired streams;
  "no run performed").
RATIONALE:
Ratified scoped claim, no stronger than up to Aut(M) and restricted to the
unpaired-stream interface; no "for any method whatsoever" and no generalization
of monoids to all representations. Unchanged from V2.
```

### Patch 5 — Essay: bounded Minimo paragraph (P5; unchanged)

```text
PATCH_ID:    5
TARGET_FILE: essay/climbing-the-wall-of-experience.md
ANCHOR_TEXT: measure the prevalence of the mechanism an experiment needs before selecting a
OPERATION:   INSERT_AFTER
OLD_TEXT:
measure the prevalence of the mechanism an experiment needs before selecting a
convenient world and mistaking it for a family, and do not rewrite a correctly
earned sparse kill when a different carrier later screens.
NEW_TEXT:


[Minimo](https://arxiv.org/abs/2407.00695), an agent that jointly learns to pose
conjectures and prove them, bootstrapping from the axioms of propositional
logic, arithmetic and group theory, is the nearest external instance of a
self-teaching formal substrate. This programme ran one repository-default
exploratory realization of it, trained on self-generated formal material and
evaluated on a fixed human-written theorem panel — the only point at which such a
substrate was actually run here, and its fixed-panel transfer measured. It is
non-citable development: not ACTIVE/YOKED evidence, not the programme's
cross-world or presentation transfer, and not a Philosophia result. A later route
built on the same substrate stopped before any scientific execution, and active
substrate search is now stopped; the programme claim remains open.
EVIDENCE: arXiv 2407.00695 (see §2); PHASE1_TERMINAL_18.md
  (EXPLORATORY_FEASIBILITY_OBSERVED__NO_PHILOSOPHIA_CLAIM; one unseeded
  repository-default CPU-debug realization; fixed 30-item human-written panel;
  "not … a general Philosophia effect"); stage_r/README.md and E2 synthesis
  (later route stopped before build; active substrate search stopped).
RATIONALE:
Distinguishes the external Minimo system from this programme's single
exploratory reproduction; names it as the only point a self-teaching substrate
was run here and its fixed-panel transfer measured. Avoids "external transfer".
Unchanged from V2.
```

### Patch 6 — Essay status ledger: Continuation route row (P4; Major 3 Stage-B)

```text
PATCH_ID:    6
TARGET_FILE: essay/climbing-the-wall-of-experience.md
ANCHOR_TEXT: | Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** |
OPERATION:   REPLACE
OLD_TEXT:
| Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** | Route B produced no locked successor scientific test: walk-world path-manufacture was void by construction; the equational cell is closed on both carriers with different verdicts (library sparse; policy screen-viable and left unrun); Officina remains frozen rather than active |
NEW_TEXT:
| Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** | Route B produced no locked successor scientific test: walk-world path-manufacture was void by construction; the equational cell is closed on both carriers with different verdicts (library sparse; policy screen-viable and left unrun); a later MINIMO-based route had its Phase-2 Stage-A and Stage-B L0–L3 engineering surfaces accepted but stopped before any scientific execution, the Stage-R route ending at its minimum-L4 paper boundary and a purpose-built E2 alternative stopping at IDEA_GATE before build; active substrate search is now stopped; Officina remains frozen rather than active |
EVIDENCE: same objects as Patch 1.
RATIONALE:
Brings the single ledger row current, now naming both accepted engineering
surfaces (Phase-2 Stage-A and Stage-B L0–L3) as engineering, not scientific,
acceptance; other ledger rows untouched.
```

### Patch 7 — essay/README.md currency (P4; Major 2 Stage-R correction)

```text
PATCH_ID:    7
TARGET_FILE: essay/README.md
ANCHOR_TEXT: on a future author-signed programme redesign, not authorized continuation.
OPERATION:   INSERT_AFTER
OLD_TEXT:
scientific endings: proof, falsification, and mapped boundary remain conditional
on a future author-signed programme redesign, not authorized continuation.
NEW_TEXT:


Beyond that signed route, several non-citable successor development branches also
stopped before any scientific lock: the walk-world path-manufacture axis (void by
construction), both equational Wall-B carriers (library sparse; policy
screen-viable and left unrun), and a later MINIMO-based route whose Phase-2
Stage-A and Stage-B L0–L3 engineering surfaces were accepted, whose Stage-R route
then ended at the minimum-L4 paper boundary, and whose purpose-built E2
alternative stopped at IDEA_GATE before build. Active substrate search is stopped
and the programme claim remains open.
EVIDENCE: same objects as Patch 1.
RATIONALE:
Removes the false "Stage-R and E2 stages stopped before build" grouping and
states the three distinct facts: Phase-2 Stage-A/Stage-B L0–L3 accepted; Stage-R
route ended at the minimum-L4 paper boundary; E2 stopped at IDEA_GATE before
build.
```

### Patch 8 — REVIEW_HANDOFF.md status currency (P4; Major 1 scoping + Major 4 nine-path list)

```text
PATCH_ID:    8
TARGET_FILE: essay/REVIEW_HANDOFF.md
ANCHOR_TEXT: turn this process boundary, Level 0, or any design artifact into a scientific
OPERATION:   INSERT_AFTER
OLD_TEXT:
turn this process boundary, Level 0, or any design artifact into a scientific
ending.
NEW_TEXT:


## Current successor boundary (status only, non-citable development)

Since this draft was first circulated, the successor stopped at development gates
without any scientific execution. At status altitude: the walk-world learner
branch closed without competence; the equational Wall-B library carrier is
`CLOSED / SPARSE` (2/40) and the policy carrier is `SCREEN-VIABLE` (12/40) and
left unrun by author choice; a later MINIMO-based route had Phase-2 Stage-A and
Stage-B L0–L3 engineering surfaces accepted and its Stage-R projection-only L3
surface accepted and closed, but the Stage-R route then ended at its minimum-L4
paper boundary and the E2 alternative stopped at IDEA_GATE before build. An
exploratory MINIMO learner was trained and evaluated on a fixed human-written
panel in Phase 1; the later Stage-R route minted no root and executed no learner.
Active substrate search is stopped; no L4 implementation or Stage-R root,
learner/selector execution, ACTIVE/YOKED comparison, scientific lock, outcome, or
programme claim followed; the programme claim remains `OPEN`. Authoritative status
objects (non-citable):
`successor/dev/WALLB_EQUATIONAL_CELL_CLOSURE.md`,
`successor/dev/WALLB_POLICY_CHANNEL_AUDIT_14B.md`,
`successor/dev/PHASE1_TERMINAL_18.md`,
`successor/dev/PHASE2_STAGE_A_DRIVER_CLOSURE_19.md`,
`successor/recovery/phase2_stage_b_20260815/README.md`,
`successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_CLOSURE_V1.md`,
`successor/stage_r/l4/STAGE_R_L4_MINIMUM_ANNEX_V1_1_DRIVER_BOUNDED_CONFIRMATION.md`,
`successor/stage_r/README.md`,
`successor/stage_r/idea_gate/STAGE_R_E2_IDEA_GATE_DRIVER_SYNTHESIS_V1.md`.
EVIDENCE: the nine authoritative status objects listed above.
RATIONALE:
Retains the full Stage-A/Stage-B/L3/L4/E2 chronology, scopes the negative to no
Stage-R root or learner/selector execution (explicitly noting the Phase-1
exploratory MINIMO learner did run), and expands the authoritative-object list
to all nine driver-audit paths. Existing status paragraph, `Read first` list, and
shared prohibitions are left verbatim and in place.
```

### Patch 9 — REVIEW_HANDOFF.md added prohibitions (P4; Major 5 L4 reclassification)

```text
PATCH_ID:    9
TARGET_FILE: essay/REVIEW_HANDOFF.md
ANCHOR_TEXT: - Do not remove uncomfortable limits for rhetorical flow.
OPERATION:   INSERT_AFTER
OLD_TEXT:
- Do not remove uncomfortable limits for rhetorical flow.
NEW_TEXT:

- Do not promote any successor development screen (the Wall-B library or policy
  carrier), accepted engineering surface (Phase-2 Stage-A/B or Stage-R L3), the
  minimum-L4 paper boundary, or the E2 IDEA_GATE stop into a scientific result,
  ACTIVE/YOKED outcome, or programme claim.
- Do not state B2 Slot 4c as closed or add its diagnostic anywhere; it has no
  formal author closure.
- Do not state the TWOPRES element-correspondence boundary as anything stronger
  than a non-citable mapped development boundary, up to `Aut(M)` and only under
  the unpaired-stream interface; do not generalize it to representations in
  general.
- Do not describe the Minimo fixed-panel evaluation as the programme's
  cross-world or presentation transfer or as an ACTIVE/YOKED result, and do not
  describe Hamilton-Zero as testing self-selected contact, path independence, or
  the Philosophia causal contrast.
EVIDENCE: author decision V1 items 2–6; STANDING_RULES.md (screens/closures are
  not results); driver audit Major 5.
RATIONALE:
Distinguishes accepted engineering surfaces (Phase-2 Stage-A/B, Stage-R L3) from
the minimum-L4 paper boundary and the E2 IDEA_GATE stop, correcting the V2
grouping of L4 as an engineering closure. All pre-existing shared prohibitions
are preserved verbatim.
```

---

## 4. Seven-finding closure table (keyed to the driver audit)

| Finding | Repair | Patch(es) | Closed? |
|---|---|---|---|
| Major 1 — unscoped learner-run denial | Scope denial to L4/Stage-R; note Phase-1 learner ran | 1, 8 | **Yes** |
| Major 2 — Stage-R described as stopping before build | State three distinct facts; L3 accepted/closed, only minimum-L4 at paper boundary, E2 at IDEA_GATE | 7 (+ 8 chronology) | **Yes** |
| Major 3 — Stage-B L0–L3 omitted on two surfaces | Add accepted Phase-2 Stage-B L0–L3 (engineering only) | 2, 6 | **Yes** |
| Major 4 — REVIEW_HANDOFF evidence list incomplete | Expand to all nine authoritative paths | 8 | **Yes** |
| Major 5 — L4 misclassified as engineering closure | Distinguish engineering surfaces (Stage-A/B, Stage-R L3) / minimum-L4 paper boundary / E2 IDEA_GATE stop | 9 | **Yes** |
| Minor 1 — exact Hamilton-Zero parameter count | Correct meta-record: `547,521,152` in full-text Introduction, `∼0.5B` in abstract; prose keeps rounded form | §2 | **Yes** |
| Minor 2 — avoid identifying HZ with preceding bet | Open with "A different at-scale neighbouring form has now appeared:"; retain non-isolation | 3 | **Yes** |

---

## 5. Coverage tables

| Bundle item | Decision | Patch(es) | Closed? |
|---|---|---|---|
| P1 (both README statements) | APPLY_WITH_README_ROUTE_CORRECTION | 1, 2 | **Yes** |
| P2 (Slot 4c) | DEFER_NO_SLOT_CLOSURE | none | **Absent** (prohibition in 9) |
| P3 (TWOPRES) | APPLY_SCOPED_TO_UNPAIRED_STREAM_INTERFACE | 4 | **Yes** (unchanged) |
| P4 (status currency) | APPLY_AS_REQUIRED_STATUS_CURRENCY | 1, 2, 6, 7, 8, 9 | **Yes** |
| P5 (bounded Minimo) | APPLY_BOUNDED_MINIMO_PARAGRAPH | 5 | **Yes** (unchanged) |
| P6 (Hamilton-Zero) | APPLY_PRIMARY_SOURCE_VERIFIED_HAMILTON_ZERO | 3 | **Yes** |

| Target file | Patches | Status |
|---|---|---|
| `README.md` | 1, 2 | both carriers; Stage-A + Stage-B L0–L3; scoped Stage-R denial; frame-gate corrected |
| `essay/climbing-the-wall-of-experience.md` | 3, 4, 5, 6 | Hamilton-Zero, TWOPRES, Minimo added; ledger row current with Stage-B L0–L3 |
| `essay/README.md` | 7 | three distinct Stage-R facts; no "stopped before build" grouping |
| `essay/REVIEW_HANDOFF.md` | 8, 9 | full chronology, nine-path list, scoped denial; L4 reclassified; existing text verbatim |

### Cross-surface chronology consistency (repair item 9)

The four final surfaces read together without contradiction: an exploratory
MINIMO learner **ran** in Phase 1 (essay Patch 5; REVIEW_HANDOFF Patch 8), while
the later **Stage-R route minted no root and executed no learner** (README
Patches 1–2 scoped denial; essay/README Patch 7; ledger Patch 6; REVIEW_HANDOFF
Patch 8). Accepted **engineering** surfaces (Phase-2 Stage-A/B, Stage-R L3) are
never labelled scientific; the minimum-L4 paper boundary and the E2 IDEA_GATE
stop are kept distinct on every surface; the programme claim is `OPEN` everywhere.

---

## 6. Negative-drift and no-Part-B confirmations

| Preservation rule | Status |
|---|---|
| Three endings not restructured or collapsed | **Held** — no patch touches §VII |
| Walk-world void row; both Wall-B rows; H4; 24/12/0; `REPRODUCED, PLATFORM ONLY` preserved | **Held** — untouched |
| "What this does not show" extended, not replaced | **Held** — patches 4, 5 INSERT_AFTER; existing prose unchanged |
| P2 (Slot 4c) absent everywhere | **Held** — no diagnostic/probe phrase/displacement figure in any patch |
| Patch 4 (TWOPRES) and Patch 5 (Minimo) substantively unchanged | **Held** |
| No `BUDGET_MASKED`, `11 -> 13`, wall-second cost, run-invariance, or length-stratum causal story added | **Held** — absent from all NEW_TEXT |
| `1.0` used only for `sign_d` | **Held** — no displacement figure appears |
| No "repeated feasibility deaths" narrative | **Held** — distinct causes named on every surface |
| Hamilton-Zero non-isolation retained; not path independence / causal contrast | **Held** — Patch 3 |
| No new patch, placement, or author decision introduced | **Held** |
| `essay/OUTLINE.md`, canonical, historical, code/JSON/logs untouched | **Held** — not targeted |

No incomplete PHASE1_18 Part-B result directory or log was read or used; no
Part-B fact appears in any patch. No experiment was run or resumed; the dirty
worktree was not touched.

---

## 7. Terminal

All nine patches are standalone and mechanically closed; every anchor and
`OLD_TEXT` is byte-exact and unique against the pinned targets; the seven driver
findings are closed; the exact `547,521,152` figure was verified from the
full-text primary source while the prose deliberately retains `roughly 0.5B`; and
the four final status surfaces carry no chronology contradiction.

```text
READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V2_1
```
