from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality


class ModelAsset(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    version_id: str = "0"
    asset_name: str
    container_modality: ContainerModality
    container_encoding: ContainerEncoding
