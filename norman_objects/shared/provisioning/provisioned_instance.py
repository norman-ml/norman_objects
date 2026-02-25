from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.provisioning.provisioned_instance_status import ProvisionedInstanceStatus


class ProvisionedInstance(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    version_id: str
    ec2_instance_id: Optional[str] = None
    status: ProvisionedInstanceStatus
