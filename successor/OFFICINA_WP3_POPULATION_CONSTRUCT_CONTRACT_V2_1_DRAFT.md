# Officina WP-3 population and construct contract — v2.1 draft (complete replacement)

Status: `WP3_V2_1_DRAFT_FOR_FINAL_CONFIRMATION`. This document wholly
replaces the v2 draft
(`successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_DRAFT.md`,
preserved unedited as review evidence) after the convergent focused
X-line (`REVISE_OFFICINA_WP3_V2`, V2-1..V2-4) and Y-line
(`REVISE_OFFICINA_WP3_V2`, two Major repairs) confirmations. It carries
v2 forward verbatim except for the five bounded corrections its closure
memo names (total oracle wire classifier; governing v1 path and exact
`contract_sha256`; softened T-dev wording; common C-randomization
protocol and corrected OR-2; complete `H_preC` information boundary).
It creates no entropy, world, frame instance, sample, panel, candidate,
datum, ledger event, root, lock, or escrow artifact; T remains
`NOT_ACTIVATED`; no author token is signable from this draft — one
literal bounded confirmation comes first. Learner-side choices remain
fully open for T. No value derives from stopped-line feasibility
outcomes or comparative data (§12).

This is a single self-contained replacement file so the eventual
`contract_sha256` binds one exact committed artifact, not a base +
addendum composition.

---

## 1. Elementary unit, orientation, and typed outcome

- **C unit:** the **unordered adjacent block** `b = {n, n+1}` (§2
  formula). Orientation — which member is the **target** world and
  which the **donor** — is a second-stage design realization, never a
  frame property. The orientation estimand is an explicit author cell
  (OR, §8); the two meanings are never mixed.
- **Q unit:** a single world (no orientation, donor, yoke, pairing, or
  arms) — qualification is non-comparative.
- **Typed terminal observation (fixes Sol-3; type only):** for block
  `b`, arm `a`, the observation is the pair `(X, Δ)` with
  `X = min(T, B) ∈ [0, B]` and `Δ = 1[T ≤ B]` — *certified at or by
  `B`* (`Δ = 1`) is distinct from *not certified by `B`* (`Δ = 0`,
  `X = B`). **WP-3 fixes the observation type only. WP-9 owns the
  certificate, budget `B`, numeric endpoint functional (including any
  restricted-mean functional), arm contrasts, direction, margins, and
  inferential method; no mean or difference is defined until that
  mapping is locked.**
- **Arm set:** `A` is a WP-9 cell containing at least ACTIVE (target
  queries chosen by the target's own learner) and YOKED (target
  answers its own oracle on query geometry produced by an independent
  donor-world ACTIVE learner). All arms of a block run on the same
  target world; the donor world hosts only the donor trajectory.
- **Donor audit (retained loudly, unchanged from v1):** the
  independent adjacent-donor yoke is RETAINED — the C1 estimand needs
  active-shaped geometry *not adapted to the target instance*;
  self-yoking or same-world replicate yoking collapses that meaning.
  Costs named: paired frame, one donor trajectory per block (treatment
  machinery in the operational ledger), adjacent-scale detector scope.
  **Donor transcript capture/replay, `B`, full arm definitions,
  endpoint, and treatment implementation are WP-9** (W3-m1).

## 2. Construct and branch-complete frame formulas

- **Construct** `officina.construct.cyclic-equality.v1`: hidden `Z/n`.
  A **word** is an ASCII string over exactly `{R (0x52), L (0x4C)}`,
  length `0..Λ` (empty allowed; `disp(w) = #R − #L`, `disp(ε) = 0`). A
  **query** is the ordered pair `(u, v)`. The **oracle** returns bit
  `1` iff `disp(u) ≡ disp(v) (mod n)`, else `0` — a pure total
  function of `(n, query)` on the valid query space.
- **`Λ = 2·n_max + 10`** for the selected band (formula frozen; value
  follows CH-1).
