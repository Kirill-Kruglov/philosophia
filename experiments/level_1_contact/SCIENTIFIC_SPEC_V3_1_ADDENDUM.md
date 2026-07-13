# Level 1 scientific specification — v3.1 addendum

Status: `ADDENDUM_FOR_SIGNATURE_CHECK`. **v3 carries forward except where a
section below explicitly replaces it.** v1–v3 are preserved unchanged. This
addendum contains exact replacement text, tables, and formulas — no deferred
implementer choices. It creates no code, allocation entropy, feasibility or
comparative datum, escrow, lock, or outcome, and predicts no arm.

Accepted v3 choices are not reopened: adjacent-only detector scope and its
thin distance-1 boundary; the 24-pair outcome frame with conditional
finite-seed reading and census at `N3 = 24`; the three zones with
`A_word = 126`, `d_acq = 125`; opaque flat indices with `m = 4`; committee
acquisition, without-replacement selection, side-effect-free scorer;
RMST-as-bounded-cost, Bonferroni primary family, `m = 60`, the total
selector; no survivor-FPC; salted encrypted escrow; the N3 no-clamp
principle; every signed negative destination.

---

## A1. S4 repair — symmetric even near-misses (replaces the S4 row of v3 §4 and its corner construction)

**Differences.** YES: `d = 2n` (8 items). NO-low: `d = 2n − 2` (4 items).
NO-high: `d = 2n + 2` (4 items).

**Proofs.**
- All three differences are even, so difference parity is label-constant.
- Remainders are nonzero for every `n ∈ [66,125]`: `2n − 2 ≡ n − 2 (mod n)`
  with `n − 2 ≥ 64 ≠ 0`; `2n + 2 ≡ 2 (mod n) ≠ 0`.
- Support `[2·66 − 2, 2·125 + 2] = [130, 252]`: entirely `> d_acq = 125`
  (difference-novel and uncontactable for every world) and realizable with
  `A_word = 126` at both edges (`130` via `(65,−65)`-class splits at
  `n = 66`; `252` only via `(126, −126)` at `n = 125`).

**Endpoint splits (exact; kills magnitude and parity features).** A word's
token length ≡ its displacement magnitude (mod 2) — a theorem — so purely
symmetric endpoints would leak per-side parity (YES sides ≡ `n`, NO sides
≡ `n ± 1 (mod 2)`). Each label class therefore mixes two split types:

| Item class | Count | Split type | Endpoints `(a, b)` | Side parity | `|a| = |b|`? |
|---|---|---|---|---|---|
| YES-sym | 4 | symmetric | `(n, −n)` | parity of `n` | yes |
| YES-off | 4 | offset | `(n+1, −(n−1))` | parity of `n+1` | no |
| NO-low-sym | 2 | symmetric | `(n−1, −(n−1))` | parity of `n+1` | yes |
| NO-low-off | 2 | offset | `(n, −(n−2))` | parity of `n` | no |
| NO-high-sym | 2 | symmetric | `(n+1, −(n+1))` | parity of `n+1` | yes |
| NO-high-off | 2 | offset | `(n+2, −n)` | parity of `n` | no |

Per label: YES = 4 parity-`n` + 4 parity-`n+1`, 4 symmetric + 4 offset;
NO = 4 parity-`n` + 4 parity-`n+1`, 4 symmetric + 4 offset — **side
parity, magnitude-equality, and split type are exactly label-balanced.**

**Edge case `n = 125` (exact).** `d = 252` admits only `(126, −126)`, and
`(n+2) = 127 > A_word` bars the NO-high offset. Replacement table at
`n = 125` only: NO-high = 4 × `(126, −126)` (parity even = parity `n+1`,
symmetric); NO-low = 4 × `(125, −123)` (parity odd = parity `n`, offset);
YES = 4 × `(125, −125)` (odd, symmetric) + 4 × `(126, −124)` (even,
offset). Counts per label remain 4 even + 4 odd and 4 symmetric + 4 offset
— balance preserved. (All endpoints `≤ 126`; all differences correct:
`250, 248, 252`.)

**Length matching (exact construction, not the word "matched").** Every
S4 item has **total pair token count `2n + 8`** and per-side padding pairs
assigned as follows (side length = `|displacement| + 2p`):

