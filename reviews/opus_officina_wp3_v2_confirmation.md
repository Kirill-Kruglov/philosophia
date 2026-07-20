# Opus 4.8 X-line — Officina WP-3 contract v2 confirmation

**`REVISE_OFFICINA_WP3_V2`**

Reviewer: Opus 4.8 (X-line, focused v2 confirmation). Repository:
`/home/master/llm_projects/philosophia`, v2 at `9f8bdc7` (HEAD differs only by
prompts). **I created no entropy, world, frame instance, sample, panel,
candidate, ledger event, root, lock, escrow, datum, or outcome; T remains
`NOT_ACTIVATED`; I ran no learner/T/Q/C process. Nothing committed; no existing
file edited.** I ran static frame recomputation for all four branches, a dummy
frame-JSON serialization probe, a v1-path existence check, and the inactive
bootstrap verifier — reported in "Checks run."

Every substantive v1/Sol repair is **closed and independently verified** — the
corrected enumeration, the branch-complete formulas and design table, the exact
frame schema, the capability invariant, the invariant T-dev rule, the OR
estimand, the transport premise, the depletion inequalities, and the multiplicity
rule. Two bounded defects remain that **prevent two independent implementations
from agreeing** and must not be waived: the §4 oracle refusal grammar is not
total/ordered, and the §1 governing v1-path reference is stale/nonexistent. A
bounded correction plus a focused re-confirmation is required before the token
packet is eligible.

---

## Findings

### Critical
None. W3-C1/Sol-1 is closed: the v1 printed list is withdrawn by name, and the
rule-derived enumeration, regression table, and pre-emission machine checks are
correct (verified below).

### Major

