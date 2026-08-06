# X review — Officina executable-contract migration charter v1 (draft)

**Reviewer:** Claude Code Opus 5, independent X line. Read-only, architecture
review. This memo is normative for nothing; the signed tokens and signature
files govern.

**Verdict:**

```text
OFFICINA_MIGRATION_CHARTER_V1_X_ACCEPTED_FOR_BOUNDED_REVISION
```

The authority graph is sound and worth signing: acyclic, one manifest, no
self-hash, no fixpoint, generated-is-not-authority, and a stopping condition the
charter binds itself to. That skeleton survives this review intact. Four
structural claims built on it do not survive as written — §1.3's "Class B
eliminated by construction", §4.1's independence claim, §5's M2/M3 gate
closure, and §6.1's budget arithmetic. Each fails in a bounded, repairable way
with replacement text supplied below; none requires a new charter. Nine edits
are marked **mandatory before T-2**, and T-4 must not be signed until they land,
because M1 and M2 would otherwise be built against an inventory this review
shows to be incomplete.

`T = NOT_ACTIVATED`; `OR-2` complete, `OR-3`..`OR-11` **NOT AUTHORIZED**;
programme claim = `OPEN`. No token is authorized by this review.

---

## §0. Input verification

Both reviewed objects recomputed. Both reproduce exactly.

```text
e9f9f641adec0d826f3c974f2e2e6ec14d184758ce933457b1949e9e7b9cd3f9  successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_DRAFT.md   OK  (35,994 B)
879d9c34aba2d8ff57c45e1fc1a29978bac627d672912b7a637a08eda8bf7d36  reviews/fable_officina_executable_contract_migration_charter.md        OK  (16,334 B)
```

**Commit note, not a finding.** The task pins commit `9e93df5`; the working tree
is at `07f4fd5`. Both reviewed files are byte-identical at `9e93df5`, at
`07f4fd5` and in the working tree — verified by `git show 9e93df5:<path> |
sha256sum` for each. `07f4fd5` adds only the two review prompts and touches
neither reviewed object. The review therefore covers the intended bytes and is
**not `BLOCKED`**.

**Output of this review:** `reviews/fable_officina_migration_charter_v1_x_review.md`
— exactly one file created, no other file modified. This file contains none of
its own digests (§2.1(4)).

Corroborating bytes read but not modified: the v2.15 X and Y confirmations, the
v1.15 composite's `§P1-15 (6B)`, and `src/philosophia/officina/**` file sizes
and symbol lists.

**The memo is an author self-assessment and is treated as untrusted.** Where it
is right I say so; §X2 below overturns one of its recommended defaults on
textual evidence it did not cite, and §X4 finds an arithmetic defect it did not
reach.

---

## X1 — independent semantic oracle

### X1.1 The charter's claim is inverted

§4.1 says the ordered machine and the guard-row predicates "are both generated
*from the same source declaration* and cross-checked, so agreement is a test,
not a coincidence of two transcriptions."

This is backwards. Two transcriptions agreeing **is** the evidence, precisely
because it is not guaranteed; two projections of one declaration agreeing is the
tautology. Independence is a property of *provenance*, not of *count*. The v2.15
X confirmation had force because a misreading of the prose in the ordered form
would not reproduce itself in the row form. Collapse both onto one declaration
and the pair agrees by construction, and agrees just as readily when the
declaration is wrong.

The memo's X-1 identifies this correctly. I confirm it and go further: as
written, §4.1 does not merely weaken the oracle, it **removes** it. After
migration the prose is gone, so there is no longer any second reading of a
shared source to be independent about. Independence must be re-anchored to
something outside the declaration or it does not exist at all.

This does **not** rise to `REVISE`. §4.7 already concedes, honestly, that
whether the extracted invariants are the right ones is "Not [bounded] by tests,
ever" — bounded instead by the equivalence ledger, M4 and M5. The defect is that
§4.1's sentence claims an independence that §4.7 correctly disclaims. One
overclaiming sentence, repairable.

### X1.2 The three candidates, assessed

**(a) Canonical implementation + independently hand-written test oracle.**
**Reject in its literal form.** If the "oracle" is a second full transition
relation, it is a maintained duplicate of every governing fact: each M2 fix must
be made twice, the two copies can diverge, and reconciling them is a repair
round. That is the Class-B/D shape re-imported into Python, and §6.1's
zero-duplicated-literals budget would be fighting it. The idea survives only if
the oracle is made **strictly weaker** than the relation — see O1 below.

