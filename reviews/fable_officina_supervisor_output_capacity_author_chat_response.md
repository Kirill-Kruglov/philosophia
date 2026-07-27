I'll start by reading the required context files.

I have the full picture. Writing the two deliverables now.

`READY_FOR_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION`

Two files created, nothing else touched:

- [OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md](successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md)
- [fable_officina_supervisor_output_capacity_author_choice_packet_v1.md](reviews/fable_officina_supervisor_output_capacity_author_choice_packet_v1.md)

## The cell

Applied the stricter rule over Opus vs Sol. A `statvfs` observation cannot represent two custody facts: retained quarantine (which v2 §V2.7.2 releases at `FAILED` while the bytes stay on disk) and monotonically accumulating archival-excluded `runtime/T_PROMOTED/**`. Those are custody, not free space — so one author cell stands, and v2.1 may not pick a provider or a number silently.

## Three options

| | Enforcement | Root | Allowlist | Frozen files | Executable here |
|---|---|---|---|---|---|
| **K1** supervisor-mediated transport | worker gets no output path; every byte written by the supervisor through an inherited pipe, counted + hashed in one pass, pipe closed at the ceiling | no | none | none | **yes** |
| **K2** preallocated ext4 container on loop | kernel `ENOSPC` at the container boundary | **yes** | none | paths relocate | **no** |
| **K3** hard `RLIMIT_FSIZE` per file | `EFBIG`/`SIGXFSZ`, irreversible for the worker tree | no | **`resource`** | **`verification.py`** | yes |

**Recommended K1** — only option enforceable today with a fail-closed preflight, and the only one that bounds the supervisor's own hash/copy work by construction (single streaming pass, 4 MiB chunks, watchdog ack serviced between chunks), which also collapses X-C3's unbounded-work and X-M5's mass-freeze cascades.

K2 is the strongest kernel bound but not immediately executable: the mount doesn't exist, needs root plus a reboot-persistent fstab entry. The ext4 project-quota variant is rejected outright — quota tools absent, no `prjquota` in `/proc/mounts` or `/etc/fstab`, and `tune2fs -l` returns `Permission denied` for uid 1000, so the superblock features aren't even verifiable. K3 is executable but per-file only, costs unfreezing the quarantine verifier, and its 4 MiB limit is below the largest immutable checkpoint artifact.

## Numbers

64 MiB per stream (×`len(declared_stream_indexes)`, ≤ 256 MiB), 32 GiB aggregate for all of T, 8 GiB filesystem margin. Anchored on `checkpoint_artifact_bytes = 25_768_935` from the Level-1 feasibility v2 report (2.60× per stream; 1,333 such artifacts inside the aggregate; 8.58% of the 373 GiB currently free) — sizes read as engineering magnitudes only, no outcome inferred.

Capacity is released by exactly one artifact (`t-capacity-disposition.v1`, proving `custody_absent`); `SETTLEMENT.json` and `FAILED` release nothing, so a rename can't replenish. Outputs retained for all of T; disposal needs a signed author artifact that may cite only ids, kinds, terminals, and byte counts.

Packet §8 maps the 24 remaining X/Y findings to determinate v2.1 loci — both reviewers independently agree they're mechanical. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` stays unsignable until v2.1 gets fresh bounded X/Y confirmation; T `NOT_ACTIVATED`, claim `OPEN`, runtime dir still just `T_RUNTIME.lock`.
