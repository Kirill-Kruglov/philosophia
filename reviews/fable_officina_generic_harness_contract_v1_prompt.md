# Fable 5 prompt: Officina generic metered harness contract v1

You are Claude Code Fable 5 drafting the next protocol-level work package for
Officina. Work in `/home/master/llm_projects/philosophia`.

Governing state:

- independent verdict:
  `reviews/fable_officina_independent_programme_validation.md`
  (`READY_FOR_OFFICINA_GENERIC_HARNESS_CONTRACT`);
- signed activation protocol:
  `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V1_DRAFT.md`,
  `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md`, and
  `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_1_CORRECTION.md`;
- signed world contract and WP-4 boundary:
  `successor/OFFICINA_WP3_SIGNATURE.md`,
  `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md`, and
  `successor/OFFICINA_WP4_IMPLEMENTATION.md`;
- inactive implementation:
  `src/philosophia/officina/{accounting,activation,runtime,verification,world}.py`
  and `successor/officina/T_ACTIVATION_IMPLEMENTATION.md`;
- pending bounded confirmations:
  `reviews/{opus,sol}_officina_t_inactive_repair_v2_confirmation_prompt.md`.

The residual confirmations may run in parallel with this drafting. Do not pin
implementation hashes, a reviewed code HEAD, or a production source set until
they land. Treat the current 267-test suite as engineering evidence only.

## Authorization boundary

