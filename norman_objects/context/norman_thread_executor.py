
from contextvars import copy_context
from concurrent.futures import ThreadPoolExecutor

class NormanThreadExecutor(ThreadPoolExecutor):
    def submit(self, fn, *args, **kwargs):
        ctx = copy_context()
        return super().submit(ctx.run, fn, *args, **kwargs)