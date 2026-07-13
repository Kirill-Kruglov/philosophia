# Level 1 scientific specification — v3.1.2 bounded signature closure

Status: `CLOSURE_FOR_AUTHOR_SIGNATURE_CHECK`. **v3 + v3.1 + v3.1.1 carry
forward except for the exact sentences superseded below** (the v3.1.1 C1
verifier paragraph, the v3.1.1 C1 "acquisition pool semantics otherwise
unchanged" count implication, and the v3.1.1 C2/C3 panel-domain lines).
v1–v3.1.1 are preserved unchanged. Nothing else is reopened: not the
world, S4 construction, 24-pair frame, adjacent-only detector scope,
operational-certificate meaning, learner, endpoint, estimand, inference
family, selector, or gate order. No code, entropy, datum, feasibility,
scout, lock, escrow, or outcome is created or authorized here.

---

## F-1. Feature-null verifier — satisfiable and honest (supersedes the v3.1.1 C1 verifier paragraph)

**Declared non-structural nuisance fields (exact, closed list):**
symmetry indicator; per-side parity pattern; `||a| − |b||`; offset sign;
padding vector; ordered side lengths; total length.

**The verifier requires:**

1. **Exact label-conditional marginal identity** for every declared
   field above (multiset equality between YES and NO). (These all hold
   for the v3.1.1 C1 construction — proven there.)
2. **Pairwise and triple combinations tested**, with an exact exemption:
   any combination from which `d` is **deterministically reconstructible
   on the S4 support** is exempt from the identity requirement —
   including `(padding vector, ordered side lengths)`,
   `(padding vector, total length)`, and every superset of an exempt
   combination (`d = Σ_sides (ℓ_side − 2·p_side)` on this support).
3. **An emitted dependency proof:** the verifier must output, for every
   exempt combination, the explicit reconstruction map by which it
   determines `d` — never silently classify a combination as exempt.
4. **The exhaustive `n`-free-rule check (retained):** no fixed `n`-free
   rule over any declared non-`d`-reconstructing surface — any tested
   non-exempt field or combination — predicts the S4 label above chance
   (exhaustive over the declared family; this check passes for the
   v3.1.1 construction, as independently confirmed by the X-line).

**Honest statement (normative):** the direct displacement fields
(`(a, b)`, `d`, `|a| + |b|`) and the exempt reconstructing combinations
are the **legitimate operational signal** the certificate tests — their
label-dependence is the structure being measured, not a nuisance-balance
failure. No claim of full raw-feature joint identity is made; such a
claim would be unsatisfiable when labels differ by `d mod n`, by design.
The v3.1.1 padding table and construction are unchanged; the authorial
token and its exact limited meaning are preserved:
`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`.

## F-2. Exact counts under `A_word = 128` (supersedes every carried acquisition-count figure)

Recomputed from the normative v3.1 A3 per-class rule (not from any
global-fraction approximation), with endpoints in `[−128, 128]` and
acquisition support `|d| ≤ d_acq = 125`:

- Class sizes: `N_0 = 257`; `N_d = 257 − d` for `d = 1..125` — the class
  sizes run over the 126 consecutive integers `132..257`.
- **Total acquisition-support cells:**
  `257 + Σ_{d=1}^{125} (257 − d) = 24,507`.
- **Reserved per class:** exactly `floor(3·N_d/10)`;
  `Σ_d floor(3·N_d/10) = (3·24,507 − 571)/10 = 7,295` (the residue sum
  571 = 12 complete decades × 45 + 31 for `N = 252..257`).
- **Non-reserved cells:**
  `Σ_{d=0}^{125} (N_d − floor(3·N_d/10)) = 24,507 − 7,295 = 17,212`.
- **Flat pool at `m = 4`:** `17,212 × 4 = 68,848` realizations —
  **34.424 × B** for `B = 2,000` (34.4× rounded).

**Bounded arithmetic correction, recorded explicitly:** the X-line
check's `68,620 / 34.3×` is the global `round(0.7 · 24,507) × 4`
approximation and is **not compatible with the exact per-class-floor
rule**; it is not normative. The v3 figures (`24,003 / 67,208 / 33.6×`)
were computed for `A_word = 126` and are superseded. The normative
figures are **24,507 cells / 17,212 non-reserved / 68,848 realizations /
34.424 × B**. Exhaustion remains impossible; every dependent normative
sentence in v3 §3 and v3.1.1 C1 is read with these figures. Historical
files remain untouched.

## F-3. Secret-keyed panel-realization domains for every stratum (supersedes the v3.1.1 C2 S4-only panel-domain line; completes C3)

**Common domain skeleton (keyed only by the escrow-secret seed):**

`("L1","panel", world_slot, stratum_id, item_id, side, cell_identity,
purpose)`

where `stratum_id ∈ {"S1","S2","S3","S4","S5"}`; `side ∈ {"u","v"}`;
`cell_identity` = the selected canonical cell/displacement identity (the
reserved cell's canonical rank for S1/S2/S3/S5; the `(a, b)` endpoint
pair for S4); and `purpose ∈ {"pad","rank","order"}` distinguishes the
padding draw, the word-rank draw, and panel-order draws. **Each domain
owns its counter starting at zero; a collision-rejection redraw
increments only that domain's counter; `U(1)` consumes nothing.**
Canonical draw order per item: `u`-side pad, `u`-side rank, `v`-side
pad, `v`-side rank; items in panel-id order within stratum; strata in
order S1–S5.

- **S4 specialization (existing construction preserved):** padding is
  **fixed** by the v3.1.1 C1 table (no `pad` draw is consumed); the
  `rank` draw selects the word by the unbiased `U(|W(a, ℓ)|)` →
  combinatorial unrank; duplicate `(u, v)` pairs are collision-rejected
  within S4.
- **S1/S2/S3/S5:** the *reserved cell selection* remains public and
  canonical (v3.1.1 C2's eligibility-then-lowest-rank rule, reproducible
  from the public reservation geometry), but the **raw realization of
  every panel item is secret-keyed**: `pad` drawn from the item's
  admissible padding set under its existing length/distinctness
  constraints (S3's `u ≠ v`, S5's `≥ 100` lengths/imbalance), `rank`
  drawn as above, collision rejection within the item's stratum.
- **Categorical prohibition:** no public-root pool realization (zone-1
  word pair) may ever be reused as a real panel word; panel words exist
  only under the secret-keyed domains above. Public reservation
  *geometry* stays reproducible; raw real-panel words and their order
  are unreconstructible from the public root.
- **Panel order:** secret-keyed (`purpose = "order"`, world-slot
  domain), as C3 already requires.
- **Dummy/test seed:** dummy panels derive from the declared test-only
  seed and **cannot emit or attest a real artifact** (real-panel
  emission requires the locked escrow environment attestation) —
  unchanged from C3, restated as binding for all five strata.

---

The three-token signature packet and the gate order of v3.1.1 C7 are
unchanged. The next step is a bounded reviewer confirmation of these
three textual repairs; **author signature is not authorized by this
document.**
