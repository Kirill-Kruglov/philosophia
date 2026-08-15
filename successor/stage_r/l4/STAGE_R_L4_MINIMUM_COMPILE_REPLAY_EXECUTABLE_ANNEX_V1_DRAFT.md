# Stage-R L4 minimum compile-and-replay executable annex V1 draft

Status: `DRAFT_FOR_DRIVER_PAPER_AUDIT`

Date: 2026-08-15

Intended durable path:
`successor/stage_r/l4/STAGE_R_L4_MINIMUM_COMPILE_REPLAY_EXECUTABLE_ANNEX_V1_DRAFT.md`

This annex authorizes nothing. It is a paper contract whose later acceptance could authorize a bounded two-file implementation. It contains no author-choice packet, no `TBD`, no implementation-defined ordering and no alternative algorithm.

---

## 0. Authority, pins and verification state

Every hash below was recomputed from disk by this author before reasoning and matched.

| object                                                                             | SHA-256                                                            |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Stage-R contract `successor/stage_r/PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1.md` | `1c3cec3aa6bd7094e2d37b062a8f349df5b226e91bbdc4a7b21e80fb785172f3` |
| L4 activation `successor/stage_r/STAGE_R_L4_MINIMUM_BOUNDARY_ACTIVATION_V1.md`     | `8cfb71f75f7ad1346eb43babf0f233169a68549a7dbb4eee2f0935dcf539f982` |
| Stage-B charter v1.1.1 (`recovery/accepted_authority/…BOUNDARY_CORRECTION.md`)     | `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311` |
| accepted L2 annex                                                                  | `3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8` |
| accepted L2 code-gate JSON                                                         | `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0` |
| accepted V3 raw exclusion ledger                                                   | `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d` |
| accepted cumulative patch through L2 V5                                            | `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683` |
| accepted L3 executable annex                                                       | `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0` |
| accepted L3 closure                                                                | `5fcf97a053a2d8b57eb0db86b17ec076e62f6f3d63f0b13bef16f8edb89d8fbb` |
| accepted L3 production `phase2_stageb_identity.py`                                 | `ee1be7afef332d8ce87b37c885760dfddcdcb911525cc377aec940b02ac07860` |
| accepted L3 test `test_phase2_stageb_identity.py`                                  | `2d71a629acb8dfa5bd8d42eef57b87746e9e6df28a80b514e950515e506dd45e` |
| accepted L3 exclusion artifact                                                     | `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` |
| accepted cumulative patch through L3                                               | `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c` |
| L4 activation commit                                                               | `6f24e6b6e0162019f9b078e16224eb4cb47d70b5`                         |
| MINIMO base commit                                                                 | `6066f482c6752915ad21119f93dc162f4cb9db72`                         |
| accepted theory `learning/theories/propositional-logic-intuitionistic-fragment.p`  | `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507` |

The current original MINIMO worktree is dirty and is neither authority nor evidence. Every source fact in §§1–4 was read from a disposable reconstruction of MINIMO base plus the two accepted cumulative patches, and from the pinned Rust sources at the base commit. `/tmp` is not a durable output location and no paper artifact of this pass lives there.

**Pinned Peano interface facts** (read-only, from `environment/src/python.rs` and `environment/src/universe/proof.rs` at the base commit; cited by symbol, not by line, so later formatting cannot invalidate them):

- P1. `peano.PyProofState(theory: str, premises: list[str], goal: str)` constructs a state; a goal parse error raises `ValueError`.
- P2. `PyProofState.actions() -> list[PyProofAction]` is **deduplicated in Rust** by `ProofAction` `Hash`/`PartialEq` before crossing the boundary.
- P3. `PyProofState.execute_action(a) -> list[PyProofState]`. The returned list **is** the successor goal frontier; length `0` means no remaining goals.
- P4. `PyProofState.clone()`, `.goal()`, `.format_goal()`, `.format_context()`, `.names_in_context()`, `.premises()`, `.is_context_empty()`, `.lookup(name)`, `.construction_from_last_action()`, `.last_proven_proposition()`, `.construction_history()`, `.generating_arguments(name)` exist.
- P5. `PyProofAction` exposes `is_intro()`, `is_construct()`, `is_apply()`, `selected_construction() -> Optional[tuple[str, str]]`, `__eq__` (Rust `ProofAction` equality) and `__str__`.
- P6. `ProofAction` has exactly five variants: `Intro`, `Construct(String)`, `SelectConstruction(bool, Term, Term)`, `Apply(String)`, `SelectGoals(Vec<Term>)`.
- P7. `ProofState::actions()` is a **strict alternation keyed on the last history action**: after `Apply(_)` it returns only `SelectGoals(_)`; after `Construct(_)` it returns only `SelectConstruction(_,_,_)`; otherwise (empty history, or last action `Intro`/`SelectGoals`/`SelectConstruction`) it returns only `Intro?` plus, for each premise `p`, `Construct(p)` and/or `Apply(p)` according to annotations. Therefore `SelectConstruction` and `SelectGoals` are **never co-enumerated**, and neither is ever co-enumerated with `Intro`/`Construct`/`Apply`.
- P8. In the "otherwise" branch the arrow name of every `Construct`/`Apply` is drawn from `self.premises`, i.e. from the closed nine-name premise list supplied at construction.
- P9. `enumerate_apply_goals` pushes a subgoal only when `context.inhabitant(&goal).is_none()` — an obligation already inhabited in context is **discharged silently and does not appear** in the `SelectGoals` vector. Unbound declaration parameters are filled from `context.inhabitants(dtype)`, one branch per inhabitant.
- P10. `Term` derives `PartialEq, Eq, Hash`; its `Display` is a faithful s-expression rendering over the fragment's constructors.
- P11. `Display` for `ProofAction` is lossy: `SelectConstruction` prints only one of dtype/value, and both `SelectConstruction` and `SelectGoals` print the `=> …` prefix. Display is therefore **forbidden as an identity** in this annex (§3).
- P12. `PyProofAction.__eq__` on `SelectConstruction` is proof-irrelevant: two such actions with equal dtype (when the dtype is a prop) compare equal regardless of value. Combined with P2 this means the enumerated survivors of a `SelectConstruction` list have pairwise distinct identity keys.

**Pinned Stage-A containment facts** (`learning/phase2_actions.py`): `canonical_action_ascii` is `str(action)`; `canonicalize_action_object_pairs` pairs each unique serialization with its original object, sorts by serialization and raises `DuplicateActionSerialization` on any repeat; `refuse_uncontained_peano` guards real `TreeSearchNode` objects behind the isolated whole-item worker. L4 never constructs a `TreeSearchNode`, never enters MCTS and never uses `QueryCodec`; it uses raw `PyProofState` only, so the containment refusal is not triggered and is not bypassed.

