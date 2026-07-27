# GPT-5.6 Sol Y-line: independent final check of Officina supervisor v2.1

Work in `/home/master/llm_projects/philosophia` using a clean review context.

Read `reviews/officina_supervisor_v2_1_authorship_note.md`: v2.1 was authored
by Claude Code Opus 5, despite historical `fable_` labels. Treat it as an
untrusted candidate contract.

Static/read-only review only. Do not edit or execute code, tests, contracts,
signatures, existing reviews, or runtime artifacts. Start no Officina process,
pipe/FIFO, journal, watchdog, or smoke. T remains `NOT_ACTIVATED`.

## Read first

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `reviews/fable_officina_supervisor_control_channel_v2_1_closure.md`
- both formal v2 X/Y reviews
- both supervisor author-selection signatures (A3/B1/C1/D1 and K1)
- the output-capacity packet
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the signed batch-settlement/generic-harness composite
- current dirty implementation/tests read-only for implementability distinction

The five author selections are closed. Test semantic totality, validity,
resource accounting, and scientific non-regression.

## Required attacks

### 1. B1 intent/ack semantics

Re-run all eight commands through lost request/reply, client crash, supervisor
generation change, effect-before-journal-phase crash, acknowledgement, GC, and
old retry. Verify repeated heartbeats/status observations receive distinct
semantic occurrences while retries reuse one.

Specifically test client-slot deletion and occurrence-index reuse; concurrent
clients sharing one scope; implicit ack by successor occurrence; a client that
observed a reply but crashed before `.done`; and a tombstone that stores only a
high-water integer plus the last effect-reply hash. No protocol error may drive
G5, no acknowledged effect may reapply, and no legitimate new effect may be
permanently refused.

Check whether unjournaled STATUS observation is consistent with signed B1 “all
eight commands,” token redelivery, bounded polling, and the separate explicit
delivery ack.

### 2. C1 validity and evidence authority

Verify watchdog registration precedes behavior, old deadline remains binding,
quiescence time is conservative, lost evidence never invents time, and every
positive/unknown overrun follows one all-live invalid route with full E1 facts.

Assess whether watchdog-written durable control-plane evidence is compatible
with the selected freezer-only/sole-supervisor-writer meaning. Reject any
second authority capable of selecting validity. Check process-tree escape and
same-UID A3 residual are reported without over-claim.

### 3. K1 capacity, custody, and scientific neutrality

Trace OPERATION_ADMIT from accepted semantic plan through reservation, bound,
admission, worker bootstrap, reply, `SIGCONT`, stream, settlement, promotion,
quarantine, delivery ack, and disposal. Attack the crash after cached ADMITTED
reply but before `SIGCONT`; no stopped worker may be stranded behind a cached
success.

Confirm the 64 MiB/stream, 256 MiB/operation, 32 GiB aggregate, 8 GiB margin,
and 4 MiB chunk limits are embedded unchanged. Capacity must include live,
pending, quarantine, and promoted custody; only a verified signed disposition
may release. Require exact author-disposition schema/path/signature semantics.

Check K1 enforcement occurs during production for contract-following workers,
all official preterminal responses remain fixed PENDING, and no byte/result/
failure fact enters Q/C or scientific interpretation.

### 4. Spawn/takeover and control artifacts

Test whether an in-process grandchild can be discovered by a cmdline
`spawning_id` marker it never execs; whether retained `SPAWN.lock` gives safety
but can deadlock liveness; and whether controller/worker bootstrap tokens are
actually interpreted before arbitrary target behavior.

Audit every immutable journal/capacity/spawn/freeze/operation schema and every
crash reducer. Client-owned files must not become hidden runtime authority.

### 5. Non-regression

Confirm A3 remains T-only and procedural against deliberate same-UID action;
D1 remains no-idle-exit; E1/E2/E3 and nine signed events are unchanged;
capability custody and all-live batch remain sole-authority; no tenth event,
new root, hidden success-conditioned resource change, Q/C evidence, automatic
retry, or claim movement appears.

Answer all three Sol questions in the v2.1 closure explicitly.

## Deliverable

Write exactly one new file:

`reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md`

First verdict line exactly one of:

- `OFFICINA_SUPERVISOR_V2_1_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`
- `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1`
- `BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1`

Lead with Critical/Major findings and minimal exact repairs. State whether any
repair reopens an author cell. If confirmed, name the exact token made eligible
conditional on X. Confirm static-only custody, T `NOT_ACTIVATED`, and claim
`OPEN`.
