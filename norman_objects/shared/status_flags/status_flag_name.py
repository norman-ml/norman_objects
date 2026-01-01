from enum import Enum


class StatusFlagName(str, Enum):
    Asset_EFS_Staging = "Asset_EFS_Staging"
    Asset_S3_Storage = "Asset_S3_Storage"
    Model_Deploy = "Model_Deploy"

    Input_EFS_Staging = "Input_EFS_Staging"
    Input_S3_Storage = "Input_S3_Storage"
    Input_EFS_Transcoding = "Input_EFS_Transcoding"
    Input_EFS_Tensor = "Input_EFS_Tensor"

    Model_Function_Run = "Model_Function_Run"

    Output_EFS_Staging = "Output_EFS_Staging"
    Output_S3_Storage = "Output_S3_Storage"