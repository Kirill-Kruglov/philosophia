# Phase 2 Stage-B L2 generator annex - final X/Y review text

Status: `READY_FOR_PHASE2_STAGE_B_L2_FINAL_XY_REVIEW`

Date: 2026-08-14

This draft authorizes nothing. It replaces
`PHASE2_STAGE_B_L2_GENERATOR_ANNEX_V1_DRAFT.md` in full. It does not authorize
L2 code, a dev root key, a generated plan, a fixture scan, L3/L4 work,
Peano/search execution, a commit or a push. No author choice remains open. The
scaffold catalogue is the single literal tuple `('A','B','C')` frozen in section
5.6, and the byte schedule is therefore fully determined by this annex. The
parts of the withdrawn author-choice packet that were never choices - the
register of what v1 cells C1-C13 became - are carried in section 0.2 below and
remain normative.

## 0. Authority and evidence

- Philosophia authority: `41adcaa96e3281746a6e59247d0fed5d1c42260c`
- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`
- Stage-A patch SHA-256:
  `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd`
  (`successor/dev/minimo_phase2_stage_a_19.patch`)
- Stage-B dev charter v1.1.1 SHA-256:
  `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311`
- accepted Stage-B L0/L1 delta SHA-256:
  `1a67b09fb63784662cce56359c5cff897023cceec2f3dd445739d0a04cf00736`
- accepted cumulative Stage-A + Stage-B L0/L1 SHA-256:
  `c0b0e9ab79a66696231e356a92f6ccace67911d2bbe5906918ca6f4cbbe9a065`
- accepted exclusion ledger V2 SHA-256:
  `31e319bdbfc7b17c65ac7c8698022c761f4f05790e1f044e692f736cf99d680a`
- superseded v1 annex SHA-256:
  `14ee7a8209b462e3437485e2a016686114ee42290901eea1bdb23bc5e0036e3b`
- superseded v1 choices SHA-256:
  `6aaedb54969a01ff10111b2dc1bdf810a9875c45de9e971425e386aafd91b60a`

All eight hashes above were recomputed by this author and match. The pinned patch
files, not any mutable disposable tree, are the evidence of record; the L0/L1
surface quoted below was reconstructed from
`minimo_phase2_stageb_l01_v1_1_1_repair_v3_delta.patch` and read only.

## 0.1 What changed from v1, and why

The v1 architecture was refuted. The driver pre-review (P1), Sol X and Fable Y
independently proved that the mandatory `EXFALSO`/`OR_ELIM` seed mandate makes
`globals |- FALSE` for every emitted plan, so every theorem is valid vacuously
and the goal is proof-irrelevant. Sol additionally refuted the v1 totality
theorem by exhibiting a reachable `build(FALSE, 1, forbidden, use_obl=(l,P))`
state with no eligible production, and refuted the v1 `OR_ELIM` free-formula
bound.

Accordingly this v2 **deletes**, with no replacement gadget of the same shape:

- the whole M1/M2/M3 mandate catalogue and author choice C13;
- the seed formula `S`, the `OR(S,FALSE)` / `NOT(AND(S,FALSE))` coverage
  carriers and the goal/seed coverage split (C2, C4);
- `plant_obl`, `PLANT_HERE`/`DELEGATE`, obligation routing and CP8/CP12;
- `A_plant`, the general `A_use` feasible-set solver and CP13;
- every contradiction-based totality witness, in particular the
  `EXFALSO^(N-3)` and `EXFALSO^b`-over-global-`FALSE` padding chains;
- the general recursive goal-directed proof synthesizer `build(...)` and its
  ten-production eligibility predicate, together with author choices C8, C9,
  C10, C11 which existed only to parameterise it.

It **replaces** them with a small finite catalogue of typed,
composition-bearing scaffolds whose global hypothesis set is classically
satisfiable by construction, instantiated directly, plus exact-size
`AND_ELIM` chain expansion. Section 9 proves the resulting object total,
exact-size complete over `N = 8..37`, and non-vacuous.

`PHASE2_STAGE_B_L2_NONVACUOUS_STRUCTURAL_BLOCKER` is **not** returned: section
9.3 exhibits, for every `N` in `8..37` and every catalogue member, a legal
construction under the full conjunction of guards.

## 0.2 Derived-not-chosen register

The v2 author-choices packet is withdrawn. Its non-menu content is
normative and is restated here. Nothing in this register is an open decision.

| v1 cell | disposition |
|---|---|
| C1 declared atom count law | Absorbed by meta-law U: `k` is uniform over the scaffold's eligible range. The range is derived: `3..6` for scaffold A; `4..6` for scaffolds B and C, because they need `|A_T| >= 3` distinct chain atoms and at least one atom the satisfying valuation sets false. Section 5.4 proves `k = 3` infeasible for those scaffolds. |
| C2 goal/seed coverage split | Deleted with the seed mandate. Coverage is carried by each scaffold's own gadget fields and proved per scaffold. |
| C3 goal size cap, C4 seed size cap, C10 soft cap | Deleted. Section 6.3 derives every leaf-count ceiling from `MAX_FORMULA_NODES = 24` alone; Lemma NB proves every derived range nonempty. No cap below the hard bound is load-bearing, so no cell is offered. |
| C5 constructor law, C6 leaf law, C7 size-split law | Absorbed by meta-law U. The C6 `FALSE`-leaf weight is not a choice at all: `sample_positive` emits only the positive fragment, because Lemma POS is what makes each scaffold's satisfying valuation checkable. |
| C8 production selection, C9 budget allocation, C11 plant-vs-delegate | Deleted with the general recursive synthesizer, the obligation solver and the plant/delegate machinery. |
| C12 PRF rejection budget | Fixed at `PRF_MAX_REJECTIONS_PER_CALL = 64` as a fail-closed engineering guard. Not an author signature. |
| C13 mandate catalogue | Deleted. Superseded by the frozen satisfiable catalogue of section 5.6, which is ratified rather than chosen. |

A single-scaffold catalogue is infeasible, not merely undesirable: covering
`OR_INTRO_LEFT`, `OR_INTRO_RIGHT`, `OR_ELIM`, `NOT_INTRO`, `NOT_ELIM` and
`EXFALSO` in one gadget costs at least eight nodes, giving a fixed frame cost of
at least eleven and a minimum `N` above the `S1` floor of `8`. Band `S1` would
be unreachable, which the charter does not permit.

## 0.3 Ratification provenance

Administrative metadata. This section states no contract clause; every normative
statement of this annex is in sections 1-13.

This standalone text is the materialization of the accepted composite:

| component | SHA-256 |
|---|---|
| v2 base text | `7e75ab038f2951b40b342ac805823d3d541c5a5891a33fb747f01c22f2fdd591` |
| bounded correction, amendments A1-A16 | `d3f01ad30be510e14a5da6e14bbec9e9c9a1cd3bfda45e5306dff5918db4afd9` |
| depth correction, amendment E1 | `e15a12c4ff881444ec5037df8bc3f8425b25b27a7362a6b74813742693a9dfde` |
| base depth correction, amendment E2 | `9bbe541f661177e1c933d8264e82ac8ca8bdcc29d0a24201570b55e4962945a6` |
| ratified author packet | `dc98ca74938eb416d9e73aeb1b41a3ddf18167128b857b152dfd2e8da37b4f7e` |
| author ratification record | `4e82ca8a66f2463cad7f9fa78bfeeaf297a0cc9e1670e4cf4dd98f7e21c82ae7` |

The author token recorded in that record, verbatim:

```text
I_ACCEPT_PHASE2_STAGE_B_L2_CATALOGUE_ABC_AND_S4_GATE
```

The token ratified the exact catalogue `('A','B','C')` of section 5.6 and
acknowledged the disclosed replacement S4 gate of section 10.7.1. It authorized
only preparation of this standalone annex and its submission for joint
independent X/Y review. It authorized no L2 code, no output literal, no fixture
scan, no exclusion ledger row, no key or root, no execution, no repository edit,
no commit and no push. Section 13 governs.

## 1. Fixed boundary

L2 is exactly two files:

```text
learning/phase2_stageb_generator.py
learning/test_phase2_stageb_generator.py
```

The production module imports only Stage-B L0 modules
(`phase2_stageb_schema`, `phase2_stageb_canonical`, `phase2_stageb_causes`) and
the standard library (`hmac`, `hashlib`, `math`, `typing`, `__future__`). It must
not import `phase2_stageb_checker`, `phase2_stageb_render`, Peano, MCTS, Torch,
MINIMO policy/search, any L3/L4 module, any generic harness, any
plugin/registry/supervisor framework or any root executor. The test module may
import the accepted L1 checker and pass constructed outputs to it.

L2 owns no theorem identity, no skeleton identity, no alpha-canonicalization, no
public projection, no compilation, no replay, no query measurement, no quota
ledger and no dev execution loop. No class hierarchy, configuration file,
registry or plugin table is authorized. The scaffold catalogue is a literal
frozen tuple of module-level functions in one production module; it is not an
extensible registry and no third party may add to it.

`phase2_stageb_render` is deliberately excluded: L2 emits no surface syntax.

## 2. Item 1 - public API and exact result schema

Preserved byte-for-byte from v1 section 2 except the subcause tuple, which is
re-derived for the new architecture.

### 2.1 Entry point

```python
def generate_draw(root_key: bytes, draw_index: int) -> dict
```

Argument validation is an API contract, not a draw outcome. `generate_draw`
raises `ValueError` when `type(root_key) is not bytes`, `len(root_key) != 32`,
`type(draw_index) is not int` (which rejects `bool`, matching L0
`is_exact_int`), or `not 0 <= draw_index < 2**64`. No other exception may
escape.

### 2.2 Success record

Exact key tuple `L2_SUCCESS_KEYS`:

```text
('schema','ok','cause','draw_index','root_id','target_band',
 'target_node_count','words_consumed','plan','expectation')
```

```text
schema            = "philosophia.stageb.generator-draw.v1"
ok                = True
cause             = None
draw_index        = int, the argument
root_id           = lowercase 64-hex SHA256(root_key)
target_band       = "S1" | "S2" | "S3" | "S4"
target_node_count = int in the target band
words_consumed    = int, total 64-bit words drawn from the draw stream
plan              = Plan, charter section 3.4, no extra field
expectation       = Expectation, charter section 3.5
```

### 2.3 Construction-failure record

Exact key tuple `L2_FAILURE_KEYS`:

```text
('schema','ok','cause','subcause','draw_index','root_id','target_band',
 'target_node_count','words_consumed')
```

```text
schema            = "philosophia.stageb.generator-draw.v1"
ok                = False
cause             = "PLAN_CONSTRUCTION_FAILED"
subcause          = member of L2_CONSTRUCTION_SUBCAUSES
target_node_count = int, or None only when the rejection budget was exhausted
                    at decision point D1
