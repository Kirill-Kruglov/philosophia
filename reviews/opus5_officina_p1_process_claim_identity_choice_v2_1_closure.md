READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_1_FINAL_XY_CONFIRMATION

# Author closure — P1 process-claim identity choice packet v2.1 (bounded correction)

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, v1, v1.1, v1.2, the v1 and v2 choice
packets, and this v2.1 correction, and am therefore **disqualified** as its
independent X-line or Y-line reviewer. **This closure is an untrusted author
self-assessment.** The verdict on its first line is a readiness claim about one
bounded final confirmation round; it is not an X or Y verdict and it clears
nothing.

**No choice was made and no token was minted or accepted.** The selection is
Kirill's and is not signable until a bounded X/Y confirmation round confirms
v2.1 on identical bytes.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round produced no selection,
X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md` | 1205 |
| `reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md` | this file |

`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`,
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`,
`reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md`,
`reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md`,
`reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md` and
both v1 review files are **byte-untouched**, as §2 demonstrates by recomputing
their digests on committed bytes.

Only read-only commands were run against the repository: `git show`, `git log`,
`grep`, `sed`, `wc` and `sha256sum`. No test, behavioural probe or
process-control operation was executed. No code was implemented, edited, or
run. No `T` state was touched.

---

## 2. Hashes and custody

### 2.1 The two binding `REVISE` verdicts, and the bytes they were returned against

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
```

The first two digests are exactly the targets **both** confirmation lines
independently recomputed and pinned in their own custody sections. The bytes
v2.1 repairs are therefore the bytes both `REVISE` verdicts were returned
against, and the two defect reports being dispositioned are the two files above.

### 2.2 Prior round, confirmed byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md   [MATCH]
e8bceb8098c9a1d96fcd76f0796fccdcd49b79ce4cd690d1ef3a7d9ced54e128  reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md        [MATCH]
bfa7f6dd6a09313033b2a00c75f0e1e0632c63f65733b80424ee889433364f3b  reviews/opus_officina_p1_process_claim_identity_choice_review.md               [MATCH]
705b36b6ce1a9387261f66f2a473295be4384903b0e0240ae8e7496af6899e80  reviews/sol_officina_p1_process_claim_identity_choice_review.md                [MATCH]
```

`[MATCH]` is against the digests the v2 closure §2.1 pinned and both v2
confirmations independently recomputed.

### 2.3 Governing contracts, recomputed on committed bytes

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
```

Every previously pinned digest matches what v1.1, v1.2, the v1 closure, the v2
closure and both v2 confirmations recorded. **The custody chain is byte-intact
across this round.**

`…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` is newly pinned this round because
`Repair 2` rests on its §2c. Its governing status is established by
`OFFICINA_GENERIC_HARNESS_SIGNATURE.md` (signed 2026-07-26): the second signed
token accepts that file "as corrected, in order, by v2.1, v2.2, v2.3, and
v2.3.1", and none of the four corrections touches §2c. This was verified
directly rather than inferred from the Y line's citation.

### 2.4 Produced this round

```text
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
```

**On this closure's own digest.** A file cannot contain the SHA-256 of its own
committed bytes without a fixpoint, so this closure does not embed it. It is
recomputed by:

```text
sha256sum reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
```

Custody stays acyclic: v2 packet → v2 closure → two `REVISE` confirmations →
v2.1 correction → this closure → final X/Y confirmation → any future signature.
The v2.1 correction contains none of its own digests.

### 2.5 Evidence used, by source location

Every citation in v2.1 was read from the committed bytes of the contracts, not
from v2's, the reviewers', or v1's quotations:

```text
claim / lease / final-record key sets; process-id preimage; group immutability
  …ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238, :241-246, :248-257,
  :296-299, :300-305, :338-341, :88-97
the signed T_PROCESS_STARTED start event carrying process_claim_sha256
  …GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102, and the lease seed at :103-106
its governing status
  OFFICINA_GENERIC_HARNESS_SIGNATURE.md, "Accepted meanings", second token
