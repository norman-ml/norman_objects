from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.assets.asset_name import AssetName
from norman_objects.shared.files.partition_name import PartitionName
from norman_objects.shared.modality.container_modality import ContainerModality


class ModelAsset(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    version_id: str = "0"
    asset_name: AssetName
    container_modality: ContainerModality
    partition_name: PartitionName
