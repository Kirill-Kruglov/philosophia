from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
import re
from typing import Mapping


NANOSECONDS_PER_SECOND = 1_000_000_000
NANOSECONDS_PER_HOUR = 3600 * NANOSECONDS_PER_SECOND
_HEX64 = re.compile(r"[0-9a-f]{64}")


def parse_utc(value: str) -> datetime:
    if not value.endswith("Z"):
        raise ValueError("timestamp must use UTC Z form")
    parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    if parsed.tzinfo != timezone.utc:
        raise ValueError("timestamp must be UTC")
    return parsed


@dataclass(frozen=True)
class TEnvelope:
    device_hour_cap: int = 168
    candidate_cap: int = 12
    review_wall_hours: int = 48
    review_device_hours: int = 40

    def __post_init__(self) -> None:
        if min(
            self.device_hour_cap,
            self.candidate_cap,
            self.review_wall_hours,
            self.review_device_hours,
        ) <= 0:
            raise ValueError("T envelope values must be positive")


@dataclass(frozen=True)
class TState:
    activated_utc: str | None = None
    device_nanoseconds: int = 0
    candidate_ids: tuple[str, ...] = ()
    last_review_utc: str | None = None
    device_nanoseconds_at_review: int = 0
    author_stopped: bool = False

    def __post_init__(self) -> None:
        if self.device_nanoseconds < 0 or self.device_nanoseconds_at_review < 0:
            raise ValueError("T accounting cannot be negative")
        if self.device_nanoseconds_at_review > self.device_nanoseconds:
            raise ValueError("review counter exceeds total device time")
        if len(set(self.candidate_ids)) != len(self.candidate_ids):
            raise ValueError("candidate registrations must be unique")
        if self.activated_utc is None:
            if self.last_review_utc is not None or self.device_nanoseconds != 0:
                raise ValueError("inactive T cannot contain active accounting")
        else:
            parse_utc(self.activated_utc)
            if self.last_review_utc is not None:
                parse_utc(self.last_review_utc)

    def activate(self, timestamp_utc: str) -> "TState":
        if self.activated_utc is not None:
            raise ValueError("T is already activated")
        parse_utc(timestamp_utc)
        return replace(self, activated_utc=timestamp_utc)

    def charge_device_nanoseconds(self, value: int, envelope: TEnvelope) -> "TState":
        if self.activated_utc is None or self.author_stopped:
            raise ValueError("T is not available for charging")
        if self.exhausted(envelope):
            raise ValueError("T envelope is already exhausted")
        if value <= 0:
            raise ValueError("device charge must be positive")
        return replace(self, device_nanoseconds=self.device_nanoseconds + value)

    def register_candidate(self, candidate_id: str, envelope: TEnvelope) -> "TState":
        if self.activated_utc is None or self.author_stopped:
            raise ValueError("T is not available for registration")
        if _HEX64.fullmatch(candidate_id) is None:
            raise ValueError("candidate id must be lowercase SHA-256")
        if candidate_id in self.candidate_ids:
            return self
        if self.exhausted(envelope):
            raise ValueError("T envelope is already exhausted")
        return replace(self, candidate_ids=(*self.candidate_ids, candidate_id))

    def exhausted(self, envelope: TEnvelope) -> bool:
        return (
            self.device_nanoseconds >= envelope.device_hour_cap * NANOSECONDS_PER_HOUR
            or len(self.candidate_ids) >= envelope.candidate_cap
        )

    def review_due(self, envelope: TEnvelope, timestamp_utc: str) -> bool:
        if self.activated_utc is None:
            return False
        now = parse_utc(timestamp_utc)
        origin = parse_utc(self.last_review_utc or self.activated_utc)
        if now < origin:
            raise ValueError("T review time cannot move backwards")
        wall_due = (now - origin).total_seconds() >= envelope.review_wall_hours * 3600
        device_due = (
            self.device_nanoseconds - self.device_nanoseconds_at_review
            >= envelope.review_device_hours * NANOSECONDS_PER_HOUR
        )
        return wall_due or device_due

    def complete_review(self, envelope: TEnvelope, timestamp_utc: str) -> "TState":
        if not self.review_due(envelope, timestamp_utc):
            raise ValueError("early review cannot reset E3 clocks")
        return replace(
            self,
            last_review_utc=timestamp_utc,
            device_nanoseconds_at_review=self.device_nanoseconds,
        )

    def record_author_stop(self, timestamp_utc: str) -> "TState":
        if self.last_review_utc != timestamp_utc:
            raise ValueError("author stop must be signed at a completed review")
        return replace(self, author_stopped=True)

    def to_mapping(self) -> dict[str, object]:
        return {
            "activated_utc": self.activated_utc,
            "author_stopped": self.author_stopped,
            "candidate_ids": list(self.candidate_ids),
            "device_nanoseconds": self.device_nanoseconds,
            "device_nanoseconds_at_review": self.device_nanoseconds_at_review,
            "last_review_utc": self.last_review_utc,
            "schema": "philosophia.officina.t-state.v1",
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> "TState":
        if value.get("schema") != "philosophia.officina.t-state.v1":
            raise ValueError("T state schema mismatch")
        candidates = value.get("candidate_ids")
        if not isinstance(candidates, list) or not all(
            isinstance(item, str) for item in candidates
        ):
            raise ValueError("T candidate ids must be strings")
        return cls(
            activated_utc=value.get("activated_utc"),  # type: ignore[arg-type]
            device_nanoseconds=int(value.get("device_nanoseconds", -1)),
            candidate_ids=tuple(candidates),
            last_review_utc=value.get("last_review_utc"),  # type: ignore[arg-type]
            device_nanoseconds_at_review=int(
                value.get("device_nanoseconds_at_review", -1)
            ),
            author_stopped=bool(value.get("author_stopped")),
        )
