from pydantic import BaseModel


class ModelAsset(BaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    asset_name: str
