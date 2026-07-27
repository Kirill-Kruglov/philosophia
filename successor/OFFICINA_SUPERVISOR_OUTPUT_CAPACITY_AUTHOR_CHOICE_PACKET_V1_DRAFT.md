# Officina supervisor output-capacity author-choice packet — v1 draft

Status: `CANDIDATE_FOR_AUTHOR_SELECTION_NOT_AUTHORIZED`.
Evidence commit: `bff27d4354ca4cdad4ad233260d4db25a595d3f4` (working tree
dirty exactly as handed over; nothing modified by this packet).

Converged X/Y verdict on the supervisor v2 draft:
`REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2` (both lines).
A3/B1/C1/D1 remain signed and are **not** reopened.

This packet presents **one** bounded author cell: the aggregate output
capacity policy and its enforcement provider. It does **not** write the
v2.1 correction. Every other X/Y finding is mechanical and is listed in
§8 for v2.1 to close without a token.

Creates nothing executable. Edits no code, test, contract, signature,
runtime artifact, or existing review. Starts no supervisor, controller,
worker, watchdog, FIFO, journal, smoke, or test. Creates no entropy,
activation, capability, world, learner, output, datum, or scientific
outcome. T remains `NOT_ACTIVATED`.

## Governing hashes

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9ab9ae65d7ddc98164118275dfbf84cc2e188202f606d4239a65abf2861d9f96  reviews/fable_officina_supervisor_control_channel_v2_closure.md
bc731d96d13c8bc6741a94d320ed51ae35cfcbdc38417fedee3ddf3684cec9b2  reviews/opus_officina_supervisor_control_channel_v2_review.md
edfbef915246080a6e022ec5e95e177603c83e542f4068dc1f3ad8d367fcf591  reviews/sol_officina_supervisor_control_channel_v2_review.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
14f798efba2fc664632a15477ea38aea1762481486c8f3fe4ea7bcfe9290d189  successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

---

## 0. Why this is an author cell and not a mechanical repair

Opus (X) holds that an admission-time `os.statvfs` reservation plus a
chunked, ack-servicing hash loop closes the output-byte hole with no
numeric policy cell, and flags a hard signed ceiling as the *conditional*
alternative that would require a token. Sol (Y) holds that a positive
caller-selected integer is not an aggregate resource bound at all, that
released quarantine accounting double-spends the same capacity, and that
one bounded author choice is therefore **required**.

The stricter rule is applied. A dynamic free-space observation alone is
insufficient because:

1. `statvfs` measures the whole filesystem, which is shared with every
   non-Officina consumer on the host; a passing observation at admission
   is not a reservation and can be invalidated by an unrelated writer
   before the first output byte is produced;
2. it bounds neither the supervisor's enumerate/hash/copy work nor the
   number of chunks a settlement loop must execute, so it does not bound
   the liveness cost that X-C3/X-M5 make load-bearing for C1;
3. it does not account for retained quarantine, which v2 §V2.7.2 releases
   at the `FAILED` terminal while the bytes remain on disk (Sol C3.3); and
4. it does not account for accumulated `runtime/T_PROMOTED/**` custody,
   which grows monotonically across the whole of T and is
   archival-excluded, so no signed archival set ever bounds it.

Therefore: **v2.1 may not choose a capacity provider, mechanism, or
number silently.** One selection below is required first.

---

## 1. Platform audit (read-only; no process, probe, or benchmark created)

Exact commands run and exact facts observed at packet authorship. These
are **current-platform observations**, not portable contract guarantees.
A portable guarantee exists only where a selected option turns an
observation into a **fail-closed preflight refusal** executed before any
claim, capability, or worker.

| Command | Observation |
|---|---|
| `findmnt -T . -o TARGET,SOURCE,FSTYPE,OPTIONS` | `/  /dev/mapper/ubuntu--vg-ubuntu--lv  ext4  rw,relatime` |
| `grep ' / ' /proc/mounts` | same; **no `usrquota`, `grpquota`, or `prjquota`** |
| `grep -v '^#' /etc/fstab` | `/ … ext4 defaults 0 1` — no quota option at boot |
| `stat -f -c '…' .` | `bsize=4096 frsize=4096 blocks=479639138 bfree=122150089 bavail=97767318 namelen=255` |
| `python3 -c "os.statvfs('.')"` | `f_frsize=4096 f_blocks=479639138 f_bfree=122150020 f_bavail=97767249` |
| derived | total `1_964_601_909_248` B (1.787 TiB); available to uid 1000 `400_454_651_904` B (372.96 GiB); `f_bfree > f_bavail` ⇒ 5 % root reserve present |
| `stat -c '%d' . successor successor/officina/runtime` | `64513` for all three ⇒ one filesystem ⇒ `os.replace` promotion is EXDEV-free today (X-M8 preflight is satisfiable) |
| `command -v quotaon quotacheck repquota setquota edquota` | **all ABSENT** (no `quota` package installed) |
| `command -v chattr lsattr tune2fs dumpe2fs` | present |
| `lsattr -p -d successor` | `0 --------------e-------` ⇒ project id `0`, no `P` (project-inherit) flag |
| `tune2fs -l /dev/mapper/ubuntu--vg-ubuntu--lv` | `Permission denied … Couldn't find valid filesystem superblock` as uid 1000 ⇒ the ext4 `project`/`quota` superblock features are **not readable without root**; project-quota feasibility here is *unverified*, not merely unconfigured |
| `id` | `uid=1000(master) gid=1000(master) … 27(sudo) …` — root is obtainable interactively by the author; the harness holds no elevated credential |
| `ulimit -f` / `ulimit -Hf` | `unlimited` / `unlimited` ⇒ no inherited `RLIMIT_FSIZE` |
| `command -v mount losetup mkfs.ext4 systemd-run` | all present; every operation needed from them requires root |
| `python3 -c "import sys; sys.version"` | `3.12.3` |
| `hasattr(os, …)` | `posix_fallocate`, `pipe2`, `statvfs`, `truncate`, `ftruncate`, `pwrite`, `sendfile`, `copy_file_range`, `memfd_create`, `O_TMPFILE` — **all present** |
| `src/philosophia/officina/verification.py:35-39` | `ALLOWED_ABSOLUTE_IMPORTS = {__future__, ast, dataclasses, datetime, enum, fcntl, hashlib, hmac, json, os, pathlib, re, subprocess, time, typing, weakref}` — `resource`, `signal`, `select`, `selectors`, `ctypes` **absent** |

