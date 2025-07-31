from contextlib import asynccontextmanager
from logging import Logger

from libre_fastapi_jwt.exceptions import AuthJWTException
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from main.app.config.settings import settings  # Very import! Load settings before importing from appodus_utils
from main.app.config.bootstrap import bootstrap_di
from main.app.domain import appodus_router

bootstrap_di()
from main.app.db.seeder import DataSeeder

from appodus_utils.db.session import close_db_engine
from appodus_utils.domain.client.controller import client_router
from appodus_utils.exception.exception_handlers import (
    appodus_exception_handler,
    http_error_handler,
    validation_exception_handler,
    generic_exception_handler,
    authjwt_exception_handler
)
from appodus_utils.exception.exceptions import AppodusBaseException
from appodus_utils.middleware.db_session_middleware import DBSessionMiddleware
from appodus_utils.middleware.request_logging_middleware import RequestLoggingMiddleware
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from httpx import AsyncClient
from kink import di
from starlette.exceptions import HTTPException as StarletteHTTPException


logger: Logger = di['logger']
data_seeder: DataSeeder = DataSeeder()
httpx_client: AsyncClient = di[AsyncClient]


@asynccontextmanager
async def lifespan_event(app: FastAPI):
    logger.debug("Running lifespan..")

    # Seed data
    await data_seeder.run_data_seed()

    logger.debug("Done running lifespan")
    yield
    logger.debug(f"Shutting down {settings.APP_NAME}...")
    await close_db_engine()
    await httpx_client.aclose()
    logger.debug(f"{settings.APP_NAME} is shutdown")


fast_api_app = FastAPI(lifespan=lifespan_event)

# Routers
fast_api_app.include_router(client_router)
fast_api_app.include_router(appodus_router)
# fast_api_app.include_router(webhook_router)

# Exception Handlers
# Custom appodus exceptions
fast_api_app.add_exception_handler(AppodusBaseException, appodus_exception_handler)
# AuthJWTException
fast_api_app.add_exception_handler(AuthJWTException, authjwt_exception_handler)
# FastAPI built-in ones
fast_api_app.add_exception_handler(StarletteHTTPException, http_error_handler)
fast_api_app.add_exception_handler(RequestValidationError, validation_exception_handler)
# Catch-all fallback
fast_api_app.add_exception_handler(Exception, generic_exception_handler)
#
# # Middlewares
# app.add_middleware(ClientAuthMiddleware)
fast_api_app.add_middleware(DBSessionMiddleware)
fast_api_app.add_middleware(RequestLoggingMiddleware)


# CORS Configuration
fast_api_app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(',') if origin.strip()],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-TIMEZONE", "X-LOCALE", "X-CSRF-Token"], )



@fast_api_app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    # logger.logger.error("Starting dev server:")
    uvicorn.run(fast_api_app, host="127.0.0.1", port=8000)