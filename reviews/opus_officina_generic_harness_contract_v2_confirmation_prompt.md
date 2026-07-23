# Opus 4.8 X-line: Officina generic harness contract v2 confirmation

Work read-only in `/home/master/llm_projects/philosophia`.

Confirm the complete replacement:

- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`
- `reviews/fable_officina_generic_harness_contract_v2_closure.md`

against your v1 review:
`reviews/opus_officina_generic_harness_contract_v1_review.md`, the signed
activation protocol v1+v2+v2.1, WP-3 signature, WP-4 inactive boundary, and the
current immutable verifier roots. This is the single bounded confirmation
allowed by the governance rule; it is not a new design round.

Required confirmation:

1. Audit every `C-1..C-4` and `R5..R12` disposition one-to-one. In particular,
   verify record-before-event ordering, INVALID record construction, no-process
   invalidity, sibling settlement, the exact three-case recovery charge,
   initial charge-hash seed, and the sole permitted idempotent cache successor.
2. Verify the global known/unknown concurrent settlement and terminal dominance
   are total, conserving and single-valued, including known overrun, zero-share
   after crossing, simultaneous E1/E3, and infrastructure-invalidity dominance.
3. Verify the roots/CLI/import/ownership contract matches the pinned boundary:
   exactly the existing three roots, `generic_harness.__main__`, no new script,
   static adapters, exact durable writer/issuer ownership, fake-type exclusion.
4. Verify isolation-and-promotion, pause/resume, recovery disposition and every
   crash cut are implementable without result leakage, silent retry, tenth
   event, Git safety precondition, or uncharged behavior-capable interval.
5. Decide whether the compatibility table honestly contains only inherited
   signed rules and deterministic implementation clarifications. Name a
   protocol amendment only if a concrete v2 clause cannot be derived from the
   signed protocol; do not reopen a resolved stylistic alternative.
6. State whether two independent implementers can derive identical terminal
   classifications, charges, artifact ordering and admission decisions. List a
   concrete ambiguity only if it changes one of those outputs.

Run read-only consistency checks as useful. Do not edit code, implement the
harness, create a manifest/authorization/runtime artifact, activate T, or spend
resources.

Write exactly one file and change nothing else:
`reviews/opus_officina_generic_harness_contract_v2_confirmation.md`.

First line exactly one token:

- `OFFICINA_GENERIC_HARNESS_V2_XLINE_CONFIRMED`; or
- `REVISE_OFFICINA_GENERIC_HARNESS_V2_XLINE`; or
- `BLOCKED_OFFICINA_GENERIC_HARNESS_V2_XLINE`.

A positive verdict authorizes only Kirill's informed contract signature. It
does not authorize implementation or activation.
