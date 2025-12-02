from typing import Type, Optional, Dict

from norman_objects.shared.errors.api_errors.norman_api_error import NormanApiError
from norman_objects.shared.errors.internal_exceptions.norman_internal_exception import NormanInternalException
from norman_objects.shared.errors.internal_exceptions.cloud_service_exception import CloudServiceException
from norman_objects.shared.errors.internal_exceptions.configuration_exception import ConfigurationException
from norman_objects.shared.errors.internal_exceptions.database_exception import DatabaseException
from norman_objects.shared.errors.internal_exceptions.infrastructure_exception import InfrastructureException
from norman_objects.shared.errors.api_errors.server_error import ServerError


class ErrorFactory:

    _INTERNAL_ERROR_MAP: Dict[str, Type[NormanInternalException]] = {
        "CloudServiceException": CloudServiceException,
        "ConfigurationException": ConfigurationException,
        "DatabaseException": DatabaseException,
        "InfrastructureException": InfrastructureException
    }

    _API_ERROR_MAP: Dict[Type[NormanInternalException], Type[NormanApiError]] = {
        CloudServiceException: ServerError,
        ConfigurationException: ServerError,
        DatabaseException: ServerError,
        InfrastructureException: ServerError
    }

    @classmethod
    def to_internal_error(
        cls,
        exc: Exception,
        fallback_message: Optional[str] = None,
        fallback_details: Optional[dict] = None
    ) -> NormanInternalException:

        error_data = cls._extract_error_data(exc)

        if error_data:
            error_class_name = error_data.get("error_class", "InfrastructureException")
            internal_error_class = cls._INTERNAL_ERROR_MAP.get(
                error_class_name,
                InfrastructureException
            )

            return internal_error_class(
                message=error_data.get("message", str(exc)),
                details=error_data.get("details", {}),
                original_exception=error_data.get("original_exception") or exc.__cause__
            )
        else:
            return InfrastructureException(
                message=fallback_message or str(exc),
                details=fallback_details or {},
                original_exception=exc
            )

    @classmethod
    def to_api_error(
        cls,
        exc: Exception,
        default_message: str,
        api_error_class: Type[NormanApiError] = None,
        fallback_details: Optional[dict] = None
    ) -> NormanApiError:

        if isinstance(exc, NormanInternalException):
            details = exc.details
            api_error_type = api_error_class or cls._API_ERROR_MAP.get(
                type(exc),
                ServerError
            )
        else:
            internal_error = cls.to_internal_error(
                exc,
                fallback_message=default_message,
                fallback_details=fallback_details
            )
            details = internal_error.details

            api_error_type = api_error_class or cls._API_ERROR_MAP.get(
                type(internal_error),
                ServerError
            )

        return api_error_type(
            message=default_message,
            details=details
        )

    @classmethod
    def _extract_error_data(cls, exc: Exception) -> Optional[dict]:

        if exc.args and len(exc.args) > 0:
            first_arg = exc.args[0]
            if isinstance(first_arg, dict) and "error_class" in first_arg:
                return first_arg

        return None
