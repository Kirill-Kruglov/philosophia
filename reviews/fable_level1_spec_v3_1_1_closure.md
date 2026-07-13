# Fable 5 — Level 1 v3.1.1 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`;
v1–v3.1 preserved unchanged; v3 + v3.1 carry forward except where the
correction explicitly replaces them. Inputs: Opus signature check
(`REVISE_LEVEL1_V3_1_ADDENDUM`) and Sol signature check
(`REVISE_LEVEL1_V3_1_INFERENCE`).

## Verdict

**READY_FOR_LEVEL1_AUTHOR_SIGNATURE**

The one scientific blocker (Opus C-1, the S4 joint-XOR leak) is closed
at the source — the offset-only construction has no symmetric items, so
the XOR channel's first input is constant, and the `±4` class spacing
makes every side parity label-constant; the joint feature-null verifier
now tests the full nuisance vector and every low-order combination. The
two generator gaps and all four Sol corrections are landed as exact
text. The certificate's meaning is honestly narrowed to an operational
modulus competence and routed to its own authorial token. No
implementation or scientific choice remains open; the three-token
packet is signable.

## 1. Finding-by-finding disposition

### Opus (signature check)

| Finding | Disposition | Correction |
|---|---|---|
| C-1 S4 joint `XOR(split, side_parity)` leak; marginal verifier insufficient | **Adopted via the mandated construction**: all symmetric items removed; `(a,b) = (c+k, −(c−k))`, `k ∈ {±1}`; differences `2n, 2n∓4` keep all class centers at one parity, so side parity is label-constant and the XOR channel has no varying input; joint-multiset verifier over the full declared nuisance vector + pairwise/triple combinations; the honest scoped meaning (operational modulus certificate) stated and routed to Kirill as its own token, exactly as the review's escalation demanded | C1 |
| MJ-1 allocation domains not bit-reproducible | **Adopted**: independently scoped domains `dev/h`, `role/pair_slot`, `sample/N3/h`; per-domain counters from zero; rejection increments only its own counter; `U(1)` consumes nothing; canonical `h = 1,2,3`, ascending pair slots | C2 |
| MJ-2 S4 words under-specified | **Adopted**: exact panel-specific PRF domain (world slot, item, side, displacement, fixed padding) with the existing unbiased rank draw and within-S4 collision rejection — keyed by the escrow-secret seed per C3 | C2, C3 |
| mn-1 `fan_in` enumeration; torch build | **Adopted**: full per-tensor enumeration (embeddings 128, QKVO 128, `W_in` 128, `W_out` 512, head 128); big-endian `uint64` decode stated; enforced build string `2.9.1+cpu` pinned with amendment rule; shape/seed/group tests required | C4 |
| mn-2 S5 length-constrained consumption | **Adopted**: eligibility (`|displacement| ≥ 90` where `≥ 100` lengths are required) precedes lowest-rank selection; fail-closed exhaustion enumerated | C2 |

Opus's O3/O4 confirmations (A5–A9 landed) are not reopened.

### Sol (signature check)

| Finding | Disposition | Correction |
|---|---|---|
| Major 1 allocation stream order | **Adopted** — identical repair to Opus MJ-1 (explicit stratum/pair components chosen over the single-counter alternative) | C2 |
| Major 2 "fails at 24" unreachable | **Adopted**: statistical precision always passes at the census; the branch is withdrawn; lock remains blockable only by resource/process/feasibility/signed-refusal routes, named as non-statistical | C6 |
| Major 3 `B²` conflation | **Adopted**: named as Popoviciu's finite-population cap, not the two-point sample-variance maximum (`2B²`); observed nonzero `s²_dev` always used as observed | C6 |
| Major 4 all-`v_h = 0` df bypass | **Adopted**: `[Δ̂, Δ̂]` directly, no df/quantile evaluation, mandatory "estimated zero sample variance, not census certainty" label | C6 |
| Minor 1 witness scope | **Adopted**: process-facts-only attestation, no independence claim | C3 |
| Minor 2 root visibility | **Adopted**: public immediately after the durable draw; panel domains removed from the public root and re-keyed to the escrow-secret seed — the A4 surface statement is now unambiguous | C3 |
| Minor 3 slot canonicalization in tests | **Adopted**: canonicalize-then-compare defined; required test that canonicalization is the only difference | C5 |

Nothing in either review is unaddressed or silently dropped.

## 2. Exact replacement index

