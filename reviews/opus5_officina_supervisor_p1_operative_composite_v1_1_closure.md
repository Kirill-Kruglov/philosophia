READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_1_XY_REVIEW

# Author closure — P1 operative composite v1.1

**Author:** Claude Code Opus 5, acting **only as the specification author**.
I authored the entire supervisor/control-channel chain, v1 of this composite,
and v1.1. I am therefore **disqualified** as an independent X-line or Y-line
reviewer of it. **This closure is an untrusted self-assessment.** Its verdict
line means "the author believes the three commissioned defects are closed and
the object is now reviewable" — it does not mean the object is correct, and it
confers no acceptance, no implementation authority and no clearance.

Every prior author closure in this chain, including
`reviews/opus5_officina_supervisor_p1_operative_composite_v1_closure.md`, is
likewise untrusted. Two of them were subsequently shown to be materially wrong:
v2.1.10.1 declared `READY` over an unimplementable transport, and v1 of this
composite claimed no behavioural placeholders remained when twenty occurrences
of a single token did. That history is the reason this closure shows the exact
search domain and the exact command results for every zero it claims, rather
than asserting the zeros.

**State unchanged by this round:** `T = NOT_ACTIVATED`; programme claim `OPEN`.
No X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement was produced or authorized.

---

## 1. Deliverables

Exactly two new files. **No existing file was edited.**

| Path | Lines | Bytes |
|---|---|---|
| `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md` | 2 518 | 151 733 |
| `reviews/opus5_officina_supervisor_p1_operative_composite_v1_1_closure.md` | this file | — |

v1.1 is a **full, self-contained replacement** for v1. It is not a delta. A
reader who has never opened v1 can implement from v1.1 alone. Nothing in v1.1
instructs anyone to open v1, and v1 appears in v1.1 only as one provenance
digest line.

---

## 2. Governing digests

Computed with `sha256sum` on the final bytes. **v1.1 contains none of its own
digests**, so the custody chain has no cycle.

```text
H_FILE       90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680
H_BODY       aff3d4eea1105f3f9572379c53a27673486a6bd263c3c23810f16be9f1b7391c
H_GUARDDATA  0d3131b4a319d0bf03310e203485320253b671501ec44f87d67e8d47f8616733
H_NORMATIVE  03536a6b72d5d9326d2b646329c295d3ee4c3a3447a49106a252932b8597622b
```

`H_NORMATIVE` is over the **ordered** concatenation `REGION(BODY) ||
REGION(GUARDDATA)`, in that order, each region being the lines strictly between
its two sentinels, each line including its terminating `0x0A`.

Region extents on the final file, and the sizes the digests cover:

| Region | Sentinel lines | Content lines | Content bytes |
|---|---|---|---|
| `BODY` | 128 and 2414 | 129–2413, 2 285 lines | 137 040 |
| `GUARDDATA` | 2416 and 2451 | 2417–2450, 34 lines | 1 487 |
| `PROVENANCE` | 2453 and 2518 | 2454–2517, 64 lines | not digested separately; covered by `H_FILE` |

The four digests are for the independent reviews to **recompute**, not to
accept. They are reported here so the manifest fields
`p1_composite_sha256`, `p1_composite_body_sha256`,
`p1_composite_guarddata_sha256` and `p1_composite_normative_sha256` have
reviewed values to record.

---

## 3. Defect R1 — marker collision — CLOSED

### 3.1 The confirmed v1 defect

v1 (`d2975d19c553d9f9338bacff9d0a2af1855af45881e305a8706c110820896935`,
2 117 lines) carried four occurrences of its two sentinel strings:

```text
  42:<!-- OFFICINA-P1-NORMATIVE-BEGIN -->
1703:    <!-- OFFICINA-P1-NORMATIVE-BEGIN -->      an indented example
1707:    <!-- OFFICINA-P1-NORMATIVE-END -->        an indented example
2013:<!-- OFFICINA-P1-NORMATIVE-END -->
```

