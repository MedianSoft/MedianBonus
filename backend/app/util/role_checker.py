from collections.abc import Callable

from fastapi import Security
from fastapi_jwt import JwtAuthorizationCredentials

from app.security.password import access_security
from app.util.exception_handler import RoleForbiddenError


def require_roles(*required: str) -> Callable[[JwtAuthorizationCredentials], JwtAuthorizationCredentials]:
    """
    RBAC dependency:
    - проверяем access token
    - проверяем наличие хотя бы одной роли из required
    """

    def dep(
        credentials: JwtAuthorizationCredentials = Security(access_security),
    ) -> JwtAuthorizationCredentials:
        role = credentials.subject.get("role", "nobody")
        if role not in required:
            raise RoleForbiddenError()
        return credentials

    return dep
