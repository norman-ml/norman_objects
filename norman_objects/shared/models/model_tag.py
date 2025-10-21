from norman_objects.norman_base_model import NormanBaseModel


class ModelTag(NormanBaseModel):
    model_id: str = "0"
    tag_name: str
    tag_count: int = 1
