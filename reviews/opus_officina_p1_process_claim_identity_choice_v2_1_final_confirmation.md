REVISE_OFFICINA_P1_IDENTITY_V2_1

# Bounded final X-line confirmation — P1 process-claim identity choice v2.1

**Reviewer:** Claude Code Opus, independent X-line engineering reviewer. I did
not author v2, v2.1, v1, the supervisor/control-channel chain, or any prior
review. This is a **bounded final confirmation**, not a design round: on the
committed v2.1 bytes I check whether the two residual defects the previous X and
Y confirmation lines returned `REVISE` on are now closed, whether the repair
introduced a new defect, and whether the eight already-closed findings survive.
I treated `reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md`
as an **untrusted author self-assessment** and re-derived every load-bearing
point from the signed contract bytes. Read-only; SHA-256 only; no file edited but
this one deliverable; no code, probe, process-control operation, activation,
spend, or programme movement.

**Verdict: `REVISE_OFFICINA_P1_IDENTITY_V2_1`.** Repair 2 (`C-5` / `YV2-C1`) is
**fully closed** and correct on the bytes. Repair 1 (`X M-2` / `Y-C1`
enforcement residual) is **substantially but not fully closed**: it leaves one
concrete leak of the same class the previous round flagged, surviving because the
`M-R4` closure's decidability rests on a premise — "each durable artifact has
exactly one open site" — that the governing composite establishes for *installs*
and for *P1-layer* reads, but **not** for *peer-layer* reads of the process
claim, which is the one root where the governed code lives. A concrete AST passes
every rule of `S-25a`..`S-25m` and reaches a second sink. The fix is small,
concrete, and preserves "no taint" (below). This is a bounded revision, not a
block: nothing here contradicts a signed contract or inverts an authority.

---

## 0. Custody — all recomputed on committed bytes

