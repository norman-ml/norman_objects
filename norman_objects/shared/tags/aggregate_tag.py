from norman_objects.norman_base_model import NormanBaseModel


class AggregateTag(NormanBaseModel):
    model_base_id: str
    tag_name: str
    tag_count: int
