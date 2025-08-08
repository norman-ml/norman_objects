from norman_objects.models.model_preview import ModelPreview
from norman_objects.norman_base_model import NormanBaseModel

class ModelBase(NormanBaseModel):
    id: str
    account_id: str
    name: str
    model_previews: list[ModelPreview] = []
