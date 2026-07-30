# Officina supervisor and control-channel amendment — v2.1.2 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1 and
v2.1.1. It is **not** an independent X-line or Y-line review of its own bytes
and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. The author's
own v2.1.1 closure is authored self-assessment, not evidence. The only next
authorization step is independent bounded X/Y confirmation of the **v2.1.2
bytes**.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
(v2),
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
(v2.1), and
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
(v2.1.1) — all three preserved unedited as review evidence. **Everything not
named in the §N0 replacement index carries forward verbatim.** Nothing earlier
is rewritten, reinterpreted, or silently narrowed. It dispositions every
finding of the two independent v2.1.1 reviews
(`reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`,
`reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`).

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen meaning carried forward unchanged** (every v2.1.1 repair both
reviewers accepted): supervisor-authoritative explicit `NEW`/`RETRY`
allocation; journaled observation-form `OPERATION_STATUS`; the
descendant-aware reducer; validity-first two-phase takeover; the two-hash
spawn template; the reviewed bootstrap adapter as executable root; watchdog
publication after every claim-start, renew, and remove; durable `RUNNING.json`
before admission success; no K1 replenishment at settlement, rename,
promotion, failure, or unused reservation; total worker status/EOF routing;
and the honest, non-citable A3 timing/metadata residuals.

**K1 is implemented literally**, including the two clauses this layer repairs:
the supervisor **writes each output byte exactly once and hashes each output
byte exactly once** (§N4), and capacity is released only after **complete**
custody absence is proved (§N2).

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature, review,
or runtime artifact. Starts no process, endpoint, pipe, FIFO, journal,
watchdog, worker, adapter, or transport. Creates no entropy, activation,
capability, world, learner, candidate, datum, Q/C object, capacity artifact,
custody disposition, or outcome. Authorizes no implementation. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed for this correction)

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
b5b5614166488bc8dca0856bf6963d84bd701757df153acaf868212687a2d797  reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
640305647c9c03d44f40899bf2434c089afb5cbbbf8286e9673852aa795cc6b1  reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

## Engineering constants

