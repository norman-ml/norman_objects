from datetime import datetime, timedelta, timezone

from pydantic import Field

from norman_objects.shared.inputs.invocation_input import InvocationInput
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.outputs.invocation_output import InvocationOutput


class Invocation(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

    inputs: list[InvocationInput] = []
    outputs: list[InvocationOutput] = []
