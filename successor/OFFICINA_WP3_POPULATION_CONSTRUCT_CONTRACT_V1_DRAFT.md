# Officina WP-3 population and construct contract — v1 draft

Status: `WP3_DRAFT_FOR_XY_REVIEW`. Governing base: the signed charter
(v2 + v2.1), `CHARTER_SIGNATURE.md`, `AUTHOR_SELECTIONS_V1_SIGNATURE.md`
(finite-frame C interpretation; sealed post-freeze Q root owned by
WP-6; `officina`, same repository), and the WP-1/WP-2 closure
(`CLOSED_FOR_WP3_DRAFTING_ONLY`). This is the **world-side** contract
for the eight objects of charter §3. It is a draft: it creates no
entropy, world, panel, sample, candidate, datum, lock, root, escrow
artifact, ledger event, or scientific claim; T remains `NOT_ACTIVATED`;
no real T world may exist until this contract is X/Y-reviewed and
signed by Kirill (including the two bounded author cells CH-1/CH-2,
§10). Learner-side choices remain fully open for T.

Predecessor artifacts (worlds, roots, pools, panels, checkpoints,
constants, outcomes) are quarantined and unused; predecessor *design
patterns* from signed pre-outcome documents are reused as patterns
only, with fresh constants. No value below derives from stopped-line
feasibility outcomes or comparative data (§9.8).

---

## 1. Object 1 — elementary unit, roles, potential outcomes

- **C unit (inferential block):** an ordered pair of distinct frame
  worlds `b_p = {n_lo(p), n_hi(p)}` with a **role orientation bit**
  `r(b) ∈ {0,1}` selecting which member is the **target** world and
  which the **donor** world. The orientation is *realized per surface*
  (C: by the post-lock secret root; never earlier) and is part of the
  design, not of the frame.
- **Q unit:** a **single world** (no roles, no arms) — qualification is
  non-comparative single-learner competence (§5).
- **Treatment potential outcomes (type only; numerics WP-9):** for
  block `b`, arm label `a ∈ A` — where `A` is fixed by the WP-9
  scientific specification and must contain at least `ACTIVE` (queries
  chosen by the target's own learner) and `YOKED` (target answers its
  own oracle on query geometry produced by an independent donor-world
  ACTIVE learner) — the outcome is the right-censored
  budget-to-certified-competence variable
  `Y_a(b; d*, s*, L*) ∈ [0, B] ∪ {censored-at-B}` under the locked
  endpoint `L*`. All arms of a block run on the same target world
  (paired design); the donor world hosts only the donor ACTIVE
  trajectory.

**Donor audit (required; retained loudly).** The independent
adjacent-donor yoke is **RETAINED**. Reasons: (i) the C1 estimand is
*online responsiveness to one's own state* — YOKED must receive
active-shaped geometry that is **not** adapted to its own world
instance; (ii) self-yoking or same-world replicate yoking hands the
YOKED learner geometry optimized for its exact instance, collapsing
the contrast's meaning (and its direction is not even conservative,
since instance-adapted geometry can either help or mislead);
(iii) the paired adjacent-scale donor gives near-matched query-scale
statistics by construction. Consequences: the C unit is a pair (the
frame is enumerated in pairs); every C block costs a donor trajectory
(treatment machinery in the operational ledger, as chartered); the C1
detector scope is honestly "adjacent, near-matched-scale donors" — a
scoped detector, exactly as in the signed claim semantics.

| Field | Value/type | Serialization | Owner / freeze | Amendment | Visible T/Q/C |
|---|---|---|---|---|---|
| block id | `officina.block.v1:p`, `p ∈ 1..20` | canonical JSON string | WP-3, at signature | new estimand, loud amendment | public |
| role bit `r(b)` | realized per surface | one bit under the surface's root domain | rule WP-3; C value post-lock root | any earlier realization = design invalidity | C: sealed until unsealing |
| arm set `A` | ⊇ {ACTIVE, YOKED}; exact set WP-9 | WP-9 spec | WP-9, at lock | WP-9 amendment rules | public at lock |
| outcome type | right-censored BTCC on `[0,B]` | WP-9 | WP-9 numerics | WP-9 | public at lock |

## 2. Object 2 — construct generator, support, exclusions

