import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.business import BusinessStatus


class BusinessCreateRequest(BaseModel):
    email: EmailStr
    name: str
    password: str

    class Config:
        from_attributes = True


class BusinessDeleteRequest(BaseModel):
    email: EmailStr


class BusinessGetByEmailRequest(BaseModel):
    email: EmailStr


class BusinessGetByIDRequest(BaseModel):
    id: uuid.UUID


class BusinessResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: BusinessStatus

    class Config:
        from_attributes = True


class BusinessListResponse(BaseModel):
    businesses: list[BusinessResponse]
