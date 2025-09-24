from datetime import datetime, timezone
from typing import Literal

from typing_extensions import override

from norman_objects.services.file_pull.download.tracked_download import TrackedDownload
from norman_objects.shared.context.norman_access_context import NormanAccessContext
from norman_objects.shared.files.file_properties import FileProperties
from norman_objects.shared.messages.asset_message import AssetMessage
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class TrackedAssetDownload(TrackedDownload):
    asset: ModelAsset
    entity_type: Literal[EntityType.Asset] = EntityType.Asset

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.asset.id

    @override
    def to_message(self, flag_value: StatusFlagValue):
        access_token = NormanAccessContext.get()
        update_time = datetime.now(timezone.utc)

        flag_name = StatusFlagName[f"{self.asset.asset_name}_EFS_Staging"]

        sns_message = AssetMessage(
            access_token=access_token,
            account_id=self.download_request.account_id,
            update_time=update_time,
            entity_type=self.entity_type,

            model=self.model,
            asset=self.asset,

            file_properties=FileProperties(
                entity_id=self.asset.id,
                file_size_in_bytes=self.downloaded_bytes,
                file_checksum=self.file_checksum
            ),

            status_flag=StatusFlag(
                account_id=self.download_request.account_id,
                entity_id=self.asset.id,
                update_time=update_time,
                flag_name=flag_name,
                flag_value=flag_value
            )
        )

        return sns_message
