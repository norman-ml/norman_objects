from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.models.model import Model
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.model_projection import ModelProjection
from norman_objects.shared.security.sensitive import Sensitive


class InvocationParams(NormanBaseModel):
    access_token: Sensitive[str]
    model: ModelProjection
    invocation: Invocation
