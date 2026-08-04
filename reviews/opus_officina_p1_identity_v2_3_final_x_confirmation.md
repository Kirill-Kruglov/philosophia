REVISE_OFFICINA_P1_IDENTITY_V2_3

# Bounded final X-line confirmation — P1 process-claim identity choice v2.3

**Reviewer:** Claude Code Opus, engineering X line. Read-only; SHA-256 only; no
file modified but this one deliverable; no code, probe, process-control
operation, activation, spend, entropy, data, trajectory or programme movement.

**Independence defect, stated first because it bears on how this review should be
weighed.** The v2.3 correction and its closure were authored in the immediately
preceding turn of **this same session**. This chain's discipline is that the X
and Y lines are independent of the author, and on these bytes that condition is
**not met for the X line**. I have therefore audited adversarially against my own
text and reported what I found: **four blocking satisfiability defects, three of
which this session introduced or propagated, and one false assertion in my own
v2.2 X-line review that I must now correct.** That outcome is evidence the audit
was not a rubber stamp, but it is not a substitute for independence. **My
recommendation to the author-principal is that a genuinely independent X line
re-run this confirmation on the repaired bytes**, and that this review be treated
as an author-side pre-check that happens to carry an X-line verdict token.

**Verdict: `REVISE_OFFICINA_P1_IDENTITY_V2_3`.**

v2.3 is **closed**: I could construct no AST in the five production roots that
reaches `controller_pid` or `process_group_id` from either
`T_PROCESS_CLAIMS` or `T_ACTIVE_LEASES` while satisfying `S-25a`..`S-25p`. The
lease is genuinely pinned, the `EV-3` audit is sound on the signed bytes, the
`PG` gate contains the alias consequence the Y line demanded, and the arithmetic
is exact but for one omission.

v2.3 is **not satisfiable**. Four required signed operations have **no conforming
spelling**, each because a `PA-6′`/`PA-5′`/`PA-7′` clause that was written for
*pathname* reads of *two pinned families* is stated as a rule over *all
filesystem operations in all five roots*:

```text
B-1  PA-6′ bans os.chdir in every production root. The signed PCS preflight's
     FIRST STEP is P-cwd, "_chdir("/")" (composite :820).
B-2  PA-6′ bans the dir_fd keyword on every read and write call. The signed
     composite states as a GENERAL RULE that "Every later filesystem operation
     is dir_fd-relative to fd 5 or fd 6" (:822) and uses it at five enumerated
     call sites (:905, :911, :916, :917-918, :1052).
B-3  PA-5′/PA-7′ require every enumerated read form's first operand to be a
     PATH. Seven of the enumerated forms take a DESCRIPTOR — including os.read
     and os.fstat, which v2.3's own MS-2 shape and PG-3 conjuncts REQUIRE. The
     central repair of v2.3 is self-refuting, and the signed descriptor reads
     P-h (:901) and L-4 (:784) are static violations.
B-4  PA-6′ asserts "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS". §P1-13.7
     assigns FOUR durable installs to generic_harness.py alone, and protocol §B
     adds the ledger, head and state. The count is false on the signed chain.
```

None is a leak; all four fail closed. All four are repairable by scoping clauses
that are already scoped correctly elsewhere in the same packet, with exact text
at §7, introducing no taint analysis, no new analysis kind, and no new author
choice. This is a revision, not a block.

---

## 0. Custody

**Reviewed bytes, recomputed, matching the mandate:**

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md   [MATCH]
55e19217502c7f217f3ec1768f4db122abd14d4ef22c315d76fde38dac790633  reviews/opus5_officina_p1_process_claim_identity_choice_v2_3_closure.md              [MATCH]
```

Both files are **untracked** — new this round and absent from `HEAD`, which is
the expected state for a correction that modifies nothing. Every other file below
was verified byte-identical to its `HEAD` blob before being read.

**The chain and the two verdicts v2.3 answers:**

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/…PACKET_V2_2_CORRECTION.md
e2ad45b7d3dd84d2537d19e52302a729ac390dae2a2fd6b169b4a84d15eca242  reviews/opus_officina_p1_identity_v2_2_final_x_confirmation.md   REVISE
e82a6974d413b830b5913ddaaa788571aac56705ddaa0f3a9843f50c5b43abc1  reviews/sol_officina_p1_identity_v2_2_final_y_confirmation.md    REVISE
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/…PACKET_V2_1_CORRECTION.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/…PACKET_V2_DRAFT.md
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/…PACKET_V1_DRAFT.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
```

**Governing signed chain, recomputed — all six match v2.3 §1.3:**

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

---

