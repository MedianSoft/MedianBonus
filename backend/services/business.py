from backend.domain.business import Business, BusinessRepository, BusinessStatus
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
from backend.utils.exception_handler import AlreadyExistsError, NotFoundError


class BusinessService:
    def __init__(self, repository: BusinessRepository = get_business_repository()):
        self.repository = repository

    async def create(self, data: BusinessCreateRequest) -> BusinessResponse:
        existing = await self.repository.get_by_email(str(data.email))
        if existing:
            raise AlreadyExistsError("Email")

        business = Business(
            name=data.name,
            email=str(data.email),
            password_hash=hash_password(data.password),
        )
        result = await self.repository.create(business)

        return BusinessResponse.model_validate(result)

    async def delete(self, data: BusinessDeleteRequest) -> BusinessResponse | None:
        existing = await self.repository.get_by_email(str(data.email))
        if not existing:
            raise NotFoundError("Business")

        existing.status = BusinessStatus.SUSPENDED
        result = await self.repository.update(existing)

        return BusinessResponse.model_validate(result)

    async def get_by_email(self, data: BusinessGetByEmailRequest) -> BusinessResponse | None:
        result = await self.repository.get_by_email(str(data.email))
        if not result:
            raise NotFoundError("Business")

        return BusinessResponse.model_validate(result)

    async def get_by_id(self, data: BusinessGetByIDRequest) -> BusinessResponse | None:
        result = await self.repository.get_by_id(data.id)
        if not result:
            raise NotFoundError("Business")

        return BusinessResponse.model_validate(result)

    async def get_all(self) -> BusinessListResponse:
        result = await self.repository.get_all()
        if not result:
            raise NotFoundError("Businesses")

        return BusinessListResponse(businesses=[BusinessResponse.model_validate(business) for business in result])
