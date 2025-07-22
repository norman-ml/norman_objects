from norman_objects.models.model import Model
from norman_objects.models.model_version_info import ModelVersionInfo
from norman_objects.norman_base_model import NormanBaseModel

class ModelBase(NormanBaseModel):
    id: str
    model: Model
    version_info: list[ModelVersionInfo] = []
