from datetime import datetime, UTC

from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.context.norman_access_context import NormanAccessContext
from norman_objects.shared.files.file_properties import FileProperties
from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.output_message import OutputMessage
from norman_objects.shared.models.model import Model
from norman_objects.shared.outputs.invocation_output import InvocationOutput
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue
from typing_extensions import override

from src.objects.tracked_download import TrackedDownload


class TrackedOutputDownload(TrackedDownload):
    def __init__(self, download_request: NormanFileDownloadRequest, file_link: str, model: Model, invocation: Invocation, invocation_output: InvocationOutput):
        super().__init__(download_request, file_link, model)
        self.invocation = invocation
        self.invocation_output = invocation_output

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.invocation_output.id

    @TrackedDownload.entity_type.getter
    def entity_type(self):
        return EntityType.Output

    @override
    def to_message(self, flag_value: StatusFlagValue):
        access_token = NormanAccessContext.get()
        update_time = datetime.now(UTC)

        sns_message = OutputMessage(
            access_token=access_token,
            account_id=self.download_request.account_id,
            update_time=update_time,
            entity_type=self.entity_type,

            model=self.model,
            invocation=self.invocation,
            output=self.invocation_output,

            file_properties=FileProperties(
                entity_id=self.invocation_output.id,
                file_size_in_bytes=self.downloaded_bytes,
                file_checksum=self.file_checksum
            ),

            status_flag=StatusFlag(
                account_id=self.download_request.account_id,
                entity_id=self.invocation_output.id,
                update_time=update_time,
                flag_name="EFS_Transfer",
                flag_value=flag_value
            )
        )

        return sns_message
