from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
import platform
from typing import Sequence

import torch
from torch import Tensor, nn

from .config import COMMITTEE_SIZE, MODEL_INPUT_LENGTH
from .serialization import DeterministicKey, prf_digest


PINNED_TORCH_BUILD = "2.9.1+cpu"
PINNED_CPYTHON = (3, 12, 3)
DTYPE = torch.float32
VOCAB_SIZE = 4
D_MODEL = 128
HEADS = 4
HEAD_WIDTH = 32
MLP_WIDTH = 512
LAYERS = 2
LN_EPS = 1e-5


def configure_canonical_runtime() -> None:
    if torch.__version__ != PINNED_TORCH_BUILD:
        raise RuntimeError(f"torch build must be {PINNED_TORCH_BUILD}")
    if tuple(map(int, platform.python_version_tuple())) != PINNED_CPYTHON:
        raise RuntimeError("CPython build must be 3.12.3")
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(1)
    try:
        torch.set_num_interop_threads(1)
    except RuntimeError as error:
        if torch.get_num_interop_threads() != 1:
            raise RuntimeError("cannot establish one interop thread") from error
    if torch.get_num_threads() != 1 or torch.get_num_interop_threads() != 1:
        raise RuntimeError("canonical single-thread runtime is not active")


def _seed_for_tensor(
    key: DeterministicKey,
    *,
    block: int,
    replicate: int,
    member: int,
    tensor_name: str,
) -> int:
    digest = prf_digest(
        key,
        ("L1", "learner", "init", block, replicate, member, tensor_name),
        0,
    )
    return int.from_bytes(digest[:8], "big", signed=False)


def _normal_parameter(
    shape: tuple[int, ...],
    fan_in: int,
    key: DeterministicKey,
    *,
    block: int,
    replicate: int,
    member: int,
    tensor_name: str,
) -> nn.Parameter:
    generator = torch.Generator(device="cpu")
    generator.manual_seed(
        _seed_for_tensor(
            key,
            block=block,
            replicate=replicate,
            member=member,
            tensor_name=tensor_name,
        )
    )
    value = torch.randn(shape, generator=generator, dtype=DTYPE) / math.sqrt(fan_in)
    return nn.Parameter(value)


class AttentionBlock(nn.Module):
    def __init__(
        self,
        key: DeterministicKey,
        *,
        block: int,
        replicate: int,
        member: int,
        layer: int,
    ) -> None:
        super().__init__()
        prefix = f"layer{layer}"
        common = dict(key=key, block=block, replicate=replicate, member=member)
        self.ln1 = nn.LayerNorm(D_MODEL, eps=LN_EPS, dtype=DTYPE)
        self.W_Q = _normal_parameter((D_MODEL, D_MODEL), D_MODEL, tensor_name=f"{prefix}.W_Q", **common)
        self.W_K = _normal_parameter((D_MODEL, D_MODEL), D_MODEL, tensor_name=f"{prefix}.W_K", **common)
        self.W_V = _normal_parameter((D_MODEL, D_MODEL), D_MODEL, tensor_name=f"{prefix}.W_V", **common)
        self.W_O = _normal_parameter((D_MODEL, D_MODEL), D_MODEL, tensor_name=f"{prefix}.W_O", **common)
        self.ln2 = nn.LayerNorm(D_MODEL, eps=LN_EPS, dtype=DTYPE)
        self.W_in = _normal_parameter((D_MODEL, MLP_WIDTH), D_MODEL, tensor_name=f"{prefix}.W_in", **common)
        self.b_in = nn.Parameter(torch.zeros(MLP_WIDTH, dtype=DTYPE))
        self.W_out = _normal_parameter((MLP_WIDTH, D_MODEL), MLP_WIDTH, tensor_name=f"{prefix}.W_out", **common)
        self.b_out = nn.Parameter(torch.zeros(D_MODEL, dtype=DTYPE))

    def forward(self, x: Tensor, key_mask: Tensor) -> Tensor:
        normalized = self.ln1(x)
        batch, sequence, _ = normalized.shape
        q = (normalized @ self.W_Q).view(batch, sequence, HEADS, HEAD_WIDTH).transpose(1, 2)
        k = (normalized @ self.W_K).view(batch, sequence, HEADS, HEAD_WIDTH).transpose(1, 2)
        v = (normalized @ self.W_V).view(batch, sequence, HEADS, HEAD_WIDTH).transpose(1, 2)
        scores = (q @ k.transpose(-2, -1)) / math.sqrt(HEAD_WIDTH)
        scores = scores.masked_fill(~key_mask[:, None, None, :], float("-inf"))
        attention = torch.softmax(scores, dim=-1)
        attended = (attention @ v).transpose(1, 2).contiguous().view(batch, sequence, D_MODEL)
        x = x + attended @ self.W_O
        normalized = self.ln2(x)
        x = x + torch.relu(normalized @ self.W_in + self.b_in) @ self.W_out + self.b_out
        return x


