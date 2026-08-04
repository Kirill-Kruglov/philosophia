READY_FOR_OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_AND_BOUNDED_Y_CONFIRMATION

# Author closure — P1 process-claim identity choice v2.4

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This closure is an untrusted author
self-assessment and must be treated as such.** The verdict token states only that
the correction is, in the author's judgement, **ready to be reviewed** — and,
this round, that it is ready to be reviewed **by an agent that did not author it**
(§7).

**Deliverables of this round, and nothing else:**

```text
successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md   NEW
reviews/opus5_officina_p1_process_claim_identity_choice_v2_4_closure.md                NEW  (this file)
```

**No existing file was modified.** No code was written, no process executed, no
resource spent, no entropy drawn, no trajectory produced, `T` was not activated,
and the programme claim was not moved.

---

## §1. Custody

### §1.1 This round's product

```text
bef7012a5fce59857372755c23f6da87d1d1045f7d62d8945914cb60d9c48fda  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md
```

This closure's own digest is not embedded and is to be recomputed by each
confirmation line on the committed bytes.

### §1.2 The bytes v2.4 repairs, and the two verdicts it answers

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/…PACKET_V2_3_CORRECTION.md
55e19217502c7f217f3ec1768f4db122abd14d4ef22c315d76fde38dac790633  reviews/opus5_officina_p1_process_claim_identity_choice_v2_3_closure.md
710d828d46a9bbb7f0cf7068c3f3f1667f83a4f22002693f5f8de48f9f321bf2  reviews/opus_officina_p1_identity_v2_3_final_x_confirmation.md   REVISE_OFFICINA_P1_IDENTITY_V2_3
f17adb9c439aa5c261bc159d505f4fda6fe73039830f90a08f6ddf900fe92a0f  reviews/sol_officina_p1_identity_v2_3_final_y_confirmation.md    OFFICINA_P1_IDENTITY_V2_3_YLINE_CONFIRMED_FOR_AUTHOR_SELECTION
```

Both v2.3 lines independently recomputed `832d3169…43e3` and pinned it as their
target. The chain v1 → v2 → v2.1 → v2.2 → v2.3 → v2.4 is acyclic and each link is
byte-identifiable; §1.2 and §1.3 of the correction carry the full preserved
record and the six governing signed inputs, all verified byte-identical to `HEAD`
before reading.

---

## §2. `B-1`..`B-4` and `R-1`..`R-7`, dispositioned one to one

### §2.1 The four blocking findings

| # | X finding | Signed locus that falsified the clause | Disposition | Where |
|---|---|---|---|---|
| `B-1` | `PA-6′` bans `os.chdir` in every root; the PCS preflight's first step is `_chdir("/")` | composite `:819-824`, with its own `CHDIR_FAILED` token and "before any name is opened" | **REPAIRED.** `PA-6″(5)`: exactly one `chdir`, PCS root, Constant `"/"`, lexically before every read and write call in that root; every other `chdir` and all `fchdir`, `symlink`, `link` still forbidden. Withdrawn at `R-W16` | v2.4 §2 |
| `B-2` | blanket `dir_fd` ban vs the composite's general rule and five sites, and vs `PG-3`'s own mechanism | `:822`, `:905`, `:911`, `:916`, `:917-918`, `:1050-1052` | **REPAIRED.** `PA-6″(6)`: prohibited only on a pinned path operand; elsewhere the value must be a signed anchor — int Constant fd 5/6, or a Name bound once from the binding block or protocol §B's held-descriptor set. Withdrawn at `R-W17` | v2.4 §2 |
| `B-3` | `PA-5′`/`PA-7′` assume a path operand; nine forms take a descriptor, two of which `MS-2` and `PG-3` require | `:901`, `:784`, `:846-857`, `:1006-1020`, and v2.3's own `MS-2`/`PG-3` | **REPAIRED.** `PA-6″(1)/(2)` partition the thirty-three forms 24/9; `PA-5″` and `PA-7″(i)-(iii)` govern path operands only; `PA-7″(iv)` binds descriptor operands to a conforming open or a signed slot. Withdrawn at `R-W18` | v2.4 §2, §3 |
| `B-4` | "exactly two write calls exist in the five roots" vs four peer installs plus ledger/head/state/locks | composite §P1-13.7; protocol `:58-72`; contract `:190-200` | **REPAIRED.** `PA-6″(3)`: exactly two write calls **whose path operand is a pinned path Name**; ordinary `PC-N` installs are uncounted and unrestricted. Withdrawn at `R-W18` | v2.4 §2 |

### §2.2 The seven repair texts

| # | X `R-n` | Adopted | Deviation |
|---|---|---|---|
| `R-1` | `chdir` scope | **in full**, `PA-6″(5)` | none |
| `R-2` | `dir_fd` scope | **in full**, `PA-6″(6)` | **one, declared:** `R-2` said the anchor must be "a plain Name". The signed sites at `:905`, `:911`, `:916`, `:917` use the **int literal `6`**, so a Name-only rule would have re-broken exactly what it repairs. `PA-6″(6)(a)` therefore admits an int Constant that is a signed anchor slot, and `(b)` admits the Name form (`:1052`'s `dir_fd = T_PCB_FD_RUNTIME_ROOT`). Same discipline, both spellings |
| `R-3` | operand-kind split | **in full**, `PA-6″(1)/(2)`, `PA-7″(iv)` | none; the two lists partition the same thirty-three forms, `24 + 9 = 33` |
| `R-4` | scoped write count | **in full**, `PA-6″(3)`, and the count line of `S-25m‴` | none |
| `R-5` | imperative write safety | **in full**, `PA-6″(4)` | none |
| `R-6` | producer accounting | **in full**, `S-25m‴`, with the two disjoint fives stated in the rule's own text | none |
| `R-7` | discriminator clause | **in full**, `PG-4′` | none |

**No repair beyond `R-1`..`R-7` was made, and no analysis kind was added.**
`PA-6″(6)` and `PA-7″(iv)` use the same intra-function single-assignment lookup
`D-14′` already prices; `D-11″` and `D-15″` restate the cost mechanically. No
taint, no transitivity, no fixpoint, no call graph, no ban on unrelated
filesystem access.

### §2.3 Y-line surface: preserved, not re-opened

The Y line confirmed v2.3 for author selection. **v2.4 amends no sentence of that
surface.** `PT-1′` and its corollaries, `CA-0`..`CA-5`, `PG-1`, `PG-2`, `PG-3`,
`PG-5`, `PG-6`, `PG-7`, `S-25p`, `CS-1`..`CS-8`, `WL-*`, `DC-*`, `EV-1`..`EV-R4`,
`C-1`..`C-6`, `LD-1`..`LD-3`, `L-0`..`L-5`, `D-1`, `D-2`, `CR-*`, `M-R*`, `MS-*`,
`ACC-*`, `RC-*`, `NC-*`, `P-R*`, `N-1`..`N-10`, the terminal routes and the author
recommendation are untouched. `PG-4′` adds one clause and changes none. The Y
line's own observation — that the `/proc/self/fd` case may terminate earlier, at
the no-follow open, than `A-T25(d)`'s shorthand suggests — remains true and
remains a stricter refusal, not a surviving route.

---

## §3. Exact revised counts

| Quantity | v2.3 | **v2.4** | Change |
|---|---|---|---|
| persistent consumers | 6 | **6** | — |
| centralized accessors | 5 | **5** | — |
| governed-mapping producers | 5 (table only) | **5, asserted in `S-25m‴`** | `R-6` |
| verifier rules | 16 | **16** (`S-25a`..`S-25p`) | none added; `S-25m‴`, `S-25n″` replace |
| behavioural tests | 26 | **27** (`A-T1`..`A-T27`) | `A-T26′` replaces `A-T26`; `A-T27` added |
| governed mapping Names | 3 | **3** | — |
| carrier Names | 5 | **5** | — |
| approved call-site rows | 15 | **15** | — |
| pinned root literals / path Names | 2 / 2 | **2 / 2** | — |
| read function / call sites | 1 / 3 | **1 / 3** | — |
| enumerated read forms | 33, one list | **33 = 24 path-operand + 9 descriptor-operand** | `R-3` |
| write calls | "2 in five roots" *(false)* | **2 with a pinned path operand**; `PC-N` writes uncounted | `R-4` |
| `chdir` occurrences | banned *(false)* | **1, at `P-cwd`** | `R-1` |
| `dir_fd` uses | banned *(false)* | **0 on pinned operands; anchored elsewhere** | `R-2` |
| `ACC-5` evaluations | 3 | **3** | — |
| persistent / transient digest values | 2 / 1 | **2 / 1** | — |
| direct destinations of the claim lineage digest | 2 | **2** (`D-1`, `D-2`) | — |
| transitive continuations | 5 | **5** (`L-1`..`L-5`) | — |
| declassifying operations | 1 | **1** | — |
| content-alias residual members | 5 | **5** (`CA-1`..`CA-5`) | — |
| retained-behaviour fixtures | 6 | **10** (`R-a`..`R-j`) | `R-1`..`R-4` |
| handoff steps | 15 | **15** | `STEP 7` reads rows 92-118 |
| sentences withdrawn this round | 7 | **3** (`R-W16`..`R-W18`) | |

**Arithmetic:** `24 + 9 = 33`, the same forms v2.3 enumerated — the split
repartitions and neither adds nor removes. `26 + 1 = 27`. `6 + 4 = 10`.
`S-25a`..`S-25p` is sixteen letters. `S-25m‴`'s two fives — five accessor
definitions and five governed-mapping producer sites — are **disjoint sets**:
`ACC-2`/`ACC-3` are `MS-8`/`MS-9`, `ACC-4`/`ACC-5` are `MS-6`/`MS-7`, `ACC-1` is
the wire accessor, and none of `MS-3`, `MS-4`, `MS-5`, `MS-11`, `MS-14` is an
accessor.

---

## §4. Fixtures — positive and negative

### §4.1 Positive: every signed operation the X line named, with its admitting clause

| Signed operation | Locus | Admitted by |
|---|---|---|
| PCS preflight `_chdir("/")` | `:819-824` | `PA-6″(5)` |
| `p-1`, `p-4`, `p-6`, `p-7` opens with `dir_fd = 6` | `:905`–`:918` | `PA-6″(6)(a)` + `PA-5″(b)` |
| `c1` `SPAWN.lock` open, `dir_fd = T_PCB_FD_RUNTIME_ROOT` | `:1050-1052` | `PA-6″(6)(b)`; `_O_RDWR` ⇒ read call, not a write call |
| `P-h` read descriptor 3; `L-4` read the reply pipe | `:901`, `:784` | `PA-7″(iv)(b)` |
| `P-f` and `A-5`..`A-11` fstat sequences | `:846-857`, `:1006-1020` | `PA-7″(iv)(b)` |
| `MS-2`'s no-follow open, its whole-content read, `PG-3`'s fstat conjuncts | v2.3 §2.4, `PG-2`, `PG-3` | `PA-5″(a)`, `PA-7″(i)`, `PA-7″(iv)(a)` — **the self-refutation `B-3` named, closed** |
| claim install `MS-12`; lease install `MS-13` | v2.3 §2.4 | `PA-6″(3)`, the two pinned-operand writes |
| spawn-intent, supervisor identity, freeze observation installs | §P1-13.7 | `PA-6″(3)` — ordinary `PC-N` writes, uncounted |
| ledger append, head, state cache, process record, locks | protocol `:58-72`; contract `:190-200` | `PA-6″(3)` |
| three `/proc/self/fd` enumerations | `S-18`, `:2612`, §P1-6.5 | `PA-5″(b)`; `PG-1` excludes enumerations |
| ordinary constant durable paths; no-stem constructors | protocol `:80-84` | `PA-5″(b)`, `PA-3′(b)` |
| every other `PC-N` peer read | `PC-R1′`, `PC-R2′` | `PA-5″`, `PA-7″(iii)`, plus the `PG` gate |

Carried as `R-a`..`R-j` (ten retained-behaviour fixtures) and asserted
individually at `A-T26′(a)`..`(k)`. **A build in which any fails is a test
failure, not a stricter build.**

### §4.2 Negative: what the scoping must not admit, asserted at `A-T27`

```text
N-a second chdir, or a non-"/" operand                   PA-6″(5)
N-b chdir outside the PCS root                           PA-6″(5)
N-c dir_fd on a pinned path operand                      PA-6″(6)
N-d dir_fd from an unanchored expression                 PA-6″(6)
N-e descriptor from a parameter, Subscript or Call       PA-7″(iv)
N-f descriptor from a non-conforming open                PA-7″(iv)(a)
N-g write call containing a read or binding bytes        PA-6″(4)
N-h a third pinned-operand write call                    PA-6″(3), PA-4′
```

**And every closure negative is re-asserted unchanged:** the v2.1 claim
construct, the v2.2 lease construct, `V-a`..`V-q`, `LV-a`..`LV-j` and the four
planted alias cases of `A-T25`. This is the property that matters most about
v2.4: **each repair widens what a conforming implementation may spell and
narrows nothing that was closed.** Every widened form remains inside `PA-1′`'s
two substring pins, `PA-4′`'s two enumerated Name-use sets, `PA-7″(i)`'s single
read function at three call sites, `CR-3′`'s five carrier positions and
`PG-1`..`PG-7`'s gate — none of which v2.4 touches.

---

## §5. Y-line status: confirmation preserved, bounded no-regression check requested

The Y line's `OFFICINA_P1_IDENTITY_V2_3_YLINE_CONFIRMED_FOR_AUTHOR_SELECTION`
stands on the v2.3 bytes and is **not** reopened. Because the bytes have changed,
a **bounded no-regression check** is requested — not a re-confirmation of the
whole surface.

> **Bounded Y question.** On the v2.4 bytes, do the four scoping repairs
> (`PA-6″(5)` `chdir`, `PA-6″(6)` `dir_fd`, `PA-6″(1)/(2)`+`PA-7″(iv)` operand
> split, `PA-6″(3)` scoped write count), the two accounting repairs (`S-25m‴`,
> `PG-4′`) and the mechanical follows (`S-25n″`, `A-T9″`, `A-T26′`, `A-T27`,
> `R-g`..`R-j`) change **any** sentence of the surface you confirmed — the
> pathname theorem and its corollaries, the alias class, the gate order and its
> four planted consequences, the conditional information boundary, `EV-3`/`C-6`
> and the authorized-use boundary, the destinations and continuations, the prior
> closures, the terminal routes, the recommendation, or the negative
> authorization?
>
> If yes, the deliverable is the sentence and its locus. If no, the deliverable
> is a bounded statement that your v2.3 confirmation carries to these bytes.

---

## §6. Bounded X question

> **On the v2.4 bytes, is the packet both CLOSED and SATISFIABLE?**
> (a) Does any AST in the five production roots reach `controller_pid` or
> `process_group_id` from `T_PROCESS_CLAIMS` or `T_ACTIVE_LEASES` while
> satisfying `S-25a`..`S-25p` — in particular through any form the four scoping
> repairs newly admit: a `dir_fd`-anchored open, a descriptor-operand read, an
> ordinary `PC-N` write call, or the single permitted `chdir`?
> (b) Does every operation the signed chain requires now have at least one
> conforming spelling, per §6 of the correction — the PCS preflight, the
> fd-relative opens, the descriptor reads and fstat sequences, `MS-2`/`PG-3`,
> the two pinned installs, the four peer installs, protocol §B's writes, the
> three `/proc/self/fd` enumerations, constant durable paths, and every `PC-N`
> read?
>
> If (a) yields an AST, that is blocking and the deliverable is the AST. If (b)
> fails, the deliverable is the signed operation with no conforming spelling and
> its locus.

---

## §7. Independence — a requirement of this round, not a recommendation

**The v2.3 correction, the v2.3 closure, the v2.3 X-line review, and this v2.4
correction and closure were all produced by the same agent in the same session.**
The v2.3 X review disclosed this and recommended an independent re-run; v2.4
adopts that as binding.

```text
THE NEXT X REVIEW OF THIS CELL MUST BE PERFORMED BY AN AGENT THAT AUTHORED
NEITHER v2.3 NOR v2.4. Preferably Claude Opus 4.8 or Fable 5.

