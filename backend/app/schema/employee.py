import uuid

from pydantic import EmailStr

from app.domain.employee import EmployeeStatus
from app.schema.base import BaseRequest, BaseResponse


class EmployeeCreateRequest(BaseRequest):
    email: EmailStr
    name: str
    password: str
    business_id: uuid.UUID


class EmployeeUpdateRequest(BaseRequest):
    id: uuid.UUID
    email: EmailStr | None
    name: str | None
    password: str | None


class EmployeeDeleteRequest(BaseRequest):
    id: uuid.UUID


class EmployeeGetByEmailRequest(BaseRequest):
    email: EmailStr


class EmployeeResponse(BaseResponse):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: EmployeeStatus


class EmployeeListResponse(BaseResponse):
    employeees: list[EmployeeResponse]
