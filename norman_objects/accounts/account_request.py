from datetime import datetime, timedelta, timezone

from norman_objects.accounts.request_method import RequestMethod
from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class AccountRequest(NormanBaseModel):
    id: str = "0"
    account_id: str = "0"
    endpoint: str
    port: int
    method: RequestMethod
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

