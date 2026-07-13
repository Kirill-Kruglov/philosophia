# Opus 4.8 X-line — Level 1 dummy panel implementation audit

Reviewer: Opus 4.8 (X-line implementation auditor). Repository:
`/home/master/llm_projects/philosophia` (uncommitted working tree; not committed).
Audited: `src/philosophia/level1/{world,serialization,pool,panel}.py`,
`tests/test_level1_{substrate,panel}.py`, against the signed v3 + v3.1.1–v3.1.3
corrections, the v3.1.4 panel amendment, and v3.1.4.1. Independent recomputation
was performed for the edge crossings, per-stratum YES counts, S4 labels, reserved
uniqueness, and the S4 exemption count. This audit authorizes no entropy, real
panel generation, feasibility/scout, N3 selection, lock, escrow, learner
trajectory, or outcome.

---

## Verdict

**`REVISE_LEVEL1_DUMMY_PANEL_IMPLEMENTATION`**

The shipped code is **correct and bit-faithful to the signed contract** — I found
no correctness defect, no ambiguity by which two contract-conforming implementers
would diverge, and no unauthorized path. Tests and the verifier pass cleanly. The
revision is **regression-coverage only**: three test gaps let a shape-/count-correct
but scientifically or byte-different refactor pass, and for an escrow-bound
bit-exact artifact those must be closed before commit. The implementation may be
committed once the three regression tests below are added.

**Environment results**
- `pytest tests/test_level1_panel.py tests/test_level1_substrate.py -q` → **14 passed**.
- `pytest -q` → **115 passed**.
- `scripts/verify_all.py` → **VALID / VALID / OK**, exit 0.

**Independent recomputation (all confirmed)**
- Per-stratum YES over 60 worlds: S1 0, S2/S3/S4/S5 8 each → **32 YES / 156 NO**.
- Non-S4 zone-3 crossings: exactly `(124,S5,126)`, `(125,S2,126)`, `(125,S5,127)`.
- Reserved reuse: **0 worlds**. S4 at `n=125`: `250×8` YES, `246×4`+`254×4` NO.
- S4 exemptions: **11**, per-world (n=66/100/125) and pooled, with **no non-`d`
  separator raised** — matching the reviewed 11.
- Entropy/real-key/escrow/outcome grep over `level1/` + `scripts/`: **none**.

---

## Findings

### Critical
None.

### Major (regression coverage — mandatory before commit)

- **PI-1 — the reserved-cell selection rule is not pinned by a golden value.**
  `panel.py:60,72–79` implement "lowest unused global A3 canonical rank, eligible,
  consumed in ascending global panel id" correctly, but no test asserts the exact
  `cell_identity` chosen for any S1/S2/S3/S5 reserved item. A refactor that changed
  the tie-break (e.g. highest rank, or per-stratum instead of global "unused")
  would produce a **different escrow panel** yet still pass every test
  (labels, counts, uniqueness, and `verify_dummy_panel` are all invariant to which
  eligible reserved cell is chosen). For a bit-exact escrow artifact this is a
  reproducibility hole.

- **PI-2 — the secret-drawn panel words are not pinned by a golden hash.**
  `panel.py:178–205` draw each word by `U(word_count)`; only *determinism* is
  tested (`test_all_world_dummy_enumeration_is_deterministic`), not the exact
  bytes. Two implementations that both run deterministically but derive the rank
  domain or draw order differently would each pass. The existing golden coverage
  stops at the PRF/allocation layer (`test_prf_and_allocation_golden_values`); it
  does not reach panel content.

- **PI-3 — the S4 feature-null verifier is never tested against a known-bad
  construction.** `panel.py:319–362` correctly raises on a non-`d` separator and
  asserts exactly 11 exemptions, but it is only ever invoked on the *good*
  construction (via `build`). A refactor that weakened the verifier (e.g. dropped
  the `len(differences) != 1` raise) paired with a leaky S4 table could pass, since
  no test feeds a deliberately separating (e.g. v3.1-style parity-XOR) S4 fixture
  and asserts `ValueError`. This is the sole scientific guard on S4's operational
  certificate and deserves an independent negative test.

### Minor

- **PI-4 — draw-order note (no defect).** The F-3 realization order is
  "`u`-pad, `u`-rank, `v`-pad, `v`-rank"; `panel.py:88–95` computes both pads
  (`_paddings`) then both ranks (`_words`). Because every draw uses an independent
  domain/counter (`_identity_domain` splits on `side` and `purpose`), the output
  bytes are identical to the contract order — but a one-line comment asserting this
  equivalence would prevent a future reader from "fixing" it into a shared counter.

---

## Answers to the required audit questions

1. **Ids/counts/differences/zones/labels/selection/padding/collision/order match
   v3.1.4+v3.1.4.1 for all `n`?** Yes. Global ids `0–187` per stratum
   (`panel.py:101–146`), differences and zones as tabled, labels verified against
   `d % n == 0` (`panel.py:276`), positive-`v` padding for S3·YES and the zone-3
   edge groups (`panel.py:169`, `positive_v` flags at `:110,:116,:136`), fixed
   S5/S4 paddings, collision per stratum. Independent enumeration confirms counts,
   YES totals, and the three crossings.