No file was written, no probe data was created, no benchmark was run,
and no block device, quota, mount, or loop device was touched.

### 1.1 Portable guarantee vs current observation

| Claim | Status |
|---|---|
| One filesystem holds repo, `runtime/`, and `runtime_control/` | current observation; becomes portable only as a `st_dev`-equality preflight |
| ≥ 372 GiB free | current observation; volatile, shared with the whole host; **never** a reservation |
| No kernel quota is active anywhere in the path | current observation **and** current configuration (`/etc/fstab` has no quota option, quota tools absent) |
| ext4 supports project quota on this device | **unknown** — superblock unreadable without root |
| No `RLIMIT_FSIZE` is inherited | current observation |

---

## 2. Immutable engineering size evidence (outcome-independent)

Existing committed artifacts, read only for their **byte sizes**. No
scientific outcome, learner success, arm contrast, or programme
inference is drawn from any of them; they are used solely as engineering
magnitude anchors for a storage envelope.

| Source | Field / command | Bytes |
|---|---|---|
| `experiments/level_1_contact/feasibility_v2/LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json` (`9d9942c8fb46112784ec1b619addf01a26fd4480ef93918f0fbe1e80b8ee34f6`) | `measurements.trajectory.checkpoint_artifact_bytes` | `25_768_935` |
| `experiments/level_0_grokking/scout/timing-storage-scout_non-outcome.json` (`14bd14093d2f1f081a0e840a0fa3445eda56cca19c74d416aef80308ac295d91`) | `checkpoint.bytes` | `2_740_993` |
| `experiments/level_0_grokking/outcomes/A-3/resume_latest.pt` | `stat -c %s` | `2_739_297` |
| `experiments/level_0_grokking/outcomes/A-3` | `du -sb` | `480_837_024` |
| `experiments/level_0_grokking/outcomes` (9 arms, dense snapshotting) | `du -sb` | `7_184_907_119` |

The largest single immutable checkpoint artifact in the repository's
history is **`25_768_935` bytes (24.58 MiB)**. That value, not a guess, is
the anchor for the per-operation envelope below.

Signed cells reused as arithmetic inputs (unchanged by this packet):
`MAX_CONCURRENT_LEASES = 4`; `device_units ∈ 1..4`; output file count
`≤ 16 × device_units`; path depth `≤ 2`; `E1 = 168` device hours;
`E2 = 12` canonical candidates; `E3 = 48` wall hours or `40` device
hours.

---

## 3. Shared numerical envelope (identical under every option)

The **numbers are not the choice**; the enforcement provider is. Each
option below restates these values as its own pinned envelope, and each
option's mechanism is the only thing that differs in how they are made
true.

```text
T_OUTPUT_PER_STREAM_MAX_BYTES     = 67_108_864       # 64 MiB
T_OUTPUT_PER_OPERATION_MAX_BYTES  = T_OUTPUT_PER_STREAM_MAX_BYTES
                                    * len(declared_stream_indexes)
                                    # ≤ 268_435_456 (256 MiB) at k = 4
T_OUTPUT_AGGREGATE_MAX_BYTES      = 34_359_738_368   # 32 GiB, whole of T
T_OUTPUT_FS_SAFETY_MARGIN_BYTES   = 8_589_934_592    # 8 GiB
T_OUTPUT_COPY_CHUNK_BYTES         = 4_194_304        # 4 MiB
T_OUTPUT_PATH_MAX_BYTES           = 1_024            # full relative path
T_OUTPUT_PATH_COMPONENT_MAX_BYTES = 255
```

Units are bytes throughout, `type(x) is int`, `bool` refused.

**Scaling.** Only the per-operation ceiling scales, and it scales with
`len(declared_stream_indexes)` (a subset of `1..device_units`), not with
`device_units` itself — an operation that declares one stream may not
reserve four streams' worth. The aggregate ceiling is a **host** policy
and does **not** scale with `device_units`, `E1`, or concurrency.

**Adequacy for the signed learner/checkpoint surface (arithmetic only):**

| Quantity | Value |
|---|---|
| Per-stream ceiling ÷ largest immutable checkpoint artifact | `67_108_864 / 25_768_935` = **2.60×** |
| Per-stream ceiling ÷ Level-0 scout checkpoint | `67_108_864 / 2_740_993` = **24.5×** |
| Aggregate ÷ largest immutable checkpoint artifact | `34_359_738_368 / 25_768_935` = **1 333** artifacts |
| Aggregate ÷ maximum-size operation | `34_359_738_368 / 268_435_456` = **128** operations |
| Aggregate ÷ `E2` candidates | 1 333 / 12 = **111** full-size checkpoint artifacts per canonical candidate |
| Aggregate vs whole Level-0 outcome corpus | `34_359_738_368 / 7_184_907_119` = **4.78×** |
| Aggregate vs currently available bytes | `34_359_738_368 / 400_454_651_904` = **8.58 %** |
| Aggregate vs total filesystem | `34_359_738_368 / 1_964_601_909_248` = **1.75 %** |
| Max simultaneous live reservation | `4 × 268_435_456` = `1_073_741_824` (1 GiB) = **3.125 %** of the envelope |
| Max chunks in one operation's copy/hash loop | `268_435_456 / 4_194_304` = **64** |
| Max chunks over the entire envelope, whole of T | `34_359_738_368 / 4_194_304` = **8 192** |

