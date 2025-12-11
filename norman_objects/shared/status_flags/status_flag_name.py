from enum import Enum


class StatusFlagName(str, Enum):
    Logo_EFS_Staging = "Logo_EFS_Staging"
    Logo_S3_Storage = "Logo_S3_Storage"

    File_EFS_Staging = "File_EFS_Staging"
    File_S3_Storage = "File_S3_Storage"
    File_Model_Deploy = "File_Model_Deploy"

    Input_EFS_Staging = "Input_EFS_Staging"
    Input_S3_Storage = "Input_S3_Storage"
    Input_EFS_Transcoding = "Input_EFS_Transcoding"
    Input_EFS_Tensor = "Input_EFS_Tensor"

    Model_Function_Run = "Model_Function_Run"

    Output_EFS_Staging = "Output_EFS_Staging"
    Output_S3_Storage = "Output_S3_Storage"
