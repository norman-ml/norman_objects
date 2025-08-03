from pydantic import BaseModel
from datetime import datetime

class Credit(BaseModel):
    id: str = "0"                   # default means "auto-generate"
    quota_id: str                   # UUID (BINARY(16) in DB)
    start_date: datetime
    end_date: datetime
    billable: bool = False
