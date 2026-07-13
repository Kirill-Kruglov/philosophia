# Opus 4.8 X-line — Level 1 panel-generator implementation-readiness audit

Reviewer: Opus 4.8 (adversarial, bounded pre-data). Target: the non-S4 panel
contract (S1/S2/S3/S5) across v3 §4, v3.1 A1/A3/A4, v3.1.1 C1–C3, v3.1.2 F-1/F-3,
v3.1.3, and the neutral substrate `src/philosophia/level1/{world,pool,serialization,config}.py`.
The scientific scope, S4 operational certificate, population, endpoint, inference,
selector, and gate order are closed and not reopened. This audit authorizes no
code, entropy, panel, data, lock, escrow, or outcome. Arithmetic was recomputed
independently.

---

## Verdict

**`REVISE_LEVEL1_PANEL_GENERATOR_CONTRACT`**

The neutral substrate is faithful, but the **non-S4 panel contract is not
implementation-ready**: two independent implementers cannot derive identical panel
bytes for every world. The known zone-3 contradiction is confirmed at the code
level (the substrate literally cannot represent the edge cells), and four further
non-S4 determinism gaps exist. All are repairable by one bounded addendum table
(below); none touches S4 or any closed scientific choice. A correction requires a
loud signed pre-data amendment and a bounded confirmation before panel
implementation.

---

## Findings

### Critical

- **PG-1 — zone-3 edge items are unconstructible under the signed contract
  (confirmed at code level).** `world.cells_for_difference` raises `ValueError`
  for `d = 126, 127`, and reserved cells exist only for `|d| ≤ 125`, yet F-3/B-2
  require S1/S2/S3/S5 `cell_identity` to be a *reserved cell's canonical rank*. The
  exact crossings (recomputed): **S5 `d = n+2 = 126` at `n = 124`**, and **S2
  `d = n+1 = 126` and S5 `d = n+2 = 127` at `n = 125`** — 4 items per crossing,
  three crossings. For these items the signed contract supplies no cell, no
  `cell_identity`, and no selection rule, and B-2 cannot serialize them. The panel
  builder cannot be written for `n ∈ {124, 125}` as specified.

- **PG-2 — S5's fourth group has no exact `d` values or provenance.** "4 × locked
  `d ∈ [3,125] \ {n, n+2}` at length ≥ 100" names neither the four `d` nor a
  deterministic rule or PRF domain to derive them. Two implementers pick different
  `d` → different panels. Non-reproducible.

### Major

- **PG-3 — S2 "NO items length-matched to YES" is unsatisfiable.** Total pair token
  length `≡ d (mod 2)`; YES has `d = n`, NO has `d = n ± 1`, opposite parity
  (verified at `n = 100, 125`), so identical total length is impossible. The claim
  must be withdrawn and relaxed honestly. This does **not** weaken S4: S2 is a
  difference-recognition stratum with no anti-lookup role (a difference-lookup that
  found `d = n` already passes it), any length correlate still requires knowing
  `parity(n)`, and S4 — the sole tooth — is offset-only with its own joint
  feature-null intact and untouched.

- **PG-4 — non-S4 selection determinism is under-specified.** (a) The "reserved
  index" ordering (rank within the reserved subset vs global cell rank) is not
  pinned; (b) the consumption order for **repeated-difference** S1 items (e.g. at
  `n = 66`, residues 1–59 each appear twice) is not stated; (c) S3's `d = 0`
  distinctness (`u ≠ v`) and its collision scope, and S5's `d = 0` `length ≥ 100`
  and `d = n` `imbalance ≥ 60` **eligibility predicates** (both sides? which
  padding?) are not exactly defined. Each is a byte-divergence surface.

### Faithful (do not reopen)

The gate-1 substrate matches the signed contract exactly: `config` freezes
`A_word = 128`, `d_acq = 125`, input `277`, and `verify_geometry` checks the S4
`±4` teeth realizability/uncontactability; `pool.verify_partition` asserts the
exact **7,295 / 17,212 / 68,848** counts (F-2); `serialization` implements the A2
`encode_component` (int→decimal ASCII, str→UTF-8, `uint16_be(len)‖payload`), the
rejection sampler (`limit = ⌊2²⁵⁶/m⌋·m`, `m=1→0`), and descending Fisher–Yates;
`world.Cell` enforces `a ≥ b` orientation and the `[0, 125]` difference bound. The
real panel builder is correctly absent, and `DeterministicKey` is dummy/`test_only`
only. B-2's "two integer components" is representable (the domain tuple already
admits consecutive `int` components).

---

## Audit answers (the seven checks)

1. **Cell selection/identity for every item** — sound for S1 (all `d_i ≤ 124`,
   zone 2), S2 non-edge, S3, and S5 non-edge *given* PG-4's ordering fixes;
   **broken** for the PG-1 zone-3 edge items and PG-2's unspecified `d`.
2. **S2 "NO length-matched to YES"** — unsatisfiable (PG-3, parity obstruction);
   must be relaxed and named.
3. **S3 "matched" + distinctness/collision** — "matched" is likewise only partly
   satisfiable (`d = 1` odd vs `d = 0, 2` even) and `u ≠ v` collision scope is
   unspecified (PG-4).
4. **S5 four locked `d`, provenance, order, eligibility** — missing (PG-2, PG-4).
5. **Padding/rank/collision/order under the secret domains** — the *general*
   mechanism (F-3, B-1, B-2) is bit-exact, but it consumes a `cell_identity` that
   PG-1/PG-2 leave undefined for the affected items.
