# Prompt — Stage-R L3 projection-only bounded repair V2

ROLE: the same bounded implementation Builder, repairing only the two concrete
driver findings. Do not reopen the annex, redesign L3, add another file or
perform a general review. Do not commit or push.

The cumulative focused-work total, including the first 1 h 25 min, must remain
within eight hours. If it cannot, stop with `STAGE_R_L3_FOCUSED_DAY_KILL`.

## Pinned inputs

- Executable annex SHA-256:
  `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0`.
- Driver audit:
  `successor/stage_r/l3/STAGE_R_L3_DRIVER_CODE_AUDIT_V1.md`, SHA-256
  `1375d71b7dd1a52c6e2915d95e878fcf2df99682c2fd3b3b06b3b503551fc374`.
- V1 production SHA-256:
  `1a04bed4366599bb3b542b6ae7bbc123dff9b56078c5552249dec31c875d0ffb`.
- V1 test SHA-256:
  `fd6948652bfa44ccdfd0da6ae1cd093312a6d09a0e4a7f6bbf430698427908c2`.
- Frozen exclusion JSON SHA-256, which must remain byte-identical:
  `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315`.
- V1 Builder report SHA-256:
  `701af4e4cf7f0706ad51bdf580f89075960d658bebb2036cd5d3ec9a3c670eec`.
- MINIMO base and all upstream pins remain those in the V1 Builder prompt.

Recompute these before editing. Work only in a fresh reconstructed tree and
`successor/stage_r/l3/candidate/`. Do not modify the original MINIMO checkout,
the annex, recovery artifacts, frozen JSON or V1 report.

## Repair 1 — enforce real canonical-theorem precondition

In production `public_projection`, retain every existing structural check and
then compare the input canonical bytes with
`canonical_theorem(canon_theorem)`. If they differ, raise
`L3InvariantError('CANONICAL_THEOREM_PRECONDITION_VIOLATED')` before hashing or
rendering. There is no normalization-on-behalf-of-the-caller and no second
public output.

In the gate:

1. replace `canonical_three_atom_theorem` with a hard-coded theorem independently
   known to equal its full-orbit byte minimum; assert that equality explicitly;
2. preserve the driver counterexample as a separate canonical-looking but
   non-minimal object;
3. prove its canonical bytes differ from `canonical_theorem(...)` and that the
   real unmodified `public_projection` refuses it with the exact invariant code;
4. prove all eleven valid fixtures retain their V1 theorem, public and skeleton
   outputs byte-for-byte.

Do not weaken the precondition to canonical atom spelling or hypothesis sorting.

## Repair 2 — complete the mandatory gate seams

### A. Authority binding before fixture reconstruction

Add one configurable Philosophia project-root environment variable with pinned
absolute default. At the start of `_load_governing`, before `_FIXTURE_CACHE` can
be populated, hash-check from disk:

- Stage-R contract;
- L3 activation;
- executable L3 annex;
- annex driver closure;
- accepted Stage-B charter;
- accepted L2 annex;
- accepted cumulative patch through L2 V5;
- V3 ledger and L2 code-gate JSON.

Keep the existing recovery-root override. Add the accepted L2 V5 test
`test_phase2_stageb_generator.py` at SHA-256
`01adece50de5dc4cece3acfed80b21725ca7400e5d375204d5010eaae0dca4e8`
to the in-tree source map. Verify every in-tree pin from the same pre-fixture
path, not merely in a test whose alphabetical execution might occur later.
Missing and mismatched files fail closed. Replace the hex-syntax-only
documentary test with exact disk-hash assertions; constants embedded in the JSON
remain unchanged.

### B. Every sealed-field refusal

Use a closed local tuple containing the annex §5 categories: `root`, `root_id`,
`draw`, `draw_index`, `band`, `target_band`, `node_count`, `plan`, `trace`,
`skeleton`, `skeleton_identity`, `scaffold`, `direction`, `source`, `branch`,
`held_out`, `certificate`, `rejection`, `subcause`, `fixture_name`. Attach each
one separately to a fresh genuinely canonical theorem and assert the real
`public_projection` raises exactly
`CANONICAL_THEOREM_PRECONDITION_VIOLATED`. Retain malformed/naming/order tests.

### C. `OR_ELIM` assumption erasure

Add a direct test which changes only one `OR_ELIM` assumption formula, keeps
the branch proof shapes fixed and proves byte-identical `rule_skeleton` output.

## Frozen-output and scope conditions

Regenerate the test artifact only for comparison. Its bytes and SHA-256 must
remain exactly:

```text
a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315
```

If any valid fixture theorem identity, theorem name, public item,
public-projection hash or skeleton identity changes, stop blocked. Do not tune
the JSON or fixtures to the new code.

Only the two candidate source files and the two patch files may be replaced.
Preserve the V1 Builder report and create:

```text
successor/stage_r/l3/candidate/STAGE_R_L3_BUILDER_REPAIR_REPORT_V2.md
```

The repaired delta must still add exactly two new MINIMO files; the cumulative
scope must remain the accepted 34 paths plus those two. No selector-helper name
or invocation, scan, new fixture, key/root/frame generation, L4, Peano,
MCTS/search, learner/selector or execution work is allowed.

## Verification

Repeat recovery manifest verification, byte compilation, ordinary Stage-B
discovery and both clean patch routes. Add an explicit standalone reproduction
of the former counterexample. Record measured counts, route manifests, all new
hashes, unchanged JSON hash, focused repair time and cumulative focused time.

If fully closed, end the V2 report and chat response with:

```text
READY_FOR_STAGE_R_L3_DRIVER_REAUDIT_V2
```

Otherwise end with exactly one:

```text
BLOCKED_STAGE_R_L3_PROJECTION_ONLY_V2
STAGE_R_L3_FOCUSED_DAY_KILL
```
