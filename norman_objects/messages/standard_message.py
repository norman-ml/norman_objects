from datetime import datetime

from norman_objects.messages.entity_type import EntityType
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class StandardMessage(NormanBaseModel):
    access_token: str = ""

    update_time: datetime
    entity_type: EntityType

    account_id:str

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

    @property
    def entity_id(self):
        if self.entity_type is not None:
            entity_name = self.entity_type.name.lower()
            id_key = f"{entity_name}_id"
            return getattr(self, id_key, None)

        return None

