# Essay status reconciliation — V2 assembly (Claude)

Role: bounded assembly analyst. Read-only except for this response file. No
essay/README/handoff/evidence/runtime file was edited; no experiment run or
resumed; no Part-B outcome inspected; no data, root, commit or push. The author
bundle in `ESSAY_STATUS_RECONCILIATION_AUTHOR_DECISION_V1.md` is treated as
binding; no author choice is reopened and no alternative placement is offered.

---

## 1. Pin verification

All governing objects and all four prospective targets match their pins exactly
(recomputed with `sha256sum`).

| File | Expected | Result |
|---|---|---|
| `successor/dev/ESSAY_STATUS_RECONCILIATION_LAUNCH_PACKET_V1.md` | `6b2d01c3…e5bbd` | **MATCH** |
| `successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V1.md` | `22913b3f…573e2` | **MATCH** |
| `successor/dev/ESSAY_STATUS_RECONCILIATION_AUTHOR_DECISION_V1.md` | `0a8a24d4…cec956` | **MATCH** |
| `README.md` | `d5ae3259…f4839` | **MATCH** |
| `essay/README.md` | `9908f5c8…01346` | **MATCH** |
| `essay/REVIEW_HANDOFF.md` | `53b0448d…bccbe4` | **MATCH** |
| `essay/climbing-the-wall-of-experience.md` | `76919e8f…e55d0f` | **MATCH** |

Assembly proceeds against a stable target.

---

## 2. Source verification (Minimo, Hamilton-Zero)

Retrieved live during this pass. One correction to the permitted ceiling is
recorded and applied: the arXiv **abstract states "~0.5B variational
parameters," not the exact `547,521,152`**. The exact figure could not be
confirmed from the abstract, GitHub, or Hugging Face pages fetched, so the
**prose uses only the verified "roughly 0.5B" form.** Every other permitted fact
was confirmed.

| Fact used in prose | Primary URL | Verified quote / finding |
|---|---|---|
| Minimo jointly learns to pose conjectures and prove them, bootstrapping from axioms | https://arxiv.org/abs/2407.00695 | "jointly learns to pose challenging problems for itself (conjecturing) and solve them (theorem proving)"; can "bootstrap from only the axioms" |
| Minimo domains: propositional logic, arithmetic, group theory | https://arxiv.org/abs/2407.00695 | "3 axiomatic domains (propositional logic, arithmetic and group theory)" |
| Hamilton-Zero is a foundation model; **~0.5B** variational parameters | https://arxiv.org/abs/2608.11911 | abstract: "~0.5B variational parameters" (exact `547,521,152` **not** stated on the abstract page; NOT used in prose) |
| Pretraining over hundreds of thousands of Hamiltonian systems varying topology, size, interaction type/strength | https://arxiv.org/abs/2608.11911 | "pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths" |
| Source released | https://github.com/simulacra-research/HamiltonZero | README: first-party "source, datasets, and released model weights are licensed under Apache-2.0" |
| Foundation checkpoint released | https://huggingface.co/simulacra-research/HamiltonZero | "the directly loadable HamiltonZero v1 foundation checkpoint at `weights/hamiltonzero_v1.eqx`" |

arXiv v2 date confirmed: **13 Aug 2026** (title: "Hamilton-Zero: A Neural
Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit
Hamiltonians"). Hamilton-Zero's generated systems are physical (quantum spin
Hamiltonians); prose says "generated Hamiltonian systems," never "formal
systems."

---

## 3. Mechanical patch specification

Nine patches across the four targets. `README.md` carries the shared P1+P4
replacements. Line wrapping in `NEW_TEXT` matches each file's convention.

### Patch 1 — README successor-status paragraph (P1 carrier split + P4 currency)

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
> active substrate search is now stopped. No successor root, learner run,
> ACTIVE/YOKED comparison, scientific lock, outcome, or programme claim exists.
EVIDENCE:
- WALLB_EQUATIONAL_CELL_CLOSURE.md (library CLOSED/SPARSE 2/40 vs floor 5;
  policy SCREEN-VIABLE 12/40 Wilson [0.181,0.454], ACTIVE/YOKED unrun by choice)
- WALLB_POLICY_CHANNEL_AUDIT_14B.md (12/40; Wilson [0.181,0.454])
- PHASE2_STAGE_A_DRIVER_CLOSURE_19.md (STAGE_A_ACCEPTED)
- stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_CLOSURE_V1.md (L3 closed)
- stage_r/l4/STAGE_R_L4_MINIMUM_ANNEX_V1_1_DRIVER_BOUNDED_CONFIRMATION.md
  (RETURN_TO_IDEA_GATE; L4 not implementable)
- stage_r/idea_gate/STAGE_R_E2_IDEA_GATE_DRIVER_SYNTHESIS_V1.md
  (STOP_STAGE_R_E2_BEFORE_BUILD; active substrate search STOP)
