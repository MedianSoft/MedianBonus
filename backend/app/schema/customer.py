import uuid

from app.schema.base import BaseRequest, BaseResponse


class CustomerCreateRequest(BaseRequest):
    phone: str
    name: str | None


class CustomerUpdateRequest(BaseRequest):
    id: uuid.UUID
    phone: str | None
    name: str | None


class CustomerDeleteRequest(BaseRequest):
    id: uuid.UUID


class CustomerGetByPhoneRequest(BaseRequest):
    phone: str


class CustomerResponse(BaseResponse):
    id: uuid.UUID
    phone: str
    name: str | None


class CustomerListResponse(BaseResponse):
    customers: list[CustomerResponse]
