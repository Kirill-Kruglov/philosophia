# Stage-R L3 projection-only driver code audit V1

Status: `BOUNDED_REPAIR_REQUIRED`

Date: 2026-08-15

Candidate pins:

| object | SHA-256 |
|---|---|
| production | `1a04bed4366599bb3b542b6ae7bbc123dff9b56078c5552249dec31c875d0ffb` |
| test | `fd6948652bfa44ccdfd0da6ae1cd093312a6d09a0e4a7f6bbf430698427908c2` |
| exclusion JSON | `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` |
| L3 delta | `9619264fc16c4222be190f350b9b873c1808358da3adc4f7897cc7c468c5e6d3` |
| cumulative patch | `e44de3a37add3dcb71e6100a83f2eee9e6c42a50602bef95a237e2294b456c2e` |
| Builder report | `701af4e4cf7f0706ad51bdf580f89075960d658bebb2036cd5d3ec9a3c670eec` |

Independent driver execution applied the cumulative patch to a fresh local
clone at MINIMO base `6066f482c6752915ad21119f93dc162f4cb9db72`, compiled both new files and ran
ordinary Stage-B discovery. Result: `Ran 131 tests in 30.519s`, `OK`. The frozen
selector scan was not called. Candidate source hashes equal the files produced
by the patch route.

## Major 1 — public projection does not enforce alpha-minimality

Annex §5 requires `public_projection` to accept only the canonical theorem.
Production lines 350–359 verify the three-key shape, canonical atom-name list
and strictly sorted hypotheses, but never compare the input with the byte-minimum
of its full atom-renaming orbit.

The smallest counterexample is already the gate helper at test lines 393–398.
It has atoms `a0,a1,a2` and sorted hypotheses, so test line 892 asserts that
`public_projection(base)` succeeds. Direct evaluation gives:

```text
canonical_bytes(base) == canonical_bytes(canonical_theorem(base))  -> False
public_projection(base).theorem_name
  = t_48a7c724c863a635a65360d28981db16fcdc9c63b1771f8124d292177e5c874d
public_projection(canonical_theorem(base)).theorem_name
  = t_c77e2e5f73a745ae9792e68688fc1eeda6b45678d82bb79fd3c221c84f1ca558
```

Thus the exposed projection function can emit two public names and sequent-byte
representations for one alpha-equivalence class. `identify` happens to call it
correctly, but the public sub-step violates its executable precondition and the
gate affirmatively blesses the invalid input.

Smallest repair: after structural checks, require
`canonical_bytes(canon_theorem) == canonical_bytes(canonical_theorem(canon_theorem))`
or raise `CANONICAL_THEOREM_PRECONDITION_VIOLATED`. Replace the helper baseline
with a hard-coded genuinely minimal theorem and add this exact non-minimal,
canonical-looking counterexample. This changes production and test hashes but
must not change any accepted fixture output or the exclusion JSON.

## Major 2 — mandatory gate seams are incomplete

### 2a. Governing hashes

Annex §7 item 1 requires every governing file hash before reconstruction. Test
lines 71–87 classify the contract, activation and charter as documentary
constants, and lines 416–420 check only that they look like lowercase hex. The
gate never reads those files. It also omits the accepted L2 annex, accepted L2
V5 test and accepted cumulative patch. Consequently a gate can pass while its
recorded authority strings do not describe the files on disk.

Smallest repair: add one configurable Philosophia project-root resolver with a
pinned absolute default, and hash-check the contract, activation, executable
annex, annex closure, charter, accepted L2 annex and cumulative patch from disk.
Add the accepted L2 V5 test to the in-tree source hash map. Missing or differing
bytes must fail before `fixtures()` can populate its cache. Keep the existing V3
and code-gate checks.

### 2b. Projection leak mutations

Annex §7 item 8 requires refusal at every enumerated sealed-field seam. Despite
its name, `test_rejects_every_sealed_field_mutation` at lines 890–946 injects
only `root_id` and `band` as extra fields. The emitted-byte substring check at
lines 948–955 is not an input-boundary refusal test. Exact key-set enforcement
means production is probably correct, but the mandatory gate is incomplete.

Smallest repair: loop over every annex §5 sealed category — root, draw, band,
node count, plan, trace, skeleton, scaffold, direction, source, branch,
held-out marker, certificate, rejection and fixture name — attaching each key
to a fresh canonical theorem and asserting the exact invariant code.

### 2c. `OR_ELIM` assumption-record erasure

Annex §§4 and 7 require assumption records to erase. Tests cover paired branch
exchange but never mutate an `OR_ELIM` assumption formula while holding branch
shape fixed. Add one direct equality test. Production does not read the record,
so no production change should be necessary.

None of the Major-2 repairs may change the exclusion JSON or any valid fixture
identity/public/skeleton bytes.

## Passed boundaries

No other production defect was found in the line-by-line audit. Raw mismatch
precedence, full `k!` minimization inside `canonical_theorem`, skeleton
sorting/retention, fresh construction, import boundary, failure schemas, V3
reverification, six-row regeneration, artifact structure, patch scope and both
reported routes are coherent. The driver independently reproduced the green
131-test route.

One bounded repair pass is sufficient. No annex edit, author choice, fixture
scan, JSON retuning, L4 work or general review is warranted.

```text
L3_DRIVER_VERDICT=BOUNDED_REPAIR_REQUIRED
FROZEN_EXCLUSION_JSON_MAY_CHANGE=NO
L4_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```
