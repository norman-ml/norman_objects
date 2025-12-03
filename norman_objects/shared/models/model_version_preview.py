from norman_objects.norman_base_model import NormanBaseModel


class ModelVersionPreview(NormanBaseModel):
    id: str
    account_id: str
    model_id: str
    active: bool = True
    label: str
