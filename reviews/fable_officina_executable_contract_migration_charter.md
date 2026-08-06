# Review — Officina executable-contract migration charter v1 (draft)

**Reviewer:** Claude Code Opus 5, independent programme architect. This memo
reviews the charter this same session authored; it is a self-assessment and is
normative for nothing. It exists to state the verdict, expose the charter's
weak points before the independent lines see them, and prove the one claim the
whole route rests on.

**Reviewed bytes:** `successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_DRAFT.md`.

---

## Verdict

```text
READY_FOR_OFFICINA_MIGRATION_CHARTER_XY_REVIEW
```

The charter is a route decision that is complete enough to review and small
enough to reject cheaply. It does not accept, repair or supersede any candidate;
it authorizes no implementation; and its own §6.2 binds it to a stopping
condition. The three open gaps in §4 below are questions for the independent
lines, not defects that block review — each is a bounded question with a stated
default, and none of them can be resolved by this author without an author
choice or an independent line.

`T = NOT_ACTIVATED`; programme claim = `OPEN`.

---

## §1. Input verification

All seven pinned inputs recomputed at `d556538`; all seven reproduce exactly:

```text
6a00e058…723f26a  successor/…WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md      OK
e156d662…95a8f4a  successor/…WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md            OK
a41c1424…76b113a  successor/…P1_OPERATIVE_COMPOSITE_V1_15.md                               OK
c9db32bb…ad2ff5a  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md              OK
279f59a2…61e31e1  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md              OK
cae4e054…b88a03ea  reviews/fable_officina_p1_wb_v2_15_final_x_confirmation.md              OK
83c3afce…5d73bdda  reviews/sol_officina_p1_wb_v2_15_final_y_confirmation.md                OK
```

(Truncated for display only; full values are in the task and in the two reviews.
No mismatch. **Not `BLOCKED`.**)

**The divergence is real and is the charter's premise.** X returned
`0 Major` / confirmed-for-acceptance; Y returned `REVISE` on three Major
findings. Neither line is wrong. X executed the machine and found it sound; Y
read the document's testimony about its own provenance and found three live
statements naming superseded generations. They did not contradict each other —
they reviewed two different surfaces that the artifact fuses into one file. That
is the evidence for an architecture verdict rather than a clause verdict, and I
record it as the single fact that most justifies the route.

---

## §2. Proof: the architecture cannot recreate manual cardinality/hash/generation drift

This is the load-bearing claim. If it fails, the charter is not worth signing.

### §2.1 Definitions

- **Live surface** — a file that governs after M5: `contract/**` (authoritative
  source) and `generated/**` (`CONTRACT.md`, `MANIFEST.json`).
- **Derived fact** — any value that is a total function of the bytes of
  `contract/**`: member cardinalities, digests, path lists, cross-references,
  and generation identity.
- **Drift defect (Class B)** — a live surface contains a token `T` asserting
  derived fact `F`, and `T ≠ F`. All three Y Major findings are of this form.
- **Green tree** — the test suite passes.

### §2.2 Lemmas

**L1 — derived facts have no writable home in source.** `contract/**` contains
only declarations: enum members, frozen-dataclass fields, transition-function
bodies, and canonical JSON data. Cardinalities are never written; they are
computed by `render.py` as `len(...)` over the declared collection at render
time. A count typed into a source file is read by no template and therefore
reaches no live surface: it is dead text, not authority.

**L2 — generated surfaces are a pure function of source.** By construction
`generated/X = render(contract/**)`. `verify.py --check` recomputes
`render(contract/**)` into memory and compares bytes; §4.3 requires a test to
invoke it. Therefore **in any green tree, `generated/** = render(contract/**)`
exactly.** A hand edit to `CONTRACT.md` fails the suite; a source change not
re-rendered fails the suite. There is no third state.

**L3 — digests.** Every digest in `MANIFEST.json` is
`sha256(read_bytes(p))` for `p ∈ contract/**`, computed at render time from
bytes read at render time. By L2, a stale digest is a red suite, never a review
finding.

**L4 — acyclicity gives L2 a single pass.** `MANIFEST.json`'s domain is
`contract/**`, disjoint from `generated/**` and from itself (§2.1(3)–(4)). No
digest is ever computed over bytes that contain that digest, so `render` needs
no fixed point and the L2 byte comparison is total and terminating. This is
precisely what the current architecture lacks: the composite carries its own
member manifest, so every member change obliges hand edits inside the file
being hashed.

**L5 — no generation cascade.** Version identifiers exist only on author-signed
artifacts (§6.1). No source file and no generated file carries a generation
number. An ordinary fix edits source in place; Git carries history.

### §2.3 Theorem

*In any green tree, no live surface contains a Class-B drift defect.*

