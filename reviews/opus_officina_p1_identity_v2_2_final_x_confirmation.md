REVISE_OFFICINA_P1_IDENTITY_V2_2

# Bounded final X-line confirmation — P1 process-claim identity choice v2.2

**Reviewer:** Claude Code Opus, independent X-line engineering reviewer. I did
not author v1, v2, v2.1, v2.2, the supervisor/control-channel chain, or any
prior closure. This is a **bounded final confirmation**, not a design round: on
the committed v2.2 bytes I check whether the three residuals the two binding
`REVISE` verdicts named are closed, whether the repair introduced a new defect,
and whether every previously accepted cell survives. I treated
`reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md` as an
**untrusted author self-assessment** and re-derived every load-bearing point
from the signed contract bytes. Read-only; SHA-256 only; no file modified but
this one deliverable; no code, probe, process-control operation, activation,
spend, or programme movement.

**Verdict: `REVISE_OFFICINA_P1_IDENTITY_V2_2`.**

Repair C (the cryptographic claim) is **fully closed** and correct on the bytes.
Repair B (the two `ACC-5` evaluations) is **closed for the claim and the
occupant** and correct at `EV-1`/`EV-2`/`OD-1..OD-4`/`L-1..L-5`. Repair A closes
the X-line's determination-2 construct **for the claims path** — the exact AST,
and every variant `V-a`..`V-q`, is genuinely rejected, and I could not defeat
`PA-1`..`PA-9` by any spelling, alias, helper, `pathlib`, `normpath`/`realpath`,
bytes path, closure, default argument, `chdir`, `dir_fd`, `/proc/self/fd`,
`mmap`, directory-enumeration or archive route **that targets the claims root**.

The verdict is `REVISE` because the repair pins **one** of the two durable
records that carry the two restricted integers. The **active lease** —
`successor/officina/runtime/T_ACTIVE_LEASES/<process_id>.json`, whose key set is
*the claim keys plus five* (`protocol :241-246`), which `v2 §2.6.1(d)` puts
**inside `RESTRICTED_PROCESS_IDENTITY` by name**, and whose reload `v2 §2.6.1`
expressly contemplates ("from a lease reload after a restart") — receives no
path pin, no read pin, no carrier position and no install row. The X-line's
determination-2 construct reproduces **verbatim** against it, passing every one
of `S-25a`..`S-25o`, and `v2.2` itself asserts that such a read **PASSES**
(`PC-R1`, `R-d`). `PT-1` corollary 2 states a lease property its own four-case
proof does not establish.

Two further defects are internal to the new rules: under `PA-6`'s own
definition, `MS-12`'s install call **is** a read call, so `PA-7` statically
rejects the packet's own install site; and `PA-5`'s "never a Constant" plus
`PA-7`'s constructor-binding requirement make the signed exact-constant
descriptor paths of `S-13`/`S-18` unspellable at the three `/proc/self/fd`
enumerations `§P1-6.5` requires.

All three are closable by bounded textual repair in the packet's own idiom. None
contradicts a signed contract; none requires a new architecture cell; none
reopens an accepted closure. This is a revision, not a block.

---

## 0. Custody — every digest recomputed on committed bytes

**Target, recomputed and matching the mandate's pinned value:**

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md   [MATCH]
```

**The chain it corrects, and the two binding verdicts it answers:**

```text
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/…PACKET_V2_1_CORRECTION.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/…PACKET_V2_DRAFT.md
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/…PACKET_V1_DRAFT.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md   REVISE
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md    REVISE
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
```

Every value in v2.2 §1.1–§1.2 matches my recomputation. The closure's own digest
is recomputed here rather than accepted (a file cannot carry its own digest).

**Governing signed chain, recomputed — all four match v2.2 §1.3:**

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

Each file above was verified **byte-identical to its `HEAD` blob** before being
read, so I reviewed the committed bytes.

**One custody note on the mandate itself.** The mandate names
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_CORRECTION.md`.
No such path exists; the v2 tier is
`…PACKET_V2_DRAFT.md` (`f5d95a0d…6095`), which is the file v2.1 and v2.2 both
name as their base and both `REVISE` lines pinned. I reviewed that file. No
substitution of content was made.

---

## Determination 1 (carries the verdict) — the lease is the unpinned half, and the determination-2 construct reproduces on it

### 1.1 What the signed chain says the lease is

```text
protocol :81       successor/officina/runtime/T_ACTIVE_LEASES/<process_id>.json
                   is a tracked durable path
protocol :241-246  "The active lease keys are exactly the claim keys plus:
                   last_charged_reading_ns, cumulative_charge_ns,
                   heartbeat_deadline_ns, outstanding_liability_ns,
                   prior_charge_event_sha256"
contract :103-106  the lease is installed with prior_charge_event_sha256 seeded
                   to the T_PROCESS_STARTED entry hash
contract :116-124  every heartbeat settles against active_lease_sha256, "the
                   hash of the exact pre-settlement lease"
```

So the durable lease **contains `controller_pid` and `process_group_id` in
cleartext**, at determinate canonical positions, exactly as the claim does. It
is not an analogue of the claim; by the protocol's own words it is a superset
of it.

### 1.2 What this packet says about the lease

