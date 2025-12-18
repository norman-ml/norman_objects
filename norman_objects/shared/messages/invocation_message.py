from typing import Literal

from pydantic import model_validator

from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.model_message import ModelMessage
from norman_objects.shared.status_flags.status_flag import StatusFlag


class InvocationMessage(ModelMessage):
    invocation: Invocation
    entity_type: Literal[EntityType.Invocation] = EntityType.Invocation

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_version_id()
        self.validate_entity_id()
        return self

    def validate_account_id(self):
        if self.account_id != self.invocation.account_id:
            raise ValueError("Message account id does not match invocation account id")

    def validate_model_id(self):
        if self.model.id != self.invocation.model_id:
            raise ValueError("Model id does not match invocation model id")

    def validate_version_id(self):
        if self.model.version.id != self.invocation.version_id:
            raise ValueError("Model version id does not match invocation version id")

    def validate_entity_id(self):
        if self.invocation.id != self.status_flag.entity_id:
            raise ValueError("Invocation id does not match status flag entity id")

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.invocation.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Invocation, status_flag)
