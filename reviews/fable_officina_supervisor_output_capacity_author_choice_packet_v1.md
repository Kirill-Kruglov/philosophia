READY_FOR_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION

# Fable 5 — Officina supervisor output-capacity author-choice packet v1

Companion:
`successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`.
Evidence commit: `bff27d4354ca4cdad4ad233260d4db25a595d3f4` (working tree
dirty exactly as handed over).

Inputs read: the supervisor v2 draft and its closure, the Opus (X) and
Sol (Y) v2 reviews, the signed supervisor author selections and the v1
choice packet, the signed generic-harness/batch-settlement composite and
its signature, the WP-1/WP-2 author selections and T envelope, the
activation-protocol archival rules, and — for byte sizes only — the
immutable Level-0/Level-1 timing and feasibility artifacts.

Exactly two files created. No contract, code, test, signature, review, or
runtime artifact edited. Nothing committed or staged. No Officina
supervisor, controller, worker, watchdog, FIFO, journal, endpoint,
operation, smoke, or test process started; no probe script run; no
benchmark created; no probe data written. Platform and storage inspection
was read-only. T remains `NOT_ACTIVATED`.

## 1. Verdict

`READY_FOR_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION`.

Not `BLOCKED`: three mutually exclusive, executable options exist, each
pinning an enforcement architecture, an exact numerical envelope, the
complete custody set, a reservation lifecycle, retention/disposal,
liveness, the A3 boundary, and the deployment/code surface. At least one
(K1) is enforceable on the current host with a fail-closed preflight, no
root, no import-allowlist delta, and no frozen-file delta.

## 2. Why this is the sole remaining author cell

Opus (X) argued that an admission-time `os.statvfs` reservation plus a
chunked, ack-servicing hash loop closes the output-byte hole
mechanically, and named a hard signed ceiling as the *conditional*
alternative that would require a token. Sol (Y) argued that a positive
caller-selected integer is not an aggregate bound at all, that releasing
the reservation at the `FAILED` terminal lets retained quarantine bytes
be double-spent, and that one bounded author choice is required.

The stricter rule is applied, on four grounds recorded in packet §0:

1. `statvfs` measures a filesystem shared with the whole host; a passing
   observation at admission is not a reservation and can be invalidated
   by an unrelated writer before the first output byte exists.
2. It bounds no supervisor work — not enumerate, not hash, not copy —
   so it cannot discharge the liveness obligation that X-C3 and X-M5 make
   load-bearing for the signed C1 watchdog.
3. It does not account for retained quarantine, which v2 §V2.7.2
   explicitly releases at `FAILED` while the bytes remain on disk.
4. It does not account for accumulated `runtime/T_PROMOTED/**` custody,
   which grows monotonically across all of T and is archival-excluded, so
   no signed archival set ever bounds it.

Points 3 and 4 are decisive: they are custody facts, not free-space
facts, and no dynamic observation of free space can represent them.
The packet therefore pins the aggregate accounting over live output,
pending settlement, quarantine, and retained `T_PROMOTED` together, and
makes exactly one durable artifact — `t-capacity-disposition.v1` —
capable of releasing capacity. Moving or renaming bytes, including the
promotion `os.replace`, changes only the recorded custody root.

## 3. Why every other X/Y finding is mechanical

Both lines say so explicitly. Opus: "Every repair below is bounded and
mechanical against v2's own text and the already-signed composite. **No
new author choice is required**, with one conditional exception" — the
capacity ceiling. Sol: "One new bounded author choice is required for the
aggregate output-capacity policy … The remaining repairs are mechanical
consequences of the selected semantics."

Independently checked, finding by finding: each remaining item names one
determinate repair whose destination already exists in signed text.
X-C1/Sol C1 restore the word "semantic" that the packet's own B1 wording
already carried, and demote a client protocol error out of the signed G5
surface. X-C2/Sol C5 need a discoverable pre-claim binding; the
argv-embedded `spawn_intent_id` plus a `/proc/*/cmdline` scan is
race-free in both directions and adds no schema key beyond the recorded
argv. X-C4/Sol C4 resolve to already-signed invalidity destinations with
one cause (`PROCESS`) and one freeze-time rule. X-C5 splits a phase that
§V2.9.1 already names as a supervisor state. X-C6/Sol M2 enumerate keys
for schemas v2 already names. X-M1–M11 and the seven minors are schema,
`errno`, ordering, actor, and bound statements. The complete list, mapped
to v2 loci, is packet §8 — 24 rows, none of which selects a policy value
or a provider.

