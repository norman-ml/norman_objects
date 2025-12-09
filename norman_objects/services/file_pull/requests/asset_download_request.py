from datetime import datetime, timezone
from typing_extensions import override

from norman_objects.services.file_pull.requests.norman_file_download_request import NormanFileDownloadRequest
from norman_objects.shared.messages.asset_message import AssetMessage
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class AssetDownloadRequest(NormanFileDownloadRequest):
    asset_id: str
    asset_name: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.asset_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Asset

    @override
    def to_base_message(self, flag_value: StatusFlagValue):
        status_flag = super().to_status_flag(flag_value)
        return AssetMessage.base_message(status_flag)

    @override
    def to_status_flag(self, flag_value: StatusFlagValue):
        update_time = datetime.now(timezone.utc)
        flag_name = StatusFlagName[f"{self.asset_name}_EFS_Staging"]

        return StatusFlag(
            account_id=self.account_id,
            entity_id=self.entity_id,
            update_time=update_time,
            flag_name=flag_name,
            flag_value=flag_value
        )