**(b) Declarative transition table + independently coded evaluator.**
**Accept as the implementation style; reject as the oracle.** A generic
evaluator contains no facts, so coding it independently checks nothing about the
table's content — it is an interpreter, not an oracle. But as a *structure* it
is the best of the three: the table is the single home of the facts, the
evaluator is fact-free, route counts become `len(...)` over the table, and
§6.1's duplicated-literal test acquires real teeth.

**(c) One generated projection + one M4-only disposable transcription from
generated documentation.** **Accept as the independence mechanism.** The
transcription's provenance runs through `generated/CONTRACT.md` only, never
through `contract/`, so it is genuinely outside the declaration. It is paid once
and discarded, so it creates no maintained duplicate and no second live
authority.

### X1.3 Recommendation — (c), amended, with (b) as the implementation style

Smallest architecture that retains a real oracle:

**Live authority — exactly one.** `contract/data/kg2_routes.json` holds the
guarded-row transition relation; `contract/machines.py` holds a fact-free
evaluator over it. This is the only object that governs.

**Demote, do not delete, the projection pair.** Keep the ordered/row agreement
check but re-label it in §4.1 a **generator and ordering test**, not an
independence check. It retains real value — `X15-M2` was exactly a step-order
versus row-order disagreement — but what it tests is the ordering algorithm, not
the semantics.

**O1 — standing weak property oracle (test-only, permanent).** Hand-written from
I-1..I-18, in `tests/test_officina_contract_properties.py`, phrased as
constraints over enumeration *outputs*, never as an alternative route function.
Examples of the required form: at most one write across any evaluation; no write
on any combination whose licensing conjunction is false; `role = WATCHDOG`
implies `pgid_or_null` is NULL on every combination; zero signals on every table
containing a protected target; no observation before its authority gate. Because
each is strictly weaker than the transition relation, O1 duplicates no governing
fact and **cannot become authority** — it can only refuse, never define.

**O2 — M4-only disposable transcription (one-time).** The M4 X reviewer codes an
independent evaluator from `generated/CONTRACT.md` alone, never opening
`contract/`, enumerates the full product, and diffs the route vector. The result
is recorded in the M4 review file. The code is **not** committed to `contract/`,
is **not** a `MANIFEST.json` member, and is **never** re-run in CI.

### X1.4 Live authority / test-only, pinned

| Object | Status |
|---|---|
| `contract/data/kg2_routes.json`, `contract/machines.py` | **Live authority.** The only transition relation. |
| `contract/data/kg2_dimensions.json` | **Live authority.** See X2. |
| Generated ordered/row projection pair | **Generated.** Documentation and generator test. No authority. |
| O1 property oracle | **Test-only.** Weaker than the relation by construction. Never a MANIFEST member. |
| O2 M4 transcription | **Test-only, disposable.** Lives in `reviews/`. Never re-run. |
| `EQUIVALENCE_LEDGER.md` | **Archival**, as §3.1 already states. |

### X1.5 Drift detection without duplicating governing facts

`render.py` emits into `generated/CONTRACT.md` one derived block: per-route
counts over the full declared product, per-route counts over the feasible
subset, the write count, and `sha256` of the canonical route vector. Every value
is `len(...)` or a digest computed at render time — no hand-typed figure, so
§2.1(5) is respected.

Consequence: any semantic change to the table moves one generated line;
`verify.py --check` forces the re-render or the suite is red; the diff is a
one-line review tripwire that no reviewer can miss and no author can suppress.

**M4 staleness detector.** The M5 signature names the route-vector digest that
O2 agreed with. If a later change moves that digest, the independence evidence
is stale *by construction*, and re-transcription is required before the next
signature. This is a pinned expectation whose **mismatch is the signal**, which
is categorically different from a derived fact asserted as authority. The two
are separated automatically because the guards of X3 are scoped by location:
they govern `contract/**` and `tools/**`, and the pin lives in a signature file
and a test.

---

## X2 — unresolved KG-2 enumeration semantics

### X2.1 The memo's proposed default is not available

The memo's X-2 asks whether M2 should "adopt the clause-1 reading (6 writes), the
reading the composite's own preamble and write-count clause support". Two
clauses do support it — `P-10`'s preamble ("no combination is excluded in
advance") and `(x2)` ("the number whose full conjunction holds", and the `W7`
conjunction does not name EINTR).

