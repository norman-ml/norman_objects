from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.notifications.notification import Notification

class ModelNotification(Notification):
    model_name: Optional[str] = None
    type: str = "model"