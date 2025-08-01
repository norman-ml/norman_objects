from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.outputs.invocation_output import InvocationOutput


class OutputMessage(InvocationMessage):
    output: InvocationOutput
    file_properties: FileProperties
