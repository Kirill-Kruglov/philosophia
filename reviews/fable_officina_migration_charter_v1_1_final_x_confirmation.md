# Final X confirmation — Officina executable-contract migration charter v1.1

**Reviewer:** Claude Code Opus 5, independent X line. Read-only except for this one review
file. This memo is normative for nothing; the signed tokens and signature files govern.

**Verdict:**

```text
OFFICINA_MIGRATION_CHARTER_V1_1_X_CONFIRMED
```

No Critical or Major semantic defect remains. The candidate is ready for Kirill's author
decision on T-1, T-2 and T-3, with T-4 separately and afterwards under §10.4's own
constraint.

Every X mandatory edit `E1`–`E9` lands, and where the Y line was stricter the charter took
Y. The four architectural claims that did not survive round 1 — the Class-B "eliminated by
construction" table, §4.1's inverted independence sentence, the unclosable crash-cut gate,
and the jointly unsatisfiable budget arithmetic — are gone, and none returns in a renamed
form. What replaced them is honest about its own limits: §2.6 disclaims what the theorem
does not cover, §4.4 states the bounded human residue instead of conceding an open one,
§5.5 names what tests cannot prove, and §2.4 declares the trust root as a premise rather
than pretending to an in-repository proof of its own checker.

The findings below are Minor, non-normative and non-blocking. Each has a determinate
resolution available from the accepted bytes, or a named fail-closed destination inside the
charter (`§3.2` blocked slot, `§5.4(3)` scope extension, `§8.3` named-limit route decision,
`§8.3` redesign trigger). None of them lets a semantically wrong contract reach M5 green
while the charter claims it cannot, which is the only thing that would defeat the route.

`T = NOT_ACTIVATED`; `OR-2` complete, `OR-3`..`OR-11` **NOT AUTHORIZED**; programme claim =
`OPEN`. No token is authorized by this review.

---

## §0. Input gate

The candidate was recomputed before substantive review and reproduces exactly:

```text
3266a18f4584e14297c886529c51f57ef20a47719a636b5101c001967c2cdb5e
  successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md   OK
```

Byte-identical at the pinned commit `28a3189` and in the working tree, verified by
`git show 28a3189:<path> | sha256sum`. The live checkout is `6a7ab84`, of which `28a3189`
is an ancestor; the single intervening commit adds only the two final-confirmation prompt
files and touches no reviewed object. **Not `BLOCKED`.**

Corroborating repository facts inspected read-only, never modified: every `§3.3` path alias
(all thirteen resolve); `CAND-C`'s heading structure and the bodies of `§P1-10.3`,
`§P1-10.7`, `§P1-11.7` and `§P1-15`; `CAND-B`'s heading structure; the three P1 signature
files in full; `src/philosophia/officina/canonical.py`'s symbol list and line count; and
line/byte totals under `src/philosophia/officina/**`.

**The closure is an author self-assessment and is treated as untrusted.** Where it is right
I say so; §X8 rules against its own ranking on two of the five items it nominated.

**Independence note.** `reviews/sol_officina_migration_charter_v1_1_final_y_confirmation.md`
exists untracked in the working tree. I did not open it. This review reads no Y-line
evidence and predicts no Y verdict.

**Output:** exactly one file created,
`reviews/fable_officina_migration_charter_v1_1_final_x_confirmation.md`. It contains none of
its own digests.

---

## X1 — Semantic authority: one live relation, weak O1, disposable O2

### X1.1 The boundary holds, and the charter states its own limit correctly

`contract/data/kg2_routes.json` plus a fact-free evaluator in `machines.py` is the sole
governing object; route and write counts are `len(...)` over the table; the ordered/row
projection pair is demoted to a generator and ordering test with the v1 sentence deleted.
That is `E2` landed exactly, including the concession I asked for: "Two projections of one
declaration agree by construction, including when the declaration is wrong."

**Can two conforming implementations disagree semantically with every named gate green?**
Yes — and the charter says so rather than hiding it. §2.6's second paragraph disclaims
"correctness of the primary author choices, since a wrong primary fact can be green", and
§5.5 places atom correctness under "the equivalence ledger, M4 and M5, never by tests". The
gates check derivation and internal consistency, not correspondence to the signed sources.
This is not a defect; it is the honest shape of the problem, and v1's error was claiming
otherwise. The relevant question is whether the human boundary is *bounded and named*, and
§4.4's closing paragraph plus §5.5 do bound it.

### X1.2 O1 cannot become authority; the constraint on it is prose, not a gate

O1's construction is sound: constraints over enumeration outputs, never an alternative route
function, each strictly weaker than the relation, so it can refuse but never define.
§4.2's "Divergence between O1 and the relation is a finding, not an authority conflict" is
the correct disposition, and §6's M2 gate requires O1 green, so a divergence reds the suite.

**Residue.** Nothing mechanical enforces strict weakness. §7 exempts test and oracle code
from the duplicated-literal ledger and *requires* it to duplicate — which is `E9` correctly
landed and is necessary for O1 to exist at all — but the same exemption removes the only
mechanical pressure against O1 growing into a maintained second relation over successive
M6 cycles. The charter's protection is §4.2's normative phrasing rule plus M4 review of a
test file. That is adequate for M2–M5 and is worth watching afterwards. Non-blocking.

