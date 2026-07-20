# Opus 4.8 X-line — Officina WP-3 population/construct contract review

**`REVISE_OFFICINA_WP3_CONTRACT`**

Reviewer: Opus 4.8 (X-line, adversarial implementation/fidelity stance).
Repository: `/home/master/llm_projects/philosophia`, WP-3 draft at `2bc781d`
(HEAD differs only by review prompts). **I created no entropy, world, sample,
panel, candidate, ledger event, root, lock, escrow artifact, datum, or outcome;
T remains `NOT_ACTIVATED`; I activated no T/Q/C process. Nothing committed; no
existing file edited.** I ran static frame recomputation (Python), the inactive
bootstrap verifier, and a bootstrap-integrity check — reported precisely in §9.

The world-side design is coherent and charter-faithful — finite frame, retained
adjacent-donor yoke, deferred WP-6/WP-9 numerics — but the contract is **not
bit-exact**: its own signed frame section prints an enumeration that contradicts
its normative rule and would violate T/Q/C disjointness, and it is byte-exact
only for the recommended CH-1a+CH-2a combination. A bounded Fable revision is
required before CH-1/CH-2 are reviewable for author selection.

---

## Disposition of the arithmetic counterexample (mandate item 1)

**Confirmed, and it is Critical.** From the normative rule (§3): `b_p =
{24+2p, 25+2p}`, `h(p)=⌈p/5⌉`, `j(p)=p−5(h−1)`, Q-reserve `= j∈{2,4}`. The
Q-reserve blocks are `p∈{2,4,7,9,12,14,17,19}`, giving

```
Q (rule)   = {28,29, 32,33, 38,39, 42,43, 48,49, 52,53, 58,59, 62,63}
```

which **equals the prompt's implied set exactly**. The draft §3 (line 119)
instead prints

```
Q (printed)= {28,29, 32,33, 40,41, 44,45, 50,51, 54,55, 60,61, 64,65}
```

whose upper twelve worlds `{40,41,44,45,50,51,54,55,60,61,64,65}` are the moduli
of `p∈{8,10,13,15,18,20}` — which the same document assigns to the **C frame**
(`j∈{3,5}`, §3 line 116). So the printed Q-reserve **overlaps the C frame in 12 of
16 worlds**. Consequences: (i) the `officina.frame.v1` document is not
byte-reproducible — an implementer computing from the rule and one transcribing
the printed list diverge, and the frame SHA that "binds every later generator"
differs; (ii) if the printed list were taken as authoritative, **T/Q/C
disjointness fails catastrophically** (Q≡C on 12 worlds) — a candidate qualifying
on a "Q" world that is simultaneously a C target, the exact leakage the phase
architecture exists to prevent. The **rule is correct**; the print is a
transcription error, and with the rule-corrected set the partition is clean
(`Q∩C=∅`, `|Q|=16`, `|C|=24`, union = all 40). **CH-2b recomputed independently:**
Q-reserve `p∈{1,2,4,6,7,9,11,12,14,16,17,19}` → 24 worlds
`{26,27,28,29,32,33,36,37,38,39,42,43,46,47,48,49,52,53,56,57,58,59,62,63}`; C
frame `p∈{3,5,8,10,13,15,18,20}` → 16 worlds
`{30,31,34,35,40,41,44,45,50,51,54,55,60,61,64,65}`; disjoint, `N_h(C)=2` per
stratum. The draft's §4 (`N_h=3`) is therefore also inconsistent with CH-2b (see
W3-M1). **The frame is not signature-ready until this is corrected.**

---

## Findings

### Critical

- **W3-C1 — §3 printed Q-reserve contradicts the rule and overlaps the C frame
  (line 119).** As adjudicated above. **Mandatory repair:** replace the printed
  Q-reserve with the rule-derived set
  `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` (CH-2a) / the CH-2b set
  above; add a full `(p, h, j, b_p, assignment)` enumeration table; and add a
  machine-checkable `Q ∩ C = ∅` and `Q ∪ C = band` assertion the WP-4 frame
  generator must satisfy before emitting `officina.frame.v1`.

### Major

- **W3-M1 — the contract is bit-exact only for CH-1a+CH-2a; the open cells are
  not parameterized (§3 lines 108, 124; §4 lines 143-150).** The band→block
  formula is stated only as `{24+2p,25+2p}` (specific to `[26,65]`); under
  CH-1b=`[126,165]` it must be `{124+2p,125+2p}`, but no generic form is given.
  §4 hard-codes `N_h=3`, `π_h=n_h/3`, `W_h=1/4`, `FPC=(1−n_h/3)`, census at
  `n_h=3` — all CH-2a-specific; under CH-2b, `N_h=2`, `π_h=n_h/2`,
  `FPC=(1−n_h/2)`, census at `n_h=2`. Since CH-1/CH-2 are **open** author cells,
  three of four admissible combinations are under-specified. **Mandatory:**
  give generic formulas parameterized by the open cells — `b_p = {(L−2)+2p,
  (L−1)+2p}` for band start `L`; `N_h = |C-frame|/4`, `π_h = n_h/N_h`,
  `W_h = 1/4`, `FPC = 1−n_h/N_h`, census at `n_h=N_h` — so the frame bytes and
  C-measure are fully determined for **every** (CH-1, CH-2) choice.