REASON, STATED PLAINLY. The chain's discipline is two independent lines on
identical bytes. On v2.3 that condition held for the Y line and not for the X
line. A self-review that finds four blocking defects in its own text is
evidence of effort, not of independence: the same blind spot that wrote a
clause can survive into the review of it, and B-1 is a proved instance — the
v2.2 X review affirmatively certified the chdir ban as sound, and it was false
on the signed bytes at the time it was certified.

CONSEQUENCE FOR THE VERDICT TOKEN. A CONFIRMED token from a non-independent X
line should not be treated as satisfying the two-line discipline, whatever its
content. The author-principal should treat any such token as an author-side
pre-check only.
```

---

## §8. Remaining weak points

The six disclosed at v2.4 §10, triaged:

```text
1  PA-6″(6) PROHIBITS dir_fd ON PINNED OPERANDS, and protocol :58-72 puts "the
   runtime DIRECTORY" in the held-descriptor set. I followed R-2 and the
   mandate exactly and pre-stated the one-line repair if an implementation
   review later requires anchored claim/lease opens. DISCLOSED RESIDUAL WITH A
   PRE-STATED REPAIR.
2  PA-7″(iv)(b) DEFERS to the signed slot table rather than enumerating it —
   deliberate, since this packet does not own it, and fail-closed. DESIGN
   CHOICE A REVIEWER MAY REVERSE.