- **Generic frame construction (fixes W3-M1 / Sol R1):** let `n0` be
  the selected lower endpoint (CH-1: `26` or `126`); for stratum
  `h ∈ {1..4}` and position `j ∈ {1..5}`,

  ```text
  p(h, j) = 5(h − 1) + j
  b_{h,j} = { n0 + 2·[p(h,j) − 1],  n0 + 2·[p(h,j) − 1] + 1 }
  ```

  40 worlds `[n0, n0 + 39]`, 20 unordered blocks, canonical
  enumeration ascending `p`. Strata are `h`, five blocks each.
- **Partition (CH-2):** C positions `J_C`, Q positions `J_Q`:
  CH-2a (C-rich): `J_C = {1,3,5}`, `J_Q = {2,4}`;
  CH-2b (Q-rich): `J_C = {3,5}`, `J_Q = {1,2,4}`.
  Both worlds of a Q block enter the Q reserve as single-use worlds.
  T holds no frame membership (§5).

### 2a. Complete low-band enumeration (`n0 = 26`) — regression vectors

| h | j | p | block | CH-2a | CH-2b |
|---|---|---|---|---|---|
| 1 | 1 | 1 | {26,27} | C | Q |
| 1 | 2 | 2 | {28,29} | Q | Q |
| 1 | 3 | 3 | {30,31} | C | C |
| 1 | 4 | 4 | {32,33} | Q | Q |
| 1 | 5 | 5 | {34,35} | C | C |
| 2 | 1 | 6 | {36,37} | C | Q |
| 2 | 2 | 7 | {38,39} | Q | Q |
| 2 | 3 | 8 | {40,41} | C | C |
| 2 | 4 | 9 | {42,43} | Q | Q |
| 2 | 5 | 10 | {44,45} | C | C |
| 3 | 1 | 11 | {46,47} | C | Q |
| 3 | 2 | 12 | {48,49} | Q | Q |
| 3 | 3 | 13 | {50,51} | C | C |
| 3 | 4 | 14 | {52,53} | Q | Q |
| 3 | 5 | 15 | {54,55} | C | C |
| 4 | 1 | 16 | {56,57} | C | Q |
| 4 | 2 | 17 | {58,59} | Q | Q |
| 4 | 3 | 18 | {60,61} | C | C |
| 4 | 4 | 19 | {62,63} | Q | Q |
| 4 | 5 | 20 | {64,65} | C | C |

Exact memberships (machine-recomputed; the rule governs, these vectors
are regression checks):

- **CH-2a:** C blocks `p ∈ {1,3,5,6,8,10,11,13,15,16,18,20}`; Q worlds
  `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` (the v1 printed
  list is **withdrawn as a transcription error** — it overlapped the C
  frame in 12 of 16 worlds; W3-C1 / Sol-1).
- **CH-2b:** C blocks `p ∈ {3,5,8,10,13,15,18,20}` = `{30,31}, {34,35},
  {40,41}, {44,45}, {50,51}, {54,55}, {60,61}, {64,65}`; Q worlds
  `{26,27,28,29,32,33,36,37,38,39,42,43,46,47,48,49,52,53,56,57,58,59,62,63}`.
- **High band (`n0 = 126`):** the same `p(h,j)` formula uniquely
  determines all memberships (e.g. CH-1b+CH-2a Q worlds
  `{128,129,132,133,138,139,142,143,148,149,152,153,158,159,162,163}`);
  no hand-copied list is authoritative anywhere.

### 2b. Branch-complete design table (fixes W3-M1 / Sol R2, R5)

