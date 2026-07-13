# Fable 5 — Level 1 v3.1 addendum closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`; v1–v3
preserved unchanged; v3 carries forward except where the addendum
explicitly replaces it. Inputs: Opus final review
(`REVISE_LEVEL1_V3_CONTRACT`) and Sol final review
(`BLOCKED_LEVEL1_RANDOMIZATION`); the signed claim graph and canonical
files.

## Verdict

**READY_FOR_LEVEL1_SIGNATURE_CHECK**

The addendum contains exact replacement text, tables, and formulas for
every blocker both reviewers named: the S4 feature leak is closed by a
parity- and magnitude-balanced even-near-miss construction with a
required feature-null verifier; the allocation mechanism is a real
one-draw randomization with a fully pinned HMAC-SHA256 PRF and unbiased
rejection sampler; the pool, raw-word, and panel generators are
bit-exact; the transformer/optimizer contract is bit-exact including
attention direction, init draw order, and environment; calibration is
per-stratum with abstention penalized; divergence, re-execution, and
missing-checkpoint semantics are ordered; both leakage gates are full
protocols; feasibility measures the dominant scorer cost; the estimator,
predicates, determinacy table, and N3 projection are written as formulas
with a conservative fallback. No implementer choice remains that can
move a trajectory, solve event, predicate, invalidity route, or
estimand.

## 1. Finding-by-finding disposition

### Opus (final review)