A first-match extractor terminates at line 1707 and yields 1 663 lines: lines
43–1702 (1 660) plus 1704–1706 (3). **Lines 1708–2012 — most of §C13, all 80
rows of the §C14 test matrix, and all of §C15 — fell outside the digested
region.** The v1 closure's own figure, "1 663 lines of the file's 2 117", is
the arithmetic proof of the truncation. The v1 `NORMATIVE_BODY` digest
`4eb1ddc63dc92d476e79f8c312322a7f7ed6052f742162cd37c05057827c5d79` therefore
pinned a truncated object and is void.

### 3.2 What v1.1 does instead

**Sentinels are never written literally inside a normative region.** They are
defined by an exact byte-construction rule from five named fragments
(`FRAG_OPEN`, `FRAG_SP`, `FRAG_TAG`, `FRAG_DASH`, `FRAG_CLOSE`) over a
three-element region set and a two-element edge set. An example can no longer
collide with a delimiter, because no example spells one.

**Six sentinels, each required to occur exactly once.** `EXTRACT` is total and
fail-closed: a count of zero *and* a count above one both fail
(`"sentinel cardinality"`), and the six indices must satisfy
`b_BODY < e_BODY < b_GUARDDATA < e_GUARDDATA < b_PROVENANCE < e_PROVENANCE`
(`"sentinel order"`). Guard `G-8` runs these checks **before any other guard
and before any digest**. New guard `G-9` requires the verifier's own compiled
fragment constants to equal the document's, so a verifier cannot silently
extract a different region than the one delimited.

### 3.3 Mechanical verification on the final bytes

```text
$ grep -n -E '^<!-- OFFICINA-P1-(BODY|GUARDDATA|PROVENANCE)-(BEGIN|END) -->$' <v1.1>
 128:<!-- OFFICINA-P1-BODY-BEGIN -->
2414:<!-- OFFICINA-P1-BODY-END -->
2416:<!-- OFFICINA-P1-GUARDDATA-BEGIN -->
2451:<!-- OFFICINA-P1-GUARDDATA-END -->
2453:<!-- OFFICINA-P1-PROVENANCE-BEGIN -->
2518:<!-- OFFICINA-P1-PROVENANCE-END -->

$ grep -o -E 'OFFICINA-P1-[A-Z]+-(BEGIN|END)' <v1.1> | sort | uniq -c
      1 OFFICINA-P1-BODY-BEGIN          1 OFFICINA-P1-GUARDDATA-BEGIN
      1 OFFICINA-P1-BODY-END            1 OFFICINA-P1-GUARDDATA-END
      1 OFFICINA-P1-PROVENANCE-BEGIN    1 OFFICINA-P1-PROVENANCE-END
```

Cardinality exactly one for all six, as **substrings anywhere in the file**,
not merely as whole lines — a stricter test than the extractor applies. Order
correct. The v1 marker string `OFFICINA-P1-NORMATIVE-` occurs zero times.

### 3.4 Nothing is lost from the digested region

Every section heading and its position relative to the region boundaries:

```text
BODY  = 129..2413
  132 §P1-1    205 §P1-2    321 §P1-3    435 §P1-4    532 §P1-5
  615 §P1-6    722 §P1-7   1134 §P1-8   1386 §P1-9   1486 §P1-10
 1658 §P1-11  1872 §P1-12  1949 §P1-13  2031 §P1-14  2298 §P1-15
 2399 §P1-16
GUARDDATA = 2417..2450
 2418 §P1-17
PROVENANCE = 2454..2517
 2455 §P1-18
```

The three sections whose v1 analogues were truncated away are now fully
interior to `BODY`: the peer interface (§P1-13, at 1949), the test matrix
(§P1-15, at 2298, **85 rows**, highest row number 85, verified by counting
`^| N |` rows within lines 2298–2398), and the negative space (§P1-16, at
2399). `BODY` ends at 2413, sixteen lines after §P1-16 opens and after its last
sentence.

