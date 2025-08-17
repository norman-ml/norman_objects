from datetime import datetime, timezone
from uuid import uuid4

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class Account(NormanBaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    name: str

    @classmethod
    def create(cls, name: str):
        return cls(name=name)