| Quantity | CH-2a (C-rich) | CH-2b (Q-rich) |
|---|---:|---:|
| C blocks per stratum `N_h` | 3 | 2 |
| total C blocks `N_C` | 12 | 8 |
| Q worlds per stratum `q_h` | 4 | 6 |
| total Q worlds | 16 | 24 |
| stratum weight `W_h = N_h/N_C` | 1/4 | 1/4 |
| C inclusion probability `π_h = n_h/N_h` | `n_h/3` | `n_h/2` |
| sampling FPC `1 − n_h/N_h` | `1 − n_h/3` | `1 − n_h/2` |
| census degeneracy | `n_h = 3` | `n_h = 2` |
| admissible point-estimation `n_h` | 1..3 | 1..2 |
| claim-capable `n_h` without a special `n_h = 1` method | 2..3 | 2 |
| analysis coefficient per sampled block | `W_h/n_h` | `W_h/n_h` |

**Small-stratum rule (fixes Sol-5/R5):** `n_h = 1` supports a
design-unbiased point estimate but **no** within-stratum
sample-variance estimate (undefined, not zero). Claim-bearing inference
with `n_h = 1` requires a WP-9-locked bounded/randomization-exact
method that does not substitute zero variance; otherwise every
non-census stratum requires `n_h ≥ 2`. Census FPC zero is a **sampling
fact about the selected finite frame only** — it does not remove
orientation randomization (under OR-1) or learner-seed randomization
unless the claim conditions on their realized values.

## 3. `officina.frame.v1` — exact canonical bytes (fixes W3-M2)

One canonical-JSON document per the WP-2 canonical library (ASCII-only,
lexicographically sorted keys, minimal separators). **Exact fields:**

```text
"band":            {"n_max": <int>, "n_min": <int>}
"blocks":          array ascending p of
                   {"assignment": "C"|"Q", "h": <int>, "j": <int>,
                    "members": [<int>, <int>] ascending, "p": <int>}
"c_block_ps":      array ascending <int>   (derived; regression)
"ch1_token":       <selected CH-1 token string>
"ch2_token":       <selected CH-2 token string>
"construct":       "officina.construct.cyclic-equality.v1"
"contract_sha256": <hex SHA-256 of the signed WP-3 contract bytes>
"lambda":          <int>  (= 2·n_max + 10)
"q_worlds":        array ascending <int>   (derived; regression)
"schema":          "officina.frame.v1"
"scientific_outcome": false
"strata":          {"blocks_per_stratum": 5, "count": 4}
"t_dev_bands":     [[10, 25], [166, 205]]
```

**`contract_sha256` (fixes V2-3):** the value is the SHA-256 of the
**exact committed bytes of
`successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md`**,
the same file named and hash-pinned in the future WP-3 author-signature
record. The relation is **acyclic**: this contract file contains no
frame hash, so the frame document depends on the contract but never the
reverse; the selected CH-1/CH-2 token strings appear independently in
the frame JSON (`ch1_token`, `ch2_token`). Frame hash = SHA-256 over
the canonical frame bytes.

The future WP-4 generator is **bound to the signed contract hash and
the two selected author tokens — never to a hand-copied list**: it
recomputes every membership from §2's rule, verifies the embedded
derived arrays, and **refuses to emit** on any mismatch. **Mandatory
pre-emission machine checks:** `Q ∩ C = ∅` (as world sets);
`Q ∪ C = [n0, n0+39]`; cardinalities and per-stratum balance (`q_h`,
`N_h` per §2b); band disjoint from `[66,125]` and from both T-dev
bands. Any failure = fail-closed refusal, no partial emission (W3-C1
check, item 8).

## 4. Oracle wire grammar and capability boundary

