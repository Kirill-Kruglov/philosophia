REVISE_OFFICINA_WP12_IMPLEMENTATION

# Findings

Reviewed object: exact load-bearing diff `d3be92f..2de1df5`, against
`successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md` and the bounded X/Y selection
reviews. Current HEAD is `614771be72630e932895086ab1723db0a2da8d5f`; its
delta from `2de1df5` consists only of the two review-prompt files. The Officina
bootstrap, source, tests, verifier, CI, packaging, and README surfaces are
byte-identical to the requested implementation anchor.

## Critical

1. **Fixture non-promotion is a voluntary in-memory label, not an enforced
   provenance boundary.** `PathPolicy.read_bytes()` correctly returns a
   non-promotable label for a hash-pinned T-only fixture, and
   `ArtifactLabel.derived()` propagates that label when a caller elects to use
   it. But a caller can write those bytes under `successor/officina/`, reopen
   the file, and receive a fresh `ArtifactLabel.native()` with
   `promotable=True`. No write API binds parent labels to a durable artifact,
   and no Q/C admission API rejects missing or laundered provenance. The test
   proves label arithmetic, not the required dataflow boundary. This fails the
   signed WP-1/WP-2 obligation that engineering fixtures be mechanically
   non-promotable.

   **Mandatory repair before WP-1/WP-2 closure:** mediate artifact writes as
   well as reads; require every derived write to carry all parent labels; bind
   the resulting provenance to the content hash in canonical durable metadata;
   and make every future Q/C admission check fail closed on absent, mismatched,
   or non-promotable provenance. Add negative tests for fixture copy-and-reopen,
   attempted relabeling, derived-file mutation, missing provenance, direct
   Q/C admission, symlink escape, and undeclared paths. The committed fixture
   list may remain empty.

2. **The pause checkpoint does not authenticate the state that must be
   resumed, and an overdue E3 review does not block work.**
   `write_pause_checkpoint()` accepts caller-asserted 64-character artifact
   hashes without paths or content verification. `verify_resume()` verifies
   the checkpoint file and ledger linkage but never verifies the recorded
   learner/optimizer artifacts. It then returns an immediately chargeable and
   registrable `TState`, even if powered-off calendar time made E3 overdue.
   `TState.from_mapping()` also coerces numeric strings with `int()` and strings
   with `bool()`, ignores unknown fields, and permits an inactive state to hold
   candidate IDs, review-device time, or `author_stopped=True`.
   `record_operational_pause()` does not require activated T, while
   `record_not_activated_maintenance()` does not receive a state and can make a
   false not-activated assertion. These paths can manufacture a nominally valid
   resume or a fictitious inactive checkpoint.

   **Mandatory repair before WP-1/WP-2 closure:** use an exact-key,
   exact-type T-state schema with the invariants `inactive => zero counters,
   empty candidate set, no review, and not author-stopped`; require an active,
   resumable state for an operational pause and an exact inactive state for
   not-activated maintenance; store canonical artifact paths/identities and
   recompute every hash at resume; verify the pause's `resets_e3:false` and all
   checkpoint/ledger fields; and return a fail-closed resume gate that forbids
   charging, registration, or real-T access until any overdue E3 review is
   durably completed. Add crash-point tests for checkpoint-before-ledger,
   partial ledger append, stale checkpoint, suffix truncation, artifact
   deletion/mutation/substitution, forged hash strings, malformed state types,
   inactive-pause fabrication, false not-activated maintenance, and overdue
   powered-off resume. Orphaned or ambiguous transactions must be process
   invalidity/recovery states, never a scientific terminal and never a free
   reset.

## Major

3. **The validity-first surface is not closed under its public constructors.**
   `QTerminal` itself correctly leaves competence unset on invalidity.
   `CTerminal`, however, accepts any nonempty string on `valid=True`, including
   a process/pause label, and therefore can turn `T_OPERATIONAL_PAUSE`, an
   invalidity spelling, or any invented text into a scientific terminal. The
   one-shot journal separately accepts arbitrary terminal payloads; after
   `LAUNCHED` it does not require `charged:true`, does not enforce a typed Q
   terminal, and does not require competence to be unset for invalidity.

   **Mandatory repair:** replace the free C label with disjoint typed validity
   and scientific-terminal enums. Scientific pass/null/boundary/`INSUFFICIENT`
   or censoring may be constructed only from a valid, complete C execution;
   invalid C must expose no scientific field. Keep T endings, Q phase endings,
   pauses, and invalid causes outside that enum. Make journal terminal creation
   accept and validate a typed `QTerminal` record, with every launched terminal
   charged and every invalid terminal's competence unset. Add exhaustive
   cross-product rejection tests, including every process/pause/invalid label
   on the C scientific surface.