Let `S` be a live surface mentioning derived fact `F`. If `S ∈ generated/**`,
then by L2 `S`'s bytes equal `render(contract/**)`, so `S`'s mention of `F` is
whatever `render` computed from current source — correct by L1/L3, or the suite
is red. If `S ∈ contract/**`, then by L1 `S` contains no derived fact at all, so
the antecedent is vacuous. ∎

### §2.4 The three Y findings, mapped

- **Y15-M1** (preamble names a retired amendment generation as live authority) —
  requires a generation identifier repeated in a live surface. By **L5** no such
  location exists. Eliminated.
- **Y15-M2** (two incompatible claims about which generation is replaced) —
  same. By L5, eliminated.
- **Y15-M3** (a live proof names one generation as the transform source while
  the transform consumes another) — requires two independent statements of the
  transform's source. By **L1/L2** there is exactly one source, and the
  documentation's statement of it is emitted from that source. Eliminated.

### §2.5 Where the proof does **not** reach — stated plainly

1. **The template layer is not covered by construction.** L1 assumes
   `render.py`'s templates emit derived values only through computation. Nothing
   in the architecture *prevents* a template from containing a hand-typed
   integer. This is the one hole, and it is why X-1 below asks for a mechanical
   guard (an AST test forbidding numeric and digest-shaped literals in the
   template layer). Until that guard is specified, the theorem holds modulo
   template review. **I regard this as the charter's weakest point.**
2. **Author signature files are outside the theorem.** §2.1(4) lets a signature
   carry `MANIFEST.json`'s digest. Signatures are hand-written. See Y-1.
3. **The theorem is conditional on a green tree.** It is a statement about
   states in which the suite has been run, not about the repository at rest.
4. **Classes A and C are untouched.** The theorem says nothing about whether the
   machine is *right*, only that the documentation does not lie about the
   source.

---

## §3. Sharpest three X questions (semantics, correctness)

**X-1 — Does generating both cross-checked implementations from one declaration
destroy the check?**
§4.1 keeps the X line's two-implementation discipline but makes both the ordered
machine and the guard-row predicates *generated from the same source
declaration*, calling agreement "a test, not a coincidence of two
transcriptions." That inverts the property that gave the v2.15 X confirmation
its force: the two implementations were valuable **because** they were
independent transcriptions of prose by one reader, so a misreading in one would
not appear in the other. Two projections of one declaration agree by
construction and may agree while both are wrong.
*Ask:* should M2 require exactly one of the two to be hand-written from the
generated `CONTRACT.md` alone, and diffed once at M4 — accepting a single
one-time transcription cost for real independence? And relatedly: the same
question applies to the template-layer guard in §2.5(1); should that AST test be
promoted from this memo into the charter's §4.4 before signature?

**X-2 — Which reading of the enumeration rule does M2 adopt, and is the declared
dimension product authoritative or derived?**
`X15-M1` showed two readings of the enumeration rule producing different route
counts (`R-E` 552 vs 560) and different write counts (6 vs 4), with both builds
claiming conformance. Migration makes the machine unambiguous but does **not**
by itself decide which reading is the intended one — that is a Class-A decision
the charter defers to M2 without naming a default. Worse, §4.7 concedes that "an
undeclared dimension is invisible," so the declared product is itself an
authority object.
*Ask:* does M2 adopt the clause-1 reading (6 writes, the reading the composite's
own preamble and write-count clause support), and is the dimension declaration a
reviewed member of `contract/data/` with its own M4 completeness review?

**X-3 — What happens when a crash-cut test finds a defect in code the charter
forbids editing?**
§4.5 puts `atomic_create` / `atomic_replace` / `fsync_directory` under test.
Those live in `src/philosophia/officina/canonical.py`, which §5's M3 explicitly
forbids editing (`contract/`, `tools/`, `generated/` and new tests only), and
which §7 does not classify at all — it is neither salvage nor extracted
invariant. If M3's crash-cut test fails against existing `src/` code, the
charter provides no route: M6 is the first package that may touch `src/`, and it
is gated behind M5 author acceptance of a contract whose tests are red.
*Ask:* should M3's crash-cut tests be permitted to *record* a defect in `src/`
as an M6 input without blocking M3's gate, or should `canonical.py`'s durability
primitives be pulled into the §3 inventory as I-16?

---

## §4. Sharpest three Y questions (provenance, boundary, negative space)

**Y-1 — §2.1(4) re-creates exactly one hand-copied digest location.**
The charter forbids self-hashes and caps live manifests at one, then permits an
author signature file — hand-written, outside `generated/**` — to carry
`MANIFEST.json`'s digest as the external release bind. That is structurally the
same shape as the existing signature files' "Governing hashes" blocks, which is
where a large share of the current drift surface lives. Nothing in §4 refuses a
stale value there: `verify.py --check` covers `generated/**`, not signatures.
*Ask:* is the signature inside or outside the §2.3 theorem, and should
`verify.py` gain a mode that checks a named signature file's digest block
against the bytes it names — or is a stale signature deliberately accepted as an
author-owned, one-time, human-verified fact?

