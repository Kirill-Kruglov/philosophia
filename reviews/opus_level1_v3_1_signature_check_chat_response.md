Written to `reviews/opus_level1_v3_1_signature_check.md`.

## Verdict: `REVISE_LEVEL1_V3_1_ADDENDUM`

The prompt's suspected XOR is real and disqualifying. A5–A9 are genuine bit-level closures, but **A1 relocates the S4 leak rather than repairing it.**

**Critical — C-1 (O1): S4 is separated by a joint XOR of two readable features.** I reconstructed the full 16-item table at general even `n`, general odd `n`, and the `n=125` special table. In every case:
- Every **marginal** feature (split-type, side-parity, magnitude-equality) is perfectly balanced 4/4 — the addendum's own claim holds.
- But `label = XOR(split, side_parity) XOR parity(n)` classifies all 16 items exactly.

All three inputs are available to a **difference-lookup** learner: `split` (`|a|=|b|?`) and `side_parity` (`|a| mod 2`) are byproducts of the `net` skill, and `parity(n)` is known to any learner that found `d=n` to pass S2. So a 2-bit XOR aces S4 with **no period representation and no `d=2n` extrapolation** — the teeth are still defeated. The A1 feature-null verifier checks only **marginal** MI, and the XOR of two zero-MI features carries full MI, so the verifier passes the broken panel. The leak is structural: symmetric items force `parity` to track the label.

**The repair is not one paragraph.** It needs (a) a **joint** feature-null verifier (identical label-conditional multiset of the full nuisance vector), (b) an **offset-only** reconstruction leaving only `d` to separate the labels, and (c) an honest re-scope — since `d=|a|+|b|` is padding-invariant and readable, the clean S4 certifies "recovers `n` and checks a novel multiple," which does not separate from difference-lookup-plus-arithmetic (my v3 CR-B, now unavoidable). If Kirill won't accept that scoped meaning, it escalates to a scope/world decision, not a silent edit.

**Major (bounded, one-paragraph each):**
- **MJ-1 (O2):** the `alloc/dev`, `alloc/role`, `alloc/sample` domains carry no stratum component and A2 doesn't fix counter-continuity across strata → two implementers get different allocations.
- **MJ-2 (O2):** S4 raw words are under-specified — A1 fixes displacement and padding length but not *which* word of that `(a, ℓ)`; route through the A3 realize draw or specify the rank.

**Landed — do not reopen:** A5 closes the entire model/optimizer contract (bidirectional attention removes the all-masked-row NaN; final LN + eps; canonical init draw order; deterministic CPU/float32 environment); A6 per-stratum Brier + divergence timing + re-execution predicate; A7 the slot-alpha-renamed noninterference gate + exact shuffled protocol; A8 scorer microbenchmark; A9 the estimator/determinacy/N3 machinery. A2/A3's PRF, `U(r)` rejection sampler, cell order, and rank/unrank are exact.

Gate-1 substrate stays eligible except allocation bookkeeping (blocked on MJ-1); everything downstream waits for a re-reviewed v3.1.1. **No entropy draw and no execution authorized**, adjacent-only scope and all negative destinations preserved. Files remain uncommitted.
