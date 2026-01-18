from fastapi import APIRouter, Depends, status

from backend.factories.employee import get_employee_service
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
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=EmployeeResponse,
)
async def register(
    data: EmployeeCreateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    return await service.create(data)


# TODO: Should suspend by id?
@router.post(
    "/suspend",
    status_code=status.HTTP_200_OK,
    response_model=EmployeeResponse,
)
async def suspend(
    data: EmployeeDeleteRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse | None:
    return await service.delete(data)


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