the five production roots and the scoped import allowlists
  …P1_OPERATIVE_COMPOSITE_V1_2.md:349-357 (§P1-3.1), :359-380 (§P1-3.2)
the code rules, their exact scopes, and the scope evidence for S-25i
  same file :2558 (CHANGE 1), :2562 (S-1), :2566 (S-2), :2573 (S-4),
  :2577 (S-6), :2581 (S-7, "the PCS and role roots"), :2601 (S-12),
  :2626 (S-23, "no production root"), :2636 (CHANGE 4), :2638 (CHANGE 5),
  :2749 (invariant 80)
single-site durable opens, invalidity routing and dominance, same-UID capability
  same file :2357-2368, :1849-1866, :2323-2330, :1942, :1952, :1240
§Z4.6 conjunct 7
  …V2_1_1_CORRECTION.md:1047
the OK/CLAIM reply matrix examined and excluded at v2.1 §3.6
  …SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:1156;
  …SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md:354;
  …V2_1_1_CORRECTION.md:479; against composite authority level 3 (:44-50)
  and §P1-13.1's two accepted peer contracts (:2038-2049)
```

The destination search behind `C-5` was run as an exhaustive text search for
`process_claim_sha256` across every committed markdown file in the repository.
Four occurrence sites exist; two are the governing destinations `D-1`/`D-2` and
two are the historical reply matrix, dispositioned at v2.1 §3.6.

---

## 3. The exact two-row replacement index

**v2.1 is a bounded correction, not a replacement.** It carries v2 forward
verbatim except for exactly these two loci.

| # | v2 locus replaced | Replaced by, in v2.1 | Defect closed |
|---|---|---|---|
| **1** | §2.6.3 `ACC-R1`..`ACC-R4`, and the §2.11 texts of `S-25d`, `S-25e`, `S-25g`, **as they bear on indirect reads** | §2 in full — `S-25i` reflection and name-indirection lockdown over all five roots; `M-R1`..`M-R5` and `S-25j` the pinned mapping representation and position discipline; `CR-1`..`CR-4` and `S-25k` the carrier discipline; the `MS-1`..`MS-12` approved call-site table; and the replaced rule texts at §4.1–§4.4 | X-line determination 2 — the residual under `X M-2` and `Y-C1` |
| **2** | §2.6.2 `C-1`..`C-4`, `P-R1`, `P-R4`, `P-R5`'s route clause, and §2.6.1's "there is no declassifying operation" | §3 in full — consumer `C-5`; accessors `ACC-4`/`ACC-5` and `ACC-R5`; classification `DC-1`..`DC-7`; laundering analysis `WL-1`..`WL-4`; class member `(f)`; the reconciliation `RC-1`..`RC-4`; and the replaced rule texts at §4.1–§4.4 | Y-line `YV2-C1` |

**There is no third row.** Everything else in v2 — §1, §2.1–§2.5, §2.6.1 (as
extended only by member `(f)`), §2.6.4–§2.6.7, §2.7, §2.8, §2.9, §2.10, §2.12,
§3, §4, §5, §6, §7, §8, §9, §10 — is carried forward as written and is the
operative text.

---

## 4. One-to-one disposition of the two residual defects

### 4.1 The X bypass — determination 2, `X M-2` and `Y-C1` residual

| X-line construct | v2.1 rule that fires | Mechanism |
|---|---|---|
| `_vals = list(claim.values()); _leaked = _vals[5]` | **`S-25j`**, three times independently | `.values` is an Attribute on a governed mapping Name (`M-R5` position closure); `list` is not an approved call for that operand (§2.4 table); `_vals` has no approved producer (`M-R4`). |
| `_leaked = locals()["attested_pid"]` | **`S-25i(i)`** | `locals` is now a forbidden Name in **all five** production roots, `generic_harness.py` included. No rule has to reason about what the reflective call returns, and the string-Constant identifier is irrelevant. |
| `_leaked = claim.controller_pid` | **`S-25j` via `M-R1` and `M-R2`** | `M-R1` forbids any attribute-bearing representation of a claim or lease; `M-R2` bans the Attribute `attr` `controller_pid` anywhere, on any object, as a pure name match. Two independent violations. |

**Unpack and iteration variants**, each rejected by the same three rules with no
new clause and fixtured at `A-T14`: `a, b, *rest = claim_mapping.values()`;
`for k, v in claim_mapping.items()`; `for k in claim_mapping`; `{**claim_mapping}`;
`dict(**claim_mapping)`; `f(**lease_mapping)`;
`[claim_mapping[k] for k in claim_mapping]`; `sorted(claim_mapping.values())[5]`;
`next(iter(claim_mapping.values()))`; `max(claim_mapping.values())`;
`json.dumps(claim_mapping)` off-site. Reflective variants are fixtured at
`A-T13`: `globals()`, `vars()`, `getattr`, `__dict__`, `eval`,
`dataclasses.asdict`. Byte-level variants are fixtured at `A-T15(b)`:
`canonical_bytes[40:47]`, `claim_bytes.decode().split(":")[6]`,
`re.search(..., canonical_bytes)`.

**Against the X line's own repair specification**, item by item:

| X-line required repair | v2.1 locus |
|---|---|
| extend `S-7`'s forbidden-name set — `locals, globals, vars, getattr, setattr, delattr, eval, exec, compile, __import__, importlib`, and reflective frame access — to the scope the governed Names span | `S-25i(i)`–`(iv)`, over all five roots, plus a categorical ban on **every** dunder Attribute so that future reflective routes need no enumeration |
| pin the in-memory representation of `t-process-claim.v1` and `t-active-lease.v1` to a plain mapping | `M-R1`, with `M-R2` as an independent name match on the two key names |
| make `ACC-2`/`ACC-3` the **sole** syntactic path by which any value of such a mapping is bound to a Name | `M-R5` position closure plus the `MS-1`..`MS-12` table; `ACC-R1(c)` states it as a rule |
| forbid `.values()/.items()/.keys()`, `list()/dict()/tuple()/set()/sorted()` over such a mapping, `**`-unpacking, and attribute access to the two keys, outside `ACC-2`/`ACC-3` and the `C-2` copy | `S-25j`, by absence from §2.4's table rather than by the catalogue; the catalogue at §2.6 is illustrative and normatively redundant |

**Two things the X line did not ask for and v2.1 adds**, because the repair is
not closed without them: the **carrier discipline** `CR-1`..`CR-4`/`S-25k`
(reading the canonical bytes wholesale is itself a route to the integers, one
level below the mapping), and the **count closure** `S-25m` (so that adding a
sixth accessor or a thirteenth call site fails by arithmetic).

**No taint analysis, call graph, or fixpoint is introduced.** `S-25i` is a name
match and a node-type match; `S-25j`, `S-25k` and `S-25m` are occurrence counts
and position matches over six enumerated Names; `S-25d`, `S-25e`, `S-25g` and
`S-25l` are literal-key, call-site and destination matches. The whole of
`S-25a`..`S-25m` remains a single AST walk over the five roots.

**The occurrence-count design for direct parsed Names is preserved exactly**
(v2.1 `P-1`..`P-4`): `V-1`..`V-9`, `Z1-R1`..`Z1-R6`, `Z2-R1`..`Z2-R5`, the
exactly-three count, the "absence is sufficient" closure, §2.5.4 and §2.5.5 all
carry forward verbatim; `S-25a`, `S-25b`, `S-25c`, `S-25f`, `S-25h` are
unchanged in text; `A-T9`'s five fixtures are unchanged, including fixture 5's
`open()`; and `S-7`'s committed bytes at `:2581` are **not** edited — `S-25i`
states the wider scope as its own rule.

### 4.2 The Y finding — `YV2-C1`

| Y-line required repair | v2.1 locus | Exactness |
|---|---|---|
| add `C-5`: after canonical claim validation, exactly one whole-object SHA-256 over the canonical claim bytes may produce `process_claim_sha256` | §3.2 `C-5` | Precondition pinned to `MS-10` validation; operand is the complete canonical byte string; keys read individually at this consumer: **none** |
| solely for the already-signed `T_PROCESS_STARTED` and final process-record lineage destinations | §3.2 `D-1`, `D-2`, cited to `…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102` and `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257` | The destination search was run exhaustively (§3.6); two occurrences are the governing destinations, two are the historical reply matrix, dispositioned explicitly |
| no partial-field hash, alternate encoding, secondary digest, derived numeric identity, or other destination | §3.2 "FORBIDDEN, EXPLICITLY AND WITHOUT EXCEPTION", `DC-6`, `CR-4`, `S-25k`, `A-T15(b)` | v2.1 **invents no encoding**: `ACC-4` uses the canonical encoding the peer contract already fixes for durable records |
| one centralized canonical-byte hash accessor that may read validated raw claim bytes but may not bind either identity field individually | §3.3 `ACC-4` (sole canonical serializer) and `ACC-5` (sole hash accessor), with `ACC-R5` forbidding any Subscript, slice, decode, split, regex, loop, comprehension, format or branch over the operand — checked as a node-type match by `S-25k` | Two accessors rather than one, because the mapping→bytes and bytes→digest steps each need a single pinned site; `ACC-R4` states `ACC-1`..`ACC-5` is complete and a sixth is a static violation |
| state the one-way classification boundary: integrity/lineage identifier, never process identity or authority, and no addressing/signalling/waiting/capacity/custody/spend/selection/qualification/Q-C/datum/evidence/outcome/Proof | §3.4 `DC-3`, `DC-4`, `DC-5`; rule `S-25l`; test `A-T16` | `DC-4` enumerates the full sink list literally; `DC-5` closes the inverse route and shows it fails at its first line, before any hash |
| choose one exact model and make it single-valued | §3.4 `DC-1`: **the digest is the sole named declassification** from `RESTRICTED_PROCESS_IDENTITY` and from `RESTRICTED_CLAIM_CANONICAL_BYTES` — exactly one, one site, one operand shape, never a second. `DC-2` states that declassified is **not** unconstrained | The derived-class model is **rejected**, with the reason at §3.5 and a second independent reason at §3.6 |
| explain why the choice cannot launder the underlying fields | §3.5 `WL-1`..`WL-4`, plus class member `(f)` at §3.3 | `WL-1` no field-level route exists (syntactic); `WL-2` the inverse route fails before the hash; **`WL-3` discloses the real residual** — SHA-256 does not conceal a ~4.2M-candidate secret from a holder of the other eighteen fields, and the packet rests nothing on preimage resistance; `WL-4` shows why that transfers no capability and no authorization under A3/P1 |
| update `P-R1`, `P-R4`, `ACC-R1..ACC-R4`, schema-reader audit, `S-25d/e/g`, tests, consumer counts, blast radius, closure dispositions, v1.3 handoff | §4.1 (`P-R1`, `P-R4`, `P-R5`), §4.2 (`ACC-R1`..`ACC-R5`), §5 (extended audit), §4.3 (`S-25d/e/g`), §7 (`A-T13`..`A-T17`), §6.1 (counts), §6.2 (`B-A1`..`B-A7`), this closure §3–§6, §6.3 (handoff steps 5, 6, 7, and new step 11) | `A-T9` is unchanged in text; the new fixtures are added as `A-T13`..`A-T17` rather than folded into it, so the already-confirmed fixture set is not disturbed |
| reconcile `C-5` with the indirect-read repair | §3.7 `RC-1`..`RC-4` | The hasher is **the one explicit mapping-and-byte consumer exempted from the field-level accessor rules**, bounded by four syntactic conditions; `RC-3` states that it is a **row of the same approved-call table**, not a carve-out from it; `RC-4` states that `C-5` consumes the record, not the fields |

**Two self-found precisions, disclosed rather than folded in.** `ACC-R2` now
names the §2.10.3 `X-3` cross-field conjunct as a third unpack site, and §3.2
names the `X-4` occupant hash as the second and last `ACC-5` call site. Both
operations were already required by v2 §2.10.3 and both yield booleans only;
naming them makes the rules single-valued instead of implied. Neither changes a
row of the crash matrix, a conjunct, or a routing decision. They are listed at
v2.1 §9 item 6 as a point a reviewer may reasonably challenge.

---

## 5. No-regression table for the eight already-closed findings

Both confirmation lines accepted these eight as closed. **v2.1 changes no byte
of any of their repairs.**

| Finding | Accepted-closed repair | v2 locus that must remain intact | v2.1 effect | Evidence it is untouched |
|---|---|---|---|---|
| **`X M-1`** journal durability asserted, not shown | §2.8.1 verbatim withdrawal; §2.8.2 thirteen-key `J4` vector with `E-1`..`E-4`; §2.8.3 `R-P1`..`R-P4`; blast radius and handoff step 8 | §2.8, §5.1, §5.5, §7.1, §7.2 step 8 | **none** | not in the two-row replacement index; `S-25h` unchanged in text (`P-2`); handoff step 8 explicitly unchanged (§6.3) |
| **`X M-2`** no-second-sink rests on unproven taint | occurrence whitelist replacing taint | §2.5 in full | **extended, not replaced** | `V-1`..`V-9`, `Z1-R1`..`Z1-R6`, `Z2-R1`..`Z2-R5`, §2.5.4, §2.5.5 carry forward verbatim (`P-1`); `S-25a/b/c` unchanged (`P-2`); the residual is closed **around** the mechanism, not by altering it |
| **`X m-1`** fresh `getpgid` authority unstated | §2.3 `A-P4a`..`A-P4d` | §2.3 | **none** | not in the index; no accessor, mapping or carrier rule touches the PCS-side attestation |
| **`X m-2`** 7-digit bound unjustified | §2.2 `PID_MAX_LIMIT = 4194304`, `G-1`..`G-6`, platform premise, `A-T8` | §2.2 | **none** | not in the index; `A-T8` unchanged; the bound is **cited** at `WL-3` and not altered |
| **`X m-3`** freeze cases conflatable | §6.1 Case 1 / Case 2 by actor, trigger, citation, status | §6.1 | **none** | not in the index; §8.2 `N-6` restates the orthogonality |
| **`Y-C1`** sole-sink closure not closed; reload launders | §2.4 withdrawal; §2.6 class, `C-1`..`C-4`, `P-R1`..`P-R5`, `ACC-1`..`ACC-3`, recomputed audit, `NC-1`..`NC-3` | §2.4, §2.6 | **the residual half is closed; the closed half is preserved** | §2.4's verbatim withdrawal stands; `C-1`..`C-4` are unchanged in content and are **added to**, not revised; `C-2`'s `:241-246` justification, `C-3`'s `:300-305`, `C-4`'s `:1047`, `NC-1`..`NC-3` and §2.6.7 all carry forward |
| **`Y-C2`** replay not constructible from `J4` | §2.8.2 durable complete representation; §2.8.3 byte-identical redelivery | §2.8 | **none** | as `X M-1` |
| **`Y-M1`** crash table contradicts durable claim; `EEXIST` not convergence | §2.10.1 withdrawal; §2.10.2 boundary-keyed matrix; §2.10.3 `X-1`..`X-4`; §2.10.4 `I-1`..`I-10` | §2.10 | **none in substance** | every row, conjunct and routing is unchanged; `ACC-R2` and §3.2 only **name** the `X-3` and `X-4` sites that §2.10.3 already required, so they become single-valued |
| **`Y-M2`** Option B blast radius overstated | §3.2 verbatim withdrawal; corrected count of two superseded schemas | §3.2, §5.5, §7.1 | **none** | `B-A7` restates B's corrected count unchanged; §5's extended audit reaffirms that `t-process-record.v1` does not inherit the keys and carries only the digest |
| **`Y-m1`** overbroad argv rationale | §1.5 `R-1`..`R-4` with `R-4`'s exact scope; §4 | §1.5, §4 | **none** | not in the index |

**Also preserved unchanged, as the mandate requires:** `J4` and replay; the
crash matrix; `EEXIST` convergence; the pinned PID bound; the fresh-PGID rule;
the corrected Option B count; the `/proc` rationale; Option A as an **explicit
bounded lexical weakening granting no process-control authority**; Option B
**non-selectable** behind sub-cells `B-1` and `B-2`; the watchdog-freeze cell
**orthogonal and unresolved**; `T = NOT_ACTIVATED`; programme claim `OPEN`.

---

## 6. Amended counts and blast radius

| Quantity | v2 | **v2.1** |
|---|---|---|
| persistent consumers | 4 | **5** (`C-1`..`C-5`) |
| centralized accessors | 3 | **5** (`ACC-1`..`ACC-5`) |
| verifier rules added by Option A | 8 | **13** (`S-25a`..`S-25m`) |
| tests added by Option A | 12 | **17** (`A-T1`..`A-T17`) |
| governed mapping Names / carrier Names / approved call sites | not pinned | **3 / 3 / 12** |
| declassifications from `RESTRICTED_PROCESS_IDENTITY` | 0, asserted | **exactly 1**, named and pinned |
| **new blast-radius items disclosed** | — | a **root-wide reflective lockdown** on `generic_harness.py` that `S-7` did not previously reach; a **pinned in-memory representation** for two peer record classes |

**Unchanged and not re-priced:** signed sentences amended (1); peer-owned
durable record schemas superseded (**0** for A, **2** for B); new durable
schemas (0 for A, 1 for B); signed validity predicates reopened (**0** for A,
≥1 for B); architectural rules inverted (**0** for A, 1 for B); wire grammar (1
response grammar, **no request grammar**); durable formats changed (1 — P1's own
`J4`); collision/idempotency rules (1 — `EEXIST` `X-1`..`X-4`); migration
(none); **selectable today: A yes, B no.**

**Honest summary of this correction: A's implementation-shape surface grew
again — a root-wide reflective lockdown, a pinned record representation, five
more rules and five more tests — and none of the rows the recommendation rests
on moved.** A still reopens no signed validity predicate, inverts no
architectural rule, supersedes no peer-owned durable schema, and remains the
only selectable option.

---

## 7. Readiness verdict

```text
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_1_FINAL_XY_CONFIRMATION
```

**Meaning precisely.** Both residual defects are dispositioned one-to-one at §4,
each by a named repair at a named locus:

- the X-line residual is closed by foreclosing the three demonstrated bypasses
  and their unpack, iteration, reflection and byte-level variants at the
  syntactic level, in `generic_harness.py` specifically, **without
  reintroducing taint analysis**, and without altering the occurrence-count
  mechanism the X line confirmed is sound;
- `YV2-C1` is closed by naming `C-5` exactly, pinning its two accessors and its
  two destinations, choosing one single-valued classification model with stated
  reasons, and disclosing the one residual that model does not eliminate.

The eight already-closed findings are untouched, as §5 demonstrates row by row.

**Therefore, yes: the packet is ready for one bounded final X/Y confirmation
round**, scoped to (a) whether the two residual defects are in fact closed on
the v2.1 bytes, (b) whether the repairs introduced a new defect, and (c) whether
the eight closed findings survive intact. It is **not** ready for selection,
because a selection requires that round to confirm first.

**It does not mean the packet is correct.** This is an author self-assessment by
the party that wrote the defects being repaired.

---

## 8. One bounded confirmation question per reviewer

### For the X line — one question, yes or no

> **With `S-25i`'s reflective and name-indirection lockdown applied to all five
> production roots including `generic_harness.py`, `M-R1`/`M-R2`/`S-25j`'s
> pinned plain-mapping representation and position discipline over the three
> governed mapping Names, `CR-1`..`CR-4`/`S-25k`'s carrier discipline over the
> three carrier Names, and the `MS-1`..`MS-12` approved call-site table as the
> sole closure — is every read of `controller_pid` or `process_group_id`, by
> any syntactic route whatsoever, now caught by a governed-Name occurrence
> count, a literal-key match, a forbidden-name match, or absence from the
> approved call-site table, with no taint analysis, call graph, or fixpoint, so
> that `X M-2` and the `Y-C1` enforcement residual are fully closed?**

Answer `YES` or `NO`. A `NO` should name **one construct** that reaches a second
sink while satisfying every rule of `S-25a`..`S-25m`, since the counts, the name
matches and the call-site table — not any catalogue — are what the closure rests
on.

### For the Y line — one question, yes or no

> **Do `C-5` as stated at §3.2, its two pinned accessors `ACC-4`/`ACC-5` with
> `ACC-R5`, its exactly-two destinations `D-1`/`D-2`, and the single-valued
> classification model `DC-1`..`DC-7` — under which `process_claim_sha256` is
> the sole named declassification from `RESTRICTED_PROCESS_IDENTITY`, is
> positively classified as an integrity and lineage identifier only, and can
> reach no addressing, signalling, waiting, capacity, custody, spend, selection,
> qualification, comparison, Q/C, datum, evidence, outcome or Proof — together
> with the laundering analysis `WL-1`..`WL-4` including the disclosed preimage
> residual at `WL-3`, close `YV2-C1` completely and reconcile the whitelist with
> the signed `T_PROCESS_STARTED` and `t-process-record.v1` lineage?**

Answer `YES` or `NO`. A `NO` should name **either** a sixth persistent consumer
the signed chain requires, **or** a third destination the digest reaches, **or**
the route by which the declassification launders either integer.

Both lines should also confirm, as part of the same bounded round, that the
eight findings listed at §5 remain closed and byte-untouched, and that the
amended counts at §6 are exact.

---

## 9. The exact residual author choices

**Unchanged in substance by this correction.** v2.1 narrows nothing and adds
nothing to what Kirill must decide.

```text
RESIDUAL CHOICE 1 — the cell AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS.
  Exactly one of:
    I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
    I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
  A is selectable once the final confirmation round confirms v2.1. B is NOT
  selectable; directing it opens sub-cells B-1 and B-2 and requires a further
  packet before any composite can bind it.

