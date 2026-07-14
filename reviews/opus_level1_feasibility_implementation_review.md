# Opus 4.8 X-line — Level 1 feasibility implementation review

Reviewer: Opus 4.8 (X-line, implementation only). Repository:
`/home/master/llm_projects/philosophia` (not committed; **feasibility driver not
invoked**; no authorization, entropy, real panel, or trajectory produced).
Reviewed code commit: `308aa6fcfd165b1742a1ec4988a660d9a6c21333`. I ran the unit
and full suites, `verify_all.py`, static inspection, and in-memory checks.

**Source-byte pin verified:** all twelve reviewed source paths are byte-identical
between `308aa6f` and HEAD (`git diff --quiet 308aa6f HEAD -- <paths>` clean); the
current HEAD differs only in review-only files.

---

## Verdict

**`REVISE_LEVEL1_FEASIBILITY_IMPLEMENTATION`**

The implementation is faithful to §5/A3/A5/A8/A10 and safely gated — hard caps, one
RANDOM-STATIC arm, one replicate, discarded scorer choices, dummy-panel separation,
source-byte pin (including `config.py`), durable pre-run claim, preflight no-retry,
and no forbidden derivation. But one Major test gap remains: the **trajectory
training step and the end-to-end feasibility loop are never exercised**, so a
shape-correct-but-trajectory-wrong refactor (e.g. per-member minibatch, mis-counted
steps, broken checkpoint cadence, or a dropped non-finite break) would pass. A few
Minor items round it out. Add the bounded tests below and it is confirmable.

**Results:** feasibility tests → 6 passed; full suite → 139 passed; verifier VALID;
no `feasibility/` artifacts and no authorization file present.

---

## Findings

### Critical
None.

### Major

- **FS-1 — the trajectory step and the end-to-end loop are untested (Q7).** The
  persistence logic (`checkpoint_qualifies`, `first_persistent_step` in
  `scoring.py`) and the scorer (`select_by_disagreement` no-mutation, `shortlist`,
  `replay_batch_indices` in `acquisition.py`) **are** component-tested. But
  `feasibility_committee_step` (`train.py:37`) and `run_noncomparative_feasibility`
  (`feasibility.py:165`) are never called by any test. Consequently these
  load-bearing behaviors are unverified: that one oracle step spends exactly one
  `trajectory_step` (not four — Q2), that all four members train on the **one**
  shared minibatch, the `forward→backward→step→zero_grad` order, the non-finite
  `break`, the checkpoint cadence at step 0 and each `% 50`, the five-window
  persistence, and the scorer `state_before == state_after` assertion. The code is
  correct on inspection, but nothing pins it. **Mandatory:** add a
  `feasibility_committee_step` unit test (four tiny committee members, one
  minibatch, `bounded_feasibility_check`; assert `capability.trajectory_steps == 1`,
  all four members updated on the shared batch, non-finite handled), and a bounded
  end-to-end wiring test (a short injected schedule / step cap) asserting
  one-step-per-oracle, checkpoint evaluation at step 0 and the cadence, the
  non-finite break setting `all_losses_finite=False` / `censored_at_b=True`, and the
  scorer no-mutation guard firing.

### Minor

- **FS-2 (Q4) — scorer timing excludes per-step candidate realization.** The timed
  region (`feasibility.py:265–267`) wraps only `select_by_disagreement`; the
  `S=512` per-step `realize_pool_index`+`encode_pair` (`:261–263`) is outside it.
  The `E×S` forward passes dominate, so `projected_active_scorer_seconds` is only
  mildly optimistic, but for an honest A8 bound either include realization in the
  timed region or state the projection is scoring-forwards-only.

- **FS-3 (Q3) — the RANDOM-STATIC projection excludes checkpoint-eval cost.**
  `projected_random_static_seconds = mean_step_latency × B` (`:287`) omits the ~41
  checkpoint panel evaluations (`_panel_qualifies`, 188 items × 4 members). Minor
  optimism; note it or fold a checkpoint-cost term into the projection.

