from norman_objects.shared.errors.internal_exceptions.infrastructure_exception import InfrastructureException


class DatabaseException(InfrastructureException):
    """Error for database operation failures (RDS, connection issues, query errors)"""
