from norman_objects.shared.messages.asset_message import AssetMessage
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue
from typing_extensions import override

from src.objects.requests.file_download_request import NormanFileDownloadRequest


class AssetDownloadRequest(NormanFileDownloadRequest):
    asset_id: str

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
