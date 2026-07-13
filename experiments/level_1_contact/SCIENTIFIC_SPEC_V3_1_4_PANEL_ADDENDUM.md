# Level 1 scientific specification — v3.1.4 panel-contract amendment

Status: `LOUD_PRE_DATA_AMENDMENT_FOR_REVIEW`. This amendment makes the
**non-S4 panel builder bit-exact**, adopting Opus PG-1–PG-4 and the
bounded repair table with the exact closures below. **S4 carries forward
verbatim.** Nothing else is reopened: not the scientific scope,
population, endpoint, inference, selector, learner, or gate order.
Historical specs (v3–v3.1.3) and the signed record
(`SCIENTIFIC_SPEC_SIGNATURES.md`) remain untouched; this amendment
supersedes only the phrases listed in its closure memo. No code, panel,
entropy, datum, feasibility/scout, lock, escrow, or outcome is created
or authorized here. Because it changes panel-item construction for
`n ∈ {124, 125}` and pins S5's locked `d`, it requires **its own author
token** after bounded X/Y confirmation (closure memo §4).

---

## 1. Global panel ids and the PRF `item_id` (removes the id ambiguity)

- **Global panel ids are zero-based and fixed:** S1 `0..123`,
  S2 `124..139`, S3 `140..155`, S4 `156..171`, S5 `172..187`.
- Stratum-local ids (1-based) appear below **only as table labels**.
- The F-3 `item_id` PRF component is **always the global zero-based
  panel id**.
- Panel serialization (A4 schema surface) and the secret panel order
  bind these same global ids.
- Draw and reserved-cell consumption proceed in **ascending global
  panel id** across the whole panel of the current world (S4 consumes
  no reserved cells; its draws occur at ids 156–171 in sequence).

## 2. Reserved-cell selection (uniform rule; fixes PG-4a/b)

For every reserved-cell item: filter the world-independent reserved
cells by the item's **exact eligibility predicate** (§4), order the
survivors by their **global A3 canonical cell rank**, and consume the
**lowest unused rank**. "Unused" is global across the current world's
entire panel, and consumption occurs in ascending global panel id — so
repeated-difference S1 items are unique and deterministic, and no cell
is consumed twice. A reserved item's `cell_identity` is **that one
global canonical integer rank**.

**Zone-3 items** (every required `d > 125`): deterministic corner
`(a, b) = (⌈d/2⌉, −⌊d/2⌋)`; `cell_identity` is **two consecutive
integer components `a`, then `b`** — v3.1.3 B-2's S4 branch is hereby
extended explicitly from S4 to **every** zone-3 panel item. Zone-3
items are secret-realized under the F-3 panel domains and are **never
a public word**.

## 3. The normative table (S1/S2/S3/S5; S4 verbatim from v3.1.1 C1 + v3.1.2)

| Group | Count | Global ids | Local ids | Exact ordered `d` | Zone | Cell selection / `cell_identity` | Padding / eligibility | Label | Collision | Realization order |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | 124 | 0–123 | 1–124 | `d_i = 1 + ((i−1) mod (n−1))` | 2 | lowest unused eligible reserved rank of `d_i`; **integer rank** | pads drawn (§4a) | NO | §5 registry | ascending global id; per item: `u`-pad, `u`-rank, `v`-pad, `v`-rank |
| S2·YES | 8 | 124–131 | 1–8 | `n` | 2 | reserved rank of `d = n`; **integer rank** | pads drawn (§4a) | YES | §5 | same |
| S2·NO-low | 4 | 132–135 | 9–12 | `n − 1` | 2 | reserved rank; **integer rank** | pads drawn (§4a) | NO | §5 | same |
| S2·NO-high | 4 | 136–139 | 13–16 | `n + 1` | 2 if `n ≤ 124`; **3 at `n = 125`** (`d = 126`) | z2: reserved rank; z3: **corner `(63, −63)`**, two-int identity | pads drawn (§4a) | NO | §5 | same |
| S3·YES | 8 | 140–147 | 1–8 | `0` | 2 | reserved rank of `d = 0`; **integer rank** | pads drawn; **`u ≠ v` rejection** (§4b) | YES | §5 + `u ≠ v` | same |
| S3·NO | 8 | 148–155 | 9–16 | `1 ×4`, then `2 ×4` | 2 | reserved ranks of `d = 1`, `d = 2`; **integer rank** | pads drawn (§4a) | NO | §5 | same |
| S4 | 16 | 156–171 | 1–16 | `2n ×8`, `2n−4 ×4`, `2n+4 ×4` | 3 | **verbatim v3.1.1 C1 / v3.1.2 F-3 / v3.1.3** (endpoint splits, fixed paddings, two-int identity) | fixed table | 8 YES / 8 NO | v3.1.3 B-1 within S4 | verbatim |
| S5·d0 | 4 | 172–175 | 1–4 | `0` | 2 | reserved rank of `d = 0`, **eligible `\|a\| ≥ 95`** (`a = b`); integer rank | **fixed `(p_u, p_v) = (5, 5)`** → both sides `= \|a\| + 10 ≥ 105 ≥ 100` | YES | §5 | same |
| S5·dn | 4 | 176–179 | 5–8 | `n` | 2 | reserved rank of `d = n`, **eligible `abs((\|a\| + 10) − \|b\|) ≥ 60`**; integer rank | **fixed `(p_u, p_v) = (5, 0)`** → side lengths `\|a\| + 10` and `\|b\|` | YES | §5 | same |
| S5·dn+2 | 4 | 180–183 | 9–12 | `n + 2` | 2 if `n ≤ 123`; **3 at `n ∈ {124, 125}`** (`d ∈ {126, 127}`) | z2: reserved rank; z3: **corners `(63, −63)` / `(64, −63)`**, two-int identity | pads drawn (§4a) | NO | §5 | same |
| S5·locked | 4 | 184–187 | 13–16 | **exact ordered `{3, 5, 7, 9}`** (canonical, `n`-independent; each `< 66 ≤ n`, hence `≠ n, n + 2` for every registry world) | 2 | reserved rank of each `d`, **eligible `\|a\| ≥ 95` and `\|b\| ≥ 95`**; integer rank | **fixed `(p_u, p_v) = (5, 5)`** → both sides `≥ 105` | NO | §5 | same |

