from norman_objects.messages.invocation_message import InvocationMessage
from norman_objects.outputs.invocation_output import InvocationOutput


class OutputMessage(InvocationMessage):
    output: InvocationOutput
