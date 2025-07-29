from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.norman_base_message import NormanBaseMessage


class InvocationMessage(NormanBaseMessage):
    invocation: Invocation
