# Opus 4.8 X-line — Level 1 v3.1.4.1 final panel confirmation

Reviewer: Opus 4.8 (adversarial, bounded to the PV0 fix). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md`, against
my v3.1.4 panel review and Sol's v3.1.4 review. PG-1–PG-4, S4, every scientific
choice, and the Y-line are not reopened. This confirmation permits only Kirill's
amendment token; it authorizes no implementation, entropy, dummy/real panel
generation, data, lock, escrow, or outcome.

---

## Verdict

**`LEVEL1_V3_1_4_1_XLINE_CONFIRMED_FOR_SIGNATURE`**

The PV0 replacement text was adopted **verbatim**, it closes the last
panel-generator ambiguity (the `p_v = 0` singleton that defeated B-1), and it
changes no label, count, cell, threshold, claim, inference rule, or gate. The panel
contract is now bit-exact.

---

## Findings

- **Clause 4d adopted verbatim and scoped exactly.** It restricts `p_v` to the
  ascending positive admissible set (`{1..5}`, cap-truncated) for precisely the
  rejection-bearing drawn-pad groups — S3·YES and the three non-S4 edge crossings
  (S2·NO-high at `n = 125`; S5·dn+2 at `n ∈ {124, 125}`) — and leaves `p_u`, every
  non-rejection group, and S4 unchanged. S4 stays verbatim (its fixed table already
  supplies `p_v ∈ {1,2,3}`). This is my supplied text word-for-word.

- **The exhaustion justification is now executable.** The §2 replacement states the
  explicit lower bounds `|W(v)| ≥ 2` (S3·YES, displacement 0) and `≥ 65` (the
  `±63/±64` corners), both verified last round, against the `≤ 4` rejections any
  group can require — so B-1's `v`-rank redraw provably terminates. The added
  dummy-only verifier assertion (every rejection-bearing `v`-draw uses the positive
  set and `|W(v)|` exceeds that group's rejection count, failure = pre-execution
  design invalidity) closes pre-execution enforcement.

- **No scientific content changed.** Only the `v`-side padding *draw set* for three
  rejection-bearing groups narrowed from `{0..5}` to `{1..5}`; padding is
  cancelling-pair length that does not affect displacement, difference, or EQ, and
  S2/S3/S5 carry no length-matching requirement (withdrawn). Labels (YES/NO),
  counts (188, 32/156), cells, thresholds, the inference family, and the gate order
  are untouched.

## Answers to the required checks

1. Clause 4d restricts `p_v` to the positive admissible set for S3·YES and the
   three non-S4 edge crossings, leaving `p_u`, other groups, and S4 unchanged. ✓
2. The explicit lower bounds (`2`, `65`) make B-1 termination executable, and the
   added dummy-verifier assertion closes pre-execution enforcement. ✓
3. No label, count, cell, threshold, claim, inference rule, or gate changed. ✓
4. `I_ACCEPT_LEVEL1_V3_1_4_PANEL_CONTRACT` can honestly accept v3.1.4 **together
   with** v3.1.4.1 — the correction states exactly this binding, and the two
   documents are consistent. ✓

## Authorization and negative space

This confirmation permits **only Kirill's amendment token**
(`I_ACCEPT_LEVEL1_V3_1_4_PANEL_CONTRACT`, covering v3.1.4 + v3.1.4.1). It authorizes
no implementation, entropy, dummy or real panel generation, data, lock, escrow, or
outcome; the panel builder may be implemented only after that token, under the §6
dummy-only enumeration verifier, and each later gate keeps its own authorization.

Preserved and unweakened: the adjacent-only detector scope; the operational-modulus
certificate and its **sole S4 tooth** (offset-only, joint feature-null intact,
verbatim); S2/S3/S5 carrying no anti-lookup authority; the public-reservation /
secret-realization confidentiality boundary (no public word is ever a panel word);
`PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation; `UNKNOWN`/censored never success;
a certificate failure is censoring, never evidence the learner lacked `n`; donor
transcripts encode `n_donor`, never `n_target`; development contrasts non-citable
forever; Level 1 never evidence for `PROOF_CORE`.

The panel-generator thread is closed: PG-1–PG-4 → the exhaustion challenge → one
positive-padding clause, adopted verbatim, at decreasing cost. The non-S4 panel
contract is bit-exact and, on the amendment token, ready for implementation.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