```

Both records are plain nested `dict`/`list`/`str`/`int`/`bool`/`None` data. There
are no dataclasses, no floats and no free-text fields. `expectation` is returned
as a separate top-level key and never as a plan field: charter section 3.5 states
the plan carries no count, band, identity or expectation field, and the accepted
checker takes the expectation as its second argument
(`check_plan(plan, expectation)`).

The draw record is dev-internal. `root_id` appears in it as SHA-256 metadata
only. It is not a public carrier record and must never be fed to a public
projection; L3 owns that boundary.

### 2.4 Closed L2 construction subcauses

`L2_CONSTRUCTION_SUBCAUSES` is a literal frozen tuple:

```text
PRF_RANGE_REFUSED
PRF_REJECTION_BUDGET_EXCEEDED
TARGET_SIZE_UNREACHABLE
FORMULA_BOUND_UNSATISFIABLE
ATOM_COVERAGE_UNSATISFIABLE
NONVACUITY_GUARD_VIOLATED
SIZE_CONSERVATION_VIOLATED
EXPECTATION_DISAGREEMENT
RECURSION_BOUND_EXCEEDED
WORK_BOUND_EXCEEDED
```

`NONVACUITY_GUARD_VIOLATED` is the one new subcause required by the derived
non-vacuity boundary of the X/Y disposition; section 8.3 defines the guard it
reports. `OBLIGATION_UNDISCHARGEABLE` and `NO_ELIGIBLE_PRODUCTION` are removed
with the architecture that created them.

Every subcause collapses to the charter draw cause `PLAN_CONSTRUCTION_FAILED`.
L2 never returns, predicts or anticipates `PLAN_SCHEMA_INVALID`,
`PLAN_TYPE_INVALID`, `PLAN_CONSTRAINT_INVALID`, `PLAN_NON_NORMAL`,
`SEQUENT_REDERIVATION_MISMATCH`, `CLASSICAL_COUNTEREXAMPLE`,
`THEOREM_ID_COLLISION`, `SKELETON_ID_COLLISION`, `COMPILER_NO_MATCH`,
`COMPILER_AMBIGUOUS_MATCH`, `PEANO_REPLAY_REFUSAL`,
`PEANO_REPLAY_NONTERMINAL`, `QUERY_MEASUREMENT_OVERFLOW` or
`TARGET_BAND_ALREADY_FULL`. Those remain owned by pipeline stages 3-11 in
charter section 8 and by their layers. Charter section 8 stage order is
unchanged by this annex, and no L1 predicate is added, removed or weakened.

### 2.5 Honest reachability statement

The API is **total as success-or-failure**: every `(root_key, draw_index)` with
valid argument types returns exactly one record with `L2_SUCCESS_KEYS` or
`L2_FAILURE_KEYS`, and no path can hang.

It is **not** claimed that every theoretical HMAC stream yields a plan. This
annex asserts exactly two things about reachability, and no more:

1. Section 9 proves that under the specified algorithm, every subcause **other
   than** `PRF_REJECTION_BUDGET_EXCEEDED` is a fail-closed guard on an
   implementation defect and cannot fire.
2. `PRF_REJECTION_BUDGET_EXCEEDED` has **no** unreachability proof. The largest
   `randbelow` argument this annex can produce is `126` (section 9.1, Lemma T1),
   so a single word is rejected with probability at most `125 / 2**64`, below
   `2**-56`, and 64 consecutive rejections has probability below `2**-3584`;
   that is a bound, not a proof of impossibility, and the record is emitted
   honestly if it ever occurs. The v1 sentence "`PLAN_CONSTRUCTION_FAILED` is
   unreachable" is withdrawn as false.

The code gate exercises the subcauses by direct injection into the internal
functions (section 10.6), never by hunting for a draw index. No yield,
feasibility or scientific claim may be derived from the unreachability of these
guards: construction feasibility is not L1 acceptance and is not quota fill.

## 3. Item 2 - frozen PRF implementation

Charter section 7 is carried byte-for-byte. Nothing in this section may be
changed by an implementer. This section is preserved unchanged from v1 except
that `PRF_MAX_REJECTIONS_PER_CALL` is now a fixed engineering constant rather
than an author cell.

### 3.1 Constants and stream

```text
L2_PRF_DOMAIN               = b'philosophia.stageb-dev.v1'   # ASCII, 25 bytes
L2_PRF_SEPARATOR            = b'\x00'                        # one NUL
ROOT_KEY_LEN                = 32
WORDS_PER_BLOCK             = 4
PRF_MAX_REJECTIONS_PER_CALL = 64
```

```python
def _block(root_key, draw_index, block_index):
    message = (L2_PRF_DOMAIN + L2_PRF_SEPARATOR
               + draw_index.to_bytes(8, 'big')
               + block_index.to_bytes(8, 'big'))
    return hmac.new(root_key, message, hashlib.sha256).digest()
```

- the HMAC-SHA256 key is the raw 32-byte `root_key`, never `root_id`, never a
  hex string, never a derived value;
- `draw_index` and `block_index` are unsigned big-endian 8-byte integers, in
  that order, after the domain and the single NUL;
- `block_index` starts at zero and the stream is the concatenation of blocks in
  ascending `block_index`;
- each block is 32 bytes, exactly four 64-bit words, so words never straddle a
  block boundary;
- word `w` is `int.from_bytes(block[8*o:8*o+8], 'big')` with
  `b = w_index // 4`, `o = w_index % 4`;
- words are non-overlapping and no word is ever reused;
- block caching is forbidden. Each word recomputes its HMAC block. At 37 plan
  nodes the cost is irrelevant and recomputation removes a whole class of
  cache-coherence defect from review.

### 3.2 Stream cursor representation

The cursor is one mutable `dict` with the exact key tuple
`('root_key','draw_index','word_index','rejections','decision_calls','max_frames')`.
`word_index` starts at 0 and is incremented by exactly one per word consumed.
`words_consumed` in the result record is the terminal `word_index`. The last
three keys are the fail-closed work counters of section 8.5 and consume no
words. The cursor is never serialized and never enters the plan.

### 3.3 `randbelow`

```python
def randbelow(cursor, n):
    if type(n) is not int or n < 1 or n > 2**64:
        return refusal PRF_RANGE_REFUSED
    limit = (2**64 // n) * n
    rejected = 0
    while True:
        w = next_word(cursor)                # always advances word_index by 1
        if w < limit:
            return w % n
        rejected += 1
        if rejected > PRF_MAX_REJECTIONS_PER_CALL:
            return refusal PRF_REJECTION_BUDGET_EXCEEDED
```

- `type(n) is not int` rejects `bool` exactly as L0 `is_exact_int` does;
- a rejected word is consumed and never reused; there is no modulo bias;
- `PRF_MAX_REJECTIONS_PER_CALL = 64` is a fail-closed engineering guard, not a
  distributional knob and not an author choice. Any sufficiently large value is
  behaviourally identical on every realisable stream; the constant exists only
  so that no loop is unbounded.

**Singleton consumption is derived, not chosen.** For `n == 1`,
`limit = 2**64` and no 64-bit word satisfies `w >= limit`, so the charter's own
frozen definition consumes exactly one word and returns `0`. This annex adopts a
**uniform call discipline**: every decision point calls
`randbelow(cursor, n)` including when `n == 1`. The consequence is that the byte
schedule is a pure function of the sequence of decision points reached and never
of eligibility cardinality, which is what makes the schedule auditable and makes
a "skip singleton calls" optimisation a detectable mutation (section 10.5).
Purely deterministic resolutions that are not decision points - hypothesis
identifier assignment, `hN`/`lN` numbering, deep copying, band lookup, colex
unranking, Lehmer decoding, expectation summarisation - consume no word.

### 3.4 Range and type refusal

`randbelow` refusal is propagated, never swallowed: the enclosing call chain
returns the failure record with the corresponding subcause and the terminal
`word_index`. No exception is raised.

### 3.5 The single distribution meta-law

> **Meta-law U.** Every genuinely random choice in this annex is uniform over
> its frozen eligible list or over its frozen inclusive integer range, realised
> as exactly one `randbelow(cursor, n)` call with `n` equal to the cardinality of
> that list or range.

Meta-law U is one prospective rule and one signature, not one cell per
application. It replaces v1 author cells C1, C2, C3, C4, C5, C6, C7, C8, C9,
C10, C11 in their entirety. It is the charter's own precedent (charter section
7: "target plan-node count is uniform over the target band's integers").

Meta-law U is a statement about each individual decision, not about the induced
distribution on whole plans. Where a composite object is built from several
uniform decisions - a formula tree, a label sequence, an atom split - the
induced law on the composite object is **not** claimed to be uniform, and the
annex says so at each such point. That is a disclosed property of the
construction, not a hidden weighting.

## 4. Item 3 - one-draw semantics

One call of `generate_draw(root_key, draw_index)` is exactly one complete
bounded construction attempt over one independent counter stream.

- The target band is `draw_index mod 4` mapped `0:S1, 1:S2, 2:S3, 3:S4`. This
  consumes no word.
- The target plan-node count is D1, uniform over the band's integers via
  `band_lo + randbelow(band_hi - band_lo + 1)`, and it is the **first** word of
  the draw stream, before any other random choice. Band widths are 4, 6, 8, 12.
- There is no retry, no backtracking, no adaptive replenishment, no alternate
  candidate and no variable number of attempts. The construction is a single
  forward pass with a finite ordered decision schedule (section 7.1).
- The only loop that can consume more than a fixed number of words for one
  decision is the charter's own `randbelow` rejection loop, bounded by
  `PRF_MAX_REJECTIONS_PER_CALL`.
- The generator never consults the checker, never scores a candidate and never
  compares two candidates.
- A filled-band draw is still one complete draw here. Ledgering and
  `TARGET_BAND_ALREADY_FULL` belong to charter stage 11, not to L2.

## 5. Items 4 and 5 - the frozen scaffold catalogue

### 5.1 Common frame

Every catalogue member instantiates the same frame. There is no recursive proof
synthesizer, no demand-directed `build`, no production eligibility predicate and
no budget solver. A plan is emitted by direct instantiation of the frame with
the scaffold's gadget substituted at one fixed position.

```text
goal  = AND( AND(T0, T1), AND(T2, W) )

proof = AND_INTRO(                                          # node R
          left  = AND_INTRO(                                # node R.L
                    left  = CHAIN(0),   conclusion T0
                    right = CHAIN(1),   conclusion T1
                  ),
          right = AND_INTRO(                                # node R.R
                    left  = CHAIN(2),   conclusion T2
                    right = GADGET,     conclusion W
                  )
        )
```

- `T0`, `T1`, `T2` are **pairwise distinct atom names** drawn from the
  scaffold's chain alphabet `A_chain`.
- `W` and the gadget are the scaffold's characteristic part. Every catalogue
  member has gadget node cost exactly **3**.
- `CHAIN(j)` is the exact-size expansion of section 5.2 with length `L_j`.

Fixed frame cost is `3` (`AND_INTRO` nodes) `+ 3` (gadget) `= 6`, so

```text
N = 6 + L0 + L1 + L2,   S := L0 + L1 + L2 = N - 6
```

### 5.2 `CHAIN(j)` - the exact-size typed expansion

Let `dir` be the plan-wide `AND_ELIM` direction, `dir in ('AND_ELIM_LEFT',
'AND_ELIM_RIGHT')`, drawn once per plan at D12. Let `Z(j,1) .. Z(j,L_j)` be
atom names drawn from `A_chain` at D13.

```text
F(j,0) = ATOM(Tj)
F(j,i) = AND( F(j,i-1), ATOM(Z(j,i)) )     if dir == AND_ELIM_LEFT
       = AND( ATOM(Z(j,i)), F(j,i-1) )     if dir == AND_ELIM_RIGHT
H_j    = F(j, L_j)                          # the chain's global hypothesis
```

```text
CHAIN(j) with L_j == 0 :  ASSUME(g_j : H_j)                       0 nodes
CHAIN(j) with L_j >= 1 :  dir( source = dir( ... dir(
                              source = ASSUME(g_j : H_j),
                              conclusion = F(j, L_j - 1) ) ...,
                              conclusion = F(j, 1) ),
                              conclusion = F(j, 0) = ATOM(Tj) )   L_j nodes
```

Typing. `AND_ELIM_LEFT` requires an `AND` source and concludes `source['left']`;
`AND_ELIM_RIGHT` concludes `source['right']`. By construction `F(j,i)` is an
`AND` whose `dir`-side component is `F(j,i-1)`, so each of the `L_j` nodes
type-checks and the topmost conclusion is `ATOM(Tj)`.

Normality. The `source` of every chain node is either the leaf `ASSUME` or the
next chain node, never `AND_INTRO`. The prohibited redex
`AND_ELIM_* directly consuming AND_INTRO` therefore cannot occur inside a chain.
It cannot occur at the chain top either: the chain top is a **child** of an
`AND_INTRO`, and `AND_INTRO` is not a redex position.

Size. `formula_nodes(F(j,i)) = 1 + 2i`, so
`formula_nodes(H_j) = 1 + 2 L_j`. With `L_j <= CHAIN_LEN_CAP = 11` this is at
most `23 <= MAX_FORMULA_NODES = 24`. Every intermediate conclusion is an
`F(j,i)` with `i < L_j`, hence strictly smaller.

Depth. The bottom chain node has only an `ASSUME` child, so its inference depth
is `0`; each further node adds one. The chain top has inference depth
`L_j - 1` for `L_j >= 1`.

`CHAIN_LEN_CAP = 11` is derived, not chosen: `1 + 2 L <= 24` gives `L <= 11`.

### 5.3 Scaffold A - `OR` commutation (positive, Sol's anchor, proved here)

`A_chain = alphabet`. Alphabet split: `A_P` and `A_Q` partition the alphabet,
both nonempty (D4/D5). `P = sample_positive(A_P, ...)`,
`Q = sample_positive(A_Q, ...)` (D6/D7, section 6).

```text
W = OR(Q, P)

globals contributed: OR(P, Q)                      (identifier h0)

GADGET =
  OR_ELIM(                                                        # node 1
    major            = ASSUME(h0 : OR(P, Q)),                     # 0 nodes
    left_assumption  = {'id': l0, 'formula': P},
    left_branch      = OR_INTRO_RIGHT(                            # node 2
                         source     = ASSUME(l0 : P),             # 0 nodes
                         conclusion = OR(Q, P) ),
    right_assumption = {'id': l1, 'formula': Q},
    right_branch     = OR_INTRO_LEFT(                             # node 3
                         source     = ASSUME(l1 : Q),             # 0 nodes
                         conclusion = OR(Q, P) ),
    conclusion       = OR(Q, P) )
```

**A.1 Exact node arithmetic.** The gadget contains exactly three non-`ASSUME`
nodes: one `OR_ELIM` and two `OR_INTRO_*`. The three `ASSUME` leaves count zero
by charter section 2.2. Gadget cost `= 3`, so `N = 6 + S` exactly.

**A.2 Typing.** `OR_ELIM` requires `major['conclusion']` of kind `OR`: it is
`OR(P,Q)`. It requires `left_assumption['formula'] == major['left'] = P` and
`right_assumption['formula'] == major['right'] = Q`: both hold by construction.
`OR_INTRO_RIGHT` requires `source == conclusion['right']`; `conclusion = OR(Q,P)`
so `conclusion['right'] = P` and the source concludes `P`. `OR_INTRO_LEFT`
requires `source == conclusion['left'] = Q` and the source concludes `Q`. Both
branch conclusions and the node conclusion are the byte-identical `OR(Q,P)`, as
the accepted checker demands.

