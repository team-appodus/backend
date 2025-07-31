from kink import inject

from main.app.domain.project.repo import ProjectRepo


@inject
class ProjectValidator:
    def __init__(self, project_repo: ProjectRepo):
        self._project_repo = project_repo
