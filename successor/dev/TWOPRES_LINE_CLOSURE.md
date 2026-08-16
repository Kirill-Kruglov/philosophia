# TWOPRES — line closure

Status: `TWOPRES_00A=NOT_CHEAPLY_AUDITABLE`
Date: 2026-08-16

The stop rule declared in `TWOPRES_00A_REVIEW_DISPOSITION_2.md` fired on its
first test. The third protocol review returned two Critical findings that are
new discoveries rather than regressions of the second disposition's repairs.
Per that rule the line closes, no author cell is signed, and no further paper
repair is authorized.

```text
THIRD_REVIEW_NEW_CRITICAL=YES
TWOPRES_00A=NOT_CHEAPLY_AUDITABLE
AUTHOR_CELLS_MAY_BE_SIGNED=NO
IMPLEMENTATION_AUTHORIZED=NO
FURTHER_PAPER_REPAIR_AUTHORIZED=NO
```

No script was written, no triple generated, no monoid completed, no run
performed. The line consumed three bounded paper passes and no compute.

## The two Criticals, verified

**C1 — certified relation deletion is circular as specified.** V2 §3.1 claimed
that M1 and M2 witnesses both reduce to normal-form comparison. True for M1,
false for M2. With `R = {a = 1}`, the completed system reduces `a` to `1`, so
checking the deletion of `a = 1` against that system finds both sides equal —
while the remaining presentation is the free monoid on `a`, where `a != 1`.
The check consumed the relation it was checking. An admissible M2 could
therefore change the presented monoid, after which `R1` and `R2` no longer
present one `M` and the sealed labels stop being the task's true target.

Repair would require deriving the relation from `R \ {r}` alone, or
re-completing after deletion: a new algorithm, budget and rejection-cause set.

**C2 — the principal baseline is not a total function.** V2 conceded that
`M3`/`M4` may leave no alphabet bijection, then left method 2 searching the
`<= 720` symbol permutations anyway. With `a = bc` in `R1` and `M4` removing
`a` by substitution, the word `a` over `Sigma_1` corresponds to `bc` over
`Sigma_2`, and no partial permutation expresses generator-to-word. Method 2
has no defined output for such pairs while `r_m(t)` and the cascade assume
totality.

This one is mine twice over: the disposition for the previous review argued
that `M3`/`M4` stay admissible *because* they break the alphabet bijection,
and then the ticket kept a permutation search as the principal method.

## Findings retained

These survive the closure and are the yield of the line.

1. **Element correspondence between two presentations of one monoid is
   identifiable only up to `Aut(M)`.** Composing the second evaluation map
   with an automorphism leaves both unpaired streams byte-identical and
   changes every cross-stream label. This holds for any method whatsoever. It
   is a concrete, computable instance of the boundary the essay states in
   prose: what a learner can earn is the world up to the equivalence class its
   interface admits.

2. **Once generator-changing moves are permitted, "cheap correspondence" is a
   word-valued morphism search, not a symbol-permutation search.** The two are
   different problems with different complexity, and the second does not
   approximate the first.

3. **Certified relation deletion is not free.** Redundancy cannot be checked
   against a system that contains the relation under test.

Together: the object needs two nontrivial algorithms — certified deletion and
word-valued morphism search — before any audit of it can begin. That is why it
does not fit a 120-line desk audit, and it is a mapped boundary rather than an
absence of result.

## Majors recorded, not repaired

For anyone reopening the line:

- the `t = 0` positive control conflates two facts — recovery of the cosmetic
  renaming, and element-equality accuracy under `METHOD_WORD_BUDGET`. A
  budget-limited cheap method could be declared a broken instrument. This is
  the same error shape as the Minimo `FLAT` verdict, which was a search
  ceiling read as a substantive failure. Third occurrence of the pattern.
- `BUDGET_EXHAUSTED` has no defined place in the recovery denominator —
  error, exclusion or abstention give different curves and different terminals.
- pair balance is fixed against one evaluation map, so `chance = 0.5` does not
  follow for the orbit-scored task actually run.
- `CAND(t)` is named for the opposite of what its formula computes, and the
  ordering `0 <= CHANCE_TOL < RECOVERY_MAX <= 0.5` was never asserted.

## Note on the stop rule

The rule was written one pass before it bound, and it bound against the line
its author wanted to continue. That is the only condition under which such a
rule is worth anything. It is recommended as standing practice for any future
line: declare, before the second review, what pattern of review outcome closes
the line rather than repairing it.

## What this closure does not claim

It does not show that two presentations are a poor route to manufactured
experience. It shows that this formulation of the question does not admit a
cheap instrument, and names the two algorithms that would be needed first.