**Pinned theory facts** (accepted theory file and the accepted L0 regression module's frozen premise table): nine premises `and_i, and_el, and_er, or_il, or_ir, or_e, not_i, not_e, exfalso`; required directions **backward** for `and_i, or_il, or_ir, or_e, not_i, not_e, exfalso` and **forward** for `and_el, and_er`; `not_e` carries no annotation and is enumerable in both directions; `or_e` is annotated `#backward or_e infer infer infer infer subgoal subgoal`.

An unresolved or mismatched pin suspends this annex.

---

## 1. Exact boundary

### 1.1 What this annex executes

Only Stage-R contract §4.1 item 3:

> Minimum semantic L4 compile plus fresh empty-goal replay, sufficient for reservoir membership and solvability witness.

The implementation target is semantic compilation plus an **independently fresh** empty-goal Peano replay of exactly the **eleven** already excluded checker-valid plan fixtures: the five L1 hand fixtures (`valid_s1_or_and`, `valid_s1_not`, `valid_s2_exfalso`, `valid_s3_pair`, `valid_s4_exfalso_chain`) and the six literal frozen L2 code-gate rows (`l2_gate_00 … l2_gate_05`). These eleven are a bounded engineering gate and permanent exclusions (Stage-R §3.3); they are never scientific data and never reservoir or held-out members.

### 1.2 Authorized MINIMO delta

Exactly two new files:

```text
learning/phase2_stageb_compile.py
learning/test_phase2_stageb_compile.py
```

No accepted existing file may change. The canonical acceptance JSON of §6 is a durable Philosophia-side Builder deliverable, **not** a third MINIMO patch path.

Production may import only: `__future__`, `typing`, `peano`, `phase2_stageb_canonical`, `phase2_stageb_checker`, `phase2_stageb_identity`, `phase2_stageb_render`, `phase2_stageb_schema`. It must not import the generator, `bootstrap`, `proofsearch`, `policy`, MCTS, Torch, `phase2_actions`, `phase2_codec`, `phase2_search`, `phase2_isolated`, any L3/L4 future module, `json`, `hashlib`, `random`, `secrets`, `os`, `subprocess`, `pathlib`, `time`, or any filesystem/process API. There is no mutable module state.

Importing the accepted checker in production is deliberate and is what removes caller trust (§1.4); charter §9 forbids the generator, MCTS, learned/uniform policy, G4ip and alternative proof search, and forbids none of the modules listed as permitted here.

The test module may additionally import `ast`, `copy`, `hashlib`, `itertools`, `json`, `os`, `subprocess`, `sys`, `tempfile`, `unittest`, `pathlib`, the accepted L2 generator (only to regenerate the six literal frozen rows), the five L1 builders from the accepted checker test module, and the accepted L3 test module's authority helpers. It must not import or call the frozen L2 selector-scan helper, scan a key range, mint or derive a key, or generate any row outside the six frozen rows.

### 1.3 Explicitly absent

No dev root or key; no quota accounting; no stage-6 collision seed; no exact-plan identity; no band-reachability sweep; no query measurement or `QueryCodec` instantiation; no G4ip, inverse, statement-model or alternative-proof audit; no generator scan; no MCTS, `TreeSearchNode`, policy or value model; no frame, reservoir or held-out selection; no learner or selector; no ambient-arrow family compilation (§5.3); no general L4 extensibility.

### 1.4 Input binding without circular trust

The production entry point takes **only** `(plan, expectation)` — the same pair the accepted L1 checker takes — plus the theory text. It does not accept a caller-supplied "already checked", "already identified", theorem, canonical theorem, public item, identity, fixture name, band, root, draw index or any generator metadata. Consequently no caller assertion can make an invalid input succeed.

Binding is performed inside production, in this fixed order:

1. `checked = check_plan(plan, expectation)` using the accepted L1 checker. If `checked['ok']` is not `True`, return the typed failure record with `cause = 'L4_INPUT_NOT_L1_ACCEPTED'` and `subcause` equal to the checker's own cause string. No compilation occurs.
2. `identified = identify(plan, checked['theorem'])` using the accepted L3 module. If `identified['ok']` is not `True`, return the typed failure record with `cause = identified['cause']` (`SEQUENT_REDERIVATION_MISMATCH`) and `subcause = identified['subcause']`. No compilation occurs.
3. L4 independently recomputes the winning alpha bijection (§2.2) and asserts that the canonical theorem it induces is byte-identical to `identified['canonical_theorem']`. Failure is `L4InvariantError('CANONICAL_THEOREM_DISAGREEMENT')`.
4. The Peano goal string is taken as `identified['public_item']['goal']` and nothing else.

There is no path on which a wrong theorem, a wrong L3 plan, an unchecked plan or a caller-supplied identity reaches compilation. L4 re-derives everything it relies on from `(plan, expectation)` using accepted, independently reviewed modules, and never re-implements L1 or L3 semantics.

---

## 2. Canonical theorem versus raw proof plan

### 2.1 What is compiled

Compilation and replay run against the **L3 canonical public sequent**, not a raw renderer string and not the raw plan's atom names or hypothesis order.

The accepted L3 public item's `goal` value is exactly `render_sequent(canon['atoms'], canon['hypotheses'], canon['goal'])`, which produces the bracketed arrow statement
`[('a0 : prop) -> … -> H1 -> … -> Hm -> G]`
in precisely the syntax the accepted L0 regression module already feeds to `peano.PyProofState` for its nine premise witnesses. This is the pinned evidence that the canonical public sequent is a parseable Peano statement; L4 introduces no new statement syntax.

Reservoir membership is therefore decided on the same bytes L3 sealed. There is **no second theorem name**: L4 never calls `canonical_hash` on any object other than through the accepted L3 functions, never re-renders a sequent, and copies `theorem_identity`, `theorem_name` and `public_projection` verbatim from `identified` into its records and artifact.

**Compilation input.** The compiler consumes a **semantic obligation tree**, not the raw checked plan and not a second "canonical plan" data object. The obligation tree is derived from the checked plan by applying the winning bijection to every formula occurrence, and it carries per node exactly: the ND rule kind, the substituted conclusion formula, the substituted local-assumption formula where the kind has one, and the ordered child obligations. It carries no identifier, no band, no node index and no plan bytes. Choosing an obligation tree rather than a transformed plan is what makes §2.4's invariance provable: the tree has no field in which a global identifier, a hypothesis position or a local name could survive.

### 2.2 The winning bijection, its uniqueness and its tie rule

Let `k = len(theorem['atoms'])`, `3 ≤ k ≤ 6`. For each `p ∈ itertools.permutations(range(k))` in native lexicographic order, let `sigma_p` map the `i`-th ascending source atom to `a{p[i]}`, and let `T(p)` be the candidate `{'atoms': ['a0'…'a{k-1}'], 'hypotheses': sorted(substituted hypotheses by canonical bytes), 'goal': substituted goal}`.

- The minimum of `canonical_bytes(T(p))` over all `p` is unique **as a byte string** — it is a minimum of a finite totally ordered set — and equals `canonical_bytes(identified['canonical_theorem'])` by the accepted L3 algorithm.
- The **permutation** attaining it need not be unique: a theorem with a non-trivial atom automorphism admits several minimising `p`.
- **Tie rule (frozen).** L4 uses the first minimising `p` in `itertools.permutations(range(k))` order, i.e. the lexicographically smallest minimising tuple. `WINNING_BIJECTION_TIE_RULE = 'FIRST_LEXICOGRAPHIC_MINIMISER'`.

**Consequence, proved.** Any two minimising permutations `p, q` satisfy `T(p) = T(q)` byte-for-byte, hence induce the same canonical theorem, the same public item and the same Peano goal string. They may induce different obligation trees, hence possibly different primitive scripts. Fixing the first minimiser makes the compiled script a deterministic function of the checked plan. The replay **acceptance** (empty goal frontier) is invariant under the choice, because it is decided against a goal string that is provably identical; only the recorded script bytes are pinned by the tie rule.

### 2.3 Global and local assumptions

- **Global assumptions are selected by formula after canonical sorting, never by raw ID or position.** In the canonical sequent the hypotheses appear in canonical-byte order, and Peano introduces them by `intro.` in exactly that order. The compiler never reads `plan['hypotheses'][i]['id']` and never uses a hypothesis list index as a Peano handle. An ND `ASSUME hN` leaf is discharged by **context inhabitation** (P9): its substituted conclusion is already inhabited, so it contributes no subgoal and no primitive action.
- **Distinct global hypotheses remain distinct** under any bijection (substitution is injective on formulas because the atom map is a bijection), and the accepted L1 checker already rejects duplicate global hypothesis formulas. Therefore the canonical hypothesis order is a strict total order and the `intro.` prelude is unambiguous.
- **Repeated subformulas are harmless**: identity is by whole-formula canonical bytes, and the compiler never matches a proper subformula.
- **Local assumptions** arise only in `OR_ELIM` (two) and `NOT_INTRO` (one). Under the theory's backward annotations these become **arrow subgoals** (`['P -> 'R]`, `['Q -> 'R]`, `['P -> false]`). The compiler discharges an arrow goal with `intro.` (§3.4), and **Peano generates the bound name itself**. ND local identifiers `lN` therefore never cross into Peano, cannot shadow anything, and are erased exactly as the accepted L3 rule skeleton erases them. The compiler tracks locals by obligation position only.
- **Formula and type bounds** are the accepted ones and are re-asserted, not re-chosen: `3 ≤ k ≤ 6` declared atoms, at most `MAX_FORMULA_NODES = 24` nodes in every walked formula, `8 ≤ N ≤ 37` non-`ASSUME` plan nodes, at most four global hypotheses in the eleven fixtures.
- **Child ordering.** The obligation tree fixes child order per kind: `AND_INTRO → (left, right)`; `AND_ELIM_LEFT`/`AND_ELIM_RIGHT` → `(source,)`; `OR_INTRO_LEFT`/`OR_INTRO_RIGHT` → `(source,)`; `OR_ELIM → (major, left_branch, right_branch)`; `NOT_INTRO → (body,)`; `NOT_ELIM → (negative, positive)`; `EXFALSO → (source,)`; `ASSUME → ()`. `AND_INTRO` is commutative in the skeleton but **not** here: the obligation tree preserves the plan's `left`/`right`, and matching is by conclusion formula, so a swapped `AND_INTRO` yields the same set of subgoals and hence the same `SelectGoals` action — see §2.4. Both `AND_ELIM` directions are retained as distinct kinds because they select different forward arrows (`and_el` vs `and_er`). `NOT_ELIM` operand order is retained. `OR_ELIM`'s major is retained in first position.

### 2.4 Invariance proof

**Claim.** Alpha renaming of the declared atoms and permutation of the global hypothesis list cannot change the compiled semantic script or the replay acceptance record.

**Proof.** Let `P` be a checked plan and `P'` differ from `P` only by (i) an atom bijection `tau` and/or (ii) a permutation of `plan['hypotheses']` with consistent global-ID rewriting.

