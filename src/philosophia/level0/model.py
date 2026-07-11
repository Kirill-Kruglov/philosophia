from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math

import torch
from torch import nn

from .config import ModelConfig


@dataclass(frozen=True)
class InitScale:
    name: str
    shape: tuple[int, ...]
    xavier_bound: float
    realized_std: float
    minimum: float
    maximum: float
    sha256: str


def _hash_tensor(tensor: torch.Tensor) -> str:
    value = tensor.detach().cpu().contiguous()
    digest = hashlib.sha256()
    digest.update(str(value.dtype).encode("ascii"))
    digest.update(str(tuple(value.shape)).encode("ascii"))
    digest.update(value.numpy().tobytes())
    return digest.hexdigest()


def _scale_record(name: str, tensor: torch.Tensor) -> InitScale:
    if tensor.ndim != 2:
        raise ValueError("Xavier scale records require a matrix")
    fan_out, fan_in = tensor.shape
    bound = math.sqrt(6.0 / float(fan_in + fan_out))
    value = tensor.detach()
    return InitScale(
        name=name,
        shape=tuple(value.shape),
        xavier_bound=bound,
        realized_std=float(value.std(unbiased=False)),
        minimum=float(value.min()),
        maximum=float(value.max()),
        sha256=_hash_tensor(value),
    )


class GrokkingTransformer(nn.Module):
    def __init__(self, config: ModelConfig, *, init_seed: int) -> None:
        super().__init__()
        self.config = config
        d_model = config.residual_width
        heads = config.heads
        d_head = config.head_width

        self.W_E = nn.Parameter(torch.empty(config.vocabulary_size, d_model))
        self.W_pos = nn.Parameter(torch.empty(config.sequence_length, d_model))
        self.W_Q = nn.Parameter(torch.empty(heads, d_head, d_model))
        self.W_K = nn.Parameter(torch.empty(heads, d_head, d_model))
        self.W_V = nn.Parameter(torch.empty(heads, d_head, d_model))
        self.W_O = nn.Parameter(torch.empty(heads, d_head, d_model))
        self.W_in = nn.Parameter(torch.empty(config.mlp_width, d_model))
        self.b_in = nn.Parameter(torch.zeros(config.mlp_width))
        self.W_out = nn.Parameter(torch.empty(d_model, config.mlp_width))
        self.b_out = nn.Parameter(torch.zeros(d_model))
        self.W_U = nn.Parameter(torch.empty(d_model, config.vocabulary_size))

        self._reset_parameters(init_seed)
        self._initial_scales = self._capture_init_scales()

    def _reset_parameters(self, init_seed: int) -> None:
        with torch.random.fork_rng(devices=[]):
            torch.manual_seed(init_seed)
            for matrix in (self.W_E, self.W_pos, self.W_in, self.W_out, self.W_U):
                nn.init.xavier_uniform_(matrix, gain=1.0)
            for tensor in (self.W_Q, self.W_K, self.W_V, self.W_O):
                for head in tensor:
                    nn.init.xavier_uniform_(head, gain=1.0)
            nn.init.zeros_(self.b_in)
            nn.init.zeros_(self.b_out)

    def _capture_init_scales(self) -> tuple[InitScale, ...]:
        records = [
            _scale_record("W_E", self.W_E),
            _scale_record("W_pos", self.W_pos),
            _scale_record("W_in", self.W_in),
            _scale_record("W_out", self.W_out),
            _scale_record("W_U", self.W_U),
        ]
        for name in ("W_Q", "W_K", "W_V", "W_O"):
            tensor = getattr(self, name)
            records.extend(
                _scale_record(f"{name}.{head_index}", head)
                for head_index, head in enumerate(tensor)
            )
        return tuple(records)

    def init_scale_observables(self) -> tuple[InitScale, ...]:
        return self._initial_scales

    def _embed(self, tokens: torch.Tensor) -> torch.Tensor:
        if tokens.ndim != 2 or tokens.shape[1] != self.config.sequence_length:
            raise ValueError("tokens must have shape [batch, 3]")
        return self.W_E[tokens] + self.W_pos.unsqueeze(0)

    def _attention(
        self,
        residual: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        query = torch.einsum("bpd,hkd->bhpk", residual, self.W_Q)
        key = torch.einsum("bpd,hkd->bhpk", residual, self.W_K)
        value = torch.einsum("bpd,hkd->bhpk", residual, self.W_V)
        scores = torch.einsum("bhqk,bhpk->bhqp", query, key)
        scores = scores / math.sqrt(self.config.head_width)
        causal_mask = torch.triu(
            torch.ones(
                self.config.sequence_length,
                self.config.sequence_length,
                dtype=torch.bool,
                device=residual.device,
            ),
            diagonal=1,
        )
        scores = scores.masked_fill(
            causal_mask.unsqueeze(0).unsqueeze(0),
            torch.finfo(scores.dtype).min,
        )
        weights = scores.softmax(dim=-1)
        attended = torch.einsum("bhqp,bhpk->bhqk", weights, value)
        output = torch.einsum("bhpk,hkd->bpd", attended, self.W_O)
        return output, weights

    def attention_weights(self, tokens: torch.Tensor) -> torch.Tensor:
        _, weights = self._attention(self._embed(tokens))
        return weights

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        residual = self._embed(tokens)
        attention_out, _ = self._attention(residual)
        residual = residual + attention_out

        hidden = torch.relu(torch.einsum("bpd,md->bpm", residual, self.W_in) + self.b_in)
        mlp_out = torch.einsum("bpm,dm->bpd", hidden, self.W_out) + self.b_out
        residual = residual + mlp_out
        return torch.einsum("bpd,dv->bpv", residual, self.W_U)