- **Construct** `officina.construct.cyclic-equality.v1`: hidden cyclic
  group `Z/n`. A **word** is a string over alphabet `{R, L}`
  (displacements +1, −1); `disp(w) = #R − #L`. A **query** is an
  ordered pair of words `(u, v)` with `0 ≤ |u|, |v| ≤ Λ`. The **oracle**
  answers the bit `[disp(u) ≡ disp(v) (mod n)]`. The oracle is a pure
  total function of `(n, query)` on the query space; a malformed query
  (length > Λ, illegal byte) is a **typed refusal**, never `false`.
- **Word-length cap (formula normative):** `Λ = 2·n_max + 10` for the
  signed band (CH-1) — sized so that later WP-9 certificate items at
  the `2n` scale are expressible with slack; the value follows the
  band, the formula freezes here.
- **Serialization:** token bytes `R = 0x52`, `L = 0x4C`, `SEP = 0x7C`,
  `PAD = 0x5F` (WP-2 canonical library conventions; fresh constants,
  no predecessor artifact read).
- **Contact surface:** the world side defines only `(n, oracle, query
  space)`. Pools, shortlists, acquisition policies, and panels are
  learner-side or WP-9 objects — deliberately **not** world objects, so
  T's openness never touches the world contract.
- **Support (author cell CH-1, §10):** a single contiguous band of
  moduli, disjoint from the quarantined predecessor registry
  `[66, 125]`. Recommended `[26, 65]` (§10). Everything below is
  written for the recommended band and scales by the stated formulas
  under CH-1.
- **Exclusion rules:** no modulus outside the signed bands may ever be
  a frame, Q-reserve, or T-dev world; no modulus in `[66, 125]` may be
  generated by any Officina surface for any purpose; frame ∩ T-dev =
  ∅ by construction.

| Field | Value/type | Serialization | Owner / freeze | Amendment | Visible |
|---|---|---|---|---|---|
| construct version | `officina.construct.cyclic-equality.v1` | version string in every artifact | WP-3 signature | new estimand | public |
| oracle semantics | as above, total, typed refusal | pure function; no state | WP-3 signature | new estimand | public |
| `Λ` | `2·n_max + 10` (=140 for `[26,65]`) | integer in frame doc | WP-3 signature | new estimand | public |
| support band | CH-1 | integer interval in frame doc | Kirill at WP-3 signature | new estimand | public |
| token bytes | fixed above | WP-2 canonical | WP-3 signature | design invalidity if drifted | public |

## 3. Frame enumeration (normative under CH-1 = `[26, 65]`)

- **Worlds:** `n ∈ [26, 65]`, 40 worlds, id `officina.world.v1:n`.
- **Blocks:** `p ∈ 1..20`, `b_p = {24+2p, 25+2p}` — `(26,27)` … `(64,65)`;
  ascending-`p` is the canonical enumeration order.
- **Strata:** `h(p) = ⌈p/5⌉`, four scale strata:
  `h1: n ∈ [26,35]`, `h2: [36,45]`, `h3: [46,55]`, `h4: [56,65]`,
  five blocks each. Within-stratum position `j(p) = p − 5(h−1) ∈ 1..5`.
- **Partition by within-stratum position (author cell CH-2, §10;
  recommended Split-1):**
  - `j ∈ {1, 3, 5}` → **C frame**: 12 blocks, 3 per stratum
    (`p ∈ {1,3,5, 6,8,10, 11,13,15, 16,18,20}`);
  - `j ∈ {2, 4}` → **Q reserve**: 8 pairs = **16 single-use Q worlds**,
    4 per stratum
    (`n ∈ {28,29,32,33, 40,41,44,45, 50,51,54,55, 60,61,64,65}`);
  - **T holds no frame membership.** T development uses only the
    **T-dev bands** `n ∈ [10, 25]` and `n ∈ [166, 205]` (open
    generation, unbounded count, registry-logged), never a frame or
    reserve modulus.
- **Frame document:** the enumeration above is serialized as one
  canonical-JSON `officina.frame.v1` document; its SHA-256 binds every
  later generator, driver, and spec. Two independent implementations
  must reproduce it byte-identically from this contract alone.

The **four easily conflated things, separated:** (i) the *registered
finite frame* — the 12 C blocks above, public; (ii) the *deterministic
partition rules* — the `j`-position rules above, public; (iii) the
*post-lock secret C root value and realized C membership/orientation* —
which **must not and do not exist yet** (WP-10; their protocol is fixed
in §4); (iv) *WP-9 scientific numerics* — endpoint, arms, margins,
alphas, confirmatory `n_h`, seed law — owned later, absent here.

