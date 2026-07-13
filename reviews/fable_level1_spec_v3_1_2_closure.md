# Fable 5 — Level 1 v3.1.2 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`;
v1–v3.1.1 preserved unchanged; the correction supersedes only the
v3.1.1 C1 verifier paragraph, the carried acquisition counts, and the
C2/C3 panel-domain lines. Inputs: Opus v3.1.1 final check
(`REVISE_LEVEL1_V3_1_1_SCOPE_TEXT`, exactly F-1/F-2/F-3) and Sol
v3.1.1 final check
(`LEVEL1_V3_1_1_YLINE_APPROVED_FOR_AUTHOR_SIGNATURE`).

## Verdict

**READY_FOR_LEVEL1_AUTHOR_SIGNATURE_CHECK**

The Y-line is approved. The X-line found no scientific blocker; its
three bounded text defects are closed with exact replacement text: the
verifier is now satisfiable and honest (F-1), every carried count is
reconciled under `A_word = 128` by the exact per-class rule (F-2), and
the secret-keyed panel-realization contract covers all five strata
(F-3). Nothing else was touched. The next step is the bounded reviewer
confirmation of these three repairs; **only after that does Kirill
sign** — this memo does not authorize author signature.

## 1. Dispositions

| Finding | Disposition | Correction |
|---|---|---|
| **Opus F-1** — verifier internally contradictory (full-joint identity over a vector whose `(padding, lengths)` joint reconstructs `d`) | **Adopted**: declared closed nuisance-field list; exact marginal identity per field; pairwise/triple combinations tested with an exact exemption for every `d`-reconstructing combination (`(pad, ordered lengths)`, `(pad, total length)`, supersets), each exemption emitted with its explicit reconstruction map, never silently classified; the exhaustive no-`n`-free-rule check retained (it passes, per the X-line's own exhaustive search); the honest statement that displacement fields and exempt combinations are the legitimate operational signal; no full raw-feature joint-identity claim; padding table and token untouched | F-1 |
| **Opus F-2** — stale counts under `A_word 126→128` | **Adopted with the exact rule, not the reviewer approximation**: `24,507` cells; reserved `Σ floor(3·N_d/10) = 7,295`; non-reserved `17,212`; pool `68,848`; headroom `34.424 × B`. Recorded explicitly: Opus's `68,620 / 34.3×` is `round(0.7·24,507)·4`, a global approximation incompatible with the normative per-class floor; the old v3 figures were `A_word = 126` values, superseded; neither was silently copied | F-2 |
| **Opus F-3** — panel-realization domains S4-only | **Adopted**: common secret-keyed skeleton `("L1","panel", world_slot, stratum_id, item_id, side, cell_identity, purpose)` with owned counters and canonical draw order; S4 fixed-padding specialization preserved; S1/S2/S3/S5 secret-keyed realization of their publicly selected reserved cells under their existing constraints; categorical prohibition on reusing public-root pool words as panel words; secret-keyed panel order; dummy seed cannot emit or attest a real artifact | F-3 |
| **Sol** — Y-line approved; three minor test-enforcement notes (dummy-seed emission impossibility, one-shot transcript assertions, canonicalization-only-difference test) | **Noted**: already implied by C2/C3/C5/C7 and F-3; they are gate-3 implementation tests, not design text; carried into the test obligations | — |

## 2. Exact count arithmetic (and why `68,620` is not normative)

Endpoints in `[−128, 128]`, support `|d| ≤ 125`: `N_0 = 257`,
`N_d = 257 − d` — class sizes are the consecutive integers `132..257`.
Total `= 24,507`. Reserved `= Σ floor(3·N_d/10)
= (3·24,507 − Σ residues)/10 = (73,521 − 571)/10 = 7,295`
(residues: twelve complete decades × 45 = 540, plus `N = 252..257`
contributing `6+9+2+5+8+1 = 31`). Non-reserved `= 17,212`; at `m = 4`
the flat pool is **68,848 = 34.424 × B**. `68,620` arises only from the
global approximation `round(0.7 · 24,507) × 4 = 17,155 × 4` and
contradicts the normative per-class `floor` rule — it is recorded and
rejected; the v3 `24,003 / 67,208 / 33.6×` figures were correct for
`A_word = 126` and are superseded, with historical files untouched.

## 3. Complete real-panel PRF surface

| Draw | Domain | Key |
|---|---|---|
| S1–S5 item padding (where not fixed) | `("L1","panel", world_slot, stratum, item, side, cell_identity, "pad")` | escrow-secret seed |
| S1–S5 word rank (all strata; S4 with fixed padding) | `(…, "rank")` | escrow-secret seed |
| Panel ordering | `("L1","panel", world_slot, "order")`-class domains | escrow-secret seed |
| Encryption salt, plaintext | escrow protocol (v3 §10 / v3.1) | escrow-secret seed / escrow env |
| Dummy/test panels | same skeleton under the declared test-only seed | test-only; cannot emit or attest a real artifact |

Everything else (allocation, pool reserve, zone-1 realizations, member
inits, shortlists, replay, controls, feasibility) remains on the public
root exactly as C3 fixed it. Public reservation geometry reproducible;
real panel words and order unreconstructible from the public root.

## 4. Unchanged author tokens

1. `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`
2. `I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`
   (alternative: `I_REJECT_LEVEL1_CYCLIC_CERTIFICATE`)
3. `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` — v3 incorporating v3.1,
   v3.1.1, **and v3.1.2**.

## 5. Requested final bounded confirmation

**To Opus:** confirm F-1's re-scoped verifier (declared family, exact
exemption rule with emitted reconstruction proofs, retained `n`-free
check), F-2's exact figures (`24,507 / 17,212 / 68,848 / 34.424×` — note
this corrects the check's own `68,620` approximation), and F-3's
five-stratum secret-keyed domains — as the three bounded repairs you
required, with no design reopening.

**To Sol:** confirm that F-2's count reconciliation and F-3's
secret-keyed realization surface leave your approved randomization,
inference, census, and surface conclusions untouched, and that your
three minor test notes are adequately carried as gate-3 obligations.

No design element is reopened by either request.

## 6. Confirmation

No code was written; no entropy was drawn; no datum, feasibility run,
comparative scout, N3 selection, lock, escrow, or outcome was created;
no constant derives from any observed comparison. The world, S4
construction, 24-pair frame, adjacent-only distance-1 scope,
operational-certificate meaning, learner, endpoint, estimand, inference
family, selector, gate order, and every signed negative destination are
preserved verbatim — including: a certificate failure is censoring,
never evidence the learner lacked `n`; UNKNOWN/all-censored is never
equivalence, boundary, or success; development contrasts are non-citable
forever. **Author signature is not authorized by this memo**; it follows
only the bounded reviewer confirmation.
