# Sol review — Level 1 gated implementation and Y-line fidelity

Verdict: `REVISE_LEVEL1_GATED_IMPLEMENTATION`

This review audits the gated Level 1 implementation against the signed v3
lineage through v3.1.4.1 and the two author-signature records. It covers
all files under `src/philosophia/level1/` and all `tests/test_level1_*.py`.
No code was changed, no commit was made, no entropy was drawn, and no
scientific gate was executed.

## Critical findings

None. The implemented substrate is fail-closed, dummy/test-seed bounded,
and largely faithful to the signed scientific contract. No current code
surface can accidentally reach the public-root draw, real panel
generation, feasibility/scout execution, N3 lock path, real escrow,
learner trajectory, or outcome.

## Major findings

1. **Outcome estimator accepts impossible sample sizes.** The signed
   outcome frame permits `N3 ∈ {12,15,18,21,24}`, hence `n_h ∈ {4,5,6,7,8}`.
   `estimate_contrast` currently accepts any equal stratum count in
   `2..8` at `src/philosophia/level1/inference.py:70`. That admits
   non-registered outcome intervals for `n_h=2` or `3`.

   Mandatory edit: change the guard to require equal `n_h ∈ {4,5,6,7,8}`
   for outcome contrasts, or split a clearly named development-only helper
   from the outcome estimator. Add tests that `n_h=2` and `n_h=3` are
   rejected by the outcome estimator.

2. **Tests do not numerically catch a missing non-census FPC.** The code
   implements the FPC in `src/philosophia/level1/inference.py:75` and
   `src/philosophia/level1/inference.py:77`, but the tests exercise a
   census point interval and zero-variance non-census label only
   (`tests/test_level1_acquisition_inference.py:55` and
   `tests/test_level1_acquisition_inference.py:66`). A future removal of
   `(1 - n_h/8)` in a nonzero-variance `n_h=4..7` case would not be
   reliably caught.

   Mandatory edit: add a hand-computed non-census interval test with
   nonzero stratum variance, checking `Vhat`, Satterthwaite df, and the
   Bonferroni half-width against the signed formula.

3. **Committee evaluation aggregation is not yet implemented.** The model
   exposes per-member `equal_probability` at
   `src/philosophia/level1/model.py:171`, and solve scoring consumes a
   scalar `p_equal` at `src/philosophia/level1/scoring.py:22`. The signed
   evaluator aggregation `p̄ = mean of four members' p_equal` is therefore
   still a later-gate evaluator piece, not implemented code.

   Mandatory edit before any evaluator/trajectory gate: add a tested
   aggregation function or keep this explicitly gated. Do not let any
   caller supply untracked scalar probabilities as if the committee
   evaluator were implemented.

## Minor findings

1. **Optimizer grouping is faithful, but order tests are shallow.** The
   decayed/non-decayed partition is implemented at
   `src/philosophia/level1/model.py:186` and exact coverage is checked at
   `src/philosophia/level1/model.py:207`. Tests verify group count and
   weight decay at `tests/test_level1_model_scoring.py:46`, but not exact
   parameter identity/order.

2. **Scoring side-effect checks omit RNG state.** ACTIVE scoring is
   `no_grad`, eval-mode, tie-broken by lowest pool index, and parameter/
   optimizer hash-checked at `src/philosophia/level1/acquisition.py:58`.
   This is adequate for the current deterministic scorer, but a future
   scorer change using RNG would need explicit RNG-state hashing.

3. **Panel real-order generation remains later-gated.** The dummy panel
   builder implements the signed panel contract and verifier, including
   global ids and secret-keyed realization domains
   (`src/philosophia/level1/panel.py:48`, `src/philosophia/level1/panel.py:152`).
   Real panel ordering and real escrow emission are correctly absent.

## Audit answers

### 1. Learner trajectory-sensitive cells

The architecture matches the signed v3 lineage: CPU-only input length 277,
learned token/position embeddings, two pre-LN transformer blocks, bidirectional
attention with PAD key masking, final LayerNorm, and a 2-logit head
(`src/philosophia/level1/model.py:123`, `src/philosophia/level1/model.py:154`).
Initialization uses per-tensor PRF-derived CPU generator seeds and the signed
fan-in scales (`src/philosophia/level1/model.py:536` in the source lineage;
implemented around `src/philosophia/level1/model.py:138`). AdamW groups are
decayed/non-decayed as required (`src/philosophia/level1/model.py:186`).

