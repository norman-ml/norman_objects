from typing import Optional

from norman_objects.shared.queries.query_constraints import QueryConstraints
from pydantic import BaseModel


class GetModelsRequest(BaseModel):
    constraints: Optional[QueryConstraints] = None
    finished_models: Optional[bool] = False
