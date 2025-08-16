from main.app.config.settings import settings
from main.app.config.bootstrap import DiBootstrap

from main.app.domain.user.controller import ext_user_router

from appodus_utils import RouterUtils
from fastapi import APIRouter

from main.app.domain.project.controller import project_router

appodus_router = APIRouter(prefix="/v1", tags=["Appodus"])

RouterUtils.add_routers(appodus_router, [
    project_router, ext_user_router
])