**A.3 Formula bounds.** Write `p = formula_nodes(P)`, `q = formula_nodes(Q)`.
Section 6.3 enforces `p + q <= 16`.

```text
OR(P,Q)                 = 1 + p + q        <= 17
W = OR(Q,P)             = 1 + p + q        <= 17
goal                    = 7 + p + q        <= 23
AND(T2, W)              = 3 + p + q        <= 19
AND(T0, T1)             = 3
H_j                     = 1 + 2 L_j        <= 23
local assumptions P, Q  = p, q             <= 15
OR_INTRO components     = q and p          <= 15
```

The accepted checker's `_walk_formulas` inspects exactly: every global
hypothesis formula, the goal, every node conclusion, both `OR_ELIM` assumption
formulas, the `NOT_INTRO` assumption formula, and both components of an
`OR_INTRO_*` conclusion of kind `OR`. Every one of those is listed above or is a
subformula of a listed formula, so all are at most `24` nodes.

**A.4 Global-hypothesis uniqueness and use.** The globals are
`OR(P,Q), H_0, H_1, H_2`.

- `OR(P,Q)` has kind `OR`; every `H_j` has kind `ATOM` (when `L_j = 0`) or `AND`
  (when `L_j >= 1`), so `OR(P,Q)` differs from each `H_j` in its first canonical
  key. Distinct.
- `H_i` versus `H_j`, `i != j`: if `L_i != L_j` then
  `formula_nodes(H_i) = 1 + 2 L_i != 1 + 2 L_j`, so the canonical byte strings
  differ. If `L_i = L_j = L`, define `pi(F)` as "follow the `left` field `L`
  times" when `dir = AND_ELIM_LEFT` and "follow the `right` field `L` times"
  when `dir = AND_ELIM_RIGHT`. Because `dir` is plan-wide, `pi(H_i) = ATOM(Ti)`
  and `pi(H_j) = ATOM(Tj)`; `Ti != Tj` by section 5.1, so `H_i != H_j`.
- Use: `OR(P,Q)` is referenced by the `OR_ELIM` major leaf; `H_j` is referenced
  by the bottom `ASSUME` of `CHAIN(j)`, which exists for every `L_j >= 0`.

So `duplicate global hypothesis formula` and `unused global hypothesis` are
impossible.

**A.5 Local hypotheses.** `l0` is referenced by the `ASSUME` inside
`left_branch`, `l1` by the `ASSUME` inside `right_branch`. The accepted
`_collect_assume_ids` collects each branch's references separately and requires
the branch's own local identifier to appear in that branch's set; both do. Local
identifiers are minted from one plan-wide counter (section 7.3), so they are
pairwise distinct plan-wide and never shadow an `hN`.

**A.6 Atom coverage.** `atoms(P) = A_P` and `atoms(Q) = A_Q` exactly (section
6.2 guarantees the label alphabet of a sampled formula is its cover, surjectively
and with no other atom). `A_P` union `A_Q` is the whole alphabet, and `OR(P,Q)`
is a global hypothesis, so `declared <= public_atom_names(plan)` holds. Every
atom occurring anywhere - `T_j`, `Z(j,i)`, `P`, `Q` - is drawn from the
alphabet, so `occurring <= declared` holds. The `atoms` list is
`('a0', ..., 'a{k-1}')`, which is duplicate-free and in ascending
byte-lexicographic order for `k <= 6`.

**A.7 Satisfiability of the global context.** `P` and `Q` are positive formulas
(section 6.1: constructors `ATOM`, `AND`, `OR` only; no `NOT`, no `FALSE`), and
every `H_j` is an `AND`-spine over atoms, hence also positive. By induction on a
positive formula, the all-true valuation makes it true. Therefore the valuation
`nu_A(a) = True for every declared atom` satisfies `OR(P,Q)` and every `H_j`
simultaneously. No global hypothesis is `FALSE`; indeed `FALSE` does not occur
anywhere in a scaffold-A plan.

**A.8 Goal is not a hypothesis.** `goal` has kind `AND`, so it differs from
`OR(P,Q)` and from any `H_j` with `L_j = 0`. For `L_j >= 1`: if
`dir = AND_ELIM_LEFT` then `H_j['right']` has kind `ATOM` while
`goal['right'] = AND(T2, W)` has kind `AND`; if `dir = AND_ELIM_RIGHT` then
`H_j['left']` has kind `ATOM` while `goal['left'] = AND(T0, T1)` has kind `AND`.
So no global hypothesis is byte-identical to the goal.

**A.9 Family set and branching.** Families present: `AND_INTRO` (three nodes),
`OR_ELIM`, `OR_INTRO`, and `AND_ELIM` whenever `S >= 1`. Since `N >= 8` implies
`S >= 2`, all four are always present, which is at least
`MIN_FAMILY_COUNT = 3`. Branching is satisfied twice over, by `AND_INTRO` and by
`OR_ELIM`.

**A.10 Dependency depth.** `OR_INTRO_*` nodes have only `ASSUME` children, depth
`0`. The `OR_ELIM` has two non-`ASSUME` children of depth `0`, so its depth is
`1`. Node `R.R` has the gadget as a child, so its depth is at least `2`; node
`R` therefore has depth at least `3 >= MIN_DEPENDENCY_DEPTH = 2`. The exact
formula is section 8.2.

**A.11 Normality.** The three prohibited immediate redexes are: `AND_ELIM_*`
consuming `AND_INTRO` - impossible, section 5.2; `OR_ELIM` consuming
`OR_INTRO_*` - the `OR_ELIM` major is an `ASSUME`; `NOT_ELIM` with a
`NOT_INTRO` negative - scaffold A contains no `NOT_ELIM`.

**A.12 Eligible atom count.** Scaffold A needs three pairwise distinct chain
atoms from `A_chain = alphabet` and a nonempty two-part split, so it is eligible
for `k in 3..6`.

### 5.4 Scaffold B - disjunctive syllogism (`NOT_ELIM` + `EXFALSO`)

Alphabet split: `A_R` nonempty with `|A_R| <= k - 3`, and `A_T =
alphabet \ A_R` with `|A_T| >= 3` (D4/D5). `A_chain = A_T`.
`R = sample_positive(A_R, ...)` (D6), `QB = sample_positive(A_T, ...)` (D7).

```text
W = QB

globals contributed: OR(R, QB)   (h0),   NOT(R)   (h1)

GADGET =
  OR_ELIM(                                                        # node 1
    major            = ASSUME(h0 : OR(R, QB)),                    # 0 nodes
    left_assumption  = {'id': l0, 'formula': R},
    left_branch      = EXFALSO(                                   # node 2
                         source = NOT_ELIM(                       # node 3
                                    negative = ASSUME(h1 : NOT(R)),
                                    positive = ASSUME(l0 : R),
                                    conclusion = FALSE ),
                         conclusion = QB ),
    right_assumption = {'id': l1, 'formula': QB},
    right_branch     = ASSUME(l1 : QB),                           # 0 nodes
    conclusion       = QB )
```

- Cost exactly `3`: `OR_ELIM`, `EXFALSO`, `NOT_ELIM`.
- Typing: `NOT_ELIM` needs `negative` of kind `NOT` concluding `NOT(R)` and
  `positive` concluding `R` with `negative['arg'] == positive`; both hold, and
  its stated conclusion is `FALSE`. `EXFALSO` needs a `FALSE` source and may
  conclude any well-formed formula; it concludes `QB`. `OR_ELIM` needs both
  branch conclusions byte-identical to its own: left is `QB`, right is `QB`.
- Locals: `l0` is referenced by the `NOT_ELIM` positive inside the left branch;
  `l1` is the right branch itself.
- Globals used: `OR(R,QB)` by the major, `NOT(R)` by the `NOT_ELIM` negative,
  `H_j` by chain `j`.
- Uniqueness: `OR(R,QB)` has kind `OR`, `NOT(R)` has kind `NOT`, `H_j` has kind
  `ATOM` or `AND`; chain globals are pairwise distinct by A.4.
- Coverage: `atoms(R) = A_R` appears in the globals `NOT(R)` and `OR(R,QB)`;
  `atoms(QB) = A_T` appears in the global `OR(R,QB)` and in the goal. Their union
  is the alphabet.
- Goal not a hypothesis: same argument as A.8; the goal has kind `AND`,
  `OR(R,QB)` has kind `OR`, `NOT(R)` has kind `NOT`, and the `H_j` case is
  A.8 verbatim.
- **Satisfiability.** Take `nu_B(a) = False for a in A_R`, `True otherwise`.
  `R` is positive over `A_R`, so all its leaves are false and, by induction on a
  positive formula, `R` is false; hence `NOT(R)` is true. `QB` is positive over
  `A_T`, so `QB` is true; hence `OR(R, QB)` is true. Each `H_j` is an `AND`-spine
  over `A_chain = A_T` atoms, all true, so `H_j` is true. All globals are
  simultaneously true. No global hypothesis is `FALSE`: `FALSE` occurs in a
  scaffold-B plan only as the `NOT_ELIM` node conclusion, which is not a
  hypothesis.
- Families: `AND_INTRO`, `OR_ELIM`, `NOT_ELIM`, `EXFALSO`, plus `AND_ELIM`
  (always, since `S >= 2`). Branching by `AND_INTRO` and `OR_ELIM`.
- Depth: `NOT_ELIM` has two `ASSUME` children, depth `0`; `EXFALSO` depth `1`;
  `OR_ELIM` depth `2`; so gadget depth `g_d = 2` and plan depth `>= 4`.
- Normality: the `OR_ELIM` major is an `ASSUME`, the `NOT_ELIM` negative is an
  `ASSUME`, chains are safe by 5.2. `EXFALSO` is not a redex position in charter
  section 2.3.
- Sizes, with `r = formula_nodes(R)`, `qb = formula_nodes(QB)`, and the section
  6.3 bounds `qb <= 17`, `r + qb <= 22`:

```text
OR(R,QB)   = 1 + r + qb   <= 23
NOT(R)     = 1 + r        <= 18
goal       = 6 + qb       <= 23
AND(T2,QB) = 2 + qb       <= 19
conclusion FALSE = 1;  local assumptions R, QB;  H_j <= 23
```

- **Eligible atom count `k in 4..6`.** This is derived and load-bearing, not a
  preference: scaffold B needs `|A_T| >= 3` for three distinct chain atoms and
  `|A_R| >= 1` for a false atom, and no valuation can make `R` false while
  keeping every chain atom true unless `A_R` and `A_chain` are disjoint. `k = 3`
  is therefore infeasible for scaffold B, and `k` is drawn uniformly over
  `4..6` under meta-law U.

**Why this is not a v1 relapse.** `EXFALSO` here consumes a contradiction that
exists **only under the local assumption `l0 : R`**, inside one `OR_ELIM`
branch. The global context is explicitly satisfiable, so `globals |- FALSE` is
underivable by soundness, and the goal is not proof-irrelevant: the other three
conjuncts must still be derived from their own hypotheses.

### 5.5 Scaffold C - negation introduction (`NOT_INTRO` + `NOT_ELIM`)

Alphabet split identical to scaffold B: `A_R` nonempty with `|A_R| <= k - 3`,
`A_T = alphabet \ A_R`, `A_chain = A_T`. `R = sample_positive(A_R, ...)` (D6),
`V = sample_positive(A_T, ...)` (D7). Let

```text
M = AND(R, V)     if dir == AND_ELIM_LEFT
  = AND(V, R)     if dir == AND_ELIM_RIGHT
```

```text
W = NOT(M)

globals contributed: NOT(R)   (h0)

GADGET =
  NOT_INTRO(                                                      # node 1
    assumption = {'id': l0, 'formula': M},
    body       = NOT_ELIM(                                        # node 2
                   negative   = ASSUME(h0 : NOT(R)),              # 0 nodes
                   positive   = dir( source = ASSUME(l0 : M),     # node 3
                                     conclusion = R ),
                   conclusion = FALSE ),
    conclusion = NOT(M) )
```

- Cost exactly `3`: `NOT_INTRO`, `NOT_ELIM`, one `AND_ELIM_*`.
- Typing: the `AND_ELIM_*` node has an `AND` source `M` whose `dir`-side
  component is `R`, so it concludes `R`. `NOT_ELIM` has `negative` concluding
  `NOT(R)` and `positive` concluding `R`, so it concludes `FALSE`. `NOT_INTRO`
  checks its body under the fresh local `l0 : M`, requires body conclusion
  `FALSE`, and concludes `NOT(M)`.
- Locals: `l0` is referenced by the `ASSUME` under the `AND_ELIM_*`, which lies
  inside the `NOT_INTRO` body.
- Globals used: `NOT(R)` by the `NOT_ELIM` negative, `H_j` by chain `j`. Kind
  `NOT` versus `ATOM`/`AND` gives uniqueness against every `H_j`.
- Coverage: `atoms(R) = A_R` in the global `NOT(R)`; `atoms(V) = A_T` in the goal
  through `W = NOT(M)`. Union is the alphabet.
