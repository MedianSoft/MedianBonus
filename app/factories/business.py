from app.domain.business import BusinessRepository
from app.services.business import BusinessService


async def get_business_repository() -> BusinessRepository:
    return BusinessRepository()


async def get_business_service() -> BusinessService:
    return BusinessService()
