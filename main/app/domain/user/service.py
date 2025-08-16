from logging import Logger

from appodus_utils.decorators.decorate_all_methods import decorate_all_methods
from appodus_utils.decorators.method_trace_logger import method_trace_logger
from appodus_utils.decorators.transactional import transactional
from appodus_utils.domain.user.models import QueryUserDto
from appodus_utils.domain.user.service import UserService
from fastapi.encoders import jsonable_encoder
from kink import inject, di

logger: Logger = di['logger']


@inject
@decorate_all_methods(transactional(), exclude=['get_account_security_messages'])
@decorate_all_methods(method_trace_logger, exclude=['get_account_security_messages'])
class UserService(UserService):

    async def post_create_user(self, created_user: QueryUserDto):
        """
        Use to handle all post user creation operations like, settings and profile creation. Please override

        :param created_user:
        :return:
        """
        pass

    async def combine_profile_data(self, user: QueryUserDto):
        """
        Use to combine user and profile data for return user details after successful auth

        :param user:
        :return:
        """
        user_data = jsonable_encoder(user)
        return user_data
