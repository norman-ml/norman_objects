from norman_objects.norman_base_model import NormanBaseModel


class ModelBaseTag(NormanBaseModel):
    id: str = "0"
    account_id: str = "0"
    model_base_id: str = "0"
    name: str
