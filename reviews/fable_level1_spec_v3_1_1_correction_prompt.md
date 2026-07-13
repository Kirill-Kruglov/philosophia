# Fable 5 prompt: Level 1 v3.1.1 bounded signature correction

Produce one final bounded correction to v3.1 after the Opus/Sol signature checks.
Do not rewrite v3/v3.1, reopen the world or 24-pair frame, implement code, draw
entropy, run data, generate escrow, create a lock/outcome, or predict an arm.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
3. `reviews/opus_level1_v3_1_signature_check.md`
4. `reviews/sol_level1_v3_1_signature_check.md`
5. `reviews/fable_level1_spec_v3_1_closure.md`
6. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`

## Deliverables

Write:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`
2. `reviews/fable_level1_spec_v3_1_1_closure.md`

V3 plus v3.1 carry forward except where this correction explicitly replaces
them. Use exactly one closure verdict:

- `READY_FOR_LEVEL1_AUTHOR_SIGNATURE`
- `REVISE_LEVEL1_V3_1_1`
- `BLOCKED_LEVEL1_CYCLIC_CERTIFICATE`

## C1. Replace S4 with an offset-only, parity-safe construction

The v3.1 marginal balance is rejected: `(symmetry, side parity)` is an XOR label
leak. Remove **all symmetric S4 items**.

Use this bounded construction unless you prove an exactly stronger one:

- increase `A_word` from 126 to **128**;
- max raw word length becomes **138** (`A_word+10`);
- model padded input/learned positions become **277** (`2*138+1`);
- keep `d_acq=125` and the acquisition world/pool semantics otherwise unchanged;
- YES difference: `2n`;
- NO-low: `2n-4` (nonzero remainder `n-4`);
- NO-high: `2n+4` (remainder `4`);
- all are uncontactable: minimum `2*66-4=128>125`;
- all are realizable: maximum `2*125+4=254<=2*128`.

For a class with center `c=d/2`, every semantic split is **offset-only** with
`k in {-1,+1}`:

`(a,b)=(c+k, -(c-k))`.

Thus every item has `|a|!=|b|`, `||a|-|b||=2`, the same endpoint parity pattern,
and no symmetry/parity XOR. Use 8 YES, 4 NO-low, 4 NO-high; balance `k` signs
within every class and use distinct raw realizations for repeated semantic
splits.

Freeze padding/length distributions exactly. A workable construction uses base
padding vectors

`A={(1,1),(1,2),(2,1),(2,2)}`:

- four YES items use `A`, four YES use `A+(1,1)`;
- four NO-low use `A+(1,1)`;
- four NO-high use `A`;
- assign `k=-1,+1` evenly and identically across the base-vector order.

Prove label-conditional equality of the distributions of: symmetry indicator,
endpoint parity pattern, `||a|-|b||`, offset sign, padding-vector multiset,
ordered/permuted side-length multiset, and total raw length. Check `n=66` and
`n=125` explicitly. If any proposed equality is false, correct the table rather
than asserting it.

**Do not make an impossible claim.** Complete raw observables determine `d`, and
the labels intentionally differ by whether that novel `d` is a multiple of the
contact-anchored `n`. The certificate may not claim to distinguish an abstract
period representation from a learner that recovered/memorized `n` and performs
correct novel-`d` arithmetic. Replace the S4 meaning with:

> The learner recovered a contact-anchored modulus value sufficient to classify
> previously uncontactable opposite-corner differences `2n` versus `2n±4`.

A pass is evidence for that operational competence only; a failure remains
censoring and never proves the learner lacked `n`. Add an authorial scope token:

`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`

Alternative: `I_REJECT_LEVEL1_CYCLIC_CERTIFICATE` (blocks Level 1 and requires a
world redesign). Do not hide this choice inside the consolidated token.

The feature-null verifier must test the **joint declared nuisance vector**, not
marginal MI. It may exclude exact features/combinations sufficient to reconstruct
`d`, because those are the operational structure being tested; list that
exclusion explicitly. It must show that no fixed `n`-free rule over the declared
non-structural surface fields predicts labels.

Update every affected constant/inequality in v3/v3.1 (`A_word`, length, input,
position count, zone maximum, edge proofs, panel table, tests). Do not change the
registry, acquisition cap, counts, or estimand.

## C2. Close generator gaps

Replace allocation domains with independently scoped streams:

- `("L1","alloc","dev",h)` for each stratum;
- `("L1","alloc","role",pair_slot)` for exactly one role bit per canonical
  outcome pair;
- `("L1","alloc","sample",N3,h)` for each stratum after N3.

Each domain owns a counter starting at zero; rejection increments only that
domain's counter; `U(1)` consumes nothing. State canonical `h=1,2,3` and ascending
pair-slot processing. This removes reset/continuity ambiguity.

Route every S4 raw side through an exact panel-specific PRF domain including
world slot, S4 item id, side, displacement, fixed padding, and word rank. Select
the word by the existing unbiased rank draw from `W(a,length)`; collision-reject
within S4. No zone-1 pool domain may be ambiguously reused for evaluator-only
cells.

