REVISE_OFFICINA_SUPERVISOR_V2_1_6

# Independent clean-context Y-line review

Date: 2026-08-01

Reviewer line: Y

## Review base, method, and recomputed hashes

Review base: `def59053afd9d570ef99ba0b28f13e3308eb419c`, proved to
descend from the required commit
`692207aa07ad87fcf46a9827524b25ca54d56c07`.

I read the complete supervisor v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4/
v2.1.5/v2.1.6 chain, both signed author-selection files, the inherited
generic-harness and batch-settlement corrections, and the completed v2.1.5
Y-line review. I treated every author closure and chat response as untrusted
self-assessment.

There was **no formal v2.1.5 X verdict**. The tracked review set contains an
X prompt and chat response, but no
`opus_officina_supervisor_control_channel_v2_1_5_final_confirmation.md` (or
equivalent formal X deliverable with a line-1 verdict). The v2.1.5 Y verdict
was `REVISE_OFFICINA_SUPERVISOR_V2_1_5`.

Recomputed SHA-256:

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md
```

The v2.1.6 digest exactly matches the expected committed value.

This was a static contract review. I used only read-only file display, Git
ancestry/status/listing, SHA-256 over specified bytes, and literal arithmetic.
No repository code, test, probe, smoke command, or Officina process ran.

## Answer

No. v2.1.6 closes the v2.1.5 close-state defect, removes the contradictory
universal bootstrap-duration language, and fixes the `boot_w`/`rel3_r` EOF
attribution. Its stable-filesystem selector also closes all five v2.1.5
malformed-terminal counterexamples.

The repaired bytes nevertheless retain three blocking defects:

1. Physical presence and validity are not bound to the same directory entry
   or to a final selector snapshot. An opposite terminal installed after its
   physical-presence observation remains `P*=false`; a releasing branch can
   then run, and the complete-custody proof permits that terminal name as an
   L2 control record. This is an unstated TOCTOU release path.
2. `STAGE_M_ROUTE` has no branch for the `c6` failures it expressly names when
   `/proc/<pid_mid>/stat` is unreadable or unparsable. Its two `os.kill`
   calls and `waitpid` also lack errno/result continuations. The route is not
   total at ordinary process-exit and host-error cuts.
3. The fail-closed stage-M continuation can leave only `SPAWNING.json`, which
   names the still-live CLI, after the middle later exits and releases the
   lock. The next preflight sees a conflicting live identity (P2b), while the
   stuck-holder route has no `SPAWNING.json`/CLI tier and is forbidden to kill
   the CLI. A long-lived caller therefore wedges every future attempt.

These defects require a bounded mechanical repair, not a new author choice.
The signature token remains unavailable.

## One-to-one disposition of the v2.1.5 findings

| v2.1.5 finding | v2.1.6 repair | Independent disposition |
|---|---|---|
| **C1** malformed opposite terminal can release | §V216.1 separates `PS/PQ/PF` from `VS/VQ/VF` and gives `MALFORMED` priority | **Not closed exactly.** The fixed-snapshot cross-product is correct, but the observation is not object-bound or revalidated. A canonical opposite terminal introduced between its presence check and branch/release is invisible to `P*` and can coexist with release. |
| **M1** normal closes lack the cleanup errno transition | §V216.2 defines `CLOSE_OWNED` and applies it at every normal, cleanup, scrub, and lock close | **Closed.** On pinned Linux, all non-`EBADF` close outcomes release the descriptor; ownership is removed before routing; the number is never retried; uniform `CONTINUE` is sound at every listed site. |
| **M2** c5–c7 can remove records while the middle lives | §V216.3 adds `STAGE_M_ROUTE`, proof-before-unlink, and a no-unlink continuation | **Not closed.** Proof-before-unlink is repaired, but unreadable/unparsable `/proc` and signal/wait errors have no route; the no-unlink continuation silently wedges a long-lived caller when only `SPAWNING.json` exists. |
| **M3** stale universal nonblocking/healthy-bound obligations | §V216.4 replaces both assertions and rows 121/126 | **Closed.** The operative composite now asserts only bounded pipe helper calls, makes no duration claim for `/proc`, installs, or `fsync`, and makes slow-valid expiry deterministic and non-citable. |
| **m1** `rel3_r` falsely causes `c13` EOF | §V216.5 moves the causal annotation to `boot_w` | **Closed.** The eight-end audit is correct: last-writer closure causes EOF; last-reader closure can only cause `EPIPE` on a later write. |

## Trace 1 — C1 physical/validity cross-product

For a **stable** directory during the held lock epoch, `V* ⇒ P*`. If any
present object is invalid (`P* ∧ ¬V*`), Rule 0 alone is effective and releases
nothing. Thus all validity assignments except `V*=P*` collapse to Rule 0.
Within the remaining well-formed subspace, the physical triples are:

| `PS PQ PF` | Binding/hash refinement | Continuation | Release |
|---|---|---|---:|
| `000` | — | Rule 5 / ordinary no-terminal refusal | 0 |
| `001` | — | Rule 5 / impossible orphan manifest invalidity | 0 |
| `010` | null binding | Rule 4 / `B-QN` | exactly one `bytes_reserved` after all downstream checks |
| `010` | non-null binding, manifest absent | Rule 5 / impossible binding-without-file invalidity | 0 |
| `011` | non-null and `HQ` | Rule 3 / `B-QM` | exactly one `bytes_reserved` after all downstream checks |
| `011` | non-null and hash mismatch | Rule 5 / refusal | 0 |
| `011` | null binding | Rule 5 / orphan-file-without-binding invalidity | 0 |
| `100` | — | Rule 5 / settlement-without-manifest invalidity | 0 |
| `101` | `HS` | Rule 2 / `B-P` | exactly one `bytes_reserved` after all downstream checks |
| `101` | hash mismatch | Rule 5 / refusal | 0 |
| `110` | any | Rule 1 / both-terminal invalidity | 0 |
| `111` | any | Rule 1 / both-terminal invalidity | 0 |

Snapshot handling of named malformed forms is correct:

| Physical canonical object | `P*` | `V*` | Result |
|---|---:|---:|---|
| symlink | 1 | 0 | Rule 0 |
| directory | 1 | 0 | Rule 0 |
| zero-byte file | 1 | 0 | Rule 0 |
| truncated/partial canonical file | 1 | 0 | Rule 0 |
| regular, nlink 1, exact canonical object | 1 | 1 | well-formed table above |
| paired stat `ENOENT` and enumeration absence | 0 | 0 | absence in table above |
| name enumerated but stat/decode unreadable | 1 | 0 | Rule 0; it cannot be valid |

The five prior static counterexamples are therefore closed: malformed
quarantine beside settlement; malformed settlement beside non-null
quarantine; malformed settlement beside null quarantine; malformed manifest
beside both terminals; and malformed opposite terminal plus a mismatching
manifest all take Rule 0 and release nothing.

The mutation trace is not closed:

1. The selector enumerates a valid settlement and manifest and observes no
   `QUARANTINE.json`: `PS=1, PQ=0, PF=1`.
2. Before or after `VS/VF/HS`, a deliberate same-UID process installs a
   canonical malformed `QUARANTINE.json`.
3. The stored `PQ` remains false; Rule 0 does not see the new object; Rule 2
   remains true and enters `B-P`.
4. Branch `B-P` does not repeat the opposite-terminal absence test.
5. §N2.3 P2 permits `QUARANTINE.json` as a member of the closed L2 control
   record set, so the complete-custody proof does not block it.
6. The author disposition can install `.disposed.json` and release
   `bytes_reserved` while a contradictory opposite terminal is present.

The symmetric `PS=0` snapshot followed by a settlement install can reach
`B-QM` or `B-QN`. Replacement of one canonical name between `stat`, decode,
and hashing is likewise not bound by `(st_dev, st_ino)` or by one opened
descriptor. The held `T_RUNTIME.lock` serializes contract actors but is not a
same-UID filesystem exclusion mechanism; the signed A3 residual makes that
limitation honest only if the contract names it. v2.1.6 instead claims the
release is “impossible by two independent conjuncts.”

## Trace 2 — selector totality, artifacts, causes, and releases

For an immutable observation set, Rule 0 and Rule 1 are disjoint because Rule
1 contains `¬MALFORMED`; Rules 2–5 all contain the same negation. Rule 0 names
every malformed path in one record-first invalidity. Rule 1 names both
physical terminal paths. Rule 5 preserves the distinction between ordinary
pending (`000`, refusal) and impossible durable layouts (`001`, `100`,
binding/file contradictions, record-first invalidity). Hash mismatch remains
a refusal, not a fabricated invalidity. The only releasing predicates are
Rule 2/3/4, and every one still requires its unchanged branch body, all
§N1.5 authority checks, and §N2.3 P1–P7 in the same lock epoch.

The selector is therefore logically total for a frozen set of objects but not
temporally total for its actual multi-syscall observations. The latter is a
governing-rule defect, not repaired by reading order.

## Trace 3 — M1 `CLOSE_OWNED` state machine

| Input/outcome | Ownership transition | Next action |
|---|---|---|
| fd not in this process's `owned` set | no syscall, no change | `NOT_OWNED`; continue |
| `close` succeeds | remove fd exactly once | `CLOSED`; continue |
| `EBADF` | remove stale ownership; nothing was open at the number | `CLOSED_ABSENT`; continue |
| `EINTR` | Linux has released the fd; remove ownership; never retry | `CLOSED_ERROR`; continue |
| `EIO`/other non-`EBADF` error | Linux has released the fd; remove ownership; never retry | `CLOSED_ERROR`; continue |
| second invocation after any attempted close | fd absent from `owned` | no syscall; a reused number is safe |

Forked copies have separate per-process ownership sets. A close in one process
does not remove the other process's copy; EOF/`EPIPE` occurs only after the
last applicable copy closes. A process crash releases that process's remaining
descriptors in the kernel; no non-crash path relies on destructor, GC,
finalizer, exception propagation, or caller exit.

Every named site is covered:

| Owner | Sites | Result of `CLOSED_ERROR` |
|---|---|---|
| CLI | `c5`, `c8`, `c12`, `c13`, `c16`, `c18` | observable pipe/lock release is the success state; continue |
| middle | `m1`, `m6`, `m8` | continue |
| grandchild | `g1`, `g3` | continue |
| any cleanup | eight fixed bootstrap ends | continue each call |
| refusal paths | `REFUSAL_SEQUENCE` lock close; `STAGE_M_ROUTE` lock close | preserve the refusal |

For both lock closes, uniform continuation is sound: success, `EINTR`, or
other non-`EBADF` error releases this process's open description; `EBADF`
means it held no lock through that number. At stage M, child death must precede
record cleanup; at normal `c18`, the grandchild's fork-shared copy may still
hold the singleton until `g3`, as intended. This repair closes v2.1.5 M1.

## Trace 4 — M2 `c5`–`c7` construction and identity

| Cut | Exact identity available | Safe action in stated text | Independent result |
|---|---|---|---|
| `c5` abandonment | `pid_mid` from the successful fork | re-read stat; if present, capture start identity and require `ppid == CLI`; then `kill(pid_mid)` only | PID-reuse protection is adequate when the read succeeds; no `killpg` is allowed |
| `c6`, stat absent | `pid_mid`; absence | no kill; proceed to proof/cleanup | safe if absence and later `waitpid` results are classified |
| `c6`, stat present and parseable | `pid_mid`, freshly captured start identity and ppid | identity-safe `kill(pid_mid)` | safe against reuse because an own unreaped child cannot have its PID reused |
| `c6`, stat unreadable or unparsable | `pid_mid` only | **no matching 2b–2e branch** | non-total |
| `c7`, record install fails before rename | in-memory pid + captured start identity | match current stat, kill pid, prove death; remove only this attempt's records | safe when all syscalls succeed |
| `c7`, rename completed but durability reports failure | same in memory; middle record may be visible | same; unlink only after death proof | live-record removal defect is repaired |
| captured start identity mismatches | recorded process gone/reused | no kill, no unlink | safe but subject to the wedge below |

The capture-to-kill race does not by itself authorize killing a reused PID:
before the CLI reaps its own exited child, the child is a zombie and its PID
cannot be reassigned. But the text does not classify the actual signal cuts:

- `SIGTERM` succeeds, the child exits, and `SIGKILL` returns `ESRCH`;
- either signal returns `EINTR`, `EPERM`, or another errno;
- the proof-loop stat becomes unreadable or unparsable;
- `waitpid(pid_mid, WNOHANG)` returns `0`, the child pid, `ECHILD`, `EINTR`, or
  another error.

Only the proof timeout has a continuation. The other results are not mapped to
proof, retry, or the no-unlink route, so two implementations can diverge.

The fail-closed path also wedges a legitimate long-lived caller:

1. Failure occurs at `c5` or `c6`; only `SPAWNING.json` exists.
2. Death proof expires; F1 leaves every record and F3 releases the CLI's lock
   reference.
3. The middle exits at its `m0` bound and releases its fork-shared reference,
   so `SPAWN.lock` becomes free.
4. The original CLI remains alive after returning the refusal.
5. A later attempt acquires the lock and sees `SPAWNING.json` naming that live
   CLI. §U6.1 P2b requires a retryable refusal and unlinks nothing.
6. Stuck-holder s1–s5 has child, group, and middle tiers but no authority over
   a `SPAWNING.json`-only live CLI, and the contract forbids killing a client.
7. Every later attempt repeats P2b. Forward progress is silently wedged until
   the unrelated lifetime of the original CLI ends.

This refutes §V216.3.2 F5's statement that inherited preflight/stuck-holder
rules provide the continuation for all surviving records.

## Trace 5 — M2 crash prefixes

| Prefix | Durable/process fact | Restart continuation |
|---|---|---|
| before identity read | attempt records survive; child may live | no unlink; later holder must revalidate identity |
| after captured identity, before `SIGTERM` | records survive | re-read start identity before any signal |
| after `SIGTERM`, before `SIGKILL` | child may be dead/dying | records survive; `ESRCH` must lead to proof, but v2.1.6 does not say so |
| after both signals, before proof | records survive | poll exact identity/death; never unlink merely because a signal was sent |
| after proof, before fd cleanup | child dead | later P3 may remove; no live unlink |
| between `CLOSE_OWNED` calls | local ownership prefix removed | a process crash releases the rest; a non-crash re-entry skips removed members |
| after fd cleanup, before child unlink | child dead, records survive | ordered removal can restart |
| between child/group/middle/spawning unlink or fsync | only a lower-tier suffix may survive | ENOENT-tolerant child→group→middle→spawning completion |
| after final unlink, before lock close | child dead, no records | close local lock reference; clean next attempt |
| after lock close | no attempt state | second invocation starts at P0 |
| no identity/death proof | no record was unlinked | fail-closed, but the `SPAWNING.json`-only long-lived-CLI wedge remains |

Thus the repair correctly prevents premature live-record removal at all stated
prefixes, but it does not give every prefix a legal forward-progress
continuation.

## Trace 6 — M3 operative-language search

The operative replacement chain was searched for the universal phrases, not
accepted from §V216.4's author table. The positive stale assertions occur in
the preserved v2.1.4 evidence and in later quotations that explicitly replace
or reject them. The governing v2.1.6 text now says only:

- all four **pipe** pairs are nonblocking;
- no bootstrap pipe read/write can exceed its helper deadline;
- `/proc` reads, canonical installs, and file/parent `fsync`s have no signed
  executable duration bound;
- no claim is made that every healthy launch completes within the grandchild
  gate policy;
- slow-valid expiry takes one deterministic refusal and creates no ledger,
  witness, fallback, capacity, custody, manifest, invalidity, datum, or
  scientific/resource fact.

Rows 121 and 126 are expressly replaced; rows 159–162 therefore become
jointly satisfiable. A slow valid c14/c15 can be refused as policy; repetition
cannot turn that refusal into a citable fact or a different class of outcome.
v2.1.5 M3 is closed.

## Trace 7 — m1 pipe causality, all eight ends

| End whose last copy closes | Mechanical consequence | Observer |
|---|---|---|
| `boot_w` | EOF on `boot_r` | `c9`/`c13`; at m7 fork failure this causes the immediate c13 EOF |
| `boot_r` | later `boot_w` write gets `EPIPE` | `m4`/`m8` |
| `rel1_w` | EOF on `rel1_r` | `m0`; not possible while the middle retains its own writer before `m1` |
| `rel1_r` | later `rel1_w` write gets `EPIPE` | `c8` |
| `rel2_w` | EOF on `rel2_r` | `m5` |
| `rel2_r` | later `rel2_w` write gets `EPIPE` | `c12` |
| `rel3_w` | EOF on `rel3_r` | `g0`; after `m1` the CLI is the sole writer |
| `rel3_r` | later `rel3_w` write gets `EPIPE` | `c16` |

The final `boot_w` copy is the only stated cause of c13 EOF in the m7 failure
route. `rel3_r` is now ownership cleanup only. No stale operative
misattribution remains. v2.1.5 m1 is closed.

## Trace 8 — no regression in preserved surfaces

The inherited illustrative identities remain unchanged:

```text
disposition preimage, 396 bytes:
e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