| Item class | side-1 `p` | side-2 `p` | side lengths | total |
|---|---|---|---|---|
| YES-sym | 2 | 2 | `n+4, n+4` | `2n+8` |
| YES-off | 1 | 3 | `n+3, n+5` | `2n+8` |
| NO-low-sym | 2 | 3 | `n+3, n+5` | `2n+8` |
| NO-low-off | 2 | 3 | `n+4, n+4` | `2n+8` |
| NO-high-sym | 1 | 2 | `n+3, n+5` | `2n+8` |
| NO-high-off | 1 | 2 | `n+4, n+4` | `2n+8` |

(Verification: YES-off sides `(n+1)+2 = n+3` and `(n−1)+6 = n+5`;
NO-low-off sides `n+4` and `(n−2)+6 = n+4`; NO-high-off sides
`(n+2)+2 = n+4` and `n+4`; every row sums to `2n+8`.) Consequently the
**per-side length multiset is exactly label-balanced**: YES realizes
`{n+4, n+4}` ×4 (sym) and `{n+3, n+5}` ×4 (off); NO realizes
`{n+4, n+4}` ×4 (low-off + high-off) and `{n+3, n+5}` ×4 (low-sym +
high-sym). Total lengths are label-constant (`2n+8`); token-count parity
of every full pair is even. All side lengths `≤ n + 5 ≤ 130 ≤ 136` ✓
(edge check at `n = 125`: YES-sym `129,129`; YES-off `128,130`; NO-low
`129,129` / `128,130`; NO-high `128,130` / `129,129` — all ≤ 136).

**Feature-null verifier (required, unit-testable).** Before any panel is
sealed, a deterministic verifier proves over the 16 S4 items of every
world: side-parity pattern, `|a| = |b|` indicator, split type, total
length, per-side length multiset, and padding counts each have **zero
mutual information with the label** (exact count check), and no exposed
syntactic field predicts the label above chance. Verifier failure =
design invalidity.

**Residual scope (unchanged, honest):** S4 still certifies **period plus
novel opposite-corner composition** — a pass is strong; a failure is
censoring, never evidence the learner lacked `n`.

**S2/S5 novelty corrections (replaces those rows' novelty entries).** At
upper-edge worlds some negative differences cross into zone 3 and are
difference-novel there: S2's `d = n + 1` at `n = 125` (`d = 126`), and
S5's `d = n + 2` at `n ∈ {124, 125}` (`d ∈ {126, 127}`). The novelty
columns read "no, except the listed edge worlds (difference-novel
there)"; this world-dependent difficulty is noted and carries **no
anti-lookup authority** — S4 remains the sole tooth.

## A2. One deterministic byte generator after one real entropy draw (replaces v3 §2's keyed public-string streams everywhere)

**Root entropy protocol (normative; no alternatives).** After this
addendum passes its signature check and Kirill signs the S-gate, but
before any development use, a reviewed fail-closed driver obtains
**exactly 32 bytes once** from the OS CSPRNG (`secrets.token_bytes(32)`,
i.e. `getrandom`). It atomically writes and commits an **allocation
transcript** binding: the root bytes, the SHA-256 of this addendum and of
v3, the git HEAD, an ISO-8601 timestamp, the environment fingerprint
(§A5), and a witness attestation line. It **refuses to run if the
transcript path exists**. No redraw, deletion/retry, or alternative seed
is permitted; a failure before the durable commit routes to a **signed
invalidity decision**, never a quiet second draw. Threat model:
**procedural**, not cryptographically independent of the operators.

**Domain PRF stream (exact).** All randomness anywhere in Level 1 derives
from `PRF(domain, counter) = HMAC-SHA256(key = root, message =
encode(domain) || uint64_be(counter))`, where `encode(domain)` is the
concatenation of the domain's components, each as
`uint16_be(byte_length) || UTF-8 bytes`; integer components are rendered
as decimal ASCII. The counter starts at 0 and increments by 1 per digest.
Domains (complete list): `("L1","alloc","dev")`; `("L1","alloc","role")`;
`("L1","alloc","sample", N3)`; `("L1","pool","reserve", d)` per `|d|`
class; `("L1","pool","realize", a, b)` per cell; `("L1","panel", world_slot,
stratum, item)`; `("L1","learner","init", block, replicate, member,
tensor_name)`; `("L1","shortlist", block, arm_slot, step)`;
`("L1","replay", block, arm, replicate, step)`;
`("L1","control","shuffle", world_slot, replicate)`; `("L1","feas")`.

