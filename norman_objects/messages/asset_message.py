from pydantic import root_validator

from norman_objects.messages.entity_type import EntityType
from norman_objects.messages.file_message import FileMessage
from norman_objects.messages.model_message import ModelMessage
from norman_objects.models.model import Model
from norman_objects.models.model_asset import ModelAsset
from norman_objects.status_flags.status_flag import StatusFlag


class AssetMessage(ModelMessage, FileMessage):
    asset: ModelAsset

    @root_validator
    def validate_account_id(cls, values):
        super().validate_account_id(values)

        account_id: str = values.get("account_id")
        asset: ModelAsset = values.get("asset")

        if account_id != asset.account_id:
            raise ValueError("Message account id does not match asset account id")

        return values

    @root_validator
    def validate_model_id(cls, values):
        model: Model = values.get("model")
        asset: ModelAsset = values.get("asset")

        if model.id != asset.model_id:
            raise ValueError("Model id does not match asset model id")

        return values

    @root_validator
    def validate_entity_id(cls, values):
        asset: ModelAsset = values.get("asset")
        status_flag: StatusFlag = values.get("status_flag")

        if asset.id != status_flag.entity_id:
            raise ValueError("Asset id does not match status flag entity id")

        return values

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.asset.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Asset, status_flag)