- Goal not a hypothesis: goal kind `AND`, `NOT(R)` kind `NOT`; `H_j` by A.8.
- **Satisfiability.** Globals are `NOT(R)` and the `H_j`. Under
  `nu_C = nu_B` (`False` on `A_R`, `True` elsewhere), `R` is false so `NOT(R)` is
  true, and every `H_j` is an `AND`-spine over `A_T` atoms, true. `V` occurs only
  in the goal and in a **local** assumption, never in a global, so its truth
  value is irrelevant to global satisfiability. No global hypothesis is `FALSE`.
- Families: `AND_INTRO`, `AND_ELIM` (always, from the gadget), `NOT_INTRO`,
  `NOT_ELIM`. Branching by `AND_INTRO`.
- Depth: `AND_ELIM_*` depth `0`, `NOT_ELIM` depth `1`, `NOT_INTRO` depth `2`, so
  `g_d = 2` and plan depth `>= 4`.
- Normality: the `NOT_ELIM` negative is an `ASSUME`, not a `NOT_INTRO`; the
  gadget `AND_ELIM_*` source is an `ASSUME`, not an `AND_INTRO`; there is no
  `OR_ELIM`.
- Sizes, with `r = formula_nodes(R)`, `v = formula_nodes(V)` and the section 6.3
  bound `r + v <= 16`:

```text
NOT(R)     = 1 + r         <= 16      (v >= 1, so r <= 15)
M          = 1 + r + v     <= 17
W = NOT(M) = 2 + r + v     <= 18
goal       = 8 + r + v     <= 24
AND(T2,W)  = 4 + r + v     <= 20
conclusions R, FALSE;  local assumption M;  H_j <= 23
```

- Eligible atom count `k in 4..6`, for the same derived reason as scaffold B.

### 5.6 The frozen catalogue

```text
L2_SCAFFOLDS = ('A', 'B', 'C')
```

This literal tuple is the **sole** catalogue. It is selected at D2 uniformly
over its three members under meta-law U, so `len(L2_SCAFFOLDS) == 3` is a frozen
constant of the byte schedule.

There is no alternative catalogue, no optional member, no conditional
catalogue branch and no configuration point. The scaffold `Bp` offered as
alternative V1(b) in the withdrawn choices packet is **withdrawn and is not
eligible**, for a reason of substance and not of preference: its characteristic
goal leaf `W = NOT(R)` is byte-identical to the global hypothesis `NOT(R)` that
its own gadget consumes, so the entire three-node gadget can be replaced by
`ASSUME(h0 : NOT(R))` with no loss, and its single `EXFALSO` maps `FALSE` to
`FALSE` and transforms nothing. `Bp` therefore demonstrates syntactic family
occurrence rather than an earned characteristic obligation, which violates the
v1 X/Y disposition's requirement that the finite catalogue be
composition-bearing. No replacement member is introduced: A/B/C is already the
minimum meaningful catalogue, and scaffold B uses `EXFALSO` in its
characteristic role, deriving the actual non-`FALSE` branch obligation `QB`.

No scaffold may be added, removed or altered after acceptance without a new
annex version and new permanently excluded fixtures.

**Rule-kind and family reachability across the catalogue.**

| element | scaffold(s) that emit it |
|---|---|
| `ASSUME` | A, B, C (every plan) |
| `AND_INTRO` | A, B, C (three nodes per plan) |
| `AND_ELIM_LEFT` | A, B, C with `dir = AND_ELIM_LEFT`; C's gadget |
| `AND_ELIM_RIGHT` | A, B, C with `dir = AND_ELIM_RIGHT`; C's gadget |
| `OR_INTRO_LEFT` | A (every plan) |
| `OR_INTRO_RIGHT` | A (every plan) |
| `OR_ELIM` | A, B (every plan) |
| `NOT_INTRO` | C (every plan) |
| `NOT_ELIM` | B, C (every plan) |
| `EXFALSO` | B (every plan) |
| family `AND_INTRO` | A, B, C |
| family `AND_ELIM` | A, B, C (always, `S >= 2`) |
| family `OR_INTRO` | A |
| family `OR_ELIM` | A, B |
| family `NOT_INTRO` | C |
| family `NOT_ELIM` | B, C |
| family `EXFALSO` | B |

All ten rule kinds and all seven families are reachable, and each is reachable
from a scaffold that emits it in **every** one of its draws, so coverage of the
fixed fixture set depends only on the scan encountering each
`(scaffold, dir)` pair, not on a rare event inside a scaffold.

### 5.7 Construct constraints: by design or by typed failure

| charter constraint | discharge |
|---|---|
| exactly the target `8..37` non-`ASSUME` nodes | by design, `N = 6 + L0 + L1 + L2` with an exact triple enumeration, section 7.2; guard `SIZE_CONSERVATION_VIOLATED` |
| no sharing, plan is a tree | by design, `fresh` copy discipline, section 8.4 |
| conclusions by natural-deduction typing | by design, each scaffold's typing proof, sections 5.2-5.5 |
| `3..6` sorted declared atoms | by design, D3 fixes `k` from the scaffold's eligible range; `atoms = ('a0'..'a{k-1}')` is ascending byte-lexicographic for `k <= 6` |
| every declared atom occurs publicly | by design, per-scaffold coverage proof (A.6, 5.4, 5.5); guard `ATOM_COVERAGE_UNSATISFIABLE` |
| every atom used anywhere is declared | by design, every atom leaf drawn from the alphabet |
| lexical and plan-wide local IDs | by design, single `next_local` counter, section 7.3 |
| global IDs | by design, `next_global` counter in a frozen mint order, section 7.3 |
| every global hypothesis used | by design, per-scaffold use proof |
| every local hypothesis used in its scope | by design, per-scaffold local-use proof |
| no duplicate global formula | by design, per-scaffold uniqueness proof (A.4) |
| formula size `<= 24` everywhere | by design, section 6.3 derived sampling bounds; guard `FORMULA_BOUND_UNSATISFIABLE` |
| dependency depth `>= 2` | by design, depth `>= 3` (A) or `>= 4` (B, C) |
| at least three families | by design, `>= 4` families in every scaffold |
| `AND_INTRO` or `OR_ELIM` | by design, three `AND_INTRO` nodes in every plan |
| none of the three immediate beta-redexes | by design, per-scaffold normality proof |
| global context classically satisfiable | by design, per-scaffold valuation; guard `NONVACUITY_GUARD_VIOLATED` |
| no global `FALSE`, no global equal to the goal | by design, sections 5.3-5.5; same guard |

The generator never weakens the accepted checker, never assumes the checker will
repair a malformed candidate and never inspects a checker result. Every row above
is an independent construction obligation; the L1 checker remains the sole
acceptance authority and the code gate asserts acceptance rather than assuming
it.

## 6. Item 7 - formula generation

### 6.1 Positive fragment

Sampled formulas use only

```text
F ::= ATOM(a_i) | AND(F,F) | OR(F,F)
```

`NOT` and `FALSE` are **never** produced by the sampler. They occur in a plan
only where a scaffold places them explicitly (`NOT(R)`, `NOT(M)`, and the
`FALSE` conclusion of a `NOT_ELIM` node). This restriction is load-bearing:

> **Lemma POS.** For a positive formula `F` with `atoms(F) = C`: if every atom
> of `C` is true under a valuation then `F` is true; if every atom of `C` is
> false then `F` is false.

Proof by induction. `ATOM(a)` is immediate. `AND(X,Y)` and `OR(X,Y)` have
`atoms(X), atoms(Y) subset C`, and both connectives preserve "all true implies
true" and "all false implies false". Lemma POS is exactly what makes each
scaffold's declared valuation checkable in linear time.

Implication is never generated; there is no implication constructor in the
charter's AST. `AND` and `OR` are treated as **ordered** pairs at L2: `left` and
`right` are generated independently and never reordered, sorted or commutatively
normalized. L2 performs no alpha-renaming, no theorem canonicalization and no
skeleton canonicalization; charter sections 5.1-5.3 assign all of that to L3.

### 6.2 `sample_positive(cursor, cover, n_max)`

`cover` is a sorted tuple of `m >= 1` distinct atom names; `n_max >= m` is a
derived leaf-count ceiling (section 6.3). The result is a positive formula with
exactly `n` leaves, hence exactly `2n - 1` AST nodes, whose atom set is exactly
`cover`. There is no rejection loop and no size retry.

```text
sample_positive(cursor, cover, n_max):
  m = len(cover)
  SF1: e = randbelow(cursor, n_max - m + 1);   n = m + e
  SF2: t = randbelow(cursor, comb(n, m))
       pos = colex_unrank(n, m, t)        # ascending m-tuple in 0..n-1
  SF3: p = randbelow(cursor, factorial(m))
       perm = lehmer_decode(m, p)         # a permutation of 0..m-1
  labels = [None] * n
  for r in 0..m-1: labels[pos[r]] = cover[perm[r]]
  SF4: for each index i in ascending order with labels[i] is None:
         labels[i] = cover[randbelow(cursor, m)]
  return build_shape(cursor, labels)

build_shape(cursor, labels):
  if len(labels) == 1:
      return {'kind': 'ATOM', 'name': labels[0]}
  SF5: nl = 1 + randbelow(cursor, len(labels) - 1)
  SF6: c = ('AND', 'OR')[randbelow(cursor, 2)]
  left  = build_shape(cursor, labels[0:nl])
  right = build_shape(cursor, labels[nl:])
  return {'kind': c, 'left': left, 'right': right}
```

Consumption order inside one `sample_positive` call is exactly
`SF1, SF2, SF3, SF4 (ascending index), SF5/SF6 in preorder with SF5 before SF6,
then the whole left subtree, then the whole right subtree`. Nothing else
consumes a word.

- **Exact size.** A binary tree over `n` leaves has `n - 1` internal nodes, so
  `formula_nodes = 2n - 1`. Sizes produced by the sampler are always odd; the
  derived ceilings of section 6.3 are stated in leaf counts precisely so that no
  even size is ever requested.
- **Exact atom set.** `pos` selects `m` distinct positions and `perm` writes each
  element of `cover` to exactly one of them, so `cover subset atoms(F)`. Every
  other label is drawn from `cover`, so `atoms(F) subset cover`. Hence
  `atoms(F) = cover`, and the coverage obligation of each scaffold is discharged
  without a rejection.
- **Totality.** `n_max - m + 1 >= 1`, `comb(n,m) >= 1`, `factorial(m) >= 1`, and
  `len(labels) - 1 >= 1` inside the recursive branch, so every `randbelow`
  argument is a positive integer and `PRF_RANGE_REFUSED` cannot fire.
- **Bounds on `n`.** Section 6.3 gives `n <= 9` for every field of every
  scaffold, and every cover is a proper nonempty subset of the alphabet, so
  `1 <= m <= 5`. Hence `comb(n, m) <= comb(9, 4) = 126` and
  `factorial(m) <= factorial(5) = 120`, both far inside the 64-bit word range.
- **Recursion.** `build_shape` recurses at most `n <= 9` deep.
- **Word count.** `W(n, m) = 3 + (n - m) + 2 (n - 1)`.
- **Disclosed non-uniformity.** Each of SF1, SF2, SF3, SF4, SF5, SF6 is uniform
  over its own frozen range, per meta-law U. The induced law on tree shapes is
  not uniform over the `Catalan(n-1)` shapes, and the induced law on label
  sequences is not uniform over surjections onto `cover`. This annex does not
  claim otherwise and introduces no weights to correct it.

`colex_unrank(n, m, t)` is the standard colexicographic unranking of the
`t`-th `m`-subset of `0..n-1`: choose the largest `c_m` with
`comb(c_m, m) <= t`, subtract, recurse on `m - 1`. `lehmer_decode(m, p)` is the
standard factorial-base decoding of `p` into a permutation of `0..m-1`. Both are
deterministic and consume no word.

### 6.3 Derived leaf-count ceilings

Let `k` be the declared atom count and let `m1`, `m2` be the cover sizes of the
scaffold's first and second sampled field. Fields are sampled in the frozen
order of section 7.1. The ceilings below are derived from
`MAX_FORMULA_NODES = 24` alone; there is **no** soft cap and no author cell for
formula breadth.

Scaffold A (`m1 = |A_P|`, `m2 = |A_Q|`, `m1 + m2 = k`). The binding constraint
is the goal, `7 + p + q <= 24`, i.e. `p + q <= 17`; since `p` and `q` are odd,
`p + q = 2(n_P + n_Q) - 2 <= 16`, i.e. `n_P + n_Q <= 9`.

```text
field 1 (P):  n_max = 9 - k + m1        so  e_P in [0, 9 - k]
field 2 (Q):  n_max = 9 - n_P           so  e_Q in [0, 9 - k - e_P]
```

Scaffold B (`m1 = |A_R|`, `m2 = |A_T|`, `m1 + m2 = k`). Two constraints:
`OR(R,QB) = 1 + r + qb <= 24` gives `n_R + n_QB <= 12`; `goal = 6 + qb <= 24`
gives `qb <= 18`, i.e. `n_QB <= 9`.

```text
field 1 (R):   n_max = 12 - k + m1                   so  e_R  in [0, 12 - k]
field 2 (QB):  n_max = min(9, 12 - n_R)              so  e_QB in [0, n_max - m2]
```