2. **Global ranks / zone-3 identities canonical, invertible, no reuse?** Yes.
   `global_cell_rank`/`cell_from_global_rank` are inverse
   (`test_global_cell_rank_round_trip`); zone-2 identity = one integer rank, zone-3
   = `(a,b)` (`panel.py:87`, checked at `:278–281`); reserved reuse impossible
   (`used_reserved` set at `:76–78`; `verify_dummy_panel:261–265`; recomputed 0).
3. **B-1 collision handling correct, exhaustion checked against the true `v`
   universe?** Yes. `_words` (`panel.py:178–205`) draws `u` once, holds both pads
   fixed, advances only the `v`-rank stream in the redraw loop, blocks exactly the
   registry pairs sharing the current `left` in the current `(cell.b, padding_v)`
   space (plus `u≠v` for S3·YES), and raises when `len(blocked) >= word_count(b,
   padding_v)` — the true admissible `v` count — **before** the loop, so it cannot
   spin. Positive-`v` guarantees `|W(v)| ≥ 2`.
4. **Public-root/panel domains byte-exact under A2/F-3/B-2?** Yes.
   `_identity_domain` (`panel.py:152–157`) emits
   `("L1","panel",world_slot,stratum,global_id,side,*identity,purpose)` with
   `identity` splatting to one int (zone 2) or two ints (zone 3, B-2), each encoded
   by the A2 `encode_component`; the F-3 `item_id` is the global zero-based id;
   `pad`/`rank` × `u`/`v` are four independent owned counters.
5. **S4 preserved; feature-null verifier independently correct?** Yes.
   `_add_s4` (`panel.py:207–237`) reproduces the v3.1.1 C1 endpoint splits, fixed
   paddings (`p_v ∈ {1,2,3}`), two-int identity, and the label self-check. The
   verifier exempts a separating combination **only** when every feature-value maps
   to a unique difference (reconstructs `d`) and otherwise raises; I independently
   reproduced exactly **11** exemptions and no non-`d` separator at n=66/100/125 and
   pooled. (Coverage gap PI-3: no negative fixture.)
6. **Schema surface world-independent without false content byte-identity?** Yes.
   `panel_schema_surface` (`panel.py:308–316`) hashes only `global_id`, `stratum`,
   `local_id` — never words, cells, labels, ciphertext, or content digests — and
   `verify_all_dummy_worlds:299–301` asserts a single surface across 60 worlds. No
   encrypted-content byte-identity is claimed (the dummy builder does no
   encryption).
7. **Mechanically dummy/test-seed only?** Yes. `DummyPanelBuilder.__init__`
   (`panel.py:49–56`) raises `PermissionError` unless both keys are `test_only`
   with the right purpose; `dummy_key` derives from a fixed `"L1-TEST-ONLY/…"`
   string; grep finds no `secrets`/`urandom`/`token_bytes`/`getrandom`, no real key
   constructor, no panel writer/encryptor, and no escrow/learner/scout/lock/outcome
   path in `level1/` or `scripts/`.
8. **Could a shape-/count-correct but wrong refactor pass?** Yes — three routes,
   each a missing regression test: PI-1 (reserved tie-break), PI-2 (secret word
   bytes), PI-3 (verifier weakening). Named and required below.
9. **Any choice exceeding authorization or reopening a negative destination?**
   No. The builder is dummy-only; `verify_dummy_panel` enforces label truth, no
   acquisition-cell reuse (`:272–275`), and zone/identity consistency; nothing
   reopens the operational-certificate scope, the sole S4 tooth, or any signed
   negative destination.

---

## Exact mandatory edits (regression tests; no source change required)

1. **PI-1:** add a golden test asserting the exact `cell_identity` (canonical
   integer rank) of representative S1/S2/S3/S5 reserved items for at least one
   non-edge world and both edge worlds (`n ∈ {66, 124, 125}`).
2. **PI-2:** add a golden test over a fixed dummy `(public, panel)` key pair that
   asserts a stable digest of one full built panel's `(left, right)` bytes for a
   fixed world — locking the exact secret-word draws (this simultaneously pins
   PI-1).
3. **PI-3:** add a negative test that feeds a deliberately label-separating,
   non-`d`-reconstructing S4 feature fixture (e.g. a v3.1-style
   `parity`/`symmetry`-XOR table) to the feature-null verifier and asserts it
   raises `ValueError` — pinning the verifier's rejection behavior independently of
   the good construction.
   (Optional: PI-4 comment.)

**Committable:** yes, once PI-1–PI-3 are added. The current source is correct and
faithful; the commit should include the source and the strengthened tests
together.

---

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its **sole
S4 tooth** (offset-only, joint feature-null intact and independently reproduced at
11 exemptions); S2/S3/S5 carry no anti-lookup authority; the public-reservation /
secret-realization confidentiality boundary (`verify_dummy_panel` forbids any
public acquisition cell in the panel); `PROOF_CORE`/`PROOF_STRONG` and
C6-as-annotation; `UNKNOWN`/censored never success; a certificate failure is
censoring, never evidence the learner lacked `n`; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever; Level 1
never evidence for `PROOF_CORE`.

**No entropy, real panel generation, feasibility/scout, N3 selection, lock,
escrow, learner trajectory, or outcome is authorized by this audit.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
