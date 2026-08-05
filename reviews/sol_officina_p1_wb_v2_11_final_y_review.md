# Officina P1 W-B v2.11 final Y review

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Reviewed commit:** `d27376538c77317116ca1cb48b631edeb0ec84d3`  
**Review mode:** bounded adversarial review of `R1`..`R6` and inert-scaffold
eligibility. The closure was treated as untrusted. W-B was treated as signed and
not reopened.

## Verdict

```text
REVISE_OFFICINA_P1_WB_V2_11
```

Three demonstrated Major defects meet the requested revision threshold: one
fail-closed termination defect in `SC-2`/`SC-6`, one executable `KG-1` defect
coupled to an unsupported `KG-2` derivation claim, and one identifiability /
quarantine defect in the Cell-2 transformation and `PO-9` oracle contract.

## Input and scope verification

All six pinned inputs recomputed to the task-supplied SHA-256 values. Commit
`d273765` adds seven files: the five successor drafts, the closure, and
`reviews/opus5_officina_p1_wb_v2_11_governing_repair_chat_response.md`. The
worktree contained pre-existing unrelated modifications and untracked files;
none was used as authority and none was modified by this review.

The canonical handoff regions extracted by whole-line delimiters are
byte-identical and hash to
`ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785`.
The joint regions are byte-identical and hash to
`9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5`.
Each true begin/end delimiter occurs exactly once per file; the quoted examples
do not satisfy whole-line equality.

## Major blockers

### M-1 — `KV_FORBIDDEN_TARGET` does not dominate earlier skips

`SC-6` requires first-failure evaluation in `KV-1` through `KV-6` order.
`SC-2` goes further and admits to the scope sequence only candidates already
satisfying `KV-1` and `KV-2`. Therefore a current-table entry whose recorded
group is a forbidden target but whose role/state/ownership causes `KV-2` to
fail is skipped before `KV-6` is evaluated. A later valid candidate can still
reach `_killpg`.

Concrete tuple: a current-generation `CONTROLLER`, `RUNNING`, `CONTRADICTED`,
with a non-null `pgid_or_null` equal to the recorded supervisor group, plus a
valid controller candidate naming another group. `SC-2` drops the first handle
at `KV-2`; no `KV_FORBIDDEN_TARGET` token or whole-classifier terminal is
produced; the second controller remains signalable. This contradicts `SC-6`'s
statement that a
handle table naming any protected group has unknown provenance, its statement
that `KV_FORBIDDEN_TARGET` dominates every other token, row 89's required
whole-classifier termination, and Q3's required dominance over every skip.

This is a Major fail-closed defect in the sole W-B endpoint-loss executor. A
pre-pass over every table entry for forbidden targets, or another unambiguous
ordering that makes the terminal condition dominant, must be specified and
tested.

### M-2 — `KG-1` cannot return `PRESENT_VALID` on a normal Linux stat line; `KG-2` is not derived by its cited clauses

`KG-1` identifies the first token after the final `)` as the process state and
then classifies a “non-integer state” as `UNPARSABLE`. The Linux stat state
field is a single state character, not an integer. Thus every ordinary
`/proc/<pid>/stat` observation fails the stated parser, `KG-2` can never
legitimately populate `pgid_or_null`, and the classifier cannot authorize a
group signal. This is an executable definition defect, not a prose nicety.

The source trace is also not honest for `KG-2`. The cited current clauses
establish that the handle has a `pgid_or_null` field, that group signalling
requires a kernel-verified group, and that bootstrap `c10`/`c11` verifies and
records the middle/supervisor group. They do not state that every handle begins
with this field null, that exactly one generic handle-table write site exists,
or that the complete legitimate population is all and only current-generation
child group leaders. Those are new normative rules needed by the repair, not
logical consequences of the cited clauses. Calling `KG-1` the only supporting
rule the live pair lacked is therefore false.

The repair must make the state-field grammar correct and either derive `KG-2`
from actual current clauses or identify it honestly as newly supplied governing
content within the licensed repair boundary.

### M-3 — the claimed byte-exact transformation and `PO-9` are not identifiable

Binding §2.2 covers the important marker-free Cell-2 assertions, but it does
not specify replacement bytes. Its purported line-by-line actions also overlap
physical lines: line 58 contains both the blocking sentence and the common fact
to retain, and line 60 contains both the common fact and “What remains open”.
The contract supplies only semantic properties `CT-1`..`CT-6`, so two
implementers can emit different post-selection bytes while each claims
conformance. That conflicts with the “byte-exact” label and handoff `R-2`'s no-
design-discretion rule.

`PO-9` is likewise not mechanical. `D1` and `D2` require closed normalized
phrase lists held in the oracle, but neither draft enumerates the literal lists
or gives a total derivation algorithm. “Derived from” the Cell-2 span does not
choose pattern boundaries; `D2` is stated only as semantic categories and
exclusions. Implementations can therefore disagree on false positives and
false negatives. This is load-bearing because `G-10` detects markers only and
`PO-9` is the claimed control for marker-free open-cell prose and rejected W-A
grants.

Until literal replacement bytes and literal normalized detector tables (or an
equally total byte algorithm) are pinned, the oracle is not eligible even as
the proposed inert scaffold and cannot provide the claimed quarantine check.

## Literal answers to closure §10 Q1–Q10

**Q1 — YES, with a log correction.** Both delimited regions are byte-identical,
the hashes and delimiter cardinalities are correct, quoted delimiters fail
whole-line equality, and no surviving sentence was found that extends the
cross-file identity claim beyond those two regions. The reported “4052 bytes”
and “222364 bytes” are Unicode character counts; the actual UTF-8 byte lengths
of the hashed contents are 4061 and 222736.

