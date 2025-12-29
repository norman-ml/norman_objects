from contextvars import ContextVar
from typing import Optional, Callable

from norman_objects.shared.authorization.jwt_token import JwtToken


class NormanPathContext:
    __asset_bucket_getter: ContextVar[Optional[Callable[[], str]]] = ContextVar("norman_asset_bucket_getter")
    __data_bucket_getter: ContextVar[Optional[Callable[[], str]]]= ContextVar("norman_data_bucket_getter")
    __mountpoint_getter: ContextVar[Optional[Callable[[], str]]] = ContextVar("norman_mountpoint_getter")

    @staticmethod
    def get_asset_bucket():
        asset_bucket_getter = NormanPathContext.__asset_bucket_getter.get()
        if asset_bucket_getter is None:
            raise ValueError("Path context asset bucket getter not provided")

        asset_bucket_name = asset_bucket_getter()
        return asset_bucket_name

    @staticmethod
    def get_data_bucket():
        data_bucket_getter = NormanPathContext.__data_bucket_getter.get()
        if data_bucket_getter is None:
            raise ValueError("Path context data bucket getter not provided")

        data_bucket_name = data_bucket_getter()
        return data_bucket_name

    @staticmethod
    def get_mountpoint():
        mountpoint_getter = NormanPathContext.__mountpoint_getter.get()
        if mountpoint_getter is None:
            raise ValueError("Path context mountpoint getter not provided")

        mountpoint = mountpoint_getter()
        return mountpoint

    @staticmethod
    def set_asset_bucket_getter(asset_bucket_getter: Callable[[], str]):
        NormanPathContext.__asset_bucket_getter.set(asset_bucket_getter)

    @staticmethod
    def set_data_bucket_getter(data_bucket_getter: Callable[[], str]):
        NormanPathContext.__data_bucket_getter.set(data_bucket_getter)

    @staticmethod
    def set_mountpoint_getter(mountpoint_getter: Callable[[], str]):
        NormanPathContext.__mountpoint_getter.set(mountpoint_getter)

    @staticmethod
    def clear():
        NormanPathContext.__asset_bucket_getter.set(None)
        NormanPathContext.__data_bucket_getter.set(None)
        NormanPathContext.__mountpoint_getter.set(None)
