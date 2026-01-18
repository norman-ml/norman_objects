from typing import Annotated

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.hydration import GeneratedId, DerivedId


class ModelAsset(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    account_id: str = ""
    model_id: Annotated[str, DerivedId("model_id")]
    version_id: Annotated[str, DerivedId("version_id")]
    asset_name: str
    data_modality: DataModality
