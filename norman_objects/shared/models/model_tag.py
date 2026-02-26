from norman_objects.norman_base_model import NormanBaseModel


class ModelTag(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    name: str
