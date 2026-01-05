from datetime import datetime, timezone

from pydantic import Field, model_validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature


class Invocation(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    version_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    inputs: list[InvocationSignature] = []
    outputs: list[InvocationSignature] = []

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_version_id()
        self.validate_signature_id()
        return self

    def validate_account_id(self):
        for invocation_input in self.inputs:
            if self.account_id != invocation_input.account_id:
                raise ValueError("Invocation account id does not match invocation input signature account id")

        for invocation_output in self.outputs:
            if self.account_id != invocation_output.account_id:
                raise ValueError("Invocation account id does not match invocation output signature account id")

    def validate_model_id(self):
        for invocation_input in self.inputs:
            if self.model_id != invocation_input.model_id:
                raise ValueError("Invocation model id does not match invocation input signature model id")

        for invocation_output in self.outputs:
            if self.model_id != invocation_output.model_id:
                raise ValueError("Invocation model id does not match invocation output signature model id")

    def validate_version_id(self):
        for invocation_input in self.inputs:
            if self.version_id != invocation_input.version_id:
                raise ValueError("Invocation version id does not match invocation input signature version id")

        for invocation_output in self.outputs:
            if self.version_id != invocation_output.version_id:
                raise ValueError("Invocation version id does not match invocation output signature version id")

    def validate_invocation_id(self):
        for invocation_input in self.inputs:
            if self.id != invocation_input.invocation_id:
                raise ValueError("Invocation id does not match invocation input signature invocation id")

        for invocation_output in self.outputs:
            if self.id != invocation_output.invocation_id:
                raise ValueError("Invocation id does not match invocation output signature invocation id")
