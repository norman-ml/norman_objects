from pydantic import model_validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.assets.model_asset import ModelAsset
from norman_objects.shared.models.model_build_status import ModelBuildStatus


class ModelVersionPreview(NormanBaseModel):
    id: str
    account_id: str
    model_id: str
    build_status: ModelBuildStatus
    active: bool = True
    label: str
    short_description: str

    assets: list[ModelAsset] = []

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_version_id()
        return self

    def validate_account_id(self):
        for asset in self.assets:
            if self.account_id != asset.account_id:
                raise ValueError("Model version account id does not match model asset account id")

    def validate_model_id(self):
        for asset in self.assets:
            if self.model_id != asset.model_id:
                raise ValueError("Model version model id does not match model asset model id")

    def validate_version_id(self):
        for asset in self.assets:
            if self.id != asset.version_id:
                raise ValueError("Model version id does not match model asset version id")