**Uniform integer `U(r)` (exact).** Interpret the 32-byte digest as an
unsigned big-endian integer `x`. Let `limit = floor(2^256 / r) · r`. If
`x ≥ limit`, increment the counter and redraw; otherwise return
`x mod r`. For `r = 1`, return 0 and consume no digest. **Fisher–Yates is
descending** — for `i` from `k−1` down to `1`: `j = U(i+1)`, swap
elements `i, j` — and uses exactly this `U`. The phrase "rejection-free"
is withdrawn.

**Timing (exact).** `D` is drawn before any development use; roles over
`O` are assigned once and conditioned on; `R_h` is drawn **only after the
frozen N3 is computed**, from the already committed root under the
`("L1","alloc","sample", N3)` domain; no allocation is regenerated after
feasibility, censoring, loss, or contrast information exists. Inclusion
probability is then `π_h = n_h/8` under the one-shot randomized
mechanism, and the design-based FPC of §A9 is justified.

## A3. Bit-exact pool and raw-word construction (replaces v3 §3's "locked draw" phrases and the realization prose)

- **Cell orientation and enumeration.** A cell is `{a, b}` written
  canonically `(a, b)` with `a > b` (for `d = 0`, `a = b`). Canonical
  enumeration: ascending `|d| = a − b` from 0 to 125; within a class,
  ascending `a`. This order fixes cell ranks.
- **Reserve count per class (exact).** For class `|d|` with `N_d` cells
  (`N_0 = 253`; `N_d = 253 − d` for `d ≥ 1`): reserve exactly
  `floor(3 · N_d / 10)` cells, selected as the first `floor(3·N_d/10)`
  entries of a descending Fisher–Yates permutation of the class's cells
  (canonical order) under domain `("L1","pool","reserve", d)` — an exact
  unbiased without-replacement sample.
- **Flat index.** Non-reserved cells in canonical order; cell rank `c`
  contributes flat indices `4c, 4c+1, 4c+2, 4c+3` (its four realization
  slots).
- **Raw-word universe.** `W(a)` = all `{R,L}` words with net displacement
  `a` and length `|a| + 2p`, `p ∈ {0,…,5}`, length ≤ 136 (for
  `|a| ≥ 126` the admissible `p` set is truncated accordingly). Canonical
  order: length ascending, then lexicographic with **`R < L`**. Within a
  fixed `(a, ℓ)`, a word is the choice of the `(ℓ + a)/2` R-positions
  among `ℓ`; rank/unrank by the standard combinatorial-number-system
  enumerator over position sets in lexicographic order.
- **Realizations.** For cell `(a, b)`, orientation fixed (`u` realizes
  `a`, `v` realizes `b`). Under domain `("L1","pool","realize", a, b)`,
  draw: `p_u = U(|P_a|)`-th admissible padding (ascending), then
  `u = unrank(U(|W(a, ℓ_u)|))`; likewise `p_v, v`. If the pair `(u, v)`
  exactly duplicates an earlier realization of the same cell, reject and
  redraw (counter advances). Draw exactly 4. For `d = 0` cells and every
  S3 YES item, additionally reject `u = v`. **Availability proof
  obligation:** `|W(a, ℓ)| ≥ 4` for every admissible `(a, ℓ)` with
  `p ≥ 1` (binomial counts; the only singleton is `p = 0`), so 4 distinct
  pairs with `u ≠ v` always exist; enumerated at the S-gate.
- **Reserved-cell consumption (exact).** Panel items consume reserved
  cells in fixed order S1 (items 1–124), S2 (YES, then NO-low, NO-high),
  S3 (YES, then NO), S5 (in its table order); S4 uses zone 3, not
  reserved cells. Each item takes the **lowest-canonical-rank reserved
  cell** matching its required `d` (and any length constraint) not yet
  consumed. Exhaustion is fail-closed design invalidity, with an S-gate
  enumeration proof that it is unreachable at both registry edges.