- **Total ordered wire classifier (fixes V2-1).** The oracle is a pure
  total function whose input is a raw byte string; every raw input
  yields **exactly one** of three typed refusals or one valid answer,
  under this fixed, normative precedence — the first matching clause
  governs and no later clause is consulted:

  1. **`MALFORMED_QUERY_STRUCTURE`** — if the raw bytes are not the
     exact WP-2 canonical-JSON encoding of one object whose keys are
     exactly `u` and `v` (no missing key, no extra key, no duplicate
     key) with both values JSON strings. This clause catches invalid
     JSON, non-canonical JSON, non-object input, missing/extra/
     duplicate keys, and non-string `u`/`v` — **structure is decided
     before any content inspection.**
  2. **`MALFORMED_QUERY_BYTE`** — if structure is valid but either
     decoded string contains any byte outside ASCII `{R = 0x52,
     L = 0x4C}`.
  3. **`MALFORMED_QUERY_LENGTH`** — if structure and alphabet are valid
     but either side's length exceeds `Λ`.
  4. **Answer** — otherwise, the canonical JSON integer `0` or `1` from
     the oracle rule.

  The order is normative: a query that is **both** over-length **and**
  contains an illegal byte classifies as `MALFORMED_QUERY_BYTE` (clause
  2 precedes clause 3); any structurally invalid encoding is
  `MALFORMED_QUERY_STRUCTURE` before content is examined. The empty
  word `ε` is a valid string (`disp(ε) = 0`), so `{"u":"","v":""}` is a
  valid query answered normally. Refusal bytes are the exact canonical
  JSON objects `{"refusal":"MALFORMED_QUERY_STRUCTURE"}`,
  `{"refusal":"MALFORMED_QUERY_BYTE"}`, `{"refusal":"MALFORMED_QUERY_LENGTH"}`;
  a refusal carries no bit and mutates no state.

- **Raw decoding vs the mathematical oracle.** Clause 1 is **raw wire
  decoding** — the boundary between an arbitrary byte string and a
  well-formed `(u, v)`. The mathematical oracle is defined only on the
  decoded pair of `{R, L}` displacement words; it never sees raw bytes
  and never returns a refusal itself (refusals are the classifier's,
  emitted before the oracle rule is evaluated). This separation makes
  oracle transcripts (used for hashing and the yoke) byte-reproducible
  across two independent implementations.

- **`PAD (0x5F)` and `SEP (0x7C)` are not construct objects** (fixes
  W3-M3): they are learner/panel *encoding* constants owned by the
  learner side and WP-9; they never appear in oracle input and are
  never oracle-visible. A raw input containing `0x5F` or `0x7C` inside
  a `u`/`v` string routes to `MALFORMED_QUERY_BYTE` by clause 2 like
  any other non-`{R,L}` byte.

- **Capability-gated construction (fixes W3-M4; contractual
  invariant):** there is **no public arbitrary-`n` oracle or world
  constructor.** World/oracle instantiation exists only through
  surface-capability objects: the **T capability** constructs oracles
  **only for signed T-dev-band moduli** (band check inside the
  constructor, fail-closed); **Q and C capabilities do not exist until
  their gates** — Q worlds arise only from sealed post-freeze attempt
  roots (WP-6), C worlds only from the post-lock secret root (WP-10).
  Contractual invariant: *no Officina surface can expose an oracle for
  a frame or reserve modulus before that surface's root exists.*
  Enforcement of the invariant is reviewed WP-4 code and tests
  (constructor requires the capability object; tests assert T-surface
  refusal on frame/reserve moduli); the alternate-import, forged-
  provenance, and symlink routes are already discharged by the
  reviewed WP-1/WP-2 deny-by-default path policy and provenance
  registry.

## 5. T-development geometry (fixes W3-M5; invariant rule, no author cell)

**T-dev bands are the fixed set `[10, 25] ∪ [166, 205]` under both
CH-1 branches**, with the named, branch-coherent meaning:

- the set is disjoint from **both** candidate frame bands (`[26,65]`,
  `[126,165]`) and from the quarantined predecessor registry
  `[66,125]` — so no CH-1 outcome, and no future amendment confusion,
  can ever place a T world in a scientific band;
- under CH-1a the **near band** `[10,25]` is *contiguously adjacent
  below* the frame (`25 | 26`); under CH-1b the **near band**
  `[166,205]` is *contiguously adjacent above* it (`165 | 166`); the
  distal band in each branch is a scale-stress surface;