Trajectory-sensitive cells currently implemented:

- PRF/domain encoding and unbiased `U(r)`:
  `src/philosophia/level1/serialization.py:80`.
- Development/role/sample allocation domains:
  `src/philosophia/level1/allocation.py:49`,
  `src/philosophia/level1/allocation.py:73`,
  `src/philosophia/level1/allocation.py:80`.
- Model tensor shapes, init seeds, attention mask, final readout, and
  optimizer groups: `src/philosophia/level1/model.py:123`,
  `src/philosophia/level1/model.py:154`,
  `src/philosophia/level1/model.py:186`.
- Shortlist, replay, disagreement scorer, and side-effect check:
  `src/philosophia/level1/acquisition.py:20`,
  `src/philosophia/level1/acquisition.py:38`,
  `src/philosophia/level1/acquisition.py:58`.
- One-step CE training primitive:
  `src/philosophia/level1/train.py:17`.

The full learner trajectory driver, YOKED transcript consumption,
RANDOM-STATIC schedule execution, checkpoint storage/resume, and evaluator
aggregation are not implemented and remain correctly gated.

### 2. Solve-window and certificate scoring

The implemented scoring rules are faithful where present:

- Per-stratum thresholds are frozen at
  `src/philosophia/level1/scoring.py:14`.
- ABSTAIN uses strict `|p-0.5| < 0.10`, ABSTAIN is never correct, and
  prediction uses `p >= 0.5` at `src/philosophia/level1/scoring.py:33`.
- Confident lies use non-abstained wrong predictions with `p >= 0.9` or
  `p <= 0.1` at `src/philosophia/level1/scoring.py:45`.
- Per-stratum Brier over all items, ABSTAIN cap, S4 zero-lie cap, and
  Brier `<=0.10` are encoded at `src/philosophia/level1/scoring.py:64`.
- Persistence windows are computed over every checkpoint from `0` to
  `B=2000`, with missing checkpoints raising a process-route exception,
  at `src/philosophia/level1/scoring.py:96`.

No early-stop driver exists; this is correct at the current gate. The
function computes solve events from sealed checkpoint observations only;
full checkpoint production remains later-gated.

### 3. Estimator, predicates, and edge cases

The estimator direction is correct: for contrast `X-Y`, the block
difference is `cost_Y - cost_X`, positive favoring `X`
(`src/philosophia/level1/inference.py:66`). The finite-population
variance uses `W_h^2 = 1/9`, the FPC `(1 - n_h/8)`, and `s_h^2/n_h`
(`src/philosophia/level1/inference.py:75`). Census and all-zero
non-census labels are separated at `src/philosophia/level1/inference.py:79`.
Satterthwaite df and Bonferroni quantile are implemented at
`src/philosophia/level1/inference.py:89`.

Predicate guards match the signed table at
`src/philosophia/level1/inference.py:109`: all-censored arms resolve no
predicate; EQ requires at least one solve event in both arms; one-sided
predicates can resolve with one arm censored. Boundaries are correct:
`SUP L>60`, `NI L>-60`, `NONSUP U<60`, and inclusive `EQ`.

Blocking defect: the sample-size guard at
`src/philosophia/level1/inference.py:70` admits `n_h=2` and `n_h=3`,
which are not outcome-frame candidates.

### 4. N3 projection

`choose_n3` requires exactly the three frozen contrasts and all three
strata (`src/philosophia/level1/inference.py:126`), applies the
Popoviciu fallback `BUDGET**2` for zero/non-finite development variances
(`src/philosophia/level1/inference.py:139`), uses the same FPC projection
and Bonferroni quantile (`src/philosophia/level1/inference.py:141`), takes
the maximum half-width across contrasts (`src/philosophia/level1/inference.py:145`),
and returns the 24-block census if no sub-census candidate passes
(`src/philosophia/level1/inference.py:149`). It does not set or tune the
margin.

### 5. ACTIVE, YOKED, RANDOM, and selector surfaces

