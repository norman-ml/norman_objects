from typing import Literal

from pydantic import model_validator

from norman_objects.files.file_properties import FileProperties
from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.file_message import FileMessage
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.outputs.invocation_output import InvocationOutput
from norman_objects.status_flags.status_flag import StatusFlag


class OutputMessage(InvocationMessage, FileMessage):
    output: InvocationOutput
    file_properties: FileProperties
    entity_type: Literal[EntityType.Output] = EntityType.Output

    def validate_account_id(self):
        super().validate_account_id()

        if self.account_id != self.output.account_id:
            raise ValueError("Message account id does not match output account id")

    def validate_model_id(self):
        super().validate_model_id()

        if self.invocation.model_id != self.output.model_id:
            raise ValueError("Invocation model id does not match output model id")

    def validate_invocation_id(self):
        if self.invocation.id != self.output.invocation_id:
            raise ValueError("Message invocation id does not match output invocation id")

    def validate_entity_id(self):
        if self.output.id != self.status_flag.entity_id:
            raise ValueError("Output id does not match status flag entity id")

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_invocation_id()
        self.validate_entity_id()
        return self

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.output.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Output, status_flag)
