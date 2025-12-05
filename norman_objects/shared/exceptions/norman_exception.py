from datetime import datetime, timezone
from typing import Optional


class NormanException(Exception):
    def __init__(
        self,
        message: str,
        cause: Optional[str] = None,
    ):
        super().__init__(message)
        self.message = message
        self.cause = cause
        self.timestamp = datetime.now(timezone.utc)
