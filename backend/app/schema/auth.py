from pydantic import BaseModel

from backend.schema.base import BaseRequest


class AuthLoginRequest(BaseRequest):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"