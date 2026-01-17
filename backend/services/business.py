from pydantic import EmailStr

from backend.domain.business import Business, BusinessRepository, Status
from backend.factories.business import get_business_repository
from backend.schemas.business import BusinessCreate, BusinessDelete
from backend.security import hash_password


class BusinessService:
    def __init__(self, repository: BusinessRepository = get_business_repository()):
        self.repository = repository

    async def get_by_email(
        self,
        email: EmailStr,
    ) -> Business | None:
        return await self.repository.get_by_email(str(email))

    async def get_all(
        self,
    ) -> list[Business | None]:
        return await self.repository.get_all()

    async def create(
        self,
        data: BusinessCreate,
    ) -> Business:
        existing = await self.repository.get_by_email(str(data.email))
        if existing:
            raise ValueError("Email already registered")

        account = Business(
            email=str(data.email),
            password_hash=hash_password(data.password_hash),
        )
        return await self.repository.create(account)

    async def delete(
        self,
        data: BusinessDelete,
    ) -> Business:
        existing = await self.repository.get_by_email(str(data.email))
        if not existing:
            raise ValueError("Business doesn't exist")

        existing.status = Status.SUSPENDED
        return await self.repository.update(existing)
