from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.norman_base_message import NormanBaseMessage


class FileMessage(NormanBaseMessage):
    file_properties: FileProperties
