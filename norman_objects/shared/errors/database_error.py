from norman_objects.shared.errors.infrastructure_error import InfrastructureError


class DatabaseError(InfrastructureError):
    """Error for database operation failures (RDS, connection issues, query errors)"""
