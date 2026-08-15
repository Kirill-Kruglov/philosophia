# PHILOSOPHIA STAGE-R L4 MINIMUM COMPILE-AND-REPLAY EXECUTABLE ANNEX V1.1

Status: `PAPER_NOT_FREEZABLE_STRUCTURAL_BLOCKER`

Date: 2026-08-15

Intended durable path:
`successor/stage_r/l4/STAGE_R_L4_MINIMUM_COMPILE_REPLAY_EXECUTABLE_ANNEX_V1_1.md`

This document is standalone and supersedes `…_V1_DRAFT.md` in full. Every defective V1 algorithmic clause is **replaced**, not annotated. It authorizes nothing, and its terminal verdict is a bounded structural blocker established in §11 from durable pinned sources.

---

## 0. Authority, pins and provenance

Every hash below was recomputed from durable files at the start of this repair pass and matched.

| object                                                                             | SHA-256                                                                                                |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Stage-R contract `successor/stage_r/PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1.md` | `1c3cec3aa6bd7094e2d37b062a8f349df5b226e91bbdc4a7b21e80fb785172f3`                                     |
| L4 activation `successor/stage_r/STAGE_R_L4_MINIMUM_BOUNDARY_ACTIVATION_V1.md`     | `8cfb71f75f7ad1346eb43babf0f233169a68549a7dbb4eee2f0935dcf539f982`                                     |
| V1 draft (superseded)                                                              | `ee48524f1c1ad2b91e218006e8c1784d3a1f425d1cf787ca7a39133ba437ce4e`                                     |
| driver paper audit                                                                 | `d651e41985d4153e03206b78dda8395f75c7de2a8ad1a501da57101988334c70`                                     |
| Stage-B charter v1.1.1                                                             | `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311`                                     |
| accepted L2 annex                                                                  | `3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8`                                     |
| accepted L2 code-gate JSON                                                         | `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0`                                     |
| accepted V3 raw exclusion ledger                                                   | `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d`                                     |
| accepted cumulative patch through L2 V5                                            | `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683`                                     |
| accepted L3 executable annex                                                       | `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0`                                     |
| accepted L3 closure                                                                | `5fcf97a053a2d8b57eb0db86b17ec076e62f6f3d63f0b13bef16f8edb89d8fbb`                                     |
| accepted L3 production / test / exclusion artifact                                 | `ee1be7af…7860` / `2d71a629…d45e` / `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` |
| accepted cumulative patch through L3                                               | `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c`                                     |
| accepted theory (durable copy `recovery/archive/accepted_l01/learning/theories/…`) | `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507`                                     |
| MINIMO base commit                                                                 | `6066f482c6752915ad21119f93dc162f4cb9db72`                                                             |
| L4 activation commit                                                               | `6f24e6b6e0162019f9b078e16224eb4cb47d70b5`                                                             |

V1's accepted scope reconciliation (V1 §§5.1–5.4, accepted by the driver) is carried unchanged into §9 below, and every frozen authority hash is preserved.

### 0.1 Provenance disclosure (audit m1)

**The V1 paper-author pass created a disposable MINIMO reconstruction, which its own task prohibited.** That deviation occurred. It produced no scientific data, no root, no key, no fixture regeneration and no durable `/tmp` artifact, and the driver independently re-verified the cited facts, but the annex does not claim full procedural compliance for that pass.

Every source claim in this V1.1 is grounded **only** in:

- durable Philosophia files under `successor/recovery/phase2_stage_b_20260815/` and `successor/stage_r/`;
- read-only `git -C <minimo> show 6066f482…:<path>` against the pinned MINIMO base;
- read-only `sha256sum`.

No worktree was created, no `/tmp` path was used as an output location, no repository was edited, no test or fixture was run, no row was regenerated and no Peano call was made in this pass.

---

## 1. Boundary

### 1.1 Executed clause

Only Stage-R contract §4.1 item 3: minimum semantic L4 compile plus fresh empty-goal replay, sufficient for reservoir membership and solvability witness.

### 1.2 Two-file MINIMO scope

Exactly:

```text
learning/phase2_stageb_compile.py
learning/test_phase2_stageb_compile.py
```

No accepted existing file changes. The acceptance JSON of §8 is a durable Philosophia-side Builder deliverable, never a third MINIMO patch path.

### 1.3 Closed import allowlist (audit M3)

Production imports **exactly**, with no alternative offered:

```text
__future__, typing, itertools, hashlib, peano,
phase2_actions            (canonicalize_action_object_pairs only)
phase2_stageb_canonical   (canonical_bytes, canonical_dumps, canonical_hash)
phase2_stageb_checker     (check_plan)
phase2_stageb_identity    (canonical_theorem, identify, rederive_theorem)
phase2_stageb_render      (render_formula)
phase2_stageb_schema      (constants, predicates, THEORY_* pins)
```

- `itertools` is permitted and required for `permutations` (§3).
- `hashlib` is permitted **solely** for `hashlib.sha256(theory_text.encode('utf-8')).hexdigest()` compared against `THEORY_SHA256`. `canonical_hash` is not a raw-byte theory hash and is not used for that purpose.
- `phase2_actions` is the accepted Stage-A containment path. Only `canonicalize_action_object_pairs` is imported. Its transitive imports are `phase2_codec` and `phase2_timeout`; **no** `QueryCodec`, query, learner, MCTS, policy, value or `TreeSearchNode` object is ever instantiated, and no codec function is ever called. `canonicalize_action_object_pairs` is used for exactly two purposes: (i) containment and duplicate-display refusal (`DuplicateActionSerialization`), (ii) producing a stable materialized list. **Its sort order never selects the semantic action** — selection is by §4's descriptor over the whole materialized list, and §10 item 10 proves order-independence by permuting the list.

Forbidden in production: the generator, `bootstrap`, `proofsearch`, `policy`, `phase2_search`, `phase2_isolated`, `phase2_root`, `phase2_spec`, Torch, `json`, `random`, `secrets`, `os`, `subprocess`, `pathlib`, `time`, and any filesystem or process API. There is no mutable module state.

### 1.4 Input binding without circular trust

Public signature, exactly three arguments, no injection keyword, no caller-supplied identity:

