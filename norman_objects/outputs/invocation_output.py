from pydantic import BaseModel


class InvocationOutput(BaseModel):
    id: str = "0"
    model_id: str
    parameter_id: str
    invocation_id: str = "0"
