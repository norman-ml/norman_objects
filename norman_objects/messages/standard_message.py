from collections.abc import Mapping
from datetime import datetime

from norman_objects.messages.entity_type import EntityType
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive import Sensitive      # ①
from norman_objects.sensitive.sensitive_type import SensitiveType
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class StandardMessage(NormanBaseModel, Mapping):
    # ──────────────────  data fields  ──────────────────
    access_token: SensitiveType(str) = ""

    update_time: datetime
    entity_type: EntityType

    account_id: str

    model_id: str
    model_name: str

    signature_id: str = ""
    invocation_id: str = ""
    input_id: str = ""
    output_id: str = ""

    asset_id: str = ""

    file_name: str = ""
    file_size_in_bytes: int = 0
    file_checksum: str = "Not yet implemented"

    flag_name: str
    flag_value: StatusFlagValue

    # ──────────────────  model config  ──────────────────
    class Config:                     # Pydantic v1
        json_encoders = {
            Sensitive: lambda v: str(v)      # → "<redacted>"
        }

    # If you’re already on Pydantic v2, delete the Config above
    # and uncomment the serializer below instead:
    #
    # @field_serializer("access_token", when_used="json")
    # def _redact_access_token(self, value: Sensitive, _info):
    #     return str(value)

    # ──────────────────  helpers  ──────────────────
    @property
    def entity_id(self):
        if self.entity_type is not None:
            entity_name = self.entity_type.name.lower()
            return getattr(self, f"{entity_name}_id", None)
        return None

    # Mapping-like behaviour so **obj still works
    def __getitem__(self, key):
        return self.dict()[key]       # ← dict() now returns the redacted token

    def __iter__(self):
        return iter(self.dict())

    def __len__(self):
        return len(self.dict())
