from typing import Optional

from pydantic import BaseModel


class ModelLinkConfig(BaseModel):
    account_id: str
    model_id: str
    model_name: str
    link: Optional[str] = None
    links: Optional[list[str]] = None
