from norman_objects.norman_base_model import NormanBaseModel

class ProvisionedInstance(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    version_id: str
    instance_id: str
