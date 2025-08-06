from typing import Any

from norman_objects.messages.asset_message import AssetMessage
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.input_message import InputMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.messages.norman_base_message import NormanBaseMessage
from norman_objects.messages.output_message import OutputMessage
from norman_objects.status_flags.status_flag import StatusFlag


class NormanMessageFactory:
    @staticmethod
    def parse_obj(raw_message: Any):
        if raw_message is None:
            raise ValueError("Cannot convert a None value to a Pydantic base message")

        if not isinstance(raw_message, dict):
            raise ValueError("Cannot convert a non-dict value to a Pydantic base message")

        if "entity_type" not in raw_message:
            raise ValueError("Cannot serialize Norman base message without an entity type field")

        if "status_flag" not in raw_message:
            raise ValueError("Cannot serialize Norman base message without an status flag field")

        try:
            entity_name = raw_message["entity_type"]
            entity_type = EntityType(entity_name)
        except Exception as e:
            raise ValueError("entity type is not a valid enum literal for the EntityType enum")

        try:
            status_flag_json = raw_message["status_flag"]
            status_flag = StatusFlag.parse_obj(status_flag_json)
        except Exception as e:
            raise ValueError("status flag is not a valid json representation of the StatusFlag class")

        # In Pydantic V2 there are more elegant solutions that do not require manually maintaining this if case
        # Once we upgrade the library we can probably omit this in favour of these solutions.
        if entity_type == EntityType.Model:
            return ModelMessage.parse_obj(raw_message)
        elif entity_type == EntityType.Asset:
            return AssetMessage.parse_obj(raw_message)
        elif entity_type == EntityType.Invocation:
            return InvocationMessage.parse_obj(raw_message)
        elif entity_type == EntityType.Input:
            return InputMessage.parse_obj(raw_message)
        elif entity_type == EntityType.Output:
            return OutputMessage.parse_obj(raw_message)
        else:
            return NormanBaseMessage.parse_obj(raw_message)
