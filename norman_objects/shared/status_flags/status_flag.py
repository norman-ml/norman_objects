from datetime import datetime, timezone
from typing import Annotated

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue
from norman_objects.hydration.id_markers import GeneratedId


class StatusFlag(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    account_id: str
    entity_id: str
    update_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    flag_name: StatusFlagName
    flag_value: StatusFlagValue
