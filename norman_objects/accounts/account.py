from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.norman_base_model.norman_base_model import NormanBaseModel
from pydantic import Field


class Account(NormanBaseModel):
    id: str = "0"
    guest_id: Optional[str] = None
    user_id: Optional[str] = None
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    email: Optional[str] = None

    __field_to_sql_mapping__ = {
        "id": "ID",
        "creation_time": "Creation_Time",
        "name": "Name",
        "email": "Email"
    }

    def to_sql_fields(self) -> dict:
        account_data = self.dict(exclude_unset=True)

        if not account_data:
            raise ValueError("No fields provided for update")

        return {self.__field_to_sql_mapping__[key]: value for key, value in account_data.items() if key in self.__field_to_sql_mapping__}
