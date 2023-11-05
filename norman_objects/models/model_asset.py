from pydantic import BaseModel


class ModelAsset(BaseModel):
    id: str = "0"
    model_id: str = "0"
    asset_name: str
