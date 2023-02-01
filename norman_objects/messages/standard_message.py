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

    file_name: str
    file_size_in_bytes: int = 0
    file_checksum: str = "Not yet implemented"

    flag_name: str
    flag_value: StatusFlagValue

    @property
    def entity_id(self):
        id_key = "{entity_type}_id".format(entity_type=self.entity_type.name.lower())
        return getattr(self, id_key, None)