```text
v2 §2.6.1(d)  RESTRICTED_PROCESS_IDENTITY contains "the values of the same two
              keys of any philosophia.officina.t-active-lease.v1 object,
              however obtained"
v2 §2.6.1(e)  and "every alias, copy, reload, deserialization, cached form",
              with "however obtained" glossed literally as including "a lease
              reload after a restart"
v2.1 CR-1     RESTRICTED_CLAIM_CANONICAL_BYTES is "every byte string that is,
              or is derived from, the canonical serialization of a
              t-process-claim.v1 OR t-active-lease.v1 object, however obtained"
v2.1 M-R3     lease_mapping is one of the three governed mapping Names
v2.1 M-R4     "No other expression in the five roots may yield a claim OR LEASE
              mapping"
```

The lease is therefore inside every restricted class this packet defines. Now
the v2.2 rules that were supposed to make those classes decidable:

```text
PA-1   pins exactly one substring: "T_PROCESS_CLAIMS"
PA-4   pins exactly one path Name: claim_path
PA-7   pins exactly one read: the claim read, to MS-2
PA-9(d) pins mappings produced from "A CLAIM-PATH READ"
PT-1   claims decidability for "a path under successor/officina/runtime/
       T_PROCESS_CLAIMS/" and for nothing else
PC-R1  "ONLY CLAIM PATHS ARE RESTRICTED"
R-d    "any other PC-N peer durable record built from a Constant root and a
       grammar-checked stem, read through a plain-Name operand   PASSES"
V-j    uses `_lease_path(...)` as its worked example of a PC-N constructor —
       so the packet itself locates a lease path constructor in the five roots
       and classifies it as unrestricted
```

The lease path contains `T_ACTIVE_LEASES`, not `T_PROCESS_CLAIMS`. It is a
`PC-N` row by construction, and `PC-R1`/`R-d` **affirmatively assert that
reading it passes**.

### 1.3 The leaking AST, in the peer root

Inside `src/philosophia/officina/generic_harness.py`, using the lease path
constructor `V-j` already presumes exists:

```python
lp     = _lease_path(process_id)     # PC-N constructor: Constant root + 64-hex stem
raw    = open(lp, "rb").read()       # builtin open RETAINED here (S-25i-N1, PC-R2)
m      = json.loads(raw)
vals   = list(m.values())
leaked = vals[5]                     # controller_pid; vals[7] = process_group_id
<peer capacity / custody / selection / Q-C / scientific expr>(leaked)
```

(The index is whatever the canonical order fixes; the lease is the claim key
set plus five appended, so the two integers sit at the same canonical positions
v2.2 §1 derives for the claim. The construct does not depend on which index it
is — only on the fact that the canonical order is signed and fixed.)

### 1.4 Rule-by-rule, on the v2.2 bytes

| Rule | Why it does not fire |
|---|---|
| `PA-1` | no Constant in the build contains `T_PROCESS_CLAIMS`. The pin is a substring test over one substring. **Blind.** |
| `PA-2` | the only path-building expression is inside `_lease_path`, over a Constant root and its own stem. **Satisfied.** |
| `PA-3` | the stem is the 64-hex `process_id`; the grammar check refuses `/`, `\`, `..`, leading `.`. **Satisfied.** |
| `PA-4` | governs the Name `claim_path`. `lp` is not it. **Blind.** |
| `PA-5` | the read's path operand `lp` is a plain Name. **Satisfied.** |
| `PA-6` | `open` is an enumerated read form; no `dir_fd`, no `follow_symlinks`. **Satisfied.** |
| `PA-7` | sentence 1 governs reads whose operand is `claim_path`. Sentence 2 requires the operand be "a Name assigned exactly once, in its own enclosing function body, from a call to a path constructor of §2.4 **other than MS-1**" — `lp` is exactly that. **Satisfied, by design.** |
| `PA-8` | governs "the byte string produced by **MS-2's** read". This is not MS-2. **Blind.** |
| `PA-9` | (a) the `json.loads` operand is the plain Name `raw` — **satisfied**; (b) `raw` is not one of `CR-2`'s three carrier Names, so the MS-3 confinement never engages; (d) is scoped to "A CLAIM-PATH READ". **Blind.** |
| `PT-1` | its four cases are over expressions that can denote a path **under the claims root**. `lp` denotes a lease path. **Out of scope by construction.** |
| `S-25n` | is exactly `PA-1`..`PA-9`. **Blind.** |
| `M-R1`/`M-R2` | `json.loads` yields a plain dict with a str-key surface; no Attribute names either key. **Satisfied, not violated.** |
| `M-R3`/`M-R5`/`S-25j` | fire only on the three governed mapping Names. `m` is not one, and `S-25j`'s own scope note affirmatively permits `.values()` on ungoverned mappings. **Blind by design.** |
| `M-R4` | violated **in intent** ("no other expression may yield a claim or lease mapping") and **not decidable**: its new anchor is `PT-1`, and `PT-1` proves nothing about a lease path. **Not enforced.** |
| `CR-1`..`CR-4`/`S-25k` | `CR-1`'s class covers lease bytes "however obtained", but `S-25k` enforces **positions on three Names**; `raw` is not one. This is the identical blindness the X line documented at v2.1, unchanged. **Blind.** |
| `S-25c`/`S-25d`/`ACC-R1` | no governed Name, no key literal, no Attribute, no wholesale access of a *recognized* claim object. **Blind.** |
| `S-25i` | `open`, `json.loads`, `list` are not forbidden names; `open` is deliberately retained here. **Blind.** |
| `S-25e′`/`S-25l′`/`S-25m′`/`S-25o` | accessor-return, digest-destination, count and occupant-digest rules. `leaked` is a bare `int` no rule tracks. **Blind.** |

**Every rule of `S-25a`..`S-25o` is satisfied, and `controller_pid` reaches a
second sink.** The construct is the X line's determination 2 with `_lease_path`
substituted for the inline claims literal — the same defect, on the record the
repair did not reach.

### 1.5 The precise textual overclaim

`PT-1` **corollary 2** (v2.2 :526-531) reads:

> "The four enumerated producers MS-3, MS-4, MS-5, MS-11 are then genuinely the
> only expressions in the five roots that yield a claim **or lease** mapping."

`PT-1`'s proof is a four-case exhaustion over path operands that can denote a
path **under the claims root**. It cannot, and does not, establish anything
about an expression that yields a *lease* mapping from a *lease* path. The
corollary asserts more than the theorem proves, and `D-8′` then rests `M-R4`'s
decidability on that corollary. This is the same shape of defect the X line
found in `D-8` at v2.1 — a decidability anchor whose premise is not established
by the locus it cites — displaced one record to the left.

Symmetrically, **`PT-1` corollary 1** ("Every byte string that is the canonical
serialization of a durable claim or occupant is produced by MS-2's read") is
true as written only because it says *claim or occupant*; `CR-1`'s class, which
corollary 1 is invoked to underwrite (`PA-P3`), is *claim **or lease*** bytes.
The premise supplied is narrower than the class it is supplied for.

### 1.6 Three further consequences of the same hole, each fail-closed

These are not leaks; they are places where the same asymmetry makes the
conforming implementation statically invalid, and they show the hole is
structural rather than an oversight in one rule.

```text
1a  NO DURABLE LEASE READ IS EXPRESSIBLE. MS-2's path operand is claim_path
    (PA-4, PA-7). There is no MS row for a lease read. So a lease reload —
    which v2 §2.6.1(e) names explicitly, and which C-3, "the claim/lease
    immutability check", needs — has no legal route in the five roots.
