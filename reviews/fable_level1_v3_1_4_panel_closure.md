# Fable 5 — Level 1 v3.1.4 panel-amendment closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`.
Historical specs v3–v3.1.3 and `SCIENTIFIC_SPEC_SIGNATURES.md` remain
untouched. Input: Opus panel-generator readiness audit
(`REVISE_LEVEL1_PANEL_GENERATOR_CONTRACT`, PG-1–PG-4 plus its bounded
repair table), grounded against the implemented neutral substrate
(`src/philosophia/level1/{config,serialization,world,pool}.py`), whose
faithfulness Opus confirmed and which is not reopened.

## Verdict

**READY_FOR_LEVEL1_PANEL_AMENDMENT_REVIEW**

The amendment adopts PG-1–PG-4 with the exact closures required: one
normative per-group table pinning count, global and local ids, exact
ordered `d`, zone, cell selection, `cell_identity` components, padding/
eligibility, label, collision registry, and realization order for
S1/S2/S3/S5, with S4 verbatim. Two independent implementers can now
derive identical panel bytes for every `n ∈ [66, 125]`, including the
three zone-3 edge crossings the signed contract could not construct.

## 1. PG dispositions

| Finding | Disposition | Amendment |
|---|---|---|
| **PG-1** — zone-3 edge items unconstructible (`d = 126` at `n ∈ {124,125}`, `d = 127` at `n = 125`; confirmed at code level against `world.cells_for_difference`) | **Adopted**: uniform zone-3 rule — deterministic corner `(⌈d/2⌉, −⌊d/2⌋)`, two-consecutive-integer `cell_identity` (B-2's S4 branch explicitly extended to every zone-3 panel item), secret-realized, never a public word; exact corners `(63,−63)` and `(64,−63)` tabled | §2, §3 |
| **PG-2** — S5's fourth group had no exact `d` | **Adopted**: exact ordered `{3, 5, 7, 9}` — canonical, `n`-independent, each `< 66 ≤ n` hence never `= n` or `n+2`; eligibility `\|a\| ≥ 95 ∧ \|b\| ≥ 95`, fixed `(5,5)` padding | §3, §4 |
| **PG-3** — S2 "length-matched" unsatisfiable (parity of total length ≡ `d`) | **Adopted**: withdrawn loudly, with the generic S3/S5 "matched" wording; replaced by exact drawn/fixed padding rules; stated loudly that S2/S3/S5 carry no anti-lookup authority and that S4's sole tooth is untouched | §4 |
| **PG-4** — selection determinism gaps (reserved ordering; repeated-difference consumption; `u ≠ v` scope; S5 eligibility predicates) | **Adopted**: eligibility-filter → global A3 canonical rank order → lowest unused rank, consumed globally in ascending zero-based panel id; S1 repeats thereby unique; `u ≠ v` as an explicit S3·YES rejection under the stratum registry; S5 predicates made exact (`\|a\| ≥ 95`; `abs((\|a\|+10) − \|b\|) ≥ 60`; `\|a\|,\|b\| ≥ 95`) with the word "achievable" eliminated | §1, §2, §4 |

**Registry-vs-B-1 consistency (named, per the mandate):** the
within-stratum accepted-pair registry is consistent with the signed B-1
availability claim. Cross-item collisions are structurally impossible
for distinct-cell items (a raw pair determines its cell); the registry
is load-bearing exactly where four items share one corner cell (the
zone-3 edge groups) and for S4's shared endpoint pairs — where the
corner word sets dwarf four draws, so exhaustion remains impossible. No
correction to B-1 was needed.

## 2. Exact superseded phrases

1. v3 §4 S2 row: "NO items length-matched to YES" — withdrawn (PG-3).
2. v3 §4 S3/S5 rows: the generic "matched" wording — withdrawn.
3. v3 §4 S5 row: "4 × locked `d ∈ [3,125] \ {n, n+2}` at length ≥ 100"
   — superseded by the exact ordered `{3, 5, 7, 9}` with `(5,5)`
   padding and `≥ 95` eligibility.
4. v3.1.1 C2's S5 eligibility sentence ("`\|displacement\| ≥ 90` where
   `≥ 100` lengths are required") — superseded by the exact per-group
   predicates of §4.
5. v3.1.2 F-3's "S1/S2/S3/S5 secret-keyed realization … under their
   existing length and distinctness constraints" — the constraints are
   now the exact tabled predicates.
6. v3.1.2 F-3's draw-order sentence ("items in panel-id order within
   stratum; strata in order S1–S5") — superseded by the equivalent but
   exact ascending **global zero-based panel id** rule, which also
   fixes the F-3 `item_id` PRF component as that global id.
7. v3.1.1 C1's implicit reserved-cell-only assumption for S2/S5 at the
   edge worlds — superseded by the zone-3 corner rule (PG-1).

Everything else in v3–v3.1.3, including S4's construction, meaning,
verifier, and tokens, carries forward verbatim.

## 3. Edge and count verifications

- Zone crossings occur exactly three times: S2·NO-high `d = 126` at
  `n = 125`; S5·dn+2 `d = 126` at `n = 124` and `d = 127` at `n = 125`
  — corners `(63, −63)`, `(63, −63)`, `(64, −63)`; all realizable
  (`|a| ≤ 64 ≤ 128`) and all `> d_acq = 125` (never contactable).
- Global ids: S1 `0..123`, S2 `124..139`, S3 `140..155`, S4 `156..171`,
  S5 `172..187`; schema surface `188 = 124+16+16+16+16` unchanged.
- S5 fixed paddings respect the 138-token cap for every eligible cell
  (`|a| + 10 ≤ 138` since `|a| ≤ 128`); S5·d0/locked sides `≥ 105`;
  S5·dn imbalance predicate is a pure inequality on the cell, no
  "achievable" language anywhere.
- `{3, 5, 7, 9}` never collides with `n` or `n + 2` on the registry
  (`n ≥ 66`), and reserved classes at those `d` hold ≈ 76 cells each —
  ample after S1's one-or-two consumptions.

## 4. Tokens

The three signed author tokens
(`I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`,
`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`,
`I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC`) **remain valid for all unchanged
science**. Because this amendment changes panel-item construction for
`n ∈ {124, 125}` and pins S5's locked `d`, it requires **its own author
token after bounded Opus and Sol confirmation**. Proposed token:

`I_ACCEPT_LEVEL1_V3_1_4_PANEL_CONTRACT`

(alternative: a named rejection reopening the panel contract review;
never a silent fold into the existing spec token).

## 5. Requested bounded confirmations

**Opus:** confirm the amendment lands your PG-1–PG-4 repair table with
the closures as specified — global-id determinism, the zone-3
two-integer extension, the exact S5 predicates, the withdrawn wording,
and the registry-consistency note — with no reopening of S4 or any
closed choice. **Sol:** confirm the panel-contract changes are
statistically inert (labels, counts, strata roles, endpoint, inference,
and surfaces unchanged; only construction determinism and two edge-world
item sources changed) and that the exhaustive dummy-only verifier
obligations are sufficient enforcement. No design element is reopened by
either request.

## 6. Confirmation

No code was written; no panel (real or dummy) was generated; no entropy
was drawn; no datum, feasibility run, comparative scout, N3 selection,
lock, escrow, or outcome was created. S2/S3/S5 explicitly carry no
anti-lookup authority; S4 remains the sole operational-certificate
tooth, textually unchanged; a certificate failure remains censoring,
never evidence the learner lacked `n`; and every signed negative
destination is preserved verbatim.
