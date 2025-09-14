from datetime import datetime, timezone
from typing import List

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class NormanFileDownloadRequest(NormanBaseModel):
    account_id: str
    model_id: str
    links: List[str]

    @property
    def entity_id(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity id")

    @property
    def entity_type(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity type")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    def to_base_message(self, flag_value: StatusFlagValue):
        raise NotImplementedError("Tracked download config subclasses must be able to serialize to a fallback sns message")

    def to_status_flag(self, flag_value: StatusFlagValue):
        update_time = datetime.now(timezone.utc)

        return StatusFlag(
            account_id=self.account_id,
            entity_id=self.entity_id,
            update_time=update_time,
            flag_name="EFS_Transfer",
            flag_value=flag_value
        )