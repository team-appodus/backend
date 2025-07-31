from main.app.config.bootstrap import bootstrap_di
from main.app.config.settings import settings  # Very import! Load settings before importing from appodus_utils

bootstrap_di()

from appodus_utils import RouterUtils
from fastapi import APIRouter

from main.app.domain.project.controller import project_router

appodus_router = APIRouter(prefix="/v1", tags=["Appodus"])

RouterUtils.add_routers(appodus_router, [
    project_router
])