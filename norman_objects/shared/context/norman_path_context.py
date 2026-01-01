from contextvars import ContextVar
from typing import Optional, Callable


class NormanPathContext:
    __mountpoint_getter: ContextVar[Optional[Callable[[], str]]] = ContextVar("norman_mountpoint_getter")

    @staticmethod
    def get_mountpoint():
        mountpoint_getter = NormanPathContext.__mountpoint_getter.get()
        if mountpoint_getter is None:
            raise ValueError("Path context mountpoint getter not provided")

        mountpoint = mountpoint_getter()
        return mountpoint

    @staticmethod
    def set_mountpoint_getter(mountpoint_getter: Callable[[], str]):
        NormanPathContext.__mountpoint_getter.set(mountpoint_getter)

    @staticmethod
    def clear():
        NormanPathContext.__mountpoint_getter.set(None)
