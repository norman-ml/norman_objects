from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.model_message import ModelMessage
from norman_objects.models.model_asset import ModelAsset


class AssetUploadMessage(ModelMessage):
    asset: ModelAsset
    file_properties: FileProperties
