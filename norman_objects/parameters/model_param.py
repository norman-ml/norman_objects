from pydantic import BaseModel

from norman_objects.parameters.data_domain import DataDomain


class ModelParam(BaseModel):
    id: str = "0"
    model_id: str = "0"
    signature_id: str = "0"
    data_domain: DataDomain
    data_encoding: str
    parameter_name: str
