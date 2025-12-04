from enum import Enum


class QuotaType(str, Enum):
    """
    Enumeration of all supported quota types.

    **Values**

    - **Base** — Default quota assigned to an account.
    - **Accrued** — Quota accumulated over time as a reward or rollover.
    - **Pre_purchased** — Quota purchased in advance.
    - **On_demand** — Quota allocated dynamically during system usage.
    """
    Base = "Base"
    Accrued = "Accrued"
    Pre_purchased = "Pre_purchased"
    On_demand = "On_demand"

