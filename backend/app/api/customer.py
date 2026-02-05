import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
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
@inject
async def create(
    data: CustomerCreateRequest,
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> CustomerResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CustomerResponse,
)
@inject
async def update(
    data: CustomerUpdateRequest,
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> CustomerResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: CustomerDeleteRequest,
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> CustomerResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CustomerListResponse,
)
@inject
async def get_all(
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> CustomerListResponse:
    return await service.get_all()


@router.post(
    "/get_by_phone",
    status_code=status.HTTP_200_OK,
    response_model=CustomerResponse,
)
@inject
async def get_by_phone(
    data: CustomerGetByPhoneRequest,
    service: CustomerService = Depends(Provide[BaseContainer.customer.service]),  # type: ignore
) -> CustomerResponse:
    return await service.get_by_phone(data)
