from datetime import datetime, timezone
from typing_extensions import override

from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.input_message import InputMessage
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class InputDownloadRequest(NormanFileDownloadRequest):
    """
    Request object for downloading input files associated with a specific
    model invocation. Extends `NormanFileDownloadRequest` with additional
    identifiers required for retrieving input artifacts.

    **Fields**

    - **account_id** (`str`)
      Inherited from `NormanFileDownloadRequest`.

    - **model_id** (`str`)
      Inherited from `NormanFileDownloadRequest`.

    - **links** (`List[str]`)
      Inherited from `NormanFileDownloadRequest`.

    - **signature_id** (`str`)
      Identifier of the input signature definition associated with
      the file being downloaded.

    - **invocation_id** (`str`)
      Identifier of the invocation to which this input belongs.

    - **input_id** (`str`)
      Identifier of the input object being downloaded.
    """
    signature_id: str
    invocation_id: str
    input_id: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.input_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Input

    @override
    def to_base_message(self, flag_value: StatusFlagValue):
        status_flag = super().to_status_flag(flag_value)
        return InputMessage.base_message(status_flag)

    @override
    def to_status_flag(self, flag_value: StatusFlagValue):
        update_time = datetime.now(timezone.utc)

        return StatusFlag(
            account_id=self.account_id,
            entity_id=self.entity_id,
            update_time=update_time,
            flag_name=StatusFlagName.Input_EFS_Staging,
            flag_value=flag_value
        )