```python
def compile_and_replay(plan: Mapping, expectation: Mapping, theory_text: str) -> dict
```

Binding order inside production:

1. `hashlib.sha256(theory_text.encode('utf-8')).hexdigest() != THEORY_SHA256` → `ValueError` (API contract).
2. `checked = check_plan(plan, expectation)`; not `ok` → failure record `cause='L4_INPUT_NOT_L1_ACCEPTED'`, `subcause=checked['cause']`.
3. `identified = identify(plan, checked['theorem'])`; not `ok` → failure record `cause=identified['cause']`, `subcause=identified['subcause']`.
4. L4 recomputes the alpha lift (§3) and asserts its induced canonical theorem is byte-identical to `identified['canonical_theorem']`; otherwise `L4InvariantError('CANONICAL_THEOREM_DISAGREEMENT')`.
5. The Peano goal is `identified['public_item']['goal']` and nothing else.

### 1.5 Production domain versus gate population (audit M5)

Two distinct statements, both operative:

- **Production interface domain.** `compile_and_replay` accepts **any** bounded L1-accepted Stage-B plan (3–6 declared atoms, formula bound 24, 8–37 non-`ASSUME` nodes) and returns either a success record or one closed compile/replay refusal from §7.2. It contains no fixture-hash check, makes **no** universal success or catalogue-completeness claim, and its fail-closed ceilings may refuse a supported-grammar plan without implying universal reachability.
- **Mandatory calibration population.** The acceptance artifact and the mandatory code gate cover **exactly the eleven permanent exclusions** — the five L1 hand fixtures and the six literal frozen L2 rows — and no other plan. No plan is generated, drawn, scanned or selected now.

This restores prospective reservoir admission without restoring the full compiler catalogue and without selecting a frame.

---

## 2. Pinned Peano facts

All verified by read-only `git show` at the pinned base, cited by symbol.

- **P1** `peano.PyProofState(theory: str, premises: list[str], goal: str)`; goal parse failure raises `ValueError`.
- **P2** `PyProofState.actions()` is deduplicated in Rust by `ProofAction` `Hash`/`PartialEq` before crossing the boundary.
- **P3** `execute_action` returns the successor frontier: `Intro` → 1 state (or `[]` if intro yields none); `Apply`/`Construct` → exactly 1 state; `SelectGoals(gs)` → **`len(gs)` states in `gs` order**; `SelectConstruction` → `[]` when the construction is equivalent to the active goal (goal closed), else 1 state.
- **P4** `PyProofAction` exposes `is_intro()`, `is_construct()`, `is_apply()`, `selected_construction() -> Optional[(dtype_str, value_str)]`, `__eq__`, `__str__`.
- **P5** `ProofAction` has exactly five variants: `Intro`, `Construct(String)`, `SelectConstruction(bool, Term, Term)`, `Apply(String)`, `SelectGoals(Vec<Term>)`.
- **P6** `ProofState::actions()` is a strict alternation on the last history action: after `Apply(_)` only `SelectGoals`; after `Construct(_)` only `SelectConstruction`; otherwise only `Intro?` plus per-premise `Construct`/`Apply` per annotation. The three groups are never co-enumerated.
- **P7** In the "otherwise" branch: a premise with a forward annotation yields `Construct(p)`; with a backward annotation yields `Apply(p)`; with **no** annotation yields **both**.
- **P8** `enumerate_apply_goals`: for an `Arrow` input that is a `Declaration{name, dtype}` unbound by the output unifier, it branches over `context.inhabitants(dtype)`; for a non-declaration input it computes the substituted goal, **prunes the whole branch if it still has free variables**, treats it as open iff `context.inhabitant(goal).is_none()`, prunes if open and `must_infer[i]`, and pushes it only if open. Pushed goals are in **input order**.
- **P9** `Context::inhabitants(ttype)` returns the **names** of context definitions whose `dtype` evaluates to `ttype`. For `ttype = prop` these are exactly the named prop objects: the declared atoms `a0..a{k-1}` and the theory's `false : prop.`.
- **P10** `Term` derives `PartialEq, Eq, Hash`; its `Display` is a faithful s-expression rendering.
- **P11** `ProofAction` `Display` is lossy and cross-variant colliding; it is **forbidden as an identity** here.
- **P12** `ProofAction` equality for `SelectConstruction` is proof-irrelevant: when the dtype is a prop, two actions with equal dtype are equal regardless of value, so P2 leaves exactly one representative per dtype.
- **P13** Theory annotations: `#backward` for `and_i, or_il, or_ir, or_e, not_i, exfalso`; `#forward` for `and_el, and_er`; **none** for `not_e`. `or_e`'s annotation is `#backward or_e infer infer infer infer subgoal subgoal.` `false : prop.` is declared.

---

## 3. Alpha-equivariant proof lift (audit M1)

V1's "first lexicographic theorem-minimiser" rule is **withdrawn**; it did not make the script invariant over the alpha orbit.

Let `k` be the declared atom count, `S` the ascending source atom list.

1. **Theorem minimum (unchanged, L3-owned).** `theta_min = min over p in permutations(range(k)) of canonical_bytes(T(p))`, where `T(p)` is the L3 candidate. `theta_min` equals `canonical_bytes(identified['canonical_theorem'])`. The L3 theorem identity, theorem name and public bytes are **exactly unchanged** by everything below.
2. **Minimising set.** `Pi = { p : canonical_bytes(T(p)) == theta_min }`, non-empty.
3. **Obligation-tree tie-break.** For each `p in Pi` build the obligation tree `O(p)` (§4.1) and take `omega_min = min over p in Pi of canonical_bytes(O(p))`.
4. **Final tie-break.** Among `p in Pi` with `canonical_bytes(O(p)) == omega_min`, take the lexicographically first `p` in `itertools.permutations(range(k))` order.

`ALPHA_LIFT_RULE = 'THEOREM_MIN_THEN_OBLIGATION_MIN_THEN_FIRST_LEXICOGRAPHIC'`.

