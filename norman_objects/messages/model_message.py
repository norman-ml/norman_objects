from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.norman_base_message import NormanBaseMessage
from norman_objects.models.model import Model
from norman_objects.status_flags.status_flag import StatusFlag


class ModelMessage(NormanBaseMessage):
    model: Model

    @NormanBaseMessage.entity_id.getter
    def entity_id(self):
        return self.model.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Model, status_flag)