6. **Enough realizations per cell** — holds where cells are pinned (S5 locked-`d`
   eligibility verified: ≥ 25 eligible cells per `d ∈ {3,5,7,9}`), but cannot be
   checked for the undefined items.
7. **Confidentiality boundary** — public reservation + secret realization is the
   right boundary and is preserved by the repair (zone-3 edge items use secret
   `(a,b)` realizations exactly like S4, never public words).

**Two implementers cannot currently produce identical bytes** → not ready.

---

## Smallest bit-exact repair (bounded addendum; S4 preserved verbatim)

Per-item-group table for S1/S2/S3/S5. All realizations use the F-3 secret-keyed
domains, the B-1 collision rule, and B-2 serialization. Reserved selection uses
**reserved cells ordered by the A3 canonical cell order; "lowest unused reserved
rank" of the required `d`; consumed in ascending item id** (fixes PG-4a/b).

| Group | Count | Item ids | Exact `d` | Zone | Cell selection & `cell_identity` | Eligibility / padding | Label | Collision |
|---|---|---|---|---|---|---|---|---|
| S1 | 124 | 1–124 | `d_i = 1+((i−1) mod (n−1))` | 2 | lowest-unused reserved rank of `d_i`; id = **canonical integer rank** | any admissible padding | NO | B-1, within item |
| S2·YES | 8 | 1–8 | `n` | 2 | reserved rank of `d=n`; **int rank** | any admissible padding | YES | B-1 |
| S2·NO-low | 4 | 9–12 | `n−1` | 2 | reserved rank of `d=n−1`; **int rank** | any admissible padding | NO | B-1 |
| S2·NO-high | 4 | 13–16 | `n+1` | 2 if `n≤124`; **3 if `n=125` (`d=126`)** | z2: reserved rank; **z3: corner `(a,b)=(⌈d/2⌉,−⌊d/2⌋)=(63,−63)`** | any admissible padding | NO | B-1 |
| S3·YES | 8 | 1–8 | `0` | 2 | reserved rank of `d=0`; **int rank** | draw until `u ≠ v` (B-1, within item) | YES | B-1 + `u≠v` |
| S3·NO | 8 | 9–16 | `1`×4, `2`×4 | 2 | reserved ranks of `d=1`,`d=2`; **int rank** | any admissible padding | NO | B-1 |
| S5·d0 | 4 | 1–4 | `0` | 2 | reserved rank of `d=0` **eligible** (`\|a\|≥95`); **int rank** | fixed `p_u=p_v=5` → both sides `≥100` | YES | B-1 |
| S5·dn | 4 | 5–8 | `n` | 2 | reserved rank of `d=n` **eligible** (`\|len_u−len_v\|≥60` achievable); **int rank** | fixed `(p_u,p_v)=(5,0)` → imbalance `≥ n−... ` (`≥60` for `n≥66`) | YES | B-1 |
| S5·dn+2 | 4 | 9–12 | `n+2` | 2 if `n≤123`; **3 if `n∈{124,125}`** | z2 reserved rank; **z3: corner `(⌈d/2⌉,−⌊d/2⌋)` (`(63,−63)`/`(64,−63)`)** | any admissible padding | NO | B-1 |
| S5·locked | 4 | 13–16 | **`{3,5,7,9}`** (canonical, `n`-independent; each `< 66 ≤ n`, so `≠ n, n+2`) | 2 | reserved rank of each `d` **eligible** (`\|a\|,\|b\|≥95`); **int rank** | fixed `p_u=p_v=5` → both sides `≥100` | NO | B-1 |

Zone-3 rule (uniform, extends S4's convention to the edge items only): an item
whose required `d > 125` has `cell_identity = (a,b)` with `a = ⌈d/2⌉`,
`b = −⌊d/2⌋` (realizable: `|a| ≤ 64 ≤ 128`; verified), serialized by B-2's S4
branch (two integer components), realized under the secret panel domain — never a
public word.

**Honest relaxation, named:** the words "length-matched" (S2) and "matched" (S3,
S5) are **withdrawn** and replaced by the fixed padding rules above. S2/S3/S5
carry **no anti-lookup force** (already stated in v3 §4); a length/parity correlate
in them still requires knowing `parity(n)`/scale, so nothing is testable there
without contact-anchored `n`, and **S4 remains the sole anti-lookup tooth,
offset-only, joint-feature-null intact, and textually unchanged.** No
outcome-dependent value and no new scientific claim is introduced; labels and
stratum roles are unchanged.

**S-gate enumeration obligations added:** for every `n ∈ [66,125]`, (i) each
required reserved `d`-class has enough eligible unused cells for its consumers
(including repeated-difference S1 and the `≥95`/`≥60` S5 eligibilities — spot-check
confirms ≥ 25 eligible cells per S5 locked `d`); (ii) the three zone-3 edge groups
construct and serialize; (iii) `u ≠ v` is achievable for every S3·YES item.

---

## Authorization and negative space

This `REVISE` authorizes **nothing**: no panel, entropy, implementation, data,
lock, escrow, or outcome. The repair is a **loud signed pre-data amendment**
(it changes panel-item construction for `n ∈ {124,125}` and pins S5's locked `d`);
it must be signed and pass a bounded confirmation before the panel builder is
implemented. Preserved and unweakened: the adjacent-only detector scope; the
operational-modulus certificate and its sole S4 tooth; `PROOF_CORE`/`PROOF_STRONG`
and C6-as-annotation; `UNKNOWN`/censored never success; a certificate failure is
censoring, never evidence the learner lacked `n`; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever; Level 1
never evidence for `PROOF_CORE`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
