from backend.domain.business import Business, BusinessRepository, Status
from backend.factories.business import get_business_repository
from backend.schemas.business import (
    BusinessCreateRequest,
    BusinessDeleteRequest,
    BusinessGetByEmailRequest,
    BusinessGetByIDRequest,
    BusinessListResponse,
    BusinessResponse,
)
from backend.security import hash_password


class BusinessService:
    def __init__(self, repository: BusinessRepository = get_business_repository()):
        self.repository = repository

    async def create(
        self,
        data: BusinessCreateRequest,
    ) -> BusinessResponse:
        existing = await self.repository.get_by_email(str(data.email))
        if existing:
            raise ValueError("Email already registered")
        account = Business(
            name=data.name,
            email=str(data.email),
            password_hash=hash_password(data.password_hash),
        )
        result = await self.repository.create(account)
        return BusinessResponse.model_validate(result)

    async def delete(
        self,
        data: BusinessDeleteRequest,
    ) -> BusinessResponse | None:
        existing = await self.repository.get_by_email(str(data.email))
        if not existing:
            raise ValueError("Business doesn't exist")
        existing.status = Status.SUSPENDED
        result = await self.repository.update(existing)
        return BusinessResponse.model_validate(result)

    async def get_by_email(
        self,
        data: BusinessGetByEmailRequest,
    ) -> BusinessResponse | None:
        result = await self.repository.get_by_email(str(data.email))
        return BusinessResponse.model_validate(result)

    async def get_by_id(
        self,
        data: BusinessGetByIDRequest,
    ) -> BusinessResponse | None:
        result = await self.repository.get_by_id(data.id)
        return BusinessResponse.model_validate(result)

    async def get_all(
        self,
    ) -> BusinessListResponse:
        result = await self.repository.get_all()
        return BusinessListResponse(
            businesses=[
                BusinessResponse.model_validate(business) for business in result
            ]
        )