Negative fixtures for the failure modes are commissioned as test 78: a
duplicated sentinel, a missing sentinel, reordered sentinels, and a
sentinel-shaped line appearing as an example each fail closed before any digest
is computed; and `G-9` rejects a verifier built with any altered fragment,
region name or edge name.

---

## 4. Defect R2 — residual placeholders — CLOSED

### 4.1 The confirmed v1 defect

Counted over the whole v1 file: `unchanged` 20, `preserved` 3,
`signed adapter` 1, `signed record` 1; `carried`, `as before` and `same as` 0.
The v1 closure's claim that no behavioural `unchanged` remained was false.

### 4.2 The exact search domain

Everything below was run over `REGION(BODY) || REGION(GUARDDATA)` of the final
v1.1 bytes — **2 318 content lines, 138 527 bytes**, extracted as file lines
129–2413 followed by file lines 2417–2450, matching `H_NORMATIVE` exactly. The
provenance region was deliberately **not** included, because its historical
digest listing is non-normative by construction and is read for behaviour by
nothing.

Match method: `grep -o -i -F "<pattern>" | wc -l` — case-insensitive **literal
substring**, counting every occurrence rather than every matching line. This is
strictly stronger than a token or word-boundary search: it catches a forbidden
token embedded inside a longer word.

### 4.3 Result

```text
unchanged              0        as above               0
carried                0        as below               0
as before              0        identical in every     0
same as                0        the same as            0
preserved              0        as stated              0
signed adapter         0        as described           0
signed record          0        see above              0
per the previous       0        prior document         0
earlier version        0        elsewhere              0
TBD                    0        TODO                   0
XXX                    0        FIXME                  0
carried over           0        left as                0
remains as             0        unspecified            0
to be defined          0

identical to           1        ← classified below, not a delegation
```

**The required count is zero for every placeholder pattern, and it is zero.**

The single `identical to` occurrence is at §P1-11.1 step P2a:

> `P2a. the same spawning_id and byte-identical to what this attempt would
> install ⇒ adopt the existing record; do not rewrite it; ...`

This is a **literal comparison predicate** over two concrete byte strings — the
durable record on disk and the record this attempt would construct — not a
delegation of content to another document. It states its own test completely. I
report it rather than suppress it so the reviewer can overrule my
classification.

### 4.4 Two false positives found and removed rather than argued

The first audit pass returned `as before` = 1. It was the substring inside
"whatever it **was before**" in the `g-5` signal-mask discussion — a false
positive under substring matching. Rather than defend it, I reworded the
sentence to "whatever value it held previously" so that a reviewer running the
same naive substring search gets zero with no judgement call required.

The same pass found five genuine **within-document** delegations that a
placeholder-token search would not catch. Because the standard is literal
self-containment, all five were literalized:

| Locus | Was | Now |
|---|---|---|
| §P1-8.3 `SIGNAL_GROUP` row | `sig` "as above"; response "as above" | `sig` in `{CONT, TERM, KILL, STOP, PROBE}`; `result` in `{SENT, GONE, DENIED, STRUCTURAL_VIOLATION}` |
| §P1-8.6 replay `ACKED` | "identical to COMPLETED" | the recorded status, detail and handle, with status `REPLAYED`, `fds_redelivered` 0, and no descriptors |
| §P1-9.4 `S-5` structural row | "identical to the ECHILD row" | the full two-ground continuation written out |
| §P1-10.4 rows I-7, I-8 | "identical in every respect to row I-6" | each row's own continuation written out in full |
| §P1-13.3 watchdog descriptors | "as above, with the role's ends at slots 3 and 4" | each is a pipe end whose peer end is held by exactly that watchdog at slots 3 and 4, and by no other process |