- **Canonical serialization.** Every committed artifact (pool, panel
  schema, transcripts) uses: `schema_name` + `uint16_be` version; all
  integers big-endian fixed-width (`uint16`/`uint32`/`uint64` as
  declared per field); tokens as single bytes `R = 0x52, L = 0x4C,
  SEP = 0x7C, PAD = 0x5F`; lists length-prefixed (`uint32_be`) and in
  canonical order; hashes = SHA-256 over exactly these bytes.

## A4. Panel metadata surfaces (replaces v3 §4's "byte-identical … hashes" sentence)

1. **Learner/acquisition-visible panel metadata: none.** Nothing of the
   panel — not counts, ids, or existence — is reachable from learner or
   policy code (fail-closed dataflow).
2. **Researcher-visible pre-outcome:** the per-world **ciphertext** and
   **salted content digest** — necessarily different across worlds; they
   bind content and reveal none.
3. **World-independent schema surface (byte-identical across worlds):**
   panel-local ids `0..187`, item counts per stratum
   `(124, 16, 16, 16, 16)`, item order, stratum names, and the **schema
   hash** (over the A3 canonical serialization of this skeleton).
   Content hashes are **removed** from the byte-identical claim.

The sealed ciphertext binds the mapping `local id → (query pair, label,
stratum construction fields)`; the schema surface binds everything else.

## A5. Bit-exact transformer and optimizer (replaces v3 §5's architecture paragraph)

One architecture; no alternatives.

- **Attention is bidirectional** (no causal mask) — this removes the
  causal/left-PAD all-masked-row pathology: every query position attends
  to all non-PAD keys; PAD **keys** are masked (`−∞` before softmax);
  PAD **query** rows compute normally over real keys and are never read
  (readout is position 272, always real under left-padding).
- Input: `x = token_embedding + position_embedding` (273 learned
  positions). Per layer (2 layers):
  `x = x + MHA(LN1(x))`; `x = x + MLP(LN2(x))`. **Final LayerNorm**
  before the 2-logit head. All LayerNorm `eps = 1e-5`.
- MHA: 4 heads × 32; scores `Q·Kᵀ/√32`; softmax over the **key** axis;
  **no Q/K/V/O biases**. MLP: 512, ReLU, **with input and output
  biases**. Head: linear `128 → 2` **with bias**.
- **Initialization (canonical tensor draw order):** `token_embedding`,
  `position_embedding`, then per layer 1..2: `W_Q, W_K, W_V, W_O, W_in,
  W_out`, then `head_W`. Each random tensor: derive
  `seed = uint64_be(PRF(("L1","learner","init", block, replicate,
  member, tensor_name), 0)[0:8])`, seed a fresh CPU `torch.Generator`,
  draw `randn`, scale by `1/√fan_in`. LayerNorm gains 1, offsets 0, all
  biases 0 (no RNG).
- **Environment (enforced):** CPU, float32, `torch 2.9.1+cpu`,
  CPython 3.12.3, `torch.use_deterministic_algorithms(True)`,
  `torch.set_num_threads(1)` and one interop thread; the environment
  fingerprint enters checkpoints and the allocation transcript. A device
  switch is a signed amendment at the feasibility gate, never a silent
  addendum change.
- **No gradient clipping. CE loss, `reduction='mean'`, no label
  smoothing.** AdamW decoupled (`torch.optim.AdamW`), lr `1e-3`
  constant, betas `(0.9, 0.98)`, eps `1e-8`; **two parameter groups**:
  decayed (`weight_decay = 0.01`) = exactly
  `{W_Q, W_K, W_V, W_O, W_in, W_out (both layers), head_W}`;
  non-decayed (`0.0`) = `{token_embedding, position_embedding, all
  LayerNorm gains/offsets, all biases}` — in that declared order.
- **Step ordering:** forward → backward → `optimizer.step()` →
  `optimizer.zero_grad()`; one shared minibatch per step per
  arm-replicate (all 4 members train on the same minibatch), drawn under
  `("L1","replay", block, arm, replicate, step)` as newest pair + 31
  distinct history pairs. Checkpoints at the evaluator cadence (every
  50 steps + 0 + B), containing all members' parameters and optimizer
  moments, every PRF counter, contact history, answered set, and step
  counter; deterministic resume must reproduce state hashes.
- **Replicates:** exactly two, `replicate ∈ {1, 2}`, entering only
  through the PRF domains above; member ids `{0..3}`; arm slots
  `{"active","yoked","random","donor"}`.

