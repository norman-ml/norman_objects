from typing import Type, Optional, Dict

from norman_objects.shared.exceptions.internal_exceptions.cloud_service_exception import CloudServiceException
from norman_objects.shared.exceptions.internal_exceptions.configuration_exception import ConfigurationException
from norman_objects.shared.exceptions.internal_exceptions.database_exception import DatabaseException
from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException
from norman_objects.shared.exceptions.internal_exceptions.norman_internal_exception import NormanInternalException


class ExceptionFactory:

    _INTERNAL_ERROR_MAP: Dict[str, Type[NormanInternalException]] = {
        "CloudServiceException": CloudServiceException,
        "ConfigurationException": ConfigurationException,
        "DatabaseException": DatabaseException,
        "InfrastructureException": InfrastructureException
    }

    @staticmethod
    def create_internal_exception(
        exception: Exception,
        fallback_message: Optional[str] = None,
        fallback_context: Optional[dict] = None
    ) -> NormanInternalException:

        if ExceptionFactory._is_structured_exception(exception):
            exception_data = exception.args[0]
            error_class_name = exception_data.get("exception_class", "InfrastructureException")
            internal_error_class = ExceptionFactory._INTERNAL_ERROR_MAP.get(
                error_class_name,
                InfrastructureException
            )

            return internal_error_class(
                message=exception_data.get("message", str(exception)),
                context=exception_data.get("context", {}),
                original_exception=exception_data.get("original_exception") or exception.__cause__
            )
        else:
            return InfrastructureException(
                message=fallback_message or str(exception),
                context=fallback_context or {},
                original_exception=exception
            )


    @staticmethod
    def _is_structured_exception(exception: Exception) -> bool:
        exception_dict = exception.args[0] if exception.args else None
        return isinstance(exception_dict, dict) and "error_class" in exception_dict