**Invariance theorem.** Let `P` be an L1-accepted plan and `P'` differ only by a raw atom bijection `tau` and/or a global-hypothesis permutation with consistent global-ID rewriting. Then the *candidate byte sets* `{canonical_bytes(T(p))}` and `{canonical_bytes(O(p)) : p in Pi}` are equal for `P` and `P'`, hence `theta_min`, `omega_min` and the selected canonical obligation tree are equal.

*Proof.* Write `S` and `S' = tau(S)` for the ascending source lists. The map `p -> p ∘ pi_tau`, where `pi_tau` is the index permutation induced by `tau` on the ascending order, is a bijection of `permutations(range(k))` onto itself, and `T'(p ∘ pi_tau) = T(p)` because both substitute the same atom to the same target. Hence the candidate byte multiset is invariant and `theta_min` is invariant, so `Pi' = Pi ∘ pi_tau`. The obligation tree (§4.1) is built from **substituted formulas and rule kinds only** — it contains no global identifier, no hypothesis position and no local identifier — and substitution composes identically, so `O'(p ∘ pi_tau) = O(p)`. Therefore `{canonical_bytes(O(p)) : p in Pi}` is invariant and `omega_min` is invariant. A global-hypothesis permutation changes neither set, because the obligation tree's hypothesis content enters only through the canonically **sorted** hypothesis list and through per-node substituted formulas. The final lexicographic tie-break is applied to a set of permutations that induce **byte-identical** obligation trees, so the selected tree is identical even when the selected permutation differs. ∎

The residual freedom is therefore exactly zero at the level of the compiled object: any two survivors of step 4 give the same obligation tree, hence the same script and the same acceptance record.

**Bound test.** §10 item 6 must exercise an automorphic case: either a natural automorphism among the eleven (a plan whose theorem is fixed by a non-identity atom permutation) or, if none exists, an explicitly constructed L1-accepted automorphic plan used **only** as an in-gate construction, never added to the artifact population.

---

## 4. Obligation tree, per-rule transitions and the ordered frontier (audit C1)

V1 §§2.3, 3.4 and 3.4.2 are **withdrawn in full**. The generic rule "open goals = child conclusions excluding `ASSUME` children" is false for this theory and is replaced by the table in §4.3.

### 4.1 Obligation tree

`O = node(kind, conclusion, assumption?, children_in_declared_order)` where `conclusion` and `assumption` are substituted formulas rendered by the accepted `render_formula`, `kind` is one of the ten accepted ND kinds, and children are in the accepted L0 `PROOF_CHILD_FIELDS` order. The tree carries no identifier, index, band or plan byte. Its canonical bytes are `canonical_bytes` of the nested `{'kind','conclusion','assumption','children'}` mapping with `assumption` absent where the kind has none.

### 4.2 Two modes

- `PROVE_ACTIVE_GOAL(state, obligation)` — the obligation's conclusion is the active Peano goal.
- `MATERIALIZE_NEUTRAL_IN_CONTEXT(state, obligation)` — the obligation's conclusion must become an **inhabited context object** before a dependent step; it is never the active goal.

### 4.3 Neutral grammar

A **neutral** obligation is generated by

```text
Neutral ::= ASSUME | AND_ELIM_LEFT(Neutral) | AND_ELIM_RIGHT(Neutral)
```

Nothing else is neutral. Anything appearing in a neutral position outside this grammar is refused with `COMPILER_NO_MATCH / NEUTRAL_GRAMMAR_VIOLATED`.

*Justification from accepted L1 normality.* The accepted checker rejects the three immediate beta-redexes, in particular `AND_ELIM_*` whose `source` is `AND_INTRO`. Therefore an `AND_ELIM` chain's ultimate source is never an introduction; in the accepted L2 catalogue and the L1 hand fixtures it is an `ASSUME`. The grammar is the exact closure of that fact, and any other shape (for example an `AND_ELIM` over an `OR_ELIM`) is refused rather than compiled by guesswork.

### 4.4 Per-rule transition table

`G` denotes the active goal, `X`, `Y`, `R` substituted formulas, `[A -> B]` a Peano arrow type. "Expected effect" is the **ordered** tuple of `PyProofState.goal()` strings of the successor frontier.

| #   | mode / kind                                             | Peano step 1                                                       | Peano step 2         | expected ordered effect                                                           | frontier push (top first)                                                               |
| --- | ------------------------------------------------------- | ------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| R0  | root                                                    | `Intro` × `(k + m)`                                                | —                    | 1 state each                                                                      | replace                                                                                 |
| R1  | `PROVE`, `AND_INTRO`, `G = (and X Y)`                   | `Apply(and_i)`                                                     | `SelectGoals`        | open subsequence of `(X, Y)`                                                      | `PROVE(left)`, `PROVE(right)` restricted to open                                        |
| R2  | `PROVE`, `OR_INTRO_LEFT`, `G = (or X Y)`                | `Apply(or_il)`                                                     | `SelectGoals`        | open subsequence of `(X,)`                                                        | `PROVE(source)` if open                                                                 |
| R3  | `PROVE`, `OR_INTRO_RIGHT`, `G = (or X Y)`               | `Apply(or_ir)`                                                     | `SelectGoals`        | open subsequence of `(Y,)`                                                        | `PROVE(source)` if open                                                                 |
| R4  | `PROVE`, `NOT_INTRO`, `G = (not X)`, assumption `X`     | `Apply(not_i)`                                                     | `SelectGoals`        | **exactly** `([X -> false],)`, unconditionally                                    | `PROVE(body)` with a mandatory 1-step intro prelude                                     |
| R5  | `PROVE`, `EXFALSO`, `G` arbitrary                       | `Apply(exfalso)`                                                   | `SelectGoals`        | open subsequence of `(false,)`                                                    | `PROVE(source)` if open                                                                 |
| R6  | `PROVE`, `NOT_ELIM`, `G = false`                        | `Apply(not_e)`                                                     | `SelectGoals`        | open subsequence of `((not P), P)` where `P` is the `positive` child's conclusion | `PROVE(negative)`, `PROVE(positive)` restricted to open                                 |
| R7  | `PROVE`, `OR_ELIM`, `G = R`, major concludes `(or P Q)` | `MATERIALIZE(major)` **first**, then `Apply(or_e)`                 | `SelectGoals`        | **exactly** `([P -> R], [Q -> R])`, unconditionally                               | `PROVE(left_branch)`, `PROVE(right_branch)`, each with a mandatory 1-step intro prelude |
| R8  | `PROVE`, `AND_ELIM_LEFT`/`RIGHT`, `G = X`               | `MATERIALIZE(self)`                                                | —                    | goal closed by the construction                                                   | nothing                                                                                 |
| R9  | `MATERIALIZE`, `ASSUME`                                 | —                                                                  | —                    | —                                                                                 | nothing; require inhabited                                                              |
| R10 | `MATERIALIZE`, `AND_ELIM_LEFT`/`RIGHT`                  | `MATERIALIZE(source)` **first**, then `Construct(and_el`/`and_er)` | `SelectConstruction` | `[]` if it closes the active goal, else 1 state                                   | nothing                                                                                 |
| R11 | `PROVE`, `ASSUME`                                       | —                                                                  | —                    | —                                                                                 | nothing; require inhabited                                                              |

