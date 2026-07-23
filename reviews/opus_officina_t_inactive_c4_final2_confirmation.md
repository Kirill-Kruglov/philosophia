OFFICINA_T_INACTIVE_C4_XLINE_CONFIRMED

# Opus 4.8 X-line — Officina T inactive C4 final namespace confirmation

Reviewer: Opus 4.8 (X-line, adversarial static provenance/quarantine).
Repository: `/home/master/llm_projects/philosophia`, commit
`fbac49309de4b4ebc26a0e82e73432a875e15d91` against parent `e703a2b`. This is the
literal follow-up required by
`reviews/opus_officina_t_inactive_c4_namespace_confirmation.md`
(`REVISE_OFFICINA_T_INACTIVE_C4_NAMESPACE`), confirming the bounded
`__builtins__.*` normalization. **I edited nothing, committed nothing, activated
nothing, created no harness, manifest, authorization, entropy source, process,
lease, or runtime artifact, and spent no E1/E2/E3.** Every probe parsed source
statically in disposable temporary directories; no inspected source was imported
or executed. The real tree is pristine and `NOT_ACTIVATED` (`activated:false`,
`runtime/` = `{T_RUNTIME.lock}`, no harness/manifest/authorization).

The diff is verifier-only (`verification.py` +6/−4, `tests/test_officina_activation.py`
+12, `tests/test_officina_bootstrap.py` +19) and does not reopen the
generic-harness contract, broaden the primitive inventory, or treat subscript
reflection as a new blocker. My reported residual is closed exactly, with no new
ordinary alias bypass found.

## The repair

`_normalized_capability_name` now iterates over both namespace roots
`("builtins.", "__builtins__.")`, mapping the suffix to the bare declared member
when it is in `BUILTIN_DYNAMIC_IMPORT_CALLS` (`verification.py:77-84`). This is
exactly the smallest bounded correction I requested: it treats `__builtins__` as
the builtins namespace for the five existing bare dynamic primitives, then applies
the unchanged loaded-reference / call / `ImportFrom` checks. Regression tests were
added for `__builtins__.eval`, `__builtins__.getattr`, and the hop
`namespace = __builtins__; resolver = namespace.eval` in **both** the production
suite (`test_officina_activation.py`) and the bootstrap suite
(`test_entropy_scan_normalizes_dunder_builtins_namespace`, `test_officina_bootstrap.py`).

## Required-check results (all static; no source imported or executed)

- **Check 1 — CONFIRMED.** In graph-complete disposable fixtures with the source
  as the exact activation root, `__builtins__.eval`, `__builtins__.getattr`, and
  `namespace = __builtins__; resolver = namespace.eval` all refuse by static
  inspection in **both** `verify_source_quarantine` and
  `verify_production_boundary`. Extending to all five bare members, each of
  `__builtins__.{__import__, compile, eval, exec, getattr}` refuses in both
  verifiers. (Previously these returned an empty failure list; the residual is
  closed.)
- **Check 2 — CONFIRMED.** Normalization is restricted to the five existing bare
  members of `DYNAMIC_IMPORT_CALLS`
  (`BUILTIN_DYNAMIC_IMPORT_CALLS = {__import__, compile, eval, exec, getattr}`,
  derived from the existing set, not enlarged); `importlib.import_module` stays
  dotted and is unaffected. The change adds only a second literal prefix to the
  normalizer loop — no capability, no executable inspection, no new AST evaluation.
- **Check 3 — CONFIRMED, not regressed.** Earlier refusals remain intact:
  `builtins.eval` (dynamic), `from os import urandom as d` at the `ImportFrom`
  statement (entropy), the cross-module `activation root → external_behavior →
  local_helper` probe (sole failure `references entropy os.urandom: local_helper.py`),
  the statically composed `/dev/urandom` device path, and the unreachable-source
  reachability failure all still refuse; manifest schema/roots/reachable/edge
  binding is unchanged.
- **Check 4 — CONFIRMED.** Focused `tests/test_officina_{accounting,activation,
  runtime,bootstrap}.py` → **75 passed**; full `pytest` → **279 passed** (was
  273; +6 tests, no regression); `verify_officina_wp12.py` → OK, inactive/
  quarantined; `verify_officina_active.py` → **exit 1**, failing solely because
  `OFFICINA_T_ACTIVATION_AUTHORIZATION.json` is absent; `runtime/` holds only
  `T_RUNTIME.lock`; no officina `src`/`successor` working-tree changes.
- **Check 5 — no reproducible bypass found within the declared set.** I searched
  for a concrete ordinary name/attribute/assignment alias reference to a declared
  primitive that still bypasses: import-alias (`import builtins as b2; b2.eval`),
  `from builtins import eval as x; y = x`, double-hop
  (`a = __builtins__; b = a; r = b.exec`), the dunder-name primitive
  (`__builtins__.__import__`), a `builtins`-var bound to `__builtins__`
  (`bi = __builtins__; q = bi.compile`), and mixed `builtins.*`/`__builtins__.*`
  in one file — **all refuse**. The two ordinary spellings of the builtins
  namespace (`builtins.` and `__builtins__.`) and their alias/assignment hops are
  now normalized; entropy members remain reachable only through their imported
  module names, which resolve to the dotted form and refuse. As agreed, subscript
  reflection (`__builtins__["eval"]`, `builtins.__dict__[name]`, `globals()[name]`)
  is the recorded static-lint limitation shared with the bootstrap quarantine and
  is out of scope for this bounded namespace repair; it belongs to the separately
  reviewed generic-harness gate.

## Disposition and scope

A positive verdict **closes only the inactive production-boundary verifier gate**
(the C4 namespace residual chain). It authorizes **no** harness implementation,
production manifest, activation candidate, authorization, activation, execution,
capability, world, process, lease, learner, candidate registration, entropy,
E1/E2/E3 spend, Q/C object, datum, outcome, or claim movement. Activation still
additionally requires the reviewed-and-pinned generic harness and its real
`PRODUCTION_CALL_GRAPH.json`, an exact author-signed authorization committed at
HEAD, and Kirill's explicit `I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver
runs exactly once.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q are
permanently non-citable for C1–C6; activation, leases, streams, tuning
observations, breathing checks, draft manifests, E3 reviews, non-finiteness, and
every T ending are non-scientific and move no claim; a future Q pass is a
spendability-gate fact only; S is unavailable; only a valid, independently locked
C execution may ever move an Officina claim, within its selection-conditional,
selected-frame, orientation, device, and learner-seed scope. Censored/`UNKNOWN`/
every invalid state is never success, equivalence, a boundary, or learner
impossibility. `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the
programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, implemented no harness, created no manifest, and
committed nothing. `essay/OUTLINE.md` untouched. My actions were reading the
bounded diff and my prior namespace finding, and running the read-only static
probes, disposable reproductions, suites, verifiers, and pristine-tree checks
above. The real repository remains `NOT_ACTIVATED`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
