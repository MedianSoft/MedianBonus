from fastapi import APIRouter, Depends, status

from app.factories.business import get_business_service
from app.schemas.business import BusinessCreate, BusinessRead
from app.services.business import BusinessService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=BusinessRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_business_account(
    data: BusinessCreate,
    service: BusinessService = Depends(get_business_service),
):
    return await service.register(data)
