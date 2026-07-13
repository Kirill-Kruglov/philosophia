# Opus 4.8 X-line — Level 1 v3.1.1 correction, final bounded check

Reviewer: Opus 4.8 (adversarial, bounded to C1–C7). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`, against the v3
spec, the v3.1 addendum, my v3.1 signature check, Sol's v3.1 check, and Fable's
v3.1.1 closure. The world, 24-pair frame, adjacent-only scope, and inference
family are not reopened. This check authorizes no implementation, entropy,
feasibility, scout, lock, escrow, or outcome, and predicts no arm. The S4 feature
analysis and cell counts below were recomputed independently.

---

## Verdict

**`REVISE_LEVEL1_V3_1_1_SCOPE_TEXT`**

The science lands. C1's offset-only reconstruction **removes the v3.1
parity/symmetry XOR at the source** (all items offset, every side parity
`≡ n+1`, so symmetry and side-parity are label-constant), and I confirmed by
exhaustive joint search that **the only feature combinations separating YES from
NO are exactly those that reconstruct `d`** (`(padding, ordered-lengths)` and
`(padding, total-length)`, both yielding `d` identically). No `n`-free,
non-`d`-reconstructing rule separates the labels. The honest operational-modulus
scope and its non-consolidated token are the correct resolution.

Two bounded **text** defects block signature, neither scientific:

1. **The C1 feature-null verifier is internally contradictory.** It requires the
   label-conditional multiset "of the entire vector, and of every pairwise and
   triple sub-combination, to be identical," while the vector *includes* padding
   and ordered side-lengths whose joint reconstructs `d` — which differs by label
   by design. Verified: `(pad, olen)` and `(pad, tot)` separate and both recover
   `d` exactly. As written the verifier is unsatisfiable and would reject its own
   sound construction. It must be re-scoped to a declared non-structural family
   that excludes `d`-reconstructing combinations.

2. **The `A_word 126→128` change makes the carried cell counts stale.**
   Recomputed: acquisition cells (`|d| ≤ 125`, endpoints in `[−128, 128]`) rise
   from `24,003` to `24,507`, pool `67,208 → 68,620`, headroom `33.6× → 34.3×`.
   The correction reuses the old figures and says "acquisition pool semantics
   unchanged" while changing the bound they depend on — reconcile.

Both are one-paragraph edits. No scientific blocker remains (not
`BLOCKED_LEVEL1_OPERATIONAL_CERTIFICATE`); the certificate is not approvable
verbatim (not `..._APPROVED`) because its own verifier would reject it and its
counts are wrong. **All Level 1 execution remains forbidden.**

---

## Findings

### Blocking (bounded text)

- **F-1 (O1) — verifier contradiction.** C1's "every pairwise/triple
  sub-combination identical" over a vector containing `(padding vector, ordered
  side lengths, total length)` is unsatisfiable when labels differ by `d`, because
  `d = Σ(ℓ_side − 2p_side)` is recoverable from that pair. The correction excludes
  the *direct* `d`-fields `(a,b), d, |a|+|b|` but not the `(padding, length)`
  *combination* that reconstructs them, then demands full-joint identity — a
  self-contradiction. Fix: declare the non-structural nuisance family explicitly
  (symmetry, side-parity, `||a|−|b||`, offset sign, padding **marginal**, ordered
  side-length **marginal**) and require joint identity **only within that family
  and only for combinations that do not reconstruct `d`**; explicitly permit
  `(padding, lengths)` and displacement fields to differ as the structural signal;
  keep the exhaustive "no `n`-free non-`d` rule separates above chance" check
  (which passes).

- **F-2 (O1/O2) — stale acquisition counts.** Update to `24,507` cells /
  `68,620` realized / `34.3× B` under `A_word = 128`, **or** explicitly decouple
  the acquisition displacement cap from `A_word` (keep it at 126, pool unchanged
  at `24,003`) and say so. Either is fine; the ambiguity is not.

### Major (bounded)

- **F-3 (O2) — panel-realization domains specified only for S4.** C3 requires all
  *real panel* realizations to derive from the 256-bit escrow-secret seed, but C2
  gives an explicit panel PRF domain only for S4
  (`("L1","panel", world_slot, "S4", …)`). The S1/S2/S3/S5 panel raw words (drawn
  on reserved cells, whose *reservation* is public but whose *panel realizations*
  must be secret) have no declared domain — a bit-level and confidentiality gap.
  Specify the panel-realization domains for every stratum under the secret seed,
  so reserved-cell *public* pool words are never reused as *panel* words.

### Accepted — do not reopen

The offset-only construction and its label-conditional balance (symmetry, parity,
`||a|−|b||`, offset sign, padding multiset, ordered/total lengths all balanced —
verified); the operational-modulus certificate meaning and its loud
non-consolidated token; C2 (per-stratum/per-pair allocation domains with
owned counters — closes v3.1 MJ-1); S4 secret-seed word ranks and S5 eligibility
(closes v3.1 MJ-2/mn-2); the token decoder; C3 public-root/escrow-secret
separation (the public root cannot derive real panel content, and dummy seeds
cannot pass the real-artifact attestation — both correct); C4 model pins (`fan_in`
enumeration, big-endian `PRF[0:8]→manual_seed`, `torch 2.9.1+cpu`, input length
`277`); C5 slot canonicalization; C6 inference corrections (zero-variance interval
labeled "estimated, not census certainty"; the census-selection clarification;
Popoviciu `B²` bound); edge realizability at `A_word = 128` (verified at `n = 66`
and `n = 125`, NO-high at `n = 125` using endpoint `128` exactly, all
uncontactable).

---

## Answers to the required checks

### O1 — S4 and the operational-certificate boundary

- **Support, remainders, bounds, parity, offset-only, raw-length** — verified.
  `d ∈ {2n−4, 2n, 2n+4}`, remainders `{n−4, 0, 4}` nonzero for all `n ∈ [66,125]`;
  minimum `d = 128 > d_acq = 125` (uncontactable); maximum `d = 254 ≤ 2·A_word =
  256` (realizable); every side parity `≡ n+1`, every item offset (`||a|−|b|| = 2`).
- **Full joint nuisance test** — the suspected `(padding, ordered side-length)`
  XOR **is present** (`(pad, olen)` separates), *and so is* `(pad, tot)`, **but
  both reconstruct `d`** (confirmed: `d_rec = d` exactly). Every non-`d` marginal
  and every non-`d`-reconstructing joint is label-balanced. So the padding/length
  XOR is not an `n`-free shortcut — it is the legitimate `d`-computation.
- **Logical boundary / verifier contradiction** — **yes, C1's verifier is
  internally contradictory** (F-1): a joint vector containing padding and lengths
  reconstructs `d`, so it cannot be label-identical when labels differ by
  `d mod n`. The permitted bounded resolution applies: the original parity/symmetry
  shortcut is removed, no `n`-free non-`d` rule separates, so **accept the
  operational-modulus scope** and re-scope the verifier to the declared
  non-structural family with `d`-reconstructing combinations explicitly allowed to
  differ — not full raw-feature joint identity.
- **`A_word 126→128`** — **changes the counts** (F-2); require corrected exact
  figures or an explicit cap decoupling.

### O2 — Generator/model closure

C2–C5 close the prior gaps: allocation domains are per-stratum/per-pair with owned
counters and a canonical order (closes v3.1 MJ-1); S4 words use the secret-seed
rank draw (closes MJ-2); S5 eligibility precedes rank (closes mn-2); the token
decoder, `fan_in`, seed decode, torch pin, input length `277`, and slot
canonicalization are exact. **Public-root vs secret-panel separation is correct**:
the public root's domain list omits `("L1","panel",…)`, real panel content derives
only from the sealed escrow-secret seed, and dummy panels use a declared test-only
seed that cannot pass the real-artifact attestation gate. **Remaining
trajectory-/confidentiality-divergent gap:** F-3 (non-S4 panel-realization domains
unspecified). No other divergence found.

### O3 — Scope/signature readiness

The operational certificate **proves**: the learner recovered a contact-anchored
modulus value sufficient to classify previously uncontactable opposite-corner
differences `2n` versus `2n ± 4`. It **forbids**: any claim to distinguish an
abstract period *representation* from a learner that recovered/memorized `n` and
performs correct novel-`d` arithmetic; a pass is that operational competence only;
a failure is censoring and never proves the learner lacked `n`. The three
non-consolidated tokens (`I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`,
`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE` with its
`I_REJECT_LEVEL1_CYCLIC_CERTIFICATE` alternative, and the v3+v3.1+v3.1.1 spec
token) make the irreducible cyclic-world limitation loud enough for an informed
signature. **No scientific blocker remains** — only the F-1 verifier text, the
F-2 counts, and the F-3 panel domains, all bounded. After those three edits the
correction is signable.

---

## Bounded edits (the complete list)

1. **F-1:** rewrite the C1 verifier to require joint label-identity only over a
   declared non-structural family, explicitly excluding every `d`-reconstructing
   combination (`(padding, ordered/total lengths)`, per-side or summed
   displacement), and retain the exhaustive "no `n`-free non-`d` rule separates"
   check.
2. **F-2:** state the corrected acquisition counts (`24,507 / 68,620 / 34.3× B`)
   or decouple and fix the acquisition displacement cap at 126 (counts unchanged),
   replacing the stale `24,003 / 67k` figures wherever carried.
3. **F-3:** declare the escrow-secret panel-realization PRF domains for S1, S2,
   S3, and S5 (as for S4), so no public reserved-cell word is reused as a panel
   word.

No change to the world, frame, scope, estimand, or inference family is required.

---

## Negative-space preservation

Unweakened: adjacent-only distance-1 detector scope and the thin
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; the 24-pair frame and census reading;
`PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation; C1 a non-core modifier;
`UNKNOWN`/censored/all-censored never equivalence, boundary, or success; **a
certificate failure is censoring, never evidence the learner lacked `n`** — now on
an honest operational meaning; RANDOM-superior an anomaly, never a C1 rewrite;
donor transcripts encode `n_donor`, never `n_target`; development contrasts
non-citable forever.

**No Level 1 execution is authorized by this check.** After the three bounded
edits the correction returns for confirmation; nothing here permits an entropy
draw, implementation, feasibility run, scout, lock, escrow, or outcome.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
