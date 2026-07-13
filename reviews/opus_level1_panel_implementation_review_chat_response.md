Written to `reviews/opus_level1_panel_implementation_review.md`.

## Verdict: `REVISE_LEVEL1_DUMMY_PANEL_IMPLEMENTATION`

The shipped code is **correct and bit-faithful to the signed contract** — no correctness defect, no contract ambiguity, no unauthorized path. The revision is **regression-coverage only**: three test gaps would let a wrong refactor pass, and for an escrow-bound bit-exact artifact those must close before commit.

**Environment:** `pytest` panel+substrate → 14 passed; full suite → 115 passed; `verify_all.py` → VALID/VALID/OK.

**Independent recomputation (all confirmed):** per-stratum YES = 8/8/8/8 (32 total); exactly the three named edge crossings `(124,S5,126)`, `(125,S2,126)`, `(125,S5,127)`; zero reserved reuse; **11 S4 exemptions per-world (n=66/100/125) and pooled with no non-`d` separator** — matching my reviewed count; correct S4 labels; and **no entropy/real-key/escrow/outcome path** anywhere in `level1/` or `scripts/`.

**No Critical findings.** The B-1 collision handling (`panel.py:178–205`) is correct — draws `u` once, holds both pads fixed, advances only the `v`-rank stream, and raises exhaustion against the *true* `word_count(b, padding_v)` universe before the loop, with positive-`v` guaranteeing `|W(v)|≥2`. The feature-null verifier correctly raises on any non-`d` separator and pins exactly 11 exemptions. Domains, zone-3 two-int identities, schema surface (skeleton only, no content byte-identity claim), and the dummy-only PermissionError guards are all faithful.

**Major (missing regression tests — mandatory before commit):**
- **PI-1** — the "lowest-unused global rank" reserved-cell selection is correct but not pinned by any golden `cell_identity` assertion; a tie-break refactor would pass.
- **PI-2** — secret-drawn panel words are only determinism-tested, not golden-hashed; the existing golden coverage stops at the PRF/allocation layer.
- **PI-3** — the S4 feature-null verifier is never tested against a known-bad (parity-XOR) fixture, so a weakened verifier + leaky table could pass. This is the sole scientific guard on S4.

**Mandatory edits (test-only, no source change):** (1) golden `cell_identity` assertions for S1/S2/S3/S5 at `n∈{66,124,125}`; (2) a golden digest of one full panel's `(left,right)` bytes for a fixed dummy key+world; (3) a negative test feeding a separating non-`d` S4 fixture and asserting `ValueError`.

**Committable:** yes, once PI-1–PI-3 are added — source and strengthened tests together. This audit authorizes no entropy, real panel generation, feasibility/scout, N3 selection, lock, escrow, learner trajectory, or outcome. Every negative destination is preserved; nothing is committed.