## Determination 1 — is v2.3 CLOSED? **Yes. No escaping AST found.**

I attacked both pinned families with every route the mandate names and with the
routes the previous three rounds established. Each is listed with the rule that
fires, on the v2.3 bytes.

| Attack | Result |
|---|---|
| the v2.1 claim construct (inline literal → `open` → `json.loads` → `.values()[5]`) | `PA-1′(a)`, `PA-2`, `PA-7′(iii)`, `PA-9′` — unchanged from v2.2, still four-fold |
| the v2.2 **lease** construct through `_lease_path` | `PA-1′(b)` (second pinned Constant) or `PA-4′` (second `MS-1L` call), `PA-7′(ii)`, `PA-9′` — **the v2.2 blocking finding is closed** |
| alias `q = claim_path` / `q = lease_path` | `PA-4′` — an `Assign` RHS is not an enumerated use of either Name |
| second construction at a new site | `PA-4′` — `MS-1`/`MS-1L` each called once |
| helper return, and helper return + parse | `PA-7′(iii)` (bare parameter Name of a function other than `MS-2`) and `PA-9′(a)` |
| **one-hop callee abuse** — declare a fake "path constructor" returning a pinned path | `PA-1′` — its root Constant would contain a pinned substring; and `PA-3′(a)`'s stem grammar refuses `/`, `..`, leading `.`, so no stem reaches a second path level |
| **bytes paths** — `b"…T_ACTIVE_LEASES…"` | `PA-1′` is explicitly "a string **or bytes** Constant". Closed |
| **constant paths** — `open("successor/officina/runtime/T_PROCESS_CLAIMS/x.json")` | `PA-1′`, and `PA-5′(b)` admits a Constant only if it contains **neither** pinned substring. The admission and the pin are a matched pair, as `A-T26(f)` asserts |
| **runtime-supplied stem** — `_runtime_path(kind)` with `kind` read from config, `kind == "T_PROCESS_CLAIMS"` | reaches the **directory** only. `PA-3′(a)`'s one-stem rule and its `/` refusal block the second path level, so no record file is namable; `os.listdir` of it yields `process_id`s, which are not restricted |
| `dir_fd`/`openat`-relative reach into a pinned directory | banned outright by `PA-6′` (**over-banned — see B-2**) |
| descriptor reads of a live pinned fd via `/proc/self/fd/<N>` | admitted by `PA-5′(b)`, then refused by `PG-4`/`PG-5`. This is exactly the division of labour Y §5.2 asked for |
| **symlink** at a `PC-N` path | `PG-2` no-follow **by flag**, `PG-3(a)` regular file → `PG-5` dominant invalidity |
| **hard link** at a `PC-N` path | `PG-3(b)` `st_nlink == 1`. v2.3 correctly states that `samestat` cannot catch this because a hard link is the same inode, and `A-T25(b)` asserts that a `samestat`-only check would have passed |
| **copied claim bytes** at a `PC-N` path, single-link regular file | `PG-3` passes, `PG-4`'s **path-bound** discriminator refuses, `PG-5` routes before any binding. This is the one case only a content gate can reach, and it is reached |
| **lease reload** | `MS-14`, pinned; a fourth `MS-2` call site fails `PA-7′(i)`'s count |
| **lease install** | `MS-13` with `CR-3′(e)`; a carrier written anywhere else fails `CR-3′` |
| attacker-planted values under an *ordinary* schema at a `PC-N` path | not an escape: the integers are the attacker's own, not a restricted record's. Worth one sentence in the packet, not a rule |

**Determination 1 is met.** I found no AST reaching either identity field from
either record while satisfying `S-25a`..`S-25p`. The domain hole the v2.2 X line
found is closed, and the provenance hole the v2.2 Y line found is contained
rather than denied.

---

## Determination 2 — is v2.3 SATISFIABLE? **No. Four signed operations have no conforming spelling.**

### B-1 — `os.chdir` is banned, and the signed PCS preflight's first step is a `chdir`

`PA-6′` carries v2.2's sentence forward verbatim:

> "os.chdir, os.fchdir, os.symlink and os.link appear in no production root"

Against the composite:

```text
composite :819-820   P-cwd. _chdir("/")                OSError ⇒ CHDIR_FAILED
composite :815-817   "§P1-7.2 The PCS preflight ... Executed after the six
                     imports, the binding block and §P1-3.5's identity check,
                     and before any name is opened."
composite :410       _chdir is a BOUND PRIMITIVE of the PCS root
```

`scripts/officina_process_control_bootstrap.py` is production root #4. `P-cwd` is
mandatory, is the **first** preflight step, and has its own failure token. Under
`PA-6′`/`S-25n′` the conforming PCS is statically rejected at its first
filesystem statement.

