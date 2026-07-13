# Fable 5 prompt: bounded Level 1 v3.1 signature addendum

Produce a **bounded v3.1 addendum** after the final Opus X-line and Sol Y-line
reviews. Do not rewrite v3, reopen accepted world/estimand choices, implement
code, generate allocation entropy, run feasibility/comparative data, create
escrow/lock/outcome, or predict an arm.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
3. `reviews/fable_level1_spec_v3_closure.md`
4. `reviews/opus_level1_spec_v3_final_review.md`
5. `reviews/sol_level1_spec_v3_final_review.md`
6. `canonical/CLAIM_LEDGER.md`
7. `canonical/KILL_MATRIX.md`

The formal reviews govern; chat captures are provenance only. Preserve v1-v3
unchanged.

## Deliverables

Write:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
2. `reviews/fable_level1_spec_v3_1_closure.md`

The addendum must state that v3 carries forward except where explicitly
replaced. Include exact replacement text/table/formulas, not commentary asking an
implementer to choose later.

Use exactly one closure verdict:

- `READY_FOR_LEVEL1_SIGNATURE_CHECK`
- `REVISE_LEVEL1_V3_1_ADDENDUM`
- `BLOCKED_LEVEL1_CERTIFICATE`

## Accepted v3 choices: do not reopen

- adjacent-only detector scope and its thin distance-1 negative boundary;
- 24-pair outcome frame, conditional finite-seed interpretation, and census at
  `N3=24`;
- three-zone structure with `A_word=126`, `d_acq=125`;
- opaque flat acquisition indices and fixed multiplicity `m=4`;
- committee acquisition, without-replacement selection, and side-effect-free
  scorer principle;
- RMST-as-bounded-cost, Bonferroni primary family, `m=60`, total selector;
- no survivor-FPC, salted encrypted escrow, and N3 no-clamp principle;
- every signed negative destination.

## Mandatory bounded replacements

### A1. Repair S4's only anti-lookup tooth

Replace S4 negative differences `2n +/- 1` with **symmetric even near-misses
`2n +/- 2`**:

- YES: `d=2n`, endpoints `(n,-n)`;
- NO-low: `d=2n-2`, endpoints `(n-1,-(n-1))`;
- NO-high: `d=2n+2`, endpoints `(n+1,-(n+1))`.

Keep 8 YES, 4 NO-low, 4 NO-high. Prove:

- all are even and magnitude-symmetric, so parity and `|a|=|b|` cannot reveal
  the label;
- negative remainders are nonzero for every `n in [66,125]`;
- support is `[130,252]`, fully outside `d_acq=125` and realizable with
  `A_word=126` at both edges;
- raw word-pair **total lengths, per-side length distributions, padding counts,
  and token-count parity are matched across labels** by an exact construction,
  not the word “matched.”

State residual scope honestly: this remains period plus novel opposite-corner
composition. Require a feature-null verifier proving no exposed syntactic field
or simple parity/magnitude/length feature predicts S4 labels above chance.

Correct S2 and S5 novelty annotations: at the stated upper-edge worlds some
negative differences cross into zone 3 and are difference-novel; note the
world-dependent difficulty without granting them anti-lookup authority.

### A2. One exact deterministic byte generator after one real entropy draw

Define a single normative RNG/serialization primitive used everywhere.

**Root entropy protocol:** after the addendum passes signature check and Kirill
signs the S-gate, but before any development use, a reviewed fail-closed driver
obtains exactly 32 bytes from the OS CSPRNG (`getrandom`/Python
`secrets.token_bytes(32)`) once. It atomically writes and commits an allocation
transcript binding root bytes, addendum/spec/git hashes, timestamp, environment,
and witness attestation. It refuses if the transcript path exists. No redraw,
deletion/retry, or alternative seed is permitted; failure before durable commit
routes to a signed invalidity decision, not a quiet second draw. State the
procedural rather than cryptographically independent threat model.

If you choose an externally auditable future beacon instead, fully specify it
and its failure behavior; do not leave alternatives in the normative path.

**Domain PRF stream:** pin one exact construction, for example:

- `HMAC-SHA256(key=root, message=canonical_length_prefixed_components ||
  uint64_be(counter))`;
- UTF-8/ASCII byte encoding, component length width/endian, integer encoding,
  and counter start/increment;
- exact domain components for allocation/dev, role, outcome sample by N3, pool
  reserve, raw realization, panel, learner replicate/member init, shortlist,
  replay, shuffled control, and feasibility.

