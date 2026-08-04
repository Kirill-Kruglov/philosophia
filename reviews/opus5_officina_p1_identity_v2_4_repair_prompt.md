# Officina P1 identity v2.4: bounded satisfiability repair

You are Claude Code Opus 5, specification author. Produce a narrowly scoped v2.4 correction. You are **not** the independent X reviewer.

## Governing inputs

Read:

- identity packet chain through `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md`;
- `reviews/opus_officina_p1_identity_v2_3_final_x_confirmation.md`;
- `reviews/sol_officina_p1_identity_v2_3_final_y_confirmation.md`;
- the v2.3 closure and every signed locus those reviews cite.

Y confirmed v2.3 for author selection. X returned `REVISE` on four fail-closed satisfiability defects and disclosed that it was a self-review. Preserve every Y-confirmed scientific/governance boundary. Repair only the X findings below.

## Mandatory repairs

Adopt X §7 `R-1` through `R-7` in full:

1. **`chdir` scope:** permit exactly the signed PCS preflight `os.chdir("/")` before any name is opened; continue to forbid every other `chdir`, all `fchdir`, symlink and link creation in production roots.
2. **`dir_fd` scope:** prohibit `dir_fd` only for pinned `claim_path`/`lease_path`; require every other `dir_fd` to be a plain Name bound from signed fd 5/fd 6 or the protocol's held-descriptor set, using only the already admitted single-assignment lookup.
3. **Operand-kind split:** distinguish path-operand and descriptor-operand read calls exactly as X R-3 specifies. Apply PA-5/PA-7 only to path operands. Descriptor operands must be plain Names with exactly one approved binding; no new taint, transitivity or analysis kind.
4. **Write count:** state exactly two writes **whose path operand is a pinned path Name**, not two writes in all roots. Preserve ordinary `PC-N` durable installs.
5. **Imperative safety:** a write call shall contain no read expression and bind no byte string; violation is static.
6. **Producer accounting:** add the five governed-mapping producers to `S-25m`, explicitly distinct from the five accessors.
7. **Schema discriminator:** state that PG-4's sole literal-key `"schema"` read is the discriminator and not the later parse; it binds no other value and is the only pre-gate content read.

Recompute all affected counts and fixtures. Demonstrate satisfiability for the signed PCS preflight, fd-relative operations, claim/lease installs and reads, four peer installs, descriptor reads, `/proc/self/fd` constants and ordinary `PC-N` paths.

## Preserved surfaces

Do not change PA-1/2/3/4/8/9, PT-1, CA-1..CA-5, PG-1..PG-3, PG-5..PG-7, S-25p, MS-1L/MS-13/MS-14, CR/M-R4, EV-3/C-6/LD, conditional information wording, destinations, author recommendation, terminal routes or any scientific cell except where a mechanical cross-reference/count must follow R-1..R-7.

Do not add a new root, schema, destination, invalidity cause, authority, option or author token. No code or existing file may be modified.

## Deliverables

Write exactly:

- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md`
- `reviews/opus5_officina_p1_process_claim_identity_choice_v2_4_closure.md`

The closure must:

- emit `READY_FOR_OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_AND_BOUNDED_Y_CONFIRMATION` or a precise blocker;
- disposition B-1..B-4 and R-1..R-7 one-to-one;
- show exact revised counts and positive/negative fixtures;
- preserve the Y v2.3 confirmation but request a bounded Y no-regression check on changed bytes;
- explicitly require the next X review to be performed by an agent that did not author v2.3/v2.4, preferably Claude Opus 4.8 or Fable 5;
- authorize nothing and keep `T = NOT_ACTIVATED`.

Do not commit.