1b  NO LEASE INSTALL IS EXPRESSIBLE. MS-5 builds lease_mapping in a production
    root. M-R5 confines a governed mapping Name to §2.4's table; S-25j bars
    serialization outside MS-6; and CR-3's four carrier positions include
    MS-12, which is the CLAIM install. No position exists at which lease bytes
    may be written to the signed durable lease path.
1c  DC-6′ IS FALSIFIED BY A SIGNED REQUIREMENT, IF THE LEASE IS HANDLED IN THE
    FIVE ROOTS. DC-6′ states "NO OTHER digest, checksum, fingerprint ... of a
    claim, a LEASE, an occupant ... exists in the five roots", and C-5's
    amended FORBIDDEN clause bans "any digest evaluation other than EV-1 and
    EV-2 ... of a claim, a LEASE, an occupant". But contract :116-124 REQUIRES
    active_lease_sha256, "the hash of the exact pre-settlement lease", at every
    heartbeat. Either that computation is outside the five roots — in which
    case the packet should say so, because MS-5 puts lease construction inside
    them — or Repair B has replaced one false digest count with another.
```

I flag `1c` as **conditional**: it depends on where the settlement layer's lease
hashing lives, which this packet never states and which I cannot settle from the
committed bytes. Stating it is part of the repair.

### 1.7 Why this is a `REVISE` and not a `BLOCK`

The repair is an extension of the mechanism v2.2 already built, in its own
idiom, at the same decidability cost. It contradicts no signed contract, inverts
no authority, reopens no accepted closure, and needs no new architecture cell.
Exact text is at §7.

---

## Determination 2 — `PA-6` makes `MS-12`'s install a read call, so `PA-7` rejects the packet's own install site

`PA-6` defines the term used by `PA-5`, `PA-7` and `S-25n`:

> "a READ CALL is any Call whose func is, or whose func's attr is, one of:
> builtin `open`; `os.open`, `os.read`, …"

The definition is by **func name only**. It has no mode or flags qualifier —
deliberately, because the whole method is syntactic.

`MS-12` is `_install_claim(claim_path, carrier)`, "exactly one atomic
no-replace write of the carrier bytes under `T_RUNTIME.lock`". Every spelling of
an atomic no-replace write is `open(claim_path, "xb")` or
`os.open(claim_path, O_WRONLY|O_CREAT|O_EXCL)`; `pathlib.Path(...).write_bytes`
is both non-atomic and a `PA-2` violation (a `pathlib.Path` call outside a path
constructor with a non-Constant operand). So `MS-12` contains a Call whose func
is `open` or whose func's attr is `open` — **a read call under `PA-6`** — whose
path operand is `claim_path`, outside `MS-2`.

```text
PA-7 sentence 1  "A read call whose path operand is the Name claim_path occurs
                 ONLY inside _read_claim_bytes (MS-2)"        VIOLATED at MS-12
PA-7 sentence 2  "A read call whose path operand is a bare parameter Name of a
                 non-constructor function ... is a static violation"
                                                              VIOLATED at MS-12
