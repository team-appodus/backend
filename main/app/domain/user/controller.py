from fastapi import APIRouter
from kink import di
from starlette import status

from main.app.domain.user.models import QueryUserDto, CreateUserDto
from main.app.domain.user.service import UserService

user_router = APIRouter(prefix="/users", tags=["Users"])

user_service: UserService = di[UserService]


@user_router.post("/", summary='Create user', response_model=QueryUserDto,
                  status_code=status.HTTP_201_CREATED)
async def user_create(
        dto: CreateUserDto
) -> QueryUserDto:
    return await user_service.create_user(dto)
