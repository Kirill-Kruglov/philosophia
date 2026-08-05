# Officina P1 W-B post-selection binding — independent Y-line review

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Review date:** 2026-08-05  
**Reviewed commit:** `ae72f2e6c4ceb294242590e3bf4869573da99ea9` (`Draft W-B post-selection implementation binding`)

## Scope and input integrity

This is a bounded adversarial review of binding correctness and inactive
implementation eligibility. It does not reopen signed W-B and it does not
accept an amendment, authorize implementation, execute an OR step, or activate
`T`. The author closure was treated as an untrusted question set, not as
evidence.

The supplied inputs match the bytes on disk:

```text
73d9cfeb4efdfd6a370f369c86162e603ab868acb088455bc9a1873a49b13942  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md
96cda63a70f8498024527323542a762d7d44b353af6781f8091e5b061ee7d440  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V1_DRAFT.md
8441a1081519a7eef6acc92548eb916e47b7be9b7f630312d86ba84e96d9dfd8  reviews/opus5_officina_p1_wb_post_selection_binding_closure.md
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
```

## Executable findings

### Y-M1 — Major — F1 is a fail-open governing contradiction

Amendment §A9 H-3 limits the pre-production enforcement point to
`CK-1..CK-12`. The same amendment's §A10 defines `CK-1..CK-15`; `VP-4` orders
fifteen checks; `IR-9` requires `CK-2..CK-15`; `CK-15` says the whole check is
`CK-1` through `CK-15`; composite §P1-14.8 says there are fifteen checks; and
the v2.10 packet count is fifteen. No reading makes the `CK-1..CK-12` sentence
consistent with those clauses.

I attempted both implementations:

```text
12-check reading
  run CK-1 through CK-12 and return success
  result: CK-13, CK-14 and CK-15 are unreachable by construction

15-check reading
  run CK-1 through CK-15 in VP-4 order and return success only after CK-15
  result: conforms to §A10, IR-9, VP-4, composite §P1-14.8 and the count,
          but contradicts the literal range in amendment §A9 H-3
```

The omission is concretely fail-open. Take an otherwise valid installed state
whose Stage A carries signed W-B and whose structurally valid, correctly signed
Stage B carries W-A as `selected_option_token`. `CK-3` checks only B1..B13, so
the mismatch survives `CK-1..CK-12`; B14 at `CK-14` is the first clause that
must refuse it with `STAGE_B_OPTION_MISMATCH`. The 12-check implementation
accepts the option mismatch. Separate counterexamples exist for the omitted
record-member equality at `CK-13` and M7 semantics at `CK-15`.

This is an executable Major on the signed W-B critical path and licenses a
bounded next governing generation under the stated exit discipline.

### Y-M2 — Major — F2 prevents implementation of the classifier scope

The complete current governing input search found `KV-1..KV-6` only twice,
both as references in composite v1.10: §P1-10.7 and test row 89. It occurs zero
times in amendment v1.7 and zero times in the v2.10 packet. Neither governing
file defines even one of the six predicates.

The classifier cannot be implemented from the governing pair. The trigger,
actor, record-first ordering, no-mediation rule, no-evidence rule and
publication boundary are stated, but the set of groups eligible for every
`_killpg` is not. This is safety-critical because the missing predicate set is
the only named rule that is supposed to exclude forbidden groups.

The definition in
`OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md` is superseded,
is not a governing member, and is not open for behaviour. Copying, adapting or
reconstructing it is prohibited by DA-1, DA-2 and IR-12. The correct result is
both: the present scope predicate has no implementation authorization, and a
later governing round must carry a complete authoritative definition before
implementation.

### Y-M3 — Major — PO-4 and PO-6 are mutually unsatisfiable

Binding PO-4 and handoff U-5 require the W-A option token and
`P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` to occur zero times in the whole
resolved composite. Binding PO-6 and handoff U-9 require TS-1's two literal
option tokens to remain. TS-1 also normatively carries both paired
option-specific amendment tokens. Therefore a correct TS-1 necessarily makes
PO-4/U-5 fail, while deleting the literals to satisfy PO-4/U-5 corrupts TS-1
and IR-13 row 47. No resolved byte string can pass both checks.

PO-4's slot-6 carve-out is also not mechanical as written. The composite uses
`slot 6`, `SOCK_SEQPACKET` and socket-pair language for the legitimate
supervisor/PCS control channel as well as for rejected watchdog capability and
retained watchdog-closed clauses. The phrase "in any clause granting the
watchdog an endpoint" requires semantic interpretation, while the handoff
claims an exact occurrence rule but supplies none; U-5 does not test the two
socket strings at all.

The repair must use an exact locus/fragment classification. It must preserve
the complete two-option and two-option-amendment vocabulary in TS-1, forbid the
W-A operational capability at the resolved operative loci, preserve legitimate
non-watchdog supervisor-channel socket clauses, and enumerate the permitted
watchdog `slot 6` occurrences only in their closed/absent sense.

