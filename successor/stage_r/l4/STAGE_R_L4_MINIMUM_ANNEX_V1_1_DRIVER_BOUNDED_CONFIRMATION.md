# Stage-R L4 minimum annex V1.1 driver bounded confirmation

Status: `REJECTED_RETURN_TO_IDEA_GATE`

Date: 2026-08-15

Object:
`STAGE_R_L4_MINIMUM_COMPILE_REPLAY_EXECUTABLE_ANNEX_V1_1.md`,
SHA-256
`3296ebbb494452ddaf9176642c734193d9a030c0c67c289d1c802cd47aa61be5`.

This is the single mechanical confirmation permitted after the bounded V1.1
paper repair. It introduces no new requirement and authorizes no code or
execution.

## Confirmed closures

V1.1 does close the paper defects C1's rule-specific frontier model, M1,
M4–M6 and m1–m2 at the level stated in its disposition, except where the
remaining semantic-action defect below prevents an implementable whole. It
preserves all authority hashes, the accepted L3 public surface, the exact
two-file MINIMO scope, the eleven-row gate population and every no-execution
boundary.

## Critical 1 — the claimed structural blocker is refuted by the pinned Rust

V1.1 §11.1, lines 441–443, claims a composite proposition never becomes a
named context object of dtype `prop`, so `or_e` can instantiate `'P` and `'Q`
only with declared atoms or `false`.

The pinned source says otherwise:

1. `ProofState::load` in
   `environment/src/universe/proof.rs` calls
   `self.derivation.define_subterms(g, false, ..., [goal_name])` for every
   initial goal.
2. `SelectGoals` calls the same `define_subterms` operation for every new
   subgoal.
3. `Derivation::define_subterms` in
   `environment/src/universe/derivation.rs` recursively visits every
   non-intrinsic `Term::Application`, including `and`, `or` and `not`
   applications. For every non-root subterm it computes `t.get_type(context)`
   and defines a generated name with that dtype and the composite term as its
   value.
4. `is_intrinsic_application` in `environment/src/universe/term.rs` lists only
   `rewrite`, `eq_symm`, `eq_refl` and `eval`; `and` and `or` are not excluded.
5. Therefore the composite disjuncts occurring inside the canonical full
   sequent are named context objects of dtype `prop`, and
   `Context::inhabitants(prop)` can supply them to the unbound `'P`/`'Q`
   declarations of `or_e`.

Thus `BLOCKING_OBSTRUCTION=OR_E_REQUIRES_NAMED_PROP_DISJUNCTS` and the claimed
mandatory-fixture deaths do not follow. The same omitted `define_subterms`
mechanism also invalidates §11.3's premise that the composite `not_e` parameter
is unresolved on paper. No Peano execution was needed for this refutation.

## Critical 2 — M2 remains open: outer actions have identical descriptors

V1.1 §5.1 defines

```text
descriptor(a,s) = (kind, dtype, effect)
```

where an outer `Apply(name)` has `kind=APPLY`, `dtype=None`, and executing it
returns exactly one cloned state with the same active goal. The same holds for
every simultaneously enumerable backward premise. Hence `Apply(and_i)`,
`Apply(or_il)`, `Apply(or_ir)`, `Apply(or_e)`, `Apply(not_i)`,
`Apply(not_e)` and `Apply(exfalso)` at a state have the same descriptor.

Likewise all outer `Construct(name)` actions have `kind=CONSTRUCT`, no dtype at
that step, and the same one-state/same-goal effect. V1.1 §5.2 line 277 says the
arrow is identified by the **subsequent** selection-group content, but §5.1's
descriptor and §5.2's matching algorithm contain no two-step lookahead or
macro-effect field. Under §5.2's own rule, two or more actions with the required
effect are `COMPILER_AMBIGUOUS_MATCH`. The compiler therefore cannot select its
first rule action and cannot implement the per-rule table.

The smallest conceptual repair would be an exact two-primitive macro descriptor
whose identity includes the complete canonical set of follow-up semantic
effects while keeping display out of selection. That is a substantive second
paper algorithm repair, not a mechanical confirmation, and the activation
permits at most one bounded paper repair. It is not authorized here.

## Major consistency findings

1. V1.1 §6's table gives the `PRIMITIVE_STEP_BOUND` row value as `100`, derives
   a total of `122`, says it is rounded to `128`, and then declares
   `PRIMITIVE_STEP_BOUND = 128`. One executable constant is not specified.
2. V1.1 §1.3 imports `phase2_actions`, which directly imports
   `phase2_codec`; the accepted Stage-A `phase2_codec` imports Torch. The same
   section then lists Torch as forbidden in production. Saying no Torch object
   is explicitly instantiated does not make the import graph consistent.

Both are locally repairable, but no paper-repair pass remains.

## Disposition

The exact V1.1 structural-blocker proof is not confirmed. The annex is also not
paper-implementable because its semantic action identity cannot select any
outer rule action, and because its bound/import contract is contradictory.

The activation's finite topology is exhausted:

- one paper-author pass: consumed;
- one driver paper audit: consumed;
- one bounded paper repair: consumed;
- one bounded mechanical confirmation: this document, consumed.

Starting another L4 paper repair would be the infinite-review failure the
topology was designed to prevent. Under the Stage-R contract §4.3 and the L4
activation, the current MINIMO L4 route closes and returns to `IDEA_GATE`.
This is an engineering-route closure, not a scientific negative and not a
falsification of the Stage-R or programme claim.

Focused-time accounting:

- before confirmation: 1.75 h;
- this bounded confirmation: 0.50 h conservative;
- cumulative L4 focused time: 2.25 h;
- unused engineering budget is not authority for another review.

```text
V1_1_CLAIMED_OR_E_BLOCKER_VALID=NO
V1_1_PAPER_IMPLEMENTABLE=NO
PAPER_REPAIR_PASSES_REMAINING=0
L4_IMPLEMENTATION_AUTHORIZED=NO
MINIMO_STAGE_R_ROUTE_STATUS=RETURN_TO_IDEA_GATE
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```

REJECT_STAGE_R_L4_MINIMUM_ANNEX_V1_1_RETURN_IDEA_GATE_DRIVER
