OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION

# Independent bounded X-line confirmation — Officina P1 process-claim identity choice v2.4

**Reviewer:** Claude Code, engineering X line, model **Claude Opus 4.8** (an
acceptable substitute for Fable 5 under the mandate's own condition). Read-only;
SHA-256 recomputed on committed bytes; no file modified but this one deliverable;
no code, probe, process-control operation, activation, spend, entropy, datum,
trajectory, comparison, outcome, Proof or programme movement.

**Independence, stated first because the mandate makes it load-bearing.**
I did **not** author v2.3 or v2.4. The v2.3 correction, the v2.3 closure, the
v2.3 X-line review, and the v2.4 correction and closure were all produced by
**Claude Code Opus 5** (the v2.3 X review self-disclosing that it ran in the
same session that authored v2.3). This confirmation is a separate invocation of
a different model (Opus 4.8) in a separate session, with no authorship of either
the v2.3 or the v2.4 bytes. The two-line discipline's independence condition —
unmet for the X line on v2.3 by the author's own admission (v2.3 X review lines
9-20; v2.4 closure §7) — **is met here.** I treated the v2.4 author closure as
untrusted and re-derived every claim below against the signed bytes.

**Verdict: `OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`.**

On the v2.4 bytes the packet is **both CLOSED and SATISFIABLE.** I could
construct no AST in the five production roots that reaches `controller_pid` or
`process_group_id` from `T_PROCESS_CLAIMS` or `T_ACTIVE_LEASES` while satisfying
`S-25a`..`S-25p` — including through any of the four forms the scoping repairs
newly admit (a `dir_fd`-anchored open, a descriptor-operand read, an ordinary
`PC-N` write call, or the single permitted `chdir`). And every one of the four
signed operations the v2.3 X line found unspellable now has at least one
conforming spelling, each because a rule was **scoped**, not because an exception
was granted. The single residual (`PA-6″(6)` vs protocol §B) is disclosed by the
author, does not render any signed operation unspellable on these bytes, and
carries a pre-stated repair that itself introduces no escape (§B below).

---

## 0. Custody — recomputed on committed bytes

Both mandate bytes recompute exactly:

```text
bef7012a5fce59857372755c23f6da87d1d1045f7d62d8945914cb60d9c48fda  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md   [MATCH]
5ac5fbc31faa565d44729bf814726e97e491fcfa5acf70ffa55fd4373eddf4f3  reviews/opus5_officina_p1_process_claim_identity_choice_v2_4_closure.md                [MATCH]
```

The bytes v2.4 repairs and the two verdicts it answers recompute to the values
v2.4 §1.1 pins:

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/…PACKET_V2_3_CORRECTION.md                              [MATCH]
55e19217502c7f217f3ec1768f4db122abd14d4ef22c315d76fde38dac790633  reviews/opus5_…v2_3_closure.md                                    [MATCH]
710d828d46a9bbb7f0cf7068c3f3f1667f83a4f22002693f5f8de48f9f321bf2  reviews/opus_officina_p1_identity_v2_3_final_x_confirmation.md    [MATCH]  REVISE
f17adb9c439aa5c261bc159d505f4fda6fe73039830f90a08f6ddf900fe92a0f  reviews/sol_officina_p1_identity_v2_3_final_y_confirmation.md     [MATCH]  YLINE_CONFIRMED
```

The governing signed chain recomputes to v2.4 §1.3:

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md               [MATCH]
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md  [MATCH]
```

The v2.4 correction and this file are **untracked** — new this round and absent
from `HEAD`, the expected state for a correction that modifies nothing. Every
other file read was verified byte-identical to its `HEAD` blob. The chain
v1→v2→v2.1→v2.2→v2.3→v2.4 is acyclic and each link is byte-identifiable. The
committed composite `V1_2` (`2c857fa8…`) is the governing operative document; the
untracked `V1_3`/`V1_4` composites present in the tree are **not** in the signed
chain and were not relied on.

**I recompute custody independently and state explicitly: I authored neither
v2.3 nor v2.4.**

---

## 1. The bounded question

> Did v2.4 make the closed identity rules satisfiable without reopening an escape?

**Yes.** The four v2.3 X-line blocking findings (`B-1`..`B-4`) are each the same
drafting error — a clause written to protect **two pinned pathname families**
stated as a rule over **all filesystem operations in all five roots** — and v2.4
repairs each by scoping, adopting the v2.3 X line's `R-1`..`R-7` in full with one
declared, necessary deviation. Below, each of the seven mandated tests is
re-derived against the signed bytes, not against the author's assertions.

