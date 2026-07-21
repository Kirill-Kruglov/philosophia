# Claude Opus 4.8 X-line: Officina T inactive implementation review

Work in `/home/master/llm_projects/philosophia` at implementation commit
`77c5a63`. Review the implementation against the accepted protocol chain:

- `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V1_DRAFT.md`
- `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md`
- `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_1_CORRECTION.md`
- `reviews/opus_officina_t_activation_protocol_v2_1_final_confirmation.md`
- `reviews/sol_officina_t_activation_protocol_v2_1_final_confirmation.md`

Primary implementation surface:

- `src/philosophia/officina/activation.py`
- `src/philosophia/officina/runtime.py`
- `src/philosophia/officina/{accounting,canonical,checkpoint,interlock,ledger,terminal,verification,world}.py`
- `scripts/officina_activate_t.py`
- `scripts/verify_officina_active.py`
- `scripts/verify_officina_wp12.py`
- `successor/officina/T_ACTIVATION_IMPLEMENTATION.md`
- `successor/officina/runtime/T_RUNTIME.lock`
- `tests/test_officina_activation.py`
- `tests/test_officina_runtime.py`

Create exactly one new file:

`reviews/opus_officina_t_inactive_implementation_review.md`

Do not edit, commit, activate T, create an authorization, create a real world,
start a process/lease, or spend E1/E2/E3. Positive activation tests may run only
as already written in disposable temporary git mirrors.

Audit adversarially:

1. Re-derive the authorization/claim/state/record schemas, canonical path set,
   source/governing/protocol hash pins, exact-stage activation commit, and
   claim-before-mutation failure routing. Identify every field/type mismatch or
   ambiguous v1/v2/v2.1 carry-forward interpretation.
2. Verify that the authorization commit may be newer than
   `reviewed_code_head` while the reviewed source diff stays empty, and that no
   unreviewed source can reach activation.
3. Attack the held-descriptor runtime lock, ledger/head/state derivation,
   atomic-create/replace ordering, symlink/hardlink/path substitution, partial
   transaction, stale index/worktree, and active/inactive verifier split.
4. Audit the closed nine-event vocabulary and the requirement that every
   state-bearing event contains a complete post-state. Check the checkpoint
   change against existing pause/resume semantics.
5. Hand-check E1/E3 reservation arithmetic at ordinary, concurrent, shortened,
   simultaneous-zero, and overshoot boundaries. Check that one concurrent
   behavior-capable stream equals one unit and that four is the global cap.
6. Recompute process-id inputs and inspect claim -> lease -> settlement -> final
   record validation for mutation, replay, bool/int confusion, clock rollback,
   reboot identity, duplicate sequence/id, and public scientific fields.
7. Attack the static production/test boundary, including aliases, indirect
   imports, dotted imports, reflection, and omitted reviewed paths. Determine
   whether a test-only world route can enter production.
8. Decide explicitly whether the absent supervisor/backend-quiescence adapter
   and concrete generic learner harness are correctly and mechanically deferred
   to the separately required harness review, or whether current code wrongly
   claims a runtime contract it cannot yet enforce.
9. Run the focused and full test/verifier suites. State exact counts and any
   untested load-bearing path. Confirm that the real tree contains only the
   reviewed immutable lock and remains `NOT_ACTIVATED`.

Lead with exactly one verdict:

- `OFFICINA_T_INACTIVE_IMPLEMENTATION_ACCEPTED`;
- `REVISE_OFFICINA_T_INACTIVE_IMPLEMENTATION`; or
- `BLOCKED_OFFICINA_T_INACTIVE_IMPLEMENTATION`.

Findings must be ordered Critical/Major/Minor with file:line references and
minimal exact repairs. A positive verdict authorizes only the next generic
metered harness design/implementation gate. It does not authorize an activation
candidate, activation, entropy, a real T world, learner execution, lease, E1/E2/E3
spend, breathing check, Q/C, or any scientific interpretation.
