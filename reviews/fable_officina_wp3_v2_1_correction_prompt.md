# Fable 5 bounded correction: Officina WP-3 v2.1

Work in `/home/master/llm_projects/philosophia`. Read the v2 contract, its
closure, and both focused v2 confirmations. Preserve all existing files and
create only:

1. `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md`
2. `reviews/fable_officina_wp3_v2_1_closure.md`

V2.1 must be a complete replacement candidate incorporating v2 plus only the
bounded corrections below. Do not edit v2. A single replacement file is
required so the eventual `contract_sha256` can bind one exact committed file,
not an informal base/addendum composition.

Do not commit. Create no entropy, world, frame instance, sample, panel,
candidate, datum, ledger event, root, lock, escrow, or outcome. Do not activate
T or execute a learner/T/Q/C process. Do not select or sign any token.

## Governing reviews

- `reviews/opus_officina_wp3_v2_confirmation.md`:
  `REVISE_OFFICINA_WP3_V2`, V2-1..V2-4.
- `reviews/sol_officina_wp3_v2_confirmation.md`:
  `REVISE_OFFICINA_WP3_V2`, two exact Major repairs.

Every substantive v1 repair is already confirmed closed. Do not reopen frame
membership, CH-1, CH-2, either OR option, transport, T-dev geometry, typed
outcome, small-stratum rule, depletion arithmetic, claim boundary, or
multiplicity except where the exact corrections below necessarily clarify text.

## Exact bounded corrections

### 1. Total ordered oracle wire classifier

Replace v2 section 4's partial refusal grammar with a total deterministic
classifier over raw input bytes. Pin the universe and precedence so every byte
string yields exactly one of three refusals or one valid answer:

1. `MALFORMED_QUERY_STRUCTURE` if the raw bytes are not the exact WP-2
   canonical-JSON encoding of one object with exactly keys `u` and `v`, no
   duplicate/extra/missing keys, and both values strings. Invalid JSON,
   non-canonical JSON, non-object input, duplicate keys, and wrong value types
   all route here.
2. `MALFORMED_QUERY_BYTE` if structure is valid but either decoded string
   contains any character/byte outside ASCII `R (0x52)` and `L (0x4C)`.
3. `MALFORMED_QUERY_LENGTH` if structure and alphabet are valid but either side
   exceeds `Lambda`.
4. Otherwise return canonical JSON integer `0` or `1` from the oracle rule.

The order above is normative: a joint illegal-byte/over-length query is BYTE;
any structurally invalid encoding is STRUCTURE before content inspection. Empty
strings remain valid. Refusal bytes are the exact canonical JSON objects
`{"refusal":"<CODE>"}`; refusals carry no bit and mutate no state. Clarify the
separation between raw wire decoding and the mathematical `(u,v)` oracle, while
preserving the capability boundary and PAD/SEP exclusion.

### 2. Governing paths and exact contract hash

- Correct the preserved v1 path to
  `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md`.
- In the frame schema, define `contract_sha256` as SHA-256 of the exact bytes of
  the committed
  `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md` file
  named and hash-pinned in the future WP-3 author-signature record. State that
  the contract file contains no frame hash, so the relation is acyclic. The
  selected token strings are independently present in the frame JSON.
- Soften the optional T-dev sentence: the near band is adjacent to one frame
  edge, while qualification may still require transfer across the selected
  frame's full scale range; the distal band is deliberate scale stress. Do not
  claim the design is not primarily scale transfer.

### 3. Common C-randomization protocol

Insert the following normative meaning before the OR alternatives, preserving
it in substance exactly:

> The block sample and every orientation realization are derived from the same
> post-lock secret C root under distinct typed PRF domains whose exact byte
> encodings are locked and reviewed at WP-10. The joint mapping must make the
> stratum sample SRSWOR and independent of orientation randomization. Under
> OR-2, for every eligible subset `s`,
> `Pr(S_h=s | r)=1/binom(N_h,n_h)`. Under OR-1, sample membership uses the
> sample domain and fair bits for sampled blocks use the independent orientation
> domain. Under OR-2, the complete orientation vector is derived and sealed
> first under the orientation domain; only then is sample membership derived
> under the sample domain. Both components form one durable, sealed,
> non-redrawable `C_design_realization_id` before any C trajectory. Failure
> never authorizes redraw.

WP-3 owns independence, order, and non-redraw. WP-10 owns the exact PRF domain
byte tags and implementation after lock. Do not generate either now.

### 4. Correct OR-2 estimator and variance

Replace the OR-2 realization/estimation text with the following mathematical
contract in substance exactly:

> After the scientific lock and C-root creation, and before C sample membership
> or any trajectory, the full-frame orientation vector
> `r in {0,1}^{N_C}` (ascending block `p`) is derived, sealed, and bound into
> `C_design_realization_id` under the common protocol. The target is
> `theta(r)=sum_h W_h(1/N_h)sum_{b in F_h}D_b(r_b)`, and the public claim is
> explicitly conditional on that sealed vector. Conditional on `r`,
> `theta_hat(r)=sum_h(W_h/n_h)sum_{b in S_h}D_b(r_b)` is design-unbiased, with
> `Var[theta_hat(r)|r]=sum_h W_h^2(1-f_h)S^2_{D(r),h}/n_h`; each sampled block
> reveals its orientation-specific contribution, not the full-frame estimand.
> Ordinary SRSWOR variance estimation is available subject to the small-stratum
> rule, and census FPC zero is exact for `theta(r)` subject to the locked
> learner-seed scope.

Do not alter OR-1 except to bind it to the common domain-separation protocol.
Neither option is selected.

### 5. Complete `H_preC` and Q information boundary

Replace v2's information-boundary paragraph with this meaning, preserving all
distinctions:

> `H_preC` retains and hashes the complete charter-required Q attempt,
> validity, released-output, stopping, depletion, and promotion history. For
> downstream routing and design identity, Q may contribute only the mechanical
> fact that the first valid `Q_PASS` occurred and the exact automatically
> promoted candidate/stack identity; neither is C evidence. The competence
> binary is used only for routing. It, Q-world identities, responses, estimates,
> variances, depletion history, and every other scientific Q quantity may not
> tune C sample size, endpoint, margins, population, or analysis and may not
> enter C evidence. Predeclared label-free resource telemetry may inform
> engineering caps only.

The complete history is conditioned on and auditable; it is not erased merely
because its quantities are forbidden from C planning/evidence.

## Closure and confirmation packet

In `reviews/fable_officina_wp3_v2_1_closure.md` provide:

- exactly one verdict:
  `READY_FOR_OFFICINA_WP3_V2_1_FINAL_CONFIRMATION`,
  `REVISE_OFFICINA_WP3_V2_1`, or `BLOCKED_OFFICINA_WP3_V2_1`;
- a five-row delta table covering oracle totality, path, contract hash/T-dev
  wording, common randomization+OR-2, and `H_preC`;
- explicit confirmation that no other contract cell changed;
- the unchanged five-token packet and recommendations, still unsigned;
- two bounded yes/no questions for Opus and two for Sol, restricted to these
  corrections;
- confirmation that `scripts/verify_officina_wp12.py` remains green and the
  exact bootstrap directory is unchanged;
- negative space: no author token, WP-4, entropy, world, T activation, Q/C
  process, root, lock, escrow, datum, outcome, Proof, or claim movement.

The next review is a literal bounded confirmation of v2.1, not another design
round. Do not predict qualification or scientific direction.
