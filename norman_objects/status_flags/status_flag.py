from datetime import datetime

from pydantic import BaseModel

from norman_objects.status_flags.status_flag_value import StatusFlagValue


class StatusFlag(BaseModel):
    id: str = "0"
    entity_id: str = "0"
    update_time: datetime
    flag_name: str
    flag_value: StatusFlagValue
