import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.employee import (
    EmployeeCreateRequest,
    EmployeeDeleteRequest,
    EmployeeGetByEmailRequest,
    EmployeeListResponse,
    EmployeeResponse,
    EmployeeUpdateRequest,
)
from app.service.employee import EmployeeService

router = APIRouter(prefix="/employee", tags=["employee"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=EmployeeResponse,
)
@inject
async def create(
    data: EmployeeCreateRequest,
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> EmployeeResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=EmployeeResponse,
)
@inject
async def update(
    data: EmployeeUpdateRequest,
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> EmployeeResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: EmployeeDeleteRequest,
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> EmployeeResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeListResponse,
)
@inject
async def get_all(
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> EmployeeListResponse:
    return await service.get_all()


@router.post(
    "/get_by_email",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
@inject
async def get_by_email(
    data: EmployeeGetByEmailRequest,
    service: EmployeeService = Depends(Provide[BaseContainer.employee.service]),  # type: ignore
) -> EmployeeResponse | None:
    return await service.get_by_email(data)
