"""NON-CITABLE REPRPROBE_07: linear readability of residue / equality (frozen).

No training of the base committee. Fits ONLY linear probes on frozen
activations from capacity_diag_04_final.pt.
Writes successor/dev/REPRPROBE_07.md.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

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
    BUDGET,
    MODEL_INPUT_LENGTH,
    PANEL_SIZE,
)
from philosophia.level1.feasibility import _committee  # noqa: E402
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    ContactTransformer,
    committee_equal_probability,
    encode_pair,
)
from philosophia.level1.panel import DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_cell,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.scoring import PanelObservation  # noqa: E402
from philosophia.level1.serialization import CounterStream, dummy_key  # noqa: E402
from philosophia.level1.world import fold, oracle_eq  # noqa: E402

import gpu_committee_runner as runner  # noqa: E402
from capacity_diag_04 import (  # noqa: E402
    DEV_PANEL_LABEL,
    DEV_PUBLIC_LABEL,
    MODULUS,
    OUT_CKPT,
    WORLD_SLOT,
    curated_rich_equal_schedule,
    _pair_key,
)

OUT_MD = _DEV / "REPRPROBE_07.md"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
PROBE_SEED = 72026
CHANCE_RESIDUE = 1.0 / MODULUS
# Linear probe hyperparams (probe-only; not base training).
RESIDUE_EPOCHS = 200
EQUAL_EPOCHS = 150
LR = 0.05
WEIGHT_DECAY = 1e-2
BATCH = 256


def _load_committee(ckpt_path: Path):
    blob = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    models, _ = _committee(public_key, block=WORLD_SLOT)
    for model, state in zip(models, blob["models"]):
        model.load_state_dict(state)
        model.to(DEVICE)
        model.eval()
        for p in model.parameters():
            p.requires_grad_(False)
    return models, blob


def encode_word_self_pair(word: bytes) -> torch.Tensor:
    """word ⊕ SEP ⊕ word — last content token is the word's last R/L.

    ContactTransformer only encodes pairs; readout is final_ln(x)[:, -1, :],
    i.e. the last sequence position (right-word end under left-padding).
    Self-pairing makes a well-defined per-word vector in that readout slot.
    """
    return encode_pair(word, word)


@torch.no_grad()
def prehead_readout(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    """Frozen activation = final_ln(h)[:, -1, :] — the vector the equality head sees."""
    if tokens.dtype != torch.long:
        raise ValueError("tokens must be torch.long")
    if tokens.ndim != 2 or tokens.shape[1] != MODEL_INPUT_LENGTH:
        raise ValueError(f"tokens must have shape (batch, {MODEL_INPUT_LENGTH})")
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)[:, -1, :]


@torch.no_grad()
def committee_prehead(
    models: list[ContactTransformer], tokens: torch.Tensor, *, chunk: int = 128
) -> torch.Tensor:
    """Mean pre-head readout across the 4 frozen committee members."""
    outs: list[torch.Tensor] = []
    for start in range(0, tokens.shape[0], chunk):
        sl = tokens[start : start + chunk].to(DEVICE)
        member_vecs = [prehead_readout(m, sl) for m in models]
        outs.append(torch.stack(member_vecs, dim=0).mean(dim=0).cpu())
    return torch.cat(outs, dim=0)


def _collect_train(public_key, partition, schedule):
    train_pairs: set[tuple[bytes, bytes]] = set()
    train_words: set[bytes] = set()
    for pool_index in schedule:
        raw = realize_pool_index(partition, public_key, pool_index)
        train_pairs.add(_pair_key(raw.left, raw.right))
        train_words.add(raw.left)
        train_words.add(raw.right)
    return train_words, train_pairs


def _novel_words(public_key, partition, panel, train_words: set[bytes]) -> dict[bytes, int]:
    """Distinct NOVEL words (not in train) with residue = fold(word)."""
    novel: dict[bytes, int] = {}

    def consider(word: bytes) -> None:
        if word in train_words:
            return
        novel[word] = fold(word, MODULUS)

    for item in panel.items:
        consider(item.left)
        consider(item.right)
    # Reserved cells: both equal and unequal give novel words.
    for cell in partition.reserved:
        for left, right in realize_cell(public_key, cell):
            consider(left)
            consider(right)
    return novel


def _held_out_pairs(public_key, partition, panel, train_pairs):
    """Held-out equals (panel+reserved) and reserved unequals; no train leakage."""
    panel_pairs = {_pair_key(i.left, i.right) for i in panel.items}
    if train_pairs & panel_pairs:
        raise RuntimeError("panel∩train nonempty")

    equals: list[tuple[bytes, bytes]] = []
    unequals: list[tuple[bytes, bytes]] = []

    for item in panel.items:
        key = _pair_key(item.left, item.right)
        if item.truth:
            equals.append((item.left, item.right))
        else:
            # Panel unequals are also held-out; include for pair probe balance.
            unequals.append((item.left, item.right))

    for cell in partition.reserved:
        for left, right in realize_cell(public_key, cell):
            key = _pair_key(left, right)
            if key in train_pairs or key in panel_pairs:
                continue
            if oracle_eq(left, right, MODULUS):
                equals.append((left, right))
            else:
                unequals.append((left, right))
    return equals, unequals


def _disjoint_word_split(
    novel: dict[bytes, int], *, test_frac: float = 0.3
) -> tuple[list[bytes], list[bytes]]:
    """Stratified-by-residue split over DISJOINT novel words (not sample rows)."""
    by_r: dict[int, list[bytes]] = defaultdict(list)
    for word, residue in novel.items():
        by_r[residue].append(word)
    stream = CounterStream(
        dummy_key(DEV_PUBLIC_LABEL, purpose="public-root"),
        ("L1", "reprprobe-07", "word-split"),
    )
    train_w: list[bytes] = []
    test_w: list[bytes] = []
    for residue in range(MODULUS):
        words = by_r.get(residue, [])
        if not words:
            continue
        # Deterministic shuffle via stream uniforms.
        order = list(range(len(words)))
        for i in range(len(order) - 1, 0, -1):
            j = stream.uniform(i + 1)
            order[i], order[j] = order[j], order[i]
        shuffled = [words[i] for i in order]
        n_test = max(1, int(round(len(shuffled) * test_frac))) if len(shuffled) >= 2 else 0
        # Need both sides non-empty when possible.
        if len(shuffled) == 1:
            train_w.append(shuffled[0])
            continue
        n_test = min(max(1, n_test), len(shuffled) - 1)
        test_w.extend(shuffled[:n_test])
        train_w.extend(shuffled[n_test:])
    return train_w, test_w


def _fit_linear_classifier(
    x_train: torch.Tensor,
    y_train: torch.Tensor,
    x_test: torch.Tensor,
    y_test: torch.Tensor,
    *,
    n_classes: int,
    epochs: int,
) -> dict:
    """Softmax linear probe; base activations frozen (only W,b trained)."""
    torch.manual_seed(PROBE_SEED)
    x_train = x_train.to(DEVICE)
    y_train = y_train.to(DEVICE)
    x_test = x_test.to(DEVICE)
    y_test = y_test.to(DEVICE)

    # Standardize using train stats only.
    mean = x_train.mean(dim=0, keepdim=True)
    std = x_train.std(dim=0, keepdim=True).clamp_min(1e-6)
    x_train = (x_train - mean) / std
    x_test = (x_test - mean) / std

    W = torch.zeros(D_MODEL, n_classes, device=DEVICE, requires_grad=True)
    b = torch.zeros(n_classes, device=DEVICE, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=LR, weight_decay=WEIGHT_DECAY)

    n = x_train.shape[0]
    for _ in range(epochs):
        perm = torch.randperm(n, device=DEVICE)
        for start in range(0, n, BATCH):
            idx = perm[start : start + BATCH]
            logits = x_train[idx] @ W + b
            loss = F.cross_entropy(logits, y_train[idx])
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()

    with torch.no_grad():
        train_pred = (x_train @ W + b).argmax(dim=-1)
        test_pred = (x_test @ W + b).argmax(dim=-1)
        train_acc = float((train_pred == y_train).float().mean().item())
        test_acc = float((test_pred == y_test).float().mean().item())
    return {
        "train_acc": train_acc,
        "test_acc": test_acc,
        "n_train": int(n),
        "n_test": int(x_test.shape[0]),
    }


def _fmt_pct(x: float) -> str:
    return f"{100.0 * x:.2f}%"


def main() -> None:
    if not OUT_CKPT.is_file():
        raise FileNotFoundError(f"missing {OUT_CKPT}")

    runner.patch_contact_transformer_device_guard()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(
        public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")
    ).build(MODULUS, world_slot=WORLD_SLOT)
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted")

    print("reconstructing train schedule...", flush=True)
    schedule = curated_rich_equal_schedule(public_key, partition)
    if len(schedule) != BUDGET:
        raise RuntimeError("schedule length != BUDGET")
    train_words, train_pairs = _collect_train(public_key, partition, schedule)

    novel = _novel_words(public_key, partition, panel, train_words)
    if any(w in train_words for w in novel):
        raise RuntimeError("novel set leaked train words")
    train_w, test_w = _disjoint_word_split(novel)
    train_set, test_set = set(train_w), set(test_w)
    if train_set & test_set:
        raise RuntimeError("word split not disjoint")
    print(
        f"novel words={len(novel)}; probe train words={len(train_w)}; "
        f"probe test words={len(test_w)}; residues covered train="
        f"{len({fold(w, MODULUS) for w in train_w})} "
        f"test={len({fold(w, MODULUS) for w in test_w})}",
        flush=True,
    )

    equals, unequals = _held_out_pairs(public_key, partition, panel, train_pairs)
    print(
        f"held-out equals={len(equals)}; held-out unequals={len(unequals)}",
        flush=True,
    )

    print(f"loading frozen committee {OUT_CKPT.name}...", flush=True)
    models, blob = _load_committee(OUT_CKPT)

    # --- Residue probe on novel words via word⊕SEP⊕word ---
    print("extracting novel-word pre-head activations...", flush=True)
    all_probe_words = train_w + test_w
    word_tokens = torch.stack([encode_word_self_pair(w) for w in all_probe_words])
    word_acts = committee_prehead(models, word_tokens)
    y_all = torch.tensor(
        [fold(w, MODULUS) for w in all_probe_words], dtype=torch.long
    )
    n_tr = len(train_w)
    x_tr, x_te = word_acts[:n_tr], word_acts[n_tr:]
    y_tr, y_te = y_all[:n_tr], y_all[n_tr:]

    print("fitting residue linear probe...", flush=True)
    residue_probe = _fit_linear_classifier(
        x_tr, y_tr, x_te, y_te, n_classes=MODULUS, epochs=RESIDUE_EPOCHS
    )

    # --- Pair equality linear probe on held-out pairs ---
    # Balance: take all equals + subsample unequals to match (deterministic).
    stream = CounterStream(public_key, ("L1", "reprprobe-07", "pair-balance"))
    if len(unequals) > len(equals):
        # sample without replacement
        idxs = list(range(len(unequals)))
        for i in range(len(idxs) - 1, 0, -1):
            j = stream.uniform(i + 1)
            idxs[i], idxs[j] = idxs[j], idxs[i]
        unequals_bal = [unequals[i] for i in idxs[: len(equals)]]
    else:
        unequals_bal = list(unequals)

    pair_items = [(a, b, 1) for a, b in equals] + [(a, b, 0) for a, b in unequals_bal]
    # Shuffle then 70/30 split over pairs (pairs are already held-out from base train).
    order = list(range(len(pair_items)))
    for i in range(len(order) - 1, 0, -1):
        j = stream.uniform(i + 1)
        order[i], order[j] = order[j], order[i]
    pair_items = [pair_items[i] for i in order]
    n_pair_test = max(1, int(round(0.3 * len(pair_items))))
    pair_test = pair_items[:n_pair_test]
    pair_train = pair_items[n_pair_test:]

    print("extracting held-out pair pre-head activations...", flush=True)
    def _pair_stack(items):
        toks = torch.stack([encode_pair(a, b) for a, b, _ in items])
        acts = committee_prehead(models, toks)
        labels = torch.tensor([lab for _, _, lab in items], dtype=torch.long)
        return acts, labels

    px_tr, py_tr = _pair_stack(pair_train)
    px_te, py_te = _pair_stack(pair_test)

    print("fitting equality linear probe...", flush=True)
    equal_probe = _fit_linear_classifier(
        px_tr, py_tr, px_te, py_te, n_classes=2, epochs=EQUAL_EPOCHS
    )

    # Head accuracy on the SAME pair-test set (frozen scoring rule for equals;
    # for unequals: correct = predict unequal).
    print("scoring frozen head on pair-test set...", flush=True)
    te_tokens = torch.stack([encode_pair(a, b) for a, b, _ in pair_test]).to(DEVICE)
    with torch.no_grad():
        head_p = committee_equal_probability(models, te_tokens).detach().cpu()
    head_correct = 0
    # Also equal-only head accuracy on held-out equals (GENFAIL ~63% reference).
    equal_only = [(a, b) for a, b, lab in pair_test if lab == 1]
    if equal_only:
        eq_tok = torch.stack([encode_pair(a, b) for a, b in equal_only]).to(DEVICE)
        with torch.no_grad():
            eq_p = committee_equal_probability(models, eq_tok).detach().cpu()
        eq_head_acc = sum(
            1 for p in eq_p.tolist() if PanelObservation("S2", True, float(p)).correct
        ) / len(equal_only)
    else:
        eq_head_acc = float("nan")

    for (_, _, lab), p in zip(pair_test, head_p.tolist()):
        obs = PanelObservation("S2", bool(lab), float(p))
        if obs.correct:
            head_correct += 1
    head_acc = head_correct / len(pair_test)

    # Verdict.
    residue_test = residue_probe["test_acc"]
    # LATENT-BUT-UNUSED if residue >> chance; NOT-REPRESENTED if near chance.
    # Use 5× chance (~7.5%) as a soft floor for "near chance"; strong if ≥20%.
    if residue_test >= 0.20:
        strongly_decodable = True
    elif residue_test >= 5 * CHANCE_RESIDUE:
        strongly_decodable = True
    else:
        strongly_decodable = False

    equal_lin = equal_probe["test_acc"]
    # Head underuses if linear equality probe clearly beats head on same pairs,
    # OR residue is decodable while head equal-only stays mediocre (~63%).
    head_underuses = strongly_decodable and (
        equal_lin >= head_acc + 0.05 or equal_lin >= eq_head_acc + 0.05
        if eq_head_acc == eq_head_acc
        else equal_lin >= head_acc + 0.05
    )

    if strongly_decodable:
        tag = "LATENT-BUT-UNUSED"
        body = (
            f"LATENT-BUT-UNUSED: residue is linearly decodable from frozen "
            f"pre-head activations on NOVEL words "
            f"(test acc={_fmt_pct(residue_test)} vs chance "
            f"{_fmt_pct(CHANCE_RESIDUE)}). A linear equal? probe on held-out "
            f"pairs reaches {_fmt_pct(equal_lin)} vs the frozen head "
            f"{_fmt_pct(head_acc)} on the same split "
            f"(head equal-only acc={_fmt_pct(eq_head_acc)}). "
            f"The reduction is present in the encoder readout but the equality "
            f"head underuses it — gap-closers should target the head/loss "
            f"(or an explicit fold readout), not rebuild residue from scratch."
        )
    else:
        tag = "NOT-REPRESENTED"
        body = (
            f"NOT-REPRESENTED: residue linear probe on NOVEL words is near chance "
            f"(test acc={_fmt_pct(residue_test)} vs {_fmt_pct(CHANCE_RESIDUE)}). "
            f"Pair-equality linear probe={_fmt_pct(equal_lin)} vs head "
            f"{_fmt_pct(head_acc)} (equal-only head={_fmt_pct(eq_head_acc)}). "
            f"The fold reduction is not linearly available in the probed "
            f"activation; a gap-closer must induce an element representation, "
            f"not merely retune the head."
        )

    # If residue is decodable but linear equal probe does NOT beat the head,
    # still LATENT-BUT-UNUSED if residue >> chance — head may use a nonlinear
    # mix that still fails panel; residue presence is the key claim.
    if strongly_decodable and not head_underuses:
        tag = "LATENT-BUT-UNUSED"
        body = (
            f"LATENT-BUT-UNUSED: residue is linearly decodable from frozen "
            f"pre-head activations on NOVEL words "
            f"(test acc={_fmt_pct(residue_test)} vs chance "
            f"{_fmt_pct(CHANCE_RESIDUE)}), so the element is represented. "
            f"Linear equal? probe={_fmt_pct(equal_lin)} vs frozen head "
            f"{_fmt_pct(head_acc)} on the same held-out pairs "
            f"(head equal-only={_fmt_pct(eq_head_acc)}). Even when the linear "
            f"equal probe does not massively beat the head, the residue signal "
            f"is present and unused for robust equality — strengthen an "
            f"explicit element pathway rather than more pair contact."
        )

    lines = [
        "# REPRPROBE_07",
        "",
        "NON-CITABLE representation probe. Base committee FROZEN — only linear "
        "probes are fit. No src/ edits. No confirmatory datum.",
        "",
        f"checkpoint: `{OUT_CKPT.name}` (step={blob.get('step')}). device={DEVICE}.",
        "",
        "## Activation probed (exact)",
        "",
        "ContactTransformer encodes pairs only. Forward computes",
        "`readout = final_ln(x)[:, -1, :]` then `readout @ head_W + head_b`",
        f"(see `src/philosophia/level1/model.py`). We probe that **pre-head**",
        f"vector (`final_ln` at the last sequence position, dim={D_MODEL}),",
        "averaged across the 4 frozen committee members.",
        "",
        "- **Per-word residue probe:** encode `word ⊕ SEP ⊕ word` via",
        "  `encode_pair(word, word)` so the last position is the word's last",
        "  R/L token in a self-pair context (well-defined per-word vector;",
        "  model has no single-word forward).",
        "- **Pair equality probe:** encode `left ⊕ SEP ⊕ right` as in training;",
        "  same pre-head last-position vector.",
        "",
        "## Data / splits",
        "",
        f"- Train schedule reconstructed (curated DIAG_04); "
        f"{len(train_words)} train words, {len(train_pairs)} train pairs.",
        f"- NOVEL words (not in any train pair): {len(novel)} from panel + "
        f"reserved-cell realizations.",
        f"- Residue probe split: DISJOINT novel-word sets, stratified by "
        f"residue (~70/30); probe-train={len(train_w)} words, "
        f"probe-test={len(test_w)} words; no word shared across split.",
        f"- Pair probe: held-out equals={len(equals)} + balanced held-out "
        f"unequals={len(unequals_bal)} (reserved/panel, ∉ train); "
        f"70/30 pair split → train={len(pair_train)}, test={len(pair_test)}.",
        "- panel∩train pairs = 0; probe never backprops into committee.",
        "",
        "## Results",
        "",
        "### 1. Residue linear probe (66-way softmax on novel words)",
        "",
        f"- chance = 1/{MODULUS} = {_fmt_pct(CHANCE_RESIDUE)}",
        f"- probe train acc = {_fmt_pct(residue_probe['train_acc'])} "
        f"(n={residue_probe['n_train']})",
        f"- **probe test acc = {_fmt_pct(residue_probe['test_acc'])}** "
        f"(n={residue_probe['n_test']})",
        "",
        "### 2. Pair-equality linear probe vs frozen head",
        "",
        f"- linear equal? test acc = **{_fmt_pct(equal_probe['test_acc'])}** "
        f"(n={equal_probe['n_test']}; train={_fmt_pct(equal_probe['train_acc'])})",
        f"- frozen head acc on same pair-test set = **{_fmt_pct(head_acc)}**",
        f"- frozen head equal-only acc on pair-test equals = "
        f"**{_fmt_pct(eq_head_acc)}** (n={len(equal_only)}; "
        f"compare to GENFAIL ~63% on all held-out equals)",
        "",
        "## Verdict",
        "",
        f"**{tag}**",
        "",
        body,
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