If canonical CPU float32 makes the frozen budget infeasible, that is a
finding for the gate-5 non-comparative feasibility check and a signed
amendment — not a silent device switch here.

## A6. Calibration and divergence semantics (replaces v3 §6's Brier rule and §7's finiteness interaction)

- **Calibration:** **per-stratum Brier ≤ 0.10 over every item of the
  stratum**, computed from `p̄` for **all** items — including those the
  classification rule ABSTAINs on (an abstention near 0.5 contributes
  ≈ 0.25 and can only hurt). Global Brier is withdrawn. The conjunction
  with the count rules is satisfiable — worked example: S5 at 14/16 with
  two abstentions (`p̄ = 0.5`): Brier = (14·0.0025 + 2·0.25)/16 ≈ 0.033
  ≤ 0.10 ✓; and a well-calibrated S4 pass: (15·0.0025 + 1·0.30)/16 ≈
  0.021 ✓. Count, ABSTAIN-cap, and confident-lie rules are unchanged.
- **Divergence timing:** if a **complete five-checkpoint qualifying
  window finished before the first non-finite state**, the established
  `T` stands and the later divergence is a mandatory recorded
  diagnostic; if no window completed first, the arm is censored at `B`.
  **Finiteness classification precedes** generic missing-checkpoint
  routing: a missing checkpoint caused by a non-finite trajectory is the
  §7.1 outcome-related route, not a process failure.
- **Re-execution predicate (corrected):** a permitted process
  re-execution must reproduce hashes **through the last committed
  pre-fault checkpoint** — it does not reproduce the transient fault
  itself. Any seal breach remains whole-level invalidity with no
  re-execution.

## A7. Exact leakage protocols (replaces v3 §6's two tolerance lines)

- **Pre-contact encoding — deterministic noninterference gate (the ML
  probe is withdrawn).** Define the exact learner/acquisition-visible
  pre-contact byte bundle: the serialized flat pool (A3), the candidate
  index list, the model/optimizer configuration, and the per-member
  init seeds' *derivation inputs*. After mapping opaque block/world
  handles through **world-independent slot indices** (slot = position in
  the committed schedule, never `n` or pair identity), the bundle must
  be **byte-identical across all development worlds**. Any
  target-`n`-dependent byte, length, hash, or query ordering anywhere in
  the bundle = design invalidity. This is a deterministic verifier, run
  on all 12 development worlds before any scout.
- **Shuffled answers (exact protocol).** Worlds: all 12 development
  worlds. Arm/schedule: the RANDOM-STATIC schedule. Replicates: exactly
  2 per world (24 runs). Permutation: a uniform permutation of the `B`
  oracle answer bits across the transcript positions via descending
  Fisher–Yates under `("L1","control","shuffle", world_slot, replicate)`
  — transcript and query geometry preserved, full `B`, sealed evaluator.
  **Invalidity rule: zero certified solves tolerated**; any solve =
  design invalidity. Scope statement: this is a development
  design-invalidity gate of finite scope, not proof of global leakage
  absence.
- **Parameter shift: diagnostic only** (unchanged).

## A8. Feasibility check measures the scorer (replaces v3 §5's feasibility contract outputs)

The single RANDOM-STATIC development trajectory (endpoint computability)
is kept, **plus a scorer-only microbenchmark**: the ACTIVE scoring path
(`S = 512`, `E = 4`, length-273 forwards) exercised for ≤ 200 scoring
steps on development/dummy inputs. **Exact allowed outputs:** latency
aggregates (count/mean/median/min/max), peak memory, projected wall
time, artifact sizes, finiteness flags, and at most the already
permitted single-arm censoring indicator. **No query, loss, or solve
series is recorded or persisted; no arm contrast exists.** The censoring
indicator can justify only a **binary feasibility-floor amendment** (the
locked architecture/B produced at least one complete development solve,
or did not); it may never tune toward a target solve rate or threshold.
Any change is a signed addendum plus repeat review before S-gate
completion.

## A9. Exact estimator, directional guards, N3 projection (replaces v3 §8's estimator/guard and §9's rule)

**Estimator (all contrasts `X−Y` on the cost scale,
`d_XY(p) = Y_Y(p) − Y_X(p)`, positive favors `X`;
`Y_X(p) = ½ Σ_{k=1}^{2} min(T_{Xpk}, B)`):**

