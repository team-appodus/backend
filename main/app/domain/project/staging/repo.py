from typing import Type, Optional

from appodus_utils.db.repo import GenericRepo
from kink import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from main.app.domain.project.staging.models import ProjectStaging, UpsertProjectStagingDto, UpdateProjectStagingDto, QueryProjectStagingDto, SearchProjectStagingDto


@inject
class ProjectStagingRepo(GenericRepo[ProjectStaging, UpsertProjectStagingDto, UpdateProjectStagingDto, QueryProjectStagingDto, SearchProjectStagingDto]):
    def __init__(self, db: AsyncSession, model: Type[ProjectStaging] = ProjectStaging, query_dto: Type[QueryProjectStagingDto] = QueryProjectStagingDto):
        super().__init__(db, model, query_dto)
        self.db = db


    async def get_id_by_email_and_phone(self, email: str, phone: str) -> Optional[str]:
        stmt = select(self._model).where(
            self._model.deleted.is_(False),
            self._model.email == email,
            self._model.phone == phone
        )

        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()

        if row:
            return row.id

        return None
