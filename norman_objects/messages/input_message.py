from norman_objects.files.file_properties import FileProperties
from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.status_flags.status_flag import StatusFlag


class InputMessage(InvocationMessage):
    input: InvocationInput
    file_properties: FileProperties

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.input.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Input, status_flag)