The capacity cell is different in kind: it selects a *provider* and a
*number*, and no signed text determines either. That is why it is the one
cell and why v2.1 may not resolve it silently.

## 4. The options

| | Enforcement | Root? | Allowlist | Frozen files | Executable here |
|---|---|---|---|---|---|
| **K1** supervisor-mediated bounded output transport | worker holds no output path; every byte is written by the supervisor through an inherited pipe, counted and hashed in one pass, pipe closed at the ceiling | no | none | none | **yes** |
| **K2** preallocated dedicated filesystem container | fixed-size ext4 image on a loop device as the accounting root; kernel `ENOSPC` at the container boundary against any same-UID writer inside it | **yes** | none | none (paths relocate) | **no** — mount absent; needs root + fstab |
| **K3** kernel `RLIMIT_FSIZE` per-file cap on the worker tree | hard rlimit lowered before `exec`, irreversible for the worker and every descendant; `EFBIG`/`SIGXFSZ` stops writes per file | no | **`resource`** | **`verification.py` unfreeze** | yes |

A plain integer ledger and a bare `statvfs` check are named in the packet
as *accounting*, never as enforcement; no option is permitted to present
them as one.

**Recommended: K1** — the only option that is enforceable today with a
fail-closed preflight, that bounds the supervisor's own work by
construction (one streaming pass, 4 MiB chunks, watchdog ack serviced
between chunks), and that costs zero root, zero allowlist delta, zero
frozen-file delta, zero new root, and zero path relocation.

**K2 is not recommended and is not presented as immediately executable.**
Its aggregate bound is the strongest of the three — kernel-enforced
against a deliberate same-UID writer inside the container — but the mount
does not exist on this host and creating it requires root, a permanent
48 GiB allocation, and a reboot-persistent `/etc/fstab` entry. Exact
prerequisites are given in packet §K2.1. The ext4 project-quota variant
is explicitly rejected as non-executable here: the `quota` tools are
absent, `/` carries no `prjquota` option in either `/proc/mounts` or
`/etc/fstab`, and `tune2fs -l` is `Permission denied` for uid 1000, so
the superblock feature set is not even verifiable without root.

**K3 is listed as executable but not recommended**: its kernel guarantee
is per-file only, so the aggregate cell this packet exists to close still
rests on the ledger; it costs an unfreeze of the quarantine verifier; and
its 4 MiB per-file limit is smaller than the largest immutable checkpoint
artifact, forcing ≥ 7-way checkpoint sharding.

## 5. Numbers and their outcome-independent sources

Signed by the same token: `T_OUTPUT_PER_STREAM_MAX_BYTES = 67_108_864`
(64 MiB), per-operation `= 67_108_864 × len(declared_stream_indexes)`
(≤ `268_435_456` at k = 4), `T_OUTPUT_AGGREGATE_MAX_BYTES =
34_359_738_368` (32 GiB for the whole of T),
`T_OUTPUT_FS_SAFETY_MARGIN_BYTES = 8_589_934_592`,
`T_OUTPUT_COPY_CHUNK_BYTES = 4_194_304`.

Every term derives from a filesystem capacity fact, an immutable
engineering measurement, or signed-constant arithmetic:

- largest immutable checkpoint artifact in repository history,
  `25_768_935` bytes, from
  `experiments/level_1_contact/feasibility_v2/LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json`;
  Level-0 scout checkpoint `2_740_993` bytes; whole Level-0 outcome
  corpus `7_184_907_119` bytes;
- host filesystem `1_964_601_909_248` bytes total, `400_454_651_904`
  available, single `st_dev` across repo, `runtime/`, `runtime_control/`;
- signed cells `MAX_CONCURRENT_LEASES = 4`, `device_units ∈ 1..4`, file
  count `≤ 16 × device_units`, depth `≤ 2`, `E2 = 12`.

Resulting adequacy: 2.60× the largest immutable checkpoint artifact per
stream; 1 333 such artifacts, or 111 per canonical candidate, inside the
aggregate; 8.58 % of currently available bytes; 4.78× the entire Level-0
outcome corpus; maximum simultaneous live reservation 1 GiB (3.125 % of
the envelope); at most 64 chunks in any one operation's copy/hash loop.

