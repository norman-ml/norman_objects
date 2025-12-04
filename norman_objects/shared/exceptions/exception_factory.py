from typing import Type, Optional, Any

from norman_objects.shared.exceptions.internal_exceptions.cloud_service_exception import CloudServiceException
from norman_objects.shared.exceptions.internal_exceptions.configuration_exception import ConfigurationException
from norman_objects.shared.exceptions.internal_exceptions.database_exception import DatabaseException
from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException
from norman_objects.shared.exceptions.internal_exceptions.norman_internal_exception import NormanInternalException


class ExceptionFactory:
    _ExceptionClassesByName: dict[str, Type[NormanInternalException]] = {
        "CloudServiceException": CloudServiceException,
        "ConfigurationException": ConfigurationException,
        "DatabaseException": DatabaseException,
        "InfrastructureException": InfrastructureException
    }

    @staticmethod
    def create_internal_exception(
        exception: Exception,
        fallback_message: Optional[str] = None
    ):
        if exception.args is None:
            exception_data = None
        else:
            exception_data = exception.args[0]  # (link_to_docs) explain that args[0] is always present

        is_structured_exception = ExceptionFactory._is_structured_exception(exception_data)
        if is_structured_exception:
            exception_class_name = exception_data.get("exception_class_name", "InfrastructureException")
            internal_exception_class = ExceptionFactory._ExceptionClassesByName.get(
                exception_class_name,
                InfrastructureException
            )

            message = exception_data.get("message", str(exception))
            original_exception = exception_data.get("original_exception")

            if original_exception is None:
                original_exception = exception.__cause__

        else:
            internal_exception_class = InfrastructureException
            message = fallback_message
            if message is None:
                message = str(exception)

            original_exception = exception

        return internal_exception_class(
            message=message,
            original_exception=original_exception
        )

    # TODO: add link and more accurate explanations
    @staticmethod
    def _is_structured_exception(exception_data: Any):
        if not isinstance(exception_data, dict):
            return False

        return "error_class" in exception_data
