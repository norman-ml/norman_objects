from typing import Optional

from norman_objects.accounts.account import Account


class AccountProfile(Account):
    email: Optional[str] = None
