from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status


class HTTPError(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "HTTP error"

    def __init__(self, detail: str | None = None):
        if detail is not None:
            self.detail = detail


class UnauthorizedError(HTTPError):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, email: str = "mail"):
        self.detail = f"Incorrect password for email - {email}"


class RefreshTokenRevokedError(HTTPError):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self):
        self.detail = "Refresh token revoked"


class RoleForbiddenError(HTTPError):
    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self):
        self.detail = "insufficient access rights"


class AlreadyExistsError(HTTPError):
    status_code = status.HTTP_409_CONFLICT

    def __init__(self, name: str = "Entity"):
        self.detail = f"{name} already exists"


class NotFoundError(HTTPError):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, name: str = "Entity"):
        self.detail = f"{name} not found"


class DeleteError(HTTPError):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, name: str = "Entity"):
        self.detail = f"{name} still exists"


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPError)
    async def http_error_handler(
        request: Request,  # noqa
        exc: HTTPError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
            },
        )
