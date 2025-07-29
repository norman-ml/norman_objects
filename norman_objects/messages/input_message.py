from norman_objects.inputs.invocation_input import InvocationInput
from norman_objects.messages.invocation_message import InvocationMessage


class InputMessage(InvocationMessage):
    input: InvocationInput