class ContactTransformer(nn.Module):
    def __init__(
        self,
        key: DeterministicKey,
        *,
        block: int,
        replicate: int,
        member: int,
    ) -> None:
        super().__init__()
        if replicate not in (1, 2):
            raise ValueError("replicate must be 1 or 2")
        if member not in range(COMMITTEE_SIZE):
            raise ValueError("member must be in 0..3")
        common = dict(key=key, block=block, replicate=replicate, member=member)
        self.token_embedding = _normal_parameter(
            (VOCAB_SIZE, D_MODEL), D_MODEL, tensor_name="token_embedding", **common
        )
        self.position_embedding = _normal_parameter(
            (MODEL_INPUT_LENGTH, D_MODEL), D_MODEL, tensor_name="position_embedding", **common
        )
        self.layers = nn.ModuleList(
            AttentionBlock(key, block=block, replicate=replicate, member=member, layer=layer)
            for layer in (1, 2)
        )
        self.final_ln = nn.LayerNorm(D_MODEL, eps=LN_EPS, dtype=DTYPE)
        self.head_W = _normal_parameter(
            (D_MODEL, 2), D_MODEL, tensor_name="head_W", **common
        )
        self.head_b = nn.Parameter(torch.zeros(2, dtype=DTYPE))

    def forward(self, tokens: Tensor) -> Tensor:
        if tokens.dtype != torch.long:
            raise ValueError("tokens must be torch.long")
        if tokens.ndim != 2 or tokens.shape[1] != MODEL_INPUT_LENGTH:
            raise ValueError(f"tokens must have shape (batch, {MODEL_INPUT_LENGTH})")
        if tokens.device.type != "cpu":
            raise ValueError("Level 1 model is CPU-only")
        key_mask = tokens.ne(0)
        if not bool(key_mask.any(dim=1).all()):
            raise ValueError("every sequence must contain a non-PAD token")
        positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
        x = self.token_embedding[tokens] + self.position_embedding[positions][None, :, :]
        for layer in self.layers:
            x = layer(x, key_mask)
        readout = self.final_ln(x)[:, -1, :]
        return readout @ self.head_W + self.head_b

    def equal_probability(self, tokens: Tensor) -> Tensor:
        return torch.softmax(self(tokens), dim=-1)[:, 1]


def committee_equal_probability(
    models: Sequence[ContactTransformer], tokens: Tensor
) -> Tensor:
    if len(models) != COMMITTEE_SIZE:
        raise ValueError(f"committee must contain exactly {COMMITTEE_SIZE} members")
    with torch.no_grad():
        probabilities = tuple(model.equal_probability(tokens) for model in models)
    shapes = {tuple(value.shape) for value in probabilities}
    if len(shapes) != 1:
        raise ValueError("committee members returned incompatible probability shapes")
    return torch.stack(probabilities, dim=0).mean(dim=0)


def encode_pair(left: bytes, right: bytes) -> Tensor:
    token_map = {0x52: 1, 0x4C: 2}
    try:
        content = [token_map[token] for token in left] + [3] + [token_map[token] for token in right]
    except KeyError as error:
        raise ValueError("pair contains a non R/L token") from error
    if len(content) > MODEL_INPUT_LENGTH:
        raise ValueError("pair exceeds frozen model input")
    return torch.tensor([0] * (MODEL_INPUT_LENGTH - len(content)) + content, dtype=torch.long)


def build_optimizer(model: ContactTransformer) -> torch.optim.AdamW:
    decayed: list[nn.Parameter] = []
    for layer in model.layers:
        decayed.extend((layer.W_Q, layer.W_K, layer.W_V, layer.W_O, layer.W_in, layer.W_out))
    decayed.append(model.head_W)

    non_decayed: list[nn.Parameter] = [model.token_embedding, model.position_embedding]
    for layer in model.layers:
        non_decayed.extend(
            (
                layer.ln1.weight,
                layer.ln1.bias,
                layer.ln2.weight,
                layer.ln2.bias,
            )
        )
    non_decayed.extend((model.final_ln.weight, model.final_ln.bias))
    for layer in model.layers:
        non_decayed.extend((layer.b_in, layer.b_out))
    non_decayed.append(model.head_b)

    if {id(parameter) for parameter in decayed} & {id(parameter) for parameter in non_decayed}:
        raise RuntimeError("optimizer parameter groups overlap")
    if {id(parameter) for parameter in model.parameters()} != {
        id(parameter) for parameter in decayed + non_decayed
    }:
        raise RuntimeError("optimizer groups do not cover the model exactly")

    return torch.optim.AdamW(
        [
            {"params": decayed, "weight_decay": 0.01},
            {"params": non_decayed, "weight_decay": 0.0},
        ],
        lr=1e-3,
        betas=(0.9, 0.98),
        eps=1e-8,
    )


def state_hash(model: nn.Module, optimizer: torch.optim.Optimizer | None = None) -> str:
    digest = hashlib.sha256()
    for name, tensor in sorted(model.state_dict().items()):
        digest.update(name.encode("utf-8"))
        digest.update(tensor.detach().cpu().contiguous().numpy().tobytes())
    if optimizer is not None:
        digest.update(repr(optimizer.state_dict()).encode("utf-8"))
    return digest.hexdigest()
