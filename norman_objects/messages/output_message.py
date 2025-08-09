from pydantic import root_validator

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

    @root_validator
    def validate_account_id(cls, values):
        super().validate_account_id(values)

        account_id: str = values.get("account_id")
        output: InvocationOutput = values.get("output")

        if account_id != output.account_id:
            raise ValueError("Message account id does not match output account id")

        return values

    @root_validator
    def validate_model_id(cls, values):
        super().validate_model_id(values)

        invocation: Invocation = values.get("invocation")
        output: InvocationOutput = values.get("output")

        if invocation.model_id != output.model_id:
            raise ValueError("Invocation model id does not match output model id")

        return values

    @root_validator
    def validate_invocation_id(cls, values):
        invocation: Invocation = values.get("invocation")
        output: InvocationOutput = values.get("output")

        if invocation.id != output.invocation_id:
            raise ValueError("Message invocation id does not match output invocation id")

        return values

    @root_validator
    def validate_entity_id(cls, values):
        output: InvocationOutput = values.get("output")
        status_flag: StatusFlag = values.get("status_flag")

        if output.id != status_flag.entity_id:
            raise ValueError("Output id does not match status flag entity id")

        return values

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.output.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Output, status_flag)