## 4. Object 4 — finite-frame C target measure

- **Design:** stratified simple random sampling **without replacement**
  of `n_h` blocks from the `N_h = 3` C-frame blocks of each stratum
  `h ∈ {1..4}`, drawn once by the post-lock secret C root (WP-10),
  together with each sampled block's orientation bit `r(b)`.
- **Inclusion probability:** `π_h = n_h / 3`, equal within stratum by
  SRSWOR; `n_h ∈ {1, 2, 3}` is a WP-9 cell.
- **Stratum weights:** `W_h = 3/12 = 1/4` exactly (equal-size strata).
- **Analysis weights and FPC:** design-based stratified estimation with
  weight `W_h / n_h` per sampled block and finite-population correction
  `(1 − n_h/3)` per stratum; **census degeneracy:** `n_h = 3` for all
  `h` gives FPC = 0 and a descriptive statement about the 12-block
  frame — the exact degenerate case of the signed interpretation.
- **Claim scope (exact):** a valid C result speaks about the registered
  12-block C frame of `officina.frame.v1` — nothing narrower is hidden,
  nothing wider is claimed: not the Q reserve, not the T-dev bands, not
  the excluded predecessor registry, not "cyclic worlds in general,"
  and not any superpopulation (§8).

| Field | Value/type | Owner / freeze | Amendment | Visible |
|---|---|---|---|---|
| design | stratified SRSWOR + orientation bit, post-lock root | WP-3 signature (protocol); WP-10 (root value) | protocol change = new estimand | protocol public; realization sealed |
| `N_h` | 3 per stratum | WP-3 signature | new estimand | public |
| `W_h` | 1/4 exact | WP-3 signature | new estimand | public |
| `π_h`, FPC | `n_h/3`, `(1 − n_h/3)` | form WP-3; `n_h` WP-9 | WP-9 rules | public at lock |

## 5. Object 5 — Q target measure and the Q→C relation

- **`P_Q`:** the uniform stratified measure over the 16-world Q
  reserve (4 per stratum). A Q attempt's sample is drawn from the
  reserve by the attempt's sealed post-freeze root (WP-6), **globally
  without replacement across all attempts** — a consumed Q world never
  returns (append-only consumption registry, WP-2 machinery).
- **Structural bound imposed on WP-6 (named, arithmetic):** total
  launches × per-attempt sample size ≤ 16, and the WP-6 sampling rule
  must be stratum-balanced or explicitly scale-spanning; with the
  recommended Split-1, e.g. a 2-world scale-spanning sample supports at
  most 8 launches ever. WP-6 owns the numbers; it cannot exceed the
  reserve.
- **Q→C relation (transport, declared, not tested):** Q worlds and C
  blocks are interleaved members of the *same* enumerated band and
  strata, generated by the *same* versioned construct, differing only
  in modulus value within a stratum's scale band. The declared design
  premise is **within-stratum exchangeability under
  `officina.construct.cyclic-equality.v1`**: single-learner competence
  on fresh Q worlds of stratum `h` is informative about target-world
  solvability on C blocks of stratum `h`. This premise is what makes a
  future valid `Q_PASS` license **spending** the C experiment. It is a
  spendability license only: a Q pass is a gate fact, is never
  scientific evidence, never enters any C estimate, and is permanently
  non-citable for C1–C6.
- **Unit mismatch, stated:** Q units are single worlds; C units are
  paired blocks. Q licenses the *target-side competence floor*; the
  comparative structure (donor, yoke, arms) is exercised for the first
  time in C — by design, since Q must remain non-comparative.

## 6. Object 6 — interaction estimand, heterogeneity, multiplicity

- The confirmatory estimand is the selection-conditional block-level
  contrast of charter §1c, instantiated on this frame: design-weighted
  stratified means of `Y_a(b; d*, s*, L*)` differences over the sampled
  C blocks, under the WP-9-locked arm set, endpoint, and analysis.
- **Heterogeneity/stratum summaries:** per-stratum block-difference
  summaries are **descriptive annotations only**. If the WP-9 spec
  wishes any stratum-level or interaction statement to be
  claim-bearing, it must register it inside the C1 multiplicity family
  before data (charter §7); otherwise no such statement may be made.
- **Multiplicity ownership:** reaffirmed as charter §7 — C1/contact
  family, C2–C4 cascade, C5, inferential C6, and proof composition are
  owned pre-data by their specs. WP-3 adds exactly one membership rule:
  any claim-bearing use of this frame's strata beyond the primary
  contrast belongs to the C1 family.