1. The accepted L3 `canonical_theorem` is invariant under both, and this is not assumed here: it is the closed L3 result, exercised in the accepted L3 gate over the full `k!` orbit for all eleven fixtures and asserted byte-for-byte. Hence `identified['canonical_theorem']`, `theorem_identity` and `public_item` are identical for `P` and `P'`, and so is the Peano goal string.
2. The winning bijection for `P'` is `sigma ∘ tau^{-1}` composed to the same canonical image; by §2.2 the induced `T(p)` is byte-identical, and the tie rule selects a minimiser deterministically in each case.
3. The obligation tree is built from **substituted formulas and rule kinds only**. Substitution composes: applying `tau` then the winning bijection of `P'` yields the same formulas as applying the winning bijection of `P`. Global IDs, hypothesis positions and local IDs are not fields of the tree. Therefore the obligation trees of `P` and `P'` are equal as data.
4. The compiler is a pure function of (goal string, theory bytes, premise list, obligation tree) — it reads no other input. Equal inputs give an equal script.
5. Replay is a pure function of (goal string, theory bytes, premise list, script). Hence the acceptance record and every count in §4.5 are equal. ∎

The one place where step 3 could fail is an automorphic theorem with two minimising permutations; step 2's frozen tie rule removes it.

---

## 3. Semantic action identity and deterministic compilation

### 3.1 Prohibited identities

No action may be selected by list index, by raw enumeration order, by `str(action)` equality or prefix, by premise name alone, or by any Python object identity. Display is forbidden as an identity by P11. Enumeration order is not assumed anywhere (§7 item 10 tests this).

### 3.2 The semantic descriptor

For an enumerated action `a` at state `s`, the descriptor is the tuple

```text
descriptor(a, s) = (kind, arrow, selection, effect)
```

computed **only** from typed accessors and executed effect:

| field       | how obtained                                                                                                                                                                                     | value                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| `kind`      | `a.is_intro()` / `a.is_construct()` / `a.is_apply()` / `a.selected_construction() is not None` / residual                                                                                        | one of `INTRO`, `CONSTRUCT`, `APPLY`, `SELECT_CONSTRUCTION`, `SELECT_GOALS` |
| `arrow`     | for `CONSTRUCT`/`APPLY` only: the unique `p` in the closed nine-premise tuple with `str(a) == 'c ' + p` resp. `'a ' + p`; zero or several matches is `L4InvariantError('ARROW_NAME_UNRESOLVED')` | premise name or `None`                                                      |
| `selection` | for `SELECT_CONSTRUCTION` only: `a.selected_construction()`                                                                                                                                      | `(dtype_string, value_string)` or `None`                                    |
| `effect`    | executed on a **clone** (§3.3): the tuple of `child.goal()` strings of `s.clone().execute_action(a)`, in returned order, plus its length                                                         | tuple of Term strings                                                       |

The five `kind` values are exhaustive and mutually exclusive by P6 and P5, and the residual case is `SELECT_GOALS` because `selected_construction()` returns `Some` exactly for `SelectConstruction`.

