from typing import Union, Annotated

from pydantic import Field

from norman_objects.messages.asset_message import AssetMessage
from norman_objects.messages.input_message import InputMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.messages.output_message import OutputMessage

NormanMessageUnion = Annotated[
    Union[
        ModelMessage,
        AssetMessage,
        InvocationMessage,
        InputMessage,
        OutputMessage,
    ],
    Field(discriminator="entity_type"),
]
