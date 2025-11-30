from datetime import datetime, UTC



class NormanIntError():
    message: str
    details: dict = {}
    timestamp: datetime = datetime.now(UTC)

    def model_post_init(self, __context):
        if self.timestamp is None:
            self.timestamp = datetime.now(UTC)
