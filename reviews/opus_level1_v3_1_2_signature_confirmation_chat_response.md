Written to `reviews/opus_level1_v3_1_2_signature_confirmation.md`.

## Verdict: `REVISE_LEVEL1_V3_1_2_BOUNDED_TEXT`

**F-1 and F-2 are fully closed. F-3 leaves two one-sentence bit-level gaps.**

**F-1 â confirmed closed.** The re-scoped verifier keeps marginal identity, exempts `d`-reconstructing combinations (with emitted reconstruction maps), and retains the exhaustive non-`d` check. I re-ran the exhaustive scan over every marginal/pair/triple of the declared 7-field family: **all 11 separating combinations reconstruct `d`** (the two base pairs `(pad,olen)`, `(pad,tot)` plus their nine supersets) â so the exemption is complete and no non-exempt combination separates. The `"no fixed n-free rule"` phrase is executable over the **closed declared family** (finite, decidable), not an unbounded universal claim â the correct formulation.

**F-2 â confirmed exact.** Recomputed from the per-class floor: **24,507 / 7,295 (residue sum 571) / 17,212 / 68,848 = 34.424ÃB**. This correctly supersedes both the old v3 `A_word=126` figures and â as I explicitly acknowledge â my own prior `68,620/34.3Ã`, which was the global-70% approximation and is not compatible with the per-class-floor rule. The normative number is 68,848.

**F-3 â structurally closed, two residual ambiguities:**
- **B-1 (collision redraw):** "increments only that domain's counter" has no single referent for a `(u,v)` *pair* collision â multiple owned domains (`u`/`v` Ã pad/rank) are involved, so two implementations could redraw different sides and produce different sealed panels.
- **B-2 (`cell_identity` encoding):** the A2 serialization covers integers/strings but not the S4 `cell_identity = (a,b)` *pair* â one composite component vs two integer components changes the PRF input.

I supplied the two exact bounded replacement sentences (redraw only the `v`-side rank domain, holding `u` and pads fixed; serialize `cell_identity` as canonical rank for S1/S2/S3/S5 and as two consecutive integer components `a` then `b` for S4). Structurally F-3 is otherwise correct: all S1âS5 panel realizations and ordering are secret-keyed and unreconstructible from the public root, public reservation geometry stays reproducible, and dummy seeds can't attest a real artifact.

On adoption of B-1 and B-2, the three repairs are complete and the document is confirmable. **No author signature and no execution is authorized** by this `REVISE`; every negative destination is preserved; files remain uncommitted.
