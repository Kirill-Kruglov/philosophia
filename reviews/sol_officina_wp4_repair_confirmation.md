REVISE_OFFICINA_WP4_R1_R2_REPAIR

# Bounded conclusion

The three-file delta `3132f79..7786137` closes the original raw-ledger/state/envelope API and removes factory-issued Q/C capabilities, but two use-time counterexamples remain. The repair therefore does not yet establish the exact R1/R2 boundary. Both defects admit bounded corrections without choosing a WP-3/WP-6/WP-9 cell or creating a production execution surface.

# Findings

## Critical

None.

## Major

1. **A valid post-issuance ledger/head substitution can survive the stored inode check.** `src/philosophia/officina/world.py:128-129,136-138` stores only `(st_dev, st_ino)` after initialization. The issued files are then closed. On the reviewed filesystem, unlinking and recreating each path immediately reused both inode numbers. Replacing the two files with the bytes of a separately valid one-entry ledger/head therefore passed the path, symlink, inode, protected-alias, and `entries()` integrity checks at `world.py:186-199`.

   I reproduced this wholly under a pytest-style temporary directory. The stored and replacement identities were identical, and `_require_test_contact_harness(harness)` accepted a substituted ledger whose sole entry was `FORGED_TEST_ENTRY`. No committed artifact was opened for writing or changed. This is not scientific evidence and cannot reach production T, but it falsifies the required claim that the fresh harness history cannot be substituted after issuance. The committed tests at `tests/test_officina_world.py:176-235` cover pre-issuance aliases and ordinary-object refusal, not this post-issuance valid replacement.

2. **An issued T capability can be relabelled Q or C and is not revalidated at use.** The constructor rejects non-T surfaces at `src/philosophia/officina/world.py:69-75`, but the consumer guard at `world.py:202-208` checks only exact class, token, and purpose. A caller needs no private token:

   ```python
   cap = test_world_capability(Surface.T, capability=test_cap, purpose="probe")
   object.__setattr__(cap, "surface", Surface.Q)
   evaluate_test_query(capability=cap, modulus=28, raw_query=valid_query)
   ```

   The frozen dataclass does not prevent `object.__setattr__`. My non-outcome probe stopped before query evaluation but confirmed that the relabelled exact object passes `_require_world_capability` and that modulus 28 is admitted by the resulting surface set. The same route applies to `Surface.C`; relabelling to `Surface.TEST` also falls through `_surface_moduli`'s non-Q branch to the C set at `world.py:327-341`. Thus the factory refusals tested at `tests/test_officina_world.py:117-123` do not establish that no source callable can use a Q/C-labelled test capability for an oracle answer.

## Minor

None.

# Exact bounded repairs

R1. Retain a non-reusable store-issued identity anchor for the root, ledger, and head (for example, held directory/file descriptors) and validate the actual opened objects used by the operation, not only a pathname's recyclable `(st_dev, st_ino)`. The verified ledger descriptor must be the object appended to, or `AppendOnlyLedger` must validate the opened descriptor against the held identity before any write. When the head is atomically replaced, retain the old anchor until the new head is opened, integrity-checked, and installed as the harness's next anchor. Recheck outside-repository location, nonsymlink status, protected aliases, and full ledger/head integrity before admitting each contact. Add a deterministic regression that replaces both issued files with a different, internally valid ledger/head and requires refusal even when inode numbers are reused; keep the direct, relative, symlink, hard-link, and committed-genesis checks.

R2. Make `_require_world_capability` require `capability.surface is Surface.T` at every use, with a T-only refusal. Add regressions that relabel a genuinely issued capability via `object.__setattr__` to each of `Surface.Q`, `Surface.C`, and `Surface.TEST`, then require refusal before `evaluate_test_query` can classify or answer any query. No Q/C modulus or root design needs to be added.

# Direct answers to the bounded questions