Every input above is a filesystem capacity fact, an immutable engineering
measurement, or signed-constant arithmetic. **No value is derived from a
result, a learner, an arm, a candidate's promise, or a desired outcome,
and none may be revised on any such basis.**

The envelope is deliberately conservative. Under the mandate, that a
number is conservative is not a defect once the author signs it before
implementation. Raising it is defined in §4.5 and requires a fresh
signature, never a supervisor decision.

---

## 4. Invariants identical under every option

These are stated once and are binding under whichever token is selected.
They are not sub-choices.

### 4.1 Complete custody set

```text
accounted_total =  Σ reserved_bytes over ADMITTED / RUNNING / PENDING_SETTLEMENT operations
                 + Σ actual_bytes   over QUARANTINED operations
                 + Σ actual_bytes   over PROMOTED operations retained under runtime/T_PROMOTED/**
                 − Σ released_bytes over operations with a durable disposition record (§4.3)
```

Moving, renaming, or promoting bytes **never** replenishes the envelope:
`os.replace` of `out/` into `runtime/T_PROMOTED/<operation_id>/` changes
the custody root recorded for the operation and nothing else. Only the
one artifact in §4.3 subtracts.

### 4.2 Durable capacity records (control plane, archival-excluded)

All under `successor/officina/runtime_control/T_SUPERVISOR/CAPACITY/`,
canonical ASCII + trailing newline, atomic no-replace, written only by
the supervisor under `T_RUNTIME.lock`, `scientific_outcome: false`,
recursive scientific-field rejection, `type(x) is int`:

| Artifact | Schema | Keys exactly | Effect on `accounted_total` |
|---|---|---|---|
| `<operation_id>.json` | `philosophia.officina.t-operation-capacity.v1` | `schema, scientific_outcome, supervisor_generation_sha256, operation_id, process_id, active_lease_sha256, declared_stream_indexes, reserved_bytes, created_utc` | **adds** `reserved_bytes` |
| `<operation_id>.settled.json` | `philosophia.officina.t-operation-capacity-settled.v1` | `schema, scientific_outcome, operation_id, terminal ∈ {PROMOTED, QUARANTINED}, actual_bytes, custody_root, settled_utc` | **re-measures** the same custody: contribution becomes `actual_bytes`; releases only the over-declaration `reserved_bytes − actual_bytes`; **never** releases retained bytes |
| `<operation_id>.disposed.json` | `philosophia.officina.t-capacity-disposition.v1` | `schema, scientific_outcome, operation_id, author_disposition_sha256, released_bytes, custody_absent (true), disposed_utc` | **the one artifact that releases capacity** |

`SETTLEMENT.json` is the promotion commit point and remains so; it is
**not** a capacity release. A `FAILED`/quarantine terminal is **not** a
capacity release. v2 §V2.7.2's "reservation releases on exactly one
durable terminal (`SETTLEMENT.json` commit, or `FAILED` quarantine
record)" is **deleted** by the selected option.

### 4.3 Reservation lifecycle

**Serve preflight** — executed by the supervisor before it serves any
frame, before any claim, capability, lease, or worker exists; failure
means *no supervisor serves* and every command is refused:

```text
reconstruct accounted_total (§4.4)
require provider_preflight()                       # option-specific, §K1.1 / §K2.1 / §K3.1
require free_bytes ≥ (T_OUTPUT_AGGREGATE_MAX_BYTES − accounted_retained)
                     + T_OUTPUT_FS_SAFETY_MARGIN_BYTES
```

**Pre-admission reserve/refuse predicate** — evaluated under
`T_RUNTIME.lock`, before `BOUND.json`, before `OPERATION.json`, before
any worker exists:

```text
admit(operation) iff
    type(declared) is int  and  declared > 0
and declared ≤ T_OUTPUT_PER_STREAM_MAX_BYTES * len(declared_stream_indexes)
and accounted_total + declared ≤ T_OUTPUT_AGGREGATE_MAX_BYTES
and free_bytes ≥ declared + T_OUTPUT_FS_SAFETY_MARGIN_BYTES
otherwise REFUSED / NO_CAPACITY  (retryable = false)
```

`NO_CAPACITY` is already in v2's closed refusal enum; no new token is
required. `free_bytes = statvfs(accounting_root).f_bavail * f_frsize`.

**Concurrent accounting.** `accounted_total` is held in supervisor memory
and is authoritative only while it equals the reconstruction of §4.4. It
is mutated exclusively under `T_RUNTIME.lock`; concurrency is bounded by
`MAX_CONCURRENT_LEASES = 4`, so the maximum simultaneous live
reservation is `1_073_741_824` bytes.

**Quarantine.** Quarantined bytes continue to consume the envelope at
`actual_bytes` until an authorized deterministic disposal/archive
transition has *actually* removed or transferred custody and the
`t-capacity-disposition.v1` record proves `custody_absent`. A `FAILED`
label alone changes nothing.

### 4.4 Crash reconstruction (fail-closed)

At every generation start and every takeover, under `T_RUNTIME.lock`,
before the first admission:

1. read every `CAPACITY/*.json`; per operation take
   `disposed → 0`, else `settled → actual_bytes`, else
   `admitted → reserved_bytes`;
2. enumerate `runtime/T_PROMOTED/**` and the quarantine root with
   directory-fd + `O_NOFOLLOW`, summing `max(st_size, st_blocks * 512)`
   per operation;
3. per operation use **`max(recorded, enumerated)`** — never the smaller;
4. any operation directory present with **no** capacity record counts as
   the full `T_OUTPUT_PER_OPERATION_MAX_BYTES` at `device_units = 4`
   (`268_435_456`) until a settled or disposition record exists;
5. any accounted path that cannot be read or enumerated ⇒ refuse all
   admission (`NO_CAPACITY`); never assume zero.

