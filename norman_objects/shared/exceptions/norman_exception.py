from datetime import datetime, timezone
from typing import Optional, Any


class NormanException(Exception):
    _norman_exception = True

    def __init__(
        self,
        message: str,
        status_code: int,
        error_type: str,
        suggestions: list[str],
        cause: Optional[str] = None,
    ):
        super().__init__(message)
        self.message = message
        self.timestamp = datetime.now(timezone.utc)
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

    @classmethod
    def from_dict(cls, data: Any):
        from norman_objects.shared.exceptions.api_exceptions.server_exception import ServerException
        from norman_objects.shared.exceptions.internal_exceptions.cloud_service_exception import CloudServiceException
        from norman_objects.shared.exceptions.internal_exceptions.database_exception import DatabaseException
        from norman_objects.shared.exceptions.internal_exceptions.configuration_exception import ConfigurationException
        from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException

        if isinstance(data, NormanException):
            return data

        if isinstance(data, Exception):
            if hasattr(data, "_norman_exception") and data._norman_exception:
                return data

            if data.args and isinstance(data.args[0], dict):
                exception_dict = data.args[0]
            else:
                return ServerException(
                    message=str(data),
                    cause=str(data.__cause__) if data.__cause__ else None
                )

        elif isinstance(data, dict):
            exception_dict = data

        else:
            return ServerException(message=str(data))

        exception_class_name = exception_dict.get("exception_class_name")

        _exception_map = {
            "CloudServiceException": CloudServiceException,
            "DatabaseException": DatabaseException,
            "ConfigurationException": ConfigurationException,
            "InfrastructureException": InfrastructureException,
        }

        exception_class = _exception_map.get(exception_class_name, ServerException)

        original_exception = exception_dict.get("original_exception")
        cause = exception_dict.get("message", "An error occurred")
        if original_exception:
            cause = str(original_exception)

        return exception_class(
            message=exception_dict.get("message", "An error occurred"),
            cause=cause
        )
