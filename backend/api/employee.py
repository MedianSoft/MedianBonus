import uuid

from fastapi import APIRouter, Depends, status

from backend.factories.service import get_employee_service
from backend.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeDeleteRequest,
    EmployeeGetByEmailRequest,
    EmployeeListResponse,
    EmployeeResponse,
    EmployeeUpdateRequest,
)
from backend.services.employee import EmployeeService

router = APIRouter(prefix="/employee", tags=["employee"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=EmployeeResponse,
)
async def create(
    data: EmployeeCreateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=EmployeeResponse,
)
async def update(
    data: EmployeeUpdateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    data: EmployeeDeleteRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeListResponse,
)
async def get_all(
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeListResponse:
    return await service.get_all()


@router.post(
    "/get_by_email",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def get_by_email(
    data: EmployeeGetByEmailRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.get_by_email(data)
