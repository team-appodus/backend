from appodus_utils.db.models import SuccessResponse
from fastapi import APIRouter
from kink import di
from starlette import status

from main.app.domain.project.staging.models import QueryProjectStagingDto, UpsertProjectStagingDto
from main.app.domain.project.staging.service import ProjectStagingService

project_staging_router = APIRouter(prefix="/staging", tags=["Project Staging"])

project_staging_service: ProjectStagingService = di[ProjectStagingService]


@project_staging_router.post("/", summary='Create or Update Project Staging', response_model=SuccessResponse[QueryProjectStagingDto],
                  status_code=status.HTTP_200_OK)
async def upsert_project_staging(
        dto: UpsertProjectStagingDto
) -> SuccessResponse[QueryProjectStagingDto]:
    return await project_staging_service.upsert_project_staging(dto)
