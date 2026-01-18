from fastapi import Depends

from backend.domain.business import BusinessRepository
from backend.services.business import BusinessService

from .repository import get_business_repository


def get_business_service(
    repository: BusinessRepository = Depends(get_business_repository),
) -> BusinessService:
    return BusinessService(repository)