**Standard applied.** Internal references of the form "per §P1-10.5" that point
at content written literally elsewhere **inside the same normative region** are
retained and are not treated as placeholders: the content is present and
digested, so the document remains self-contained. What is eliminated is every
reference whose content is *not* in this document, and every construction that
substitutes a pointer for a value the implementer needs.

### 4.5 The eight commissioned loci, literalized

| # | Locus | Literal content now in v1.1 |
|---|---|---|
| 1 | controller/worker descriptors and argv | §P1-6.2 gives all four role classes slot by slot; §P1-7.4 gives argv indices 0–11 common and 12–18+N for controller/worker, with `"3,4"` for `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` and the exact fdmap strings per class |
| 2 | dynamic table state cells | §P1-4.3 carries an explicit state-retention rule: for any process whose adopted set is empty, the wait-set after adoption **is** its initial wait-set and its authority **is** its authority cell. "No cell in this table inherits a value from any other document." |
| 3 | `SigIgn` before/after relation | §P1-7.2 `g-5` states it as an exact 64-bit relation: `SIGIGN_AFTER == SIGIGN_BEFORE & ~(1 << (int(_SIGCHLD) - 1))`, together with `SIGCGT_AFTER == 0`, `SIGBLK_AFTER == 0`, `THREADS_AFTER == 1`, plus a plain-English restatement and the two operative consequences (`SIGPIPE` survives; no `SIGINT` handler remains) |
| 4 | `SPAWNING_MIDDLE` schema and keys | §P1-5.1 gives all four singleton records' schema values and exact key lists; §P1-5.3 gives both in-flight records; §P1-5.2 defines every key's meaning once, including that `cli_pid` and `cli_start_identity` denote the **PCS** |
| 5 | watchdog C1 properties | §P1-9.2 enumerates **thirteen** numbered properties, including the prohibition on `getppid()` inference and the single-detector model; test 63 requires all thirteen |
| 6 | `I-5`…`I-8` | §P1-10.4 writes each row's verdict, capture decision, resulting ownership and continuation in full; no row points at another |
| 7 | §C12 peer reference | replaced by §P1-13, a typed interface: §P1-13.1 names both peer contracts by path and digest; §P1-13.2 lists exactly what P1 reads and its ordering requirement; §P1-13.3 lists the five things P1 provides with their invariants; §P1-13.4 names what P1 neither reads nor writes; §P1-13.5/§P1-13.6 bound P1's obligation at settlement and invalidity; §P1-13.7 declares fifteen areas out of scope |
| 8 | verifier and test statements | §P1-14 and §P1-15 are fully interior to `BODY`; the test matrix is 85 rows with no row deferring to another document |

---

## 5. Defect R3 — verifier input mislabelled — CLOSED

v1 placed the guard-pattern data in a section labelled non-normative while the
verifier read it to decide pass or fail. That is an authority contradiction: a
change to those bytes changes verifier behaviour.

v1.1 resolves it structurally rather than by relabelling prose:

- the patterns occupy their **own delimited region**, `GUARDDATA`, declared
  **"normative verifier data"** in the region table, in §P1-14.0, and in
  §P1-17's own opening sentence;
- they have their own digest, `H_GUARDDATA`, and they enter `H_NORMATIVE` as an
  ordered component;
- guard `G-6` enforces `H_BODY`, `H_GUARDDATA` **and** `H_NORMATIVE` against the
  manifest, so editing a pattern fails the verifier;
- `PROVENANCE` is the only non-normative region and is stated to be read for
  behaviour by nothing;
- the guard target is `REGION(BODY)` alone, so `GUARDDATA` is never a substring
  target of itself.

**A related defect I found in my own draft and fixed.** The first self-fire
scan showed guard `G-4`'s pattern `cannot gain process authority` occurring once
in `BODY` — inside §P1-14.3's own prose *describing the rule that forbids it*.
That is the R1 failure mode in a new dress: a document that documents its own
guards can trip them. Two repairs:

