from pydantic import BaseModel


class AccountMergeRequest(BaseModel):
    primary_id: str
    secondary_id: str
