REVISE_OFFICINA_T_ACTIVATION_PROTOCOL

# Bounded conclusion

The draft has the correct scientific architecture: activation is process state, T is adaptive and permanently non-citable, E2 registration waits for WP-6, Q is a routing/competence gate rather than evidence, and only locked C can move C1-C6. It does not introduce a T estimand or an outcome-dependent scientific choice. However, three mechanical promises are not yet specified strongly enough for implementation: test-labelled access can evade E1, reviewed runtime controls are not pinned across adaptive learner commits, and crash/concurrency accounting lacks a durable bounded-liability rule. Reporting and recovery also need closed schemas so no T process fact can acquire scientific semantics.

# Findings

## Critical

1. **“Mechanically lacking a real-T capability” is currently a free development route, not a sufficient E1 definition.** Sections 2 and 7 correctly say that every real-T lease spends E1, but section 7.140-141 exempts tests, dummy worlds, and paths lacking the future capability. The already reviewed WP-4 source exposes `test_world_capability` and `evaluate_test_query` on every signed T-band modulus. Those functions are legitimate for fixed disposable unit tests, yet the protocol does not prohibit a behavior-capable learner, draft manifest, tuning loop, or developer script from using that same callable and calling the resulting observations “tests.” Under the draft's literal rule, such a path lacks the real capability and spends zero E1 despite performing the behavior-relevant T work that E1 governs.

   Classification must follow what the operation does, not its function name or artifact label. Fixed oracle unit assertions may remain free; arbitrary T-band evaluation, learner fitting, hyperparameter choice, stack choice, checkpoint creation, or behavior-changing use must require a lease.

2. **A clean later HEAD does not preserve the reviewed metering/interlock implementation.** The authorization pins a reviewed implementation commit at section 3.55-58, but active verification at sections 6.119-133 requires only mutually exact artifacts at the current clean HEAD. T is intentionally adaptive, so learner/config commits must be able to change after activation. Without a separate immutable source-path/hash allowlist, the same clean later commit can also change the activation verifier, capability issuer, world gate, lease meter, ledger transaction, or test/production boundary. A process could then obtain an apparently current capability under unreviewed accounting code.

   Runtime-control bytes and adaptive learner bytes need distinct identities. The former remain equal to the reviewed activation record for the whole activation; the latter may change only between leases and must be bound to the applicable claim/manifest.

3. **E1 is conceptually continuous but not durably total under crash or concurrent overshoot.** Sections 7.151-169 defer charge to heartbeat/close, call an ambiguous interval invalid, and require a future maximum-uncharged-interval constant. They do not define a durable per-lease last-charged cursor, boot/clock identity, outstanding liability, or transaction order for advancing that cursor. Nor do they reserve aggregate liability across concurrent leases. A process can therefore expose a T world or complete learner work after its last durable heartbeat and disappear; the draft blocks recovery but does not say what E1 is irreversibly charged. Many concurrent leases can also cross E1 or the 40-device-hour E3 boundary by an unbounded aggregate amount before their next heartbeats.

   `T_RUNTIME_INVALID:PROCESS` is a validity classification, not an accounting value. “No estimated zero charge” does not by itself make every exposure spend E1. A conservative, bounded, durable liability rule is required before implementation.

## Major

4. **Device/stack/process-tree identity is recorded but not invariant at every use.** A process claim records command, stack, and positive device count at sections 7.143-149, while the capability in section 6 is bound only to activation record, process id, source HEAD, T bands, and lease identity. The protocol does not say how actual worker processes and devices map to `k`, whether child workers require the same lease, or what happens when a process changes device count, stack, numerical mode, or code while its lease is open. This leaves both E1 undercounting and behavior-untracked stack switching possible.

5. **T process artifacts and endings lack a closed, validity-first reporting surface.** The draft says every T ending is non-scientific, but process-record fields and individual process terminals are not enumerated. Normal close, voluntary development stop, learner exception/non-finiteness, wall/OOM/resource failure, process loss, hash failure, E1 exhaustion, E3 review due, pause, and author stop can therefore be narrated inconsistently. Nothing expressly forbids `pass`, `fail`, `censored`, `INSUFFICIENT`, competence, arm/effect, or outcome-summary fields in process records, E3 reviews, breathing records, or the public ledger.

   T may retain quarantined development observations and checkpoints for adaptive selection, and the eventual selected checkpoint may be part of the frozen candidate. That is not C evidence. Public process artifacts should carry only allowlisted authorization, lineage, stack, resource, validity, and routing facts; checkpoint hashes may establish lineage but no T metric may enter a C estimator, margin, subgroup, decision, or C1-C6 narration.

