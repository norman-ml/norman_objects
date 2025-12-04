from enum import Enum


class StatusFlagName(str, Enum):
    """
    Enumeration of all workflow steps tracked in the Norman system.

    Each entry represents a discrete stage in model processing,
    file lifecycle, EFS/S3 handling, input preparation, output handling,
    or execution.

    **Groups of Flags**

    - **Logo / Branding Asset Handling**
      - `Logo_EFS_Staging`
      - `Logo_S3_Storage`

    - **File Preparation & Staging**
      - `File_EFS_Staging`
      - `File_S3_Storage`
      - `File_Image_Build`

    - **Input Processing**
      - `Input_EFS_Staging`
      - `Input_S3_Storage`
      - `Input_EFS_Transcoding`
      - `Input_EFS_Tensor`

    - **Model Execution**
      - `Model_Function_Run`

    - **Output Handling**
      - `Output_EFS_Staging`
      - `Output_S3_Storage`
    """
    Logo_EFS_Staging = "Logo_EFS_Staging"
    Logo_S3_Storage = "Logo_S3_Storage"

    File_EFS_Staging = "File_EFS_Staging"
    File_S3_Storage = "File_S3_Storage"
    File_Image_Build = "File_Image_Build"

    Input_EFS_Staging = "Input_EFS_Staging"
    Input_S3_Storage = "Input_S3_Storage"
    Input_EFS_Transcoding = "Input_EFS_Transcoding"
    Input_EFS_Tensor = "Input_EFS_Tensor"

    Model_Function_Run = "Model_Function_Run"

    Output_EFS_Staging = "Output_EFS_Staging"
    Output_S3_Storage = "Output_S3_Storage"
