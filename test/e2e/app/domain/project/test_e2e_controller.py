import unittest

from kink import di

from main.app.config.settings import settings  # Very import! Load settings before importing from appodus_utils
from main.app.config.bootstrap import bootstrap_di

bootstrap_di()
from appodus_utils.common.client_utils import ClientUtils

from appodus_utils.decorators.transactional import transactional, TransactionSessionPolicy
from main.app.domain.project.models import CreateProjectDto
from main.app.domain.project.staging.models import ProjectStaging, UpsertProjectStagingDto, QueryProjectStagingDto
from main.app.domain.project.staging.service import ProjectStagingService
from appodus_utils.db.session import close_db_engine


from appodus import app
from appodus_utils.test.appodus_test_utils import TestUtils
from starlette import status

class TestProjectController(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):

        self.client = TestUtils.get_app_test_client(app=app)
        self.endpoint = "/v1/projects"

        self.project_dto = CreateProjectDto(
            fullname="Kingsley Ezenwere",
            email="kingsley.ezenwere@gmail.com",
            phone="2347039018727",
            company_name="Appodus Technologies Limited",

            budget_range="NGN50M",
            timeline="ASAP",

            what_building="We're building a flying car",
            what_not_building="It's a car not a plane, it's not going to have a wing",
            build_summary="ai generated build summary",
            customer_location="NIGERIA",

            build_type="New build",
            platform="Both",
            post_production_support="yes",  # -1=not-sure, 0=no, 1=yes
            staging_id="staging_id"
        )

    async def asyncTearDown(self):
        await self._truncate_tables()
        await self.client.aclose()
        await close_db_engine()

    @staticmethod
    async def _truncate_tables():
        await TestUtils.truncate_entities([ProjectStaging])

    @transactional(session_policy=TransactionSessionPolicy.ALWAYS_NEW)
    async def  _create_project_staging(self) -> QueryProjectStagingDto:
        project_staging_service: ProjectStagingService = di[ProjectStagingService]
        create_project_staging_dto = UpsertProjectStagingDto(**self.project_dto.model_dump(exclude={"staging_id"}))
        response = await project_staging_service.upsert_project_staging(obj_in=create_project_staging_dto)

        return response.data

    async def test_upsert_project_staging(self):
        # Prepare
        project_staging = await self._create_project_staging()
        self.project_dto.staging_id = project_staging.id

        headers = ClientUtils.create_auth_headers(
            client_id=settings.APPODUS_CLIENT_ID,
            client_secret=settings.APPODUS_CLIENT_SECRET,
            method="post",
            path=self.endpoint,
            body=self.project_dto.model_dump()
        )

        # Act
        response = await self.client.post(f"{self.endpoint}",
                                          json=self.project_dto.model_dump(),
                                          headers=headers,
                                          follow_redirects=True
                                          )

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("data", response.json())
