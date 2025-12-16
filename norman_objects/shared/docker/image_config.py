from pydantic import BaseModel


class ImageConfig(BaseModel):
    region_name : str
    layer_name: str
    environment_name: str
    sandbox_name: str
    registry_name: str
    model_id: str
    image_version: str = "latest"

    @property
    def repository_name(self):
        return f"{self.layer_name}-{self.environment_name}-{self.sandbox_name}-{self.model_id}".lower()

    @property
    def repository_uri(self):
        return f"{self.registry_name}/{self.repository_name}".lower()

    @property
    def image_uri(self):
        return f"{self.repository_uri}:{self.image_version}".lower()
