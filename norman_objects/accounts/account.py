from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.authentication.signup_request import SignupRequest
from norman_objects.authentication.user_properties import UserProperties
from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class Account(NormanBaseModel):
    id: str = "0"
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    email: Optional[str] = None
    registered: int
    confirmed: int

    @staticmethod
    def from_signup_request(account_id: str, signup_request: SignupRequest, registered: bool, confirmed: bool):
        return Account(
            id=account_id,
            name=signup_request.name,
            email=signup_request.email,
            registered=registered,
            confirmed=confirmed,
        )
