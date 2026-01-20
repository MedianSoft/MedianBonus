import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.employee import EmployeeStatus
from backend.schemas.base import BaseRequest


class EmployeeCreateRequest(BaseRequest):
    email: EmailStr
    name: str
    password: str
    business_id: uuid.UUID


class EmployeeDeleteRequest(BaseRequest):
    id: uuid.UUID


class EmployeeGetByEmailRequest(BaseRequest):
    email: EmailStr


class EmployeeGetByIDRequest(BaseRequest):
    id: uuid.UUID


class EmployeeResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: EmployeeStatus


class EmployeeListResponse(BaseModel):
    employeees: list[EmployeeResponse]
