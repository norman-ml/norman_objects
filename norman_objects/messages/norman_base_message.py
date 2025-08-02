from datetime import datetime, UTC
from typing import Any

from norman_objects.context.context_tokens import NormanContext
from norman_objects.messages.asset_message import AssetMessage
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.input_message import InputMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.messages.output_message import OutputMessage
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType
from norman_objects.status_flags.status_flag import StatusFlag
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class NormanBaseMessage(NormanBaseModel):
    access_token: SensitiveType(str)
    account_id: str
    update_time: datetime
    entity_type: EntityType
    status_flag: StatusFlag

    @property
    def entity_id(self):
        raise NotImplementedError("Norman base message subclasses must implement an entity id property")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    @staticmethod
    def base_message(status_flag: StatusFlag):
        raise NotImplementedError("Norman base message subclasses must implement a serialization from flag method")

    @classmethod
    def _base_message(cls, entity_type: EntityType, status_flag: StatusFlag):
        access_token = NormanContext.get_access_token()
        update_time = datetime.now(UTC)

        return cls(
            access_token=access_token,
            account_id = status_flag.account_id,
            update_time=update_time,
            entity_type=entity_type,
            status_flag=status_flag
        )

    @classmethod
    def parse_obj(cls, raw_message: Any):
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
        if status_flag.flag_value == StatusFlagValue.Error:
            return super().parse_obj(raw_message)
        elif entity_type == EntityType.Model:
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
            return super().parse_obj(raw_message)