PA-4(b)          affirmatively enumerates that very position as legal
```

`PA-4(b)` and `PA-7` contradict each other on the one required install site, and
`S-25n` — which is stated as `PA-1`..`PA-9` conjoined — therefore rejects the
conforming build. This fails **closed**, so it is not an escape; it is an
internal incoherence in the load-bearing rule of Repair A.

**A second, adjacent incoherence at the same locus.** `PA-4(a)` requires
`claim_path` to be "the path operand of the single read call inside `MS-2`",
while `PA-P4` carries `MS-2`'s v2.1 row text forward verbatim, and that row
names the function `_read_claim_bytes(path)` — parameter `path`. Under the row
text, `MS-2`'s read operand is the parameter Name `path`, which is precisely
what `PA-7` sentence 2 declares a static violation ("a bare parameter Name of a
non-constructor function"), and `PA-4(a)` is unsatisfied. Under the alternative
reading — the parameter is renamed `claim_path` — `PA-4`'s "EXACTLY THREE
positions and NOWHERE ELSE" is exceeded, because `claim_path` then also occurs
as `MS-1`'s Assign target and as the argument at each of the `MS-2`, `MS-11` and
`MS-12` call sites. **No implementation satisfies `PA-4` and `PA-7` as
written.** Repair text at §7.

---

## Determination 3 — `PA-5`/`PA-7`/`PA-3` make the signed exact-constant paths unspellable

`PA-5`: the path operand of every enumerated read call is "a PLAIN NAME. Never a
Constant …". `PA-7` sentence 2: that Name must be assigned in its own enclosing
function body **from a call to a path constructor**. `PA-3`: every path
constructor takes a dynamic stem and its **first statement** is a stem grammar
check; "A constructor without this first statement … is a static violation".

Against the signed composite:

```text
composite :2603  S-13  "no /proc/self/fd/ string literal is concatenated with a
                       non-constant expression; the descriptor paths are exact
                       constants"
composite :2612  S-18  "a /proc/self/fd enumeration appears only at the three
                       sites of §P1-6.5 with that site's permission"
composite :725-737     §P1-6.5 requires enumeration at P-f (PCS root), A-5 (role
                       root) and G-5 (grandchild)
composite :2718  inv 49 the enumeration happens at exactly those three sites
```

An enumeration is `os.listdir`/`os.scandir` — both enumerated read forms in
`PA-6` — over the exact constant `/proc/self/fd`. Under `PA-5` a Constant path
operand is a static violation; routing it through a Name requires a path
constructor (`PA-7`), and a path constructor requires a dynamic stem with a
grammar check (`PA-3`), which for `/proc/self/fd/` is what `S-13` forbids. The
same bind catches every durable path the chain fixes as an exact constant
(`T_STATE.json`, `T_LEDGER.md`, `T_LEDGER.md.head.json`, the two lock files):
they are expressible only by pushing a Constant stem through a constructor whose
grammar check has nothing to check.

This too fails closed. It also means `PC-R2`'s assurance — "No peer read site is
removed, relocated, or made to pass through `MS-2`" — and the `R-a`..`R-d`
retained-behaviour fixtures are **incomplete as evidence**: every retained
fixture is a constructor-built dynamic path, and none is a constant path or a
descriptor path. `B-A4(iii)` prices a reshaping cost; it does not disclose that
three signed enumeration sites and every constant durable path currently have no
conforming spelling. Repair text at §7.

---

## Determination 4 — `PA-7`'s new analysis kind: within `X M-2`, but `D-14` mislabels it

The closure's §6.1 asks whether `PA-7`'s intra-function single-assignment lookup
spends the no-taint/no-call-graph property. My answer, in two parts.

**Is it acceptable? Yes.** It is one pass, terminating, finite, and produces no
approximation: at a read call, take the operand Name, require exactly one
`Assign` to it in the enclosing body, require the RHS to be a path-constructor
call. There is no fixpoint, no transitive propagation, no may/must alias
lattice, and no soundness assumption about value flow. Nothing in `X M-2` is
spent. I also note that `PA-7` does **not** in fact depend on `S-4` for
uniqueness as `D-14` says it does: `PA-7` states the exactly-once requirement
itself, so it stays sound in the peer root regardless of `S-4`'s scope. That is
a strengthening, and it should be recorded rather than left as an inherited
citation.

**Is `D-14`'s description accurate? No — by one hop.** `D-14` says the lookup is
"a local index over one function's own statements. IT IS NOT interprocedural".
But the check is not "the RHS is a Call"; it is "the RHS is a Call **to a path
constructor of §2.4**", and deciding whether the callee is a path constructor
requires resolving the callee Name to its `FunctionDef` and testing that
definition against `PA-3`. That is a **one-hop, module-level, name-keyed
definition lookup** — still not a call graph (no transitivity, no edges beyond
depth 1), still not taint, still one pass — but it is not intra-function, and
the packet's own standard is that increments are disclosed in the words that
mean them rather than absorbed. `D-14` should say so. **Nonblocking**; correction
text at §7.

**Does unrelated filesystem access remain possible?** For dynamic
constructor-built peer paths, yes — `PC-R1`, `PC-R2` and `R-a`..`R-d` hold, and I
confirm the mechanism does not remove or relocate those read sites. For constant
paths and descriptor paths, no — see Determination 3. So the claim is true of
the fixtures the packet tests and false of a class it does not test.

---

## Determination 5 — the two `ACC-5` evaluations, the two destinations, the five continuations

**Exhaustive and non-overlapping for the claim and the occupant: CONFIRMED.**

| | `EV-1` | `EV-2` |
|---|---|---|
| operand | canonical bytes of the claim being installed, after `MS-10` | canonical bytes of the `EEXIST` occupant, after that occupant independently passes `MS-10`, `X-2`, `X-3` |
| overlap | none — the operands are the two distinct carriers of `CR-2`, and `EV-R3` preconditions each separately | |
| destinations | exactly `D-1`, `D-2` | none |
| consumer | the two signed durable fields | exactly the `X-4` boolean |
| confinement | `S-25l′`, `L-R2` | `OD-1`..`OD-4`, `S-25o` |

`EV-R1` + `S-25m′` make a third evaluation an arithmetic failure, and `S-25o` is
a genuine occurrence-and-position rule on one Name at one site, not a semantic
test. I could construct no route by which `EV-2`'s value escapes the conjunct
without firing `OD-1`..`OD-4`.

**Direct destinations, verified against the signed chain, not the closure:**

```text
D-1  contract :99-102   T_PROCESS_STARTED, "the non-state-bearing start event
                        carrying process_claim_sha256"                    LIVE
