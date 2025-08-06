from datetime import datetime, timedelta, timezone

from norman_objects.authentication.signup_request import SignupRequest
from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class UserProperties(NormanBaseModel):
    account_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    registered: int
    confirmed: int

    @staticmethod
    def from_signup_request(account_id: str, signup_request: SignupRequest, registered: bool):
        return UserProperties(
            account_id=account_id,
            name=signup_request.name,
            registered=registered,
            confirmed=False
        )