The `arrow` field is an exact equality test against a **closed, pinned nine-name set** that is cross-checked by the typed predicate, not a prefix scan of an open string space; by P8 the arrow of any enumerated `Construct`/`Apply` is a member of that set, and by P6 `ProofAction::Apply`/`Construct` equality **is** equality of that name. This is semantic identity, not string prefixing.

`effect` supplies the identity that Display destroys (P11) and that no typed accessor exposes for `SelectGoals`.

### 3.3 Safe candidate evaluation

Computing `effect` executes a candidate. It is done under these frozen rules:

1. The action is executed on `s.clone()`, never on `s`.
2. The returned child states are used only to read `goal()`; they are then discarded and never retained, cached, stored in a descriptor, or carried into replay.
3. No clone, child or action object crosses from compilation into replay (§4.1).
4. Any exception from `execute_action` during candidate evaluation is caught and the candidate is recorded as **non-evaluable** and excluded from matching; if a PyO3 panic (`type(exc).__module__ == 'pyo3_runtime'` and `type(exc).__name__ == 'PanicException'`) occurs it is converted to the public refusal `PEANO_REPLAY_REFUSAL` at replay and `COMPILER_NO_MATCH` at compile, never to a success and never to a retry.
5. `s` is asserted unchanged after evaluation by comparing `s.goal()`, `s.format_context()` and `s.names_in_context()` before and after; a difference is `L4InvariantError('CANDIDATE_EVALUATION_MUTATED_STATE')`.

### 3.4 Deterministic traversal

The traversal is obligation-directed. It never searches, never backtracks and never retries.

```text
compile_node(state, obligation):
    state = intro_prelude(state)                     # §3.4.1
    kind = obligation.kind
    if kind == 'ASSUME':
        require obligation.conclusion is inhabited in state   # §3.4.2
        return state, []                                       # zero primitives
    required = REQUIRED_DIRECTION[ARROW_OF_KIND[kind]]
    if required == BACKWARD:
        state, s1 = step_unique(state, APPLY, arrow=ARROW_OF_KIND[kind])
        state, s2 = step_unique(state, SELECT_GOALS,
                                expected_open_goals=open_goals(obligation))
        for child in obligation.children_in_frontier_order:
            state = compile_node(state, child)
    else:
        state, s1 = step_unique(state, CONSTRUCT, arrow=ARROW_OF_KIND[kind])
        state, s2 = step_unique(state, SELECT_CONSTRUCTION,
                                expected_dtype=obligation.conclusion_term)
    return state, script_fragment
```

with the frozen rule-to-arrow map and direction table (both taken from the accepted theory and the accepted frozen premise table, not chosen here):

| ND kind          | arrow     | required direction  |
| ---------------- | --------- | ------------------- |
| `AND_INTRO`      | `and_i`   | BACKWARD            |
| `AND_ELIM_LEFT`  | `and_el`  | FORWARD             |
| `AND_ELIM_RIGHT` | `and_er`  | FORWARD             |
| `OR_INTRO_LEFT`  | `or_il`   | BACKWARD            |
| `OR_INTRO_RIGHT` | `or_ir`   | BACKWARD            |
| `OR_ELIM`        | `or_e`    | BACKWARD            |
| `NOT_INTRO`      | `not_i`   | BACKWARD            |
| `NOT_ELIM`       | `not_e`   | BACKWARD            |
| `EXFALSO`        | `exfalso` | BACKWARD            |
| `ASSUME`         | —         | — (zero primitives) |

#### 3.4.1 `intro.` prelude

While the current goal is an arrow, exactly one `INTRO` action is enumerated (this is the pinned behaviour the accepted L0 regression module already asserts for all nine premise witnesses and for the ambient chains). Emit it and recurse.

**Monovariant.** Each `Intro` strictly decreases the number of input types of the goal arrow. The canonical sequent has `k` declarations plus `m ≤ 4` hypotheses, so the root prelude is exactly `k + m ≤ 10` steps; an `or_e`/`not_i` subgoal arrow has exactly one input, so its prelude is one step. `INTRO_PRELUDE_BOUND = 12` per node; exceeding it is `L4InvariantError('INTRO_PRELUDE_BOUND_EXCEEDED')`. There is no `while` loop without this proved monovariant.

#### 3.4.2 `ASSUME` and silently discharged obligations

By P9 an obligation already inhabited in context never appears in a `SelectGoals` vector. Therefore:

- an ND `ASSUME` leaf compiles to **zero** primitive actions and is verified by requiring that its substituted conclusion does **not** appear among the open goals produced by its parent's `SelectGoals`;
- `open_goals(obligation)` is defined as the ordered list of child conclusions **excluding** those whose child kind is `ASSUME`;
- `children_in_frontier_order` is the ordered list of non-`ASSUME` children.

This is the exact reconciliation between the charter's non-`ASSUME` node count and Peano's inhabitation-filtered frontier, and it is why the two counts in §4.5 differ by design.

#### 3.4.3 `step_unique`

```text
step_unique(state, expected_kind, **key):
    candidates = enumerate_contained(state)                    # §3.5
    matches = [c for c in candidates if matches_key(descriptor(c, state), expected_kind, key)]
    if len(matches) == 0: raise PublicRefusal('COMPILER_NO_MATCH', context)
    if len(matches) >= 2: raise PublicRefusal('COMPILER_AMBIGUOUS_MATCH', context)
    a = matches[0]
    children = state.execute_action(a)
    record descriptor and expected child count
    return successor_state(children), descriptor
```

Match keys, per kind:

- `APPLY` / `CONSTRUCT`: `descriptor.kind` equals the expected kind **and** `descriptor.arrow` equals the expected arrow. Ambiguity is impossible here by P2 plus P6 (equality is name equality), so two matches would itself be a Rust-level dedup violation and is reported as `COMPILER_AMBIGUOUS_MATCH` rather than assumed away.
- `SELECT_GOALS`: `descriptor.effect` goal-string multiset equals the multiset of `str`-rendered expected open goals, and the lengths agree. Because `SelectGoals` equality is `Vec<Term>` equality (P6) and `Term` Display is faithful (P10), two surviving candidates with equal effect would have been deduplicated by P2; a residual double match is therefore reported, not silently resolved.
- `SELECT_CONSTRUCTION`: `descriptor.selection[0]` equals the expected conclusion Term string. Two survivors sharing a dtype would have been deduplicated by P12; a residual double match is reported.

Zero matches is `COMPILER_NO_MATCH`; two or more is `COMPILER_AMBIGUOUS_MATCH`, **even when their display strings agree** — the descriptor, not the display, decides.

`successor_state` requires exactly one successor for `INTRO`, `APPLY`, `CONSTRUCT` and `SELECT_CONSTRUCTION`; for `SELECT_GOALS` it pushes the returned frontier in returned order onto an explicit obligation stack, and the compiler asserts that the frontier length equals `len(open_goals(obligation))`. A mismatch is `COMPILER_NO_MATCH` with sub-context `FRONTIER_ARITY`.