eight-line decision file, 504 bytes; line 8 is 43 bytes including LF:
0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f

canonical result entries, 265 bytes:
5359c361351c1538a4f4a73c4736e9f11951e63eb7398aea3e147f0da8e678a3

canonical RESULT_MANIFEST.json, 638 bytes:
e4ec318294827b6e28d4fd2a13e503d559b9f627bcf732a7e0c2e2968b7454ed

operation-directory enumeration:
3f8e1c99d74c4b0a881b776794d615eee7aae03f43595c46604358dbd7eca0dc

canonical empty array, [] plus LF:
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

| Surface | Independent re-test |
|---|---|
| **Preserved selector bodies** | `B-P` P1–P5, `B-QM` QM1–QM6, and `B-QN` QN1–QN4 remain mutually exclusive after a stable selector observation. The temporal entry defect is isolated above. |
| **K1 accounting/custody** | One write and one sole hash per content byte; `bytes_reserved` never falls at settlement, failure, quarantine, rename, promotion, ack, or unused reservation; L1–L5/P1–P7 and the content-closed author authority carry. The C1 TOCTOU path can improperly enter a releasing body but does not alter the accounting formula. |
| **Bootstrap/forks** | Four nonblocking pipes, both middle gates, the grandchild gate, fixed adapter root, verified `setsid`, pre-group `kill(pid)`, post-group `killpg`, fixed fd remap, and m7→m8 deadlock repair carry. Stage-M totality is the isolated regression. |
| **A3** | One-write/one-hash residuals R1a/R1b/R2/R3, timing/metadata leakage, and slow-bootstrap policy remain procedural and non-citable. The new selector race is not honestly named and is therefore blocking. |
| **B1** | All eight commands retain explicit `NEW`/`RETRY`, immutable phases, current-envelope redelivery, journaled observation STATUS, prefix-first classification, frontier ack, and `committed→reply→ack→accepted` GC. No B1 text changes. |
| **C1 watchdog** | Publication after start/renew/remove, old-deadline authority, drain-before-freeze, validated witness/fallback, swap-only replacement state machine, and sole-supervisor settlement remain unchanged. |
| **D1** | No idle exit remains. Stage-M's `SPAWNING.json`-only path can wedge future construction, so practical forward progress is not fully preserved. |
| **GC** | G1/G2/G3 bind through `accepted.json`; deletion order, four fsync points, empty-directory completion, crash-prefix classification, and no owed reply after prefix acknowledgement carry. |
| **Singleton lifecycle** | Lock-first P0–P3, no mutation in the unlocked stuck-holder route, PID-reuse protection, EEXIST, and child→group→middle→spawning removal carry. The surviving SPAWNING-only state falls outside the claimed next-attempt recovery. |
| **Author authority** | Derived path, acyclic disposition id, exact eight lines, timestamp equality, manifest-bound identifier set, same-lock complete absence, and no-replace single use carry. |
| **Generic harness / batch settlement** | v2.3.1 §J1–§J3, v1.1.1 §D1/§D2, nine signed events, inline meter evidence, E1/E2/E3, roots, archival order, and Q/C boundary are unchanged. |
| **Scientific boundary** | No new result-responsive field, resource value, invalidity cause, learner/candidate field, or scientific authority is introduced. Close outcomes are routing-inert internal control facts. |

