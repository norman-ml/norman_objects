from norman_objects.shared.errors.internal_exceptions.infrastructure_exception import InfrastructureException


class ConfigurationException(InfrastructureException):
    """Error for configuration and parameter retrieval failures (AppConfig, Secrets Manager)"""
