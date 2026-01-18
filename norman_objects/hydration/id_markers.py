from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GeneratedId:
    context_key: Optional[str] = None


@dataclass(frozen=True)
class DerivedId:
    source: str
