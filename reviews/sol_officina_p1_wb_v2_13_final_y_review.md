# Officina P1 W-B v2.13 final Y review

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Requested reviewed commit:** `23a7816d85f7118171512764bd2e84a06dac71c2`  
**Review path:** `reviews/sol_officina_p1_wb_v2_13_final_y_review.md`  
**Whole-file SHA-256:** reported after finalization in the accompanying chat; a
file cannot truthfully contain its own ordinary whole-file digest without a
self-referential digest convention that the request does not define.

The author closure was treated as adversarially untrusted. No governing,
historical, code, test, signature or runtime artifact was modified, no contract
process was run, no signal was sent, nothing was staged or committed, and this
review is the sole repository file created by this review.

`T = NOT_ACTIVATED`. Programme claim = `OPEN`. W-B remains signed and was not
reopened.

## Verdict

```text
REVISE_OFFICINA_P1_WB_V2_13
```

Four current executable Majors block acceptance review: SC-10 leaves a
same-Phase-4 `T1`/`T3` collision unordered; KG-2 gives opposite population
answers on an ordinary `AWAIT_STOP/TIMEOUT` route; composite test rows 105 and
106 retain 81-member literals against the current 85-member contract; and the
mandatory bootstrap calls for `getsid`/`getpgid` answers while the closed
primitive surface supplies neither operation. These are independent of the
signed W-B scientific choice.

## Input and checkout verification

All six task-pinned inputs were hashed from disk before substantive review and
matched exactly:

```text
d50f378ca419f891e79356315d59115b6ec06c38474e812fa01ccb847b15f200  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_13_CORRECTION.md
2999e2129de19ff38dee12071453c7156a5432efaf299bc69e79dc7e7b04ac53  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md
15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
10207f833a00b0e7e5106ca8a781916f3414d995ab05161fb734078b5ffaef93  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md
080000c478c933bedd91124983c4c9e44cc4b850e52eba17b7628304274cbef9  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V4_DRAFT.md
8245b0f960fa4a349667a0c75213cbe0e39cf83ab4a914be94146d56f93626fd  reviews/opus5_officina_p1_wb_v2_13_closure_repair.md
```

The live checkout was at descendant `9ed98a704ab964ad96430b74ca39ad52be24f75c`,
not literally at `23a7816`; `git diff 23a7816 -- <the six pinned paths>` was
empty. The later commit adds the review request, not different pinned inputs.
Pre-existing unrelated dirty and untracked paths were not used as authority and
were preserved.

## Severity-ordered findings

### Major Y-M1 — SC-10 is not a mathematical decision function within Phase 4

SC-10 says precedence is phase order “and nothing else.” That orders faults in
different phases, but Phase 4 contains two distinct terminal-producing
predicates:

- `SC-8`: a wrong-shaped `KG-1` return, `PRIMITIVE_FAULT`, or a non-`OSError`
  `BaseException` produces `T1 / PCS_FREEZE_CLASSIFIER_STRUCTURAL_VIOLATION`;
- `SC-9 P4` plus `KV-6(b)`: a `PRESENT_VALID` fresh observation whose `pgrp` is
  protected produces `T3 / PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET`.

Use two structurally valid, current-generation prospective candidates, both
with unprotected recorded groups. Let entry `a`'s Phase-4 observation be
`PRIMITIVE_FAULT`, and let entry `b`'s be `PRESENT_VALID` with a protected
fresh `pgrp`. Both terminal predicates are applicable in Phase 4. In table
order `[a,b]`, immediate termination returns T1 before observing `b`; in order
`[b,a]`, it returns T3 before observing `a`. If an implementation instead
collects the whole phase, it obtains both terminals and the bytes provide no
tie-break. Thus permutation invariance, terminal uniqueness, qualifier
uniqueness and per-entry-token uniqueness are false for this table.

The ordinary cross-phase claims do hold: Phase-1 malformed dominates stale and
both protected forms; Phase-2 stale dominates both protected forms; Phase-3
recorded protection dominates Phase-4 fresh protection; and Phase-4 fresh
protection precedes Phase-5 identity/group mismatch. The missing case is a
later structural fault and fresh protection in the same observation phase.