- **FS-4 (Q6) — `public_root.py` is not in `REVIEWED_SOURCE_PATHS`.** The driver
  imports `atomic_create`, `canonical_json`, and `sha256_file` from it (output
  plumbing: the durable claim/report and recorded hashes), yet it is absent from
  the twelve pinned paths (`level1_run_feasibility.py:37–50`). Impact is low — the
  measurements come from the pinned `feasibility.py`, and no-retry is independently
  enforced by the preflight `claim/report .exists()` check (`:148–151`) — but a
  drift in `atomic_create`/`canonical_json` could change the artifact's durability
  or byte format. Add `src/philosophia/level1/public_root.py` to the pinned set for
  completeness (the m3 lesson).

- **FS-5 (Q1) — `realize_cell` has no explicit exhaustion guard.** The
  `while len(accepted) < 4` loop (`pool.py:63–81`) rejects duplicates and, for
  `d=0`, `u==v`, but never raises on exhaustion. It always terminates for
  acquisition cells (ample words; 68,848-realization headroom), but a defensive
  cap-and-raise would match the panel builder's B-1 discipline.

- **FS-6 (Q7) — the report's contamination guards are declarative.** The
  `contamination_guards` block (`level1_run_feasibility.py:240–251`) is a hardcoded
  set of `False` booleans, not derived from the run. The actual prevention is
  structural (one-arm loop, discarded choices, no contrast) plus the driver import
  check (no `sample_outcome_pairs`/`estimate_contrast`/`choose_n3`) and the
  aggregate-only report surface — all tested — so this is documentation, not a
  hole; consider a comment saying so.

---

## Answers to the seven checks

1. **A3 pool realization.** `realize_cell` (`pool.py:59`) materializes four distinct
   slots on the `("L1","pool","realize",a,b)` stream with full `{0..5}` padding
   (correct — the positive-`v` rule is panel-only), rejecting duplicates and `d=0`
   `u==v`; `realize_pool_index` maps `divmod(index,4)` to `(cell, slot)`;
   `random_static_schedule` draws a full `B=2000` without-replacement schedule on
   `("L1","feas")`. Pinned by `test_raw_pool_realization...` and the schedule test.
   ✓ (FS-5 guard aside).
2. **Update order / shared minibatch / oracle-step counting.** One minibatch
   (newest + ≤31 history, `replay_batch_indices`) is built per oracle step and
   passed to all four members; `feasibility_committee_step` computes four losses on
   that shared batch, then `backward`/`step`/`zero_grad`, spending **one**
   `trajectory_step` — so the capability counts **oracle steps, not member
   updates**. Correct on inspection; **untested (FS-1)**.
3. **Persistence / non-finite / censoring / checkpoint size.** Five-checkpoint
   window including step 0 (`recent_qualifying`, `feasibility.py:186,219–222`);
   non-finite loss breaks the loop and flips `all_losses_finite`; `censored_at_b`
   is the single binary result; `_checkpoint_size` measures a `torch.save`→`BytesIO`
   payload **in memory, not persisted**. `first_persistent_step`/`checkpoint_qualifies`
   are component-tested; the loop wiring is **untested (FS-1)**; FS-3 noted.
4. **Scorer microbenchmark.** Exact `S=512` (asserted, `:258`), `E=4`; `no_grad`
   + eval-mode + double state-hash guard (in `select_by_disagreement` and across the
   scorer loop, raising on mutation); the chosen `pool_index` is **discarded** (only
   `disagreement` finiteness is read) — a pure timing path. Honest A8 modulo FS-2.
5. **Dummy-panel separation.** `DummyPanelBuilder` now requires only
   `public_key.purpose=="public-root"` (accepts the real public root for genuine
   reservation geometry) but **mandates a `test_only` panel key** — so it can build
   only dummy panels and can never touch the real escrow-secret seed or the real
   panel. `_dummy_panel` uses the real public root + `dummy_key("...",purpose="panel")`;
   `panel_computable` is measured on dummy realizations. The real-panel escrow
   boundary is intact (the panel-key guard + `forbidden_derivations` preflight).
   Pinned by `test_dummy_panel_accepts_real_public_root_but_requires_test_panel_key`.
   ✓.
