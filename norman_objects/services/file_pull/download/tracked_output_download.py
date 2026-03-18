from typing import Literal

from norman_objects.services.file_pull.download.tracked_download import TrackedDownload
from norman_objects.shared.entities.entity_type import EntityType
from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature


class TrackedOutputDownload(TrackedDownload):
    invocation: Invocation
    invocation_output: InvocationSignature
    entity_type: Literal[EntityType.Output] = EntityType.Output

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.invocation_output.id
