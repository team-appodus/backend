from appodus_utils import RouterUtils
from appodus_utils.db.models import SuccessResponse
from fastapi import APIRouter
from kink import di
from starlette import status

from main.app.domain.project.models import CreateProjectDto, QueryProjectDto
from main.app.domain.project.service import ProjectService
from main.app.domain.project.staging.controller import project_staging_router

project_router = APIRouter(prefix="/projects", tags=["Projects"])
RouterUtils.add_routers(project_router, [project_staging_router])

project_service: ProjectService = di[ProjectService]


@project_router.post("", summary='Create project', response_model=SuccessResponse[QueryProjectDto],
                  status_code=status.HTTP_201_CREATED)
async def project_create(
        dto: CreateProjectDto
) -> SuccessResponse[QueryProjectDto]:
    return await project_service.create_project(dto)