- **named extrapolation property (softened per V2-4):** the near band
  abuts **one edge** of the selected frame, so a candidate developed
  on it and later qualified on a frame-scale world still crosses the
  frame's full internal scale range (e.g. under CH-1a, from `[10,25]`
  to an upper-frame block near `65`); qualification therefore tests
  generalization across **both modulus identity and scale** within the
  registered surface, and the distal band exists for deliberate
  scale-stress engineering. No claim is made that the design avoids
  scale transfer; the near band controls only the *lower* edge.

T world creation is open within these bands (registry-logged,
capability-gated per §4); T supports no population claim.

## 6. C target measure (branch-complete)

Stratified SRSWOR of `n_h` blocks from the `N_h` C-frame blocks per
stratum, realized once by the post-lock secret C root (WP-10), with
`π_h`, `W_h`, FPC, and census degeneracy exactly per §2b for the
selected CH-2 branch. `n_h` is a WP-9 cell bounded by §2b's
claim-capability rows. The C design realization additionally includes
the orientation realization per the selected OR cell (§8), under the
common C-randomization protocol of §8.

**Claim boundary (fixes Sol R9/12):** a valid C claim generalizes to
the **selected registered C frame** of the emitted `officina.frame.v1`
and nothing wider. **The deterministic partition and public finite
frame are conditioned-on design facts. C weights generalize only over
the selected registered C frame and do not adjust for candidate
selection, public-frame tailoring, Q depletion, the deterministic Q/C
partition, or the exclusion of Q, T, predecessor, and unenumerated
worlds.** Forbidden language (design invalidity): "worlds like these,"
"cyclic groups in general," "the construct class," any i.i.d./
superpopulation phrasing, any extension to non-frame moduli — **and,
absent a later WP-6 candidate-admissibility rule, any narration that a
result shows the learner "learned the modulus," "learned the
construct," "represents the group," or "validates a small-learner /
contact mechanism"** (W3-M6, item 10). The WP-6 admissibility rule is
not chosen here.

## 7. Q reserve, per-stratum depletion, and spendability

- **`P_Q`:** the frozen Q reserve of the selected branch (16 or 24
  worlds, `q_h` per stratum). Attempt `ℓ` draws its sample from the
  **remaining** reserve by its sealed post-freeze root: the
  attempt-indexed measure `P_{Q,ℓ}` is defined **conditional on
  `H_{<ℓ}`, the remaining-world registry, the frozen candidate/stack,
  and the attempt id** (WP-6 must state its guarantee under every
  admissible depletion history).
- **Depletion constraints (replaces the v1 product shortcut; fixes
  Sol-7/8, R6, W3-m2):** if attempt `ℓ` consumes `m_{ℓ,h}` worlds of
  stratum `h`, then

  ```text
  Σ_ℓ m_{ℓ,h} ≤ q_h   for every stratum h,   and   Σ_{ℓ,h} m_{ℓ,h} ≤ |Q|
  ```

  with `q_h = 4, |Q| = 16` (CH-2a) or `q_h = 6, |Q| = 24` (CH-2b).
  Every charged launch — including typed-invalid launches — consumes
  its worlds, attempt id, cap slot, and error allocation; **nothing
  replenishes a world or alpha.** If WP-6 requires full stratum
  coverage per attempt (`m_{ℓ,h} ≥ 1 ∀h`), the absolute launch
  ceilings are **4** (CH-2a) and **6** (CH-2b); any pooled or
  staggered coverage design is WP-6's to define **with** its
  family-guarantee proof under depletion. The v1 "two-world sample /
  eight launches" example is **withdrawn**. `E2 = 12` is a
  candidate-*registration* ceiling, never a promise of twelve Q
  attempts.
