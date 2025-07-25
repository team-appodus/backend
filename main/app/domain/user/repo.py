from typing import Type

from kink import inject
from sqlalchemy.ext.asyncio import AsyncSession

from main.app.db.repo import GenericRepo
from main.app.domain.user.models import User, CreateUserDto, UpdateUserDto, SearchUserDto, QueryUserDto


@inject
class UserRepo(GenericRepo[User, CreateUserDto, UpdateUserDto, QueryUserDto, SearchUserDto]):
    def __init__(self, db: AsyncSession, model: Type[User] = User, query_dto: Type[QueryUserDto] = QueryUserDto):
        super().__init__(db, model, query_dto)
        self.db = db