4. **The one-shot state machine does not implement the exhaustive launch
   partition or reset resistance.** It has no terminal/disposition transition
   from `CLAIMED`, so a pre-entropy failure cannot be durably closed as the
   signed no-launch/no-charge case. `DRAW_ARMED` recovery is conservatively
   charged, which is correct, but deleting a valid suffix reopens an earlier
   phase because the per-directory chain has no independently pinned head.
   A launched terminal can contradict the earlier charge as described above.
   Thus the primitive does not yet establish “pre-byte and no charge” versus
   “first byte or ambiguity and charged” as an exclusive, total, durable
   partition.

   **Mandatory repair:** add a typed, author/signed-disposition-required
   pre-entropy close from `CLAIMED` with `charged:false` and competence unset;
   retain `DRAW_ARMED -> charged Q_INVALID` as the only ambiguous recovery;
   require all `LAUNCHED` successors to remain charged; forbid reuse of every
   closed or ambiguous attempt ID; and bind the attempt ID plus current event
   head into an append-only external journal/head commitment so deletion of a
   suffix cannot buy a new look. Tests must cover every legal and illegal
   transition, failures before arming, at the invocation boundary, after the
   first byte, after commitment, and during terminal persistence. Concrete
   OS-CSPRNG custody, alpha spending, caps, and Q numerics remain WP-6 cells.

5. **The PRF domain encoding is not injective, and its public key type blurs
   the authorization boundary.** Integer `1` and string `"1"` have identical
   encodings, so distinct typed domains collide. In addition,
   `ProvidedKey(test_only=False)` is freely constructible and is accepted by
   `CounterStream`; the boolean is only a caller assertion. The module draws no
   entropy, but this API can be mistaken for an approved production/Q root
   derivation surface even though no such capability is authorized.

   **Mandatory repair:** add an explicit component-type tag to the length-
   delimited domain encoding and golden tests proving separation of every
   supported type and boundary value. Under WP-1/WP-2, PRF operations must
   accept only an unforgeable test-only capability/key created by the internal
   dummy factory. A distinct sealed-root type and factory must remain absent
   until WP-6 installs and reviews it; a caller-set boolean is insufficient.

6. **Candidate identity does not implement the signed behavior-inert
   equivalence rule.** The manifest is canonical, content-addressed,
   from-scratch, and conservative for field changes, but
   `behaviorally_equivalent()` is only byte equality of the whole manifest.
   Any code-commit change consumes a new identity, including the signed inert
   class of names, comments, packaging, timestamps, and serialization-only
   changes. The tests explicitly reject an `"inert?"` field rather than test a
   canonical inert normalization. This prevents undercharging, but it does not
   satisfy the equally explicit rule that a known behavior-inert edit cannot
   consume or replenish E2.

   **Mandatory repair:** define and test a conservative whitelist normal form
   that removes only the signed inert class, keeps all unknown changes
   behavior-relevant, and makes both `candidate_id()` and equivalence use that
   form. If source identity remains commit-based, bind it to a reviewed
   behavior-bearing source/config digest rather than the raw commit alone.
   Unknown or ambiguous edits must consume a new slot.

## Minor

7. **Core arithmetic is directionally sound, but real metering is correctly
   still absent.** Device time uses integer nanoseconds and explicit additions;
   duplicate candidate IDs do not consume E2; the twelfth distinct candidate
   exhausts E2; subsequent charge/registration is refused; powered-off calendar
   time advances E3; and early reviews cannot reset E3. A single charge may
   overshoot E1 by an arbitrary amount before exhaustion is observed, and the
   library does not measure concurrent processes, reserve capacity, bind a
   charge to a ledger entry, or authenticate an author stop. Those real-harness
   duties belong to WP-4, but WP-4 must record actual overrun rather than erase
   it, prevent new work at/crossing the cap, charge concurrent active training
   additively through quiescence, exclude paused/off time, preclaim real-T work
   durably, and require Kirill's separate author-stop record. None may become a
   competence or scientific threshold.

8. **The verifier passes the present tree but is not a complete fail-closed
   verifier.** It checks selected hashes, deny-by-default, inactive T, an empty
   ledger, direct forbidden imports, and a short list of directly spelled
   entropy calls. It does not enforce the exact schemas and every signed value
   of `PATH_POLICY.json`, `T_ENVELOPE.json`, and `LINEAGE.json`; nor does its AST
   scan resolve imported aliases or cover other entropy APIs. A mutated cap or
   aliased entropy call can therefore evade it.

   **Repair before treating the verifier as a gate:** validate exact keys,
   types, authorized values, lowercase-hex hashes, paths, empty fixture list,
   and inactive-ledger genesis; resolve import aliases and use a fail-closed
   entropy/import allowlist or a materially complete forbidden set. Add mutant
   tests for every governed JSON field and alias form. This is engineering
   assurance only and supplies no scientific evidence.

# Direct answers to the required checks