**I must correct my own v2.2 review here.** At its Determination 1 I disposed of
fixture `V-l` with "`os.chdir` appears in no production root", accepted that
clause as true, and carried it into v2.3. **It was false on the signed bytes at
v2.2 and it is false now.** The clause is also unnecessary: `P-cwd` chdirs to
`"/"` exactly once, before any name is opened, precisely so that "the inherited
working directory affects nothing" (`:821-824`). The anti-redirect property comes
from `:822`'s dir_fd discipline, not from banning `chdir`.

### B-2 — the blanket `dir_fd` ban contradicts the signed general rule

`PA-6′`:

> "NO READ CALL AND NO WRITE CALL IN THE FIVE ROOTS PASSES A dir_fd KEYWORD"

Against the composite:

```text
:822        "Every later filesystem operation is dir_fd-relative to fd 5 or
             fd 6, or acts on an already-open descriptor, or is an absolute
             /proc name"                          <-- A GENERAL SIGNED RULE
:905        p-1. _open("scripts/officina_process_control_bootstrap.py",
                       _O_RDONLY|_O_NOFOLLOW|_O_CLOEXEC, dir_fd = 6)
:911        p-4. _open("src/philosophia/officina/generic_harness.py", …,
                       dir_fd = 6)
:916        p-6. _open("scripts/officina_role_bootstrap.py", …, dir_fd = 6)
:917-918    p-7. _open("src", _O_RDONLY|_O_DIRECTORY|_O_CLOEXEC, dir_fd = 6)
:1052       c1.  _open("SPAWN.lock", _O_RDWR|_O_CREAT|_O_CLOEXEC, 0o600,
                       dir_fd = T_PCB_FD_RUNTIME_ROOT)
```

Five signed call sites and one general rule. `P-p` is mandatory — "Only after
every step above may `c1` acquire `SPAWN.lock`" (`:920`).

Worse, the ban contradicts **v2.3's own gate**. `PG-3(c)`/`PG-3(d)` import
protocol §B's held-descriptor discipline, and §B's list opens with **"The runtime
directory**, ledger, external head, state cache, process claim, active lease, and
process record"* (`protocol :67-69`). A held *directory* descriptor exists in
order to be resolved against. `PA-6′` bans the mechanism `PG-3` imports.

The intent behind the ban — no read is resolved against a redirected base — is
correct and is preserved by scoping it to the pinned families and by requiring a
`PC-N` read's `dir_fd` to be one of the signed anchor descriptors. Repair at §7.

### B-3 — seven enumerated "read call" forms take a descriptor, not a path, and `MS-2`/`PG-3` require two of them

`PA-5′`: "the **path operand** of every enumerated read call form (`PA-6′`) is
EITHER (a) a PLAIN NAME, or (b) a str/bytes Constant …". `PA-7′(iii)`: that Name
must be "assigned exactly once, in its own enclosing function body, from a call
to a path constructor".

`PA-6′` enumerates, among the read forms: `os.read`, `os.pread`, `os.preadv`,
`os.readv`, `os.sendfile`, `os.copy_file_range`, `mmap.mmap`, and — **added in
v2.3** — `os.fstat`. Every one of these takes a **file descriptor** as its first
operand. A descriptor Name is assigned from an `open`, which is **not** a path
constructor, so `PA-7′(iii)` makes each a static violation; and a literal
descriptor number is an `int` Constant, which `PA-5′(b)` does not admit (it
admits only str/bytes Constants).

The consequences are not hypothetical, and two of them are self-inflicted:

```text
(i)   MS-2's OWN MANDATED SHAPE. v2.3 §2.4 requires "exactly one os.open …
      exactly one fstat of that descriptor … exactly one whole-content read".
      The fstat and the read are descriptor-operand forms. MS-2 IS A STATIC
      VIOLATION OF PA-5′/PA-7′ AS WRITTEN.
(ii)  PG-3'S OWN CONJUNCTS. PG-3(a)/(c) are fstat checks on the held
      descriptor. THE GATE VIOLATES THE RULES IT IS CONJOINED WITH.
(iii) composite :901  P-h. "read descriptor 3 to EOF"          — signed
(iv)  composite :784  L-4. "read the reply pipe to EOF"        — signed
(v)   composite :848-849, :1006-1020  the P-f and A-5..A-11 fstat sequences
      — signed, and the very discipline PG-3 claims to import
```

This is the same defect class the v2.2 X line found at `PA-6`/`MS-12` — a
call-form enumeration written for one operand kind and applied to another —
reproduced one level down. v2.3 fixed it for write-mode opens and did not
generalize the lesson.

