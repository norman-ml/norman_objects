from pydantic import BaseModel


class ModelAsset(BaseModel):
    id: str = "0"
    model_id: str
    asset_name: str
