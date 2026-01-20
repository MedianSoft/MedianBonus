import uuid

from pydantic import BaseModel

from backend.schemas.base import BaseRequest


class CustomerCreateRequest(BaseRequest):
    phone: str
    name: str | None


class CustomerDeleteRequest(BaseRequest):
    id: uuid.UUID


class CustomerGetByPhoneRequest(BaseRequest):
    phone: str


class CustomerGetByIDRequest(BaseRequest):
    id: uuid.UUID


class CustomerResponse(BaseModel):
    id: uuid.UUID
    phone: str
    name: str | None


class CustomerListResponse(BaseModel):
    customers: list[CustomerResponse]
