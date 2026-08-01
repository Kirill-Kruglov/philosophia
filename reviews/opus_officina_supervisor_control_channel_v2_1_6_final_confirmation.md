REVISE_OFFICINA_SUPERVISOR_V2_1_6

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.6

Date: 2026-08-01
Reviewer line: X (adversarial Linux / process / crash / hash-construction semantics)
Review base: commit `def5905` (HEAD), whose ancestry includes the required
`692207aa07ad87fcf46a9827524b25ca54d56c07`. Working tree dirty exactly as
handed over; **nothing modified by this review.**

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.6 was authored
by **Claude Code Opus 5 in the specification-author role** (Fable 5
unavailable). I read the v2.1.6 closure/chat response **only as untrusted
author claims** and used none as evidence. Per v2.1.6's own record and the
task, **there is no X verdict for v2.1.5** (that trace stopped before a
deliverable); I do not carry any prior confirmation across.

**Disclosure of my own record.** My in-progress v2.1.5 trace was heading toward
a confirmation, yet the Y line correctly **revised** v2.1.5 with a Critical
(C1: a malformed *opposite* terminal makes `¬Q`/`¬S` true, letting a positive
branch release) that I had glossed. That is the third consecutive round in
which the Y line caught a Critical/Major after my X analysis leaned confirm. I
have therefore, this round, (1) independently **rebuilt** the disposition
cross-product from the predicates rather than trusting the author's table, (2)
verified the `CLOSE_OWNED` claims against actual Linux/PEP-475 semantics, and
(3) executed the required attack item 6 literally — a whole-chain **and
test-obligation** search for bound claims. That search found a Major the
author's own "exhaustive search" missed.

## Recomputed hashes (all verified)

```text
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md   (== expected)
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The v2.1.6 digest matches the expected value exactly; every inherited surface
and the Sol v2.1.5 review are byte-identical to what v2.1.6 cites.

**Method.** Static and read-only. No process, test, or probe ran. Literal
hashing/arithmetic and text greps over documented bytes only. Import-allowlist
facts cited from `verification.py:35-38`; every primitive v2.1.6 uses is inside
`os`/`hashlib`/`json`, zero delta.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_V2_1_6
```

v2.1.6 genuinely closes **Sol C1, M1, M2, and m1** with exact, executable text
I re-derived and, for the selector, rebuilt from first principles. But it does
**not** close **Sol M3** (the contradictory-bound-language class) by *total*
text, and in the attempt it introduces two false universal/completeness claims
refuted by operative carried text — a new **Major**, **X216-M1**. Because the
required question gates on "Sol ... M3 ... closed by exact, executable and
**total** text" and on "no new ... Major," and attack item 6 explicitly directs
the whole-chain-plus-test-obligation search that exposes it, the token remains
unavailable.