- `Δ̂_XY = Σ_h W_h · mean_{p ∈ S_h} d_XY(p)`, `W_h = 1/3`;
- `s²_{h,XY} = (n_h − 1)^{-1} Σ_{p ∈ S_h} (d_XY(p) − mean_h)²`;
- `v_{h,XY} = W_h² (1 − n_h/8) s²_{h,XY} / n_h`;
  `V̂_XY = Σ_h v_{h,XY}`;
- Satterthwaite `ν_XY = V̂²_XY / Σ_h [v²_{h,XY} / (n_h − 1)]`; zero
  `v_h` terms contribute zero to the denominator; **if all `v_h = 0` at
  `N3 < 24`, the point interval is reported as *estimated zero sample
  variance*, never known-zero population uncertainty**;
- Bonferroni critical value `t_{1 − 0.05/(2·3), ν_XY}` per contrast;
- **census rule at `N3 = 24`:** `n_h = 8`, FPC = 0, intervals collapse
  to points; descriptive of the 24 role-assigned blocks under the
  conditioned seed schedule only.

**Boundary inequalities (exact):** `SUP(X,Y)` iff `L_XY > +60`;
`NI(X,Y)` iff `L_XY > −60`; `NONSUP(X,Y)` iff `U_XY < +60`;
`EQ(X,Y)` iff `L_XY ≥ −60` **and** `U_XY ≤ +60`. Exact equality at a
one-sided margin is unresolved/false for that predicate — never a
success or boundary by narration.

**Determinacy table (replaces the v3 guard; Sol Y3 verbatim):**

| Solve pattern (compared pair) | Eligible | Forbidden | If nothing resolves |
|---|---|---|---|
| neither arm has any event | none | `SUP, EQ, NI, NONSUP` | `INSUFFICIENT` |
| exactly one arm has ≥ 1 event | `SUP, NI, NONSUP` by the interval alone | `EQ` | `INSUFFICIENT` |
| both arms have ≥ 1 event | all four | none | `INSUFFICIENT` |

This admits a strong C1-negative direction when YOKED solves and ACTIVE
does not, while an administrative tie at `B` can never become
equivalence.

**N3 projection (exact, conservative):** compute development block
differences for **all three ordered contrasts** `{A−Y, Y−R, A−R}` under
the frozen endpoint and seed aggregation; per stratum and contrast,
`s²_{dev,h,XY}` over the two development blocks (denominator 1). For
each candidate `N3 ∈ {12, 15, 18, 21, 24}`, `n_h = N3/3`:
`V_proj,XY(N3) = Σ_h (1/9)(1 − n_h/8) s²_{dev,h,XY} / n_h`, with the
matching Satterthwaite `ν` and Bonferroni critical value; projected
half-width `= t · √V_proj`. **Conservative fallback:** any undefined,
non-finite, or exactly-zero `s²_{dev}` from two blocks is replaced for
projection by the bounded-difference maximum `s² = B²` (differences lie
in `[−B, B]`). Choose the **smallest** `N3` whose **maximum projected
half-width over the three contrasts** is ≤ 30. If no candidate through
24 passes: **no lock** — the only routes remain the signed redesign or
`INSUFFICIENT` by design.

## A10. Gate sequence (replaces v3 §11)

| # | Gate | Status |
|---|---|---|
| 1 | v3.1 final signature check (Opus + Sol, bounded to the repairs) | next step |
| 2 | Kirill scope/spec signatures (tokens below) | after 1 |
| 3 | Implementation of the exact generators/model + tests (A2–A5, A7 verifiers) | after 2 |
| 4 | Reviewed one-shot root-entropy/allocation driver + its single execution | after 3 |
| 5 | Optional reviewed non-comparative feasibility execution (A8) | after 4 |
| 6 | Any signed feasibility amendment + re-review | if needed |
| 7 | Comparative development scout | after 5/6 |
| 8 | N3 selection (A9) + preregistration lock | after 7 |
| 9 | Real escrow | after 8 |
| 10 | Outcome driver + execution | after 9, explicit authorization |

No entropy draw, implementation, feasibility run, comparative scout,
lock, escrow, or outcome is authorized by this addendum itself.