1. **Validity-first types: not yet sufficient.** Q invalidity is correct in
   `QTerminal`, but the free-form C label and untyped journal payload leave
   process-to-science routes. No current file contains a scientific result.

2. **Q launch accounting: not yet sufficient.** The draw-armed ambiguity rule
   is correct, canonical event files and interior hash links detect mutation,
   and no entropy source is called. The pre-entropy close is missing, launched
   terminal invariants are unenforced, suffix deletion is not externally
   detectable, and the caller-constructible PRF key is not an authorized
   entropy/root type. No real Q launch has occurred.

3. **T accounting: partially correct, not closable.** Integer/additive state,
   E2 uniqueness/cap, E3 clocks, early-review refusal, pause non-terminal
   spelling, and no automatic off-time E1 accrual are correct. Candidate
   equivalence, resume authentication, inactive-state invariants, overdue-review
   gating, cap-crossing integration, concurrency metering, ledger-before-work,
   and signed author-stop enforcement are missing or deferred as identified
   above. A planned power cycle is conceptually a non-scientific pause, but the
   present resume path is not strong enough for real T.

4. **Information boundary: not yet sufficient.** The committed configuration
   has no fixture grant, the tests are deterministic engineering-only fixtures,
   and interlocked real entry points refuse execution. Persistent fixture taint
   can nevertheless be laundered, and the breathing-check contract/numerics are
   correctly absent.

5. **Canonical/durable artifacts: partially correct, not closable.** NaN is
   rejected; loaded JSON must be canonical; journal creation is no-replace;
   ledger entries are canonical, sequential, hash-linked, file- and
   directory-flushed; content tampering and partial lines fail closed. Valid
   suffix truncation lacks an independent anchor, checkpoint artifact hashes
   are not verified, schema coercions are accepted, and crash recovery is not
   total. Those defects can erase resource lineage or manufacture a nominal
   resume.

6. **Statistical scope: confirmed within this diff.** The finite-frame choice
   appears only as the signed interpretation type; no frame, member, sampling,
   inclusion-probability, weight, FPC, seed, endpoint, margin, contrast,
   competence numeric, or sample-size value is instantiated. Committed T is
   `NOT_ACTIVATED`. The source and tests contain no scientific datum, model run,
   trajectory, comparison, or outcome.

# Closure blockers and valid deferrals

The Critical and Major repairs above are WP-1/WP-2 closure blockers. They must
be implemented and boundedly re-reviewed before WP-1/WP-2 are closed or the
work-package sequence is advanced to WP-3.

The following cells remain validly deferred and must not be chosen by these
repairs:

| Owner | Deferred cell |
|---|---|
| WP-3 | All eight finite-frame population/construct objects and every frame, partition, inclusion probability, weight, FPC, seed-scope, and heterogeneity value |
| WP-4 | Real-T generator/harness; exact active-process clock and parallel metering; ledger-before-real-work transaction; runtime cap enforcement; checkpoint contents for the eventual learner; authenticated author-stop integration |
| WP-6 | OS-CSPRNG root mechanism and custody; root attestation; Q attempt/candidate caps; `delta_Q` and spending; competence predicate and numerics; stack-family identity; breathing-check tolerance and bounded reproducibility contract |
| WP-9 and later | Scientific endpoint, arms/contrasts, margins, alpha, sample size, C roots, escrow contents, lock, execution, outcomes, and claims |

# Tests and verification run

- `git diff --check d3be92f..2de1df5` — passed.
- `git diff --exit-code 2de1df5..HEAD -- successor/officina src/philosophia/officina tests/test_officina_accounting.py tests/test_officina_bootstrap.py tests/test_officina_governance.py scripts/verify_officina_wp12.py .github/workflows/ci.yml pyproject.toml README.md` — passed; the load-bearing post-anchor diff is empty.
- `.venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_officina_accounting.py tests/test_officina_bootstrap.py tests/test_officina_governance.py` — **22 passed**.
- `.venv/bin/python -B scripts/verify_officina_wp12.py` — **OK**.

The passing tests establish their asserted positive paths; they do not close
the untested counterexamples above. The system `python3 -B -m pytest ...`
attempt was non-executing because that interpreter has no `pytest` module; no
test was run by that attempt.

# Disposition and negative space

Codex may not close WP-1/WP-2 on this implementation and this review does not
open WP-3. After the bounded repairs, the exact implementation delta needs a
new focused Y-line confirmation. WP-3 may then be drafted only; no real world
may be generated without WP-3's separate reviewed and signed contract.

This review created only this review file. It created no entropy, real world,
model run, candidate registration, T activation or run, Q attempt, promotion,
breathing-check qualification, scientific specification, authorization, lock,
escrow secret, C execution, trajectory, comparative datum, or outcome. It did
not modify `essay/OUTLINE.md`, the pre-existing Sol prompt-header change, or any
other existing file, and it did not commit.
