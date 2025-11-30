from datetime import datetime, UTC
from typing import Optional


class NormanIntError():
    def __init__(
        self,
        message: str,
        details: dict = None,
        timestamp: datetime = None,
        original_exception: Optional[Exception] = None
    ):
        self.message = message
        self.details = details if details is not None else {}
        self.timestamp = timestamp if timestamp is not None else datetime.now(UTC)
        self.original_exception = original_exception
