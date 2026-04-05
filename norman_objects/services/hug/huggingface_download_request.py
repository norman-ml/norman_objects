from norman_objects.norman_base_model import NormanBaseModel


class HuggingFaceDownloadRequest(NormanBaseModel):
    account_id: str
    model_id: str
    version_id: str
    asset_id: str
    asset_name: str
    model_name: str