6. **Wall / caps / path / auth / pin / claim / no-retry.** 12 h shared wall
   (`43200 s`) and caps (`B=2000` trajectory, `200` scorer, one world) enforced by
   `FeasibilityCapability` and re-checked against the authorization; canonical output
   dir frozen (`:80–82`); authorization and public-root transcript must be
   git-**tracked** (`ls-files --error-unmatch`) and schema/token/caps/world/output/
   `reviewed_code_head`-validated; reviewed source byte-pin over the twelve paths
   (incl. `config.py`); durable pre-run claim before the run; preflight refuses a
   pre-existing claim/report and any later-gate artifact (`PREREG.lock`,
   `REAL_PANEL.enc`, `decision.json`). ✓ (FS-4 aside).
7. **Do the tests catch a wrong/contamination-prone impl?** Partly: pool, schedule,
   caps, dummy-panel separation, report surface, driver gating, scoring, and
   acquisition are pinned; the **trajectory training step and end-to-end wiring are
   not (FS-1)**, and the contamination guards are declarative (FS-6, mitigated by
   the structural/import/surface tests).

---

## Mandatory edits

1. **FS-1 (Major):** add the `feasibility_committee_step` unit test and a bounded
   end-to-end wiring test described above.
2. **FS-2 / FS-3 (Minor):** include realization/checkpoint costs in the projections
   or document them as forwards-only bounds.
3. **FS-4 (Minor):** add `src/philosophia/level1/public_root.py` to
   `REVIEWED_SOURCE_PATHS`.
4. **FS-5 (Minor):** add an exhaustion cap-and-raise to `realize_cell`.

No signed scientific constant, allocation output, or gate needs to change.

---

## Exact execution guards a future authorization must bind

The authorization JSON (`FEASIBILITY_EXECUTION_AUTHORIZATION.json`, git-tracked)
must carry: `schema = philosophia.level1.feasibility-authorization.v1`;
`token = I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY`; `scientific_outcome: false`;
`execution_once: true`; `arm: "RANDOM-STATIC"`;
`caps = {development_worlds:1, trajectory_steps:2000, scorer_steps:200, wall_seconds:43200}`;
`development_world = {pair_slot:0, modulus:66}`;
`output_directory = experiments/level_1_contact/feasibility`; and a 40-hex
`reviewed_code_head`. Execution additionally requires: `EXPECTED_HEAD == HEAD`,
clean tracked tree, empty index; the public-root transcript tracked, canonical,
non-outcome, with unchanged `forbidden_derivations`; reviewed source byte-identity
over the pinned paths (add `public_root.py`); no pre-existing claim/report; no
later-gate artifact; the durable pre-run claim; a single invocation; and the report
declaring `scientific_outcome:false` with all contamination guards false.

## May Codex prepare an authorization candidate, but not execute it?

**Yes — prepare, not execute, and not self-authorize.** Codex may draft the
authorization-candidate JSON with the frozen structural fields (schema, caps, arm,
world, output dir, `scientific_outcome:false`, `execution_once:true`, and the
resolved `reviewed_code_head`/`EXPECTED_HEAD`). But the `I_AUTHORIZE_...` **token
and the commit of that file are Kirill's explicit act** — Codex must not assert the
token on his behalf. Codex must **not** invoke `scripts/level1_run_feasibility.py`,
create the claim/report, draw entropy, build a real panel, or touch any later gate.
Preparation is a reviewable candidate; execution is a separate, human-authorized
one-shot.

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its sole S4
tooth; the public-root / escrow-secret-panel separation and R_h-deferred; the
public-reservation / secret-realization boundary (feasibility uses a dummy panel
only); `PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation; feasibility is
`scientific_outcome:false` and single-arm — never a contrast, N3, lock, escrow, or
decision; `UNKNOWN`/censored never success; donor transcripts encode `n_donor`,
never `n_target`; Level 1 never evidence for `PROOF_CORE`.

**No feasibility execution, authorization, entropy, real panel, N3, lock, escrow,
trajectory, or outcome is authorized by this review.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