Counts: `124 + 16 + 16 + 16 + 16 = 188` — the A4 schema surface is
unchanged.

## 4. Exact eligibility and padding (no "achievable", no "matched")

a. **Drawn padding (S1, S2 all groups, S3·NO, S5·dn+2):** the `pad`
   draw selects from the item side's **ascending admissible padding
   set** (`p ∈ {0..5}` truncated by the 138-token word cap) via
   `U(|set|)`, then the word `rank` draw as already specified (F-3).
b. **S3·YES:** the same pad and rank draws, with **`u ≠ v` as an
   additional rejection predicate** under §5.
c. **Fixed paddings (S5·d0, S5·dn, S5·locked, and all of S4):** as
   tabled; **every fixed padding must also satisfy the global 138-token
   word cap** (`|a| + 2p ≤ 138`; holds for all eligible cells since
   `|a| ≤ 128` and `p ≤ 5`); the exhaustive availability verifier (§6)
   failing on any item is **design invalidity**.

**Withdrawn wording (loud):** S2's "NO items length-matched to YES" is
**withdrawn as mathematically unsatisfiable** (total pair length
`≡ d (mod 2)`; `d = n` and `d = n ± 1` have opposite parity — Opus
PG-3), and the generic S3/S5 "matched" wording is **withdrawn as
non-executable**, both replaced by the exact padding rules above.
**Stated loudly: S2, S3, and S5 carry no anti-lookup authority** — they
are breadth, syntactic-identity, and robustness strata whose length or
parity correlates still require a contact-anchored `n` to exploit —
**and this relaxation does not touch S4**, which remains the sole
operational-certificate tooth, offset-only, with its joint feature-null
verifier intact and its text unchanged.

## 5. Collision semantics (operationalizes v3.1.3 B-1 without changing its redraw rule)

- Each stratum owns an **accepted-pair registry**, initially empty per
  world.
- A candidate `(u, v)` for the current item **collides iff it is
  already in that stratum's registry**; S3·YES additionally rejects
  `u = v`.
- On either rejection: hold `u` and both pads fixed and advance **only
  the current item's `v`-side `rank` domain counter**, redrawing `v`
  until acceptance — exactly v3.1.3 B-1. After acceptance, add
  `(u, v)` to the registry.
- Exhaustion routes to **design invalidity**.

**Consistency with the signed B-1 availability claim (named, not
hidden):** the registry is consistent. For distinct-cell items a
cross-item collision is structurally impossible (a raw pair determines
its displacement pair, and each such item consumes its own cell), so
the registry is idle there and B-1's within-item reading is unchanged.
The registry is **load-bearing exactly for the shared-cell groups** —
the zone-3 edge groups (S2·NO-high at `n = 125`; S5·dn+2 at
`n ∈ {124, 125}`), where four items realize one corner cell, and S4's
shared endpoint pairs (already covered by v3.1.1's "within S4"
rejection) — where duplicate `(u, v)` across items is possible and must
be rejected. Availability is untouched: the corner word sets
`|W(63 or 64, ℓ)|` are astronomically larger than four draws, so B-1's
"exhaustion impossible under the A3 availability proof" stands. No
correction to B-1 is required.

## 6. Enumeration obligations (exhaustive, dummy-only verifier)

A dummy-seed-only verifier must prove, for **every `n ∈ [66, 125]`**,
before any real panel exists: (i) counts, global and local ids, and
labels exactly as tabled; (ii) zone crossings occur exactly at the
three named edges (S2 at `n = 125`; S5·dn+2 at `n ∈ {124, 125}`) and
nowhere else; (iii) global-rank consumption yields unique cells with no
reuse across the whole panel; (iv) every eligibility predicate and the
138-token word cap hold for every selected cell and fixed padding;
(v) every required reserved `d`-class retains enough eligible unused
cells for all its consumers (including S1's repeated differences and
S5's `≥ 95`/imbalance predicates) and every word-rank set is large
enough; (vi) `u ≠ v` is satisfied for all S3·YES items; (vii) all three
edge-crossing groups construct and serialize under B-2's two-integer
branch; (viii) the exposed schema surface is exactly
`188 = 124 + 16 + 16 + 16 + 16`; (ix) **no public-root pool word
appears as a panel word**. Verifier failure is design invalidity.

---

This amendment supersedes only the sentences its closure memo lists.
The three signed author tokens remain valid for all unchanged science;
this amendment awaits bounded Opus and Sol confirmation and then **its
own author token** (closure memo §4). No execution of any kind is
authorized by this document.
