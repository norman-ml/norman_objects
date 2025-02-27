from datetime import datetime, timedelta, timezone
from typing import List
from pydantic import Field

from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.outputs.invocation_output import InvocationOutput
from norman_objects.norman_base_model.norman_bose_model import NormanBaseModel


class Invocation(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

    inputs: List[InvocationInput] = []
    outputs: List[InvocationOutput] = []
