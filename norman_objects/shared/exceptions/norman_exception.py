from datetime import datetime, timezone
from typing import Optional, Any


class NormanException(Exception):
    _norman_exception = True

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
        from norman_objects.shared.exceptions.api_exceptions.server_exception import ServerException

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
            if hasattr(data, "_norman_exception"):
                if data._norman_exception:
                    return data

            has_dict_args = False
            if data.args:
                if isinstance(data.args[0], dict):
                    has_dict_args = True
                    exception_dict = data.args[0]

            if not has_dict_args:
                cause = None
                if data.__cause__:
                    cause = str(data.__cause__)

                return ServerException(
                    message=str(data),
                    cause=cause
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
