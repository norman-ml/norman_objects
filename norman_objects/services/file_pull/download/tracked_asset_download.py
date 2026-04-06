from typing import Literal
from typing_extensions import override

from norman_objects.services.file_pull.download.tracked_download import TrackedDownload
from norman_objects.shared.assets.model_asset import ModelAsset
from norman_objects.shared.entities.entity_type import EntityType


class TrackedAssetDownload(TrackedDownload):
    asset: ModelAsset
    entity_type: Literal[EntityType.Asset] = EntityType.Asset

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.asset.id
