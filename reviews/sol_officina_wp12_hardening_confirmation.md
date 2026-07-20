REVISE_OFFICINA_WP12_HARDENING

# Bounded answer

No. The exact diff `c6a41b2..6b6d55d` closes substantial parts of the prior
review, but it does not close every Critical and Major WP-1/WP-2 blocker. The
remaining failures are reproducible without entropy, a world, a model, or a
scientific execution. They are confined to the hardening surfaces and require
no choice of a deferred WP-3/WP-4/WP-6/WP-9 cell.

The repository is currently at `955ecca12b8293fd6bb68c8cc30cf83a5ab15abe`.
Its committed delta from `6b6d55d22be506e5bedab014098015a79d76dacb`
contains only the two hardening-review prompts; the load-bearing files match the
requested hardening commit.

# Findings

## Critical

1. **The one-shot transition table still permits an uncharged close after the
   entropy boundary.** `record_pre_entropy_disposition()` delegates directly to
   `_append(TERMINAL, ...)`. `_append()` permits `TERMINAL` after each of
   `CLAIMED`, `DRAW_ARMED`, and `LAUNCHED`, but does not couple the payload kind
   to the predecessor phase. Consequently both of these public sequences
   succeed:

   ```python
   j.create_claim("a" * 64)
   j.arm_draw("future-root")
   j.record_pre_entropy_disposition(signature_id="shape", reason="after-arm")
   ```

   and:

   ```python
   j.create_claim("a" * 64)
   j.arm_draw("future-root")
   j.record_launch_commitment("b" * 64)
   j.record_pre_entropy_disposition(signature_id="shape", reason="after-launch")
   ```

   Each persisted `charged:false`, competence-unset
   `PRE_ENTROPY_STOP`. This defeats the signed first-byte/ambiguous-draw charge
   partition. The existing test checks only the intended `CLAIMED` path and
   misses both transitions.

   The journal's Q terminal is also not runtime-typed. After `LAUNCHED`, an
   arbitrary object with a `validity` attribute and a malicious `to_mapping()`
   is accepted by `record_q_terminal()`. The probe persisted a mapping that
   simultaneously said `Q_INVALID`, `competence:true`, `PROCESS`, and contained
   an extra field. Thus the closed `QTerminal` constructor can be bypassed at
   the journal boundary.

   **Smallest bounded repair:** make the central transition validator operate
   on a typed event kind, predecessor phase, and exact payload schema.
   `PRE_ENTROPY_STOP` must require predecessor exactly `CLAIMED`;
   `DRAW_ARMED -> TERMINAL` must require a canonical round-trip
   `QTerminal(Q_INVALID, None, cause)` and `charged:true`; and every
   `LAUNCHED -> TERMINAL` must require an exact `QTerminal` and
   `charged:true`. Require `type(terminal) is QTerminal` or reconstruct it with
   `QTerminal.from_mapping()` before persistence. Add negative tests for the
   pre-entropy method after `DRAW_ARMED` and `LAUNCHED`, arbitrary terminal
   objects/subclasses/mappings, extra fields, and contradictory competence.
   Keep entropy, caps, alpha, and Q numerics absent.

2. **An overdue resume still exposes a work-admitting state, and resume time can
   precede the pause.** `ResumeGate.admit_work()` correctly refuses when
   `review_required` is true, but the public `ResumeGate.state` is the same
   active `TState`; its public `charge_device_nanoseconds()` and
   `register_candidate()` methods remain usable. The following succeeded while
   `gate.review_required` was true:

   ```python
   charged = gate.state.charge_device_nanoseconds(
       NANOSECONDS_PER_HOUR, TEnvelope()
   )
   ```

   In addition, a pause ledgered at `2026-07-20T08:00:00Z` was accepted by
   `verify_resume(..., timestamp_utc="2026-07-20T01:00:00Z")`; it returned
   `review_required=False` and `admit_work()` succeeded. Neither the ledger nor
   resume verifier enforces monotone timestamps or `resume >= pause`.

   **Smallest bounded repair:** carry a serialized `resume_review_pending`
   state (or an equivalent opaque work-admission capability) such that the raw
   resumed state itself rejects charge, registration, and future real-T access.
   Clear it only in the same durable operation that appends the completed E3
   review. Validate `pause >= activation/last review`, `resume >= pause`, and
   `review completion >= resume`, and enforce monotone canonical UTC timestamps
   in the relevant ledger transitions. Add direct-bypass and time-travel tests.
   This is a WP-2 state-machine repair, not selection of WP-4's real metering
   implementation.

