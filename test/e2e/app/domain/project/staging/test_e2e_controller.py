import unittest

from main.app.config.settings import settings  # Very import! Load settings before importing from appodus_utils
from appodus_utils.common.client_utils import ClientUtils



from main.app.config.bootstrap import bootstrap_di
from main.app.domain.project.staging.models import ProjectStaging, UpsertProjectStagingDto

bootstrap_di()
from appodus_utils.db.session import close_db_engine


from appodus import app
from appodus_utils.test.appodus_test_utils import TestUtils
from starlette import status

class TestProjectStagingController(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):

        self.client = TestUtils.get_app_test_client(app=app)
        self.endpoint = "/v1/projects/staging"

        self.project_staging_dto = UpsertProjectStagingDto(
            fullname="Kingsley Ezenwere",
            email="kingsley.ezenwere@gmail.com",
            phone="2347039018727",
            company_name="Appodus Technologies Limited"
        )

    async def asyncTearDown(self):
        await self._truncate_tables()
        await self.client.aclose()
        await close_db_engine()

    @staticmethod
    async def _truncate_tables():
        await TestUtils.truncate_entities([ProjectStaging])

    async def test_upsert_project_staging(self):
        # Prepare
        headers = ClientUtils.create_auth_headers(
            client_id=settings.APPODUS_CLIENT_ID,
            client_secret=settings.APPODUS_CLIENT_SECRET,
            method="post",
            path=self.endpoint,
            body=self.project_staging_dto.model_dump()
        )

        # Act
        response = await self.client.post(f"{self.endpoint}/",
                                          json=self.project_staging_dto.model_dump(),
                                          headers=headers,
                                          follow_redirects=True
                                          )

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.json())