D-2  protocol :248-257  t-process-record.v1 carries process_claim_sha256 and
                        NEITHER identity key — re-read key by key           LIVE
```

**All five transitive continuations, verified at their cited loci:**

```text
L-1  contract :103-106  lease installed with prior_charge_event_sha256 seeded to
                        the T_PROCESS_STARTED entry hash                CONFIRMED
L-2  contract :116-124  heartbeat settlement's T_DEVICE_TIME_CHARGED carries
                        active_lease_sha256, a containing-object hash    CONFIRMED
L-3  contract :125-140  T_PROCESS_STOPPED carries process_record_sha256 "of that
                        record"; :163-173 the invalid-close route, same shape
                                                                        CONFIRMED
L-4  protocol :85-97    close archival set stages "that process claim and final
                        record, state, ledger, head"                    CONFIRMED
                        — and L-4's own plain statement that the archive stages
                        the CLAIM ITSELF, in cleartext, is correct and material
L-5  contract :125-140 + protocol :85-97   recovery re-reads and compares
                                                                        CONFIRMED
```

`L-0`'s direct/continuation distinction and `L-R1`'s one-question test are sound,
and `L-R2` keeps a third direct destination forbidden by two independent rules.
I searched for a sixth continuation in the governing chain and found none.

**One residual, carried from Determination 1.6(1c):** `DC-6′`'s inventory says no
other digest of "a claim, a **lease**, an occupant" exists in the five roots,
while `L-2` cites the signed `active_lease_sha256` as a permitted continuation.
`L-0` reconciles them only if the lease hash is computed outside the five roots
or is not a digest "of a lease" in `DC-6′`'s sense. The packet does not say
which. It must.

---

## Determination 6 — Repair C: every confidentiality claim withdrawn. CONFIRMED, closed.

I re-derived the arithmetic rather than accepting it. Given the other eighteen
canonical fields, `A-P4c` forces `attested_pgid == attested_pid` for the leader
case this contract installs, and `PID_MAX_LIMIT = 4194304` (`v2 §2.2`, `X m-2`),
so the candidate space is **at most 4,194,304 single values** and exhaustive
enumeration against the digest is practical. `CS-1`..`CS-4` state exactly that,
tagged `[IP]`, and `CS-3` is right that the constructing supervisor holds all
eighteen fields without reading anything, and `CS-4`/`L-4` right that the archive
reader holds the two integers in cleartext.

| Claim withdrawn | Where | Verified withdrawn, not restated |
|---|---|---|
| `C-5` "EXACTLY ONE SHA-256" | `R-W4`, §3.2 | ✅ |
| `DC-1` "there is never a second" | `R-W5`, `DC-1′` | ✅ |
| `DC-6` "NO SECOND DIGEST … the only value derived from a carrier" | `R-W6`, `DC-6′` | ✅ |
| `DC-3` "never process identity … never a name of anything addressable" | `R-W7`, `DC-3′` | ✅ |
| `DC-4` blanket "comparison"/"evidence" ban | `R-W7`, `DC-4′` | ✅ |
| `DC-5` unqualified "ONE-WAY" | `R-W7`, `DC-5′` | ✅ — retained only as the **name** of the `ACU` property, which is honest |
| `WL-4(a)` "obtainable only by reading the claim" | `R-W8`, `WL-4′(a)` | ✅ |

I grepped v1, v2 and v2.1 for every surviving instance of *one-way*, *preimage*,
*conceal*, *secret*, *confidential*. The only survivors are (i) v2.1 §3.4's
section **heading**, which `DC-5′` expressly retains as a name; (ii) v2.1 §8's
author self-disclosure, which already says the digest "does not conceal a
4-million-candidate secret" and is therefore consistent with the withdrawal;
(iii) v2's `R-L4`/§P1-13.0 "one-way **call direction**", which is about layer
call direction and is unrelated. `CS-7`'s governing sentence and `WL-3′`'s "no
sentence in v2, v2.1 or v2.2 may be read as asserting one" close the residue by
construction, and `STEP 13` records it so no future contract can cite this cell
for the stronger claim.

The full-claim commitment is described honestly: **searchable over at most
4,194,304 candidates**, **identity and equality information**, **not a
confidentiality boundary**. The Y line's §9.2/§9.3 are satisfied without
narrowing one item of the authorization boundary. Repair C needs no further
work.

---

## Determination 7 — no process-control or scientific use is authorized, and none is smuggled transitively. CONFIRMED.

`DC-4′` preserves the entire sink prohibition and extends it to "ANY VALUE
RECOVERED OR INFERRED FROM IT" via class member `(f)` — addressing, selection,
signalling, waiting, process-control primitives, request builders for the nine
opcodes, handle keys and comparisons, journal and retry keys, capacity, custody,
spend, settlement, qualification, blinding, Q/C, scientific datum, observation,
evidence, outcome, Proof. `CS-6`/`CS-7` state the digest confers no
process-control authority and is not an authorized PID selector. `WL-R1` grounds
the property in `S-25l′`, `S-25o` and `P-R5`'s dominant invalidity rather than in
an assumption about what an actor can compute — which is the correct footing.

I walked each transitive consumer looking for smuggling and found none:

```text
L-1  the lease seed is a hash OF the T_PROCESS_STARTED entry, not the raw
     digest; it authorizes reservation, not addressing
