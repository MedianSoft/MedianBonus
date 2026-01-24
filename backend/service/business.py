from typing import TYPE_CHECKING

from pydantic.v1 import EmailStr

from backend.domain.business import Business, BusinessStatus
from backend.schema.business import (
    BusinessListResponse,
    BusinessResponse,
)
from backend.security import hash_password
from backend.util.exception_handler import AlreadyExistsError, NotFoundError

if TYPE_CHECKING:
    import uuid

    from backend.domain.business import BusinessRepository
    from backend.schema.business import (
        BusinessCreateRequest,
        BusinessDeleteRequest,
        BusinessGetByEmailRequest,
        BusinessUpdateRequest,
    )


class BusinessService:
    def __init__(self, repository: "BusinessRepository"):
        self.repository = repository

    async def create(self, data: "BusinessCreateRequest") -> BusinessResponse:
        existing = await self.repository.get_by_email(str(data.email))
        if existing:
            raise AlreadyExistsError("Email")

        business = Business(
            name=data.name,
            email=str(data.email),
            password_hash=hash_password(data.password),
        )
        result = await self.repository.create(business)

        return BusinessResponse(
            id=result.id,
            email=EmailStr(result.email),
            name=result.name,
            status=result.status,
        )

    async def update(self, data: "BusinessUpdateRequest") -> BusinessResponse:
        existing = await self.repository.get(Business, data.id)
        if not existing:
            raise NotFoundError("Business")

        if data.name:
            existing.name = data.name
        if data.email:
            existing.email = str(data.email)
        if data.password:
            existing.password_hash = hash_password(data.password)

        result = await self.repository.update(existing)

        return BusinessResponse.model_validate(result)

    async def delete(self, data: "BusinessDeleteRequest") -> None:
        existing = await self.repository.get(Business, data.id)
        if not existing:
            raise NotFoundError("Business")

        existing.status = BusinessStatus.SUSPENDED
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> BusinessResponse:  # noqa
        result = await self.repository.get(Business, id)
        if not result:
            raise NotFoundError("Business")

        return BusinessResponse.model_validate(result)

    async def get_all(self) -> BusinessListResponse:
        result = await self.repository.get_all(Business)
        if not result:
            raise NotFoundError("Businesses")

        return BusinessListResponse(businesses=[BusinessResponse.model_validate(business) for business in result])

    async def get_by_email(self, data: "BusinessGetByEmailRequest") -> BusinessResponse:
        result = await self.repository.get_by_email(str(data.email))
        if not result:
            raise NotFoundError("Business")

        return BusinessResponse.model_validate(result)
