from datetime import datetime, timedelta, timezone
from typing import List

from pydantic import BaseModel, Field

from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.outputs.invocation_output import InvocationOutput


class Invocation(BaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

    inputs: List[InvocationInput] = []
    outputs: List[InvocationOutput] = []
