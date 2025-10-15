from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.parameters.data_modality import DataModality


class ModelParam(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    signature_id: str = "0"
    data_modality: DataModality
    data_encoding: str
    parameter_name: str
