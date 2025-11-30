from datetime import datetime, UTC

from pydantic import ConfigDict

from norman_objects.norman_base_model import NormanBaseModel


class NormanError(NormanBaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    message: str
    details: dict = {}
    timestamp: datetime = datetime.now(UTC)

    def model_post_init(self, __context):
        if self.timestamp is None:
            self.timestamp = datetime.now(UTC)
