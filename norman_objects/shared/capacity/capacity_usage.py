from norman_objects.norman_base_model import NormanBaseModel


class CapacityUsage(NormanBaseModel):
    version_id: str
    model_id: str
    account_id: str
    machine_type: str
    capacity: int
    active: bool