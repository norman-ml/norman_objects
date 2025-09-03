from typing import Optional

from norman_objects.shared.accounts.account import Account


class AccountProfile(Account):
    email: Optional[str] = None
