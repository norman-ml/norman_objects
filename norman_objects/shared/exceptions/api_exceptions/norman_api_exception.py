from datetime import datetime, UTC

from norman_objects.shared.exceptions.norman_exception import NormanException


class NormanApiException(NormanException):

    status_code: int = 500
    error_type: str = "api_error"
    suggestions: list[str] = ["Contact support for assistance"]

    def __init__(
        self,
        message: str,
        timestamp: datetime = None,
        suggestions: list[str] = None
    ):

        NormanException.__init__(
            self,
            message=message,
            timestamp=timestamp if timestamp is not None else datetime.now(UTC)
        )

        if suggestions is not None:
            self.suggestions = suggestions

    def to_dict(self) -> dict:
        return {
            "message": self.message,
            "status_code": self.status_code,
            "error_type": self.error_type,
            "suggestions": self.suggestions,
            "timestamp": self.timestamp.isoformat()
        }
