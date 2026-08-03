All five hashes match what v1.1 pinned. Now locating the four artifacts across the accepted chain:

This is decisive for I2's hardest question. Reading §N5 of v2.1.2 in full:

§N5 resolves it. Reading the remainder plus the other three schemas:

`killer ∈ {WATCHDOG, SUPERVISOR}` is in the signed schema — the fallback is real, not superseded. Checking whether P1 retained it, and pulling the remaining two schemas:

I have every literal I need, and the chain resolves the freeze question without an author choice. Creating v1.2 from v1.1's exact bytes so the preserved mechanics are byte-faithful rather than retyped:

One row needs care — `t-process-claim.v1` requires literal `controller_pid` and `process_group_id`, but P1 says the supervisor can express no PID. Checking whether the chain resolves this:

This may be a genuine signed-contract conflict. Checking exhaustively before concluding:

No P1-chain document addresses the claim's PID fields. This is a real conflict between signed contracts. Confirming the exact header strings before editing:

Now the core repair — replacing §P1-13 entirely:

Now replacing §P1-13.2 through §P1-13.7 with the total matrix:

Now the interface tests (I3) and the remaining structural updates:

Now provenance, edit surface, and the §P1-16 negative-space reference:

Now the full mechanical audit on final bytes:

Two `unchanged` and one `carried` crept into my new text. Locating:

Both deliverables are in place. **The verdict is `BLOCKED`, not `READY`.**

## Why

Literalizing the interface — exactly what this round commissioned — surfaced a conflict between two separately signed contracts that the accepted chain does not resolve.

`t-process-claim.v1` mandates the literal integer keys `controller_pid` and `process_group_id` (T activation protocol v2), and its `process_group_id` is load-bearing: §Z4.6 conjunct 7 compares a freeze witness's pgid against it. The record is written by the generic-harness peer layer executing in the supervisor process.

But the signed nine-opcode response set returns no pid and no group number anywhere:

```
controller_start_identity  <- AWAIT_STOP's start_identity     AVAILABLE
argv                       <- argv_template + ctrl fds 3,4    AVAILABLE
controller_pid             <- no source                     UNAVAILABLE
process_group_id           <- no source                     UNAVAILABLE
```

`pgid_is_leader ∈ {0,1}` is the near miss and isn't enough — knowing the group id equals the process id is worthless when the process id is unavailable. I searched the whole P1 chain (binding through v2.1.10.7): nothing addresses these two keys. The one sentence that touches the subject asserts the claim is written "unchanged… the same fact, obtained by the same syscall" — an assertion about the *stop fact* that never reaches the identity keys.

The PCS can't absorb it either: it has no access to `activation_record_sha256`, `device_identity` and the rest. Two coherent repairs exist (extend the response set with a read-only identity tuple; or relocate the keys), with different costs to different signed sentences. **I chose neither.** Cell: `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`.

## What is complete

**I1** — §P1-13.0 gives three logical layers, five process kinds, and rules `R-L1`–`R-L6`: a supervisor-process write is not automatically a P1-layer write; call direction is one-way peer→P1 through the nine opcodes.

**I2** — three of four artifact rows fully literalized with paths, key sets, writers, readers, ordering and deletion authority.

The freeze question you told me not to guess at **is resolved by the chain**, not by me: the supervisor *does* write `t-freeze-observation.v1`. Evidence is two-part and mutually confirming — the signed key set contains `killer ∈ {WATCHDOG, SUPERVISOR}`, and §W3.5's ack-absence row says "supervisor freezes all live groups itself… with `killer = SUPERVISOR`". Owner: the peer layer's freeze-witness function — **one** logical writer, two executing processes, discriminated by the mandatory `killer` key. C1 holds because that branch is part of the signed watchdog failure table, and under P1 it additionally requires `SIGNAL_GROUP`. P1 replaced only the tail clause: replacement is `SPAWN_WATCHDOG`, not a supervisor fork.

**I3** — §P1-13.4's title "neither reads nor writes" deleted as literally false; total matrix, `SW-1`–`SW-5`, eight operations each assigned to one root/function, tests 84–85 recomputed and 86–91 added.

**I4** — verified mechanically on final bytes: six unique sentinels, **zero** placeholders across 27 patterns over 2 665 lines, **TOTAL GUARD FIRES: 0**, 91 test rows. `H_GUARDDATA` is byte-identical to v1.1 — direct evidence the guard data was untouched.

```
H_FILE       2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d
H_BODY       318cc6589c3840b8538b6818bfa3e42701fb25e55bfbf8a27897c5fc06ad82e1
H_GUARDDATA  0d3131b4a319d0bf03310e203485320253b671501ec44f87d67e8d47f8616733
H_NORMATIVE  2606e941bfe3400af49b5ecdb7fa02a9ef69a99a90aa0e55caeb476c033564cd
```

I completed v1.2 in every other respect rather than abandoning it, so the signed decision lands in a document that is otherwise ready. v1.1 is byte-untouched (`90ddf3ff…`); only the two new files were created. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

The single point most worth attacking first: if any accepted document does supply those two keys to the supervisor, the block is wrong and row 2 should simply be completed.