The defect is a single, bounded, mechanical repair (narrow the CLI-total-bound
claims and correct the two completeness assertions). It reopens no author cell.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT   — NOT signable
```

---

## New findings

### X216-M1 (Major) — Sol M3 is not closed by total text: operative fixed-CLI-total-bound claims contradict §V216.4.1, and §V216.4's completeness assertions are false

**Loci.** v2.1.6 §V216.4.1 (its universal sentence "**no statement anywhere**
asserts that no bootstrap syscall can outlive a deadline") and §V216.4.2 ("An
exhaustive search ... yields **exactly these five loci; there are no others**"),
against operative carried text: v2.1.3 §U2.4 (lines 375–377), v2.1.2 §N12 **test
row 86** (line 1462, carried by v2.1.6 §V216.6's "§N12 rows 75–96 carry
forward"), v2.1.2 §N3.5 (line 687), and v2.1.3 §U2.7 (line 479).

**The contradiction.** §V216.4.1 admits, correctly, that the bootstrap's
"canonical file installs, and file and parent-directory `fsync`s ... none of
these has an executable duration bound," and then makes the sweeping claim that
**no statement anywhere** asserts a bootstrap syscall cannot outlive a deadline.
That sweeping claim is false. The CLI performs the `SPAWNING*.json` installs
(`c2`, `c7`, `c11`, `c15`) with `fsync`s **while holding `SPAWN.lock`**, and
operative carried text asserts the CLI's *total* is fixed-bounded:

- **§U2.4 (operative, verbatim):** "**Total CLI bound**:
  `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` + 3 × `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` +
  bounded kill/death proof (30 s + 30 s + bounded) ... **No wait is
  unbounded**." (v2.1.4 replaced only §U2.4's `c9/c12/c13/c16` *steps*, not this
  sentence.)
- **§N12 test row 86 (operative):** "no `flock` wait is unbounded anywhere; **the
  CLI's total bound equals the stated arithmetic sum**."
- **§N3.5 (operative):** "a contract-following CLI **always releases within that
  arithmetic sum** (30 s + 10 s + 10 s + bounded proof)."

A "total bound = fixed arithmetic sum" is precisely an assertion that every CLI
syscall — including the acknowledged-unbounded installs/`fsync`s — completes
within that sum. So §U2.4 / row 86 / §N3.5 **assert exactly what §V216.4.1 says
no statement asserts**, and they assert exactly what §V216.4.1 admits is not
true. §V216.4.2's "exhaustive search ... there are no others" is likewise false:
its own search terms include `always releases`, which matches §N3.5 line 687
verbatim, and the "Total CLI bound" / "total bound equals" loci are additional
matches it did not enumerate.

**Why this is Sol M3's class, unclosed.** Sol M3 required that "no bootstrap
syscall can outlive its deadline / healthy launch releases inside the bound"
language be **replaced**, not merely extended, and that only bounded pipe I/O
carry such a guarantee. v2.1.6 R4 did that for the grandchild-gate and
"no blocking syscall" loci but left the **CLI-total-bound** sub-class operative
and contradicted. The task's attack item 6 states the criterion exactly: "Only
bounded pipe I/O may carry that guarantee." The CLI-total-bound claims carry a
bounded guarantee resting on non-pipe I/O (the install `fsync`s).

**Failure scenario / counterexample.** An implementer must satisfy operative
test **row 86** ("the CLI's total bound equals the stated arithmetic sum") while
§V216.4.1 states the CLI's `c15` install `fsync` has **no** duration bound.
These cannot both be honored in the worst case: under a slow or hung `fsync` the
CLI's total (and its lock-hold) exceeds the stated sum, so row 86's assertion is
false, exactly as §V216.4.1 concedes. The contract thus leaves the CLI-total-
bound behaviour to implementer resolution — one implementer adds an unsigned
deadline to the installs to pass row 86; another leaves them unbounded per
§V216.4.1 and cannot — which is the "left to the implementer" defect Sol M3
named.

**Severity rationale (Major, not Critical; not Minor).** It is not Critical:
behaviour under a working filesystem is benign (the CLI releases in `fsync`-time
and does not wedge), and D1 holds **independently** via the separate operative
fact "no supervisor waits on `SPAWN.lock`," so the running supervisor's lifetime
never depends on the CLI's bound. It is not Minor: it is the exact class Sol M3
required be **totally** eliminated, it is left **operative** (carried verbatim,
including a **test obligation**, row 86), and v2.1.6's repair asserts two
**verifiably false** completeness/universality claims (§V216.4.1's "no statement
anywhere," §V216.4.2's "no others") — the same false-exhaustiveness failure that
motivated Sol M3. The required question's "closed by ... total text" criterion
for M3 is therefore not met.

**Smallest bounded repair.** Extend §V216.4's search-and-replace to the
CLI-total-bound loci: replace §U2.4's "Total CLI bound: [fixed sum] ... No wait
is unbounded", §N12 row 86's "the CLI's total bound equals the stated arithmetic
sum", and §N3.5/§U2.7's "always releases within that arithmetic sum" with the
accurate narrower statement — the CLI's **pipe reads/writes and its lock
acquisition** are bounded by their deadlines, but its `/proc` reads and canonical
installs/`fsync`s have **no** duration bound (per §V216.4.1); and D1 holds
because **no supervisor waits on `SPAWN.lock`**, not because the CLI's total is
fixed-bounded. Correct §V216.4.1's "no statement anywhere" and §V216.4.2's
"exactly these five loci; there are no others" to enumerate these additional
loci. No new constant, author cell, or import. The corrected bytes require a
fresh X/Y check.

### X216-m1 (Minor) — `STAGE_M_ROUTE` step 2 does not explicitly route a non-`ENOENT` `/proc` stat read failure to the fail-closed continuation

**Locus.** §V216.3.2 step 2 (`2a`–`2f`) and §V216.3.3's `c6` row ("otherwise
`2d`"). Step `2a` reads `/proc/<pid_mid>/stat`; the branches handle ABSENT
(`2b`), PRESENT+matching (`2c`), PRESENT+capture-now (`2d`), and
PRESENT+mismatch (`2e`). A **present-but-unreadable or parse-failing** stat (not
`ENOENT`) is not explicitly routed: `2d`'s "capture it now" presupposes a
readable stat, and `2e` requires a *captured* mismatch.

**Assessment.** The safe behaviour is implied by the section's governing rule
("KILL, only if identity-safe") — an unreadable stat is not identity-safe, so no
kill and the fail-closed continuation (no record removed) should apply — and
step 3's death-proof poll is already total (any non-death outcome → bound →
FAIL-CLOSED). It is also essentially **unreachable on the pinned Linux target**:
`/proc/<own-child-pid>/stat` is world-readable while the process exists and
returns `ENOENT` once it is reaped, and the middle child is a benign Python fork
whose `comm` cannot break a correct parser. So it is fail-closed by implication
and unreachable in practice. **Smallest repair:** add one sentence — "if `2a`'s
stat is present but cannot be read or parsed, treat as not identity-safe ⇒
FAIL-CLOSED CONTINUATION." Non-blocking on its own.

No new Critical survived re-derivation.

---

## One-to-one disposition of the Sol v2.1.5 findings

| Sol v2.1.5 | v2.1.6 locus | Verdict | Basis (re-derived) |
|---|---|---|---|
| **C1** malformed opposite terminal treated as absence ⇒ releasing branch | §V216.1 | **CLOSED** | The predicates are split into **physical presence** `PS`/`PQ`/`PF` (decided *without* decoding — symlink/dir/zero-byte/truncated all count as present) and **validity** `VS`/`VQ`/`VF`; `MALFORMED = (PS∧¬VS)∨(PQ∧¬VQ)∨(PF∧¬VF)` is Rule 0 and dominates, and every releasing rule carries `¬MALFORMED` **and** physical absence of the opposite terminal (`¬PQ` for B-P, `¬PS` for B-QM/B-QN) — a **double block**. I **independently rebuilt** the cross-product (decision tree on `(PS,PQ)`): rows are exhaustive and disjoint, and all five Sol counterexamples now hit Rule 0 and release nothing. The three branch bodies and the P1–P7 custody proof are unchanged. |
| **M1** normal close sites outside the pinned close/errno state machine | §V216.2 | **CLOSED** | One `CLOSE_OWNED` primitive (four outcomes `CLOSED`/`CLOSED_ABSENT`/`CLOSED_ERROR`/`NOT_OWNED`) is used at **every** close site including both `SPAWN.lock` closes (§V216.2.3 lists `c5/c8/c12/c13/c16/c18/m1/m6/m8/g1/g3/cleanup/refusal/stage-M`). I verified the Linux semantics: `EINTR`⇒released-not-retried (PEP 475), `EBADF`⇒nothing was open, other errno⇒released; `NOT_OWNED`⇒no syscall (prevents closing a reused number); ownership removed unconditionally-once. The uniform `CLOSED_ERROR→CONTINUE` is justified because on Linux the descriptor is released in every outcome, so the observable reader/writer counts (and every EOF/`EPIPE`) equal the success case — **no site's correctness depends on the close return**. Forked copies are distinct ownerships. |
| **M2** `c5`–`c7` failure removes records while the middle may be live | §V216.3 | **CLOSED** (one Minor, X216-m1) | `STAGE_M_ROUTE` pins an exact stage (pre-group ⇒ `kill(pid_mid)` only, never `killpg`), an identity source per cut, a **kill and proved death before any record removal**, and a FAIL-CLOSED continuation (PID reuse `2e` or death-proof expiry) that removes **no** record and states honestly the singleton is not free until the middle exits at its bound. The two v2.1.5 false claims (EOF at `m0`; "released") are deleted with the correct reason (middle owns its own `rel1_w` until `m1`; fork-shared flock). Every §V216.3.4 crash prefix keeps the death-proved-only boundary. |
| **M3** carried universal no-blocking / healthy-bound obligations contradict the honest policy | §V216.4 | **NOT CLOSED (by total text)** | The two `no blocking syscall` invariants and rows 121/126 are correctly replaced (I verified the five §V214 loci by grep). But the **CLI-total-bound** sub-class of the same defect is left operative and contradicts §V216.4.1, and §V216.4's completeness claims are false — **X216-M1** above. |
| **m1** ownership table attributes boot EOF to the wrong end | §V216.5 | **CLOSED** | The annotation moves to the `boot_w` row and the `rel3_r` row becomes ownership-cleanup only; §V216.5.2 audits all eight ends (closing a **write** end ⇒ EOF on the paired read; closing a **read** end ⇒ `EPIPE` on the paired write), and tightens the `m7`/row-154 attributions to name `boot_w`. `c13` EOF is from the last `boot_w`; no impossible `m0` EOF claim survives. |

---

## The eight required attack traces

### 1. Physical/valid selector

`PS`/`PQ`/`PF` are decided by `stat(follow_symlinks=False)`+enumeration
**without decoding**, so a symlink, directory, zero-byte, truncated, or partial
object at a canonical name is **present** and (being non-regular/non-decoding)
**invalid** ⇒ `MALFORMED` ⇒ Rule 0. `.tmp`/extra-name entries never appear at a
canonical name and are L4/L5 custody refusals. `MALFORMED` dominates (Rule 0
first; every other rule carries `¬MALFORMED`). Both-terminal uses **physical**
`PS∧PQ` (Rule 1), catching an unreadable opposite terminal. Every releasing rule
requires physical absence of the opposite terminal. Mutations between the
presence stat and the validity read are in one lock epoch for the supervisor; an
A3 same-UID process racing a mutation is the signed procedural residual, and a
swapped-but-valid terminal still fails the hash/custody conjuncts. **No malformed
or physically-present opposite terminal is read as absent.**

### 2. Selector exactness

I rebuilt the complete cross-product independently via the `(PS,PQ)` decision
tree (§V216.1.3): every leaf reached by one path; the four quadrants partition;
each state satisfies exactly one rule. All five prior counterexamples now
release nothing (Rule 0, and additionally the `¬PQ`/`¬PS` block). Rule 0 and
Rule 1 share the **same continuation class** (record-first invalidity, release
nothing), differing only in which paths the record names, so their order changes
no outcome. Every ordinary-pending (`5b`) vs impossible-durable-layout
(`5c`–`5h`, Rule 1) state has exactly one correct continuation; rows 2/5/8 are
the only releasing rows and each releases `bytes_reserved` once after the
unchanged body + P1–P7 + §N1.5.

### 3. `CLOSE_OWNED`

Linux/PEP-475 semantics verified: `EINTR` releases the fd (no retry), `EBADF`
means nothing open, other errno releases; `NOT_OWNED` performs no syscall; a
second call is `NOT_OWNED`; fd-number reuse is defeated by removing ownership
and never retrying/re-closing. The uniform `CLOSED_ERROR→CONTINUE` is challenged
and holds at every normal, cleanup, forked-copy, and `SPAWN.lock` site: the
release is unconditional, so the observable pipe state (and the flock release)
equals success; no site's correctness depends on observing a successful return.
The `SPAWN.lock` exclusion of v2.1.5 is deleted — the lock is tracked in `owned`
and closed via `CLOSE_OWNED`.

### 4. `c5`/`c6`/`c7` identity and kill

`STAGE_M_ROUTE` captures the strongest available identity (`pid_mid` always,
start identity if `c6` done, durable record if `c7` done), kills only if
identity-safe (`kill(pid_mid)`, never `killpg` pre-group), requires a `ppid ==
getpid()` cross-check when capturing fresh, treats PID reuse (`2e`) as
no-kill-fail-closed, and proves death (`/proc` absence or `Z` + `waitpid`)
**before** any record removal; a record with a different `spawning_id` is never
unlinked. If identity or death cannot be proved, the FAIL-CLOSED continuation
removes **no** record and does not claim the singleton is free. **One gap
(X216-m1):** a present-but-unreadable/parse-failing `/proc` stat is not
explicitly routed (fail-closed by implication; unreachable on Linux).

### 5. Crash prefixes

§V216.3.4's eleven prefixes each have one continuation; none removes a
live-identity record (kill+death-proof precede removal), none kills/releases an
unrelated process/descriptor (start-identity revalidation; `CLOSE_OWNED` acts
only on this process's owned set), and a CLI crash mid-route releases only the
CLI's own fds/lock via kernel action while the next attempt's P0–P3 governs the
surviving records. Consistent and total.

### 6. Bound language

**This trace fails — X216-M1.** The narrow pipe-only invariant (§V216.4.1) and
rows 121/126 are correctly replaced. But my whole-chain-plus-test-obligation
grep (as attack item 6 mandates) found operative fixed-**CLI-total**-bound
claims — §U2.4 "Total CLI bound: [fixed sum] ... No wait is unbounded", §N12
**test row 86** "the CLI's total bound equals the stated arithmetic sum", §N3.5
"always releases within that arithmetic sum", §U2.7 — that rest on the CLI's
`SPAWNING*.json` install `fsync`s, which §V216.4.1 itself admits are unbounded.
§V216.4.1's "no statement anywhere" and §V216.4.2's "exhaustive search ... no
others" are therefore false. Only bounded pipe I/O may carry the guarantee; these
do not. Slow-valid `c14`/`c15` is correctly non-citable for the **grandchild
gate** (§V215.3), but the CLI-total-bound claims are not narrowed.

### 7. EOF provenance

§V216.5.2 audits all eight ends. Closing a **write** end causes EOF on its
paired read (`boot_w`→`boot_r` at `c9`/`c13`; `rel2_w`→`rel2_r`;
`rel3_w`→`rel3_r`); closing a **read** end causes `EPIPE` on its paired write
(never EOF). `c13`'s EOF is correctly attributed to the last `boot_w`, never
`rel3_r`; the impossible `m0` EOF (via `rel1_w`, which the middle owns until
`m1`) is named impossible and replaced by the bound. The two loose `boot_w`/
`rel3_r` pair attributions (`m7` row, test row 154) are tightened to name
`boot_w`. Correct.

### 8. No regression

Aside from X216-M1's operative stale CLI-bound text, the nonblocking bootstrap,
`B-P`/`B-QM`/`B-QN` bodies and K1 release, GC (`accepted` last + `D6`),
lock-first preflight, watchdog partition, A3 stream-hash truth (four residuals),
author authority (all carried digests reproduce as in prior reviews), capacity/
custody accounting, nine events, E1/E2/E3, Q/C boundary, and T inactivity are
carried verbatim (§V216.0 replacement index checked row-by-row). Zero new
constant/object/path/schema/token/import.

---

## No-regression table

| Signed cell / surface | Status under v2.1.6 |
|---|---|
| **A3** | Not reopened; four write/hash residuals and close diagnostics remain procedural, non-citable. |
| **B1** | Not reopened; no journal/ack/frontier/prefix/GC/classification rule changes. |
| **C1** | Not reopened; watchdog remains witness/freezer, supervisor sole settler. |
| **D1** | Policy intact (no idle exit; supervisor never waits on `SPAWN.lock`). **X216-M1** leaves operative CLI-total-bound text contradicting §V216.4.1's unbounded-`fsync` admission; behaviourally benign (D1 holds independently) but a totality/exactness defect of the M3 class. |
| **K1** | Not reopened; five constants, one-write/one-hash, no replenishment, three branch bodies unchanged; §V216.1 **removes** the malformed-layout release path (Sol C1). |
| Author authority / custody / manifest / fallback / fd-remap | Preserved; illustrative digests reproduce (verified in prior reviews). |
| Generic harness v2.3.1 / batch v1.1.1 | Unchanged; §J1–§J3, §D1/§D2, nine events, archival order intact. |
| Q/C boundary / T inactivity | Every new fact control-plane, non-citable; T `NOT_ACTIVATED`. |

## Author-cell determination

**No new author cell is required.** X216-M1 and X216-m1 are mechanical text
repairs (narrow the CLI-total-bound claims; correct two completeness
assertions; add one fail-closed sentence to `STAGE_M_ROUTE`) over the
already-signed A3/B1/C1/D1/K1 policy. No new constant, resource value,
invalidity cause, custody destination, or token.

## Authorization boundary

Because the verdict is **REVISE**, Kirill's informed signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **unavailable**
and is not made signable. This review authorizes **no** implementation, commit
of the untracked/dirty implementation, T activation, entropy, runtime
construction (supervisor, controller, worker, watchdog, adapter, middle child,
endpoint, pipe, FIFO, journal, spawn record, operation, capacity artifact,
custody disposition, author decision file), E1/E2/E3 spend, Q/C work, or
science. The smallest correction (X216-M1's bound-language narrowing plus
X216-m1's one sentence) must be prepared as a bounded v2.1.7 layer and receive a
**fresh independent X-line and Y-line review** of its own bytes; no earlier
confirmation carries across.

## Contract versus implementation

Every finding is a property of the v2.1.6 **contract**. The implementation
(`src/philosophia/officina/generic_harness.py`) is untracked and contains no
supervisor, control channel, adapter, journal, or transport; it neither causes
nor cures any v2.1.6 contract finding.

## Custody confirmation

No process, test, or probe ran; no Officina process, pipe, FIFO, or journal was
started; this review started no process of its own. The only computations were
`sha256`/grep over documented bytes in read-only inspection. No code, test,
contract, signature, prior review, or runtime artifact was edited; nothing was
committed or staged; the dirty and untracked handover files are preserved
unmodified. Exactly one new file was created — this review. No runtime or
scientific artifact was created. `successor/officina/runtime/` contains only
`T_RUNTIME.lock`; `successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. No capability,
claim, lease, batch, operation, entropy, E1/E2/E3 spend, world, learner,
candidate, Q/C object, datum, or outcome exists. **T remains `NOT_ACTIVATED`;
the programme claim remains `OPEN`.**
