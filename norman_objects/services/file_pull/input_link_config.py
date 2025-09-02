from norman_objects.services.file_pull.model_link_config import ModelLinkConfig


class InputLinkConfig(ModelLinkConfig):
    signature_id: str
    invocation_id: str
    input_id: str