---

## Test 1 — `PA-6″(5)`: exactly the signed `chdir` is admitted; no second/dynamic chdir, fchdir, link or symlink becomes legal

**Signed fact, verified.** Composite `V1_2` §P1-7.2 (region `:815-825`):
`P-cwd. _chdir("/")` with its own `CHDIR_FAILED` token, "before any name is
opened", followed by `:822`'s general dir_fd rule and `:824`'s "the inherited
working directory affects nothing". `_chdir` is a bound primitive.

**Rule, tested.** `PA-6″(5)` admits `os.chdir` **exactly once** in the five
roots, at `P-cwd`, in `scripts/officina_process_control_bootstrap.py`, with the
single `str` Constant `"/"`, lexically before every path-operand read call and
write call in that root; "Any other chdir, a chdir with a non-Constant or
non-`"/"` operand, or a chdir at any other position or in any other root, is a
static violation. `os.fchdir`, `os.symlink` and `os.link` appear in NO production
root."

- Recognition is an occurrence count + root match + node-order (position) check +
  one Constant test. This is the same node-order discipline `S-25p`/`PA-3′`
  already use. **No flow, no new analysis kind.**
- A **second** chdir → occurrence count 2 → violation. A **dynamic** operand
  (Name/expr, not the `"/"` Constant) → violation. A chdir in
  `generic_harness.py` or a role root → root mismatch → violation (`N-a`, `N-b`).
- `fchdir`/`symlink`/`link` remain banned **outright** — the repair widens
  nothing here.
- **No escape:** `chdir` neither opens nor names a restricted record; it only
  sets cwd. The anti-redirect property is supplied by `PA-6″(6)`'s `dir_fd`
  discipline and `PA-5″`'s prohibition of relative reads except through signed
  anchors — not by banning `chdir`. A single `chdir("/")` cannot make a pinned
  record namable.

**PASS.** The signed operation is spellable; no dynamic or duplicate chdir, and
no fchdir/symlink/link, becomes legal.

---

## Test 2 — `PA-6″(6)`: signed `dir_fd=6` constants and the approved descriptor Name are admitted on `PC-N`; pinned operands cannot use `dir_fd`; unanchored constants/expressions/Names are rejected — and the protocol `:58-72` question

**Signed facts, verified.** Composite `:822` states dir_fd-relative access as the
**general** rule. The four package-root opens use an **int literal**:
`:905` `dir_fd = 6`, `:911` `dir_fd = 6`, `:916` `dir_fd = 6`, `:917-918`
`dir_fd = 6`. The lock open `:1051-1052` uses a **Name**:
`dir_fd = T_PCB_FD_RUNTIME_ROOT`. (A role-root open at `:1011` similarly resolves
under the held Name `T_ROLE_FD_PKGROOT`.) Descriptors 5 and 6 are `S_ISDIR`
(`:848-849`, P-f).

**Rule, tested.** `PA-6″(6)` forbids `dir_fd` on any read/write whose path operand
is `claim_path` or `lease_path`; elsewhere it admits (a) an `int` Constant that is
a signed anchor slot (fd 5 or fd 6) **or** (b) a plain Name assigned once from a
signed anchor or a protocol §B held descriptor; every other value — Call,
Subscript, Attribute, arithmetic, unbound parameter — is a static violation.

- The signed `int` `6` is admitted by (a); `T_PCB_FD_RUNTIME_ROOT` and
  `T_ROLE_FD_PKGROOT` by (b). **The declared R-2 deviation is not merely
  acceptable — it is necessary:** the v2.3 X line's `R-2` said the anchor "must be
  a plain Name", and the signed sites at `:905/911/916/918` are the int literal
  `6`. A Name-only rule would re-break exactly what it repairs. `PA-6″(6)(a)`
  admitting the int Constant is the correct reading of the signed bytes, and the
  closure discloses the deviation plainly (§2.2, `R-2`).
- **Unanchored forms rejected:** an int Constant other than 5/6 fails (a) and is
  not a Name → violation (`N-d`); a Name bound from a non-anchor fails (b); any
  expression fails outright.
- **No escape via the int-Constant deviation:** fd 5/6 are the **package roots**,
  not the runtime records directory. `open("…/T_PROCESS_CLAIMS/x.json", dir_fd=6)`
  requires a path Constant containing the pinned substring → `PA-1′` static
  violation on sight; `claim_path` as operand → forbidden by `PA-6″(6)`'s first
  sentence; a multi-level relative Constant → `PA-3′(a)`'s one-stem grammar
  refuses `/` and `..`. No `dir_fd` route reaches a restricted record.