## 7. Object 7 — learner seeds at this layer

WP-3 fixes **status only**: the world side is seed-free (the oracle is
deterministic; frame membership and partition are deterministic; the
only world-side randomness is the C design realization, owned by the
post-lock root, and Q sampling, owned by sealed attempt roots). Learner
seeds appear solely inside `L*`: whether they are fixed and conditioned
on or drawn from a locked seed law is a WP-9 cell, unconstrained by
this contract, and the potential-outcome notation `Y_a(b; d*, s*, L*)`
carries the seed scope inside `L*`. Nothing here narrows or selects a
WP-9 seed numeric.

## 8. Object 8 — interpretation and forbidden language

The signed interpretation is instantiated: **C is a probability sample
from the fixed finite frame of §3** with locked `π_h`, weights, and
FPC, census-degenerate at full sampling. Its generalization boundary is
the registered 12-block frame — exactly.

**Forbidden language (design invalidity in any Officina scientific
artifact):** "worlds like these," "cyclic groups in general," "the
construct class," "i.i.d. draws from the generator," any superpopulation
phrasing, any extension of a C statement to the Q reserve, the T-dev
bands, the predecessor registry, or unenumerated moduli, and any
statement that the frame choice makes success likely. The design-based
claim needs no i.i.d. assumption and none may be smuggled in.

## 9. Required scientific checks

1. **Frame richness for C1–C5 (no success claimed):** the frame class
   supports the C1 skeleton (paired adjacent blocks, chosen vs yoked
   contact); its construct class extends to the later programme —
   unseen families for C2 are other bands or constructs, representation
   transfer (C3) has canonical Cayley-graph duals for cyclic groups,
   ledger/path objects (C4/C5) attach to the learner side and are
   frame-agnostic. Later levels own their own frames; nothing here
   promises any contrast succeeds.
2. **Donor audit:** §1 — RETAINED with reasons and costs.
3. **T cannot alter the freeze:** the frame, partition, `P_C`, `P_Q`,
   and estimand form are content-addressed in this signed document; T
   surfaces hold no write path (deny-by-default path policy +
   provenance registry); T generates worlds only in the T-dev bands
   under T domains, and the WP-4 generator must take the
   `officina.frame.v1` hash as input and **refuse on mismatch**. Any
   post-signature change to generator, support, strata, or weights
   defines a new estimand and requires a loud pre-data amendment.
4. **Design-based scope:** §4 and §8 — stratified SRSWOR, exact
   `π_h`/FPC, census degeneracy, no i.i.d. or superpopulation reading.
5. **Q→C spendability:** §5 — declared within-stratum exchangeability
   premise; a pass licenses spending, never evidences.
6. **Leakage audit (each threat named and routed):**
   - *Generator leakage:* the oracle is a pure function of `(n, query)`;
     generator code holds no realized secrets; dummy fixtures use
     test-only seeds (WP-2). Violation → design invalidity.
   - *Finite-frame memorization / parameter encoding:* the support
     bounds are public and unavoidable — any frozen candidate knows the
     40 candidate moduli. The load-bearing boundary is **realized-draw
     unpredictability**: Q draws exist only post-freeze (charter §2),
     C membership only post-lock (§4). Partition publicity narrows a
     symbolic eliminator's search from 40 to 16/24 moduli — a marginal,
     **named residual**, immaterial to gradient-class learners and
     dominated by the next item.
   - *Construct shortcuts:* a deliberately engineered
     divisibility-testing candidate could pass Q by symbolic
     elimination. Under the signed selection-conditional claim this is
     **admissible** — the C claim would then be about that design,
     honestly scoped. If Kirill wishes to guard the programme's
     small-learner spirit, the control point is a **WP-6
     candidate-admissibility rule** (e.g., architecture-class
     constraints in the manifest) — flagged as an optional author
     consideration for WP-6, deliberately **not** legislated here.
   - *Predecessor-world reuse:* forbidden by the signed path policy and
     provenance registry; no Officina surface reads predecessor
     artifacts; engineering fixtures are declared, T-only,
     non-promotable (currently none).
   - Each unrouted occurrence at run time → design invalidity,
     fail-closed.