| Finding | Disposition | Addendum |
|---|---|---|
| C-1 S4 symmetry/parity leak | **Adopted and strengthened**: `2n ± 2` even near-misses; **and** because side length ≡ displacement (mod 2) makes purely symmetric endpoints leak per-side parity, each label mixes symmetric and offset-by-2 splits so side parity, magnitude-equality, split type, total length, and per-side length multiset are exactly label-balanced; `n = 125` edge table; feature-null verifier required | A1 |
| C-2 generators not bit-reproducible | **Adopted**: PRF + `U(r)` rejection sampler + descending Fisher–Yates ("rejection-free" withdrawn); per-class reserve `floor(3·N_d/10)`; canonical cell order and flat index; combinatorial rank/unrank word enumerator; realization draw law with collision rejection and availability proof; reserved-cell consumption order; canonical serialization | A2, A3 |
| C-3 model under-specified | **Adopted**: bidirectional attention (kills the all-masked-row NaN), biases pinned, `√32` scale, final LN, `eps = 1e-5`, canonical init draw order with per-tensor PRF-seeded generators, CPU/float32/pinned-versions/single-thread/deterministic flags, no clipping, CE mean, exact param groups, step ordering, exact key strings and replicate ids | A5 |
| MJ-1 byte-identical hashes contradictory | **Adopted**: three surfaces; content hashes removed from the byte-identical claim; sealed id→content binding | A4 |
| MJ-2 solve-then-non-finite | **Adopted**: completed window stands, later divergence = mandatory diagnostic; else censored | A6 |
| MJ-3 global Brier incoherent | **Adopted**: per-stratum Brier ≤ 0.10 over every item, ABSTAIN scored at `p̄` (≈ 0.25 near 0.5); satisfiability shown by worked examples | A6 |
| MJ-4 gates are thresholds, not protocols | **Adopted**: deterministic noninterference bundle gate (ML probe withdrawn); exact shuffled-answer protocol (12 worlds × 2 replicates, PRF permutation, geometry preserved, zero-solve rule, finite scope stated) | A7 |
| MJ-5 feasibility misses scorer; indicator tuning | **Adopted**: scorer-only microbenchmark; censoring indicator limited to a binary feasibility-floor amendment | A8 |
| MJ-6 routing/re-execution gaps | **Adopted**: finiteness-before-routing; prefix predicate = hashes through the last committed pre-fault checkpoint; seal breach unchanged | A6 |
| MJ-7 S2/S5 novelty columns | **Adopted**: edge-world zone crossings annotated, no anti-lookup authority granted | A1 |
| mn-1 loss/bias/ordering pins | **Adopted** | A5 |
| mn-2 canonical serialization | **Adopted** | A3 |
| mn-3 S1 unevenness note | **Adopted** (noted in A1's S2/S5 correction context; S1 rule unchanged) | A1 |
| mn-4 seed schedule enumeration | **Adopted**: replicate ids {1,2}, member ids {0..3}, arm slots, exact key strings; the root value itself is the one-draw transcript's output | A2, A5 |

### Sol (final review)

| Finding | Disposition | Addendum |
|---|---|---|
| Critical 1 deterministic ≠ randomized | **Adopted in full**: one-shot 32-byte OS-CSPRNG draw, committed allocation transcript, refuse-if-exists, no redraw, failure → signed invalidity; procedural threat model stated; SRS/FPC language now justified by the one-shot mechanism; exact timing (D pre-development; roles once; `R_h` post-N3 with N3 in the domain; no regeneration after any information) | A2 |
| Critical 2 sampler bias | **Adopted**: exact `U(r)` (big-endian, `limit = floor(2^256/r)·r`, reject-and-redraw, `r = 1 → 0`), descending Fisher–Yates, full domain separation | A2 |
| Major 1 estimator not executable | **Adopted**: Sol Y2 formulas verbatim — `s²_h` (`n_h − 1`), `v_h`, `V̂`, Satterthwaite `ν` with zero-component rule, "estimated zero sample variance" reporting, Bonferroni `t_{1−0.05/6, ν}`, census rule | A9 |
| Major 2 guard discards one-sided evidence | **Adopted**: Sol Y3 determinacy table verbatim — one-sided predicates eligible with ≥ 1 event across the pair; `EQ` needs events in both; all-censored resolves nothing | A9 |
| Major 3 N3 rule underspecified | **Adopted**: projection formula for all three contrasts, max half-width ≤ 30, `s² = B²` conservative fallback for undefined/zero two-block variance, failure at 24 = no lock | A9 |
| Major 4 calibration/gates incomplete | **Adopted**: per-stratum Brier with ABSTAIN penalty; full gate protocols | A6, A7 |
| Major 5 boundary behavior | **Adopted**: exact inequalities; equality at a one-sided margin = unresolved/false | A9 |
| Minor 1–4 (panel improved; step-0 coherent; routing directionally correct; scope honest) | **Affirmed**; the Minor-3 evidentiary requirement (outcome-independence from pre-unseal mechanical logs) is restated inside A6's re-execution rule | A1, A6 |

Nothing in either review is unaddressed or silently dropped.

## 2. Exact replacement index (addendum → v3)

| Addendum | Replaces in v3 |
|---|---|
| A1 | §4 S4 row + corner construction; S2/S5 novelty entries |
| A2 | §2 keyed public-string streams (all allocation and stochastic streams) |
| A3 | §3 "locked draw"/"lowest unused"/realization prose; adds canonical serialization |
| A4 | §4 "byte-identical … hashes" sentence |
| A5 | §5 architecture/optimizer paragraph |
| A6 | §6 Brier rule; §6/§7 divergence, missing-checkpoint, and re-execution semantics |
| A7 | §6 leakage tolerance lines |
| A8 | §5 feasibility-contract outputs |
| A9 | §8 estimator/guard; §9 N3 rule |
| A10 | §11 gate table |

All other v3 sections carry forward unchanged.

## 3. Normative constants/algorithms (compact)

| Item | Value / algorithm |
|---|---|
| S4 | YES `2n` (4 sym + 4 off), NO `2n−2`/`2n+2` (each 2 sym + 2 off; `n = 125` table); total length `2n+8`; per-side multisets `{n+4,n+4}` ×4 and `{n+3,n+5}` ×4 per label; feature-null verifier |
| Root entropy | 32 bytes, `secrets.token_bytes`, once, transcript-committed, no redraw |
| PRF | HMAC-SHA256(root, len-prefixed components ‖ uint64_be counter) |
| `U(r)` | big-endian 256-bit, `limit = floor(2^256/r)·r`, reject/redraw, `r=1 → 0` |
| Reserve | `floor(3·N_d/10)` per class via descending Fisher–Yates prefix |
| Words | `W(a)`: length `|a|+2p`, `p ∈ {0..5}`, ≤ 136; order length→lex (`R < L`); combinatorial rank/unrank; 4 distinct pairs, collision-reject |
| Model | 2-layer pre-LN, bidirectional MHA (4×32, `/√32`, no QKVO bias), MLP 512 + biases, final LN, eps 1e-5, head 128→2 + bias, left-pad 273, PAD key mask |
| Init | canonical tensor order; per-tensor PRF-seeded `torch.Generator`; `randn/√fan_in` |
| Env | CPU float32, torch 2.9.1+cpu, CPython 3.12.3, deterministic algorithms, 1 thread |
| Optim | AdamW 1e-3 const, (0.9, 0.98), 1e-8; decayed = {W_Q,K,V,O, W_in, W_out ×2, head_W} @ 0.01; rest 0; no clipping; CE mean |
| Calibration | per-stratum Brier ≤ 0.10, all items, ABSTAIN at `p̄` |
| Gates | noninterference byte-identity bundle; shuffled answers 12×2, zero solves |
| Estimator | Sol Y2 formulas; Bonferroni `t_{1−0.05/6, ν}`; census at 24 |
| Predicates | `SUP L>60`; `NI L>−60`; `NONSUP U<60`; `EQ L≥−60 ∧ U≤60`; determinacy table |
| N3 | max half-width over 3 contrasts ≤ 30; fallback `s² = B²`; fail at 24 = no lock |

## 4. Signature-check questions (bounded to the repairs)

**Opus:** (1) Does A1's mixed-split construction close C-1 completely —
in particular, is the parity theorem's residue (side parity ≡
displacement) now provably label-independent at every `n` including 125,
and does the feature-null verifier cover the features you would attack
next? (2) Do A2/A3/A5 reach your bit-level implementability standard —
would two independent implementers now produce identical pools, panels,
and trajectories? (3) Does A6's ordering (finiteness → routing;
pre-fault prefix predicate) close MJ-2/MJ-6 without opening a new
masking path?