Scaffold C (`m1 = |A_R|`, `m2 = |A_T|`, `m1 + m2 = k`). The binding constraint
is the goal, `8 + r + v <= 24`, i.e. `r + v <= 16`, i.e. `n_R + n_V <= 9`.

```text
field 1 (R):  n_max = 9 - k + m1        so  e_R in [0, 9 - k]
field 2 (V):  n_max = 9 - n_R           so  e_V in [0, 9 - k - e_R]
```

**Lemma NB (every ceiling range is nonempty).** For scaffolds A and C,
`k <= 6` gives `9 - k >= 3 >= 0`, and after `e_field1 <= 9 - k` the second range
`[0, 9 - k - e_field1]` is nonempty. For scaffold B, `k <= 6` gives
`12 - k >= 6 >= 0`; and `12 - n_R = 12 - m1 - e_R >= 12 - m1 - (12 - k) = m2`,
while `m2 = k - m1 <= 6 - 1 = 5 <= 9`, so `min(9, 12 - n_R) >= m2` and
`e_QB in [0, min(9, 12 - n_R) - m2]` is nonempty. Hence
`FORMULA_BOUND_UNSATISFIABLE` cannot fire.

**Lemma CB (every emitted formula respects the 24-node bound).** By construction
`formula_nodes = 2n - 1` with `n` inside the ceilings above; substituting the
worst case into the size tables of sections 5.3, 5.4 and 5.5 gives at most `24`
for every formula that the accepted `_walk_formulas` inspects. Scaffold C's goal
attains exactly `24` in the worst case, which is legal (`<= MAX_FORMULA_NODES`).

## 7. Items 5 and 6 - schedule, allocation and identifiers

### 7.1 The exact finite ordered decision schedule

Every random decision in a draw is one of the following, in this order. Nothing
else consumes a word. Each entry is one `randbelow` call unless a count is
given, and every call obeys the uniform call discipline of section 3.3
(a singleton range still consumes exactly one word).

```text
D0   target band                     no word; ('S1','S2','S3','S4')[draw_index % 4]
D1   target node count N             randbelow(band_hi - band_lo + 1)
D2   scaffold index                  randbelow(len(L2_SCAFFOLDS))
D3   declared atom count k           randbelow(k_hi - k_lo + 1)
D4   alphabet split size s           randbelow(s_hi - s_lo + 1)
D5   alphabet split subset index     randbelow(comb(k, s))
D6   gadget free field 1             sample_positive(...)   W(n1, m1) calls
D7   gadget free field 2             sample_positive(...)   W(n2, m2) calls
D8   chain leaf T0                   randbelow(len(A_chain))
D9   chain leaf T1                   randbelow(len(A_chain) - 1)
D10  chain leaf T2                   randbelow(len(A_chain) - 2)
D11  chain-length triple index       randbelow(len(TRIPLES(S)))
D12  AND_ELIM direction              randbelow(2)
D13  chain padding atoms             randbelow(len(A_chain))   S calls
```

Per-scaffold parameters, frozen:

| scaffold | `(k_lo, k_hi)` | D4 range `(s_lo, s_hi)` | D5 subset is | `A_chain` | D6 field 1 | D7 field 2 |
|---|---|---|---|---|---|---|
| A | `(3, 6)` | `(1, k - 1)` | `A_P` | `alphabet` | `P` over `A_P` | `Q` over `A_Q` |
| B | `(4, 6)` | `(1, k - 3)` | `A_R` | `A_T` | `R` over `A_R` | `QB` over `A_T` |
| C | `(4, 6)` | `(1, k - 3)` | `A_R` | `A_T` | `R` over `A_R` | `V` over `A_T` |

`A_Q = alphabet \ A_P`; `A_T = alphabet \ A_R`. D5 unranks the `s`-subset of
`(0, ..., k-1)` in colexicographic order and maps indices to `a0..a{k-1}`.

D8/D9/D10 draw ordered distinct atoms: `A_chain` is a sorted tuple; `T0` is its
`i0`-th element; `T1` is the `i1`-th element of the tuple with `T0` removed;
`T2` is the `i2`-th element of the tuple with `T0` and `T1` removed. This
requires `len(A_chain) >= 3`, which the per-scaffold `k` range guarantees.

D13 draws padding atoms in the order: chain `0` positions `i = 1..L0`
(innermost wrapper first), then chain `1`, then chain `2`.

**The free-field order is explicit per scaffold in the table above.** This annex
does not refer to `PROOF_CHILD_FIELDS` or any other schema child order to fix a
free-field draw order; the v1 defect identified as Fable m-b is thereby removed.

Total words consumed by a draw, excluding `randbelow` rejections:

```text
words = 5 + W(n1, m1) + W(n2, m2) + 3 + 1 + 1 + S
      = 10 + W(n1, m1) + W(n2, m2) + S
```

with `W(n, m) = 3 + (n - m) + 2(n - 1)` from section 6.2. Since
`W(n1,m1) + W(n2,m2) = 2 + 3(n1 + n2) - k`, the ceilings of section 6.3 give at
most `2 + 3*12 - 4 = 34` for scaffold B and `2 + 3*9 - 3 = 26` for scaffolds A
and C, so a draw consumes at most `10 + 34 + 31 = 75` words.

Every member of `L2_SCAFFOLDS` has exactly two free fields, D6 and D7 both occur
in every draw, and the schedule `words = 10 + W(n1,m1) + W(n2,m2) + S` has no
exception.

### 7.2 Chain-length allocation - exact triple enumeration

```text
S = N - 6
TRIPLES(S) = the ascending lexicographic list of all (L0, L1, L2)
             with 0 <= Lj <= CHAIN_LEN_CAP = 11 and L0 + L1 + L2 == S
if TRIPLES(S) is empty: guard TARGET_SIZE_UNREACHABLE
D11: j = randbelow(cursor, len(TRIPLES(S)));  (L0, L1, L2) = TRIPLES(S)[j]
```

`N in 8..37` gives `S in 2..31`, and `3 * 11 = 33 >= 31`, so `TRIPLES(S)` is
never empty (section 9.3).

**Normative implementation clause.** D11 constructs the ascending lexicographic
list of triples by **direct enumeration** and passes its actual `len(...)` to
`randbelow`. The closed form below is a review aid and a test oracle only. It is
never an executable substitute for the enumeration, and an implementation that
computes the `randbelow` argument from a closed form rather than from the
enumerated list is a defect, whether or not the two agree.

By inclusion-exclusion over the three upper bounds `Lj <= 11`, for
`0 <= S <= 33`:

```text
len(TRIPLES(S)) = comb(S+2,2) - 3*comb(S-10,2) + 3*comb(S-22,2)
```

with each binomial term taken as zero when its upper argument is below `2`. The
third term counts the pairwise overlaps in which two coordinates are both at
least `12`; no triple-overlap term occurs because `S < 36`.

**Bounded cardinality regression.** The gate asserts, for every `S` in `0..33`,
that direct enumeration returns exactly the value tabulated here, that it equals
the three-term closed form, that the symmetry `count(S) == count(33 - S)` holds,
and that `sum over S of count(S) == 12**3 == 1728`.

```text
S     :   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
count :   1   3   6  10  15  21  28  36  45  55  66  78  88  96 102 106 108

S     :  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33
count : 108 106 102  96  88  78  66  55  45  36  28  21  15  10   6   3   1
```

The maximum is `108`, attained at `S = 16` and `S = 17`, so every bound stated
elsewhere in this annex that depends on `len(TRIPLES(S))` holds: the Lemma T1
argument bound `len(TRIPLES(S)) <= 108`, the global maximum `randbelow` argument
`126` (which comes from `comb(9,4)` in the sampler, not from D11), the per-word
rejection bound `125 / 2**64`, the one-word cost of D11, the closed-form word
counts of section 7.1 and the `MAX_DECISION_CALLS = 128` guard. Over the
reachable range `S in 2..31` the cardinality lies in `6..108`, so the D11
`randbelow` argument is always at least `1` and Lemma T3 is unaffected.

The enumeration is cheap and the `randbelow` argument is far inside range. There
is no post-hoc bump, repair or retry.

### 7.3 Hypothesis identifiers

Global identifiers are minted `h0, h1, ...` in a frozen per-scaffold order,
consuming no word:

```text
A : h0 = OR(P, QQ)      h1 = H_0   h2 = H_1   h3 = H_2      (QQ denotes Q)
B : h0 = OR(R, QB)      h1 = NOT(R)   h2 = H_0   h3 = H_1   h4 = H_2
C : h0 = NOT(R)         h1 = H_0   h2 = H_1   h3 = H_2
```

The plan's `hypotheses` list is that mint order. The accepted checker imposes no
order on that list; L3 alone reorders by sorted formula bytes for identity, and
L2 makes no identity claim. Contraction is not needed: each scaffold's globals
are pairwise byte-distinct by construction, and each is referenced by at least
one `ASSUME` leaf.

Local identifiers are minted `l0, l1, ...` from one plan-wide counter in the
scaffold's own binder order, consuming no word: scaffold A and B mint `l0` for
the `OR_ELIM` left assumption and `l1` for the right; scaffold C mints `l0` for
the `NOT_INTRO` assumption. Plan-wide pairwise distinctness follows from the
single counter, and the `hN`/`lN` namespaces are disjoint by grammar, so no
shadowing is possible. L2 assigns local identifiers in its own construction
order and makes no claim that this order equals L3's "preorder first
introduction" normalization. L3 owns that.

### 7.4 `fresh` and the no-aliasing discipline

`fresh(F)` is the deep-copy constructor for formulas: it allocates a new `dict`
per formula node. Every formula written into any node field, hypothesis record or
plan field is the result of `fresh` on a value not otherwise stored, so no two
positions in the emitted plan share a mutable object. A hypothesis record's
`formula` and each referencing leaf's `conclusion` are separate copies; a
binder's `assumption['formula']` and the branch's `ASSUME.conclusion` are
separate copies; no proof node object is ever placed in two slots.

## 8. Items 8 and 11 - expectation, guards and mechanical invariants

### 8.1 Expectation derivation and cross-check

Two independent computations must agree.

1. **Closed-form accumulator.** From the scaffold parameters alone:

```text
node_count = 6 + L0 + L1 + L2
families   = FAM(scaffold) union ({'AND_ELIM'} if S >= 1 else {})
depth      = section 8.2
```

with

```text
FAM(A)  = {AND_INTRO, OR_INTRO, OR_ELIM}
FAM(B)  = {AND_INTRO, OR_ELIM, NOT_ELIM, EXFALSO}
FAM(C)  = {AND_INTRO, AND_ELIM, NOT_INTRO, NOT_ELIM}
```

2. **Post-construction traversal.** `summarize_plan(proof)` is an
   explicit-stack, non-recursive post-order traversal over the **emitted** plan
   that recomputes `count`, `depth` and `family_set` from the charter section 2.2
   definitions: `count = 1 + sum(child counts)` for an inference node and `0` for
   an `ASSUME`; `depth = 0` when no child is an inference node, else
   `1 + max(inference child depths)`; `family_set` unions `KIND_TO_FAMILY[kind]`.
   It uses an iterative worklist rather than the checker's three separate
   recursive functions, and neither imports nor copies `phase2_stageb_checker`.
   The import-graph test of section 8.6 pins that.

Disagreement between (1) and (2) is the guard `EXPECTATION_DISAGREEMENT`. A
`count` differing from `target_node_count` is the guard
`SIZE_CONSERVATION_VIOLATED`.

The emitted expectation is exactly charter section 3.5:

```text
{'schema': 'philosophia.stageb.plan-expectation.v1',
 'node_count': count,
 'band': band_of_node_count(count),
 'families': [f for f in FAMILY_ORDER if f in family_set],
 'max_dependency_depth': depth}
```

`families` is duplicate-free and ordered by the frozen seven-family order.
`node_count` and `max_dependency_depth` are Python `int`, never `bool`. The
expectation is the draw's **target and record**; acceptance belongs solely to
L1, and L2 asserts nothing about it.

Inference-only dependency depth is computed exactly as charter section 2.2
defines it: one vertex per non-`ASSUME` node, an edge only to a non-`ASSUME`
child, and the longest directed path in edges. Edges into `ASSUME` leaves do not
count.

### 8.2 Closed-form depth

Let `g_d` be the gadget top-node depth: `g_d = 1` for scaffold A, `g_d = 2` for
scaffolds B and C. Let `c(L) = L - 1` be the chain-top depth for `L >= 1`; a
chain with `L = 0` is an `ASSUME` and contributes no edge.

```text
dL = 0                                        if L0 == 0 and L1 == 0
   = 1 + max{ c(Lj) : j in {0,1}, Lj >= 1 }   otherwise
dR = 1 + max({ g_d } union { c(L2) : L2 >= 1 })
depth = 1 + max(dL, dR)
```

`dR >= 1 + g_d >= 2`, so `depth >= 3` for scaffold A and `depth >= 4` for
scaffolds B and C. `MIN_DEPENDENCY_DEPTH = 2` is met unconditionally.

### 8.3 The non-vacuity guard

