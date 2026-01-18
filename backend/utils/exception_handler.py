from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status


class HTTPError(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "HTTP error"

    def __init__(self, detail: str | None = None):
        if detail is not None:
            self.detail = detail


class AlreadyExistsError(HTTPError):
    status_code = status.HTTP_409_CONFLICT

    def __init__(self, name: str = "Entity"):
        self.detail = f"{name} already exists"


class NotFoundError(HTTPError):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, name: str = "Entity"):
        self.detail = f"{name} not found"


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