**Sol:** (1) Does the one-shot root-entropy protocol restore the
design-based SRS/FPC reading you blocked on, given `R_h`'s post-N3
domain? (2) Is the `s² = B²` fallback acceptably conservative, or too
conservative to ever pass at `N3 ≤ 24` (in which case it is an honest
no-lock, not a defect)? (3) Does the adopted determinacy table plus the
exact boundary inequalities close Majors 2 and 5 as you intended?

## 5. Signature tokens (unchanged authorial scope)

- `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE` — unchanged from v3.
- `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` — **explicitly incorporating the
  v3.1 addendum**: signing it accepts v3 as amended by A1–A10.

## 6. Implementation authorization and negative space

**Codex after gate 2 (Kirill's signatures):** the exact generators and
model of A2–A5 with their verifiers (feature-null, noninterference,
enumeration, state-hash) — gate 3. **Gate-4 driver** (root entropy) and
**gate-5 feasibility** each require their own review before their single
executions. **Before gate 2:** only the previously authorized neutral
parameterized substrate on dummy fixtures; the allocation sampler is not
scientific machinery until the root draw exists. **Cursor:** after
gate 2, mechanical breadth under Codex verification. **Forbidden until
their gates:** entropy draw, feasibility run, comparative scout, N3,
lock, escrow, outcome.

**Negative space (restated, binding):** a certificate failure is
censoring, never evidence the learner lacked `n`; C1 is never broadened
beyond distance 1; deterministic selection is never called
randomization (that is exactly what A2 repairs); UNKNOWN/all-censored is
never a boundary, equivalence, or success; Level 1 is never evidence
for `PROOF_CORE` in either direction; development contrasts are
non-citable forever; RANDOM-superior never rewrites C1.

## 7. Confirmation

No code was written; no entropy was drawn; no feasibility or comparative
datum, scout, escrow, lock, or outcome was created; no constant derives
from any observed comparison. v1–v3 are unchanged; the addendum replaces
only the sections listed in §2.