Before the success record is returned, the generator computes, from the emitted
plan and the scaffold's **declared** valuation `nu` (all-true for A;
`False` on `A_R`, `True` elsewhere for B and C):

```text
NV1  every global hypothesis formula evaluates to True under nu
NV2  no global hypothesis formula has kind 'FALSE'
NV3  canonical_bytes(hyp['formula']) != canonical_bytes(plan['goal'])
     for every global hypothesis
```

Any violation returns the failure record with subcause
`NONVACUITY_GUARD_VIOLATED`. Evaluation is a direct structural recursion over
the five formula kinds with a `{atom_name -> bool}` environment; it is linear in
the formula and consumes no word.

This is an **L2 construction guard on the L2 population**. It is not a new L1
predicate, it does not alter `check_plan`, and it does not reorder charter
section 8. Sections 5.3, 5.4 and 5.5 prove NV1-NV3 hold by construction for
every catalogue member, so the guard is fail-closed on an implementation defect.

An exhibited satisfying Boolean valuation is a **sufficient certificate** that
the global context cannot intuitionistically derive `FALSE`. By soundness of
intuitionistic natural deduction with respect to classical two-valued semantics,
`globals |- FALSE` would force every valuation to falsify some global
hypothesis; exhibiting one valuation that satisfies all of them therefore rules
out exactly the degeneration the v1 X/Y disposition proved. The certificate is
decisive for that property and for nothing else.

NV1-NV3 together are an **imposed population guard**, adopted to exclude
explosion from the L2 population. They are not evidence of difficulty, of
minimality, or of substantive proof relevance, and no later stage may read them
as such. Shortcut and minimality risk remain owned by the later
alternative-proof audit.

### 8.4 No aliasing, no hidden DAG sharing

The gate walks the emitted plan collecting `id()` of every `dict` and `list` and
asserts they are pairwise distinct, which fails on any accidental alias or
shared subtree. See section 7.4 for the construction-side discipline.

### 8.5 Canonical byte stability and bounded work

`canonical_bytes(result)` is stable across repeated calls in one process and
byte-identical across fresh processes (section 10.1). L2 uses the single Stage-A
serializer from `phase2_stageb_canonical`; no second serializer is introduced.

Derived bounds, enforced as fail-closed guards on the cursor counters:

```text
MAX_FORMULA_RECURSION_FRAMES = MAX_FORMULA_NODES = 24
MAX_DECISION_CALLS           = 128
```

Justification. There is no proof-node recursion: the frame of section 5.1 is
instantiated directly and `CHAIN(j)` is built by an iterative loop of at most
`11` steps. `build_shape` recurses at most `n <= 9` levels, matching the ceiling
derived in sections 6.2 and 6.3, and `fresh` recurses
at most `24` levels, since each level consumes at least one formula node. The
decision count is `10 + W(n1,m1) + W(n2,m2) + S <= 10 + 34 + 31 = 75` by section
7.1, so `128` is a strict upper bound with margin and cannot be reached by any
legal schedule. All bounds are far below the default interpreter recursion limit,
which is why no `RecursionError` can escape L2; the closure forward obligation
"L2 must preserve the 24-formula-node and 37-plan-node construction bounds before
calling the recursive L1 checker" is discharged by these bounds together with
sections 5.2 and 6.3.

Exceeding a bound returns `RECURSION_BOUND_EXCEEDED` or `WORK_BOUND_EXCEEDED`;
neither can fire under section 9.

### 8.6 Import-graph boundary

The gate parses `learning/phase2_stageb_generator.py` with `ast` and asserts the
imported top-level module set is a subset of

```text
{'phase2_stageb_schema', 'phase2_stageb_canonical', 'phase2_stageb_causes',
 'hmac', 'hashlib', 'math', 'typing', '__future__', 'annotations'}
```

and disjoint from

```text
{'phase2_stageb_checker', 'phase2_stageb_render', 'peano', 'torch',
 'proofsearch', 'policy', 'phase2_policy', 'phase2_search', 'phase2_root',
 'phase2_isolated', 'phase2_actions', 'phase2_spec', 'transformers', 'numpy',
 'random', 'secrets', 'os', 'subprocess', 'json'}
```

`random` and `secrets` are forbidden because the only entropy source is the
frozen PRF. `json` is forbidden in production because canonical bytes come from
the L0 helper. `math` is admitted solely for `comb` and `factorial`; the gate
asserts no other `math` attribute is referenced. The gate also asserts the
source contains none of the substrings `check_plan`, `skeleton`, `bijection`,
`public_projection`, `compile`, `alpha`, `canonicaliz`.

### 8.7 Distinctions the gate must state, not blur

Construction feasibility, L1 acceptance and quota fill are three different
things. The gate may assert the first two. It may not assert, imply or measure
the third, and no fixture may be described as yield, band reachability, interface
survival or scientific evidence.

## 9. Feasibility on paper

### 9.1 Totality of the specified algorithm

**Lemma T1 (every `randbelow` argument is legal).** D1: band width in
`{4,6,8,12}`. D2: `len(L2_SCAFFOLDS) == 3`. D3: `k_hi - k_lo + 1 in {3,4}`.
D4: `s_hi - s_lo + 1 = k - 1 >= 2` for A and `= k - 3 >= 1` for B/C, both
positive because `k >= 3` for A and `k >= 4` for B/C. D5: `comb(k,s) >= 1`.
D6/D7: Lemma NB plus section 6.2. D8/D9/D10: `len(A_chain) >= 3`, so the three
arguments are `>= 3, >= 2, >= 1`. D11: `len(TRIPLES(S)) >= 1` by Lemma T3.
D12: `2`. D13: `len(A_chain) >= 3`. Hence `PRF_RANGE_REFUSED` cannot fire.

The same enumeration bounds every argument from above: band width `<= 12`,
`len(L2_SCAFFOLDS) == 3`, `k_hi - k_lo + 1 <= 4`, `s` range `<= 5`,
`comb(k,s) <= comb(6,3) = 20`, `len(A_chain) <= 6`,
`len(TRIPLES(S)) <= 108` (section 7.2), and inside `sample_positive`
`comb(n,m) <= comb(9,4) = 126`, `factorial(m) <= factorial(5) = 120`,
`n_max - m + 1 <= 9`, `len(labels) - 1 <= 8`, `2`. The maximum `randbelow`
argument reachable anywhere in this annex is therefore `126`, which is the bound
used in section 2.5.

**Lemma T2 (no unbounded loop).** The schedule of section 7.1 is a finite
sequence determined by `(N, scaffold, k, s, n1, n2, S)`, all of which are fixed
before the loops they bound. `build_shape` recurses on strictly shorter label
lists. `CHAIN(j)` iterates exactly `L_j <= 11` times. The only loop whose trip
count is not fixed in advance is `randbelow`'s rejection loop, bounded by
`PRF_MAX_REJECTIONS_PER_CALL = 64`.

**Theorem (totality as success-or-failure).** By T1 and T2 every draw terminates
after at most `128 * 65` word reads and returns exactly one record. Every
subcause other than `PRF_REJECTION_BUDGET_EXCEEDED` is proved unreachable:
`PRF_RANGE_REFUSED` by T1; `TARGET_SIZE_UNREACHABLE` by T3;
`FORMULA_BOUND_UNSATISFIABLE` by Lemmas NB and CB;
`ATOM_COVERAGE_UNSATISFIABLE` by the per-scaffold coverage proofs;
`NONVACUITY_GUARD_VIOLATED` by the per-scaffold satisfiability proofs;
`SIZE_CONSERVATION_VIOLATED` and `EXPECTATION_DISAGREEMENT` by T4;
`RECURSION_BOUND_EXCEEDED` and `WORK_BOUND_EXCEEDED` by section 8.5.
`PRF_REJECTION_BUDGET_EXCEEDED` is **not** proved unreachable; see section 2.5.

**Lemma T4 (size and expectation agree).** The emitted plan contains exactly
`3` `AND_INTRO` nodes, exactly `3` gadget nodes and exactly `L0 + L1 + L2` chain
nodes, all non-`ASSUME`, and no other non-`ASSUME` node. So
`inference_node_count(proof) = 6 + S = N` and the closed-form accumulator agrees
with `summarize_plan` by the same case analysis. The depth formula of section 8.2
is the same recursion the traversal performs.

### 9.2 Non-vacuity for the actual frozen catalogue

For every catalogue member and every reachable parameter tuple:

- the complete global hypothesis set has an explicit satisfying valuation
  (A.7, 5.4, 5.5), so by soundness the context does not derive `FALSE`;
- `FALSE` is not a global hypothesis;
- no global hypothesis is byte-identical to the goal (A.8 and its restatements);
- there is no root-level `EXFALSO` and no proof of `FALSE` from the globals: the
  root of every plan is `AND_INTRO`, and `EXFALSO` occurs only in scaffold B,
  strictly inside one `OR_ELIM` branch, under the local assumption `l0 : R`;
- `NOT_ELIM` occurs only in scaffold B (under `l0 : R`, against the global
  `NOT(R)`) and in scaffold C (under `l0 : M`, against the global `NOT(R)`). In
  both cases the contradiction is **local**: `nu` makes `R` false and `NOT(R)`
  true, so the global context is untouched.

The goal is not proof-irrelevant. Three of its four conjuncts are atoms that must
be extracted from three distinct global conjunction hypotheses, and the fourth is
the scaffold's characteristic formula, which must be derived through the
gadget.

### 9.3 Every target size `8..37` has a legal construction

**Lemma T3.** For every `N in 8..37`, `S = N - 6 in 2..31`. Since
`0 <= S <= 33 = 3 * CHAIN_LEN_CAP`, the triple
`(min(S,11), min(max(S-11,0),11), max(S-22,0))` lies in `TRIPLES(S)`, so
`TRIPLES(S)` is nonempty and `TARGET_SIZE_UNREACHABLE` cannot fire.

**Theorem (exact-size completeness under the full guard conjunction).** Fix any
`N in 8..37`, any catalogue member `X in {A, B, C}`, any `k` in `X`'s eligible
range, any legal alphabet split, any sampled fields inside the section 6.3
ceilings, any `(L0,L1,L2) in TRIPLES(N-6)`, any distinct `T0,T1,T2` in
`A_chain`, any `dir` and any padding atoms. The resulting plan satisfies:

1. `inference_node_count = 6 + (N - 6) = N`, and `band_of_node_count(N)` equals
   the draw's target band because `N` was drawn inside it (T4, D1);
2. every formula it contains is at most `24` nodes (Lemma CB);
3. no prohibited beta-redex occurs (per-scaffold normality proofs plus 5.2);
4. every conclusion is the natural-deduction typing of its children
   (per-scaffold typing proofs plus 5.2);
5. the global hypothesis formulas are pairwise byte-distinct and each is
   referenced (A.4 and its restatements);
6. every local hypothesis is referenced inside its own scope;
7. `3 <= k <= 6`, `atoms` is ascending and duplicate-free,
   `occurring <= declared <= public_atom_names(plan)`;
8. `depth >= 3`, at least four families, branching by `AND_INTRO`;
9. the global context has an explicit satisfying valuation, contains no `FALSE`
   and contains nothing byte-equal to the goal.

Therefore every `N in 8..37` has at least one legal construction, for **every**
catalogue member independently, and the exact-size property is carried by
`AND_ELIM` chain expansion rather than by contradiction padding.

**Expansion invariance.** Increasing any `L_j` by one wraps `H_j` in one more
`AND` with an atom of `A_chain` and adds one `AND_ELIM_*` node. This preserves:
global satisfiability (`H_j` remains a positive `AND`-spine over `A_chain`
atoms, all true under `nu`); typing (5.2); the formula bound
(`1 + 2 L_j <= 23`); normality (the new node's source is the old chain top or
the leaf `ASSUME`, never `AND_INTRO`); the no-goal-as-hypothesis invariant
(A.8 argues from the kind of `H_j`'s `dir`-opposite child, which remains an
`ATOM`); atom coverage (unchanged, since coverage is carried by the gadget
fields); and global uniqueness (A.4 argues from size and the `dir`-spine
projection, both of which remain valid). The conjunction therefore holds for
every reachable `S`, and no structural blocker arises.

### 9.4 Every S4 draw is structurally diverse

**Lemma S4.** For `N in 26..37`, `S >= 20`. Since `CHAIN_LEN_CAP = 11 < 20`, at
least two chains have `L_j >= 1`, and `max_j L_j >= ceil(20/3) = 7`. Hence
`max_j L_j >= 7`. Section 8.2 gives `dR` only the arguments `g_d` and
`c(L2)`, so `max_j L_j - 1` may not be substituted into `dR`; the bound is
obtained by a case split instead.

- If `L2 >= 7`, then `c(L2) = L2 - 1 >= 6`, so `dR >= 1 + (L2 - 1) >= 7`.
- Otherwise `L2 < 7`, so `max_j L_j >= 7` forces `max(L0, L1) >= 7`. That value
  is at least `1`, so `dL` takes its second branch and
  `dL >= 1 + (max(L0, L1) - 1) >= 7`.

