# Officina supervisor process-authority selection v1

Selected by Kirill Kruglov on 2026-08-02.

Selection base: commit
`ee7a1973e752ac11442ac8cde6c12b00c859484c`.

Governing packet verdict:
`READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION`.

## Selected token

```text
OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1

P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

## Selected meaning

- One clean, constructed Process-Control Server holds every PID and all
  process-control authority for the middle process, controllers, workers, and
  every watchdog.
- The contaminated supervisor receives opaque handles only. It cannot express
  a PID and does not call `fork`, `Popen`, `waitpid`, `kill`, or `killpg` on a
  result-bearing path.
- Every watchdog is created as an isolated role by the PCS. Supervisor death is
  detected through the watchdog update-pipe EOF. The additional direct-parent
  `getppid()` detector is deliberately not retained under P1.
- Watchdog death and replacement are mediated through the PCS, giving the same
  one-detector process model to the first watchdog and every replacement.
- The PCS is a mandatory resident process. Its loss is an unrecoverable
  whole-generation process invalidity; a new PCS may not adopt a live
  generation.
- `t-pcs.v1` introduces a second durable control-plane journal. Descriptor-
  bearing replies transfer capabilities through Linux `SCM_RIGHTS`; their byte
  records are replayable, but the descriptors themselves are never redelivered.
  This is an explicitly accepted narrowing of B1 on that channel.
- The selected architecture remains Linux/x86_64-specific, uses five production
  roots, and retains `_socket`/`SCM_RIGHTS` in the reviewed control surface.

P3 is rejected because it leaves contaminated-supervisor process authority as
an open Major defect. P4 is not selected because its hybrid authority model
retains `waitpid` in the supervisor, cannot safely signal a wedged watchdog,
and degrades replacement watchdogs to the same one-detector model as P1 while
carrying additional first-versus-replacement asymmetry.

## Mandatory binding repair

The selected P1 architecture must be emitted as one operative composite before
independent review. The binding correction must:

- delete P3/P4 and every branch-only count, table, token, and test obligation;
- bind the exact P1 process tree, protocols, descriptor ownership, journal,
  crash, invalidity, import, verifier, and test surfaces;
- preserve the v2.1.10.3 corrections to role-bootstrap imports,
  `generic_harness.py`'s `_socket` requirement, and removal of the unsafe global
  `/proc/self/fd` remediation sweep;
- correct the remaining statement that an unparsed installed descriptor would
  be merely a resource fact: an `SCM_RIGHTS` descriptor is a capability. Any
  possible unparsed installed descriptor must be contained by an immediate
  fail-closed process exit and described as a transient capability leak, or the
  pinned Linux semantics must prove it cannot exist;
- receive fresh independent X-line and Y-line review on identical bytes.

## Authorization boundary

This selection authorizes only preparation of the P1 binding correction and
its review prompts. It does not accept that future composite and does not make
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` signable.

It authorizes no implementation, code or test edit, verifier or manifest edit,
host change, process/socket/pipe/FIFO/fork/exec/signal operation, supervisor,
controller, worker or watchdog, journal instance, activation artifact,
capability, world, learner, entropy, E1/E2/E3 spend, Q/C object, datum, outcome,
Proof, or claim movement. T remains `NOT_ACTIVATED`; the programme claim remains
`OPEN`.

## Governing hashes

```text
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
d46414389187bb87068e5105a0a914a56f5f49f1244bdb5b527ccea89acba18c  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md
0b9b67f7d57892012df3ad44e6f943a8c8ccf0eb8ed71d966d88b694b8ca5163  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_cell_p_completion_chat_response.md
```

The exact selected token and this formal signature govern. The saved chat
response is a provenance aid only.
