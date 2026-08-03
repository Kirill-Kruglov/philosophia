# Prompt for Claude Code Opus 5: repair the P1/peer ownership interface in a full v1.2 composite

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. Read-only repository/file commands and SHA-256 computation are
permitted. Do not edit any existing file, implement code, run tests or
behavioural probes, or execute process-control operations. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing input

Read and hash in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md`;
- `reviews/opus5_officina_supervisor_p1_operative_composite_v1_1_closure.md`;
- the accepted generic-harness and batch-settlement contracts/signatures;
- every historical schema definition needed by the four peer artifacts below;
- the current untracked implementation only as non-authoritative evidence of
  ownership; do not modify or treat it as governing.

Treat the v1.1 closure as untrusted author self-assessment. v1.1 mechanically
closes the sentinel, region-hash, placeholder and guard-data defects. Preserve
those closures. This round addresses one remaining internal contradiction in
the typed peer interface and must produce a full replacement, not a delta.

## Confirmed interface contradiction

The same operating-system process contains code belonging to two logical
contracts: the P1 control-plane layer and the accepted generic-harness peer
layer. v1.1 sometimes uses the word **P1** to mean a logical layer and sometimes
to mean the whole supervisor/watchdog process. That makes §P1-13 internally
false:

1. §P1-13.2 says the **supervisor makes the spawn-intent durable before
   `SPAWN_ROLE`**, then says **P1 writes no field and creates no such record**.
   The only coherent reading is that the co-resident peer-harness layer writes
   it and the P1 client/PCS consumes it, but that ownership split is unstated.
2. §P1-13.3 says the process-claim is written by the supervisor, then says P1
   writes it nowhere. Again, the peer layer writes from evidence returned by
   the P1 layer; process identity is being confused with logical ownership.
3. §P1-13.4 is titled "Artifacts P1 names but neither reads nor writes", but:
   - `c17` polls/live-verifies `SUPERVISOR_IDENTITY.json`;
   - the watchdog verifies against that identity record;
   - the watchdog writes the freeze-observation record under its witness id.
   These are P1 construction/role operations, so "neither reads nor writes" is
   literally false regardless of which contract owns each schema.
4. Test 84 and the out-of-scope table inherit the same incomplete read/write
   set, so a conforming implementation could pass while omitting required
   identity/freeze I/O or could duplicate peer-owned writes.

This is a specification ownership defect, not a new author choice.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md`
2. `reviews/opus5_officina_supervisor_p1_operative_composite_v1_2_closure.md`

Do not modify any existing file. v1.2 must be a complete self-contained
replacement for v1.1, with one operative object after acceptance.

## I1. Define logical ownership separately from process residence

Add an exact terminology/ownership table covering at least:

- `P1 control-plane layer`;
- `generic-harness peer layer`;
- `batch-settlement peer layer`;
- PCS bootstrap, role bootstrap, supervisor role and watchdog role processes;
- co-resident call direction between layers.

For each layer state what code/root owns the decision, what process executes
it, and which contract owns its schema/semantics. State explicitly:

- a write performed by the supervisor process is not automatically a P1-layer
  write;
- a peer-owned schema may still be read or physically emitted by a P1-created
  role, which must appear in the interface table;
- no artifact may have two logical writers, and process residence never decides
  schema authority.

Do not invent new modules or split processes. This is a logical ownership map
over the already selected topology.

## I2. Rebuild the four-artifact interface literally

For each artifact below give one row with exact path rule, schema value, complete
key set relevant to construction/validation, logical schema owner, logical
writer, executing process, readers, exact fields read, durability/ordering,
deletion/archive authority, and the P1-produced or P1-consumed invariant:

1. `t-spawn-intent.v1`;
2. `t-process-claim.v1`;
3. `t-supervisor-identity.v1` / `SUPERVISOR_IDENTITY.json`;
4. `t-freeze-observation.v1` / witness-id path.

Trace the accepted historical contracts to literalize these values. In
particular:

- spawn intent: peer harness writes durably under its signed lock/order; P1
  client names it; PCS reads/validates exactly the fields it needs and rebuilds
  argv without accepting argv over the wire;
- process claim: P1 returns the exact stop/evidence tuple; peer harness alone
  decides and performs the durable claim write under its accepted schema/order;
- supervisor identity: identify exactly which P1 bootstrap/role step installs
  it, which `c17` path reads/live-verifies it, which watchdog step reads it, and
  who may remove it;
- freeze observation: identify exactly which watchdog/P1 role step writes it,
  which peer/supervisor path reads or archives it, and the no-replace/witness-id
  rule.

If the accepted chain permits the supervisor to write freeze observation when
the watchdog is dead, state which **logical layer** owns that fallback and why
it does not violate single-writer or C1. If the final selected P1 contract
removed that fallback, state its exact replacement. Do not guess: if the chain
does not resolve it, emit `BLOCKED_...` and name the author cell.

## I3. Repair the interface tests and out-of-scope boundary

- Replace §P1-13.2–§P1-13.7 with a total read/write/ownership matrix.
- Recompute test 84 and add negative tests for wrong logical writer, missing
  identity read, duplicate claim write, wrong freeze writer, and a process-name
  based ownership inference.
- Rewrite test 85/out-of-scope so it excludes only peer-internal state that no
  P1 path actually consumes or produces. It must not exclude an artifact that
  `c17`, the watchdog, PCS or P1 client reads/writes.
- Ensure the implementation edit surface assigns every operation to exactly one
  root/function and prevents both layers from independently installing the same
  no-replace record.
- Add a closed invariant: every durable artifact visible at the interface has
  exactly one schema owner and exactly one authorized logical writer, even when
  reader/writer code shares an OS process.

## I4. Preserve v1.1 mechanics and P1 science boundary

Except for the interface repair, preserve v1.1 byte-semantically:

- six unique sentinels and exact extraction/order/cardinality rules;
- `BODY` and normative `GUARDDATA`, non-normative `PROVENANCE`;
- zero placeholder/historical-reference count in normative regions;
- G-1…G-10, S-1…S-24b, region/file hashes and acyclic custody;
- all 85 existing test obligations, renumbering only if the repaired interface
  requires new rows;
- process topology, descriptors, opcodes, journals, crash cuts, F1–F5,
  subreaper/A3 safety-liveness boundary, signed A3/B1/C1/D1/K1/P1 choices;
- T `NOT_ACTIVATED`, claim `OPEN`, no implementation authority.

Recompute `H_FILE`, `H_BODY`, `H_GUARDDATA`, `H_NORMATIVE`, sentinel counts,
placeholder audit and guard fires on final bytes. The required guard-fire and
placeholder counts remain zero.

## Verdict and closure

If literal reconstruction reveals a conflict in the accepted peer contracts,
stop with an exact `BLOCKED_...` verdict. Do not choose. Otherwise, if and only
if the ownership contradiction is closed without changing topology or signed
semantics, closure line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_2_XY_REVIEW
```

The closure must include:

- exact v1.1→v1.2 replacement table;
- one-to-one disposition of I1–I4 and the four contradictions;
- complete artifact ownership/read/write/path/schema matrix;
- peer-contract source locations and hashes supporting every literal field;
- all four recomputed hashes and mechanical audit output;
- no-regression table for v1.1 and every prior X finding;
- exact implementation/verifier/test/manifest surface;
- weakest points and bounded X/Y questions on identical bytes;
- confirmation existing files were untouched and no token is available.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or behavioural probe, T activation, entropy,
E1/E2/E3 spend, Q/C work, datum, outcome, Proof or claim movement.
