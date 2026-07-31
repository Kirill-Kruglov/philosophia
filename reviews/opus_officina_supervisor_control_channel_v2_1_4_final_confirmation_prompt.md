# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.4 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.4; its correction, closure, and chat response are author claims,
not review evidence. Re-derive the result from the normative bytes.

Work in `philosophia` at or after commit
`d6be6b246e853dacb2ce209b2341dfd0d5313da0`. Read the complete
v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4 supervisor chain, both author signatures,
the inherited generic-harness and batch-settlement contracts, and both
independent v2.1.3 reviews. Treat
`reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md` only as
an untrusted self-assessment.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md`;
expected:

```text
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62
```

Static review only. Read-only inspection and literal-example arithmetic or
hashing are allowed. Run no repository code, test, probe, smoke command, or
Officina process. Alter no existing file or runtime state.

## Required question

Are X213-m1 and X213-m2 closed; is every v2.1.3 closure you independently
confirmed carried forward unmodified; and does v2.1.4 introduce no new
Critical or Major defect, weaken no fail-closed behavior, promote no watchdog
or replacement fact to a second runtime authority, and reopen no
A3/B1/C1/D1/K1 author cell?

Attack at least:

1. **Bootstrap pipes and spawn cuts:** all four channels are nonblocking at
   creation; every read/write errno, EOF, malformed frame, timeout and death
   ordering has one continuation; no inherited descriptor can retain EOF or
   `SPAWN.lock`; verify the middle-death/grandchild-live `c13` case.
2. **Manifest quarantine branches:** prove B-P/B-QM/B-QN are exclusive and
   total for admitted states; bindings cannot be forged, replayed, missing or
   satisfied by the wrong manifest; valid orphan-manifest quarantine can
   release custody without settlement or output reread.
3. **B1 garbage collection:** verify the exact
   `committed -> reply -> ack -> accepted` order, permanent tombstone prefix,
   command/effect authority until the last deletion, all crash prefixes, and
   absence of a state where a reply or semantic phase survives without its
   authority.
4. **Singleton lock order:** `SPAWN.lock` precedes every mutating/adopting
   preflight read; the unlocked stuck-holder route removes nothing; all
   EEXIST, PID-reuse, malformed, live/dead, crash and retry paths remain
   single-valued.
5. **Watchdog partition:** I1..I7 priority, exact-current-table I2 ack,
   replacement-fork failure, I3 absorption of every state other than T,
   sorted diagnostic set, and the proof that diagnostics cannot affect the
   route. Re-run all race rows and look for zero/two-continuation states.
6. **A3 hash truth:** the hash claims only the byte stream actually read;
   during-pass mixed streams need not be any file state or promoted bytes;
   no surviving text restores a stronger claim or an outcome-responsive
   route.
7. **Schemas and arithmetic:** the two one-key schema extensions are closed,
   canonical and sufficient; the timestamp example is exactly 43 bytes
   including LF and does not change the signed decision-file total.
8. **No regression:** closed custody/disposition, result-manifest, supervisor,
   resource, event, Q/C and T-inactivity surfaces; zero new constants, paths,
   objects, tokens or imports except the two declared schema keys.

Do not accept worked examples or the author's closure in place of governing
rules. Report any new issue by severity, exact locus, counterexample and
smallest repair.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_4_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_4_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_4`

Include the recomputed hash and base commit, disposition of X213-m1/m2 and all
v2.1.4 repairs, the eight attack traces, findings by severity, a no-regression
table, author-cell determination, and the exact authorization boundary.

If confirmed, authorize only Kirill's signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`; not implementation,
T activation, entropy, runtime construction, Q/C work, or science. If revised,
keep the token unavailable and require another bounded X/Y check.

Confirm no process/test/probe ran, no existing file changed, no runtime or
scientific artifact was created, T remains `NOT_ACTIVATED`, and the programme
claim remains `OPEN`.