**The protocol `:58-72` sub-question — decided.** Protocol §B (`:59-71`) requires
the held-file-descriptor **`samestat`** discipline: the runtime directory, ledger,
head, state cache, process claim, active lease and process record are validated by
holding an anchor descriptor and requiring a freshly-opened descriptor's
`(st_dev, st_ino)` to equal it ("Pathname hashes or recyclable inode tuples alone
are insufficient"), the whole transaction under `T_RUNTIME.lock`
(`flock LOCK_EX`). This is an **identity-validation** requirement on the *resulting
descriptor*; it does **not** textually require that the claim/lease *open itself
carry a `dir_fd` keyword*. An `O_NOFOLLOW` open by the pinned Name, followed by
`os.fstat` of the descriptor and a `samestat` comparison against the held anchor —
exactly what `PG-2`/`PG-3` already require — satisfies §B **without** `dir_fd` on
the pinned operand. The held descriptors are the samestat *reference*, not a
mandatory `openat` base for the file open. **Therefore protocol `:58-72` does not
require anchored claim/lease opens in a way that conflicts with `PA-6″(6)`, and no
signed operation is thereby rendered unspellable.**

**PASS.** The residual the author discloses at §10.1 — that a *future
implementation* review might decide the claim/lease opens must be `openat`-relative
— is real but is (i) not forced by the signed bytes as written, and (ii) covered
by a pre-stated one-line repair (permit `dir_fd` on the pinned families only when
its value is a signed anchor under (a)/(b), forbidding every other value). That
repair **does not reopen an escape**: `PA-1′`, `PA-4′` and `PA-7″(i)` continue to
pin the path, the Name-use set and the single read site regardless of the open's
base, and the `PG` gate still fires on content. See §B.

---

## Test 3 — the 24 path-operand and 9 descriptor-operand forms are exhaustive, disjoint and correctly classified; laundering/aliasing/helper/default/closure/one-hop attacks fail without taint

**Counts, re-enumerated independently.**
- Path-operand (`PA-6″(1)`): `open` (1) + `os.open, os.stat, os.lstat, os.statvfs,
  os.readlink, os.listdir, os.scandir, os.walk, os.fwalk` (9) + `pathlib .open,
  .read_bytes, .read_text, .iterdir, .glob, .rglob, .stat, .lstat, .readlink` (9)
  + `io.open, io.FileIO, codecs.open, fileinput.input, linecache.getline` (5) =
  **24**.
- Descriptor-operand (`PA-6″(2)`): `os.read, os.pread, os.preadv, os.readv,
  os.fstat, os.sendfile, os.copy_file_range` (7) + `mmap.mmap, shutil.copyfileobj`
  (2) = **9**.
- `24 + 9 = 33`, the same forms v2.3 enumerated: the split repartitions, adding
  and removing none.

**Disjoint and correctly classified.** No func appears in both lists. The
diagnostic pairs are right: `os.stat`/`os.lstat` (path) vs `os.fstat`
(descriptor); `os.open` (path) vs `os.read` (descriptor). `os.sendfile` and
`os.copy_file_range` take descriptors → correctly in (2). `mmap.mmap` and
`shutil.copyfileobj` are judgement calls (author §10.3), both take a
descriptor/file-object and both are unimportable under every current allowlist
(`G-9`); the placement in (2) is defensible and inert today.

**Adversarial descriptor attacks, each defeated by `PA-7″(iv)` without taint.**
`PA-7″(iv)` requires a descriptor operand to be either (a) a Name assigned exactly
once, in its own enclosing function body, from a **path-operand read call that
itself satisfies `PA-5″`/`PA-7″(i)-(iii)`**, or (b) an `int` Constant signed slot
or a Name bound once from the signed binding block / slot table.

- **Laundering** (descriptor from a parameter, `Subscript`, `Attribute`, `Call`
  result, arithmetic): none is (a) or (b) → static violation (`N-e`).
- **Aliasing** (`fd2 = fd1`): `fd2` is assigned from a Name, not from a
  path-operand read call → not (a); not a Constant/binding-block Name → not (b) →
  violation.
- **Helper / default / closure returns**: a descriptor received from an arbitrary
  helper `Call` is not "assigned from a path-operand read call" → not (a); a
  defaulted-parameter or free-variable descriptor is not a single intra-body
  assignment from such a call → violation.
- **Non-conforming source** (descriptor from an open that itself failed
  `PA-5″`/`PA-7″`): (a) requires the source open be conforming → violation
  (`N-f`).
- **One-hop path bypass**: `PA-7″(iii)` admits a path Name bound once from a path
  constructor other than `MS-1`/`MS-1L`, but a pinned path cannot be manufactured
  — any pinned-substring Constant is a `PA-1′` violation at any depth, and
  `PA-3′(a)`'s one-stem grammar refuses `/`/`..`, so no one-hop helper builds a
  second path level to a restricted record.

**Closure argument, checked and sound.** Every descriptor traces back exactly one
hop to a path-checked open (recognition: the *same* intra-function
single-assignment lookup `D-14′` already prices, applied to a descriptor Name).
The only path-operand read of a pinned family is `MS-2` (`PA-7″(i)`/`(ii)`), so a
**pinned-record descriptor exists only inside `MS-2`**, where `PA-8` already
confines the bytes. The `PA-7″(iv)(b)` slot descriptors are the signed fds 3-8
(pipes, package dirs, source files per `:848-857`, `:1006-1008`) — none names a
restricted record. **No descriptor-operand read yields identity bytes outside
`MS-2`.** No taint, transitivity, fixpoint or call graph is introduced (`D-11″`,
`D-15″`).

**PASS.**

---

## Test 4 — every signed operation in the 18-row table has a conforming spelling

I verified the load-bearing rows against the signed bytes, then checked each row
names an admitting clause that actually admits it.

| Signed op | Locus verified | Admitting clause — checked |
|---|---|---|
| PCS preflight `_chdir("/")` | composite `:821` | `PA-6″(5)` — one chdir, PCS root, Constant `"/"`, first ✔ |
| `p-1`,`p-4`,`p-6`,`p-7` `dir_fd=6` | `:905`,`:911`,`:916`,`:917-918` | `PA-6″(6)(a)` int anchor + `PA-5″(b)` path Constants ✔ |
| `c1` `SPAWN.lock` open | `:1051-1052` | `_O_RDWR` readable ⇒ **read** call `PA-6″(3)`; `PA-5″(b)` admits `"SPAWN.lock"`; `PA-6″(6)(b)` admits the Name ✔ |
| `P-h` read fd 3; `L-4` read reply pipe | `:901`, `:784` | `PA-7″(iv)(b)` signed slot descriptors ✔ |
| `P-f` fstat 3-8; `A-5`..`A-11` fstat | `:848-857`, `:1006-1021` | `PA-7″(iv)(b)` — `os.fstat` descriptor-operand on signed slots ✔ |
| `MS-2` open + whole-content read; `PG-3` fstat conjuncts | v2.3 §2.4; `PG-2`/`PG-3` | `PA-5″(a)`, `PA-7″(i)`, `PA-7″(iv)(a)` — **the `B-3` self-refutation, closed** ✔ |
| claim install `MS-12`; lease install `MS-13` | v2.3 §2.4 | `PA-6″(3)` — the two pinned-operand writes ✔ |
| spawn-intent / supervisor-identity / freeze installs | composite §P1-13.7 `:2361-2367` | `PA-6″(3)` — ordinary `PC-N` writes, uncounted ✔ |
| ledger, head, state cache, process record, locks | protocol `:66-71`, `:80-84` | `PA-6″(3)` ordinary writes ✔ |
| three `/proc/self/fd` enumerations | `S-18`, §P1-6.5 | `PA-5″(b)` exact Constant; `PG-1` excludes enumerations ✔ |
| constant durable paths | protocol `:80-84` | `PA-5″(b)`, `PA-3′(b)` ✔ |
| every other `PC-N` peer read | `PC-R1′`, `PC-R2′` | `PA-5″`, `PA-7″(iii)`, plus the `PG` gate ✔ |

Every row has a conforming spelling and a clause that admits it. The four
formerly-unspellable operations (`B-1`..`B-4`) are the first, second, fourth and
seventh–ninth rows and are all now spellable. **PASS.**

---

## Test 5 — the two-write statement is scoped only to pinned operands and does not forbid ordinary signed installs; write safety is imperative

`PA-6″(3)` counts **exactly two write calls whose path operand is a pinned path
Name** (`MS-12`/`claim_path`, `MS-13`/`lease_path`) and states that "EVERY OTHER
DURABLE INSTALL THE SIGNED CHAIN REQUIRES IS AN ORDINARY `PC-N` WRITE CALL AND IS
NOT RESTRICTED BY THIS RULE", enumerating the spawn-intent, supervisor-identity
and freeze installs (composite §P1-13.7, verified `:2361-2367` — four installs to
`generic_harness.py`) and the ledger/head/state/record/locks (protocol §B,
verified `:66-71`, `:80-84`). The false v2.3 sentence "exactly two write calls
exist in the five roots" is withdrawn (`R-W18`). The scoped count therefore does
**not** forbid the ordinary signed installs — closing `B-4` — while a **third**
pinned-operand write is still a violation (`N-h`, `PA-4′`).

`PA-6″(4)` is imperative: "A write call SHALL contain no read expression and SHALL
bind no byte string … IS A STATIC VIOLATION", converting v2.3's descriptive
property into a checked clause (v2.3 X Determination 3 / `R-5`). **PASS.**

---

## Test 6 — `PG-4′` permits only its literal `schema` discrimination read before gate completion, with no other value binding

`PG-4′` carries every clause of `PG-4` verbatim and adds one: the discriminator
"reads exactly the key `"schema"` by literal subscript, binds no other value,
yields a boolean, and is THE ONLY READ OF THE CONTENT PERMITTED BEFORE THE GATE
COMPLETES. … No other key, no slice, no iteration and no second subscript is
permitted before the gate completes." This reconciles the tension the v2.3 X line
flagged (Determination 6 / `R-7`) between "before any parse" and "the
discriminator reads one key", **without** widening what is read: exactly one
literal-subscript read, boolean result, no value binding, and `PG-5` still routes
record-first before any mapping/value binding. The ordinary parse `PG-4′`/`PG-5`
order against is unchanged. No identity field is bound before the gate. **PASS.**

---

## Test 7 — recompute the counts and confirm no regression of the Y-confirmed boundary

| Quantity | Value | Check |
|---|---|---|
| behavioural tests | **27** | `26 + 1`; `A-T27` new, `A-T26′` replaces `A-T26` ✔ |
| retained-behaviour fixtures | **10** | `6 + 4` (`R-a`..`R-f` + `R-g`..`R-j`) ✔ |
| enumerated read forms | **33** | `24 + 9` partition, same forms (Test 3) ✔ |
| centralized accessors | **5** | `ACC-1`..`ACC-5` unchanged ✔ |
| governed-mapping producers | **5** | `MS-3,4,5,11,14`, **disjoint** from accessors (`ACC-2/3=MS-8/9`, `ACC-4/5=MS-6/7`, `ACC-1` wire) — no shared member; the two fives are asserted separately so a sixth of either fails by arithmetic (`R-6`) ✔ |
| persistent consumers | **6** | unchanged ✔ |
| `ACC-5` evaluations | **3** | `EV-1`,`EV-2`,`EV-3` unchanged ✔ |
| direct destinations of the claim lineage digest | **2** | `D-1`,`D-2` unchanged ✔ |
| transitive continuations | **5** | `L-1`..`L-5` unchanged ✔ |
| declassifying operations | **1** | unchanged ✔ |
| digest values | **2 persistent / 1 transient** | unchanged ✔ |
| verifier rules | **16** | `S-25a`..`S-25p`; `S-25m‴`,`S-25n″` replace, none added ✔ |
| write calls (pinned-operand) | **2** | `MS-12`,`MS-13` (Test 5) ✔ |
| chdir / `dir_fd` (pinned) | **1 / 0** | one at `P-cwd`; zero on pinned operands ✔ |

**No regression of the Y-confirmed surface.** The Y line
(`f17adb…`) confirmed `PT-1′` and its corollaries, `CA-0`..`CA-5`, the gate order
`PG-1`..`PG-7` and its four planted cases, the conditional information boundary
(≤4,194,304 candidates; no unconditional confidentiality/recoverability claim),
`EV-3`/`C-6` and the authorized-use boundary, `D-1`/`D-2`, `L-0`..`L-5`, the
prior closures, the terminal routes, the recommendation and the negative
authorization. v2.4's replacement index touches **none** of these except `PG-4′`,
which *adds* the one-key clause the Y line's own §3 already observed the
discriminator necessarily performs, and changes no other clause. The four planted
alias cases (symlink / hard-link `st_nlink==1` / copied-bytes / `/proc/self/fd`)
are unaffected. **No confirmed sentence is amended; the alias and information
boundaries carry to these bytes.**

---

## A. Adversarial closure search over the four newly-admitted forms

I attempted to reach `controller_pid` / `process_group_id` from either restricted
record through each form the scoping newly permits, requiring `S-25a`..`S-25p`:

1. **The single `chdir`** — `chdir("/")` only; no relative pinned open follows
   (Constant with pinned substring → `PA-1′`; `claim_path` operand → `PA-6″(6)`;
   multi-level stem → `PA-3′(a)`). No reach.
2. **A `dir_fd`-anchored open** — anchors are fd 5/6 (package roots) or held
   descriptors; a pinned path operand forbids `dir_fd`; a Constant reaching the
   claim trips `PA-1′`. No reach.
3. **A descriptor-operand read** — every descriptor traces one hop to a
   path-checked open; a pinned descriptor lives only in `MS-2` (`PA-8`-bounded);
   slot descriptors name pipes/dirs/sources, not records. No reach.
4. **An ordinary `PC-N` write call** — writes bind no bytes and contain no read
   (`PA-6″(4)`); an installed record carries the actor's own values, not a
   restricted record's. No reach.

In every case the widened form remains inside `PA-1′`'s two substring pins,
`PA-4′`'s two Name-use sets, `PA-7″(i)`'s single read function at three call
sites, `CR-3′`'s five carrier positions and `PG-1`..`PG-7`'s gate — none of which
v2.4 touches. **No escaping AST exists; the scoping widened only what a conforming
implementation may spell.**

## B. The one residual, weighed

`PA-6″(6)` prohibits `dir_fd` on the pinned operands, while protocol §B holds the
runtime **directory** in its descriptor set (author §10.1). I find this
**non-blocking on these bytes**: §B mandates `samestat` identity validation of the
*resulting* descriptor, which an `O_NOFOLLOW` open by the pinned Name plus
`fstat`/`samestat` against a held anchor satisfies **without** `dir_fd` on the
pinned operand (Test 2). Should a later implementation review nonetheless require
`openat`-relative claim/lease opens, the author's pre-stated one-line repair —
permit `dir_fd` on the pinned families only when its value is a signed anchor,
forbidding every other value — preserves closure, because the path, the Name-use
set and the read site stay pinned regardless of the open's base. **The residual
neither renders a signed operation unspellable now nor, under its stated repair,
reopens an escape.** It is disclosed, bounded and does not block confirmation.

Secondary disclosed items (author §10.2-§10.4) are all fail-closed: the deferral
to the signed slot table (`PA-7″(iv)(b)`) makes an out-of-table descriptor a
static violation; the readable-mode table's omissions keep a call inside
`PA-5″`/`PA-7″`; `mmap`/`shutil` placements are inert under current allowlists.
None affects the closure or satisfiability verdict.

---

## Verdict and authorization

**`OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`.**

On the exact v2.4 bytes (`bef7012a…`), by an X line that authored neither v2.3 nor
v2.4: the packet is **CLOSED** — no AST reaches either identity field from either
restricted record while satisfying `S-25a`..`S-25p`, including through the four
newly-admitted forms — and **SATISFIABLE** — every signed operation the chain
requires has at least one conforming spelling, each by a scoped rule rather than a
granted exception. `B-1`..`B-4` are repaired by adopting `R-1`..`R-7` in full,
with `R-2`'s single deviation (an int-Constant anchor as well as a Name) both
declared and *required* by the signed `dir_fd = 6` sites. The counts re-derive
(`24+9=33`, `26+1=27`, `6+4=10`, `S-25a`..`S-25p` = 16, the two disjoint fives),
and no sentence of the Y-confirmed surface is amended.

This confirmation, **together with** the standing bounded Y-line no-regression
check requested by the v2.4 closure §5, authorizes only **Kirill's identity
author-choice token** `I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY`. It
does **not** sign or mint that token, and authorizes nothing else — not
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not the A/B selection,
implementation, a verifier or manifest edit, a commit, activation, process
control, resource use, entropy, data, a trajectory, comparison, outcome, Proof or
programme-claim movement. No existing file was modified in producing this review;
its sole product is this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT MADE, NOT AUTHORIZED (author-choice token now unblocked on the X side)
OPTION A = RECOMMENDED, UNSELECTED
OPTION B = NON-SELECTABLE
X-LINE INDEPENDENCE = SATISFIED ON THESE BYTES (Opus 4.8; authored neither v2.3 nor v2.4)
```