A partially written tree is never re-measured downward while its
operation is non-terminal: the conservative `reserved_bytes` stands.

### 4.5 Retention and disposal

**Outputs are retained for the whole of T.** There is no deterministic
class-based deletion rule, no TTL, no size-pressure eviction, and no
automatic disposal.

Disposal requires a **signed author disposition artifact** that names
exactly: operation ids, their recorded byte counts, and the destination
(absent or a named archive). The supervisor validates the artifact's
signature, proves custody absence, and writes
`t-capacity-disposition.v1`. The artifact may cite only operation id,
operation kind, terminal class, byte count, and timestamps. It may
**not** cite result bytes, result hashes, learner state, candidate
identity, or any judgement that an output looks promising, failed
usefully, or helps a desired candidate.

Raising `T_OUTPUT_AGGREGATE_MAX_BYTES` requires a **new signed author
capacity amendment**. It is forbidden while any operation is live and
while any invalidity is unresolved, and it may never be enacted in
response to a `NO_CAPACITY` refusal, an `ENOSPC`, or a partially
completed operation. The supervisor can never raise it.

### 4.6 Liveness

- Enumeration work per operation is bounded by the signed grammar: file
  count `≤ 16 × device_units ≤ 64`, depth `≤ 2`, component
  `≤ 255` bytes, full relative path `≤ 1_024` bytes.
- Copy/hash work per operation is bounded by the frozen reservation:
  `≤ 268_435_456` bytes, i.e. `≤ 64` chunks of `T_OUTPUT_COPY_CHUNK_BYTES`.
