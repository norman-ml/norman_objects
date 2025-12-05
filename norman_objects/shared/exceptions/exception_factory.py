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
        message: str
    ):
        if exception.args is None:
            exception_data = None
        else:
            # TODO: add link and more accurate explanations
            exception_data = exception.args[0]  # (link_to_docs) explain that args[0] is always present

        is_structured_exception = ExceptionFactory._is_structured_exception(exception_data)
        if is_structured_exception:
            exception_class_name = exception_data.get("exception_class_name", "InfrastructureException")
            internal_exception_class = ExceptionFactory._ExceptionClassesByName.get(
                exception_class_name,
                InfrastructureException
            )

            original_exception = exception_data.get("original_exception")
            cause = exception_data.get("message", str(exception))

            if original_exception is None:
                original_exception = exception.__cause__

        else:
            internal_exception_class = InfrastructureException

            original_exception = exception
            cause = str(original_exception)

        return internal_exception_class(
            message=message,
            original_exception=original_exception,
            cause=cause
        )

    @staticmethod
    def _is_structured_exception(exception_data: Any):
        if not isinstance(exception_data, dict):
            return False

        return "exception_class_name" in exception_data
