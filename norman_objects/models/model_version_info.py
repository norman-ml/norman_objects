from datetime import datetime

from norman_objects.norman_base_model import NormanBaseModel


class ModelVersionInfo(NormanBaseModel):
    id: str
    version_label: str
    creation_time: datetime
