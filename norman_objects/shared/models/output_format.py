from enum import Enum


class OutputFormat(str, Enum):
    Binary = "Binary"
    Json = "Json"
    Text = "Text"
