import http
from typing import Any

from starlette import status


class VeripropsException(Exception):
    def __init__(self, message: str = None, code: str = "00"):
        self.message = message
        self.code = code
        
        super().__init__(self.message)


class NoActiveSessionException(VeripropsException):
    def __init__(self, message: str = None):
        self.message = message if message else 'Your session has expired'

class AuthenticationException(VeripropsException):
    def __init__(self, message: str = None):
        self.message = message if message else 'Authentication failed'
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.code = "authentication_failed"

        super().__init__(self.message, self.code)

class TokenException(VeripropsException):
    def __init__(self, message: str = None):
        self.message = message if message else 'Token is invalid or has expired'
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.code = "validation_failed"

        super().__init__(self.message, self.code)

class TemplateRenderingException(VeripropsException):
    def __init__(self, message: str = None):
        self.message = message if message else 'Template exception'

        super().__init__(self.message)


class InvalidPayloadException(VeripropsException):
    def __init__(self, message: str = None):
        self.message = message if message else 'Template exception'

        super().__init__(self.message)


class EntityNotFoundException(VeripropsException):
    def __init__(self, entity_name: str, entity_id: Any, entity_id_name='ID'):
        self.message = f"No {entity_name} found with {entity_id_name} '{entity_id}'"


class DBOperationalException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"


class FatalException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"


class DataVersionException(VeripropsException):
    def __init__(self, table_name: str):
        self.message = f"Version mismatch for table '{table_name}'"


class TransactionException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"


class ValidationException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"

class UnallowedBehaviourException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"

class BusinessValidationException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"

class NotImplementedException(VeripropsException):
    def __init__(self, message: str):
        self.message = f"{message}"

class Social0AuthExistsException(VeripropsException):
    def __init__(self, message: str, data: Any):
        self.message = message
        self.data = data

        super().__init__(code="45")

class Social0AuthNotExistsException(VeripropsException):
    def __init__(self, message: str, data: Any):
        self.message = message
        self.data = data

        super().__init__(code="44")


class EntityConstrainException(VeripropsException):
    def __init__(self, entity_name: Any, obj: Any, exc: Any):
        self.message = f"{entity_name} with '{obj}' already exists {exc}"
