from pydantic import BaseModel

from norman_objects.messages.entity_type import EntityType
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class StandardMessage(BaseModel):
    entity_type: EntityType

    model_id: str
    model_name: str

    parameter_id: str = ""
    invocation_id: str = ""
    input_id: str = ""
    output_id: str = ""

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

