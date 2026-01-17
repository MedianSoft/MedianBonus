from fastapi import APIRouter, Depends, status

from backend.factories.customer import get_customer_service
from backend.schemas.customer import (
    CustomerCreateRequest,
    CustomerGetByPhoneRequest,
    CustomerListResponse,
    CustomerResponse,
)
from backend.services.customer import CustomerService


router = APIRouter(prefix="/customer", tags=["customer"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=CustomerResponse,
)
async def register(
    data: CustomerCreateRequest,
    service: CustomerService = Depends(get_customer_service),
):
    return await service.create(data)


@router.post(
    "/get_by_phone",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def get_by_phone(
    data: CustomerGetByPhoneRequest,
    service: CustomerService = Depends(get_customer_service),
):
    return await service.get_by_phone(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=CustomerListResponse,
)
async def get_all(
    service: CustomerService = Depends(get_customer_service),
):
    return await service.get_all()