## New findings

### Critical

#### C1. Physical presence and validity are not one object-bound snapshot, allowing a TOCTOU release

Loci: v2.1.6 §V216.1.1 lines 148–185; §V216.1.2 Rules 0–4, especially
lines 204–205 and the “impossible by two independent conjuncts” claim at
lines 222–225; inherited §N2.2 L2 allowed set and §N2.3 P2.

The `P*` predicates come from one enumeration plus a separate stat, while the
`V*` and hash predicates decode later bytes without an opened-fd/inode binding
or a final revalidation. An absent opposite terminal can be installed after
its `P*` observation. Its stale `P*=false` enables `B-P`, `B-QM`, or `B-QN`;
L2 treats the new terminal as an allowed control record, so custody absence
does not stop the release. The symmetric settlement/quarantine attacks both
work. This is precisely a release across an unacknowledged A3 TOCTOU window.

Smallest bounded repair: define one observation record per canonical name
that binds enumeration membership, `lstat` identity, an `O_NOFOLLOW` opened
descriptor for valid regular files, exact decoded bytes, and hashes. Require
every predicate to consume that record. Immediately before entering a branch
and again before `.disposed.json`, repeat the paired name observation and
require the same identity/bytes for present objects and paired absence for an
absent opposite terminal. Any change releases nothing. State honestly that a
deliberate same-UID mutation after the final observation is the signed A3
procedural residual; delete the unconditional “impossible” claim. Re-run all
create/remove/replace cuts.

