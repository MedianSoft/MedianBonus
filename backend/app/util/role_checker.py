from fastapi import Security
from fastapi_jwt import JwtAuthorizationCredentials

from backend.api.auth import access_security
from backend.util.exception_handler import RoleForbiddenError


def require_roles(*required: str):
    """
    RBAC dependency:
    - проверяем access token
    - проверяем наличие хотя бы одной роли из required
    """

    def dep(credentials: JwtAuthorizationCredentials = Security(access_security)) -> JwtAuthorizationCredentials:
        role = credentials.subject.get("role", "nobody")
        print(role)
        if role not in required:
            raise RoleForbiddenError()
        return credentials

    return dep