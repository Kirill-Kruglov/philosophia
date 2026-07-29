REVISE_OFFICINA_SUPERVISOR_V2_1_1

# Independent clean-context Y-line review

Date: 2026-07-30

Reviewer line: Y

## Review base, method, and recomputed hashes

Review base: commit
`30e02102a9bf697f1cb9465900bbbf1401c8efa0`, verified to descend from
required commit `9a60ca5`.

I read every artifact named in the review request in full. I treated
`reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md` as
an untrusted author claim and derived the result below from the contract
and signature bytes. Its SHA-256 is recorded only for custody; none of
its conclusions is review evidence.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
c97f98a0c0050f28e0849dc1782f9a403b4c99f58ee64636215dab114a47b1cd  reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md
cf4fab454e27f0c4c2ad6a7583c70a79a7aff8ed1711bf279c13683b85f74c60  reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
526a0ffeb95e233705aad413a13dae5487d91bc9503c8b7d3d2cbcdb4b7df927  reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md
```

The v2.1.1 digest exactly matches the committed expected value
`ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635`.

This was a static contract review. I ran no repository code, test, probe,
Officina command, supervisor, controller, worker, watchdog, endpoint, or
smoke. Read-only file-display, Git, and SHA-256 utilities were used. I
modified no existing file and created only this review.

## Answer

No. v2.1.1 closes most of the v2.1 findings, including the central
occurrence-allocation, descendant-head, takeover-order, renewal,
admission-release, no-replenishment, status/EOF, and A3-leakage repairs.
It nevertheless does not yet implement the signed selections literally
or totalize every required cut:

1. the purported author custody-disposition identifier is circular and
   cannot be constructed;
2. its absence proof can release capacity while the same operation's
   custody remains at the other side of the promotion rename;
3. the supervisor grandchild can hold `SPAWN.lock` while hanging before
   the first durable identity record;
4. K1 says each byte is hashed once, while v2.1.1 expressly hashes it
   inline and then hashes it again;
5. rejected current-generation watchdog evidence cannot always be
   replaced at its occupied no-replace witness path, and the required
   `UNKNOWN` member count is inconsistent with a later proved-quiescent
   tree;
6. descriptor remapping is not total when the source fds overlap or
   cross fds 3 and 4;
7. ordinary-effect acknowledgement has an overlapping wrong-hash rule,
   and the stated GC epoch can make acknowledged records permanently
   non-GC-able.

These are contract defects, not implementation findings. They are
bounded repairs. They reopen no scientific or resource value and require
no genuinely new author-choice cell, but they require repaired bytes and
another independent X/Y check.

## One-to-one disposition of the prior Sol findings

| Prior finding | v2.1.1 disposition | Independent result |
|---|---|---|
| Sol C1: total B1 allocation, STATUS, ack, tombstone | **Not fully closed** | Explicit `NEW`/`RETRY`, supervisor allocation, journaled observation STATUS, contiguous prefix, and post-GC classification are substantively correct (§Z1.1–§Z1.9). The wrong-hash acknowledgement overlap and impossible-later GC epoch below remain. |
| Sol C2: descendant-aware reducer and validity-first takeover | **Closed** | §Z2.1–§Z2.5 admits legitimate descendant heads, distinguishes legal prefixes from conflicting suffixes, and performs old-generation freeze/settlement before non-behavioral reduction. |
| Sol C3: constructible and total spawn/bootstrap | **Not fully closed** | The two hash domains and fixed adapter root are constructible (§Z3.1–§Z3.4), but §Z3.5 records the grandchild only after descriptor scrubbing and §Z3.3 leaves colliding `dup2` remaps undefined. |
| Sol C4: `OPERATION_ADMIT` success before release | **Closed** | `RUNNING.json` precedes `SIGCONT`, which precedes `committed.json` and `reply.json`; after supervisor loss the worker is settled and never resumed (§Z5.1–§Z5.2). |
| Sol C5: K1 settlement replenishment | **Closed numerically, not closed as a complete K1 authority** | §Z6.1–§Z6.3 and §Z6.7 retain `bytes_reserved` through every named terminal and rename. The only release authority is circular and its absence proof is incomplete. |
| Sol M1: closed author disposition authority | **Not closed** | §Z6.4–§Z6.6 supplies schemas and checks, but the authority cannot be constructed and does not prove all custody absent. |
| Sol M2: false timing secrecy | **Closed** | §Z8.1 limits the official guarantee to fixed reply bytes and names timing, backpressure, path, metadata, and scheduling observations as procedural and non-citable. |
| Sol M3: strict-positive equality cut | **Closed** | §Z4.4 re-proves quiescence while sampling for strict progress and falls to `UNKNOWN` if none is established. |

## New findings

### Critical

#### C1. The author-disposition identifier is self-referential and unconstructible

Loci: v2.1.1 §Z6.4, especially lines 1203–1206 and 1234–1242.

The contract defines:

```text
disposition_id = SHA-256({
  activation_record_sha256, operation_id, author_decision_sha256
})
```

It then requires the tracked author-decision file's SHA-256 to equal
`author_decision_sha256` and requires that same file to contain
`disposition_id` as an exact standalone line. Thus the file bytes contain
an identifier derived from the hash of those same bytes. This is the same
fixed-point defect that §Z3.1 correctly removed from `spawn_intent_id`.
Calling the preimage “three-field” does not remove the dependency cycle.
No ordinary construction can produce the authority, so the one K1 release
route is not executable.

Smallest bounded repair: derive `disposition_id` without the decision
file's content hash, for example from
`{activation_record_sha256, operation_id, canonical_author_decision_path}`,
then require the decision file to contain that already-computable id and
bind its resulting SHA-256 from the disposition object. Alternatively,
remove `disposition_id` from the signed file. Keep all bindings
one-directional and state both hash domains explicitly.

#### C2. The custody-absence proof checks one name, not the complete custody set

Loci: carried §W6.1 in v2.1 lines 1263–1265; v2.1.1 §Z6.2 line 1173;
§Z6.4–§Z6.5, especially verifier conjuncts 7 and 10.

The immutable `<op>.settled.json` is written before
`os.replace(out/, T_PROMOTED/<op>/)` and contains one `custody_root`.
Promotion then changes custody between the source and destination, but
there is no post-rename immutable custody-transition artifact and the
settled record is no-replace. The disposition verifier proves absence
only at the one named `custody_root`.

Either possible value is unsafe:

- if `custody_root` is the future promoted destination, a crash before
  rename leaves real custody in `operations/<op>/out/` while the named
  destination is absent;
- if it is the source `out/`, a completed rename makes the source absent
  while real custody remains under `runtime/T_PROMOTED/<op>/`.

In either case a disposition can satisfy conjunct 10 and install
`.disposed.json` while custody for that operation still exists. This
violates signed K1's sole release condition.

Smallest bounded repair: have the same-lock verifier prove absence from
**every canonical custody location for the operation**—at least the
operation `out/`, the quarantine root, and `T_PROMOTED/<op>/`—and reject
any other operation-bound custody record or directory. Alternatively add
a no-replace post-rename custody-transition artifact and still prove
absence from both predecessor and successor locations. Do not rely on one
mutable concept stored in a pre-rename no-replace record.

#### C3. Pre-identity supervisor recovery still has an unrecorded lock-holder cut

Locus: v2.1.1 §Z3.5 lines 795–840.

The grandchild's ordered “FIRST actions” are:

```text
a. scrub inherited descriptors and redirect stdio
b. install SPAWNING_CHILD.json
c. report on the bootstrap pipe
```

If it hangs during step a, it already holds the fork-shared
`SPAWN.lock`, but neither `SPAWNING_CHILD.json` nor the bootstrap line
exists. The CLI timeout says to kill by the **recorded** pid/start
identity, and the stuck-holder route acts only when
`SPAWNING_CHILD.json` exists. With no record, later clients return
`BOOTSTRAP` without killing the holder, so the lock and D1 can remain
wedged indefinitely.

Smallest bounded repair: make a kernel-verifiable identity binding the
literal first post-fork action before any descriptor enumeration or
stdio work. A safe construction is for the middle child/CLI to retain a
sealed parent-report channel and record the grandchild pid, pgid, and
start identity immediately after the second fork, with a bounded parent
wait and kill route. Every cut after the grandchild exists must leave
either a killable record or a process whose death releases the lock.

#### C4. v2.1.1 hashes output bytes twice contrary to literal signed K1

Loci: output-capacity signature lines 22–24; v2.1.1 §Z8.3 lines
1443–1456.

The signed selection says the supervisor “writes and hashes each byte
once.” v2.1.1 retains an inline streaming SHA-256 during the write pass
and then re-reads the file and recomputes `content_sha256` in a second
verification pass. Each byte is therefore hashed twice. The second pass
is bounded and usefully detects equal-size substitution, but it is not a
literal implementation of the selected provider.

Smallest bounded repair: write each byte once without computing the
content hash in that pass, retain the descriptors and byte counts, and
compute the sole content hash in the bounded pre-settlement verification
pass. This preserves the signed “writes once, hashes once” rule and the
equal-size/inode-substitution defense without reopening K1.

### Major

#### M1. Rejected current-generation freeze evidence has no writable replacement path

Loci: v2.1.1 §Z4.5–§Z4.6, especially lines 1025–1038 and 1061–1066.

`witness_id` depends only on
`{supervisor_generation_sha256, process_id, table_seq}` and its file is
atomic no-replace. When a current-generation file at that path is
malformed or unverifiable, §Z4.6 says the supervisor writes “its own
replacement witness” for the same generation/process/table. That
recomputes the same `witness_id`, so the occupied no-replace path prevents
the required write.

The `UNKNOWN` schema is also inconsistent at this cut: conjunct 9
requires `unresolved_member_count >= 1`, while the replacement must carry
“the member count it observes itself.” A later supervisor freeze can
prove all members stopped/dead and observe zero unresolved members while
the historical timestamp is still unknowable.

Smallest bounded repair: define a separate deterministic rejection/
supervisor-fallback witness id or path bound to the rejected file's
SHA-256, and distinguish `unknown_reason` from the current unresolved
member count. Permit `UNKNOWN` with zero currently unresolved members
when the missing fact is the historical freeze instant. The original
object remains non-evidence and is never overwritten.

#### M2. The adapter's fd remap is not total on overlapping descriptors

Locus: v2.1.1 §Z3.3 lines 734–744.

The adapter says to parse `(low, high)` and `dup2` them to `(3, 4)`, but
does not state a collision-safe algorithm. If `(low, high) = (4, 3)`,
executing `dup2(low, 3)` first destroys the original fd 3 before it is
copied to fd 4; both destinations can then refer to the same pipe.
Related overlaps such as one source already being 3 or 4 also require a
pinned order or temporary duplicate.

Smallest bounded repair: specify a four-case, collision-safe remap or
first duplicate both sources to fresh `O_CLOEXEC` temporaries outside
`{3,4}`, then `dup2` the temporaries to 3 and 4 and close them. Verify
pipe type and direction/role after the remap.

#### M3. A wrong prior-reply hash has two incompatible acknowledgement continuations

Locus: v2.1.1 §Z1.7 lines 380–398.

For a successor occurrence carrying a wrong non-null prior hash, the
`SUCCESSOR_OCCURRENCE` row says “any other value acknowledges nothing.”
The `CLIENT_ECHO` row says **any frame** carrying a mismatching hash is
`INVALID/REPLAY_BYTES` with no state movement. The same frame therefore
has two continuations: admit without acknowledgement, or reject as
invalid.

Smallest bounded repair: pin priority and one result. A clean total rule
is: `null` means no ordinary acknowledgement; an exact hash acknowledges
the named/highest occurrence according to the closed source rule; a
non-null mismatch is `INVALID/REPLAY_BYTES` before allocation or other
state movement.

#### M4. GC is tied to an ack-install epoch that may precede archival

Locus: v2.1.1 §Z1.9 lines 442–452.

The prefix correctly advances in the lock epoch that installs `ack.json`.
The text also permits GC only “in the same lock epoch that installed the
ack that advanced the prefix,” while requiring the owning transition's
archival commit already to exist. If acknowledgement precedes archival,
the ack is no-replace and cannot be installed again; when archival later
becomes durable, no legal epoch remains in which GC can occur.
Observation-form `OPERATION_STATUS` also has no clearly named owning
archival transition. Thus the claimed polling-independent growth bound is
not executable even though replay safety itself remains conservative.

Smallest bounded repair: keep prefix advance atomic with ack install, but
permit GC in any later locked epoch once the immutable ack, contiguous
prefix, and applicable archival predicate are all verified. State the
archival predicate for empty-effect observation plans explicitly
(including whether it is vacuously satisfied).

#### M5. The tracked author-decision file is not content-closed

Loci: v2.1.1 §Z6.4 lines 1234–1242 and §Z6.5 conjuncts 8–9.

The disposition JSON forbids result, learner, candidate, and Q/C values,
but the tracked author-decision Markdown is required only to contain
three standalone lines and may contain arbitrary additional text. It can
therefore cite a result hash, candidate identity, or judgement about
output content while still authorizing release. The verifier's recursive
prohibition applies to values “in the record,” not to all bytes of the
author-decision file. This leaves scientific/outcome-responsive custody
selection outside the closed schema.

Smallest bounded repair: make the tracked decision file exact and
canonical—fixed heading/schema plus exactly the token, operation id, and
disposition id, with no additional content—or apply an exact parser and
the same recursive prohibited-value/field checks to the entire signed
authority. Enumerate the operation-bound identifiers against which the
check runs.

### Minor

#### m1. The absent-scope tombstone default is implicit

Locus: v2.1.1 §Z1.3.

`next(scope)` dereferences
`tombstone(scope).next_occurrence_index` even for a never-seen scope,
while also taking `max(..., 1)`. The intended absent value is plainly 1,
but a two-implementer contract should state
`tombstone_next(absent) := 1` and
`acknowledged_prefix(absent) := 0`.

Smallest bounded repair: add those two defaults.

## Mandatory B1 traces

Legend: `N(i)` is explicit `NEW` naming index `i`; `R(i)` is explicit
`RETRY` of the allocated handle. “Cached” means the transport-free
effect reply is byte-identical and is rewrapped in the current transport
envelope. These results are derived from §Z1 rather than copied from the
author's §Z1.10 examples.

| Trace | `CLAIM` | `START` | `HEARTBEAT` | `CLOSE` | `PAUSE` | `RESUME` | `OPERATION_ADMIT` | `OPERATION_STATUS` |
|---|---|---|---|---|---|---|---|---|
| Lost request before `accepted.json` | Re-send `N(i)`; if nothing landed, allocate one sequence/claim. `R(i)` before allocation is refused, never creates one. | Re-send `N(i)`; one start event/lease. | Re-send `N(i)`; one captured reading/charge. | Re-send `N(i)`; one close automaton. | Re-send `N(i)`; one checkpoint/pause. | Re-send `N(i)`; one selected checkpoint automaton. | Re-send `N(i)`; one reservation/op/cursor/worker. | Re-send `N(i)`; one cached observation or ack effect. |
| Lost reply after `reply.json` | `R(i)` returns cached process id/claim hash; no second claim. | `R(i)` returns cached lease; no second start. | `R(i)` returns cached charge and cumulative value; no fresh meter read. | `R(i)` returns cached record/stopped hashes. | `R(i)` returns cached pause/checkpoint hashes. | `R(i)` returns cached phase/head. | `R(i)` returns cached operation id/bound; no second reservation or worker. | `R(i)` returns the exact cached phase and token bytes, even after later promotion/ack. |
| Client crash after observing reply, before local `.done` | `.done` is irrelevant. `R(i)` is old reply; `N(next)` is a distinct new claim. | `R(i)` is old reply; `N(next)` is a separately evaluated start and normally refuses against started state. | `R(i)` is old reply; `N(next)` is a new heartbeat and new disjoint interval. | `R(i)` remains redeliverable; `N(next)` is a new post-close refusal. | `R(i)` redelivers; `N(next)` evaluates G3. | `R(i)` redelivers; `N(next)` re-evaluates state. | `R(i)` redelivers; `N(next)` is a distinct operation subject to stream/capacity rules. | `R(i)` is the old observation; `N(next)` is a new poll of current state. |
| Generation change | Completed reply is cached/current-wrapped. Accepted-only behavioral spawn cannot continue; it closes by takeover route. | Completed reply is cached/current-wrapped; an open behavioral start is settled before reduction and never resumed. | Completed reply is cached/current-wrapped; an open renewal cannot continue behavior. | Recorded non-behavioral close/archival completion may finish; no new live charge is invented. | Recorded non-behavioral artifact/cache work only. | Recorded non-behavioral automaton work only; no behavior starts. | Completed reply is cached/current-wrapped only if release occurred; an open worker is frozen/settled, never resumed. | Observation/ack cache work is non-behavioral and may complete; `R(i)` remains byte-stable. |
| Effect exists before `committed.json` | Same generation follows intent/child/claim locators once; after loss, no respawn and the prior live set is settled first. | Same generation follows start event → lease → publication/ack → release; after loss no lease/release continuation. | Uses recorded reading: charge → successor lease → table/ack; after loss no renewal. | Signed close order resumes at first missing locator, archival last; no second charge. | Signed pause order resumes; impossible condition takes its closed failure route. | Same checkpoint and first-event locators; never chooses another checkpoint. | Same generation follows capacity → bound → admission → intent/binding → `RUNNING` → `SIGCONT` → commit/reply; after loss invalid settlement dominates. | Observation writes empty-tuple commit/reply from its captured observation; ack form installs the one delivery ack. |
| Ack + GC + old retry | `R(i)` is `ALREADY_ACKNOWLEDGED`; no claim. | Same; no start. | Same; no charge. | Same, but only after hash-proving client/successor ack; own terminal cannot self-ack. | Same own-terminal restriction. | Same; no automaton rerun. | Same; no op/reservation/worker. | Same; no observation replay after its owed bytes were acknowledged. |
| Concurrent same-scope clients | Two distinct `N(next)` allocations serialize; loser re-anchors and creates a distinct claim. Only common `R(i)` collapses. | Distinct occurrences; signed live-state rules usually refuse the second. | Distinct occurrences and disjoint cursor intervals; no collapse. | Distinct occurrences; only one can close, later one is cached refusal. | Distinct occurrences; later state decides second. | Distinct occurrences; later state decides second. | Distinct occurrences; stream exclusivity/capacity decides second. | Distinct polls; common `R(i)` is the same cached poll. The wrong-hash ack overlap in M3 prevents a fully total ack trace. |
| Repeated STATUS / repeated same-scope intent | Each `N` is a distinct claim; each `R` is one claim. | Each `N` is separately evaluated; `R` never restarts. | Accepted `N`s are rate-limited and charge disjoint cursor spans; refused `BUSY` has empty tuples. | Repeated `N` after terminal produces distinct cached refusals. | Repeated `N` in paused state produces signed refusals. | Repeated `N` re-evaluates signed phase. | Repeated `N` creates a distinct bounded op or refusal. | Every poll is `N(i+1)` and cached; `R(i)` remains stable across promotion and delivery acknowledgement. |

The effect semantics in this table are exactly-once and generation-total
apart from M3/M4's acknowledgement/GC defects. `NEW` never means retry by
inference, and `RETRY(handle)` never allocates.

## Tombstone and allocator arithmetic

Let `J(S)` be the set of occurrence indexes with a durable
`accepted.json`; let `T.next` and `T.prefix` be the two monotone
tombstone integers. With the minor absent-default repair made explicit,
the intended arithmetic is:

```text
next(S) = max(T.next or 1, 1 + max(J(S)) or 1, 1)
GC-eligible(i) only if i <= T.prefix, ack(i) is durable,
and the owning archival predicate is satisfied.
```

Independent cuts:

| Attack/cut | Derived result |
|---|---|
| Arbitrary deletion of all client intent and `.done` files | No supervisor state changes. A client can send `N(1)`, receive `OCCURRENCE_INDEX` plus authoritative `next`, and re-anchor. No reuse or wedge. |
| Two concurrent allocations of `N(i)` | One lock epoch installs `accepted(i)` and advances `T.next`; another allocator cannot install the same no-replace file. A foreign allocator is refused and re-anchors. |
| Crash before `accepted(i)` | Nothing allocated; `N(i)` may allocate. |
| Crash after `accepted(i)`, before tombstone advance | Journal maximum makes `next >= i+1`; repair advances `T.next`; `i` is never reused. |
| Missing `.done` | No effect; it is convenience state only. |
| Successor with null prior-reply hash | Admits no acknowledgement. |
| Successor with exact prior-reply hash | Installs one ack and advances the largest contiguous prefix. |
| Successor with wrong non-null prior hash | **Defective:** §Z1.7 says both “acknowledges nothing” and `INVALID/REPLAY_BYTES`; M3 must select one. |
| Ack of occurrence 3 while 2 is unacked | `ack(3)` may exist, but `T.prefix` cannot pass 1. Neither 2 nor 3 is prefix-GC-eligible. |
| Ack of 2 later | The same lock epoch may advance the prefix through 3. |
| Ack before owning archival commit | Replay remains safe, but §Z1.9's same-ack-epoch GC wording makes later GC impossible; M4 must permit a later verified GC epoch. |
| GC at/below prefix | Per-key phase files may disappear; the tombstone never does. |
| Post-GC `R(i)` with `i <= prefix` | `ALREADY_ACKNOWLEDGED`, no effect, using only the incoming derivation and the two tombstone integers. No unavailable old reply hash is consulted. |
| Directory missing with `prefix < i < next` | Impossible under compliant prefix-only GC; record-first invalidity is appropriate for the corrupted layout. |
| `R(i)` with `i >= next` and no journal | Never allocated; non-retryable `OCCURRENCE_INDEX`, no effect. |

## Reducer and takeover trace

| State | Chain test | Continuation |
|---|---|---|
| Committed/replied plan, current head is any legitimate descendant | Recorded post-head is in the raw durable chain; declared events are ordered; current durable head follows them | Accept and serve/write the cached reply. Ordinary later history does **not** become G5. |
| Accepted-only, no conflicting suffix, no locator | Pre-head is in chain; declared present events form an ordered legal prefix | Resume at the first locator, subject to the generation behavior cut. |
| Accepted-only, some declared locators/events form the exact legal prefix | Same | Resume only the missing ordered locators. |
| Conflicting suffix, no plan locator present | Conflict is ordinary later state and the plan never started | Cache `SUPERSEDED_PLAN`; no invalidity. |
| Conflicting suffix, some plan locator present | The held-lock order should make this impossible | Record-first invalidity naming both plan and intervening entry. |
| Pre-head or committed post-head absent from the raw chain | Impossible durable layout | Record-first invalidity. |
| Supervisor loss with live old-generation work | Phase 2A reconstructs capacity, identifies and freezes/kills old identities, writes/validates witnesses, settles the complete affected live set through the signed invalid batch, archives before resolution, and resolves intents | Only then phase 2B performs non-behavioral record/archive/cache work. No `Popen`, `SIGCONT`, lease install/renewal, admission, worker release, or behavior-presupposing charge crosses takeover. |

The reducer repair itself passes the required legitimacy and
validity-first traces. The C1 witness-path defect in M1 affects how one
required freeze fact is durably represented, not the takeover ordering.

## Spawn/bootstrap construction and cuts

### Hash dependency check

No concrete spawn instance is supplied, so no instance digest can be
numerically evaluated. The two domains can nevertheless be independently
recomputed as a dependency graph:

```text
argv_template_sha256
  = SHA-256(canonical JSON array(
      adapter fields, literal "<SPAWN_INTENT_ID>",
      literal "<CTRL_FDS>", "--", target argv))

