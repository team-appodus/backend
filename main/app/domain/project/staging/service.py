from logging import Logger

from appodus_utils.db.models import SuccessResponse
from appodus_utils.decorators.decorate_all_methods import decorate_all_methods
from appodus_utils.decorators.method_trace_logger import method_trace_logger
from appodus_utils.decorators.transactional import transactional
from kink import inject, di

from main.app.domain.project.staging.models import UpsertProjectStagingDto, QueryProjectStagingDto
from main.app.domain.project.staging.repo import ProjectStagingRepo
from main.app.domain.project.staging.validator import ProjectStagingValidator

logger: Logger = di['logger']


@inject
@decorate_all_methods(transactional(), exclude=['get_account_security_messages'])
@decorate_all_methods(method_trace_logger, exclude=['get_account_security_messages'])
class ProjectStagingService:
    def __init__(self,
                 project_staging_repo: ProjectStagingRepo,
                 project_staging_validator: ProjectStagingValidator
                 ):
        self._project_staging_repo = project_staging_repo
        self._project_staging_validator = project_staging_validator

    async def upsert_project_staging(self, obj_in: UpsertProjectStagingDto) -> SuccessResponse[QueryProjectStagingDto]:
        existing_id = await self._project_staging_repo.get_id_by_email_and_phone(
            email=obj_in.email,
            phone=obj_in.phone
        )
        if existing_id:
            return await self._project_staging_repo.update(existing_id, obj_in.model_dump(exclude_none=True))

        return await self._project_staging_repo.create(obj_in)

    async def hard_delete_project_staging(self, project_staging_id: str) -> bool:
        await self._project_staging_validator.should_exist_by_id(project_staging_id)
        await self._project_staging_repo.hard_delete(project_staging_id)

        return True
