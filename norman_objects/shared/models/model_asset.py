from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.asset_name import AssetName


class ModelAsset(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    version_id: str = "0"
    asset_name: AssetName