ACTIVE scoring is oracle-blind at the current abstraction: it receives
candidate tensors and no labels, runs under `torch.no_grad`, switches to
eval mode, restores modes, and verifies no model/optimizer mutation
(`src/philosophia/level1/acquisition.py:58`). Shortlists are drawn from
unanswered indices under domain-separated streams
(`src/philosophia/level1/acquisition.py:20`).

YOKED donor provenance, RANDOM-STATIC schedule execution, and the total
contact-mode selector are not yet implemented. They are not represented as
completed science and remain later-gated.

### 6. v3.1.4 panel repair

The dummy panel builder implements the signed inert panel repair:
188 items, fixed global ids, S4 unchanged, edge zone-3 sourcing,
S5 locked `{3,5,7,9}`, positive `p_v` for rejection-bearing drawn-pad
groups, and the dummy-only verifier
(`src/philosophia/level1/panel.py:62`,
`src/philosophia/level1/panel.py:159`,
`src/philosophia/level1/panel.py:178`,
`src/philosophia/level1/panel.py:245`,
`src/philosophia/level1/panel.py:284`).

Tests cover edge crossings and positive `p_v`
(`tests/test_level1_panel.py:30`), S4 unchanged
(`tests/test_level1_panel.py:46`), all-world enumeration
(`tests/test_level1_panel.py:55`), schema surface and S4 exemptions
(`tests/test_level1_panel.py:64`), and S5/S3 eligibility
(`tests/test_level1_panel.py:76`).

This repair is statistically inert: counts, label counts, thresholds,
endpoint, estimand, margins, predicates, and inference remain unchanged.
No anti-lookup authority is assigned outside S4.

### 7. Execution surfaces

The interlock exposes only a one-shot unit-step capability
(`src/philosophia/level1/interlock.py:17`) and makes trajectory execution
fail closed (`src/philosophia/level1/interlock.py:33`). The dummy panel
builder requires test-only public and panel keys
(`src/philosophia/level1/panel.py:48`). There is no code path for
OS-CSPRNG public-root drawing, real panel emission, real escrow,
feasibility/scout execution, N3 lock creation, or outcome execution.

### 8. Test capability

The Level 1 tests catch many key reversals:

- estimator direction and strict margin at
  `tests/test_level1_acquisition_inference.py:55`;
- all-censored guard and one-arm-censored `NONSUP` at
  `tests/test_level1_acquisition_inference.py:66`;
- N3 census fallback at `tests/test_level1_acquisition_inference.py:75`;
- side-effect-free scoring and tie-break at
  `tests/test_level1_acquisition_inference.py:26`;
- scoring thresholds/ABSTAIN at `tests/test_level1_model_scoring.py:85`;
- persistence window edge cases at `tests/test_level1_model_scoring.py:99`.

Gaps: add explicit tests for invalid `n_h=2/3`, non-census nonzero FPC and
Satterthwaite values, exact optimizer parameter identity/order, and future
committee mean aggregation once implemented.

### 9. Implementation defects vs later-gate absences

Implementation defects to fix now:

1. Restrict outcome contrast estimation to signed `n_h ∈ {4,5,6,7,8}` or
   split development and outcome estimators.
2. Add numeric non-census FPC/Satterthwaite tests.
3. Add explicit tests for invalid sample sizes and, preferably, optimizer
   parameter identity/order.

Later-gate absences that should remain absent:

- public-root entropy driver;
- real panel generator and real panel order;
- full learner trajectory/checkpoint/resume driver;
- evaluator committee aggregation and sealed checkpoint scorer;
- YOKED transcript execution, RANDOM-STATIC execution, total selector
  driver;
- feasibility/scout, N3 selection lock, real escrow, and outcome.

## Tests independently run

- `python3 -m pytest tests/test_level1_*.py` — failed because system
  Python has no `pytest` module.
- `.venv/bin/python -m pytest tests/test_level1_*.py` — 26 passed.
- `.venv/bin/python scripts/verify_all.py` — inherited primary and Level
  0 decisions valid.
- `.venv/bin/python -m pytest` — 115 passed.

## Exact next gate

After the mandatory edits and tests above, the next authorized step is
committing reviewed gated implementation code only. Acceptance after those
fixes still would not authorize the public-root draw, real panel
generation, learner data, feasibility/scout execution, N3 selection, lock,
escrow, trajectory, or outcome.
