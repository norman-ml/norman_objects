from norman_objects.norman_base_model import NormanBaseModel


class AggregateTag(NormanBaseModel):
    model_id: str
    name: str
    tag_count: int
