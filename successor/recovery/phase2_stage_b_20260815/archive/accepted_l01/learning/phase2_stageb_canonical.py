#!/usr/bin/env python3
"""Single Stage-A canonical JSON serializer and SHA-256 helper."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_dumps(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def canonical_bytes(obj: Any) -> bytes:
    return canonical_dumps(obj).encode('ascii')


def canonical_hash(obj: Any) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()
