I'll start by orienting myself in the repository and locating the normative files.

First, the required hash recomputation and the target file's identity.

Hash confirmed: `33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50` — matches expected. Base commit `6e15856` is an ancestor of HEAD.

Now let me read the two v2.1.7 REVISE reviews (the inherited findings) and the author's untrusted v2.1.8 closure.

I now have the five inherited findings clearly. Let me read the author's untrusted v2.1.8 closure and repair chat response, plus the signed generic harness signature (the reviewed-amendment clause).

Let me verify the author's cited governing hashes independently and read the reviewed-amendment clause (§9) of the signed harness contract.

All governing hashes verify byte-for-byte. Let me read the exact reviewed-amendment clause in the signed harness.

All governing hashes verify. The signed harness clause (lines 534-541) is confirmed: the harness "uses no `signal`/`threading`/`multiprocessing`/backend import. Any ... backend import, requires a reviewed amendment to that allowlist." Now the core work — reading the v2.1.8 normative bytes. Let me get its section structure.

Let me read the correction in sequential chunks. First the header through §V218.1.

Now the core normalization mechanics — §V218.2 (attacks 1, 2, 3).

Excellent detail. §V218.2 handles the kernel semantics carefully. Let me verify one pinned platform fact independently and continue reading §V218.3–§V218.4.

requires-python `>=3.11` and the unamended 16-member allowlist both confirm the correction's platform pins. Now the terminals, residuals, causal proof, and governance.

Now the causal proof, crash matrix, tests, no-regression, and governance sections.

Let me read the final governance and the two confirmation questions.

I've read the full correction. Let me run targeted independent verifications: `signal.` member containment (attack 1), and `m5`/`rel2` stage-M citations (attack 8/m217-1).

Containment confirmed: the only actually-used `signal` members are `SIGCHLD`, `SIG_DFL`, `signal`, `getsignal`; every forbidden API (SIG_IGN, pidfd_send_signal, pthread_*, set_wakeup_fd, alarm, etc.) appears only inside the §V218.1.2 "Forbidden, explicitly" list. Let me confirm the `m5`/`rel2` occurrences are all in the deletion/retention-scoping context.

All `m5`/`rel2` occurrences are confined to the replacement-index entry, §V218.5's deletion/retention-scoping, unreachability assertions, test rows, and the review questions — no operative stage-M continuation rests on them. m217-1's repair is genuine. Let me confirm the runtime state assertions.

All independent checks pass. I have a complete picture. Let me record the key facts in memory context and write the single deliverable review file.

Everything verifies:
- **Hash** `33b0b916…0ed50` matches; base `6e15856` is an ancestor of HEAD; all governing hashes reproduce byte-for-byte.
- **verification.py** holds exactly the 16 members (no `signal`), digest `327b1bb2…` matches, unedited.
- **Containment**: only `signal.SIGCHLD/SIG_DFL/signal/getsignal` are used; every forbidden API appears only in the prohibition list.
- **Kernel semantics** (`sigaction` full-record replacement clearing both `SIG_IGN` and `SA_NOCLDWAIT`; auto-reap = `SIG_IGN ∨ SA_NOCLDWAIT`; exec preserves `SIG_IGN` but clears `sa_flags`) are correctly pinned; `requires-python >= 3.11` confirmed.
- **`m5`/`rel2`** appear only in deletion/retention-scoping — no operative stage-M continuation rests on them.
- **T** `NOT_ACTIVATED`; `runtime_control/` absent.

Independent X-line review complete. Let me confirm exactly one new file was created and nothing else altered.

Let me reconcile the count — I created only one file but the total grew by more than one from the initial snapshot.

Confirmed: the status is byte-identical to the handover snapshot plus exactly one new file — my review. Nothing else was created, modified, staged, or committed.

## Independent X-line review complete — **CONFIRM**

I reconstructed the v2.1.8 result from the normative bytes (full v2→v2.1.8 chain, both v2.1.7 REVISE reviews, the signed harness/batch-settlement composites and signature, `verification.py`), treating the author closure as untrusted.

**Deliverable:** [opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md](reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md) — line 1 `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X`.

**Hash & base.** `33b0b916…0ed50` matches expected exactly; base `6e15856` is an ancestor of HEAD `568f68a`; every governing hash (incl. both v2.1.7 reviews and the unamended `verification.py` `327b1bb2…`) reproduces byte-for-byte.

**All five inherited findings closed at root:**
- **C217-1 / X217-M1** — `c3n` performs one `signal.signal(SIGCHLD, SIG_DFL)` before every first fork; the single `sigaction` clears both inherited `SIG_IGN` and `SA_NOCLDWAIT`, verified against `/proc` `SigIgn`/`SigCgt`, with no fork on any non-`NORMALIZED` result, backed by three `CONTRADICTED` detectors; `ECHILD ⇒ INCONCLUSIVE`.
- **X217-m1** — the `ppid ≠ getpid()` gap becomes row I-4, resolved in the safe direction.
- **M217-1** — `T3` deleted; `T1`/`T2`/non-returning `B` are pairwise disjoint and exhaustive; ownership carries the kill so a stopped child is reaped with `/proc` unreadable.
- **m217-1** — the causal proof rests at `m0`/`rel1`/fork-shared lock; I verified no operative stage-M claim cites `m5`/`rel2`.

**Independently verified:** the delta is exactly `signal` (only `SIGCHLD/SIG_DFL/signal/getsignal` used; forbidden APIs appear only in the prohibition list); the pinned CPython≥3.11 `sigaction` semantics and Linux auto-reap condition (`SIG_IGN ∨ SA_NOCLDWAIT`) hold, so clearing `SA_NOCLDWAIT` is mechanically warranted; the supervisor X/Y review **is** the reviewed amendment the signed harness §9 clause anticipates — no contract conflict. Both admitted residuals (the zombie residual; `B-CONTRADICTED` non-termination) are honest fail-closed states, not the prohibited silent wedge. No regression across §V217.1/§V217.4 and the whole signed surface.

**Authorization boundary.** Kirill's token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is authorized **only conditionally** — signable iff the independent **Y line confirms the identical bytes**. No implementation, commit, `verification.py` edit, activation, entropy, spend, Q/C, or science is authorized. **T `NOT_ACTIVATED`; claim `OPEN`.** No code, test, or Officina process ran; exactly one file created.
