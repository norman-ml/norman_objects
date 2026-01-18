from typing import Annotated

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.hydration import GeneratedId, DerivedId


class ModelParam(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    model_id: Annotated[str, DerivedId("model_id")]
    version_id: Annotated[str, DerivedId("version_id")]
    signature_id: Annotated[str, DerivedId("signature_id")]
    data_modality: DataModality
    data_encoding: str
    parameter_name: str
