from typing import Dict

from pydantic import BaseModel


class SignatureTransform(BaseModel):
    id: str = "0"
    signature_id: str = "0"
    transform_name: str
    transform_args: Dict[str, str] = {}