In either case `max(dL, dR) >= 7`, and the outer `AND_INTRO` root gives
`depth = 1 + max(dL, dR) >= 8 >= 5`. Every scaffold contributes at
least four distinct globals (`A`: 4, `B`: 5, `C`: 4) and at least four families,
and every scaffold contains at least one scope-introducing node (`OR_ELIM` in A
and B, `NOT_INTRO` in C). Therefore the `structurally_diverse_S4` predicate of
section 10.7 is satisfied by every **successfully constructed and
checker-accepted** S4 row, so charter section 7's pre-root-minting requirement
cannot be blocked *by the diversity predicate itself* once such a row exists in
the scan.

This is conditional and is not a guarantee about the scan. The fixed
`5 x 256` scan is not formally guaranteed to contain any S4 success, or every
`(scaffold, dir)` pair: a bounded `PRF_REJECTION_BUDGET_EXCEEDED` remains
theoretically reachable (section 2.5), and no coverage of the finite scan has
been observed, because no scan has been run and none is authorized. Absence of
required scan coverage remains the section 10.7 blocker and is not repaired by
Lemma S4. See section 10.7.1.

### 9.5 What this proof does not establish

It does not establish that the plans are scientifically interesting, that any
band's quota can be filled, that L1 will accept every construction, that L4 can
compile any of them, that the family distribution is broad, or that the
population is free of a shared structural signature. It establishes exactly:
totality as success-or-failure, exact-size completeness, and the three
non-vacuity properties of section 9.2. Those are construction properties. The
L1 checker remains the sole acceptance authority; the code gate asserts
acceptance rather than assuming it. Section 12 records the declared narrowing.

## 10. Items 9 and 10 - the fixed-fixture code gate

No root key is minted or consumed at L2. The keys below are **public test
vectors**: fixed literal byte patterns, chosen so that no computation is needed
to write them down, permanently excluded from every dev, audit, cost, selector,
pilot and scientific scope, and never usable as a dev root.

```text
FIXTURE_KEY_0 = bytes.fromhex('00' * 32)
FIXTURE_KEY_1 = bytes.fromhex('ff' * 32)
FIXTURE_KEY_2 = bytes.fromhex('55' * 32)
FIXTURE_KEY_3 = bytes.fromhex('aa' * 32)
FIXTURE_KEY_4 = bytes.fromhex('000102030405060708090a0b0c0d0e0f'
                              '101112131415161718191a1b1c1d1e1f')
```

The gate must assert that these five constants are the only keys appearing in
the L2 module and its test, and that neither file contains any key-derivation,
`secrets`, `os.urandom` or root-registration code.

### 10.0 Gate chronology (replaces the circular v1 order)

The v1 requirement to freeze generated literals inside the accepted annex is
withdrawn as circular: the rows require `generate_draw`, which does not exist
until implementation is authorized. The order is:

1. This v2 annex freezes the algorithm, the byte schedule, the five public
   fixture keys, the scan range, the coverage predicate and the deterministic
   selection rule - and **no output literal whatsoever**.
2. The author ratification token of section 0.3 is recorded, which fixes the
   catalogue and acknowledges the section 10.7.1 gate replacement but authorizes
   nothing further; this annex is then submitted for joint independent X/Y
   review. Recorded X/Y acceptance of this annex authorizes exactly the two L2
   files of section 1 and nothing else.
3. Builder implements those two files. Only then may the frozen scan of section
   10.7 run, exactly once, on the five public vectors.
4. The selected literal rows and exclusion ledger V3 become **code-gate
   artifacts**, produced at the gate and reviewed as such.
5. Driver review and an independent code review accept or reject L2, on excluded
   fixtures only.

No dev root is minted or consumed before accepted L2, L3 and L4.

### 10.1 Determinism across fresh processes

For every selected fixture `(key, draw_index)`: two fresh interpreters, launched
with different `PYTHONHASHSEED` values, must emit byte-identical
`canonical_bytes(result)`, or the identical failure record. The gate compares
SHA-256 of those bytes against the literals frozen at step 4 above.

### 10.2 Exact byte-consumption records

Each selected fixture row records a literal `words_consumed`, frozen at step 4.
The gate asserts equality. Any decision-order drift, skipped singleton call or
extra draw changes at least one row. The gate additionally asserts, for every
success row, that `words_consumed` equals the closed form
`10 + W(n1,m1) + W(n2,m2) + S` of section 7.1 plus the recorded rejection count,
so a row and the schedule are cross-checked against each other rather than
against a single recorded number.

### 10.3 Conservation over a fixed draw range

For `FIXTURE_KEY_4` and `draw_index` in `0..63`:

- every index yields exactly one outcome, success or a named failure - no index
  missing, none represented twice;
- every success has `expectation['node_count'] == target_node_count`;
- every success has `expectation['band'] == target_band` and
  `target_band == ('S1','S2','S3','S4')[draw_index % 4]`;
- the multiset of bands over `0..63` is exactly 16 of each;
- `check_plan(result['plan'], result['expectation'])['ok']` is `True` for every
  success;
- for every success, the independent non-vacuity traversal of section 10.4
  passes.

### 10.4 Independent non-vacuity recomputation

For every success in every gate fixture and over the whole `0..63` conservation
range, the **test module** independently recomputes, without using the
generator's declared valuation and without importing any generator helper:

- **exhaustive satisfiability.** Enumerate all `2**k <= 64` valuations of the
  declared atoms; evaluate every global hypothesis formula by a direct
  structural recursion written in the test module; assert that at least one
  valuation makes all of them true.
- `no global hypothesis has kind 'FALSE'`;
- `canonical_bytes(hyp['formula']) != canonical_bytes(plan['goal'])` for every
  global hypothesis;
- the root proof node's kind is `AND_INTRO` (no root-level `EXFALSO`);
- every `EXFALSO` and `NOT_ELIM` node in the plan lies inside the lexical scope
  of at least one local assumption.

This traversal is the independent recomputation the disposition requires. It is
deliberately exponential in `k` and trivially small, so it shares no code path
and no reasoning with the production guard of section 8.3.

### 10.5 Mutation tests

Each mutation must change at least one frozen fixture output or fail an explicit
assertion. Mutations are applied to copies in the test, never to the production
module.

```text
PRF domain string changed ('...v2', trailing byte dropped)
NUL separator removed
HMAC key = root_id hex instead of raw 32 bytes
draw_index and block_index order swapped
draw_index little-endian; block_index little-endian
draw/block index encoded in 4 bytes instead of 8
block concatenation descending instead of ascending
word stride 4 bytes instead of 8 (overlapping words)
word taken little-endian
rejection threshold replaced by plain modulo
rejected word reused instead of consumed
singleton decisions skipped instead of drawing a word
D1 moved after D2 (decision-order drift)
D6 and D7 swapped (free-field order per scaffold)
D8/D9/D10 permuted
D13 padding order reversed (outermost wrapper first)
scaffold catalogue order permuted
chain direction forced per chain instead of per plan
CHAIN_LEN_CAP raised to 12
sampler admits NOT or FALSE (breaks Lemma POS)
```

The last two are the non-vacuity mutations and must be caught by explicit
assertions, not only by a changed hash: `CHAIN_LEN_CAP = 12` must fail the
24-node bound assertion for a maximal chain, and admitting `NOT`/`FALSE` into
`sample_positive` must fail the exhaustive satisfiability assertion of section
10.4 on at least one constructed input. `chain direction forced per chain` must
fail the duplicate-global assertion on a constructed collision
(`L_i = L_j = 1`, `T_i = Z_j`, `Z_i = T_j`), which is the exact reason section
5.2 fixes `dir` per plan.

The threshold and reuse mutations cannot be observed through a fixture, because
for `n <= 126` a rejection is astronomically unlikely. They are therefore
tested against the **pure core** `_randbelow_from_words(words, n)`, driven by
literal word lists containing `limit - 1`, `limit`, `2**64 - 1` and a following
usable word, asserting: the boundary word is rejected, it is consumed, the next
word is used, and the returned value equals `word % n` for the accepted word.
`randbelow(cursor, n)` is that core over the cursor's word source, so the seam is
a refactoring boundary, not a second implementation.

Singleton consumption is additionally tested directly: `randbelow(cursor, 1)`
returns `0` and advances `word_index` by exactly one.

### 10.6 Subcause injection

Each member of `L2_CONSTRUCTION_SUBCAUSES` is exercised by direct injection at
the internal function boundary - `randbelow` with `n = 0` and `n = 2**64 + 1`;
a rejection budget of `0`; a triple enumeration handed an out-of-range `S`; a
ceiling function handed a negative range; a cover handed an atom outside the
alphabet; a global hypothesis list perturbed to include `FALSE` or a copy of the
goal; a decision counter pre-loaded past its bound; a formula recursion counter
pre-loaded past its bound; an accumulator perturbed against `summarize_plan`;
a node count perturbed against `target_node_count`. The gate asserts the
returned record matches `L2_FAILURE_KEYS` exactly with
`cause == 'PLAN_CONSTRUCTION_FAILED'`. The gate must state in the same test that
no draw index is known to reach any subcause, that section 9 proves nine of the
ten cannot fire, and that `PRF_REJECTION_BUDGET_EXCEEDED` carries no
unreachability proof.

### 10.7 Feasibility coverage without real execution

The gate must contain checker-accepted fixed outputs covering:

- every band `S1, S2, S3, S4`;
- every rule kind: `ASSUME`, `AND_INTRO`, `AND_ELIM_LEFT`, `AND_ELIM_RIGHT`,
  `OR_INTRO_LEFT`, `OR_INTRO_RIGHT`, `OR_ELIM`, `NOT_INTRO`, `NOT_ELIM`,
  `EXFALSO`;
- all seven families;
- every catalogue member;
- both values of `dir`;
- at least one **structurally diverse S4** plan.

`structurally_diverse_S4` is the exact conjunction: `band == 'S4'`; at least four
of the seven families; `max_dependency_depth >= 5`; at least four distinct global
hypotheses; at least one node of kind `OR_ELIM` or `NOT_INTRO`; at least two
maximal `AND_ELIM_*` chains of length `>= 1`; and the longest chain of
parent-to-child `EXFALSO` nodes is at most `1`. This predicate **replaces** the
predicate of the unaccepted v1 annex; the replacement is recorded and justified
in section 10.7.1 and is not a preserved definition. Lemma S4 proves every
checker-accepted S4 row satisfies it, so the predicate itself cannot become a
blocker; the absence of an S4 row, or of any other required coverage element, in
the fixed scan still can and must be reported as one.

### 10.7.1 Replacement index for `structurally_diverse_S4` - LOUD DISCLOSURE

This gate was **redefined**, not preserved. It is the concrete discharge of the
L1 review's m9 concern and of the charter section 7 pre-root-minting obligation,
so its redefinition is recorded here in full rather than left to a diff.

**The unaccepted v1 predicate.** `PHASE2_STAGE_B_L2_GENERATOR_ANNEX_V1_DRAFT.md`
section 10.7 (SHA-256 `14ee7a8209b462e3437485e2a016686114ee42290901eea1bdb23bc5e0036e3b`,
never accepted) defined `structurally diverse S4` as the exact conjunction:

```text
band == 'S4'
at least five of the seven families
the longest chain of parent-to-child EXFALSO nodes is at most 4
at least two nodes that introduce a lexical scope (OR_ELIM or NOT_INTRO)
    beyond the mandate gadget's own OR_ELIM
max_dependency_depth >= 5
at least three distinct global hypotheses
```

**Why two of those dimensions are unsatisfiable under this architecture.** They
were written against v1's mandate architecture, in which a plan could contain an
arbitrary number of scope-introducing nodes because `OR_ELIM` and `NOT_INTRO`
were freely selectable productions of a recursive synthesizer, and in which the
threat model was a long `EXFALSO` chain hanging off one mandatory gadget.

The population of this annex is a single fixed frame plus exactly one gadget:

- **"at least two scope-introducing nodes beyond the gadget's own" is
  unsatisfiable for every plan.** Every plan contains exactly one
  scope-introducing node in total - the `OR_ELIM` of scaffold A or B, or the
  `NOT_INTRO` of scaffold C. The rest of a plan is three `AND_INTRO` nodes and
  three `AND_ELIM_*` chains, none of which introduces a binder. The count
  "beyond the gadget's own" is therefore identically zero. No draw of any
  catalogue member could ever satisfy it.
- **"at least five of the seven families" is unsatisfiable for two of the three
  catalogue members.** Scaffold A yields exactly four families
  (`AND_INTRO`, `AND_ELIM`, `OR_INTRO`, `OR_ELIM`) and scaffold C exactly four
  (`AND_INTRO`, `AND_ELIM`, `NOT_INTRO`, `NOT_ELIM`). Only scaffold B reaches
  five. Retaining the threshold would silently confine the mandatory S4 witness
  to one third of the population for no stated reason.

Retaining the v1 predicate verbatim would therefore have made the charter
section 7 obligation permanently undischargeable. The predicate could not be
preserved; it had to be replaced.

**The frozen replacement.** As stated in section 10.7:

```text
band == 'S4'
at least four of the seven families
max_dependency_depth >= 5
at least four distinct global hypotheses
at least one node of kind OR_ELIM or NOT_INTRO
at least two maximal AND_ELIM_* chains of length >= 1
the longest chain of parent-to-child EXFALSO nodes is at most 1
```

