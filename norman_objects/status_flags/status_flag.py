from datetime import datetime

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class StatusFlag(NormanBaseModel):
    id: str = "0"
    account_id: str
    entity_id: str = "0"
    update_time: datetime
    flag_name: str
    flag_value: StatusFlagValue