RESIDUAL CHOICE 2 — conditional on A only.
    P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
  the bounded weakening of the signed process-authority sentence, in the exact
  text of v2 §2.12, carried forward unchanged. Selecting A without this token is
  not a coherent state. The weakening is LEXICAL-TO-SYNTACTIC and grants NO
  process-control authority.

NEITHER IS SIGNABLE UNTIL THE BOUNDED FINAL X/Y CONFIRMATION ROUND CONFIRMS
v2.1 ON IDENTICAL BYTES.

NOT A CHOICE IN THIS PACKET, AND NOT OPENED BY IT:
  AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM  — orthogonal, unresolved, and
  neither fixed nor worsened by either option (v2 §6). P1 remains non-operative
  until it is resolved, even if A is selected.
  Sub-cells B-1 and B-2                     — reachable only by directing B.
  §Z3.4's stale /proc indices under P1       — a separate peer-chain defect,
  recorded and not repaired here.
```

---

## 10. Weakest points in v2.1, stated by the author

Repeated from v2.1 §9 so that a reviewer sees them without opening the packet:

1. `S-25i` is root-wide, broader than the two identity fields need; a
   function-scoped lockdown would not be closed without a call graph.
2. `M-R1`'s representation pin forecloses a dataclass or attribute-bearing
   claim or lease; `S-25j` is scoped to governed mapping Names only, so other
   peer mappings are untouched, but a peer layer already using a dataclass for
   these two schemas would have to change shape.
3. `DC-1`'s model choice is mine, resolved for single-valuedness; §3.5 and §3.6
   give two independent reasons, but a reviewer preferring the derived-class
   model would have to reconcile it with the digest's onward signed chains.
4. `WL-3` is a real residual: SHA-256 does not conceal a ~4.2M-candidate secret
   from a holder of the other eighteen canonical fields. `WL-4` argues this
   transfers no capability and no authorization under A3/P1; a reviewer weighing
   confidentiality rather than authorization should say so.
5. §3.6's disposition of the `OK`/`CLAIM` reply matrix rests on the composite's
   authority level 3 and on the key's absence from both accepted peer contracts.
   If it is live under some other route, the destination count is three; the
   `DC-1` model survives that, but the count sentence would need amending.
6. `ACC-R2`'s `X-3` site and §3.2's second `ACC-5` call site were found by me,
   not by either reviewer, and are marked as bookkeeping precisions inside
   already-closed repairs rather than folded in silently.
7. Everything here is decidable because `PRODUCTION_ROOTS` is exactly five
   paths. A sixth root would require every count and closure to be re-derived.

Carried forward from the v2 closure and still live: §2.8.2's all-opcode `J4`
generalization is larger than its finding; the occurrence-count discipline is
strict enough to be awkward to implement; `NC-1`..`NC-3` remains the
least-scrutinized construction; §2.6.7's disposal of the admission-time
membership question depends on one reading of `SIGNAL_GROUP`'s precondition;
`A-P4a`'s fresh-read choice is an author judgement; and §7.1's recommendation
rests on fewer criteria than v1's did.

---

## 11. Negative authorization — explicit

This closure and the v2.1 correction authorize **nothing**. In particular:

```text
NO SELECTION. Neither A nor B is selected, recommended into effect, or treated
   as selected. No selection token is minted, accepted, signed, or made
   signable by this round.
