# Opus 4.8 X-line: Officina supervisor/control-channel v1 confirmation

Work read-only in `/home/master/llm_projects/philosophia`.

Write exactly one new file:

```text
reviews/opus_officina_supervisor_control_channel_v1_confirmation.md
```

Do not edit code, contracts, tests, signatures, runtime artifacts, or any
existing review. Do not commit. Do not start any real supervisor/controller/
worker and do not activate T. Disposable test-only process probes under `/tmp`
are allowed if they create no production-compatible artifact.

## Candidate under review

Commit:

```text
9b05da09a1a45ac79368ed7abba09eb029db94fe
```

Artifacts:

```text
746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
2285ae09f964f7aa9f6ccd473f118b8de5a5dcc8b747f4479188c182eb5cdfa7  reviews/fable_officina_supervisor_control_channel_v1_closure.md
```

Read the signed composite and implementation reviews named by the closure. This
is a bounded confirmation of the one formerly blocked surface, not a fresh
redesign of batch settlement or science.

## X-line mandate

Determine whether two independent implementers can build the same safe process
tree, watchdog, control channel, confinement, promotion, and crash recovery
from this draft without choosing policy inline. Trace actual Linux semantics,
not intended prose.

Answer Fable's two Opus questions and attack at least the following.

### Spawn and lifetime

1. `subprocess.Popen(...); os.kill(pid, SIGSTOP)` is a race: arbitrary
   controller code can execute between `exec` and the external stop. Does the
   draft actually guarantee behavior-incapability before the durable claim?
   If not, require one exact fork/self-stop/exec handshake or equivalent.
2. A crash after spawn but before claim leaves an unrecorded stopped session.
   The takeover scan enumerates durable claims/leases and therefore may not know
   its PID/start identity. Is the proposed "operator route or boot" compatible
   with the required single automatic continuation? If not, require a durable
   pre-spawn claim or an exact supervisor-generation child registry that does
   not alter signed runtime evidence.
3. Trace double-fork cuts: before/after each fork, setsid, endpoint creation,
   identity installation, CLI death, spawn-lock release, and two concurrent
   clients. Prove at most one serving supervisor or name the missing handshake.
4. Check the 60-second idle exit in G1/G2. Can it race a client, pending frame,
   claim, frozen controller, batch archive, or watchdog? Is it necessary and
   single-valued, or should it be removed/strengthened before signature?
5. Prove the poll-loop rule really initiates action at or before the deadline
   when request processing, filesystem I/O, Git archival, worker status, or
   another settlement consumes more than one poll interval. "Sleeps at most
   100 ms" is not itself a bound on loop work.

### Process identity and custody

6. Verify `/proc/<pid>/stat` parsing and the claimed field number exactly.
7. Prove controller/worker group parentage, `pass_fds`, close-on-exec, reaping,
   process-group emptiness, PID reuse, and takeover killing are deterministic at
   every cut.
8. Check whether one same-UID controller can open/modify deterministic FIFO or
   operation paths, chmod a `0000` directory, signal the supervisor, or
   impersonate a CLI client. Distinguish the signed privileged-operator threat
   model from the untrusted adaptive controller: the latter must be confined.
9. Verify that `claim` can open controller stdout/stderr paths before a
   process_id exists and that their exact canonical location is specified.

### Channel and watchdog

10. Audit FIFO open/read/write behavior with nonblocking endpoints, including
    ENXIO, EOF-before-writer, partial reads, PIPE_BUF, full pipes, reply-client
    death, and watchdog progress.
11. Determine whether the request/reply `arguments` and `detail` schemas are
    fully enumerated for every command/status. "Exact signed arguments" and
    "closed fact classes" are not byte specs unless all keys/types are named.
12. Trace retry after a committed transaction but lost reply. A new
    `client_monotonic_ns` yields a new request hash; prove the command cannot be
    applied twice, especially `CLAIM`, or require an exact durable idempotency
    binding/reply cache.
13. Check role authorization: can a controller or worker use the repository
    FIFO as a CLI client, or issue CLI commands through its inherited channel?
    Pin command sets per endpoint and peer identity.

### Promotion and crash cuts

14. Prove worker output is inaccessible to the controller before settlement.
    The controller knows `operation_id`, repository path, and runs under the
    same UID; mode `0700`/`0000` alone may provide no isolation.
15. Require exact path grammar, no symlink/hardlink/path traversal, regular-file
    checks, bounded output set, hashing order, and a single atomic directory
    rename for multi-file promotion.
16. Trace generation death after charge but before promotion and after
    promotion but before token delivery. Confirm no double charge, late
    promotion, or result exposure; decide whether never reissuing a lost token
    is the signed intended terminal.
17. Verify operation-to-lease/meter/stream/charge binding and that no unrelated
    charge can be substituted.

### Compatibility

18. Verify the claim that no allowlist or frozen-file delta is needed.
19. Verify that the six new control schemas and five constants do not silently
    amend signed runtime evidence, archival sets, or resource policy.
20. Confirm every non-blocked Cursor repair in §S6 remains mechanical and is
    neither weakened nor contradicted.

## Required verdict

First line exactly one:

```text
OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1_XLINE_CONFIRMED
REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1
BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1
```

Use Critical/Major/Minor findings. If revision is required, give the smallest
exact correction and say whether it needs another author choice. State whether
the token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is ready for Kirill's signature. Confirm no implementation, activation,
manifest, supervisor, capability, process, entropy, spend, datum, or outcome
was created.