- **W3-M2 — the `officina.frame.v1` canonical-JSON schema is unspecified (§3
  lines 124-127).** The document is content-addressed and "binds every later
  generator," yet no exact schema (field names, value types, key/enumeration
  order, which derived values are included) is given; "a future implementation
  will choose a schema" is not closure. **Mandatory:** specify the exact
  canonical-JSON schema so two implementations reproduce the SHA from the
  contract alone (leveraging the WP-2 canonical-JSON library conventions).

- **W3-M3 — oracle/query byte grammar under-specified; PAD/SEP conflated with
  world semantics (§2 lines 74-75, 80-82).** (a) The typed refusal has no fixed
  byte representation; (b) the query wire format consumed by the oracle
  (SEP placement, padding, ordering of `(u,v)`) is not pinned; (c) `PAD (0x5F)`
  and `SEP (0x7C)` do **not** enter `disp(w)=#R−#L`, so they are serialization
  constants, **not** world semantics, yet §2 lists them as construct
  serialization. **Mandatory:** pin the typed-refusal value and the exact
  oracle-input serialization; state that the oracle is defined on `{R,L}`
  displacements only and that `SEP`/`PAD` are learner/WP-9-panel encoding
  constants that are **not oracle-visible** (mandate item 3).

- **W3-M4 — the "pure function of (n, query)" oracle plus a public frame leaves a
  caller-supplies-`n` route open (§2 line 74; §11 lines 342-347).** The moduli
  are **public**, so quarantine cannot rely on secrecy; the load-bearing barrier
  is the surface-capability gate. The contract states "no T surface may generate
  a frame/reserve modulus" but does not forbid a raw arbitrary-`n` oracle/world
  API by which a T candidate could instantiate an oracle for a C modulus (e.g.
  `n=40`) and contact a frame world during open T. **Mandatory (WP-3 text):** the
  oracle is instantiable **only** through the surface-capability-gated world
  constructor — T receives oracles bound to T-dev-band worlds only; frame/reserve
  worlds arise only via sealed post-freeze (Q, WP-6) / post-lock (C, WP-10) roots
  — with no free arbitrary-`n` oracle on the T/Q surface. Enforcement is reviewed
  WP-4 code. (The alternate-import/forged-provenance/symlink routes are already
  discharged by the WP-1/WP-2 deny-by-default path policy and provenance
  registry.)

- **W3-M5 — frozen T-dev bands `[10,25]∪[166,205]` are unjustified and do not
  scale with CH-1 (§3 lines 120-123).** Because the whole frame band is
  partitioned into Q∪C (T holds no in-band membership), T development is forced
  entirely off the frame scale — a substantive **scale-extrapolation** design
  (candidates develop at `[10,25]∪[166,205]` and must qualify on frame-scale
  worlds they never trained on). The bands are frozen independent of CH-1, so
  their relationship to the frame is uncontrolled and asymmetric (under CH-1a:
  just-below + far-above; under CH-1b: far-below + just-above). **Mandatory:**
  either justify the bands as a deliberate, CH-1-coherent design — naming the
  extrapolation property and how the bands relate to each CH-1 band — or make the
  T-dev boundaries their own explicit author/design cell. Both CH-1 options yield
  disjoint constructions (verified), but the T-dev↔frame relationship must not be
  a hidden, CH-1-dependent side effect.

- **W3-M6 — public finite support + admitted symbolic solver narrow but do not
  break interpretability; the forbidden-language must foreclose over-claiming
  (§8 lines 230-236; §9.6 lines 273-281).** Under the selection-conditional claim
  both arms use the same promoted design, so C1 remains a well-defined
  online-responsiveness contrast **for that design** even if it is a
  divisibility/lookup solver — the estimand is **not** uninterpretable. But the
  finite public support admits shortcut solvers, so §8's forbidden list must be
  extended to bar any claim that the selected learner "acquired/represented the
  modulus," "learned the construct," or achieved "small-learner contact," absent
  a WP-6 candidate-admissibility constraint. That admissibility rule, if Kirill
  wants it, is correctly owned by **WP-6** (item 7 answer); do not legislate its
  content here.

