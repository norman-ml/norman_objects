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

    @staticmethod
    def to_internal_error(
        exception: Exception,
        fallback_message: Optional[str] = None,
        fallback_context: Optional[dict] = None
    ) -> NormanInternalException:

        if ErrorFactory._is_structured_exception(exception):
            error_data = exception.args[0]
            error_class_name = error_data.get("error_class", "InfrastructureException")
            internal_error_class = ErrorFactory._INTERNAL_ERROR_MAP.get(
                error_class_name,
                InfrastructureException
            )

            return internal_error_class(
                message=error_data.get("message", str(exception)),
                context=error_data.get("context", {}),
                original_exception=error_data.get("original_exception") or exception.__cause__
            )
        else:
            return InfrastructureException(
                message=fallback_message or str(exception),
                context=fallback_context or {},
                original_exception=exception
            )

    @staticmethod
    def to_api_error(
        exception: Exception,
        default_message: str,
        api_error_class: Type[NormanApiError] = None,
        fallback_context: Optional[dict] = None
    ) -> NormanApiError:

        if isinstance(exception, NormanInternalException):
            context = exception.context
        else:
            internal_error = ErrorFactory.to_internal_error(
                exception,
                fallback_message=default_message,
                fallback_context=fallback_context
            )
            context = internal_error.context

        api_error_type = api_error_class or ServerError

        return api_error_type(
            message=default_message,
            context=context
        )

    @staticmethod
    def _is_structured_exception(exception: Exception) -> bool:
        exception_dict = exception.args[0] if exception.args else None
        return isinstance(exception_dict, dict) and "error_class" in exception_dict
