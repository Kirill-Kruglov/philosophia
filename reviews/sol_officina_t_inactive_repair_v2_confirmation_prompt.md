# Y-line prompt: Officina T inactive repair v2 confirmation

You are GPT-5.6 Sol acting as the statistical/governance Y-line. Work read-only
in the local `philosophia` repository. Do not edit, commit, activate, generate a
manifest or harness, issue a capability, or create any runtime artifact.

Review the bounded repair commit `2277331` against its parent `2d0cc0b` and
against your reproduced residuals C1-C4 in:

- `reviews/sol_officina_t_inactive_repair_confirmation.md`
- `reviews/opus_officina_t_inactive_repair_confirmation.md`

The review is confirmation-only. Do not reopen signed scientific cells or the
activation-protocol design unless the repair itself creates a concrete new
Critical/Major contradiction. The real tree must remain `NOT_ACTIVATED`.

## Required adversarial checks

1. **C1, pre-WP-6 E2:** independently attempt direct active `TState`
   construction and `from_mapping` with nonempty `candidate_ids`; verify
   `exhausted`, reservation routing, and `validate_ledger_event` cannot create
   or interpret E2 consumption. Only the signed E1 cap may exhaust T.
2. **C2, closed process composition:** verify `build_active_lease` and
   `build_process_record` require the exact activation-record hash and immutable
   control map. Re-run both original cross-kind probes. Verify a valid close is
   backed by its process-specific `T_DEVICE_TIME_CHARGED`; an invalid close
   additionally requires the immediately following hash-linked
   `T_RUNTIME_INVALID`, matching public cause, canonical invalidity-record hash,
   state, liability, observation time, process/lease identity, and activation
   identity. Confirm the signed v1 process-record key set was not changed.
3. **C3, reviewed-commit provenance:** in disposable mirrors reproduce both
   remove-at-reviewed-HEAD/restore-at-authorization cases, one governing file
   and one protocol file. Both must refuse before claim creation. Confirm the
   check covers the union of reviewed source, governing, and protocol paths.
4. **C4, closed local graph:** without executing reviewed sources, reproduce an
   arbitrary repository-root module importing an omitted local helper that
   names a test-world symbol. Verify omitted dependencies, ambiguous local
   resolution, an undeclared executable root, and unreachable asserted sources
   all refuse. Confirm the manifest is compared to graph reachability from the
   three exact roots, not to the caller's entire reviewed list, and quarantine
   checks cover every reachable source.
5. Run the focused suite, full suite, inheritance/decision verifiers,
   `verify_officina_wp12.py`, and the active verifier. The last must fail only
   because production authorization is absent. Confirm `runtime/` contains only
   `T_RUNTIME.lock` and no harness/manifest/authorization/output was created.

## Verdict and output

Write exactly one new file:
`reviews/sol_officina_t_inactive_repair_v2_confirmation.md`.

Use exactly one verdict token as its first line:

- `OFFICINA_T_INACTIVE_REPAIR_V2_CONFIRMED`, only if C1-C4 are all closed; or
- `REVISE_OFFICINA_T_INACTIVE_REPAIR_V2`, with a minimal reproducible blocker;
  or
- `BLOCKED_OFFICINA_T_INACTIVE_REPAIR_V2`, only for an external impossibility.

A positive verdict opens only the generic metered-harness scope/design gate. It
does not authorize implementation, a production manifest, activation,
execution, entropy, E1/E2/E3 spend, T/Q/C data, or scientific interpretation.