6. **Clock and recovery semantics leave discretionary process choices.** System-UTC rollback is not classified, a monotonic clock's boot identity and restart behavior are unspecified, and “newly reviewed invocation” before an activation claim does not say whether the one-shot authorization remains usable. Runtime recovery is signed and bounded, but the draft does not require its packet to exclude learner observations or to settle all outstanding E1 liability before work resumes. These are procedural choices, not scientific choices, but leaving them open after T observations exist would permit outcome-aware recovery handling.

## Minor

7. **The separation claims need one lineage/evidence clarification.** Sections 2.42-44 and 11.235-238 correctly forbid T/Q facts from moving C1-C6. The later locked record will nevertheless have to hash `H_preC`, including selection and process lineage. The protocol should say explicitly that a T/breathing/E3 hash may enter `H_preC` or `selection_scope_id` only as conditioning/lineage metadata; neither the hash nor its underlying value is a covariate, statistic, effect estimate, competence fact, margin input, or evidence.

# Exact bounded repairs

R1. Replace the zero-E1 sentence in section 7 with:

> E1 ownership is functional, not label-based. Any operation that instantiates or queries a signed T-band world, evaluates or trains a behavior-capable learner against it, creates a behavior-bearing checkpoint from it, or uses its observation to alter learner, optimizer, policy, interface, stack, or configuration is real-T work and requires an active lease. Only fixed, precommitted disposable assertions and dummy fixtures that accept no learner, candidate, draft manifest, adaptive input, or exportable observation spend zero E1. Reviewed production and learner paths must fail closed on the WP-4 test-capability factories and test-oracle contact functions.

Add a required implementation test/verifier rule that every production activation/learner import and dynamic call graph excludes the test-only world/contact factories, and that a test label cannot exempt a learner loop or arbitrary T-band query.

R2. Add to sections 3 and 6:

> The activation record contains an exact allowlist and hashes for every immutable runtime-control source: authorization/preflight, active-state verifier, capability issuer and consumer guards, world gate, lease/meter, clock, ledger/state transaction, pause/resume, and terminal serializer. Every claim, capability issuance, heartbeat, oracle admission, learner admission, and close revalidates those bytes against the activation record. A clean HEAD is necessary but insufficient. Adaptive learner/config/manifest paths are disjoint from the immutable list, are hashed in the process claim, and may change only between leases. Any runtime-control change blocks work and requires a new bounded implementation review, authorization, and signed recovery/amendment; it is never an in-place T edit.

R3. Add a complete E1 transaction rule:

> Each lease durably stores a process id, process-tree scope, exact stack and source identities, device identities/count, monotonic clock kind, boot identity, start reading, last durably charged reading, cumulative charge, heartbeat deadline, outstanding-liability bound, and prior charge-event hash. Before capability issuance or renewal, the global transaction reserves `k * H` device-time liability, where `H` is the reviewed maximum interval, and refuses if charged E1 plus all live liabilities would exceed the applicable E1/E3 boundary. Each heartbeat settles only the cursor delta under the global lock, appends the full global and per-lease post-state, replaces the cache/lease cursor, and renews liability. Real-world answers and behavior-bearing checkpoints are released only through a still-current lease and a post-operation settlement. Process loss, clock ambiguity, or missed deadline revokes capability and charges the full outstanding bound before any recovery; never zero. Crossing charge is retained, all leases are revoked when a boundary is reached, and no new work is admitted.

The numeric `H` and maximum concurrent lease/device envelope are engineering constants owned by the reviewed implementation/authorization, fixed before activation, and never selected from T performance.

R4. Extend the capability binding and lease rules with:

> Every use revalidates exact command, process-tree membership, behavior source, stack, numerical mode, device identities/count, and lease cursor. Child workers are covered by exactly one declared lease and cannot create an unmetered contact route. Any behavior-relevant source/stack/device/config change closes the current lease after full charge and requires a new non-reusable claim; it cannot mutate an open lease. Concurrent charges are serialized into one global state without loss or double counting.

R5. Add an exact T reporting contract:

> T artifacts are validity-first and contain `scientific_outcome:false`. Activation/process/pause/review/breathing records use closed schemas containing only authorization, lineage, source/stack/device, clock, resource, validity, and routing fields. They contain no arm, contrast, score series, competence, pass/fail, censoring, `INSUFFICIENT`, equivalence, boundary, effect, margin, or C1-C6 field. `T_ENVELOPE_EXHAUSTED` is set only by E1 or, after WP-6 registration exists, E2 exhaustion; `T_AUTHOR_STOP` requires its signed review-bound transaction; E3 due and operational pause are nonterminal gates. Environment/resource/process/hash faults are typed T invalidity. Learner exceptions and non-finiteness are quarantined development facts, never scientific censoring or learner impossibility. A candidate-submission record after WP-6 is routing only. Every valid or invalid T ending proves only the recorded process/resource history.

R6. Add exact clock/recovery clauses:

> Canonical UTC may advance E3 but never rewind an activation/review/ledger origin. UTC rollback or disagreement is fail-closed clock invalidity; a forward correction may conservatively make review due. Lease monotonic readings are accepted only under the recorded boot identity; reboot or an unavailable/non-monotone cursor with an open lease invokes the outstanding-liability rule. Recovery packets contain only authorization, filesystem, clock, lease, charge, hash, and process-validity facts; learner observations and tuning metrics are unavailable to the decision. Recovery cannot delete/reuse a claim or process id, erase charge, reset E3, or resume before liability and state are durably reconciled. A pre-claim activation failure creates no T exposure, but another invocation requires an exact bounded pre-claim disposition stating whether a fresh one-shot authorization is required; it is not an automatic retry.

R7. Add to the evidence boundary:

> `H_preC` and `selection_scope_id` may commit hashes of T, breathing, E3, and selection history solely to identify what was conditioned on. No such hash or underlying T/Q value is an analysis input or evidence. Draft manifests before WP-6 are explicitly `unregistered`, `q_ineligible`, and order-free; the future WP-6 registry recomputes canonical behavioral identity from exact source/stack bytes, ignores draft-supplied eligibility or queue position, charges E2 once, and remains the only route to Q submission.

# Direct scope decisions

## Separation of phases

The intended activation/T/E2/Q/C ordering at sections 2, 6, 9, and 11 is scientifically correct. Activation creates no learner fact. T is fully adaptive inside its envelope and has no confirmatory estimand. Registration is absent until a signed candidate-blind WP-6 contract exists; draft manifests consume no E2 and convey no Q eligibility. Q cannot run from this protocol. C evidence remains unavailable until later promotion, specification, lock, escrow, and one-shot authorization gates. No T ending can be scientific censoring or programme `INSUFFICIENT`.

The six governing hashes in section 1 match the repository bytes. E2 remains unavailable in the proposed implementation surface; it must not be added by this work package.

## Author choice and learner-harness gate

No new scientific author choice is required before **inactive implementation** once R1-R7 are incorporated and boundedly reconfirmed. The heartbeat/concurrency limits, clock primitive, runtime source list, and conservative ambiguity charge are engineering cells: implementation proposes them, X/Y review checks them, and Kirill later accepts their exact values only through the separate activation authorization. They cannot be chosen from T outcomes because activation has not occurred.

Actual activation must remain blocked until a concrete metered real-T learner harness and its complete world/oracle/checkpoint call graph receive separate bounded review. This means a reviewed generic harness capable of containing later adaptive learners, not preselection of a learner, optimizer, stack, candidate, or expected winner. That review must prove that all real-T exposure routes require the lease and that no test-only, subprocess, device-switch, checkpoint, or direct-oracle bypass exists. Activation before that proof would start E3 without establishing the central E1 invariant.

## Meaning of a valid T ending

A valid T ending is process evidence only: it can establish that a particular authorization, resource counter, review, pause, submission, exhaustion, or signed author stop occurred. It cannot establish learner competence, construct difficulty, efficacy, feasibility on Q/C, an arm ordering, a boundary, falsification, or programme support. Adaptive T observations may select what is tried next; their inferential price is the later selection-conditional C claim, not retrospective citation of T.

# Eligible implementation surface after repair

This verdict authorizes only bounded revision of the protocol and another X/Y review. It does not yet authorize implementation.

After R1-R7 are closed, a positive protocol verdict may authorize inactive implementation and disposable-mirror tests of only:

- canonical authorization/preflight and activation claim/state/ledger/envelope/record transactions;
- immutable runtime-source pins and active-state re-derivation;
- exact-type real-T capability and a disabled generic learner/world interface;
- global lease, reservation, heartbeat, E1/E3, clock, process-terminal, pause/resume, and recovery primitives;
- Q/C/E2/test-surface refusals and static call-graph/import verification;
- failure injection and temporary-mirror concurrency tests.

Production authorization JSON, activation outputs, a concrete real learner adapter, candidate registration, breathing qualification, Q/C roots, and scientific fields remain absent. A concrete learner harness may be prepared only as a later separately reviewed inactive candidate before any activation authorization.

# Negative space and pristine-state check

I performed only read-only repository inspection and hash verification. Before and after review, `git diff --exit-code` reports no change to `successor/officina/T_ENVELOPE.json`, `T_LEDGER.md`, or its external head. T remains pristine and `NOT_ACTIVATED`.

I created no code, activation authorization, activation claim/state/record, runtime artifact, real capability, process claim/lease/record, real world, entropy, learner, draft manifest, candidate, registration, E1/E2/E3 spend, breathing check, Q/C object, lock, escrow, scientific datum, outcome, terminal, or claim movement. No stopped-line outcome informed this review. No qualification, contrast direction, learner competence, or programme success is predicted.