### 3.5 Contained enumeration

`enumerate_contained(state)` returns `list(state.actions())`. It performs no MCTS, constructs no `TreeSearchNode`, instantiates no `QueryCodec`, applies no 75-character prefix filter and imposes no order. It asserts that the returned length is at most `ENUMERATION_CANDIDATE_BOUND` (below) and that all pairwise `__eq__` comparisons are `False` (the Rust dedup contract P2); a violation is `L4InvariantError('ENUMERATION_DEDUP_VIOLATED')`.

The compiler never sorts candidates and never uses their position. Descriptor matching is order-independent by construction, which §7 item 10 tests by permuting the enumerated list.

### 3.6 Bounds

All bounds are fail-closed constants derived from pinned facts; exceeding any is a typed refusal, never a retry.

| constant                      | value | derivation                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MAX_DECLARED_ATOMS`          | 6     | accepted L0 schema                                                                                                                                                                                                                                                                                           |
| `MAX_GLOBAL_HYPOTHESES`       | 4     | maximum over the eleven fixtures; re-asserted per input                                                                                                                                                                                                                                                      |
| `MAX_FORMULA_NODES`           | 24    | accepted L0 schema                                                                                                                                                                                                                                                                                           |
| `MAX_PLAN_NODES`              | 37    | accepted band `S4` upper edge                                                                                                                                                                                                                                                                                |
| `INTRO_PRELUDE_BOUND`         | 12    | `k + m ≤ 6 + 4`, plus 2 headroom (§3.4.1)                                                                                                                                                                                                                                                                    |
| `OBLIGATION_RECURSION_BOUND`  | 40    | `MAX_PLAN_NODES + 3`                                                                                                                                                                                                                                                                                         |
| `PRIMITIVE_STEP_BOUND`        | 512   | `MAX_PLAN_NODES × 2` primitives per node, plus `MAX_PLAN_NODES × 12` prelude steps, rounded up                                                                                                                                                                                                               |
| `ENUMERATION_CANDIDATE_BOUND` | 4096  | fail-closed ceiling on one `actions()` list; the annotated outer list is at most `1 + 2 × 9 = 19` by P7/P8, while `SelectGoals`/`SelectConstruction` list sizes depend on `context.inhabitants` and are not bounded a priori on paper, so this is an explicit fail-closed constant, not a claimed worst case |
| `CANDIDATE_EVALUATION_BOUND`  | 8192  | fail-closed ceiling on total clone-executions per fixture                                                                                                                                                                                                                                                    |

`ENUMERATION_CANDIDATE_BOUND` and `CANDIDATE_EVALUATION_BOUND` are declared as fail-closed constants precisely because P9's `context.inhabitants` branching is data-dependent; the annex does not pretend to a derived worst case it cannot prove from pinned sources. Exceeding either returns `COMPILER_NO_MATCH` with sub-context `CANDIDATE_BUDGET_EXHAUSTED`, which fails the gate closed.

---

## 4. Independently fresh replay

### 4.1 Freshness

Compilation and replay use **distinct new** `PyProofState` instances, each constructed as
`peano.PyProofState(theory_text, list(THEORY_PREMISES), canonical_public_goal)`
from the pinned theory bytes (verified against `THEORY_SHA256` before construction), the exact nine premise names in `THEORY_PREMISES` order, and the accepted L3 canonical public sequent.

Replay may not reuse compiler state objects, action objects, clones, child states, cached enumerations or any module-level mutable value. The implementation holds no cache; §7 item 9 proves by object-identity comparison that no compile-side object reaches replay.

### 4.2 Rematching at each replay step

At each replay step the replayer **re-enumerates** contained actions from the current fresh state, recomputes descriptors, and requires a **unique** match to the stored descriptor for that step. It never reuses the compile-time action object and never trusts the stored index.

Refusal semantics, all mapped to closed charter causes:

| replay situation                                                | outcome                                                     |
| --------------------------------------------------------------- | ----------------------------------------------------------- |
| zero rematches                                                  | `PEANO_REPLAY_REFUSAL`, sub-context `NO_REMATCH`            |
| two or more rematches                                           | `PEANO_REPLAY_REFUSAL`, sub-context `AMBIGUOUS_REMATCH`     |
| `execute_action` raises, including PyO3 panic                   | `PEANO_REPLAY_REFUSAL`, sub-context `ACTION_EXCEPTION`      |
| successor frontier arity differs from the stored expected arity | `PEANO_REPLAY_REFUSAL`, sub-context `WRONG_CHILD_FRONTIER`  |
| frontier becomes empty while script steps remain                | `PEANO_REPLAY_REFUSAL`, sub-context `EARLY_TERMINAL`        |
| script exhausted while the frontier is non-empty                | `PEANO_REPLAY_NONTERMINAL`, sub-context `OPEN_GOALS_REMAIN` |
| any step beyond `PRIMITIVE_STEP_BOUND`                          | `PEANO_REPLAY_REFUSAL`, sub-context `STEP_BOUND_EXCEEDED`   |

Leftover script and script exhaustion are therefore distinct outcomes with distinct causes.

### 4.3 Empty goal without search

Success requires that after executing exactly the stored script — no more and no fewer steps — the obligation stack is empty **and** the last `execute_action` returned an empty list. By P3 an empty returned frontier is precisely "no remaining proof states", which is the same predicate the repository's own `HolophrasmNode.is_terminal()` uses (`len(self._proof_states) == 0`). No MCTS, search, policy, value model or `is_terminal` helper is invoked; L4 observes the returned list length directly.

After success the replayer asserts that no further action is possible or required by checking that the obligation stack is empty; it does not enumerate again, and it does not execute an additional action.

### 4.4 Canonical semantic-script hash

The script is serialized as an ordered list of step records

```text
{'step': int, 'kind': str, 'arrow': str|None,
 'selection_dtype': str|None, 'selection_value': str|None,
 'effect_goals': [str, ...], 'expected_arity': int}