Only the per-operation ceiling scales, and it scales with the declared
stream subset rather than with `device_units`, so a one-stream operation
cannot reserve four streams' worth. The aggregate is a host policy and
scales with nothing. The sizes are read as engineering magnitudes only;
no scientific outcome, learner success, or arm contrast is inferred from
any of them, and no value may be revised on a result-dependent basis.

The envelope is deliberately conservative. Under the mandate that is not
a defect once it is signed before implementation. Raising it requires a
fresh signed author capacity amendment, is forbidden while any operation
is live or any invalidity is unresolved, and may never be enacted in
response to a `NO_CAPACITY` refusal or an `ENOSPC`.

## 6. A3 boundary, stated without over-claim

Under one login UID, each option is mechanical only against a
contract-following worker (K1: no output path and no writable descriptor
at all; K2: the container boundary; K3: the per-file hard rlimit, which
does hold against a deliberate worker inside that process tree). Against
a deliberate same-UID process writing *outside* the accounted roots,
every option is procedural: the supervisor's answer is a fail-closed
refusal (`NO_CAPACITY`, or the `FILESYSTEM` invalidity route), not
prevention. No option claims a kernel compartment, confidentiality,
integrity, or isolation. K2's container is a capacity boundary only — a
same-UID process can still read, modify, and delete its contents.

This boundary is T-development only. It must not be cited, inherited, or
relied upon as Q/C confidentiality, blinding, capacity attestation, or
candidate secrecy, and it may not appear in Q, C, `H_preC`,
`selection_scope_id`, candidate, or claim schemas.

## 7. Consolidated author response template

Exactly one option is selected. Copy, keep one `K:` line, delete the
others, do not combine.

```text
OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION_V1

K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING

# Alternatives (replace the line above if desired):
# K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K2_PREALLOCATED_FILESYSTEM_CONTAINER
# K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K3_RLIMIT_FSIZE_PER_FILE_WITH_LEDGER
```

The selected token also signs the §3 envelope and the §4 invariants of
the packet as written. To sign a different integer, add it on its own
line beneath the token, e.g.
`# T_OUTPUT_AGGREGATE_MAX_BYTES = <exact int>`; any replacement must come
from a filesystem capacity fact, an immutable engineering measurement,
model-size arithmetic, or an explicit author resource commitment, never
from a result.

## 8. What the selection authorizes, and what stays closed

The selection authorizes **only** a later v2.1 correction of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
that embeds the selected token normatively, deletes v2 §V2.7.1's
"no universal constant is invented" position and §V2.7.2's release of the
reservation at the `SETTLEMENT.json`/`FAILED` terminals, applies packet
§3–§4 verbatim, and applies the 24 mechanical repairs of packet §8.

It authorizes nothing else — in particular no implementation, no host
change, and no execution of K2's root prerequisites, which would require
their own operator step and separate author confirmation.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** until v2.1 exists and receives fresh bounded X/Y confirmation
that accepts it. A3, B1, C1, and D1 remain signed and are not reopened by
this packet.

## 9. Negative authorization and custody confirmation

This closure and its packet authorize no implementation, commit, staged
change, host change, root command, mount, quota, loop device, fstab edit,
unit install, import-allowlist edit, supervisor/controller/worker/watchdog
process, FIFO, journal instance, spawn intent, operation, output bound,
promoted object, capability, lease, batch, activation artifact,
production call-graph manifest, entropy, E1/E2/E3 spend, world, learner,
candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim
movement.

Custody: exactly two files were created — the packet and this closure.
No code, test, contract, signature, prior review, or runtime artifact was
edited; the dirty Cursor files and every unrelated untracked file are
preserved unmodified; nothing was committed or staged. Read-only
inspection only: `df`, `stat`, `findmnt`, `/proc/mounts`, `/etc/fstab`,
`lsattr`, `command -v`, `ulimit`, one `python3 -c` capability/`statvfs`
query importing only `os` and `sys`, and `stat`/`du` over existing
immutable artifacts. One command, `tune2fs -l`, was refused by the kernel
with `Permission denied`, and that refusal is recorded as the reason the
project-quota variant is not presented as executable.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent. T remains
`NOT_ACTIVATED` and the programme claim remains `OPEN`.