RATIONALE:
Restores the second Wall-B carrier the old text omitted and brings the paragraph
current with the MINIMO Stage-R/E2 stop, at status altitude, without narrating
distinct-cause stops as one feasibility pattern.
```

### Patch 2 — README Research route (P1 frame-gate correction + P4 currency)

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
spent; and a later MINIMO-based route reached an accepted Phase-2 Stage-A
engineering surface but stopped before any scientific execution, its Stage-R
route ending at a minimum-L4 paper boundary and a purpose-built E2 alternative
stopping at IDEA_GATE before build. Active substrate search is now stopped, and
the registered chosen-contact contrast remains unrun.
EVIDENCE: same objects as Patch 1.
RATIONALE:
The old sentence said the equational Wall-B cell "failed its preregistered
five-world frame gate" as a whole; only the library carrier failed, while the
policy carrier passed its screen and was deliberately not spent. Also adds the
MINIMO route currency at status altitude.
```

### Patch 3 — Essay Introduction: Hamilton-Zero neighbour (P6)

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
 That bet now has an at-scale empirical form:
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
EVIDENCE: arXiv 2608.11911 (v2 2026-08-13); github/huggingface simulacra-research
  (see §2). Only the verified "~0.5B" figure is used; the exact 547,521,152 count
  was not confirmed and is not used.
RATIONALE:
Adds Hamilton-Zero as a current neighbouring empirical system inside the
existing "stronger and more current forms" discussion, attached to the
emergence-from-interaction line so the subsequent "both are right" reference is
undisturbed. States its scale and its exact limit relative to this essay.
```

### Patch 4 — Essay: TWOPRES scoped boundary (P3)

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
Adds the ratified scoped claim, no stronger than up to Aut(M) and explicitly
restricted to the unpaired-stream interface; does not use "for any method
whatsoever" and does not generalize monoids to all representations.
```

### Patch 5 — Essay: bounded Minimo paragraph (P5)

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
Distinguishes the external Minimo system (primary-source ceiling) from this
programme's single exploratory reproduction (local-evidence ceiling), naming it
as the only point a self-teaching substrate was actually run and its fixed-panel
transfer measured. Avoids the bare phrase "external transfer."
```

### Patch 6 — Essay status ledger: Continuation route row (P4)

```text
PATCH_ID:    6
TARGET_FILE: essay/climbing-the-wall-of-experience.md
ANCHOR_TEXT: | Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** |
OPERATION:   REPLACE
OLD_TEXT:
| Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** | Route B produced no locked successor scientific test: walk-world path-manufacture was void by construction; the equational cell is closed on both carriers with different verdicts (library sparse; policy screen-viable and left unrun); Officina remains frozen rather than active |
NEW_TEXT:
| Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** | Route B produced no locked successor scientific test: walk-world path-manufacture was void by construction; the equational cell is closed on both carriers with different verdicts (library sparse; policy screen-viable and left unrun); a later MINIMO-based route had its Phase-2 Stage-A engineering accepted but stopped before any scientific execution, the Stage-R route ending at its minimum-L4 paper boundary and a purpose-built E2 alternative stopping at IDEA_GATE before build; active substrate search is now stopped; Officina remains frozen rather than active |
EVIDENCE: same objects as Patch 1.
RATIONALE:
Brings the single ledger row current with the MINIMO Stage-R/E2 stop at status
altitude; leaves both Wall-B rows and every other ledger row untouched.
```

### Patch 7 — essay/README.md currency (P4)

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
Stage-A engineering was accepted while its Stage-R and E2 stages stopped before
build. Active substrate search is stopped and the programme claim remains open.
EVIDENCE: same objects as Patch 1.
RATIONALE:
Makes the essay README describe the current bounded-result draft's successor
boundary, not only the old Level-1 stop.
```

### Patch 8 — REVIEW_HANDOFF.md status currency (P4)

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
Stage-B L0–L3 engineering surfaces accepted, but the Stage-R route ended at its
minimum-L4 paper boundary and the E2 alternative stopped at IDEA_GATE before
build. Active substrate search is stopped; no root, learner run, ACTIVE/YOKED
comparison, or scientific outcome followed; the programme claim remains `OPEN`.
Authoritative status objects (non-citable):
`successor/dev/WALLB_EQUATIONAL_CELL_CLOSURE.md`,
`successor/dev/PHASE1_TERMINAL_18.md`, `successor/stage_r/README.md`,
`successor/stage_r/idea_gate/STAGE_R_E2_IDEA_GATE_DRIVER_SYNTHESIS_V1.md`.
EVIDENCE: same objects as Patch 1.
RATIONALE:
Gives a new reviewer the current successor boundary as status-only context.
Existing status paragraph, read list, and shared prohibitions are left verbatim.
```

### Patch 9 — REVIEW_HANDOFF.md added prohibitions (P4)

```text
PATCH_ID:    9
TARGET_FILE: essay/REVIEW_HANDOFF.md
ANCHOR_TEXT: - Do not remove uncomfortable limits for rhetorical flow.
OPERATION:   INSERT_AFTER
OLD_TEXT:
- Do not remove uncomfortable limits for rhetorical flow.
NEW_TEXT:

