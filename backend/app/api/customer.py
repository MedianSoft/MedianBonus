import uuid

from fastapi import APIRouter, Depends, status

from app.factoriy.service import get_customer_service
from app.schema.customer import (
    CustomerCreateRequest,
    CustomerDeleteRequest,
    CustomerGetByPhoneRequest,
    CustomerListResponse,
    CustomerResponse,
    CustomerUpdateRequest,
)
from app.service.customer import CustomerService

router = APIRouter(prefix="/customer", tags=["customer"])


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


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CustomerResponse,
)
async def update(
    data: CustomerUpdateRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    data: CustomerDeleteRequest,
    service: CustomerService = Depends(get_customer_service),
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CustomerListResponse,
)
async def get_all(
    service: CustomerService = Depends(get_customer_service),
) -> CustomerListResponse:
    return await service.get_all()


@router.post(
    "/get_by_phone",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
async def get_by_phone(
    data: CustomerGetByPhoneRequest,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    return await service.get_by_phone(data)
