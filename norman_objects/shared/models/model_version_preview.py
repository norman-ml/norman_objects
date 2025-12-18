from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.models.model_build_status import ModelBuildStatus


class ModelVersionPreview(NormanBaseModel):
    id: str
    model_id: str
    build_status: ModelBuildStatus
    active: bool = True
    label: str
    short_description: str

    assets: list[ModelAsset] = []