Rule-specific facts that the generic V1 rule got wrong, each now explicit:

- **R4.** `not_i`'s second input is the arrow `['P -> false]`. It is a fresh arrow type, never inhabited, so it is **always** open — independently of whether the ND body is an `ASSUME`. The body is then compiled after exactly one `Intro` that introduces the local hypothesis; Peano names it, ND `lN` never crosses.
- **R7.** `or_e`'s major input is `must_infer`, so it is **pruned when open**: the major must already be inhabited. Hence the mandatory `MATERIALIZE(major)` before `Apply(or_e)`. The two branch inputs are fresh arrows, always open, so the effect is exactly the two branch arrows, in that order, unconditionally. Each branch is compiled after exactly one `Intro`.
- **R8/R10.** A forward `AND_ELIM` must first materialize its **source neutral spine recursively**; V1 never visited the forward child and could only handle a one-step elimination.
- **R9/R11.** An `ASSUME` obligation compiles to zero primitives and is discharged by context inhabitation.

### 4.5 Open-subsequence law and silent-inhabitation refusal

For rules R1, R2, R3, R5, R6 the expected effect is an **ordered subsequence** of the rule's obligation tuple. Let `expected_full` be that tuple and `observed` the ordered effect of the unique `SelectGoals` candidate. Compute the unique order-preserving alignment of `observed` into `expected_full`; if none exists, refuse `COMPILER_NO_MATCH / EFFECT_NOT_A_SUBSEQUENCE`.

For every position of `expected_full` **absent** from `observed`:

- if the corresponding child's kind is `ASSUME` → correct discharge;
- if the corresponding child's kind is **not** `ASSUME` → refuse `COMPILER_NO_MATCH / NON_ASSUME_OBLIGATION_SILENTLY_INHABITED`.

For every position **present** whose child kind is `ASSUME` → refuse `COMPILER_NO_MATCH / ASSUME_NOT_INHABITED`.

A silently inhabited non-`ASSUME` subtree therefore **fails closed** and can never be counted as compiled rule coverage. Rule coverage is credited only from nodes that actually emitted their rule's primitive steps (R9/R11 credit `ASSUME` explicitly).

### 4.6 Repeated equal goals

By P3 the `SelectGoals` successor states are returned in the **goal-vector order**, and by P8 that vector is in arrow-input order. The alignment of §4.5 is therefore positional and exact, not a multiset guess, even when two goals are textually identical. If the alignment of §4.5 is not unique — the only way this can occur is a strict subsequence with repeated equal entries where two distinct alignments are order-preserving — refuse `COMPILER_AMBIGUOUS_MATCH / AMBIGUOUS_EFFECT_ALIGNMENT`. There is no positional guessing anywhere.

### 4.7 Ordered global frontier

A single explicit stack `F` of entries `(state, mode, obligation)`.

- Initialise: `F = [(root_state_after_prelude, PROVE, root_obligation)]`.
- Step: pop the **top** entry, execute its rule from §4.4, and push its generated entries **in reverse rule order** so that the first rule child is on top. Sibling entries below the popped one are never touched, reordered or discarded.
- Intro preludes are applied to the popped entry's state before its rule fires, and are bounded by §6.
- `MATERIALIZE` entries are executed to completion before the dependent `PROVE`/`Construct` step of the same rule; they push their own sub-entries by the same law.
- **Success requires both**: the script is exhausted **and** `F` is empty. "The last returned child list was empty" is **not** the success condition and is never used as one (audit C1.4, m2).

Replay uses the identical frontier law, driven by the stored script, and asserts at each step that the popped entry's expected arity equals the observed successor count.

### 4.8 Termination and exact counts

Define `mu(F) = sum over entries of (2·size(obligation subtree) + arrow_inputs(goal))`, where `size` counts all proof nodes including `ASSUME`.

Every rule strictly decreases `mu`: R1–R7 replace one entry by entries whose subtrees are proper sub-multisets of the parent's, and consume the parent node; R8/R10 consume the current node and materialize strictly smaller neutral sources; R9/R11 remove an entry without pushing; each `Intro` decreases `arrow_inputs` by exactly one. `mu` is a non-negative integer, so the traversal terminates. There is no `while` without this monovariant, no retry, no backtracking and no search.

Exact per-mode counts for a plan with `n_total` proof nodes (`n_assume` of them `ASSUME`, `n = n_total - n_assume` non-`ASSUME`), `k` atoms and `m` global hypotheses:

- `PROVE_ACTIVE_GOAL` entries: one per non-`ASSUME` node compiled in prove position, plus one per `ASSUME` discharged in prove position.
- `MATERIALIZE_NEUTRAL_IN_CONTEXT` entries: one per node of every neutral spine visited, i.e. one per `AND_ELIM` node in materialize position plus its terminal `ASSUME`, plus one per `OR_ELIM` major spine.
- `Intro` steps: `k + m` at the root, plus exactly `1` per `NOT_INTRO` and exactly `2` per `OR_ELIM`.
- Primitive steps per node: `2` for R1–R7 (`Apply` + `SelectGoals`), `2` for each R10 (`Construct` + `SelectConstruction`), `0` for R9/R11.

---

## 5. Semantic action identity (audit M2)

### 5.1 Descriptor

For an enumerated action `a` at state `s`:

```text
descriptor(a, s) = (kind, dtype, effect)
```

- `kind` from typed predicates only: `is_intro()` → `INTRO`; `is_construct()` → `CONSTRUCT`; `is_apply()` → `APPLY`; `selected_construction() is not None` → `SELECT_CONSTRUCTION`; residual → `SELECT_GOALS`. Exhaustive and disjoint by P4/P5.
- `dtype`: for `SELECT_CONSTRUCTION` only, `selected_construction()[0]`. **The proof-term value is omitted** from identity and from the script hash.
- `effect`: the ordered tuple of `child.goal()` strings from `s.clone().execute_action(a)`, plus its length.

**Nothing else may select or disambiguate.** `str(action)`, list position, premise name and object identity are excluded from matching, from ambiguity resolution and from the script hash. V1's `arrow` field, obtained by `str(a)` equality, is deleted.

*Why omitting the proof value is sound.* By P12 Rust equality for a prop-dtype `SelectConstruction` compares only the dtype, and by P2 the enumerated survivors therefore carry exactly one representative per dtype. The fragment is prop-only: every theory arrow's output is a proposition and every context object introduced by the canonical sequent is either a declared prop or a proof of a prop, so every `SelectConstruction` reachable here is prop-valued. Including the value would let an equally-valid representative move a supposedly semantic hash without moving any proof effect. Omitting it makes the hash a function of exactly what Peano treats as identical.

### 5.2 Selection

Matching uses `kind`, `dtype` where applicable, and `effect` only. Zero matches → `COMPILER_NO_MATCH`. **Two or more actions with the required effect → `COMPILER_AMBIGUOUS_MATCH`**, without exception and regardless of display agreement.

For `APPLY`/`CONSTRUCT` the required effect is the single successor state whose subsequent enumeration is the corresponding `SelectGoals`/`SelectConstruction` group (P6); the rule's arrow is identified **semantically** by that group's content per §4.4, never by the premise name.

### 5.3 Post-selection diagnostic only

After a unique semantic selection, the gate may assert that `str(a)` equals the closed expected display (`intro.`, `a <premise>`, `c <premise>`) as a **rule-coverage diagnostic**. This assertion may not disambiguate, may not be consulted during selection or rematching, and may not enter the script hash.

### 5.4 Containment

`enumerate_contained(state)` is `canonicalize_action_object_pairs(list(state.actions()))` from the accepted Stage-A module, used for containment and duplicate-display refusal only; the returned pairs are consumed as an unordered candidate pool, and the descriptor decides. `DuplicateActionSerialization` becomes `COMPILER_NO_MATCH / DUPLICATE_ACTION_DISPLAY`.

### 5.5 Candidate evaluation and exceptions (audit M6)

Evaluation executes on `s.clone()`; children are read for `goal()` only and discarded; nothing crosses into replay; `s` is asserted unchanged (`goal()`, `format_context()`, `names_in_context()`).

**Any exception during candidate effect evaluation — PyO3 panic or otherwise — fails the whole compilation immediately** with `COMPILER_NO_MATCH / CANDIDATE_EVALUATION_EXCEPTION`. A candidate is never silently excluded while another succeeds. V1's silent-exclusion clause is withdrawn.

### 5.6 Script and hash

Step record: `{'step', 'kind', 'dtype'|None, 'effect_goals', 'expected_arity'}`. `semantic_script_sha256 = canonical_hash(list_of_step_records)`. It depends on no display string, no enumeration order, no object address, no hash seed and no proof term.

---

## 6. Bounds and counters (audit M6)

Derived from §4.8, not from the eleven-row sample.

| constant                      | value  | derivation                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MAX_DECLARED_ATOMS`          | 6      | accepted L0 schema                                                                                                                                                                                                                                                                                                   |
| `MAX_GLOBAL_HYPOTHESES`       | 5      | accepted L2 grammar: scaffold A contributes `OR(P,Q)` plus three chain hypotheses `H_0,H_1,H_2` (4); scaffold B contributes `OR(R,QB)`, `NOT(R)` plus the three chains (5); scaffold C contributes `NOT(R)` plus three chains (4). Maximum over the accepted catalogue is 5, and the L1 hand fixtures are within it. |
| `MAX_PLAN_NODES`              | 37     | accepted band `S4` upper edge                                                                                                                                                                                                                                                                                        |
| `INTRO_PRELUDE_BOUND`         | 11     | `k + m ≤ 6 + 5` at the root; 1 for `NOT_INTRO`; 1 per `OR_ELIM` branch                                                                                                                                                                                                                                               |
| `OBLIGATION_RECURSION_BOUND`  | 80     | `2 × MAX_PLAN_NODES + 6`, covering materialize entries                                                                                                                                                                                                                                                               |
| `PRIMITIVE_STEP_BOUND`        | 100    | `(k+m) ≤ 11` root intros `+ 2 × 37 = 74` rule primitives `+` at most `37` rule-local intros (one per `NOT_INTRO`, two per `OR_ELIM`, jointly bounded by node count) `= 122`; rounded **up** to a declared ceiling of **`128`**                                                                                       |
| `ENUMERATION_CANDIDATE_BOUND` | 4096   | fail-closed ceiling on one `actions()` list                                                                                                                                                                                                                                                                          |
| `CANDIDATE_EVALUATION_BOUND`  | 524288 | `PRIMITIVE_STEP_BOUND(128) × ENUMERATION_CANDIDATE_BOUND(4096)`                                                                                                                                                                                                                                                      |