But a third clause, which the memo does not cite, points the other way. The
composite's required-fixture clause `§P1-15 (6B)(v)` reads, on its own bytes:

> `EINTR` … retry through the deadline must produce `ERROR` inside the ONE
> observation and take `R-E`'s `ERROR` sub-row.

That is the forcing reading, stated in the clause that defines the *required
build fixture* — the most operative position in the document. The published
closure's counts (`R-E` 560, writes 4) follow it. So the textual evidence is
split 2–1 across clauses of unequal operative weight, not 2–0 as the memo
implies. **There is no majority reading available to adopt, and M2 must not
adopt one by preponderance.**

### X2.2 The ambiguity is an artifact of a wrong factorization, not a semantic dispute

Working from the X line's own published table
(`reviews/fable_officina_p1_wb_v2_15_final_x_confirmation.md`, the measured
comparison at its `X15-M1`; I did not re-enumerate — there is no executable
machine to run, and this charter authorizes me to build none):

```text
                       R-E   R-F  R-G  R-H   writes
clause 1 (non-forcing) 552    12    6     6        6
clause 2 (forcing)     560     8    4     4        4
```

The two readings differ on exactly 8 tuples, and the X line records what those
tuples are: they assert *both* that the observation was retried through the
deadline *and* that `KG-1 = PRESENT_VALID`. They are self-contradictory. Under
clause 1 they sit in `R-F`/`R-G`/`R-H` (4+2+2); under forcing they sit in `R-E`.

Restrict both readings to the tuples that are not self-contradictory and the
divergence vanishes:

```text
feasible subset only   552     8    4     4        4      (568 tuples)
```

**Both readings assign identical routes to every realizable combination.** The
4-versus-6 write divergence is entirely a disagreement about whether to *count*
impossible tuples. There was never a semantic dispute about the machine.

The reason the prose needed a forcing rule is now visible: `P-10` declares
KG-1 result and EINTR as two independent dimensions, but they are not
independent — "retried through the deadline" *determines* `KG-1 = ERROR`. The
declared cross-product is not a product. `(x4)` clause 2 exists to patch that,
and patching a bad factorization with a prose rule is what produced two
conforming builds publishing different counts.

### X2.3 Recommendation — encode; do not choose, and do not expose a choice

**M2 must not adopt a reading, and must not expose a bounded author choice.**
Both would inherit an ambiguity that has a correct structural resolution.

