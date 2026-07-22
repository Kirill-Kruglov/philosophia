OFFICINA_T_INACTIVE_C4_FINAL_CONFIRMED

# Opus 4.8 X-line — Officina T inactive C4 final quarantine confirmation

Reviewer: Opus 4.8 (X-line, adversarial static provenance/quarantine).
Repository: `/home/master/llm_projects/philosophia`. Bounded mandate: commit
`6ba2d23` against parent `f87477d`, under the single Major finding in
`reviews/sol_officina_t_inactive_repair_v2_confirmation.md` (the C4 reachable-
source quarantine false negative). **I edited nothing, committed nothing,
activated nothing, created no harness, manifest, authorization, entropy source,
world, process, lease, capability, candidate, Q/C object, datum, or outcome, and
spent no E1/E2/E3.** Every positive probe parsed source only, in disposable
temporary directories; the real tree was never mutated and remains pristine and
`NOT_ACTIVATED`: `T_ENVELOPE.json activated:false`, `runtime/` = `{T_RUNTIME.lock}`,
no `generic_harness.py`, `runtime_control/PRODUCTION_CALL_GRAPH.json`,
authorization, claim, record, lease, or process artifact.

The diff `f87477d..6ba2d23` is **verifier-only**: exactly
`src/philosophia/officina/verification.py` (+22) and
`tests/test_officina_activation.py` (+56). It adds no manifest, harness, entropy
source, execution authority, or WP-3/WP-4/WP-6/WP-9 choice, changes no scientific
cell or envelope numeric, and reopens no C1–C3 or activation design. Sol's Major
finding is closed; no Critical contradiction is introduced.

## Closure of the C4 reachable-source quarantine gap

Sol's residual: `verify_production_boundary`'s entropy/dynamic quarantine covered
only resolved `ast.Call` expressions per file, so a **loaded reference** such as
`draw = os.urandom` bound in one reachable module and reached through an import
alias in another passed the quarantine despite a graph-complete manifest.

The repair extends the production-boundary scan — applied to **every source in
the computed reachable closure** — to mirror the bootstrap quarantine's stronger
checks:

1. **Loaded-symbol quarantine.** For every `ast.Name`/`ast.Attribute` in a
   **Load** context, `_resolved_symbol` (through the fixpoint `_local_symbol_table`
   over assignment pairs, plus import aliases) is matched against `ENTROPY_CALLS`
   and `DYNAMIC_IMPORT_CALLS` and refused even when the primitive is **assigned
   rather than called** (`verification.py:319-332`). Because `draw = os.urandom`
   binds `os.urandom` as a loaded attribute in `local_helper.py`, the refusal
   fires at that binding site — every reachable source is scanned, so an entropy
   primitive cannot be bound anywhere in the closure without detection, and the
   `_local_symbol_table` fixpoint also resolves a later loaded `draw` to
   `os.urandom`.
2. **Static random-device-path quarantine.** `_static_string` (constant / `Name`
   binding / `+` concatenation / f-string join) is matched against
   `RANDOM_DEVICE_PATHS = {"/dev/random","/dev/urandom"}` on every node
   (`verification.py:344-349`), so a statically composed device path is refused.

Both checks are purely static (`ast.parse` + `read_text` only); no reviewed
source is imported or executed.

## Required-check results (all CONFIRMED, static, no source imported/executed)

1. **Every reachable source is checked for a loaded reference resolving to every
   `ENTROPY_CALLS`/`DYNAMIC_IMPORT_CALLS` member, not only direct calls —
   CONFIRMED.** Independent sweep: all nine `ENTROPY_CALLS`
   (`os.getrandom/os.urandom`, `random.SystemRandom`,
   `secrets.choice/randbits/randbelow/token_bytes`,
   `torch.initial_seed/seed`) and all six `DYNAMIC_IMPORT_CALLS`
   (`__import__/compile/eval/exec/getattr`, `importlib.import_module`) refuse when
   **assigned rather than called**. The `from os import urandom as draw` alias
   form refuses both as a call `draw(32)` and as a bare assignment `keep = draw`.