### Minor

- **W3-m1 — §1:** state explicitly that the donor-ACTIVE transcript
  capture/replay mechanism and the budget `B` are WP-9 (the yoke topology and the
  instance-non-adapted property are correctly world-side and preserved).
- **W3-m2 — §5 (lines 171-176):** the "launches × sample-size ≤ 16" reserve bound
  is CH-2a-specific (≤ 24 under CH-2b); state it generically as
  `≤ |Q-reserve|`.

---

## Answers to the remaining audited surfaces

- **World/frame boundary (item 3):** pools, shortlists, acquisition, panels are
  correctly excluded as learner/WP-9 objects (§2 line 83-85), and WP-4 can still
  implement the world (oracle + frame + T-dev generation). The only defect is the
  PAD/SEP conflation (W3-M3) — they are serialization, not world semantics.
- **Quarantine/no-reuse (item 4):** routes belonging in **WP-3 text**: the
  surface-gated oracle/world constructor and the caller-supplies-`n` prohibition
  (W3-M4), the band-check fail-closed rule (present), realized-draw
  unpredictability (present, §9.6). Routes safely **discharged by reviewed
  WP-1/WP-2 code**: alternate imports, forged provenance, symlink escape,
  predecessor reads (path policy + provenance registry, already X-line-confirmed).
- **Ownership (item 8):** no WP-6/WP-9 numeric is accidentally fixed (`B`, arm set
  beyond the skeleton, margins, alphas, `n_h`, seed law, Q caps/`δ_Q` all
  deferred; §7's structural reserve bound is a world-side consequence, not a WP-6
  number). WP-3 world-side values **improperly deferred**: the frame-document
  bytes/schema (W3-M2), the generic block/measure formulas (W3-M1), the
  typed-refusal/query wire bytes (W3-M3). **No stopped-Level-1 outcome tuning:**
  confirmed — band, split, and `Λ` derive from registry-disjointness hygiene,
  equal-strata arithmetic, the `Λ=2·n_max+10` pattern, and the signed resource
  envelope; §9.8's attestation holds and I found no value traceable to the
  censored binaries or any comparative datum.

## Item 9 — verifier and bootstrap integrity

- `scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**.
- The WP-3 draft lives at `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_
  V1_DRAFT.md` (and its Fable memo), **not** under `successor/officina/`; the
  committed WP-3 change touches **0** files in the exact
  `successor/officina/` bootstrap set (`LINEAGE.json`, `PATH_POLICY.json`,
  `README.md`, `T_ENVELOPE.json`, `T_LEDGER.md`, `T_LEDGER.md.head.json`,
  `WP1_WP2_IMPLEMENTATION.md`), which remains unchanged and inactive.

## CH-1 / CH-2 reviewability and authorization

CH-1 and CH-2 are **not yet reviewable for author selection.** They become
reviewable only after W3-C1 (corrected enumeration + disjointness assertion),
W3-M1 (generic formulas for all four combinations), and W3-M2 (exact frame
schema) — because until then the frame bytes are undetermined for CH-1b and/or
CH-2b, so the author cannot select against a byte-exact frame. After those repairs
(and W3-M3–M6), the eligible packet would be
`I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT` **plus exactly one** of
`I_SELECT_OFFICINA_FRAME_BAND_LOW` / `..._HIGH` **and one** of
`I_SELECT_OFFICINA_SPLIT_C_RICH` / `..._Q_RICH` — **but I do not authorize
selection now.**

This review authorizes **only a bounded Fable revision** of the WP-3 contract
addressing W3-C1 and W3-M1..M6 (and the two Minors). It authorizes **no** author
selection, WP-4 implementation, entropy, world generation, T activation, Q/C
process, root, lock, escrow, datum, or outcome. After the bounded revision, the
exact revised delta requires a new focused X/Y confirmation; CH-1/CH-2 selection
follows that.

## Negative space

This review moved no scientific claim and predicts no qualification or outcome.
The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its C1 unrun and untested; v1/v2 non-comparable, non-citable, and choosing nothing
here (no band, split, `Λ`, or T-dev value derives from them). Officina's T and Q
can never earn, kill, or boundary-label C1–C6; S is unavailable; only a valid,
independently locked C execution may ever move an Officina claim, within its
selection-conditional scope, generalizing to the registered finite frame and
nothing wider. Censored/`UNKNOWN`/every invalid state are never success,
equivalence, a boundary, or learner impossibility. `PROOF_CORE`/`PROOF_STRONG`
remain earned by nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), selected no
open cell or token, and committed nothing. `essay/OUTLINE.md` untouched. My
actions were reading the governing files and running the static frame
recomputation, the bootstrap verifier, and the bootstrap-integrity check reported
above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