1. **API ownership:** Partly confirmed. `record_test_t_contact` at `world.py:410-418` now accepts only an exact issued `TestTContactHarness`; its factory owns the ordinary `AppendOnlyLedger`, internally activated fake `TState`, and default `TEnvelope` at `world.py:112-129`. Ordinary caller-supplied production-compatible ledger/state/envelope arguments no longer exist. Major finding 1 prevents the stronger durable-ownership conclusion after issuance.

2. **Factory and path boundary:** The factory requires an exact test-only capability, an absolute canonical nonsymlink directory outside the repository, and absent ledger/head paths before initialization (`world.py:147-183`). Direct repository roots, relative roots, symlink roots, and pre-existing ledger/head hard links are refused. Each contact invokes location, symlink, stored-inode, protected-alias, and integrity checks before its pure evaluation/charge/append sequence (`world.py:186-199,421-448`). Sequential symlink and protected hard-link substitutions are refused, and in-place malformed content fails integrity. The valid unlink/recreate counterexample in Major finding 1 remains. The committed envelope, ledger, and external head were byte-identical after all probes and suites.

3. **Returned state:** Confirmed. The return is exact `TestTContactState`, carries `test_only=True`, and exposes only device nanoseconds and purpose (`world.py:89-95,452-459`). It is not a `TState`; no checkpoint, activation, timer, registration, or production transaction accepts it or is introduced by this delta.

4. **Q/C pre-root boundary:** Not confirmed because of Major finding 2. Absent relabelling, the factory is T-only, T rejects all selected-frame moduli, the frame Q/C sets remain deterministic definitions, and `launch_q`/`execute_c` remain fail-closed (`tests/test_officina_world.py:105-123`). The use-time validator nevertheless trusts the mutable public `surface` field.

5. **Artifact admission:** Confirmed for the current `ArtifactStore` surface. The regression at `tests/test_officina_world.py:238-261` gives the response explicit test-only provenance and Q/C admission refuses it. Static inspection found no public store method that can turn that source into a promotable artifact: native records require exact external-registry provenance, `promotable` must be false, derived writes preserve parent-source union, and engineering fixtures are T-only (`src/philosophia/officina/provenance.py:129-219,221-282`; `quarantine.py:59-63,86-107`). Major finding 2 is a pre-provenance oracle-capability bypass, not a successful `ArtifactStore.admit` laundering route.

6. **Scientific cells:** Confirmed unchanged. The load-bearing delta is exactly `world.py`, `tests/test_officina_world.py`, and `successor/OFFICINA_WP4_IMPLEMENTATION.md`. It changes no signed frame constant or member, construct classifier/answer, transport premise, selected token, future root design, estimator, endpoint, or scientific claim. `7786137..HEAD` is empty for those three files.

7. **Checks and genesis:** I ran:

   ```text
   .venv/bin/python -m pytest -q \
     tests/test_officina_world.py \
     tests/test_officina_bootstrap.py \
     tests/test_officina_governance.py \
     tests/test_officina_accounting.py
   65 passed in 2.25s

   .venv/bin/python -m pytest -q
   232 passed in 25.52s

   .venv/bin/python scripts/verify_officina_wp12.py
   OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.

   git diff --check 3132f79..7786137
   passed
   ```

   After the committed suites and temporary adversarial probes, `git diff --exit-code` reports no change to `successor/officina/T_ENVELOPE.json`, `T_LEDGER.md`, or `T_LEDGER.md.head.json`. The envelope remains `activated:false`; the ledger remains the exact `NOT_ACTIVATED` header with no entry; the external head remains count 0 with the all-zero genesis hash.

# Boundary and negative space

This verdict authorizes only bounded repair of the two findings and another focused confirmation. It does not authorize preparation of a T-activation candidate.

I created no real world, production capability, entropy, frame realization, sample, panel, candidate, production root, committed ledger event, T activation, E1/E2/E3 spend, learner run, Q attempt, Q/C execution, competence binary, `H_preC` update, lock, escrow, scientific datum, outcome, or claim movement. The only created objects were temporary test capabilities and ledgers under temporary storage; the capability probe produced no oracle answer. T remains at pristine genesis and `NOT_ACTIVATED`. No qualification, contrast direction, or programme outcome is predicted.