### X1.3 O2's provenance is genuinely outside the declaration

An M4 reviewer codes an evaluator from `generated/CONTRACT.md` alone, never opening
`contract/**`, enumerates the declared product and diffs the route vector once; the result
lives in that reviewer's review file, is never committed to `contract/**`, never a manifest
member, never re-run. That is `E2`'s (c) landed intact, and it is the only object in the
architecture whose provenance runs outside the one declaration. Its scope is the KG-2 route
vector and nothing else; the classifier, the parser grammar and the schema families get
§5.1's exhaustive assertions against the declaration plus M4's human read. The charter does
not claim otherwise. Sound.

---

## X2 — Closed dimensions: `ObservationOutcome` and `G-DIM-1..4`

### X2.1 The bypasses tested, and how each resolves

| Attempt | Result |
|---|---|
| **Destructuring** — evaluator reads `inp.__dict__` or `astuple(inp)` once, then works on the copy | `G-DIM-2` goes **red**, not green: observed reads become `{__dict__}`, which is not equal to the declared dimension set. Fail-closed. The closure's §7.4 worry is inverted — the proxy defeats the destructuring evaluator, not the reverse |
| **Positional access / iteration** | Same disposition: any access path that is not per-field attribute reads produces an observed-read set unequal to the declared set |
| **Defaults** — a frozen-dataclass field default lets enumeration skip a value | The declared product comes from `kg2_dimensions.json`'s value sets, not from constructor defaults, so §5.1 enumerates the declaration regardless. No effect |
| **Infeasible products** | `G-DIM-4` requires the feasibility predicate to be *identically true*. That is a ratchet against the `(x4)` defect class: it forbids retaining an infeasible region and patching it with a rule, forcing the sum-type collapse instead. Correct, and it is exactly the check that turns generation-15's Minor finding into a red M2 suite |
| **Unregistered dimension** | `G-DIM-1` (field set = key set) plus `G-DIM-4`'s register-equality clause |
| **Globals / environment / clock / import** | `G-DIM-3`'s AST closure — **with one carve-out, below** |

### X2.2 Minor — `G-DIM-3`'s `contract.constants` carve-out

`G-DIM-3` permits transition functions to reference "their parameters, `contract.constants`
bindings and the stdlib allowlist". A module-scope constant that is *consulted as a
condition* rather than compared against an input field is therefore a machine-consulted
dimension that is declared nowhere: it is not a field of the frozen input type
(`G-DIM-1` blind), not an attribute read on the input (`G-DIM-2` blind), an allowed free
name (`G-DIM-3` blind), and not an A-0 atom (`G-DIM-4` blind). `G-SRC` requires it to carry
a resolving `# PROTOCOL:` citation, but `G-SRC` checks that the cited section *exists*, not
that it says what the constant claims.

§4.4's closing sentence says "a dimension the machine consults but does not declare fails at
**M2 or M4**." My counterexample does not fail at M2. It does fail at M4, because §4.1
characterises `machines.py` as a **fact-free** evaluator and an evaluator branching on a
module constant is not fact-free — and `machines.py` sits inside a 2,500-line hand-reviewed
surface with M4 review as a named gate. So the sentence is true as written, via its second
disjunct only. **Non-blocking**, and worth stating plainly so M4 knows this is its job and
not the gate's: the "fact-free" property is normative and ungated.

### X2.3 `G-DIM-2` admits a read-but-unused dimension

Read-coverage proves consultation, not use. `_ = inp.role` with `role` never influencing the
route passes `G-DIM-2`, and §5.1's exactly-one-route assertion is indifferent to a dimension
that partitions nothing. The consequence is an *inflated* declared product, never a missing
distinction, so the direction of the residue is safe. Non-blocking.

### X2.4 `§4.3` — the sum type is right, and its sixth variant is mislabelled

I confirm the structural resolution in full. The `(KG-1 result × EINTR)` pair is not a
product; the divergence between the two published write counts is entirely about counting
self-contradictory tuples; both readings agree on every realizable combination; and
collapsing to one sum type makes the impossible tuples unrepresentable, deletes the forcing
clause rather than interpreting it, and exposes no author choice. Publishing the full
sum-type population and the feasible counts as `len(...)` values, with the charter fixing no
figure, is `E5` landed exactly.

**One labelling defect, and the register is what catches it.** `CAND-C`'s `R-E` sub-rows
partition `KG-1`'s **six disjoint result classes**: `PRESENT_VALID`, `ABSENT`, `UNREADABLE`,
`UNPARSABLE`, `ERROR`, `PRIMITIVE_FAULT`. The source is explicit that deadline exhaustion is
not its own class — `ERROR` is "**ALSO** where `W4`'s deadline exhaustion after `EINTR`
retry arrives, and it arrives as an observation result and not as a route of its own". §4.3
names its sixth variant "error-after-deadline-exhaustion", which is strictly narrower than
`ERROR`. Read literally, an ordinary non-deadline `ERROR` observation would have no variant:
a reachable outcome class escaping the sum type, with §5.1's "never zero" vacuously
satisfied because enumeration never presents the state.

