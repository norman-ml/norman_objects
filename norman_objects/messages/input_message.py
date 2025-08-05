from pydantic import root_validator

from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.file_message import FileMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.status_flags.status_flag import StatusFlag


class InputMessage(InvocationMessage, FileMessage):
    input: InvocationInput

    @root_validator
    def validate_account_id(cls, values):
        super().validate_account_id(values)

        account_id: str = values.get("account_id")
        input: InvocationInput = values.get("input")

        if account_id != input.account_id:
            raise ValueError("Message account id does not match input account id")

    @root_validator
    def validate_model_id(cls, values):
        super().validate_model_id()

        invocation: Invocation = values.get("invocation")
        input: InvocationInput = values.get("input")

        if invocation.model_id != input.model_id:
            raise ValueError("Invocation model id does not match input model id")

        return values

    @root_validator
    def validate_invocation_id(cls, values):
        invocation: Invocation = values.get("invocation")
        input: InvocationInput = values.get("input")

        if invocation.id != input.invocation_id:
            raise ValueError("Message invocation id does not match input invocation id")

        return values

    @root_validator
    def validate_entity_id(cls, values):
        input: InvocationInput = values.get("input")
        status_flag: StatusFlag = values.get("status_flag")

        if input.id != status_flag.entity_id:
            raise ValueError("Input id does not match status flag entity id")

        return values

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.input.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Input, status_flag)
