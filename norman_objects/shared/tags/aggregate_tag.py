from norman_objects.norman_base_model import NormanBaseModel


class AggregateTag(NormanBaseModel):
    modelBase_id: str
    name: str
    tag_count: int