Smallest repair: give Phase 4 and Phase 6 an explicit intra-phase terminal
reduction, normally `STRUCTURAL_VIOLATION > FORBIDDEN_TARGET`, require the whole
applicable scan needed to apply it, and pin terminal, qualifier and per-entry
token when both occur. Add the same-phase pair to SC-10 and row 89.

### Major Y-M2 — KG-2 P-2 and P-10 disagree on `AWAIT_STOP/TIMEOUT`

P-2 attaches its population attempt to every PCS evaluation of `AWAIT_STOP` at
the instant the `pgid_is_leader` response operand is computed. It requires
exactly one `PGRP_OBSERVE`, and says the write occurs iff the observation is
`PRESENT_VALID`, the identity matches, and `pgrp == pid`. It does not require
the operation outcome to be `STOPPED`.

P-10 separately says that when `AWAIT_STOP` returns `TIMEOUT`, no write occurs,
the handle remains `H-NULL-GROUP`, and a later operation may retry. An ordinary
counterexample is a live controller created with `setsid=True`, still in
`SPAWNED`, whose wait expires before its self-stop is observed. At response
construction its stat observation may be `PRESENT_VALID`, with matching start
identity and `pgrp == pid`. P-2 then mandates the one write and
`H-GROUP-RECORDED`; P-10 mandates no write and `H-NULL-GROUP`. Both rules govern
the same instant.

The authored route table silently chose P-10 and therefore did not reconstruct
P-2 independently. Smallest repair: make `outcome == STOPPED` an explicit P-2
population conjunct and state that `TIMEOUT` and `EXITED` set
`pgid_is_leader := 0` without a population observation or write (or specify a
different single rule consistently across P-2, P-9 and P-10).

### Major Y-M3 — the forced 85-member sweep left executable 81-member literals

The raw sets do recount to 71/85/79, but composite v1.13 line 7790, test row
105, still says a `members` array of any length other than **81** is a
structural failure. `IR-3`, `MS-8`, `CK-6`, TS-3 B7/B17, IR-13 row 38 and test
rows 104, 107, 108 and 115 require **85**. A conforming 85-entry record is
therefore both structurally valid under IR-3 and required to fail row 105.

Row 106 at line 7791 also constructs its coherent-rollback fixture with “all
81 of its members.” If that is intended to name an older generation, the row
does not identify that generation or its governing bytes; as the current
rows-104..115 fixture it is stale and conflicts with the 85-member setup. The
closure's claim that every dependent literal moved is false.

Smallest repair: change row 105's 81 to 85 and make row 106's fixture explicitly
current at 85, or explicitly bind its 81-member historical generation and its
whole restored byte set if historical rollback was intended.

### Major Y-M4 — Q8: mandatory bootstrap observations are mechanically unreachable

The exact reachability proof is:

1. `§P1-7.5 c1..c9` is the mandatory successful bootstrap prefix. `c10` must
   then verify `getsid(pid_mid) == pid_mid` and
   `getpgid(pid_mid) == pid_mid` before `c11` may install
   `SPAWNING_GROUP.json`. `c14` again requires `getpgid(supervisor_pid)`.
   Middle step `m3` also requires both answers for pid 0.
2. `§P1-3.4` is the exact primitive-binding list. It binds `_setsid`, `_getpid`
   and `_getppid`, but neither `_getsid` nor `_getpgid`.
3. `§P1-3.6` requires every later primitive use through a bound local name,
   forbids later module attribute access and dynamic lookup/import, and forbids
   `getattr`, `ctypes`, `eval`, `exec`, `__import__` and equivalent escape
   routes. `§P1-14.6 S-3`, S-5, S-6 and S-7 mechanically enforce that closure.
4. `_setsid` is a mutator on the calling process and cannot answer either query
   for an arbitrary pid. The canonical stat parser returns `pgrp` but not the
   session field, explicitly forbids interpreting any other suffix field, and
   in any event does not implement the literal `getsid`/`getpgid` operations
   promised by c10/c14/m3.
