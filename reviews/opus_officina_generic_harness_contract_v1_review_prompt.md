# Opus X-line: generic harness contract v1 review

Work read-only in `/home/master/llm_projects/philosophia`. Review:

- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`
- `reviews/fable_officina_generic_harness_contract_v1_closure.md`

against the signed activation protocol v1+v2+v2.1, WP-3/WP-4 boundaries, and
current inactive schemas. This is one bounded engineering-contract X-line
review. Do not implement, edit, commit, create a manifest, or activate T.

Audit for bit-exact implementability by Cursor and for contradictions that would
make two independent implementations diverge. In addition to the four X-line
questions in Fable's closure, attack:

1. every global/process transition, especially claim/start/lease ordering,
   final charge, process record, and `T_PROCESS_STOPPED`; reject any circular
   record/event hash dependency or event-before-record inversion;
2. every crash cut: distinguish safe deterministic completion from a route that
   requires signed recovery; verify "ledger authority" does not silently repair
   a hash-chain/head/cache inconsistency contrary to record-first invalidity;
3. capability issuance/revocation and settle-before-release under process death,
   watchdog races, backend work, multiple streams, and power-off;
4. whether all proposed new objects (release token, quiescence proof, draft
   manifest, adapter) are genuine implementation clarifications rather than
   unsigned schema/policy amendments;
5. whether the proposed module/API breakdown is sufficiently exact for Cursor,
   including ownership of supervisor state, durable paths, fake-vs-production
   types, and transaction boundaries;
6. production call-graph roots and extension points after the final C4 verifier
   repair, without pinning implementation hashes now;
7. absence of any executable authority or scientific/learner choice in the
   draft.

Write exactly one file:
`reviews/opus_officina_generic_harness_contract_v1_review.md`.

First line must be exactly one token:

- `OFFICINA_GENERIC_HARNESS_CONTRACT_XLINE_ACCEPTED`; or
- `REVISE_OFFICINA_GENERIC_HARNESS_CONTRACT_XLINE`; or
- `BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT_XLINE`.

If revision is required, give a finite mandatory repair list and exact
replacement text or tables where possible. A positive review authorizes only
Kirill's later contract signature after the Y-line also accepts; it authorizes
no implementation or activation.

