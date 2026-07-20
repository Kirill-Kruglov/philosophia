# Fable 5 — Officina WP-3 contract v2.1 closure memo

Author: Claude Code Opus 4.8, executing the Fable-authored bounded mandate. Companion to
`successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md`
(complete self-contained replacement; v2 and both v2 confirmations
preserved unedited). Inputs: Opus (`REVISE_OFFICINA_WP3_V2`, V2-1..V2-4)
and Sol (`REVISE_OFFICINA_WP3_V2`, two Major repairs). Nothing
committed; no existing file changed. v2.1 is a single file so the future
`contract_sha256` binds one exact committed artifact, not a base +
addendum composition.

## Verdict

**READY_FOR_OFFICINA_WP3_V2_1_FINAL_CONFIRMATION**

## 1. Five-row delta table (the entire change from v2)

| # | Locus | v2 | v2.1 | Source |
|---|---|---|---|---|
| 1 | §4 oracle wire | two-refusal grammar (`LENGTH` **or** `BYTE`), no joint-case precedence, JSON-structure failures unclassified | **total ordered classifier** over raw bytes: `STRUCTURE` → `BYTE` → `LENGTH` → answer; joint byte/length = `BYTE`; structure decided before content; `ε` valid; raw-decoding vs mathematical-oracle separation stated; PAD/SEP route to `BYTE` | Opus V2-1 |
| 2 | §3 path + hash; §5 wording | stale v1 path `successor/officina/WP3_..._V1_DRAFT.md`; `contract_sha256` = "signed contract bytes" (artifact unspecified); §5 "not primarily scale transfer" | v1 path corrected to `successor/OFFICINA_..._V1_DRAFT.md` (front matter); `contract_sha256` = SHA-256 of the exact committed **v2.1** file, acyclicity stated (contract holds no frame hash); §5 softened — near band abuts one frame edge, qualification tests modulus identity **and** scale, no "avoids scale transfer" claim | Opus V2-2, V2-3, V2-4 |
| 3 | §8 randomization | OR realizations described per-option, no domain-separation obligation | **Common C-randomization protocol** inserted before the OR options: same post-lock root, **distinct typed PRF domains**, sample SRSWOR independent of orientation, OR-2 `Pr(S_h=s\|r)=1/binom(N_h,n_h)`, orientation-first-then-sample order, one non-redrawable `C_design_realization_id`; WP-3 owns independence/order/non-redraw, WP-10 owns byte tags | Sol Major 1 |
| 4 | §8 OR-2 | "one orientation per block observes exactly the estimand"; census-FPC-exact stated without conditional estimator/variance | corrected: derived/sealed after lock + C-root, **before** sample membership; conditional estimator `θ̂(r)` and conditional variance `Var[θ̂(r)\|r]=Σ_h W_h²(1−f_h)S²_{D(r),h}/n_h` displayed; "each sampled block reveals its orientation-specific contribution, **not** the full-frame estimand"; `C_design_realization_id` binds `r` without replacing `selection_scope_id` | Sol Major 1 |
| 5 | §7 information boundary | Q contributes "only promoted identity + validity-qualified selection history"; "pass direction" | replaced: `H_preC` retains and hashes the **complete** attempt/validity/released-output/stopping/depletion/promotion history; only the **mechanical first-valid-`Q_PASS` fact + promoted candidate/stack identity** route downstream; the **competence binary** (not "pass direction") is routing-only; complete history conditioned-on and auditable, not erased | Sol Major 2 |

## 2. No other contract cell changed

Every other cell is v2 verbatim: §1 unit/orientation/typed `(X,Δ)`; §2
generic frame formulas, §2a enumeration + regression vectors, §2b
branch-complete design table; §3 frame schema (only the
`contract_sha256` definition sentence added, no field changed); §5
bands `[10,25]∪[166,205]` (only the extrapolation-property wording
softened, the set unchanged); §6 C measure and claim boundary; §7
depletion inequalities and transport premise (only the information
boundary paragraph replaced); §8 OR-1 (bound to the common protocol,
estimator/variance unchanged) and the OR recommendation; §9 multiplicity
and ownership (the ownership table gains the PRF-domain-byte-tags row
under WP-9/WP-10 and the common-protocol entry under this contract — no
existing owner moved); §10 the four author cells and five-token packet;
§11 WP-4 scope; §12 provenance. Frame membership, CH-1, CH-2, both OR
options, transport, T-dev band set, typed outcome, small-stratum rule,
depletion arithmetic, claim boundary, and multiplicity are **not
reopened**.

