from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.file_message import FileMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.models.model_asset import ModelAsset
from norman_objects.status_flags.status_flag import StatusFlag


class AssetMessage(ModelMessage, FileMessage):
    asset: ModelAsset

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.asset.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Asset, status_flag)
