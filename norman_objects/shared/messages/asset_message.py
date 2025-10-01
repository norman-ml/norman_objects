from typing import Literal

from pydantic import model_validator

from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.file_message import FileMessage
from norman_objects.shared.messages.model_message import ModelMessage
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.status_flags.status_flag import StatusFlag


class AssetMessage(ModelMessage, FileMessage):
    asset: ModelAsset
    entity_type: Literal[EntityType.Asset] = EntityType.Asset

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_entity_id()
        return self

    def validate_account_id(self):
        super().validate_account_id()

        if self.account_id != self.asset.account_id:
            raise ValueError("Message account id does not match asset account id")

    def validate_model_id(self):
        if self.model.id != self.asset.model_id:
            raise ValueError("Model id does not match asset model id")

    def validate_entity_id(self):
        if self.asset.id != self.status_flag.entity_id:
            raise ValueError("Asset id does not match status flag entity id")

    @ModelMessage.entity_id.getter
    def entity_id(self):
        return self.asset.id

    @classmethod
    def base_message(cls, status_flag: StatusFlag):
        return cls._base_message(EntityType.Asset, status_flag)
