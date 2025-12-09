from enum import Enum


class SignatureType(str, Enum):
    """
    Identifies whether a signature represents input data or output data.

    **Values**

    - Input
    - Output
    """
    Input = "Input"
    Output = "Output"
