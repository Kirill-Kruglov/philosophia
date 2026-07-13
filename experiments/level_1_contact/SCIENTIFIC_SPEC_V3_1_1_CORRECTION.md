# Level 1 scientific specification — v3.1.1 bounded signature correction

Status: `CORRECTION_FOR_AUTHOR_SIGNATURE`. **v3 plus v3.1 carry forward
except where a section below explicitly replaces them.** v1–v3.1 preserved
unchanged. This correction creates no code, entropy, feasibility or
comparative datum, escrow, lock, or outcome, and predicts no arm. The
world, 24-pair frame, adjacent-only scope, estimand, registry, acquisition
cap, counts, and selector are not reopened.

---

## C1. S4 replaced: offset-only, parity-safe (replaces v3.1 A1's construction, meaning, and verifier)

**Constants updated (replaces the corresponding v3 §3 rows and every
dependent inequality/test):** `A_word = 128`; max raw word length
**138** (`A_word + 10`); model padded input and learned positions
**277** (`2·138 + 1`); extrapolation zone becomes `|d| ∈ (125, 256]`.
`d_acq = 125` and all acquisition world/pool semantics are unchanged.

**Differences.** YES: `d = 2n` (8 items). NO-low: `d = 2n − 4`
(remainder `n − 4 ≥ 62 ≠ 0`; 4 items). NO-high: `d = 2n + 4`
(remainder `4 ≠ 0`; 4 items). Uncontactable: minimum
`2·66 − 4 = 128 > 125`. Realizable: maximum `2·125 + 4 = 254 ≤ 2·128 =
256`.

**Splits — offset-only, no symmetric items.** For a class with center
`c = d/2` (integer: all three `d` are even), every split is
`(a, b) = (c + k, −(c − k))` with `k ∈ {−1, +1}`. Hence every item has
`|a| ≠ |b|`, `||a| − |b|| = 2`, and — because `c ∈ {n − 2, n, n + 2}`
share one parity — **every side of every item has parity
`≡ c + 1 ≡ n + 1 (mod 2)`**: the endpoint parity pattern is
label-constant, the symmetry indicator is label-constant (all offset),
and the v3.1 `XOR(split, side-parity)` channel is gone at the source.
`k` signs are balanced within every class; repeated semantic splits use
distinct raw realizations.

**Padding (exact).** Base vectors `A = {(1,1), (1,2), (2,1), (2,2)}`
(pairs `(p_u, p_v)` of cancelling-pair counts), with `k` assigned
`(−1, +1, −1, +1)` across the base-vector order identically in every
group:

| Group | Count | `c` | Padding vectors |
|---|---|---|---|
| YES-A | 4 | `n` | `A` |
| YES-A′ | 4 | `n` | `A + (1,1)` |
| NO-low | 4 | `n − 2` | `A + (1,1)` |
| NO-high | 4 | `n + 2` | `A` |

**Label-conditional equality proofs (computed, not asserted).** Side
length = `|displacement| + 2p`; total = `2c + 2(p_u + p_v)`.

- *Symmetry indicator:* constant (all offset). ✓
- *Endpoint parity pattern:* constant `≡ n + 1 (mod 2)` for every side
  of all 16 items. ✓
- *`||a| − |b||`:* constant `= 2`. ✓
- *Offset sign:* `(−1, +1, −1, +1)` in every group → 2:2 per class,
  4:4 per label. ✓
- *Padding-vector multiset:* YES = `A ⊎ (A + (1,1))`; NO =
  `(A + (1,1)) ⊎ A`. Identical. ✓
- *Total raw length:* YES = `2n + {4,6,6,8} ⊎ 2n + {8,10,10,12}`; NO =
  `(2n − 4) + 2Σ(A + (1,1)) = 2n + {4,6,6,8}` ⊎
  `(2n + 4) + 2ΣA = 2n + {8,10,10,12}`. Identical multisets. ✓
- *Ordered side-length sequences:* the `c`-shift and the padding shift
  cancel exactly (`c − 2` with `p + 1` ⇒ same side lengths as `c` with
  `p`), so NO-low reproduces YES-A's ordered side lengths
  `{(n+1, n+3), (n+3, n+3), (n+3, n+3), (n+5, n+3)}` and NO-high
  reproduces YES-A′'s `{(n+3, n+5), (n+5, n+5), (n+5, n+5), (n+7, n+5)}`
  — the label-conditional ordered and permuted side-length multisets are
  identical. ✓

**Edge checks (explicit).** `n = 66`: NO-low `c = 64`, endpoints
`(63, −65)/(65, −63)`, `d = 128 > 125` ✓; NO-high `c = 68`, max
endpoint 69 ✓. `n = 125`: NO-high `c = 127`, endpoints
`(128, −126)/(126, −128)`, `|a| ≤ 128 = A_word` ✓, `d = 254 ≤ 256` ✓;
max side length `n + 7 = 132 ≤ 138` ✓. No edge-world special table is
needed — one construction covers the whole registry.