3  mmap.mmap AND shutil.copyfileobj were placed in the descriptor-operand list
   by judgement; both are unimportable under every current allowlist.
   DISCLOSED.
4  PA-6″(3)'s READABLE-MODE TABLE is enumerated, not proved total; an omission
   fails closed, because a readable mode keeps the call inside PA-5″/PA-7″.
   INSTRUCTION TO THE REVIEWER: check the table against the modes an
   implementation actually uses.
5  I RE-READ rather than RE-DERIVED the Y-confirmed surface, which is the
   weaker act; §5's bounded check is what should establish it still holds.
   DISCLOSED.
6  TWO CONSECUTIVE ROUNDS HAVE SATISFIED THE TWO-LINE DISCIPLINE ON ONE SIDE
   ONLY. §7 makes independence a requirement rather than a preference.
   BLOCKING FOR THE NEXT ROUND'S PROCESS, NOT FOR THESE BYTES.
```

---

## §9. Verdict and negative authorization

```text
READY_FOR_OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_AND_BOUNDED_Y_CONFIRMATION
```

The verdict asserts exactly this and nothing more: in the author's judgement the
four fail-closed satisfiability defects the X line returned are repaired exactly,
by adopting `R-1`..`R-7` in full with one declared deviation (`R-2`'s anchor may
be an int Constant as well as a Name, because the signed sites use the literal
`6`); every signed operation now has a demonstrated conforming spelling; every
closure negative is re-asserted unchanged; the counts are re-derived; and no
sentence of the surface the Y line confirmed is amended. The bytes are therefore
**fit to be reviewed** — by an independent X line and by a bounded Y
no-regression check. It asserts no correctness that a confirmation line has not
independently established.

**This closure authorizes nothing.** Not Kirill's identity author selection, not
`I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY`, not
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not implementation, not a
verifier or manifest edit, not a commit, not a code or test artifact, not
activation, not process control, not resource use, not entropy, not data, not a
trajectory, not a comparison, not spend, not custody disposition, not a datum,
outcome, Proof or claim movement. **Kirill's author selection remains
unauthorized pending an independent X-line confirmation and a bounded Y-line
no-regression check on these exact bytes.** No existing file was modified in
producing this round; its sole products are the v2.4 correction and this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT MADE, NOT AUTHORIZED
OPTION A = RECOMMENDED, UNSELECTED
OPTION B = NON-SELECTABLE
NEXT X LINE = MUST BE INDEPENDENT OF v2.3 AND v2.4
```
