import os
from datetime import timedelta

from fastapi_jwt import JwtAccessBearer, JwtRefreshBearer, JwtAuthorizationCredentials
from passlib.context import CryptContext

from backend.util.exception_handler import RefreshTokenRevokedError

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
)

JWT_SECRET = os.getenv("JWT_SECRET", default="SECRET")
access_ttl = int(os.getenv("ACCESS_TTL", default=5))
ACCESS_TTL = timedelta(minutes=access_ttl)
refresh_ttl = int(os.getenv("REFRESH_TTL", default=30))
REFRESH_TTL = timedelta(days=refresh_ttl)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

access_security = JwtAccessBearer(
    secret_key=JWT_SECRET,
    auto_error=True,
    access_expires_delta=ACCESS_TTL,
)
refresh_security = JwtRefreshBearer.from_other(
    access_security,
    auto_error=True,
    refresh_expires_delta=REFRESH_TTL,
)
revoked_refresh_jti: set[str] = set()


def ensure_refresh_not_revoked(credentials: JwtAuthorizationCredentials) -> None:
    if credentials.jti in revoked_refresh_jti:
        raise RefreshTokenRevokedError()