NO TOKEN MOVEMENT. P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 exists only as
   proposed text in a draft packet, carried forward unchanged. It is NOT
   accepted here and this correction does not weaken the signed sentence.
NO X/Y VERDICT. The first line of this file is an author readiness claim, not
   an X-line or Y-line verdict, and not a signature. The two REVISE verdicts of
   the previous round remain the standing verdicts until a new round is run.
NO IMPLEMENTATION. No code, test, verifier rule, manifest entry or schema was
   written, edited, or executed. S-25a..S-25m, MS-1..MS-12, M-R1..M-R5,
   CR-1..CR-4, DC-1..DC-7, ACC-1..ACC-5 and A-T1..A-T17 are specification text,
   not artifacts. No production root was modified and none was executed.
NO ACTIVATION. T remains NOT_ACTIVATED. No activation record, claim, lease,
   process record, review record or invalidity record was created or read for
   effect.
NO PROCESS EXECUTION. No fork, exec, posix_spawn, signal, wait, prctl, socket,
   pipe or lock operation was performed. No supervisor, PCS, controller,
   worker, middle or watchdog was created or contacted. No behavioural probe
   was run. No /proc path was read for effect.
NO SPEND. No E1, E2 or E3 resource was reserved, charged or released. No
   capacity artifact, custody disposition, liability or ledger entry was
   created or moved.
NO DATUM, NO OUTCOME, NO PROOF. No scientific datum, observation, qualification,
   comparison, blinding claim, Q or C fact, entropy draw, world, learner or
   result manifest was produced, predicted, or optimized toward.
NO CLAIM MOVEMENT. The programme claim remains OPEN. No process claim was
   installed, read for effect, amended, or removed. No process_claim_sha256 was
   computed over any real record.
NO FILE MODIFIED. Exactly two files were created. v2, v1, the v1 and v2
   closures, both v1 reviews and both v2 confirmations are byte-untouched, as
   §2 demonstrates.
NO WATCHDOG REPAIR. AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM is untouched and
   unresolved, and P1 remains non-operative independently of this cell.
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_1_FINAL_XY_CONFIRMATION
```
