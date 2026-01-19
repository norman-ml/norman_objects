from norman_objects.norman_base_model import NormanBaseModel


class AccountCapacity(NormanBaseModel):
    id: str = "0"
    account_id: str
    machine_type: str
    capacity: int