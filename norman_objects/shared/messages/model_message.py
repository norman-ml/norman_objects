from pydantic import model_validator
from typing_extensions import Literal

from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.norman_base_message import NormanBaseMessage
from norman_objects.shared.models.model import Model
from norman_objects.shared.models.model_projection import ModelProjection
from norman_objects.shared.status_flags.status_flag import StatusFlag


class ModelMessage(NormanBaseMessage):
    model: ModelProjection
    entity_type: Literal[EntityType.Model] = EntityType.Model

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_account_id()
        self.validate_entity_id()
        return self

    def validate_account_id(self):
        super().validate_account_id()

        if self.account_id != self.model.account_id:
            raise ValueError("Message account id does not match model account id")

    def validate_entity_id(self):
        if self.model.version.id != self.status_flag.entity_id:
            raise ValueError("Model id does not match status flag entity id")

    @NormanBaseMessage.entity_id.getter
    def entity_id(self):
        return self.model.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Model, status_flag)