- **Transport premise (replaces "exchangeability"; fixes Sol-6, R7):**
  the Q→C relation is an **author-accepted fixed-frame
  target-competence transport premise**: that a valid Q pass by the
  frozen candidate/stack on fresh reserve worlds, under the WP-6
  competence rule covering the locked strata/support, makes spending
  the C experiment reasonable on its **target side**. It is **neither
  design-identified nor tested by Q** — no probability law makes fixed
  public Q moduli exchangeable with distinct fixed C blocks; it is a
  declared relevance assertion requiring its **own author token**
  (§9). What it licenses: C spend. What it does not identify or
  license: any C-frame mean, treatment effect, donor/yoke validity,
  orientation behavior, or evidentiary statement. **Single-world Q
  cannot validate comparative machinery** — Q has no orientation,
  donor, yoke, pairing, or arms; therefore **separate non-outcome
  engineering validation of orientation, donor/yoke, persistence, and
  arm-construction machinery is required before C execution** (its
  numerics and implementation belong to WP-4 tests and the pre-C
  engineering gate of WP-9/WP-10, not here).
- **Information boundary (fixes item 18; completed per Sol Major 2).**
  `H_preC` retains and hashes the **complete** charter-required Q
  attempt, validity, released-output, stopping, depletion, and
  promotion history. For downstream routing and design identity, Q may
  contribute only the mechanical fact that the first valid `Q_PASS`
  occurred and the exact automatically promoted candidate/stack
  identity; neither fact is C evidence. The competence binary is used
  only for that routing; it, Q-world identities, responses, estimates,
  variances, depletion history, and every other scientific Q quantity
  may not tune C sample size, endpoint, margins, population, or
  analysis and may not enter C evidence. Predeclared label-free
  resource telemetry may inform engineering caps only. The complete
  history is conditioned on and auditable; it is not erased merely
  because its quantities are forbidden from C planning and evidence.

## 8. Orientation estimand — author cell OR (fixes Sol-2, R3)

The base block is unordered; exactly one of the following defines the
finite-population quantity. For a WP-9-locked numeric contrast, write
`D_b(r)` for the block contrast when orientation `r` selects the
target.

**Common C-randomization protocol (inserted per Sol Major 1).** The
block sample and every orientation realization are derived from the
same post-lock secret C root under **distinct typed PRF domains** whose
exact byte encodings are locked and reviewed at WP-10. The joint
mapping must make the stratum sample SRSWOR and **independent of**
orientation randomization; under OR-2 this requires
`Pr(S_h = s | r) = 1/binom(N_h, n_h)` for every eligible stratum subset
`s`. Under OR-1, the sample is derived under the sample domain and the
fair bits for sampled blocks under the independent orientation domain.
Under OR-2, the complete orientation vector is derived and sealed
**first** under the orientation domain, then sample membership is
derived under the sample domain. Both components become one durable,
sealed, **non-redrawable** `C_design_realization_id` before any C
trajectory; any failure never authorizes a redraw. WP-3 owns
independence, order, and non-redraw; WP-10 owns the exact PRF
domain-byte tags and implementation after lock.

**OR-1 — orientation-averaged two-stage estimand.**
Target `θ = Σ_h W_h (1/N_h) Σ_{b∈F_h} D̄_b`, `D̄_b = [D_b(0)+D_b(1)]/2`.
Design: SRSWOR of blocks (sample domain) + independent fair orientation
bit `R_b ~ Bernoulli(1/2)` per sampled block (orientation domain), per
the common protocol above.
Estimator `θ̂ = Σ_h (W_h/n_h) Σ_{b∈S_h} D_b(R_b)` — design-unbiased.
**Variance obligation:** the design variance has two components,
`Σ_h W_h² [(1−f_h) S²_{D̄,h}/n_h + (n_h N_h)^{-1} Σ_{b∈F_h} σ²_{R,b}]`
with `σ²_{R,b} = [D_b(0)−D_b(1)]²/4`; one observed orientation per
block **cannot estimate the second term** — WP-9 must lock a valid
route (conservative bound from the bounded outcome, replicated
orientations on a declared subset, or a randomization-exact method).
At block census the first term is zero; **the second is not** — census
never removes orientation randomness. Serialization: per-sampled-block
bits, ascending `p`, sealed with the C design realization.
Resource consequence: wider intervals or partially doubled block cost.
Token: `I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND`.

