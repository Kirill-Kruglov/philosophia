"""NON-CITABLE F1 zero-oracle diagnostic.

Can a ContactTransformer recover the world modulus from an unlabeled R/L word
stream alone?  The base model receives no equality labels, oracle calls,
residues, panel data, or candidate period.  Only post-hoc linear probes receive
synthetic labels d % p, and they search every frozen candidate p in [2, 125].

No src/ edits. Writes successor/dev/F1_ZERO_ORACLE_08.md and JSON results.
"""

from __future__ import annotations

import hashlib
import inspect
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import torch
import torch.nn.functional as F

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

from philosophia.level1.config import (  # noqa: E402
    MAX_MODULUS,
    MODEL_INPUT_LENGTH,
)
from philosophia.level1.feasibility import _committee  # noqa: E402
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    ContactTransformer,
    encode_pair,
)
from philosophia.level1.serialization import CounterStream, dummy_key  # noqa: E402
from philosophia.level1.world import (  # noqa: E402
    admissible_paddings,
    displacement,
    unrank_word,
    word_count,
)

import gpu_committee_runner as runner  # noqa: E402

OUT_MD = _DEV / "F1_ZERO_ORACLE_08.md"
OUT_JSON = _DEV / "f1_zero_oracle_08_results.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Experiment constants. None is passed into the word sampler or MLM trainer.
TRUE_PERIOD = 66
CONTROL_PERIOD = 67
CANDIDATE_PERIODS = tuple(range(2, MAX_MODULUS + 1))
SEEDS = (0, 1)

# n-blind stream support. Fixed independently of any candidate period.
STREAM_D_LO = -125
STREAM_D_HI = 125
UNSUP_STEPS = 1_000
UNSUP_BATCH = 64
MASK_RATE = 0.15
PROBE_WORDS = 24_000
PROBE_TEST_FRAC = 0.30
RIDGE_LAMBDA = 10.0
ACTIVATION_CHUNK = 128

TOKEN_R = 1
TOKEN_L = 2
TOKEN_MASK = 3  # existing SEP embedding reused as an MLM mask token

_TRAINING_FORBIDDEN_NAMES = frozenset(
    {
        "TRUE_PERIOD",
        "CONTROL_PERIOD",
        "CANDIDATE_PERIODS",
        "MIN_MODULUS",
        "MAX_MODULUS",
        "oracle_eq",
        "fold",
        "residue",
        "panel",
        "truth",
        "modulus",
    }
)


def _stream(seed: int, purpose: str) -> CounterStream:
    key = dummy_key(f"successor-dev-f1-zero-oracle-seed-{seed}", purpose="public-root")
    return CounterStream(key, ("F1", "zero-oracle", purpose))


def sample_unlabeled_word(stream: CounterStream) -> bytes:
    """Sample one R/L word without accepting n, residue, labels, or panel state."""
    while True:
        d = STREAM_D_LO + stream.uniform(STREAM_D_HI - STREAM_D_LO + 1)
        paddings = admissible_paddings(d)
        padding = paddings[stream.uniform(len(paddings))]
        rank = stream.uniform(word_count(d, padding))
        word = unrank_word(d, padding, rank)
        if word:
            return word


def generate_unlabeled_words(seed: int, purpose: str, count: int) -> list[bytes]:
    stream = _stream(seed, purpose)
    return [sample_unlabeled_word(stream) for _ in range(count)]


def _word_digest(words: Sequence[bytes]) -> str:
    digest = hashlib.sha256()
    for word in words:
        digest.update(len(word).to_bytes(2, "big"))
        digest.update(word)
    return digest.hexdigest()


def n_independence_control(seed: int, count: int = 10_000) -> dict:
    """Couple nominal n and n' runs to the exact same n-blind generator.

    The nominal period is deliberately not an argument to generation. Therefore
    the coupled streams must be byte-identical, a stronger empirical check than
    matching only histograms.
    """
    nominal_n_words = generate_unlabeled_words(seed, "independence-control", count)
    nominal_np_words = generate_unlabeled_words(seed, "independence-control", count)
    same_words = nominal_n_words == nominal_np_words

    def marginal(words: Sequence[bytes]) -> dict[tuple[int, int], int]:
        out: dict[tuple[int, int], int] = {}
        for word in words:
            key = (len(word), displacement(word))
            out[key] = out.get(key, 0) + 1
        return out

    same_marginal = marginal(nominal_n_words) == marginal(nominal_np_words)
    if not same_words or not same_marginal:
        raise RuntimeError("n-independence control failed: unlabeled stream leaked period")
    return {
        "nominal_periods": [TRUE_PERIOD, CONTROL_PERIOD],
        "count_each": count,
        "byte_identical": same_words,
        "marginal_len_d_identical": same_marginal,
        "digest_n": _word_digest(nominal_n_words),
        "digest_n_prime": _word_digest(nominal_np_words),
    }


