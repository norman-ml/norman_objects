from norman_objects.norman_base_model import NormanBaseModel


class ModelAsset(NormanBaseModel):
    id: str = "0"
    account_id: str = ""
    model_id: str = "0"
    asset_name: str