For S5 length-constrained reserved consumption, define eligibility before rank:
the cell must admit the required `>=100` side lengths/imbalance under `p<=5`;
then choose the lowest canonical eligible unused reserved cell. Exhaustion is
fail-closed and enumerated.

Clarify serialization decoder mapping: ASCII artifact token bytes map normatively
to model token ids `{PAD=0,R=1,L=2,SEP=3}`.

## C3. Separate public allocation entropy from secret panel entropy

Resolve Sol's root-visibility question and the escrow interaction:

- the one-shot allocation/training root is **public in its committed transcript
  immediately after the durable draw**; this is required for allocation and
  learner reproducibility;
- it may derive allocation, pool, model init, shortlist, replay, controls, and
  feasibility streams;
- it must **not derive the real evaluator panel**, panel raw realizations, panel
  ordering, encryption salt, or escrow plaintext.

Remove `("L1","panel",...)` from the public-root domain list. Real panel
randomness comes from a separate 256-bit **escrow-secret seed generated exactly
once inside the later locked escrow environment**, encrypted before exposure and
never published before outcome. Its commitment/protocol follows the existing
salted-encryption escrow rules. Dummy panel tests use a declared test-only seed
and can never emit a real artifact. This prevents a public root from making the
sealed panel reconstructible.

Witness attestation for the public root covers process facts only: path absent,
one OS-CSPRNG call, durable write/commit, environment fingerprint, no redraw. It
claims no cryptographic independence.

## C4. Complete model pins

Update A5 to input length/learned positions **277** and displacement/word length
128/138.

Enumerate `fan_in`:

- token/position embeddings: 128 for initialization scale;
- each Q/K/V/O: 128;
- MLP `W_in`:128, `W_out`:512;
- head:128.

State that `PRF(...)[0:8]` is decoded as an unsigned big-endian integer in
`[0,2^64-1]` and passed to `torch.Generator.manual_seed`. Pin the exact locally
available torch build string; if `2.9.1+cpu` is not installable, use the actual
enforced `torch.__version__` and treat any later change as amendment. Add tests
for every tensor shape/draw seed/param-group membership.

## C5. Noninterference canonicalization

Literal bundles cannot be byte-identical if they contain different slot values.
Define comparison as:

1. serialize each learner-visible bundle;
2. replace its opaque schedule-slot field with one canonical placeholder value
   (or omit it entirely if unused by the learner);
3. compare the canonicalized bytes across worlds.

The slot-to-world mapping remains outside learner/acquisition reach. Add a test
that canonicalization is the only permitted difference and that no `n`, pair id,
world hash, target-specific length, or panel-root material appears.

## C6. Exact inference text corrections

Carry A9 formulas but add:

- if all `v_h=0` at `N3<24`, define `[L,U]=[Delta_hat,Delta_hat]` directly;
  do not evaluate df or a t quantile; label “estimated zero sample variance, not
  census certainty”;
- if only some `v_h=0`, omit their denominator terms exactly as already stated;
- boundary inequalities and Sol's directional table remain unchanged.

Clarify N3:

- candidates below 24 may fail projected precision;
- if none below 24 passes, the statistical rule selects the **24-block census**,
  whose FPC half-width is identically zero;
- therefore “precision fails at 24” is withdrawn as unreachable;
- a lock may still be blocked by resource infeasibility, process/design
  invalidity, feasibility failure, or Kirill's signed refusal to run the census —
  these are not statistical half-width failures.

Clarify fallback:

- `B^2` is Popoviciu's upper bound on the finite-population variance of a
  variable in `[-B,B]`, used only when a two-block development variance is zero,
  undefined, or non-finite;
- any observed finite nonzero `s_dev^2` is used as observed, even if it exceeds
  `B^2` (the unbiased two-point sample variance can reach `2B^2`);
- show the projection formula and maximum-over-three-contrasts rule unchanged.

## C7. Final gate/signature packet

The correction must leave no implementation or scientific choice open. Updated
signature packet:

1. `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`
2. `I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`
3. `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` — v3 incorporating v3.1 and v3.1.1.

Gate order remains: final bounded Opus/Sol check → all three Kirill signatures →
implementation/tests → reviewed one-shot public-root driver/execution → reviewed
optional feasibility → comparative scout → N3/census selection + lock → secret
real-panel escrow → outcome.

No code, entropy, feasibility, comparative scout, lock, escrow, or outcome is
authorized by this correction.

## Closure memo

Include:

- the single verdict;
- disposition of Opus C-1/MJ-1/MJ-2/mn-1/mn-2 and every Sol Major/Minor;
- exact replacement index into v3/v3.1;
- algebraic verification of the new S4 at both edges and the precise operational
  certificate scope;
- public-root versus escrow-secret surface table;
- final bounded questions for Opus/Sol;
- implementation/gate authorization and confirmation of no execution.
