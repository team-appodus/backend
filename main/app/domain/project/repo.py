from typing import Type

from appodus_utils.db.repo import GenericRepo
from kink import inject
from sqlalchemy.ext.asyncio import AsyncSession

from main.app.domain.project.models import Project, CreateProjectDto, UpdateProjectDto, SearchProjectDto, QueryProjectDto


@inject
class ProjectRepo(GenericRepo[Project, CreateProjectDto, UpdateProjectDto, QueryProjectDto, SearchProjectDto]):
    def __init__(self, db: AsyncSession, model: Type[Project] = Project, query_dto: Type[QueryProjectDto] = QueryProjectDto):
        super().__init__(db, model, query_dto)
        self.db = db
