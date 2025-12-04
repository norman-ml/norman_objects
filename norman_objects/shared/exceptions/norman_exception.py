from datetime import datetime, timezone


class NormanException(Exception):
    def __init__(
        self,
        message: str,
    ):
        super().__init__(message)
        self.message = message
        self.timestamp = datetime.now(timezone.utc)