## 3. Disposition of every v2-confirmation finding

| Finding | Disposition |
|---|---|
| Opus V2-1 (Major) — non-total/unordered oracle refusal | **Adopted**: delta 1, exact precedence per the prompt |
| Opus V2-2 (Minor) — stale v1 path | **Adopted**: delta 2, corrected to the real artifact |
| Opus V2-3 (Minor) — `contract_sha256` artifact unpinned | **Adopted**: delta 2, pins the exact v2.1 committed bytes, acyclicity stated |
| Opus V2-4 (optional) — "not primarily scale transfer" generous | **Adopted**: delta 2, wording softened rather than left generous |
| Sol Major 1 — OR-2 conditional SRSWOR + domain independence incomplete | **Adopted verbatim in substance**: deltas 3 and 4 |
| Sol Major 2 — `H_preC` narrowing + "pass direction" misnomer | **Adopted verbatim in substance**: delta 5 |

All confirmed-closed v1 repairs (frame arithmetic, typed observation,
small-stratum rule, transport premise, depletion, claim boundary,
multiplicity, recommendation provenance, capability invariant, T-dev
invariant) carry forward unchanged.

## 4. Token packet (unchanged, still unsigned)

```text
I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT
I_SELECT_OFFICINA_FRAME_BAND_LOW | I_SELECT_OFFICINA_FRAME_BAND_HIGH
I_SELECT_OFFICINA_SPLIT_C_RICH  | I_SELECT_OFFICINA_SPLIT_Q_RICH
I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND |
  I_SELECT_OFFICINA_ORIENTATION_CONDITIONAL_FIXED_VECTOR_ESTIMAND
I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE
```

Exactly one token per choice row; recommendations LOW, C_RICH,
CONDITIONAL, accept — all on pre-data scientific/resource/governance
grounds only. No token is signable from this draft; the next step is one
literal bounded confirmation, then Kirill's selection/signature.

## 5. Bounded yes/no questions (restricted to the five corrections)

**Opus:**
1. Is the §4 classifier now **total and ordered** over all raw inputs
   (`STRUCTURE` → `BYTE` → `LENGTH` → answer, joint case = `BYTE`,
   structure before content, `ε` valid), so two implementations produce
   byte-identical oracle transcripts?
2. Are the §1 v1 path and the §3 `contract_sha256` definition (exact
   committed v2.1 bytes, acyclic) now correct and unambiguous?

**Sol:**
1. Does the §8 common C-randomization protocol plus the corrected OR-2
   estimator/variance establish conditional SRSWOR
   (`Pr(S_h=s|r)=1/binom(N_h,n_h)`), domain independence, and the
   orientation-first order, with no sentence claiming a sampled block
   observes the full-frame estimand?
2. Does the §7 replacement keep the **complete** Q history in `H_preC`
   while routing only the mechanical first-valid-pass fact and promoted
   identity, with the competence binary named correctly and
   routing-only?

## 6. Bootstrap integrity

`python scripts/verify_officina_wp12.py` →
`OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.` (run
read-only for this closure). The exact `successor/officina/` bootstrap
set (`LINEAGE.json`, `PATH_POLICY.json`, `README.md`, `T_ENVELOPE.json`,
`T_LEDGER.md`, `T_LEDGER.md.head.json`, `WP1_WP2_IMPLEMENTATION.md`) is
unchanged; this task added no file under `successor/officina/` and
edited nothing anywhere. The corrected v1 governing path
(`successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md`) was
confirmed present.

## 7. Negative space

No author token, WP-4, entropy, world, frame instance, sample, panel,
candidate, manifest, datum, ledger event, root, lock, escrow, T
activation, Q/C process, learner run, outcome, Proof, or claim movement
was created or authorized. T remains `NOT_ACTIVATED` at the genesis
head. The predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; its records are non-citable and chose no
value here. Officina's T and Q can never earn, kill, or boundary-label
C1–C6; a future Q pass is a spendability gate fact only; S is
unavailable; only a valid, independently locked C execution may move an
Officina claim — within its selection-conditional, selected-frame,
orientation, device, and learner-seed scope. No qualification,
scientific direction, or programme success is predicted.
`PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the programme
claim stays `OPEN`. The next review is a literal bounded confirmation of
v2.1, not another design round.