### B-4 — "exactly two write calls" is false against four signed peer installs

`PA-6′`: "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS: the atomic no-replace
claim install at `MS-12`, and the durable lease write at `MS-13`."

Against the signed chain:

```text
composite §P1-13.7 assigns to src/philosophia/officina/generic_harness.py:
    write the spawn-intent record          install, no-replace
    write the process claim                install  (this cell's MS-12)
    install the supervisor identity record install, no-replace
    write a freeze observation             install, no-replace
protocol :58-72 / contract :190-200 add the ledger append, the external head,
    the state cache and the T_RUNTIME.lock creation (:1052 shows the lock open
    is itself a create-mode open)
```

At least six write-mode opens exist in the peer root alone. A creation cannot be
spelled with a read-mode open, so there is no evasion; the count is simply
false, and because `S-25n′` conjoins `PA-1′`..`PA-9′`, it rejects every
conforming build.

The correct count is the **scoped** one, which is what the rule was for: exactly
two write calls have a **pinned path Name** as their path operand.

### Everything else in Determination 2 passes

| Required signed operation | Conforming spelling exists? |
|---|---|
| the claim install `MS-12` | **yes**, once B-4 is scoped — `PA-6′`'s write-call definition itself is correct and total |
| the lease install `MS-13` | **yes**, same |
| the three `MS-2` reads (claim verify, `MS-11`, `MS-14`) | **only after B-2 and B-3**; the shape is otherwise expressible, with `claim_bytes = _read(fd, st_size)` a single `Assign` satisfying `PA-8`'s one-binding rule |
| the three evaluations `EV-1`/`EV-2`/`EV-3` | **yes** — one accessor, three call sites, `CR-3′(b)` |
| the three `/proc/self/fd` enumerations (`S-18`, `§P1-6.5`) | **yes** — `PA-5′(b)` admits the exact constant and `PG-1` excludes enumerations from the gate. `R-e` asserts it |
| ordinary constant durable paths (`T_STATE.json`, ledger, head, locks) | **yes** — `PA-5′(b)` and `PA-3′(b)`. `R-f` asserts it |
| every `PC-N` peer read | **yes for spelling**; **no for `P-p`/`c1` until B-2** |
| the `PCS` preflight `P-cwd` | **no, until B-1** |

---

## Determination 3 — is the read/write split syntactically total and non-misclassifying? **Total and safe; one drafting weakness.**

`PA-6′` defines a write call as a Call to `open`/`os.open` whose mode-or-flags
operand is a Constant, or a `BinOp Or` over Constants, denoting creation or
writing **without read access**. I checked totality and misclassification in both
directions:

```text
open(p)                 no mode operand           ⇒ read call   (default "r")
open(p, "rb")           Constant, readable        ⇒ read call
open(p, "xb"/"wb"/"ab") Constant, not readable    ⇒ write call
open(p, "r+b"/"w+b")    Constant, readable        ⇒ read call   — so a
                        write-mode-looking open that can read is NEVER
                        classified as a write, and PA-7′ still applies to it
os.open(p, O_WRONLY|O_CREAT|O_EXCL)   BinOp Or of Constants     ⇒ write call
os.open(p, O_RDWR|O_CREAT)            readable                  ⇒ read call
os.open(p, flags)       flags a Name, not a Constant            ⇒ read call
                        ⇒ PA-7′ applies ⇒ fail-closed
```

The classification is a fixed table over `Constant` nodes: decidable, one pass,
no flow. **It cannot misclassify a readable open as a write**, which is the only
direction that could leak, because every readable mode keeps the call inside
`PA-5′`/`PA-7′`. `composite :1052`'s `_O_RDWR|_O_CREAT` lock open confirms the
split behaves correctly on real signed code: it is a read call, its Constant path
operand `"SPAWN.lock"` is admitted, and only its `dir_fd` (B-2) fails.

**Drafting weakness, nonblocking.** `PA-6′` states the write call's safety
properties — "it contains no read expression, and it binds no byte string" —
inside a *definition* rather than as a checked clause. A verifier author could
read them as descriptive. Nothing leaks even under that reading, because a
non-readable descriptor cannot yield content at run time, but the sentence should
be imperative. Repair at §7 `R-5`.

---

## Determination 4 — the `EV-3` audit, re-derived independently. **CONFIRMED, with a stronger citation than the packet leads on.**

