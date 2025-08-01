# from aiocache import Cache
from typing import Type, List

import redis
from httpx import AsyncClient

from main.app.config.settings import settings
from appodus_utils.config.logger import LoggerFactory
from kink import di
from libre_fastapi_jwt import AuthJWTBearer
from redis import Redis

bootstrap_di_called = False


def bootstrap_di() -> None:
    global bootstrap_di_called

    if bootstrap_di_called:
        return

    # di[Cache] = lambda _di: Cache(Cache.REDIS, endpoint=settings.REDIS_HOST, port=settings.REDIS_PORT)
    di[Redis] = lambda _di: redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        username=settings.REDIS_USERNAME
    ) if settings.REDIS_ENABLED else {}

    di['logger'] = lambda _di: LoggerFactory().get_logger()
    di[AuthJWTBearer] = lambda _di: AuthJWTBearer()
    di[AsyncClient] =  lambda _di: AsyncClient()

    bootstrap_di_called = True


def register_all_subclasses(base_cls: Type):
    instances = _get_all_subclasses_instances(base_cls)

    di[List[base_cls]] = instances
    return instances

def _get_all_subclasses_instances(base_cls: Type):
    subclasses: List = base_cls.__subclasses__()
    instances = []
    for subclass in subclasses:
        other_subclasses = subclass.__subclasses__()
        if len(other_subclasses) > 0:
           _instances = _get_all_subclasses_instances(subclass)
           instances.extend(_instances)
        else:
            instance = di[subclass]  # Use DI container to resolve dependencies
            instances.append(instance)

    return instances