```

and hashed with the accepted `canonical_hash` from `phase2_stageb_canonical`. It depends only on typed accessor values and Term strings. It does **not** depend on the Python hash seed (no set or dict iteration enters the serialization; all containers are ordered lists built in traversal order), on object addresses, on action enumeration order (order-independent matching, §3.5), or on `str(action)` for any kind other than the closed nine-name arrow lookup, which is itself order-free.

### 4.5 Retained counts

Per fixture the implementation retains, and the artifact records:

- `plan_node_count` — L1 non-`ASSUME` plan nodes (equals `expectation['node_count']`, re-asserted);
- `proof_tree_node_count` — total proof-tree nodes including `ASSUME` leaves;
- `primitive_action_count` — length of the compiled script;
- `compile_candidate_enumerations` and `compile_candidate_evaluations` — compile-side work;
- `replay_action_count` — actions executed during replay (must equal `primitive_action_count`);
- `final_frontier_size` — must be `0` on success;
- `semantic_script_sha256` — §4.4.

---

## 5. Exact minimum-scope reconciliation

### 5.1 Why the eleven valid plans are the entire current minimum gate

Charter §8 states the full future acceptance pipeline for **every consumed draw** (stages 1–11, including root processing, stage-6 collision seeding, truth-table check, query measurement and quota admission). Stage-R contract §4.1 replaces "every consumed draw" with a named minimum and says of its six required components "and only these"; §4.2 defers the eight-root quota terminal, universal `4x4` band quota fulfilment, skeleton-collision economy beyond the sealed frame, the full compiler-family catalogue, the complete-prover/G4ip audit, the inverse/statement-model/alternative-proof audits and general L3/L4 extensibility, by explicit author ratification recorded as a boundary correction rather than a silent override. Stage-R §3.3 makes every L0–L2 fixture, every gate item and every calibration item a permanent exclusion.

The intersection is exact: the only checker-valid plans that exist, are already permanently excluded, and are needed to demonstrate "semantic compile plus fresh empty-goal replay, sufficient for reservoir membership and solvability witness" are the five L1 hand fixtures and the six frozen L2 code-gate rows. Charter §8 stages 1–2 (draw derivation and construction) and 6–7 and 10–11 (collision seeding, truth-table, query measurement, quota admission) are outside this minimum; stages 3–5 are discharged by the accepted L1 checker and accepted L3 identity, which L4 calls rather than re-implements; stages 8–9 are exactly what this annex specifies. No accepted L0–L2 predicate is weakened, and no charter stage is reordered.

### 5.2 The nine premise witnesses and eight ambient-arrow chains

Both families are hand-declared **statements** in the accepted L0 regression module. Neither has an accepted L1 proof plan, and therefore neither has an L3 theorem identity, public projection or rule-skeleton identity — the accepted L3 exclusion artifact deliberately maps identities for exactly the eleven valid plans and records the two-role raw alias without inventing an identity for any renderer-only or enumerability object.

They are therefore classified `ENUMERABILITY_WITNESS_ONLY`. **They must not be assigned fabricated compiler inputs.** L4 must not synthesize a plan, theorem, canonical theorem or public item for any of them, and must not add them to the acceptance artifact's per-fixture rows.

### 5.3 Charter §9's ambient-arrow sentence

Charter §9 ends: "Full compilation and fresh replay of this family are L4 duties." Stage-R §4.2 defers "the full compiler-family catalogue". These reconcile exactly, and the reconciliation is not an inference of convenience:

- the ambient-arrow chains at depths 1..8 exercise `Construct(h)` on **context-introduced arrow hypotheses**, not on the nine theory premises. By P8 this is a different arrow population from the one the ND fragment uses;
- the accepted L0 module checks them for **enumerability only**, and the charter says so in the same paragraph;
- the accepted engineering audit of record classifies "L4 ambient-arrow family completeness / `COMPILER_FAMILY_UNREACHABLE` suite" as deferred universality, and `COMPILER_FAMILY_UNREACHABLE` is a charter §10 reason code under `DEV_CORE_FEASIBILITY_STOP` — i.e. it belongs to the eight-root dev-core run that Stage-R §4.2 defers wholesale;
- Stage-R §4.1's minimum is scoped to "reservoir membership and solvability witness", and reservoir items are ND plans, never ambient-arrow chains.

Accordingly the ambient-arrow family's full compilation and fresh replay remain an L4 duty **of the deferred dev-core route**, not of this minimum. This annex neither performs nor forbids it later; it records the deferral as already ratified under Stage-R §4.2 and carries Stage-R §1.6's price: every Stage-R result stays instrument-relative to the frozen prover. No new deferral is created here and no authority is overridden. The two authorities are reconcilable, so the structural-blocker verdict is not triggered on this ground.

### 5.4 Not restored

The eight-root quota, universal `4x4` band reachability, stage-6 collision economy, query measurement, G4ip, alternative-proof audits, generator scan and general compiler extensibility are not restored by this annex in any form.

### 5.5 Rule-kind and family coverage of the eleven fixtures

Coverage is **pinned**, not assumed. The accepted L2 code-gate JSON records, for the six frozen rows, `rule_kinds` containing all ten accepted ND kinds (`ASSUME, AND_INTRO, AND_ELIM_LEFT, AND_ELIM_RIGHT, OR_INTRO_LEFT, OR_INTRO_RIGHT, OR_ELIM, NOT_INTRO, NOT_ELIM, EXFALSO`), `families` containing all seven, `directions` containing both `AND_ELIM` directions, `bands` containing `S1..S4` and `catalogue` containing scaffolds `A`, `B`, `C`. The five L1 hand fixtures independently contribute `ASSUME`, `AND_INTRO`, both `AND_ELIM` directions, both `OR_INTRO` directions, `OR_ELIM`, `NOT_INTRO`, `NOT_ELIM` and `EXFALSO`.

Under §3.4 every non-`ASSUME` kind compiles through its own theory arrow and its own required direction, and `ASSUME` compiles through the inhabitation discharge of §3.4.2 — so each kind occupies a **semantically meaningful** compilation path rather than metadata. The gate asserts observed coverage from the compiled scripts themselves (§7 item 5), not from the JSON.

**Fail-closed rule.** If any of the ten kinds or seven families cannot be semantically compiled and replayed on the eleven fixtures, the L4 gate fails with `COMPILER_NO_MATCH` or `PEANO_REPLAY_REFUSAL` and the Builder stops with the blocked verdict. It is forbidden to substitute a new fixture, relax a kind, widen the catalogue or mint a replacement plan.

---

## 6. Acceptance artifact and frozen-output law

Durable Philosophia-side deliverable, canonical JSON plus exactly one trailing newline, produced by a test-only writer taking an explicit caller-supplied output path:

```text
STAGE_R_L4_COMPILE_REPLAY_ACCEPTANCE_V1.json
```

Top-level keys, exactly and in this set:

```text
('schema','contract_sha256','activation_sha256','charter_sha256',
 'l3_annex_sha256','l3_exclusions_sha256','source_v3_sha256',
 'l2_code_gate_sha256','theory_sha256','minimo_base_commit',
 'identity_domain','compile_domain','source_l3_exclusions',
 'fixture_results','coverage')
```

with `schema = "philosophia.stager.l4-compile-replay-acceptance.v1"`,
`identity_domain = "L1_CHECKED_ND_PLAN_WITH_3_TO_6_DECLARED_ATOMS"`,
`compile_domain = "SEMANTIC_COMPILE_PLUS_FRESH_EMPTY_GOAL_REPLAY_ELEVEN_EXCLUDED_VALID_PLANS"`,
and `source_l3_exclusions` embedding the **complete parsed accepted L3 exclusion artifact byte-for-value unchanged**.

`fixture_results` is ascending by `fixture_name`, exactly eleven rows, each with exactly:

```text
('fixture_name','source','raw_plan_sha256','raw_theorem_sha256',
 'theorem_identity_sha256','theorem_name','public_projection_sha256',
 'skeleton_identity_sha256','band','plan_node_count',
 'proof_tree_node_count','primitive_action_count','replay_action_count',
 'compile_candidate_enumerations','compile_candidate_evaluations',
 'semantic_script_sha256','rule_kinds','families','final_frontier_size',
 'empty_goal')
