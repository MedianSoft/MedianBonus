from fastapi import APIRouter, Depends, status

from backend.factories.business import get_business_service
from backend.schemas.business import BusinessCreate
from backend.services.business import BusinessService


router = APIRouter(tags=["business"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
async def register_business(
    data: BusinessCreate,
    service: BusinessService = Depends(get_business_service),
):
    return await service.create(data)
