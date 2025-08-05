from pydantic import root_validator

from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.norman_base_message import NormanBaseMessage
from norman_objects.models.model import Model
from norman_objects.status_flags.status_flag import StatusFlag


class ModelMessage(NormanBaseMessage):
    model: Model

    @root_validator
    def validate_account_id(cls, values):
        super().validate_account_id(values)

        account_id: str = values.get("account_id")
        model: Model = values.get("model")

        if account_id != model.account_id:
            raise ValueError("Message account id does not match model account id")

        return values

    @root_validator
    def validate_entity_id(cls, values):
        model: Model = values.get("model")
        status_flag: StatusFlag = values.get("status_flag")

        if model.id != status_flag.entity_id:
            raise ValueError("Model id does not match status flag entity id")

        return values

    @NormanBaseMessage.entity_id.getter
    def entity_id(self):
        return self.model.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Model, status_flag)