5. Adding `_getsid` or `_getpgid` in an implementation violates the exact
   binding block and S-3. Omitting them leaves no callable capable of satisfying
   the mandatory comparisons. Consequently no conforming implementation can
   traverse c10 to c11.

The current absence of runtime-implementation authorization prevents execution
today, but it does not isolate this defect for acceptance. `§H11` can later
authorize writes and execution only; it grants no authority to alter the
accepted governing primitive surface. Acceptance would therefore bind an
operation that a later separately authorized implementation still could not
supply. This is not a usable fail-closed gate; it is an implementation dead end.

Smallest semantic repair: bind both `_getsid` and `_getpgid` from `os`, add both
to the primitive-identity and exact-binding checks, and regenerate every
dependent exact-byte digest/test/accounting surface. Binding only `_getpgid`
does not repair c10 or m3 because `_getsid` is missing too. This requires a new
governing generation; a future runtime authorization alone is insufficient.

### Minor Y-L1 — the advertised fresh protected cross-product exceeds Phase 4's domain

The signed handle space is 72 tuples. Phase 4's prospective set contains only
12: role in `{CONTROLLER, WORKER}`, state in the three non-REAPED values,
ownership in `{OWNED, CONTRADICTED}`, and non-NULL group. The closing
position-independence paragraph nevertheless quantifies the fresh form over
every role, state and ownership. Of the claimed `3*4*3*4 = 144` combinations
over four protected values, only `2*3*2*4 = 48` receive a fresh observation.
The other 96 are excluded and have no Phase-4 fresh result to permute.

This does not widen signal scope—the operational prospective-set definition is
clear and the excluded tuples fail KV-2—but the conformance claim should be
narrowed to the prospective domain. Likewise, removing only the WATCHDOG role
filter does not make a normal `setsid=False`, NULL-group watchdog prospective,
because the independent NULL exclusion still applies; the “including watchdog
entries” necessity argument needs to say which other exclusion is being held
fixed.

## Q1 — exact 52-field stat classifier

I implemented `STAT_PARSE` from §P1-10.3 alone, using first `(`, last `)`, exact
single-space framing, exactly 50 suffix fields, the nine state bytes, canonical
UDEC31/UDEC64 parsing and inclusive bounds. I instantiated all published labels;
because V5 denotes nine concrete states and V24 denotes three rejected states,
this is 50 concrete byte buffers. Every expected result and every five published
positive digest/length check reproduced. V39 alone parses while the group
consumer refuses `pgrp == 0`, which is an admissibility difference and not a
parse disagreement.

The shifted, surplus and missing forms all refuse before field extraction;
signs, prefixes, underscores, points, leading zeros and one-past-bound values
refuse; last-`)` correctly admits `)` inside comm because any `)` remaining in
the suffix is refused; and every refusal returns only `PARSE_REFUSED(reason)`,
with no field value. I also exhaustively evaluated 66,430 buffers of length
0..5 over an alphabet spanning parentheses, spaces, digits, state, newline,
tab and signs; every call returned exactly one closed parser result.

Totality follows for arbitrary finite byte buffers: the first/last searches
either find indices or refuse; each later rule is a finite boolean test; exact
split/count either refuses or selects fixed positions; and the two digit folds
terminate with either an in-range integer or refusal. Thus each buffer has one
of the two parser outcomes. `STAT_READ` then partitions primitive behavior into
`BUFFER`, `READ_ABSENT`, `READ_UNREADABLE`, `READ_ERROR` or
`PRIMITIVE_FAULT`; composing it with the parser gives exactly the six observer
outcomes and no fall-through.

**Q1 answer:** yes, the parser itself is exact, total and shared.

## Q2 — SC-9/SC-10 decision function