**OR-2 — realized-orientation conditional finite-frame estimand
(recommended; corrected per Sol Major 1).**
After the scientific lock and C-root creation, and **before** C sample
membership or any trajectory, the full-frame orientation vector
`r ∈ {0,1}^{N_C}` (ascending block `p`) is derived, sealed, and bound
into `C_design_realization_id` under the common protocol above. The
target is `θ(r) = Σ_h W_h (1/N_h) Σ_{b∈F_h} D_b(r_b)`, and the public
claim is **explicitly conditional on that sealed vector**. Conditional
on `r`, `θ̂(r) = Σ_h (W_h/n_h) Σ_{b∈S_h} D_b(r_b)` is design-unbiased,
with `Var[θ̂(r) | r] = Σ_h W_h² (1−f_h) S²_{D(r),h}/n_h`; each sampled
block reveals its **orientation-specific contribution, not the
full-frame estimand**. Ordinary SRSWOR variance estimation is available
subject to §2b's small-stratum rule, and census FPC zero is exact for
`θ(r)` subject to the locked learner-seed scope.
Realization/freeze: post-lock, before any C trajectory; never earlier;
never redrawn. Resource consequence: none beyond the base design.
Scope cost: the claim conditions on one realized orientation vector
(as it already conditions on `H_preC`, `d*`, `s*`, `L*`); the sealed
`C_design_realization_id` binds `r` without replacing the pre-C
`selection_scope_id`.
Token: `I_SELECT_OFFICINA_ORIENTATION_CONDITIONAL_FIXED_VECTOR_ESTIMAND`.

**Recommendation (not a selection):** OR-2 — it is exactly estimable
with the frame's small strata, adds no unidentifiable variance
component, and its conditionality is of the same kind the charter
already prices; OR-1 remains fully available for an author who wants
the orientation-marginal quantity and accepts its variance route.
Refusal of both = WP-3 blocked pending redesign. Neither is selected
here; **never claim census FPC removes orientation or learner-seed
randomness under either option.**

## 9. Multiplicity, seeds, and ownership

