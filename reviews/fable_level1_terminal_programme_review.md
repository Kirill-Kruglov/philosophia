# Fable 5 — Level 1 terminal programme review

Author: Fable 5. Scope: programme review and discussion after canonical
admission of the Level 1 feasibility-v2 terminal (admission commit
`822ef1d`; two later commits exist — the review prompt `c25bd65` and the
evidence atlas `3ca5f3e` — and are noted where relevant). This document
authorizes nothing: no repair, rerun, retry, scout, N3, lock, panel,
escrow, outcome, or programme continuation. It changes no existing file.
Read-only recomputation was performed; all values below were verified
against committed bytes.

## Primary verdict

**READY_FOR_AUTHOR_ROUTE_DECISION**

The canonical synthesis is correct, complete, and honest. Independently
recomputed: the v2 claim/report/authorization hashes
(`366029b7…121222`, `9d9942c8…ee34f6`, `54b70ead…20dc02`) match
`RESULTS_CANONICAL.md` and the gate decision; the v1 evidence is
byte-unchanged; the resource aggregates recompute exactly
(64.47593 s × 2,000 = 128,951.863 s = 35.820 h; 52,200,036 KiB =
49.782 GiB); no scout, N3, lock, panel, escrow, or outcome artifact
exists. `BLOCKED_LEVEL1_FEASIBILITY` is the single valid route (§1.1).
The essay, ledger, kill matrix, and roadmap preserve every required
negative statement. Nothing blocks Kirill's route decision except the
decision itself.

---

# 1. Ordered findings

## Critical

None. No integrity error, no forbidden inference, no overclaim that
converts the blocked route into an outcome.

## Major

None requiring revision of the canonical synthesis.

## Minor (wording suggestions only; none blocks the verdict)

- **MN-1 — atlas hero wording collides with the essay's own "wall"
  vocabulary.** The evidence atlas (`docs/index.html`, commit `3ca5f3e`,
  outside the admission snapshot) opens with "The Workshop reached a
  wall before the experiment." The essay carefully reserves *wall* for
  the world-versus-route ambiguity (§III) and *false wall* for shared
  blindness; the feasibility stop is neither — it is the apparatus's own
  gate refusing to spend the experiment. Suggested hero: "The Workshop
  stopped at its own gate before the experiment." This is a metaphor
  hygiene note, not a factual error: the atlas's gate section itself is
  accurate.
- **MN-2 — ROADMAP status note "Level 1 завершился валидным
  `BLOCKED_LEVEL1_FEASIBILITY`".** "Завершился" (concluded with) is
  defensible — the *gate* did terminate — but "остановился валидным…"
  (stopped with) would better match the essay's "stopped, open" framing.
  Optional.
- **MN-3 — essay §VI.1 Arm B sentence.** "The alternate-fidelity arm
  also generalized in three of three seeds" is immediately bounded by
  `NO_PRIMARY_INFERENCE`, which is correct; consider ordering the caveat
  first ("recorded diagnostic-only, it also…") so a skimming reader
  cannot quote the 3/3 alone. Optional.

## 1.1 Is `BLOCKED_LEVEL1_FEASIBILITY` still the only valid route?

Yes — re-derived independently from the immutable report bytes, not
from the reviews. The report records `validity:
valid-scientific-terminal`, `steps_completed: 2000/2000`,
`all_losses_finite: true`, `all_parameters_finite: true`,
`panel_computable: true`, `censored_at_b: true`, all twelve
contamination guards `false`. Against the signed validity-first table
(amendment §7 as corrected by v2.1/v2.2): route 1 is excluded by the
censor bit; route 3 by both finiteness flags; route 4 because the run
is a valid terminal at `B` (35.820 h against the 129,600 s cap — the
wall never raised, with ≈ 11 minutes of headroom); route 5 because
every hash verifies. Route 2 is forced. Both X and Y lines confirmed
this mechanically; no author discretion was exercised anywhere in the
terminal, which is itself the strongest evidence the preregistration
discipline held.

