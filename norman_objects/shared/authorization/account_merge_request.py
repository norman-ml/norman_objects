from pydantic import BaseModel


class AccountMergeRequest(BaseModel):
    """
    Request object used to merge two accounts into a single primary account.

    **Fields**

    - **primary_id** (`str`)
      Identifier of the account that will remain active after the merge.

    - **secondary_id** (`str`)
      Identifier of the account that will be merged into the primary and
      subsequently deactivated or archived.
    """
    primary_id: str
    secondary_id: str