For a table `E`, define the claimed decision as the terminal attached to the
least numbered phase with a satisfied terminal predicate. This is a function
for Phase 1 malformed, Phase 2 stale and Phase 3 recorded-protected faults, and
fresh protection dominates Phase-5 identity/group mismatch. Recorded protected
membership across every role/state/ownership and protected value terminates
before candidate filtering. A Phase-4 fresh protected hit in the actual
prospective domain discards all collected candidates and reaches no signal.

It is not a total single-valued function once later SC-8 faults are included:
Y-M1's Phase-4 table has terminal set `{T1,T3}` at the same least phase and its
sequential result changes under permutation. Therefore the literal Q2 answer is
**no**.

No static table whose recorded group is protected can reach `_killpg`, and no
table whose Phase-4 observations already contain a protected fresh group can
reach it. A temporal Phase-6 schedule can have signalled an earlier safe group
before a later per-signal recheck newly observes another group as protected;
the contract explicitly calls that `FREEZE_ABANDONED`. It permits no signal to
the protected group and no signal after discovery, but it disproves an
unqualified claim that a pass can never contain both an earlier signal and a
later fresh-protected observation.

## Q3 — Phase 4 candidate set and exclusions

The operational set is complete as the complement of four exclusions among
structurally valid current entries:

```text
signed tuples                                      72
excluded by role WATCHDOG first                    24
then state REAPED                                  12
then ownership REAPED                              12
then pgid_or_null NULL                             12
prospective Phase-4 tuples                         12
```

Trace results:

- NULL after creation, non-leader observation, ordinary observation failure or
  timeout contributes no Phase-3 group, is excluded from Phase 4, fails KV-2 in
  Phase 5, is absent from SC-2 and cannot reach the final recheck or signal.
- WATCHDOG is never signalable. Its normal `setsid=False` lifecycle leaves it a
  non-leader with NULL recorded group; if a conforming exceptional topology
  gives it a recorded leader group, that group is inserted into G and its own
  recorded value terminates Phase 3.
- CONTRADICTED entries with non-NULL groups are checked in recorded and fresh
  form before their Phase-5 KV-2 skip. REAPED state or ownership is checked in
  recorded form, then excluded from unsafe fresh PID-reuse observation and
  skipped by KV-2.
- Every group entering Phase 6 came from Phase-5 KV_OK and is freshly checked
  at each action; any newly protected observation abandons remaining action.

The four safety proofs are therefore sufficient. The overbroad fresh-form and
WATCHDOG-necessity prose is Y-L1, not a signal-scope expansion.

**Q3 answer:** candidate membership and no-signal consequences are complete;
the universal fresh cross-product/necessity description is not literal.

## Q4 — KG-2 population and transition graph

The named nominal graph covers creation failure/success for all three roles,
the six ordinary observation results, wrong-shaped returns, non-`OSError`
exceptions, EINTR, deadline exhaustion, generation invalidation, reap and
release. Group provenance is limited to the one PCS writer, a current child pid,
one canonical observation, exact identity equality and `pgrp == pid`; no
request, durable artifact or default can populate it. Reap freezes the last
value, release removes the handle, and ids are not reused. No unnamed seventh
nominal state is necessary.

But the transition is not exact because Y-M2 gives both H-NULL-GROUP and
H-GROUP-RECORDED at the same TIMEOUT response. Accordingly the literal Q4
answer is **no** despite otherwise complete route names.

## Q5 — OR-4 bytes, resolved identity and quarantine

I independently located the eleven source spans by their sentinels, checked
cardinality and non-overlap, extracted the fenced replacements, applied the four
literal single-line replacements, and spliced in ascending source order. Every
source/replacement length reproduced:

```text
       source  replacement
S1       2184         2120
S2        163           61
S3        598          207
S4        298           22
S5        299           47
S6        218           61
S7        982          727
S8       1329          440
S9        504          271
S10      9868         9778
S11       449          315
```

All 22 pinned span hashes matched. The independent output is:

```text
FULL OUTPUT    586426 bytes
3a88798f8f18a5e2f38108c9873e5b36045c7533126685034ad17a28998dc339
H_BODY         f57002460cc94d5f1c220193459ec662f713e0f5e3a1564f76f1732d4e1830df
H_GUARDDATA    faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE    3bbd378dec0d189d1b4374970a01272b73634c539eb2182773e46ea4cec6811f
```

