from pydantic import model_validator

from norman_objects.files.file_properties import FileProperties
from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.file_message import FileMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.status_flags.status_flag import StatusFlag


class InputMessage(InvocationMessage, FileMessage):
    input: InvocationInput
    file_properties: FileProperties

    def validate_account_id(self):
        super().validate_account_id()

        if self.account_id != self.input.account_id:
            raise ValueError("Message account id does not match input account id")

    def validate_model_id(self):
        super().validate_model_id()

        if self.invocation.model_id != self.input.model_id:
            raise ValueError("Invocation model id does not match input model id")

    def validate_invocation_id(self):
        if self.invocation.id != self.input.invocation_id:
            raise ValueError("Message invocation id does not match input invocation id")

    def validate_entity_id(self):
        if self.input.id != self.status_flag.entity_id:
            raise ValueError("Input id does not match status flag entity id")

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_invocation_id()
        self.validate_entity_id()
        return self

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.input.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Input, status_flag)
