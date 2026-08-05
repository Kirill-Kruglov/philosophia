REVISE_OFFICINA_P1_WATCHDOG_V2_9

# Officina P1 watchdog v2.9 — final Y confirmation

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Date:** 2026-08-05  
**Review target:** commit `1731811f2e72d5c6cc322d16dd4117292195b8be`
(`Consolidate watchdog authority contract in v2.9`)

This is a bounded final confirmation against the four byte-pinned governing
inputs and the prior Y review. The v2.9 author closure was treated as an
untrusted self-assessment. I did not use the modified or untracked
implementation work in the live worktree as evidence, did not execute or
compile a project module, and did not modify any governing, historical, code,
test, signature, or runtime file.

The exact inputs recompute to:

```text
22f2e3dcb3922f89ea0afc0b4d8c6a1e529620b0b6230bc0fc2bc5224efb6c66  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_9_CORRECTION.md
d5e1d4dbd7731bd6a154c423b36f41e60de771d5ff635423b608bba02d88640f  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md
3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md
991c7389d528f21d6361a8566432ff295bffeb52e7a564c2961db3015e3d0fab  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_9_closure.md
88efa91dcb9142483cab6f832088ee3d19c51eb79ba20335deb84e005ea90a46  reviews/sol_officina_p1_watchdog_v2_8_final_y_confirmation.md
```

## Answers 1–7

### 1. Is Y28-B1 closed in all four parts?

**No.** Three parts are closed, but the fourth retains two contrary governing
sentences.

- `IR-3` now assigns both install-record id equalities to `CK-12` alone. Its
  explanation correctly says that the `CK-11` recomputation does not exist at
  `CK-8` and that `CK-12` is the sole owner.
- Every missing M4 key has one earlier answer: `CK-8` `S4`,
  `MEMBER_SUBSTITUTED`. Row 111 expressly fails a fixture expecting a later
  `STAGE_A_*` code.
- `CK-13` is a total, disjoint and literally ordered partition. D1 compares the
  69 `(class,path)` pairs index by index and precedes D2; D2 is reachable only
  after exact D1 agreement and then compares recorded digests in index order.
- The operative `VP-2`, `VP-3`, `VP-4`, and `CK-10` lists enumerate the intended
  nine M4 semantic relations. But `MS-4` still says that `CK-7 requires
  equality` of `reachable_closure` with the canonical value, even though
  `CK-7` precedes M4 structural validation at `CK-8`. The concluding sentence
  of `MS-12` also says that `CK-10` evaluates **exactly eleven** rows not owned
  by `TS-2B`, contradicting the same section's explicit `3 + 9 + 9 = 21`
  partition and `CK-10`'s exact nine-item list. These are governing ownership
  statements, not merely a harmless visualization.

The first contrary sentence recreates an undefined prerequisite: a literal
implementation cannot value-compare `reachable_closure` at `CK-7` before M4
has been proved parseable, object-shaped, exactly keyed and correctly typed at
`CK-8`. It also permits a factually wrong closure to be considered before the
earlier-by-contract `CK-9` Stage-A relations. Y28-B1 is therefore not globally
closed.

### 2. Is retiring `MEMBER_EXTRA` coverage-preserving?

**Yes.** Under the fixed structural cardinality, the retired code has no
disjoint state.

- A 70th record entry, with or without a stale digest or another replacement,
  fails at `CK-6` because the record is not a structurally valid 69-entry
  object.
- A structurally valid 69-entry record containing an unenumerated path must
  displace at least one enumerated `(class,path)` pair and therefore fails D1
  with `MEMBER_SUBSTITUTED`.
- A replacement plus any stale digest still fails D1 first. D2 cannot run while
  a D1 disagreement exists.
- Only when all 69 pairs agree can a wrong recorded digest reach D2 and produce
  `MEMBER_STALE`.
- An unrelated file not named by the literal enumeration or the record is not
  a member. The formerly tested extra-member state added the entry to the
  record/class accounting; it is covered by the cardinality/D1 cases above.

Thus combined extra/stale/replacement states do not reopen a gap or create two
first codes.

### 3. Is Y28-B2 closed?

**No.** The four necessary project modules are correctly identified, their
reviewed byte digests are correct, their import edges and execution order are
pinned, and `CK-10` is told to recompute their digests from the installed bytes
before any production entry point. The governing text also correctly keeps
them outside the five roots, M1..M7, `root_source_sha256`, and the 89-row
standard-library closure.

