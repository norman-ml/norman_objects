from typing import Optional

from pydantic import model_validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.model_signatures.http_location import HttpLocation
from norman_objects.shared.model_signatures.receive_format import ReceiveFormat
from norman_objects.shared.model_signatures.signature_transform import SignatureTransform
from norman_objects.shared.model_signatures.signature_type import SignatureType
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.shared.parameters.model_param import ModelParam


class ModelSignature(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    version_id: str = "0"
    signature_type: SignatureType
    data_modality: DataModality
    data_domain: str
    data_encoding: str
    receive_format: ReceiveFormat
    http_location: HttpLocation
    hidden: bool
    display_title: str
    default_value: Optional[str] = None

    parameters: list[ModelParam] = []
    transforms: list[SignatureTransform] = []
    signature_args: dict[str, str] = {}

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_version_id()
        self.validate_signature_id()
        return self

    def validate_account_id(self):
        for parameter in self.parameters:
            if self.account_id != parameter.account_id:
                raise ValueError("Model signature account id does not match model parameter account id")

    def validate_model_id(self):
        for parameter in self.parameters:
            if self.model_id != parameter.model_id:
                raise ValueError("Model signature model id does not match model parameter model id")

    def validate_version_id(self):
        for parameter in self.parameters:
            if self.version_id != parameter.version_id:
                raise ValueError("Model signature version id does not match model parameter version id")

    def validate_signature_id(self):
        for parameter in self.parameters:
            if self.id != parameter.signature_id:
                raise ValueError("Model signature id does not match model parameter signature id")

        for transform in self.transforms:
            if self.id != transform.signature_id:
                raise ValueError("Model signature id does not match signature transform signature id")