L-2  charge events and heartbeat settlements carry containing-entry hashes;
     no PID addressing follows, and DC-4′'s spend/settlement ban is not
     evaded because no field's value equals the raw digest (L-R1's test)
L-3  T_PROCESS_STOPPED carries a record hash, not the claim digest
L-4  archive composites are Git object/tree/commit hashes over the staged set
L-5  recovery "MAY consume D-2 or a containing hash for integrity", with the
     explicit sentence that NO RECOVERY RULE AUTHORIZES PID-BASED CONTROL
```

`WL-4′(b)` is verified against `composite :1942`/`:1952`: under A3 the supervisor
is same-UID and already holds kernel power over every process in this contract,
with "Kernel power is admitted; Officina authorization is not conferred". A
recovered pid therefore conveys zero operating-system capability the actor did
not already have, and `WL-4′(c)` is verified against the opcode grammar — no
request field of any of the nine opcodes accepts a pid.

`N-3` survives: observing a PID confers no authorized process control, and `C-5`
confers none.

---

## Determination 8 — counts and interfaces

| Quantity claimed | Recomputed | Status |
|---|---|---|
| verifier rules 15 | `S-25a`..`S-25o` = 15 letters; `S-25n`, `S-25o` are the two added | ✅ |
| tests 21 | `A-T1`..`A-T21`; `17 + 4` (`A-T18`..`A-T21`); `A-T9′` amends an assertion only | ✅ |
| consumers 5 / accessors 5 | `C-1`..`C-5`, `ACC-1`..`ACC-5` | ✅ |
| call sites 12 | `MS-1`..`MS-12`, unchanged | ✅ |
| evaluations 2 | `EV-1`, `EV-2` | ✅ |
| direct destinations 2 | `D-1`, `D-2` | ✅ |
| transitive continuations 5 | `L-1`..`L-5` | ✅ |
| handoff steps 13 | 1–4, 8–10 unchanged; 5/6/7 amended; 11 unchanged; 12, 13 new | ✅ |
| governed mapping Names 3 / carrier Names 3 | `M-R3`, `CR-2` | ✅ |
| variant fixtures | `V-a`..`V-q` = 17, each individually asserted at `A-T19` | ✅ |
| claim-path Names 1 / read functions 1 | `PA-4`, `PA-7` — **arithmetically consistent, but see Determination 2**: no implementation satisfies the position count as written | ⚠ |

The arithmetic is internally exact. Two interface observations: `S-25n`'s name
("claim path or claim read outside its anchored site") understates its actual
scope, which by `PA-2`/`PA-3`/`PA-5`/`PA-7` is *every* path constructor and
*every* read call in the five roots; and any repair under §7 re-derives the
`S-25m′` count line, which is the packet's own stated consequence of adding a
row.

---

## Determination 9 — no regression, and no authorization created. CONFIRMED.

I re-checked all eighteen loci §7.1/§7.2 assert untouched, against the v2 and
v2.1 bytes, rather than accepting the author's table.

```text
X M-1, X m-1, X m-3, Y-C2, Y-m1     not in the replacement index; verbatim
X m-2   PID_MAX_LIMIT = 4194304 unchanged; CS-2 cites the bound as the size of
        the search space and neither changes nor reopens the grammar or the
        over-range rejection
Y-M1    X-1..X-4 intact — X-4 is not removed, narrowed or renumbered; EV-2,
        OD-1..OD-4 and S-25o describe the digest X-4 already used; no matrix
        row, conjunct or routing changes
Y-M2    t-process-record.v1 re-read key by key at protocol :248-257: carries
        process_claim_sha256, carries NEITHER identity key; the two-superseded-
        schemas count stands
S-25i / S-25i-N1..N4, M-R1/M-R2, M-R3/M-R5/S-25j, CR-1..CR-4/S-25k,
MS-4..MS-12/MS-R1..MS-R4, ACC-4/ACC-5/ACC-R5, ACC-R1..ACC-R4, C-5 as a
record-level consumer, D-1/D-2, DC-2/DC-7, RC-1..RC-4, §3.5 model choice,
§3.6 destination search, NC-1..NC-3                          all unchanged
D-8′    withdraws only the READ-site reading of §P1-13.7; NC-2 rests on its
        INSTALL-site property, which I re-read at composite :2354-2371 and
        which is undisturbed
```

I re-verified `D-8′`'s two grounds directly: `§P1-13.7`'s sentence is "Every
interface operation is assigned to exactly one root and one function, so that no
two layers can **install** the same no-replace record", its table pins installs
and three **named** reads, invariant 84 (`:2753`) constrains the **P1 layer**,
invariant 88 (`:2757`) enforces one install site — and `MS-2` has two call sites
by design. The withdrawal is correct and correctly bounded. The composite's bytes
are **not** edited by this packet, as `STEP 12` states.

Finding the lease residual is **not** a reopening: `X M-2`/`Y-C1` were classed
"substantially closed — residual", the residual is exactly what Repairs A/B set
out to close, and I find the repair incomplete rather than a closed item broken.

**No authorization is created by v2.2.** §9's negative space is accurate: no
selection, no token, no implementation, no verifier or manifest edit, no code or
test artifact, no process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, no capability, capacity, custody, spend, datum, outcome, Proof or
claim movement. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`;
the watchdog-freeze cell remains unresolved and orthogonal. Option A remains
recommended and unselected; Option B remains non-selectable behind `B-1`/`B-2`.

