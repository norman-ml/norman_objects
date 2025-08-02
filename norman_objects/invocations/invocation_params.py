from norman_objects.invocations.invocation import Invocation
from norman_objects.models.model import Model
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class InvocationParams(NormanBaseModel):
    access_token: SensitiveType(str)
    model: Model
    invocation: Invocation
