from norman_objects.inputs.input_source import InputSource
from norman_objects.norman_base_model.norman_base_model import NormanBaseModel


class InvocationInput(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    signature_id: str
    invocation_id: str = "0"
    input_source: InputSource
    url: str = ""