**Targets (this round):**

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
```

The v2 draft digest matches the digest **both** prior confirmation lines pinned
and the value v2.1 §1 records as its repair target. The closure digest is
recomputed here rather than embedded (a file cannot carry its own digest); it is
verified by `sha256sum` on the committed bytes.

**Prior confirmations and v1, confirmed byte-untouched:**

```text
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md   [MATCH]
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md    [MATCH]
```

**Governing contracts, recomputed — every digest matches the closure's §2.3:**

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

The bytes v2.1 repairs are the bytes the two `REVISE` verdicts were returned
against, and the contracts I re-derive from are the signed ones.

---

## Determination 2 (taken first — it carries the verdict): a leaking AST that satisfies every `S-25a`..`S-25m` rule

### The construct

Inside `src/philosophia/officina/generic_harness.py` — the peer root, the one
root where every governed value actually lives:

```python
# process_id is a non-restricted claim key (a 64-hex digest), freely in scope
# in the peer layer, which builds the claim (MS-4). It is NOT controller_pid
# or process_group_id and no rule restricts it.
p   = "successor/officina/runtime/T_PROCESS_CLAIMS/" + process_id + ".json"
raw = open(p, "rb").read()          # builtin open is RETAINED in this root (S-25i-N1)
m   = json.loads(raw)               # json is a general peer-layer import
vals = list(m.values())             # m is NOT one of the three governed mapping Names
leaked = vals[5]                    # controller_pid by canonical key order; vals[7] = process_group_id
<peer capacity / custody / selection / Q-C / scientific expr>(leaked)
```

Key order verified from the canonical claim key set
(`…T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238`): the twenty keys place
`controller_pid` at index 5 and `process_group_id` at index 7. `json.loads`
preserves the canonical insertion order, so `vals[5]`/`vals[7]` are the two
restricted integers by position, using neither key literal.

### Why it passes every rule — checked clause by clause on the v2.1 bytes

- **`S-25a`/`S-25b`/`S-25c` (governed-Name occurrence count):** the construct
  never names `attested_pid`/`attested_pgid`. The count stays at its pinned
  three. **Blind.**
- **`S-25d` / `ACC-R1(a)`,`(b)` (literal-key / attribute):** no `"controller_pid"`
  or `"process_group_id"` string literal appears; `.values()` has no key operand;
  no Attribute names either key. **Blind.**
- **`ACC-R1(c)`,`(d)` and `S-25d`'s "or any wholesale or byte-level form":** these
  clauses govern accesses of *"a t-process-claim.v1 object."* To fire on `m`,
  `raw`, or `p`, the verifier must **know** `m` is a claim object — i.e. trace
  `path-literal → open → bytes → json.loads → mapping`. That is precisely the
  taint/flow reasoning `D-9` forbids. The **decidable** recognizer for "claim
  mapping" is `M-R3`/`M-R4`: the three governed Names produced by the four
  enumerated calls. `m` is none of them. **Blind under the no-taint constraint.**
- **`S-25i` (reflection/dunder):** `open`, `json.loads`, `list` are not in the
  forbidden-name set; `S-25i-N1` **explicitly retains** the builtin `open` in
  `generic_harness.py`; `json.loads` is not one of the `(iii)` reflective
  qualified forms (that list is `JSONDecoder`/`JSONEncoder`); no dunder Attribute
  appears. **Blind.**
- **`S-25j` (governed mapping discipline):** fires **only** on the three governed
  mapping Names. `m` is not one. The rule's own scope note is decisive here:
  *"Ordinary peer-layer mappings … are entirely unaffected, and `.values()`,
  `.items()` and `**` remain available on them"* (v2.1 :333-336). So
  `list(m.values())` on the laundered mapping is **affirmatively permitted** by
  the rule as written. **Blind by design.**
- **`S-25k` / `CR-1`..`CR-4` (carrier discipline):** fires **only** on the three
  carrier Names (`CR-2`). `raw` is not one of them. `CR-1` defines the byte class
  "however obtained," but `S-25k` enforces **positions on three Names**, not a
  semantic class-membership test on arbitrary Names. **Blind.**
- **`M-R1`/`M-R2`:** `json.loads` returns a plain `dict` with a str-key surface
  and no attribute surface, so `M-R1` is *satisfied*; `M-R2` bans the two keys as
  Attributes, and none is used. **Satisfied — not violated.**
- **`M-R4` (the rule meant to catch this):** *"No other expression … may yield a
  claim or lease mapping."* `m = json.loads(raw)` violates this **in intent** —
  but its enforcement is not decidable here. `D-8` grounds `M-R4`'s decidability
  in "the durable-read route to a mapping is `MS-2 → MS-3` with both sites
  enumerated. §P1-13.7 already gives each durable artifact exactly one open
  site." That premise fails for peer-layer claim reads (see below), so the
  verifier cannot classify the un-enumerated `json.loads` as a claim producer
  without the forbidden flow analysis. **Not enforced.**
- **`MS-R1`:** constrains the *MS functions* (defined once, called at enumerated
  sites). The construct calls **no** MS function — it inlines `open`+`json.loads`,
  bypassing `_read_claim_bytes` and `_claim_mapping_from_bytes` entirely. **Not
  triggered.**
- **`S-25e`/`S-25f`/`S-25g`/`S-25l`/`S-25m`:** accessor-return / whitelisted-shape
  / destination / count rules — none triggered; `leaked` is a bare `int` the
  rules do not track. **Blind.**

Every rule of `S-25a`..`S-25m` is satisfied, and `controller_pid` reaches a
second sink. **Determination 2 is met: a leaking AST exists.**

### Why the premise fails — the peer-layer claim read is not open-site-pinned

`D-8`'s load-bearing sentence is *"§P1-13.7 (:2357-2368) already gives each
durable artifact exactly one open site."* Re-derived from the composite bytes,
`§P1-13.7` gives each interface operation *"exactly one root and one function, so
that no two layers can **install** the same no-replace record."* Its table pins
**install** sites and a few **named** reads (spawn-intent at `SPAWN_ROLE`,
supervisor identity at `c17` and in the watchdog). Invariant 84 (composite
:2753) pins that *"the P1 layer opens the process-claim … on **no** path"* —
i.e. it constrains the **P1 layer** (the four scripts), not the peer layer.
Invariant 88 (:2757) enforces single **install** sites ("duplicate claim
**write**"). None of these pins the **peer layer's** process-claim **read** to a
single `open()` site — and:

- the builtin `open()` is deliberately retained in `generic_harness.py`
  (`S-25i-N1`), where the peer layer already opens many durable records
  (spawn-intent, supervisor-identity, freeze-observation) via `open`+`json.loads`;
- the claims-directory path literal
  `successor/officina/runtime/T_PROCESS_CLAIMS/` is **not** pinned to a single
  construction site — `MS-1` is *a* construction site, but no rule makes it the
  *only* one, and `process_id` is freely available;
- `MS-2` is itself called at **≥2** sites by design (post-install verify, and the
  `EEXIST` occupant load `MS-11`), so "exactly one open site" is not even true
  within the packet's own design.

So the reflection/mapping/carrier closure is airtight **only while every claim
byte string is forced through a carrier Name** — which holds if and only if
peer-layer opens of the claims path are pinned to `MS-2`. They are not. This is
the same defect class the previous X round demonstrated (`E1:
list(claim.values())[5]`); v2.1 closed it for the *governed* Name `claim_mapping`
(via `M-R1`/`M-R2`/`S-25j`) but the "launder into a fresh mapping via a second
open" variant survives, because the input pins `M-R4`/`D-8` assume are absent.

### The smallest repair (closes it; introduces no taint, no call graph, no fixpoint)

Add to §2, over `generic_harness.py` specifically, three occurrence/position
rules — each a single-AST-walk property, exactly the discipline v2.1 already
uses:

1. **Pin the claims path literal.** The string constant
   `successor/officina/runtime/T_PROCESS_CLAIMS/` (and any expression yielding a
   path under it) occurs at **exactly one** site, `MS-1`. Any other occurrence is
   a static violation (the `G-8`/`G-9` single-occurrence discipline, applied to
   this literal).
2. **Pin the claim open.** In the five roots, `open(...)` (and any `os`/`pathlib`
   read) whose path operand is `claim_path`, the occupant path, or any
   `T_PROCESS_CLAIMS` path occurs **only** inside `_read_claim_bytes` (`MS-2`), so
   every claim/occupant byte string is bound to a carrier Name.
3. **Pin `json.loads` of a claims read** to `MS-3` (subsumed once (2) forces the
   bytes into a carrier, since `CR-3` already bars `json.loads(carrier)` outside
   `MS-3`).

With (1)+(2), `raw = open(<claims path>).read()` at any non-`MS-2` site is a
static violation, `json.loads` can only ever see a carrier, `M-R4` becomes
**decidably** sound, and `list(m.values())[5]` on a laundered fresh mapping is
unreachable. After this lands and a bounded X/Y round confirms the repaired
bytes, Repair 1 is closable.

---

## Determination 1 — do `S-25i`, `M-R1/M-R2`, `CR-1..CR-4`, `S-25j/k`, and `MS-1..MS-12` close every route without taint/call-graph? **REFUTED (one route open).**

For every route where the mapping or bytes are reached through a **governed
Name** (`claim_mapping`/`lease_mapping`/`occupant_mapping`) or a **carrier Name**
(`canonical_bytes`/`claim_bytes`/`occupant_bytes`), the closure is sound and I
confirm it:

| Route | Rule that fires | Confirmed |
|---|---|---|
| `list(claim_mapping.values())[5]` | `S-25j` (`.values` Attribute on a governed Name; `list` not approved; result has no `M-R4` producer) | ✅ |
| `claim_mapping.controller_pid` | `S-25j` via `M-R1`+`M-R2` | ✅ |
| `locals()["attested_pid"]`, `globals()`, `vars`, `getattr`, `eval`, `dataclasses.asdict`, `__dict__[…]` | `S-25i` (name / dunder match), all five roots | ✅ |
| `a,b,*rest = claim_mapping.values()`; `for k in claim_mapping`; `{**claim_mapping}`; `f(**lease_mapping)`; comprehensions; `sorted/next/iter/max` over a governed mapping | `S-25j` | ✅ |
| `json.dumps(claim_mapping)` off-site | `S-25j` | ✅ |
| `canonical_bytes[40:47]`; `claim_bytes.decode().split(":")[6]`; `re.search(…, canonical_bytes)`; second hash/encoding | `S-25k` (`CR-4`), `S-25i(iii)` | ✅ |
| `json.loads(claim_bytes)` inline (carrier Name as operand) | `S-25k` (`CR-3`: carrier outside its four positions) | ✅ |
| pattern match `case {"controller_pid": v}` on a governed mapping | `S-25j` (subject outside approved call) **and** `ACC-R1(a)` (key literal) | ✅ |
| structural inverse (construct candidate claim, compare digests) | fails at first bound identity integer: `S-25c`/`M-R4`/`S-25j` before any hash (`WL-2`, `DC-5`) | ✅ |

**The one open route** is the launder-into-a-fresh-mapping variant of
Determination 2: reach the claim bytes through a **non-carrier** Name via a
second `open()`, `json.loads` into a **non-governed** mapping Name, then
`.values()[5]`. It touches no governed Name, no carrier Name, no key literal, no
dunder, no reflective name — so `S-25i/j/k`, `M-R1/M-R2`, `CR-*` are all blind,
and `M-R4`'s intended catch is not decidable without the pins named above. So the
answer to the closure's bounded X-question is **NO**, and the one construct that
reaches a second sink while satisfying every rule of `S-25a`..`S-25m` is the AST
above.

---

## Determination 3 — root-wide bans vs. the actual five production roots. **Mechanically compatible; one nonblocking flag.**

- **Reflective-module names** (`copy`, `pickle`, `marshal`, `inspect`,
  `operator`, `importlib`, `builtins`) banned by `S-25i(i)` are **absent from
  `generic_harness.py`'s 17-module allowlist** (`__future__ ast dataclasses
  datetime enum fcntl hashlib hmac json os pathlib re subprocess time typing
  weakref _socket`), so banning them as Names forbids nothing importable. ✅
- **Builtin reflection** (`getattr`/`setattr`/`delattr`/`vars`/`globals`/
  `locals`/`eval`/`exec`/`compile`) is already banned in the PCS and role roots
  by `S-7` (composite; the "PCS and role roots" scope is confirmed verbatim, and
  `S-23`/`CHANGE 5` show the framers say "no production root"/"all five roots"
  when they mean wider — so `S-7`'s two-root scope is deliberate). `S-25i`
  extends the ban to the peer root as its **own** rule without editing `S-7`'s
  committed bytes. No required governance behavior in the composite grammar needs
  these. ✅
- **`S-25i-N1`** correctly does **not** add builtin `open` to the peer root's
  forbidden set (the peer layer's signed durable I/O is preserved). ✅ — this is
  the correct decision, but it is exactly the surface the Determination-2 leak
  exploits, which is why the *open-site pin*, not an open *ban*, is the right fix.
- **Nonblocking flag:** `S-25i(iii)` forbids `json.JSONEncoder`/`json.JSONDecoder`
  root-wide, while `ACC-4` (`MS-6`) must produce "the canonical serialization …
  the peer contract already fixes for durable records" and "invents no encoding."
  Standard canonical JSON (`json.dumps(..., sort_keys=True, separators=(",",":"))`)
  needs no encoder subclass, so this is compatible **provided** the fixed
  canonical encoding is achievable without a `JSONEncoder` subclass. The packet
  should state that it is; I classify it **nonblocking** because the standard
  canonical form satisfies it, but it is an unstated dependency.

No root-wide ban accidentally forbids a required behavior without a named
replacement, on the composite grammar and allowlists.

---

## Determination 4 — is the whole-canonical-byte `ACC-4`/`ACC-5` exception the only field-level-accessor exemption, and can it expose intermediate bytes/fields? **CONFIRMED, and it cannot — within its operand pinning.**

- `ACC-R4` makes `ACC-1..ACC-5` the complete accessor set; a sixth is a static
  violation. `RC-1`/`RC-3` state `ACC-4`/`ACC-5` (`MS-6`/`MS-7`) are the **one**
  mapping-and-byte consumer exempted from the field-level rules, and are **rows of
  the same approved-call table**, not a carve-out. ✅
- `ACC-R5` forbids, in the `ACC-4`/`ACC-5` bodies, any Subscript, slice, decode,
  split, regex, loop, comprehension, format, or branch over the operand —
  checked as a **node-type match** by `S-25k`, not inferred. So neither function
  can bind, return, or surface an intermediate field or byte range: whole mapping
  in → carrier out (`ACC-4`); whole carrier in → 64-hex digest out (`ACC-5`). ✅
- The `ACC-5` count is single-valued: the lineage call site (→ `D-1`/`D-2`) and
  the `X-4` occupant-hash comparison (→ a boolean, reaching neither destination).
  Verified against §3.2 and `S-25e`/`S-25l`. ✅

**Caveat, consistent with Determination 2:** `ACC-4`'s operand is a *governed
mapping Name* and `ACC-5`'s is a *carrier Name*. The exemption is airtight for
those operands. The Determination-2 leak does **not** go through `ACC-4`/`ACC-5`
at all — it inlines `json.loads`, so it is not an exemption breach; it is the
same `M-R4`/open-pin gap. The exemption itself is correctly the **only** one and
is well-bounded.

---

## Determination 5 — do the eight closed findings remain closed, and are counts/handoff exact? **CONFIRMED.**

The two-row replacement index (§0.2) touches only §2.6.3/§2.11 (Repair 1) and
§2.6.2/§2.6.1 (Repair 2). The eight findings' loci — `X M-1` (§2.8), `X m-1`
(§2.3 `A-P4a..d`), `X m-2` (§2.2 `PID_MAX_LIMIT=4194304`), `X m-3` (§6.1), `Y-C2`
(§2.8), `Y-M1` (§2.10), `Y-M2` (§3.2), `Y-m1` (§1.5) — are **not** in the index
and carry forward verbatim. Spot-checked against the bytes:

- `Y-M2`: `t-process-record.v1` keys (`…ACTIVATION_PROTOCOL:248-257`) contain
  **neither** `controller_pid` nor `process_group_id` and **do** carry
  `process_claim_sha256` — the corrected "two superseded schemas" count stands. ✅
- The claim key set is exactly **20** keys (`:231-238`); the lease is the claim
  keys plus five (`:241-246`). ✅

**Counts (§6.1), verified internally consistent:** consumers 4→**5**
(`C-1..C-5`); accessors 3→**5** (`ACC-1..ACC-5`); verifier rules 8→**13**
(`S-25a..S-25m` = 13); tests 12→**17** (`A-T1..A-T17`); governed mapping Names
**3**; carrier Names **3**; approved call sites **12** (`MS-1..MS-12`);
declassifications **exactly 1**. Handoff steps 5/6/7 amended and new step 11
present; steps 1–4/8–10 unchanged. All exact. ✅

Note: finding the Repair-1 residual is **not** a reopening of a closed finding —
`X M-2`/`Y-C1` were classed "substantially closed — residual," and the residual
is exactly what v2.1 set out to close; I find the *repair* incomplete, not a
previously-closed item broken.

### Repair 2 (`C-5` / `YV2-C1`) — independently CONFIRMED closed

Re-derived from the signed bytes, not the closure:

- **The finding is real.** `process_claim_sha256` is required durably by
  `…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102` (`T_PROCESS_STARTED`, `D-1`) and
  `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257` (`t-process-record.v1`, `D-2`);
  the hashed claim bytes contain both restricted integers; the operation binds
  neither key literal, so it escaped `C-1..C-4`. ✅
- **The destination set is exhaustive.** I re-ran the repository-wide search: in
  the **governing** chain `process_claim_sha256` occurs at exactly
  `…CONTRACT_V2_DRAFT.md:101` (`D-1`) and `…ACTIVATION_PROTOCOL:252` (`D-2`). It
  is **absent** from the governing composite `…P1_OPERATIVE_COMPOSITE_V1_2.md` and
  from **both** accepted peer contracts (`…GENERIC_HARNESS_CONTRACT_V2_3_1` and
  `…BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1`, grep count 0). The only other
  occurrences are the `OK`/`CLAIM` reply matrix in **earlier** control-channel
  files (`…V2_DRAFT:354`, `…V2_1:1156`, `…V2_1_1:479`), which composite authority
  level 3 marks *"immutable historical and provenance evidence only."* §3.6's
  disposition is correct. ✅
- **The declassification model (`DC-1..DC-7`) is single-valued and sound.** The
  digest is the sole named declassification; `ACC-R5` forecloses field exposure;
  `DC-4` enumerates the full sink ban; `DC-5` closes the inverse route
  statically. The `WL-3` preimage residual is disclosed, not glossed, and `WL-4`
  correctly shows it transfers no authorization (no opcode accepts a pid;
  same-UID kernel capacity pre-exists observation). ✅

Repair 2 needs no further work.

---

## Determination 6 — the author's disclosed weak points, classified

| # | Author weak point | Classification |
|---|---|---|
| 1 | `S-25i` root-wide, broader than needed | **Nonblocking** — decidability price, disclosed at `B-A4`; a function-scoped ban would need a call graph. |
| 2 | `M-R1` representation pin on a peer record class | **Nonblocking** — implementation-shape constraint, scoped to governed Names; disclosed and priced. |
| 3 | `DC-1` model choice is the author's | **Nonblocking, with proof** — §3.5 and the verified §3.6 destination search give two independent reasons; the model survives a "reply-matrix live" ruling. |
| 4 | `WL-3` preimage residual (~4.2M candidates) | **Nonblocking, with proof** — confidentiality residual only; `WL-4`'s no-authorization/no-addressing argument verified against A3 same-UID capacity and the opcode grammar. |
| 5 | §3.6 rests on authority level 3 | **Nonblocking** — verified: key absent from governing composite and both accepted peer contracts; only in historical files. |
| 6 | self-found `X-3`/`X-4` precisions | **Nonblocking** — booleans only; `Y-M1`'s matrix/conjuncts/routing unchanged. |
| 7 | five roots are a fixed list | **Nonblocking** — decidability caveat; a sixth root re-derives every count. |

All seven disclosed residuals are acceptable. **The blocking item is one the
author did NOT disclose:** the `M-R4`/`D-8` decidability gap for peer-layer claim
opens (Determination 2). Weak point 1 is adjacent but is about `S-25i`'s
*breadth*, not about the *un-pinned peer-layer `open()`* that lets a laundered
mapping escape `S-25j`'s governed-Name scope. That is a **concrete blocker to
confirmation**, closable by the bounded repair in Determination 2.

---

## Verdict and authorization

**`REVISE_OFFICINA_P1_IDENTITY_V2_1`.**

Repair 2 is fully and independently closed. Repair 1 is substantially closed but
leaves one concrete leak: a fresh `open()` of the claims path in
`generic_harness.py`, `json.loads` into a non-governed mapping Name, then
`list(m.values())[5]`, reaches `controller_pid` at a second sink while satisfying
every rule of `S-25a`..`S-25m`. The root cause is that `M-R4`'s decidability
(`D-8`) assumes "each durable artifact has exactly one open site," which the
governing `§P1-13.7` establishes for installs and for P1-layer reads but not for
peer-layer claim reads. The fix is bounded and preserves "no taint": pin the
claims path literal to `MS-1`, pin claim opens to `MS-2`, and (thereby) pin
`json.loads` of a claims read to `MS-3`. After it lands and a bounded X/Y round
confirms the repaired bytes, v2.1 should be confirmable.

Because the verdict is `REVISE`, this round authorizes **nothing** — not Kirill's
A/B selection, not the `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` token, not
implementation, not activation. No existing file was modified in producing this
review; its sole product is this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT AUTHORIZED (REVISE)
```