1. §P1-14.3's `G-4` description was reworded to paraphrase ("is unable to
   obtain process authority") without quoting the pattern;
2. a standing constraint `G-10` was added: no pattern string may be reproduced
   in the body region, **including inside the prose describing the rule that
   forbids it**, and there is explicitly **no self-description exemption** —
   an exemption would be an exclusion list, and the guard target admits none.
   Test 76 checks it.

Self-fire verification on the final bytes, all thirty guard patterns searched
against `NORMALIZE(REGION(BODY))` — lowercased, comment markers and
`* _ \``  stripped, whitespace runs collapsed, per §P1-14.2:

```text
TOTAL GUARD FIRES: 0
```

Every one of the thirty patterns returns zero. The guards accept the real
document.

---

## 6. Preserved contract — what v1.1 keeps from the earned P1 semantics

All six signed choices are restated in operative form in §P1-1.3 with no
alteration: A3 same-UID procedural rescope, B1 durable journal/ack/redelivery
with the explicit descriptor-non-redelivery narrowing, C1 dedicated freezer
watchdog with the single-detector trade named as a trade, D1 no idle exit with
the mandatory-resident-PCS cost named, K1 supervisor-mediated transport under a
fixed ceiling, P1 full PCS mediation.

Retained without weakening: the clean-runtime construction (`-I -S -E -P`,
empty environment, object-bound `/proc/self/fd/<N>` interpreter and source,
`os.posix_spawn` with explicit file actions); the descriptor leak proof resting
on `POSIX_SPAWN_DUP2` clearing `FD_CLOEXEC` on the destination; the
`SCM_RIGHTS` transport with `MSG_CMSG_CLOEXEC`, `CMSG_SPACE(12)`, a maximum of
three descriptors, and the non-aborting `B-2` parser that closes exactly the
parsed vector; the nine-opcode handle model and the J1–J6 automaton; the
pre-fork mechanical normalization of child-reaping state; the six-result
`WAIT_ONE` classifier in which only a positive targeted return proves death and
`ECHILD`/`ESRCH` never do; the process-boundary sole-reaper premise; the
`PR_SET_CHILD_SUBREAPER` adoption honesty in §P1-4.2/§P1-4.3; the three-terminal
stage-M construction with the non-returning `B` state; safety `S1`–`S4` claimed
and liveness `L1`–`L5` explicitly not claimed; and the three named residuals,
all permanently non-citable.

**No new numeric constant, scientific value or resource choice was invented.**
`T_SUPERVISOR_POLL_INTERVAL_NS` is 50 000 000, and v1.1 states that 100 000 000
appears in no rule. Every other constant in §P1-2.2 through §P1-2.5 carries the
value already fixed by the signed chain.

**Additions are confined to structure and to closing the three defects:**
`G-8`, `G-9` and `G-10`; §P1-14.0's in-body restatement of the region scheme;
§P1-13's typed peer interface replacing an unnamed reference; and test rows for
the new guards. The test matrix grew from 80 rows to 85 to cover them. No
executable rule of the P1 architecture was changed.

---

## 7. No author choice was required

**No `BLOCKED_...` verdict is emitted.** Literalizing the eight commissioned
loci and the five within-document delegations required only transcribing values
that the signed chain had already fixed. No conflict between signed contracts
surfaced, and I selected no value, no constant and no architecture on Kirill's
behalf.

One near-miss deserves naming, because it is where a choice *could* have hidden.
The preamble that defines the region scheme necessarily sits **outside** all
three regions — a reader must apply it before any region exists — so it is
covered by `H_FILE` but not by `H_BODY`. I did not resolve that by silently
picking an authority level. v1.1 states the situation explicitly in the
preamble, restates the operative rule inside `BODY` as §P1-14.0 so it is also
covered by `H_BODY`, and adds `G-9` so a verifier's own constants must match.
Both statements are present and must agree; if a reviewer judges that
arrangement insufficient, the remedy is a signed decision, not an author one.

---

