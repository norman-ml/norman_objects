from norman_objects.shared.exceptions.internal_exceptions.norman_internal_exception import NormanInternalException


class InfrastructureException(NormanInternalException):
    """Base class for infrastructure-related exceptions (AWS services, network, etc.)"""
