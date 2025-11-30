from norman_objects.shared.errors.infrastructure_error import InfrastructureError
from pydantic import ConfigDict


class CloudServiceError(InfrastructureError):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    pass