| Step | v2.3's citation | My re-derivation |
|---|---|---|
| what computes it | `contract :116-124`, `batch :93-97` | **confirmed**: "`active_lease_sha256` is the hash of the **exact pre-settlement lease**"; batch: "SHA-256 of the durable pre-settlement lease" |
| which file | `contract :576` (implementation-surface row) **and** `:517-522` | **confirmed, but the weight should shift.** `:576` sits in "§11. Cursor implementation handoff", an ownership table whose normativity is arguable. `:517-522` is not arguable: `generic_harness.py`'s `__main__` **is** the CLI, its subcommands are named and include **`heartbeat`**, and "**No additional `scripts/*.py` entry point is introduced**". The heartbeat computes `active_lease_sha256`; the heartbeat is in that file; no other entry point may exist |
| is it a production root | `contract :505-514`, `composite :349-357` | **confirmed under both**, third in each tuple |

**`active_lease_sha256` is evaluated inside the governed surface.** The audit
holds, and it holds on `:517-522` alone, so it does not depend on the disputable
normativity of a handoff table. v2.3 §9 item 3 already tells a reviewer to check
the audit rather than the conclusion; the conclusion survives the check, and the
load-bearing citation should be re-ordered.

**Exactly one new consumer, and no identity destination.** `C-6` is the only
addition: `ACC-R5` forbids any Subscript, slice, decode, split, regex, loop,
comprehension, format or branch over the operand, so `EV-3` binds no identity
field and routes no integer anywhere. **`D-1` and `D-2` are untouched** — I
re-verified at `protocol :241-246` that the lease key set is the claim's twenty
plus five and contains **no** `process_claim_sha256`, so the lease is not a third
carrier of the claim lineage digest (`LD-1`). **`L-1`..`L-5` are untouched** —
they enumerate objects *containing* the claim digest, and the lease contains none
(`LD-2`). `EV-3`'s destinations are correctly classified rather than enumerated
(`LD-3`), which keeps the packet out of the peer's record set.

One honest note, correctly handled by the packet: `EV-3`'s value is a persistent
commitment to a record that *does* contain both integers, so it inherits the same
conditional channel. `CS-8` states this, tagged `[IP]`, and extends every sink
ban to it via `S-25l″` and class member `(f)`. That is the right treatment.

---

## Determination 5 — arithmetic, and the accessor/producer terminology

I enumerated rather than accepted each label.

| Claim | Enumeration | Status |
|---|---|---|
| 6 persistent consumers | `C-1` claim constructor, `C-2` lease constructor, `C-3` claim/lease immutability, `C-4` freeze-evidence predicate, `C-5` claim lineage digest, `C-6` lease integrity digest | ✅ |
| 5 accessors | `ACC-1`..`ACC-5` = `MS-?`, `MS-8`, `MS-9`, `MS-6`, `MS-7` | ✅ |
| 5 governed-mapping producers | `MS-3`, `MS-4`, `MS-5`, `MS-11`, `MS-14` | ✅ |
| 16 verifier rules | `S-25a`..`S-25p` | ✅ |
| 26 tests | `A-T1`..`A-T26`; `21 + 5` | ✅ |
| 5 carriers | `canonical_bytes`, `claim_bytes`, `occupant_bytes`, `lease_canonical_bytes`, `lease_bytes` | ✅ |
| 15 call-site rows | `MS-1`, `MS-1L`, `MS-2`..`MS-14` = `1 + 1 + 13` | ✅ |
| 3 evaluations | `EV-1`, `EV-2`, `EV-3` | ✅ |
| 2 direct destinations | `D-1`, `D-2` | ✅ |
| 5 continuations | `L-1`..`L-5` | ✅ |
| 15 handoff steps | 1–13 + `STEP 14`, `STEP 15` | ✅ |
| 2 write calls | **false as stated** — see B-4; true when scoped to pinned operands | ❌ |

**The terminology mismatch the mandate asked me to resolve is real and is not
cosmetic.** Two disjoint sets each have five members: the **accessor
definitions** `ACC-1`..`ACC-5`, and the **governed-mapping producer sites**
`MS-3`, `MS-4`, `MS-5`, `MS-11`, `MS-14`. They share no member — `ACC-2`/`ACC-3`
are `MS-8`/`MS-9`, `ACC-4`/`ACC-5` are `MS-6`/`MS-7`, none of which produces a
governed mapping. The coincidence invites exactly the confusion the count rule
exists to prevent, and **`S-25m″` asserts the accessor count but omits the
producer count entirely**, so a sixth producer would be added without failing any
arithmetic — the precise failure mode `S-25m″` was written to prevent. `M-R4′`
carries the list but is not a count. Repair at §7 `R-6`; **nonblocking**, because
a sixth producer would still have to bind a governed Name and would fail `M-R4′`
by enumeration.

