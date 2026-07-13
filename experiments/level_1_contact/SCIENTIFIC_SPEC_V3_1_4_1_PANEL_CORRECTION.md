# Level 1 scientific specification — v3.1.4.1 panel exhaustion correction

Status: `CLOSURE_FOR_FINAL_XLINE_CONFIRMATION`. v3.1.4 carries forward
unchanged except for the exact clause and justification below. This correction
adopts Opus PV0 verbatim, changes no label, count, cell, stratum role, threshold,
or claim, and creates or authorizes no code, entropy, panel, data, lock, escrow,
or outcome.

## 1. Positive `v` padding for rejection-bearing drawn-pad groups

Add as v3.1.4 clause 4d:

> For the `v`-side draw of every **rejection-bearing drawn-pad group** —
> S3·YES, and any zone-3 repeated-corner group (S2·NO-high at `n = 125`;
> S5·dn+2 at `n ∈ {124, 125}`) — `p_v` is drawn from the **ascending
> positive admissible padding set** (`p_v ∈ {1..5}`, truncated by the
> 138-token cap) via `U(|set|)`; `p_u` and all non-rejection-bearing groups
> keep the full `{0..5}` rule of §4a. This guarantees `|W(v)| ≥ 2`, so
> B-1's `v`-rank redraw always reaches a novel `v`.

S4 carries forward verbatim: its fixed table already has `p_v ∈ {1,2,3}`.

## 2. Corrected collision-exhaustion justification

This sentence replaces v3.1.4 §5's earlier informal word-set-size
justification:

> Exhaustion is impossible **because clause 4d forces `p_v ≥ 1`** on every
> rejection-bearing `v`-draw, giving `|W(v)|` at least 2 (S3·YES,
> displacement 0) and at least 65 (the `±63/±64` corners) — far more than
> the ≤ 4 rejections any group can require; the earlier "astronomically
> larger" wording, which implicitly assumed `p_v ≥ 1`, is replaced by this
> explicit bound.

The exhaustive dummy-only verifier additionally asserts, for every registry
world, that every rejection-bearing `v` draw uses the positive admissible set
and that its `|W(v)|` exceeds the number of rejections required by that group.
Failure remains pre-execution design invalidity.

The author token remains `I_ACCEPT_LEVEL1_V3_1_4_PANEL_CONTRACT`; when signed
after final confirmation, it accepts v3.1.4 together with this v3.1.4.1
correction.
