from enum import Enum


class Severity(str, Enum):
    """
    Enumeration of notification importance levels.

    These levels categorize how the client (UI or APIs) should present
    the message to the user.

    **Values**

    - **Error** — A failure or critical issue requiring user attention.
    - **Info** — Neutral informational update.
    - **Success** — Positive event, confirmation, or completion notice.
    - **Warning** — Non-critical issue or cautionary event.
    """
    Error = "Error"
    Info = "Info"
    Success = "Success"
    Warning = "Warning"

