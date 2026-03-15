from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.entities.entity_type import EntityType


class AssetDownloadRequest(NormanFileDownloadRequest):
    asset_id: str
    asset_name: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.asset_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Asset
