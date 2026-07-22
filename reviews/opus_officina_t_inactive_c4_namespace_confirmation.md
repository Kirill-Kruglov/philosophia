REVISE_OFFICINA_T_INACTIVE_C4_NAMESPACE

# Opus 4.8 X-line — Officina T inactive C4 namespace confirmation

Reviewer: Opus 4.8 (X-line, adversarial static provenance/quarantine).
Repository: `/home/master/llm_projects/philosophia`, commit
`38ea2f3af57a6425b61b97031845f5ab716f22b5` against parent `1050d07`, under the
Major finding in `reviews/sol_officina_t_inactive_c4_final_confirmation.md`
(builtins-qualified declared primitives). **I edited nothing, committed nothing,
activated nothing, created no harness, manifest, authorization, entropy source,
process, lease, or runtime artifact, and spent no E1/E2/E3.** Every probe parsed
source statically in disposable temporary directories; no inspected source was
imported or executed. The real tree is pristine and `NOT_ACTIVATED`
(`activated:false`, `runtime/` = `{T_RUNTIME.lock}`, no harness/manifest/
authorization).

The diff is verifier-only (`verification.py` +52, `tests/test_officina_activation.py`
+12) and does not reopen activation design or the generic-harness contract. It
correctly closes Sol's exact reproduced `builtins.<name>` variants — **but a
sibling namespace spelling of the same declared primitives, `__builtins__.<name>`,
still bypasses the check reproducibly.** Because the residual is a
semantics-preserving reference to an already-declared dynamic primitive (check 5),
the inactive production-boundary verifier gate cannot close yet.

## What the repair closes (confirmed)

`_normalized_capability_name` maps a resolved `builtins.<name>` to `<name>` when
`<name>` is a declared bare member of `DYNAMIC_IMPORT_CALLS`
(`BUILTIN_DYNAMIC_IMPORT_CALLS = {__import__, compile, eval, exec, getattr}`), and
is applied in **both** `verify_source_quarantine` and `verify_production_boundary`
at the loaded-symbol check, the call check, and a new `ImportFrom`-statement
check. The forbidden inventory is unchanged.

- **Check 1 — CONFIRMED for the `builtins.` namespace.** Each of the five bare
  builtins refuses via `builtins.<name>`, `from builtins import <name> as …`, and
  a multi-hop local alias (`import builtins as bi; r = bi.<name>; q = r`), in both
  verifiers. The inventory is not broadened (`BUILTIN_DYNAMIC_IMPORT_CALLS` is
  derived from the existing set; `importlib.import_module` stays dotted).
- **Check 2 — CONFIRMED.** The normalization fires on the **import statement
  itself**: `from builtins import eval as r` and `from os import urandom as d`
  both refuse at the `ImportFrom`, not only at a later call, in both verifiers.
- **Check 3 — CONFIRMED, not regressed.** The graph-complete cross-module entropy
  probe `activation root → external_behavior → local_helper` with
  `draw = os.urandom` still returns the sole failure
  `references entropy os.urandom: local_helper.py`; omitted-local-dependency,
  ambiguous-resolution, missing/undeclared-root, and unreachable-source refusals
  remain intact.
- **Check 4 — CONFIRMED.** Focused `tests/test_officina_{accounting,activation,
  runtime}.py` → **51 passed**; full `pytest` → **273 passed** (was 270; +3
  namespace tests, no regression); `verify_officina_wp12.py` → OK, inactive/
  quarantined; `verify_officina_active.py` → **exit 1**, failing solely because
  `OFFICINA_T_ACTIVATION_AUTHORIZATION.json` is absent; `runtime/` holds only
  `T_RUNTIME.lock`; no officina `src`/`successor` working-tree changes.

## Blocking residual (check 5) — `__builtins__.<name>` bypasses the same normalization

`_normalized_capability_name` normalizes only names with the literal prefix
`builtins.` (`verification.py:77-82`: `name.startswith("builtins.")`). The
built-in namespace is also reachable, with no import at all, through the
auto-injected global `__builtins__`, whose resolved spelling is `__builtins__.…`
— which does not match that prefix and is therefore never normalized to the bare
declared member. This is the same class Sol closed (an ordinary namespace-
qualified reference to a declared bare builtin), differing only in the namespace
root.

**Reproduction (static; no source imported or executed).** In a disposable
fixture containing all three exact roots and a graph-complete manifest whose
`reachable_sources` and `import_edges` exactly match the computed closure, with
the activation root `scripts/officina_activate_t.py` = `r = __builtins__.eval`,
`verify_production_boundary(...)` returned **`[]`**. The same empty result holds
for `r = __builtins__.getattr` and for the multi-hop `b = __builtins__; r = b.eval`.
`_resolved_symbol` yields `__builtins__.eval`; `_normalized_capability_name`
returns it unchanged, so it never reaches `DYNAMIC_IMPORT_CALLS` membership. By
contrast Sol's `builtins.eval` in the same fixture correctly refuses with
`references dynamic resolution eval`.

**Why it is semantics-preserving and reachable.** Two of the three declared
executable roots — `scripts/officina_activate_t.py` and
`scripts/verify_officina_active.py` — run as the `__main__` module, where CPython
binds `__builtins__` to the `builtins` **module**; thus
`__builtins__.eval is builtins.eval is eval`, a live reference to the declared
`eval`/`getattr`/`__import__`/`compile`/`exec` primitive, needing no import
statement (so the `ImportFrom` and import-alias paths never engage). This is
within the currently declared capability set: no new primitive is proposed, only
a second ordinary spelling of the same callables. (In an imported module such as
`generic_harness.py`, `__builtins__` is a dict and `__builtins__.eval` would raise
at runtime — but the two `__main__` script roots are sufficient to make the
channel live in the exact sources the boundary is meant to fail-closed.)

**Smallest bounded correction.** In `_normalized_capability_name`, also map a
resolved `__builtins__.<name>` to `<name>` when `<name> ∈
BUILTIN_DYNAMIC_IMPORT_CALLS` (treat the `__builtins__` root as the builtins
namespace), then apply the existing loaded-reference / call / import checks. Add
one static regression covering `__builtins__.eval` (direct attribute),
`__builtins__.getattr`, and a multi-hop `b = __builtins__; r = b.eval`. Do not
broaden the primitive inventory, execute inspected source, or change the graph,
manifest, activation, or scientific contracts. Another literal C4 namespace
confirmation is then required.

## Out-of-scope limitation (recorded, not the blocker)

Subscript reflection such as `builtins.__dict__["eval"]` remains outside every
static symbol/string lint (it is not an attribute or call the resolver can name);
this is the pre-existing static-lint boundary shared with the bootstrap
quarantine and belongs to the separately reviewed generic-harness gate, not to
this repair. It is recorded for completeness and is not the basis of this verdict;
the blocking residual above is a plain attribute reference of exactly the class
this gate normalizes.

## Disposition and scope

This verdict authorizes **only** the bounded verifier normalization and
regression stated above, followed by another bounded confirmation. It does not
close the inactive production-boundary verifier gate, and authorizes **no**
harness implementation, production manifest, activation candidate, authorization,
activation, execution, capability, world, process, lease, learner, candidate
registration, entropy, E1/E2/E3 spend, Q/C object, datum, outcome, or claim
movement.

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
bounded two-file diff and Sol's finding, and running the read-only static probes,
disposable reproductions, suites, verifiers, and pristine-tree checks above. The
real repository remains `NOT_ACTIVATED`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