Create exactly two new files and change nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`
2. `reviews/fable_officina_generic_harness_contract_v1_closure.md`

Do not implement code, create `generic_harness.py`, create
`runtime_control/PRODUCTION_CALL_GRAPH.json`, create an activation
authorization, activate T, issue a capability, create a real world or learner,
draw entropy, register a candidate, spend E1/E2/E3, or create runtime/Q/C data.

This is a generic infrastructure contract. It must not select a learner,
architecture, optimizer, training rule, certificate numeric, Q predicate,
alpha, margin, candidate, device winner, or scientific endpoint.

## Required contract content

### 1. Scope and authority

Define the harness as the only future issuer and revoker of exact real-T
capabilities. State precisely what activation authorizes and what still
requires later WP-6/WP-9/WP-10 gates. Preserve:

- T is adaptive, open, permanently non-citable for C1-C6;
- E2 and candidate registration remain impossible before WP-6;
- no T event can become Q/C evidence;
- no implementation object or enum implies execution authority.

### 2. Executable lifecycle state machine

Specify an exclusive, total process/lease state machine from inactive genesis
through activation and all T terminals. Include exact preconditions,
postconditions, durable artifacts, ledger events, capability state, and legal
next states for at least:

- process claim creation;
- `T_PROCESS_STARTED`;
- lease installation and renewal;
- behavior-capable operation;
- heartbeat settlement;
- voluntary stop;
- resource stop;
- E1 exhaustion;
- E3 review due/completed;
- operational pause;
- author stop;
- process loss, deadline miss, reboot, clock ambiguity, filesystem/hash fault;
- record-first `T_RUNTIME_INVALID`;
- resume after an ordinary power-off.

No branch may fall through, silently retry, erase liability, or reinterpret an
invalid run as a valid terminal.

### 3. Durable transaction ordering

For every lifecycle transition, give a numbered write/`fsync`/atomic-install/
ledger/cache ordering and its crash cut-points. State which recovery action is
legal after failure at every cut. Reuse the repository's canonical JSON,
no-replace creation, held-descriptor lock, hash chain, and record-before-event
discipline. No Git commit may be a runtime safety precondition.

### 4. Metering and liability

Close the operational meaning of aggregate device time without choosing a
device winner:

- exact monotonic readings and units;
- multiple concurrent behavior-capable streams;
- process tree and child-process ownership;
- heartbeat liability and the four-stream cap;
- settle-before-release of every oracle answer, learner-update completion, and
  behavior-bearing checkpoint;
- conservative charge for unknown intervals, process loss, watchdog expiry,
  reboot, or counter reset;
- simultaneous E1/E3 boundary priority;
- refusal before overspend, never post-hoc truncation.

Define a device-meter adapter contract for CPU and future off-CPU stacks. Do
not invent the future breathing-check tolerance or pass threshold.

### 5. Supervisor and watchdog

Specify controller identity, process-group containment, child escape detection,
PID reuse defense, boot identity, watchdog ownership, heartbeat deadlines,
revocation, quiescence, and backend synchronization. A dead controller must not
leave a usable capability or uncharged liability. State the threat model: this
prevents accidental/process faults, not a privileged malicious operator.

### 6. Power-off, pause, and resume

The user may need to power the workstation off before the 168-device-hour
envelope is consumed. Define a tested ordinary-pause path that:

- stops issuance;
- quiesces and settles every live stream;
- revokes all capabilities;
- hashes model/optimizer/config/stack and relevant runtime artifacts;
- records state without resetting E1 or E3;
- survives shutdown and reboot;
- refuses resume on mutation, deletion, substitution, boot/clock ambiguity,
  stale lease, or ledger/cache mismatch.

Distinguish ordinary pause from runtime invalidity and author stop.

### 7. Learner-generic and scientific-data boundary

Define a narrow adapter surface for future learner processes without specifying
their content. Infrastructure may see only facts necessary for process,
resource, integrity, and deterministic replay. Learner behavior, loss,
certificate state, competence, arm labels, and scientific interpretation must
not enter recovery, activation, E3, or author-stop decisions.

T-development logs and checkpoints must carry a non-citable T label and be
mechanically inadmissible to Q/C. Define response gating so a behavior-bearing
result is released only after its charge and integrity transition is durable.

### 8. Draft candidate and WP-6 extension points

Define only a canonical **unregistered draft manifest** surface for T:
behavior source, exact config, stack, numerical mode, device identity, and
checkpoint lineage hashes. It must be `q_ineligible`, order-free, and consume no
E2. Candidate equivalence, registration, Q attempt claims, entropy, depletion,
and promotion remain absent until WP-6.

Name stable extension points so WP-6 can later add its own reviewed objects
without changing the metering core. Do not define WP-6 numerics.

### 9. Production call-graph duty

Specify how the future implementation produces and verifies the canonical
closed production graph:

- exact executable roots;
- every repository-local transitive dependency;
- reachability from roots;
- no unreachable asserted source;
- no ambiguous resolution, dynamic import/reflection, hidden entropy, test-only
  capability, or inherited Level 0/1 behavior dependency;
- exact reviewed source bytes and reviewed-commit provenance.

The manifest itself must remain absent until implementation review authorizes
its creation.

### 10. Verification and fault-injection matrix

Give a complete acceptance matrix suitable for Cursor implementation and Codex
integration. It must include deterministic unit/integration tests for every
state transition and every durable cut-point, plus at least:

- concurrent streams and liability overflow;
- killed controller/child, PID reuse, escaped child, missed heartbeat;
- counter reset/backward motion and reboot;
- backend synchronization failure;
- disk-full/partial write/fsync/rename failures;
- ledger/head/cache divergence;
- artifact mutation, deletion, symlink, hardlink, path substitution;
- response-before-settlement attempt;
- scientific-field leakage into infrastructure records;
- pre-WP-6 E2/candidate attempt;
- Q/C/test-only capability confusion;
- E1/E3 simultaneous boundary;
- clean pause, physical-reboot simulation, and exact resume;
- all valid and invalid process terminals.

Tests may use disposable roots, fake clocks/meters, and test-only worlds. They
must not create a production-compatible real-T artifact.

### 11. Cursor implementation handoff

Provide a bounded, mechanical work breakdown for Cursor Compose after contract
signature. Identify proposed modules, public APIs, schemas, state-machine
tables, transaction helpers, supervisor/meter adapters, CLI surfaces, and test
files. Separate tasks safe for Cursor from tasks retained by Codex, Opus/Sol,
Fable, and Kirill. Cursor must receive no authority to choose scientific cells,
weaken refusals, create author tokens, or activate T.

### 12. Gate and governance simplification

Apply the accepted programme-audit recommendation: one bounded X/Y review of
this engineering contract, one bounded confirmation after mandatory repairs,
then Kirill's signature. Multi-round reopening is permitted only for a concrete
Critical contradiction. This simplification does not apply automatically to
WP-6/WP-9 scientific contracts or one-shot drivers.

List every remaining author choice. Prefer none; if a choice is unavoidable,
give mutually exclusive exact tokens and explain why the signed protocol does
not already decide it.

## Closure deliverable

The closure file must contain:

1. one verdict token, exactly one of:
   - `READY_FOR_OFFICINA_GENERIC_HARNESS_XY_REVIEW`
   - `REVISE_OFFICINA_GENERIC_HARNESS_CONTRACT`
   - `BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT`
2. a traceability table from every requirement above to contract sections;
3. a signed-protocol compatibility table identifying any proposed
   clarification versus amendment;
4. unresolved choices and why they cannot be derived;
5. four bounded attack questions for Opus X-line;
6. four bounded attack questions for Sol Y-line;
7. the exact negative authorization surface;
8. confirmation that no implementation/hash pins/manifest/activation/runtime
   artifact or scientific object was created.

Do not predict whether any learner will qualify or whether Philosophia will be
proved, falsified, or bounded.

