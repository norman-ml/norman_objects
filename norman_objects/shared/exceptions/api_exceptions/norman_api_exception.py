from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class NormanApiException(NormanException):

    def __init__(
        self,
        message: str,
        status_code: int,
        error_type: str,
        suggestions: list[str],
        cause: Optional[str] = None,
    ):

        super().__init__(
            message=message,
            cause=cause,
        )

        self.status_code = status_code
        self.error_type = error_type
        self.suggestions = suggestions
        self.cause = cause

    def to_dict(self):
        return {
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
            "status_code": self.status_code,
            "error_type": self.error_type,
            "suggestions": self.suggestions,
            "cause": self.cause
        }
