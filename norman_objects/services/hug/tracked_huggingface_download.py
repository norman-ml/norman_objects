from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.services.hug.huggingface_download_request import HuggingFaceDownloadRequest
from norman_objects.shared.assets.model_asset import ModelAsset
from norman_objects.shared.models.model_projection import ModelProjection


class TrackedHuggingFaceDownload(NormanBaseModel):
    download_request: HuggingFaceDownloadRequest
    model: ModelProjection
    asset: ModelAsset
