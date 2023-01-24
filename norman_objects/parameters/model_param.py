from typing import List

from pydantic import BaseModel

from norman_objects.parameters.model_param_domain import ModelParamDomain
from norman_objects.parameters.model_param_receive_format import ModelParamReceiveFormat
from norman_objects.parameters.model_param_record_type import ModelParamRecordType
from norman_objects.parameters.model_param_transform import ModelParamTransform


class ModelParam(BaseModel):
    id: str = "0"
    model_id: str = "0"
    record_type: ModelParamRecordType
    parameter_domain: ModelParamDomain
    parameter_receive_format: ModelParamReceiveFormat
    parameter_name: str
    parameter_display_title: str
    transforms: List[ModelParamTransform] = []
