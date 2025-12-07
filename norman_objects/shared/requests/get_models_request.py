from typing import Optional

from norman_objects.shared.queries.query_constraints import QueryConstraints
from pydantic import BaseModel


class GetModelsRequest(BaseModel):
    """
    Request object used for retrieving models with optional filtering,
    sorting, and pagination rules.

    This request wrapper allows clients to control:

    - Query constraints (filters, sorting, pagination)
    - Whether to return only models considered "finished"

    **Fields**

    - **constraints** (`Optional[QueryConstraints]`)
      Optional structured query object controlling:
        - Filtering (`FilterClause`)
        - Sorting (`SortClause`)
        - Pagination (`PageClause`)
      If `None`, the server applies default retrieval behavior.

    - **finished_models** (`Optional[bool]`)
      Whether to limit results to models marked as fully processed or
      finalized.
      - `True` Return only completed models
      - `False` or `None` Return all models
      Defaults to `False`.
    """
    constraints: Optional[QueryConstraints] = None
    finished_models: Optional[bool] = False

