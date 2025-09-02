from typing import Any

from norman_objects.inputs.input_source import InputSource
from pydantic import BaseModel


class InvocationConfig(BaseModel):
    account_id: str
    model_id: str
    model_name: str
    model_primitives: dict[str, Any]
    model_links: dict[str, str]
    model_file_names: list[str]

    def get_input_source(self, signature_id: str):
        if signature_id in self.model_primitives:
            return InputSource.Primitive
        elif signature_id in self.model_links:
            return InputSource.Link
        elif signature_id in self.model_file_names:
            return InputSource.File
        return InputSource.Storage

    def get_input_value(self, signature_id: str):
        if signature_id in self.model_primitives:
            return self.model_primitives[signature_id]
        elif signature_id in self.model_links:
            return self.model_links[signature_id]
        return None