```

`source` is `L1_HAND_FIXTURE` for the five `valid_*` rows and `L2_CODE_GATE_FIXTURE` for `l2_gate_00..05`. The first eight fields are **copied verbatim** from the accepted L3 artifact and the accepted V3 ledger after re-verification; L4 recomputes none of them. `empty_goal` must be `true` and `final_frontier_size` must be `0` in every accepted row.

`coverage` has exactly `('rule_kinds','families','bands','directions')`, aggregated from the compiled scripts and obligation trees, sorted, and asserted to contain all ten kinds, all seven families, `S1..S4` and both `AND_ELIM` directions.

Serialization is `canonical_dumps(obj) + '\n'` using the accepted L0 serializer. Row order is `sorted(fixture_name)`; every list value is sorted where it is a set-like field (`rule_kinds`, `families`, `bands`, `directions`) and traversal-ordered where it is a sequence (`effect_goals`).

**Frozen-output law.** No fixture input, L2 result, L3 identity, L3 public byte, V3 row, existing JSON or existing hash may change. The L4 artifact adds compile/replay facts only. It contains no root, no key, no draw index, no scaffold, no scientific identity, no reservoir/held-out marker and no L3/L4 future namespace. If any accepted L3 or V3 value would move, the Builder stops blocked rather than rewriting it.

---

## 7. Mandatory sectioned code gate

The new test module must implement all thirteen sections. A test that exercises only a private helper without asserting the unmodified **public** record is insufficient everywhere below.

1. **Authority.** Hash-before-use verification of every governing file this gate consumes, resolved through the same configurable project-root and recovery-root variables the accepted L3 gate uses, verified as the first statement of the governing loader so nothing can populate a fixture cache first, missing and mismatched both failing closed. Adds the accepted L3 annex, L3 closure, L3 production/test/artifact, the L4 activation, this annex and the theory file to the bound set.
2. **Fixtures.** Reconstruct only the five existing L1 builders and the six literal frozen L2 `(key_hex, draw_index)` rows; assert their `canonical_result_sha256`; re-verify all eleven V3 raw plan and raw theorem hashes. The selector-scan helper name must not appear in either new file (assembled from parts if it must be referenced) and must not be imported or called. No new draw, no key range, no `5 x 256` scan.
3. **Binding.** Assert that production itself calls the accepted checker and the accepted L3 `identify`, that an unchecked or mutated plan cannot reach compilation, and that a caller cannot inject a theorem, canonical theorem, identity or public item.
4. **Compile and double fresh replay.** For each of the eleven fixtures: one compile, then **two independently constructed fresh replays**, asserting identical acceptance records and identical `semantic_script_sha256`; plus the same eleven compiled and replayed in two fresh subprocesses under different `PYTHONHASHSEED` values, comparing canonical bytes.
5. **Coverage.** Assert from the compiled scripts and obligation trees that all ten rule kinds and all seven families are observed on real semantic paths, and that each observed kind consumed its own theory arrow in its required direction.
6. **Canonical/raw metamorphics.** Over each fixture's full `k!` atom orbit, plus global-hypothesis permutation with consistent global-ID rewriting, plus local-ID relabelling: assert the L3 theorem identity, public bytes and skeleton identity are unchanged (not re-proved, re-asserted, so L3 is not weakened) **and** that the L4 goal string, `semantic_script_sha256`, all counts and the acceptance record are unchanged. Assert the winning-bijection tie rule is exercised, including at least one automorphic case if one exists among the eleven, and that its outcome is the first lexicographic minimiser.
7. **Collisions at the real candidate boundary.** Deliberate zero-match injection (an obligation whose conclusion is not derivable by its arrow) asserting the public `COMPILER_NO_MATCH` record; and duplicate-match injection at the real boundary — an opposite-direction `AND_ELIM` obligation and a semantically distinct second `SelectGoals`/`SelectConstruction` candidate — asserting the public `COMPILER_AMBIGUOUS_MATCH` record even when the two candidates' `str()` values agree. The smallest direct injection seam is a test-only candidate-list transformer passed to the public entry point as an explicitly named keyword whose default is `None` and whose production default path is untouched; the assertion is always on the unmodified public record, never on the helper.
8. **Records.** Mutations for every success and failure key, every cause and sub-context, and the full precedence order of §8.2, asserting exact key tuples and the absence of compile/replay fields on every failure record.
9. **Freshness and aliasing.** Object-identity proof that no compiler state, child state, action object, clone or cached enumeration reaches replay; input plan and expectation byte-unchanged; no mutable output alias with inputs or within the output; replay-step order, leftover-script, script-exhaustion, early-terminal and wrong-frontier mutations each asserting their distinct public cause.
10. **Order independence.** Permute the enumerated candidate list at every step through the injection seam of item 7 and assert byte-identical scripts, hashes and acceptance records.
11. **Discipline.** AST checks on production: import allowlist, no forbidden call names, no `while` without the §3.4.1 monovariant guard, no `try` that converts a refusal into a retry, no filesystem or process access, no mutable module global, no `random`/`time`/`hashlib`/`json` name.
12. **Artifact.** Write the §6 acceptance JSON twice to separate caller-supplied temporary paths; assert byte identity, the exact top-level and per-row schemas, eleven rows in ascending order, aggregate coverage, `empty_goal` true and `final_frontier_size` zero everywhere, and byte-for-value preservation of the embedded L3 artifact and every V3 row.
13. **Routes.** Ordinary Stage-B discovery with the measured count reported, not assumed; the coherent L3-delta-plus-L4-delta route and the single cumulative route producing identical non-`.git` manifests; exact two-new-file L4 delta scope; unchanged original MINIMO and Philosophia worktrees, neither presented as implementation evidence.

---

## 8. Production API, records and precedence

### 8.1 Entry point

```python
def compile_and_replay(plan: Mapping, expectation: Mapping, theory_text: str) -> dict
```

Argument validation is an API contract, not an outcome: `TypeError` for non-mapping `plan`/`expectation` or non-`str` `theory_text`; `ValueError` if `theory_text` does not hash to `THEORY_SHA256`. No other exception escapes. All outputs are fresh plain data; inputs are unchanged; no returned mutable object aliases an input or another returned position.

Success keys, exactly and in this order:

```text
('schema','ok','cause','subcause','theorem_identity','theorem_name',
 'public_projection_sha256','skeleton_identity','plan_node_count',
 'proof_tree_node_count','primitive_action_count','replay_action_count',
 'compile_candidate_enumerations','compile_candidate_evaluations',
 'semantic_script_sha256','rule_kinds','families','final_frontier_size',
 'empty_goal')