**Clause-by-clause index.**

| dimension | v1 (unaccepted) | frozen replacement | direction |
|---|---|---|---|
| band | `S4` | `S4` | unchanged |
| families | `>= 5` | `>= 4` | **lowered** (forced: A and C top out at 4) |
| scope-introducing nodes | `>= 2` beyond the gadget | `>= 1` in total | **lowered** (forced: plans have exactly 1) |
| `max_dependency_depth` | `>= 5` | `>= 5` | unchanged |
| distinct global hypotheses | `>= 3` | `>= 4` | **raised** |
| `EXFALSO` chain length | `<= 4` | `<= 1` | **tightened** |
| elimination chains | not required | `>= 2` maximal `AND_ELIM_*` chains of length `>= 1` | **added** |
| global-context satisfiability | not required, and provably false for v1 | required by NV1-NV3 for every success, independently recomputed by section 10.4 | **added** |

Two dimensions are numerically lower and are architecture-forced; three are
strictly stronger and one is new. In particular the v1 threshold that actually
carried m9 - "do not let a long `EXFALSO` chain masquerade as a diverse plan" -
is tightened from `<= 4` to `<= 1`, and the contradiction padding it was written
against no longer exists at all: node count here is carried by typed
`AND_ELIM` elimination chains from satisfiable positive hypotheses, not by
`EXFALSO`.

**Proof that every successful S4 A/B/C construction passes.** Let a draw of any
catalogue member succeed with `N in 26..37`, so `S = N - 6 >= 20`.

1. `band == 'S4'` by `band_of_node_count(N)` and Lemma T4.
2. Since `CHAIN_LEN_CAP = 11 < 20`, no single chain can absorb `S`, so at least
   two of `L0, L1, L2` are `>= 1`: the two-chain clause holds. It also forces
   `max_j Lj >= ceil(20/3) = 7`.
3. Depth: recall section 8.2, in which `c(L) = L - 1`,

   ```text
   dL = 0                                        if L0 == 0 and L1 == 0
      = 1 + max{ c(Lj) : j in {0,1}, Lj >= 1 }   otherwise
   dR = 1 + max({ g_d } union { c(L2) : L2 >= 1 })
   depth = 1 + max(dL, dR)
   ```

   `dR` sees only `g_d` and `c(L2)`; it does not see `L0` or `L1`, so
   `max_j Lj - 1` may not be substituted into `dR`. Step 2 gives
   `max_j Lj >= 7`. Two cases:

   - if `L2 >= 7`, then `c(L2) = L2 - 1 >= 6`, so section 8.2 gives
     `dR >= 1 + c(L2) >= 1 + 6 = 7`;
   - otherwise `L2 < 7`, so `max_j Lj >= 7` forces `max(L0, L1) >= 7`. That
     value is at least `1`, so `dL` takes its second branch and
     `dL >= 1 + (max(L0, L1) - 1) >= 1 + 6 = 7`.

   In either case `max(dL, dR) >= 7`, and the outer `AND_INTRO` root gives

   ```text
   depth = 1 + max(dL, dR) >= 8 >= 5
   ```

   so the `max_dependency_depth >= 5` clause of the predicate holds with
   margin.
4. Families: scaffold A gives `{AND_INTRO, OR_INTRO, OR_ELIM, AND_ELIM}`,
   scaffold B `{AND_INTRO, OR_ELIM, NOT_ELIM, EXFALSO, AND_ELIM}`, scaffold C
   `{AND_INTRO, AND_ELIM, NOT_INTRO, NOT_ELIM}`; `AND_ELIM` is present because
   `S >= 20 >= 1`. Each is at least four.
5. Distinct globals: A has `OR(P,Q), H_0, H_1, H_2` = 4; B has
   `OR(R,QB), NOT(R), H_0, H_1, H_2` = 5; C has `NOT(R), H_0, H_1, H_2` = 4.
   All are pairwise byte-distinct by A.4, so each is at least four.
6. Scope-introducing node: `OR_ELIM` in A and B, `NOT_INTRO` in C.
7. `EXFALSO` chain: `EXFALSO` occurs only in scaffold B and only once per plan,
   so the longest parent-to-child `EXFALSO` chain is `1` in B and `0` in A and C,
   both `<= 1`.

**What this does not guarantee.** The proof is conditional on a successful,
checker-accepted S4 construction existing in the fixed scan. It does not
guarantee that the frozen `5 x 256` scan contains an S4 success, every catalogue
member, both `dir` values, every rule kind or every family. No scan has been run
and none is authorized before section 10.0 step 3. If the frozen scan budget does
not cover every required element, the correct response is a reported gate blocker
and a revised annex - never a widened scan, a weakened predicate or a tuned
distribution. That blocker remains live and is not discharged by this section.

**Fixture selection procedure** (runs only at gate time, per section 10.0 step 3;
it runs no Peano, no search, no training and mints nothing):

```text
for key in (FIXTURE_KEY_0 .. FIXTURE_KEY_4):          # fixed order
    for draw_index in 0 .. 255:                        # ascending
        r = generate_draw(key, draw_index)
        record (key, draw_index, r) if r['ok'] and
               check_plan(r['plan'], r['expectation'])['ok']
COVER = the four bands, the ten rule kinds, the seven families,
        the catalogue members, and the two dir values
select rows in scan order; a row is selected iff it covers at least one
        element of COVER not covered by an already selected row;
        stop as soon as every element of COVER is covered
then append the first row in scan order satisfying structurally_diverse_S4,
        if it is not already selected
```

The scan budget is exactly five keys times 256 indices. If that budget does not
cover every rule kind, every family, every catalogue member, both directions and
the diverse-S4 predicate, the correct response is a reported blocker and a
revised annex, never a silently widened scan, a weakened predicate or a tuned
distribution.

**Freeze obligation.** The resulting literal `(key_hex, draw_index)` pairs,
together with each row's `words_consumed`, `node_count`, `band`, `families`,
`max_dependency_depth`, scaffold, `dir` and `canonical_bytes` SHA-256, are frozen
as literals in the **code-gate artifact** produced at section 10.0 step 4. They
are deliberately absent from this annex and from the accepted annex.

### 10.8 Exclusion ledger V3

Produced as a code-gate artifact at section 10.0 step 4, before L2 acceptance:

- retain every V2 row unchanged, including the five valid-plan exclusions, the
  two renderer-only rows and the seventeen enumerability rows with both the
  raw-ASCII and canonical-JSON-string sequent hashes;
- append, for every selected L2 fixture: `raw_plan_sha256` =
  `canonical_hash(plan)` and `raw_theorem_sha256` = `canonical_hash` of the
  checker-rederived theorem object returned by `check_plan`;
- keep fixture names unique and cover every selected row exactly once;
- record the same `sequent_hash_kinds` convention V2 established, so an L3
  implementer re-deriving an exclusion from an ASCII string cannot conclude it is
  missing - the m6 recording obligation carried forward;
- state that the five fixture keys are permanently barred from dev, audit, cost,
  selector, pilot and scientific scopes.

Skeleton identities are not computed at L2. L3 computes and registers theorem and
skeleton identities for every V3 row before any root key can be minted or
consumed, retaining the `premise_witness_or_e` / `renderer_or_commute` provenance
aliases for the one byte-identical theorem.

## 11. Item 12 - staged implementation and review

### 11.1 Authorized files

Exactly `learning/phase2_stageb_generator.py` and
`learning/test_phase2_stageb_generator.py`, both new. No Stage-A file, no L0
file, no L1 file, no theory byte and no other test may change. In particular
`phase2_stageb_schema.py` remains the sole home of `MAX_FORMULA_NODES`,
`DEV_QUERY_MEASUREMENT_N_POSITIONS`, band edges and the seven-family order; all
new L2 constants live in the L2 module.

One production module and one test module. No framework, no registry, no plugin
table, no configuration file, no class hierarchy. The scaffold catalogue is a
literal frozen tuple of module-level functions.

### 11.2 Test commands

```bash
python3 -m unittest discover -s learning -t learning -p 'test_phase2_stageb*.py' -v
```

and the same Stage-A command used for the accepted L0/L1 gate. Expected
**categories**, not invented counts:

- the accepted Stage-B baseline of 36 tests must still pass unchanged;
- Stage-A must be unchanged;
- the new L2 categories are: PRF vector and mutation tests; singleton and
  rejection-core tests; determinism across fresh processes; byte-consumption
  records and their closed-form cross-check; conservation over `0..63`;
  first-word binding; per-band checker-accepted fixtures; rule-kind, family,
  scaffold and direction coverage; the diverse-S4 fixture; the independent
  exhaustive non-vacuity recomputation; aliasing and canonical-byte invariants;
  recursion and work bounds; size conservation and expectation agreement;
  subcause injection; import-graph boundary; fixture-key discipline.

The new total is whatever is measured after implementation. Any number stated
before the run is an invention and must not appear in the annex or the gate
report.

### 11.3 Patch export routes

- new delta over the accepted L0/L1 cumulative:
  `minimo_phase2_stageb_l2_v2_delta.patch`;
- new cumulative over the pinned MINIMO base:
  `minimo_phase2_stagea_stageb_l01_l2_v2_cumulative.patch`.

Both must `git apply --check` clean on `6066f482c6752915ad21119f93dc162f4cb9db72`
in the documented order, both must be `git diff --check` clean, and both routes
must yield byte-identical trees. Both SHA-256 values, plus the V3 ledger
SHA-256, are recorded in the L2 closure. The pinned patch files are the evidence
of record; a mutable disposable tree is not evidence where it differs from them.
The delta must name exactly the two authorized paths, both as new files.

### 11.4 Mandatory stop

After implementation and the code gate, work stops for driver review and an
independent code review, on excluded fixtures only. No commit and no push to
MINIMO or Philosophia. The eight dev root keys are minted only after accepted
L2, L3 and L4 implementations execute the complete ordered pipeline of charter
section 8; L2 may not mint or consume them, and the five fixture keys are public
test vectors that can never become dev roots.

## 12. Handoff obligations

These are the only forward statements this annex makes; it restates no L3/L4
design and no audit contract.

1. **To L3.** L2 emits hypothesis IDs in a frozen per-scaffold mint order and
   local IDs in construction order, and performs no alpha, theorem or skeleton
   canonicalization. L3 owns charter sections 5.1-5.3 and 6, must import the
   complete V3 exclusion set, and must register theorem and skeleton identities
   for every L2 fixture before any root key is minted.
2. **To L4.** Lemma S4 guarantees that every checker-accepted S4 row satisfies
   the section 10.7 diverse-S4 predicate, which is a replacement predicate
   disclosed in section 10.7.1. Charter section 7's pre-root-minting requirement
   is therefore met with a genuinely diverse plan **provided the fixed scan
   yields an S4 row**; if it does not, that is the section 10.7 gate blocker and
   must be reported as such. The open `COMPILER_FAMILY_UNREACHABLE` risk recorded
   in the L0/L1 disposition (Opus M2) remains open and must be carried into the
   L4 annex: a green enumerability table is not evidence of family
   compilability. Note specifically that scaffold C emits no `OR_*` node and
   scaffold A emits no `NOT_*` or `EXFALSO` node, so per-family compilability
   must be demonstrated across scaffolds, not on one fixture.
3. **Declared structural narrowing.** Every plan in this population has the same
   frame: an `AND_INTRO` root over a four-leaf conjunction, three `AND_ELIM_*`
   chains from three distinct positive conjunction hypotheses, and one of the
   catalogue's gadgets. Node count is carried almost entirely by chain length.
   This is a **known, disclosed narrowing** of the dev family, adopted because it
   is what makes exact-size totality compatible with non-vacuity, and it must be
   disclosed wherever dev evidence is later used, labelled `dev-fit`. It is a
   different narrowing from v1's, not the absence of one.
4. **No claims from fixtures.** Nothing in the L2 gate may be reported as
   generator yield, band reachability, quota fill, interface survival,
   scientific suitability, or ACTIVE/YOKED evidence. The fixtures demonstrate
   construction feasibility, L1 acceptance and global-context satisfiability of
   specific excluded outputs, and nothing else. The exhibited satisfying Boolean
   valuation is a sufficient certificate that the global context cannot
   intuitionistically derive `FALSE`, and an imposed population guard; it is not
   evidence of difficulty, minimality or substantive proof relevance, and it says
   nothing about proof difficulty. Shortcut and minimality risk remain owned by
   the later alternative-proof audit.

## 13. Negative authorization

This unaccepted draft authorizes nothing. It does not authorize L2 code, a dev
root key, a generated plan, a fixture scan, a cost or audit root, L3/L4 work,
Peano or MCTS execution, proof search, calibration, G4ip, inverse, statement or
selector fitting, learner training, a SELF/YOKED branch, a scientific outcome, a
commit or a push. No author choice remains open and no alternative catalogue
exists. The ratification token recorded in section 0.3 authorizes only
preparation of this annex and its independent X/Y review; it authorizes no code,
no output literal, no scan, no root and no execution. Joint independent X/Y
acceptance of this annex must be obtained before any L2 implementation may
begin. Fixture literals and exclusion ledger V3 are code-gate artifacts produced
after that authorization, never prerequisites to it.
