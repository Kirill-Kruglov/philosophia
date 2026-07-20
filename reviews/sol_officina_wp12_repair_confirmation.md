REVISE_OFFICINA_WP12_REPAIR

# Bounded answer

No. The exact repair diff `fe9a982..bd61cf9` closes four of the five live
counterexample families from my hardening review and preserves the cells both
archived reviews accepted. One verifier counterexample remains reproducible.
It requires a small WP-2 engineering correction and no WP-3/WP-4/WP-6/WP-9
choice.

The repository is currently at `416ed5d56539c7cf8e33ae51d35fe6202fb79988`.
Its committed delta from `bd61cf9e748f86c857ba2d07c5a4a7270f2f5036`
contains only the two repair-confirmation prompts. The load-bearing tree matches
the requested repair commit.

# Sole blocker

## Major — local aliasing still bypasses the entropy verifier

The verifier now catches direct and imported aliases, direct
`getattr(os, "urandom")`, direct dynamic execution/import calls, exact random-
device literals, unreviewed imports, exact ledger-genesis mutations, exact head
field/type mutations, and backdated ledger entries. It still reasons mainly
about the function expression at each `ast.Call` and does not reject sensitive
callable references assigned through ordinary Python variables.

This independent probe returned `[]`:

```python
import os
draw = os.urandom
value = draw(32)
```

```python
verify_source_quarantine([probe_path]) == []
```

Two variants also returned `[]`:

```python
import os
g = getattr
draw = g(os, "urandom")
value = draw(32)
```

and:

```python
path = "/dev/" + "urandom"
value = open(path, "rb").read(32)
```

A fourth probe, `from os import *; urandom(32)`, also returned `[]`.

No probe source was executed, so no entropy was obtained. These are static
verifier false negatives. The reviewed Officina source itself contains none of
these forms, but the verifier's advertised fail-closed “zero entropy calls”
gate is not yet closed under ordinary local aliasing and compile-time string
construction.

### Smallest bounded correction

Extend `verify_source_quarantine()` and its mutation tests as follows:

1. Reject a resolved entropy attribute whenever it is loaded, not only when it
   is the immediate `ast.Call.func`; this rejects `draw = os.urandom` before a
   later call.
2. Reject loaded references to `getattr`, `__import__`, `eval`, `exec`, and
   `compile` (and reject star imports), so assigning a reflective/dynamic
   primitive to a local alias cannot hide it.
3. Evaluate static string constants formed by concatenation or formatted
   literals and reject any expression resolving to `/dev/random` or
   `/dev/urandom`.
4. Add the three probes above, a star-import probe, and locally aliased dynamic
   execution/import probes as negative tests.

A bounded alternative is an exact reviewed-source hash allowlist in addition
to the AST checks. Do not add an entropy implementation or production key type.

# Closure of the other four live families

## 1. One-shot — closed

The replay path and append path now share `_validate_transition()`. The original
late-disposition probes reject after both `DRAW_ARMED` and `LAUNCHED`; a direct
private `_append()` with an uncharged terminal rejects; duck objects and
`QTerminal` subclasses reject; the public adapter canonical-round-trips an
exact `QTerminal`; contradictory/extra mappings fail on replay; and non-hex or
wrong-length manifest/root commitments reject. File, head, and suffix mutation
each fail closed against the journal and external attempt registry.

The permitted partition is therefore exact: only `CLAIMED` may close through
the signed-disposition-shaped, uncharged `PRE_ENTROPY_STOP`; `DRAW_ARMED` may
close only as charged typed Q invalidity; every `LAUNCHED` terminal is charged
and typed. No entropy source, alpha spending, cap, or Q numeric was introduced.

## 2. Resume — closed

