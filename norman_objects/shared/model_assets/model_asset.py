import os

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.context.norman_path_context import NormanPathContext
from norman_objects.shared.files.partition_name import PartitionName
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.model_assets.asset_name import AssetName


class ModelAsset(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    version_id: str = "0"
    asset_name: AssetName
    partition_name: PartitionName

    def staging_path(self):
        mountpoint = NormanPathContext.get_mountpoint()
        partition_name = self.partition_name.value.lower()
        pluralized_entity_type = f"{EntityType.Asset.value.lower()}s"
        asset_name = self.asset_name.value.lower()

        path = os.sep.join([
            mountpoint,
            partition_name,
            self.account_id,
            self.model_id,
            self.version_id,
            pluralized_entity_type,
            self.id,
            asset_name
        ])

        return path

    def storage_path(self):
        asset_bucket_name = NormanPathContext.get_asset_bucket()
        asset_name = self.asset_name.value.lower()

        bucket = os.sep.join([
            asset_bucket_name,
            self.account_id,
            self.model_id,
            self.version_id,
            self.id,
            asset_name
        ])

        return bucket