That reading is not available, and the arithmetic is what forecloses it: six variants against
six disjoint `KG-1` classes is a bijection, and a genuinely narrower sixth variant would need
a seventh for plain `ERROR`. A-0's closure rule — "one atom per dimension **and per value**"
over `CAND-C` §P1-10 — puts an `ERROR` value-atom in the register, and `G-DIM-4`'s
register-equality clause then forces the declared variant set to denote it. **The closed
inventory constrains the machine here exactly as intended**, which is the best available
evidence that §3's register does real work. The label originates in my own round-1 `E5` text
and v1.1 implemented it faithfully; it is a naming imprecision with a determinate
denotation, not a lost class. Non-blocking.

### X2.5 Minor — `G-DIM-4`'s register clause versus §4.3's mandated collapse

`CAND-C`'s published cross-product declares **twelve** dimensions, `KG-1 result` and `EINTR`
among them. §4.3 mandates that those two become one. A-0's source-derived atom set therefore
carries twelve dimension-atoms while the declared dimension set carries eleven, and
`G-DIM-4`'s "the declared dimension set equals the A-0 atoms in the register" cannot be a
raw equality. A-18's Content cell carries the exception — "the §4.3 sum-type relation, which
forbids re-declaring these as independent dimensions" — but A-0's cell does not, and A-0 is
the family `G-DIM-4` names.

Read whole, the charter determines the adjustment completely: §4.3 fixes both the collapsed
pair and the resulting variant set, and A-18's atom states the constraint, so the comparison
is A-0-as-constrained-by-A-18 with no degrees of freedom. Read as raw equality, `G-DIM-4`
is unsatisfiable and M2's gate cannot close. The harmonizing reading is the only coherent
one and is available from the accepted bytes. **Non-blocking**, and the sharpest of the
register-boundary notes: it is where M2 will first feel §3.3's cell-level imprecision.

### X2.6 Is read coverage plus AST closure plus product faithfulness mechanically sufficient?

For the failure classes it was built against — a missing dimension, a dead dimension, an
illegally independent pair, a dimension entering through the environment — yes. For a
distinction absent from both the machine and the declaration, no, and §4.4 says so and
bounds the residue to one finite diff against the atom register at M4. The one gap the gate
text does not cover is X2.2's constants carve-out, which lands on M4 rather than M2.

---

## X3 — Atom closure: is the register a real closed inventory?

This is the charter's load-bearing claim and the closure's own second-ranked worry. My
answer: **the derivation is genuinely mechanical in structure, and four of the twenty Source
cells are imprecise enough that M1 will have to raise them.** The imprecision is bounded, it
is visible at M1's own gate, and every route out of it is fail-closed. It does not defeat
the closure claim, but it is where the migration will first cost time.

### X3.1 What is genuinely closed

Testing the closure rules against the actual sources, family by family, the mechanism works
where the source is a signature:

- **A-1** over `SIG-W` — "one atom per named capability and per named negative capability"
  derives cleanly: two sealed liveness pipes, no freeze-request socket, slot 6 closed; the
  EOF five-fold negative (sends, writes, freezes, signals nothing; exits); and the six named
  negative capabilities of the fourth bullet. Mechanical, no judgement.
- **A-2** over `SIG-P` — five forbidden primitives named literally (`fork`, `Popen`,
  `waitpid`, `kill`, `killpg`) plus the authority edges. Mechanical.
- **A-13** over `SIG-I`/`SIG-CH` — the final `SIG-I` bullet enumerates the excluded
  destination classes directly. Mechanical.
- **A-5** — "exactly one atom; its value is a non-operative token", which is a closure rule
  that cannot yield anything but one atom. Correct, and it is the right way to keep an
  unaccepted token representable-as-unaccepted.

`G-ATOM`'s four checks — exactly one locator per atom, no shared locator-and-meaning, every
locator resolves, no closure-rule output absent from the register — are all mechanically
executable, and §3.2's blocked decision slot is the correct destination for a source clause
that admits more than one reading, with §6's M1 terminal failure firing if one is *chosen*.
That machinery is sound and is a genuine advance over v1's `I-1..I-15`.

### X3.2 Minor — A-17's Source cell is a search predicate, not a locator

§3.1 requires each atom to carry a primary locator of the form `<path>#<section>`, and fixes
the source set by the §3.3 table. A-17's Source cell reads "`CAND-C` record-first clauses;
`CANON` (observed, §5.3)". The first names no section: it is a predicate over a 9,027-line
document — *the clauses that are record-first* — and deciding which clauses those are is
editorial judgement performed at M1 against no stated rule. The second names an
implementation file that §5.3 classifies "**dependency under observation**: not a member,
not salvage, not extracted by copy" and that §7 forbids importing into authority.

