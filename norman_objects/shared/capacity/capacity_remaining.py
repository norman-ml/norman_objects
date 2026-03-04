from norman_objects.norman_base_model import NormanBaseModel


class CapacityRemaining(NormanBaseModel):
    account_id: str
    machine_type: str
    capacity: int