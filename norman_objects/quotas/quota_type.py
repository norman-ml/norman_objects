from enum import Enum


class QuotaType(str, Enum):
    BASE = "Base"
    ACCRUED = "Accrued"
    PRE_PURCHASED = "Pre_purchased"
    ON_DEMAND = "On_demand"