1. **Collapse the mis-factored pair into one sum type.** Replace the
   (`KG-1 result` × `EINTR`) dimension pair with a single tagged
   `ObservationOutcome` whose variants include `PRESENT_VALID`, `ABSENT`,
   `UNREADABLE`, `UNPARSABLE`, `PRIMITIVE_FAULT`, and
   `ERROR_DEADLINE_EXHAUSTED` (reached after `§P1-10.3`'s bounded EINTR retry).
   The 8 impossible tuples cease to exist as expressible values. `(x4)` clause 2
   is **deleted**, not interpreted.
2. **Derive both counts.** `render.py` emits per-route counts over the full
   declared product *and* over the feasible subset, plus the write count. No
   figure is written by hand anywhere.
3. **Assert totality over the full product; publish over the feasible subset.**
   Exactly-one-route is asserted across every declared combination — fail-closed
   demands that even an unreachable input route deterministically — while the
   published counts are the feasible ones. Because both numbers are emitted,
   there is nothing left to choose.

Under this encoding the write count is **4**, agreeing with the published
closure, but derived rather than forced — and reached without adopting the
forcing prose the other two clauses contradict. That is the outcome the charter's
own thesis predicts, and it is the strongest single piece of evidence for the
route.

### X2.4 The dimension set as a reviewed executable object

Required, and the charter must say so. `contract/data/kg2_dimensions.json` is a
live-authority MANIFEST member, an M4 review object in its own right, and the
sole declaration of the product. `machines.py`'s transition input is a frozen
dataclass whose field set is checked equal to the declaration's key set.

### X2.5 The exact gate that detects a missing dimension

Four mechanical parts. All four are required; the fourth is the one that would
have caught `(x4)`.

- **G-DIM-1 — single declaration.**
  `set(f.name for f in fields(Kg2Input)) == set(dimensions.keys())`. A dimension
  cannot exist outside the declared input type.
- **G-DIM-2 — read-coverage.** Run the full enumeration with the input wrapped
  in a recording proxy that logs every attribute read. Assert
  `reads_observed == declared_dimensions`: every declared dimension is consulted
  on at least one combination (no dead dimension), and no attribute outside the
  declared set is read. An access to an undeclared name raises, and the raise is
  a hard failure with no fallback branch.
- **G-DIM-3 — closure.** AST assertion that transition functions reference no
  free name other than their parameters, `contract.constants` bindings and the
  stdlib allowlist. No dimension may enter through a module global, the
  environment, a clock or an import.
- **G-DIM-4 — product faithfulness.** Assert the declared product contains **no
  infeasible combination**: the feasibility predicate over the declared
  dimensions must be identically true. A non-empty infeasible set is a
  *declaration defect* — a wrong factorization to be collapsed into a sum type —
  never something to be patched by a rule. This is the exact check that turns
  the `(x4)` class of defect into a red suite at M2 instead of a Minor finding
  at generation 15.

**What the gate cannot do, stated plainly.** G-DIM detects a dimension the
machine consults but did not declare, a declared dimension the machine ignores,
and a pair of dimensions that are not independent. It cannot detect a
distinction that is absent from *both* the machine and the declaration. That
residue is irreducibly human. But the gate bounds it precisely: the remaining
question is "is there a distinction present in the signed sources and absent
from `kg2_dimensions.json`?", which is a finite diff against I-1..I-18 performed
once at M4. §4.7's fourth bullet ("an undeclared dimension is invisible") should
be replaced with that bounded statement rather than left as an open concession.

---

## X3 — template theorem and crash-cut boundary

### X3.1 The theorem is unsound as stated, and the hole is larger than the memo admits

The memo's §2.5(1) concedes the template layer is uncovered and calls it "the
charter's weakest point". That concession is correct but understated. The defect
is in **L1 itself**, not only in the templates.

L1 claims `contract/**` "contains only declarations", so "a count typed into a
source file is read by no template and therefore reaches no live surface: it is
dead text, not authority."

Both halves fail. Templates *do* read `constants.py` — that is their purpose. A
hand-typed cardinality in `constants.py` is syntactically indistinguishable from
a protocol constant: `ROUTE_COUNT = 9` and `STAT_SUFFIX_FIELDS = 50` are the
same construct, and nothing in the architecture stops `render.py` from
interpolating the first. So a derived fact **does** have a writable home in
source, and it **does** reach a live surface.

Therefore §1.3's table entry for Class B — "**Eliminated by construction.** §2
and §6.2 give the argument: the architecture provides no location in which a
human may type a derived fact" — is **false as written**. Class B is eliminated
*modulo two guards that the charter does not specify*. This is the single most
important correction in this review, because Class B is the charter's entire
justification.

**Answering X3's first question directly: yes.** `render.py` and its templates
can today contain hand-typed counts, digests, paths, generation identifiers and
authority claims, and so can `constants.py`. Nothing refuses any of them.

### X3.2 Is an AST/token guard sufficient? No — and here is what is

A blocklist over an unbounded prose surface is always evadable: `COUNT = 2 * 4`,
`int("8")`, or the word "six" spelled out in a template sentence all pass a
literal scan. Sufficiency requires **three** rules of different kinds, scoped by
location.

**G-TPL — allowlist, not blocklist, over `tools/officina_contract/**`.** No
literal in the generator layer may reach output except structural chrome. AST-walk
every literal that flows to an output-writing call or a template body; permit
only Markdown layout characters (`^[\s#|:>\-*\`\[\]().,'"/]+$`) plus a declared
heading vocabulary that contains no digit, no path separator, no number word and
no authority verb. Everything with semantic content must arrive as an
interpolated name bound in `contract/**`. This is the form that closes the prose
hole, because it makes the permitted set finite instead of enumerating an
infinite forbidden one.

The forbidden literal classes G-TPL necessarily excludes, stated for the test's
error messages:

| Class | Shape |
|---|---|
| `L-DIGEST` | `^[0-9a-fA-F]{7,}$` |
| `L-COUNT` | any `int` literal ≥ 2 outside a loop or slice index; any English number word |
| `L-PATH` | any string containing `/` that resolves under `successor/`, `src/` or `tools/` |
| `L-GEN` | `(?i)\bv\d+(\.\d+)*\b`, `_V\d+(_\d+)*`, `generation \d+` |
| `L-AUTH` | `(?i)\b(govern|authoritative|supersed|replac|normative|accepted|signed)\w*` |

**G-SRC — citation rule over `contract/**`.** Every literal bound at module
scope must either be a member of a declared collection, or carry a
`# PROTOCOL: <path>#<section>` comment whose path resolves to an existing file.
This is how legitimate protocol constants are distinguished from derived facts —
**by mandatory resolving citation, not by value**. `E1 = 168`, descriptor slot
`6`, the exactly-50 stat suffix fields, the nine state characters and the seven
closed `SC-5` tokens all survive: they are cited. `ROUTE_COUNT = 9` has no
signed source to cite and dies.

**G-CARD — value comparison, not AST.** The one rule that must be semantic:
import `contract/**`, and for every declared collection `C`, assert that no
module-scope binding holds a value equal to `len(C)`. This catches `2 * 4`,
`int("8")` and every other computed cardinality that AST inspection cannot see.

AST for shape, evaluated values for cardinality, allowlist for prose. Any one
alone is insufficient; the three together make §1.3's Class-B claim true rather
than aspirational.

### X3.3 Can generated Markdown introduce authority the source does not encode?

**Yes, and §2.1(2) does not stop it.** §2.1(2) says a disagreement between
`CONTRACT.md` and `contract/` is a test failure. But a test can only detect
disagreement about facts the source *encodes*. A template sentence asserting
something the source is silent about — "this contract supersedes the prose
line", "amendment v1.12 remains a live authority surface" — has nothing to
disagree with, passes every test in §4, and reads to a human as authority. That
is `Y15-M1` reconstituted inside the new architecture.

**Fix: templates emit layout, never sentences.** Every normative sentence in
`CONTRACT.md` is emitted from a `NORMATIVE_TEXT` mapping in
`contract/constants.py`, making it a declared fact, a MANIFEST member and an M4
review object. Plus a generated, non-editable header, itself emitted from
constants: *"Generated from `contract/`. Documentation only, not authority. If
this disagrees with `contract/`, `contract/` governs and the suite is red."*
With that rule, §2.1(2) becomes structurally true.

### X3.4 The crash-cut / `canonical.py` deadlock — confirmed, and worse than stated

Verified against the tree. `src/philosophia/officina/canonical.py` is 103 LOC and
defines exactly the three primitives §4.5 puts under test — `fsync_directory`
(line 43), `atomic_create` (line 51), `atomic_replace` (line 77). §5's M3 allows
edits to `contract/**`, `tools/officina_contract/**`,
`successor/officina/generated/**` and new test files only. §7's disposition table
does **not** classify `canonical.py` at all: it is neither salvage, nor extracted
invariant, nor untouched-by-reference. And §3 contains no invariant governing
durability, so the primitives are tested against nothing declared.

So M3 is required to test code it may not edit, against an invariant that does
not exist, in a file the charter does not classify. If the test fails, M3's
terminal-failure list ("the generator is not deterministic … or the verifier
passes a perturbed copy") does not cover it, M3's gate cannot close, and M6 —
the first package permitted to touch `src/` — is gated behind an M5 acceptance
of a contract whose suite is red. That is a genuine unclosable gate.

### X3.5 Recommendation — record an M6 blocker; do not expand M3

**Do not expand M3.** Granting M3 edit rights over `src/` merges contract scope
with implementation scope, which is precisely the coupling M6 exists to resolve;
and §5.1 makes M3 the Cursor-eligible package, so expansion would place routine
delegated work adjacent to production durability code, which §5.1 does not
contemplate and should not.

Fail-closed route, four parts:

1. **Add I-17** (durability and atomicity at the persistence boundary), so the
   invariant has a home and M6 has a named target. See X4.4.
2. **§7 gains a row** classifying `src/philosophia/officina/canonical.py` as a
   *dependency under observation* — not a member, not salvage, not extracted by
   copy; M3 may import and test it, M3 may not edit it.
3. **§5 M3 gains:** "A §4.5 failure attributable to `src/**` is **not** an M3
   terminal failure and **not** grounds to expand M3's edit rights. M3's gate may
   close only when each such failure is committed as
   `pytest.mark.xfail(strict=True)` naming the I-n it violates and an M6 blocker
   id." Strict xfail is what makes this fail-closed rather than a waiver: the
   suite is green while the defect stands, and the moment the defect is fixed the
   test fails as XPASS, forcing the marker's removal. The blocker cannot be
   silently forgotten, and it cannot be silently resolved.
4. **§5 M5 gains:** the acceptance signature must state the number of open
   strict-xfail durability blockers, **derived** from a test-collection run and
   not hand-typed, so the figure itself cannot drift.

---

## X4 — complexity budget and semantic completeness

### X4.1 The budget is internally inconsistent — arithmetic

§6.1 caps `contract/**` at **2,500 LOC and 120 KiB** jointly, and `contract/data/**`
at **64 KiB**. Measured against this repository's own density —
`src/philosophia/officina/**` is 7,349 lines in 305,045 bytes, **41.5 B/line**,
with per-file values from 28 (canonical.py) to 43 (accounting.py) — the three
caps are not jointly satisfiable:

```text
2,500 LOC × 41.5 B/line          ≈ 103,750 B  ≈ 101.3 KiB
120 KiB total                    =  122,880 B
remaining for contract/data/**   ≈   19,130 B ≈  18.7 KiB   (29% of its declared 64 KiB cap)

conversely, with data/** at its declared 64 KiB cap:
(122,880 − 65,536) / 41.5        ≈ 1,382 LOC              (55% of the declared 2,500 LOC cap)
```

At most two of the three caps can ever bind. A build that spends its declared
data budget may write only ~1,382 LOC; a build that writes 2,500 LOC may spend
only ~29% of its declared data budget. Under §6.3 this is not a repairable
finding but a §6.2 event, so it must be fixed before signature, not after.

**Recommended fix: delete the 120 KiB aggregate cap.** Keep 2,500 LOC across
`contract/**/*.py` and 64 KiB across `contract/data/**` as the two binding caps.
A byte cap on source optimizes exactly the wrong thing — it penalizes the
docstrings and the `# PROTOCOL:` citations that G-SRC (X3.2) *requires*, and
citations are the mechanism by which protocol constants are distinguished from
drift. A charter should not price its own safety rule as overhead.

### X4.2 Is 2,500 LOC credible for the inventory?

Yes, with roughly 15–20% headroom, **but only under an exclusion the charter
does not currently state**. Estimating by component: constants (12 dimensions, 9
routes, 7 `SC-5` tokens, 9 state characters, ~20 negative boundaries, pinned
kernel assumptions with citations) ≈ 400–600; schemas ≈ 400–600; machines
(KG-2 evaluator plus the six-phase classifier) ≈ 600–900; parser grammar ≈
200–300 — total ≈ 1,600–2,400. Credible, provided the 40 published parser
vectors live in `data/` as JSON rather than in Python, and provided I-16..I-18
are added *now* rather than discovered at M4.

The exclusion that must be stated: §6.1's justification sentence — "the contract
is a specification of one subsystem and must be smaller than the subsystem" —
implies whole-subsystem coverage, which §3's closed 15-item inventory does not
provide and 2,500 LOC could not deliver against 7,349 LOC of implementation
(`generic_harness.py` alone is 2,380 LOC). **§3 must state that the contract
specifies the control plane — I-1..I-18 — and not the harness's data-plane
behaviour**, and §6.1's justification must be rewritten to match. Otherwise M6
will discover an I-19..I-n that §3 declares out of bounds, which forces a
charter amendment at exactly the moment the 21-day clock is tightest.

### X4.3 Separate ledgers — yes, four

The budget must **not** be one number. Four ledgers:

| Ledger | Cap | Rationale |
|---|---|---|
| `contract/**/*.py` | 2,500 LOC | Authoritative source. Binding. |
| `contract/data/**` | 64 KiB | Declarations, not code. Binding. |
| `tools/officina_contract/**` | **400 LOC (new)** | X3 shows this is the highest-risk surface; the G-TPL allowlist is only auditable if the layer is small enough to read in one sitting. |
| `tests/**` and the O1/O2 oracles | **Uncapped, explicitly excluded** | Capping tests creates pressure to under-test, which inverts the charter's purpose. |

**§6.1's "12 live files under `contract/`" is ambiguous** about whether
`data/*.json` counts. With constants, schemas, machines, `__init__`, plus
dimensions, routes, parser vectors, classifier fixtures and negative boundaries
as data, 12 is reachable but leaves ~4 slots for eighteen invariants. Restate as
**6 Python modules + 8 data files**, counted separately.

**Mandatory interaction fix.** §6.1's "Duplicated string literals across live
surfaces — **0**, enforced by a test — the Class-B kill switch" would, if "live
surfaces" is read to include tests, **forbid the O1 and O2 oracles outright**,
since restating expectations independently is their entire function. The kill
switch must be scoped explicitly to `contract/**` ∪ `generated/**`, with a
sentence stating that test and oracle code are exempt **and required** to
duplicate. As drafted, the charter's Class-B kill switch destroys the Class-A
oracle.

### X4.4 Missing invariants M6 would necessarily need

Three. Each is a surface §4 already proposes to *test* while §3 declares no
invariant to test it *against* — the clearest possible signature of an
incomplete inventory.

**I-16 — canonical `/proc/<pid>/stat` parse grammar.** One `STAT_PARSE` grammar
and one `PGRP_OBSERVE`, with no consumer-local grammar; the closed nine-character
state set; exactly 50 suffix fields; rejection of sign bytes, leading zeros,
embedded whitespace, shifted/extra/missing fields, overflow, and `pgrp = 0`;
`PRIMITIVE_FAULT` taking the structural-violation continuation; and the published
`V0`..`V39` vector corpus with its results. Source: composite `§P1-10.3` and
`§P1-10.7`. §4.2 proposes property- and mutation-testing "the parser, the
canonicalizer and the framing code" — a surface with roughly forty published
adversarial vectors that **no I-n in §3 governs**. Without I-16 the property
tests have no specification and M6 has nothing to reconcile the harness's parse
code against.

**I-17 — durability and atomicity at the persistence boundary.** Record-first
ordering, atomic create/replace semantics, directory fsync, and the crash-cut
invariant that a reopened boundary shows either the pre-state or the post-state
and never a torn one. Source: the existing `canonical.py` primitives plus the
composite's record-first clauses. This is the invariant §4.5 tests and §3 omits,
and it is what X3.5 requires to exist before M3's gate can close.

**I-18 — deadline and interruption semantics.** The one-observation rule;
`§P1-10.3`'s bounded EINTR retry; deadline exhaustion producing `ERROR` inside
the single observation; and — per X2.3 — the sum-type relationship between
interruption and observation result, so the two are never declared as
independent dimensions again. This is a precondition for M2 to encode the KG-2
input type at all; without it, M2 either re-derives the factorization informally
or inherits `(x4)`.

Not proposed as separate invariants, but flagged for M1's attention: `SC-10`'s
full multi-fault dominance matrix and the closed seven-token `SC-5` set are
operative objects that I-9 and I-10 cover only in part. They should be pulled in
as sub-items of I-9 rather than discovered at M4.

---

## Mandatory edits before T-2

Bounded replacement decisions, not a new charter. T-4 must not be signed until
these land: M1 and M2 would otherwise be built against an inventory this review
shows to be incomplete.

| # | Locus | Edit |
|---|---|---|
| **E1** | §1.3, Class B row | Replace "**Eliminated by construction.** §2 and §6.2 give the argument: the architecture provides no location in which a human may type a derived fact" with "**Eliminated by construction, conditional on the G-TPL, G-SRC and G-CARD guards of §4.4.** Without those guards a derived fact has a writable home in `constants.py` and in the template layer." (X3.1) |
| **E2** | §4.1, ¶2 | Delete "so agreement is a test, not a coincidence of two transcriptions." Re-label the projection pair a **generator and ordering test**. Add O1 (standing weak property oracle, test-only) and O2 (M4-only disposable transcription from `generated/CONTRACT.md` alone). (X1.3) |
| **E3** | §4.4 | Add G-TPL (allowlist over `tools/**`), G-SRC (`# PROTOCOL:` resolving-citation rule over `contract/**`), G-CARD (evaluated-value `len(C)` comparison), and the rule that **templates emit layout, never sentences** — all normative prose emitted from a `NORMATIVE_TEXT` mapping in `constants.py`. (X3.2, X3.3) |
| **E4** | §3 | Add **I-16** (canonical stat/`PGRP_OBSERVE` grammar and `V0`..`V39`), **I-17** (durability/atomicity), **I-18** (deadline and interruption semantics). State that the contract specifies the **control plane**, not the harness data plane. (X4.2, X4.4) |
| **E5** | §4.1, §5 M2 | Require the sum-type collapse of the (`KG-1 result` × `EINTR`) pair; delete `(x4)` clause 2 rather than interpret it; emit full-product **and** feasible-subset counts, both derived. M2 adopts no reading and exposes no author choice. (X2.3) |
| **E6** | §4.1, §4.7 | Add the G-DIM-1..4 gates, with G-DIM-4 (product faithfulness) mandatory. Replace §4.7's fourth bullet with the bounded statement of what remains human. (X2.5) |
| **E7** | §5 M3, §5 M5, §7 | `canonical.py` classified as *dependency under observation*; a §4.5 failure in `src/**` is not an M3 terminal failure and not grounds to expand M3; strict-xfail plus named M6 blocker id required before M3's gate closes; M5's signature states the derived open-blocker count. (X3.5) |
| **E8** | §6.1 | Delete the 120 KiB aggregate cap. Keep 2,500 LOC (`contract/**/*.py`) and 64 KiB (`contract/data/**`). Add a 400 LOC cap on `tools/officina_contract/**`. Restate the file cap as 6 modules + 8 data files. Rewrite the "smaller than the subsystem" justification to match §3's control-plane scope. (X4.1, X4.2, X4.3) |
| **E9** | §6.1, duplicated-literal row | Scope the kill switch to `contract/**` ∪ `generated/**`; state that test and oracle code are exempt from it and required to duplicate. (X4.3) |

**Logged, not mandatory.** (i) The memo's §2.4 attributes `Y15-M1`'s elimination
to L5 (generation identifiers); it is more precisely eliminated by §2.1(1)'s
single-authority rule, since `Y15-M1` is a multi-surface delegation defect rather
than a version-string defect. (ii) §1.2 cites `X15-M1` and `X15-M2` as
"representative live instances" of Class A; the X line graded both **Minor**,
which §1.1 states correctly — no inconsistency, recorded for the reader. (iii)
§6.1's "2 review rounds per work package" interacts with M4, which is itself a
review package; worth one clarifying sentence.

**Out of X scope, referred to the Y line.** The memo's Y-1 (signature digest
blocks outside the theorem) and Y-3 (whether T-1 mandates or merely authorizes
the archive move, given §7, §5 M0 and T-1 read differently). I take no position.

---

## Negative space

This review created exactly one file: `reviews/fable_officina_migration_charter_v1_x_review.md`.

Nothing else was modified, moved, staged, committed or deleted. No governing or
historical document, no signature, no code, no test, no runtime artifact, no
prior review and none of the dirty or untracked working-tree work was touched —
the two uncommitted modules and the modified test files remain exactly as found.
No commit was made and no branch was created.

No contract module, schema, fixture, generator, verifier, manifest or test was
created. No machine was executed and no cross-product was enumerated: the route
tables in X2.2 are read from the X line's published `X15-M1` comparison and
arithmetic performed on it, not re-derived from an implementation. No
Philosophia production module was imported or executed — `canonical.py` was read
for its symbol list and line count only. No `/proc` was read; no socket, pipe,
FIFO or descriptor was opened; no `fork`, `exec`, `signal`, `wait` or `prctl` was
called; no clock was sampled for any contract purpose. No key, entropy, seed or
world was generated. No E1/E2/E3 was spent.

This review predicts no Y-line verdict and no scientific outcome. It reopens no
signed science, designs no v2.16, and demands no copied historical prose. It
asserts no acceptance: amendment `v1.12` remains not accepted,
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` remains not accepted, and the X
line's v2.15 confirmation is neither completed nor withdrawn by anything here.

This file contains none of its own digests.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
WATCHDOG AUTHORITY AMENDMENT V1.12 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

---

## Exact next boundary

The Y line's review of the same charter bytes, independently. Nothing in this
memo is an input to it.

Then, and only then: the author's consideration of **E1..E9 as a bounded
revision of the charter's §1.3, §3, §4.1, §4.4, §4.7, §5, §6.1 and §7**. The
revision touches no signed science and adds no new route; it makes the charter's
own Class-B claim true, restores an oracle the draft removes, and closes one
unclosable gate.

After the revised bytes exist: T-1, T-2 and T-3 are considerable. **T-4 is not
considerable until E1..E9 land**, because M1 and M2 would otherwise be
implemented against an inventory known to be short three invariants and a
budget known to be arithmetically unsatisfiable.

No token is authorized by this review.
