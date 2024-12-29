from pydantic import BaseModel


class InvocationOutput(BaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    signature_id: str
    invocation_id: str = "0"