**Zero new constants.** Every constant of v2.1.1's block carries forward
unchanged, including the five immovable author-signed `T_OUTPUT_*` values,
`T_CTRL_FD_LOW = 3`, `T_CTRL_FD_HIGH = 4`,
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`,
`T_SPAWN_BOOTSTRAP_MAX_AGE_NS`, and
`T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64`. No repair in this layer needs a
new tunable, and none is introduced. The import allowlist delta remains
**none**: this layer uses only `os.dup`, `os.dup2`, `os.close`,
`os.set_inheritable`, `os.fstat`, `os.pread`, `os.read`, `os.write`,
`os.listdir`, `os.open(dir_fd=…)`, `os.stat(dir_fd=…, follow_symlinks=False)`,
`os.fork`, `os.pipe2`, `os.kill`, `os.killpg`, `os.waitpid`, `os._exit`,
`fcntl.flock`, `fcntl.fcntl` with `F_GETFL`, `time.clock_gettime_ns`,
`hashlib`, `json`, `re`, and `pathlib` — all inside
`ALLOWED_ABSOLUTE_IMPORTS`; `select`, `selectors`, `signal`, `ctypes`, and
`sys` remain outside it.

---

## N0. Exact replacement index (v2.1.1 → v2.1.2)

Everything else carries forward verbatim, including all of v2 §V2.8, §V2.1.1,
§V2.1.3, §V2.1.7, §V2.7.5, §V2.9.2, §V2.9.4, §V2.14; v2.1 §W2.6, §W3.1,
§W3.2, §W3.4, §W4.1, §W4.7, §W5.1–§W5.5, §W6.1, §W6.3–§W6.6; and v2.1.1
§Z1.1, §Z1.2, §Z1.4, §Z1.6, §Z1.8, §Z1.10, §Z2 (all), §Z3.1, §Z3.2, §Z3.4,
§Z3.6, §Z3.7, §Z4.1–§Z4.4, §Z5 (all), §Z6.3, §Z6.7, §Z7.1, §Z7.2, §Z7.4,
§Z8.1, §Z8.2, §Z9.1–§Z9.6, §Z10.1, §Z10.3–§Z10.6, §Z12, §Z13.

| v2.1.1 locus (exact sentence / clause / table row) | Action in v2.1.2 |
|---|---|
| §Z1.3 formula line `next(scope) := max( tombstone(scope).next_occurrence_index , … )` | **extended** by §N9.1 (absent-scope defaults pinned) |
| §Z1.5 table **row order** ("Let `i = occurrence_index` … rows 1–8" evaluated in listed order) | **replaced** by §N8.3 (the prefix test is evaluated **first**, making GC timing invisible and partial GC harmless) |
| §Z1.5 row 2 result cell | **extended** by §N8.3 (reached only when `i > acknowledged_prefix_occurrence`) |
| §Z1.5 sentence "Rows 5–7 are the complete post-GC classification, and they need only two integers from the tombstone." | **replaced** by §N8.3 (row 5 is evaluated first and is the complete post-ack classification) |
| §Z1.7 table row `SUCCESSOR_OCCURRENCE`, clause "A successor that carries `null` or any other value acknowledges **nothing**" | **replaced** by §N7.2 (one pre-allocation priority rule; a non-null mismatch is `INVALID`/`REPLAY_BYTES`) |
| §Z1.7 table row `CLIENT_ECHO`, clause "`h` equals the recorded `effect_reply_sha256` of the **highest unacknowledged** occurrence" | **replaced** by §N7.1–§N7.2 (the acknowledgement **frontier** is the *lowest* unacknowledged occurrence with a durable reply, published in the reply envelope) |
| §Z1.9 bullet "`acknowledged_prefix_occurrence` advances **only** in the same lock epoch that installs an `ack.json`…" | **retained**, and its GC coupling replaced by §N8.1 |
| §Z1.9 bullet "**GC** of `accepted/committed/reply/ack` for occurrence `i` is permitted only when all three hold, **in the same lock epoch that installed the ack that advanced the prefix**" | **replaced** by §N8.1–§N8.2 (GC permitted in any later held-lock epoch once ack, prefix, and the command-specific archival predicate all verify) |
| §Z1.9 bullet "**Growth bound.** … A polling or heartbeating client keeps the count at one by echoing the previous reply's `effect_reply_sha256`" | **replaced** by §N7.3 + §N8.4 (frontier drain path and the two-part retention arithmetic) |
| §Z3.3 duty 2 "parse argv[9] as exactly two decimal ints (low, high); os.dup2 them to `T_CTRL_FD_LOW = 3` and `T_CTRL_FD_HIGH = 4`; close the originals if different; os.fstat both and require S_ISFIFO" | **replaced** by §N6.1 (collision-safe eight-step remap; direction/role verification; failure cleanup) |
| §Z3.3 duty ordering list (duties 1–6) | **replaced** by §N6.3 (remap → forbidden-fd closure → target preflight → self-stop → post-`SIGCONT` re-verify → `execv`) |
| §Z3.5 block "CLI, before the first fork:" (three lines) | **replaced** by §N3.2 (two sealed pipes; `SPAWNING_GROUP.json` after the first fork) |
| §Z3.5 block "Grandchild, as its FIRST actions … a. scrub every inherited descriptor …" (steps a–e) | **replaced** by §N3.3 (the literal first instruction is a gated read on the release pipe; scrub moves after the durable record) |
| §Z3.5 block "CLI wait: read the bootstrap line …" and "Stuck-holder route (SPAWN.lock acquisition expiry …)" | **replaced** by §N3.4–§N3.5 (middle-child report; CLI-installed record; three-tier identity set; kill-by-pgid from the first fork return) |
| §Z3.5 sentence "Both identity facts the CLI needs are now **kernel-verifiable and non-circular**: the pipe delivers pid + start identity + pgid, and the durable record persists them for a later takeover." | **replaced** by §N3.6 (the report is written by the **middle child**, the record by the **CLI**, both before the grandchild executes anything but its gated read) |
| §Z4.5 `t-freeze-observation.v1` key list | **unchanged**; its `UNKNOWN` interpretation is narrowed by §N5.4 |
| §Z4.5 "**Consumption order:**" bullet | **replaced** by §N5.5 (fallback and replacement-freeze objects enter the same total order) |
| §Z4.6 conjunct 9's line `quiescence == UNKNOWN ⇒ freeze_ns is null, overrun_ns is null, unresolved_member_count ≥ 1` | **replaced** by §N5.4 (the clause binds the **watchdog-written** witness only; the supervisor's fallback separates `unknown_reason` from the current member count) |
| §Z4.6 paragraph "The supervisor then writes its own replacement witness with `quiescence = UNKNOWN`, `freeze_ns = null`, `overrun_ns = null`, `killer = SUPERVISOR`, and the member count it observes itself…" | **replaced** by §N5.1–§N5.3 (a separate no-replace fallback namespace and id; the rejected object is never overwritten or deleted) |
| §W3.5 row "Ack absent past `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS`" clause "supervisor freezes all live groups itself … then settles every overdue lease per §W3.4" (as invoked by §Z4.3 rule 3) | **extended** by §N5.6 (non-overdue groups frozen only for the swap have an exact, durably recorded resume route) |
| §Z6.1 formula line `+ Σ T_OUTPUT_PER_STREAM_MAX_BYTES × 4 … for every custody directory found under operations/**/out/, the quarantine root, or runtime/T_PROMOTED/**` | **replaced** by §N2.2 (the derived complete custody-location set replaces the informal three-place enumeration; "the quarantine root" is defined) |
| §Z6.2 table row `CAPACITY/<op>.settled.json`, clause "`custody_root` is updated" | **replaced** by §N2.4 (`custody_root` is diagnostic only and is never a proof target) |
| §Z6.4 line `disposition_id = SHA-256(canonical { activation_record_sha256, operation_id, author_decision_sha256 })` | **replaced** by §N1.2 (acyclic preimage with a domain tag and the derived decision path; `author_decision_sha256` removed from the preimage) |
| §Z6.4 sentence "The three-field preimage removes any self-reference." | **deleted as false** and replaced by §N1.3 (the dependency DAG, with a worked forward construction) |
| §Z6.4 path-grammar block `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_[A-Z0-9_]{1,64}_SIGNATURE.md` | **replaced** by §N1.1 (the path is **derived** from `operation_id`; exactly one legal path per operation) |
| §Z6.4 sentence "a **tracked** repository file whose SHA-256 equals `author_decision_sha256` and which contains, each as an exact standalone line, the `author_token`, the `operation_id`, and the `disposition_id`." | **replaced** by §N1.4 (byte-exact eight-line content-closed decision file) |
| §Z6.5 conjunct 2 | **replaced** by §N1.5 conjunct 2 (recompute from the acyclic preimage) |
| §Z6.5 conjunct 7 (`custody_root` proof target and grammar) | **replaced** by §N2.3 (the derived custody-location set is the proof target) |
| §Z6.5 conjunct 8 (author token / path / tracked / hash / three standalone lines) | **replaced** by §N1.5 conjuncts 8a–8d (derived path, byte-exact content, hash binding, and the honest split between supervisor-mechanical and author-procedural verification) |
| §Z6.5 conjunct 9 ("NO value anywhere in the record equals …") | **extended** by §N1.6 (the prohibition now covers **every byte** of the tracked decision file, which is content-closed) |
| §Z6.5 conjunct 10 (single-name custody-absence proof, recursing upward) | **replaced** by §N2.3 (complete-set proof in one held-lock epoch) |
| §Z6.5 conjunct 12 (`.disposed.json` install) | **extended** by §N2.5 (adds `custody_locations_proved`) |
| §Z6.2 table row `CAPACITY/<op>.disposed.json` key list | **replaced** by §N2.5 |
| §Z6.6 rows "the named custody exists, or any level is unreadable" and "`author_decision_path` untracked, mis-grammared, or hash-mismatched" | **replaced** by §N1.7 and §N2.6 |
| §Z7.3 table row cell `result_sha256 = SHA-256(b"[]")` (the canonical empty result) | **replaced** by §N9.2 (`SHA-256(canonical_json([])) = SHA-256(b"[]\n")`, reconciling it with §W4.5's canonical-form definition) |
| §W4.5 sentence "The supervisor then opens the file itself … and **updates one streaming SHA-256 per file in the same pass**" (as carried by §Z8.3) | **replaced** by §N4.1 (no content hash in the write path) |
| §Z8.3 code-block lines "and holds both; the inline streaming SHA-256 is computed during the single write pass, exactly as before." and step 4 "require it to equal the inline hash" | **replaced** by §N4.2 (the verification pass is the **sole** content hash) |
| §Z8.3 sentence "each byte is *written* exactly once, and exactly one bounded verification pass re-reads the written bytes immediately before the settle step." | **replaced** by §N4.2 (each byte is written exactly once **and hashed exactly once**) |
| §W3.2 clause "**every** bounded long loop … services one watchdog step and one control-frame step between chunks" (as invoked by §Z8.3) | **clarified** by §N4.4 (inside a held lock epoch the serviced control step may only read and buffer, never apply an effect) |
| §Z10.2 reply-envelope key list | **replaced** by §N7.1 (adds `ack_frontier_occurrence_or_null`, `ack_frontier_effect_reply_sha256_or_null`) |
| §Z10.7 durable-object table | **extended** by §N10.1 (four added objects; three replaced rows) |
| §Z11 crash-cut matrix | **extended** by §N11 (twenty-one added or replaced rows) |
| §Z12.1 inherited-closure qualification | **extended** by §N10.3 (v2.1.1 closures are marked *confirmation pending v2.1.2*) |
| §Z12.2 test-obligation rows 51–74 | **extended** by §N12 (rows 75–96) |

---

## N1. Acyclic, content-closed custody-disposition authority (R1)

Closes Opus X211-C1 and Sol C1/M5. One construction, not a menu.

### N1.1 The decision path is derived, not chosen

```text
canonical_author_decision_path(operation_id) :=
  "successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_" + operation_id + "_SIGNATURE.md"
```

`operation_id` is exactly 64 lowercase hex characters, so the path matches
exactly

```text
^successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_[0-9a-f]{64}_SIGNATURE\.md$
```

and its hex segment **must equal** `operation_id`. v2.1.1's free
`[A-Z0-9_]{1,64}` segment is deleted: **there is exactly one legal decision
path per operation**, derived from an already-known value. This removes the
wrong-path attack surface entirely rather than checking for it.

### N1.2 The identifier preimage is acyclic

```text
disposition_id := SHA-256(canonical {
  "schema": "philosophia.officina.t-output-custody-disposition-id.v1",
  "activation_record_sha256": <64 hex>,
  "author_decision_path": <the derived path of §N1.1>,
  "operation_id": <64 hex>
})
```

`author_decision_sha256` is **removed** from the preimage. The domain tag is
the `schema` member, so this hash can never collide with any other preimage in
the contract. `canonical` is the repository's canonical JSON: `json.dumps`
with `sort_keys=True`, `separators=(",",":")`, `ensure_ascii=True`, plus one
trailing `"\n"`, ASCII-encoded — the same function every other Officina hash
uses.

### N1.3 Dependency DAG (no self-reference)

```text
activation_record_sha256 ─────────────┐
                                      ├──► disposition_id ──► decision-file bytes
operation_id ──► canonical_author_    │                              │
                 decision_path ───────┘                              ▼
                                                          author_decision_sha256
                                                                     │
                                                                     ▼
                                                    disposition object (§N1.5)
                                                                     │
                                                                     ▼
                                              CAPACITY/<op>.disposed.json (§N2.5)
```

Every edge points forward. `author_decision_sha256` is a **sink**: it is
computed from the completed file and is bound in the disposition object and in
the verifier, and it never feeds back into `disposition_id`, into the path, or
into the file. The four construction steps are therefore executable in one
forward order:

```text
S1. compute canonical_author_decision_path from operation_id
S2. compute disposition_id from {tag, activation_record_sha256,
    author_decision_path, operation_id}
S3. write the tracked decision file, which contains disposition_id from S2
S4. compute author_decision_sha256 = SHA-256(exact file bytes) and write the
    disposition object naming it
```

### N1.4 The tracked decision file is content-closed (byte-exact)

The file is **exactly eight lines**, in this order, US-ASCII, `\n` line
endings only, exactly one trailing `\n`, no CR, no BOM, no blank line, no
leading or trailing whitespace on any line, one `": "` separator (colon then
one space) after each key, and **no other byte anywhere in the file**:

```text
# OFFICINA T OUTPUT CUSTODY DISPOSITION SIGNATURE V1
schema: philosophia.officina.t-output-custody-decision.v1
author_token: I_AUTHORIZE_OFFICINA_T_OUTPUT_CUSTODY_ABSENCE
activation_record_sha256: <64 lowercase hex>
operation_id: <64 lowercase hex>
disposition_id: <64 lowercase hex>
custody_destination: DELETED_OUTSIDE_T | MOVED_OUTSIDE_REPOSITORY
signed_utc: <canonical UTC, exactly YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ>
```

Line 1 and the values on lines 2 and 3 are **fixed literals**. Lines 4–6 are
64 lowercase hex. Line 7 is one of exactly two enum tokens. Line 8 is a
canonical nanosecond UTC timestamp. There are exactly five variable values in
the whole file, each of a pinned syntactic class.

**Prohibition, now total by construction.** Because no additional byte may
exist, the file **cannot** contain a result hash, promoted content hash,
learner state, candidate identity, Q/C identifier, scientific field,
output-content judgement, free text, prose, comment, or any other value. Sol
M5's gap — "the tracked author-decision Markdown … may contain arbitrary
additional text" — is closed by exhaustion rather than by enumeration of
forbidden things. The verifier additionally rejects the file if any of its
five variable values equals the operation's `result_sha256` or any of its
recorded per-file content hashes (§N1.6).

### N1.5 Verifier (fail-closed; every conjunct mandatory)

The disposition object's path, schema, and key set are unchanged from §Z6.4
**except** that `author_decision_path` must equal §N1.1's derived value:

```text
successor/officina/runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json
schema philosophia.officina.t-output-custody-disposition.v1, keys exactly
(unchanged from §Z6.4):
  schema, scientific_outcome, disposition_id, activation_record_sha256,
  settlement_generation_sha256, operation_id, operation_terminal,
  bytes_reserved, actual_bytes, custody_root, custody_parent_sha256,
  custody_destination, author_token, author_decision_path,
  author_decision_sha256, authorized_utc
```

Under `T_RUNTIME.lock`, in one lock epoch. Conjuncts 1, 3, 4, 5, 6, and 11 of
§Z6.5 are unchanged. Replaced and added conjuncts:

```text
 2. disposition_id recomputes EXACTLY from §N1.2's four-member preimage and
    equals the filename stem
 7. (replaced) see §N2.3: the proof target is the derived complete
    custody-location set, not the record's custody_root
 8a. author_decision_path equals canonical_author_decision_path(operation_id)
     byte-for-byte; any other value refuses
 8b. the file resolves through an O_DIRECTORY|O_NOFOLLOW dir-fd walk from the
     repository root with no symlink component, is a regular file, and has
     st_nlink == 1
 8c. its bytes are EXACTLY the eight-line form of §N1.4 — parsed by the exact
     line/key/value grammar, with total length equal to the sum of the eight
     line lengths plus eight; any extra, missing, reordered, re-cased,
     re-separated, CR-bearing, or trailing byte refuses
 8d. author_decision_sha256 == SHA-256(those exact bytes); line 3's
     author_token equals the pinned literal; line 4's
     activation_record_sha256, line 5's operation_id, line 6's
     disposition_id, and line 7's custody_destination equal the disposition
     object's corresponding values
 9. (extended) see §N1.6
10. (replaced) see §N2.3
12. (extended) see §N2.5
```

**The honest verification split, stated rather than claimed.** The supervisor
mechanically verifies conjuncts 8a–8d — grammar, resolution, regular-file and
link status, byte-exact content, and hash equality — from inside its own
module root, with **no `git` dependency and no new import**. That the file is
**tracked at HEAD and committed before use** is an author/operator obligation,
already enforced for every activation-relevant checkpoint by the signed
activation-protocol clean-HEAD rule; the supervisor does not shell out to Git
and does not claim to verify repository history. Under one login UID the file
is also same-UID writable, so its authority is **mechanical** against
accident, stale facts, wrong path, wrong parent, substitution, replay,
truncation, and every grammar error, and **procedural** against a deliberate
same-UID forger — exactly the signed A3 residual. This is not a cryptographic
or kernel authority and is not claimed to be.

### N1.6 Recursive content prohibition over the whole authority

Conjunct 9 is extended to cover both objects:

```text
9. In the disposition object AND in every byte of the tracked decision file:
   no value may equal the operation's result_sha256, any recorded per-file
   content_sha256, any promoted path, any learner/candidate/Q/C identifier, or
   any judgement about output content; the recursive scientific-field
   rejection applies at every depth of the JSON object; and the decision
   file's content-closed grammar (§N1.4) leaves no byte in which such a value
   could appear. The check runs against the operation-bound identifier set
   {result_sha256, every content_sha256 in SETTLEMENT.json, every
   promoted_relative_path, charge_event_sha256, lease_sha256} — all of which
   the supervisor already holds durably.
```

### N1.7 Attack table (no failure releases capacity)

| Attack | Mechanical result |
|---|---|
| **Stale** — activation record has moved | conjunct 3 refuses |
| **Stale** — `settlement_generation_sha256` ≠ `OPERATION.json`'s | conjunct 5 refuses |
| **Substituted** — a valid decision file for operation *X* offered for operation *Y* | impossible: the path is derived from `operation_id` (§N1.1) and `disposition_id` binds it (§N1.2); conjuncts 2 and 8a both refuse |
| **Substituted** — a different `custody_parent_sha256` | conjunct 4 refuses |
| **Replayed** — a previously used disposition re-offered | conjunct 11 (no-replace `.disposed.json`) releases nothing; and §N2.3 refuses unless custody is still absent |
| **Replayed** — offered before custody is gone | §N2.3 refuses |
| **Partial** — decision file truncated, or written without its trailing `\n` | conjunct 8c refuses on byte-exact length/grammar |
| **Partial** — disposition object written, `.disposed.json` install crashed | no release recorded; the operation still counts `bytes_reserved`; a later epoch re-verifies every conjunct and installs idempotently by no-replace |
| **Wrong path** — any path other than the derived one | conjunct 8a refuses; and no other path can produce a matching `disposition_id` |
| **Wrong id** — hand-chosen `disposition_id` | conjunct 2 refuses |
| **Forged** — a same-UID process writes both objects | **not** mechanically excluded; named A3 procedural residual (§N1.5) |
| **Content-bearing** — decision file cites a result hash or judgement | impossible under §N1.4; conjunct 8c refuses any extra byte, and conjunct 9 refuses a prohibited value in any of the five variable fields |

### N1.8 Worked forward construction (illustrative arithmetic only)

**Non-installable illustration.** The values below are patterned synthetic
hex that cannot correspond to any real activation record or operation; no such
file is created by this document, none is tracked, and this example authorizes
nothing. It exists solely so both implementers can verify the arithmetic in
forward order.

```text
S1  activation_record_sha256 = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    operation_id             = bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    canonical_author_decision_path =
      successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb_SIGNATURE.md

S2  preimage bytes (396 bytes, canonical JSON + trailing newline):
{"activation_record_sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","author_decision_path":"successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb_SIGNATURE.md","operation_id":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","schema":"philosophia.officina.t-output-custody-disposition-id.v1"}

    disposition_id = e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd

S3  decision-file bytes (504 bytes, eight LF-terminated lines):
# OFFICINA T OUTPUT CUSTODY DISPOSITION SIGNATURE V1
schema: philosophia.officina.t-output-custody-decision.v1
author_token: I_AUTHORIZE_OFFICINA_T_OUTPUT_CUSTODY_ABSENCE
activation_record_sha256: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
operation_id: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
disposition_id: e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd
custody_destination: DELETED_OUTSIDE_T
signed_utc: 2026-07-30T00:00:00.000000000Z

S4  author_decision_sha256 = 0773f29c4f4946242fb17078bd1ee3e97c475146e3ae10557d8bd8b59a61a06f
    disposition object path =
      successor/officina/runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/e330a38411a403175152b0c786f4f7592053ca7822329abe66e30432e96997bd.json
```

Each of S1→S4 is computable from its predecessors alone. No step requires
knowing a later value. Under v2.1.1's clause, S2 required
`author_decision_sha256`, which required S3, which required S2 — the
unsatisfiable fixed point both reviewers refuted.

---

## N2. Complete custody-absence proof (R2)

Closes Sol C2. Custody anywhere means `bytes_reserved` remains fully
accounted.

### N2.1 Definition of the quarantine custody location (reconciliation)

v2.1 §W4.6/§Z6.1 referred to "the quarantine root" without defining it.
Reconciled, adding nothing: a quarantined operation's bytes are **never
moved** — `QUARANTINE.json` records the terminal and the custody stays where
it was written. The quarantine custody location is therefore exactly
`runtime_control/T_SUPERVISOR/operations/<operation_id>/out/`, the same path
as live custody. There is no separate quarantine directory and none is
created.

### N2.2 The canonical complete custody-location set

Derived **only** from the immutable `operation_id` and the two fixed roots
`R_OPS = runtime_control/T_SUPERVISOR/operations/` and
`R_PROM = runtime/T_PROMOTED/` (both under `successor/officina/`). No record
field is trusted to name it.

| # | Location | What can hold or name retained bytes |
|---|---|---|
| L1 | `R_OPS<operation_id>/out/` | the source custody tree; also the quarantine custody location (§N2.1) |
| L2 | `R_OPS<operation_id>/` | the operation directory itself: it may legally hold **only** the closed immutable control-record set `{BOUND.json, OPERATION.json, RUNNING.json, SETTLEMENT.json, QUARANTINE.json, DELIVERY_ACK.json}`; any other entry is an unknown custody location |
| L3 | `R_PROM<operation_id>/` | promoted custody |
| L4 | `R_OPS<operation_id>/.<name>.tmp` and `R_PROM.<operation_id>.tmp` | every §3 durability temporary name reachable for this operation (`atomic_create` writes `.<basename>.tmp` beside its target) |
| L5 | any entry, at any type, directly under `R_OPS` or `R_PROM` whose name **contains** `operation_id` and is not L1–L4 | an additional/unknown operation-bound custody location |

`R_OPS<operation_id>/out/` is the only protocol-allowed staging or
pre-rename copy location: promotion is one `os.replace(out/ → R_PROM<op>/)`
on a single device (guaranteed by the §Z9.4 `st_dev` serve preflight), so no
cross-device copy, no second staging tree, and no partial-copy location can
exist. There is no other rename destination in the protocol.

### N2.3 The proof (one held-lock epoch, descriptor-safe)

Replaces §Z6.5 conjuncts 7 and 10 entirely. All steps in the **same**
`T_RUNTIME.lock` epoch as the `.disposed.json` install, with no frame served
and no effect applied between them:

```text
P1. open R_OPS with O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC; open R_PROM likewise
    (if R_PROM is absent, prove it absent in `runtime/` by P-abs below and
     treat L3/L4-prom as absent)
P2. L2: os.stat(operation_id, dir_fd=R_OPS_fd, follow_symlinks=False)
    - ENOENT and operation_id absent from os.listdir(R_OPS_fd)
      ⇒ L1, L2, L4-ops are all absent; go to P4
    - present and S_ISDIR ⇒ open it with O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC and
      enumerate: the entry set must be a SUBSET of the closed control-record
      set of §N2.2 L2. Any other entry — including `out`, any `.tmp`, any
      directory, any symlink, any device — ⇒ REFUSE (unknown or live custody)
    - present and not S_ISDIR ⇒ REFUSE
P3. L1: within the operation directory, prove `out` absent by BOTH
    os.stat("out", dir_fd=op_fd, follow_symlinks=False) raising ENOENT AND
    "out" being absent from the enumeration of P2
P4. L3: prove operation_id absent under R_PROM by BOTH
    os.stat(operation_id, dir_fd=R_PROM_fd, follow_symlinks=False) raising
    ENOENT AND absence from os.listdir(R_PROM_fd)
P5. L4: no entry matching the temp grammar for this operation exists in the
    P2 enumeration or the R_PROM enumeration
P6. L5: no entry in the R_OPS or R_PROM enumerations whose name contains
    operation_id is outside L1–L4  ⇒ any such entry REFUSES
P7. every level opened in P1–P6 resolved with O_NOFOLLOW and no symlink
    component; any level that cannot be opened, stat'ed, or enumerated
    ⇒ REFUSE (never assume absence)

P-abs (used when a parent is itself absent): prove the parent absent in ITS
    parent by the same paired stat/enumerate test, recursing up to the
    repository root; an unreadable level refuses.
```

Release is permitted **only** if every one of L1–L5 is proved absent (or
vacuously absent by P-abs) in that single epoch. Absence is always proved by
**two** independent observations (a `follow_symlinks=False` stat raising
`ENOENT` **and** absence from a directory-fd enumeration), so a single
misleading `stat` cannot authorize a release.

### N2.4 `custody_root` is diagnostic only

§Z6.2's clause "`custody_root` is updated" and every use of `custody_root` as
a proof target are replaced: `custody_root` in
`CAPACITY/<op>.settled.json` and in the disposition object is an
**informational record of where custody was at settlement**. It is compared
for consistency (it must equal L1 for `QUARANTINED` and L3 for `PROMOTED`) but
it is **never** the thing whose absence is proved. Sol C2's objection — that a
pre-rename no-replace record cannot describe post-rename custody — is
structurally removed, because the proof target is derived from the immutable
operation identity, not read from a record.

### N2.5 The supervisor-produced disposed record

```text
CAPACITY/<operation_id>.disposed.json
schema philosophia.officina.t-capacity-disposition.v1, atomic no-replace,
supervisor under T_RUNTIME.lock, keys exactly:
  schema, scientific_outcome, operation_id, disposition_id,
  author_disposition_sha256, released_bytes (== bytes_reserved),
  custody_absent (true), custody_locations_proved (sorted list of the exact
  L1–L5 location strings proved absent in this epoch), proof_epoch_utc,
  disposed_utc
```

`custody_root` is replaced by `custody_locations_proved` (§Z6.2's row is
superseded): the record now states **what was proved**, not one name.
`author_disposition_sha256` remains SHA-256 of the exact disposition-object
file bytes.

### N2.6 Both crash directions, proved

| Cut | Real custody | v2.1.1 outcome | v2.1.2 outcome |
|---|---|---|---|
| after `SETTLEMENT.json` + `<op>.settled.json`, **before** the promotion rename | L1 present, L3 absent | if `custody_root` named the destination, conjunct 10 passed and released capacity **while bytes existed** | P2/P3 find the operation directory holding `out` ⇒ **REFUSE**; `bytes_reserved` stays accounted |
| **after** the promotion rename completes | L1 absent, L3 present | if `custody_root` named the source, conjunct 10 passed and released capacity **while bytes existed** | P4 finds `R_PROM<op>/` ⇒ **REFUSE** |
| quarantined operation, custody retained | L1 present | one-name proof could pass against L3 | P2/P3 ⇒ **REFUSE** |
| a durability temporary survives a crash | L4 present | undetected | P5 ⇒ **REFUSE** |
| author removed L1 and L3 but left a stray `<op>.old` beside `R_PROM` | L5 present | undetected | P6 ⇒ **REFUSE** |
| author removed every location; only the immutable control records remain | none | — | P2 subset test passes, P3–P7 prove absence ⇒ release exactly `bytes_reserved`, once |
| any location unreadable (permissions, I/O error) | unknown | — | P7 ⇒ **REFUSE**; never assume absence |

Interaction pins, all unchanged in policy: **quarantine** keeps custody at L1
until the author removes it, so a quarantined operation's reservation is
retained until then; **partial promotion** cannot exist (`os.replace` of a
directory is atomic and same-device); **crash recovery** (§Z6.3) still counts
every custody directory without a capacity record at the full ceiling and
never re-measures downward; **delivery acknowledgement** releases nothing and
touches no custody; the **disposed record** is installed only after §N2.3
succeeds in the same epoch.

---

## N3. Earliest supervisor-grandchild identity (R3)

Closes Sol C3. **Requirement met literally:** the only instruction the
grandchild executes while holding the fork-shared `SPAWN.lock` before a
parent-controlled, kernel-verifiable, durable identity exists is a **single
blocking read on a pipe whose only write end is held by the CLI** — and that
read cannot outlive the CLI, because its EOF forces immediate exit and
releases the lock.

### N3.1 Two sealed channels

```text
boot_pipe    = os.pipe2(0)   # middle child → CLI: the grandchild's identity
release_pipe = os.pipe2(0)   # CLI → grandchild: the one-byte release
```

Both are created by the CLI **before** the first fork, so both are inherited.
The middle child **closes the release-pipe write end before the second fork**,
so the grandchild inherits only the release **read** end and can never keep
the release channel open against itself. The CLI holds the only release write
end.

### N3.2 CLI, before and immediately after the first fork

```text
c1. acquire SPAWN.lock with flock(LOCK_EX|LOCK_NB), retrying at
    T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS;
    on expiry take the §N3.5 stuck-holder route
c2. install SPAWNING.json (§W2.2 keys unchanged, atomic no-replace,
    same-directory temp → file fsync → no-replace rename → parent fsync)
c3. create boot_pipe and release_pipe
c4. pid_mid = os.fork()
c5. IMMEDIATELY, in the CLI: install T_SUPERVISOR/SPAWNING_GROUP.json
    (atomic no-replace, §3 durability), schema
    philosophia.officina.t-supervisor-spawning-group.v1, keys exactly:
      schema, scientific_outcome, spawning_id, cli_pid, cli_start_identity,
      middle_child_pid, middle_child_start_identity, boot_identity,
      created_utc
    The recorded middle_child_pid is also the grandchild's pgid and session
    id, because the middle child's only action before forking is setsid()
    (§N3.3). This record exists BEFORE the grandchild exists.
c6. close the release-pipe READ end and the boot-pipe WRITE end in the CLI
```

`SPAWNING_GROUP.json` gives every later client a **durable, kernel-verifiable
kill handle for the whole spawn group before the grandchild is created**. This
is the object whose absence made Sol C3's wedge unrecoverable.

### N3.3 Middle child: setsid, fork, report, exit

```text
m1. close the release-pipe WRITE end and the boot-pipe READ end
m2. os.setsid()                     # the middle child becomes session/group leader
m3. pid_gc = os.fork()
m4. (middle child only) read /proc/<pid_gc>/stat for the grandchild's kernel
    start identity, and /proc/sys/kernel/random/boot_id
m5. write EXACTLY ONE canonical ASCII JSON line ≤ T_CONTROL_FRAME_MAX_BYTES on
    the boot pipe, schema philosophia.officina.t-supervisor-bootstrap.v1, keys
    exactly (unchanged from §Z3.5): schema, scientific_outcome, spawning_id,
    supervisor_pid, supervisor_start_identity, supervisor_pgid,
    boot_identity, reported_monotonic_ns
    — the write cannot block: one line ≤ 4096 ≤ PIPE_BUF into an empty pipe;
      EPIPE (CPython ignores SIGPIPE) ⇒ go to m6
m6. os._exit(0)                     # the grandchild is reparented to init
```

The middle child performs no filesystem write, holds no lock epoch, and its
whole lifetime is two `/proc` reads and one non-blocking pipe write. It cannot
wedge.

### N3.4 Grandchild: the gated first instruction

```text
g0. os.read(release_read_fd, 1)          ← THE LITERAL FIRST INSTRUCTION
      == b"\x01"                 ⇒ proceed to g1
      EOF (b"") or any other byte ⇒ os._exit(3) IMMEDIATELY, executing nothing
                                   else; the lock is released by process exit
g1. close the release read fd and the boot-pipe write fd; scrub every other
    inherited descriptor except the SPAWN.lock fd; stdio → os.devnull
g2. create endpoints; fork the watchdog; write WATCHDOG_CHILD.json (§Z3.6);
    await the watchdog's first ack, BOUNDED by
    T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
g3. install SUPERVISOR_IDENTITY.json (atomic no-replace); unlink
    SPAWNING_CHILD.json, SPAWNING_GROUP.json, and SPAWNING.json; close the
    SPAWN.lock fd
```

Step g1 — the descriptor scrub that Sol C3 identified as the unrecorded
window — now runs **only after** the CLI has installed a durable identity
record (§N3.5 step c9). Everything the grandchild does while holding the lock
before that record either (a) is the gated read, which EOFs and exits on CLI
death, or (b) happens after the record exists.

### N3.5 CLI: report, record, release, and the identity set

```text
c7. read one line from the boot pipe, bounded by
    T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
      - a valid line ⇒ c8
      - EOF, malformed line, or timeout ⇒ kill by the RECORDED group:
        killpg(middle_child_pid, SIGTERM) then SIGKILL; prove death of the
        whole group by /proc absence or state Z for every member found;
        unlink SPAWNING_GROUP.json and SPAWNING.json; release the lock; return
        REFUSED / BOOTSTRAP (retryable = false)
c8. verify the reported supervisor_pid's live start identity equals the
    reported value, and that its pgid equals middle_child_pid
      - mismatch or not live ⇒ the same kill/refuse route as c7
c9. install T_SUPERVISOR/SPAWNING_CHILD.json (atomic no-replace, §3
    durability: same-directory temp → file fsync → no-replace rename →
    parent-directory fsync), schema
    philosophia.officina.t-supervisor-spawning-child.v1, keys exactly
    (unchanged from §Z3.5 plus the recorded pgid, which §Z3.5 already had):
      schema, scientific_outcome, spawning_id, supervisor_pid,
      supervisor_start_identity, supervisor_pgid, boot_identity, created_utc
    — written by the CLI, not by the grandchild (§Z3.5's writer is replaced)
c10. write exactly one byte b"\x01" on the release-pipe write end, then close
     it                                          ← the release
c11. poll for a live-verified SUPERVISOR_IDENTITY.json, bounded by
     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS; on expiry take the c7 kill/refuse route
c12. release SPAWN.lock (the grandchild's retained fd keeps the flock until g3)
```

**Three-tier durable identity set**, each with a kernel-verifiable kill:

| Tier | Record | Identity | Kill |
|---|---|---|---|
| CLI | `SPAWNING.json` | `cli_pid`, `cli_start_identity` | **never killed by another client** — see the residual below |
| spawn group | `SPAWNING_GROUP.json` | `middle_child_pid` = pgid = session id, `middle_child_start_identity` | `killpg(middle_child_pid)`, death proved per member |
| grandchild | `SPAWNING_CHILD.json` | `supervisor_pid`, `supervisor_start_identity`, `supervisor_pgid` | `killpg(supervisor_pgid)` or `kill(supervisor_pid)`, death proved |

**Stuck-holder route** (replaces §Z3.5's), taken by a later CLI **without**
the lock after `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` expires, in this order:

```text
s1. if SUPERVISOR_IDENTITY.json exists and live-verifies ⇒ there is a live
    supervisor; no kill; proceed as an ordinary client
s2. else if SPAWNING_CHILD.json exists, its recorded process is live by
    pid + start identity, and the record is older than
    T_SPAWN_BOOTSTRAP_MAX_AGE_NS ⇒ killpg(supervisor_pgid), prove death,
    retry the bounded acquisition exactly once
s3. else if SPAWNING_GROUP.json exists, the recorded middle_child_pid names a
    live process group by start identity or any live member, and the record is
    older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS ⇒ killpg(middle_child_pid), prove
    death, retry the bounded acquisition exactly once
s4. else ⇒ REFUSED / BOOTSTRAP (retryable = true)
```

Because `SPAWNING_GROUP.json` is installed immediately after the first fork,
s3 covers **every** cut in which a grandchild or middle child exists,
including the pre-`SPAWNING_CHILD` window.

**Named residual, stated not claimed away.** One case remains outside
mechanical recovery: a **CLI process that is itself wedged or `SIGSTOP`ed
while holding the lock**. Its own `flock` reference is released only when that
process exits. Every CLI wait in this contract is bounded — lock acquisition
`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`, boot read
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, identity poll
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, plus bounded kill/death proof — so a
contract-following CLI always releases within that arithmetic sum
(30 s + 10 s + 10 s + bounded proof). A deliberately stopped or externally
wedged same-UID client is the signed A3 **procedural** residual and an
operator matter; this contract does not authorize one client to kill another
client process. **D1 is unaffected**: the supervisor's lifetime never depends
on a client, and no supervisor waits on `SPAWN.lock`.

### N3.6 Complete fork/record/lock automaton with every cut

| Cut | Lock state | Grandchild state | Single continuation |
|---|---|---|---|
| before c1 | free | absent | ordinary acquisition |
| c1 expires, no records | free or held | absent | s4 ⇒ `BOOTSTRAP` (retryable) |
| after c2, CLI dies | released by CLI exit | absent | next holder finds `SPAWNING.json` with no group record and no live pid ⇒ unlinks it, spawns |
| after c4, before c5 (group record not yet durable) | held by CLI **and** middle child | may exist, blocked at g0 | if the CLI dies: release-pipe write ends all closed ⇒ EOF ⇒ `_exit(3)`; if the middle child dies: CLI's bounded c7 read gets EOF or times out ⇒ killpg by `pid_mid` from the fork return ⇒ death proved |
| after c5, before the second fork | held by CLI + middle child | absent | group record durable; s3 kills the group |
| after the second fork, before the middle child reports | held by CLI + middle + grandchild | blocked at g0 | grandchild executes **nothing** but the gated read; s3 or c7 kills the group; CLI death ⇒ EOF ⇒ `_exit(3)` |
| middle child killed before m5 | held by CLI + grandchild | blocked at g0 | CLI's c7 read times out (the grandchild still holds a boot-pipe write end, so EOF may not arrive) ⇒ timeout ⇒ killpg by the recorded group ⇒ death proved ⇒ `BOOTSTRAP` |
| report received, before c9 | held by CLI + grandchild | blocked at g0 | CLI death ⇒ EOF ⇒ `_exit(3)`; CLI wedge ⇒ s3 by the group record |
| after c9, before c10 | held by CLI + grandchild | blocked at g0 | `SPAWNING_CHILD.json` durable ⇒ s2 kills precisely; CLI death ⇒ EOF ⇒ `_exit(3)` |
| after c10, grandchild proceeding at g1/g2 | held by grandchild (CLI still holding until c12) | initializing | s2 kills by the durable record; the grandchild's own bounded first-ack wait (g2) exits it on failure, releasing the lock |
| grandchild's first-ack wait expires | held by grandchild | initializing | kill the watchdog by `WATCHDOG_CHILD.json`, prove death, unlink `SPAWNING_CHILD.json`, `os._exit(3)` ⇒ lock released |
| identity-install no-replace collision | held by both candidates | one serving | the loser exits immediately, writing nothing, unlinking nothing (§Z3.5, unchanged) |
| after g3 | free | serving | ordinary live-supervisor path; s1 applies to later clients |
| grandchild killed at any point | released on exit | dead | proved by `/proc` absence or state `Z`; `os.waitpid` only for own-generation children |

**Every cut after the grandchild exists yields either a killable durable
identity (`SPAWNING_GROUP.json`, then `SPAWNING_CHILD.json`) or proved process
death that releases the lock.** No `flock` wait anywhere is unbounded, and the
single-supervisor invariant is unchanged: the fork-shared lock still holds
through identity installation, and the no-replace identity install still
resolves any race with the loser exiting silently.

---

## N4. Literal K1 write-once / hash-once (R4)

Closes Sol C4. Signed K1: the supervisor "writes and hashes each byte once."

### N4.1 The write path computes no content hash

§W4.5's clause "and **updates one streaming SHA-256 per file in the same
pass**" is **deleted**, together with §Z8.3's "the inline streaming SHA-256 is
computed during the single write pass, exactly as before." The framed write
path now does exactly this per frame, and nothing else:

```text
1. validate the header BEFORE creating anything: relative, non-empty, no "."
   or "..", no absolute prefix, no NUL, unique within the operation, depth ≤ 2,
   component ≤ T_OUTPUT_PATH_COMPONENT_MAX_BYTES, path ≤
   T_OUTPUT_PATH_MAX_BYTES, file count ≤ 16 × device_units,
   type(content_bytes) is int, > 0, and
   bytes_written_total + content_bytes ≤ bytes_reserved
2. w = os.open(rel, O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, dir_fd=out_fd)
   r = os.open(rel, O_RDONLY|O_NOFOLLOW|O_CLOEXEC,                dir_fd=out_fd)
   (both held for the operation's lifetime; r is opened before any byte exists)
3. copy exactly content_bytes bytes in T_OUTPUT_COPY_CHUNK_BYTES chunks,
   maintaining ONLY integer counters: bytes_written[rel], bytes_written_total,
   frame_count. NO hash object is updated in this pass.
4. a chunk that would cross bytes_reserved ⇒ write nothing further, close the
   read end, killpg, prove death, BOUND_EXCEEDED quarantine (§W4.5, unchanged)
```

Ceilings, counts, path grammar, and file counts are therefore enforced
**while writing** with no hashing whatsoever, which is what makes the
once-hash rule attainable. The §Z7.1 worker-status cross-check compares the
worker's `frame_count` and `total_content_bytes` against these
supervisor-maintained integer counters exactly as before, and can still only
cause a fail-closed `TRANSPORT` quarantine.

### N4.2 The sole content hash: the pre-settlement verification pass

```text
under T_RUNTIME.lock, per file, in sorted relative_path order:
1. v = os.open(rel, O_RDONLY|O_NOFOLLOW|O_CLOEXEC, dir_fd=out_fd)   # re-resolve
2. require (st_dev, st_ino) of v == those of the HELD r, st_nlink == 1, and
   st_size == bytes_written[rel]                    # inode substitution defence
3. read the file through v with os.pread in T_OUTPUT_COPY_CHUNK_BYTES chunks,
   updating ONE hash object → content_sha256; require the total read length to
   equal bytes_written[rel] and require EOF exactly at that offset
                                                    # equal-size content
                                                    # substitution defence
4. NO other step in the contract reads or hashes an output content byte
```

Each output content byte is therefore **written exactly once (§N4.1 step 3)
and hashed exactly once (§N4.2 step 3)** — the literal signed provider. The
equal-size and inode substitution defences are fully retained, because step 2
compares against a descriptor held since before the first byte existed and
step 3 hashes the freshly re-resolved, inode-verified descriptor.

### N4.3 The canonical result hash is metadata-only

```text
result_sha256 = SHA-256(canonical [
  {"byte_length": …, "content_sha256": …, "relative_path": …} …
] sorted by relative_path)
```

This hashes **canonical metadata** — paths, per-file content hashes, and
lengths — and never re-reads a content byte. It is the value written into
`SETTLEMENT.json` and carried in the release token, unchanged in role from
§W6.1. The empty-output case is §N9.2.

### N4.4 Placement, lock epoch, and crash routing

The verification pass and the settle step occur in **one** `T_RUNTIME.lock`
epoch, because a streaming hash is not serializable across a crash and must
not be resumable. §W3.2's servicing rule is clarified for this case: between
chunks the supervisor services one watchdog step and **reads at most one
control frame into its endpoint buffer without applying any effect** — a lock
epoch is not reentrant, so no frame may be admitted, allocated, or applied
while the epoch is open.

| Cut | Continuation |
|---|---|
| crash after writing, before the pass | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; **no content hash was ever computed**; no resume, no respawn |
| crash during the pass | identical: the pass is not resumable and no partial hash is retained |
| crash after the pass, before `SETTLEMENT.json` | identical: `result_sha256` existed only in memory; nothing can promote without `SETTLEMENT.json` |
| inode/size/nlink mismatch at step 2 | `HASH` quarantine class (§W4.7, unchanged) |
| content mismatch at step 3 (short read, long read, or EOF at the wrong offset) | `HASH` quarantine class |
| after `SETTLEMENT.json` | promotion is a rename only; the release token and every later path carry `result_sha256` by value; nothing re-reads content |

**Why no later path hashes content again**, exhaustively: promotion is
`os.replace` (no read); `SETTLEMENT.json` stores the value; the release token
carries the value; `OPERATION_STATUS` returns the token bytes;
`DELIVERY_ACK.json` compares hashes for identity only; the capacity ledger
uses integers only; the custody-absence proof (§N2.3) is existence-only and
opens no output file; the crash reconstruction (§Z6.3) enumerates directories
and never reads file content.

**Named residual, unchanged and not enlarged.** Same-name substitution of the
`out/` **directory** between the verification pass and the promotion
`os.replace` remains an A3 **procedural** residual, because the kernel offers
no rename-by-descriptor. It is named here exactly as in §Z8.3, and nothing
further is claimed.

---

## N5. Writable rejected-witness fallback and the non-overdue resume (R5)

Closes Sol M1 and Opus X211-m2.

### N5.1 A separate fallback namespace and id

```text
fallback_witness_id = SHA-256(canonical {
  "schema": "philosophia.officina.t-freeze-fallback-id.v1",   # domain tag
  "supervisor_generation_sha256": …,
  "process_id": …,
  "table_seq": …,
  "rejected_witness_path_or_null": …,      # the exact rejected object's path
  "rejected_object_sha256_or_null": …      # null ONLY for the ABSENT sentinel
})

path: runtime_control/T_SUPERVISOR/WATCHDOG/FREEZE_FALLBACK/<fallback_witness_id>.json
```

The id is deterministic, domain-tagged, and **cannot** collide with
`witness_id` (different tag and different member set). Because it binds the
rejected object's path and SHA-256, a different rejected object yields a
different path, so the no-replace install always has somewhere to go. The
`ABSENT` sentinel (`rejected_witness_path_or_null = null`,
`rejected_object_sha256_or_null = null`) is used when the expected witness is
simply missing.

### N5.2 Fallback schema

```text
schema philosophia.officina.t-freeze-fallback-observation.v1
atomic no-replace, §3 durability, written by the SUPERVISOR under
T_RUNTIME.lock, keys exactly:
  schema, scientific_outcome, supervisor_generation_sha256,
  fallback_witness_id, process_id, pgid, start_identity, deadline_ns,
  table_seq, rejected_witness_path_or_null, rejected_object_sha256_or_null,
  rejection_conjunct (int 0..10; 0 == the ABSENT sentinel, else the §Z4.6
    conjunct number that failed first, in ascending order),
  unknown_reason ∈ {EVIDENCE_ABSENT, EVIDENCE_UNVERIFIABLE,
                    FREEZE_INSTANT_UNKNOWN},
  current_unresolved_member_count (int ≥ 0),
  supervisor_quiescence ∈ {PROVED, UNKNOWN},
  killer ("SUPERVISOR"), created_utc
```

The rejected object is **never overwritten, truncated, renamed, or deleted to
make room**. It remains immutable and permanently non-evidence, and it is
removed only where §Z4.5 already permits — after the settlement's archival
commit.

### N5.3 The routing is unchanged; only its representation is repaired

A fallback drives exactly the signed route §W3.4 already fixes for
`UNKNOWN`: record-first live-process invalidity, the all-live batch
(§2c.12b/§4d) with the §4c(c)/§4d unknowable pool, public cause `PROCESS`, and
full §4c charging. No fallback can select a valid terminal, a zero-overrun
branch, a synthesized freeze instant, or an `overrun_ns`. **The fallback is a
supervisor runtime-authority fact**: it is written only by the supervisor
under the runtime lock, in a namespace the watchdog has no path to and never
writes. The watchdog remains a **witness only** — no lock, no capability, no
`runtime/` write, no ledger append, no settlement, no validity authority.

### N5.4 `unknown_reason` is separated from the current member count

§Z4.6 conjunct 9's clause
`quiescence == UNKNOWN ⇒ … unresolved_member_count ≥ 1` is narrowed to bind
**only the watchdog-written `t-freeze-observation.v1`**, where it is correct:
the watchdog reports `UNKNOWN` precisely because it could not prove
quiescence, so at least one member was unresolved *to it*.

For the supervisor fallback the two facts are distinct fields:

```text
unknown_reason                  — why the HISTORICAL fact is unknowable
current_unresolved_member_count — what the supervisor observes NOW
supervisor_quiescence           — whether the supervisor itself proved the
                                  tree stopped/dead now
```

Therefore `unknown_reason = FREEZE_INSTANT_UNKNOWN` with
`current_unresolved_member_count = 0` and `supervisor_quiescence = PROVED` is
**legal and expected**: the supervisor has proved the tree quiescent, yet the
instant at which it became quiescent is not recoverable, so the settlement
still takes the `UNKNOWN` invalid route and no timestamp is synthesized. Sol
M1's inconsistency is removed without weakening any route.

### N5.5 Production, duplicate, conflict, and consumption order

```text
production: validate the witness per §Z4.6; on the FIRST failing conjunct
  (ascending), compute fallback_witness_id, install the fallback no-replace,
  then consume it. The rejected object is left byte-intact.
duplicate:  EEXIST at the fallback path means an identical rejection for the
  identical rejected bytes is already durable ⇒ consume the existing object;
  write nothing.
conflict:   two fallbacks for the same (generation, process_id, table_seq)
  with DIFFERENT rejected_object_sha256_or_null values imply the immutable
  witness bytes changed between reads — only reachable through the A3
  same-UID procedural residual ⇒ record-first invalidity naming both
  fallbacks and the witness path. Fail-closed; no valid terminal.
consumption order (replaces §Z4.5's bullet): witnesses, fallbacks, and
  replacement-freeze records are consumed in one total order:
    (generation == current) desc,
    table_seq asc,
    process_id asc,
    object class: FREEZE_FALLBACK before FREEZE,
    fallback_witness_id / witness_id asc
  For a given (generation, process_id): if any fallback exists, the FALLBACK
  is authoritative and every witness for that pair is permanently
  non-evidence. Otherwise the earliest table_seq witness is authoritative,
  exactly as §Z4.5 already says. Later same-pair objects are retained as
  duplicates and never consumed twice.
```

### N5.6 Non-overdue groups after a watchdog death (Opus X211-m2)

§W3.5's dead-watchdog row freezes **all** live groups. Groups whose lease
deadline had **not** passed at the freeze instant were frozen only for the
swap, and v2.1/v2.1.1 left their fate unstated. Pinned:

```text
at the moment the supervisor freezes a group solely for watchdog replacement
(deadline not yet reached, quiescence proved), it installs, under the lock:

runtime_control/T_SUPERVISOR/WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json
replacement_freeze_id = SHA-256(canonical {
  "schema": "philosophia.officina.t-replacement-freeze-id.v1",
  "supervisor_generation_sha256": …, "process_id": …, "table_seq": … })
schema philosophia.officina.t-replacement-freeze.v1, atomic no-replace,
keys exactly:
  schema, scientific_outcome, supervisor_generation_sha256,
  replacement_freeze_id, process_id, pgid, start_identity, table_seq,
  deadline_ns, frozen_monotonic_ns, overdue (false), created_utc
```

Resume predicate — **every** conjunct mandatory, under `T_RUNTIME.lock`:

```text
R1. the replacement watchdog is live by its §Z3.6 WATCHDOG_CHILD.json record
    AND has durably acked the EXACT current table_seq whose table contains
    this group's row
R2. the recorded lease is still the current durable lease for that process,
    and now_ns < that row's deadline_ns          (still non-overdue)
R3. every recorded group member's pid + start identity still matches, and
    every member is in state T                  (see the R6 relaxation below)
R4. no freeze witness and no fallback exists for that process in the current
    generation
R5. no unresolved invalidity blocks: G5 clear and the record-first ordering
    and v2.1 §B.4 satisfied
R6. install <replacement_freeze_id>.resumed.json (no-replace) BEFORE
    killpg(pgid, SIGCONT); if that marker is already durable, R3 is relaxed to
    "every member's pid + start identity matches and every member is in state
    T or running", and the SIGCONT is re-issued idempotently
```

If **any** conjunct fails — an overdue deadline, a member absent/`Z`/unknown,
an identity mismatch, a missing or stale ack, an existing witness or fallback,
or an unresolved invalidity — the group takes the **signed invalid route**
(all-live batch, cause `PROCESS`; the `UNKNOWN` pool when any member state is
unknowable). Nothing is resumed on doubt.

| Cut | Continuation |
|---|---|
| frozen, crash before the `REPLACEMENT_FREEZE` record | no record ⇒ **not resumable**; the group is settled through the signed invalid route |
| record durable, replacement watchdog not yet acked | R1 fails; hold frozen; if the deadline passes first, R2 fails ⇒ invalid route |
| record durable, ack durable, deadline passed while waiting | R2 fails ⇒ invalid route (an honest infrastructure invalidity, not a relabelled healthy heartbeat) |
| record + ack, all conjuncts hold, crash between `.resumed.json` and `SIGCONT` | R6's marker is durable ⇒ re-verify with the relaxed R3 and re-issue `SIGCONT` idempotently |
| crash after `SIGCONT` | the group is live under a lease already inside the acked table; the records are removed after the process's durable terminal + archival commit |
| a `REPLACEMENT_FREEZE` record from a **prior** generation | fails R1's generation binding ⇒ invalid route; §Z2.5 phase 2A settles it before any reducer step |

This is the **only** path in the contract that `SIGCONT`s an already-frozen
group. It never applies to a watchdog deadline freeze (every such freeze is
invalidity by §W3.4), and it never crosses a supervisor loss.

---

## N6. Collision-safe fixed-fd remap (R6)

Closes Sol M2. Total for every distinct valid `(low, high)`.

### N6.1 The algorithm (replaces §Z3.3 duty 2)

```text
given argv[9] parsed as exactly two decimal ints (low, high):
 0. require type int, both ≥ 0, low ≠ high, and both present in
    /proc/self/fd; else failure cleanup
 1. duplicate BOTH sources to temporaries BEFORE either target is written:
        t_low  = os.dup(low)
        t_high = os.dup(high)
    os.dup returns the lowest free descriptor, so a temporary may land on 3 or
    4. While t_low ∈ {3,4} or t_high ∈ {3,4} or t_low == t_high:
        keep every already-obtained descriptor OPEN (never close one to make
        room) and dup the SAME source again;
        at most four descriptors (3, 4, low, high) can occupy the low range, so
        at most four extra dups per source are ever needed and the loop is
        bounded by 8 iterations;
        once an acceptable pair (t_low, t_high) with both ∉ {3,4} and
        t_low ≠ t_high is held, close every rejected temporary whose number is
        NOT in {3, 4, low, high}
 2. os.set_inheritable(t_low, True); os.set_inheritable(t_high, True)
 3. os.dup2(t_low, T_CTRL_FD_LOW)      # 3   — atomic; closes any old 3
    os.dup2(t_high, T_CTRL_FD_HIGH)    # 4   — atomic; closes any old 4
    Because both descriptions are already held by temporaries outside {3,4},
    overwriting 3 and 4 cannot destroy either source description.
 4. close every descriptor in {t_low, t_high, low, high} \ {3, 4}
 5. os.set_inheritable(3, True); os.set_inheritable(4, True)   # survive execv
 6. os.fstat(3), os.fstat(4): both must be S_ISFIFO
 7. direction/role, via fcntl.fcntl(fd, F_GETFL) & O_ACCMODE:
      CONTROLLER: fd 3 == O_WRONLY (control-request write)
                  fd 4 == O_RDONLY (control-reply read)
      WORKER:     fd 3 == O_WRONLY (worker-status write)
                  fd 4 == O_WRONLY (framed-output write)
 8. close every other inherited descriptor except 0,1,2,3,4 by a bounded
    /proc/self/fd enumeration (os.listdir), then re-verify 6 and 7
```

### N6.2 Exhaustive case table

| `(low, high)` class | Behaviour | Result |
|---|---|---|
| `(3, 4)` | `t_low`, `t_high` land ≥ 5; `dup2(t_low,3)` is a no-op-equivalent re-point; `dup2(t_high,4)` likewise; step 4 closes only the temporaries (3 and 4 are excluded) | correct |
| `(4, 3)` | both descriptions are held by temporaries ≥ 5 **before** either target is written, so `dup2(t_low,3)` cannot destroy the original 3 (already duplicated as `t_high`) | correct — this is the case v2.1.1 got wrong |
| `(3, k)`, `k ∉ {3,4}` | `t_low` may be 4 ⇒ rejected by the loop and kept open while re-duping; the accepted pair is ≥ 5 | correct |
| `(k, 3)`, `k ∉ {3,4}` | symmetric | correct |
| `(4, k)`, `k ∉ {3,4}` | `t_low` may be 3 ⇒ rejected and re-duped | correct |
| `(k, 4)`, `k ∉ {3,4}` | symmetric | correct |
| `(j, k)`, `j,k ∉ {3,4}` | temporaries may land on 3 and/or 4 ⇒ rejected and re-duped; then `dup2` overwrites 3 and 4 safely | correct |
| `low == high` | step 0 refuses | `os._exit(4)` ⇒ `BOOTSTRAP` |
| non-int, negative, or malformed `argv[9]` | step 0 refuses | `os._exit(4)` |
| a source not present in `/proc/self/fd` | step 0 refuses | `os._exit(4)` |
| a source is not a pipe | step 6 refuses | `os._exit(4)` |
| wrong direction for the role | step 7 refuses | `os._exit(4)` |
| a forbidden descriptor survives | step 8 refuses | `os._exit(4)` |

### N6.3 Duty order, failure cleanup, and self-stop (replaces §Z3.3's list)

```text
1. verify the exact thirteen-index argv layout; N == len(argv) - 13, N ≥ 1;
   argv[7] is 64 lowercase hex                          (§Z3.3, unchanged)
2. the §N6.1 remap, including its verification steps 6–8
3. forbidden-descriptor closure and re-verification     (§N6.1 step 8)
4. target preflight: argv[13] exists, is a regular file, is executable
   (os.stat, os.access(X_OK))                           (§Z3.3, unchanged)
5. install NO signal disposition, then os.kill(os.getpid(), SIGSTOP)
6. after SIGCONT: re-verify that 3 and 4 are still pipes with the role's
   directions, then os.execv(argv[13], argv[13:])

failure cleanup, at ANY step: close every descriptor the adapter opened that
is not 0, 1, or 2 — including every temporary still held — then os._exit(4),
which the supervisor observes as the §W2.5 BOOTSTRAP route (bounded
WNOHANG|WUNTRACED wait, killpg, proved death, reaped, intent resolved, no
claim, no lease, no capability).
```

The remap therefore completes **before** the self-stop, and the post-`SIGCONT`
re-verification precedes the `execv`, so the target never receives a
mis-numbered, wrongly-directed, or non-pipe descriptor. No import is added and
no step is left to implementer discretion.

---

## N7. Total acknowledgement priority (R7)

Closes Sol M3 and addresses Opus X211-m1 by construction.

### N7.1 The frontier is published in the reply envelope

```text
ack_frontier(S) := the LOWEST occurrence index in scope S that has a durable
                   reply.json and NO durable ack.json;  null if none exists
```

The reply envelope (replacing §Z10.2's key list) is:

```text
schema ("philosophia.officina.t-control-reply.v1"),
scientific_outcome, supervisor_generation_sha256, request_sha256,
intent_scope_sha256, occurrence_index, idempotency_key,
effect_reply_sha256, next_occurrence_index,
ack_frontier_occurrence_or_null, ack_frontier_effect_reply_sha256_or_null,
status, detail
```

Both added fields are control identifiers already inside supervisor
authority — an integer and a hash of a control reply the same client could
retrieve by `RETRY` — never outcome fields, never scientific values. `detail`
remains exactly §W5.2's matrix. Frame arithmetic: the two fields add at most
about 110 bytes; the largest legal reply (a `PROMOTED` observation carrying
the six-field release token and two hashes) stays under `T_REPLY_MAX_BYTES =
2048` and far under `T_CONTROL_FRAME_MAX_BYTES = 4096`.

Because the frontier and its hash are published on **every** reply, a client
can always acknowledge in prefix order without guessing and without retaining
old replies.

### N7.2 One pre-allocation priority rule

Evaluated **before** allocation and before any other state movement, so no
acknowledgement error can move runtime state (replacing both the
`SUCCESSOR_OCCURRENCE` "acknowledges nothing" clause and the `CLIENT_ECHO`
mismatch clause):

```text
let a = acked_effect_reply_sha256_or_null, S = scope, i = occurrence_index,
    m = ack_frontier(S)

A0. a is null                       ⇒ no ordinary acknowledgement is
                                      installed; continue to §N8.3
                                      classification
A1. a is non-null and m is null     ⇒ INVALID / REPLAY_BYTES, no state movement
A2. a is non-null, a == reply(m).effect_reply_sha256, and
      mode == NEW   and i == m + 1  ⇒ permitted, ack_source = SUCCESSOR_OCCURRENCE
      mode == RETRY and i == m      ⇒ permitted, ack_source = CLIENT_ECHO
      any other (mode, i)           ⇒ INVALID / REPLAY_BYTES, no state movement
A3. a is non-null and a != reply(m).effect_reply_sha256
                                    ⇒ INVALID / REPLAY_BYTES, no state movement
                                      (this is the single deterministic result
                                       for a stale-but-genuine hash)
```

The two ordinary sources are now **disjoint** — `SUCCESSOR_OCCURRENCE`
requires `NEW` at `m+1`, `CLIENT_ECHO` requires `RETRY` at `m` — so no frame
has two continuations. A permitted acknowledgement installs `ack.json` for
occurrence `m` and advances the contiguous prefix in the **same** lock epoch
(§N8.1). Because only the frontier can be acknowledged, the prefix advances by
at least one on every permitted acknowledgement and the contiguous-prefix
proof is preserved trivially.

`PROCESS_TERMINAL` and `DELIVERY_ACK` are unchanged and independent of `a`:
they are supervisor-installed on their own durable triggers (with own-terminal
scopes still excluded from `PROCESS_TERMINAL` per §Z1.7), and each recomputes
the prefix in its own epoch. `m` ranges only over occurrences with a durable
`reply.json`, so nothing without cached bytes can be acknowledged.

### N7.3 The drain path is total

Steady state: each occurrence is acknowledged by its successor, so
`m = i − 1` always and a contract-following client never sees `INVALID`. If a
client falls behind (`m < i − 1`), its next reply publishes `m` and
`reply(m).effect_reply_sha256`, so it drains with `RETRY(m)` + echo, one
occurrence per frame, at most `T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64`
frames. A client that never acknowledges is refused
`REFUSED`/`UNRESOLVED_JOURNAL` (`retryable = true`) at 64 unacknowledged
occurrences and can always clear the backlog with the published frontier, so
the refusal is never a wedge. §Z1.9's clause "keeps the count at one by
echoing the previous reply's `effect_reply_sha256`" is replaced by this
frontier-based statement.

---

## N8. Later safe GC (R8)

Closes Sol M4.

### N8.1 Ack and prefix stay atomic; GC is decoupled

Unchanged: `ack.json` installation and the contiguous-prefix advance occur in
**one** lock epoch, and the prefix advances only to the largest `m'` such that
occurrences `1..m'` all have a durable `ack.json`.

Deleted: the requirement that physical GC occur in that same epoch. GC of the
phase files for occurrence `i` is permitted in **any later held-lock epoch**
once all three verify in that epoch:

```text
G1. ack.json for i is durable and immutable
G2. i ≤ acknowledged_prefix_occurrence
G3. the command-specific archival predicate of §N8.2 holds
```

No TTL, no size pressure, no outcome-derived deletion, and the tombstone is
never deleted.

### N8.2 The archival predicate, per command

| Command | Archival predicate |
|---|---|
| `CLAIM` | the owning process's terminal archival commit exists (the claim is archived with the process-record set) |
| `START` | the same terminal archival commit exists (the start event is archived with the process's close or invalid archival set) |
| `HEARTBEAT` | the archival commit that covered that `charge_event_sha256` exists — the process's terminal archival set, or the batch-settlement archival commit (`ARCHIVE` before `RESOLVED`) that covered the charge |
| `CLOSE` | the signed §2c.6 close archival commit exists (`archive_set "close"`) |
| `PAUSE` | the signed §6a pause archival commit exists (`archive_set "pause"`) |
| `RESUME` | the resume transaction's archival commit exists; for a plan that appended no event, the predicate is satisfied when every declared artifact of the plan is durable and the durable phase is `G1` or `G4` |
| `OPERATION_ADMIT` | the operation has a durable terminal (`SETTLEMENT.json` or `QUARANTINE.json`) **and** the archival commit covering its settling charge exists |
| `OPERATION_STATUS`, ack form | `DELIVERY_ACK.json` is durable **and** the operation's terminal is durable |
| `OPERATION_STATUS`, observation form | **explicitly vacuous.** An empty-effect plan appends no ledger entry and owns no archival item, so there is nothing to archive: the predicate is satisfied by durable `committed.json` **and** durable `reply.json` alone. Stated explicitly because Sol M4 observed that this plan has no owning archival transition |

### N8.3 Classification consults the prefix first

§Z1.5's rows are unchanged in content but their evaluation order is pinned:
**the prefix test (row 5) is evaluated first**, then rows 1–4 and 6–8 in their
listed order.

```text
step 1: if i ≤ T.acknowledged_prefix_occurrence
          ⇒ REFUSED / ALREADY_ACKNOWLEDGED, retryable = false, no effect,
            envelope carries next_occurrence_index — REGARDLESS of whether the
            journal directory is present, absent, or partially deleted
step 2: otherwise evaluate §Z1.5 rows 1–4 and 6–8 exactly as written
```

Three consequences, each required:

- **GC timing becomes invisible to clients.** An acknowledged occurrence gets
  the same answer before and after its physical GC, so the deferred-GC epoch
  of §N8.1 changes no observable behaviour.
- **A partially deleted directory is harmless.** Any subset of the four phase
  files may be missing at or below the prefix; step 1 answers first, so no
  reducer runs and no effect can be re-applied. GC therefore needs no
  particular deletion order, and a crash mid-GC is completed idempotently in a
  later epoch.
- **This is signed B1 exactly.** Signed B1 makes replies redeliverable "until
  a durable acknowledgement records the one-use effect"; the acknowledged
  prefix *is* that record, so redelivery is not owed past it. Row 8's
  impossible band (`prefix < i < next` with the directory absent) still routes
  to record-first invalidity.

### N8.4 Concurrency, crash cuts, and retention arithmetic

- **Concurrency.** GC and frame service are both under `T_RUNTIME.lock` and
  therefore serialize; there is no interleaving. A retry that arrives before
  the GC epoch and one that arrives after receive the identical
  `ALREADY_ACKNOWLEDGED` answer (§N8.3).
- **Crash cuts.** Crash mid-GC ⇒ a partial phase set at or below the prefix ⇒
  step 1 answers; a later epoch completes the deletion idempotently. Crash
  after `ack.json` but before archival ⇒ nothing is GC'd yet; when archival
  later becomes durable, any later epoch may GC. This is exactly the state
  v2.1.1 made permanently non-GC-able.
- **Retention arithmetic (two parts).** Live journal size is bounded by
  (a) unacknowledged occurrences: at most
  `T_MAX_UNACKED_OCCURRENCES_PER_SCOPE = 64` per scope, plus
  (b) acknowledged-but-unarchived occurrences: bounded by the number of open
  transitions, itself bounded by `MAX_CONCURRENT_LEASES = 4` live processes
  and by the signed 32 GiB operation envelope (≤ 128 maximum-size operations).
  Scope count is bounded exactly as §W1.7 states. Growth is therefore bounded
  and is **not** a function of polling frequency — the claim v2.1.1 made but
  could not execute.

---

## N9. Absent-scope defaults and exact reconciliation (R9)

### N9.1 Absent-scope defaults (Sol m1)

```text
tombstone_next(absent)        := 1
acknowledged_prefix(absent)   := 0
```

§Z1.3's formula reads, in full:

```text
next(S) := max( tombstone_next(S) ,
                1 + max{ i : JOURNAL/<key(S,i)>/accepted.json exists } ,
                1 )
where tombstone_next(S) = 1 and acknowledged_prefix(S) = 0 when
TOMBSTONES/<S>.json is absent, and the inner max{} term is omitted when no
such i exists.
```

Both defaults are used everywhere the two integers appear, including §N8.3
step 1 (an absent tombstone can never make an occurrence
`ALREADY_ACKNOWLEDGED`, since `0 < 1 ≤ i`).

### N9.2 Canonical empty-result hash (author-found reconciliation)

§Z7.3's cell wrote `result_sha256 = SHA-256(b"[]")`, which is inconsistent
with §W4.5/§N4.3's definition of `result_sha256` over the **canonical** form:
the repository's canonical JSON appends a trailing newline, so the canonical
empty array is the three bytes `[]\n`. Reconciled, with both values shown so
no implementer can pick the wrong one:

```text
canonical_json([])                      == b"[]\n"
result_sha256 (canonical empty result)  ==
  37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
NOT 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945,
which is SHA-256(b"[]") without the canonical trailing newline.
```

Everything else in the zero-frame canonical-empty-result row is unchanged:
`promoted_relative_paths = []`, `actual_bytes = 0`, capacity retained at
`bytes_reserved`, and it is explicitly not an invalidity. Neither reviewer
raised this; it is disclosed here as an author-found exactness defect rather
than carried silently.

### N9.3 Reconciliation of every affected item

| Item | Reconciled state |
|---|---|
| Schemas added | `t-supervisor-spawning-group.v1` (§N3.2), `t-freeze-fallback-observation.v1` (§N5.2), `t-replacement-freeze.v1` (§N5.6), and the two id domain tags `t-output-custody-disposition-id.v1` (§N1.2) and `t-freeze-fallback-id.v1` / `t-replacement-freeze-id.v1` (computed, never stored alone) |
| Schemas changed | `t-output-custody-disposition.v1` (`author_decision_path` now derived), `t-capacity-disposition.v1` (`custody_root` → `custody_locations_proved`), `t-request-tombstone.v1` (unchanged keys; absent-scope defaults pinned), the reply envelope (two frontier fields), `t-output-custody-decision.v1` (new content-closed file grammar, §N1.4) |
| Schemas whose interpretation is narrowed | `t-freeze-observation.v1` (§Z4.6 conjunct 9 binds the watchdog-written object only, §N5.4) |
| Paths added | `T_SUPERVISOR/SPAWNING_GROUP.json`, `WATCHDOG/FREEZE_FALLBACK/<fallback_witness_id>.json`, `WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json` and its `.resumed.json`, and the derived `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_<operation_id>_SIGNATURE.md` |
| Paths whose grammar changed | the author decision file (derived, one legal path per operation) |
| Constants | **none added, none moved**; the five signed `T_OUTPUT_*` values are untouched |
| Enums | `ack_source` values unchanged (the rule is now priority-ordered and disjoint); refusal and `INVALID` token sets unchanged — **no new token is introduced**; three added enums live only inside the new schemas (`unknown_reason`, `supervisor_quiescence`, `rejection_conjunct` range) |
| Public commands | unchanged: six CLI commands, two controller commands, one refusal-first `--officina-bootstrap` adapter token, unknown command ⇒ exit 2 |
| Signed events | none added, none moved (nine unchanged) |
| Resource values | none added, none moved |
| Q/C surface | none added; every new object is control-plane, T-development-only, `scientific_outcome: false`, recursively scientific-field-rejecting, archival-excluded, untracked, and permanently non-citable |
| Immutable-object owners | §N10.1 |
| Verifier duties | §N1.5, §N1.6, §N2.3, §N5.5, §N5.6, §N6.1 |
| Worked examples | §N1.8 (forward hash construction), §N9.2 (canonical empty result), §N2.6 (both rename directions), §N6.2 (fd cases) |
| Test obligations | §N12 rows 75–96 |
| Free text / hidden author judgement | none: every new field is a hash, an identity, a bounded integer, a closed enum, a derived canonical path, or a canonical UTC timestamp |

---

## N10. Object table, authority, and inherited-closure qualification

### N10.1 Durable-object table delta (extends §Z10.7)

**Authority classes** as in the author's §Z10.7: `convenience` (never read by
the supervisor), `transport` (frames, never authority at rest), `witness`
(control-plane evidence admitted only through an acceptance predicate),
`runtime` (supervisor authority under `T_RUNTIME.lock` or `SPAWN.lock`),
`author` (author authority).

| Object | Path (under `successor/officina/`) | Schema | Install | Writer / lock | Authority | Removed by |
|---|---|---|---|---|---|---|
| **Spawning group record** *(added)* | `runtime_control/T_SUPERVISOR/SPAWNING_GROUP.json` | `t-supervisor-spawning-group.v1` | no-replace, §3 durability | **CLI** under `SPAWN.lock`, immediately after the first fork | runtime | supervisor at g3, or the next `SPAWN.lock` holder |
| **Spawning child record** *(writer replaced)* | `…/SPAWNING_CHILD.json` | `t-supervisor-spawning-child.v1` | no-replace, §3 durability | **CLI** under `SPAWN.lock` (was: the grandchild) | runtime | supervisor at g3, or the killing CLI |
| **Bootstrap frame** *(writer replaced)* | boot pipe (no file) | `t-supervisor-bootstrap.v1` | — | **middle child** (was: the grandchild) | transport | — |
| **Release byte** *(added)* | release pipe (no file) | one byte `0x01` | — | CLI | transport | — |
| **Freeze fallback** *(added)* | `…/WATCHDOG/FREEZE_FALLBACK/<fallback_witness_id>.json` | `t-freeze-fallback-observation.v1` | no-replace, §3 durability | **supervisor** under `T_RUNTIME.lock`; the watchdog has no path here and never writes it | **runtime** | supervisor after the settlement's archival commit |
| **Replacement freeze** *(added)* | `…/WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json` and `….resumed.json` | `t-replacement-freeze.v1` | no-replace | supervisor under lock | runtime | supervisor after the process's durable terminal + archival commit |
| **Freeze observation** *(unchanged; interpretation narrowed)* | `…/WATCHDOG/FREEZE/<witness_id>.json` | `t-freeze-observation.v1` | no-replace | watchdog (or supervisor when the watchdog is dead) | **witness** — never overwritten, never deleted to make room | supervisor after the settlement's archival commit |
| **Capacity disposed** *(keys replaced)* | `…/CAPACITY/<op>.disposed.json` | `t-capacity-disposition.v1` (§N2.5) | no-replace | supervisor under lock | runtime | never |
| **Author custody disposition** *(path binding replaced)* | `runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/<disposition_id>.json` | `t-output-custody-disposition.v1` (§N1.5) | author-installed, no-replace, single use | **the author**; the supervisor never writes here | **author** | never (the supervisor never removes it) |
| **Author decision file** *(grammar and path replaced)* | `successor/OFFICINA_T_OUTPUT_CUSTODY_DISPOSITION_<operation_id>_SIGNATURE.md` | `t-output-custody-decision.v1` (§N1.4) | tracked commit, byte-exact eight lines | the author | **author** | never |

`runtime/T_OUTPUT_CUSTODY_DISPOSITIONS/**` remains archival-excluded and
untracked, inheriting the exclusion of the `T_PROMOTED` custody it disposes,
so **no signed activation-protocol §B archival set changes**. The author
decision file is a **tracked** path that must be committed before use, which
the clean-HEAD rule already governs.

### N10.2 Where each repaired fact now lives

| Fact | Class | Object |
|---|---|---|
| grandchild killability before it executes anything | runtime | `SPAWNING_GROUP.json`, then `SPAWNING_CHILD.json` |
| historical freeze instant unknowable | runtime | `FREEZE_FALLBACK/*` (`unknown_reason`) |
| current member quiescence at rejection time | runtime | `FREEZE_FALLBACK/*` (`current_unresolved_member_count`, `supervisor_quiescence`) |
| the rejected witness bytes | witness, permanently non-evidence | `FREEZE/<witness_id>.json`, immutable |
| a group frozen only for a watchdog swap | runtime | `REPLACEMENT_FREEZE/*` |
| the sole output content hash | runtime | `SETTLEMENT.json` (`result_sha256`, metadata-only per §N4.3) |
| which custody locations were proved absent | runtime | `.disposed.json` (`custody_locations_proved`) |
| the author's custody-absence decision | author | the byte-exact tracked decision file + the disposition object |
| the acknowledgement frontier | runtime | the journal phase files; published in the reply envelope |

### N10.3 Inherited-closure qualification

Every closure recorded in §Z12.1 and in the author's v2.1.1 closure now reads
**"closed in v2.1.1; confirmation pending independent v2.1.2 X/Y"**. In
addition, the four v2.1.1 rows that this layer repairs are re-read as:

| v2.1.1 row | v2.1.2 reading |
|---|---|
| X21-M8 / Sol M1 capacity-release authority | closed **subject to** §N1 (the id was an unconstructible fixed point) and §N2 (the absence proof was incomplete) |
| Sol C3 spawn/bootstrap totality | closed **subject to** §N3 (the earliest grandchild cut) and §N6 (the fd remap) |
| Sol C1 / X21-M5 acknowledgement and GC | closed **subject to** §N7 (priority) and §N8 (later GC) |
| K1 literal provider | closed **subject to** §N4 (write-once/hash-once) |

No closure in this document is asserted by author fiat; the author line cannot
confirm its own bytes.

---

## N11. Crash-cut matrix (extends §Z11)

Every §Z11 row carries forward except where §N0 names a replacement. Added and
replaced rows:

| Cut | Single continuation |
|---|---|
| CLI dies after the first fork, before `SPAWNING_GROUP.json` | release-pipe write end closed ⇒ grandchild's gated read EOFs ⇒ `os._exit(3)` ⇒ lock released; middle child's report takes `EPIPE` ⇒ `_exit(0)` |
| CLI dies after `SPAWNING_GROUP.json`, before the release byte | same EOF exit; the group record lets any later client kill and prove death |
| middle child dies before reporting | CLI's bounded boot read times out ⇒ `killpg(middle_child_pid)` from the durable group record ⇒ death proved ⇒ `REFUSED`/`BOOTSTRAP` |
| grandchild blocked at the gated read while the CLI wedges | `SPAWNING_GROUP.json` (and later `SPAWNING_CHILD.json`) make it killable by the §N3.5 stuck-holder route; the grandchild has executed **nothing** else |
| CLI wedged holding the lock with no live grandchild | s4 ⇒ `REFUSED`/`BOOTSTRAP`; every contract-following CLI wait is bounded; a stopped client is the named A3 procedural residual |
| grandchild's watchdog first-ack wait expires | kill the watchdog by `WATCHDOG_CHILD.json`, prove death, unlink `SPAWNING_CHILD.json`, `_exit(3)` ⇒ lock released |
| adapter fd remap fails at any step | close every adapter-opened descriptor except 0,1,2; `os._exit(4)` ⇒ supervisor's `BOOTSTRAP` route; no claim, lease, or capability |
| `(low, high) == (4, 3)` | both sources duplicated to temporaries ≥ 5 before either target is written ⇒ both descriptions survive ⇒ correct 3/4 assignment |
| crash after writing output, before the sole hash pass | `SUPERVISOR_CRASH` quarantine at `bytes_reserved`; **no content hash was ever computed**; nothing can promote |
| crash during the sole hash pass | identical; the pass is not resumable and no partial hash is retained |
| crash after the hash pass, before `SETTLEMENT.json` | identical; `result_sha256` existed only in memory |
| current-generation witness malformed or unverifiable | install the §N5.1 fallback at its own no-replace path (the witness path stays occupied and immutable) ⇒ `UNKNOWN` all-live invalid route |
| expected witness absent entirely | fallback with the `ABSENT` sentinel (`rejection_conjunct = 0`, `unknown_reason = EVIDENCE_ABSENT`) ⇒ same route |
| supervisor proves quiescence now but the freeze instant is unknowable | fallback with `unknown_reason = FREEZE_INSTANT_UNKNOWN`, `current_unresolved_member_count = 0`, `supervisor_quiescence = PROVED` ⇒ `UNKNOWN` route; no timestamp synthesized |
| `EEXIST` at the fallback path | an identical rejection is already durable ⇒ consume it; write nothing |
| two fallbacks for one (generation, process, table) with different rejected hashes | record-first invalidity naming both and the witness path (A3 residual) |
| group frozen for a watchdog swap, crash before its record | not resumable ⇒ signed invalid route |
| replacement freeze recorded, ack not yet durable, deadline passes | R2 fails ⇒ signed invalid route |
| replacement freeze recorded and acked, crash between `.resumed.json` and `SIGCONT` | re-verify with the relaxed R3 and re-issue `SIGCONT` idempotently |
| prior-generation replacement-freeze record | fails R1 ⇒ §Z2.5 phase 2A settles it before any reducer step; never resumed |
| non-null `acked_effect_reply_sha256` mismatching the frontier | `INVALID`/`REPLAY_BYTES` **before** allocation and before any other state movement |
| acknowledged occurrence retried before its GC epoch | `REFUSED`/`ALREADY_ACKNOWLEDGED` (prefix tested first) — identical to the answer after GC |
| crash mid-GC leaving a partial phase set at or below the prefix | prefix test answers first; a later epoch completes the deletion idempotently; no effect is re-applied |
| ack durable, archival not yet durable | nothing is GC'd; when archival becomes durable, **any** later held-lock epoch may GC |
| disposition offered before the promotion rename | P2/P3 find `out` ⇒ refuse; capacity retained |
| disposition offered after the promotion rename | P4 finds `T_PROMOTED/<op>/` ⇒ refuse; capacity retained |
| a durability temporary or an unknown `<op>`-named entry survives | P5/P6 ⇒ refuse; capacity retained |
| every custody location proved absent | release exactly `bytes_reserved`, once, recording `custody_locations_proved` |

No cut releases capacity while any custody location exists or is unreadable.
No cut hashes an output content byte twice. No cut leaves the singleton lock
held by a process without a durable killable identity or proved death. No cut
resumes a frozen group except through §N5.6's fully conjunctive predicate. No
cut re-applies an acknowledged effect.

---

## N12. Implementation and test obligations (no implementation authorization)

**No implementation is authorized by this document.** No code, test, commit,
host change, process, or signature is permitted. These obligations become due
only after both independent v2.1.2 confirmations accept these bytes **and** the
author signs the amendment token.

§Z12.2 rows 51–74 and §W10 rows 1–50 carry forward. Added:

| # | Test | Covers |
|---|---|---|
| 75 | forward construction S1→S4: derive the path, compute `disposition_id`, write the eight-line file, hash it; verify the §N1.8 digests reproduce exactly | R1, X211-C1, Sol C1 |
| 76 | every §N1.7 attack row refuses and releases nothing; a decision file for operation *X* cannot authorize *Y* | R1 |
| 77 | decision-file grammar: extra byte, missing trailing `\n`, CRLF, reordered lines, re-cased key, double space after the colon, added comment, added prose line, non-hex value — each refuses | R1, Sol M5 |
| 78 | a decision file whose variable value equals the operation's `result_sha256` or a `content_sha256` refuses | R1, Sol M5 |
| 79 | disposition offered before the rename, after the rename, with custody quarantined, with a surviving `.tmp`, and with a stray `<op>`-named entry — each refuses; only complete absence releases | R2, Sol C2 |
| 80 | absence proved twice per location (stat `ENOENT` **and** enumeration); an unreadable level refuses; a symlinked level refuses | R2 |
| 81 | `custody_locations_proved` records exactly L1–L5; `custody_root` is never used as a proof target | R2 |
| 82 | the grandchild executes only its gated read before `SPAWNING_CHILD.json` is durable, verified at every injected cut of §N3.6 | R3, Sol C3 |
| 83 | CLI death at each pre-release cut ⇒ EOF ⇒ grandchild `_exit(3)` ⇒ lock released; second CLI proceeds | R3 |
| 84 | middle-child death before reporting ⇒ bounded timeout ⇒ `killpg` by the durable group record ⇒ death proved | R3 |
| 85 | `SPAWNING_GROUP.json` exists before the second fork returns in the CLI; the stuck-holder route s1→s4 in order | R3 |
| 86 | no `flock` wait is unbounded anywhere; the CLI's total bound equals the stated arithmetic sum | R3, D1 |
| 87 | output byte accounting: each byte written once and hashed once; assert exactly one hash update per byte across the whole operation | R4, Sol C4 |
| 88 | ceilings, counts, and path grammar enforced during the write pass with no hash object instantiated | R4 |
| 89 | equal-size content substitution and inode substitution still detected by the sole pass; crash before/during/after the pass each route to `SUPERVISOR_CRASH` with no promotion | R4 |
| 90 | `result_sha256` is metadata-only and reproducible from `SETTLEMENT.json`; no later path reads a content byte | R4 |
| 91 | rejected witness at an occupied path ⇒ fallback installs at its own id; the original stays byte-intact; `EEXIST` and conflict rows behave as pinned | R5, Sol M1 |
| 92 | `UNKNOWN` with zero current unresolved members and `supervisor_quiescence = PROVED` is legal and routes to all-live invalidity with no synthesized timestamp | R5, Sol M1 |
| 93 | non-overdue replacement resume: each of R1–R6 violated singly ⇒ signed invalid route; the happy path resumes exactly once and is idempotent across the `.resumed.json` cut | R5, X211-m2 |
| 94 | all seven valid `(low, high)` classes plus every invalid class from §N6.2; after the remap fds 3/4 have the pinned role and direction and survive `execv` | R6, Sol M2 |
| 95 | acknowledgement priority: `null`, exact-frontier `NEW(m+1)`, exact-frontier `RETRY(m)`, stale-but-genuine hash, wrong hash, and no-frontier — each has exactly one result, decided before allocation | R7, Sol M3, X211-m1 |
| 96 | GC in a later epoch after archival; observation-form vacuous predicate; retry before and after GC give identical answers; crash mid-GC completes idempotently; the two-part retention bound holds | R8, Sol M4 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, or scientific
object.

---

## N13. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The custody-disposition
authority is one forward hash chain with a worked, reproducible example
(§N1.2, §N1.8) and a byte-exact eight-line decision file (§N1.4); the
custody-absence proof is a five-location derived set with paired
absence observations (§N2.2–§N2.3); the spawn bootstrap is a gated
first-instruction automaton with three durable identity tiers and an
exhaustive cut table (§N3); output bytes are written once and hashed once with
an exhaustive statement of every path that does **not** hash content (§N4);
rejected evidence has its own deterministic namespace with pinned production,
duplicate, conflict, and consumption order (§N5.1–§N5.5); the non-overdue
resume is a six-conjunct predicate with its own crash table (§N5.6); the fd
remap is an eight-step algorithm with a seven-class exhaustive table (§N6);
acknowledgement is a four-branch pre-allocation rule over a published frontier
(§N7); GC is a three-condition later-epoch rule with a per-command archival
predicate (§N8); and the two absent-scope defaults are pinned (§N9.1). No
clause resolves to "as reviewed", "as appropriate", or implementer discretion.

**Compatibility classification.** Unchanged: an engineering/control amendment
surface over the signed harness composite, containing no protocol amendment
except §W6.5's explicitly named supersession of harness §5a's physical
at-or-before-deadline sentence. The signed generic-harness contract
(v2/v2.1/v2.2/v2.3/v2.3.1) and the signed batch-settlement amendment
(v1/v1.1/v1.1.1, including §D1 head/cache completion and §D2 inline
`meter_evidence`) are referenced unchanged. No signed archival set, event,
runtime schema, root, constant, resource value, T band, or Q/C boundary moves.
The import allowlist delta remains **none**.

**No author cell is reopened.** A3 keeps its procedural same-UID residual and
gains only honesty: the new named residuals are the wedged-client case
(§N3.5), the disposition-forgery case (§N1.5), the fallback-conflict case
(§N5.5), and the unchanged `out/`-directory-swap case (§N4.4). B1 keeps
journaled exactly-once effects and retry-stable replies; §N7 and §N8 repair
acknowledgement priority and GC timing, not policy, and §N8.3 realizes signed
B1's "until a durable acknowledgement" boundary exactly. C1 keeps a watchdog
that witnesses and freezes and never holds runtime authority or settles; the
fallback is a **supervisor** fact in a namespace the watchdog cannot reach, so
no watchdog fact becomes a second runtime authority, and §N5.6 resumes a group
only on the supervisor's own fully conjunctive proof. D1 keeps no idle exit,
and §N3 removes the last pre-identity wedge without any unbounded `flock`
wait. K1 keeps its five signed constants, its no-replenishment rule, and now
its literal write-once/hash-once provider and its complete-custody release
condition. **No new author-choice token is proposed, and none was found to be
unavoidable.**

**Negative space.** This correction creates nothing executable and authorizes
no implementation, commit, host change, process, supervisor, controller,
worker, watchdog, adapter, endpoint, pipe, FIFO, journal instance, tombstone,
spawn intent, operation, output bound, promoted object, capacity artifact,
custody disposition, author decision file, capability, lease, batch,
activation artifact, production call-graph manifest, entropy, E1/E2/E3 spend,
world, learner, candidate, Q attempt, Q/C object, datum, outcome, Proof, or
claim movement. It predicts no qualification and no C1–C6 outcome. Process
invalidity, resource exhaustion, and missing evidence remain infrastructure
facts and are nowhere treated as scientific evidence. The §N1.8 example is
patterned synthetic arithmetic that cannot correspond to any real activation
record or operation; no decision file, disposition object, or capacity record
is created by this document.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Its only next authorization step is
independent bounded X/Y confirmation of the **v2.1.2 bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
