from enum import Enum


class QuotaType(str, Enum):
    Base = "Base"
    Accrued = "Accrued"
    Pre_purchased = "Pre_purchased"
    On_demand = "On_demand"