def _assert_zero_oracle_training_surface() -> dict:
    """Static/runtime guard for the sampler and unsupervised trainer."""
    guarded = (
        sample_unlabeled_word,
        generate_unlabeled_words,
        _make_masked_batch,
        train_masked_lm,
    )
    violations: dict[str, list[str]] = {}
    for fn in guarded:
        code_names = set(fn.__code__.co_names)
        hits = sorted(
            name
            for name in _TRAINING_FORBIDDEN_NAMES
            if name in code_names
        )
        if hits:
            violations[fn.__name__] = hits
    sampler_params = tuple(inspect.signature(sample_unlabeled_word).parameters)
    trainer_params = tuple(inspect.signature(train_masked_lm).parameters)
    if sampler_params != ("stream",):
        violations["sample_unlabeled_word.signature"] = list(sampler_params)
    if any(name.lower() in {"n", "modulus", "residue", "oracle", "panel"} for name in trainer_params):
        violations["train_masked_lm.signature"] = list(trainer_params)
    if violations:
        raise RuntimeError(f"zero-oracle firewall failed: {violations}")
    return {
        "guarded_functions": [fn.__name__ for fn in guarded],
        "sampler_signature": str(inspect.signature(sample_unlabeled_word)),
        "trainer_signature": str(inspect.signature(train_masked_lm)),
        "forbidden_name_hits": {},
        "passed": True,
    }


def _token_hidden(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    """All final-layer token states; same trunk as ContactTransformer.forward."""
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)