**Uniform integer `U(r)`:** interpret the 32-byte digest as an unsigned
big-endian integer; let `limit=floor(2^256/r)*r`; reject `x>=limit`, increment
counter, otherwise return `x mod r`. Define behavior for `r=1`. Fisher-Yates is
descending and uses this exact `U(i+1)`. Remove “rejection-free.”

**Timing:** draw `D` before development use; assign roles over `O` once and
condition; draw `R_h` only after frozen N3 is computed, from the already
committed root and domain containing N3; no regeneration after feasibility,
censoring, loss, or contrasts. Inclusion probability is then `n_h/8` under the
one-shot randomized mechanism.

### A3. Bit-exact pool and raw-word construction

Freeze:

- cell orientation and canonical enumeration order;
- exact reserve count for each `|d|` class (use `floor(3*N_d/10)` unless a
  different single rule is justified);
- exact unbiased sample without replacement of reserved cells;
- exact flat index order of non-reserved cells and four realizations;
- canonical serialization with schema/version, integer widths/endian, token
  bytes, list ordering, and hashes.

Define raw words mechanically. A suitable normative construction is:

- `W(a)` = all `{R,L}` words with net displacement `a`, length
  `|a|+2p`, `p in {0..5}`, length <=136;
- canonical order = length, then lexicographic tokens (`R<L` or the exact
  reverse, choose one);
- combinatorial rank/unrank or another exact enumerator;
- for cell `{a,b}`, enumerate/sample raw `(u,v)` pairs without replacement from
  `W(a) x W(b)`, orientation fixed by the cell; reject exact duplicate pairs;
- draw exactly four by the normative PRF; specify collision handling and prove
  availability, including `d=0` and S3 `u!=v`.

Define reserved-cell consumption by fixed stratum order `S1..S5`, item order,
canonical eligible-cell order, and a fail-closed exhaustion rule. Replace every
“locked draw,” “lowest unused,” and “matched” with an algorithm or an exact
verifier predicate.

### A4. Correct the panel metadata surfaces

Separate exactly:

1. learner/acquisition-visible panel metadata: none;
2. researcher-visible pre-outcome: per-world ciphertext and salted content
   digest, necessarily different;
3. world-independent schema surface: panel-local ids `0..187`, counts, order,
   stratum names, and schema hash, byte-identical.

Remove content/ciphertext hashes from the byte-identical claim. Give canonical
panel serialization and bind the sealed local-id-to-query/label mapping inside
the ciphertext.

### A5. Bit-exact transformer and optimizer

Choose one architecture, not alternatives. Prefer **bidirectional** self-
attention to avoid causal left-PAD all-masked rows unless a different exact
repair is justified. Freeze:

- token+learned-position sum, PAD key mask, PAD query behavior, no causal mask;
- per layer: `x = x + MHA(LN1(x))`; `x = x + MLP(LN2(x))`; final LayerNorm
  before the 2-logit head;
- LayerNorm epsilon, attention `QK^T/sqrt(32)`, softmax axis, Q/K/V/O bias
  presence, MLP biases, projection orientations;
- final readout position and PAD handling;
- initialization for token embeddings, positional embeddings, every matrix,
  bias, LN gain/offset, plus a canonical tensor draw order;
- CPU/accelerator, float32, torch/Python versions, thread count, deterministic
  algorithm flags, and environment enforcement;
- no gradient clipping (or exact clipping), CE reduction=`mean`, no label
  smoothing;
- AdamW decoupled update semantics, one parameter group for decayed matrices and
  one for non-decayed tensors, exact membership/order;
- step/backward/zero ordering and checkpoint cadence/state;
- two exact replicate master ids and the normative PRF keys for member init,
  shortlist, replay, arm, block, and purpose.

If canonical CPU float32 makes the frozen budget infeasible, that is for the
later non-comparative feasibility gate and signed amendment; do not silently
switch devices in the addendum.

### A6. Calibration and divergence semantics

Replace global non-abstained Brier with **per-stratum Brier <=0.10 over every
item**, using `p_bar` even when the classification rule says ABSTAIN. Thus an
abstention near 0.5 contributes approximately 0.25 and cannot improve
calibration by exclusion. Keep count/ABSTAIN/confident-lie rules unless their
logical conjunction becomes impossible; verify with examples.

Resolve non-finite timing:

- if a full five-checkpoint qualifying window completed before the first
  non-finite state, its already established `T` stands and later divergence is a
  mandatory diagnostic;
- if no window completed first, record censored at B;
- finiteness classification precedes generic missing-checkpoint routing;
- a permitted process re-execution must reproduce hashes through the last
  committed **pre-fault** checkpoint, not reproduce the transient fault;
