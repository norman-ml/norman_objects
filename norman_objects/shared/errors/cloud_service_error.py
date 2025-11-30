from norman_objects.shared.errors.infrastructure_error import InfrastructureError


class CloudServiceError(InfrastructureError):
    """Error for AWS cloud service failures (S3, RDS, SQS, etc.)"""
