import time
from contextlib import asynccontextmanager
from logging import Logger
from uuid import uuid4

import uvicorn
from main.app.config.settings import settings  # Very import! Load settings before importing from appodus_utils
from appodus_utils.db.session import close_db_engine, create_new_db_session
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from httpx import AsyncClient
from kink import di
from libre_fastapi_jwt.exceptions import AuthJWTException

from main.app.config.bootstrap import bootstrap_di
from main.app.domain.user.controller import user_router
from main.app.exception.exception_handlers import generic_exception_handler, authentication_exception_handler, \
    validation_exception_handler, token_exception_handler
from main.app.exception.exceptions import AuthenticationException, TokenException

bootstrap_di()

logger: Logger = di['logger']
httpx_client: AsyncClient = di[AsyncClient]


@asynccontextmanager
async def lifespan_event(app: FastAPI):
    logger.debug("Running lifespan..")

    # Seed data

    # Initialize other services
    # cost_tracker.load_rates_from_db()  # Would implement this
    logger.debug("Done running lifespan")
    yield
    logger.debug("Shutting down veriprops...")
    await close_db_engine()
    await httpx_client.aclose()
    logger.debug("Veriprops is shutdown")


app = FastAPI(lifespan=lifespan_event)

# Routers
app.include_router(user_router)

# Exception Handlers
app.add_exception_handler(AuthenticationException, authentication_exception_handler)
app.add_exception_handler(TokenException, token_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request_id = str(uuid4())
    start_time = time.time()

    logger.info(f"[{request_id}] Incoming request: {request.method} {request.url.path}")

    async with create_new_db_session():
        try:

            response = await call_next(request)

        finally:
            duration = time.time() - start_time
            logger.debug(f"[{request_id}] DB session context reset.")
            logger.info(f"[{request_id}] Request completed in {duration:.3f}s")

    return response


# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(',') if origin.strip()],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-TIMEZONE", "X-LOCALE", "X-CSRF-Token"], )


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    # logger.logger.error("Starting dev server:")
    uvicorn.run(app, host="127.0.0.1", port=8001)
