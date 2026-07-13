Written to `reviews/opus_level1_v3_1_1_final_check.md`.

## Verdict: `REVISE_LEVEL1_V3_1_1_SCOPE_TEXT`

**The science lands this time.** C1's offset-only reconstruction genuinely removes the v3.1 parity/symmetry XOR at the source (all items offset, every side parity `â¡ n+1`, so symmetry and side-parity are label-constant). I ran an exhaustive joint search over the declared nuisance fields: **the only feature combinations that separate YES from NO are `(padding, ordered-lengths)` and `(padding, total-length)` â and both reconstruct `d` exactly** (`d_rec = d` verified). No `n`-free, non-`d` rule separates the labels. So the shortcut is gone and the certificate now honestly tests operational modulus competence â the permitted resolution the prompt described.

But two **bounded text** defects block signature, neither scientific:

- **F-1 (O1) â the C1 verifier is internally contradictory.** It demands label-identity of "the entire vector and every pairwise/triple sub-combination," yet that vector includes padding and lengths, whose joint reconstructs `d` â which differs by label by design. As written it's unsatisfiable and would reject its own sound construction. This is exactly the contradiction the prompt flagged. Fix: re-scope the verifier to a declared non-structural family, explicitly allowing `d`-reconstructing combinations to differ, while keeping the "no `n`-free non-`d` rule separates" check (which passes).
- **F-2 (O1) â stale counts.** `A_word` 126â128 raises the acquisition cell count 24,003â**24,507** (pool 67,208â68,620, headroom 34.3Ã). The correction reused the old figures while changing the bound they depend on â reconcile, or explicitly decouple the acquisition cap.

**Major (bounded):**
- **F-3 (O2):** C3 requires all real-panel realizations to use the escrow-secret seed, but C2 gives a panel PRF domain only for S4; S1/S2/S3/S5 panel words have no declared secret domain â a reproducibility + confidentiality gap.

**Accepted â closes the prior gaps:** C2 per-stratum/per-pair allocation domains (closes v3.1 MJ-1); S4 secret-seed word ranks and S5 eligibility (MJ-2/mn-2); C3 public-root/secret-panel separation (public root can't derive the panel; dummy seeds can't pass the real-artifact attestation â both correct); C4 model pins (`fan_in`, big-endian seed decode, torch pin, input 277); C5 slot canonicalization; C6 inference corrections; edge realizability at `A_word=128` verified (NO-high at `n=125` uses endpoint 128 exactly).

**O3 (readiness):** the operational certificate proves "recovered contact-anchored `n` sufficient to classify novel `2n` vs `2nÂ±4`," forbids the abstract-period claim, and the three non-consolidated tokens make the irreducible cyclic-world limitation loud enough for an informed signature. **No scientific blocker remains** â only the three bounded text edits, after which the correction is signable. All Level 1 execution stays forbidden; every negative destination preserved; files uncommitted.