An overdue resume serializes `resume_review_pending:true` into the returned
`TState`. That state itself rejects device charge, candidate registration, and
ordinary `complete_review()`. The gate rejects admission, backdated completion,
and repeated completion; one successful gate completion first appends the
monotone `T_REVIEW_COMPLETED` record and returns a state with the pending bit
cleared. Resume-before-pause, pause-before-activation/last-review, and backdated
ledger append reject. The raw-state bypass and time-travel probes from my prior
review no longer succeed.

## 3. Provenance — closed

WP-1/WP-2 `ArtifactLabel.promotable` is structurally always false; copied views
and `dataclasses.replace()` carry no issuance or write authority. Derived writes
accept parent paths and re-read them. Reopen requires the exact metadata record
in the externally headed append-only registry and recursively verifies every
parent path, parent provenance hash, content, and exact source union. Missing
metadata, copied/relabelled metadata, in-place relabel plus re-hash, empty or
changed parents, deleted parents, hand-built metadata, event/head mutation, and
suffix deletion reject. Direct Q and C admission always rejects. No production
or promotable artifact type exists.

## 4. PRF — closed

Typed domain components remain injective for the supported integer/string
boundaries, and booleans reject. `prf_digest()` and `CounterStream` both call the
same issued-identity check. Duck objects, direct construction, shallow copies,
objects made with copied material, booleans, negative counters, and counters at
or above `2^64` reject. Only the exact object identity registered by
`dummy_key()` is accepted. No public production or sealed-root key type was
added.

# Accepted cells not reopened

The closed C scientific enum, exact Q/C validity-first constructors, exact
T-state schema and inactive invariant, artifact hash/path recomputation,
checkpoint/ledger linkage, ordinary external-head behavior, and candidate
behavioral identity remain as accepted in the parent reviews. Candidate
identity still removes only `provenance_commit` and the closed inert-metadata
class; behavior source, stack, initialization, optimizer, policy, interface,
config, and schema remain load-bearing or reject unknown fields.

# Scope

The repair diff introduces no finite frame, construct, population member,
inclusion probability, weight, FPC, real-T meter, production entropy/root/key,
Q predicate, cap, alpha, competence numeric, C endpoint, margin, sample size,
world, registered candidate, trajectory, datum, outcome, execution authority,
lock, escrow secret, or claim transition. The committed T ledger remains the
exact inactive genesis. WP-3 population objects, WP-4 real harness/metering,
WP-6 entropy/custody/Q-family numerics, and WP-9 scientific fields remain
deferred.

# Checks run

- `.venv/bin/python -m pytest -q tests/test_officina_bootstrap.py tests/test_officina_governance.py tests/test_officina_accounting.py` — **45 passed**.
- `.venv/bin/python scripts/verify_officina_wp12.py` — **OK**.
- `git diff --check fe9a982..bd61cf9` — passed.
- The load-bearing diff `bd61cf9..HEAD` is empty.
- Independent `/tmp` probes re-ran late one-shot dispositions, private append,
  duck/subclass terminals, malformed commitments, journal file/head/suffix
  mutation, pending-state work bypasses, repeated/backdated resume operations,
  provenance copy/relabel/parent/registry/admission attacks, and PRF
  duck/copy/counter/domain attacks; all rejected as summarized above.
- Independent static verifier probes reproduced the four false negatives in
  the sole blocker. Those source files were inspected only, never executed.

# Disposition and negative space

WP-1/WP-2 may not close on `bd61cf9`, and WP-3 may not yet be opened by this
review. Apply only the bounded verifier correction and regression tests above,
then perform one focused Y-line confirmation. If that confirmation succeeds,
WP-1/WP-2 may close and WP-3 may be drafted only.

This review created only this review file and did not commit. It created no real
world, real entropy, T activation, real candidate, real Q/C execution,
promotion, scientific specification, lock, escrow secret, trajectory,
comparative datum, scientific datum, outcome, or claim movement. Temporary
test-only journals and dummy files used by the mandated tests and bounded probes
were confined to pytest temporary directories or `/tmp` and removed. No
existing file, including `essay/OUTLINE.md` and the pre-existing prompt-header
change, was modified.