3. **Durable provenance remains forgeable even though path admission is
   conservatively denied.** The new store correctly rejects missing metadata,
   copied metadata at a different path, content mutation, `promotable:true`
   metadata, fixture Q/C reads, undeclared paths, and symlink escape. Direct
   path-based `ArtifactStore.admit()` is therefore fail-closed under the current
   no-promotion regime.

   Two required attacks nevertheless succeed:

   - A caller holding one genuine `TaggedArtifact` can read its `_token` and
     invoke the public `TaggedArtifact` constructor with an arbitrary certified,
     promotable label. `forged.label.require_promotable(Surface.Q)` then passes.
     The token is a shared object carried on every returned artifact, not a
     non-transferable issuance fact.
   - Provenance JSON has only a recomputable self-hash. Relabeling an in-place
     fixture-derived record from `engineering-fixture` to `test-only-native`,
     deleting its parent hashes, and recomputing `provenance_sha256` is accepted
     by `ArtifactStore.read()`. The observed reopened sources were
     `("test-only-native",)` rather than the true fixture ancestry. This remains
     non-promotable, but it breaks the promised durable parent/source
     provenance and can manufacture a store-issued parent from forged metadata.

   **Smallest bounded repair:** make promotability structurally impossible in
   the WP-1/WP-2 label type (there is no promotion authority yet); make the
   tagged implementation private and validate parent object identity against a
   store-maintained issuance table, or accept parent paths and re-read them
   instead of trusting caller-carried tokens; and bind each metadata record and
   its exact parent/source union into an append-only provenance registry with an
   externally checked head. Reopen must verify the registry entry and recursively
   verify the recorded parents, not merely a self-hash. Add tests for token
   copying, `dataclasses.replace`, same-path relabel/re-hash, parent deletion,
   forged empty parents, and a hand-built metadata record. No promotable or
   production artifact type should be added by this repair.

## Major

4. **The PRF key boundary is bypassable through two public routes.** Typed
   domain tags now separate integer `1` from string `"1"`; supported boundary
   encodings are distinct; and booleans are rejected as domain components.
   No production or sealed-root class was added. However:

   - `prf_digest()` performs no runtime key validation. An arbitrary object
     having `material=b"x" * 32` is accepted and returns a digest.
   - A genuine dummy key exposes `_token`; passing that token to the public
     `TestOnlyKey` constructor creates a different accepted key with arbitrary
     caller-chosen material. `CounterStream` accepts it.

   Therefore the internal dummy factory is not the only way to produce an
   accepted PRF key.

   **Smallest bounded repair:** centralize an exact runtime
   `require_test_only_key()` check and call it from `prf_digest`,
   `CounterStream`, and every helper. Return a private opaque key implementation
   from `dummy_key`; do not expose a reusable authority token or a public raw-
   material constructor. Add the fake duck-typed object and copied-token cases
   as negative tests, plus exact-integer checks for counters. Do not add a
   production/sealed-root key type before WP-6.

5. **The verifier is stricter but still misses an indirect entropy route and
   does not verify exact ledger genesis bytes.** Direct and aliased imports,
   direct entropy calls, dynamic imports, unreviewed imports, exact manifest
   values/types, and the external genesis-head object are now checked. Two
   probes still returned an empty failure list:

   ```python
   import os
   draw = getattr(os, "urandom")
   value = draw(32)
   ```

   and a repository copy whose `T_LEDGER.md` explanatory genesis sentence was
   changed while retaining `Status: NOT_ACTIVATED` and no entry line.
   `verify_bootstrap()` uses substring checks rather than exact `HEADER` bytes,
   and the AST scanner permits reflective access through an otherwise allowed
   module. Similar reflection through `getattr(importlib, "import_module")` and
   reads of `/dev/urandom` are not closed by the present call-name set.

   **Smallest bounded repair:** require the committed ledger bytes to equal the
   canonical inactive `HEADER` exactly and its head to equal the canonical
   genesis payload. Add field/type mutants for the head and byte mutants for
   every ledger section. For source verification, reject reflective/dynamic
   execution constructs (`getattr` on import/entropy-capable modules,
   `eval`/`exec`/`compile`) and constant accesses to system random devices, or
   enforce an exact reviewed-source hash allowlist in addition to the import
   allowlist. Add each missed form as a negative test. The verifier remains
   engineering assurance, never scientific evidence.