| Correction | Replaces |
|---|---|
| C1 | v3.1 A1 (construction, meaning, verifier); v3 §3 constants `A_word`/word length/input rows and dependent inequalities, panel S4 row, edge proofs, affected tests |
| C2 | v3.1 A2 allocation-domain lines; A3 S4-realization gap and S5 consumption rule; A3 decoder note |
| C3 | v3.1 A2 domain list (panel entry removed); adds the two-key surface table |
| C4 | v3.1 A5 length/position values; adds `fan_in` table, decode rule, build pin, tests |
| C5 | v3.1 A7 byte-identity sentence |
| C6 | v3.1 A9 zero-variance, N3-at-24, and fallback prose |
| C7 | v3.1 A10 signature-packet line and gate order |

All other v3/v3.1 content carries forward unchanged.

## 3. Algebraic verification of the new S4 (both edges)

- Differences `{2n − 4, 2n, 2n + 4}`: remainders mod `n` are
  `{n − 4, 0, 4}`, nonzero for negatives at every `n ∈ [66, 125]`.
- Uncontactability: min `2·66 − 4 = 128 > d_acq = 125`. Realizability:
  max `2·125 + 4 = 254 ≤ 2·A_word = 256`; largest endpoint `n + 3 ≤ 128`
  (`n = 125`, NO-high: `(128, −126)`); largest side length
  `n + 7 = 132 ≤ 138`.
- Parity: sides ≡ `c + 1 ≡ n + 1 (mod 2)` for all 16 items —
  label-constant; symmetry indicator constant; `||a| − |b|| = 2`
  constant; `k` balanced 2:2 per class.
- Padding/length: label-conditional padding-vector multisets identical
  (`A ⊎ A+(1,1)` both sides); total-length multisets identical
  (`2n + {4,6,6,8,8,10,10,12}` both); ordered side-length multisets
  identical (the `c ∓ 2` shift cancels against the `p ± 1` shift:
  NO-low ≡ YES-A rows, NO-high ≡ YES-A′ rows).
- One construction covers the whole registry — no edge-world special
  table remains.

**Certificate scope (precise):** S4 certifies that the learner
*recovered a contact-anchored modulus value sufficient to classify
previously uncontactable opposite-corner differences `2n` vs `2n ± 4`* —
operational competence only; it does not distinguish an abstract period
representation from recovered-`n`-plus-arithmetic (raw observables
determine `d` by construction). Pass = evidence for that competence;
failure = censoring, never evidence the learner lacked `n`.

## 4. Public-root vs escrow-secret surfaces

| Surface | Key | Pre-outcome visibility |
|---|---|---|
| Allocation (dev/role/sample), pool reserve + zone-1 realizations, member inits, shortlists, replay, shuffled controls, feasibility | public root (one-shot OS-CSPRNG, committed transcript) | public immediately after durable draw |
| Real panel content, S4/panel realizations, panel ordering, encryption salt, escrow plaintext | 256-bit escrow-secret seed, generated once inside the locked escrow environment | sealed; released only at authorized outcome |
| Dummy/test panels | declared test-only seed | public; mechanically unable to emit a real artifact |

Witness attestation covers process facts only; no cryptographic
independence is claimed anywhere.

## 5. Final bounded questions

**Opus:** (1) Does the offset-only construction eliminate the joint
channel to your standard — specifically, is there any residual function
of the declared surface fields (excluding the `d`-reconstructing set)
that separates labels at any `n`? (2) Is the panel-specific,
secret-keyed S4 word draw the closure you intended for MJ-2?

**Sol:** (1) Does the two-key split (public root vs escrow-secret panel
seed) keep your S1 randomization repair intact while resolving your
Minor 2? (2) Are the C6 texts the exact bounded corrections you
required, with no residual statistical branch you would rewrite?

## 6. Implementation/gate authorization and confirmation

After the final bounded check and all three signatures: gate-3
implementation of the exact generators/model + verifiers (now including
the joint feature-null and slot-canonicalization tests); then the
reviewed one-shot **public-root** driver (single execution); then
optional reviewed feasibility; comparative scout; N3/census + lock;
**secret real-panel escrow**; outcome — in that order, nothing skipped.
Before signatures: only the previously authorized neutral parameterized
substrate on dummy fixtures (allocation bookkeeping now unblocked by C2's
reproducible domains, per Opus's gate note).

**Confirmation:** no code was written; no entropy was drawn; no
feasibility or comparative datum, scout, escrow, lock, or outcome was
created; no constant derives from any observed comparison. The 24-pair
frame, adjacent-only distance-1 scope, total selector, `PROOF_CORE`/
`PROOF_STRONG` layers, C6-as-annotation, and every signed negative
destination are preserved verbatim — including: a certificate failure is
censoring, never evidence the learner lacked `n`; UNKNOWN/all-censored
is never equivalence, boundary, or success; development contrasts are
non-citable forever.
