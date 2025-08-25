from typing import Union, Annotated
from pydantic import Field, TypeAdapter

from norman_objects.messages.asset_message import AssetMessage
from norman_objects.messages.input_message import InputMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.messages.output_message import OutputMessage


NormanMessage = Annotated[
    Union[
        ModelMessage,
        AssetMessage,
        InvocationMessage,
        InputMessage,
        OutputMessage,
    ],
    Field(discriminator="entity_type"),
]


class NormanMessageFactory:
    @staticmethod
    def parse_obj(raw_message: dict) -> NormanMessage:
        if raw_message is None:
            raise ValueError("Cannot convert None to Norman message")
        if not isinstance(raw_message, dict):
            raise ValueError("Cannot convert non-dict to Norman message")

        return TypeAdapter(NormanMessage).validate_python(raw_message)