`PRIMITIVE_STEP_BOUND = 128`. V1's `518 → 512` arithmetic is withdrawn.

**Counters and precedence.** `enumeration_count` increments once per `enumerate_contained` call; `evaluation_count` once per candidate clone-execution; `primitive_count` once per executed script step. Checks fire in this strict order at each step: (1) `ENUMERATION_CANDIDATE_BOUND` on the just-materialized list; (2) `CANDIDATE_EVALUATION_BOUND` on the cumulative evaluation counter; (3) `PRIMITIVE_STEP_BOUND` before executing the selected action. The first to trip wins and returns `COMPILER_NO_MATCH / CANDIDATE_BUDGET_EXHAUSTED`, `…/EVALUATION_BUDGET_EXHAUSTED`, `…/STEP_BUDGET_EXHAUSTED` respectively. A ceiling may refuse a supported plan; it asserts no universal reachability.

---

## 7. Records, causes and the exception law (audit m2)

### 7.1 Records

Success keys, exactly and in order:

```text
('schema','ok','cause','subcause','theorem_identity','theorem_name',
 'public_projection_sha256','skeleton_identity','plan_node_count',
 'proof_tree_node_count','primitive_action_count','replay_action_count',
 'compile_enumerations','compile_evaluations','semantic_script_sha256',
 'rule_kinds','families','final_frontier_size','empty_goal')
```

