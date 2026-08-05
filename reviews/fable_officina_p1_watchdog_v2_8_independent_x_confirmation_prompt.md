# Independent X-line final confirmation: Officina P1 watchdog v2.8

Use Fable 5 in a fresh session. If unavailable, use Claude Code Opus 4.8,
never Opus 5, because Opus 5 authored v2.8. Work in:

`/home/master/llm_projects/philosophia`

Review exact commit `dba33e6` (`Repair watchdog role import closure in v2.8`).
Do not edit historical files or untracked implementation work. Do not commit.
Treat the Opus 5 closure as adversarial context only.

## Primary bytes

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md`
  `5666d2bf9cee3c4404cc1f26ac13050a40403af9b4631fa774a1bfacbe481ca8`
- `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md`
  `28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md`
  `6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176`
- identity state:
  `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md`
  `7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f`

Prior reviews:

- `reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md`
- `reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md`

Do not trust:

- `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_8_closure.md`

## X1 — independently reconstruct the 89-row role closure

Do not copy MS-11.1. On the exact pinned interpreter/build/flags, starting from
the three scoped direct-import allowlists after the proposed reduction:

1. derive every runtime direct/transitive module without importing or executing
   any Philosophia production module;
2. correctly handle relative imports, aliases, pseudo-modules, unexecuted
   branches and `from __future__` compiler/runtime behavior;
3. independently derive every `kind` and every import-time edge;
4. independently audit all 267 booleans, especially module-level calls to
   `os.register_at_fork`, task/thread starts, signal/atexit/audit/trace/profile/
   import-hook installation;
5. confirm/refute the claimed 89 rows, kind counts 29/13/2/45, 76 imported
   names, 39 empty arrays, canonical length 20534 and SHA-256
   `aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee`;
6. verify the previously confirmed fourteen-row bootstrap subset is identical;
7. enumerate every platform-conditional branch and compare with the author's
   claimed six.

Run a clean-process differential that is not polluted by reviewer tooling.
Report your independently derived table or a machine-readable digest plus every
difference. Any wrong row, kind, edge, boolean, normalization or branch is
BLOCKING.

## X2 — independently test the `subprocess` reduction

Using the prospective 17-name scoped allowlist, verify whether adding
`subprocess` reaches exactly the claimed extra surface, including `threading`,
`signal`, `select`, `selectors`, `_posixsubprocess`, `locale`, `_locale`, and
whether `threading` really calls `os.register_at_fork` at module scope on the
pinned build.

Then verify that removing only `subprocess` yields the claimed 16-name direct
allowlist and eliminates every import-time starts-task/registers-at-fork/
installs-handler violation. Check whether another direct import independently
reaches any forbidden or side-effectful surface. Do not accept “zero scan hits”
without inspecting the scan definition and false-negative cases.

Confirm whether `__future__` is actually a runtime `IMPORT_NAME` on this exact
build and whether the `_thread` residency/edge disclosure is accurate.

## X3 — total validation topology

Audit `TS-2A`, `TS-2B`, `VP-1..VP-4` and `CK-1..CK-15` as executable logic, not
only tables. Verify that prerequisites exist before reads, the install record's
position is literal, and no relation is owned twice or zero times.

Reproduce all six mandatory multi-fault states and expected first codes. Try to
construct additional multi-fault states that permit divergent codes. Check the
distinction between `HISTORICAL_BYTE_MOVED` at CK-7 and `MEMBER_STALE` at CK-13.

## X4 — integrity, counts and regressions

Derive every graph edge from path/digest/id/signature/option/key/count/assertion
relations. Confirm B14's Stage-B-to-Stage-A option edge and find any omission.
Recompute region and joint hashes, A0.4 cardinality, member classes/digests,
counts, rule/check/code/test totals and cross-references.

Verify preservation of A0.4's honest scope, FS-1..FS-5, TR-2(a)/(b), row 106(i)
PASS, option symmetry, identity boundaries, `T=NOT_ACTIVATED`, programme claim
`OPEN`, and all negative authorization space.

## Verdict

Emit exactly one:

- `OFFICINA_P1_WATCHDOG_V2_8_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`
- `REVISE_OFFICINA_P1_WATCHDOG_V2_8`
- `BLOCKED_OFFICINA_P1_WATCHDOG_V2_8`

Write:

`reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md`

Confirmation permits only Kirill's watchdog option choice. It authorizes no
keys, artifacts, implementation, tests, install, activation or science.

In chat report the verdict, hashes, independent closure result/differences,
subprocess experiment, topology result, findings by severity and next boundary.
Do not modify existing files or commit.