## 1.2 Does the essay keep the process/evidence distinction?

Yes. The load-bearing sentences are all present and correct: the
plain-words preface ("That is a feasibility boundary, not an answer
about contact"), §VI.2 ("This does not show that the learner lacked the
modulus… There is no third learner-policy intervention under the signed
route"), §VII ("a valid feasibility censor is not a fourth ending and
cannot be narrated as one"), the unreached-boundary paragraph (the
registered `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` described in the
subjunctive and marked "not observed"), and the "What this does not
show" ledger entry. The status ledger's distinct states
(`BLOCKED_LEVEL1_FEASIBILITY, PROCESS ONLY` vs `UNRUN / UNTESTED` vs
`BLOCKED UPSTREAM / UNRUN`) are exactly the right taxonomy. I attacked
each interpretive sentence for a silent conversion of censoring into
capacity, arm ordering, or boundary language and found none.

## 1.3 Is the current result publishable?

**Yes, as it stands.** The honest central contribution is *not* a
finding about experience. It is threefold:

1. **The inherited instrument with measured limits** (Line 12): shared
   wrong answers can expose shared derivation; the combined blade
   falsified on holdout; independence practiced, not inherited. Already
   public; Philosophia adds the framing that this is the quality-control
   department of any manufactured-experience claim.
2. **A replication anchor under full preregistration** (Level 0):
   grokking reproduced 5/5 with a locked decision procedure and a
   negative control — modest but real, and the platform for everything.
3. **A demonstrated fail-closed research architecture** (Level 1): a
   multi-agent workshop that signed its outcomes' meanings before data,
   was stopped by its own gate, and *did not negotiate with itself* —
   two censors, one signed amendment, zero post-outcome discretion, and
   a terminal that every reviewer could re-derive mechanically. The
   discipline was exercised under temptation, not merely described.

What would make it more than a process diary: (a) publishing the
apparatus as a reusable instrument (the validity-first taxonomy, the
escrow-before-outcome pattern, the one-shot no-retry driver discipline)
with the Level 1 stop as its worked example; (b) the honest engineering
finding (§2, resource profile) that CPU-scale online learners are the
binding constraint for active-learning-versus-yoked designs at this
rigor; (c) the negative-space sections, which are the genre's rarest
element. Do not manufacture a more dramatic ending; the record's value
is that it refuses one.

---

# 2. Four-way knowledge inventory

**Scientific findings (earned, bounded):**

- Correlated wrong-value failures can expose shared derivation; the
  token channel survived an escrowed holdout (H1/H2/H5). (Line 12,
  inherited.)
- Co-success is the world's credit; it cannot certify ancestry. (Line
  12, Amendment 1.)
- Independence is practiced, not inherited: 24/12/0 gradient; the
  0/1200 visibility limit where validation discipline erases the trace
  of true derivation. (Line 12.)
- The combined token+journal blade is **falsified** as world-portable
  (H4 journal false positive; confirmation withheld as preregistered).
  (Line 12.)
- The locked instrument did not reproduce the informal 24/24
  common-prior flag (`C_C8` read CLEAN); published as it fell. (Line 12.)
- Canonical modular-addition grokking reproduces on this locked CPU
  platform, 5/5 seeds, delays 5,000–7,500; random-label control
  memorizes without generalizing. **Platform only.** (Level 0.)
- From Level 1: **no scientific finding.** The valid censor is a
  process boundary by signed definition.

**Engineering findings (resource-only, non-citable as science):**

- Full-history CPU float32 training with batch growing to 2,000 × 277
  tokens across a 4-member committee costs mean 64.48 s/step (max
  135.47 s, super-linear tail) and 49.78 GiB peak RSS — ≈ 37× the
  minibatch-32 step cost, against a 31.5× linear projection. The AM-4
  relabeling ("planning projection, not a bound") was vindicated by 11
  minutes of wall headroom; a 30 h cap would have invalidated the run.
