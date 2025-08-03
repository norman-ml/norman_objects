from enum import Enum


class QuotaType(str, Enum):
    BASE = "BASE"
    ACCRUED = "ACCRUED"
    PRE_PURCHASED = "PRE_PURCHASED"
    ON_DEMAND = "ON_DEMAND"
