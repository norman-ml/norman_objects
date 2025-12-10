from datetime import datetime, timezone
from typing_extensions import override

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.messages.asset_message import AssetMessage
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class HuggingFaceDownloadRequest(NormanBaseModel):
    account_id: str
    model_id : str
    huggingface_model_id: str
    asset_id: str


    def entity_id(self):
        return self.asset_id

    def entity_type(self):
        return EntityType.Asset

    def to_base_message(self, flag_value: StatusFlagValue):
        status_flag = super().to_status_flag(flag_value)
        return AssetMessage.base_message(status_flag)

    def to_status_flag(self, flag_value: StatusFlagValue):
        update_time = datetime.now(timezone.utc)
        flag_name = StatusFlagName[f"{self.huggingface_model_id}_EFS_Staging"]

        return StatusFlag(
            account_id=self.account_id,
            entity_id=self.entity_id,
            update_time=update_time,
            flag_name=flag_name,
            flag_value=flag_value
        )
