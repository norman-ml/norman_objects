from pydantic import root_validator

from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.model_message import ModelMessage
from norman_objects.models.model import Model
from norman_objects.status_flags.status_flag import StatusFlag


class InvocationMessage(ModelMessage):
    invocation: Invocation

    @root_validator
    def validate_account_id(cls, values):
        super().validate_account_id(values)

        account_id: str = values.get("account_id")
        invocation: Invocation = values.get("invocation")

        if account_id != invocation.account_id:
            raise ValueError("Message account id does not match invocation account id")

        return values

    @root_validator
    def validate_model_id(cls, values):
        model: Model = values.get("model")
        invocation: Invocation = values.get("invocation")

        if model.id != invocation.model_id:
            raise ValueError("Model id does not match invocation model id")

        return values

    @root_validator
    def validate_entity_id(cls, values):
        invocation: Invocation = values.get("invocation")
        status_flag: StatusFlag = values.get("status_flag")

        if invocation.id != status_flag.entity_id:
            raise ValueError("Invocation id does not match status flag entity id")

        return values

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.invocation.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Invocation, status_flag)
