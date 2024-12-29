from pydantic import BaseModel

from norman_objects.inputs.input_source import InputSource


class InvocationInput(BaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    signature_id: str
    invocation_id: str = "0"
    input_source: InputSource
    url: str = ""