The new value is nevertheless not implementable as specified. `MS-13` defines
each element of `project_import_dependencies.modules` as an object with
**exactly five keys**:

```text
module, path, sha256, project_imports, stdlib_seeds
```

`MS-13.1` then says that each module asserts eight named booleans as false and
that all 32 assertions are part of that value. No key or nested object in the
exact schema can carry those booleans. `CK-8` is required to reject every extra
key, while `CK-10` and row 111 are required to compare/toggle the absent
assertions. Consequently there is no canonical JSON value that both satisfies
the exact-five-key shape and serializes the 32 asserted values. The digests and
order are bound; the claimed effect-assertion part is not identified in bytes.

The source-only audit also understates the import-time calls in
`interlock.py`: `@dataclass(frozen=True)` evaluates a decorator-factory call
and applies the returned decorator at import, in addition to `_TOKEN =
object()`. Those calls do not demonstrate any of the eight forbidden effects,
so this factual correction is implementation-log-only; it does not cure or
worsen the missing schema.

### 4. Is Y28-M1 closed?

**No.** `IR-4` is prominently relabelled non-exhaustive, declares `IR-13`
normative where the two differ, and defines its quotienting rule: relations
between the same object pair are combined, and `TS-2`/`TS-5` clause subjects
are drawn at the objects constrained. That part is an honest usable quotient,
subject to stale wording logged below.

`IR-13`, however, is not exhaustive under its own declared scope. It says a
relation is in the table iff a scoped check can refuse on it, including every
object-to-literal relation evaluated by `TS-2A` and `TS-5`. An otherwise valid
Stage A with `author` unequal to the literal `Kirill Kruglov` is refused at A6,
and one with `signature_algorithm` unequal to `Ed25519` is refused at A7, but
neither relation has an `IR-13` row. The same omission exists for, among other
literal checks, Stage-A schema/version (A4/A5) and Stage-B schema/version,
member-count literal and signature algorithm (B4/B5/B7/B10). By contrast the
table includes the comparable option-token, literal-path and threat-model
relations at rows 43, 45 and 46.

The boundary is internally inconsistent as well: it excludes intra-object
consistency constraints and gives A9 as the example, yet row 44 includes the
intra-object A11 relation between `StageA.key_id` and its own
`public_key_hex`. This is not a forty-seven-row exhaustive quotient of the
declared sixteen-section range. It is a Major relation-accounting defect in the
new normative surface.

### 5. Is Y28-R closed at the owning loci?

**Yes.** Composite `§P1-3.2` withdraws the obsolete claim that excluding the
pure-Python `signal` wrapper can make `_thread` absent and replaces it with the
measured, control-ownership rationale. The same owning locus states the
subprocess history in the correct order: the accepted generic-harness chain did
grant the subprocess/`start_new_session`/`killpg` launcher; the later signed P1
architecture superseded it with the bound `_posix_spawn` route and the
operative prohibitions; removal from this scoped allowlist is the later
bookkeeping consequence, not a retroactive denial of the accepted grant.

### 6. Are all preserved boundaries carried without narrowing?

**Yes.** Direct byte and locus checks establish:

- The amendment has exactly one strict v2.9 `§A0.4` anchor line. Its value is
  `3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad`,
  exactly the SHA-256 of the v1.9 composite. It remains an acyclic cross-file
  commitment, not freshness or rollback resistance.
- The complete `MS-11.1` literal region is byte-identical to v1.8. The 89-row
  standard-library value, 14-row bootstrap subset, exact equality rule,
  canonical length/digest, and `MS-11.6` prospective new-generation freeze are
  carried.
- The current-generation/fixed-chain/proper-subset qualifiers and both rollback
  residuals remain: `TR-2(a)` full-chain substitution and `TR-2(b)` complete
  coherent rollback. `FS-1`..`FS-5` retain the one-instant final-state proof,
  non-reconstruction, operator obligation, contemporaneous refusal and
  undiscovered-procedure residual. Row 106(i) still requires **PASS** for a
  fully restored earlier valid generation.
- B14 remains a signed Stage-B-to-Stage-A selected-option equality at `CK-14`.
- All 20 W-A/W-B variant-bearing lines are byte-identical to v1.8 (13 W-A
  markers and 13 W-B markers across those lines). Neither option is selected;
  W-B remains the recommendation on the same criteria.