**Certificate meaning (replaces v3.1's "period plus novel opposite-corner
composition" sentence).** Complete raw observables determine `d`, and the
labels differ exactly by whether that novel `d` is a multiple of the
contact-anchored `n`; the certificate therefore may not claim to
distinguish an abstract period representation from a learner that
recovered/memorized `n` and performs correct novel-`d` arithmetic. The S4
meaning is:

> The learner recovered a contact-anchored modulus value sufficient to
> classify previously uncontactable opposite-corner differences `2n`
> versus `2n ± 4`.

A pass is evidence for that operational competence only; a failure
remains censoring and never proves the learner lacked `n`. Authorial
scope token (not hidden inside the consolidated token):
`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`; alternative:
`I_REJECT_LEVEL1_CYCLIC_CERTIFICATE` — blocks Level 1 and requires a
world redesign.

**Feature-null verifier (replaces v3.1's marginal check).** The verifier
tests the **joint declared nuisance vector** — per item: (symmetry
indicator, per-side parity pattern, `||a| − |b||`, offset sign, padding
vector, ordered side lengths, total length) — requiring the
**label-conditional multiset of the entire vector, and of every pairwise
and triple sub-combination, to be identical for YES and NO** (exact
count identity, unit-testable). It explicitly **excludes** the features
sufficient to reconstruct `d` — the signed displacement pair `(a, b)`,
`d` itself, and `|a| + |b|` — because classifying by `d mod n` is the
operational structure being tested. It must additionally show that **no
fixed `n`-free rule over the declared non-structural surface fields
predicts labels above chance** (exhaustive check over the declared field
set). Verifier failure = design invalidity.

## C2. Generator gaps closed (replaces the corresponding v3.1 A2/A3 lines)

**Allocation domains (independently scoped, replaces A2's three
domains):** `("L1","alloc","dev", h)` per stratum;
`("L1","alloc","role", pair_slot)` — exactly one role bit per canonical
outcome pair; `("L1","alloc","sample", N3, h)` per stratum after `N3`.
**Each domain owns its own counter starting at zero; a rejection redraw
increments only that domain's counter; `U(1)` consumes nothing and
leaves the counter unchanged.** Canonical processing order: strata
`h = 1, 2, 3`; pair slots ascending within each stratum. No counter is
ever shared or reset across domains.

**S4 raw words (closes Opus MJ-2).** Every S4 raw side is drawn through
an exact **panel-specific** PRF domain
`("L1","panel", world_slot, "S4", item_id, side, displacement,
p_fixed)` — keyed by the **escrow-secret seed** (C3), not the public
root — selecting the word by the existing unbiased rank draw
`U(|W(a, ℓ)|)` → combinatorial unrank, with A1's fixed paddings;
duplicate `(u, v)` pairs are collision-rejected **within S4** (counter
advances). No zone-1 pool domain is reused for evaluator-only cells.

**S5 length-constrained consumption (closes Opus mn-2).** Eligibility
precedes rank: a reserved cell is eligible for an S5 item iff it admits
the required `≥ 100` side lengths / imbalance under `p ≤ 5` (i.e.
`|displacement| ≥ 90` where required); the item takes the
lowest-canonical-rank **eligible** unused reserved cell. Exhaustion is
fail-closed design invalidity, enumerated at the S-gate.

**Serialization decoder (clarifies A3):** artifact token bytes map
normatively to model token ids: `0x5F (PAD) → 0`, `0x52 (R) → 1`,
`0x4C (L) → 2`, `0x7C (SEP) → 3`.

## C3. Public allocation entropy vs secret panel entropy (replaces the panel line of v3.1 A2's domain list)

- The one-shot allocation/training root is **public in its committed
  transcript immediately after the durable draw** — required for
  allocation and learner reproducibility. It derives: allocation
  (`dev`, `role`, `sample`), pool reservation and zone-1 realizations,
  model member inits, shortlists, replay, shuffled controls, and
  feasibility streams.
- It **must not and does not derive**: the real evaluator panel, panel
  raw realizations, panel ordering, the encryption salt, or escrow
  plaintext. `("L1","panel", …)` is **removed from the public-root
  domain list.**
- Real panel randomness comes from a separate **256-bit escrow-secret
  seed generated exactly once inside the later locked escrow
  environment**, encrypted before any exposure and never published
  before outcome, under the existing salted-encryption escrow rules
  (v3 §10 / v3.1). Panel streams use the same PRF/`U`/Fisher–Yates
  machinery keyed by this secret seed.
- **Dummy panel tests** use a declared test-only seed
  (`"L1-TEST-ONLY"` derivation, non-secret) and can never emit a real
  artifact (fail-closed: real panel emission requires the escrow
  environment attestation).
- **Witness attestation scope (public root):** process facts only —
  transcript path absent before the draw, exactly one OS-CSPRNG call,
  durable write/commit, environment fingerprint, no redraw. No
  cryptographic-independence claim.

Surface table:

| Surface | Key | Visibility |
|---|---|---|
| Allocation, pool, inits, shortlist, replay, controls, feasibility | public root | public transcript immediately after draw |
| Real panel content/realizations/ordering, salt, plaintext | escrow-secret seed | sealed; released only at authorized outcome |
| Dummy/test panels | declared test-only seed | public; can never produce a real artifact |

## C4. Model pins completed (amends v3.1 A5)

- Input length and learned positions: **277**; displacement/word-length
  bounds **128/138** (from C1).
- **`fan_in` enumeration (initialization scale `1/√fan_in`):** token
  embedding **128**; position embedding **128**; each of
  `W_Q, W_K, W_V, W_O` **128**; MLP `W_in` **128**; MLP `W_out` **512**;
  head **128**.
- `PRF(domain, 0)[0:8]` is decoded as an **unsigned big-endian integer
  in `[0, 2⁶⁴ − 1]`** and passed to `torch.Generator.manual_seed`.
- Torch build: the enforced local build string is **`2.9.1+cpu`**
  (verified installed and already pinned by the Level 0 platform); the
  environment gate enforces exact equality of `torch.__version__`, and
  any change is a signed amendment.
- Required tests: every tensor's shape, its draw seed derivation, and
  its parameter-group membership (decayed vs non-decayed) are asserted
  by enumeration.

## C5. Noninterference canonicalization (replaces the byte-identity sentence of v3.1 A7)

Literal bundles cannot be byte-identical while containing different slot
values. Comparison is defined as: (1) serialize each learner/
acquisition-visible pre-contact bundle; (2) replace its opaque
schedule-slot field with one canonical placeholder value — or omit the
field entirely if the learner never reads it; (3) compare the
canonicalized bytes across all development worlds, which must be
identical. The slot-to-world mapping remains outside learner/acquisition
reach. Required test: canonicalization is the **only** permitted
difference, and no `n`, pair id, world hash, target-specific length, or
panel-root material appears anywhere in the bundle.

## C6. Exact inference text corrections (amends v3.1 A9)

All A9 formulas carry forward, with:

- **All-zero variance at `N3 < 24`:** if every `v_h = 0`, the interval
  is defined directly as `[L, U] = [Δ̂, Δ̂]`; no degrees of freedom and
  no `t` quantile are evaluated; the decision artifact labels it
  **"estimated zero sample variance, not census certainty."** If only
  some `v_h = 0`, their denominator terms are omitted exactly as
  already stated. Boundary inequalities and the directional determinacy
  table are unchanged.
- **N3 clarification (replaces "if no candidate through 24 passes: no
  lock"):** candidates below 24 may fail the projected precision rule;
  **if none below 24 passes, the frozen statistical rule selects the
  24-block census**, whose FPC half-width is identically zero —
  "precision fails at 24" is withdrawn as unreachable. A lock may still
  be blocked by resource infeasibility, process/design invalidity,
  feasibility-gate failure, or Kirill's signed refusal to run the
  census; none of these is a statistical half-width failure.
- **Fallback clarification:** `B²` is **Popoviciu's upper bound on the
  finite-population variance of a variable in `[−B, B]`**, used only
  when a two-block development variance is zero, undefined, or
  non-finite. It is not the maximum two-point unbiased sample variance
  (which can reach `2B²`). **Any observed finite nonzero `s²_dev` is
  used as observed, even if it exceeds `B²`.** The projection formula
  and the maximum-over-three-contrasts ≤ 30 rule are unchanged.

## C7. Final gate order and signature packet (replaces v3.1 A10's packet line)

**Signature packet (three tokens, none consolidated away):**

1. `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`
2. `I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`
   (alternative: `I_REJECT_LEVEL1_CYCLIC_CERTIFICATE` — blocks Level 1,
   requires world redesign)
3. `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` — v3 incorporating v3.1 **and
   v3.1.1**.

**Gate order:** final bounded Opus/Sol check → all three Kirill
signatures → implementation/tests → reviewed one-shot **public-root**
driver/execution → reviewed optional feasibility → comparative scout →
N3/census selection + lock → **secret real-panel escrow** → outcome.

No code, entropy, feasibility, comparative scout, lock, escrow, or
outcome is authorized by this correction.
