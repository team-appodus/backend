from appodus_utils.config.bootstrap import BaseDiBootstrap
from appodus_utils.domain.user.service import UserService as UtilsUserService
from kink import di

from main.app.domain.user.service import UserService

BaseDiBootstrap.register_subclass_if_exists(UtilsUserService)

# Very import, to override utils UserService
from appodus_utils.domain.user.controller import user_router
ext_user_router = user_router

user_service: UserService = di[UserService]
@ext_user_router.get("/another-user-api")
async def another_user_api():
    pass