### Major

#### M1. `STAGE_M_ROUTE` does not classify the failures it is invoked to handle

Loci: v2.1.6 §V216.3.2 steps 2a–3, lines 481–499; §V216.3.3 c6 row,
line 533.

The c6 row expressly covers unreadable and unparsable `/proc` state, but step
2 has branches only for absent or successfully parsed present state. It also
does not classify `os.kill` or `waitpid` results. An ordinary exit between
`SIGTERM` and `SIGKILL` can yield `ESRCH`; `EINTR`, `EPERM`, `ECHILD`, and
other errors are reachable. No continuation says when to retry, proceed to
proof, or enter F1–F5.

Smallest bounded repair: add an explicit stat result enum
`ABSENT|PRESENT_VALID|UNREADABLE|UNPARSABLE|ERROR`; only the first two may
prove identity. Route the last three to no-kill/no-unlink bounded handling.
Pin both signal calls (`success`; `ESRCH`→proof; `EINTR`→bounded retry;
permission/other→no-unlink fail-close) and every `waitpid` result (`pid`, `0`,
`EINTR`, `ECHILD`, other). A wait result may prove this own child dead only
under a stated identity-safe rule. No syscall exception may escape the route.

#### M2. The stage-M fail-closed continuation can permanently wedge a long-lived caller

