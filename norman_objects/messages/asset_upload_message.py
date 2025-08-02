from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.model_message import ModelMessage
from norman_objects.models.model_asset import ModelAsset
from norman_objects.status_flags.status_flag import StatusFlag


class AssetUploadMessage(ModelMessage):
    asset: ModelAsset
    file_properties: FileProperties

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.asset.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Asset, status_flag)