### Y-M4 — Major — the preamble transformation is incomplete

The marker census is correct but is not a complete transformation census.
Binding §2.2 deletes only preamble lines 79, 80 and 83 because those are the
three marker-bearing lines. It leaves the surrounding Cell-2 prose saying:

```text
the version is not acceptable until the watchdog cell is signed
the mechanism remains open
W-A and its request socket/frame are still an available description
the document selects neither and predicts neither
```

Those surviving assertions are false after the signed W-B resolution. PO-2
detects marker strings outside guarddata, not these marker-free statements.
PO-4 cannot repair this omission: its token ban is already inconsistent with
TS-1 and it provides no transformation action for the surrounding block. Thus
a transformation following the advertised 20-locus table can pass PO-1 and
PO-2 while retaining a normative preamble that still says the cell is open.

The binding needs a byte-exact preamble resolution table covering the complete
Cell-2 notice, not only the three marker-bearing lines. It must record the
signed W-B state, remove the discharged open/unsigned assertions and rejected
W-A capability exposition, and leave TS-1's closed option vocabulary intact.

### Y-M5 — Major — the handoff is not a whole inactive implementation surface

The §H1.1 list is complete only for an inert oracle/declarative scaffold. Its
two code paths are restricted to an in-memory byte oracle and pure data with no
I/O, syscall or clock. No allowed path can implement §H3's watchdog EOF route,
PCS classifier, supervisor routes, descriptor handling or process-control
ordering, and F2 independently fences the classifier's central scope
predicate. Several named tests therefore have no allowed implementation under
test.

The frozen-path side is correct for the current boundary: neither MS-6 module,
no `test_p1_row_NNN_` function, no production root, no governing/runtime path
and no install artifact may be created or edited before its later authorized
OR step. But the draft must not call the allowed subset a complete inactive
implementation of W-B. The smallest repair is to label it explicitly as
oracle/contract scaffolding only and defer runtime implementation; expanding
the allowed surface would be a separate authorization decision.

## Literal answers to closure §9 Q1–Q10

### Q1

**Yes.** §A9 H-3 is an operative contradiction of §A10, §P1-14.8, `VP-4`,
`IR-9` and the fixed count. It is Major and licenses bounded regeneration. The
12-check reading is fail-open because it omits `CK-13..CK-15`, including B14 at
`CK-14`. No consistent 12-check reading exists.

### Q2

**No.** `KV-1..KV-6` cannot be implemented from the governing pair. A later
governing round must supply the complete definition; until then the scope
predicate has no implementation authorization. Reconstruction from the
superseded V2 draft is not permitted under DA-1/DA-2/IR-12.

### Q3

The mechanical marker result is confirmed exactly:

```text
sentinels: BODY 248..6461; GUARDDATA 6463..6504; PROVENANCE 6506..6696
marker-bearing lines: 20
marker occurrences: [W-A] 13, [W-B] 13
split: preamble 3, body 16, guarddata 1
```

Body-only resolution can satisfy G-10 while leaving the preamble markers, so a
whole-file-minus-guarddata check is needed. Line 6501 must remain byte-identical;
independent extraction hashes guarddata to
`faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426`.
Deleting line 6501 destroys G-10's pattern source and changes `H_GUARDDATA`.

The closure's further claim is refuted: PO-2 is necessary but not sufficient.
Deleting only marker-bearing preamble lines leaves the larger Cell-2 blocking
notice and rejected-option prose, as Y-M4 shows.

### Q4

**Identity code exclusion is correct for this bounded W-B-only surface.** The
governing pair contains zero occurrences of `attested_pid` and
`attested_pgid`; row 2 says it chooses neither repair and invents no value.
Writing identity-observation code from this pair would invent a contract.

This draft is not the later combined binding named by XS-1: it does not resolve
row 2, accept the bounded weakening, decide membership for the identity
signature, or re-derive identity fields. Treating it as that combined binding
would incorrectly import an unaccepted weakening. Conversely, this exclusion
does not clear the later combined-binding gate: that future binding still must
record separate weakening review and acceptance or refuse to proceed. No
operative P1/identity activation follows from the W-B-only work.

### Q5

**Not precise enough to be mechanical.** The semantic distinction between a
watchdog endpoint grant, a watchdog closed-slot clause and the unrelated
supervisor/PCS slot-6 socket is substantively correct, but no exact permitted
occurrence/fragment table implements it. PO-4 also conflicts with TS-1 as
written, and U-5 omits `SOCK_SEQPACKET` and `socketpair`. The binding/handoff
must carry an exact locus-based rule.

### Q6

**Confirmed.** OR-4 must not delete the non-selected token from TS-1. TS-1 is
the closed two-option validation set, and B14 at `CK-14` compares Stage B's
selected token with Stage A's value. IR-13 row 47 records that equality edge.
The paired two-option-amendment vocabulary must remain as well. "Remove every
W-A string" is therefore not a valid resolution rule.

