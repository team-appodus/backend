from logging import Logger

from appodus_utils.db.models import SuccessResponse
from appodus_utils.decorators.decorate_all_methods import decorate_all_methods
from appodus_utils.decorators.method_trace_logger import method_trace_logger
from appodus_utils.decorators.transactional import transactional
from kink import inject, di

from main.app.domain.project.models import CreateProjectDto, QueryProjectDto
from main.app.domain.project.repo import ProjectRepo
from main.app.domain.project.staging.service import ProjectStagingService

logger: Logger = di['logger']

@inject
@decorate_all_methods(transactional(), exclude=['__init__', 'get_account_security_messages'], exclude_startswith='_')
@decorate_all_methods(method_trace_logger, exclude=['__init__', 'get_account_security_messages'], exclude_startswith='_')
class ProjectService:
    def __init__(self,
                 project_repo: ProjectRepo,
                 project_staging_service: ProjectStagingService
                 ):
        self._project_repo = project_repo
        self._project_staging_service = project_staging_service

    async def create_project(self, obj_in: CreateProjectDto) -> SuccessResponse[QueryProjectDto]:
        staging_id = obj_in.staging_id
        created_project_dto = await self._project_repo.create(obj_in.model_dump(exclude={"staging_id"}))

        await self._project_staging_service.hard_delete_project_staging(project_staging_id=staging_id)

        return created_project_dto
