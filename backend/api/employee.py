from fastapi import APIRouter, Depends, status

from backend.factories.service import get_employee_service
from backend.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeDeleteRequest,
    EmployeeGetByEmailRequest,
    EmployeeGetByIDRequest,
    EmployeeListResponse,
    EmployeeResponse,
)
from backend.services.employee import EmployeeService

router = APIRouter(prefix="/employee", tags=["employee"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


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


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def delete(
    data: EmployeeDeleteRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.delete(data)


@router.post(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def get(
    data: EmployeeGetByEmailRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.get(data)


@router.post(
    "/get_by_id",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def get_by_id(
    data: EmployeeGetByIDRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.get_by_id(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeListResponse,
)
async def get_all(
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeListResponse:
    return await service.get_all()
