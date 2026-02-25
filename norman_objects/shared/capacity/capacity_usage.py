from norman_objects.norman_base_model import NormanBaseModel


class CapacityUsage(NormanBaseModel):
    account_id: str
    model_id: str
    version_id: str
    machine_type: str
    capacity: int
    active: bool