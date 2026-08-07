# Prompt for Claude Code Opus 5: materialize the single Officina P1 operative composite

You are **Claude Code Opus 5 acting only as the specification author**. You are
not the independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. You may use **read-only** repository/file commands and SHA-256
computation to inspect committed bytes. Do not edit any existing file,
implement code, run tests or behavioural probes, or execute any
process-control experiment involving socket/pipe/fork/exec/signal/wait/prctl.
T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing evidence

Read in full:

- `reviews/opus_officina_supervisor_p1_final_xy_review.md`
  (`REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`);
- `reviews/sol_officina_supervisor_p1_final_xy_review.md`
  (`BLOCKED_...` solely because the prior Y prompt accidentally prohibited the
  reviewer's only read/hash mechanism; this is not a merits finding);
- the signed P1 selection and the complete v2.1 through v2.1.10.7 chain;
- all signed A3/B1/C1/D1/K1/output-capacity choices;
- the generic-harness and batch-settlement contracts and signatures;
- current `verification.py`, inactive runtime/envelope state and authorship note.

Recompute all relevant hashes. Treat every author closure, including 10.7, as
an untrusted self-assessment. The X review found the Linux/process-control core
sound, but found one Major specification defect: the signed P1 selection
requires **one operative composite**, while the committed contract is still a
transitive prose-delta chain. The prose guards S-23/S-26/S-27/S-28 therefore
have no mechanically decidable domain and fire on correctly superseded
historical text.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md`
2. `reviews/opus5_officina_supervisor_p1_operative_composite_v1_closure.md`

Do not modify any existing file.

## C1. One normative object, not another delta

The first file must be the **single, complete, self-contained and authoritative
operative P1 supervisor-control contract**. It is not a correction layer and
must not require a reader or implementer to apply any historical replacement
index.

It must restate every executable/normative P1 element in its final selected
form, including at minimum:

- scope, threat model and signed A3/B1/C1/D1/K1/P1 meanings;
- exact constants, schemas, enums, frames, byte limits and failure tokens;
- process topology and every parent/adopter/reaper/wait/signal/PID/handle
  authority relation, including the dynamic subreaper model;
- caller→PCS→middle→supervisor and PCS→role construction sequences;
- exact descriptors, logical slots, `CLOEXEC`, `DUP2`, `CLOSE`, `P-f`, A-1…A-13,
  G-1…G-6 and `/proc/self/fd` permissions;
- all `t-pcs.v1` opcodes, request/reply schemas, handle model, journal/ACK/replay
  automaton, no-redelivery rule and SCM_RIGHTS parsing/cleanup;
- controller/worker/watchdog spawn, stop, replace, reap and shutdown paths;
- batch-settlement/generic-harness composition points;
- every crash cut, invalidity dominance, terminal route, PCS-loss rule,
  no-adoption rule and PID-reuse/death-proof rule;
- exact safety guarantees and explicitly absent liveness/confinement guarantees;
- production roots, imports, builtins/method identities, manifests, hashes,
  verifier rules and complete future test matrix.

For executable behaviour, phrases such as "carried", "unchanged", "as in
v2.1.10.x", "apply replacement row", or "see predecessor for the rule" are
forbidden. Historical files may be cited only in a **non-normative provenance
table** by path/hash/selection identifier. Every implementable value and rule
must appear literally in the composite itself.

The composite must declare an exact authority hierarchy:

1. author signatures remain the source of accepted choices;
2. this composite is the sole operative specification of how those choices are
   implemented;
3. v2.1–v2.1.10.7 remain immutable historical/provenance evidence and are not
   scanned or interpreted for operative behaviour;
4. any future change to this composite requires a new signed/reviewed version,
   never an implicit prose override.

If consolidation exposes a real signed conflict that cannot be resolved without
a new Kirill choice, stop with `BLOCKED_...`. Do not choose or silently prefer a
layer.

## C2. Make the guard domain mechanically decidable

Define one exact named contract-guard target: the normative body of the new
composite file. Historical documents are categorically outside that domain.

Re-express S-23/S-26/S-27/S-28 as mechanically implementable checks against
that named target. Give exact matching/normalization semantics or replace the
fragile wording checks with a stronger closed invariant/hash mechanism. The
result must satisfy both requirements:

- the correct composite passes without ignoring a historical false positive;
- a future operative composite cannot silently reintroduce absolute-init,
  exclusive-ancestor-wait-set, closed-adopter-status-set, death-proof-liveness,
  or unqualified-process-authority overclaims.

Do not scan the historical chain. Do not rely on an undefined adjective such as
"operative". Do not make a verifier infer supersession from prose.

The composite cannot contain its own SHA-256 without a cycle. State the
acyclic custody rule exactly: the author closure pins the composite digest;
later implementation authorization/manifests pin that reviewed digest. Include
a complete transitive provenance hash table for the source chain, including
intermediate corrections omitted from 10.7's abbreviated block, or state a
smaller sufficient Merkle-like ancestry root whose verification algorithm is
fully explicit and mechanically covers every incorporated byte.

## C3. Close both X Minor findings

1. Split S-25 into what is statically decidable and what is topological/runtime:
   - AST/static verifier: exactly one decision branch consumes a wait-status
     word and it is the named `WIFSTOPPED` site;
   - topology invariant and behavioural test: its target is a live-custody,
     non-orphan direct PCS child. A future topology change must fail a named
     check even if the AST count remains one.
2. Make the governing/provenance custody self-sufficient as required by C2,
   without a self-hash cycle.

## C4. No regression and no new science

Preserve byte-semantically the earned final meanings of:

- v2.1.10.5 F1–F5;
- 10.6 child-subreaper semantics and phase-scoped `S-18'`;
- 10.7 dynamic adopter/wait table, untrusted adopter status, false-positive
  safety versus absent liveness, and authorization distinction;
- signed P1 full PCS mediation, A3 procedural rescope, B1 non-redelivery,
  C1 one-detector trade, D1 mandatory PCS/no adoption, K1 fixed output ceiling;
- generic harness and batch-settlement accepted contracts.

Do not add a process, syscall, import, recovery path, signal route, confinement
claim, liveness guarantee, T activation, resource observation or scientific
claim. Do not modify implementation scope beyond making the already selected
contract implementable.

## C5. Author audit and handoff

Perform a static author audit of the completed composite:

- independently reconstruct every process/fd/authority table from its literal
  rules and check internal equality;
- trace every opcode and crash cut to one terminal continuation;
- confirm no forbidden historical wording or unresolved cross-reference is
  needed for behaviour;
- enumerate every exact future code/test/verifier/manifest edit surface;
- check the new composite against the X review's concrete Major and two Minors;
- confirm the Sol access blocker will be removed by a later review prompt that
  explicitly permits read-only file access and hashing.

If and only if the composite is complete, single-valued and no new choice is
needed, closure line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_XY_REVIEW
```

The closure must contain:

- SHA-256 of the new composite and all custody inputs;
- a section-by-section coverage map from the historical chain into the single
  composite;
- one-to-one disposition of X Major 1, X Minor 1, X Minor 2 and Sol's access
  blocker;
- exact guard-domain and acyclic hash-custody description;
- complete constants/process/fd/opcode/crash/verifier/test summaries;
- weakest points and explicit negative space;
- three bounded questions each for future X and Y reviewers of identical bytes;
- confirmation that no existing file changed and no acceptance token is
  available from this author round.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or behavioural probe, T activation, entropy,
E1/E2/E3 spend, Q/C work, datum, outcome, Proof or claim movement.