`schema='philosophia.stager.l4-compile-replay.v1'`, `ok=True`, `cause=None`, `subcause=None`, `final_frontier_size=0`, `empty_goal=True`.

Failure keys, exactly `('schema','ok','cause','subcause')`; **no** identity, count, script or coverage field appears on a failure record.

### 7.2 Closed causes, strict precedence

```text
1. L4_INPUT_NOT_L1_ACCEPTED   (subcause = accepted checker cause)
2. SEQUENT_REDERIVATION_MISMATCH (subcause = accepted L3 subcause)
3. COMPILER_NO_MATCH  (NO_CANDIDATE, EFFECT_NOT_A_SUBSEQUENCE,
                       NON_ASSUME_OBLIGATION_SILENTLY_INHABITED,
                       ASSUME_NOT_INHABITED, NEUTRAL_GRAMMAR_VIOLATED,
                       DUPLICATE_ACTION_DISPLAY, CANDIDATE_EVALUATION_EXCEPTION,
                       CANDIDATE_BUDGET_EXHAUSTED, EVALUATION_BUDGET_EXHAUSTED,
                       STEP_BUDGET_EXHAUSTED)
4. COMPILER_AMBIGUOUS_MATCH (MULTIPLE_OUTER, MULTIPLE_SELECT_GOALS,
                             MULTIPLE_SELECT_CONSTRUCTION,
                             AMBIGUOUS_EFFECT_ALIGNMENT)
5. PEANO_REPLAY_REFUSAL (NO_REMATCH, AMBIGUOUS_REMATCH, ACTION_EXCEPTION,
                         WRONG_CHILD_FRONTIER, EARLY_TERMINAL,
                         STEP_BOUND_EXCEEDED)
6. PEANO_REPLAY_NONTERMINAL (OPEN_FRONTIER_REMAINS)
```

Causes 3–6 are exactly charter §8's closed compiler/replay causes.

### 7.3 One exception law

`compile_and_replay` raises **exactly two** exception classes and nothing else: `TypeError`/`ValueError` for argument-contract violations (§1.4 step 1), and `L4InvariantError(code)` for internal defects, with `code` from the closed tuple

```text
CANONICAL_THEOREM_DISAGREEMENT, ENUMERATION_DEDUP_VIOLATED,
CANDIDATE_EVALUATION_MUTATED_STATE, INTRO_PRELUDE_BOUND_EXCEEDED,
OBLIGATION_RECURSION_BOUND_EXCEEDED, FRONTIER_LAW_VIOLATED,
THEORY_BYTES_MISMATCH
```

Every **Peano-originated** exception is converted at its boundary into a §7.2 public refusal and never escapes. `L4InvariantError` is the only escaping non-argument exception, and none may arise for an accepted input; any occurrence is a gate failure, not a draw cause. V1's contradictory "no other exception escapes" clause is withdrawn.

### 7.4 Fresh replay

Replay builds a **new** `PyProofState` from the pinned theory bytes, `THEORY_PREMISES` and the same canonical public goal; re-enumerates and rematches by §5 descriptor at every step; reuses no compile-side state, action, clone or cache. Refusal semantics are §7.2 cause 5/6, with the global success condition of §4.7.

---

## 8. Acceptance artifact

Canonical JSON plus one newline, written by a test-only writer to a caller-supplied path:
`STAGE_R_L4_COMPILE_REPLAY_ACCEPTANCE_V1.json`.

Top level, exactly:

```text
('schema','contract_sha256','activation_sha256','charter_sha256',
 'l3_annex_sha256','l3_exclusions_sha256','source_v3_sha256',
 'l2_code_gate_sha256','theory_sha256','minimo_base_commit',
 'identity_domain','compile_domain','source_l3_exclusions',
 'fixture_results','coverage')
```

Per row, exactly:

```text
('fixture_name','source','raw_plan_sha256','raw_theorem_sha256',
 'theorem_identity_sha256','theorem_name','public_projection_sha256',
 'skeleton_identity_sha256','band','plan_node_count','proof_tree_node_count',
 'primitive_action_count','replay_action_count','compile_enumerations',
 'compile_evaluations','semantic_script_sha256','rule_kinds','families',
 'final_frontier_size','empty_goal')
```

Eleven rows ascending by `fixture_name`; the first eight fields copied **verbatim** from the accepted L3 artifact and V3 ledger after re-verification; `source_l3_exclusions` embeds the complete parsed L3 artifact byte-for-value; `coverage` aggregates `rule_kinds`, `families`, `bands`, `directions` from compiled scripts only. No L2, L3 or V3 byte may change; the artifact adds compile/replay facts only and carries no root, key, draw, scaffold, reservoir marker or future namespace.

---

## 9. Scope reconciliation (carried unchanged from accepted V1 §§5.1–5.4)

The eleven excluded valid plans are the entire current minimum gate; charter §8 stages 1–2, 6–7 and 10–11 are outside it, stages 3–5 are discharged by the accepted checker and accepted L3, stages 8–9 are this annex. The nine premise witnesses and eight ambient-arrow chains are `ENUMERABILITY_WITNESS_ONLY`: they have no accepted L1 plan and no L3 identity, and **must not** receive fabricated compiler inputs. Charter §9's ambient-arrow "full compilation and fresh replay" sentence is the deferred dev-core `COMPILER_FAMILY_UNREACHABLE` duty already ratified as deferred by Stage-R §4.2; Stage-R §1.6's instrument-relativity price stands. The eight-root quota, `4x4` band reachability, stage-6 collision economy, query measurement, G4ip, alternative-proof audits, generator scan and general extensibility are not restored.

