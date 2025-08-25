from norman_objects.invocations.invocation import Invocation
from norman_objects.models.model import Model
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive import Sensitive


class InvocationParams(NormanBaseModel):
    access_token: Sensitive[str]
    model: Model
    invocation: Invocation
