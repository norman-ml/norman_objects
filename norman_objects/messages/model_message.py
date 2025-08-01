from norman_objects.messages.norman_base_message import NormanBaseMessage
from norman_objects.models.model import Model


class ModelMessage(NormanBaseMessage):
    model: Model