Guarddata is byte-identical. The 4,167-byte handoff region hashes to
`7c5cabe2e48587ad34cd19ae0f4300f78965b27afc93cb719868aae9f5cd44a7`;
the 223,866-byte joint region hashes to
`7f58b11dfaaa2a59aa3fd9ab48bc350049461d1771cdc609b9d2b81dd5b2c8fa`;
each is byte-identical in amendment, source composite and resolved composite.

MP-1 independently reproduces at 586,621 bytes and
`afbdb075d2d8dbb864e163cf0be5927b495d29d36a70ae641981938129275ccf`.
It produces zero D1/D2 matches, zero outside-guard markers, unchanged guarddata
and intact class-R content, but fails PO-0.

**Q5 answer:** yes, all transformation and quarantine bytes reproduce.

## Q6 — quarantine claim and W-A count

Binding §2.6.0 expressly limits D1/D2 to the 11 and 13 exact normalized
literals, withdraws arbitrary-semantic-paraphrase coverage and makes PO-0 the
primary whole-output quarantine. The binding, handoff, packet and closure do not
restore the withdrawn broad claim; historical mentions identify it as
withdrawn. Handoff T-9 says “listed literal,” and T-10 requires MP-1 to evade
the literal detectors but fail PO-0.

The resolved W-A option token occurs exactly three times: the S1 historical
rejection, TS-1 grammar and CK-14 fixture. The W-A amendment token occurs twice.
No stale assertion of a post-resolution W-A option count of two remains in the
four current surfaces except as an explicit report of v3's withdrawn error.

**Q6 answer:** yes, the claim is now no broader than exact-literal defence plus
full-output identity, and MP-1 demonstrates the boundary.

## Q7 — counts, maintenance rows, identities and shared regions

Independent extraction gives:

```text
MS-2                       71 rows, 71 distinct paths
MS-3                        7 rows,  7 distinct paths
MS-2 intersection MS-3     empty
MS-8                       85 = 2+71+7+1+1+2+1
provenance                 79 rows, 79 distinct paths
                            = MS-2 union MS-3 plus verifier baseline
recorded M2+M3 digests     78
```

The four new MS-2 rows and their digests match the packet. Titles, openings,
MS-1 paths, DA-1 history, DA-4 live surfaces, TS-1 paths, IR-11 pairings and the
v1.10/v1.13 live identities are correct. Exactly one A0.4 anchor line matches
the grammar and its value equals the pinned composite H_FILE. Retired anchor
segments are absent. The two shared regions are byte-identical as reported in
Q5.

The maintenance sweep nevertheless fails on rows 105/106 as Y-M3 proves.
Therefore the literal Q7 answer is **no**: 71/85/79 and the live identities are
right, but stale current-generation accounting remains.

## Q8 — getpgid implementability boundary

The governing pair already promises mandatory bootstrap observations no
conforming implementation can supply. The separate runtime-authorization gate
prevents execution now but cannot repair an accepted primitive surface later.
The exact reachability proof and smallest repair are Y-M4. Amendment v1.10 must
not be accepted while this remains mechanically unreachable.

**Q8 answer:** current Major implementability defect; no conforming fail-closed
gate isolates it for acceptance.

## Exact next boundary

The next permissible boundary is a bounded replacement governing generation,
not acceptance and not implementation. It must, at minimum:

1. totalize same-phase SC-8/KV-6 terminal reduction and its fixtures;
2. make KG-2 population conditional on one unambiguous AWAIT_STOP outcome;
3. repair current test-row member cardinalities; and
4. bind and validate both `_getsid` and `_getpgid`, regenerating all affected
   exact-byte identities and review inputs.

Only after independent X/Y review confirms that replacement may Kirill consider
its replacement acceptance token. This review permits no acceptance of
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10`,
no scaffold, implementation, key, OR step, install, activation or identity
weakening. `T = NOT_ACTIVATED`; claim = `OPEN`.