```

with `schema = "philosophia.stager.l4-compile-replay.v1"`, `ok = True`, `cause = None`, `subcause = None`, `empty_goal = True`, `final_frontier_size = 0`.

Failure keys, exactly:

```text
('schema','ok','cause','subcause')
```

with `ok = False`, `cause` one of the closed set below and `subcause` a member of that cause's closed sub-context tuple. **No failure record carries any identity, count, script or coverage field.**

### 8.2 Closed causes and strict precedence

```text
1. L4_INPUT_NOT_L1_ACCEPTED      (subcause = the accepted checker's own cause)
2. SEQUENT_REDERIVATION_MISMATCH (subcause = the accepted L3 subcause)
3. COMPILER_NO_MATCH             (NO_CANDIDATE, FRONTIER_ARITY,
                                  ASSUME_NOT_INHABITED, CANDIDATE_BUDGET_EXHAUSTED,
                                  PEANO_PANIC_AT_COMPILE)
4. COMPILER_AMBIGUOUS_MATCH      (MULTIPLE_APPLY, MULTIPLE_CONSTRUCT,
                                  MULTIPLE_SELECT_GOALS, MULTIPLE_SELECT_CONSTRUCTION)
5. PEANO_REPLAY_REFUSAL          (NO_REMATCH, AMBIGUOUS_REMATCH, ACTION_EXCEPTION,
                                  WRONG_CHILD_FRONTIER, EARLY_TERMINAL,
                                  STEP_BOUND_EXCEEDED)
6. PEANO_REPLAY_NONTERMINAL      (OPEN_GOALS_REMAIN)
```

The first applicable cause fires and suppresses the rest. Causes 3–6 are exactly the charter §8 closed compiler/replay causes; causes 1–2 delegate to already-accepted layers and invent nothing.

### 8.3 Invariant errors

Programmer and invariant defects raise `L4InvariantError(code)` carrying only `.code`, from the closed tuple:

```text
CANONICAL_THEOREM_DISAGREEMENT
ARROW_NAME_UNRESOLVED
ENUMERATION_DEDUP_VIOLATED
CANDIDATE_EVALUATION_MUTATED_STATE
INTRO_PRELUDE_BOUND_EXCEEDED
OBLIGATION_RECURSION_BOUND_EXCEEDED
PRIMITIVE_STEP_BOUND_EXCEEDED
THEORY_BYTES_MISMATCH
```

None may arise for any of the eleven accepted fixtures; any raise is a code-gate failure, not a new draw cause. **No unhandled Peano or PyO3 exception may become a success or an outcome-dependent retry**: every such exception is converted at its boundary to `PEANO_PANIC_AT_COMPILE` under `COMPILER_NO_MATCH` or to `ACTION_EXCEPTION` under `PEANO_REPLAY_REFUSAL`.

---

## 9. Deliverables, review stop and authorization boundary

### 9.1 Builder deliverables

Durable, under `successor/stage_r/l4/candidate/`:

```text
learning/phase2_stageb_compile.py
learning/test_phase2_stageb_compile.py
STAGE_R_L4_COMPILE_REPLAY_ACCEPTANCE_V1.json
minimo_phase2_stageb_l4_compile_v1_delta.patch
minimo_phase2_stagea_stageb_l01_l2_l3_l4_compile_v1_cumulative.patch
STAGE_R_L4_BUILDER_REPORT_V1.md
```

The delta is a Git patch relative to the **accepted L3 tree** (MINIMO base plus the accepted cumulative patch through L3, SHA-256 `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c`) and adds exactly the two authorized files. The cumulative patch is relative to MINIMO base `6066f482c6752915ad21119f93dc162f4cb9db72` and changes exactly the accepted 36 paths plus those two, i.e. 38 entries. Neither patch may contain a candidate-package path. The Builder works only in a fresh `mktemp -d` reconstruction, never modifies the original MINIMO or Philosophia worktrees, and does not commit or push.

### 9.2 Report

The Builder report must pin every input and output SHA-256; exact production and test line counts; every test command with measured counts and elapsed times; both route manifests and their equality; exact delta and cumulative path scopes; confirmation that the selector scan was not called and only six literal rows were regenerated; confirmation that the original worktrees are unchanged and not used as evidence; the unchanged L3 and V3 bytes; and focused time used against the budget.

### 9.3 Review topology and time kill

The activation's topology is finite and is enforced here: one paper-author pass; one driver paper audit; at most one bounded paper repair for a concrete defect; one bounded implementation pass after durable paper closure; one driver code audit and at most one independent targeted confirmation; at most one bounded code repair. The implementation phase may not begin from a draft — only from a committed, durably frozen annex.

The entire L4 route — paper closure, implementation, compile and fresh replay — must close within **24 focused working hours** measured from the first focused execution of the L4 paper-author task. Exhaustion of the budget or a structural incompatibility closes the MINIMO Stage-R route and returns to `IDEA_GATE`; neither ever broadens L4.

### 9.4 Authorization boundary

Even a fully green L4 gate authorizes **no** key or root minting or derivation, **no** fixture, reservoir, held-out or frame selection, **no** learner repair, training or selector qualification, **no** MCTS, search or query measurement, **no** disposable execution and **no** scientific execution. L4 closure requires a new literal author decision before any subsequent Stage-R component begins. This annex itself authorizes nothing: it is paper only, and its acceptance authorizes at most the two-file implementation described above.

---

## 10. Focused-time record

- Pass start: `2026-08-15T16:51:34+03:00`. Pass end: `2026-08-15T17:12+03:00`.
- Focused hours this paper-author pass, rounded conservatively upward to the next 0.25 h: **0.50 h**.
- Cumulative L4 focused hours consumed: **0.50 h**.
- Hours remaining from the 24-hour L4 budget: **23.50 h**.

User reading and decision latency is excluded. Prior L3 focused time (1 h 59 min) is not charged to the L4 budget, which the activation measures from the first focused execution of the L4 paper-author task.

---

```text
L4_SCOPE=MINIMUM_SEMANTIC_COMPILE_PLUS_FRESH_EMPTY_GOAL_REPLAY
L4_INPUT_DOMAIN=ELEVEN_EXCLUDED_CHECKER_VALID_PLANS
L4_AUTHORIZED_MINIMO_FILES=2
AMBIENT_ARROW_FAMILY_IN_SCOPE=NO
FULL_COMPILER_CATALOGUE_IN_SCOPE=NO
EXACT_PLAN_IDENTITY_IN_SCOPE=NO
QUERY_MEASUREMENT_IN_SCOPE=NO
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
LEARNER_OR_SELECTOR_EXECUTION_AUTHORIZED=NO
DISPOSABLE_EXECUTION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED_BY_THIS_DRAFT=NO
```

READY_FOR_STAGE_R_L4_MINIMUM_ANNEX_DRIVER_AUDIT_V1
