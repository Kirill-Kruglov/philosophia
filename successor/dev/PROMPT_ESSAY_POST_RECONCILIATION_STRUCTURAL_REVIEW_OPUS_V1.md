# Prompt — post-reconciliation philosophical/structural essay review (Claude Opus)

ROLE: independent philosophical and structural reviewer. Read-only. This is one
of two parallel reviews; do not read or anticipate the formal reviewer's
response. Do not edit the essay, invent a scientific route, inspect incomplete
runtime state, generate data, commit or push.

## Governing handoff

Read completely and verify:

```text
successor/dev/ESSAY_POST_RECONCILIATION_REVIEW_HANDOFF_V1.md
a9ddde576e47608010ba1f4dd672de00db966d9ca8fbc7dab92a810bb2ed18cc
```

Verify every pinned publication surface before review. If any differs, write
the response file with exact mismatch evidence and the blocking terminal.

Read the voice sources named in `essay/REVIEW_HANDOFF.md`. Treat
`essay/OUTLINE.md` as pre-result authorial context, not governing evidence.

## Review task

Read the complete essay once as an essay. Focus findings on the reconciliation
delta and its effect on the whole argument.

1. Introduction, current lines 47–69: does Hamilton-Zero belong between
   Computational Life and Formal Conjectures? After adding a third neighbouring
   system, is `I think both are right` still unambiguous? Does `stronger
   contemporary form ... than any position paper` advance the argument or sound
   like scale standing in for relevance?
2. Current lines 968–1001: do the TWOPRES and Minimo additions deepen the
   essay's boundary, or turn `What this does not show` into a development log?
   If either belongs elsewhere or needs compression, give one exact local move
   or replacement, not a rewrite.
3. Status ledger: does the enlarged continuation row remain legible and
   subordinate to the essay, or has the ledger become taxonomy substituting for
   a conclusion? Distinguish necessary honesty from apparatus displayed for its
   own sake.
4. Check the sequence climb → fall → trace → balcony after the additions. Flag
   only a real broken transition, doubled conclusion or antecedent ambiguity.
5. Re-read the three endings and the last `What this does not show` paragraph.
   Do proof, falsification and mapped boundary still leave genuine negative
   space, or does the new successor history pre-decide one ending rhetorically?
6. Check that non-citable development remains visibly subordinate to the
   programme question. A screen, engineering closure or inability to build must
   never feel like accumulated empirical falsification merely through volume.
7. Compare cadence and honesty to the sibling essays without forcing their
   syntax onto this one. Preserve the author's voice and the uncomfortable
   limits.

Do not redo statistical or source verification assigned to the formal line. You
may identify a factual ambiguity when it damages the argument, but do not build
a parallel evidence audit.

## Non-binding plan audit

Read `successor/dev/PROGRAMME_GOAL_AND_REENTRY_PLAN_V1.md`. In a separate short
section, answer:

- Does the plan genuinely return attention to verification/falsification, or
  does `event-driven carrier watch` merely rename indefinite waiting?
- Is prioritizing a bounded `PROOF_CORE` witness philosophically faithful to the
  essay's definition of experience?
- Does the review stop rule preserve corrigibility without making review itself
  the project?

This advice does not control the essay verdict and authorizes nothing.

## Findings standard

Findings first, ordered Critical/Major/Minor. For every Critical or Major give:

- exact current file:line or section;
- why the defect changes meaning rather than taste;
- the smallest local repair;
- `DELTA_CAUSED=YES|NO`.

Cadence preferences and optional compression are Minor unless they change the
reader's understanding of evidence or conclusion. Do not rewrite the essay
wholesale.

## Output

Write exactly one new file:

`successor/dev/ESSAY_POST_RECONCILIATION_STRUCTURAL_REVIEW_OPUS_RESPONSE_V1.md`

Include these literal advisory answers before the terminal:

```text
NEGATIVE_SPACE_PRESERVED=YES|NO
LEDGER_SERVES_ARGUMENT=YES|NO
REVIEW_STOP_RULE_COHERENT=YES|NO
REENTRY_PLAN_IS_ACTIONABLE=YES|NO
```

End with exactly one:

```text
ACCEPT_ESSAY_POST_RECONCILIATION_STRUCTURAL_V1
REVISE_ESSAY_POST_RECONCILIATION_STRUCTURAL_V1
BLOCKED_ESSAY_POST_RECONCILIATION_STRUCTURAL_V1
```

Use `REVISE` only for a concrete Critical/Major defect in the current essay.
Plan criticism alone does not revise the essay.
