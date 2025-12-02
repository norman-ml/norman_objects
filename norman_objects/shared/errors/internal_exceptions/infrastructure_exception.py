from norman_objects.shared.errors.internal_exceptions.norman_internal_exception import NormanInternalException


class InfrastructureException(NormanInternalException):
    """Base class for infrastructure-related errors (AWS services, network, etc.)"""