- **V2-1 — §4 oracle refusal grammar is not total or priority-ordered (mandate
  item 3; lines 180-184).** The typed refusal is `MALFORMED_QUERY_LENGTH`
  ("any side > Λ") **or** `MALFORMED_QUERY_BYTE` ("any byte outside `{0x52,
  0x4C}`"), with **no stated priority** for a query that is **both** over-length
  **and** contains an illegal byte — two legal implementations return different
  refusal bytes, so oracle transcripts (used for hashing/yoke) are **not
  byte-reproducible**. The taxonomy is also **not exhaustive**: malformed JSON, an
  object missing/adding a key, a non-string `u`/`v`, and non-canonical JSON are
  unclassified. Because `§4` is a WP-3 world-contract object and the oracle is
  declared a *pure total function with a typed refusal, never `false`*, this is a
  contract-completeness gap, not a WP-4 detail. **Mandatory edit:** give a
  **total, ordered** refusal classification over *all* inputs — e.g. a fixed
  precedence `MALFORMED_QUERY_STRUCTURE` (input is not exactly a canonical-JSON
  object with keys `{u,v}` whose values are ASCII strings) → `MALFORMED_QUERY_BYTE`
  (any byte outside `{0x52,0x4C}`) → `MALFORMED_QUERY_LENGTH` (any side `> Λ`) →
  answer — or any fixed order, stated as normative so the joint case and every
  edge resolve to one deterministic refusal. (The empty word `ε` is correctly a
  valid query, `disp(ε)=0` — no ambiguity there.)

### Minor

- **V2-2 — §1 governing v1-path reference is stale/nonexistent (mandate item 7;
  lines 4-5).** v2 cites the v1 draft as
  `successor/officina/WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md`, which **does
  not exist** (verified); the actual preserved v1 artifact is
  `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md` (top of
  `successor/`, filename prefixed `OFFICINA_`). A stale governing path must be
  repaired even though it is documentary. **Mandatory edit:** correct the path to
  the actual committed v1 artifact.

- **V2-3 — §3 `contract_sha256` must pin the exact hashed artifact (lines 157,
  166-169).** The field is "hex SHA-256 of the signed WP-3 contract bytes," but
  *which* bytes (the committed `.md` file, verbatim) is not stated. The hash is
  acyclic (the contract does not reference the frame) and resolves at signature
  via the signature record's hash pin — consistent with the project pattern — but
  for byte-reproducibility across two implementers the contract should state that
  `contract_sha256` equals the SHA-256 of the exact committed WP-3 contract file
  bytes named in the signature record. **Recommended edit:** one sentence pinning
  the artifact.

- **V2-4 — §5 "not primarily scale transfer" is generous (optional; lines
  220-225).** Under CH-1a a candidate developing on the near band `[10,25]` that
  qualifies on an upper-frame world (e.g. 60-65) *does* jump scale; the "adjacent
  scale" characterization is exact only at the frame's low edge. This is a design
  characterization, not a bit-exactness or disjointness defect; consider softening
  the wording. Non-blocking.

---

## Independent recomputation (mandate item 1) — CONFIRMED

Using the generic rule `p(h,j)=5(h−1)+j`, `b_{h,j}={n0+2(p−1), n0+2(p−1)+1}`, for
`n0∈{26,126}` and both splits, machine-recomputed:

| Branch | `|C|` | `|Q|` | `N_h` | `q_h` | `Q∩C=∅` | `Q∪C=[n0,n0+39]` | excl. `[66,125]` & T-dev |
|---|---:|---:|---:|---:|:--:|:--:|:--:|
| LOW × C-rich | 24 | 16 | 3 | 4 | ✓ | ✓ | ✓ |
| LOW × Q-rich | 16 | 24 | 2 | 6 | ✓ | ✓ | ✓ |
| HIGH × C-rich | 24 | 16 | 3 | 4 | ✓ | ✓ | ✓ |
| HIGH × Q-rich | 16 | 24 | 2 | 6 | ✓ | ✓ | ✓ |

The regression vectors match the contract exactly: CH-2a Q worlds
`{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` (= my v1-flagged corrected
set); CH-2b C worlds `{30,31,34,35,40,41,44,45,50,51,54,55,60,61,64,65}`; HIGH×C-rich
Q worlds `{128,…,163}`. §2b design rows are correct for both branches
(`W_h=1/4`; `π_h=n_h/3` vs `n_h/2`; FPC `1−n_h/3` vs `1−n_h/2`; census at
`n_h=3` vs `2`; claim-capable `n_h` 2..3 vs 2), and the small-stratum `n_h=1`
rule (unbiased point estimate but no within-stratum variance) is sound. **No
hand-copied list is authoritative; the rule governs and the §3 machine checks are
fail-closed.**

## Frame byte-reproducibility (mandate item 2) — CONFIRMED (with V2-3 note)

I instantiated `officina.frame.v1` for a dummy CH-1a+CH-2a selection using only
§3's schema (ASCII, sorted keys, minimal separators): field types and ordering
are fully determined, the derived arrays (`c_block_ps`, `q_worlds`) are
regression-checkable against the rule, `ch1_token`/`ch2_token` bind the selection,
and re-serializing the parsed object reproduces identical bytes and hash. The
`contract_sha256`→frame relation is **acyclic** (the contract never embeds the
frame hash). The only residual is V2-3 (pin the exact contract bytes). The
freeze/serialization relation between the signed contract and the selected tokens
is otherwise unambiguous.

## Capability invariant (mandate item 4) — CONFIRMED (contract level)

§4 closes the caller-supplies-`n` route at the contractual level: no public
arbitrary-`n` oracle/world constructor; construction only via surface-capability
objects; the T capability's band check refuses frame/reserve moduli fail-closed;
Q/C capabilities do not exist until their post-freeze/post-lock roots. The
enforcement remainder (constructor requires the capability object; no importable
raw arbitrary-`n` helper; T-surface refusal tests on frame/reserve moduli) is
correctly assigned to reviewed WP-4 code/tests, and the alternate-import /
forged-provenance / symlink routes are already discharged by the WP-1/WP-2 path
policy + provenance registry. A candidate *simulating* the construct for a known
public modulus is not a capability leak but the §6/W3-M6 shortcut concern
(admissible, scoped, over-claim-forbidden) — correctly separated.

## T-dev geometry (mandate item 5) — CONFIRMED, no author cell

§5's fixed `[10,25]∪[166,205]` is CH-1-invariant and coherent: disjoint from both
candidate frame bands and the predecessor registry under both branches; exactly
one band is contiguously adjacent to the frame in each branch (`25|26` for LOW,
`165|166` for HIGH) and the other is a named scale-stress surface; the
extrapolation property is named. This resolves W3-M5 without a hidden
CH-1-dependent side effect and needs **no** author cell (V2-4 is a wording note
only).

## Donor / shortcut / ownership (mandate item 6) — CONFIRMED

Donor transcript capture/replay, `B`, full arm definitions, endpoint, and
treatment implementation are WP-9 (§1); the typed observation `(X,Δ)` is WP-3
type-only. §6's extended forbidden language forecloses "learned the
modulus/construct/represents the group/small-learner contact" absent a WP-6
admissibility rule (not chosen). The §9 ownership table cleanly separates
WP-3 world-side values from WP-6/WP-9-10 numerics; the launch ceilings 4/6 are
derived world-side consequences ("conditional on the WP-6 coverage design"),
not selected numbers. **No later-phase numeric is selected here**, and §12's
no-stopped-line-tuning attestation holds (band/split/`Λ`/T-dev derive from
disjointness hygiene, strata arithmetic, the `Λ` pattern, and the signed
envelope).

## Answers to Fable's three Opus questions

1. **Frame byte-reproducible for all four branches?** **Yes** — verified for all
   four CH-1×CH-2 combinations from the contract alone; the rule governs,
   regression vectors check, the generator binds to the contract hash + selected
   tokens, and the machine checks are fail-closed; no hand-copied list is
   authoritative. One bounded caveat: pin the `contract_sha256` artifact (V2-3).
2. **§4 closes the caller-supplies-`n` route at the contractual level?** **Yes** —
   capability invariant + no public arbitrary-`n` constructor + Q/C capabilities
   nonexistent until their roots, with exactly the enforcement remainder
   (capability-object requirement + T-surface refusal tests) assigned to reviewed
   WP-4 code. (Independent of the separate V2-1 refusal-grammar gap.)
3. **§5's invariant T-dev rule resolves W3-M5 without a hidden cell?** **Yes** —
   no author cell is required; the near/distal structure is CH-1-invariant and the
   extrapolation property is named (V2-4 is a non-blocking wording note).

## Checks run (read-only)

- Static recomputation of all four CH-1×CH-2 branches (memberships, strata,
  cardinalities, `N_h`/`q_h`, `Q∩C=∅`, `Q∪C=band`, predecessor/T-dev exclusion) —
  all pass and match the contract's regression vectors.
- Dummy `officina.frame.v1` serialization probe (CH-1a+CH-2a) — canonical,
  byte-reproducible, acyclic hash.
- v1-path existence check — the §1 reference **does not exist** (V2-2); the actual
  v1 artifact does.
- `scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**; the exact
  `successor/officina/` bootstrap set is unchanged and the v2 commit touched **0**
  files under it (the v2 draft lives at `successor/OFFICINA_WP3_..._V2_DRAFT.md`).

## Packet eligibility and disposition

The five-token packet (`I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT` + one CH-1 + one
CH-2 + one OR + `I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE`) is
**not yet eligible** for Kirill's selection/signature: V2-1 leaves the oracle wire
contract non-byte-reproducible, and V2-2 is a stale governing reference. **A
bounded correction plus a focused X/Y re-confirmation is required — I do not waive
it.** This confirmation authorizes **only** the bounded Fable revision (V2-1 total
refusal ordering + exhaustiveness; V2-2 path fix; V2-3 `contract_sha256` pin; V2-4
optional wording). It authorizes **no** author token, WP-4, entropy, T activation,
world generation, Q/C process, lock, escrow, datum, outcome, or claim movement,
and predicts no qualification or scientific direction. After the bounded revision
lands, the exact delta needs a focused re-confirmation; the packet becomes
eligible only then.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q can never
earn, kill, or boundary-label C1–C6; a future Q pass is a spendability gate fact
only; S is unavailable; only a valid, independently locked C execution may move an
Officina claim — within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope, generalizing to the registered C frame and nothing
wider. Censored/`UNKNOWN`/every invalid state are never success, equivalence, a
boundary, or learner impossibility. `PROOF_CORE`/`PROOF_STRONG` remain earned by
nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this confirmation),
selected no cell or token, and committed nothing. `essay/OUTLINE.md` untouched. My
actions were reading the governing inputs and running the static recomputation,
serialization probe, path check, and bootstrap verifier above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
