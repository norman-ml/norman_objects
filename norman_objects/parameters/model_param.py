from pydantic import BaseModel

from norman_objects.parameters.param_domain import ParamDomain


class ModelParam(BaseModel):
    id: str = "0"
    model_id: str = "0"
    signature_id: str = "0"
    parameter_domain: ParamDomain
    mime_type: str
    mime_subtype: str
    parameter_name: str