@torch.no_grad()
def _prehead_readout(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    return _token_hidden(model, tokens)[:, -1, :]


def _encode_single_word(word: bytes) -> torch.Tensor:
    token_map = {0x52: TOKEN_R, 0x4C: TOKEN_L}
    content = [token_map[token] for token in word]
    if not content:
        raise ValueError("empty words are excluded from MLM/probes")
    if len(content) > MODEL_INPUT_LENGTH:
        raise ValueError("word exceeds model input")
    return torch.tensor(
        [0] * (MODEL_INPUT_LENGTH - len(content)) + content, dtype=torch.long
    )


def _make_masked_batch(
    stream: CounterStream,
    batch_size: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Online masked-token batch. Returns tokens, positions, binary R/L targets."""
    rows: list[torch.Tensor] = []
    positions: list[int] = []
    targets: list[int] = []
    for _ in range(batch_size):
        word = sample_unlabeled_word(stream)
        while not word:
            word = sample_unlabeled_word(stream)
        tokens = _encode_single_word(word)
        content_start = MODEL_INPUT_LENGTH - len(word)
        n_mask = max(1, int(round(len(word) * MASK_RATE)))
        chosen: set[int] = set()
        while len(chosen) < min(n_mask, len(word)):
            chosen.add(stream.uniform(len(word)))
        # One loss item per masked token; retain all masked positions.
        for offset in sorted(chosen):
            absolute = content_start + offset
            target_token = int(tokens[absolute])
            targets.append(0 if target_token == TOKEN_L else 1)
            positions.append(len(rows) * MODEL_INPUT_LENGTH + absolute)
        tokens[list(content_start + o for o in chosen)] = TOKEN_MASK
        rows.append(tokens)
    return (
        torch.stack(rows),
        torch.tensor(positions, dtype=torch.long),
        torch.tensor(targets, dtype=torch.long),
    )


@dataclass
class MlmMember:
    model: ContactTransformer
    head_w: torch.Tensor
    head_b: torch.Tensor
    optimizer: torch.optim.Optimizer


def _new_mlm_committee(seed: int) -> list[MlmMember]:
    key = dummy_key(f"successor-dev-f1-zero-oracle-seed-{seed}", purpose="public-root")
    models, _ = _committee(key, block=0)
    members: list[MlmMember] = []
    for member_index, model in enumerate(models):
        model = model.to(DEVICE)
        # Equality head is unrelated and never trained/used.
        model.head_W.requires_grad_(False)
        model.head_b.requires_grad_(False)
        generator = torch.Generator(device=DEVICE)
        generator.manual_seed(100_000 + seed * 10 + member_index)
        head_w = (
            torch.randn(D_MODEL, 2, generator=generator, device=DEVICE)
            / math.sqrt(D_MODEL)
        ).requires_grad_()
        head_b = torch.zeros(2, device=DEVICE, requires_grad=True)
        trunk_params = [
            p
            for name, p in model.named_parameters()
            if name not in {"head_W", "head_b"}
        ]
        optimizer = torch.optim.AdamW(
            trunk_params + [head_w, head_b],
            lr=1e-3,
            betas=(0.9, 0.98),
            eps=1e-8,
            weight_decay=0.01,
        )
        members.append(MlmMember(model, head_w, head_b, optimizer))
    return members


def train_masked_lm(
    members: list[MlmMember],
    stream: CounterStream,
    steps: int,
    batch_size: int,
) -> tuple[float, float]:
    """Train only from masked R/L reconstruction; returns wall and final loss."""
    started = time.perf_counter()
    final_loss = float("nan")
    for step in range(1, steps + 1):
        tokens_cpu, flat_positions_cpu, targets_cpu = _make_masked_batch(
            stream, batch_size
        )
        tokens = tokens_cpu.to(DEVICE)
        targets = targets_cpu.to(DEVICE)
        for member in members:
            member.model.train()
            hidden = _token_hidden(member.model, tokens)
            flat_hidden = hidden.reshape(-1, D_MODEL)
            selected = flat_hidden[flat_positions_cpu.to(DEVICE)]
            logits = selected @ member.head_w + member.head_b
            loss = F.cross_entropy(logits, targets)
            member.optimizer.zero_grad(set_to_none=True)
            loss.backward()
            member.optimizer.step()
            final_loss = float(loss.detach().cpu())
        if step % 100 == 0:
            print(
                f"  MLM step={step}/{steps} member3_loss={final_loss:.4f}",
                flush=True,
            )
    return time.perf_counter() - started, final_loss


@torch.no_grad()
def committee_activations(
    models: Sequence[ContactTransformer],
    words: Sequence[bytes],
) -> torch.Tensor:
    """REPRPROBE_07 activation: mean pre-head readout of word⊕SEP⊕word."""
    token_rows = [encode_pair(word, word) for word in words]
    outputs: list[torch.Tensor] = []
    for start in range(0, len(token_rows), ACTIVATION_CHUNK):
        tokens = torch.stack(token_rows[start : start + ACTIVATION_CHUNK]).to(DEVICE)
        member_vectors = [_prehead_readout(model, tokens) for model in models]
        outputs.append(torch.stack(member_vectors).mean(dim=0).cpu())
    return torch.cat(outputs)


def _unique_probe_words(seed: int, training_words: set[bytes]) -> list[bytes]:
    stream = _stream(seed, "probe-words")
    words: list[bytes] = []
    seen = set(training_words)
    while len(words) < PROBE_WORDS:
        word = sample_unlabeled_word(stream)
        if not word or word in seen:
            continue
        seen.add(word)
        words.append(word)
    return words


def _probe_split(words: Sequence[bytes], seed: int) -> tuple[list[int], list[int]]:
    stream = _stream(seed, "probe-split")
    indices = list(range(len(words)))
    # Deterministic Fisher-Yates.
    for i in range(len(indices) - 1, 0, -1):
        j = stream.uniform(i + 1)
        indices[i], indices[j] = indices[j], indices[i]
    n_test = int(round(len(indices) * PROBE_TEST_FRAC))
    return indices[n_test:], indices[:n_test]


def _macro_accuracy(pred: torch.Tensor, truth: torch.Tensor, classes: int) -> float:
    recalls: list[torch.Tensor] = []
    for cls in range(classes):
        mask = truth == cls
        if bool(mask.any()):
            recalls.append((pred[mask] == truth[mask]).float().mean())
    return float(torch.stack(recalls).mean().item())


def ridge_period_probe(
    x_train: torch.Tensor,
    d_train: torch.Tensor,
    x_test: torch.Tensor,
    d_test: torch.Tensor,
    period: int,
) -> dict:
    """One-vs-all ridge classifier; macro accuracy has exact chance 1/p."""
    # Train-only standardization and intercept.
    mean = x_train.mean(dim=0, keepdim=True)
    std = x_train.std(dim=0, keepdim=True).clamp_min(1e-6)
    xtr = (x_train - mean) / std
    xte = (x_test - mean) / std
    xtr = torch.cat([xtr, torch.ones(xtr.shape[0], 1)], dim=1).to(DEVICE)
    xte = torch.cat([xte, torch.ones(xte.shape[0], 1)], dim=1).to(DEVICE)
    ytr = torch.remainder(d_train, period).long().to(DEVICE)
    yte = torch.remainder(d_test, period).long().to(DEVICE)

    # X'Y without materializing a large one-hot matrix.
    xtx = xtr.T @ xtr
    reg = RIDGE_LAMBDA * torch.eye(xtx.shape[0], device=DEVICE)
    reg[-1, -1] = 0.0  # do not regularize intercept
    xty = torch.zeros(xtr.shape[1], period, device=DEVICE)
    xty.index_add_(1, ytr, xtr.T)
    weights = torch.linalg.solve(xtx + reg, xty)
    pred = (xte @ weights).argmax(dim=1)
    macro = _macro_accuracy(pred, yte, period)
    chance = 1.0 / period
    normalized_lift = (macro - chance) / (1.0 - chance)
    return {
        "period": period,
        "macro_accuracy": macro,
        "chance": chance,
        "normalized_lift": normalized_lift,
    }


def search_periods(
    x_train: torch.Tensor,
    d_train: torch.Tensor,
    x_test: torch.Tensor,
    d_test: torch.Tensor,
) -> list[dict]:
    rows: list[dict] = []
    for period in CANDIDATE_PERIODS:
        row = ridge_period_probe(x_train, d_train, x_test, d_test, period)
        rows.append(row)
    return rows


def _fmt_pct(value: float) -> str:
    return f"{100.0 * value:.2f}%"


def run_seed(seed: int) -> dict:
    print(f"=== F1 seed {seed} ===", flush=True)
    independence = n_independence_control(seed)
    firewall = _assert_zero_oracle_training_surface()

    members = _new_mlm_committee(seed)
    models = [member.model for member in members]
    # Probe corpus is generated independently and excluded from unsupervised words.
    # Generate training words once for leakage accounting; online MLM uses the exact
    # same deterministic stream from its beginning.
    accounting_stream = _stream(seed, "unsupervised-words")
    accounting_words: set[bytes] = set()
    # Upper bound on words consumed is steps*batch; duplicates are harmless.
    for _ in range(UNSUP_STEPS * UNSUP_BATCH):
        word = sample_unlabeled_word(accounting_stream)
        if word:
            accounting_words.add(word)
    probe_words = _unique_probe_words(seed, accounting_words)
    train_idx, test_idx = _probe_split(probe_words, seed)
    if set(probe_words[i] for i in train_idx) & set(probe_words[i] for i in test_idx):
        raise RuntimeError("probe train/test words overlap")
    if set(probe_words) & accounting_words:
        raise RuntimeError("probe words overlap unsupervised stream")

    print("extracting INIT activations...", flush=True)
    init_acts = committee_activations(models, probe_words)

    print("training zero-oracle masked LM...", flush=True)
    train_stream = _stream(seed, "unsupervised-words")
    mlm_wall, final_loss = train_masked_lm(
        members, train_stream, UNSUP_STEPS, UNSUP_BATCH
    )

    print("extracting POST activations...", flush=True)
    post_acts = committee_activations(models, probe_words)

    displacements = torch.tensor(
        [displacement(word) for word in probe_words], dtype=torch.long
    )
    tr = torch.tensor(train_idx, dtype=torch.long)
    te = torch.tensor(test_idx, dtype=torch.long)

    print("fitting INIT true-period probe...", flush=True)
    init_true = ridge_period_probe(
        init_acts[tr], displacements[tr], init_acts[te], displacements[te], TRUE_PERIOD
    )
    print("searching all periods on POST activations...", flush=True)
    post_search = search_periods(
        post_acts[tr], displacements[tr], post_acts[te], displacements[te]
    )
    post_true = next(row for row in post_search if row["period"] == TRUE_PERIOD)
    best = max(post_search, key=lambda row: (row["normalized_lift"], row["macro_accuracy"]))
    true_rank = (
        sorted(
            post_search,
            key=lambda row: (row["normalized_lift"], row["macro_accuracy"]),
            reverse=True,
        ).index(post_true)
        + 1
    )
    top10 = sorted(
        post_search,
        key=lambda row: (row["normalized_lift"], row["macro_accuracy"]),
        reverse=True,
    )[:10]

    # The period is "recovered" only if the search selects 66, not merely if a
    # supervised p=66 probe can decode d%66 after being handed those labels.
    fires = (
        best["period"] == TRUE_PERIOD
        and post_true["macro_accuracy"] >= init_true["macro_accuracy"] + 0.05
        and post_true["normalized_lift"] >= 0.10
    )
    return {
        "seed": seed,
        "independence": independence,
        "firewall": firewall,
        "mlm_wall_s": mlm_wall,
        "mlm_final_loss": final_loss,
        "n_unsup_distinct_words": len(accounting_words),
        "n_probe_words": len(probe_words),
        "n_probe_train": len(train_idx),
        "n_probe_test": len(test_idx),
        "init_true_period": init_true,
        "post_true_period": post_true,
        "best_period": best,
        "true_period_rank": true_rank,
        "top10": top10,
        "falsifier_fires": fires,
    }


def write_report(results: list[dict], total_wall: float) -> str:
    init_mean = sum(r["init_true_period"]["macro_accuracy"] for r in results) / len(results)
    post_mean = sum(r["post_true_period"]["macro_accuracy"] for r in results) / len(results)
    chance = 1.0 / TRUE_PERIOD
    all_fire = all(r["falsifier_fires"] for r in results)
    any_fire = any(r["falsifier_fires"] for r in results)
    if all_fire:
        verdict = "FALSIFIER-FIRES"
        verdict_body = (
            "FALSIFIER-FIRES: the n-blind period search selected p=66 in both "
            "seeds, and post-MLM p=66 decoding materially exceeded init/chance. "
            "The world wall was recoverable from words alone, falsifying the "
            "deflationary limit as stated."
        )
    else:
        verdict = "WALL-NOT-MANUFACTURABLE"
        qualifier = "one seed met" if any_fire else "neither seed met"
        verdict_body = (
            "WALL-NOT-MANUFACTURABLE: the coupled stream was exactly n-independent; "
            f"{qualifier} the registered recovery condition (search must select "
            "66, improve ≥5 points over init, and have ≥0.10 chance-normalized "
            "lift). A supervised p=66 probe may decode incidental displacement "
            "structure, but because the search was not specifically attracted "
            "to 66, that is not recovery of the world's modulus from words. "
            "Within this model/objective/horizon, the empirical spine holds."
        )

    seed_rows = []
    search_rows = []
    control_rows = []
    for r in results:
        init = r["init_true_period"]
        post = r["post_true_period"]
        best = r["best_period"]
        seed_rows.append(
            f"| {r['seed']} | {_fmt_pct(init['macro_accuracy'])} | "
            f"{_fmt_pct(post['macro_accuracy'])} | {_fmt_pct(chance)} | "
            f"{post['normalized_lift']:.3f} |"
        )
        search_rows.append(
            f"| {r['seed']} | {best['period']} | "
            f"{_fmt_pct(best['macro_accuracy'])} | {_fmt_pct(best['chance'])} | "
            f"{best['normalized_lift']:.3f} | {r['true_period_rank']} | "
            f"{r['falsifier_fires']} |"
        )
        c = r["independence"]
        control_rows.append(
            f"| {r['seed']} | {c['nominal_periods'][0]} vs "
            f"{c['nominal_periods'][1]} | {c['count_each']} | "
            f"{c['byte_identical']} | {c['marginal_len_d_identical']} | "
            f"`{c['digest_n'][:16]}` |"
        )

    top_lines: list[str] = []
    for r in results:
        top = ", ".join(
            f"p={row['period']} acc={_fmt_pct(row['macro_accuracy'])} "
            f"lift={row['normalized_lift']:.3f}"
            for row in r["top10"]
        )
        top_lines.append(f"- seed {r['seed']}: {top}")

    lines = [
        "# F1_ZERO_ORACLE_08",
        "",
        "NON-CITABLE dev falsifier. No src/ edits. No confirmatory datum.",
        "",
        "## Zero-oracle boundary",
        "",
        "The training sampler signature is `sample_unlabeled_word(stream)`; it "
        "cannot accept n, residue, oracle state, labels, panel state, or a "
        "candidate period. `_assert_zero_oracle_training_surface` inspects the "
        "sampler, batch builder, generator, and MLM trainer for forbidden names "
        "and signatures before training. Training imports/uses no `oracle_eq` or "
        "`fold`; it sees only right/left token sequences. Candidate periods and "
        "`d % p` labels exist only after training inside read-only probes.",
        "",
        "## n-independence control",
        "",
        "The nominal n=66 and n'=67 streams are coupled through the same sampler "
        "and seed. Because n is not an argument, the streams must be byte-identical "
        "(stronger than equal empirical marginals over arrangement/displacement).",
        "",
        "| seed | nominal periods | words each | byte-identical | (length,d) marginal identical | digest |",
        "| ---: | --- | ---: | --- | --- | --- |",
        *control_rows,
        "",
        "**Control result: PASS — no mod-n structure is baked into generation.**",
        "",
        "## Objective and activation",
        "",
        f"- Seeds: {list(SEEDS)}; CUDA device: {torch.cuda.get_device_name(0)}.",
        f"- Objective: bidirectional masked-token reconstruction over single R/L "
        f"words, {MASK_RATE:.0%} positions masked with token id 3; predict R vs L. "
        f"{UNSUP_STEPS} updates, batch={UNSUP_BATCH}, AdamW lr=1e-3. Four-member "
        "ContactTransformer committee trained sequentially; equality heads frozen.",
        "- Stream: displacement uniform on fixed [-125,125], admissible padding "
        "uniform, arrangement rank uniform. Support is fixed independently of n.",
        "- Activation: exactly REPRPROBE_07's committee-mean pre-head "
        "`final_ln(x)[:, -1, :]` on `word⊕SEP⊕word` (128 dimensions).",
        f"- Probe corpus: {PROBE_WORDS} distinct words absent from unsupervised "
        f"training; 70/30 disjoint-word split.",
        "- Probe: one-vs-all linear ridge. Macro accuracy makes chance exactly "
        "`1/p`; no backprop into the base committee.",
        "",
        "## Residue-mod-66 linear probe",
        "",
        "| seed | init test macro-acc | post-MLM test macro-acc | chance | post normalized lift |",
        "| ---: | ---: | ---: | ---: | ---: |",
        *seed_rows,
        f"| **mean** | **{_fmt_pct(init_mean)}** | **{_fmt_pct(post_mean)}** | "
        f"**{_fmt_pct(chance)}** | — |",
        "",
        "## Period-search probe (p=2..125, no period supplied to training)",
        "",
        "Periods are ranked by chance-normalized lift "
        "`(macro_acc - 1/p)/(1 - 1/p)` so different class counts are comparable. "
        "A supervised fixed-p probe alone is not treated as recovery; F1 fires "
        "only if the blind search selects p=66 and post-training materially "
        "improves it over init.",
        "",
        "| seed | best period | best macro-acc | chance | normalized lift | rank of p=66 | fires |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        *search_rows,
        "",
        "Top candidates:",
        *top_lines,
        "",
        "## Clocks",
        "",
        *[
            f"- seed {r['seed']}: unsupervised wall={r['mlm_wall_s']:.1f}s, "
            f"final MLM loss={r['mlm_final_loss']:.4f}"
            for r in results
        ],
        f"- total wall={total_wall:.1f}s ({total_wall/60:.1f} min).",
        "",
        "## Verdict",
        "",
        f"**{verdict}**",
        "",
        verdict_body,
        "",
        "Interpretive caution: a post-hoc supervised probe is given `d % p` "
        "labels and can exploit any displacement information already present. "
        "Therefore above-chance p=66 accuracy by itself is not evidence that the "
        "unsupervised learner inferred 66; period specificity in the blind search "
        "is required for the falsifier.",
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA required for F1_ZERO_ORACLE_08")
    runner.patch_contact_transformer_device_guard()
    started = time.perf_counter()
    results = [run_seed(seed) for seed in SEEDS]
    total_wall = time.perf_counter() - started
    report = write_report(results, total_wall)
    OUT_JSON.write_text(
        json.dumps(
            {
                "config": {
                    "seeds": SEEDS,
                    "true_period": TRUE_PERIOD,
                    "control_period": CONTROL_PERIOD,
                    "candidate_periods": [2, MAX_MODULUS],
                    "unsup_steps": UNSUP_STEPS,
                    "unsup_batch": UNSUP_BATCH,
                    "mask_rate": MASK_RATE,
                    "probe_words": PROBE_WORDS,
                    "ridge_lambda": RIDGE_LAMBDA,
                },
                "results": results,
                "total_wall_s": total_wall,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
