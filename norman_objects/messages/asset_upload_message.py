from norman_objects.messages.norman_base_message import NormanBaseMessage
from norman_objects.models.model_asset import ModelAsset


class AssetUploadMessage(NormanBaseMessage):
    asset: ModelAsset