- any seal breach remains whole-level invalidity with no re-execution.

### A7. Replace vague leakage gates with exact protocols

**Pre-contact encoding:** prefer the stronger mechanical gate. Define the exact
learner/acquisition-visible pre-contact byte bundle. After removing opaque
block/seed handles or encoding them through world-independent slots, require
byte identity (or an exact approved equality relation) across all development
worlds. Any target-`n`-dependent byte/length/hash/query ordering is design
invalid. Withdraw the underpowered “top-1 <=1/6” ML probe unless you fully define
a stronger protocol; a deterministic noninterference verifier is preferred.

**Shuffled answers:** freeze worlds, arm/schedule, number of runs, two exact
replicates, permutation method/PRF domain, preservation of transcript/query
geometry, full B, sealed evaluator, and zero-solve invalidity rule. Explain that
this is a development design-invalidity gate with finite scope, not proof of
global leakage absence.

Parameter shift remains diagnostic only.

### A8. Feasibility check must measure the scorer

Keep the single RANDOM-STATIC development trajectory for endpoint computability,
but add a scorer-only microbenchmark or one ACTIVE timing path that exercises
`S=512`, `E=4`, length273 without recording/persisting query/loss/solve series or
arm contrasts. Exact allowed outputs: latency aggregates, peak memory, projected
wall, artifact sizes, finiteness, and at most the already permitted single-arm
censoring indicator.

The censoring indicator can justify only a binary feasibility floor amendment
(the locked architecture/B produced at least one complete development solve or
did not); it may never tune toward a target solve rate or threshold. Any change
requires a signed addendum and repeat review before S-gate completion.

### A9. Exact estimator, directional guards, and N3 projection

Display the complete formulas:

- `s_h^2` with denominator `n_h-1`;
- `v_h`, `Vhat=sum(v_h)`;
- Satterthwaite `nu=Vhat^2 / sum(v_h^2/(n_h-1))`;
- zero-component behavior; if all components zero at `N3<24`, point interval is
  reported as **estimated zero sample variance**, not known zero population
  uncertainty;
- Bonferroni critical `t_(1-0.05/(2*3),nu)`;
- census point rule at 24.

Freeze boundary inequalities: `SUP L>60`; `NI L>-60`; `NONSUP U<60`; `EQ
L>=-60 and U<=60`. Equality at a one-sided margin is unresolved/false for that
predicate.

Replace the guard with the Sol table:

- both arms all-censored: no predicate;
- exactly one arm has any event: one-sided `SUP/NI/NONSUP` may resolve solely by
  interval direction; `EQ` forbidden;
- both have events: all predicates eligible.

This allows a strong C1-negative direction when YOKED solves and ACTIVE does
not, without allowing administrative equivalence.

N3 projection must use the **maximum** projected Bonferroni half-width over all
three contrasts. With only two development blocks per stratum, freeze a
conservative fallback: any undefined/non-finite scout variance, or exact zero
from only two blocks, is replaced for projection by the bounded-difference
maximum variance `B^2` (or another explicit mathematically conservative bound).
Show the formula. If no candidate through 24 passes, no lock.

### A10. Updated gates and signature packet

Gate order must now distinguish:

1. v3.1 final signature check;
2. Kirill scope/spec signatures;
3. implementation of exact generators/model plus tests;
4. reviewed one-shot root-entropy/allocation driver and execution;
5. optional reviewed non-comparative feasibility execution;
6. any signed feasibility amendment + re-review;
7. comparative development scout;
8. N3 selection and lock;
9. real escrow;
10. outcome driver/execution.

No entropy draw, implementation, feasibility run, comparative scout, lock,
escrow, or outcome is authorized by the addendum itself.

## Closure memo

Include:

1. the single verdict;
2. disposition of every Opus C/MJ/mn and Sol Critical/Major/Minor;
3. exact replacement index mapping addendum sections to v3 sections;
4. compact normative constants/algorithms table;
5. final Opus/Sol signature-check questions, limited to whether the bounded
   repairs landed;
6. unchanged authorial tokens:
   `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE` and
   `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC`, with the latter explicitly incorporating
   the v3.1 addendum;
7. implementation authorization and negative space;
8. confirmation no code/data/entropy/scout/escrow/lock/outcome was created.

Do not strengthen a certificate failure into evidence that the learner lacked
`n`; do not broaden C1 beyond distance 1; do not treat deterministic selection
as randomization; do not allow UNKNOWN/all-censored to become a boundary.