### Q7

**PR-2 is correct.** OR-4 resolves same-generation bytes at the same MS-1 path;
it does not replace the v1.7/v1.10 pair and is not a provenance-growth round.
The four deferred rows do not enter during this handoff.

**PR-3 is also correct for the next actual governing generation.** The deferred
v1.6/v1.9/X/Y four and that round's own replaced-pair/X/Y four must enter in
one internally consistent update, not as two transient member sets. Because
this review confirms that a v2.11 governing repair is required, that repair is
the first such actual next generation and must perform the accounting once.

### Q8

The frozen list and the prohibition on premature MS-6/row-test creation are
correct. No `test_p1_row_NNN_` function and neither MS-6 module may exist before
OR-5 installs the modules and OR-7 runs them. The current repository matches
that state.

The allowed list is complete only for the oracle/contract scaffold, not for
W-B inactive implementation as a whole. Whole implementation is impossible
under the list and is additionally blocked by F2. The handoff must be narrowed
to say so; no path expansion is authorized by this review.

### Q9

**Confirmed.** The current untracked `generic_harness.py` is production root
3 of §P1-3.1. Its docstring identifies the generic-harness/batch-settlement
lineage, and it currently imports `subprocess`, calls `subprocess.Popen(...,
start_new_session=True)`, `os.kill` and `os.killpg`. That is consistent with
the older generic-harness grant described by the governing composite, but it
violates P1's 16-name scoped allowlist and S-12. It must not be edited, adopted
or treated as P1 evidence here. A fresh, recorded and reviewed audit is
mandatory before any P1 reuse.

### Q10

A governing-pair Major gates the binding itself. F1 and F2 are independently
Major, and Y-M3/Y-M4 make the draft transformation/oracle internally
non-implementable even apart from the governing defects. The correct boundary
is bounded governing-pair repair followed by fresh independent review and a
regenerated binding/handoff; it is not implementation review.

## Smallest bounded v2.11 repair

The smallest admissible next round is a replacement governing pair (the next
amendment/composite generation) plus regenerated binding/handoff drafts. It
must do only the following:

1. Replace every operative handoff-range statement with `CK-1..CK-15`, keep
   the fifteen checks and their VP-4 order unchanged, and re-establish the
   claimed identical copies.
2. Add one complete, authoritative `KV-1..KV-6` definition to current
   governing bytes and make both §P1-10.7 and row 89 resolve to it. The author
   must supply and review those rules; an implementer may not recover them from
   a superseded draft.
3. Advance every generation-scoped literal, anchor, member path and shared
   block consistently. Since this is the first actual replacement generation,
   add both four-row provenance sets in one accounting update: `MS-2` 55→63,
   `MS-8`/member count 69→77, and composite provenance rows 63→71, with all
   dependent literals and checks updated together.
4. Regenerate the W-B binding's transformation table to resolve the complete
   Cell-2 preamble, not merely marker-bearing lines; retain guarddata exactly.
5. Replace PO-4/U-5 with an exact locus/fragment rule consistent with PO-6 and
   TS-1: retain both option tokens and paired amendment tokens in TS-1, remove
   rejected W-A operational capability, preserve unrelated supervisor-channel
   socket language, and enumerate permitted closed watchdog slot-6 text.
6. Narrow the handoff to inert oracle/declarative scaffolding only. Do not
   imply that the listed paths implement §H3 as a whole, and do not expand the
   write surface without a separate authorization.

This bounded repair must not accept or implement the identity weakening. The
later XS-1 combined binding remains a separate gate.

## Implementation-log notes (non-blocking)

- F3 is confirmed Minor: OR-4's operative reference to the v1.3 amendment is a
  fifth generation-scoped string omitted from §A9's claimed complete audit.
- F4 is confirmed Minor: composite line 90 locates G-10 in §P1-14.3 although
  G-10 is defined in §P1-14.4.
- Binding §2A.1 duplicates the `O-3` line verbatim.
- Handoff E-7 should say no actual key material or authorization artifact
  exists; read literally, the identifiers `key_id` and `public_key_hex` occur
  throughout governing prose.
- §H11's current line-number observations are accurate for this worktree but
  are not durable evidence; the required fresh audit is the correct control.

## Exact next boundary

No amendment acceptance, implementation authorization, code or test change,
key, Stage A/B artifact, OR step, install or activation may follow this review.
The next permissible act is author preparation of the bounded v2.11 governing
replacement described above. That replacement requires fresh independent
review before the W-B binding/handoff can be regenerated and reviewed again.
Only after those gates may an author separately consider amendment acceptance
and a narrowly scoped inactive-scaffold authorization. The XS-1 combined
identity binding remains blocked on separately reviewed and accepted bounded
weakening.

```text
REVISE_OFFICINA_P1_WB_GOVERNING_PAIR
```

`T = NOT_ACTIVATED`  
`PROGRAMME CLAIM = OPEN`
