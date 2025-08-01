from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.model_message import ModelMessage


class InvocationMessage(ModelMessage):
    invocation: Invocation
