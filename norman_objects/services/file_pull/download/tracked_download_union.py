from typing import Union, Annotated

from pydantic import Field

from norman_objects.services.file_pull.download.tracked_asset_download import TrackedAssetDownload
from norman_objects.services.file_pull.download.tracked_input_download import TrackedInputDownload
from norman_objects.services.file_pull.download.tracked_output_download import TrackedOutputDownload

TrackedDownloadUnion = Annotated[
    Union[
        TrackedAssetDownload,
        TrackedInputDownload,
        TrackedOutputDownload
    ],
    Field(discriminator="entity_type")
]
