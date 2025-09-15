from datetime import datetime, timedelta, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.invocations.invocation_signature import InvocationSignature


class Invocation(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

    inputs: list[InvocationSignature] = []
    outputs: list[InvocationSignature] = []