- Between every two chunks the supervisor **must** execute one watchdog
  update/ack service step and one control-frame poll step (closing
  X-M5's mass-freeze cascade). No uninterrupted work exceeds one chunk.
- The serve loop is a `time`-paced nonblocking poll: `select`/`selectors`
  are absent from the import allowlist.
- **`ENOSPC` / `EDQUOT` / `EFBIG` / `SIGXFSZ` (any provider):** stop
  writing, kill the worker group, prove death, record the conservative
  reservation, route the operation to the signed record-first invalidity
  terminal with public cause `FILESYSTEM`, and refuse all further
  admission until a signed disposition exists. **Never** delete anything
  to make room; never retry automatically; never lower a reservation.
- **Sparse files:** counted at full logical `st_size`, and every
  reservation charge uses `max(logical st_size, st_blocks * 512)`.
- **Restart:** a crashed copy/hash never resumes from an offset and never
  respawns the worker (X-M7). It is a quarantine terminal at the
  conservative `reserved_bytes` until a disposition. Streaming SHA-256
  state is not serializable and no contract text may assume otherwise.
- **Filesystem safety margin:** `8_589_934_592` bytes, enforced by the
  serve preflight and by every admission.

### 4.7 The A3 boundary (identical bar under every option)

Under one login UID:

- **Mechanical** for a contract-following worker: bytes are stopped by
  the option's provider at the pinned limit, during production.
- **Procedural** against a deliberate same-UID process: it may `open()`
  and `write()` any path its UID can reach, including outside the
  accounted roots, and exhaust the filesystem. No option claims a kernel
  compartment against that, and none may be described as one.
- The supervisor's response to a deliberate exhaustion is a fail-closed
  **refusal** (`NO_CAPACITY`, or the `FILESYSTEM` invalidity route), not
  prevention.
- This boundary is **T-development only**. It must not be cited,
  inherited, or relied upon as Q/C confidentiality, blinding, capacity
  attestation, or candidate secrecy, and it may not appear in Q, C,
  `H_preC`, `selection_scope_id`, candidate, or claim schemas.

### 4.8 Negative rules binding on all options

No option may: make output capacity depend on a result; expose byte
counts, file counts, or capacity state to a controller before settlement
(v2 §V2.2.3 fixed pending shapes stand); add a ninth control command;
add a public CLI command; add a production root; change a signed runtime
event, schema, constant, or the roots tuple; or move `E1`/`E2`/`E3`.

---

## Option K1 — Supervisor-mediated bounded output transport with a fixed signed ceiling

### K1.1 Enforcement architecture

The worker is given **no writable output directory and no output
pathname**. `operations/<operation_id>/out/` is created and held by the
supervisor alone; the worker inherits exactly two descriptors — the
existing status pipe and one `os.pipe2(O_CLOEXEC)` **output write end**.

Bytes are stopped *in the data path*, not counted after exit:

1. The worker emits, per output file, one canonical ASCII JSON line
   frame terminated by `\n` and `≤ 4096` bytes —
   `philosophia.officina.t-worker-output-frame.v1`, keys exactly
   `schema, scientific_outcome, operation_id, relative_path,
   content_bytes` — followed by exactly `content_bytes` raw bytes.
2. The supervisor validates the path grammar **before** creating
   anything: relative, non-empty, no `.`/`..`, no absolute, no NUL,
   unique within the operation, depth `≤ 2`, component
   `≤ 255` bytes, full path `≤ 1_024` bytes, count `≤ 16 × device_units`.
3. It opens the file itself:
   `os.open(rel, O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,
   dir_fd=out_dirfd)`. The worker never holds this descriptor.
4. It copies in `T_OUTPUT_COPY_CHUNK_BYTES` chunks, **hashing in the same
   single pass** (no second read of the bytes ever occurs), servicing one
   watchdog ack step and one control poll step between chunks.
5. On the chunk that would make `bytes_written + len(chunk) > reserved`,
   it writes **nothing further**, closes the pipe read end — the worker's
   next `write` takes `EPIPE`/`SIGPIPE` and stops producing — `killpg`s
   the worker group, proves death, and routes the operation to the
   quarantine terminal at the conservative `reserved_bytes`.

Backpressure is inherent: a worker that outruns the supervisor blocks on
a full pipe and is covered by the C1 watchdog deadline like any other
blocked controller work.

Because the supervisor is the only writer, no sparse file can be created
in `out/`, the count is the supervisor's own counter rather than a
directory scan, and the copy/hash pass is bounded by the reservation by
construction. After group death the supervisor re-verifies `st_size`,
`st_ino`, and `st_nlink` from its **held** descriptors and fails closed
on any mismatch (X-M7).

*Preflight (`provider_preflight`)*: `os.pipe2` available;
`fpathconf(fd, PC_PIPE_BUF) ≥ 4096` on the output pipe;
`st_dev(operations root) == st_dev(runtime/T_PROMOTED)` (X-M8, EXDEV);
`out/` creatable and writable by the supervisor. Any failure ⇒ no serve.

**A plain integer ledger and a bare `statvfs` check are not enforcement,
and neither is offered as one here** — the ledger of §4.2 is the
*accounting*; the pipe is the *enforcement*.

### K1.2 Numerical envelope

Exactly §3: per-stream `67_108_864`; per-operation
`67_108_864 × len(declared_stream_indexes)` (`≤ 268_435_456`); aggregate
`34_359_738_368`; margin `8_589_934_592`; chunk `4_194_304`. Scaling and
adequacy arithmetic as §3. Sources: filesystem capacity facts (§1), the
immutable `25_768_935`-byte checkpoint artifact and the `2_740_993`-byte
scout checkpoint (§2), and signed-constant arithmetic. Outcome-independent
in every term.

### K1.3 Complete custody set

§4.1 exactly. Live output = the supervisor's own write counter; pending
settlement, quarantine, and retained `runtime/T_PROMOTED/**` are all
carried at `actual_bytes`; promotion is a custody-root change only.

### K1.4 Reservation lifecycle

§4.2–§4.4 exactly. The one artifact that releases capacity is
`CAPACITY/<operation_id>.disposed.json`
(`philosophia.officina.t-capacity-disposition.v1`). Quarantine consumes
until that record proves `custody_absent`.

### K1.5 Retention / disposal

§4.5 exactly: retained for the whole of T; disposal only under a signed
author disposition; ceiling raised only by a new signed amendment.

### K1.6 Liveness

§4.6 exactly. `ENOSPC` on a supervisor write is the `FILESYSTEM`
invalidity route. Sparse files cannot arise in `out/`. A crashed copy is
a quarantine terminal, never a resumed offset, never a respawned worker.

### K1.7 A3 boundary

§4.7. **Mechanical** for contract-following workers in an unusually
strong form: the worker holds no output path and no writable descriptor,
so even an accidental oversized write is stopped by the supervisor's
counter and the pipe close. **Procedural** against a deliberate same-UID
worker, which can `open()` reachable paths directly and consume the
filesystem outside the accounted roots — refused, not prevented. No
kernel isolation is claimed. Not Q/C-citable.

### K1.8 Deployment and code surface

- **Host setup: none.** No root, no mount, no fstab, no unit, no package.
- **Portability:** POSIX pipes + `statvfs`. No ext4, quota, or Linux
  rlimit dependency.
- **Import allowlist delta: none** (`os.pipe2`, `os.read`, `os.write`,
  `os.open` with `dir_fd`, `os.statvfs`, `hashlib`, `json` are all
  already allowed).
- **Frozen-file delta: none.** `verification.py`, `runtime.py`,
  `ledger.py`, `checkpoint.py`, `activation.py`, signed events, schemas,
  constants, and the roots tuple stay byte-unchanged.
- **New production root: none.** No ninth command, no public CLI command.
- **Signed runtime events: unchanged.** New objects are control plane and
  archival-excluded (`runtime_control/**`, `runtime/T_PROMOTED/**`),
  and remain untracked.
- **Power cycle:** enforcement is code plus the durable capacity ledger,
  so it survives reboot unconditionally; the serve preflight and §4.4
  reconstruction re-establish it before the first admission.
- **v2.1 code surface:** `generic_harness.py` and its tests only.

**Selection token:**

```text
I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

---

## Option K2 — Preallocated dedicated filesystem container (real kernel capacity provider)

### K2.1 Enforcement architecture

A fixed-size ext4 image is preallocated on a loop device and mounted as
the **accounting root**; both `operations/` and `T_PROMOTED/` are
relocated under that mount. The filesystem *is* the quota: the kernel
returns `ENOSPC` to the writing process at the container boundary, during
production, regardless of which process writes. The worker keeps v2's
direct `out/` write model.

*Root prerequisites (exact, one-time, before any T activation):*

```text
fallocate -l 51539607552 /var/lib/officina-t/OFFICINA_T_OUTPUT.img
mkfs.ext4 -m 0 -F        /var/lib/officina-t/OFFICINA_T_OUTPUT.img
mkdir -p <repo>/successor/officina/runtime_capacity
chown 1000:1000 <repo>/successor/officina/runtime_capacity
# /etc/fstab — REQUIRED for the enforcement to survive a power cycle:
/var/lib/officina-t/OFFICINA_T_OUTPUT.img <repo>/successor/officina/runtime_capacity ext4 loop,nosuid,nodev,noexec,noatime 0 2
mount <repo>/successor/officina/runtime_capacity
```

*Preflight (`provider_preflight`, fail-closed, before any serve):*

```text
require st_dev(accounting_root) != st_dev(repo_root)          # a real mount, not a directory
require statvfs(accounting_root).f_blocks * f_frsize
        ≥ T_OUTPUT_AGGREGATE_MAX_BYTES + T_OUTPUT_FS_SAFETY_MARGIN_BYTES
require st_dev(operations root) == st_dev(T_PROMOTED root)    # X-M8, EXDEV
```

Absent the mount, `st_dev` equals the repo root and the supervisor
refuses to serve. This is the one option whose aggregate bound is
enforced by the kernel against **any** same-UID writer inside the
container, and `nosuid,nodev,noexec` additionally prevent executing
anything written there.

Rejected sub-variant — **ext4 project quota on `/`**: `quotaon`,
`quotacheck`, `repquota`, `setquota`, `edquota` are all absent (no
`quota` package); `/` is mounted `rw,relatime` with no `prjquota` and
`/etc/fstab` carries no quota option; `lsattr -p -d successor` shows
project id `0` with no `P` inherit flag; and `tune2fs -l` on the device
is `Permission denied` for uid 1000, so it is **not verifiable here**
whether the root filesystem even carries the `project`/`quota`
superblock features. It would additionally require a remount or reboot
of the root filesystem. **It is not presented as executable.**

### K2.2 Numerical envelope

Exactly §3, plus one provider constant:

```text
T_OUTPUT_CONTAINER_BYTES = 51_539_607_552   # 48 GiB image
```

`48 GiB` ≥ `32 GiB` envelope + `8 GiB` margin with room for ext4 metadata
overhead at `-m 0`. The container is `2.63 %` of the `1.787 TiB`
filesystem and `12.9 %` of currently available bytes — a permanent
allocation, taken once, that no other host consumer can reclaim.
Per-operation and aggregate values, scaling, and adequacy arithmetic are
identical to §3 and rest on the same outcome-independent sources.

### K2.3 Complete custody set

§4.1 exactly, with one strengthening: because all four custody classes
live inside one container, `statvfs(accounting_root)` is an independent
second witness for `accounted_total` and any divergence beyond the
enumeration granularity is a fail-closed refusal.

### K2.4 Reservation lifecycle

§4.2–§4.4 exactly, plus: admission additionally requires
`statvfs(accounting_root).f_bavail * f_frsize ≥ declared`, evaluated on
the container rather than on `/`. Release artifact:
`CAPACITY/<operation_id>.disposed.json` — unchanged.

### K2.5 Retention / disposal

§4.5 exactly.

### K2.6 Liveness

§4.6, with `ENOSPC` now the *ordinary* provider stop signal rather than a
host-wide emergency: the worker's write fails at the container boundary,
the supervisor kills the group, records the conservative reservation, and
routes to the `FILESYSTEM` invalidity terminal. Enumerate/hash/copy still
run **after** worker exit under this option (v2's direct-write model), so
the chunked, ack-serviced loop of §4.6 is mandatory and the dual
logical/allocated sparse rule of v2 §V2.7.2 is retained in full.

### K2.7 A3 boundary

§4.7, with the strongest honest statement available: the container
boundary is enforced by the kernel against a deliberate same-UID process
**for writes inside the container**. It provides **no** protection
against a deliberate same-UID process writing outside the container, and
it is not a confidentiality, isolation, or integrity compartment — a
same-UID process can still read, modify, and delete container contents.
Not Q/C-citable.

### K2.8 Deployment and code surface

- **Host setup: root required**, exactly as listed in §K2.1, including an
  `/etc/fstab` entry. Without fstab the mount does not survive a power
  cycle and the supervisor's preflight will correctly refuse to serve
  after reboot — enforcement fails closed but availability is lost until
  an operator remounts.
- **Portability:** Linux + loop devices + ext4. Does not port to a host
  where the author lacks root.
- **Import allowlist delta: none.**
- **Frozen-file delta: none** in Python, but the **path layout changes**:
  `operations/` and `runtime/T_PROMOTED/` move under
  `successor/officina/runtime_capacity/`, which touches v2 §V2.3's object
  table, §V2.9.4's archival exclusions, and the activation-protocol
  clean-HEAD/untracked rule (a mountpoint inside the repository tree).
- **New production root: none.** No new command.
- **Signed runtime events: unchanged.**
- **Not immediately executable on this host**: the mount does not exist,
  and creating it requires root and a reboot-persistent fstab edit.

**Selection token:**

```text
I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K2_PREALLOCATED_FILESYSTEM_CONTAINER
```

---

## Option K3 — Kernel `RLIMIT_FSIZE` per-file cap on the worker tree, plus the aggregate ledger

### K3.1 Enforcement architecture

The worker keeps v2's direct `out/` write model. Before `exec`, the
supervisor lowers `RLIMIT_FSIZE` for the worker process via
`subprocess.Popen(preexec_fn=…)` calling
`resource.setrlimit(resource.RLIMIT_FSIZE, (n, n))`. The kernel then
stops writes past `n` bytes **in any single file**: the write returns
`EFBIG` or the process takes `SIGXFSZ` (default action: terminate). The
limit is inherited by every descendant and, being a **hard** limit
lowered by an unprivileged process, cannot be raised again by the worker
or any child — so the per-file bound holds even against a *deliberate*
same-UID worker inside that process tree.

*Preflight (`provider_preflight`)*: `resource.getrlimit(RLIMIT_FSIZE)`
readable; a lowered limit verified to be actually installed in the child
(observed by the supervisor from `/proc/<pid>/limits` after the stopped
bootstrap and before `SIGCONT`); `st_dev` promotion equality (X-M8). Any
failure ⇒ no serve, no admission.

**Honest limit of this provider.** `RLIMIT_FSIZE` bounds bytes **per
file**, not per tree. The file-count cap (`≤ 16 × device_units`) is part
of the output grammar and is checked by the supervisor *after* worker
exit, so a worker that ignores the count can create arbitrarily many
files each under `n`. The aggregate ceiling under K3 therefore rests on
the §4.2 ledger plus the `statvfs` margin, not on the kernel — the kernel
contributes a hard per-file stop only. This is materially weaker than K1
and K2 for the aggregate cell that this packet exists to close.

### K3.2 Numerical envelope

Exactly §3, plus one provider constant:

```text
T_OUTPUT_PER_FILE_RLIMIT_BYTES = 4_194_304   # 4 MiB
```

Chosen so that the grammar-capped file count reproduces the §3 ceiling
exactly: `16 × device_units` files × `4_194_304` bytes
= `67_108_864 × device_units`. The installed limit is
`min(T_OUTPUT_PER_FILE_RLIMIT_BYTES, reserved_bytes)`. Note that
`4_194_304` is **smaller than the immutable `25_768_935`-byte checkpoint
artifact**, so under K3 a checkpoint must be emitted as ≥ 7 shards; that
is a real constraint on the signed learner/checkpoint surface and is
stated here rather than discovered at implementation.

### K3.3 Complete custody set

§4.1 exactly.

### K3.4 Reservation lifecycle

§4.2–§4.4 exactly. Release artifact:
`CAPACITY/<operation_id>.disposed.json` — unchanged.

### K3.5 Retention / disposal

§4.5 exactly.

### K3.6 Liveness

§4.6. `EFBIG`/`SIGXFSZ` is the provider stop; `ENOSPC` remains the
host-wide `FILESYSTEM` invalidity route. Enumerate/hash/copy run after
worker exit, so the chunked ack-serviced loop and the dual
logical/allocated sparse rule are mandatory in full.

### K3.7 A3 boundary

§4.7, refined: the **per-file** bound is mechanical against a deliberate
same-UID worker inside the launched process tree (hard rlimits are
irreversible downward for unprivileged processes). The **aggregate**
bound is not mechanical under K3 — a deliberate worker can create
unbounded files under the per-file cap, and the count grammar is only
checked afterward. Do not describe K3 as kernel-enforced aggregate
capacity. Not Q/C-citable.

### K3.8 Deployment and code surface

- **Host setup: none.** No root.
- **Portability:** POSIX rlimits.
- **Import allowlist delta: `resource`** must be added to
  `ALLOWED_ABSOLUTE_IMPORTS` — which means editing
  `src/philosophia/officina/verification.py`, a file v2 §V2.10 pins as
  **byte-unchanged frozen**. This requires an explicit unfreeze and a
  fresh signature over the quarantine verifier's own surface, and it
  widens the verified import surface for every future audit. That is the
  dominant governance cost of this option.
- **`preexec_fn` caveat:** documented as unsafe in multithreaded
  processes; the supervisor is single-threaded (`threading` is not in the
  allowlist), so it is usable — but it must be stated, not assumed.
- **Frozen-file delta:** `verification.py` (see above).
- **New production root: none.** No new command.
- **Signed runtime events: unchanged.**
- **Power cycle:** enforcement is code plus the durable ledger; survives
  reboot; re-established by the serve preflight.

**Selection token:**

```text
I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K3_RLIMIT_FSIZE_PER_FILE_WITH_LEDGER
```

---

## 5. Comparison and recommendation

| | K1 transport | K2 container | K3 rlimit |
|---|---|---|---|
| Bytes stopped during production | yes — supervisor counter + pipe close | yes — kernel `ENOSPC` at container boundary | yes — kernel `EFBIG`/`SIGXFSZ` per file |
| Aggregate bound mechanical? | yes, for contract-following workers; supervisor is the sole writer | **yes, kernel, against any same-UID writer inside the container** | **no** — per-file only |
| Bounds hash/copy work | **yes, single streaming pass, by construction** | after exit; needs the chunked loop | after exit; needs the chunked loop |
| Enforceable on this host today | **yes** | no — needs root + mount + fstab | yes |
| Root / system administration | none | **required** | none |
| Import allowlist delta | none | none | **`resource`** |
| Frozen-file delta | none | none | **`verification.py` unfreeze** |
| Path layout change | none | `operations/` + `T_PROMOTED/` move under a mountpoint | none |
| Survives power cycle | yes | only with the fstab entry | yes |
| Constrains checkpoint shape | no | no | **yes — 4 MiB shards** |
| Fail-closed preflight available | yes | yes (but the mount must exist) | yes |

**Recommendation: K1.**

Reasoning, against the mandate's bar:

1. **Enforceability today.** K1 is enforceable on the current host with a
   fail-closed preflight, no root, and no host policy change. K2 is the
   strongest kernel guarantee but is **not immediately executable** here —
   the mount does not exist and creating it needs root plus a
   reboot-persistent fstab edit — so under the mandate it may not be
   recommended. K3 is executable but does not deliver the aggregate bound
   this cell exists to close.
2. **It bounds the work, not only the bytes.** K1 is the only option in
   which the supervisor reads each output byte exactly once, hashing in
   the same pass. That collapses X-C3's unbounded-work cascade and
   X-M5's mass-freeze cascade at the source, and it makes X-M7's
   restartable-hash defect moot because there is no separate hash pass to
   restart.
3. **Lowest governance and implementation complexity.** Zero allowlist
   delta, zero frozen-file delta, zero new root, zero new command, zero
   path relocation, zero signed-event movement. K3's price is unfreezing
   the quarantine verifier — the highest governance cost of the three for
   the weakest guarantee.
4. **It closes the custody gap Sol raised.** Retained quarantine and
   accumulated `T_PROMOTED` custody are inside the accounted total and
   are released by exactly one signed artifact; a rename can never
   replenish the envelope.

**Select K2 instead** if the author wants the aggregate ceiling enforced
by the kernel against a deliberate same-UID process and accepts the root
prerequisite, the permanent 48 GiB allocation, and the path relocation.
K2 is the correct pick for that requirement — but the prerequisites in
§K2.1 must be executed and verified *before* v2.1 is written, not
assumed.

**Select K3** only if the author specifically wants v2's direct-write
worker model preserved and accepts both the `verification.py` unfreeze
and 4 MiB checkpoint sharding. It is listed as executable and is **not
recommended**.

---

## 6. What the selection authorizes

The selection authorizes **only** a later v2.1 correction of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
that:

1. embeds the selected token's normative text (not by reference alone);
2. deletes v2 §V2.7.1's "no universal constant is invented" position and
   §V2.7.2's "reservation releases on exactly one durable terminal
   (`SETTLEMENT.json` … or `FAILED` quarantine record)";
3. applies §3 and §4 of this packet verbatim as the capacity contract;
4. applies every mechanical X/Y repair in §8 below; and
5. still leaves `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
   **not signable** until a fresh bounded X/Y confirmation of v2.1
   accepts it.

It authorizes no implementation, no process, no host change (including
K2's root prerequisites, which would need their own operator step and
author confirmation), and no scientific movement.

---

## 7. Consolidated author response template

Copy, keep exactly one `K:` line, delete the others. Do not combine
options.

```text
OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION_V1

K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING

# Alternatives (replace the line above if desired):
# K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K2_PREALLOCATED_FILESYSTEM_CONTAINER
# K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K3_RLIMIT_FSIZE_PER_FILE_WITH_LEDGER
```

Selecting a token also signs the §3 envelope
(`67_108_864` per stream, `34_359_738_368` aggregate, `8_589_934_592`
margin) and the §4 invariants as written. To sign a different number,
replace the value on its own line beneath the token, e.g.:

```text
# T_OUTPUT_AGGREGATE_MAX_BYTES = <exact int>
```

Any replacement value must come from a filesystem capacity fact, an
immutable engineering measurement, model-size arithmetic, or an explicit
author resource commitment — never from a result.

---

## 8. Mechanical (non-choice) X/Y repairs for v2.1

Listed so the author can see that the capacity cell is the only cell.
Each has one determinate repair against v2's own text or already-signed
composite, and none requires a token.

| Finding | Mechanical repair locus |
|---|---|
| X-C1 / Sol C1 semantic request hash, `idempotency_key` derivation, demote key-reuse from record-first invalidity | §V2.4.2, §V2.5 |
| Sol C1 immutable phase-file journal layout, effect reducer, key allocation | §V2.3, §V2.5 |
| X-C2 / Sol C5 `spawn_intent_id` in child argv + `/proc/*/cmdline` takeover scan; self-stop timeout; `BOOTSTRAP` refusal token | §V2.1.4, §V2.1.6, §V2.4.5 |
| X-C3(1–3) / Sol C3.1 `OPERATION_ADMIT` as the sole bound-installer; drop `output_bound_sha256` circularity; define the operation directory key | §V2.4.4, §V2.7.1, §V2.7.3 |
| X-C3(4) / Sol C3.2–3.3 aggregate capacity | **this packet — author cell** |
| X-C4 / Sol C4 forbid `T_PROCESS_RESOURCE_STOP` for watchdog freezes; pin cause `PROCESS`; delete or constantise the zero-overrun branch; watchdog writes the freeze observation, or `FREEZE_TIME_UNKNOWN` ⇒ invalidity | §V2.6.4–§V2.6.5 |
| X-C5 split takeover into a client control-plane phase and a supervisor settlement phase | §V2.1.6, §V2.9.1 |
| X-C6 / Sol M2 define `t-operation-admission.v1`, one ack schema, the `FAILED`/quarantine artifact, mandatory `CHILDREN/<process_id>/` rename, per-object retention actor | §V2.3, §V2.5 |
| Sol C2 separate effect-ack from delivery redemption; bounded status protocol; key tombstones | §V2.4.4, §V2.5 |
| Sol C3.4 map every failure class to a signed process/global route | §V2.7, §V2.8 |
| X-M1 in-process post-fork entry; delete argv tokens; pin how the controller learns its inherited fd numbers | §V2.1.2, §V2.10 |
| X-M2 / Sol M2 bound frame, path, and `argv` bytes; one `INVALID` token for oversize | §V2.4.2, §V2.4.5 |
| X-M3 `\n`-delimited frames; canonical `reply_fifo` path; `ENXIO` route | §V2.4.1 |
| X-M4 / Sol M1 move "escaped children" to the A3 procedural residual; add the fail-closed quiescence proof; reject controller descendants at the FIFO role check | §V2.2.1–§V2.2.2, §V2.6.4 |
| X-M5 ack liveness judged on the watchdog's own monotonic sample; supervisor poll cadence constant; ack service inside every long loop | §V2.6.3, §V2.6.6 |
| X-M6 durable `SPAWNING.json` marker; bounded CLI wait; identity-install collision route | §V2.1.2 |
| X-M7 delete the after-crash offset claim; hold descriptors through settle; re-verify before commit | §V2.7.2, §V2.7.4 |
| X-M8 same-`st_dev` preflight; idempotent completion predicate; `T_PROMOTED` creation/mode rule | §V2.7.4 |
| X-M9 add harness §5a to the replacement index; remove the client-triggerable G5 | §V2.0, §V2.5 |
| X-M10 include `process_sequence` in `spawn_intent_id`; pin `created_utc` resolution | §V2.1.4 |
| X-M11 / Sol M2 add `ALREADY_DELIVERED` to both enums | §V2.4.5, §V2.9.3 |
| Sol M1 collapse pre-terminal status to one fixed `PENDING` detail | §V2.2.3, §V2.4.5 |
| X minors 1–7 no signal dispositions before self-stop; define the capability invariant instead of "behavior-capable"; client reply-timeout continuation; `REPLY/` rules; adopt §3 durability for `runtime_control/**`; truthfulness qualifier on the mechanical list; keep control paths untracked | as listed |

---

## 9. Negative authorization

This packet authorizes only Kirill's selection of exactly one `K` token
(and, optionally, an explicit replacement of a pinned integer under the
rules of §7), followed by the later drafting of a v2.1 correction from
that selection plus the mechanical ledger of §8.

It authorizes **no** implementation, commit, host change, root command,
mount, quota, loop device, fstab edit, unit install, allowlist edit,
supervisor/controller/worker/watchdog process, FIFO, journal instance,
spawn intent, operation, output bound, promoted object, capability,
lease, batch, activation artifact, production manifest, entropy,
E1/E2/E3 spend, world, learner, candidate, Q/C object, datum, outcome,
Proof, or claim movement.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. `successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent. T remains
`NOT_ACTIVATED` and the programme claim remains `OPEN`.
