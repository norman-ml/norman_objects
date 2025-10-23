from norman_objects.norman_base_model import NormanBaseModel


class ModelTag(NormanBaseModel):
    model_id: str = "0"
    name: str
    count: int = 1