**Y-2 — the source budget may be under-counted against what M6 must reconcile.**
§6.1 caps `contract/**` at 2,500 LOC. The single uncommitted salvage file
`src/philosophia/officina/generic_harness.py` is 2,380 LOC, and the existing
`src/philosophia/officina/` tree is 7,349 LOC. §7 keeps that work untouched and
defers evaluation to M6. If the accepted contract must specify most of the
harness's behaviour, either the budget is wrong or the extraction boundary in §3
is narrower than the subsystem it claims to govern.
*Ask:* is 2,500 LOC a budget for *specifying* I-1..I-15 only, with the harness
implementation explicitly out of contract scope — and if so, does §3's inventory
actually close over what M6 will need, or will M6 discover an I-16..I-n that
§3 declares out of bounds without a charter amendment?

**Y-3 — is the archive move mandatory or conditional, and what gates it?**
§7 states the prose generations "move to `successor/archive/`" on the M0 token;
§5's M0 permits the move "**only** if the author's token so directs"; and T-1's
text says the halt "archives it as unaccepted evidence." Those three readings
are not identical. Separately, the move is a bulk `git mv` over 100+ files, and
M0 lists no test and no reviewer for it.
*Ask:* does T-1 mandate the archive move or merely authorize it; must the move
be a separate commit with a pre/post path inventory; and — since §7 also insists
"no current candidate becomes accepted by implication" — does moving the
X-confirmed v2.15 into an archive directory risk reading as a disposition of
that confirmation rather than of the document?

---

## §5. Bounded author choices

Four tokens. Three carry a recommendation; one is a genuine choice with a
recommended default. Full text and exact boundaries are in charter §8.

| Token | Recommendation |
|---|---|
| `I_HALT_OFFICINA_PROSE_CONTRACT_LINE_V1` | **Sign.** The line currently sits under two divergent verdicts on identical bytes with no defined next act. Halting is not accepting v2.15. |
| `I_ACCEPT_OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1` | **Sign**, conditional on X-1's template guard being folded into §4.4 first. It accepts a route and a stopping condition, not a contract. |
| `I_SELECT_OFFICINA_CONTRACT_DEPENDENCY_STDLIB_ONLY` **vs** `…_STDLIB_PLUS_HYPOTHESIS_DEV_ONLY` | **Stdlib only.** The contract's whole value is being auditable by reading it; a third-party semantic layer subtracts from that. Hypothesis remains available as a test-only dev extra if the byte-surface corpus proves inadequate at M3, which is a §6.3 override, not a silent expansion. |
| `I_AUTHORIZE_OFFICINA_CONTRACT_M1_M2_IMPLEMENTATION` | **Do not sign yet.** Signable only after independent X and Y review of the charter bytes, per charter §8 T-4. |

No token authorizes `T` activation, any `OR` step, science, entropy, install,
key, commit, or any edit to `src/`, existing tests, runtime artifacts or the
uncommitted salvage work.

---

## §6. Negative space

This review created exactly one file: this memo. It modified nothing else.

No governing or historical document, no signature, no code, no test, no runtime
artifact, no prior review and none of the dirty or untracked working-tree work
was modified, moved, staged, committed or deleted. The two uncommitted salvage
modules and the two modified test files remain exactly as found. No commit was
made and no branch was created.

No contract module, schema, fixture, generator, verifier, manifest or test was
created. No machine was executed against any live process. No cross-product was
enumerated. No `/proc` was read; no socket, pipe, FIFO or descriptor was opened;
no `fork`, `exec`, `signal`, `wait` or `prctl` was called; no clock was sampled
for any contract purpose. No key, entropy, seed or world was generated. No
Philosophia production module was imported or executed — file sizes and layout
were read with `wc`, `ls` and `grep` only.

This memo predicts no X-line or Y-line verdict, and no scientific outcome. It
asserts no acceptance: amendment `v1.12` remains not accepted,
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` remains not accepted, and the
X line's v2.15 confirmation is neither completed nor withdrawn by anything here.

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

## §7. Next boundary

Independent X-line and Y-line review of the charter bytes — the same bytes to
both lines. The X line should take §3's questions and the §2.3 theorem; the Y
line should take §4's questions and §2.5's stated holes. Neither line's verdict
is predicted here.

After that round, and only then, Kirill's consideration of T-1 through T-3, with
T-4 following separately.

The goal is not a better contract document. It is a smaller auditable base that
returns the programme to scientific development.
