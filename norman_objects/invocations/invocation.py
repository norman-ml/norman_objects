from typing import List

from pydantic import BaseModel

from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.outputs.invocation_output import InvocationOutput


class Invocation(BaseModel):
    id: str = "0"
    model_id: str

    inputs: List[InvocationInput] = []
    outputs: List[InvocationOutput] = []