Loci: v2.1.6 §V216.3.2 F1–F5, lines 512–525; inherited §U6.1 P2b and
§U2.5 stuck-holder s1–s5; §V216.3.4 final row, line 550.

At c5/c6 only `SPAWNING.json` exists. If proof expires, F1 leaves it. After
the middle's bound releases the lock, it still names the live original CLI.
The next attempt's P2b refuses and cannot unlink; s1–s5 has no CLI/SPAWNING
tier and the contract rightly forbids killing a client. A long-lived caller
therefore makes the singleton falsely unavailable forever. F5's claimed next
attempt continuation is false.

Smallest bounded repair: give the SPAWNING-only route an executable terminal.
Prefer a bounded own-child `waitpid` proof independent of `/proc`; after proof,
perform ordered removal under the still-held lock. If proof remains
unavailable, define a recoverable durable child identity before returning, or
define a safe SPAWNING-only completion that cannot leave a live-CLI P2b wedge.
Do not rely on caller exit, GC, or an unstated operator action. Re-run a
long-lived CLI, a stopped middle, unreadable `/proc`, and restart before/after
the middle's bound.

### Minor

None.

## No-regression table

| Signed/inherited surface | v2.1.6 result |
|---|---|
| **A3** | Four inherited output residuals remain honest; the new selector TOCTOU is not named or bounded, so overall result is **revise**. |
| **B1** | Preserved: all eight commands, retry-stable cached bytes, generation totality, ack priority, tombstone prefix, and GC. |
| **C1** | Preserved: watchdog/freezer is never settlement authority; fallback/replacement records remain supervisor-only. |
| **D1** | No idle exit preserved, but M2 can silently wedge later supervisor construction. |
| **K1** | Five constants, one write/one hash, full reservation accounting, complete custody, and sole author disposition preserved; C1 can incorrectly admit a release branch. |
| **Acyclic author authority** | Preserved; exact path, forward hash DAG, closed eight-line file, timestamp equality, and prohibited-value set unchanged. |
| **Result manifest** | Preserved; sole-pass tuples, canonical manifest, settlement/quarantine binding, orphan branch, and no content reread unchanged. |
| **Watchdog evidence/replacement** | Preserved; exact-current ack, I1–I7, fallback, UNKNOWN, swap-only resume, and supervisor-only settlement unchanged. |
| **FD remap and close ownership** | Fixed-fd remap preserved; `CLOSE_OWNED` closes the remaining normal/cleanup gap. |
| **Singleton records** | Proof-before-unlink restored at c5–c7, but SPAWNING-only forward recovery is not total. |
| **Harness/batch/events** | Generic-harness v2.3.1, batch v1.1.1, nine events, inline meter evidence, E1/E2/E3, and archival ordering unchanged. |
| **Q/C and T boundary** | No T activation, Q/C authority, spend, entropy, or science is introduced. |

## Author-cell determination

No genuinely new author cell is required. Object-bound selector observation,
total syscall-result classification, and a recoverable SPAWNING-only cleanup
are mechanical consequences of signed A3/B1/C1/D1/K1. The repair must not add
a resource quantity, scientific value, invalidity cause, custody destination,
or new author token.

## Authorization boundary

Because the verdict is `REVISE`, Kirill's token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable**. The bounded repair requires a fresh independent X/Y
review of the repaired bytes. This review authorizes no implementation, code
or test edit, commit, T activation, entropy, runtime construction, supervisor,
controller, worker, watchdog, adapter, endpoint, pipe, journal, capacity or
custody artifact, spend, Q/C work, or scientific work.

## Static custody and programme state

No repository code, test, probe, smoke command, supervisor, controller,
worker, watchdog, adapter, endpoint, or other Officina process ran. No existing
file or runtime state was changed; exactly this review file was created. No
T/Q/C, runtime, capacity, custody, result-manifest, entropy, or scientific
artifact was created. All pre-existing modified and untracked paths were
preserved.

`successor/officina/runtime/` still contains only `T_RUNTIME.lock`,
`successor/officina/runtime_control/` remains absent, and
`successor/officina/T_ENVELOPE.json` remains unactivated. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
