from norman_objects.shared.errors.infrastructure_error import InfrastructureError


class ConfigurationError(InfrastructureError):
    """Error for configuration and parameter retrieval failures (AppConfig, Secrets Manager)"""
