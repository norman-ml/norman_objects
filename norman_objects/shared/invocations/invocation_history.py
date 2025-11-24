from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class InvocationHistory(NormanBaseModel):
    """
    Represents a historical record of a model invocation, including metadata,
    the associated asset, and the final status flag.

    This object is typically used for audit logs, user-visible invocation
    histories, dashboards, and post-processing workflows.

    **Fields**

    - **id** (`str`)
      Unique identifier for the invocation history entry.

    - **account_id** (`str`)
      Identifier of the account that executed the invocation.

    - **model_id** (`str`)
      Identifier of the model involved in the invocation.

    - **asset_id** (`str`)
      Identifier of the related asset (e.g., input file, output file,
      staged artifact).

    - **creation_time** (`datetime`)
      Timestamp (UTC) marking when the invocation occurred.
      Defaults to the current time.

    - **model_name** (`str`)
      Human-readable name of the model at the time the invocation occurred.

    - **flag_value** (`StatusFlagValue`)
      Final status flag for the invocation:
      - Not_Started
      - Enqueued
      - In_Progress
      - Finished
      - Error
    """
    id: str
    account_id: str
    model_id: str
    asset_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    model_name: str
    flag_value: StatusFlagValue