---

## Determination 6 — `PG-1`..`PG-7`/`S-25p` as a contract. **Sound, with its residual correctly disclosed.**

The division of labour is the right one and is stated honestly:

```text
STATIC, and S-25p enforces it   presence, ORDER and failure-successor of the
                                gate statements inside one function body; no
                                bypass, cache, fallback branch or early binding
RUNTIME, and v2.3 §9 item 2     whether the predicate is CORRECT
                                disclosed as a real weakening of the all-static
                                property, not described as if decided
TESTED, A-T25                   the four alias cases as runtime dispositions
```

I checked the one property that matters most — **no route may parse or bind
before the gate** — clause by clause. `PG-4` requires the discriminator "BEFORE
the bytes are parsed into a mapping that any ordinary consumer may touch, before
they are returned from the reading function, and before any value of the parsed
object is bound to a Name". `PG-5` routes record-first "BEFORE any mapping is
bound, any value is read, any comparison is made and any consumer sees it".
`PG-6` closes the obvious evasions: no bypass flag, no cached result, no trusted
path list, no retry proceeding on failure, no branch binding content before the
gate completes. `S-25p` makes the ordering a node-order check inside one function
body — the same discipline `PA-3′` already uses for the stem grammar check, and
no new analysis kind.

Two observations, neither blocking:

1. `PG-4` necessarily reads one key (`schema`) before the record is validated at
   `MS-10`. That is a parse — of one key, by literal subscript, binding nothing
   else. The packet should say so explicitly, because "before the bytes are
   parsed" and "the discriminator reads the single key" are in tension on a
   literal reading. Repair `R-7`.
2. The gate's guarantee is about **restricted content**, not about all content.
   An actor who plants a record under an *ordinary* schema at an ordinary path
   supplies only values the actor already knows. That is not a leak, and one
   sentence in the packet would forestall a future reviewer re-deriving it.

---

## Determination 7 — prior cells, recommendation, negative authorization. **CONFIRMED unchanged.**

I re-checked each against the v2, v2.1 and v2.2 bytes rather than accepting §8's
table.

```text
X M-1, X m-1, X m-3, Y-C2, Y-m1     not in the replacement index; verbatim
X m-2   PID_MAX_LIMIT = 4194304 unchanged; cited only as the size of a
        CONDITIONAL search space, which is the Y line's own repair
Y-M1    X-1..X-4 intact; CR-3′(d) is unchanged text; no matrix row, conjunct or
        routing changes
Y-M2    re-read protocol :248-257 — the final record carries
        process_claim_sha256 and NEITHER identity key
EV-1, EV-2, OD-1..OD-4, S-25o       unchanged; EV-R4 states disjointness
D-1, D-2                            still exactly two
L-0..L-5, L-R1, L-R2                unchanged
ACC-1..ACC-5, ACC-R1..ACC-R5, RC-1..RC-4, NC-1..NC-3, P-R1..P-R5   unchanged
DC-2, DC-3′, DC-4′, DC-5′, DC-7, WL-1, WL-2, WL-4′, WL-R1          unchanged
CS-1..CS-3, CS-5..CS-7, IP/ACU, class member (f)                   unchanged
§3.5 model choice, §3.6 destination search                         unchanged
S-25i/i-N1..N4, M-R1, M-R2, M-R3, M-R5, S-25j + scope note         unchanged
CR-1, CR-4, S-25k                                                  unchanged
```

`CS-4′`/`WL-3″` correctly replace the two absolutes the Y line refused, and
`CS-4′(c)` makes **no** claim in either direction for a reader lacking the
conditioning fields — which is the honest position and is weaker than v2.2's, as
it should be. Every sink prohibition is verbatim.

**The recommendation is unchanged**: Option A recommended and **unselected**;
Option B non-selectable behind `B-1`/`B-2`. **Negative authorization is intact**:
v2.3 §10 and closure §9 disclaim implementation, activation, entropy, capacity,
custody, spend, datum, trajectory, comparison, outcome, Proof and claim movement,
and state that Kirill's selection remains unauthorized pending both
confirmations. `N-10` adds an explicit no-scientific-cell statement. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`; the watchdog-freeze cell
remains orthogonal and unresolved.

---

## §7. The smallest exact repairs

All are scoping corrections to clauses the same packet already scopes correctly
elsewhere. None introduces taint analysis, a fixpoint, a transitive call graph, a
new analysis kind, a new authority, or an author choice.

### `R-1` — withdraw the `chdir` ban and replace it with the signed fact (B-1)

```text
PA-6″, REPLACING PA-6′'s final paragraph, first sentence:
  os.fchdir, os.symlink and os.link appear in no production root. os.chdir
  occurs EXACTLY ONCE in the five roots, at the PCS preflight step P-cwd
  (composite :819-824), with the single str Constant "/" as its operand, before
  any name is opened. Any other chdir, or a chdir with a non-Constant operand,
  is a static violation.
  RECOGNITION: occurrence count, position, and one Constant test.