A-17's own Content cell names "the crash-cut invariant that a reopened boundary shows the
pre-state or the post-state and never a torn one" — an object whose home in `CAND-C` is
§P1-11.7's crash-and-cut matrix, which no cell in §3.3 cites.

The closure rule carries part of the load: "one atom per persistence boundary and per
ordering constraint" pins the boundaries structurally, from the record schemas. The ordering
constraints do not have that anchor. This is the one cell where §3.1's own diagnosis of v1 —
"the v1 thematic list incorporated large unnamed sets by reference … That is closed here" —
does not hold of the replacement.

**Why it is non-blocking.** M1's gate condition is "every locator resolves"; its terminal
failure is "an atom has no single home". A-17's ordering-constraint atoms have no single home
under this cell, so M1 raises it rather than passing green — the gate detects its own
shortfall. The destinations are §3.2 (if M1 reads it as plural readings) or §5.4(3) (if
M1 reads it as a source addition). Both are fail-closed and author-visible; neither silently
amends anything.

### X3.3 Minor — A-9 and A-10 are sourced to `CAND-C`'s test matrix

A-9 ("classifier phases, terminals, precedence edges … the multi-fault dominance matrix and
the closed `SC-5` token set") and A-10 (stable tie-break, permutation invariance) both cite
`CAND-C` §P1-15. §P1-15 is titled **"The test matrix"**, and `CAND-C` states on its own bytes
that the classifier operates "under `KV-1`..`KV-6` and `SC-1`..`SC-10` **as defined in full
at §P1-10.7 and nowhere else**."

The consequence is concrete and executable. A-9's closure rule includes "one atom per …
dominance cell". §P1-15 row 89 enumerates **seven** same-phase pair rows inline while
*referencing* `SC-10`'s full dominance table without containing it; the table itself is at
§P1-10.7. Two M1 authors applying the same closure rule — one to §P1-15 as cited, one to
§P1-10.7 as `CAND-C` directs — produce registers differing by the whole of `SC-10`, and both
pass `G-ATOM`, because `G-ATOM` checks derivability from the section read, not coverage of
the object named. §P1-15 does supply the terminals, the qualifiers and `SC-5`'s seven tokens
directly (rows 89 and 101), so the cell is not empty — it is the *test* site rather than the
definition site.

**Why it is non-blocking.** §P1-10.7 is already inside the §3.3 source set (A-16 cites it),
so the correct derivation adds no source and triggers no §5.4(3) event. The divergence is
resolved by reading `CAND-C`'s own "and nowhere else" sentence, which is in the frozen
source. M4 reviews the register against the sources with §5.5 naming that as its job.

### X3.4 Minor — `G-ATOM` does not check locators against the §3.3 source set

§3.1's source closure is normative — "M1 may not add a source outside it" — but none of
`G-ATOM`'s four checks is source-set membership. A locator anywhere in the repository that
resolves passes. Atom closure is mechanically gated; **source closure is prose plus M4
review.** The charter does not claim otherwise, and an out-of-set locator is trivially
visible in review, but the two halves of "closed in both directions" are not equally
enforced and the asymmetry is worth knowing before M1 begins.

### X3.5 Verdict on atom closure

Closed enough to be a real inventory, not editorial interpretation relocated into a
generator. The families whose sources are signatures derive mechanically with no judgement.
The families whose sources are sections of `CAND-C` derive mechanically *once the section is
the right one*, and three cells point at the wrong or at no section. The judgement that
remains is bounded to those cells, is forbidden to Cursor by §6 ("Cursor may not … decide an
extraction boundary"), surfaces at M1's own gate rather than downstream, and has only
fail-closed exits. That is materially different from v1, where the same judgement was
invisible and had no gate at all.

---

## X4 — State-machine totality

### X4.1 What is covered, and covered well

- **Totality.** §5.1 asserts exactly one route over the **full declared product** — never
  zero, never two — while publishing feasible counts. Asserting over the full product is
  right: fail-closed demands that even an unreachable input route deterministically. Both
  numbers are emitted as `len(...)`, so nothing is left to choose.
- **Impossible states.** Unrepresentable by construction under §4.3, not excluded by a rule.
  `G-DIM-4` forbids re-introducing them and patching with a predicate.
- **Two enabled transitions.** §5.1's "never two or more" plus the ordered/row projection
  agreement test, which is the `X15-M2` defect class and is correctly re-labelled a generator
  and ordering test rather than an independence check.
- **Observation-only identity.** A-4 and A-13 over `SIG-I` derive the forbidden uses and the
  excluded destination classes directly. `SIG-I`'s "or otherwise control a process" is an
  open-ended catch-all whose executable test cannot be written without a reading — which is
  precisely §3.2's blocked decision slot, raised to the author, never a default. The
  machinery routes it correctly.
- **W-B peer-endpoint loss.** `SIG-W` bullet 3 states it operatively: the PCS detects
  endpoint loss, performs the record-first freeze classification and remains sole executor.
  A-1 and A-6 derive from it. `CAND-C` §P1-13.9's `[W-B]` trigger site and §P1-15 row 89's
  two-signed-execution-sites rule corroborate. Covered.
- **Deadline / interruption / recovery.** A-18 over §P1-10.3, with the sum-type relation
  explicitly forbidding re-declaration as independent dimensions. Covered.

### X4.2 Minor — `CAND-C` §P1-11 is in no family's Source cell

§P1-11 ("Records, crash cuts, terminals, invalidity") holds §P1-11.4 PCS loss, §P1-11.5
Stage-M terminals, §P1-11.6 invalidity routing, and §P1-11.7's 27-row crash-and-cut matrix,
each row a cut mapped to exactly one continuation. This is control-plane material — the §3.3
scope sentence excludes the harness *data* plane, not this — and three families name its
content: A-3 ("PCS loss as unrecoverable whole-generation process invalidity", sourced to
`SIG-P`), A-8 ("every structurally violating or undeterminable state has exactly one named
continuation", sourced to §P1-10), A-17 (the crash-cut invariant). No cell cites §P1-11.

A-8 is defensibly KG-2-scoped: its "and takes no write" clause is write-machine vocabulary,
and §P1-10.2's wait classifier plus KG-2's routes do supply continuation edges. A-3 over
`SIG-P` yields the *policy* (loss ⇒ unrecoverable whole-generation invalidity; no adoption of
a live generation) without §P1-11.4's transitions. So the register as sourced pins the
policy and leaves the crash-cut continuations — supervisor death with the PCS alive, PCS
death, crash between an ordered unlink and its `fsync`, `_recvmsg` raising, ancillary
violation, lost acknowledgement on a descriptor-bearing reply, unreaped watchdog — outside
contract scope.

**Why it is non-blocking.** §3.1 claims the source set is *fixed*, not that it is *complete*
over `CAND-C`, and §5.4(3) is the declared route for anything outside it: `M6_BLOCKED_NEW_INVARIANT`,
the accepted contract not edited, M6 unable to close, a separate future signed
scope-extension route required. Late discovery is therefore author-visible and fail-closed,
which is the designed behaviour. The cost is that this material surfaces at M6 rather than
at M1, and A-17's cell is the place where that boundary is least clearly drawn.

### X4.3 No outcome class escapes the sum type

Tested directly at X2.4. The one candidate escape — plain `ERROR` versus
error-after-deadline-exhaustion — is closed by the six-to-six correspondence with `KG-1`'s
disjoint classes and by A-0's per-value atoms. Nothing else in the declared product is
unrepresentable, and §5.1's exactly-one assertion over the full product forecloses both the
zero-route and the two-route failures.

---

## X5 — Migration feasibility: can the budgets contain the machinery?

### X5.1 The arithmetic reproduces, and the v1 defect is gone

Measured on this repository: tracked `src/philosophia/officina/**` is 4,969 physical lines in
199,150 bytes (**40.1 B/line**); including the uncommitted salvage work, 7,349 lines in
305,045 bytes (**41.5 B/line**). The closure's density figures reproduce.

v1's three caps were not jointly satisfiable — 2,500 lines at this density needs ~101 KiB of
the 120 KiB aggregate, leaving 29% of the declared 64 KiB data cap; conversely a full data
budget permits ~1,382 lines, 55% of the LOC cap. `E8` deleted the aggregate, and v1.1's caps
now separate cleanly:

| Ledger | Cap | Binding axis | Satisfiable |
|---|---|---|---|
| `contract/**` | 2,500 physical lines | lines only | Yes — no byte cap on source, so the axes are disjoint and cannot collide |
| `contract/data/**` | 64 KiB | bytes only | Yes — disjoint from the line cap |
| Non-test trusted base | 1,000 lines **and** 64 KiB | joint | Yes — permits 65.5 B/line, 47% above the densest file observed anywhere here |
| Generator / template layer | 400 lines | sub-cap | Yes, inside the 1,000 |

Taking Y's stricter physical-line counting over every regular file rather than X's
`contract/**/*.py` is the right call, and it does not threaten the line cap: canonical JSON
is emitted compact, so a 45 KB atom register is a small number of physical lines while
consuming most of the byte cap. The two ledgers bind on different files for different
reasons, which is what makes them separable.

### X5.2 Minor — the two reliefs for the trusted base are not independent

The closure is right that the trusted base is the tightest budget and honest that its
pessimistic sizing (~1,120 lines) exceeds 1,000. Of the two reliefs §7 already provides, the
first is clean — the `MF-1..MF-10` mutation fixtures are tests and §7 places tests outside
both ledgers explicitly. The second is not free: moving the template **grammar declaration**
into `contract/data/**` relieves the line budget by spending the 64 KiB data budget, which
the closure separately names as the budget most likely to bind first at M1 with the atom
register at 25–45 KB of it. The two tight budgets are coupled through that move.

This is not a defect. §7 enforces both limits mechanically before review, and §8.3 makes an
overrun a redesign event rather than a silent expansion — which is the correct behaviour and
is what v1 lacked. It is a scheduling risk worth naming: if the register lands at the top of
its range, the template-grammar relief is unavailable and the base must fit in 1,000 lines
unaided.

### X5.3 Normative semantics are not pushed into uncounted material

The exclusion is enforced structurally rather than by intent. §7 places generated docs,
tests and the oracles outside both ledgers while stating they carry **no primary authority**;
§2.3 requires every normative sentence in `CONTRACT.md` to be emitted from `NORMATIVE_TEXT`
in `constants.py`, which makes it a declared `PRIMARY` fact, a manifest member and an M4
review object; and `G-TPL`'s allowlist leaves a template sentence asserting an unencoded
claim with no place to live. Uncapped tests cannot become authority because §1.2(1) gives
every operative fact exactly one home in `contract/**` and `G-CARD` catches evaluated
cardinalities that AST inspection misses. §7's zero-duplicated-literal ledger is the
enforcement, and `E9`'s test exemption does not weaken it, because the exemption grants
tests permission to *restate* expectations, not to *hold* facts.

**One scope-wording note.** The ledger reads "0 across `contract/**` ∪ `generated/**`". Read
as comparing string *literals* — a source-code term, and Markdown prose contains none — it
is satisfiable and is the rule `E9` intended. Read as comparing any string appearing in both
sets, it is violated on every render by the generator's core function, since §2.3 requires
`CONTRACT.md`'s normative sentences to be copies of `constants.py` bindings. The first
reading is the only coherent one and is pinned by §2.3 and §1.2(7); no choice is left to M3.
Non-blocking.

---

## X6 — The M3/M6 boundary

### X6.1 The crash-cut gate is closed, and closed correctly

This was round 1's genuine unclosable gate and `E7` closes it exactly as X3.5 required.
`CANON` is classified **dependency under observation** in §9 and §5.3; M3 may import and
test the durability primitives and may not edit `src/**`; a crash-cut failure attributable
to `src/**` is explicitly **not** an M3 terminal failure and **not** grounds to widen M3's
edit rights.

The two required products are the right ones. `xfail(strict=True)` is what makes this
fail-closed rather than a waiver: the suite is green while the defect stands, and the moment
the defect is fixed the test fails as an unexpected pass, forcing the marker's removal — so
the blocker can be neither silently forgotten nor silently resolved. The blocker record
being *derived from the failing test's own collection output, never hand-typed* keeps it
consistent with §1.2(5), and §1.3's decision to have the release check **report** blocker
state rather than copy a count into the tag is the correct resolution of my `E7` against Y1's
prohibition — Y was stricter and the charter took Y.

I verified `canonical.py` against the tree: 103 lines, eight module-level functions with no
import-time side effects, including exactly the three primitives under test —
`fsync_directory`, `atomic_create`, `atomic_replace` — plus the `canonical_json` and
`sha256_*` helpers §1.4 relies on for its stdlib-only recommendation. §1.4's factual premise
holds.

### X6.2 Minor — M3's gate requires writing to a path M3's allowed-edit cell excludes

§5.3 requires the blocker record to be generated under
`successor/officina/migration/blockers/`. §6's M3 row lists allowed edits as
`tools/officina_contract/**`, `successor/officina/generated/**` and new
`tests/test_officina_contract_*.py`. `successor/officina/migration/**` is **M1's** territory,
not M3's, and M1's gate has closed by then. So M3's gate condition — "every crash-cut failure
carries a blocker and a strict xfail" — requires producing a file M3 is not permitted to
produce.

**Why it is non-blocking, and why the repair is free.** §10 carries tokens for T-1 through
T-4 only; T-4 authorizes M1 and M2 "and nothing else". M3 therefore requires a separate
future authorization act regardless of this finding, and that act is where M3's boundary is
stated. Fixing the path there costs nothing and amends no charter. Failing that, §8.3
supplies an explicit route — "Every other limit in this charter may be exceeded only by a new
author-signed route decision naming the limit, the new value and the reason" — which is
author-visible and is not silent expansion. The one thing that is *not* available is M3
quietly writing outside its cell, and §8.3 forbids exactly that.

A second, smaller residue: §5.3 presupposes the failing test *collects*, since the blocker is
derived from collection output. A crash-cut defect that errored at import would fall outside
both products. `canonical.py` imports cleanly and defines no import-time behaviour, so the
case is not reachable through the named dependency.

### X6.3 The three-way M6 rule cannot amend or expand the accepted contract

I attacked Case 2 ("consequence of an existing atom") as the closure invited, and the
attack fails in the direction that matters. Nothing mechanically separates Case 2 from
Case 3 — that classification is a judgement, and the closure is right that a deadline-pressed
implementer will over-use it. But the *consequences* are contract-neutral in all three
dispositions:

- Case 1 stays in `src/**` and its tests and "creates no contract authority";
- Case 2 yields "a derived test only. **No new primary atom**";
- Case 3 emits `M6_BLOCKED_NEW_INVARIANT` and "the accepted contract is **not** edited".

So **no classification, correct or mistaken, edits or expands the accepted contract.** A
Case 3 misfiled as Case 2 produces a test rather than a blocked-scope-extension signal —
under-reporting to the author, not contract corruption — and it does not touch §5.3's
independent rule that M6 cannot close while any blocker remains open. §5.4's closing
sentence is therefore earned: Case 3 "cannot amend this charter, reopen M1/M2, reset any
counter, or authorize integration", and that is what stops "charter amendment" from becoming
the renamed generation loop. Confirmed.

---

## X7 — Negative space

Each item verified against the candidate's own bytes.

| Surface | Disposition |
|---|---|
| **T activation** | `T = NOT_ACTIVATED` in the header block and in §11. §10.5 forbids it by name. §6's closing sentence: "Activation is separately authorized and is reachable from no token here." A-12 represents the interlocks as atoms rather than acting on them |
| **Scientific run** | §10.5 excludes every scientific specification, preregistration, world, learner, candidate, Q or C object, datum, outcome, Proof and claim movement. §11 confirms none occurred |
| **Entropy, seeds, keys** | Forbidden in §10.5; §11 states none was drawn; §5.2's one integration smoke test is explicitly bounded to "drawing no entropy, spending no `E1`/`E2`/`E3` and creating no runtime artifact" |
| **Production installation** | §10.5 excludes install, attestation, detached signature, Stage A, Stage B and install record |
| **Acceptance token** | §10.5 excludes acceptance of amendment `v1.12` and of `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`; §9's rows keep both not accepted; A-5 makes the weakening an explicitly unaccepted non-operative token rather than an omission; §9 closes with "**No candidate becomes accepted by implication**" and forbids converting the v2.15 X confirmation into acceptance |
| **Uncommitted salvage** | Triple-covered: §9's disposition row ("Salvage candidates only, untouched. No edit, commit, revert or deletion is authorized"), §7's exclusion from every budget and from M1/M2 authority, and §10.5's prohibition on editing it. §6's M6 is "planning and review only", so "M6 evaluates them" yields a plan, not edits |
| **Git objects** | §1.3: "**No Git object is created by this charter**, and §10 authorizes none." The release binding is a future gate |
| **Path moves** | §9's logical archive: "Every Git path stays exactly where it is", `NO_ACCEPTANCE_EFFECT`, and §10.1 redefines T-1's "archive" as classification rather than `git mv`. Y3's Major is fully absorbed |

**One consistency observation, not a finding.** M0's gate requires the generated path index
to classify "every path exactly once against the tree". The salvage modules are untracked and
so lie outside the tree; §10.5 forbids committing them; therefore they can never enter the
index for the life of this episode, and §9's disposition row is the only thing holding them.
That is coherent — the two rules compose correctly rather than colliding.

---

## X8 — Rulings on the five items the closure nominated

**1. `G-STALE`'s digest in the M4 review file — acceptable. Not a finding.** The closure
named this correctly as the single digest outside `MANIFEST.json` and asked the confirming
lines to rule. I rule for it, on four grounds. §1.2(4)'s prohibition is scoped by its own
words to **author-authored** files, and §1.3 confines author-authored acceptance material to
a token-only tag message; a reviewer's evidence file under `reviews/` is neither. The release
check **recomputes** the route-vector digest at the tagged tree rather than trusting the
recorded value, so the recorded digest has no authority in the green direction — it can only
cause refusal. That inverts `Y1-M1`'s failure mode: there, a stale copy stayed green; here, a
stale copy goes red, which is the definition of a pinned expectation whose mismatch is the
signal. And it lives outside `contract/**` and `generated/**`, so `G-PROV`(7)'s
digest-literal rejection over live locations is untouched. Y was stricter than my round-1
`X1.5` on where the pin may live, the charter took Y, and the relocation preserves the
staleness detector rather than deleting it.

**2. Atom closure by derivation rather than enumeration — genuinely closed in mechanism,
imprecise in three cells.** X3 above. Derivation is the only form that fits the line limit
without copying prose, and §3.1's dual closure plus `G-ATOM` is a real advance. The residue
is X3.2, X3.3 and X3.4.

**3. The trusted-base line budget — satisfiable, with the coupling noted.** X5.2.

**4. `G-DIM-2`'s recording proxy — the closure over-worried.** X2.1. An evaluator that
destructures its input defeats read-coverage by making the gate go **red**, not by slipping
past it: the observed-read set stops equalling the declared set. The proxy is fail-closed
against exactly the attack the closure feared. The real residues are elsewhere — `G-DIM-3`'s
`contract.constants` carve-out (X2.2) and the read-but-unused dimension (X2.3).

**5. M6 Case 2 over-use — real as a reporting risk, contract-neutral as a hazard.** X6.3.
All three dispositions leave the accepted contract unedited, so over-use costs the author
visibility, not contract integrity.

---

## Consolidated Minor notes

Non-normative and non-blocking. Recorded so M1 and M2 know where the bytes are thinnest; no
replacement text is proposed and none is authorized.

| # | Locus | Note | Named destination |
|---|---|---|---|
| N1 | §3.3 A-17 | Source cell is a search predicate over `CAND-C`, not a `<path>#<section>` locator, and its second source is a file §5.3/§7 forbid as authority | M1's "an atom has no single home" terminal, or §3.2, or §5.4(3) |
| N2 | §3.3 A-9, A-10 | Sourced to §P1-15, `CAND-C`'s test matrix; `CAND-C` states the classifier is defined in full at §P1-10.7 "and nowhere else". "One atom per dominance cell" yields seven inline rows there versus the full `SC-10` table at §P1-10.7 | §P1-10.7 is already in the source set, so the correct derivation adds no source |
| N3 | §4.4 `G-DIM-4` | "Declared dimension set equals the A-0 atoms" cannot be raw equality once §4.3 collapses twelve source dimensions to eleven; A-18 carries the exception, A-0 does not | Harmonizing reading is determinate from §4.3 and A-18 |
| N4 | §4.3 | Sixth variant labelled "error-after-deadline-exhaustion" is narrower than `KG-1`'s `ERROR`, which the source says deadline exhaustion "ALSO" arrives at | Six-to-six correspondence and A-0's per-value `ERROR` atom pin the denotation |
| N5 | §6 M3 / §5.3 | M3's gate requires a blocker record under `successor/officina/migration/blockers/`, outside M3's allowed-edit cell | The future M3 authorization act (required anyway, since T-4 is M1/M2-only), or §8.3's named-limit route |
| N6 | §3.3 vs `CAND-C` §P1-11 | Crash cuts, PCS loss, invalidity routing and Stage-M terminals are in no family's Source cell while A-3, A-8 and A-17 name their content | §5.4(3) at M6 — fail-closed, author-visible, contract unedited |
| N7 | §4.4 `G-DIM-3` | The `contract.constants` carve-out permits a machine-consulted undeclared dimension; §4.4's "fails at M2 or M4" holds via M4 only, against §4.1's ungated "fact-free" characterization | M4 review of `machines.py` |
| N8 | §3.1 `G-ATOM` | Checks derivability, not membership of locators in the §3.3 source set; source closure is normative but ungated | M4 review of the register |
| N9 | §4.2 O1 | "Strictly weaker" is a phrasing rule with no gate, and §7's test exemption removes the mechanical pressure against O1 growing into a second relation | M4 review; M2 gate requires O1 green |
| N10 | §7 last ledger row | "Duplicated string literals — 0 across `contract/**` ∪ `generated/**`" is satisfiable only on the source-literal reading; the any-string reading is violated by every render under §2.3 | Source-literal reading is the only coherent one, pinned by §2.3 and §1.2(7) |

---

## Negative space of this review

This review created exactly one file:
`reviews/fable_officina_migration_charter_v1_1_final_x_confirmation.md`.

**I changed no file other than this review.** Nothing else was created, modified, moved,
staged, committed or deleted. No governing or historical document, no signature, no code, no
test, no runtime artifact, no prior review, and none of the dirty or untracked working-tree
work was touched — the two uncommitted modules, the accounting edits and the modified test
files remain exactly as found, and the untracked Y-line confirmation file was neither opened
nor altered. No commit, tag, branch or other Git object was created.

**I created no code, data, entropy or artifact.** No contract module, schema, fixture,
generator, verifier, provenance gate, manifest, test or oracle was created. No machine was
executed and no cross-product was enumerated: the `KG-1` six-class analysis in X2.4 and the
dimension arithmetic in X2.5 are read from `CAND-C`'s own published bytes, not derived from
any implementation. No Philosophia production module was imported or executed —
`src/philosophia/officina/**` was measured with `git ls-tree`, `wc` and `grep` only, and
`canonical.py` was read for its symbol list and line count. No `/proc` was read; no socket,
pipe, FIFO or descriptor was opened; no `fork`, `exec`, `signal`, `wait` or `prctl` was
called; no clock was sampled for any contract purpose. No key, entropy, seed or world was
generated. No `E1`/`E2`/`E3` was spent.

**I authorized no M0–M6 work, no token, no installation, no activation and no outcome.** No
charter, executable contract, amendment, composite, binding, handoff, implementation, archive
operation, path move, signature or acceptance is accepted or authorized here. T-1, T-2, T-3
and T-4 remain unsigned and this review signs none of them; T-4 remains constrained by §10.4
regardless of this verdict. No `OR-3`..`OR-11` step is authorized. Amendment `v1.12` remains
not accepted, `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` remains not accepted, and the X
line's v2.15 confirmation is neither completed nor withdrawn by anything here.

This review predicts no Y-line verdict and no scientific outcome. It reopens no signed
science, designs no v1.2, proposes no prose patch, and demands no copied historical prose.
It fixes no route count, write count, population figure or digest. This file contains none of
its own digests.

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

The Y line's independent confirmation of these same bytes, on which nothing in this memo is
an input. Together those two evaluations are **round 2** for the charter-design scope under
§8.2, and this episode's last.

Then, and only then: Kirill's consideration of T-1, T-2 and T-3. T-4 is separately signable
afterwards under §10.4's own constraint. No M0–M6 work, implementation, archive operation,
Git object, token or activation is in scope before that.

No token is authorized by this review.
