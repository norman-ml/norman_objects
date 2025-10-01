from norman_objects.shared.files.file_properties import FileProperties
from norman_objects.shared.messages.norman_base_message import NormanBaseMessage


class FileMessage(NormanBaseMessage):
    file_properties: FileProperties

