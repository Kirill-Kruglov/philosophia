Written to `reviews/opus_level1_v3_1_4_panel_review.md`.

## Verdict: `REVISE_LEVEL1_V3_1_4_PANEL_TEXT`

The amendment adopts PG-1–PG-4 exactly and the table enumerates correctly — but the exhaustion challenge is **confirmed real**, requiring one bounded edit.

**Blocking — PV0 (`p_v=0` singleton defeats B-1):** I verified that `|W(disp, |disp|)| = 1` at `p_v=0` for every displacement — a singleton (the all-`R`/all-`L` reduced word). Since B-1 holds `u` and both pads fixed and redraws only `v`, a collision at `p_v=0` is unresolvable → design invalidity. This bites exactly where drawn pads meet a rejection: **S3·YES** (`u≠v`) and the **zone-3 repeated-corner edge groups** (S2·NO-high at `n=125`; S5·dn+2 at `n∈{124,125}`), where four items share one corner cell. §5's "exhaustion impossible" justification silently assumed `p_v≥1` and is false for the `p_v=0` draw the amendment permits.

**Confirmed correct (not reopened):**
- **PG-1–PG-4 adopted exactly** — global zero-based ids, `item_id` binding, global-rank reserved selection, zone-3 corner rule with the B-2 two-integer identity, S5 `{3,5,7,9}` + eligibilities, loudly withdrawn "matched" claims, verbatim S4.
- **Table verified** for every `n∈[66,125]`: 188 items, 32 YES/156 NO, correct labels, and exactly the three named crossings and no others.
- **`item_id` unambiguous** (global zero-based; one byte stream).
- **S4 already exhaustion-safe** — its fixed paddings give `p_v∈{1,2,3}`, never 0.

**Exact bounded repair** (changes no label, count, cell, or claim): a new §4 clause 4d drawing `p_v` from the **positive** admissible set (`{1..5}`) for the rejection-bearing groups (S3·YES and the zone-3 repeated-corner edges), keeping `p_u` and all non-rejection groups on `{0..5}`; plus a corrected §5 justification. I verified sufficiency — `p_v=1` gives `|W(v)|=2` for the S3·YES worst case (disp 0, enough for `v≠u`) and 65–66 for the edge corners (enough for four distinct pairs). S4's fixed table already supplies `p_v≥1`, so it stays verbatim.

This `REVISE` authorizes no signature or execution; with clause 4d adopted the amendment is bit-exact and returns for bounded confirmation before its own author token. Every negative destination is preserved; files remain uncommitted.