7. **Ownership of remaining numeric cells:**

   | Cell | Owner |
   |---|---|
   | support band (CH-1), Q/C split (CH-2) | **Kirill, at WP-3 signature** |
   | frame members, strata, `N_h`, `W_h`, partition rule, `Λ` formula, T-dev bands | **this contract** (frozen at signature) |
   | Q caps, `δ_Q`, spending rule, per-attempt sample size/structure, competence certificate numerics, entropy custody, breathing-check numerics | WP-6 (bounded by §5's reserve arithmetic) |
   | endpoint, arm set beyond the skeleton, budget `B`, margins, alphas, confirmatory `n_h`, seed law, C escrow environment | WP-9 / WP-10 |
8. **Provenance attestation:** every number above derives from: band
   disjointness from the quarantined registry (hygiene), equal-size
   scale strata (arithmetic), the `Λ = 2·n_max + 10` certificate-scale
   formula (a *pattern* from signed pre-outcome predecessor design,
   not from any outcome), and the signed T envelope (resource
   commitment). The stopped line's v1/v2 records are binary,
   single-fixture, non-citable, and contain no modulus-, scale-, or
   frame-relevant information; **no value here is selected from them or
   from any comparative datum.**

## 10. Author cells (mutually exclusive; do not default)

**CH-1 — frame scale band.**

| Option | Token | Scientific consequence | Resource consequence |
|---|---|---|---|
| **CH-1a (recommended):** `n ∈ [26, 65]` | `I_SELECT_OFFICINA_FRAME_BAND_LOW` | 40 worlds, certificate scale `2n ≤ 130`, `Λ = 140`; disjoint below the quarantined registry | shorter words; lighter per-step cost within the signed 168 h envelope |
| CH-1b: `n ∈ [126, 165]` | `I_SELECT_OFFICINA_FRAME_BAND_HIGH` | 40 worlds, certificate scale `2n ≤ 330`, `Λ = 340`; disjoint above the registry | ~2.4× token scale; substantially heavier trajectories |

Recommendation rationale (world-side only): the low band keeps
certificate words expressible at modest `Λ`, maximizing what the fixed
T envelope can explore; the direction is **not** licensed by the
stopped line's censored binaries, which carry no scale information —
provenance is the `Λ` formula plus the signed resource envelope.

**CH-2 — Q/C split of the 20 blocks (within-stratum positions).**

| Option | Token | C frame | Q reserve | Consequence |
|---|---|---|---|---|
| **CH-2a (recommended):** Q = `{2,4}`, C = `{1,3,5}` | `I_SELECT_OFFICINA_SPLIT_C_RICH` | 12 blocks (3/stratum) | 16 worlds | richer confirmatory frame; WP-6 launches ≤ 16 / sample-size |
| CH-2b: Q = `{1,2,4}`, C = `{3,5}` | `I_SELECT_OFFICINA_SPLIT_Q_RICH` | 8 blocks (2/stratum) | 24 worlds | more qualification headroom (≤ 24 / sample-size) toward the E2 = 12 candidate envelope; coarser C frame (`π_h ∈ {1/2, 1}`) |

Recommendation rationale: the confirmatory frame is the line's entire
claim surface; qualification headroom of ~8 launches (2-world samples)
under CH-2a is compatible with serial first-valid promotion, where most
registered candidates never need a launch.

Both cells are bounded to WP-3; every other value in this contract is
normative at signature.

## 11. WP-4 implementability and no-reuse mechanics

WP-4 can implement, without touching any scientific result: the
construct oracle (pure function + typed refusal); the `officina.frame.v1`
document generator and hash verifier (refuse-on-mismatch); T-dev world
creation restricted to the T-dev bands with registry logging under the
deny-by-default path policy; and the Q-consumption registry hooks
(append-only, WP-2 primitives). Mechanically impossible for WP-4/T:
reading or reconstructing future Q/C realized units — Q draws require
sealed post-freeze roots that do not exist (WP-6), C membership
requires the post-lock root that must not exist (WP-10), and no T
surface may generate a frame or reserve modulus (band check,
fail-closed). Canonical IDs, enumeration order, version strings, and
the frame-document hash make two independent implementations agree
byte-for-byte or fail loudly.

---

This contract moves no scientific claim. The predecessor line remains
immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; T/Q remain
permanently non-citable for C1–C6; only a valid, independently locked C
execution may ever move an Officina claim, within its
selection-conditional scope. After bounded X/Y review, the signature
packet is: `I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT` plus exactly one
CH-1 token and one CH-2 token.
