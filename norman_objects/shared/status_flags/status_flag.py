from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class StatusFlag(NormanBaseModel):
    """
    Represents a status indicator for a specific entity (model, file, input,
    output, staging step, or processing stage) within the Norman system.

    A `StatusFlag` tracks the progress of a workflow step, how far it has
    advanced, and whether it completed successfully or encountered an error.
    Status flags are used extensively across staging pipelines, model builds,
    file processing, input/output transformation, and more.

    **Fields**

    - **id** (`str`)
      Unique identifier for the status flag record. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account that owns this entity.

    - **entity_id** (`str`)
      Identifier of the entity being tracked (e.g., model ID, asset ID,
      invocation ID, or upload ID).

    - **update_time** (`datetime`)
      UTC timestamp of the most recent update to this flag.
      Defaults to the current time.

    - **flag_name** (`StatusFlagName`)
      Name of the workflow step being tracked (see `StatusFlagName` enum).

    - **flag_value** (`StatusFlagValue`)
      Current progress state for the step (see `StatusFlagValue` enum).
    """
    id: str = "0"
    account_id: str
    entity_id: str
    update_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    flag_name: StatusFlagName
    flag_value: StatusFlagValue

