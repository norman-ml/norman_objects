from datetime import datetime, UTC

from norman_objects.context.context_tokens import NormanContext
from norman_objects.messages.entity_type import EntityType
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType
from norman_objects.status_flags.status_flag import StatusFlag


class NormanBaseMessage(NormanBaseModel):
    access_token: SensitiveType(str)
    account_id: str
    update_time: datetime
    entity_type: EntityType
    status_flag: StatusFlag

    @property
    def entity_id(self):
        raise NotImplementedError("Norman base message subclasses must implement an entity id property")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    @staticmethod
    def base_message(status_flag: StatusFlag):
        raise NotImplementedError("Norman base message subclasses must implement a serialization from flag method")

    @classmethod
    def _base_message(cls, entity_type: EntityType, status_flag: StatusFlag):
        access_token = NormanContext.get_access_token()
        update_time = datetime.now(UTC)

        return cls(
            access_token=access_token,
            account_id = status_flag.account_id,
            update_time=update_time,
            entity_type=entity_type,
            status_flag=status_flag
        )
