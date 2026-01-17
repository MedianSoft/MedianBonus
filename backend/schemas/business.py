import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.business import Status


class BusinessCreateRequest(BaseModel):
    email: EmailStr
    name: str
    password_hash: str


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
    status: Status

    class Config:
        from_attributes = True


class BusinessListResponse(BaseModel):
    businesses: list[BusinessResponse]