## 8. Author audit — what a reviewer should attack first

I am not a reviewer, and the items below are where I judge my own work weakest.
This list is offered as attack surface, not as mitigation.

1. **The zeros in §4.3 are substring counts, not a semantic proof.** A
   placeholder phrased in words I did not search for would survive. The domain
   and method are stated exactly so a reviewer can re-run them with a different
   pattern set — which is the point of showing the commands.
2. **`G-10` is authoring discipline, not a mechanism.** The verifier will catch
   a pattern that reappears in `BODY`, but only for patterns already in
   `GUARDDATA`. A *new* overclaim phrased in new words is caught by nothing but
   review. `G-6` and `G-7` make such an edit detectable, not impossible.
3. **The preamble/`H_BODY` split of §7** is the structurally novel part of v1.1
   and has had the least adversarial scrutiny.
4. **§P1-13's peer interface is my reading of the boundary.** I derived what P1
   reads and provides from the signed chain; a Y-line reviewer holding the peer
   contracts should confirm that §P1-13.2's read set, §P1-13.3's five outputs
   and §P1-13.7's out-of-scope list actually partition the boundary with no gap
   and no overlap.
5. **Test 33 and `TI-1`** rest on the claim that `S-24a` and `S-24b` together
   cover the topology invariant that neither covers alone. That decomposition is
   mine and is worth testing directly.
6. **The `_recvmsg` handler.** v1.1 states plainly what it does **not** claim:
   that no hook, finalizer or same-process callback can run between the C call's
   failure and the single `_exit_` statement. The residual is named in §P1-12.4
   item 3 and lies inside A3. A reviewer should confirm the document nowhere
   quietly assumes otherwise.
7. **The X-line finding on `S-25`** was closed in v1 by splitting it into
   `S-24a` and `S-24b` plus test 33; a reviewer should confirm the split is
   genuinely decidable statically and does not merely relocate the undecidable
   part.
8. **The Y-line blocker** on the prior round was an access blocker, not a
   merits finding: the Y prompt had prohibited every read and hash mechanism.
   This round's constraints permit read-only file commands and SHA-256, so a Y
   review can now recompute the four digests and read the full chain.

---

## 9. Scope and negative space

This closure creates nothing executable. It authorizes no implementation,
commit, host change, verifier edit, manifest write, process, socket, pipe,
fork, exec, signal, wait or `prctl` call, no supervisor, PCS, controller,
worker or watchdog, no capability, world, learner, entropy, capacity artifact,
custody disposition, result manifest, quarantine record, promoted object,
freeze witness, spend, datum, outcome, Proof or claim movement. It predicts no
qualification and no comparison outcome.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not signable** and
was not made signable. v1.1's status is
`CANDIDATE_FOR_INDEPENDENT_X_AND_Y_REVIEW_NOT_ACCEPTED`.

Only read-only commands were executed this round: `grep`, `sed`, `wc`, `sort`,
`uniq`, `tr` and `sha256sum`, against repository files and against extracted
copies in the session scratchpad. No repository file other than the two
deliverables was created, modified or removed. No test, behavioural probe or
process-control experiment was run.

---

## 10. Verdict

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_1_XY_REVIEW
```

Meaning, precisely and only: the three commissioned defects are closed by
mechanically verified evidence shown above — R1 by unique-cardinality sentinels
defined by byte construction, with all six occurring exactly once and every
previously-truncated section interior to the digested region; R2 by a
zero-result byte-level audit over a stated 2 318-line, 138 527-byte domain, with
the one surviving `identical to` classified openly; R3 by giving guard-pattern
data its own normative region, its own digest and its own enforcement, plus the
`G-4` self-fire repair and `G-10` — and no new author choice was required.

It does **not** mean the composite is correct, complete or safe. That
determination belongs to the independent X-line and Y-line reviewers, who
should recompute all four digests before reading, treat every sentence of this
closure as untrusted, and begin with §8.