- The one-shot discipline works end-to-end at the byte level: canonical
  JSON, per-domain PRF separation, source pins stable from review
  through execution (Opus verified empty diffs), 158 tests, two
  independent verifiers returning `VALID`, atomic claim-before-run.
- A dummy-panel endpoint remained computable at every cadence point
  under the amended learner — the evaluation machinery itself never
  faulted.

**Programme-governance findings:**

- Pre-signed terminal routes convert disappointment into mechanical
  classification: no post-outcome author choice was needed or made at
  any Level 1 gate. This is the strongest demonstrated result of the
  whole line.
- The "no third intervention" rule is enforceable in practice: the
  programme preferred stopping to tuning, under real temptation
  (twice-censored, with an obvious next knob available).
- Adversarial two-line review repeatedly caught load-bearing pre-data
  defects (parity leaks, unsatisfiable verifiers, a hash transcription
  error, the censor/invalidity conflation). The crack-migration law
  ("reviews converge or the instrument fails") held.
- Cost honestly named: the one-shot-gate architecture front-loads
  learner competence into a fail-closed bottleneck. The budget was
  spent proving the gate works, not the science. Any successor must
  demonstrate competence *before* locking, not after.

**Completely untested:**

- C1 (chosen contact), C2 (forward shortening), C3 (representation
  transfer), C4 (ledger causality), C5 (path credit), C6 (balcony
  diagnostics) — every one, in both directions.
- Every arm ordering; every contact-mode question; whether *any*
  learner class on this platform can certify an operational modulus
  within any budget (two policy points were probed, both censored, and
  they may not be contrasted even with each other).
- The programme claim itself — manufactured experience — in either
  direction. `OPEN` is exact.

---

# 3. Route comparison and recommendation

| | Route A — freeze & publish | Route B — publish + new signed line | Route C — signed redesign of Philosophia |
|---|---|---|---|
| Claim | "A fail-closed workshop refused its own one-shot experiment; here is the record and the instrument." | A's claim, plus a successor line testing a redesigned learner-competence architecture | The original programme claim, with the one-shot competence gate replaced |
| Current evidence supports | fully (everything is committed) | fully for the publication half; the new line starts with zero scientific evidence | the *need* for redesign (process fact), never a preference among redesigns |
| Remains forbidden | any contact/capacity claim; v1/v2 contrast; narrating the stop as an ending | citing v1/v2 censors as evidence for any specific new design choice | same, plus silent supersession of any signed rule |
| Signatures/reviews | none new scientifically; publication is Kirill's act | new line charter + claim graph + two-line review before its first lock | loud named supersession of the Level 1 execution route + total contact-mode rule; new tokens; full bounded review |
| Scope | weeks (essay/atlas polish; two missing figures) | A + months for the new line's development phase before any lock | months; heavier governance than B for the same experiments |
| Main Goodhart risk | narrating the stop as profundity ("the wall" mystique) | development-phase results leaking citability; dev→lock selection overfitting the world registry | strongest: continuation inside the same name invites reading the redesign as a third intervention |
| Stop condition | publication | new line's own preregistered kills; dev phase has a declared budget/deadline | same as B plus the supersession review itself |
| Can reach `PROOF_CORE`/`PROOF_STRONG` | never (stays `OPEN`) | yes, in the successor line (definitions inherited by fresh signature) | yes, if the redesign survives review |

