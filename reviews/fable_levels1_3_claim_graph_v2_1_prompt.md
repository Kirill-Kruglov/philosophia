# Fable 5 bounded correction: claim graph v2.1

Perform one narrow correction pass on
`reviews/fable_levels1_3_claim_graph_v2.md`. Preserve v1 and v2 unchanged as
review artifacts. Do not redesign accepted science, write code, choose numeric
thresholds, create a lock/scout/escrow, or predict outcomes.

Read the v2 prompt and v2 response, plus the formal Opus/Sol reviews. Write the
corrected document to `reviews/fable_levels1_3_claim_graph_v2_1.md`.

## Six mandatory corrections

### 1. Emit the required verdict

v2 did not use any verdict token required by its prompt and substituted
`CLOSED_FOR_SIGNATURE`. Use exactly one of the original allowed verdicts:

- `READY_FOR_LEVEL1_SPEC`
- `REVISE_CLAIM_GRAPH_AGAIN`
- `BLOCKED_LEVEL1_ENDPOINT`
- `REJECT_YOKED_DESIGN`

A status such as `CLOSED_FOR_SIGNATURE` may be secondary but cannot replace
the verdict.

### 2. Make the C4 cascade executable and exclusive

v2 says the order is exclusive but lists weights-only and inherited-ledger
branches before their joint branch, making the joint branch unreachable under
literal sequential evaluation. Define all locked predicates first, then use an
explicit priority that evaluates the joint predicate before either component.

Because equivalence is not transitive, also state the priority if the placebo,
weights, or inherited-ledger predicates overlap under their locked intervals.
Evidence for a content-bearing weights channel must not be erased by a
ledger-form placebo overlap. Any incoherent/non-classifiable interval pattern
must route to `INSUFFICIENT`, not be resolved by narration.

Replace the directionally incorrect phrase "E not greater than B,
margin-locked non-inferiority" with a precise **non-superiority upper-bound**
condition on one consistently oriented benefit scale. Define once that larger
benefit means lower budget-to-certified-solve / better performance, and use
that orientation for every A-E `>`, `~=`, and margin in the truth table.

### 3. Replace the incomplete contact-mode table with a total rule

v2 does not cover outcomes where RANDOM-STATIC is superior to ACTIVE, including
`RANDOM > ACTIVE > YOKED`. Replace case fragments with an exhaustive selection
procedure over all three arms on the locked primary benefit scale:

1. invalid or unresolved required comparisons -> Level 2 blocked;
2. if one arm is uniquely superior to both others -> select it;
3. if a set of arms is mutually equivalent at the locked margin and jointly
   superior/non-inferior to the remainder -> select the least adaptive member
   by the preregistered priority `RANDOM-STATIC`, then `YOKED-GEOMETRY`, then
   `ACTIVE`;
4. non-transitive, cyclic, or otherwise unclassified simultaneous intervals ->
   `INSUFFICIENT`, Level 2 blocked.

State separately how C1 is read from ACTIVE versus YOKED; contact-mode
selection must not rewrite the C1 estimand. Include RANDOM-superior anomaly
reporting. The resulting procedure must truly map every statistically
classifiable three-arm result to exactly one mode.

### 4. Move equivalence margins before comparative data

v2 places N6 after the comparative scout and says `N3 + N6-L1 from scout
precision logic`. This is not allowed. An equivalence/non-superiority margin is
the minimum scientifically meaningful effect, not a sampling-variance output.

For each level:

- endpoint, benefit orientation, comparison family, N6 margins, and interval/
  test rules freeze at the S-gate **before any comparative scout**;
- justify N6 from the scientific claim, external anchors, or a declared
  conservative bound, never observed arm differences;
- the comparative scout may estimate variance, censoring, feasibility, and the
  block count/precision rule only;
- N3 follows the Level 1 scout;
- N4 follows a distinct Level 2 development calibration after the five-arm
  endpoint/contrasts/N6-L2 are frozen. The Level 1 scout cannot estimate N4.

Correct §5, §7, the unresolved-numerics note, and S2/S5 accordingly.

### 5. Make the donor variance unit operational

With disjoint one-to-one donors, define each inferential block as the evaluated
target world plus its uniquely assigned donor transcript/world. Blocks must be
disjoint across the primary analysis. Explain whether assignment randomization
is used for design balance, an exact test, or a sensitivity analysis; do not
claim randomization inference can observe unrun counterfactual YOKED training
trajectories. If one assignment is realized, ordinary block-level inference is
allowed only under the declared independent-block sampling model, with the
assignment-conditioned scope stated. Seeds remain repeated measures.

### 6. Replace fictional AI key custody with an honest escrow role

Gemini, Grok, and a local llama process can serve as a clean-room **generator/
witness**, but not as a persistent second cryptographic key holder. Replace S6
with an operational choice:

- name the clean-room generator;
- it receives the locked generator contract and a precommitted public key,
  generates once, returns only ciphertext + plaintext hash + generation
  attestation, and does not expose plaintext in the research chat;
- Kirill holds the decryption key under an explicitly procedural escrow threat
  model; or a real named human/service is separately designated as key holder;
- do not claim cryptographic independence from Kirill when none exists;
- malformed generation still ends the holdout.

Make S6 an acceptance/naming line that describes the chosen generator and
custody threat model, not `Kirill + AI room` key custody.

## S1 wording correction

The essay literally makes C6-null survival a condition of its current Proof
paragraph. Removing it from the conjunct is scientifically justified by R5,
but is an explicit authorial amendment, not merely an annotation clarification.
