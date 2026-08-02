# Prompt for Claude Code Opus 5: replace the P1 composite with a marker-safe, literally self-contained v1.1

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. Read-only file/repository commands and SHA-256 computation are
permitted. Do not edit any existing file, implement code, run tests or
behavioural probes, or execute any process-control experiment involving
socket/pipe/fork/exec/signal/wait/prctl. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.

## Governing input

Read and hash in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md`;
- `reviews/opus5_officina_supervisor_p1_operative_composite_v1_closure.md`;
- the prompt that mandated v1 and the independent X review it was meant to
  close;
- the complete signed/provenance chain v1 incorporates.

Treat the v1 closure and chat summary as untrusted author self-assessment. v1
was a useful materialization, but it is **not ready for X/Y**. This round must
create a complete replacement, not a correction delta.

## Three confirmed defects

### R1 — the body extractor terminates at the example marker, not the real marker

The physical marker lines occur at least four times:

- the real BEGIN near the start;
- literal BEGIN and END example lines inside §C13.1;
- the intended real END near §C15.

But §C13.1 defines `NORMATIVE_BODY` as the bytes between the first BEGIN and the
first subsequent END. Therefore the actual body ends at the **example END**
inside §C13.1. The author's reported 1,663-line body confirms that truncation.
Most of §C13, the static verifier rules, §C14 tests and §C15 negative space are
outside the extracted/digested target.

### R2 — executable behaviour still depends on `unchanged` and unnamed peer bytes

The v1 prompt forbade behavioural placeholders such as `unchanged`, but they
remain inside the body, including:

- controller/worker descriptors "unchanged from the signed adapter";
- dynamic authority-table state cells labelled `unchanged`;
- signal-disposition state "otherwise unchanged from g-1";
- `SPAWNING_MIDDLE` schema/field statement labelled `unchanged`;
- watchdog C1 properties said to hold `unchanged`;
- identity-table ownership/continuation cells labelled `unchanged` or `as I-6`;
- almost the whole §C12 harness/batch interface described as `unchanged`;
- test/preflight language that depends on those placeholders.

These are not literal values. Two implementers can resolve them against
different historical or peer artifacts. The author summary's claim that no
behavioural `unchanged` remained is false.

### R3 — verifier input is labelled non-normative

§C16 says everything below the END marker is non-normative and carries no
operative force. But §C16.1 contains the exact G-1…G-5 pattern data that the
verifier reads and that changes pass/fail behaviour. Those bytes are therefore
normative verifier input despite being labelled non-normative. Whole-file hash
custody makes changes visible but does not repair the authority contradiction.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md`
2. `reviews/opus5_officina_supervisor_p1_operative_composite_v1_1_closure.md`

Do not modify any existing file. The v1.1 file must be a **full, self-contained
replacement** for v1. It must not require applying v1 as a delta and must remain
the only operative implementation object after acceptance.

## A. Marker-safe normative regions

Design a mechanically total extraction scheme with these properties:

1. Every sentinel line used by the parser occurs **exactly once** in the entire
   file. Cardinality and order are verified before extraction; zero, duplicate
   or reversed sentinels fail closed.
2. The normative prose/body region includes every executable contract rule,
   all verifier rule definitions, the full test matrix and negative space.
3. Exact guard-pattern data is explicitly **normative verifier data**, not a
   non-normative appendix. It may live in a second uniquely delimited normative
   region excluded from its own substring target, but its authority and digest
   must be explicit.
4. Historical provenance may remain in a separately delimited non-normative
   region and must never be read for behaviour.
5. The document must define its sentinels without repeating their literal full
   line inside a normative region. Use an exact byte-construction rule (for
   example fixed byte fragments concatenated by the verifier) or another
   single-valued scheme. Add negative fixtures for duplicate, missing,
   reordered and example-collision markers.
6. Define and independently report SHA-256 for every normative region and for
   their ordered composite. The whole-file digest remains pinned by the author
   closure and later reviews/manifests, without a self-hash cycle.

The closure must recompute the regions using the stated algorithm and prove
that the intended final section, test matrix and negative space are inside the
normative coverage.

## B. Literal self-containment

Inside every normative region:

- eliminate **every occurrence of the token `unchanged`**;
- eliminate behavioural placeholders such as `same as`, `as before`,
  `preserved`, `carried`, or an unnamed "signed adapter/record/contract";
- internal references to a fully literal section of v1.1 are allowed;
- external peer contracts may own functionality outside P1, but the P1
  boundary must name the exact peer contract path/digest/schema and must state
  every field, ordering, input/output and invariant that P1 consumes or
  produces. Do not make implementation depend on opening a historical P1
  predecessor.

Repair every known locus explicitly:

1. restate controller/worker descriptor values as literals;
2. replace dynamic-table state placeholders with exact sets/states or an exact
   entry-state retention rule defined locally;
3. express the `SigIgn` postcondition as an exact relation between before/after
   bitsets;
4. pin the complete `SPAWNING_MIDDLE` schema value, key set and meanings;
5. enumerate every retained watchdog C1 property as current operative rules;
6. make I-5…I-8 ownership and continuations literal, with explicit entry-state
   preconditions where necessary;
7. replace §C12 with an exact typed interface boundary to the accepted generic
   harness and batch-settlement contracts: named paths/digests plus every P1
   consumed/produced schema, order and invariant. Peer-internal rules unused by
   P1 should be declared out of scope, not labelled `unchanged`;
8. repair every associated verifier/test statement.

Run a byte-level self-audit of all normative regions and report all remaining
occurrences of `unchanged`, `carried`, `as before`, `same as`, `preserved`,
historical P1 section references and unnamed peer references. The required
count is zero. Do not claim zero without showing the exact search domain and
result in the closure.

## C. Preserve the earned contract

Except for R1–R3, v1's literal final P1 semantics must remain identical:

- process topology, descriptors, opcodes, journals and crash cuts;
- F1–F5, `S-18'`, subreaper semantics and dynamic adopter/wait model;
- false-positive safety versus absent liveness/confinement;
- signed A3/B1/C1/D1/K1/P1 meanings and output ceiling;
- S-25 split (`S-24a` static plus `S-24b` topology and behavioural test);
- complete transitive provenance custody;
- T `NOT_ACTIVATED`, claim `OPEN`, no implementation authority.

Do not add a process, syscall, import, recovery path, signal route, scientific
claim, resource observation or author choice. If literalizing a placeholder
reveals a genuine conflict between signed contracts, stop with an exact
`BLOCKED_...` verdict and identify the author cell; do not choose.

## D. Author audit and verdict

Independently verify:

- sentinel cardinality/order and exact extracted byte ranges;
- region hashes and whole-file acyclic custody;
- guards G-1…G-6 against the real target and negative fixtures;
- no normative verifier input is called non-normative;
- all previously placeholder-bearing tables are now literal;
- the process/fd/opcode/crash invariants still agree;
- the composite remains one object and never opens historical P1 files for
  execution or verification.

If and only if all three defects are closed without a new choice, closure line
1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_1_XY_REVIEW
```

The closure must include:

- exact v1→v1.1 replacement/coverage table;
- one-to-one R1/R2/R3 dispositions;
- sentinel/region authority table and recomputed full hashes;
- literal interface table for generic harness and batch settlement;
- no-regression table for every earned P1 cell and X finding;
- exact future implementation/verifier/test/manifest surface;
- weakest points and negative space;
- three bounded questions each for X and Y reviewers of identical bytes;
- confirmation that existing files were untouched and no token is available.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or behavioural probe, T activation, entropy,
E1/E2/E3 spend, Q/C work, datum, outcome, Proof or claim movement.
