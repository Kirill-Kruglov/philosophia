# Opus 4.8 X-line — Level 1 v3.1.4 panel-amendment review

Reviewer: Opus 4.8 (adversarial, bounded to the panel amendment). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`, against my
readiness audit, Fable's v3.1.4 closure, the governing v3.1.1–v3.1.3 corrections,
and the substrate `src/philosophia/level1/{config,serialization,world,pool}.py`.
S4, scope, population, learner, endpoint, inference, selector, and gate order are
not reopened. This review authorizes no signature or execution. The exhaustion
challenge and the table were verified by independent computation.

---

## Verdict

**`REVISE_LEVEL1_V3_1_4_PANEL_TEXT`**

The amendment adopts PG-1–PG-4 exactly, the table enumerates correctly for every
world, the global `item_id` is unambiguous, and the honest relaxations are named —
**but the exhaustion challenge is confirmed real.** The amendment still permits
`p_v = 0` in the rejection-bearing drawn-pad groups, where `W(v)` is a **singleton**,
so B-1's "advance only the `v`-rank counter" cannot escape a collision, and §5's
claim that B-1 exhaustion is impossible is false in that case. One bounded repair
(the `p_v ≥ 1` rule the audit anticipated) closes it; S4 is already safe and
untouched. Nothing else requires change.

---

## Findings

### Blocking (one bounded edit)

- **PV0 — `p_v = 0` singleton defeats B-1 in the rejection-bearing groups.**
  Verified: for any displacement, `|W(disp, |disp|)| = 1` at `p_v = 0` (a
  singleton — the all-`R` or all-`L` reduced word). B-1 holds `u` and both pads
  fixed and redraws only `v`; with `p_v = 0` there is no other `v`, so a collision
  is unresolvable → design invalidity. This bites where drawn pads coincide with a
  rejection: **S3·YES** (`u ≠ v`), and the **zone-3 repeated-corner edge groups**
  (S2·NO-high at `n = 125`; S5·dn+2 at `n ∈ {124, 125}`), where four items share
  one corner cell and the registry rejects duplicate `(u, v)`. §5's justification
  ("`|W(63 or 64, ℓ)|` astronomically larger than four draws") silently assumes
  `p_v ≥ 1`; it does not hold for the `p_v = 0` draw the amendment permits. Repair
  below.

### Confirmed adopted / correct (do not reopen)

- **PG-1–PG-4 adopted exactly.** Global zero-based ids (S1 `0–123`, S2 `124–139`,
  S3 `140–155`, S4 `156–171`, S5 `172–187`), the F-3 `item_id` bound to the global
  id, global-A3-canonical-rank reserved selection, ascending-global-id consumption
  with global "unused", the zone-3 corner rule `(⌈d/2⌉, −⌊d/2⌋)` with the B-2
  two-integer identity extended to every zone-3 item, S5's locked `{3, 5, 7, 9}`
  and the `|a|, |b| ≥ 95` / imbalance eligibilities, the loudly withdrawn
  "length-matched"/"matched" claims, and verbatim S4.
- **Table enumerates correctly.** Independently for every `n ∈ [66, 125]`: exactly
  188 items, 32 YES / 156 NO, labels correct, and the non-S4 zone-3 crossings are
  **exactly** `(124, S5, 126)`, `(125, S2, 126)`, `(125, S5, 127)` and nowhere
  else — matching §6(ii).
- **`item_id` is unambiguous** (§1: always the global zero-based panel id; one byte
  stream). `cell_identity` is one integer rank (zone 2) or two integer components
  `a, b` (zone 3), deterministic from the item's zone; each domain component is
  `int`/`str` and encodes to a single A2 byte string.
- **S4 is already exhaustion-safe.** Its fixed padding table gives `p_v ∈ {1, 2, 3}`
  (never 0), so the `v`-side is never a singleton and B-1 within S4 always resolves
  — no S4 change needed, consistent with preserving it verbatim.
- **Substrate faithful.** `config`/`pool`/`serialization`/`world` match the signed
  contract (A_word 128, counts 7 295/17 212/68 848, A2 encoding, rejection sampler,
  `a ≥ b`); the real panel builder is correctly absent.

---

## Answers to the required checks

1. **PG-1–PG-4 adoption** — exact (above). ✓
2. **Algebraic enumeration `n = 66..125`** — counts, labels, zones, caps, repeated
   differences, and the three edge crossings all verified. ✓
3. **F-3 `item_id`** — unambiguously global zero-based; every domain
   component/ordering yields one byte stream. ✓
4. **Accepted-pair registry vs B-1 exhaustion** — the registry logic is right for
   distinct-cell items (idle) and load-bearing for shared-cell groups, but the
   exhaustion analysis is **incomplete**: it treats only ordinary collision
   probability against large `W`, missing the `p_v = 0` singleton (PV0). This is
   the one blocking gap.

---

## Exact bounded repair (adopt verbatim; changes no label, count, cell, or claim)

Add to §4 and correct §5's justification:

- **§4 (new clause 4d):** "For the `v`-side draw of every **rejection-bearing
  drawn-pad group** — S3·YES, and any zone-3 repeated-corner group (S2·NO-high at
  `n = 125`; S5·dn+2 at `n ∈ {124, 125}`) — `p_v` is drawn from the **ascending
  *positive* admissible padding set** (`p_v ∈ {1..5}`, truncated by the 138-token
  cap) via `U(|set|)`; `p_u` and all non-rejection-bearing groups keep the full
  `{0..5}` rule of §4a. This guarantees `|W(v)| ≥ 2`, so B-1's `v`-rank redraw
  always reaches a novel `v`."

- **§5 (corrected justification sentence):** "Exhaustion is impossible **because
  clause 4d forces `p_v ≥ 1`** on every rejection-bearing `v`-draw, giving `|W(v)|`
  at least 2 (S3·YES, displacement 0) and at least 65 (the `±63/±64` corners) — far
  more than the ≤ 4 rejections any group can require; the earlier
  'astronomically larger' wording, which implicitly assumed `p_v ≥ 1`, is replaced
  by this explicit bound."

Verified sufficiency: at `p_v = 1`, `|W(v)| = 2` for the S3·YES worst case
(displacement 0) — enough to choose `v ≠ u` — and `|W(v)| = 65` (disp `−63`) / `66`
(disp `−64`) for the edge corners — enough for four distinct accepted pairs. S4's
fixed table already supplies `p_v ∈ {1,2,3}`, so its rank surface is unaffected and
S4 stays verbatim.

The §6 enumeration verifier should additionally assert, per world, that every
rejection-bearing `v`-draw uses the positive padding set and that `|W(v)| >` the
number of that group's rejections — failure is design invalidity.

---

## Authorization and negative space

This `REVISE` authorizes **no signature and no execution**. With clause 4d and the
§5 correction adopted, the panel amendment is bit-exact and returns for a bounded
confirmation before its own author token. Preserved and unweakened: the
adjacent-only detector scope; the operational-modulus certificate and its **sole
S4 tooth** (offset-only, joint feature-null intact, verbatim); the loudly-named
fact that S2/S3/S5 carry no anti-lookup authority; `PROOF_CORE`/`PROOF_STRONG` and
C6-as-annotation; `UNKNOWN`/censored never success; a certificate failure is
censoring, never evidence the learner lacked `n`; the public-reservation /
secret-realization confidentiality boundary (no public word is ever a panel word);
donor transcripts encode `n_donor`, never `n_target`; development contrasts
non-citable forever; Level 1 never evidence for `PROOF_CORE`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
