from enum import Enum


class FunctionStateReasonsCodes(str, Enum):
    Creating = "Creating"
    Restoring = "Restoring"

    Idle = "Idle"

    DisabledKMSKey = "DisabledKMSKey"
    EFSIOError = "EFSIOError"
    EFSMountConnectivityError = "EFSMountConnectivityError"
    EFSMountFailure = "EFSMountFailure"
    EFSMountTimeout = "EFSMountTimeout"
    EniLimitExceeded = "EniLimitExceeded"
    FunctionError = "FunctionError"
    ImageAccessDenied = "ImageAccessDenied"
    ImageDeleted = "ImageDeleted"
    InsufficientRolePermissions = "InsufficientRolePermissions"
    InternalError = "InternalError"
    InvalidConfiguration = "InvalidConfiguration"
    InvalidImage = "InvalidImage"
    InvalidRuntime = "InvalidRuntime"
    InvalidSecurityGroup = "InvalidSecurityGroup"
    InvalidStateKMSKey = "InvalidStateKMSKey"
    InvalidSubnet = "InvalidSubnet"
    InvalidZipFileException = "InvalidZipFileException"
    KMSKeyAccessDenied = "KMSKeyAccessDenied"
    KMSKeyNotFound = "KMSKeyNotFound"
    SubnetOutOfIPAddresses = "SubnetOutOfIPAddresses"

    Unknown = "Unknown"
