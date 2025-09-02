from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.models.model import Model
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.sensitive.sensitive import Sensitive


class InvocationParams(NormanBaseModel):
    access_token: Sensitive[str]
    model: Model
    invocation: Invocation
