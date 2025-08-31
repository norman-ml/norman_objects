from datetime import datetime, timezone

from pydantic import model_validator

from norman_objects.authorization.jwt_token import JwtToken
from norman_objects.context.norman_access_context import NormanAccessContext
from norman_objects.messages.entity_type import EntityType
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.status_flags.status_flag import StatusFlag


class NormanBaseMessage(NormanBaseModel):
    access_token: JwtToken
    account_id: str
    update_time: datetime
    entity_type: EntityType
    status_flag: StatusFlag

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        return self

    def validate_account_id(self):
        if self.account_id != self.status_flag.account_id:
            raise ValueError("Message account id does not match status flag account id")

    @property
    def entity_id(self):
        raise NotImplementedError("Norman base message subclasses must implement an entity id property")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    @staticmethod
    def base_message(status_flag: StatusFlag):
        raise NotImplementedError("Norman base message subclasses must implement a serialization from flag method")

    @classmethod
    def _base_message(cls, entity_type: EntityType, status_flag: StatusFlag):
        access_token = NormanAccessContext.get()
        update_time = datetime.now(timezone.utc)

        return cls(
            access_token=access_token,
            account_id = status_flag.account_id,
            update_time=update_time,
            entity_type=entity_type,
            status_flag=status_flag
        )
