from norman_objects.shared.errors.internal_exceptions.infrastructure_exception import InfrastructureException


class CloudServiceException(InfrastructureException):
    """Error for AWS cloud service failures (S3, RDS, SQS, etc.)"""