2. **The exact three-file alias route
   `activation root → external_behavior → local_helper` with `draw = os.urandom`
   refuses despite a graph-complete exact manifest — CONFIRMED.** Reproduced
   independently in a disposable static fixture with the exact roots and a
   reachability-complete manifest (exact `reachable_sources` and `import_edges`
   from the activation root); `verify_production_boundary` returned the **single**
   failure `production source references entropy os.urandom: local_helper.py`
   (graph and manifest completeness do not mask it). The committed regression
   `test_production_boundary_rejects_cross_module_loaded_entropy_alias` exercises
   the same route on a full mirror.
3. **A loaded `getattr` reference and a statically composed `/dev/urandom` path
   refuse — CONFIRMED** (also `/dev/random` via f-string), matching the committed
   parametrized `test_production_boundary_rejects_loaded_dynamic_and_random_device_paths`.
4. **No reviewed source is imported or executed by the verifier — CONFIRMED.**
   `verify_production_boundary` uses only `ast.parse`/`read_text` and static AST
   resolution; there is no `import`, `__import__`, `exec`, `eval`, `compile`, or
   `importlib` call over inspected source.
5. **Local graph reachability, ambiguity, root, provenance, test-world, and prior
   C1–C3 closures remain intact — CONFIRMED.** Full suite is `270 passed`
   (was `267`, only `+3` new C4-quarantine tests, no regression), so
   omitted-local-dependency, ambiguous-resolution, missing/undeclared-root,
   unreachable-source, reviewed-commit provenance (C3), closed process
   composition (C2), and pre-WP-6 E2 (C1) tests all still pass; the added
   loaded-symbol/device checks produced no false positive on the real reviewed
   production sources (the disposable-mirror activation-completes test passes).
6. **Suites/verifiers pass; the active verifier refuses only for absent
   authorization; the real tree stays pristine and `NOT_ACTIVATED` — CONFIRMED.**
   Focused `tests/test_officina_{accounting,activation,runtime}.py` → `48 passed`;
   full `pytest` → `270 passed`; `verify_officina_wp12.py` → OK, inactive/
   quarantined; `verify_inheritance.py` → OK, 71 files; `verify_officina_active.py`
   → **exit 1**, failing solely because `OFFICINA_T_ACTIVATION_AUTHORIZATION.json`
   is absent. `runtime/` holds only `T_RUNTIME.lock`; no harness, manifest,
   authorization, or runtime artifact exists; no officina `src/`/`successor`
   working-tree changes.

## New issues

None gating; no Critical contradiction is introduced by this two-file repair. As
a scope note (not a repair demand, and outside this mandate): the quarantine
remains a **static symbol/reference and static-string lint**, as the
implementation note already states — it does not resolve entropy reached through
non-static reflection (e.g. `os.__dict__["urandom"]` subscripting). That is a
pre-existing property shared with the bootstrap quarantine, is not caused or
widened by this repair, and belongs to the separately reviewed generic
metered-harness gate; it is recorded, not used to reopen the chain.

## Disposition and scope

A positive verdict **closes only the inactive-runtime residual chain** (C1–C4).
It does **not** open or authorize the generic metered-harness implementation or
its design gate by implication, and authorizes **no** harness code, production
manifest, activation candidate, authorization, activation, execution, capability,
world, process, lease, learner, candidate registration, entropy, E1/E2/E3 spend,
Q/C object, datum, outcome, or claim movement. Activation still additionally
requires the reviewed-and-pinned generic harness and its real
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
bounded two-file diff and Sol's Major finding, and running the read-only static
probes, disposable reproductions, suites, verifiers, and pristine-tree checks
above. The real repository remains `NOT_ACTIVATED`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