---

## §7. The smallest exact repairs

Each is a replacement of packet text in the packet's own idiom. None invents an
implementation detail, none broadens the contract to records this packet does
not already claim (`RESTRICTED_PROCESS_IDENTITY (d)`, `CR-1`), and none touches a
signed byte.

### R-1 — close the lease half (Determination 1). **Required.**

The author must choose one of two bounded routes and say which. I recommend
(i); (ii) is admissible and smaller if the facts support it.

**(i) Pin the lease exactly as the claim is pinned.** Replace `PA-1`, and amend
`PA-4`, `PA-7`, `PA-9(d)` and `PT-1`, by substituting a two-member pinned family:

```text
PA-1′  REPLACES PA-1. THE IDENTITY-BEARING RECORD-ROOT LITERALS ARE PINNED.
       In the five production roots, a string or bytes Constant whose value
       contains the substring "T_PROCESS_CLAIMS" occurs EXACTLY ONCE, as the
       single Constant path-root operand inside _claim_path (MS-1); and a
       string or bytes Constant whose value contains the substring
       "T_ACTIVE_LEASES" occurs EXACTLY ONCE, as the single Constant path-root
       operand inside _lease_path (MS-1L). Any other occurrence of either
       substring, in any syntactic position, at any depth, in any of the five
       roots, is a static violation.

PA-4′  ... claim_path and lease_path are each ONE Name with ONE construction
       site (MS-1, MS-1L), each occurring only at the positions this rule
       enumerates for it.

PA-7′  ... A read call whose path operand is the Name claim_path OR the Name
       lease_path occurs ONLY inside _read_claim_bytes (MS-2). Every other read
       call ... other than MS-1 and MS-1L.

PA-9(d)′ ... FROM A CLAIM-PATH OR LEASE-PATH READ ...

PT-1′  ... the ONLY expressions that can denote a path under
       successor/officina/runtime/T_PROCESS_CLAIMS/ or under
       successor/officina/runtime/T_ACTIVE_LEASES/ are the Names claim_path and
       lease_path, and the only read of either is MS-2's. Corollary 2 then
       covers "a claim or lease mapping" as it claims to.
```

with the consequential minimum: `CR-2` gains a fourth carrier Name
`lease_bytes`; §2.4 gains `MS-1L` (the lease path constructor) and, if the
answer to `1c` is that the lease is installed in the five roots, one lease
install row with its `CR-3` position; `S-25m′`'s count line is re-derived
(13 or 14 call sites, 4 carrier Names, 2 pinned root literals).

**(ii) Or state and enforce that the lease is not handled in the five roots.**
If no durable lease read, lease install, or lease digest occurs in the five
production roots, say exactly that as a rule, reconcile it with `v2 §2.6.1(d)`
and `(e)`'s "lease reload after a restart", with `C-3`'s claim/lease immutability
check, with `MS-5`'s in-root lease construction, and with `CR-1`'s inclusion of
lease bytes — and scope `PT-1` corollary 2 to claims only, since it will then be
claiming nothing about leases.

Either route also resolves `1a`, `1b` and `1c`.

### R-2 — make `MS-12` and `MS-2` expressible (Determination 2). **Required.**

```text
PA-6, ADD AS ITS FINAL SENTENCE:
  THE SINGLE ATOMIC NO-REPLACE INSTALL CALL AT MS-12 IS A WRITE CALL AND NOT A
  READ CALL. It is the one Call in the five roots whose func is builtin open or
  os.open, whose path operand is claim_path, and which lies outside MS-2;
  PA-4(b) enumerates it, PA-5 and PA-7 do not apply to it, and it contains no
  .read() and binds no byte string.

PA-4, ADD AS A CLOSING NOTE:
  The three positions are counted as USES of the value. The MS-1 Assign target
  and the argument occurrences at the MS-2, MS-11 and MS-12 call sites are the
  same three uses named at (a), (b) and (c), not additional ones.

MS-2's ROW, AMENDED IN ONE WORD:
  the enumerated function is _read_claim_bytes(claim_path); its path parameter
  is named claim_path, so that PA-4(a) and PA-7 are satisfiable. Nothing else
  in the row changes.
```

### R-3 — restore constant and descriptor paths (Determination 3). **Required.**

```text
PA-5, AMENDED FIRST SENTENCE:
  ... is a PLAIN NAME, or a str/bytes Constant whose value contains neither
  pinned root substring. Never a concatenation or f-string, never a Call
  result, never a Subscript, never an Attribute, never a comprehension
  variable, never a starred or defaulted argument. A Constant operand is
  admissible precisely because PA-1′ makes a Constant that could denote an
  identity-bearing record root a static violation on sight, and because the
  signed chain fixes the descriptor paths of S-13 and the three /proc/self/fd
  enumerations of §P1-6.5 as exact constants.

PA-3, ADD:
  A path constructor with NO dynamic stem parameter has no grammar check and is
  well-formed; the first-statement requirement applies only to a constructor
  that takes a stem.

PA-7 sentence 2, ADD:
  ... or is a str/bytes Constant admitted by PA-5.

§2.7, ADD TWO RETAINED-BEHAVIOUR FIXTURES asserted to PASS:
  R-e  the three /proc/self/fd enumerations of §P1-6.5, over the exact constant
  R-f  a constant durable path read — T_STATE.json, the ledger, the head, a lock
```