- **Multiplicity (replaces v1's rule; fixes Sol-9, R8):** a
  claim-bearing stratum or interaction statement is assigned **before
  data to the multiplicity family of the claim it supports**: C1 for
  C1 contact claims, the C2–C4 family for those cascade claims, C5 for
  path-credit claims, and the separately controlled C6 family for any
  inferential C6 annotation. Unregistered and post-hoc subgroup claims
  are forbidden; locked descriptive summaries are non-inferential and
  may carry no p-values, claim-capable intervals, threshold language,
  directional emphasis, or subgroup narration.
- **Seeds:** the world side is seed-free; learner-seed scope lives
  inside `L*` at WP-9 (fixed-conditioned or locked seed law), and no
  FPC or census statement removes seed randomness unless the claim
  conditions on realized seeds.
- **Ownership table (complete):**

  | Cell | Owner |
  |---|---|
  | CH-1 band, CH-2 split, OR estimand, transport premise | **Kirill**, at WP-3 signature |
  | generic frame formulas, enumeration, schema/bytes, `Λ` formula, wire grammar, capability invariant, T-dev bands, `W_h`, `π_h`/FPC forms, depletion inequalities, small-stratum rule, typed observation `(X,Δ)`, common C-randomization protocol, forbidden language | **this contract** (frozen at signature) |
  | Q caps, `δ_Q`/alpha spending, competence null/certificate/horizon/aggregation, per-attempt schedule `m_{ℓ,h}` and its coverage design + family-guarantee proof under depletion, entropy custody/attestation, breathing-check numerics, candidate admissibility (optional) | **WP-6** |
  | certificate content, `B`, endpoint functional, arm set and treatment implementation, donor transcript capture/replay, margins, alphas, `n_h`, `n_h = 1` special method (if any), OR-1 variance route (if OR-1), exact PRF domain-byte tags for the common C-randomization protocol, seed law, C escrow environment | **WP-9 / WP-10** |
  | pre-C non-outcome engineering validation of orientation/donor/yoke/persistence/arm machinery | WP-4 tests + the pre-C engineering gate (existence required by this contract) |

## 10. Author cells (mutually exclusive; none selected here)

| Cell | Options (exact tokens) | Recommendation | Refusal destination |
|---|---|---|---|
| CH-1 band | `I_SELECT_OFFICINA_FRAME_BAND_LOW` (`n0 = 26`, `Λ = 140`) / `I_SELECT_OFFICINA_FRAME_BAND_HIGH` (`n0 = 126`, `Λ = 340`, ≈2.4× token scale) | LOW — word-length/resource planning under the signed 168 h envelope; **not** an expected-success argument; no scale information exists in the non-citable censored binaries | refusing both = WP-3 blocked; new band = loud amendment |
| CH-2 split | `I_SELECT_OFFICINA_SPLIT_C_RICH` (12 C blocks / 16 Q worlds; full-coverage ceiling 4 launches) / `I_SELECT_OFFICINA_SPLIT_Q_RICH` (8 / 24; ceiling 6) | C_RICH — confirmatory frame richness; the launch arithmetic is **conditional on the WP-6 coverage design** and promises nothing | refusing both = WP-3 blocked |
| OR estimand | `I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND` / `I_SELECT_OFFICINA_ORIENTATION_CONDITIONAL_FIXED_VECTOR_ESTIMAND` | CONDITIONAL (§8) | refusing both = WP-3 blocked pending redesign |
| Q→C transport premise | `I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE` (dedicated token; not subsumable into generic contract acceptance) | accept — without it Q cannot license C spend | named refusal = the three-surface spend architecture is unusable as designed → charter-level redesign decision |

T-dev geometry requires **no** token (§5's invariant rule removed the
cell). The consolidated packet after the focused final confirmation:
`I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT` + exactly one CH-1 token +
one CH-2 token + one OR token + the transport token. The contract
token does not silently subsume any of the four load-bearing cells.

## 11. WP-4 implementability

WP-4 (only after the final confirmation of this v2.1 and Kirill's
complete signature) can implement without touching any scientific
result: the pure oracle with the §4 total wire classifier and typed
refusals; the frame generator bound to contract hash + selected tokens
with §3's pre-emission machine checks; capability-gated T-dev world
construction with registry logging; Q-consumption registry hooks.
Mechanically impossible for WP-4/T: instantiating a frame/reserve
oracle (no capability), reading or reconstructing future Q/C realized
units (their roots do not exist), emitting a frame document that fails
any machine check, or binding to anything but the signed contract
bytes.

## 12. Provenance attestation

Every number here derives from: band disjointness from the quarantined
registry (hygiene); equal-size scale strata (arithmetic); the
`Λ = 2·n_max + 10` certificate-scale formula (a design pattern from
signed pre-outcome predecessor documents, not from outcomes); the
signed T envelope (author resource commitment); and the reviewers'
branch-complete corrections. The stopped line's v1/v2 records are
binary, single-fixture, non-citable, and contain no modulus-, scale-,
or frame-relevant information; no value is selected from them or from
any comparative datum. No qualification, contrast direction, or
scientific outcome is predicted anywhere in this contract.

---

This contract moves no scientific claim. The predecessor line remains
immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; Officina's T and Q
remain permanently non-citable for C1–C6; S is unavailable; only a
valid, independently locked C execution may ever move an Officina
claim — within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope.
