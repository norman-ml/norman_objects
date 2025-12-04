from datetime import datetime, timezone
from typing import List

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class NormanFileDownloadRequest(NormanBaseModel):
    """
    Base request object describing a file download operation within the
    Norman platform. This includes all metadata required to authorize
    and locate files across storage layers.

    **Fields**

    - **account_id** (`str`)
      Identifier of the account requesting the download.

    - **model_id** (`str`)
      Identifier of the model associated with the requested file(s).

    - **links** (`List[str]`)
      List of storage links or paths pointing to the files that should
      be downloaded. These may reference S3 paths, EFS paths, or internal
      storage URLs.
    """
    account_id: str
    model_id: str
    links: List[str]

    @property
    def entity_id(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity id")

    @property
    def entity_type(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity type")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    def to_base_message(self, flag_value: StatusFlagValue):
        raise NotImplementedError("Tracked download config subclasses must be able to serialize to a fallback sns message")

    def to_status_flag(self, flag_value: StatusFlagValue):
        raise NotImplementedError("Tracked download config subclasses must be able to serialize to a status flag")