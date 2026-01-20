from fastapi import APIRouter, Depends, status

from backend.factories.service import get_customer_service
from backend.schemas.customer import (
    CustomerCreateRequest,
    CustomerDeleteRequest,
    CustomerGetByIDRequest,
    CustomerGetByPhoneRequest,
    CustomerListResponse,
    CustomerResponse,
)
from backend.services.customer import CustomerService

router = APIRouter(prefix="/customer", tags=["customer"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=CustomerResponse,
)
async def create(
    data: CustomerCreateRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    return await service.create(data)


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def delete(
    data: CustomerDeleteRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse | None:
    return await service.delete(data)


@router.post(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def get(
    data: CustomerGetByPhoneRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    return await service.get(data)


@router.post(
    "/get_by_id",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def get_by_id(
    data: CustomerGetByIDRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse | None:
    return await service.get_by_id(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=CustomerListResponse,
)
async def get_all(
    service: CustomerService = Depends(get_customer_service),
) -> CustomerListResponse:
    return await service.get_all()