---

## 10. Mandatory code gate

1. **Authority.** Hash-before-use of every consumed governing file, resolved through the configurable project-root and recovery-root variables, verified as the first statement of the governing loader; missing and mismatched both fail closed.
2. **Fixtures.** Only the five existing L1 builders and the six literal frozen rows; assert `canonical_result_sha256`; re-verify all eleven V3 raw hashes; selector-scan name absent from both files, never imported or called; no new draw.
3. **Binding.** Production itself calls the accepted checker and accepted L3 `identify`; no caller-supplied identity path exists.
4. **Compile and double fresh replay** per fixture, plus two fresh subprocesses under different `PYTHONHASHSEED`, comparing canonical bytes.
5. **Coverage** asserted from compiled scripts: all ten rule kinds and seven families, each credited only from nodes that emitted their rule's primitives (§4.5).
6. **Alpha/hypothesis/local metamorphics** over the full `k!` orbit: L3 identity, public bytes and skeleton identity re-asserted unchanged, **and** L4 goal string, script hash, counts and acceptance record unchanged; the §3 automorphic case exercised explicitly.
7. **Collisions** at the real candidate boundary: zero-match and semantically distinct duplicate-match injections asserting the exact public refusal, including a case where the two candidates' `str()` agree.
8. **Records**: every key, cause, subcause and the §7.2 precedence; absence of compile/replay fields on failures.
9. **Freshness/aliasing**: object-identity proof that no compile-side object reaches replay; inputs byte-unchanged; no output alias; replay order, leftover, exhaustion, early-terminal and wrong-frontier mutations each asserting their distinct cause; explicit frontier-emptiness assertions.
10. **Order independence**: permute the materialized candidate list at every step; assert byte-identical scripts and records.
11. **Discipline**: AST import allowlist of §1.3, no forbidden call, no unguarded `while`, no retry `try`, no filesystem/process access, no mutable module global.
12. **Artifact** written twice to caller-supplied temporary paths; byte identity; exact schemas, counts, coverage; byte-for-value L3 and V3 preservation.
13. **Routes**: ordinary discovery with measured count reported; L3-delta-plus-L4-delta and single-cumulative routes with identical manifests; exact two-new-file L4 delta scope; original worktrees unchanged and not used as evidence.

**Injection seam (audit M4).** The single injection point is the module-private candidate materialization boundary `_materialize_candidates`. Tests rebind it temporarily and **restore it in a `finally`**; every injection test asserts the result through the unmodified public `compile_and_replay`. A dedicated test asserts the public signature is exactly `(plan, expectation, theory_text)` and that no public name accepts a hook.

---

## 11. Structural blocker

The repairs above are complete and self-consistent, **except** that R1's per-rule derivation exposes a hard incompatibility between the mandatory calibration population and the pinned Peano surface. It is stated exactly, with durable evidence, and it is not repairable inside the authorized boundary.

### 11.1 The obstruction

By P13 `or_e` carries `#backward` only, so by P7 **only** `Apply(or_e)` is ever enumerated; there is no forward path. By P8, after `Apply(or_e)` the `('P : prop)` and `('Q : prop)` inputs are unbound by the output unifier (the output is `'R`, which unifies with the goal alone) and are therefore filled by branching over `context.inhabitants(prop)`. By P9 those inhabitants are exactly the **named** prop objects: the declared atoms `a0..a{k-1}` and the theory's `false`. A composite formula never becomes a named object of dtype `prop` in these states: the canonical sequent's declarations are exactly `('a_i : prop)`, its hypotheses are introduced as objects whose dtype is the hypothesis formula, and every theory arrow produces a proof of a proposition, never an object of dtype `prop`.

The `or_e` major input is `must_infer` (P13), so by P8 any branch whose `(or 'P 'Q)` is **not already inhabited** is pruned. Consequently, when the ND `OR_ELIM` major has a **non-atomic** disjunct, every candidate `(or ai aj)` over named props fails to match the inhabited composite major, every branch is pruned, and `actions()` after `Apply(or_e)` is **empty**. Rule R7 then necessarily returns `COMPILER_NO_MATCH / NO_CANDIDATE`.

### 11.2 Which mandatory fixtures this kills

From the durable accepted L3 exclusion artifact (`a64aaeb1…`), the canonical public sequents show the `OR_ELIM` major hypotheses:

- **`l2_gate_04`** (scaffold B): major `(or (and (or 'a3 'a4) (or 'a4 'a4)) (and (and (and 'a2 'a1) (or (or 'a2 'a1) 'a2)) (or (and 'a1 'a0) 'a0)))` — **both disjuncts composite**.
- **`l2_gate_05`** (scaffold A): major `(or (and (and (and 'a1 'a1) (and (and 'a2 'a4) 'a2)) 'a0) 'a3)` — **left disjunct composite**.

Both are members of the eleven permanent exclusions that §1.5 and §8 make the mandatory calibration population, and both contain a semantically required `OR_ELIM`. Neither can compile.

(For contrast, the four L1 fixtures with `OR_ELIM` — `valid_s1_or_and`, `valid_s2_exfalso`, `valid_s3_pair`, `valid_s4_exfalso_chain` — have atomic disjuncts and are unaffected by this obstruction.)

### 11.3 A second, unresolvable-on-paper risk

`not_e` has no annotation (P13), so `('P : prop)` is likewise filled from named props in the backward direction, and scaffolds B and C negate composite `R` (`l2_gate_00`, `01`, `03`, `04`). Unlike `or_e`, `not_e` does have a forward path (`Construct(not_e)` is enumerated by P7), whose viability depends on `application_results_with_preconditions` unifying against actual context objects. Whether that path yields the required construction **cannot be settled on paper** and could only be settled by executing Peano, which this pass, the activation and the repair task all forbid. It is recorded as an open risk, not as a proven blocker; the proven blocker of §11.2 is sufficient on its own.

### 11.4 Why no authorized repair closes it

