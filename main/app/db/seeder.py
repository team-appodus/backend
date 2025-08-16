from logging import Logger

from appodus_utils.decorators.decorate_all_methods import decorate_all_methods
from appodus_utils.decorators.transactional import transactional, TransactionSessionPolicy
from appodus_utils.domain.client.models import _CreateClientDto, ClientAccessRuleDto
from appodus_utils.domain.client.service import ClientService
from kink import di

from main.app.config.settings import settings

client_service: ClientService = di[ClientService]

logger: Logger = di['logger']


@decorate_all_methods(transactional(session_policy=TransactionSessionPolicy.ALWAYS_NEW), exclude=['__init__'])
class DataSeeder:
    def __init__(self):
        self.seeded = False

    @staticmethod
    async def _seed_clients():
        if not await client_service.client_exists(settings.APPODUS_CLIENT_ID):
            create_client_dto = _CreateClientDto(
                name="Nigeria",
                description="Lagos",
                id=settings.APPODUS_CLIENT_ID,
                client_secret=settings.APPODUS_CLIENT_SECRET,
                access_rules=ClientAccessRuleDto(
                    allowed_ips=["127.0.0.1"],
                    allowed_origins=[],
                    allowed_domains=["localhost"]
                )
            )

            await client_service.seed_client(create_client_dto)

    async def run_data_seed(self):
        if self.seeded:
            return

        # await self._seed_clients()

        self.seeded = True
