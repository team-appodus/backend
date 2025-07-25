import traceback
from logging import Logger
from typing import Union

from fastapi.exceptions import RequestValidationError
from kink import di
from sqlalchemy.exc import OperationalError, StatementError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from main.app.exception.exceptions import EntityNotFoundException, DBOperationalException, AuthenticationException, \
    TokenException

logger: Logger = di["logger"]

def create_error_response(status_code: int, message: str, code: str = "error", details: dict = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": message,
            "code": code,
            "details": details or {},
        }
    )

async def authentication_exception_handler(request: Request, exc: AuthenticationException):
    logger.warning(f"AppException: {exc}")
    return create_error_response(exc.status_code, exc.message, exc.code)

async def token_exception_handler(request: Request, exc: TokenException):
    logger.warning(f"AppException: {exc}")
    return create_error_response(exc.status_code, exc.message, exc.code)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"ValidationError: {exc.errors()}")
    return create_error_response(
        status_code=422,
        message="Validation Failed",
        code="validation_error",
        details={"errors": exc.errors()}
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {traceback.format_exc()}")
    return create_error_response(
        status_code=500,
        message="Internal Server Error",
        code="internal_server_error"
    )

async def entity_not_found_exception_handler(request: Request, exc: Union[EntityNotFoundException]):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.message}."},
    )


def handle_exceptions(exc: Exception):
    if isinstance(exc, OperationalError):
        message = exc.orig.args[0]
        raise DBOperationalException(message)
    if isinstance(exc, StatementError):
        message = exc.orig.args[0]
        raise DBOperationalException(message)
    else:
        message = exc.args[0]
        raise DBOperationalException(message)