- Signed identity Option A remains external author state only, outside M1..M7
  and the install record; the bounded-weakening token remains unaccepted.
- `T = NOT_ACTIVATED` and `PROGRAMME CLAIM = OPEN`. No implementation,
  activation, key, Stage A/B artifact, signature, manifest, record, candidate,
  trajectory, datum, outcome, Proof, or programme-claim movement occurs.

These preserved boundaries do not repair the new authority and accounting
defects above.

### 7. Does any Critical/Major defect remain?

**Yes. Three Major defects remain.**

#### Blocking counterexample A — contradictory `reachable_closure` owner

Start from an otherwise valid final byte state. Make M4 structurally valid but
give it a self-closed, well-typed and factually wrong `reachable_closure`; also
make Stage A disagree with one well-formed M4 binding field. Re-canonicalize
both objects and coordinate all later digests/signatures as needed to reach the
gate.

The literal `VP-4` order requires `CK-9` to return the applicable `STAGE_A_*`
code before `CK-10` considers the closure. `MS-4` instead assigns closure
equality to `CK-7`, before M4 structural validation and before `CK-9`, while
`MS-12` separately gives an incompatible eleven-row count. A verifier cannot
implement both governing instructions, and two implementations can select a
different first locus/code or encounter an undefined read. This is a Major
fail-closed and authority defect.

#### Blocking counterexample B — no byte representation for effect assertions

Construct `project_import_dependencies` exactly as `MS-13` defines it: two
top-level keys and four module objects with exactly the five named keys. The
result contains no bits for any of the 32 effect assertions, so `CK-10` cannot
compare them or run row 111's `true` fixture. Add any direct boolean key or an
`import_time_effects` object and the module object no longer has exactly five
keys, so `CK-8` must refuse it structurally. No byte state satisfies both
requirements. This blocks a deterministic M4 implementation and leaves the
new effect-accounting claim unidentified.

#### Blocking counterexample C — `IR-13` omits a refusable scoped relation

Take an otherwise valid canonical Stage-A object and change only `author` to
`"Mallory"`. A6 necessarily refuses with `STAGE_A_MALFORMED`, yet no `IR-13`
row represents that object-to-literal relation even though `IR-13` says a
relation appears iff a scoped check can refuse on it. The same construction can
be made at A7 or B10. Thus row 115 cannot honestly audit all relations against
the claimed exhaustive table, and the normative relation accounting required
to close Y28-M1 is absent.

## Implementation-log-only notes

The following should be corrected in the same documentation repair but do not
independently determine this verdict:

1. `MS-4` and `VP-3` still call the now 21-key M4 a twenty-key manifest in
   several sentences.
2. Despite the new non-exhaustive heading and precedence rule, `IR-4` still
   introduces `THE ACTUAL GRAPH, COMPLETE`; `TR-1` says `IR-4 states the
   complete directed integrity graph`; and composite `§P1-14.5` repeats that
   `IR-4` is complete. The explicit quotient/precedence rule and row 115 make
   those stale labels non-operative, but they should be removed rather than
   left to contradict the owning correction.
3. `IR-13` row 7 maps the one record-cardinality relation to two conditional
   codes while the following prose says every row has exactly one code. `CK-5`
   makes the zero-versus-multiple behavior executable, so the table should
   split the cases or qualify the count claim.
4. Correct the `interlock.py` import-time call inventory to include dataclass
   decorator evaluation/application; the observed calls still do not satisfy
   any forbidden-effect predicate.

## Authorization and next boundary

This verdict authorizes **nothing**: not Kirill's watchdog author selection,
not either watchdog option, not implementation, not creation of a key or Stage
A/B artifact, not signing, testing, installation, activation, or scientific
movement.

The next permissible boundary is one bounded documentation-only repair that:

1. removes every contrary `CK-7`/eleven-row M4 ownership statement and leaves
   one nine-relation `CK-10` authority;
2. defines an exact canonical JSON location and shape for all 32 project-module
   effect assertions, then reconciles `MS-13`, `CK-8`, `CK-10`, `IR-13`, and
   row 111 to that value; and
3. re-derives `IR-13` from its stated scope, including or expressly and
   consistently excluding every self-contained literal and intra-object
   relation.

The repaired identical bytes then require bounded independent X/Y review.
