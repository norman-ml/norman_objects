from norman_objects.shared.errors.norman_internal_error import NormanInternalError


class InfrastructureError(NormanInternalError):
    """Base class for infrastructure-related errors (AWS services, network, etc.)"""