```

### `R-2` — scope the `dir_fd` ban to the pinned families and anchor it (B-2)

```text
PA-6″, REPLACING PA-6′'s dir_fd sentence:
  NO READ CALL AND NO WRITE CALL WHOSE PATH OPERAND IS claim_path OR lease_path
  PASSES A dir_fd KEYWORD. Every other read or write call may pass dir_fd, and
  where it does, the keyword's value is a plain Name bound from one of the
  signed anchor descriptors — the composite's fd 5 or fd 6 (:822), or a runtime
  root descriptor of protocol §B's held-descriptor set — and never from an
  expression. THIS IS THE SIGNED DISCIPLINE (composite :822: "Every later
  filesystem operation is dir_fd-relative to fd 5 or fd 6"), NOT AN EXCEPTION
  TO IT, and PG-3(c)'s held-descriptor identity check depends on it.
  RECOGNITION: name match at the keyword, plus the same single-assignment
  lookup PA-7′ already performs. No new analysis kind.
```

### `R-3` — split the read forms by operand kind (B-3)

```text
PA-6″, REPLACING PA-6′'s single enumeration:
  A PATH-OPERAND READ CALL is any Call whose func is, or whose func's attr is:
    builtin open; os.open, os.stat, os.lstat, os.statvfs, os.readlink,
    os.listdir, os.scandir, os.walk, os.fwalk;
    pathlib .open, .read_bytes, .read_text, .iterdir, .glob, .rglob, .stat,
    .lstat, .readlink;
    io.open; io.FileIO; codecs.open; fileinput.input; linecache.getline
  A DESCRIPTOR-OPERAND READ CALL is any Call whose func is, or whose func's
  attr is:
    os.read, os.pread, os.preadv, os.readv, os.fstat, os.sendfile,
    os.copy_file_range; mmap.mmap; shutil.copyfileobj
  PA-5′ and PA-7′ apply to PATH-OPERAND read calls ONLY.
  A DESCRIPTOR-OPERAND read call's first operand is a plain Name assigned
  EXACTLY ONCE, in its own enclosing function body, from a PATH-OPERAND read
  call that itself satisfies PA-5′ and PA-7′ — or, for the reply and request
  descriptors of the signed protocol path (composite :784, :901) and the
  enumerated slot descriptors of §P1-6.5, from the signed binding block. A
  descriptor operand with no such binding is a static violation.
  RECOGNITION: the SAME intra-function single-assignment lookup PA-7′ already
  performs, applied to a descriptor Name instead of a path Name. NO NEW
  ANALYSIS KIND, NO TAINT, NO TRANSITIVITY.
```

This is what makes `MS-2`'s mandated shape and `PG-3`'s conjuncts legal, and it
preserves the closure: a descriptor can only come from an open that was itself
path-checked.

### `R-4` — scope the write-call count (B-4)

```text
PA-6″, REPLACING "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS":
  EXACTLY TWO WRITE CALLS IN THE FIVE ROOTS HAVE A PINNED PATH NAME AS THEIR
  PATH OPERAND: the atomic no-replace claim install at MS-12 (claim_path) and
  the durable lease write at MS-13 (lease_path). Every other durable install
  the signed chain requires — the spawn-intent record, the supervisor identity
  record, the freeze observation, the ledger, the head, the state cache and the
  locks (composite §P1-13.7; protocol :58-72) — is a write call over a PC-N
  path and is NOT restricted by this rule, only by PA-2, PA-3′ and PA-5′.
```

### `R-5` — make `PA-6′`'s write-call safety properties imperative (Determination 3)

```text
PA-6″, ADD:
  A write call SHALL contain no read expression and SHALL bind no byte string;
  a write call that does either is a static violation.
```

### `R-6` — close the producer count in `S-25m″` (Determination 5)

```text
S-25m″, ADD to the enumerated numbers:
  ... exactly FIVE governed-mapping producer sites (M-R4′: MS-3, MS-4, MS-5,
  MS-11, MS-14) — which is a DIFFERENT set of five from the five accessor
  definitions, sharing no member with it ...
```

### `R-7` — reconcile `PG-4`'s one-key read with "before any parse" (Determination 6)

```text
PG-4, ADD:
  The discriminator's own one-key read is not the parse this rule orders
  against: it reads exactly the key "schema" by literal subscript, binds no
  other value, returns a boolean, and is the ONLY read of the content permitted
  before the gate completes.
```

### What is **not** required

No change to `PA-1′`, `PA-2`, `PA-3′`, `PA-4′`, `PA-8`, `PA-9′`, `PT-1′`,
`CA-1`..`CA-5`, `PG-1`..`PG-3`, `PG-5`..`PG-7`, `S-25p`, `MS-1L`, `MS-13`,
`MS-14`, `CR-2′`/`CR-3′`, `M-R4′`, `EV-3`, `C-6`, `LD-1`..`LD-3`, `CS-4′`,
`WL-3″`, `CS-8`, or any Repair C, D-domain or count text beyond `R-6`. No
enumeration of the peer record set. No new durable schema, production root,
destination, invalidity cause or authority cell. No taint engine, no fixpoint, no
unrestricted interprocedural analysis. No new author choice.

---

## §8. The author's disclosed weak points, classified

| # | Weak point | Classification |
|---|---|---|
| 1 | the gate's cost, and `st_nlink == 1` being new to the live tier | **Nonblocking, correctly priced at `B-A8`.** The conjunct is necessary: `CA-2` shows `samestat` is structurally blind to a hard link |
| 2 | `PG-4` is a runtime predicate; `S-25p` enforces placement only | **Nonblocking, correctly disclosed.** The all-static property is genuinely weakened and the packet says so in those words |
| 3 | `EV-3`/`C-6` rest on the audit | **Nonblocking, and the audit survives re-derivation** — on `:517-522`, which is stronger than the `:576` row the packet leads with |
| 4 | five carriers, not the four `R-1` named | **Nonblocking and correct.** The fifth is forced by `MS-13`'s write position, exactly as stated |
| 5 | five `MS` functions renamed descriptively | **Nonblocking.** `MS-R6` pins shape, operand count, result kind and single definition |
| 6 | `CS-4′(c)` leaves the digest-only reader open | **Nonblocking and right.** The Y line proved the universal was unearned |
| 7 | `M-R4′` leans on the gate for non-pinned pathnames | **Nonblocking, and stated in the open** — which is precisely what v2.2 failed to do |
| 8 | everything rests on exactly five roots | **Nonblocking**, and now also true of the `EV-3` audit |
| 9 | the no-regression assertion is the author's | **Re-checked here; confirmed** |

**The four blocking items are ones the author did not disclose**, and three of the
four (`B-2`, `B-3`, `B-4`) arise from clauses this session either wrote or
propagated. `B-1` is a clause I affirmatively certified as sound in my own v2.2
review; that certification was wrong.

---

## Verdict and authorization

**`REVISE_OFFICINA_P1_IDENTITY_V2_3`.**

v2.3 closes both blocking findings of the v2.2 round. The lease is pinned with
the same instruments as the claim and I could construct no AST that reaches
either identity field from either record while satisfying `S-25a`..`S-25p`;
`PT-1′` is narrowed to the pathname theorem it proves; the content-alias class is
named honestly and its governance consequence is contained before any parse or
binding; `EV-3` is located on the signed bytes and carries exactly one new
consumer with no identity destination and no addition to `D-1`/`D-2` or
`L-1`..`L-5`; the information statement is conditional everywhere; every prior
accepted cell, the recommendation and the negative authorization are intact; and
the arithmetic is exact but for one omitted count.

It is returned for revision because four operations the signed chain **requires**
have no conforming spelling under `PA-5′`/`PA-6′`/`PA-7′` as written — the PCS
preflight's `chdir`, the composite's general `dir_fd`-relative filesystem
discipline, every descriptor-operand read including the two that `MS-2` and
`PG-3` themselves mandate, and every durable install beyond the two pinned ones.
Each is closed by the scoping text at §7, all of which the packet already applies
correctly to its pinned families.

Because the verdict is `REVISE`, this round authorizes **nothing** — not Kirill's
identity author-choice token, not the A/B selection, not
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not implementation, not a
verifier or manifest edit, not a commit, not activation, not process control, not
resource use, not entropy, not data, not a trajectory, not an outcome. No
existing file was modified in producing this review; its sole product is this
file.

**And separately from the verdict:** the independence condition for the X line
was not met on these bytes, because this session authored them. The
author-principal should obtain an independent X line on the repaired bytes before
treating any future `CONFIRMED` token from this line as satisfying the chain's
two-line discipline.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT AUTHORIZED (REVISE)
X-LINE INDEPENDENCE = NOT SATISFIED ON THESE BYTES
```
