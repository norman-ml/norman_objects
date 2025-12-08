from datetime import datetime, timezone
from typing import Optional, Any


class NormanException(Exception):
    _norman_exception = True
    status_code = 500
    error_type = "server"
    suggestions = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check the service status page"
    ]

    def __init__(
        self,
        message: str,
        cause: Optional[str] = None,
        suggestions: Optional[list[str]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.timestamp = datetime.now(timezone.utc)
        self.cause = cause
        self.suggestions = suggestions

    def to_dict(self):
        from norman_objects.shared.exceptions.server_exception import ServerException

        status_code = getattr(self, 'status_code', None)
        if status_code is None:
            status_code = ServerException.status_code

        error_type = getattr(self, 'error_type', None)
        if error_type is None:
            error_type = ServerException.error_type

        suggestions = getattr(self, 'suggestions', None)
        if suggestions is None:
            suggestions = ServerException.suggestions

        return {
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
            "status_code": status_code,
            "error_type": error_type,
            "suggestions": suggestions,
            "cause": self.cause
        }

    @staticmethod
    def to_norman_exception(data: Any):
        if isinstance(data, NormanException):
            return data

        if isinstance(data, Exception):
            if hasattr(data, "_norman_exception"):
                if data._norman_exception:
                    return data

            has_args = bool(data.args)
            if has_args:
                first_arg = data.args[0]
                is_dict = isinstance(first_arg, dict)
                if is_dict:
                    exception_dict = first_arg
                    exception = NormanException(
                        message=exception_dict.get("message", "An error occurred"),
                        cause=exception_dict.get("cause"),
                        suggestions=exception_dict.get("suggestions", NormanException.suggestions)
                    )
                    exception.status_code = exception_dict.get("status_code", NormanException.status_code)
                    exception.error_type = exception_dict.get("error_type", NormanException.error_type)
                    return exception

        message = str(data)
        exception = NormanException(
            message=message,
            cause=message,
            suggestions=NormanException.suggestions
        )
        return exception
