from datetime import datetime, timezone
from typing import Literal

from typing_extensions import override

from norman_objects.services.file_pull.download.tracked_download import TrackedDownload
from norman_objects.shared.context.norman_access_context import NormanAccessContext
from norman_objects.shared.files.file_properties import FileProperties
from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.output_message import OutputMessage
from norman_objects.shared.status_flags.status_flag import StatusFlag
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class TrackedOutputDownload(TrackedDownload):
    invocation: Invocation
    invocation_output: InvocationSignature
    entity_type: Literal[EntityType.Output] = EntityType.Output

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.invocation_output.id

    @override
    def to_message(self, flag_value: StatusFlagValue):
        access_token = NormanAccessContext.get()
        update_time = datetime.now(timezone.utc)

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
                flag_name=StatusFlagName.Output_EFS_Staging,
                flag_value=flag_value
            )
        )

        return sns_message