**The "bypass Level 1" idea, explicitly.** Under the signed total
contact-mode rule it is forbidden: Level 2's contact mode requires
resolved Level 1 comparisons, and none exist. Could an author honestly
demote C1 and *fix* a contact mode by signed decision for a new
C2/C3/C4 programme? Structurally yes — C1 was always a modifier
(`PROOF_CORE` never contained it), so a core-only programme is
conceptually coherent, and the choice would be a named decision, never
evidence. But the semantic cost must be stated in full: (i)
`PROOF_STRONG` becomes permanently unreachable in that programme, so
the word *Proof* would forever carry the qualification the signatures
reserve; (ii) the thesis loses "chosen contact" — the experience tested
becomes *contact happened*, not *contact was chosen*, which retreats
from the essay's central active-contact chapter; (iii) the fixed mode
cannot be selected *by* the censors (that would be outcome-triggered),
only by design argument. And one thing the demotion does **not** buy:
the feasibility wall was learner competence, not the C1 gate. A Level 2
learner must still solve worlds; bypassing Level 1 relocates the same
floor without crossing it. For these reasons a C1 demotion is honest
only inside a redesign that *also* fixes the competence architecture —
at which point it is Route B/C with an extra semantic loss, and I would
not pay that loss up front.

**Recommendation (Kirill's decision, stated explicitly as such):**
**Route B.** Publish the stopped-open record now — it is ready, and its
value degrades if it waits on a successor — and open a genuinely new
signed line whose defining architectural change is *development before
lock*: an openly iterated, permanently non-citable engineering phase
that must demonstrate the competence floor (certified development
solves, any learner/world/budget it likes) **before** any confirmatory
contract is signed, with confirmatory worlds disjoint from every
development world and the selection rule for the confirmatory
configuration frozen before the demonstration is inspected. That is
what makes it a new estimand and not outcome-triggered tuning: the old
programme gated a locked design on a one-shot competence check; the new
line earns competence first and locks second. The censors motivate the
*architecture change* (a process lesson) while supplying no preference
among learners — exactly the boundary the signed record draws. Route A
is the honorable fallback if there is no appetite for a successor;
Route C buys the same experiments as B at higher governance cost and
higher perceived-continuation risk inside the same name. This
recommendation is based on claim clarity and information value; the
successor is as likely to be censored at its own floor as not, and the
publication must not promise otherwise.

---

# 4. Evidence visualization plan

Note: commit `3ca5f3e` already ships an atlas (`docs/`) with five
sections — hero, instrument gradient, platform event map, gate flow,
claim grid, sources. The plan below treats it as the de-facto first
release, names its two gaps, and ranks all seven mandated candidates.

| # | Figure | Rank | Status in atlas |
|---|---|---|---|
| 1 | Line 12 error-independence gradient | **must-have** | present — verify 0/1200 shown separately |
| 2 | Line 12 holdout matrix H1–H5 | **must-have** | **missing** |
| 3 | Level 0 grokking event map | **must-have** | present |
| 4 | Level 1 gate-flow diagram | **must-have** | present |
| 5 | Claim-state map | **must-have** | present |
| 6 | Resource profile | useful | missing — appendix only |
| 7 | Proof-layer DAG | **must-have** | **missing** |

1. **Error-independence gradient.** Question: does declared origin buy
   error independence? Source: `PREREG_v4_DRAFT.md` Appendix R /
   first-contact table; values 24/24, 12/24, 0/24. Grammar: three
   labeled dot-bar rows on a 0–24 count axis; the 0/1200 visibility
   limit as a **separate annotated strip** ("derivation invisible to
   the detector: 0 firings / 1,200 trials"), never averaged into the
   gradient. Caption: "Shared wrong answers with the reference path out
   of 24 diagnostic cases; independence followed practice, not
   pedigree." Accessibility: values printed as text at each row; no
   color-only encoding. Forbidden inference: not a ranking of model
   vendors; 0/24 is *no visible trace*, not certified independence.
   Placement: essay + evidence site.

2. **Holdout matrix.** Question: what did the escrowed holdout confirm
   and falsify? Source: `holdout_result.json` — per-arm `P_tok`, `P_j`,
   `P_union` with `tok_m`/`J_m`. Grammar: 5 rows (H1–H5) × 3 columns
   (token / journal / combined), categorical cells
   DEPENDENT/CLEAN/INADMISSIBLE rendered by shape+label; **H4 visually
   dominant**: token CLEAN at ≈ 0.0 beside journal DEPENDENT J = 0.857
   → combined DEPENDENT — the false positive that withheld
   confirmation. Caption must state: "the combined blade called a
   registered clean pair coupled; portability confirmation was withheld
   as preregistered." Accessibility: never color-only; the H4 cell gets
   a text badge. Forbidden inference: H4's combined DEPENDENT is an
   instrument failure record, not a detection; the matrix supports the
   token channel within the registered family only. Placement: essay
   evidence section + site; this is the single most load-bearing
   honesty figure and its absence from the atlas is the bigger of the
   two gaps.

3. **Level 0 grokking event map.** Question: did delayed generalization
   reproduce? Source: `OUTCOME_RESULT.md` table / `decision.json`
   runs. Grammar: one horizontal timeline row per seed A-0..A-4 on a
   step axis to 8,000; FIT-start marker at 200, GENERALIZE-start
   marker, shaded delay span; R-0 in a **separated control panel** with
   FIT marker and an explicit "no GENERALIZE within 40,000" label,
   never pooled; Arm B omitted or in a collapsed "diagnostic only,
   `NO_PRIMARY_INFERENCE`" strip. Caption: "Platform replication only;
   no programme inference." Forbidden: any mechanism/Fourier claim on
   the figure. Placement: essay + site.

4. **Gate-flow diagram.** Question: where and why did the route stop?
   Source: SCIENTIFIC_SPEC_SIGNATURES, public-root transcript, v1
   claim/report, amendment chain, v2 claim/report, gate decision.
   Grammar: vertical flow — signed contract → public root → v1 floor
   record (censored) → one signed amendment → valid v2 censor →
   `BLOCKED_LEVEL1_FEASIBILITY` → C1 untested → Level 2 blocked — with
   the two signed status lines verbatim as terminal labels, commit
   hashes as node subtitles. **v1 and v2 boxes must share no numeric
   axis and no comparative arrow**; print the rule on the figure: "the
   two records may not be compared." Distinct edge style for
   "blocked" (procedural) vs anything that could read as "failed."
   Placement: essay + site hero candidate (see below).

5. **Claim-state map.** Question: what may this repository currently
   claim? Source: `CLAIM_LEDGER.md` + `KILL_MATRIX.md` rows, one cell
   per claim. Grammar: grid with **seven visually distinct states** —
   earned / inherited / rejected / falsified-on-holdout / process-only
   / blocked-unrun / diagnostic-only — where blocked/unrun uses hollow
   outlines and negative states use filled marks, plus text labels
   (shape+text, never color alone). Forbidden: rendering blocked in the
   same visual family as negative. Placement: site (present); a
   condensed version may close the essay.

6. **Resource profile.** Question: what did the valid v2 execution
   cost? Source: v2 report `measurements.trajectory.latency`
   aggregates, `peak_rss_kib`, `checkpoint_artifact_bytes`, wall cap.
   Grammar: a small table or labeled bar set of the five aggregates
   plus "35.820 h of a 36 h cap"; **no time series exists and none may
   be drawn** — a synthetic learning/latency curve would fabricate
   evidence. If v1's step cost appears at all, only in the technical
   appendix, labeled "engineering cost of the amended regime; not an
   efficacy contrast." Rank: useful, technical appendix only.

7. **Proof-layer DAG.** Question: what would proof even mean here?
   Source: `CLAIM_LEDGER.md` signed semantics. Grammar: nodes C1–C6;
   `PROOF_CORE = C2∧C3∧C4` boxed; `PROOF_STRONG = CORE∧C1∧C5` as an
   enclosing box; C6 attached by a dashed annotation edge labeled
   "reported, never decisive"; every node currently rendered in the
   *blocked/unrun* style (hollow), with C1 sub-labeled "untested —
   feasibility-blocked" — and a legend stating no node is negative.
   Forbidden: any state that reads as failed/false. Placement: essay
   §VII + site; second of the two atlas gaps.

**Central visual question.** Both — but with one hero. The public story
should open with a single overview (the gate-flow, which is the only
figure that answers "what happened" without risking an outcome
reading), followed by the evidence sequence (gradient → holdout matrix
→ Level 0 map → claim states → proof DAG). A "Workshop wall" hero alone
would over-weight the stop; a bare figure sequence would bury it.
**Minimal first release:** the existing atlas + figure 2 (holdout
matrix) + figure 7 (proof DAG) + the MN-1 hero wording fix — everything
buildable from committed bytes with no invented data.

---

# 5. Exact essay/README corrections

**None required.** The canonical files, README, ROADMAP, and essay pass
the audit as admitted. MN-1..MN-3 are optional wording improvements,
listed with exact locations in §1; none makes the blocked route sound
like an outcome, so none is a condition of this verdict.

---

# 6. Questions for Kirill (five)

1. **Route:** A, B, or C — and if B/C, do you accept *development
   before lock* as the successor's defining architecture (competence
   demonstrated in a non-citable sandbox before any confirmatory
   contract is signed)?
2. **C1's standing:** does chosen contact remain a first-class question
   in any successor, or do you accept its honest demotion (fixed
   contact mode by named decision, `PROOF_STRONG` permanently
   unreachable there) to prioritize C2/C3/C4?
3. **Publication unit:** is essay + atlas + repository the publication
   now, and do you want the two missing figures (holdout matrix, proof
   DAG) built before release?
4. **Platform identity:** the valid v2 record prices one development
   trajectory at ~36 h on CPU float32. Is CPU-only part of the
   programme's identity for any successor, or is a signed device change
   on the table at a successor's own gate?
5. **Metaphor budget:** keep "wall" for the feasibility stop in public
   copy, or reserve it — as the essay defines it — for the world/route
   ambiguity, renaming the stop a *gate*?

---

# 7. Negative space (preserved, unweakened)

`BLOCKED_LEVEL1_FEASIBILITY` is a process boundary, never a
falsification, boundary, or capacity claim; C1 is unrun and untested;
no ACTIVE/YOKED/RANDOM ordering exists;
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` was not observed; the v1 and v2
records may never form an efficacy contrast; censored/`UNKNOWN` never
success, equivalence, or a narrated boundary; a feasibility failure
never proves the learner lacked `n`; the resource aggregates support no
capacity or improvement claim; development artifacts are non-citable
forever; the Level 1 kill neither fired nor survived; Level 2 was not
run and is blocked upstream by `INSUFFICIENT` contact-mode selection,
which is not a Level 2 outcome; no route in §3 is authorized by this
review, and the terminal supplies no empirical preference among
redesigns; Line 12's instrument cannot certify independence and its
combined blade is falsified as world-portable; Level 0 licenses
platform replication only; the programme claim is `OPEN` — neither
Proof, nor Falsification, nor a scientific Boundary was earned; and no
continuation exists under the present signed route without a genuinely
new author-signed programme decision with bounded review.

# 8. Confirmation

This review changed no existing file — no evidence, canonical record,
essay, code, README, ROADMAP, or atlas file was edited — and
`essay/OUTLINE.md` was left untouched. It created exactly one new file
(this document) and committed nothing. No code, entropy, run, retry,
learner, scout, N3 selection, lock, panel, escrow, or outcome was
created. The only computations were read-only: SHA-256 recomputation of
the five feasibility artifacts (all match the canonical record) and
arithmetic on committed aggregates (35.820 h; 49.782 GiB). No series
was inspected or reconstructed (none exists); no arms were compared; no
v1/v2 contrast was formed.