- Do not promote any successor development screen (the Wall-B library or policy
  carrier), engineering closure (Phase-2 Stage-A/B, Stage-R L3/L4), or IDEA_GATE
  stop (E2) into a scientific result, ACTIVE/YOKED outcome, or programme claim.
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
  not results).
RATIONALE:
Adds the minimum prohibitions to keep successor screens, engineering closures,
IDEA_GATE stops, and the P3/P5/P6 additions from being read as scientific
results. All pre-existing shared prohibitions are preserved verbatim.
```

---

## 4. Coverage table

| Bundle item | Decision | Patch(es) | Closed? |
|---|---|---|---|
| P1 (both README statements) | APPLY_WITH_README_ROUTE_CORRECTION | 1 (carrier split), 2 (frame-gate) | **Yes** |
| P2 (Slot 4c) | DEFER_NO_SLOT_CLOSURE | none | **Absent** (asserted; prohibition added in 9) |
| P3 (TWOPRES) | APPLY_SCOPED_TO_UNPAIRED_STREAM_INTERFACE | 4 | **Yes** |
| P4 (status currency) | APPLY_AS_REQUIRED_STATUS_CURRENCY | 1, 2, 6, 7, 8, 9 | **Yes** |
| P5 (bounded Minimo) | APPLY_BOUNDED_MINIMO_PARAGRAPH | 5 | **Yes** |
| P6 (Hamilton-Zero) | APPLY_PRIMARY_SOURCE_VERIFIED_HAMILTON_ZERO | 3 | **Yes** |

| Target file | Patches | Status |
|---|---|---|
| `README.md` | 1, 2 | successor status + research route both current; both carriers represented |
| `essay/climbing-the-wall-of-experience.md` | 3, 4, 5, 6 | Hamilton-Zero, TWOPRES, Minimo added; Continuation-route row current |
| `essay/README.md` | 7 | describes current bounded-result draft's successor boundary |
| `essay/REVIEW_HANDOFF.md` | 8, 9 | status currency + minimum new prohibitions; existing text verbatim |

P2 is confirmed absent from every target: no Slot 4c diagnostic, no
`positive-VICReg alignment probe` phrase, no `0.770/0.753`/`sign_d`/`1.0`
displacement number, no non-identification status sentence appears in any patch.

---

## 5. Negative-drift checklist

| Preservation rule | Status |
|---|---|
| Three endings (Proof/Falsification/Boundary) not restructured or collapsed | **Held** — no patch touches §VII |
| Walk-world void row preserved | **Held** — untouched (only Continuation-route row changed) |
| Both Wall-B rows preserved | **Held** — rows at essay lines 921–922 untouched |
| H4 preserved | **Held** — untouched |
| 24/12/0 preserved | **Held** — untouched |
| `REPRODUCED, PLATFORM ONLY` preserved | **Held** — untouched |
| "What this does not show" extended, not replaced | **Held** — patches 4 and 5 INSERT_AFTER; existing paragraphs unchanged |
| No `BUDGET_MASKED` added | **Held** — absent from all NEW_TEXT |
| No `11 -> 13` arithmetic added | **Held** — absent |
| No wall-second cost claim added | **Held** — absent |
| No 16D run-invariance claim added | **Held** — absent |
| No Part-B outcome added | **Held** — absent |
| No length-stratum causal story added | **Held** — absent |
| `1.0` used only for `sign_d` | **Held** — no displacement figure appears at all |
| No "repeated feasibility deaths" narrative | **Held** — stops named with distinct causes |
| Minimo not "external transfer"; "fixed human-written theorem panel" used | **Held** — patch 5 |
| Hamilton-Zero not a test of self-selected contact / path independence / causal contrast | **Held** — patch 3 states the explicit non-isolation limit |
| `essay/OUTLINE.md`, canonical, historical, code/JSON/logs untouched | **Held** — not targeted |

---

## 6. Part-B confirmation

No incomplete PHASE1_18 Part-B result directory or log was read or used. Part-B
amendment files were not consulted for this assembly; the current Part-B runtime
state supplies no fact in any patch. No experiment was run or resumed, and the
dirty worktree was not touched.

---

## 7. Terminal

Every edit is final prose; every anchor exists exactly once in its pinned target
and was quoted byte-exact; every external fact used in prose was independently
verified from a primary source (the unverified exact parameter count was
downgraded to the verified "~0.5B"). No author choice is reopened.

```text
READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V2
```