spawn_intent_id
  = SHA-256(canonical {
      supervisor_generation_sha256, role, process_sequence,
      argv_template_sha256, created_utc
    })

complete_argv_sha256
  = SHA-256(canonical JSON array(
      the same template after substituting spawn_intent_id
      and the actual low/high descriptors))
```

The first two hashes contain no derived marker or descriptor number, so
the construction is acyclic. In-generation respawn retains the same
template/id while allowing new descriptor numbers in the separately
hashed complete argv. Cross-generation respawn is forbidden.

### Role and crash trace

| Cut/role | Required construction | Result |
|---|---|---|
| CLI singleton acquisition | Bounded `LOCK_EX|LOCK_NB`; holds through live identity | Correct after a record exists. |
| Grandchild before any post-fork action | Must already be discoverable or leave no held lock | **Not total:** it exists with the lock before any record. |
| Grandchild descriptor scrub | Must not precede the first killable identity | **Fails C3:** scrub is step a; record/report are b/c. |
| Grandchild after `SPAWNING_CHILD` and bootstrap line | CLI verifies pid/start identity/pgid; timeout kill is identity-safe | Correct. |
| Watchdog fork | In-process, no argv/spawn intent; exact fork-child record; only sealed update/ack fds | Correct after parent writes the record. It has no capability or runtime lock. |
| Controller/worker adapter exec | Fixed module root at indexes 0–12; marker at fixed index; target after `--`; target cannot spoof the prefix under compliant behavior | Correct. |
| Adapter target preflight | Target exists, regular, executable before intent/again before stop | Correct. |
| Adapter fd normalization | Per-role meaning pinned at 3/4 | **Not total on overlapping/crossed source fds (M2).** |
| Adapter self-stop | No signal disposition; stop before target exec; no capability before `SIGCONT` | Correct. |
| PID reuse | Every kill using a record checks start identity; mismatch is not killed | Correct. |
| Stale unbound controller/worker | Fixed-index `/proc/cmdline` marker; kill group and prove dead | Correct for execing children. |
| Stale grandchild/watchdog | Record-based, not cmdline-based | Correct only after their respective records exist. |
| Watchdog identity cut | Current-generation `WATCHDOG_CHILD.json`, parent identity, pipe type, and ack history | Correct as a raw freezer identity; M1 affects rejected witness persistence. |

Thus `spawn_intent_id` is now computable and the adapter is the executable
root, but spawn/bootstrap is not total at the earliest grandchild cut.

## C1 evidence-authority checklist

| Required item | Result |
|---|---|
| Publish after every successful locked claim-start, renew, remove | Yes, §Z4.1; four effect plans bind `watchdog_table_seq`. |
| Ack exact table before corresponding behavior | Yes. `START`, renewal success, and admission cannot use an unacked extension. |
| Old deadline remains authoritative until ack | Yes. No unacknowledged update extends behavior. |
| Drain before freeze | Yes. At `now >= deadline`, the watchdog drains/re-reads and adopts a newer observable table before freezing. |
| Ack absence | Re-publish; at 60 s take the dead-watchdog route and cache `WATCHDOG_UNACKED` with the artifacts actually durable. No later renewal is fabricated. |
| Stale-generation filename collision | Generation/process/table are in `witness_id`; ordinary cross-generation collision is removed. |
| Strict-positive overrun | Yes. Re-prove while sampling; equality/nonprogress becomes `UNKNOWN`, never a valid zero-overrun terminal. |
| Process-tree versus backend fact | Honest. `PROVED` is only a reachable process-tree fact; backend synchronization remains settlement work. |
| Supervisor validation | Ten conjuncts bind schema, name, generation, table/deadline, lease/claim identity, killer, arithmetic, and present quiescence. |
| Malformed/planted current witness | **Not total:** fallback wants the occupied same `witness_id`, and `UNKNOWN` count can conflict with zero current unresolved members (M1). |
| Missing/lost evidence | Must degrade to supervisor `UNKNOWN`; the route is correct in policy but needs M1's writable schema/path. |
| Watchdog settlement authority | None. It writes control-plane witness bytes only; it holds no runtime lock/capability and appends no ledger entry. |
| Valid-terminal selection | Impossible: `PROVED` positive and `UNKNOWN` both route to the signed invalid all-live settlement; close/resource stop/E1/E3/pause/review terminals are forbidden. |
| Sole authority | The supervisor alone validates evidence and settles. No watchdog fact is a second runtime authority. |

## `OPERATION_ADMIT` ordering at every cut

The ordered locators are:

```text
accepted
→ capacity reservation
→ bound
→ admission
→ worker spawn intent
→ pipes + adapter Popen + stopped binding
→ RUNNING.json
→ SIGCONT attempt
→ committed
→ reply(ADMITTED)
```

| Cut | Same generation | After supervisor loss |
|---|---|---|
| Before `accepted` | Nothing allocated; `N(i)` may allocate once. | Nothing to reduce. |
| `accepted` to capacity/bound/admission/intent | Create only the missing no-replace locators. | Phase 2A resolves any old identity/custody; no behavioral continuation. |
| Intent/binding incomplete | Discover by fixed marker, kill/prove dead if needed, then same-generation respawn under the same template/id. | Kill/prove dead; never respawn. |
| Worker stopped/bound, no `RUNNING` | Same generation can continue to `RUNNING`. | Freeze/settle; never release. |
| `RUNNING`, before `SIGCONT` | Verify exact live stopped identity; attempt `SIGCONT`, then commit/cache. | Freeze/settle invalid; never `SIGCONT`. |
| After `SIGCONT`, before committed | Commit/cache from recorded identities if the same supervisor remains. | Phase 2A first settles old work; phase 2B caches only the resulting closed terminal. |
| Committed, no reply | Write reply from committed terminal. | Non-behavioral cache completion only after settlement. |
| Reply present, `RUNNING` present | Probe release locator/identity before serving. | Never release old work. |
| Reply present, `RUNNING` absent | Impossible layout → record-first invalidity. | Same. |

The v2.1 stranded-worker defect is closed. No cached positive
`ADMITTED` precedes the same-generation release attempt.

## K1 custody and capacity trace

### Arithmetic

For any operation with `CAPACITY/<op>.json` and without a valid
`.disposed.json`:

```text
contribution(op) = bytes_reserved
```

`actual_bytes` never appears in the admission total. Unrecorded custody
counts the full 268,435,456-byte ceiling. Unreadable custody refuses
admission rather than assuming zero.

| Transition/attack | Accounted result |
|---|---|
| Reservation → `ADMITTED` | Add exactly `bytes_reserved`. |
| `ADMITTED` → `RUNNING` | Still `bytes_reserved`. |
| Live → pending settlement | Still `bytes_reserved`. |
| Successful settlement | Still `bytes_reserved`; `actual_bytes` is diagnostic. |
| Failure/quarantine | Still `bytes_reserved`. |
| Rename to promoted custody | Still `bytes_reserved`. |
| Promotion | Still `bytes_reserved`. |
| Delivery acknowledgement | Still `bytes_reserved`. |
| Unused reservation / one-byte result | No reduction; still the full reservation. |
| Supervisor crash and reconstruction | Reservation record dominates; no remeasurement downward. |
| Custody directory without a capacity record | Full 268,435,456 is conservatively charged. |
| Stale activation disposition | Refuse, release zero. |
| Wrong terminal / wrong parent hash | Refuse, release zero. |
| Substituted operation/reservation/actual-byte facts | Refuse, release zero. |
| Forged token or untracked/hash-mismatched decision file | Refuse under the stated checks, subject to A3 procedural forgery. |
| Partial disposition install crash | No `.disposed` means full reservation remains; retry may reverify. |
| Replayed/second disposition | Releases zero; contradiction routes to invalidity. |
| Custody present at the **named** root | Absence check refuses. |
| Custody present at the alternate pre/post-promotion root | **Can pass as written (C2); the proof is not complete.** |
| Construct author disposition and signature | **Impossible as written because of C1's hash cycle.** |

The reservation-to-delivery accounting is literal K1: settlement,
failure, rename, promotion, acknowledgement, and unused reservation
replenish nothing. The sole release route nevertheless fails
constructibility and complete-custody absence, so K1 is not confirmed.

## Worker status, EOF, and output-integrity matrix

| Status/output cut | Route |
|---|---|
| Valid `COMPLETED`, one or more frames, counts match, group dead | Verification pass, settlement, promotion. |
| Valid `COMPLETED`, zero frames/zero bytes, group dead | Canonical empty result `SHA-256(b"[]")`, empty path list, `actual_bytes = 0`; reservation retained. |
| Valid `FAILED` | `WORKER_FAILED` quarantine and signed invalid route. |
| No status frame | `WORKER_FAILED`, public cause `PROCESS`. |
| Malformed/oversize/second/wrong-operation status | `TRANSPORT` quarantine. |
| Status count/byte mismatch | `TRANSPORT` quarantine. |
| EOF mid-header or mid-content | `PARTIAL_OUTPUT`; written prefix remains conservatively accounted by reservation. |
| Output status present but output pipe remains open at death | `TRANSPORT`. |
| Header/path/count/content bound violation | Kill group, prove death, quarantine; no excess frame bytes written. |
| Pipe full | Backpressure; deadline remains under C1. |
| `ENOSPC`/quota/write failure | `FILESYSTEM` invalidity; no deletion to make room. |
| Equal-size in-place content substitution | Detected by the verification re-read/hash comparison. |
| Inode substitution at the file name | Detected by `(st_dev, st_ino)` comparison with the held read descriptor. |
| Link substitution | `st_nlink == 1` required. |
| Crash in verification | `SUPERVISOR_CRASH`, full reservation retained, no resume/respawn. |
| Same-name `out/` directory swap after verification, before rename | Explicit A3 procedural residual; not mechanically closed or Q/C-citable. |
| Reply latency/backpressure/path/timing/metadata observation | Explicit A3 procedural residual; fixed official `PENDING` bytes only. |
| Hash-count literal | **Fails C4:** inline hash plus verification hash means two hashes per byte. |

The matrix is closed with respect to status and EOF. Its remaining
directory/timing/metadata residuals are honestly named. The extra hash
pass must be reconciled with literal K1 as specified in C4.

## No-regression table

| Surface | Result |
|---|---|
| A3 | **Preserved.** Same-UID deliberate interference remains procedural; fixed response bytes are not promoted into timing or metadata secrecy; residuals are non-citable for Q/C. |
| B1 | **Substantially repaired but not confirmable.** All eight commands, including observation STATUS, have occurrence-stable journal replies. M3/M4 leave acknowledgement/GC non-total. |
| C1 | **Policy preserved.** The watchdog remains freezer/witness only and can select no terminal. M1 leaves one evidence-fallback persistence cut non-executable. |
| D1 | **No idle exit preserved**, but C3 leaves a pre-record lock-holder wedge, so the total lifetime/singleton construction is not confirmed. |
| K1 | **No-replenishment arithmetic preserved.** C1/C2 make the sole release authority non-executable/unsafe, and C4 violates the signed once-hash wording. |
| Nine signed events and runtime schemas | No intentional movement. New objects are control-plane/T-development objects. |
| E1/E2/E3 values and arithmetic | Unchanged; actual elapsed charge is not clipped. |
| Batch settlement / §V2.8 / amendment §D1–§D2 | Descendant parsing, all-live invalid batches, `ARCHIVE` before `RESOLVED`, inline meter evidence, and head/cache completion boundaries are carried unchanged. |
| Validity precedence and invalid terminals | No new valid terminal is intentionally reachable from a freeze or failed output. The rejected-witness fallback needs M1's mechanical repair. |
| Stream ownership / concurrency cap | Unchanged. |
| Sole capability and runtime custody | Unchanged. Client/watchdog/worker hold no runtime capability or lock. |
| Import allowlist and frozen roots | No delta is authorized. The adapter remains within the named module root. |
| T/Q/C and scientific boundary | Unchanged in principle. M5 must close arbitrary scientific content in the author authority before it can release capacity. |
| Archival exclusions / clean-HEAD | Existing exclusions carry forward; no configuration change is authorized. |

## Author cells and bounded repair

No genuinely new author-choice cell is required. The defects concern
acyclic identity construction, complete custody proof, earliest
grandchild identity, collision-safe fd handling, one acknowledgement
precedence, later safe GC, exact authority content, and compliance with
the already-signed once-hash provider. The existing A3/B1/C1/D1/K1
selections supply the policy.

The per-operation custody-absence decision remains an act of author
authority already required by signed K1; specifying its bytes does not
create a new scientific/resource choice. It must, however, be made
acyclic, content-closed, and complete over all custody roots.

## Authorization boundary

The token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is **not available** for signature.

The smallest bounded correction described above requires another
independent X/Y review of the repaired bytes. This review authorizes
neither that repair nor implementation.

No implementation, code/test change, T activation, entropy, runtime
construction, supervisor/controller/worker/watchdog/adapter process,
endpoint, pipe, FIFO, journal instance, capability, lease, batch,
operation, capacity artifact, custody disposition, promoted object,
world, learner, candidate, Q attempt, Q/C object, datum, outcome,
scientific work, E1/E2/E3 spend, or claim movement is authorized.

## Static custody and programme state

No existing file was changed. Exactly this one new review file was
created. No repository code, test, probe, supervisor, controller, worker,
watchdog, endpoint, smoke, or Officina process ran. No T/Q/C or
scientific artifact was created. The pre-existing dirty and untracked
working-tree files were preserved.

Static inspection shows `successor/officina/runtime/` still contains only
the tracked immutable `T_RUNTIME.lock`,
`successor/officina/runtime_control/` is absent, and
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
T remains `NOT_ACTIVATED`. The programme claim remains `OPEN`.
