from norman_objects.services.file_pull.model_link_config import ModelLinkConfig


class OutputLinkConfig(ModelLinkConfig):
    signature_id: str
    invocation_id: str
    output_id: str
