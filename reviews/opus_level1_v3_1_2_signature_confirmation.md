# Opus 4.8 X-line — Level 1 v3.1.2 bounded signature confirmation

Reviewer: Opus 4.8 (adversarial, bounded to F-1/F-2/F-3 only). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`, against my
v3.1.1 final check, Sol's v3.1.1 check, and Fable's v3.1.2 closure. No accepted
design element is reopened. This confirmation authorizes no implementation,
entropy, feasibility, scout, lock, escrow, or outcome. F-1 and F-2 were recomputed
independently.

---

## Verdict

**`REVISE_LEVEL1_V3_1_2_BOUNDED_TEXT`**

**F-1 is closed. F-2 is closed and its arithmetic is exactly right.** **F-3 closes
the panel-domain and confidentiality structure but leaves two bit-level
ambiguities** that let two conforming implementations produce different sealed
panels: the collision-redraw counter surface and the `cell_identity` serialization.
Both are one-sentence fixes, supplied below. Nothing else is reopened.

---

## Findings

### Closed

- **F-1 — verifier is now satisfiable and honest.** The re-scoped verifier keeps
  exact marginal identity for the seven declared non-structural fields, **exempts
  any combination from which `d` is deterministically reconstructible on the S4
  support** (`(padding, ordered lengths)`, `(padding, total length)`, and every
  superset), **emits the reconstruction map** per exempt combination, and retains
  the exhaustive non-`d` check. Independently confirmed (below): over every
  marginal, pair, and triple of the declared family, **the only separating
  combinations are exactly the `d`-reconstructing ones** — so the exemption is
  complete and no non-exempt field or combination separates the labels. The
  operational-certificate boundary, construction, padding table, and token are
  unchanged.

- **F-2 — exact counts confirmed.** Recomputed from the per-class floor rule with
  endpoints in `[−128, 128]`, `|d| ≤ 125`: total **24,507**, reserved
  `Σ_d ⌊3·N_d/10⌋ = 7,295` (residue sum **571** confirmed), non-reserved
  **17,212**, flat `×4 = 68,848 = 34.424× B`. This correctly supersedes both the
  old v3 `A_word=126` figures (`24,003 / 67,208 / 33.6×`) and my prior
  `68,620 / 34.3×`, which was the global `round(0.7·24,507)×4` approximation and is
  **not** compatible with the per-class floor — the correction is right to label it
  non-normative.

### Blocking (bounded text — F-3)

- **B-1 — collision-redraw counter surface is ambiguous.** Each item's word is
  built from several owned domains (`u`-pad, `u`-rank, `v`-pad, `v`-rank; for S4
  only the two `rank` domains). "A collision-rejection redraw increments only that
  domain's counter" has no single referent for a **pair** `(u,v)` collision — two
  implementations could redraw `u`, redraw `v`, or redraw both, producing different
  panel words and therefore different sealed escrow. Pin the redraw surface.

- **B-2 — `cell_identity` serialization is under-specified for S4.** The domain
  `("L1","panel", world_slot, stratum_id, item_id, side, cell_identity, purpose)`
  encodes each component by the A2 rule (`uint16_be(len)‖UTF-8`, integers as
  decimal ASCII), which covers integers and strings but **not** the S4
  `cell_identity = (a,b)` endpoint *pair*. Whether it is one composite component or
  two consecutive integer components changes the PRF input and the drawn word.
  Pin the encoding.

---

## Answers to the required confirmations

### F-1

Confirmed on all four points. The re-scoped verifier **no longer requires identity
of any `d`-reconstructing surface** (exemption clause), **mechanically classifies
exemptions and emits reconstruction maps** (dependency-proof clause), and my
exhaustive scan shows **no non-`d`-reconstructing declared marginal/pair/triple
separates the labels** — every separator (the two base pairs and their nine
supersets) reconstructs `d`. The operational-certificate boundary is unchanged.

On the executability question: **"no fixed `n`-free rule" is executable over the
closed tested family, not an unbounded universal claim.** Item 4 scopes it to "the
declared family" — the seven fields and their finite marginal/pair/triple
combinations — which is a finite, decidable check (each combination tested for
above-chance separation). It is not, and must not be read as, a claim that no
function whatsoever over all raw bytes can separate — that would be unverifiable.
The correction's wording ("exhaustive over the declared family") is the right,
bounded formulation; keep it explicit.

### F-2

Confirmed exact: **24,507 / 7,295 / 17,212 / 68,848 / 34.424× B**. Explicitly
acknowledged: this supersedes both the old v3 figures and my own global-70%
approximation (`68,620`), which was not normative; the per-class-floor value
`68,848` governs. Exhaustion remains impossible (34.4× headroom).

### F-3

Confirmed at the structural level: every S1–S5 raw panel realization and the panel
ordering are **secret-keyed** (the escrow-secret seed), **unreconstructible from
the public root** (the `("L1","panel",…)` domain is absent from the public-root
list; the categorical prohibition bars reusing any public zone-1 word as a panel
word), while the **public reservation geometry stays reproducible** (eligibility +
lowest-canonical-rank selection from the public reservation). Dummy panels cannot
attest a real artifact. The common domain skeleton, canonical per-item draw order
(`u`-pad, `u`-rank, `v`-pad, `v`-rank; items in panel-id order; strata S1–S5), and
owned per-domain counters are otherwise bit-exact.

The two residual ambiguities (B-1, B-2) are the only bit-level divergence surfaces.

---

## Exact bounded replacement sentences (adopt verbatim; no design change)

- **B-1 (collision redraw):** "On a duplicate `(u,v)` within an item, `u` and both
  pad draws are held fixed and **only the `v`-side `rank` domain's counter
  advances**, redrawing `v` until `(u,v)` is novel; no other domain is re-drawn on
  a collision, and exhaustion of the `v`-side word set (impossible under the A3
  availability proof) is design invalidity."

- **B-2 (`cell_identity` encoding):** "`cell_identity` is serialized as its
  canonical integer rank for S1/S2/S3/S5, and for S4 as **two consecutive integer
  components `a` then `b`** (each decimal ASCII under the A2
  `uint16_be(len)‖bytes` rule), never as a single composite token."

With these two sentences added to F-3, the three repairs are complete and the
document is confirmable.

---

## Authorization and negative space

This is a `REVISE`: **no author signature is authorized** until B-1 and B-2 are
adopted; on adoption, a bounded re-confirmation authorizes only Kirill's three
signatures (`I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`,
`I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE`,
`I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC`) — never implementation or execution.

Preserved and unweakened: adjacent-only distance-1 detector scope and the thin
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; the 24-pair frame and census reading;
`PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation; C1 a non-core modifier; the
operational-modulus certificate meaning (a pass is that competence only; a failure
is censoring, never evidence the learner lacked `n`); `UNKNOWN`/censored never
success; RANDOM-superior an anomaly, never a C1 rewrite; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever.

**No Level 1 execution is authorized by this confirmation.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
