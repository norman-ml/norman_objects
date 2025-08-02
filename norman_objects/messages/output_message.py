from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.outputs.invocation_output import InvocationOutput
from norman_objects.status_flags.status_flag import StatusFlag


class OutputMessage(InvocationMessage):
    output: InvocationOutput
    file_properties: FileProperties

    @InvocationMessage.entity_id.getter
    def entity_id(self):
        return self.output.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Output, status_flag)
