from fastapi import Depends
from pydantic import EmailStr

from app.domain.business import Business, BusinessRepository
from app.factories.business import get_business_repository
from app.schemas.business import BusinessCreate
from app.security import hash_password


class BusinessService:
    def __init__(self, repo: BusinessRepository = Depends(get_business_repository)):
        self.repo = repo

    async def get_by_email(
        self,
        email: EmailStr,
    ) -> Business | None:
        return await self.repo.get_by_email(email)

    async def register(
        self,
        data: BusinessCreate,
    ) -> Business:
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")

        account = Business(
            email=data.email,
            password_hash=hash_password(data.password),
        )
        return await self.repo.add(account)
