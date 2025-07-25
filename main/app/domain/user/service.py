from logging import Logger
from kink import inject, di
from main.app.domain.user.models import CreateUserDto, QueryUserDto

from main.app.domain.user.repo import UserRepo
from main.app.utils.decorators.decorate_all_methods import decorate_all_methods
from main.app.utils.decorators.method_trace_logger import method_trace_logger
from main.app.utils.decorators.transactional import transactional

logger: Logger = di['logger']

@inject
@decorate_all_methods(transactional(), exclude=['__init__', 'get_account_security_messages'], exclude_startswith='_')
@decorate_all_methods(method_trace_logger, exclude=['__init__', 'get_account_security_messages'], exclude_startswith='_')
class UserService:
    def __init__(self, user_repo: UserRepo
                 ):
        self._user_repo = user_repo

    async def create_user(self, obj_in: CreateUserDto) -> QueryUserDto:
        return await self._user_repo.create(obj_in)
