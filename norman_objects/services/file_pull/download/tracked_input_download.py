from typing import Literal
from typing_extensions import override

from norman_objects.services.file_pull.download.tracked_download import TrackedDownload
from norman_objects.shared.entities.entity_type import EntityType
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature
from norman_objects.shared.invocations.invocation import Invocation


class TrackedInputDownload(TrackedDownload):
    invocation: Invocation
    invocation_input: InvocationSignature
    entity_type: Literal[EntityType.Input] = EntityType.Input

    @TrackedDownload.entity_id.getter
    def entity_id(self):
        return self.invocation_input.id

    @override
    def staging_path(self):
        return self.invocation_input.staging_path()