**Q2 — YES.** The three surviving exact `CK-1`..`CK-12` occurrences per file
are historical descriptions or explicit negations. The operative range is
fifteen checks. Given the fixture's single changed field, `CK-2` and `CK-3`
through `B13` do not compare the cross-stage option value, `CK-4`..`CK-13` do
not compare it, and `B14` at `CK-14` is the first and only refusal with
`STAGE_B_OPTION_MISMATCH`. Placing the fixture in the already shared joint
block avoids changing the `MS-6`/`MS-7` row membership.

**Q3 — NO.** `SC-7`'s ordered arithmetic does partition the 72 signed tuples as
`24+32+4+6+6`, stale generation is separately named, `SC-8` has no default-
allow branch, and per-signal fresh re-verification is stated. But the forbidden-
target terminal does not dominate earlier `KV-1`/`KV-2` skips, and the
`KG-1` parser prevents ordinary `PRESENT_VALID` results. The current definition
is therefore not the claimed total executable fail-closed classifier.

**Q4 — NO.** Reading the third token from the already read stat buffer is
smaller than binding `_getpgid` and does not by itself change the allowlists,
the 89-row closure, `MS-13`, or `S-12`. However `KG-1`'s state grammar is wrong,
and `KG-2`'s null initialization, unique write site, immutability, and complete
population rule are not derivable from the cited `c10`/`c11` bootstrap-record
clauses. `KG-1` is not the only missing supporting rule.

**Q5 — NO, due to one surviving dependent literal.** All eight added digests
and paths recompute correctly. `MS-2` has 63 unique correct rows; the provenance
region has 71 unique correct rows; `MS-8`, `TS-3`, `B7`, and `B17` use 77 in
their operative definitions. The one-update treatment and retention of the
v2.10 pair-confirmation reviews are correct. Amendment §A11 `N-16`, however,
still says “`MS-8`'s member cardinality is 69”. This is a Minor stale count
because the executable algorithm and gates consistently use 77, but the claim
that every dependent literal moved is false.

**Q6 — NO.** The table reaches the marker-free blocking notice, open-mechanism
sentence, W-A exposition, and selects-neither assertion; the marker census,
class-R retention of TS-1 vocabulary and the CK-14 token, guard-data retention,
and supervisor/watchdog slot-6 distinctions recompute correctly. But the
transformation supplies no exact replacement bytes, and `PO-9` supplies no
literal `D1`/`D2` pattern table or total pattern-generation algorithm. It
therefore cannot establish the claimed false-positive/false-negative boundary.

**Q7 — YES, report rather than silently repair; MINOR.** `H-4` wrongly names
`CK-12`; `CK-7` is explicitly the sole owner of `HISTORICAL_BYTE_MOVED`, while
`CK-12` owns install-record id equalities. The operative joint block and test
matrix make the true owner unambiguous, and the wrong citation does not omit the
actual `CK-7` refusal. Log it for the next governing maintenance/replacement
round, and repair it before any `OR-5` verifier implementation is authorized.

**Q8 — NO overall.** The handoff honestly narrows itself to an inert oracle and
declarative data, correctly removes the three tests that had no implementation
under test, keeps process/runtime work excluded, and `D-4` is a legitimate pure
synthetic-table test. The later-stage table preserves distinct scaffold,
runtime, and one-shot permissions. Nevertheless the oracle is not scaffold-
eligible because its Cell-2 output and `D1`/`D2` pattern constants are not
identifiable without new design choices.

**Q9 — YES.** No identity-observation code or schema is introduced;
`attested_pid` and `attested_pgid` are absent from both governing files; the
Option A weakening remains unaccepted; this is not the `XS-1` combined binding;
and that combined binding remains blocked. Recording Cell 1 as binding-ledger
gate 0, without altering the composite outside the licensed governing repair,
is the correct scope disposition.

**Q10 — YES, at one non-governing commit locus.** The substantive governing,
binding, and handoff changes otherwise trace to `R1`..`R6` and forced
accounting, and the commit changes no code, tests, signatures, or runtime
artifacts. But commit `d273765` also adds
`reviews/opus5_officina_p1_wb_v2_11_governing_repair_chat_response.md`, while
closure §2.2/§9.4 and that chat response say exactly six files were created and
nothing else. This seventh file is outside the declared six-deliverable scope.
It is non-governing and graded a log/scope-accounting error, not an additional
Major authority defect.

## Implementation-log notes

1. Correct the UTF-8 region byte lengths to 4061 and 222736; the hashes are
   already correct.
2. Correct amendment §A11 `N-16` from member cardinality 69 to 77 in the next
   authorized governing replacement.
3. Correct canonical `H-4` from `CK-12` to `CK-7` in that round, before verifier
   implementation.
4. Resolve the retained stale “finished replacement for v1.2” wording when
   literal Cell-2 replacement bytes are pinned.
5. Reconcile the commit's seventh chat-response file with the closure's
   exactly-six scope claim.

## Exact next boundary

The next act is a bounded governing/binding repair on new reviewed bytes. This
review authorizes no acceptance consideration, implementation, inactive
scaffold, key, entropy, Stage A, Stage B, `OR-3`..`OR-11`, install, activation,
identity weakening, or programme-claim movement. After repair, both independent
lines must review the same new bytes. Only a later passing independent round may
authorize Kirill to consider the v1.8 amendment acceptance token; that later
consideration would still authorize none of the excluded acts.

`T = NOT_ACTIVATED`. Programme claim `OPEN`.
