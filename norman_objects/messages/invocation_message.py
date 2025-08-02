from norman_objects.invocations.invocation import Invocation
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.model_message import ModelMessage
from norman_objects.status_flags.status_flag import StatusFlag


class InvocationMessage(ModelMessage):
    invocation: Invocation

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.invocation.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Invocation, status_flag)
