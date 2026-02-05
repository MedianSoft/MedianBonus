from app.domain.business import Business, BusinessRepository
from app.domain.employee import Employee, EmployeeRepository
from app.schema.auth import AuthLoginRequest, TokenResponse
from app.security.password import access_security, pwd_context, refresh_security
from app.util.exception_handler import UnauthorizedError


class AuthService:
    def __init__(
        self,
        business_repository: "BusinessRepository",
        employee_repository: "EmployeeRepository",
    ):
        self.business_repository = business_repository
        self.employee_repository = employee_repository

    async def get_user_role_by_email(self, data: "AuthLoginRequest") -> tuple[Business | Employee | None, str | None]:
        user: Business | Employee | None = None
        role: str | None = None
        business = await self.business_repository.get_by_email(email=data.email)
        if business and pwd_context.verify(data.password, business.password_hash):
            user, role = business, "business"

        employee = await self.employee_repository.get_by_email(email=data.email)
        if employee and pwd_context.verify(data.password, employee.password_hash):
            user, role = employee, "employee"

        return user, role

    async def get_jwt_token(self, data: "AuthLoginRequest") -> TokenResponse:
        user, role = await self.get_user_role_by_email(data=data)
        if user is None:
            raise UnauthorizedError(email=data.email)

        subject = {
            "user_id": str(user.id),
            "user_email": user.email,
            "username": user.name,
            "role": role,
        }

        access_token = access_security.create_access_token(subject=subject)
        refresh_token = refresh_security.create_refresh_token(subject=subject)

        return TokenResponse(access_token=access_token, refresh_token=refresh_token)