# Closed cells

The following prior blockers are correctly closed and must not be reopened by
the bounded repairs:

- T-state mappings now require exact keys and types; inactive T is exactly
  pristine; inactive pause and false inactive maintenance are refused.
- Pause checkpoints now recompute canonical artifact paths and hashes; missing,
  mutated, deleted, and substituted artifacts fail closed. Checkpoint/ledger
  linkage, `resets_e3:false`, stale checkpoints, partial entries, and ordinary
  suffix deletion are checked against external heads.
- `CScientificTerminal` is a closed enum; strings, T/pause labels, Q labels,
  invalid causes, and invalid C scientific fields are rejected. `QTerminal`
  itself is exact and validity-first; only the journal adapter remains open as
  finding 1 states.
- The attempt registry records attempt IDs and journal heads, detects ordinary
  suffix deletion and persistence ambiguity, and blocks serial ID reuse. The
  payload/phase coupling defect is narrower than the registry design.
- Candidate identity removes only `provenance_commit` and the closed
  `inert_metadata` class. Behavior source, stack, from-scratch initialization,
  optimizer, policy, interface, config, and schema remain load-bearing;
  unknown top-level or inert fields are rejected.

# Deferred cells and scope

The hardening diff does not instantiate a finite frame, construct, frame member,
partition, inclusion probability, weight, FPC, learner-seed scope, real-T clock
or process meter, production root, entropy source, Q predicate, cap, alpha,
competence numeric, C endpoint, margin, sample size, lock, escrow secret, world,
registered candidate, trajectory, scientific datum, or outcome. The generic C
terminal enum is the already-authorized validity taxonomy, not a selected C
endpoint. The committed T ledger remains inactive at genesis.

Accordingly, WP-3 population objects, WP-4 real metering and harness details,
WP-6 entropy/custody/Q-family/breathing-check numerics, and WP-9 scientific
fields remain correctly deferred. None of the repairs above may choose them or
add a real execution capability.

# Checks run

- `.venv/bin/python -m pytest -q tests/test_officina_bootstrap.py tests/test_officina_governance.py tests/test_officina_accounting.py` — **38 passed**.
- `.venv/bin/python scripts/verify_officina_wp12.py` — **OK**.
- `git diff --check c6a41b2..6b6d55d` — passed.
- `git diff --exit-code 6b6d55d..HEAD` over the load-bearing Officina,
  bootstrap, test, verifier, CI, package, and README paths — passed.
- Bounded `/tmp` probes reproduced the two uncharged one-shot transitions, the
  arbitrary Q-terminal mapping, overdue-state bypass, pre-pause resume, fake
  PRF object, copied PRF token, copied provenance token, same-path provenance
  relabel/re-hash, indirect `getattr(os, "urandom")`, and mutated-ledger-genesis
  acceptance described above.

The passing committed tests cover their intended positive and negative cases;
they do not negate these independent counterexamples.

# Disposition and negative space

WP-1/WP-2 may not yet be closed, and this review does not open WP-3. After only
the bounded repairs above, the exact repair diff requires another focused
Y-line confirmation. On confirmation, WP-1/WP-2 may be closed and WP-3 may be
drafted only; no real world may be generated.

This review created only this review file and did not commit. It created no real
entropy, world, learner/model run, T activation, real candidate registration,
real Q attempt or execution, promotion, scientific specification, lock, escrow
secret, C execution, trajectory, comparative datum, scientific datum, outcome,
or claim movement. Temporary test-only journals and dummy files used by the
mandated tests and bounded counterexamples were confined to pytest temporary
directories or `/tmp` and were removed. No existing file, including
`essay/OUTLINE.md` and the pre-existing prompt-header change, was modified.
