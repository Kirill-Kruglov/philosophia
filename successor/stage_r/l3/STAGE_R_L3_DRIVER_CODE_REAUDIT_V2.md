# Stage-R L3 projection-only driver code re-audit V2

Status: `READY_FOR_ONE_INDEPENDENT_BOUNDED_CODE_REVIEW`

Date: 2026-08-15

## Repaired candidate pins

| object | SHA-256 |
|---|---|
| production | `ee1be7afef332d8ce87b37c885760dfddcdcb911525cc377aec940b02ac07860` |
| test | `2d71a629acb8dfa5bd8d42eef57b87746e9e6df28a80b514e950515e506dd45e` |
| frozen exclusion JSON | `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` |
| L3 delta | `4f4b692a0ae8f3e989a6e353618cab19d20becc05d7dfe2007f6d58e7f354b71` |
| cumulative patch | `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c` |
| Builder repair report V2 | `92752e0bae86a5c4d5db5d77a56457693b5467c87c766f949722be9ac085cf9c` |

## Driver result

All findings in `STAGE_R_L3_DRIVER_CODE_AUDIT_V1.md` are closed.

1. `public_projection` now compares its structurally canonical-looking input
   against the full-orbit `canonical_theorem` byte minimum before hashing or
   rendering. The exact V1 counterexample now raises
   `CANONICAL_THEOREM_PRECONDITION_VIOLATED`; its normalized representative is
   the only accepted public name across all six permutations.
2. Authority verification is the first operation of `_load_governing` and binds
   the contract, activation, annex, annex closure, charter, L2 annex, accepted
   cumulative patch, V3, L2 gate JSON and nine in-tree accepted files by exact
   disk hash before the fixture cache can be populated.
3. All twenty sealed-field categories have direct refusal injections.
4. `OR_ELIM` and `NOT_INTRO` assumption-record formula erasure have direct
   hold-other-children-fixed tests.
5. All eleven V1 valid-fixture theorem, public and skeleton outputs are pinned
   unchanged by the gate.

The driver independently reconstructed a fresh local MINIMO clone at base
`6066f482c6752915ad21119f93dc162f4cb9db72`, applied the repaired cumulative
patch after `git apply --check`, and verified candidate source hashes. Both files
compiled; the applied tree passed `git diff --check`.

Ordinary Stage-B discovery result:

```text
Ran 144 tests in 59.533s
OK
```

No selector scan was called. The gate used only the six literal frozen L2 rows.
The driver then invoked the explicit artifact helper once at a caller-supplied
temporary path. It reproduced SHA-256
`a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315`;
`cmp` against the durable candidate JSON was byte-identical.

The repaired delta still has exactly two new-file entries; the cumulative patch
has 36 entries. Production remains limited to the accepted imports and pure
bounded operations. The approximately doubled gate runtime is the declared
cost of enforcing the public subfunction's full-orbit precondition and does not
affect scientific execution.

## Remaining gate

Exactly one independent bounded code review remains. It may check this code
against the executable annex and direct regression only. It may not reopen the
Stage-R contract, add exact-plan identity or stage-6 seed, request a general
review or authorize L4.

```text
DRIVER_MAJOR_1_CLOSED=YES
DRIVER_MAJOR_2A_CLOSED=YES
DRIVER_MAJOR_2B_CLOSED=YES
DRIVER_MAJOR_2C_CLOSED=YES
FROZEN_EXCLUSION_JSON_CHANGED=NO
L3_INDEPENDENT_CODE_REVIEWS_REMAINING=1
L4_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```