- Using an alternative arrow or proof shape for `OR_ELIM` is alternative proof search, forbidden by charter §9.
- Search or backtracking over `SelectGoals` candidates is forbidden by the activation and by R1.
- A third module, a helper outside the two files, or a Peano/theory change exceeds the two-file scope and the accepted charter.
- Substituting, regenerating or dropping `l2_gate_04`/`l2_gate_05` is forbidden by §4.5's fail-closed rule, by Stage-R §3.3's permanent exclusions and by the audit.
- Re-rendering the canonical sequent so that composite disjuncts become declared atoms would change L3 theorem identity and public bytes, which are frozen.
- Weakening the ten-kind semantic-coverage requirement would weaken an accepted predicate, which the activation names as the exact condition for returning a blocker rather than proceeding.

The activation's own instruction applies: *"If the paper author cannot reconcile this minimum with the accepted charter without weakening an accepted predicate, the only valid paper result is a bounded structural blocker."*

### 11.5 Driver reproduction path

Read-only, no execution: `git -C <minimo> show 6066f482…:environment/src/universe/proof.rs` (`ProofState::actions`, `enumerate_apply_goals`, `execute_action`), `…:environment/src/universe/term.rs` (`Context::inhabitants`), `…:environment/src/python.rs` (`PyProofState`, `PyProofAction`); the durable theory at `recovery/archive/accepted_l01/learning/theories/…` (`2056deaf…`); and the durable L3 exclusion artifact (`a64aaeb1…`) for the two canonical sequents in §11.2.

---

## 12. Audit disposition

| item                                 | disposition                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C1** obligation/frontier semantics | **Replaced** by §4: per-rule table R0–R11, two modes, neutral grammar with refusal, R4 unconditional arrow goal, R7 inferred major plus mandatory materialization and two branch arrows, R8/R10 recursive neutral spines, ordered frontier with fixed push/pop and dual success condition, ordered-subsequence alignment with silent-inhabitation refusal, termination proof and exact counts. Derivation surfaces the §11 blocker. |
| **M1** alpha tie proof               | **Replaced** by §3: theorem-min → obligation-tree-min → first-lexicographic, with an invariance proof over the full orbit and a bound automorphic test. L3 bytes unchanged.                                                                                                                                                                                                                                                         |
| **M2** display/proof-noise identity  | **Replaced** by §5: typed kind + dtype + ordered executed effect only; display forbidden in matching and hashing, permitted only as a post-selection diagnostic; proof value omitted from `SelectConstruction` identity with proof; Stage-A helper used for containment with a proof that its sort never selects.                                                                                                                   |
| **M3** import allowlist              | **Closed** in §1.3: one allowlist permitting `itertools`, `hashlib` (raw UTF-8 theory pin only) and `phase2_actions.canonicalize_action_object_pairs`, with transitive imports disclosed and no codec/query/learner/MCTS instantiation. No alternative offered.                                                                                                                                                                     |
| **M4** public test seam              | **Closed** in §1.4 and §10: exact three-argument public signature, no public hook, single private `_materialize_candidates` seam restored in `finally`, public-record assertions, signature test.                                                                                                                                                                                                                                   |
| **M5** domain conflation             | **Closed** in §1.5: production interface domain versus eleven-row calibration population, with no completeness claim and no plan generated or selected.                                                                                                                                                                                                                                                                             |
| **M6** bounds/exceptions             | **Closed** in §6 and §5.5: `PRIMITIVE_STEP_BOUND = 128` re-derived (false `518→512` withdrawn), `MAX_GLOBAL_HYPOTHESES = 5` derived from the accepted L2 grammar, `CANDIDATE_EVALUATION_BOUND` derived as the product, counter increments and strict terminal precedence stated, every candidate-evaluation exception failing closed under `CANDIDATE_EVALUATION_EXCEPTION`.                                                        |
| **m1** provenance                    | **Disclosed** in §0.1 without claiming compliance; all V1.1 claims from durable files and `git show`.                                                                                                                                                                                                                                                                                                                               |
| **m2** exception/empty-goal wording  | **Closed** in §7.3 (one exception law) and §4.7 (global frontier emptiness, never the last returned child list).                                                                                                                                                                                                                                                                                                                    |

---

## 13. Deliverables, review stop and authorization boundary

Builder deliverables, if implementation were ever authorized, would live under `successor/stage_r/l4/candidate/`: the two `learning/` files, the acceptance JSON, a delta against the accepted L3 tree (`6194d40c…`) adding exactly two files, a cumulative against MINIMO base with exactly 38 paths, and a Builder report pinning every hash, count, route manifest and focused time. No commit, no push, no worktree of the original checkouts.

**Nothing in this document authorizes implementation.** No key or root minting or derivation, no fixture/frame/reservoir/held-out selection, no learner or selector, no MCTS, search or query measurement, no disposable execution, no scientific execution. The bounded paper-repair pass allowed by the activation is now consumed; per the audit's disposition, an unresolved critical algorithmic point returns the structural blocker rather than starting implementation.

---

## 14. Focused-time record

- This bounded paper-repair pass: start `2026-08-15T17:26:20+03:00`, end `2026-08-15T17:52+03:00`; rounded conservatively upward to the next 0.25 h: **0.50 h**.
- Accepted cumulative L4 focused time before this pass: **1.25 h**.
- Cumulative L4 focused time: **1.75 h**.
- Remaining from the 24-hour L4 budget: **22.25 h**.

User reading and decision latency is excluded. L3 focused time is not charged to the L4 budget.

---

```text
L4_SCOPE=MINIMUM_SEMANTIC_COMPILE_PLUS_FRESH_EMPTY_GOAL_REPLAY
C1_M1_M6_m1_m2_REPAIRS_SPECIFIED=YES
PAPER_IMPLEMENTABLE_AS_TWO_FILES=NO
BLOCKING_OBSTRUCTION=OR_E_REQUIRES_NAMED_PROP_DISJUNCTS
BLOCKED_MANDATORY_FIXTURES=l2_gate_04,l2_gate_05
OPEN_UNRESOLVABLE_ON_PAPER_RISK=NOT_E_COMPOSITE_FORWARD_PATH
L4_IMPLEMENTATION_AUTHORIZED=NO
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```

STAGE_R_L4_MINIMUM_STRUCTURAL_BLOCKER_V1_1
