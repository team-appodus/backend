from appodus_utils.exception.exceptions import ResourceNotFoundException
from kink import inject

from main.app.domain.project.staging.repo import ProjectStagingRepo


@inject
class ProjectStagingValidator:
    def __init__(self, project_staging_repo: ProjectStagingRepo):
        self._project_staging_repo = project_staging_repo


    async def should_exist_by_id(self, _id: str):
        if not (await self._project_staging_repo.exists_by_id(_id)):
            raise ResourceNotFoundException("Project Staging")
