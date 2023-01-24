from pydantic import BaseModel


class StatusFlag(BaseModel):
    id: str = "0"
    entity_id: str = "0"
    flag_name: str
    flag_value: str
