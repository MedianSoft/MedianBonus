import uuid

from pydantic import BaseModel


class CustomerCreateRequest(BaseModel):
    phone: str
    name: str | None

    class Config:
        from_attributes = True


class CustomerGetByPhoneRequest(BaseModel):
    phone: str


class CustomerResponse(BaseModel):
    id: uuid.UUID
    phone: str
    name: str | None

    class Config:
        from_attributes = True


class CustomerListResponse(BaseModel):
    customers: list[CustomerResponse]