### R-4 — label the analysis kind accurately (Determination 4). **Recommended, nonblocking.**

```text
D-14′  REPLACES D-14's characterization. PA-7's second sentence is the ONE new
       analysis kind in v2.2: a SINGLE-ASSIGNMENT LOOKUP IN THE ENCLOSING
       FUNCTION BODY, FOLLOWED BY A ONE-HOP LOOKUP OF THE CALLEE'S OWN
       DEFINITION to test it against PA-3. Both indices are built during the
       same AST walk. It is NOT a taint analysis, NOT a call graph (there is no
       transitivity and no edge beyond depth one), NOT a fixpoint, and it
       terminates in one pass. It is nevertheless MORE than the pure
       name/position matching of S-25a..S-25m, and more than an intra-function
       lookup, and it is disclosed as such. PA-7 does not rely on S-4: it states
       its own exactly-once requirement, so it is sound in the peer root
       whatever S-4's scope.
```

### R-5 — state where the lease digest lives (Determination 5). **Required, one sentence.**

```text
DC-6′, ADD:
  The signed active_lease_sha256 of contract :116-124 — the hash of the exact
  pre-settlement lease — is [inside | outside] the five production roots. If
  inside, it is a third named evaluation and DC-6′, C-5's FORBIDDEN clause,
  EV-R1 and S-25m′ are re-derived to admit it as an enumerated integrity
  evaluation with no persistent identity destination. If outside, that fact is
  stated, and DC-6′'s inventory is expressly scoped to the five roots.
```

### What is **not** required

Nothing in this review asks for: a wider taint analysis; an enumerated `PC-N`
table; a ban on the peer layer's `open`; a change to `S-25i`, `M-R1`..`M-R5`,
`CR-1`..`CR-4`, `MS-4`..`MS-12`, `ACC-*`, `RC-*`, `NC-*`, `D-1`/`D-2`, `L-1`..`L-5`,
`CS-1`..`CS-7` or any Repair C text; a change to the composite's bytes; or a
reopening of any of the eight findings both lines closed. `V-m`'s
externally-planted-symlink residual is correctly disclosed at §8 item 3 and I
accept it as a residual on `WL-4′(b)`'s grounds — it is a filesystem fact, not a
static property, and it conveys no capability an A3 same-UID actor lacks.

---

## §8. The author's disclosed weak points, classified

| # | Author weak point | Classification |
|---|---|---|
| 1 | `PA-7`'s new analysis kind | **Nonblocking, with one correction** — acceptable under `X M-2`; `D-14`'s "not interprocedural" is inaccurate by one hop (`R-4`) |
| 2 | `PC-N` closed by shape, not enumeration | **Nonblocking, and the right call** — enumerating the peer's durable set would be the `YV2-C1` error; the shape closure is sound for the paths it covers |
| 3 | `V-m` symlink indirection not closed | **Nonblocking** — correctly disclosed; no new exposure under A3 |
| 4 | `B-A4(iii)`'s cost to the peer root | **Nonblocking as priced, incomplete as stated** — Determination 3 shows the cost also lands on constant and descriptor paths, which the item does not name |
| 5 | Repair C makes the claim strictly weaker | **Nonblocking, correct, and the honest outcome** — `STEP 13` records it properly |
| 6 | `L-1`..`L-5` classify lineage other contracts own | **Nonblocking** — `L-R1`'s one-question test is the right instrument; all five verified at their loci |
| 7 | the five roots are a fixed list | **Nonblocking** — a sixth root re-derives every count and re-opens `PT-1`, as stated |
| 8 | the no-regression assertion is the author's | **Re-checked here and confirmed** — see Determination 9 |

**The blocking item is one the author did not disclose:** the repair pins the
claim and leaves the lease — the other durable record carrying the same two
restricted integers, named in this packet's own restricted class — entirely
unpinned, while `PT-1` corollary 2 asserts the lease is covered.

---

## Verdict and authorization

**`REVISE_OFFICINA_P1_IDENTITY_V2_2`.**

Repair C is fully and independently closed. Repair B is closed for the claim and
the occupant, with one sentence outstanding about the signed lease digest.
Repair A closes the X-line's determination-2 construct for the claims path and I
could break none of `PA-1`..`PA-9` there — but the identical construct reaches
`controller_pid` through the durable active lease, which is inside
`RESTRICTED_PROCESS_IDENTITY` by name, is the claim key set plus five by the
signed protocol, and is affirmatively asserted by `PC-R1` and fixture `R-d` to be
readable. Two further internal incoherences — `PA-6`/`PA-7` against `MS-12`, and
`PA-5`/`PA-3` against the signed exact-constant descriptor paths — make the
conforming implementation statically invalid at sites the signed chain requires.
All are closable by the bounded text at §7, at the same decidability cost and
with no new architecture cell. After that lands and a bounded X/Y round confirms
the repaired bytes, the identity author choice should be confirmable.

Because the verdict is `REVISE`, this round authorizes **nothing** — not Kirill's
identity author-choice token, not the A/B selection, not
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not implementation, not a
verifier or manifest edit, not a commit, not activation, not process execution,
not data, not an outcome. No existing file was modified in producing this review;
its sole product is this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT AUTHORIZED (REVISE)
OPTION A = RECOMMENDED, UNSELECTED
OPTION B = NON-SELECTABLE
```
